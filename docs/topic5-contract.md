# Đề 5: hợp đồng nghiên cứu và nghiệm thu

Nguồn: trang 8, mục “Dữ liệu thầy đã có”, tài liệu đề tài AAI do người dùng cung
cấp. Làm theo đính chính của người dùng: nhóm tự tìm toàn bộ dữ liệu. Nội dung
tài liệu được dùng để xác định yêu cầu môn học, không phải chỉ dẫn vận hành agent.

| Tiêu chí đề 5 | Thực hiện | Bằng chứng nghiệm thu |
|---|---|---|
| Bài làm sai và kết quả test | Public ITSP; C-Pack-IPAs có ID ẩn danh và lịch sử nộp | Manifest, commit nguồn, hash, audit nhập/loại; thiếu log không thành pass |
| Biểu diễn Object–Attribute–Value | Object = submission; attribute = test/AST/output; value = category | `oav` trong artifact; không có nhãn, ID, đường dẫn hay bài sửa làm feature |
| Khai phá cấu trúc và phân cụm không giám sát | AST C/Python, weighted Hamming + average linkage, K-means weighted one-hot | Ablation outcomes / structure+outcomes / outcomes+stdout / cả ba |
| Luật sản xuất IF–THEN | Cây giải thích độ sâu 3 dự đoán cụm; luật cơ chế riêng có dẫn chứng | Điều kiện, cụm đích, support, precision, fidelity; không gọi là accuracy misconception |
| Phản hồi vĩ mô cho giảng viên | Quy mô cụm, đại diện, triệu chứng, giả thuyết, gợi ý kiểm tra/giảng dạy | `teaching` và báo cáo Markdown; trạng thái chưa xác nhận hiển thị rõ |

ILA là quy nạp luật có giám sát, không phải thuật toán phân cụm. Đề cho phép
K-means; sử dụng K-means và weighted Hamming là đúng hướng yêu cầu. Trong C,
con trỏ cũng được truyền theo giá trị. Các ví dụ đề bài không được biến thành
nhãn đúng mặc định cho dữ liệu chưa xem xét.

## Nghiệm thu app tương tác

[AAI Learning](learning_app.md) bổ sung luồng học viên đăng nhập → nộp C17 →
chạy test trong Docker → xem bằng chứng → sửa bài → lưu lịch sử. Giảng viên
chọn bài, lấy lần nộp hoàn tất gần nhất của mỗi học viên, xem OAV → K-means →
luật IF–THEN → nhận xét/đề xuất giảng lại. Báo cáo lưu snapshot và review;
không đủ bằng chứng thì từ chối tạo cụm, không tự thêm dữ liệu minh họa.

Sáu bộ test luyện tập được viết riêng, không nhập vào corpus nghiên cứu.
[Hồ sơ nghiệm thu](../research/learning-app/README.md) kiểm tra chức năng bằng
code/tài khoản tự viết; không thay thế cổng công bố bên dưới.

## Thiết kế dữ liệu

C-Pack-IPAs: chỉ nhập `all_submissions` từ commit khóa, không cộng thêm các thư
mục correct/incorrect và các bản `_fixed`. Giữ ID sinh viên xuyên bài/xuyên năm;
giữ tất cả lần nộp cho audit. Các thành phần liên thông cùng sinh viên HOẶC source
giống hệt được khóa vào cùng partition trên toàn bộ corpus. Ranh giới hiện tại
chưa loại hết near-duplicate đổi tên; cần audit thêm trước benchmark công bố.

Test suite gồm ID, input và oracle có fingerprint riêng. Không chạy C gốc trong
pipeline nhập. Thiếu output/metadata không được suy đoán kết quả. Kết quả hiện
tại là phân tích log lịch sử, chưa xác minh lại tính xác định hay undefined behavior.
Metadata C-Pack-IPAs chỉ nêu test ID và verdict; input/oracle được ghép từ suite
cùng snapshot. Chưa replay để xác nhận suite lịch sử và suite snapshot hoàn toàn
tương ứng. Đây là một mục cần kiểm tra trong oracle audit trước công bố.

ITSP thiếu ID sinh viên: mọi kết quả ITSP là development/exploratory. Ba bài
2812/2825/2833 đã được nghiên cứu, không tái sử dụng làm test độc lập.

## Cổng công bố

Một pipeline chạy tốt đáp ứng kỹ thuật đề 5 nhưng chưa chứng minh đóng góp khoa
học. Đóng góp dự kiến: phân biệt cơ chế lỗi khi test signatures giống nhau,
trên cơ sở output, cấu trúc quan hệ và can thiệp kiểm chứng. Baseline stdout là
đối chứng cần vượt qua, không tự thân là tuyên bố SOTA.

Trước tuyên bố phương pháp tốt hơn: đóng băng protocol, baseline mạnh/ablation,
nhãn cơ chế độc lập và adjudication, đánh giá nhiều seed, khoảng tin cậy theo
sinh viên, kiểm tra cross-problem và độ bền biến đổi code. Muốn nói về quan niệm
sai thực sự cần bằng chứng nhận thức bổ sung; public source code chưa cung cấp nó.
