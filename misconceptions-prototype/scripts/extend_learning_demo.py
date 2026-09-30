"""Append authored fixtures to the existing synthetic demo through its live Docker API."""

import argparse
import hashlib
import json
import sqlite3
import time
from datetime import UTC, datetime
from http.cookiejar import CookieJar
from pathlib import Path
from urllib.request import HTTPCookieProcessor, Request, build_opener

from misconceptions.learning_problems import get_problem
from misconceptions.research_io import write_json

ROOT = Path(__file__).resolve().parents[2]
DEMO = ROOT / '.cache/course-demo'
PASSWORD = 'Demo-AAI-2026!'
PURPOSE = 'synthetic_course_demo_not_research_or_real_class'
PROBLEMS = ('max-array', 'count-positive', 'swap', 'circle-position')


def fixtures():
    """Expected counts are authored assertions, never injected into actual grading results."""
    cases = []
    for number in range(1, 11):
        variant = (number - 1) % 4
        group = 'first_error' if number <= 4 else 'second_error' if number <= 8 else 'correct'
        for problem in PROBLEMS:
            prefix = '#include <stdio.h>\n'
            if problem in ('max-array', 'count-positive'):
                start = ('int main(void) {\n int n, a[100];\n scanf("%d", &n);\n'
                         ' for (int p=0;p<n;p++) scanf("%d", &a[p]);\n')
                if problem == 'max-array':
                    init = '0' if group == 'first_error' else 'a[0]'
                    end = 'n-1' if group == 'second_error' else 'n'
                    body = 'if (a[i] > answer) answer = a[i];'
                    count = 4 if group == 'first_error' else 5 if group == 'second_error' else 6
                    intent = {'first_error': 'Khởi tạo max bằng 0',
                              'second_error': 'Bỏ phần tử cuối khi tìm max',
                              'correct': 'Tìm max từ dữ liệu, duyệt đủ'}[group]
                else:
                    init = '0'
                    end = 'n-1' if group == 'second_error' else 'n'
                    op = '>=' if group == 'first_error' else '>'
                    body = f'if (a[i] {op} 0) answer += 1;'
                    count = 3 if group == 'first_error' else 2 if group == 'second_error' else 6
                    intent = {'first_error': 'Đếm cả số 0 là số dương',
                              'second_error': 'Bỏ phần tử cuối khi đếm',
                              'correct': 'Đếm đủ các phần tử lớn hơn 0'}[group]
                loops = [f'for (int i=0;i<{end};i++) {{ {body} }}',
                         f'int i=0; while (i<{end}) {{ {body} i++; }}',
                         f'for (int i=({end})-1;i>=0;i--) {{ {body} }}',
                         f'int i=0; if ({end}>0) do {{ {body} ++i; }} while (i<{end});']
                source = prefix + start + f' int answer={init};\n ' + loops[variant] + (
                    '\n printf("%d\\n",answer);\n return 0;\n}\n')
            elif problem == 'swap':
                if group == 'first_error':
                    functions = [
                        'void exchange(int a,int b){int t=a;a=b;b=t;}',
                        'void exchange(int a,int b){int copy=b;b=a;a=copy;}',
                        'void exchange(int a,int b){if(a!=b){int old=a;a=b;b=old;}}',
                        'void exchange(int a,int b){int values[2]={a,b};a=values[1];b=values[0];}',
                    ]
                    call = 'exchange(a,b);'
                    intent = 'Hoán vị bản sao tham số, không sửa biến ở main'
                elif group == 'second_error':
                    functions = [
                        'void exchange(int *a,int *b){*a=*b;*b=*a;}',
                        'void exchange(int *a,int *b){int temp=*b;*a=temp;*b=*a;}',
                        'void exchange(int *a,int *b){if(*a!=*b){*a=*b;*b=*a;}}',
                        'void exchange(int *a,int *b){int *left=a;int *right=b;*left=*right;*right=*left;}',
                    ]
                    call = 'exchange(&a,&b);'
                    intent = 'Ghi đè mất giá trị ban đầu khi hoán vị'
                else:
                    functions = ['void exchange(int *a,int *b){int t=*a;*a=*b;*b=t;}',
                                 'void exchange(int *a,int *b){if(a!=b){int saved=*b;*b=*a;*a=saved;}}']
                    call = 'exchange(&a,&b);'
                    intent = 'Hoán vị giá trị được trỏ tới bằng biến tạm'
                source = (prefix + functions[variant] + '\nint main(void){\n int a,b;\n'
                          ' scanf("%d %d",&a,&b);\n ' + call +
                          '\n printf("%d %d\\n",a,b);\n return 0;\n}\n')
                count = 6 if group == 'correct' else 1
            else:
                start = ('int main(void){\n int x,y,r;\n scanf("%d %d %d",&x,&y,&r);\n')
                distance = ['x*x+y*y', '(x*x)+(y*y)', 'y*y+x*x', 'x*x + y*y'][variant]
                radius = 'r' if group == 'first_error' else 'r*r'
                middle = 'if' if group == 'second_error' else 'else if'
                source = (prefix + start + f' int distance={distance};\n int limit={radius};\n'
                          ' if(distance<limit) puts("INSIDE");\n '
                          + middle + '(distance>limit) puts("OUTSIDE");\n'
                          ' else puts("ON");\n return 0;\n}\n')
                count = 3 if group == 'first_error' else 4 if group == 'second_error' else 6
                intent = {'first_error': 'So sánh khoảng cách bình phương với r thay vì r*r',
                          'second_error': 'Else gắn if thứ hai, in hai kết luận khi ở trong',
                          'correct': 'So sánh hai bình phương, ba nhánh loại trừ'}[group]
            cases.append({'number': number, 'problem_id': problem, 'source': source,
                          'authored_intent_not_gold': intent, 'expected_passed': count})
    return cases


class Client:
    def __init__(self, base):
        self.base = base
        self.opener = build_opener(HTTPCookieProcessor(CookieJar()))
        self.csrf = ''

    def request(self, path, payload=None):
        headers = {'Origin': self.base}
        data = None
        if payload is not None:
            data = json.dumps(payload).encode()
            headers.update({'Content-Type': 'application/json', 'X-CSRF-Token': self.csrf})
        with self.opener.open(Request(self.base + path, data=data, headers=headers), timeout=60) as response:
            value = json.load(response)
        if isinstance(value, dict) and value.get('csrf'):
            self.csrf = value['csrf']
        return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8767)
    args = parser.parse_args()
    marker = json.loads((DEMO / 'demo_manifest.json').read_text(encoding='utf-8'))
    if marker.get('purpose') != PURPOSE:
        raise SystemExit('Only the explicitly synthetic course-demo database is supported.')
    base = f'http://127.0.0.1:{args.port}'
    teacher = Client(base)
    user = teacher.request('/api/login', {'username': 'demo_teacher', 'password': PASSWORD})['user']
    with sqlite3.connect(DEMO / 'learning.sqlite3') as db:
        owner = db.execute("SELECT id FROM users WHERE username='demo_teacher'").fetchone()
        if not owner or owner[0] != user['id']:
            raise SystemExit('Server does not match the synthetic demo database.')
        if db.execute("SELECT count(*) FROM attempts WHERE status IN ('queued','running')").fetchone()[0]:
            raise SystemExit('Wait for existing attempts to finish before extending the demo.')
        stamp = datetime.now(UTC).strftime('%Y%m%dT%H%M%S%fZ')
        output = DEMO / ('extension-' + stamp)
        output.mkdir()
        with sqlite3.connect(output / 'before.sqlite3') as backup:
            db.backup(backup)
    health = teacher.request('/api/runner', {})
    if not health['ready']:
        raise SystemExit(health['message'])
    before = teacher.request('/api/teacher/overview')
    manifest = {'purpose': PURPOSE, 'status': 'running', 'runner': health,
                'before': before['problems'], 'attempts': [], 'reports': {}}
    write_json(output / 'manifest.json', manifest)
    try:
        cases = fixtures()
        for number in range(1, 11):
            client = Client(base)
            username = f'demo_more_{number:02d}'
            name = f'DEMO bổ sung {number:02d} (tự viết)'
            with sqlite3.connect(DEMO / 'learning.sqlite3') as db:
                existing = db.execute('SELECT name FROM users WHERE username=?', (username,)).fetchone()
            if existing:
                if existing[0] != name:
                    raise ValueError('Fixture username conflicts with a different account')
                client.request('/api/login', {'username': username, 'password': PASSWORD})
            else:
                client.request('/api/register', {'username': username, 'name': name, 'password': PASSWORD})
            for case in (c for c in cases if c['number'] == number):
                problem = get_problem(case['problem_id'])
                history = client.request('/api/history')['attempts']
                previous = next((a for a in history if a['problem_id'] == problem['id']), None)
                attempt = None
                if previous:
                    existing_attempt = client.request('/api/attempt?id=' + previous['id'])
                    if (existing_attempt['source'] == case['source'] and
                            existing_attempt['suite_version'] == problem['suite_version'] and
                            existing_attempt['status'] == 'completed'):
                        attempt = existing_attempt
                if attempt is None:
                    key = client.request('/api/submit', {'problem_id': problem['id'],
                        'source': case['source'],
                        'reflection': 'DEMO tự viết; không phải bài sinh viên thật hoặc nhãn gold.'})['id']
                    deadline = time.monotonic() + 240
                    while time.monotonic() < deadline:
                        attempt = client.request('/api/attempt?id=' + key)
                        if attempt['status'] not in ('queued', 'running'):
                            break
                        time.sleep(.5)
                    else:
                        raise TimeoutError('Docker attempt did not finish within 240 seconds')
                if attempt['status'] != 'completed':
                    raise RuntimeError(f"Attempt infrastructure failure: {attempt['status']}")
                result = attempt['result']
                expected_verdict = 'accepted' if case['expected_passed'] == 6 else 'needs_work'
                if (result['verdict'] != expected_verdict or result['passed'] != case['expected_passed'] or
                        result['total'] != 6 or any(t['outcome'] not in ('pass', 'fail') for t in result['tests'])):
                    raise RuntimeError(f"Unexpected fixture result: {problem['id']} {number}: "
                                       f"{result['verdict']} {result['passed']}/6")
                manifest['attempts'].append({**case, 'username': username, 'attempt_id': attempt['id'],
                    'passed': result['passed'], 'total': result['total'],
                    'source_sha256': hashlib.sha256(case['source'].encode()).hexdigest(),
                    'suite_sha256': problem['suite_sha256'], 'provenance': result['provenance']})
                write_json(output / 'manifest.json', manifest)
                print(f"{len(manifest['attempts'])}/40 {problem['id']} DEMO {number:02d}: "
                      f"{result['passed']}/6", flush=True)
        for problem in PROBLEMS:
            value = teacher.request('/api/teacher/analyze', {'problem_id': problem, 'k': 2})
            report = value['report']
            if report['status'] != 'ok' or report['n_clusters'] != 2:
                raise RuntimeError(f'Clustering abstained for {problem}; inspect evidence before retrying')
            write_json(output / f'{problem}.report.json', value)
            manifest['reports'][problem] = {'id': value['id'], 'status': report['status'],
                                            'n_clusters': report['n_clusters']}
        manifest['after'] = teacher.request('/api/teacher/overview')['problems']
        manifest['status'] = 'ready'
    except Exception:
        manifest['status'] = 'incomplete_inspect_before_retry'
        raise
    finally:
        write_json(output / 'manifest.json', manifest)
    print(f'Completed. Audit and backup: {output}', flush=True)


if __name__ == '__main__':
    main()
