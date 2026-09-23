# Trợ lý đề xuất nhãn cụm

Sau khi phân cụm, backend chuẩn bị bằng chứng và gọi OpenAI, Anthropic hoặc Gemini. Kết quả
luôn là **nhãn nháp**. Giảng viên đọc, duyệt, chỉnh sửa hoặc bỏ qua nhóm hỗn hợp.
LLM không thay thế thuật toán gom cụm và không tự xác nhận quan niệm của sinh viên.

## Cấu hình và chạy

Server tự đọc `.env` tại thư mục gốc dự án khi khởi động. File này được bỏ qua bởi
Git. Biến môi trường đã có được ưu tiên hơn `.env`; sau khi sửa file, khởi động lại
server bằng `./start_web.ps1` hoặc lệnh Python bên dưới. Cài dependency mới bằng
`.venv/Scripts/python.exe -m pip install -e '.[dev]'` khi cập nhật từ bản cũ.
Việc nạp file dùng [python-dotenv](https://bbc2.github.io/python-dotenv/reference/),
không nội suy biến trong giá trị khóa.

PowerShell 7, tại thư mục dự án:

```powershell
$env:MISCONCEPTIONS_LLM_PROVIDER = "openai"
$env:MISCONCEPTIONS_LLM_MODEL = Read-Host "Model ID hỗ trợ structured outputs"
$env:OPENAI_API_KEY = Read-Host "API key" -MaskInput
& .venv/Scripts/python.exe -m misconceptions.web --port 8766
```

Mở http://127.0.0.1:8766. Cổng 8766 cho phép thử mà không đụng phiên 8765 đang chạy.
Muốn dùng Claude: đổi provider thành `anthropic`, chọn model hỗ trợ tool use và đặt
`ANTHROPIC_API_KEY` thay cho `OPENAI_API_KEY`. Biến môi trường phải được thiết lập
trước khi khởi động server. Khóa chỉ được đọc ở backend, không nhập vào trình duyệt.
Không mặc định một model ID để tránh chọn model không có quyền truy cập.

Nếu thiếu cấu hình, lỗi API hoặc JSON không hợp lệ, hệ thống dùng bộ luật cục bộ
và ghi rõ nguồn trên từng thẻ. Đây không phải phản hồi LLM. Kiểm thử tự động dùng
API giả lập; cần khóa/model hợp lệ để kiểm thử kết nối nhà cung cấp thực tế.

## Demo trên web

Gemini: đặt `MISCONCEPTIONS_LLM_PROVIDER=gemini`,
`MISCONCEPTIONS_LLM_MODEL=gemini-3.5-flash-lite` và `GEMINI_API_KEY` trong `.env`, rồi
khởi động lại server. Backend dùng [GenerateContent API của Google](https://ai.google.dev/api/generate-content)
với JSON schema; khóa nằm trong header, không nằm trong URL. Model phải còn khả dụng
với project của khóa. Kết quả vẫn được kiểm tra schema và chờ giảng viên duyệt.

1. **Thí nghiệm** → chọn bộ dữ liệu → **Chạy thí nghiệm**.
2. **Tổng quan lớp**: biểu đồ hiển thị ngay các nhóm với tên đề xuất, số bài và tỷ lệ.
   Nhãn chưa duyệt được phân biệt với nhãn đã duyệt. Tỷ lệ là số bài trong nhóm
   chia toàn bộ bài của bộ dữ liệu, không phải xác suất AI đúng hoặc tỷ lệ sinh viên.
3. Bấm một thanh biểu đồ để tới **Duyệt & chỉnh sửa**, đúng nhóm tương ứng.
4. Nhập tên người duyệt một lần, đọc lý giải và bằng chứng. Chọn **Duyệt nhãn này**,
   **Chỉnh sửa** hoặc **Bỏ qua cụm này**. Có thể mở lại nhóm để đổi quyết định.
5. **Luật giải thích**: điều kiện dễ đọc, kết luận lấy từ nhãn nhóm và kèm trạng thái.
   Mở **Xem biểu diễn OAV đầy đủ** để đối chiếu bộ ba và toán tử gốc.

Bỏ qua không xóa bài hoặc thay đổi mẫu số biểu đồ. Mỗi quyết định tạo bản kết quả
mới theo đúng lượt chạy; không sửa annotation chấm mù hay kết quả nghiên cứu gốc.

## Bằng chứng và hợp đồng đầu ra

`ai_labeling.py` tổng hợp phân bố OAV của toàn nhóm; chọn tối đa bốn bài, ưu tiên
medoid và mẫu OAV khác nhau. Mỗi bài gửi tối đa 3.000 ký tự source và bốn log test,
mỗi trường log tối đa 240 ký tự. Các giới hạn được ghi trong payload. Mô tả đề tối
đa 4.000 ký tự, không lấy mã lời giải tham chiếu làm mô tả. Payload không có trường
student ID/submission ID; bảng ánh xạ sample được giữ cục bộ. Tuy nhiên source hoặc
comment có thể chứa thông tin cá nhân: cần rà soát trước khi dùng dữ liệu lớp thật
với API bên ngoài. Nội dung code/log được coi là dữ liệu, không phải chỉ dẫn cho AI.

System prompt chính thức nằm trong `llm_client.py` (`SYSTEM_PROMPT`). JSON gồm bốn
trường yêu cầu: `misconception_name`, `misconception_type`, `reasoning` (<50 từ tính
theo khoảng trắng), `teaching_hint`; bổ sung `category` và `evidence_samples` để chỉ
rõ nhóm hỗn hợp, lỗi trình bày hoặc chưa đủ bằng chứng và truy ngược bài dẫn chứng.
`misconception_type` cho phép null khi không phù hợp năm loại lỗi đã định nghĩa.
Không ép mọi cụm thành một quan niệm sai lầm. Validation kiểm tra schema và sample
tham chiếu; không chứng minh rằng suy luận của LLM đúng.

Mỗi nhánh phân tích gọi tối đa 12 lần, timeout 40 giây/lần; dừng gọi tiếp sau lỗi
đầu tiên. So sánh A/B/C có ba nhánh. Cache ở `results/llm_cache`, khóa theo provider,
model, prompt, schema và payload. Cache giảm lời gọi lặp lại, không loại bỏ chi phí
API. Báo cáo lưu nguồn đề xuất, model, usage và bằng chứng để truy vết.

## Cơ sở triển khai

- [OpenAI Chat API](https://developers.openai.com/api/reference/resources/chat):
  JSON schema structured outputs; request đặt `store: false`.
- [Anthropic Messages API](https://platform.claude.com/docs/en/api/messages/create):
  trả JSON qua tool schema `label_cluster`; không thực thi công cụ hoặc source.

Luật OAV giải thích quyết định cụm. Nhãn LLM là một lớp diễn giải cần đánh giá riêng
bằng chuyên gia; silhouette cao không chứng minh tên quan niệm đúng. Quy ước diễn
giải xem thêm [Rule Style Guide](itsp_rule_explanation_style.md).
