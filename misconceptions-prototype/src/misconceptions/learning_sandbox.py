"""Bounded Docker execution. Never fall back to executing C on the host."""

import base64
import hashlib
import shutil
import struct
import subprocess
import threading
import time
import uuid

IMAGE = 'aai-c-runner:1'
OUTPUT_LIMIT = 65536


class SandboxUnavailable(RuntimeError):
    pass


class DockerSandbox:
    def __init__(self, image=IMAGE):
        self.image = image
        self.image_id = None

    def health(self):
        if not shutil.which('docker'):
            return {'ready': False, 'message': 'Cần cài Docker để chạy bài C.'}
        try:
            result = subprocess.run(
                ['docker', 'image', 'inspect', self.image, '--format', '{{.Id}}'],
                capture_output=True, timeout=8, check=False,
            )
            image_id = result.stdout.decode().strip()
            if result.returncode or not image_id.startswith('sha256:'):
                return {'ready': False,
                        'message': 'Mở Docker và chạy lệnh tạo môi trường trong hướng dẫn cài đặt.'}
            self.image_id = image_id
            return {'ready': True, 'message': 'Sẵn sàng chạy C17', 'image_id': image_id}
        except (OSError, subprocess.TimeoutExpired):
            return {'ready': False, 'message': 'Chưa kết nối được môi trường chạy code.'}

    def _command(self, name, script, compile_mode=False):
        return ['docker', 'run', '--rm', '--init', '--pull=never', '--name', name, '-i',
                '--network=none', '--read-only', '--cap-drop=ALL',
                '--security-opt=no-new-privileges', '--user=65534:65534',
                '--pids-limit=32', '--cpus=1', '--memory=256m', '--memory-swap=256m',
                '--ulimit', 'nofile=64:64', '--ulimit', 'core=0:0',
                '--ulimit', 'fsize=8388608:8388608', '--ulimit',
                'cpu=10:12' if compile_mode else 'cpu=2:3', '--log-driver=none',
                '--tmpfs', '/work:rw,exec,nosuid,size=32m,mode=1777',
                '--tmpfs', '/tmp:rw,noexec,nosuid,size=16m,mode=1777',
                self.image_id, 'python', '-I', '/opt/aai/' + script]

    def _run(self, payload, *, compile_mode=False):
        name = 'aai-' + uuid.uuid4().hex
        args = self._command(name, 'compile.py' if compile_mode else 'execute.py', compile_mode)
        limits = [4 * 1024 * 1024 if compile_mode else OUTPUT_LIMIT, OUTPUT_LIMIT]
        buffers = [bytearray(), bytearray()]
        overflow = threading.Event()
        started = time.monotonic()
        process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)

        def read(stream, index):
            while chunk := stream.read(4096):
                remaining = limits[index] - len(buffers[index])
                buffers[index].extend(chunk[:remaining])
                if len(chunk) > remaining:
                    overflow.set()
                    break
            stream.close()

        def feed():
            try:
                process.stdin.write(payload)
                process.stdin.flush()
            except (BrokenPipeError, OSError):
                pass
            finally:
                process.stdin.close()

        workers = [threading.Thread(target=read, args=(process.stdout, 0), daemon=True),
                   threading.Thread(target=read, args=(process.stderr, 1), daemon=True),
                   threading.Thread(target=feed, daemon=True)]
        for worker in workers:
            worker.start()
        reason = None
        deadline = started + (20 if compile_mode else 5)
        try:
            while process.poll() is None:
                if overflow.is_set() or time.monotonic() > deadline:
                    reason = 'output_limit' if overflow.is_set() else 'timeout'
                    break
                time.sleep(.02)
        finally:
            if reason:
                # Unique container name is owned by this invocation; never prune shared containers.
                try:
                    subprocess.run(['docker', 'rm', '-f', name], capture_output=True,
                                   timeout=10, check=False)
                finally:
                    process.kill()
            process.wait(timeout=10)
            for worker in workers:
                worker.join(timeout=2)
        if overflow.is_set():
            reason = 'output_limit'
        return {'returncode': process.returncode, 'stdout': bytes(buffers[0]),
                'stderr': bytes(buffers[1]), 'limit': reason,
                'elapsed_ms': round((time.monotonic() - started) * 1000)}

    def evaluate(self, source, tests, progress=lambda _message: None):
        if not self.health()['ready']:
            raise SandboxUnavailable('Môi trường chạy chưa sẵn sàng. Bài chưa được chấm.')
        progress('Đang biên dịch C17…')
        compiled = self._run(source.encode('utf-8'), compile_mode=True)
        if compiled['returncode'] in (125, 126, 127):
            raise SandboxUnavailable('Docker không thể khởi chạy bộ biên dịch.')
        diagnostic = compiled['stderr'].decode('utf-8', errors='replace')
        provenance = {'runner': 'docker-isolated-c17-v1', 'image_id': self.image_id,
                      'source_sha256': hashlib.sha256(source.encode()).hexdigest(),
                      'comparison': 'whitespace_separated_tokens', 'network': 'none',
                      'memory_bytes': 268435456, 'cpu_seconds_per_test': 2,
                      'wall_seconds_per_test_including_container_start': 5,
                      'output_bytes_per_stream': OUTPUT_LIMIT}
        if compiled['returncode'] or compiled['limit']:
            return {'verdict': 'compile_error', 'diagnostics': diagnostic,
                    'compile_limit': compiled['limit'], 'tests': [], 'passed': 0,
                    'total': len(tests), 'provenance': provenance}
        executable = compiled['stdout']
        if not executable.startswith(b'\x7fELF'):
            raise SandboxUnavailable('Bộ biên dịch không trả về chương trình hợp lệ.')
        provenance['executable_sha256'] = hashlib.sha256(executable).hexdigest()
        observations = []
        for index, test in enumerate(tests, 1):
            progress(f'Đang kiểm tra {index}/{len(tests)}…')
            payload = struct.pack('!I', len(executable)) + executable + test['input'].encode()
            run = self._run(payload)
            invalid_encoding = False
            try:
                output = run['stdout'].decode('utf-8')
            except UnicodeDecodeError:
                invalid_encoding = True
                output = '(Output không phải UTF-8; byte gốc được giữ trong báo cáo.)'
            if run['returncode'] == 125 and b'docker:' in run['stderr'].lower():
                raise SandboxUnavailable('Docker gặp lỗi trong khi chạy test; không ghi thành lỗi bài.')
            if run['limit'] == 'timeout' or run['returncode'] == 152:
                outcome = 'timeout'
            elif run['returncode'] or run['limit'] or invalid_encoding:
                outcome = 'runtime_error'
            else:
                outcome = 'pass' if run['stdout'].split() == test['expected'].encode().split() else 'fail'
            observations.append(test | {'output': output, 'outcome': outcome,
                                       'stderr': run['stderr'].decode('utf-8', errors='replace'),
                                       'exit_code': run['returncode'], 'limit': run['limit'],
                                       'elapsed_ms': run['elapsed_ms'],
                                       'output_encoding': 'invalid_utf8' if invalid_encoding else 'utf8',
                                       'output_bytes_base64': base64.b64encode(run['stdout']).decode()
                                       if invalid_encoding else None,
                                       'stdout_sha256': hashlib.sha256(run['stdout']).hexdigest()})
        passed = sum(t['outcome'] == 'pass' for t in observations)
        return {'verdict': 'accepted' if passed == len(tests) else 'needs_work',
                'diagnostics': diagnostic, 'tests': observations, 'passed': passed,
                'total': len(tests), 'provenance': provenance}
