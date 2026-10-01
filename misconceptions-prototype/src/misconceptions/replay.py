"""Host side of the research replay runner: container pool, verdicts and oracle audit.

Student programs run only inside `aai-c-replay` containers (no network, read-only root,
unprivileged child uid, rlimits). The host keeps every oracle and decides verdicts from
raw stdout bytes, so a program cannot author its own result.
"""

import base64
import hashlib
import json
import queue
import subprocess
import threading
from concurrent.futures import Future, as_completed
from pathlib import Path

IMAGE = "aai-c-replay:1"
CPACK_FLAGS = ["-ansi", "-pedantic", "-Wall", "-Wextra"]  # Historical flags minus -Werror.
STORED_STDOUT = 65536
# Selected by scripts/replay_cpack.py on train-partition agreement with historical verdicts.
POLICY_DEFAULT = {"pass_relations": ("exact",), "exit_code_matters": True}
SIGXCPU = 24
SERVER = Path(__file__).resolve().parents[2] / "sandbox-replay" / "replay_server.py"


def docker_command(image_id):
    return ["docker", "run", "--rm", "-i", "--init", "--pull=never", "--network=none",
            "--read-only", "--cap-drop=ALL", "--cap-add=CHOWN", "--cap-add=SETUID",
            "--cap-add=SETGID", "--cap-add=KILL", "--security-opt=no-new-privileges",
            "--pids-limit=128", "--cpus=1", "--memory=1g", "--memory-swap=1g",
            "--log-driver=none", "--tmpfs", "/work:rw,exec,nosuid,size=256m,mode=1777",
            "--tmpfs", "/tmp:rw,exec,nosuid,size=256m,mode=1777", image_id,
            "python", "-I", "/opt/aai-replay/replay_server.py"]


def image_id(image=IMAGE):
    result = subprocess.run(["docker", "image", "inspect", image, "--format", "{{.Id}}"],
                            capture_output=True, text=True, timeout=30, check=False)
    value = result.stdout.strip()
    if result.returncode or not value.startswith("sha256:"):
        raise RuntimeError(f"Build the research image first: docker build -t {image} sandbox-replay")
    return value


class _Worker:
    def __init__(self, image):
        self.image = image
        self.process = None

    def _start(self):
        self.process = subprocess.Popen(docker_command(self.image), stdin=subprocess.PIPE,
                                        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

    def call(self, request):
        if self.process is None or self.process.poll() is not None:
            self._start()
        try:
            self.process.stdin.write((json.dumps(request) + "\n").encode("utf-8"))
            self.process.stdin.flush()
            line = self.process.stdout.readline()
        except (BrokenPipeError, OSError):
            line = b""
        if not line:
            self.close()
            return {"id": request["id"], "infrastructure_error": "container_exited"}
        response = json.loads(line)
        if response.get("id") != request["id"]:
            self.close()
            return {"id": request["id"], "infrastructure_error": "response_id_mismatch"}
        return response

    def close(self):
        if self.process is not None:
            try:
                self.process.stdin.close()
            except OSError:
                pass
            try:
                self.process.wait(timeout=30)
            except subprocess.TimeoutExpired:
                self.process.kill()
            self.process = None


class ReplayPool:
    """Persistent container workers; `submit` returns a Future of the raw response."""

    def __init__(self, workers=4, image=None):
        self.image = image or image_id()
        self.tasks = queue.Queue()
        self.threads = [threading.Thread(target=self._loop, daemon=True)
                        for _ in range(max(1, workers))]
        for thread in self.threads:
            thread.start()

    def _loop(self):
        worker = _Worker(self.image)
        try:
            while (item := self.tasks.get()) is not None:
                request, future = item
                if not future.set_running_or_notify_cancel():
                    continue
                try:
                    response = worker.call(request)
                    if "infrastructure_error" in response:
                        response = worker.call(request)
                    future.set_result(response)
                except Exception as error:  # noqa: BLE001 - surfaced to the waiting caller.
                    future.set_exception(error)
        finally:
            worker.close()

    def submit(self, request):
        future = Future()
        self.tasks.put((request, future))
        return future

    def close(self):
        for _ in self.threads:
            self.tasks.put(None)
        for thread in self.threads:
            thread.join()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()


def run_requests(requests, workers=4, image=None, progress=None):
    """Yield responses in completion order; infrastructure failures retry once."""
    with ReplayPool(workers, image) as pool:
        futures = [pool.submit(request) for request in requests]
        for done, future in enumerate(as_completed(futures), 1):
            if progress and (done % 200 == 0 or done == len(futures)):
                progress(done, len(futures))
            yield future.result()


def relation(actual: bytes, expected: str) -> str:
    """Oracle relation on the host; `expected` uses the import's LF normalization."""
    try:
        text = actual.decode("utf-8")
    except UnicodeDecodeError:
        return "invalid_utf8"
    text = text.replace("\r\n", "\n")
    if text == expected:
        return "exact"
    if text.rstrip() == expected.rstrip():
        return "trailing_whitespace"
    if text.split() == expected.split():
        return "whitespace"
    return "different"


def stored_test(test, expected):
    raw = base64.b64decode(test["stdout_b64"])
    try:
        text, encoding = raw[:STORED_STDOUT].decode("utf-8").replace("\r\n", "\n"), "utf8"
    except UnicodeDecodeError:
        text, encoding = None, "invalid_utf8"
    return {"test_id": test["test_id"], "relation": relation(raw, expected),
            "exit_code": test["exit_code"], "signal": test["signal"], "timeout": test["timeout"],
            "output_truncated": test["output_truncated"], "elapsed_ms": test["elapsed_ms"],
            "stdout": text, "stdout_encoding": encoding, "stdout_bytes": len(raw),
            "stdout_stored_truncated": len(raw) > STORED_STDOUT,
            "stdout_sha256": hashlib.sha256(raw).hexdigest(),
            "stderr_tail": test.get("stderr_tail", "")[:512]}


def request_for(submission_id, source, tests, flags=CPACK_FLAGS):
    return {"id": submission_id, "source": source, "flags": list(flags),
            "tests": [{"id": tid, "input": definition["input"]} for tid, definition in tests.items()]}


def outcomes_from_record(record, tests, **policy):
    """Outcome dict for a stored replay record, or None when execution evidence is absent."""
    if "compile" not in record or record["compile"]["returncode"] != 0:
        return None  # Skipped, infrastructure failure or compile error: no execution evidence.
    by_id = {test["test_id"]: test for test in record["tests"]}
    if set(by_id) != set(tests):
        return None
    result = {}
    for tid in tests:
        test = by_id[tid]
        if test.get("timeout") or test.get("signal") == SIGXCPU:
            result[tid] = "timeout"
        elif (test.get("output_truncated") or test.get("signal") is not None
              or policy.get("exit_code_matters", True) and test.get("exit_code") != 0):
            result[tid] = "runtime_error"
        else:
            result[tid] = "pass" if test["relation"] in policy.get("pass_relations", ("exact",)) \
                else "fail"
    return result
