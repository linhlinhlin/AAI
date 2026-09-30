# Sửa dấu hiệu lỗi trong app — 29/09/2026

## Nguyên nhân

- Cụm unsupervised không tương đương một loại lỗi. Năm bài demo in các hằng 0, 1, 3, 15, 5050 có kết quả test khác nhau nên thuộc nhiều cụm. Với k=3, nhóm đầu còn chứa ba bài dùng n, n*n, n*(n-1)/2; trước đây chỉ hiển thị dấu hiệu in 0 của một bài.
- Luật cục bộ chỉ có bốn mẫu; bộ nhận diện if/else đường tròn chỉ hiểu câu tiếng Anh dài, bỏ sót INSIDE/ON/OUTSIDE. Luật trình bày yêu cầu nguyên output xuất hiện trong string literal, bỏ sót printf có biến.
- Thư viện lab02-ex03 thuộc C-Pack-IPAs, không phải dữ liệu của bài demo. Khớp 35/35 không phải nhãn cho nhóm bài đang luyện tập.

## Thay đổi

- Hiển thị tỷ lệ trượt từng test, đối chiếu đầu ra từng bài, độ phủ toàn nhóm/một phần nhóm, giá trị in cứng và danh sách bài chưa chẩn đoán.
- Sửa hai giới hạn nhận diện trên; bổ sung giả thuyết có điều kiện code/log cho các bài demo: ba biểu thức tổng sai, đếm cả số 0, khởi tạo max bằng 0, bỏ phần tử cuối, so sánh bình phương khoảng cách với bán kính.
- Luật riêng của bài demo được chặn bằng problem ID và đối chiếu input/expected/actual; không áp sang mã đề C-Pack. Các mẫu AST hiện vẫn hẹp, không phải bộ chứng minh chương trình tổng quát.
- Bản báo cáo cũ khi mở được tính lại chẩn đoán từ code/log lưu sẵn. Không sửa payload lịch sử, assignments, split hay luật quy nạp; không chạy lại mã C.
- Không đổi nhãn gold, không đưa chẩn đoán vào features clustering, không báo cáo độ chính xác misconception từ các kiểm tra này.

## Kiểm chứng

- harness check: 285 passed, 13 skipped (Docker opt-in), 3 subtests passed; ruff đạt.
- Kiểm tra trình duyệt ở sum-range k=2/k=3; max-array, count-positive, circle-position, swap k=2. Không lỗi JavaScript.
- Minh chứng cục bộ: .cache/cluster-signs-qa/verification.json và sum-k2.png, sum-k3.png.
- Kết quả là kiểm tra phần mềm và bằng chứng demo, không phải đánh giá độc lập trên gold/holdout. Những bài chưa có luật vẫn hiện bằng chứng test và trạng thái chưa xác định nguyên nhân.
