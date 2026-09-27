"""Live formative learning, kept separate from sealed research cohorts."""

import hashlib
import json
import logging
import secrets
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict

from .domain import Submission
from .features import extract_oav
from .learning_problems import PROBLEMS, get_problem
from .learning_sandbox import DockerSandbox
from .learning_store import Store
from .output_features import output_oav
from .pipeline import run_experiment
from .semantic_rules import build_teaching_report, describe_condition
from .teacher_dashboard import build_dashboard, validate_mapping

logger = logging.getLogger(__name__)

def evidence(attempt):
    result = attempt['result']
    problem = get_problem(attempt['problem_id'])
    observed = {test['test_id']: test['outcome'] for test in result['tests']}
    row = Submission(attempt['id'], attempt['user_id'], problem['id'], 'c', attempt['source'],
                     attempt['suite_version'],
                     {t['test_id']: observed.get(t['test_id'], 'not_run') for t in problem['tests']},
                     'live_docker_execution_formative')
    logs = [{k: test[k] for k in ('test_id', 'input', 'expected', 'output')}
            for test in result['tests']]
    return row, logs


class LearningService:
    def __init__(self, directory, sandbox=None):
        directory.mkdir(parents=True, exist_ok=True)
        self.store = Store(directory / 'learning.sqlite3')
        self.store.recover()
        self.sandbox = sandbox or DockerSandbox()
        self.executor = ThreadPoolExecutor(max_workers=1)
        token_file = directory / 'teacher-setup-token.txt'
        if not token_file.exists():
            token_file.write_text(secrets.token_urlsafe(32), encoding='utf-8')
        self.setup_token = token_file.read_text(encoding='utf-8').strip()
        self.health = self.sandbox.health()
        self.health_checked_at = time.monotonic()

    def runner_health(self):
        if time.monotonic() - self.health_checked_at > 15:
            self.health = self.sandbox.health()
            self.health_checked_at = time.monotonic()
        return self.health

    def submit(self, user, request):
        if user['role'] != 'student':
            raise PermissionError('Chỉ tài khoản học viên có thể nộp bài.')
        problem = get_problem(request.get('problem_id'))
        self.health = self.sandbox.health()
        if not self.health['ready']:
            raise ValueError(self.health['message'])
        key = self.store.create_attempt(user, problem, request.get('source'),
                                        request.get('reflection', ''))
        self.executor.submit(self._evaluate, key, user)
        return {'id': key}

    def _evaluate(self, key, user):
        attempt = self.store.attempt(key, user)
        problem = get_problem(attempt['problem_id'])
        try:
            result = self.sandbox.evaluate(
                attempt['source'], problem['tests'],
                lambda message: self.store.update_attempt(key, 'running', message),
            )
            result['provenance']['suite_sha256'] = problem['suite_sha256']
            result['provenance']['purpose'] = 'formative_practice_not_sealed_research_test'
            row, logs = evidence(attempt | {'result': result})
            result['oav'] = extract_oav(row) | output_oav(row, {row.submission_id: logs})
            teaching = build_teaching_report([row], {row.submission_id: logs}, {})
            result['findings'] = teaching['findings']
            result['feedback'] = self.feedback(result, problem)
            self.store.update_attempt(key, 'completed', 'Đã chấm xong.', result)
        except Exception:  # Persist interruption without inventing student outcomes.
            logger.exception('Attempt %s failed in execution infrastructure', key)
            self.store.update_attempt(key, 'system_error',
                                      'Môi trường chấm bị gián đoạn. Bài chưa được kết luận; hãy nộp lại.')

    @staticmethod
    def feedback(result, problem):
        if result['verdict'] == 'compile_error':
            return {'title': 'Chương trình chưa biên dịch được',
                    'message': 'Đọc thông báo đầu tiên của trình biên dịch và kiểm tra dòng được chỉ ra.',
                    'next_steps': ['Sửa lỗi biên dịch rồi chạy lại; chưa có test nào được thực thi.']}
        if result['verdict'] == 'accepted':
            return {'title': 'Bạn đã vượt qua các test hiện có',
                    'message': 'Hãy giải thích vì sao chương trình xử lý được cả trường hợp biên.',
                    'next_steps': ['Tự nghĩ thêm một đầu vào khác. Vượt test chưa chứng minh đúng với mọi đầu vào.']}
        failed = [t for t in result['tests'] if t['outcome'] != 'pass']
        if any(t['outcome'] == 'timeout' for t in failed):
            steps = ['Kiểm tra biến điều khiển có thay đổi và điều kiện dừng có thể đạt được không.']
        elif any(t['outcome'] == 'runtime_error' for t in failed):
            steps = ['Kiểm tra chỉ số mảng, địa chỉ con trỏ, phép chia và giới hạn output.']
        else:
            steps = list(dict.fromkeys(t['focus'] for t in failed))
        return {'title': 'Có bằng chứng để bạn kiểm tra tiếp',
                'message': f"{result['passed']}/{result['total']} test đạt. "
                           'Đối chiếu đầu ra ở test đầu tiên chưa đạt trước khi sửa.',
                'next_steps': steps, 'hint_levels': problem['hints'],
                'interpretation': 'Gợi ý kiểm tra, chưa phải kết luận về điều bạn hiểu sai.'}

    def overview(self):
        students, attempts = self.store.classroom()
        counts = self.store.attempt_counts()
        latest = {}
        for attempt in attempts:
            latest.setdefault((attempt['user_id'], attempt['problem_id']), attempt)
        problems = []
        for problem in PROBLEMS:
            rows = [a for a in latest.values() if a['problem_id'] == problem['id']]
            problems.append({'id': problem['id'], 'title': problem['title'],
                             'learners': len(rows),
                             'accepted': sum(a['result']['verdict'] == 'accepted' for a in rows),
                             'needs_work': sum(a['result']['verdict'] != 'accepted' for a in rows),
                             'attempts': counts.get(problem['id'], 0)})
        return {'students': students, 'total_attempts': sum(counts.values()), 'problems': problems,
                'recent_reports': self.store.recent_reports(),
                'scope': 'Bài đã chấm; mỗi học viên lấy lần nộp đã hoàn tất gần nhất theo bài tập.'}

    def analyze(self, teacher, problem_id, k=2):
        if teacher['role'] != 'teacher':
            raise PermissionError('Chức năng dành cho giảng viên.')
        problem = get_problem(problem_id)
        students, attempts = self.store.classroom()
        selected = {}
        for attempt in attempts:
            if attempt['problem_id'] == problem_id and attempt['suite_version'] == problem['suite_version']:
                selected.setdefault(attempt['user_id'], attempt)
        if len(selected) > 2000:
            raise ValueError('Cohort vượt giới hạn 2.000 người. Cần chia lớp trước khi phân tích.')
        pairs = [evidence(a) for a in selected.values()]
        rows, logs = [p[0] for p in pairs], {p[0].submission_id: p[1] for p in pairs}
        report = run_experiment(rows, test_ids=[t['test_id'] for t in problem['tests']],
                                method='kmeans', k=k, feature_mode='combined_stdout', logs=logs)
        report['population'] = {r.submission_id: r.student_id for r in rows}
        report['observed_oav'] = {r.submission_id: extract_oav(r) | output_oav(r, logs) for r in rows}
        report['teaching'] = build_teaching_report(rows, logs, report)
        labels = {t['test_id']: 'Ca «' + t['name'] + '»' for t in problem['tests']}
        for rule in report['teaching']['cluster_rules']:
            rule['if_vi'] = [describe_condition(condition, labels) for condition in rule['if']]
        report['teacher'] = build_dashboard(report)
        report['problem'] = problem
        report['students'] = students
        report['submissions'] = [asdict(row) | {'logged_tests': logs[row.submission_id]} for row in rows]
        report['provenance'] = {
            'source': 'live_learning_app', 'cohort_policy': 'latest_completed_per_student',
            'purpose': 'exploratory_classroom_analysis', 'human_validated': False,
            'suite_sha256': problem['suite_sha256'],
            'input_sha256': hashlib.sha256(json.dumps(
                report['submissions'], sort_keys=True, ensure_ascii=False).encode()).hexdigest(),
        }
        key = self.store.save_report(teacher, report)
        return {'id': key, 'report': report, 'reviews': []}

    def review(self, teacher, key, mappings):
        if teacher['role'] != 'teacher':
            raise PermissionError('Chức năng dành cho giảng viên.')
        report, _ = self.store.report(key)
        validate_mapping(report, mappings, teacher['username'])
        self.store.review(key, teacher, mappings)
        return {'id': key, 'teacher': build_dashboard(report, mappings),
                'notice': 'Đã lưu nhận xét giảng viên. Đây không phải nhãn đánh giá độc lập.'}
