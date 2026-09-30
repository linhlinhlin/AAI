"""Research replay server: compile and run historical C programs inside one container.

Reads one JSON request per stdin line and writes one JSON response per stdout line.
The server keeps no oracle: it returns raw stdout bytes, and the host decides verdicts.
Student code never runs as the server user; it runs as an unprivileged, per-container
uid with rlimits, its own session and a scratch directory that is removed afterwards.
"""

import base64
import json
import os
import resource
import shutil
import signal
import subprocess
import sys
import threading
import time

CHILD_UID = 10001
WORK = "/work"
COMPILE_SECONDS = 20
RUN_WALL_SECONDS = 5
RUN_CPU_SECONDS = 3
OUTPUT_CAP = 2 * 1024 * 1024
STDERR_CAP = 8192
ALLOWED_FLAGS = {"-ansi", "-pedantic", "-Wall", "-Wextra", "-std=c89", "-std=c90", "-std=c99",
                 "-std=c11", "-std=c17"}
ENV = {"LANG": "C.UTF-8", "LC_ALL": "C.UTF-8", "PATH": "/usr/bin:/bin"}


def _limits(cpu, address_space):
    def apply():
        resource.setrlimit(resource.RLIMIT_CPU, (cpu, cpu + 1))
        resource.setrlimit(resource.RLIMIT_AS, (address_space, address_space))
        resource.setrlimit(resource.RLIMIT_NPROC, (64, 64))
        resource.setrlimit(resource.RLIMIT_FSIZE, (1 << 20, 1 << 20))
        resource.setrlimit(resource.RLIMIT_NOFILE, (64, 64))
        resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    return apply


def _kill_child_processes():
    """Remove every process of the child uid, including double-forked escapees."""
    for entry in os.listdir("/proc"):
        if not entry.isdigit():
            continue
        try:
            if os.stat(f"/proc/{entry}").st_uid == CHILD_UID:
                os.kill(int(entry), signal.SIGKILL)
        except (FileNotFoundError, ProcessLookupError, PermissionError):
            pass


def _run(args, cwd, stdin_bytes, wall, cpu, address_space, cap):
    started = time.monotonic()
    process = subprocess.Popen(
        args, cwd=cwd, env=ENV, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, user=CHILD_UID, group=CHILD_UID, extra_groups=[],
        process_group=0, preexec_fn=_limits(cpu, address_space), close_fds=True,
    )
    buffers = [bytearray(), bytearray()]
    caps = [cap, STDERR_CAP]
    truncated = threading.Event()

    def read(stream, index):
        while chunk := stream.read(65536):
            room = caps[index] - len(buffers[index])
            buffers[index].extend(chunk[:max(room, 0)])
            if len(chunk) > room and index == 0:
                truncated.set()
                break
        stream.close()

    def feed():
        try:
            process.stdin.write(stdin_bytes)
            process.stdin.close()
        except (BrokenPipeError, OSError):
            pass

    workers = [threading.Thread(target=read, args=(process.stdout, 0), daemon=True),
               threading.Thread(target=read, args=(process.stderr, 1), daemon=True),
               threading.Thread(target=feed, daemon=True)]
    for worker in workers:
        worker.start()
    timed_out = False
    while process.poll() is None:
        if truncated.is_set():
            break
        if time.monotonic() - started > wall:
            timed_out = True
            break
        time.sleep(0.005)
    if process.poll() is None:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
    process.wait()
    _kill_child_processes()
    for worker in workers:
        worker.join(timeout=2)
    code = process.returncode
    return {
        "stdout": bytes(buffers[0]), "stderr": bytes(buffers[1]),
        "exit_code": code if code is not None and code >= 0 else None,
        "signal": -code if code is not None and code < 0 else None,
        "timeout": timed_out, "output_truncated": truncated.is_set(),
        "elapsed_ms": round((time.monotonic() - started) * 1000),
    }


def handle(request, index):
    directory = os.path.join(WORK, f"r{index}")
    os.mkdir(directory)
    # Search-only for the server: Popen changes directory before it drops privileges.
    os.chmod(directory, 0o711)
    os.chown(directory, CHILD_UID, CHILD_UID)
    try:
        source = request["source"].encode("utf-8")
        path = os.path.join(directory, "main.c")
        # Write as the child uid so the server never follows child-controlled paths.
        subprocess.run(["/bin/sh", "-c", 'cat > "$1"', "sh", path], input=source, check=True,
                       user=CHILD_UID, group=CHILD_UID, extra_groups=[], env=ENV)
        flags = [flag for flag in request["flags"] if flag in ALLOWED_FLAGS]
        compiled = _run(["gcc", *flags, "-O0", "-fdiagnostics-color=never", "main.c", "-lm",
                         "-o", "program"], directory, b"", COMPILE_SECONDS, COMPILE_SECONDS,
                        1 << 30, 1 << 16)
        diagnostics = compiled["stderr"].decode("utf-8", errors="replace")
        result = {"id": request["id"], "compile": {
            "returncode": compiled["exit_code"], "signal": compiled["signal"],
            "timeout": compiled["timeout"], "diagnostics": diagnostics[:STDERR_CAP],
            "warning_free": compiled["exit_code"] == 0 and "warning:" not in diagnostics}}
        if compiled["exit_code"] != 0 or not os.path.exists(os.path.join(directory, "program")):
            result["tests"] = []
            return result
        tests = []
        for test in request["tests"]:
            run = _run(["./program"], directory, test["input"].encode("utf-8"),
                       RUN_WALL_SECONDS, RUN_CPU_SECONDS, 512 << 20, OUTPUT_CAP)
            tests.append({"test_id": test["id"], "stdout_b64": base64.b64encode(run["stdout"]).decode(),
                          "stderr_tail": run["stderr"][-1024:].decode("utf-8", errors="replace"),
                          "exit_code": run["exit_code"], "signal": run["signal"],
                          "timeout": run["timeout"], "output_truncated": run["output_truncated"],
                          "elapsed_ms": run["elapsed_ms"]})
        result["tests"] = tests
        return result
    finally:
        _kill_child_processes()
        subprocess.run(["rm", "-rf", "--one-file-system", directory], check=False,
                       user=CHILD_UID, group=CHILD_UID, extra_groups=[], env=ENV)
        shutil.rmtree(directory, ignore_errors=True)


def main():
    index = 0
    for line in sys.stdin:
        if not line.strip():
            continue
        index += 1
        request = json.loads(line)
        try:
            response = handle(request, index)
        except Exception as error:  # Report infrastructure failures; never invent a verdict.
            response = {"id": request.get("id"), "infrastructure_error": repr(error)[:500]}
        sys.stdout.write(json.dumps(response) + "\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
