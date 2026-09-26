"""Export committed source and two fresh practice accounts, never the live database."""

import argparse
import hashlib
import json
import secrets
import subprocess
import tempfile
from datetime import UTC, datetime
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

from misconceptions.learning_store import Store


def export_handoff(root, output):
    def git(*args):
        return subprocess.check_output(['git', '-C', str(root), *args])

    if git('status', '--porcelain', '--untracked-files=no').strip():
        raise ValueError('Commit tracked changes before exporting the handoff.')
    revision = git('rev-parse', 'HEAD').decode().strip()
    tracked = [Path(name) for name in git('ls-files', '-z').decode().split('\0') if name]
    accounts = [
        {'username': 'aai_teacher', 'name': 'Giảng viên bàn giao', 'role': 'teacher'},
        {'username': 'aai_student', 'name': 'Học viên bàn giao', 'role': 'student'},
    ]
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='aai-handoff-') as temporary:
        database = Path(temporary) / 'learning.sqlite3'
        store = Store(database)
        for account in accounts:
            account['password'] = secrets.token_urlsafe(18)
            user = store.register(account['username'], account['name'],
                                  account['password'], account['role'])
            assert store.login(account['username'], account['password']) == user
        with store.connect() as db:
            db.execute('PRAGMA wal_checkpoint(TRUNCATE)')
        private = (
            '# Tài khoản bàn giao riêng\n\n'
            'Đăng nhập tại http://127.0.0.1:8766 sau khi chạy app trên máy nhận.\n'
            'Hai tài khoản này chỉ dùng cho bản luyện tập được bàn giao.\n'
            'Mỗi bản giải nén có database riêng, không đồng bộ với máy người gửi.\n'
            'Không đăng file này hoặc gói ZIP có mật khẩu lên GitHub công khai.\n\n'
            '| Vai trò | Tên đăng nhập | Mật khẩu |\n|---|---|---|\n'
            + ''.join(f"| {a['role']} | {a['username']} | `{a['password']}` |\n" for a in accounts)
            + '\nTài khoản học viên mới có thể tự đăng ký trên giao diện.\n'
            'Chỉ có một giảng viên được thiết lập cho mỗi database trong phiên bản này.\n'
        )
        manifest = {
            'source_commit': revision, 'created_utc': datetime.now(UTC).isoformat(),
            'scope': 'Fresh handoff accounts; no live learner data, sessions or API keys.',
            'accounts': [{k: a[k] for k in ('username', 'role')} for a in accounts],
            'database_sha256': hashlib.sha256(database.read_bytes()).hexdigest(),
            'tracked_file_hashes': {},
        }
        with ZipFile(output, 'x', compression=ZIP_DEFLATED) as archive:
            for relative in tracked:
                if any(part in {'.cache', '.venv', '.git', 'artifacts'} for part in relative.parts):
                    raise ValueError(f'Private/runtime path unexpectedly tracked: {relative}')
                if relative.name.startswith('.env') and relative.name != '.env.example':
                    raise ValueError(f'Environment credentials unexpectedly tracked: {relative}')
                data = (root / relative).read_bytes()
                name = relative.as_posix()
                manifest['tracked_file_hashes'][name] = hashlib.sha256(data).hexdigest()
                archive.writestr('AAI-handoff/' + name, data)
            archive.writestr('AAI-handoff/.cache/learning-app/learning.sqlite3', database.read_bytes())
            archive.writestr('AAI-handoff/PRIVATE_ACCOUNTS.md', private)
            archive.writestr('AAI-handoff/HANDOFF_MANIFEST.json',
                             json.dumps(manifest, ensure_ascii=False, indent=2))
    return revision


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True,
                        help='New private ZIP path, preferably under ignored artifacts/')
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    revision = export_handoff(root, args.output.resolve())
    print(f'Private handoff ZIP: {args.output.resolve()}')
    print(f'Source revision: {revision}')
    print('Passwords are inside PRIVATE_ACCOUNTS.md in the ZIP; not printed or committed.')


if __name__ == '__main__':
    main()
