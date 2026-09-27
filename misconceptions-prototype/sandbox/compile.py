"""Trusted compiler entrypoint; receives only source, never application files."""
import pathlib
import subprocess
import sys

source = sys.stdin.buffer.read(65537)
if len(source) > 65536:
    raise SystemExit(2)
pathlib.Path('/work/main.c').write_bytes(source)
result = subprocess.run(
    ['gcc', '-std=c17', '-O0', '-Wall', '-Wextra', '-fdiagnostics-color=never',
     '/work/main.c', '-lm', '-o', '/work/program'], check=False,
    stdout=sys.stderr, stderr=sys.stderr,
)
if result.returncode:
    raise SystemExit(1)
sys.stdout.buffer.write(pathlib.Path('/work/program').read_bytes())
