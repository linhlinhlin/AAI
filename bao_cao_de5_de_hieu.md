# Đề 5: chúng ta đang làm gì, dùng mô hình nào?

Cập nhật triển khai: **27/09/2026**. Khảo sát tài liệu đang giữ mốc
**26/09/2026**. Báo cáo này mô tả mã và kết quả đã có, không bổ sung tuyên bố SOTA.

## Giải thích như kể chuyện cho trẻ nhỏ

Tưởng tượng cả lớp đang dạy những con robot biết đếm. Một số robot đếm sai.
Thầy cô có rất nhiều bài nên khó nhìn từng bài ngay lập tức.

Ứng dụng của chúng ta làm bốn việc:

1. Cho robot thử vài câu hỏi nhỏ, ghi lại nó trả lời gì.
2. Nhìn thêm cách robot được hướng dẫn trong chương trình.
3. Đặt những bài có dấu hiệu giống nhau vào cùng một “rổ”.
4. Đưa cho thầy cô vài bài tiêu biểu và nói rõ vì sao chúng được xếp chung,
   để thầy cô quyết định nên giảng lại điều gì.

Một rổ chưa có nghĩa mọi bạn đều nghĩ sai giống nhau. Máy nhìn thấy bài làm,
không đọc được suy nghĩ của người viết. Khi chưa đủ bằng chứng, máy phải nói
“chưa biết”.

## Tên hướng nghiên cứu

**Khám phá cơ chế lỗi lập trình C dựa trên bằng chứng, với phân cụm không giám
sát và luật giải thích hỗ trợ giảng dạy.**

Đề 5 dùng tên *Misconceptions Clustering*. Nhóm thực hiện đúng chuỗi kỹ thuật
đó, đồng thời phân biệt ba mức: dấu hiệu sai quan sát được → cơ chế lỗi cần
kiểm chứng → quan niệm sai của người học cần bằng chứng bổ sung.

Câu hỏi nghiên cứu chính: **Hai bài cùng trượt một số test có thật sự mắc cùng
một cơ chế lỗi không? Thêm đầu ra cụ thể, quan hệ trong code và các lần thử có
kiểm chứng có giúp phân biệt chúng tốt hơn không, với cùng chi phí?**

Ví dụ minh họa: hai bài cùng tính sai tổng. Một bài bỏ mất số cuối cùng, bài
khác luôn in số 0. Chỉ ghi “sai” khiến chúng trông giống nhau. Nhìn output và
thử đầu vào phù hợp có thể giúp tách hai cách hỏng này. Đây là ví dụ giải thích,
không phải một kết quả đo mới trên dữ liệu nghiên cứu.

## Hiện dùng mô hình và kỹ thuật gì?

| Thành phần | Đang dùng trong mã | Hiểu đơn giản |
|---|---|---|
| Đọc code C | tree-sitter / tree-sitter-c; chỉ báo cú pháp AST | Nhìn bài có vòng lặp, rẽ nhánh và cấu trúc gì |
| Ghi bằng chứng | OAV, trạng thái từng test, mô tả chênh lệch expected/actual stdout | Làm một thẻ ghi “bài nào, dấu hiệu gì, giá trị bao nhiêu” |
| Mô hình phân cụm của app | **K-means**, biểu diễn one-hot có trọng số | Xếp các thẻ giống nhau vào cùng rổ |
| Mô hình tạo luật | **DecisionTreeClassifier**, sâu tối đa 3, lá tối thiểu 2 mẫu | Viết những câu NẾU… THÌ… giải thích việc xếp rổ |
| Bài đại diện | Medoid theo weighted Hamming | Chọn một bài thật tiêu biểu cho mỗi rổ |
| Đối chứng nghiên cứu | Exact test signatures; Agglomerative average linkage + weighted Hamming; K-means | So sánh các cách xếp rổ trên cùng dữ liệu |
| Phản hồi | Bằng chứng từng test, bộ luật cơ chế viết tay có dẫn chứng, giảng viên duyệt | Đưa gợi ý kiểm tra và nội dung giảng lại |
| Thực thi app | GCC C17 trong Docker Linux có hạn mức; SQLite lưu lịch sử | Cho chạy bài trong một hộp riêng rồi giữ lại kết quả |

Thư viện học máy được khóa ở **scikit-learn 1.9.1** trong
`requirements-lock.txt`. Đây là học máy cổ điển, không phải mô hình ngôn ngữ
lớn đã được huấn luyện sẵn. App hiện **không cần ChatGPT, Claude, Gemini, API
key hoặc GPU**. Không có checkpoint deep learning hay encoder nào đã được
nhóm huấn luyện cho kết quả đang báo cáo.

Bàn nghiên cứu cũ có tích hợp tùy chọn API LLM để đề xuất tên cụm. Phần này
khác app học viên và không phải thuật toán phân cụm. Chưa có lần gọi LLM thực
tế được xác nhận trong bộ nghiệm thu hiện tại; không báo cáo một tên model API
như mô hình đã chạy cho các kết quả này. Công cụ AI hỗ trợ viết phần mềm cũng
không phải mô hình mà sản phẩm dùng để phân tích bài nộp.

## Chi tiết đủ để trả lời khi thầy hỏi

- **OAV:** Object là bài nộp, Attribute là một đặc trưng, Value là giá trị.
  Ví dụ minh họa: `(bài_07, test_1, fail)`. Bộ `combined_stdout` kết hợp kết quả
  test, chỉ báo AST và mô tả stdout. Không đưa tên sinh viên/nhãn giảng viên vào
  feature để máy học thuộc người hoặc đáp án.
- **K-means trong app:** `n_init=10`, seed 42; giao diện cho chọn k=2 hoặc 3.
  Fit trên phần xây dựng, giữ lại khoảng 25% theo nhóm sinh viên/source để
  kiểm tra. Nếu không đủ mẫu hoặc đặc trưng khác nhau thì không ép tạo cụm.
- **Biểu diễn:** category được one-hot và có trọng số. Khi cả ba nhóm feature
  đều có mặt, cấu hình mặc định phân khối lượng 48% test, 12% AST, 40% stdout.
  Feature AST/stdout không thay đổi trên train bị bỏ; nếu một nhóm vắng thì
  trọng số thực tế được điều chỉnh theo mã, không mặc định ba nhóm luôn có.
- **Gán bài giữ lại:** dùng medoid của train gần nhất theo weighted Hamming
  cho mọi phương pháp, kể cả K-means. Đây là chính sách gán cố định của pipeline,
  không gọi là phép dự đoán nearest-centroid gốc của K-means.
- **Luật:** cây quyết định học dự đoán **ID cụm**. Vì vậy phân cụm là không
  giám sát, còn cây giải thích là học có giám sát từ ID cụm. ILA không được gọi
  là thuật toán phân cụm; bản đang chạy dùng cây quyết định cho bước sinh luật.
- **Luật viết tay:** giúp nêu giả thuyết cơ chế và gợi ý kiểm tra; được tách
  với luật cây giải thích cụm. Cả hai không tự trở thành nhãn chuyên gia độc lập.

Mã đối chiếu: `src/misconceptions/pipeline.py`, `features.py`,
`output_features.py`, `semantic_rules.py`, `learning_service.py` trong
`misconceptions-prototype`. Luồng đầy đủ và nguồn yêu cầu nằm trong
[hợp đồng đề 5](topic5-contract.md).

## Dữ liệu và kết quả đã có

Nhóm tự tìm dữ liệu; không chờ bộ dữ liệu giảng viên.

| Nội dung | Kết quả đã ghi nhận |
|---|---|
| C-Pack-IPAs-26 | 8.607 lần nộp, 246 ID sinh viên ẩn danh, 25 bài tập |
| Đủ điều kiện baseline lỗi hiện tại | 2.392 lần nộp; các trường hợp khác được phân loại riêng |
| Chia C-Pack-IPAs | 6.088 train, 1.569 validation, 950 test giữ kín |
| Lượt thí nghiệm C-Pack-IPAs | 675 lượt: 624 có kết quả, 51 từ chối do không đủ điều kiện |
| Lượt thí nghiệm ITSP | 81 cấu hình có kết quả; dùng cho phát triển/thăm dò |
| Annotation chuyên gia thật hoàn tất | 0; chưa có gold độc lập để báo accuracy chẩn đoán |
| App học viên | 6 bài C17, tài khoản, chạy test thật, phản hồi, sửa bài, lịch sử |
| App giảng viên | Tổng quan lớp, OAV, cụm, luật, bài đại diện, lưu/mở lại nhận xét |
| Kiểm thử phần mềm bản app | 184 tests + 3 subtests; 27 research smoke; 14 checks Docker |

Một kiểm tra cấu hình Docker nằm trong cả suite offline và suite Docker,
không cộng các con số thành tổng tests độc lập. Các cấu hình benchmark cũng
không phải 756 mô hình SOTA hoặc 756 lần thử trên sinh viên mới.

Kiểm thử trình duyệt đã dùng chương trình/tài khoản do dự án tự viết: bài đầu
đạt 1/6 test, sau sửa đạt 6/6; lịch sử, phiên và review lưu được. Đây là bằng
chứng chức năng hoạt động, **không phải kết quả can thiệp học tập trên người**.
Ảnh, kết quả, hash nguồn và phạm vi ở [hồ sơ nghiệm thu](../research/learning-app/README.md).

Dữ liệu công khai hiện được phân tích từ log lịch sử. Runner mới đã chạy C do
dự án viết cho app/kiểm thử; chưa replay toàn bộ corpus sinh viên nghiên cứu.
Split nghiên cứu giữ các bài của cùng người và source trùng trong cùng nhóm.
ITSP thiếu ID người học nên không được tuyên bố độc lập theo sinh viên.

## Hướng bài báo tiếp theo

Đóng góp dự kiến tập trung vào **bằng chứng giúp phân biệt cơ chế lỗi**, không
chỉ làm giao diện hoặc đổi một model lớn hơn. Những việc dưới đây chưa hoàn tất:

1. Kiểm tra lại oracle và khả năng chạy của corpus bằng runner cách ly.
2. Bổ sung quan hệ trong code: biến nào là cùng một biến, giá trị được gán ở
   đâu và dùng ở đâu. AST hiện mới là các dấu hiệu có/không.
3. Thử sửa nhỏ có kiểm chứng và chọn test phân biệt các giả thuyết. Một bản sửa
   vượt vài test vẫn chưa đủ để kết luận người viết có một quan niệm sai cụ thể.
4. Tạo nhãn cơ chế từ chuyên gia độc lập, xử lý bất đồng, cho phép chưa rõ hoặc
   nhiều cơ chế. Review AI và review dashboard không thay thế việc này.
5. So sánh với baseline stdout, code embedding và cùng một LLM ở chế độ chỉ
   code/có log theo protocol đóng băng, cùng ngân sách và phạm vi trả lời.
   **Chưa chốt checkpoint encoder/LLM**; chưa thuê GPU cho phần đang báo cáo.

Thước đo chính dự kiến: máy ghép đúng bao nhiêu cặp cùng cơ chế
(precision/recall/F1), mức lỗi khi máy dám trả lời nhiều/ít hơn (risk–coverage),
chi phí, và khả năng làm việc với sinh viên/bài tập chưa thấy. Báo khoảng tin
cậy theo nhóm sinh viên. Silhouette chỉ đo cấu trúc cụm; fidelity chỉ đo cây
có bắt chước cách phân cụm được không. Hai số này không đo đọc đúng suy nghĩ.

Thí nghiệm đầy đủ được ghi rõ `proposal_not_executed` trong
[protocol](../research/protocol.json). Chưa được báo “vượt SOTA”, “chẩn đoán
quan niệm sai chính xác X%” hay “giúp sinh viên học tốt hơn X%”.

## Đoạn có thể gửi nguyên văn cho đồng nghiệp

Nhóm đang làm đề 5 Misconceptions Clustering, theo hướng tìm nhóm cơ chế lỗi
trong chương trình C từ bằng chứng test và code. Bản hiện tại dùng OAV kết hợp
kết quả test, AST và stdout; K-means để phân cụm; cây quyết định nông sinh luật
IF–THEN; giảng viên xem bằng chứng và duyệt nhận xét. App có đăng nhập học viên/
giảng viên, sáu bài C, chạy code trong Docker, lưu lịch sử và dashboard lớp.
Hiện chạy CPU, không cần LLM/API/GPU. Nhóm đã chạy baseline trên C-Pack-IPAs và
ITSP, nhưng chưa có nhãn chuyên gia độc lập nên chưa tuyên bố SOTA hay hiệu quả
học tập. Hướng bài báo tiếp theo là thêm quan hệ ngữ nghĩa và các lần thử/sửa
có kiểm chứng để tách những lỗi trông giống nhau, rồi đánh giá độc lập trên
dữ liệu chưa thấy với cùng ngân sách.
