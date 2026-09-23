# Test bằng giao diện web

**Đề xuất nhãn tự động:** [Cấu hình OpenAI/Claude và luồng duyệt nhãn](ai_cluster_labeling.md).
Web chạy được không cần API; đề xuất LLM cần cấu hình riêng, nếu thiếu sẽ ghi rõ dùng bộ luật cục bộ.

**Luồng mới:** [Dashboard giảng viên → K-means → gắn nhãn → luật OAV](teacher_dashboard_flow.md).
K-means là mặc định. Cấu hình kỹ thuật nằm trong Advanced Settings. Ví dụ Average-linkage
bên dưới là baseline nghiên cứu, cần mở Advanced Settings và chọn rõ thuật toán đó.

Chạy trong PowerShell với môi trường `.venv` đã cài theo README:

```powershell
Set-Location E:/AAI/misconceptions-prototype
& .venv/Scripts/python.exe -m misconceptions.web --port 8765
```

Mở http://127.0.0.1:8765 trong trình duyệt. Giữ terminal mở; Ctrl+C để dừng.
Có thể dùng `./start_web.ps1` thay cho lệnh Python. Nếu cổng đang bận, mở phiên đã chạy
hoặc chọn `--port 8766`. Không cần Node.js, tài khoản, API key hoặc GPU để chạy web.

## Lượt test đầu tiên

1. **Thí nghiệm:** chọn ITSP `2825`, Average-linkage, Test + cấu trúc, k=3,
   seed=42, trọng số test 80%, holdout 25%. Bấm **Chạy thí nghiệm**.
   Dữ liệu hiện có cho 22 bài đủ điều kiện, 3 cụm; silhouette train khoảng 0.696.
2. Xem **Cụm & bài làm**; bấm một submission để xem source, OAV và log test.
   Các tab còn lại hiển thị luật, ma trận đặc trưng và thông tin chia tập/routing.
   Tab luật có thêm giả thuyết cơ chế từ AST + log, kèm dòng code và test dẫn chứng.
   Xem [phạm vi và ví dụ luật](teaching_rules.md); chọn `demo_swap_by_value` để thử mẫu hoán vị.
3. **So sánh A/B/C:** bấm chạy để đối chiếu outcomes, cấu trúc và kết hợp với cùng
   cấu hình. Arm không đủ thông tin sẽ ghi lý do chưa thể phân cụm.
4. **Dữ liệu & OAV:** mở dữ liệu đang chọn hoặc nhập manifest JSON + submissions
   JSONL. Có hai file mẫu tải trực tiếp. Input sai schema được báo lỗi.
5. **Kiểm tra kỹ thuật:** chạy pytest, Ruff, audit gói vòng 1 hoặc hash nguồn reviewer.
6. **Kho báo cáo:** tìm `web_runs` để xem/tải kết quả vừa chạy; tìm `summary` để đọc
   báo cáo nghiên cứu đã có. File Markdown hiển thị dưới dạng văn bản gốc.

## Hồ sơ reviewer

Tải ZIP vòng 1/vòng 2 và đọc codebook. Có thể tải lên annotation JSON để kiểm tra
schema, hợp nhất vòng 1 hoặc tính metrics theo cơ chế hiện có. Hợp nhất và tính metrics
yêu cầu người điều phối xác nhận nguồn dữ liệu; backend vẫn áp dụng validation gốc.
Phiếu trống không tạo ra nhãn hoặc metrics giả. Chức năng này chỉ áp dụng cho 17 mẫu
ITSP cố định, không cho các cụm mới tạo trong giao diện.

Đây là giao diện điều phối có thể thấy cụm và báo cáo AI. Người chấm độc lập vòng 1
sử dụng ZIP riêng, không dùng giao diện này làm môi trường chấm mù.

## Phạm vi và lưu trữ

- Server chỉ lắng nghe trên `127.0.0.1`, dành cho thử nghiệm trên máy cá nhân.
- Mỗi thao tác tạo thư mục riêng `results/web_runs/<job-id>/` với kết quả/log;
  dữ liệu nhập mới và annotation output cũng nằm tại đó. Không ghi đè artifact nghiên cứu.
- Một tác vụ xử lý tại một thời điểm. Sau khi tải lại trang, dùng Kho báo cáo để tìm
  kết quả đã lưu; các bảng kết quả tương tác thuộc phiên trình duyệt hiện tại.
- Upload tối đa 16 MB mỗi request; pipeline giới hạn 2.000 bài/cohort.
- Chỉ khai thác log có sẵn, không biên dịch hoặc thực thi bài nộp.
- Cụm/luật là giả thuyết cần kiểm chứng; silhouette và fidelity không xác thực misconception.
- Các chức năng chưa có được liệt kê ở **Chức năng sắp có** với nút vô hiệu hóa:
  sandbox, đặc trưng ngữ nghĩa nâng cao, ILA, editor chấm web, adjudication trên web,
  đánh giá cơ chế/tập mới, adapter LMS và đo hiệu quả giảng dạy. Đây chưa phải cam kết lịch phát hành.

Giao diện là HTML/CSS/JavaScript tĩnh; HTTP adapter trong `src/misconceptions/web.py`
gọi trực tiếp core hiện có. Kiểm thử web tại `tests/test_web.py`.
