"""Build the local C runner; no learner code is executed during setup."""

import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[1]
subprocess.run(['docker', 'info', '--format', '{{.OSType}}'], timeout=15, check=True)
subprocess.run(['docker', 'build', '--tag', 'aai-c-runner:1', str(root / 'sandbox')], check=True)
print('Runner ready. Start: python -m misconceptions.learning_web')
