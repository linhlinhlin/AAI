"""Real-browser, real-Docker acceptance on isolated, explicitly authored fixtures."""

import argparse
import json
import threading
import time
from http.server import ThreadingHTTPServer
from pathlib import Path

from playwright.sync_api import expect, sync_playwright

from misconceptions.learning_problems import get_problem
from misconceptions.learning_service import LearningService
from misconceptions.learning_web import make_handler


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    service = LearningService(args.output / 'synthetic-app-data')
    if not service.health['ready']:
        raise RuntimeError(service.health['message'])
    # Deliberately authored programs; these accounts are never part of the research corpus.
    for number, expression in enumerate(['0', '1', '3', '15', '5050', 'n', 'n*n', 'n*(n-1)/2']):
        user = service.store.register(f'fixture_{number}', f'Kiểm thử {number + 1}',
                                      'fixture-password-only')
        source = '#include <stdio.h>\nint main(void){int n;scanf("%d",&n);printf("%d\\n",' + expression + ');return 0;}'
        key = service.submit(user, {'problem_id': 'sum-range', 'source': source})['id']
        deadline = time.monotonic() + 120
        while time.monotonic() < deadline:
            attempt = service.store.attempt(key, user)
            if attempt['status'] not in ('running', 'queued'):
                assert attempt['status'] == 'completed', attempt
                break
            time.sleep(.2)
        else:
            raise TimeoutError('Fixture execution did not finish')
        print(f'Authored classroom fixture {number + 1}/8 completed', flush=True)
    server = ThreadingHTTPServer(('127.0.0.1', 0), make_handler(service))
    worker = threading.Thread(target=server.serve_forever, daemon=True)
    worker.start()
    base = f'http://127.0.0.1:{server.server_address[1]}'
    errors = []
    try:
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=True)
            page = browser.new_page(viewport={'width': 1440, 'height': 1100}, device_scale_factor=1)
            page.on('pageerror', lambda error: errors.append(str(error)))
            page.goto(base + '/#setup=' + service.setup_token)
            page.wait_for_load_state('networkidle')
            expect(page.locator('#auth-title')).to_have_text('Thiết lập lớp học.')
            page.locator('#auth-name').fill('Giảng viên kiểm thử')
            page.locator('#auth-username').fill('fixture_teacher')
            page.locator('#auth-password').fill('fixture-password-only')
            page.locator('#auth-submit').click()
            expect(page.locator('#view-teacher')).to_be_visible()
            page.locator('#logout').click()
            expect(page.locator('#auth-view')).to_be_visible()
            page.screenshot(path=str(args.output / '01-welcome.png'), full_page=True)
            page.locator('#auth-toggle').click()
            page.locator('#auth-name').fill('Học viên kiểm thử')
            page.locator('#auth-username').fill('fixture_learner')
            page.locator('#auth-password').fill('fixture-password-only')
            page.locator('#auth-submit').click()
            expect(page.locator('#view-practice')).to_be_visible()
            page.locator('#source').fill(get_problem('sum-range')['starter'])
            page.locator('#reflection').fill('Chạy bản ban đầu để đọc bằng chứng.')
            page.locator('#submit-code').click()
            expect(page.locator('#run-status')).to_have_text('Đã chấm xong.', timeout=120000)
            expect(page.locator('.test-row')).to_have_count(6)
            expect(page.locator('.feedback')).to_contain_text('1/6 test đạt')
            page.screenshot(path=str(args.output / '02-student-evidence.png'), full_page=True)
            solutions = json.loads((Path(__file__).resolve().parents[1] /
                                    'tests/fixtures/learning_solutions.json').read_text())
            page.locator('#source').fill(solutions['sum-range'])
            page.locator('#reflection').fill('Cộng các số từ 1 đến n, có tính cả n.')
            page.locator('#submit-code').click()
            expect(page.locator('.feedback.success')).to_be_visible(timeout=120000)
            expect(page.locator('#solved-count')).to_have_text('1 / 6')
            page.locator('[data-view=progress]').click()
            expect(page.locator('#all-history tbody tr')).to_have_count(2)
            page.screenshot(path=str(args.output / '03-progress.png'), full_page=True)
            page.reload()
            expect(page.locator('#app-view')).to_be_visible()
            page.locator('#logout').click()
            page.locator('#auth-username').fill('fixture_teacher')
            page.locator('#auth-password').fill('fixture-password-only')
            page.locator('#auth-submit').click()
            expect(page.locator('#view-teacher')).to_be_visible()
            page.locator('[data-analyze=sum-range]').click()
            expect(page.locator('.cluster-card')).to_have_count(2, timeout=30000)
            assert page.locator('.rule').count() >= 2
            page.locator('.cluster-card [data-evidence]').first.click()
            expect(page.locator('#detail')).to_be_visible()
            expect(page.locator('#detail .oav-table tbody tr')).not_to_have_count(0)
            page.locator('#close-detail').click()
            form = page.locator('.review-form').first
            form.locator('[name=label]').fill('Nhận xét kiểm thử từ bằng chứng')
            form.locator('[name=rationale]').fill('Đã đối chiếu source và output của bài đại diện.')
            form.locator('[name=follow_up]').fill('Yêu cầu giải thích các giá trị cộng vào tổng.')
            form.locator('button[type=submit]').click()
            expect(form.locator('.review-status')).to_contain_text('Đã lưu')
            page.reload()
            expect(page.locator('[data-open-report]')).to_have_count(1)
            page.locator('[data-open-report]').click()
            expect(page.locator('.review-form').first.locator('[name=label]')).to_have_value(
                'Nhận xét kiểm thử từ bằng chứng')
            page.screenshot(path=str(args.output / '04-teacher-clusters.png'), full_page=True)
            page.locator('#logout').click()
            expect(page.locator('#auth-view')).to_be_visible()
            page.set_viewport_size({'width': 390, 'height': 844})
            page.reload()
            page.wait_for_load_state('networkidle')
            page.screenshot(path=str(args.output / '05-mobile.png'), full_page=True)
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
            page.locator('#auth-username').fill('fixture_learner')
            page.locator('#auth-password').fill('fixture-password-only')
            page.locator('#auth-submit').click()
            expect(page.locator('#view-practice')).to_be_visible()
            assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
            page.screenshot(path=str(args.output / '06-mobile-practice.png'), full_page=True)
            assert not errors, errors
            browser.close()
        report = {'status': 'passed', 'authored_classroom_accounts': 9,
                  'learner_revision': {'before': '1/6', 'after': '6/6'},
                  'teacher_clusters': 2, 'review_saved': True, 'review_reopened_after_reload': True,
                  'session_survived_reload': True, 'mobile_practice_no_overflow': True,
                  'browser_errors': errors, 'runner': service.health,
                  'scope': 'Software acceptance with authored fixtures; not a learning-effect study.'}
        (args.output / 'acceptance.json').write_text(json.dumps(report, ensure_ascii=False, indent=2),
                                                    encoding='utf-8')
        print(json.dumps(report, ensure_ascii=False), flush=True)
    finally:
        server.shutdown()
        server.server_close()
        service.executor.shutdown(wait=True)
        worker.join(timeout=3)


if __name__ == '__main__':
    main()
