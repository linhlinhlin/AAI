# Nhận diện in hằng số — 28/09/2026

## Phát hiện nguyên nhân

Đối chiếu read-only báo cáo demo lưu trong `.cache/course-demo/learning.sqlite3`:
Nhóm 1 có bốn mẫu in `15`, `3`, `5050`, `1`, mã nguồn dài 83–86 ký tự. Bản builder
trước đã gửi code trong `source`, cắt tối đa 3.000 ký tự. Vì vậy với các mẫu này,
việc cắt code không giải thích được kết quả sai. Không có raw request/trace suy
luận của lời gọi cũ để khẳng định chính xác tại sao model bỏ sót lỗi.

Các thiếu sót có thể kiểm chứng trong mã nguồn trước sửa:

- OAV chỉ có AST presence, chưa mô tả output hằng hoặc sự phụ thuộc đầu vào.
- Bộ luật chưa có mẫu in hằng số; bản local “chưa đủ bằng chứng” cũng được gửi
  trong context và có thể làm model thiên về kết luận đó.
- Prompt chưa bắt buộc đối chiếu `scanf → tính toán → printf` trước khi trả unclear.
- Bộ ghép diễn giải cho phép AI thay nhãn/căn cứ đã biết bằng câu trả lời chung chung.

## Thay đổi

`hardcoded_output.py` dùng tree-sitter, không tìm chuỗi bằng regex để xác định
lời gọi. Rule hẹp cho thân `main` tuyến tính, `printf`/`puts` dùng giá trị hằng
hoặc biến đã được gán hằng, cùng ít nhất hai verdict fail quan sát được.
Biến nhận từ `scanf` mất trạng thái hằng; biểu thức có biến nhập không được
coi là hằng. Chuỗi format `%d` không phải đáp án in cứng.

- OAV quan sát có boolean `is_hardcoded_output`.
- Luật `C_HARDCODED_OUTPUT` có dòng/lệnh code và test trượt làm dẫn chứng.
- Nhãn mặc định: **In hằng số / Chưa tính toán theo đầu vào**.
- Đếm trên toàn bộ thành viên nhóm, không lấy bốn mẫu LLM thay cho toàn nhóm.
  4/4 khớp cho nhãn cơ chế lỗi quan sát; 1/4 khớp thì ghi số lượng và nhóm hỗn hợp.
- Khi gợi ý từ báo cáo lưu cũ, kiểm tra lại source/outcomes trong snapshot để
  không phụ thuộc việc báo cáo cũ chưa có rule này. Không sửa snapshot gốc.
- `raw_code` chứa nguyên code của tối đa bốn mẫu, kèm dòng in và cờ OAV. Không cắt
  âm thầm; context JSON vượt 200 KB bị chặn trước HTTP bằng `context_too_large`
  và gợi ý cục bộ vẫn dùng được.
- Prompt chung áp dụng Groq, Gemini và các adapter khác: đọc raw_code, kiểm tra
  lệnh in và đường phụ thuộc dữ liệu trước khi kết luận không rõ lỗi.
- Với mẫu hardcoded đã khớp, AI chỉ bổ sung câu hỏi/giảng lại; không được xóa
  nhãn/căn cứ xác định bằng một câu “Không rõ lỗi”. Vẫn là bản nháp chưa duyệt.
- `PROMPT_VERSION=raw-code-hardcoded-output-v3` cùng hash prompt vô hiệu hóa cache
  gợi ý cũ khi bấm tạo gợi ý mới. Không xóa lịch sử nhận xét đã lưu.

## Giới hạn và bằng chứng

Rule không phải phân tích luồng dữ liệu C tổng quát: nhánh, vòng lặp, macro,
helper, alias và cấu trúc chưa hỗ trợ đều abstain. `False` nghĩa là chưa nhận diện
được bằng rule này, không phải chứng minh chương trình dùng input đúng.
Nhãn chỉ mô tả code/lỗi quan sát; chưa khẳng định niềm tin của học viên.

Cờ kết hợp verdict và AST là **OAV chẩn đoán**, không được tự đưa vào vector
clustering hoặc ablation structural-only đã đóng băng. FeatureSpace vẫn dùng
các block có sẵn; không thay các kết quả nghiên cứu lịch sử. Muốn đưa cờ này
vào clustering cần một biến thể/protocol và lượt chạy mới riêng.

Kiểm thử có positive/negative AST, biến hằng/biến scanf, mixed coverage,
code dài hơn giới hạn cũ, budget context, saved report và AI trả nhãn mơ hồ.
Đối chiếu demo: Nhóm 1 nhận đúng 4/4; nhóm còn lại chỉ 1/4. Không gọi API thật
để đo lại chất lượng Groq/Gemini trong đợt kiểm tra này.

## Cách thử

Dừng app cũ bằng Ctrl+C rồi chạy `./misconceptions-prototype/start_demo.ps1` từ
root, tải lại trang. Mở báo cáo cũ và bấm **Gợi ý nhận xét** để tính gợi ý phiên
bản mới, sau đó **Diễn giải bằng AI** nếu muốn gọi model. Để thấy cờ mới trong
OAV của báo cáo JSON, bấm **Xem nhóm lỗi** tạo báo cáo mới. Các nhận xét đã lưu
không bị tự ghi đè; cần bấm **Điền vào bản nháp** rồi lưu sau khi kiểm tra.
