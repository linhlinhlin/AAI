# Gán nhãn nhanh — mở file HTML

1. Mở `reviewer_1.html` bằng Chrome hoặc Edge. Không cần server, đăng nhập hay API key.
2. Nhập tên/mã của bạn, phiên bản và người duyệt bộ nhãn. Dán các nhãn đã thống nhất,
   **mỗi dòng một nhãn**. Bộ nhãn cần được người phụ trách chốt trước khi chấm;
   không tự xem tên cụm hoặc gợi ý AI để lấy làm đáp án.
3. Xác nhận chấm độc lập nếu đúng với việc bạn thực hiện. Nếu đã xem kết quả cụm/AI
   của các bài này, nhờ người chưa xem chấm độc lập, không xác nhận hộ.
4. Đọc từng bài: code và test ở bên trái; chọn dòng code và test làm căn cứ.
   Bên phải chọn kết luận, nhãn lỗi chính và ghi lý do. Bấm **Kiểm tra và sang bài tiếp**.
5. Bấm **Tải phiếu JSON**: nhận `reviewer_1.json`, đúng định dạng bộ đánh giá hiện có.
   Có thể xuất khi mới chấm một phần. Bài chưa chấm vẫn `pending`.

## Chọn kết luận nào?

| Kết luận | Điền gì? |
|---|---|
| Có cơ chế lỗi được bằng chứng hỗ trợ | Chọn nhãn trong bộ nhãn chung, ít nhất một dòng code và một test; ghi lý do |
| Chưa đủ bằng chứng | Ghi đang thiếu gì; không gán nhãn lỗi chính |
| Có nhiều cơ chế | Ghi các khả năng và vì sao chưa chọn được lỗi chính |
| Không quan sát thấy lỗi mục tiêu | Ghi căn cứ; không gán nhãn lỗi chính |
| Chưa chấm | Để phiếu bài đó trống; dùng “Để lại chưa chấm” nếu muốn xóa nhận định của bài hiện tại |

Ví dụ **cách viết lý do**, không phải đáp án cho bài đang mở:
“Dòng X cập nhật biến cục bộ; test Y cho thấy output vẫn giữ giá trị ban đầu.”
Chọn số dòng và test thực sự có trong bài; không chép ví dụ vào phiếu.

## Lưu và tiếp tục

- Nháp được lưu trên trình duyệt. Khi mở lại, bấm **Khôi phục nháp trên máy**.
- Nên **Tải bản nháp** trước khi nghỉ; bản nháp cho phép để dở các trường.
- **Nhập lại JSON** nhận cả bản nháp và phiếu đã xuất của chính bạn.
- Nháp phụ thuộc trình duyệt/đường dẫn file và có thể mất khi xóa dữ liệu trình duyệt.
  File HTML gốc không tự chứa các nhãn vừa điền; hãy giữ JSON tải xuống.
- Nút **Chữ lớn** tăng cỡ chữ cả code/test. Có thể dùng thêm Ctrl + dấu cộng.

## Từ phiếu cá nhân đến gold

Gói này có **48 bài ITSP development**, từ packet đã khóa
`.cache/teacher-validation-itsp-20260928`. Không phải dữ liệu của sáu bài demo trên app.
Mỗi bài chấm riêng, không lộ ID cụm, luật hay nhãn AI. Chưa điền sẵn nhãn nào.
Gói hiện **thiếu đề gốc**; điều phối viên cần cung cấp đề đã kiểm chứng riêng.
Không suy ra đề từ lời giải mẫu, không ép kết luận khi thiếu bằng chứng.

Gửi `reviewer_2.html` cho người thứ hai chấm độc lập với **cùng bộ nhãn**.
Không gửi phiếu bạn đã điền. Người thứ ba phân xử trong `adjudication.json`
của packet gốc sau khi cả hai đã chấm. Giao diện này phục vụ hai lượt chấm đầu;
không tự phân xử và không biến một phiếu cá nhân thành gold đã xác nhận.
Quy trình đầy đủ và lệnh đánh giá nằm ở `docs/teacher_validation.md`.

Phiếu xác nhận **cơ chế lỗi từ code/test**, không xác nhận niềm tin người học.
`cognitive_status` luôn `unassessed` vì không có lời giải thích và quan sát kiểm tra tiếp.
Giữ các JSON đã điền ngoài Git. Có thể gửi lại file JSON để kiểm tra và nhập vào luồng đánh giá.
