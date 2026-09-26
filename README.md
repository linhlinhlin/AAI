# AAI — Misconceptions Clustering

Dự án khai phá các nhóm lỗi trong bài lập trình, biểu diễn OAV và đề xuất nhãn
quan niệm sai lầm để giảng viên duyệt.

Mã nguồn, dữ liệu demo/ITSP và hồ sơ nghiên cứu nằm tại
[`misconceptions-prototype`](misconceptions-prototype/README.md).

## App học viên và giảng viên

[AAI Learning](docs/learning_app.md) có tài khoản, 6 bài C17, editor, chạy test
thật trong Docker, phản hồi theo bằng chứng và lịch sử sửa bài. Giảng viên xem
OAV, nhóm lỗi, luật IF–THEN và ghi nội dung giảng lại từ bài nộp mới.

Từ `misconceptions-prototype`, sau khi cài môi trường Python và mở Docker:

```powershell
& .venv/Scripts/python.exe scripts/setup_learning.py
./start_learning.ps1
```

Mở `http://127.0.0.1:8766` để đăng ký học viên. Đường dẫn thiết lập giảng viên
đầu tiên được in trong terminal. Đây là app local; xem hướng dẫn trước khi
vận hành qua Internet. Dữ liệu lớp học mới tách khỏi bộ dữ liệu nghiên cứu.

## Nghiên cứu đề 5 — cập nhật 26/09/2026

Nhóm tự tìm dữ liệu công khai; mục tiêu là nghiên cứu cơ chế lỗi có bằng chứng,
với quan niệm sai là giả thuyết cần xác nhận. Không giả định hệ thống lớp học
hay dataset sẽ được giảng viên cung cấp.

- [Harness: cài đặt, kiểm tra, tái lập thí nghiệm](docs/harness.md)
- [Đối chiếu chính xác tiêu chí đề 5](docs/topic5-contract.md)
- [Trạng thái và kết quả có bằng chứng](research/STATE.md)
- [Khảo sát nghiên cứu đến 26/09/2026](research/literature/bao_cao_nghien_cuu.md)
- [Hướng dẫn agent](AGENTS.md) và [skill thực nghiệm](.agents/skills/aai-experiment/SKILL.md)

Harness thêm C-Pack-IPAs adapter, split toàn corpus và baseline dùng stdout.
Các hồ sơ tháng 9 trước đây được giữ làm lịch sử; STATE.md là nguồn trạng thái hiện tại.

## Chạy web trên Windows

```powershell
Set-Location misconceptions-prototype
py -m venv .venv
& .venv/Scripts/python.exe -m pip install -r requirements-lock.txt
& .venv/Scripts/python.exe -m pip install --no-deps --no-build-isolation -e .
Copy-Item .env.example .env
# Điền API key của bạn vào .env nếu muốn dùng gợi ý LLM.
./start_web.ps1
```

Mở http://127.0.0.1:8765. Web vẫn chạy bằng bộ luật cục bộ khi chưa cấu hình API.
Không commit `.env`. Nhãn AI là đề xuất chờ duyệt, không phải chẩn đoán đã xác nhận.

- [Hướng dẫn web](misconceptions-prototype/docs/web_workbench.md)
- [Cấu hình Gemini/OpenAI/Claude](misconceptions-prototype/docs/ai_cluster_labeling.md)
- [Hồ sơ nghiên cứu](misconceptions-prototype/docs/research_plan.md)

Dữ liệu ITSP đi kèm có nguồn gốc và giấy phép tại
[`data/raw/itsp`](misconceptions-prototype/data/raw/itsp).
Môi trường Python, khóa API, cache LLM và các lượt chạy web cục bộ không đưa lên Git.
