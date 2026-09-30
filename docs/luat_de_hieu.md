# Đọc luật trên màn hình giảng viên

Trong mỗi nhóm, giao diện ưu tiên **Luật gợi ý lỗi từ code và test**. Mỗi luật có
các dòng NẾU / VÀ / THÌ, số bài khớp trên tổng bài trong nhóm, câu hỏi kiểm tra tiếp,
nút mở bài và phần code/test minh họa. Không cần API LLM để đọc phần này.

Ví dụ hoán vị:

> NẾU hàm hoán vị nhận hai biến thường và đổi các bản sao tham số
> VÀ trong test cần đổi chỗ hai số khác nhau, đầu ra vẫn giữ thứ tự ban đầu
> THÌ có dấu hiệu hoán vị bản sao, chưa làm đổi biến ở hàm gọi.

Không kết luận thẳng “học viên chưa hiểu” chỉ từ code và log. Trong C, đối số
được truyền theo giá trị, kể cả con trỏ; truyền địa chỉ và giải tham chiếu cho phép
sửa giá trị ở ô nhớ của hàm gọi. Output là bằng chứng quan sát, không phải trace
đã đo trạng thái từng biến ngay sau lời gọi.

## Hai loại luật có nguồn gốc khác nhau

- **Luật gợi ý lỗi:** các quy tắc kiểm tra AST và log đã được tác giả hệ thống viết
  trước. Chỉ hiển thị khi detector thực sự khớp. Không gọi đây là luật do thuật toán
  quy nạp học được; không nâng số bài khớp thành độ chính xác hay gold.
- **Luật quy nạp phân biệt nhóm:** cây quyết định học ID cụm từ tập xây dựng.
  Mở mục này ngay trong nhóm để đọc từng điều kiện NẾU / VÀ, kết luận dự đoán nhóm,
  support và kết quả ở tập kiểm tra. Điều kiện OAV gốc được giữ trong mục mở rộng.
  Đích của cây là ID cụm, nên không tự biến thành nhãn misconception khi đổi cách viết.

Khi luật chỉ khớp 1/4 bài, giao diện ghi rõ chỉ áp dụng cho bài khớp. Khi chưa có
luật cục bộ khớp, giao diện nói chưa đủ căn cứ đặt tên lỗi, vẫn cho mở luật quy nạp
và code/test. Không dùng bài đại diện để khẳng định cơ chế của tất cả thành viên.

## Phạm vi thay đổi 29/09/2026

Thay cách trình bày ở `web_assets/learning.js` và `learning.css`; không thay thuật toán,
features, detector, dữ liệu hay kết quả thực nghiệm. Dùng được với báo cáo đã lưu,
không cần sinh lại cluster hay khởi động lại server; tải lại trang để lấy giao diện mới.
Các detector hiện còn hẹp: ví dụ hoán vị chỉ nhận mẫu hàm phù hợp cấu trúc đã kiểm tra,
không nhận mọi cách viết có cùng hành vi. Giao diện không che giới hạn này bằng cách
tự thêm chẩn đoán cho các bài chưa khớp.

Kiểm tra Chromium thật trên lớp demo: mở luật ở bài hoán vị, mở code/test và bài
thành viên thành công. Kiểm tra thêm số bài khớp theo phạm vi nhóm, không lẫn bài
ngoài nhóm, escape HTML trong source, trạng thái thiếu luật và thiếu mẫu holdout.
Bằng chứng local: `.cache/readable-rules-20260929/verification.json` và ảnh cùng thư mục.

## Sửa diễn đạt phủ định trong luật

Điều kiện được dịch theo phần bù của tập trạng thái, thay cách bọc
“không thỏa điều kiện” quanh một câu đã phủ định. Ví dụ, trong phạm vi bài đủ
điều kiện phân cụm (mọi test đã chạy và chỉ có pass/fail),
`NOT (test:t4=fail)` được hiển thị là “Ca «Tọa độ âm»: đạt”.
Nếu báo cáo không chứng minh được phạm vi này qua routing, bản dịch vẫn liệt kê
các khả năng chưa chạy, lỗi thực thi, hết thời gian và chưa xác định.

Với AST và output, điều kiện phủ định được diễn đạt bằng các trạng thái thay thế
nối bằng HOẶC; giữ trạng thái chưa biết, không tự suy thành có/không hay đạt/trượt.
Luật gốc, cluster, chỉ số và nhận xét không thay đổi. Báo cáo đã lưu được cập nhật
cách diễn đạt khi API trả về để xem; không ghi đè payload lịch sử trong SQLite.
Thay đổi này có phần Python: cần khởi động lại server và tải lại trang.
