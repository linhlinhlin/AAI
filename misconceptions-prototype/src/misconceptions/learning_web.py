"""Authenticated local learning app. Run with python -m misconceptions.learning_web."""

import argparse
import hashlib
import hmac
import json
import logging
import threading
import time
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from .learning_problems import PROBLEMS
from .learning_service import LearningService

STATIC = Path(__file__).with_name('web_assets')
logger = logging.getLogger(__name__)


def csrf(token):
    return hashlib.sha256(('aai-csrf:' + token).encode()).hexdigest()


def make_handler(service):
    auth_attempts = {}
    throttle_lock = threading.Lock()

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, *_args):
            pass  # Never log session cookies, passwords or learner source.

        def respond(self, status, data, mime='application/json; charset=utf-8', cookie=None):
            body = data if isinstance(data, bytes) else json.dumps(
                data, ensure_ascii=False, allow_nan=False).encode()
            self.send_response(status)
            self.send_header('Content-Type', mime)
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Cache-Control', 'no-store')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.send_header('Referrer-Policy', 'no-referrer')
            self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; "
                             "style-src 'self'; img-src 'self' data:; frame-ancestors 'none'; "
                             "base-uri 'none'; form-action 'self'")
            if cookie is not None:
                self.send_header('Set-Cookie', cookie)
            self.end_headers()
            try:
                self.wfile.write(body)
            except (BrokenPipeError, ConnectionResetError):
                pass

        def session(self):
            cookies = SimpleCookie()
            try:
                cookies.load(self.headers.get('Cookie', ''))
                token = cookies['aai_session'].value if 'aai_session' in cookies else ''
            except Exception:  # noqa: BLE001 — reject malformed client cookie
                token = ''
            return token, service.store.authenticate(token) if token else None

        def boundary(self):
            port = self.server.server_address[1]
            hosts = {f'127.0.0.1:{port}', f'localhost:{port}'}
            if self.headers.get('Host') not in hosts:
                raise PermissionError('Chỉ truy cập qua địa chỉ local được cấu hình.')
            origin = self.headers.get('Origin')
            if origin and origin not in {'http://' + host for host in hosts}:
                raise PermissionError('Nguồn yêu cầu không hợp lệ.')

        @staticmethod
        def teacher(user):
            if not user or user['role'] != 'teacher':
                raise PermissionError('Chức năng dành cho giảng viên.')

        def do_GET(self):
            try:
                self.boundary()
                path = urlparse(self.path)
                assets = {'/': ('learning.html', 'text/html'),
                          '/learn.js': ('learning.js', 'text/javascript'),
                          '/learn.css': ('learning.css', 'text/css')}
                if path.path in assets:
                    filename, mime = assets[path.path]
                    return self.respond(200, (STATIC / filename).read_bytes(), mime + '; charset=utf-8')
                token, user = self.session()
                if path.path == '/api/bootstrap':
                    return self.respond(200, {'user': user, 'csrf': csrf(token) if user else None,
                                              'problems': PROBLEMS, 'runner': service.runner_health()})
                if not user:
                    return self.respond(401, {'error': 'Hãy đăng nhập để tiếp tục.'})
                query = parse_qs(path.query)
                if path.path == '/api/history':
                    return self.respond(200, {'attempts': service.store.history(user),
                                              'stats': service.store.history_stats(user)})
                if path.path == '/api/attempt':
                    return self.respond(200, service.store.attempt(query.get('id', [''])[0], user))
                if path.path == '/api/teacher/overview':
                    self.teacher(user)
                    return self.respond(200, service.overview())
                if path.path == '/api/teacher/report':
                    self.teacher(user)
                    key = query.get('id', [''])[0]
                    report, reviews = service.store.report(key)
                    return self.respond(200, {'id': key, 'report': report, 'reviews': reviews})
                return self.respond(404, {'error': 'Không tìm thấy nội dung.'})
            except PermissionError as error:
                self.respond(403, {'error': str(error)})
            except (ValueError, TypeError) as error:
                self.respond(400, {'error': str(error)})

        def do_POST(self):
            try:
                self.boundary()
                if self.headers.get('Content-Type', '').split(';')[0] != 'application/json':
                    raise ValueError('Yêu cầu phải là JSON.')
                length = int(self.headers.get('Content-Length', '0'))
                if not 0 < length <= 100000:
                    raise ValueError('Yêu cầu vượt giới hạn kích thước.')
                request = json.loads(self.rfile.read(length))
                if not isinstance(request, dict):
                    raise TypeError('Nội dung yêu cầu không hợp lệ.')
                path = urlparse(self.path).path
                if path in ('/api/login', '/api/register', '/api/setup'):
                    with throttle_lock:
                        now = time.monotonic()
                        key = self.client_address[0]
                        attempts = [t for t in auth_attempts.get(key, []) if t > now - 60]
                        if len(attempts) >= 20:
                            return self.respond(429, {'error': 'Quá nhiều lần đăng nhập. Đợi một phút.'})
                        auth_attempts[key] = attempts + [now]
                    if path == '/api/login':
                        user = service.store.login(request.get('username'), request.get('password'))
                    else:
                        role = 'student'
                        if path == '/api/setup':
                            if not hmac.compare_digest(str(request.get('token', '')), service.setup_token):
                                raise PermissionError('Mã thiết lập không đúng.')
                            role = 'teacher'
                        user = service.store.register(request.get('username'), request.get('name'),
                                                       request.get('password'), role)
                    token = service.store.session(user)
                    return self.respond(200, {'user': user, 'csrf': csrf(token)}, cookie=
                                        f'aai_session={token}; HttpOnly; SameSite=Strict; Path=/; Max-Age=43200')
                token, user = self.session()
                if not user:
                    return self.respond(401, {'error': 'Hãy đăng nhập để tiếp tục.'})
                if not hmac.compare_digest(self.headers.get('X-CSRF-Token', ''), csrf(token)):
                    raise PermissionError('Phiên không hợp lệ. Hãy tải lại trang.')
                if path == '/api/logout':
                    service.store.logout(token)
                    return self.respond(200, {'ok': True}, cookie=
                                        'aai_session=; HttpOnly; SameSite=Strict; Path=/; Max-Age=0')
                if path == '/api/submit':
                    return self.respond(202, service.submit(user, request))
                if path == '/api/runner':
                    service.health = service.sandbox.health()
                    return self.respond(200, service.health)
                if path == '/api/teacher/analyze':
                    self.teacher(user)
                    return self.respond(200, service.analyze(user, request.get('problem_id'),
                                                            request.get('k', 2)))
                if path == '/api/teacher/review':
                    self.teacher(user)
                    return self.respond(200, service.review(user, request.get('id'),
                                                           request.get('mappings')))
                return self.respond(404, {'error': 'Không tìm thấy chức năng.'})
            except PermissionError as error:
                self.respond(403, {'error': str(error)})
            except (ValueError, TypeError, KeyError) as error:
                self.respond(400, {'error': str(error)})
            except Exception:  # Fail closed without exposing database or host details.
                logger.exception('Learning API failed')
                self.respond(500, {'error': 'Có lỗi xử lý. Dữ liệu đã lưu vẫn được giữ; hãy thử lại.'})

    return Handler


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8766)
    parser.add_argument('--data-dir', type=Path,
                        default=Path(__file__).resolve().parents[3] / '.cache/learning-app')
    args = parser.parse_args()
    service = LearningService(args.data_dir)
    server = ThreadingHTTPServer(('127.0.0.1', args.port), make_handler(service))
    print(f'AAI Learning: http://127.0.0.1:{args.port}', flush=True)
    if not service.store.has_teacher():
        print(f'Teacher setup (local owner only): http://127.0.0.1:{args.port}/'
              f'#setup={service.setup_token}', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        service.executor.shutdown(wait=True)


if __name__ == '__main__':
    main()
