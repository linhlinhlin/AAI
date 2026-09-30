# AAI — Misconceptions Clustering

Dự án khai phá các nhóm lỗi trong bài lập trình, biểu diễn OAV và đề xuất nhãn
quan niệm sai lầm để giảng viên duyệt.

Mã nguồn, dữ liệu demo/ITSP và hồ sơ nghiên cứu nằm tại
[`misconceptions-prototype`](misconceptions-prototype/README.md).

[Báo cáo 5 chương, slide và kịch bản thuyết trình](deliverables/De5_NghiemThu_20260928/README.md).

[Kiểm chứng baseline/ablation mới](research/runs/validation-summary-20260928.md) ·
[Quy trình nhãn giảng viên và xác thực misconception](docs/teacher_validation.md).

## AAI Lab — app chính (30/09/2026)

Một app local, không cần đăng nhập, gom bài C sai thành nhóm lỗi để dạy lại:

- **Lớp học**: nhóm lỗi, bằng chứng test, luật NẾU–THÌ (ILA-2), gợi ý dạy lại và đánh giá của giảng viên.
- **Chạy thử**: chạy bài C trong Docker cách ly, xem giả thuyết lỗi, thêm bài vào lớp.
- **Dữ liệu C-Pack**: cùng cách phân tích trên 25 bài thật, đối chiếu nhãn kiểm chứng.
- **Nghiên cứu**: câu hỏi, giả thuyết, ARI và luật từ kết quả kiểm định đã niêm phong.

```powershell
Set-Location misconceptions-prototype
./start_lab.ps1
```

Hoặc bấm đúp `misconceptions-prototype/start_lab.cmd`. App mở `http://127.0.0.1:8770`
và chỉ chạy khi cửa sổ đó còn mở. [Cách dùng, cách hoạt động và giới hạn](docs/aai_lab.md).
Hai app bên dưới (cổng 8766 và 8765) là bản cũ, giữ để tham khảo.

## App học viên và giảng viên (bản cũ)

[Chạy demo nghiệm thu môn học trong 10 phút](docs/demo_nghiem_thu.md):
cổng 8767, tài khoản demo và tám bài minh họa tự viết trong database riêng.

[Bàn giao cho đồng nghiệp và tài khoản riêng](docs/ban_giao_dong_nghiep.md) ·
[Báo cáo dễ hiểu: hướng nghiên cứu, mô hình, kết quả](docs/bao_cao_de5_de_hieu.md).

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

## Nghiên cứu đề 5 — cập nhật 30/09/2026

Nhóm tự chuẩn bị dữ liệu: chạy lại 8.607 bài C-Pack-IPAs trong môi trường cách ly, tạo nhãn cơ chế từ bản sửa tối thiểu đã kiểm chứng của chính sinh viên và bộ tiêm lỗi có kiểm soát, rồi đánh giá theo protocol đăng ký trước.

- [Benchmark cơ chế và cách tái lập](docs/mechanism-benchmark.md)
- [Trạng thái và kết quả kiểm định](research/STATE.md)
- [Bản thảo bài báo (EN)](paper/manuscript.pdf) · [bản dịch tiếng Việt](paper/vi/manuscript.pdf)
- [Báo cáo dễ hiểu](docs/bao_cao_de5_de_hieu.md)

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

## Bàn nghiên cứu trên Windows (bản cũ)

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
