# Đối chiếu bản thảo với một bài Q1 (30/09/2026)

## Bài dùng để đối chiếu

- **Bài chính (Q1):** V. Zhang, B. Jeffries, I. Koprinska (2025). *A Machine Learning Approach for
  Predicting Student Progress in Online Programming Education.* International Journal of Artificial
  Intelligence in Education 35:3614–3644. doi:10.1007/s40593-025-00510-9. Truy cập mở, CC BY.
  IJAIED xếp Q1 theo SJR (Scimago).
- **Bài cùng chủ đề:** J. C. Paiva, J. P. Leal, Á. Figueira (2025). *Clustering source code from
  automated assessment of programming assignments.* International Journal of Data Science and
  Analytics 20:1581–1592. doi:10.1007/s41060-024-00554-5. Truy cập mở, CC BY. Chưa kiểm chứng
  xếp hạng Q của tạp chí này; chỉ dùng để xem cách trình bày chủ đề gom cụm mã.

PDF được lưu cục bộ ở `.cache/q1-papers/` (không commit).

## Bài Q1 được viết như thế nào

1. Mở đầu nêu khoảng trống rồi đánh số câu hỏi nghiên cứu. Phần Thảo luận trả lời lần lượt từng câu (Q1–Q4).
2. Có mục Data riêng mô tả từng nguồn dữ liệu, và mục phân tích khám phá (EDA) trước khi mô hình hóa.
3. Phương pháp tách thành đặc trưng, chọn đặc trưng, mô hình, cửa sổ dự đoán và cài đặt.
4. Kết quả trình bày bằng bảng có đủ các chỉ số, cộng hình theo từng khóa học.
5. Có đánh giá với giảng viên thật (Q4 của bài).
6. Có phần Declarations: tài trợ, xung đột lợi ích, đạo đức, dữ liệu.
7. Bản thân các hình không cầu kỳ (heatmap matplotlib mặc định, cây quyết định đơn giản). Chuẩn Q1
   nằm ở lập luận và bằng chứng, không nằm ở hiệu ứng.

## Khoảng cách của bản thảo cũ và cách đã sửa

| Khoảng cách | Đã sửa |
|---|---|
| Bốn câu hỏi viết lẫn trong đoạn văn | RQ1–RQ4 đánh số, mỗi RQ gắn giả thuyết đã đăng ký; phần Kết quả xếp theo RQ |
| Không có ví dụ mở đầu | Hình 1: ba bài thật cùng bài tập, cùng trượt 4/4 test, ba bản sửa tối thiểu thuộc ba cơ chế (78/89 bài sai của bài tập này cùng chữ ký) |
| Không có sơ đồ tổng quan | Hình 2: nhãn đánh giá, biểu diễn, bốn RQ và công cụ |
| Luồng dữ liệu chỉ viết bằng lời | Hình 3: sơ đồ luồng kiểu CONSORT, đủ mọi bước loại trừ và số lượng (750 → 746 → 339; 4.350 → 3.320) |
| Quy trình gán nhãn khó theo dõi | Thuật toán 1 |
| OAV độ lệch chỉ mô tả bằng lời | Định nghĩa hình thức: $x^{out}$, $d_k$, $\bar d_k$ (mode trên test trượt), trọng số $w_a$ và khoảng cách Hamming có trọng số (đúng như mã nguồn) |
| Chữ trong hình chỉ khoảng 6 pt vì vẽ 7,2 inch rồi thu nhỏ | Mọi hình vẽ đúng khổ in 390 pt, chữ 7–8,5 pt, font nhúng |
| Phân tích theo loại chỉ có bảng ở phụ lục | Hình 6: heatmap khôi phục theo loại và biểu diễn |
| Không có hình cho luật | Hình 7: macro-F1 kèm khoảng bootstrap; ghi rõ CART nhỉnh hơn ILA-2 ở bài chưa thấy |
| Không có phần ứng dụng cho giáo viên | Mục 6.1 và Hình 8: AAI Lab, thiết kế rút ra từ RQ1–RQ3, ghi rõ chưa đánh giá với giảng viên |
| Thiếu Highlights, Graphical abstract, Declarations | Đã thêm: dữ liệu và mã, đạo đức, tuyên bố dùng AI theo mẫu Elsevier, xung đột lợi ích |
| "Holm p = 0.0000" | Ghi "p < 0,0001" |
| Tiêu đề đoạn bị hai dấu chấm (lớp elsarticle tự thêm dấu chấm) | Bỏ dấu chấm trong mã nguồn |

## Chuẩn hình đã áp dụng

- Mọi số liệu trong hình đọc từ artifact đã commit (`paper/make_figures.py`), không gõ tay.
- Vẽ đúng khổ in, không co giãn trong LaTeX. Script tự kiểm tra chữ không tràn khung hay ra ngoài hình.
- Một màu chàm cho biểu diễn đề xuất, xám cho baseline. Bảng màu đã qua bộ kiểm định của skill
  `dataviz` (phân biệt được với người mù màu), và mọi điểm dữ liệu đều có nhãn số.
- Khoảng tin cậy bootstrap 95% trên mọi biểu đồ số liệu. Trục tick đúng giá trị, không làm tròn gây hiểu sai.

## Việc còn lại trước khi nộp (nhóm tác giả)

1. Audit nhãn độc lập bởi hai người am hiểu C (hiện do AI thực hiện).
2. Trang tiêu đề riêng: tác giả, CRediT, tài trợ, lời cảm ơn (bản thảo để ẩn danh).
3. Xác nhận câu tuyên bố xung đột lợi ích và tuyên bố dùng AI.
4. Chọn tạp chí cuối cùng và định dạng lại theo hướng dẫn tác giả. Mẫu hiện tại theo Computers and
   Education: Artificial Intelligence.
5. Nếu có thể: một nghiên cứu nhỏ với giảng viên dùng AAI Lab, tương tự Q4 của bài đối chiếu.
