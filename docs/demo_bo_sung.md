# Dữ liệu bổ sung cho bốn bài demo

Script `misconceptions-prototype/scripts/extend_learning_demo.py` bổ sung dữ liệu
tự viết vào lớp DEMO có sẵn ở `.cache/course-demo`, thông qua API ứng dụng đang chạy.
Code được biên dịch và chạy test bằng Docker runner của ứng dụng; script kiểm tra
đúng số test đạt và không tự ghi kết quả chấm giả vào database.

Mỗi bài có thêm 10 tài khoản `demo_more_01` đến `demo_more_10`, tên hiển thị
`DEMO bổ sung NN (tự viết)`. Cùng 10 tài khoản được sử dụng xuyên bốn bài.
Mật khẩu của tài khoản demo này là `Demo-AAI-2026!`, chỉ dành cho lớp demo local.
Các tài khoản/lượt nộp cũ được giữ nguyên. Các số bên dưới chỉ tính phần bổ sung.

| Bài | DEMO 01–04 | DEMO 05–08 | DEMO 09–10 |
|---|---|---|---|
| Phần tử lớn nhất | Max khởi tạo 0: 4/6 test | Bỏ phần tử cuối: 5/6 test | Đúng 6/6 test |
| Đếm số dương | Đếm cả 0: 3/6 test | Bỏ phần tử cuối: 2/6 test | Đúng 6/6 test |
| Hoán vị qua hàm | Đổi bản sao tham số: 1/6 test | Ghi đè mất giá trị cũ: 1/6 test | Đúng 6/6 test |
| Điểm và đường tròn | So sánh khoảng cách bình phương với r: 3/6 test | Else gắn if thứ hai: 4/6 test | Đúng 6/6 test |

Mỗi nhóm gồm các biến thể code. Những dạng lỗi trong bảng là chủ đích của tác giả
fixture, không phải gold nhãn nhận thức hay nhận xét giảng viên. Clustering vẫn
chạy từ OAV/test/output; không đưa các tên lỗi này vào features, không ép hai cụm
thuật toán phải trùng với hai nhóm lỗi dự kiến. Bài đúng nằm trong thống kê lớp
nhưng không được đưa vào tập bài sai cần phân cụm.

## Xem trên giao diện

1. Mở `http://127.0.0.1:8767/`, tải lại trang nếu đang mở.
2. Đăng nhập `demo_teacher` với mật khẩu demo ở trên.
3. Vào **Lớp học & nhóm lỗi**, chọn một trong bốn bài, giữ `k = 2` rồi bấm
   **Xem nhóm lỗi** để phân tích dữ liệu hiện tại.
4. Mở bài đại diện, đối chiếu code với input/expected/output; xem OAV và IF–THEN.
5. Bấm **Gợi ý nhận xét** để xem bản cục bộ. Gợi ý có thể chưa xác định được cơ chế
   chung; phải xem bằng chứng trước khi lưu nhận xét. Không tự gán gold cho demo.

Ví dụ dễ trình bày: hai nhóm lỗi hoán vị đều chỉ qua test hai số bằng nhau nhưng
output ở các test khác khác nhau. Với đường tròn, lỗi else in cả INSIDE và ON
cho một điểm ở trong. Với max, test toàn số âm làm lộ giả định max ban đầu bằng 0.

## Chạy lại khi cần

Giữ ứng dụng DEMO ở cổng 8767 và Docker Desktop đang chạy, chờ các bài đang chấm
hoàn tất. Từ repository root:

```powershell
& .\misconceptions-prototype\.venv\Scripts\python.exe `
  misconceptions-prototype/scripts/extend_learning_demo.py
```

Script kiểm tra marker lớp synthetic và ID giảng viên để tránh nạp vào database khác.
Trước khi thêm dữ liệu, nó sao lưu SQLite bằng backup API trong
`.cache/course-demo/extension-<timestamp>/before.sqlite3`.
Mỗi lần chạy có manifest với hash source, suite, provenance thực thi và ID bài nộp;
bốn snapshot phân cụm được lưu cùng thư mục. Nếu bản nộp gần nhất của tài khoản
fixture khớp source/suite và đã hoàn tất, script dùng lại, không nộp trùng.
Snapshot báo cáo mới vẫn được tạo khi chạy lại.

Database, backup và manifest local không đưa lên Git. Không nhập dữ liệu này vào
ITSP/C-Pack, packet nghiên cứu hay sealed test. Hai bài tổng/trung bình giữ dữ liệu
hiện có; script này chỉ bổ sung bốn bài đã chọn.
