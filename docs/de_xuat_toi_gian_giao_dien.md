# Đề xuất tối giản giao diện — 29/09/2026

Đã triển khai sau khi người dùng đồng ý. Phần bên dưới lưu lại đề xuất ban đầu.
Đã xem mã HTML/CSS/JS
và mở màn hình giảng viên thật bằng Chromium ở 1366×768. Ảnh khảo sát local:
`.cache/ui-review-20260929/teacher-1366.png`.
Tham khảo: https://raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main/command.md

## Phát hiện theo file

- `misconceptions-prototype/src/misconceptions/web_assets/learning.html:9`:
  khẩu hiệu trên header không hỗ trợ thao tác; bỏ, giảm header từ 88 xuống khoảng 60 px.
- `misconceptions-prototype/src/misconceptions/web_assets/learning.html:16`:
  eyebrow và lời chào trùng vai trò với tab; thay bằng một tiêu đề chức năng hoặc bỏ
  khối này khi tab đã đủ ngữ cảnh. Runner để badge nhỏ, chỉ mở chi tiết khi có lỗi.
- `misconceptions-prototype/src/misconceptions/web_assets/learning.html:20`:
  hai lớp tiêu đề trang trí và đoạn giải thích dài đẩy bài tập xuống dưới; thay bằng
  “Bài tập” và một dòng “Dữ liệu: bài nộp gần nhất”. Chi tiết phương pháp đặt trong trợ giúp.
- `misconceptions-prototype/src/misconceptions/web_assets/learning.css:4`:
  nhiều thành phần cần đọc thường xuyên dùng 10–12 px, thấp hơn hẳn tiêu đề trang trí;
  tăng nội dung lên 16 px, chú thích ít nhất 14 px, rule/code 15–16 px. Đây là đề xuất
  thiết kế cho màn hình demo, không phải tuyên bố ngưỡng tuân thủ accessibility.
- `misconceptions-prototype/src/misconceptions/web_assets/learning.js`:
  `loadClass` dồn 25 báo cáo vào danh sách bài; `renderReport` nối toàn bộ phân tích
  xuống cuối trang và mở form nhận xét ở mọi nhóm. Cần chuyển sang màn chi tiết bài,
  nhận xét tùy chọn, lịch sử theo bài và thu gọn.

Đo trực tiếp: topbar 88 px; khối lời chào 61 px; thẻ thống kê 115 px;
danh sách bài bắt đầu ở y≈547 px. Tên bài 14 px; thống kê và lịch sử 11 px.
Đây là số đo của phiên hiện tại, không khẳng định áp dụng cho mọi viewport.

## Nội dung nên bỏ hoặc thay

| Hiện tại | Đề xuất |
|---|---|
| KHÔNG GIAN GIẢNG VIÊN | Bỏ; vai trò đã biết sau đăng nhập |
| Nhìn rõ từng bước tiến của lớp. | Bỏ; tiêu đề chức năng “Phân tích bài làm” nếu cần |
| Mỗi lỗi sai là một điểm bắt đầu. | Bỏ khỏi header |
| TỪ BẰNG CHỨNG ĐẾN NỘI DUNG GIẢNG LẠI | Bỏ |
| Lớp đang vướng ở đâu? | Bài tập |
| Lớp học & nhóm lỗi | Phân tích bài làm |
| Hành trình của tôi | Lịch sử bài nộp |
| Các đoạn nhắc phạm vi lặp lại | Badge ngắn “Chưa xác thực”; giải thích trong “Phạm vi đánh giá” |
| Luật gợi ý lỗi từ code và test | Dấu hiệu lỗi |
| Báo cáo đã lưu | Lịch sử phân tích, chỉ trong bài đang mở |

Giữ các thông tin làm thay đổi cách hiểu kết quả: số bài khớp, tập mẫu số,
nhóm hỗn hợp, trạng thái chưa xác thực, nguồn luật cục bộ/quy nạp. Không xóa hết
để tạo cảm giác hệ thống chẩn đoán chắc chắn. Thông báo thiếu dữ liệu chỉ hiện khi
thật sự thiếu, ví dụ “Chưa đủ bài sai để phân nhóm”.

## Bố cục đề xuất

Màn danh sách: header gọn → điều hướng → thống kê một dòng → bảng sáu bài.
Bảng gồm tên bài, số học viên đã nộp, đạt, cần hỗ trợ, trạng thái phân tích và nút
“Mở phân tích”. Không đặt k=2/3 lặp lại ở mọi dòng; đưa “Số nhóm” vào tùy chọn
của bài đang xem. Tài khoản giảng viên ưu tiên phân tích; mục luyện tập để phụ.

Màn chi tiết: nút “Quay lại bài tập”, tên bài, trạng thái dữ liệu, nút cập nhật.
Mỗi nhóm mặc định chỉ hiện tên/ID, số bài, dấu hiệu lỗi, luật NẾU/VÀ/THÌ ngắn và
một bài đại diện. Mở “Xem bằng chứng” để xem code và bảng input/expected/actual.
Danh sách toàn bộ thành viên, OAV, số đo fidelity và điều kiện gốc mở khi cần.
Không tự đặt tên lỗi cho nhóm chưa đủ căn cứ: giữ “Nhóm 1 — chưa xác định lỗi chung”.

Nhận xét: một nút “Ghi chú giảng viên” thay cho form luôn mở. Có nội dung thì hiện
tóm tắt và trạng thái lưu; sửa trong vùng mở rộng. Nhận xét đã lưu không tự chuyển
thành nhãn được xác thực. Nháp nên tự lưu với trạng thái rõ, phân biệt với xác nhận.

Lịch sử: thu gọn theo bài, mặc định kết quả hiện tại; có bộ lọc “Có nhận xét”.
Dữ liệu/cấu hình không đổi thì dùng lại phân tích thay vì tạo snapshot trùng.
Khóa dùng lại cần xét source/outcomes/suite/k/phiên bản thuật toán. Khi có dữ liệu
mới, nhận xét cũ vẫn gắn bằng chứng cũ; không chuyển nhãn sang nhóm khác chỉ vì cùng ID.
Đây là thay đổi luồng lưu trữ/API, không thể giải quyết chỉ bằng CSS.

## Cỡ chữ và chế độ trình chiếu

- Nội dung 16 px; nhãn/phụ 14 px; tiêu đề bài 24–28 px; code/luật 15–16 px.
- Cỡ chữ dựa trên rem, nút chính cao khoảng 44 px, line-height 1.5–1.65.
- Thêm “Cỡ chữ: Thường / Lớn” (ví dụ tăng 16 lên 18 px), lưu lựa chọn trình duyệt.
- Màn 1366 px và trình duyệt zoom 125% không được tràn ngang ở nội dung chính.
  Code dài có vùng cuộn riêng. Không yêu cầu người dùng phải có màn hình lớn hơn.
- Chế độ xem code rộng/toàn màn hình có nút đóng và thao tác bàn phím rõ ràng.

## Thứ tự thực hiện và nghiệm thu

1. Bỏ slogan, giảm tầng tiêu đề, tăng chữ, thu gọn thống kê và form nhận xét.
2. Tách danh sách/chi tiết bài; lịch sử theo bài; mở nhanh nhận xét hiện tại.
3. Dùng lại phân tích không đổi, đánh dấu có dữ liệu mới và quản lý nháp nhận xét.

Tiêu chí: ở 1366×768 thấy được sáu bài với nút mở mà không bị lời dẫn lấn chỗ;
mở bài và tới luật/bằng chứng trong tối đa hai thao tác; xem nhận xét từ đúng bài
mà không dò hàng chục báo cáo; chữ không nhỏ hơn thiết kế nêu trên; vẫn phân biệt
luật máy học với luật cục bộ và giả thuyết với kết luận đã xác thực.

## Kết quả triển khai

- Bảng sáu bài riêng với phân tích; bỏ các slogan giảng viên và header.
- Nội dung 16 px, có nút Chữ lớn 18 px lưu trên trình duyệt; code mở rộng được.
- Ghi chú tùy chọn, nháp theo tài khoản/báo cáo/nhóm được lưu local. Ghi chú đã lưu
  trên hệ thống hiện ngay tại nhóm và có lối mở từ danh sách bài.
- History theo bài chỉ hiển thị bản mới nhất và mọi bản có ghi chú, có bộ lọc.
  Không xóa database hay mất đường dẫn tới báo cáo cũ. Không gắn nhận xét cũ vào cụm mới.
- Phân tích dùng lại snapshot khi problem/suite, bài nộp, k, tài khoản/phạm vi người dùng
  và fingerprint implementation không đổi. Lock trong service tránh tạo trùng khi bấm đồng thời.
- 261 tests + 3 subtests pass; 13 test Docker được skip trong suite offline.
  Chromium trên bản sao SQLite kiểm tra ghi chú/nháp, cache, navigation, escape bằng
  renderer hiện có và cỡ chữ lớn. Sáu dòng bài kết thúc ở y≈731 trên viewport 1366×768.
  Kiểm tra viewport 1093 px tương đương vùng CSS khi zoom 125% không tràn ngang trang.
- Bằng chứng local: `.cache/compact-ui-verification-20260929/`.
  Chạy thử ghi chú chỉ trên bản sao, không thêm nhận xét giả vào lớp đang dùng.

Báo cáo 0 ghi chú: cần giữ bản hiện tại để xem lại phân tích và tạo ghi chú sau đó;
không cần phô bày mọi snapshot trung gian. Bản trung gian cũ hiện được ẩn, không xóa.
