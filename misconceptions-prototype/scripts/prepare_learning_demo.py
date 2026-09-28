"""Create a separate, explicitly synthetic classroom for course demonstrations."""

import argparse
import json
import time
from pathlib import Path

from misconceptions.learning_sandbox import DockerSandbox
from misconceptions.learning_service import LearningService

ROOT = Path(__file__).resolve().parents[2]
DEMO_DIR = ROOT / '.cache/course-demo'
PASSWORD = 'Demo-AAI-2026!'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    # Never seed the normal learning-app database or overwrite an existing demo.
    if DEMO_DIR.exists():
        raise SystemExit('Demo directory already exists; data was not changed.')
    sandbox = DockerSandbox()
    health = sandbox.health()
    if not health['ready']:
        raise SystemExit(health['message'])
    service = LearningService(DEMO_DIR, sandbox=sandbox)
    try:
        service.store.register('demo_teacher', 'Giảng viên DEMO', PASSWORD, 'teacher')
        service.store.register('demo_student', 'Học viên DEMO - tự thử', PASSWORD)
        attempts = []
        # Same authored expressions exercised by the real-browser acceptance suite.
        for number, expression in enumerate(['0', '1', '3', '15', '5050', 'n', 'n*n', 'n*(n-1)/2'], 1):
            user = service.store.register(f'demo_fixture_{number}', f'Mẫu DEMO {number}', PASSWORD)
            source = ('#include <stdio.h>\nint main(void){int n;scanf("%d",&n);'
                      'printf("%d\\n",' + expression + ');return 0;}\n')
            key = service.submit(user, {
                'problem_id': 'sum-range', 'source': source,
                'reflection': 'Chương trình minh họa tự viết; không phải dữ liệu sinh viên thật.',
            })['id']
            deadline = time.monotonic() + 120
            while time.monotonic() < deadline:
                attempt = service.store.attempt(key, user)
                if attempt['status'] not in ('queued', 'running'):
                    if attempt['status'] != 'completed':
                        raise RuntimeError(f'Demo execution failed: {attempt["status"]}')
                    if attempt['result']['verdict'] != 'needs_work':
                        raise RuntimeError('Expected an authored incorrect program')
                    attempts.append({'id': key, 'passed': attempt['result']['passed'],
                                     'total': attempt['result']['total']})
                    break
                time.sleep(.2)
            else:
                raise TimeoutError('Demo execution did not finish within 120 seconds')
            print(f'Executed authored demo {number}/8', flush=True)
        manifest = {
            'status': 'ready', 'purpose': 'synthetic_course_demo_not_research_or_real_class',
            'student': 'demo_student', 'teacher': 'demo_teacher',
            'authored_attempts': attempts, 'runner': health,
        }
        (DEMO_DIR / 'demo_manifest.json').write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
        print('Demo ready. Student: demo_student; teacher: demo_teacher', flush=True)
        print(f'Local demo password for both accounts: {PASSWORD}', flush=True)
    finally:
        service.executor.shutdown(wait=True)


if __name__ == '__main__':
    main()
