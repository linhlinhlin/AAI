"""Account boundaries and evidence preservation use explicit synthetic fixtures."""

import json
import threading
import time
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer

import pytest

from misconceptions.learning_problems import PROBLEMS, get_problem
from misconceptions.learning_service import LearningService
from misconceptions.learning_store import Store
from misconceptions.learning_web import make_handler


class RecordedFixtureSandbox:
    def health(self):
        return {'ready': True, 'message': 'Synthetic test fixture'}

    def evaluate(self, source, tests, progress):
        progress('Synthetic fixture only')
        if source == 'infrastructure_failure':
            raise RuntimeError('synthetic infrastructure outage')
        observations = [t | {'output': '0\n',
                              'outcome': 'pass' if t['expected'].strip() == '0' else 'fail'}
                        for t in tests]
        return {'verdict': 'needs_work', 'diagnostics': '', 'tests': observations,
                'passed': sum(t['outcome'] == 'pass' for t in observations),
                'total': len(tests), 'provenance': {'runner': 'synthetic_test_fixture'}}


@pytest.fixture
def service(tmp_path):
    app = LearningService(tmp_path, RecordedFixtureSandbox())
    yield app
    app.executor.shutdown(wait=True)


def account(store, name, role='student'):
    return store.register(name, name, 'test-password-only', role)


def wait_attempt(app, key, user):
    for _ in range(200):
        attempt = app.store.attempt(key, user)
        if attempt['status'] not in ('queued', 'running'):
            return attempt
        time.sleep(.01)
    pytest.fail('Synthetic submission did not finish')


def test_password_session_and_persistence(tmp_path):
    store = Store(tmp_path / 'app.sqlite3')
    user = account(store, 'alice')
    with pytest.raises(ValueError):
        store.login('alice', 'wrong-password')
    assert store.login('ALICE', 'test-password-only') == user
    token = store.session(user)
    assert Store(store.path).authenticate(token) == user
    with store.connect() as db:
        row = dict(db.execute('SELECT * FROM users').fetchone())
    assert 'test-password-only' not in row['password']
    store.logout(token)
    assert store.authenticate(token) is None


def test_submission_ownership_evidence_and_no_gold(service):
    alice, bob = account(service.store, 'alice'), account(service.store, 'bob')
    key = service.submit(alice, {'problem_id': 'sum-range',
                                 'source': 'int main(void){return 0;}'})['id']
    attempt = wait_attempt(service, key, alice)
    assert attempt['status'] == 'completed'
    assert attempt['result']['oav']['test:t1'] == 'pass'
    assert attempt['result']['oav']['test:t2'] == 'fail'
    assert attempt['result']['provenance']['purpose'] == 'formative_practice_not_sealed_research_test'
    assert attempt['source'] == 'int main(void){return 0;}'
    with pytest.raises(PermissionError):
        service.store.attempt(key, bob)
    assert not service.store.history(bob)


def test_infrastructure_failure_never_becomes_student_failure(service):
    alice = account(service.store, 'alice')
    key = service.submit(alice, {'problem_id': 'swap', 'source': 'infrastructure_failure'})['id']
    attempt = wait_attempt(service, key, alice)
    assert attempt['status'] == 'system_error'
    assert attempt['result'] is None
    assert not service.store.classroom()[1]


def test_latest_attempt_classroom_and_teacher_boundaries(service):
    alice, teacher = account(service.store, 'alice'), account(service.store, 'teacher', 'teacher')
    for i in range(2):
        key = service.submit(alice, {'problem_id': 'sum-range',
                                     'source': f'int main(void){{return {i};}}'})['id']
        wait_attempt(service, key, alice)
    with pytest.raises(PermissionError):
        service.analyze(alice, 'sum-range')
    report = service.analyze(teacher, 'sum-range')['report']
    assert report['status'] == 'abstained'
    assert len(report['submissions']) == 1
    assert report['submissions'][0]['submission_id'] == key
    assert key in report['observed_oav']
    assert report['provenance']['human_validated'] is False
    assert service.overview()['total_attempts'] == 2
    assert len(service.overview()['recent_reports']) == 1


def test_analysis_reuses_snapshot_and_keeps_reviews_but_invalidates_new_data(service):
    alice, teacher = account(service.store, 'alice'), account(service.store, 'teacher', 'teacher')
    key = service.submit(alice, {'problem_id': 'sum-range', 'source': 'int main(){return 0;}'})['id']
    wait_attempt(service, key, alice)
    first = service.analyze(teacher, 'sum-range')
    # Store an authored historical note; its presence must not invalidate analysis inputs.
    service.store.review(first['id'], teacher, [{'label': 'fixture annotation, not gold'}])
    reused = service.analyze(teacher, 'sum-range')
    assert reused['id'] == first['id'] and reused['reused']
    assert reused['reviews'][0]['payload'][0]['label'] == 'fixture annotation, not gold'
    changed_k = service.analyze(teacher, 'sum-range', k=3)
    assert changed_k['id'] != first['id']
    key = service.submit(alice, {'problem_id': 'sum-range', 'source': 'int main(){return 1;}'})['id']
    wait_attempt(service, key, alice)
    changed_data = service.analyze(teacher, 'sum-range')
    assert changed_data['id'] not in (first['id'], changed_k['id'])
    assert changed_data['reviews'] == []
    history = service.overview()['recent_reports']
    assert {row['id'] for row in history} == {first['id'], changed_data['id']}
    # Hidden, unreviewed versions are retained, not destroyed.
    assert service.store.report(changed_k['id'])[0]['config']['k'] == 3


def test_reviewed_history_is_not_lost_after_many_empty_snapshots(service):
    teacher = account(service.store, 'teacher', 'teacher')
    payload = {'problem': get_problem('swap'), 'config': {'k': 2}}
    first = service.store.save_report(teacher, payload)
    service.store.review(first, teacher, [{'label': 'fixture only'}])
    for _ in range(30):
        last = service.store.save_report(teacher, payload)
    other = service.store.save_report(teacher, {'problem': get_problem('max-array')})
    history = service.store.recent_reports()
    assert {r['id'] for r in history} == {first, last, other}
    assert next(r for r in history if r['id'] == first)['reviews'] == 1


def test_restart_marks_pending_as_infrastructure_interruption(service):
    alice = account(service.store, 'alice')
    key = service.store.create_attempt(alice, get_problem('swap'), 'int main(){}', '')
    with pytest.raises(ValueError):
        service.store.create_attempt(alice, get_problem('swap'), 'int main(){}', '')
    service.store.recover()
    assert service.store.attempt(key, alice)['status'] == 'system_error'


def test_public_problem_oracles():
    assert len(PROBLEMS) == 6
    for p in PROBLEMS:
        assert len(p['tests']) == 6
        assert len({t['test_id'] for t in p['tests']}) == 6
        for t in p['tests']:
            numbers = list(map(int, t['input'].split()))
            if p['id'] == 'sum-range':
                value = str(sum(range(numbers[0] + 1)))
            elif p['id'] == 'mean-two':
                value = f'{sum(numbers) / 2:.2f}'
            elif p['id'] == 'max-array':
                value = str(max(numbers[1:]))
            elif p['id'] == 'count-positive':
                value = str(sum(n > 0 for n in numbers[1:]))
            elif p['id'] == 'swap':
                value = f'{numbers[1]} {numbers[0]}'
            else:
                x, y, r = numbers
                value = 'ON' if x*x+y*y == r*r else 'INSIDE' if x*x+y*y < r*r else 'OUTSIDE'
            assert t['expected'].strip() == value


def test_http_auth_csrf_roles_and_logout(service):
    server = ThreadingHTTPServer(('127.0.0.1', 0), make_handler(service))
    worker = threading.Thread(target=server.serve_forever, daemon=True)
    worker.start()
    conn = HTTPConnection(*server.server_address, timeout=10)

    def request(method, path, body=None, headers=None):
        supplied = {'Content-Type': 'application/json'} | (headers or {})
        conn.request(method, path, json.dumps(body) if body is not None else None, supplied)
        response = conn.getresponse()
        data = response.read()
        return response, json.loads(data)

    try:
        assert request('GET', '/api/history')[0].status == 401
        assert request('POST', '/api/register', {}, {'Origin': 'http://evil.example'})[0].status == 403
        response, data = request('POST', '/api/register', {
            'username': 'alice', 'name': 'Alice', 'password': 'test-password-only', 'role': 'teacher'})
        assert response.status == 200
        assert data['user']['role'] == 'student'
        cookie = response.getheader('Set-Cookie')
        assert 'HttpOnly' in cookie and 'SameSite=Strict' in cookie
        session = {'Cookie': cookie.split(';')[0]}
        assert request('GET', '/api/teacher/overview', headers=session)[0].status == 403
        assert request('POST', '/api/logout', {}, session)[0].status == 403
        assert request('POST', '/api/teacher/suggest', {}, session)[0].status == 403
        session['X-CSRF-Token'] = data['csrf']
        assert request('POST', '/api/teacher/suggest', {}, session)[0].status == 403
        assert request('POST', '/api/logout', {}, session)[0].status == 200
        assert request('GET', '/api/history', headers=session)[0].status == 401
        assert request('POST', '/api/setup', {'token': 'wrong'})[0].status == 403
    finally:
        conn.close()
        server.shutdown()
        server.server_close()
        worker.join(timeout=3)


def test_teacher_setup_is_single_use(service):
    account(service.store, 'teacher', 'teacher')
    with pytest.raises(ValueError):
        account(service.store, 'another_teacher', 'teacher')


@pytest.fixture
def suggestion_report(service, monkeypatch):
    from misconceptions import learning_service

    monkeypatch.setattr(learning_service, 'configuration', lambda *_: {
        'configured': False, 'provider': 'gemini', 'model': 'test-model'})
    teacher = account(service.store, 'teacher', 'teacher')
    student = account(service.store, 'private_student_name')
    problem = get_problem('sum-range')
    key = service.submit(student, {'problem_id': 'sum-range', 'source': problem['starter']})['id']
    attempt = wait_attempt(service, key, student)
    row, logs = learning_service.evidence(attempt)
    report = {'train_assignments': {key: 0}, 'holdout_assignments': {}, 'medoids': {'0': key},
              'problem': problem, 'teaching': {'summaries': []},
              'submissions': [learning_service.asdict(row) | {'logged_tests': logs}]}
    report_id = service.store.save_report(teacher, report)
    return teacher, student, report_id, report


def test_suggestion_without_key_is_explicit_local_draft(service, suggestion_report, monkeypatch):
    from misconceptions import learning_service

    teacher, student, key, original = suggestion_report
    monkeypatch.setattr(learning_service, 'request_label',
                        lambda *_: pytest.fail('No API call allowed without configuration'))
    with pytest.raises(PermissionError):
        service.suggest(student, key, '0')
    with pytest.raises(ValueError, match='Nhóm'):
        service.suggest(teacher, key, '99')
    proposal = service.suggest(teacher, key, '0')
    assert proposal['source'] == 'local_rules'
    assert proposal['status'] == 'draft'
    assert proposal['provider'] is None
    assert service.store.report(key) == (original, [])
    assert service.suggest(teacher, key, '0')['cached'] is True


def test_ai_suggestion_is_anonymized_cached_and_never_auto_approved(
        service, suggestion_report, monkeypatch):
    from misconceptions import learning_service

    teacher, student, key, original = suggestion_report
    monkeypatch.setattr(learning_service, 'configuration', lambda *_: {
        'configured': True, 'provider': 'gemini', 'model': 'test-model'})
    calls = []

    def call(payload, config):
        calls.append(payload)
        serialized = json.dumps(payload)
        assert student['username'] not in serialized and student['id'] not in serialized
        assert original['submissions'][0]['submission_id'] not in serialized
        return {'misconception_name': 'Chưa tính tổng', 'misconception_type': None,
                'reasoning': 'Chương trình luôn in 0.', 'teaching_hint': 'Liệt kê các số cần cộng.',
                'category': 'other_error', 'evidence_samples': ['sample_1']}, {'tokens': 10}

    monkeypatch.setattr(learning_service, 'request_label', call)
    proposal = service.suggest(teacher, key, '0', use_llm=True)
    assert proposal['source'] == 'llm' and proposal['status'] == 'draft'
    assert service.suggest(teacher, key, 0, use_llm=True)['cached'] is True
    assert len(calls) == 1
    assert service.store.report(key) == (original, [])
    assert Store(service.store.path).suggestions(key)[0]['output'] == proposal['output']


@pytest.mark.parametrize('bad_output', [False, True])
def test_failed_ai_suggestion_preserves_review_and_releases_lock(
        service, suggestion_report, monkeypatch, bad_output):
    from misconceptions import learning_service

    teacher, _, key, original = suggestion_report
    monkeypatch.setattr(learning_service, 'configuration', lambda *_: {
        'configured': True, 'provider': 'gemini', 'model': 'test-model'})

    def call(*_):
        if not bad_output:
            raise ValueError('Provider unavailable')
        return {'misconception_name': 'Tên', 'misconception_type': None,
                'reasoning': 'Căn cứ.', 'teaching_hint': 'Kiểm tra.',
                'category': 'other_error', 'evidence_samples': ['invented_sample']}, {}

    monkeypatch.setattr(learning_service, 'request_label', call)
    proposal = service.suggest(teacher, key, '0', use_llm=True)
    assert proposal['source'] == 'local_rules'
    assert proposal['output'] == proposal['local_output']
    assert proposal['llm_error']['code'] == 'invalid_response'
    assert 'Provider unavailable' not in proposal['notice']
    assert not service.suggestion_lock.locked()
    assert not service.store.suggestions(key)
    assert service.store.report(key) == (original, [])


def test_local_first_never_calls_configured_api(service, suggestion_report, monkeypatch):
    from misconceptions import learning_service
    teacher, _, key, _ = suggestion_report
    monkeypatch.setattr(learning_service, 'configuration', lambda *_: {
        'configured': True, 'provider': 'groq', 'model': 'test-model'})
    monkeypatch.setattr(learning_service, 'request_label', lambda *_: pytest.fail('Local must not call API'))
    proposal = service.suggest(teacher, key, '0')
    assert proposal['source'] == 'local_rules' and proposal['llm_error'] is None
    service.suggestion_lock.acquire()
    try:
        busy = service.suggest(teacher, key, '0', use_llm=True)
        assert busy['source'] == 'local_rules' and busy['llm_error']['code'] == 'busy'
    finally:
        service.suggestion_lock.release()


def test_api_failure_cooldown_and_recovery(service, suggestion_report, monkeypatch):
    from misconceptions import learning_service
    from misconceptions.llm_client import LLMRequestError
    teacher, _, key, original = suggestion_report
    monkeypatch.setattr(learning_service, 'configuration', lambda *_: {
        'configured': True, 'provider': 'groq', 'model': 'test-model'})
    calls = []
    def unavailable(*_):
        calls.append(1)
        raise LLMRequestError('API key không hợp lệ.', 'invalid_api_key')
    monkeypatch.setattr(learning_service, 'request_label', unavailable)
    first = service.suggest(teacher, key, '0', use_llm=True)
    assert first['llm_error']['code'] == 'invalid_api_key'
    assert service.suggest(teacher, key, '0', use_llm=True)['llm_error']['retry_after_seconds'] == 30
    assert len(calls) == 1 and not service.store.suggestions(key)
    service.suggestion_failures.clear()  # Simulate expiry without waiting or paid requests.
    monkeypatch.setattr(learning_service, 'request_label', lambda *_: (
        {'misconception_name': 'Diễn giải', 'misconception_type': 'Lỗi thuật toán',
         'reasoning': 'Có biểu hiện sai.', 'teaching_hint': 'Kiểm tra test.',
         'category': 'misconception', 'evidence_samples': ['sample_1']}, {}))
    recovered = service.suggest(teacher, key, '0', use_llm=True)
    assert recovered['source'] == 'llm'
    assert recovered['output']['category'] == recovered['local_output']['category']
    assert recovered['output']['misconception_type'] is None
    assert recovered['validation_status'] == 'unvalidated_hypothesis'
    assert service.store.report(key) == (original, [])
