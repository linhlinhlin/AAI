# AAI — Misconceptions Clustering

Dự án khai phá các nhóm lỗi trong bài lập trình, biểu diễn OAV và đề xuất nhãn
quan niệm sai lầm để giảng viên duyệt.

Mã nguồn, dữ liệu demo/ITSP và hồ sơ nghiên cứu nằm tại
[`misconceptions-prototype`](misconceptions-prototype/README.md).

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
