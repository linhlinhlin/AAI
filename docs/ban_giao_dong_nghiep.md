# Bàn giao đề 5 cho đồng nghiệp — 27/09/2026

Đọc [báo cáo dễ hiểu về hướng nghiên cứu và mô hình](bao_cao_de5_de_hieu.md).
Mã hiện nằm ở nhánh `research/topic5-harness` của
[meiiie/AAI](https://github.com/meiiie/AAI/tree/research/topic5-harness), đang gửi về
repo nhóm qua [PR #1](https://github.com/linhlinhlin/AAI/pull/1), chưa merge `main`.

## Nhận ZIP có tài khoản

Giải nén gói riêng người bàn giao gửi, mở thư mục `AAI-handoff`.
File `PRIVATE_ACCOUNTS.md` chứa tên đăng nhập và mật khẩu cho hai vai trò:

| Tài khoản | Dùng để |
|---|---|
| `aai_student` | Viết/nộp code, xem test và lịch sử |
| `aai_teacher` | Xem lớp, OAV, cụm, luật và ghi nhận xét |

Mật khẩu được tạo ngẫu nhiên theo mỗi gói, không có mật khẩu mặc định công khai.
Gói này có database mới gồm đúng hai tài khoản, chưa có bài nộp và không có
phiên đăng nhập. Không mang theo tài khoản cá nhân, code riêng, API key hoặc
database lớp học của người gửi. Không đăng ZIP hay file mật khẩu lên repo công khai.

Mỗi người chạy một bản app/database trên máy mình. `127.0.0.1` nghĩa là
“máy đang ngồi dùng”, không phải đường dẫn vào máy người gửi. Code trong GitHub
không tự biến thành website online; các bản giải nén không đồng bộ bài nộp.

## Chạy trên Windows

Chuẩn bị Python 3.12 có lệnh `py`, Docker Desktop đang chạy **Linux engine**,
và Internet để tải dependency/image lần đầu. Không cần GPU, khóa LLM hoặc Kaggle.
Tại thư mục `AAI-handoff`, mở PowerShell và chạy:

```powershell
./misconceptions-prototype/setup_and_start_learning.ps1
```

Nếu máy chặn script PowerShell, chạy trực tiếp các lệnh sau thay vì thay đổi
execution policy toàn máy:

```powershell
Set-Location misconceptions-prototype
py -3.12 -m venv .venv
& .venv/Scripts/python.exe -m pip install -r requirements-lock.txt
& .venv/Scripts/python.exe -m pip install --no-deps --no-build-isolation -e .
& .venv/Scripts/python.exe scripts/setup_learning.py
& .venv/Scripts/python.exe -X utf8 -m misconceptions.learning_web --port 8766
```

Mở **http://127.0.0.1:8766**, dùng tài khoản trong `PRIVATE_ACCOUNTS.md`.
Giữ terminal và Docker đang chạy. Những lần sau chỉ cần chạy
`./misconceptions-prototype/start_learning.ps1`. Nếu cổng bận, thêm `--port 8767`
vào lệnh Python hoặc `-Port 8767` vào script setup rồi mở đúng cổng đó.

Linux: tạo `.venv` bằng Python 3.12, dùng `.venv/bin/python` thay đường dẫn
Windows trong các lệnh cài/chạy; cần Docker Linux hoạt động.

## Nếu lấy mã trực tiếp từ GitHub

```text
git clone --branch research/topic5-harness https://github.com/meiiie/AAI.git
cd AAI
```

Chạy script setup ở trên. Bản clone không chứa tài khoản/mật khẩu/database.
Học viên chọn “Đăng ký học viên”; chủ máy dùng đường dẫn **Teacher setup**
in trong terminal để tạo giảng viên đầu tiên. Không ghép database ZIP vào
một lớp đã có dữ liệu; hãy giải nén và dùng thư mục riêng.

## Kịch bản giới thiệu trong 5 phút

1. Đăng nhập học viên, chọn “Tổng từ 1 đến n”. Chạy code ban đầu, xem từng test.
2. Sửa code, chạy lại, mở “Hành trình của tôi” và xem cả hai lần nộp.
3. Đăng xuất, đăng nhập giảng viên. Xem đúng số học viên/lượt nộp vừa phát sinh.
4. Một học viên chưa đủ để phân cụm: thông báo thiếu dữ liệu là hành vi đúng.
   Cần ít nhất bốn bài sai đủ điều kiện và đủ nhóm/source/đặc trưng độc lập.
5. Dùng [ảnh và kết quả nghiệm thu](../research/learning-app/README.md) để
   trình bày màn hình cụm/luật đã chạy. Các tài khoản trong ảnh được ghi rõ là
   fixture kiểm thử, không gọi là lớp sinh viên thực.

Chi tiết sandbox, quyền truy cập, bằng chứng và giới hạn ở
[hướng dẫn app](learning_app.md). Bản này chạy local; chưa triển khai Internet.

## Tạo lại gói bàn giao riêng

Sau khi commit mã, từ repo root:

```powershell
& misconceptions-prototype/.venv/Scripts/python.exe misconceptions-prototype/scripts/export_learning_handoff.py --output artifacts/AAI-handoff-private.zip
```

Script chỉ đóng gói các file Git theo dõi ở checkout sạch, giữ nguyên byte
của các artifact đã khóa, tạo database và mật khẩu mới. File manifest trong
ZIP ghi commit nguồn và hash từng file. Không ghi đè ZIP đã có, không đọc
database app đang dùng. Đường dẫn `artifacts/` và `PRIVATE_ACCOUNTS.md` đã ignore.
