# Phân cụm các biểu hiện lỗi trong bài lập trình

BÁO CÁO MÔN HỌC AAI

Đề 5  Misconceptions Clustering

Từ bằng chứng kiểm thử đến nhóm lỗi và phản hồi giảng dạy

Phiên bản phục vụ nghiệm thu

Ngày 28 tháng 9 năm 2026

Báo cáo trình bày bài toán, thiết kế phương pháp, ứng dụng AAI Learning, kết quả đã kiểm chứng và kịch bản trình diễn. Phạm vi kết luận dựa trên hồ sơ của dự án tại thời điểm lập báo cáo. Các tài khoản và chương trình trong demo là dữ liệu do dự án tự tạo; không phải một thực nghiệm can thiệp trên lớp học thật.

Kho mã tham chiếu  github.com/linhlinhlin/AAI

---PAGE---

# Mục lục và cách đọc báo cáo

| Nội dung | Trang |
| Tóm tắt và phạm vi nghiệm thu | 3 |
| Chương 1 Tổng quan và giới thiệu bài toán | 4–6 |
| Chương 2 Khảo sát và thu thập dữ liệu | 7–9 |
| Chương 3 Phân tích và thiết kế hệ thống | 10–20 |
| 3.1 Kiến trúc và 3.2 đến 3.4 Biểu diễn đặc trưng | 10–13 |
| 3.5 đến 3.7 Phân cụm và luật giải thích | 14–16 |
| 3.8 đến 3.11 Phản hồi và ứng dụng | 17–20 |
| Chương 4 Demo và đánh giá kết quả | 21–26 |
| 4.1 đến 4.3 Kết quả và kiểm chứng | 21–23 |
| 4.4 đến 4.6 Hướng dẫn chạy và trình diễn | 24–26 |
| Chương 5 Kết luận và hướng phát triển | 27–28 |
| 5.1 Hạn chế và 5.2 Hướng phát triển | 27–28 |
| Tài liệu tham khảo | 29 |
| Phụ lục thuật ngữ và câu hỏi bảo vệ | 30 |

Báo cáo gồm năm chương chính. Chương 1 xác định bài toán và yêu cầu; Chương 2 trình bày nguồn dữ liệu và cách thu thập có kiểm toán; Chương 3 giải thích thiết kế; Chương 4 trình bày kết quả cùng kịch bản demo; Chương 5 nêu kết luận, hạn chế và hướng phát triển. Tóm tắt, tài liệu tham khảo và phụ lục nằm ngoài năm chương.

Người đọc muốn hiểu nhanh có thể xem ví dụ OAV tại trang 11 và kịch bản demo tại trang 24–26. Các trích dẫn [1]–[8] được liệt kê ở trang 29; đường dẫn tương đối được tính từ thư mục gốc gói bàn giao AAI.

“Đã thực hiện” chỉ nội dung có hồ sơ kiểm chứng; “minh họa” chỉ ví dụ giải thích hoặc kiểm thử; “đề xuất” chỉ công việc chưa hoàn tất. Kết quả nghiên cứu và kiểm chứng phần mềm được giữ rõ phạm vi.


---PAGE---

# Tóm tắt và phạm vi nghiệm thu

Đề tài xây dựng một quy trình hỗ trợ giảng viên nhìn ra các nhóm biểu hiện lỗi trong bài lập trình. Đầu vào là bài nộp và bằng chứng kiểm thử. Hệ thống chuyển dữ liệu sang biểu diễn Object–Attribute–Value, phân cụm các bài sai, sinh luật IF–THEN giải thích việc chia nhóm và trình bày các dẫn chứng để giảng viên quyết định nội dung cần giảng lại. Chuỗi kỹ thuật này bám theo yêu cầu đề 5 của môn học AAI. [1]

Sản phẩm gồm hai phần bổ trợ nhau. Phần nghiên cứu offline xử lý dữ liệu lập trình công khai và lưu dấu vết để tái lập thí nghiệm. Phần AAI Learning cho phép học viên nộp chương trình C17, nhận kết quả từng test, sửa bài và lưu lịch sử; giảng viên xem các nhóm lỗi, luật và nhận xét đã lưu. Dữ liệu luyện tập của ứng dụng không được trộn vào corpus nghiên cứu hoặc tập test khóa kín.

Trên C-Pack-IPAs, dự án đã nhập 8.607 bài nộp từ 246 định danh sinh viên ẩn danh và 25 bài tập. Có 675 lượt chạy cấu hình baseline, gồm 624 lượt tạo được kết quả và 51 lượt từ chối phân cụm khi dữ liệu không đủ điều kiện. Hồ sơ ITSP có 81 lượt trên ba bài development. Đây là bằng chứng về hoạt động của pipeline, chưa phải độ chính xác chẩn đoán quan niệm sai. [2]

Ứng dụng đã có kiểm chứng luồng trình duyệt và thực thi C trong Docker. Hồ sơ bổ sung Groq ghi nhận API gợi ý nhận xét trả HTTP 200; 193 kiểm thử offline và 3 kiểm thử con đạt ở phiên bản đó. Các gợi ý vẫn là bản nháp, được lưu riêng với nhận xét của giảng viên. [5][6]

Kết luận phù hợp cho nghiệm thu là hệ thống đã hiện thực hóa luồng từ bài sai đến phản hồi có bằng chứng. Chưa có nhãn chuyên gia độc lập hoàn tất, chưa đánh giá phương pháp trên sealed test và chưa đo hiệu quả học tập trong lớp thật. Do đó, báo cáo dùng cụm từ “biểu hiện lỗi” hoặc “giả thuyết quan niệm sai” khi bằng chứng chưa cho phép kết luận sâu hơn.

---PAGE---

# Chương 1 Tổng quan và giới thiệu bài toán

## 1.1 Bài toán và mục tiêu

Trong một lớp học lập trình, nhiều bài nộp có thể cùng không vượt qua bộ test nhưng sai theo những cách khác nhau. Với bài tính tổng từ 1 đến n, một chương trình luôn in 0, một chương trình in n và một chương trình tính n(n−1)/2 đều có thể trượt phần lớn test. Nếu chỉ nhìn điểm số, giảng viên khó biết nên giảng lại vòng lặp, điều kiện biên hay cách diễn giải yêu cầu.

Đề tài đặt câu hỏi thực dụng: có thể tự động gom các bài sai có đặc điểm gần nhau và đưa ra dẫn chứng để giảng viên đọc nhanh hơn không? Đầu ra cần giúp người dạy trả lời nhóm nào đang cần hỗ trợ, biểu hiện sai của nhóm là gì, các test nào thể hiện điều đó và nên dùng câu hỏi nào để kiểm tra cách hiểu của người học.

Mục tiêu kỹ thuật là tạo được chuỗi xử lý nhất quán từ nguồn dữ liệu đến phản hồi. Mỗi nhóm phải có bài đại diện và dấu vết quay lại source, test, OAV. Luật phải nêu điều kiện và nhóm dự đoán. Nhận xét cần tách dữ kiện quan sát được khỏi suy luận về nguyên nhân. Khi dữ liệu thiếu hoặc quá đồng nhất, hệ thống cần giải thích rằng chưa thể tạo cụm đáng tin cậy.

| Mục tiêu | Kết quả cần nhìn thấy |
| Chuẩn hóa bằng chứng | Biết test nào pass, fail hoặc chưa quan sát được |
| Phân nhóm không giám sát | Cụm hình thành từ đặc trưng, không từ nhãn giảng viên |
| Giải thích | Có luật, bài đại diện và nguồn bằng chứng |
| Hỗ trợ giảng dạy | Có nội dung giảng lại hoặc câu hỏi kiểm tra tiếp |

Mục tiêu môn học là hoàn thiện và chứng minh luồng kỹ thuật. Một mục tiêu nghiên cứu cao hơn là xác định cơ chế lỗi chính xác hoặc cải thiện việc học; hai mục tiêu này đòi hỏi đánh giá độc lập mà phiên bản hiện tại chưa có. Việc nêu giới hạn không làm giảm giá trị demo mà giúp xác định đúng phần đóng góp đã hoàn thành. [1][2]

---PAGE---

## 1.2 Các khái niệm cần phân biệt

Một kết quả test sai cho biết chương trình không đáp ứng kỳ vọng ở một đầu vào. Nó chưa cho biết tác giả chương trình đang tin điều gì. Báo cáo phân biệt triệu chứng, cơ chế lỗi và quan niệm sai để tránh suy diễn quá mức từ dữ liệu mã nguồn. Chẳng hạn, output luôn bằng 0 là triệu chứng; không cập nhật biến tổng là một cơ chế có thể kiểm tra trong source; hiểu rằng biến tự cộng dồn chỉ vì xuất hiện trong vòng lặp là một giả thuyết về nhận thức cần hỏi người học.

| Mức thông tin | Ví dụ trong bài tổng | Cách kiểm tra |
| Triệu chứng quan sát | n=2 nhưng actual=0, expected=3 | Đọc input và output |
| Cơ chế trong chương trình | Chương trình chỉ in hằng số | Đọc source và chạy test phù hợp |
| Giả thuyết quan niệm sai | Chưa hiểu ý nghĩa tích lũy | Yêu cầu giải thích hoặc dự đoán kết quả |

Phân cụm là học không giám sát: các bài được nhóm theo quan hệ tương đồng của đặc trưng. ID cụm không tự có ý nghĩa sư phạm và có thể đổi khi thay dữ liệu, seed hoặc số cụm. Đặt tên cho cụm là một bước diễn giải sau phân cụm, cần xem nhiều thành viên thay vì chỉ đọc một bài đại diện.

Luật IF–THEN trong dự án là lời giải thích cho cách phân cụm. Cây quyết định được huấn luyện có giám sát với nhãn đích là ID cụm đã tạo ra. Do đó, toàn bộ quy trình gồm một bước phân cụm không giám sát và một bước học mô hình giải thích có giám sát. ILA cũng là quy nạp luật có giám sát; dự án không gọi ILA là thuật toán phân cụm và không tuyên bố đã hiện thực ILA thay cho cây quyết định. [1]

Trong ví dụ bài con trỏ, cần diễn giải đúng ngôn ngữ C: đối số, kể cả con trỏ, đều được truyền theo giá trị. Truyền địa chỉ cho phép hàm sửa đối tượng được trỏ tới, nhưng không biến cơ chế truyền tham số của C thành truyền tham chiếu. Quy tắc này được giữ trong nội dung phản hồi để không tạo thêm quan niệm sai khi giải thích lỗi.

---PAGE---

## 1.3 Yêu cầu nghiệm thu của đề tài

Hợp đồng nghiệm thu trong dự án quy định năm mắt xích: bài làm sai và kết quả test, biểu diễn OAV, khai phá cấu trúc và phân cụm, luật sản xuất IF–THEN, phản hồi tổng hợp cho giảng viên. Dữ liệu được nhóm tự tìm từ nguồn công khai; không giả định có sẵn một bộ dữ liệu giáo viên đã gán nhãn. [1]

| Yêu cầu | Hiện thực trong dự án | Bằng chứng trình diễn |
| Bài sai và test | Adapter dữ liệu lịch sử và runner C17 cho bài mới | Source, input, expected, actual |
| Object–Attribute–Value | Giá trị phân loại từ test, AST và stdout | Bảng OAV của từng bài |
| Phân cụm | K-means trong app; thêm baseline offline | Thành viên và bài đại diện |
| IF–THEN | Cây giải thích độ sâu tối đa 3 | Điều kiện, support, fidelity |
| Phản hồi giảng viên | Nhận xét có căn cứ, nội dung giảng lại | Lưu, mở lại, xuất JSON |

Các chức năng đăng nhập, lưu tiến độ và giao diện học viên hỗ trợ việc trình diễn một quy trình hoàn chỉnh. Chúng không thay thế các yêu cầu cốt lõi về dữ liệu và phân cụm. Vai trò học viên và giảng viên giúp giới hạn ai được nộp bài, ai được xem lớp và ai được lưu nhận xét. Trong phạm vi môn học, đây là phần ứng dụng hóa kết quả thay vì một đóng góp thuật toán mới.

Điều kiện nghiệm thu nên được quan sát trực tiếp. Ví dụ, sau khi tạo báo cáo, người trình diễn mở một bài đại diện, chỉ ra OAV, đọc một luật, lưu nhận xét, tải lại trang và kiểm tra nội dung còn tồn tại. Chỉ có ảnh giao diện hoặc một file JSON không đủ để chứng minh toàn bộ luồng tương tác, nhưng chúng hữu ích để lưu hồ sơ sau khi luồng đã được chạy.

Một tiêu chí về tính trung thực là hệ thống không tự tạo sinh viên giả trong dữ liệu sử dụng thực tế khi thiếu mẫu. Dữ liệu minh họa nằm trong cơ sở dữ liệu demo riêng và mang tên DEMO. Khi mẫu thật không đủ, phần phân tích có thể từ chối phân cụm thay vì tạo một kết quả có vẻ hoàn chỉnh nhưng không có căn cứ.

---PAGE---

# Chương 2 Khảo sát và thu thập dữ liệu

## 2.1 Khảo sát nguồn và phạm vi thu thập

Nguồn chính của nghiên cứu là C-Pack-IPAs tại snapshot C-Pack-IPAs-26, commit 76901e1223b250a093a02d5e29113ad735c3d2b9. Dự án chỉ nhập các bản nộp gốc trong all_submissions. Những bản sao được tổ chức lại vào thư mục đúng hoặc sai và các file sửa hậu nghiệm có hậu tố _fixed không được cộng thêm thành quan sát mới. Lựa chọn này giảm đếm trùng và tránh dùng thông tin sửa lỗi của tương lai. [2][7]

| Thuộc tính corpus | Giá trị đã kiểm toán |
| Bài nộp | 8.607 |
| Định danh sinh viên ẩn danh | 246 |
| Bài tập | 25 |
| Cặp input và oracle | 106 |
| Đường nhập chính | all_submissions |

ID sinh viên được sử dụng để tổ chức chia tập, không phải đặc trưng đầu vào của mô hình. Việc có nhiều lần nộp của cùng một người cũng có nghĩa 8.607 bài không tương đương 8.607 quan sát độc lập về mặt thống kê. Khi đánh giá sâu hơn, cần tính sự phụ thuộc theo sinh viên thay vì chỉ tăng độ tin cậy bằng số lượng bản ghi.

ITSP được sử dụng làm nguồn development cho ba bài 2812, 2825 và 2833. Vì nguồn này thiếu định danh sinh viên và đã được xem trong quá trình thiết kế đặc trưng, các kết quả ITSP mang tính thăm dò. Không dùng chúng làm test độc lập để tuyên bố tổng quát hóa sang người học mới. [2]

Corpus công khai giúp đề tài có dữ liệu thật về chương trình và kết quả chấm, nhưng không cung cấp toàn bộ ngữ cảnh nhận thức. Một chương trình sai có thể do gõ nhầm, bỏ dở hoặc thử nghiệm tạm thời. Không có phỏng vấn hay câu trả lời giải thích đi kèm thì không thể suy ra chắc chắn người viết giữ một niềm tin sai cụ thể. Đây là giới hạn của nguồn dữ liệu, không thể khắc phục chỉ bằng cách tăng số cụm hoặc gọi một mô hình ngôn ngữ lớn hơn.

---PAGE---

## 2.2 Kiểm toán và phân tuyến dữ liệu

Trước khi phân cụm, dự án phân tuyến bài nộp theo chất lượng bằng chứng. Một bài chưa có đủ log không được coi là đã qua test; lỗi biên dịch hoặc lỗi parse cũng không tự được quy thành lỗi thuật toán. Phân tuyến bảo vệ ý nghĩa của các giá trị OAV và giúp người đọc biết mẫu nào thực sự tham gia baseline. [2]

| Trạng thái sau nhập | Số bài |
| Có failure và đủ điều kiện baseline | 2.392 |
| Không quan sát thấy failure | 3.600 |
| Thiếu bằng chứng hoặc chưa chạy đủ test | 2.136 |
| Lỗi thực thi hoặc vượt hạn mức | 267 |
| Parse error | 212 |
| Tổng | 8.607 |

Nhóm “không quan sát thấy failure” chỉ mô tả dữ liệu đang có. Nhóm “thiếu bằng chứng” không được gộp vào pass. Những trường hợp hệ thống chấm gặp Internal Error là chưa quan sát được kết quả. Nếu một bài accepted không lưu stdout, dự án giữ verdict pass nhưng không chép expected sang actual để làm như đã quan sát output.

Audit còn ghi nhận 193 output thuộc 61 submissions không phải UTF-8. Dữ liệu giữ hash byte gốc thay vì thay byte lỗi bằng ký tự giả rồi coi đó là nội dung ban đầu. Với output rất dài, phần so khớp có chi phí cao được đánh dấu not_computed_large_output khi vượt ngưỡng xử lý; trạng thái này chỉ nghĩa là chưa tính một đặc trưng, không phải một kiểu lỗi mới. [2]

Log lịch sử không phải bằng chứng rằng corpus đã được thực thi lại trong runner hiện tại. Input và oracle được ghép theo bộ test của cùng snapshot, nhưng chưa replay toàn bộ corpus để xác minh mọi liên hệ lịch sử hoặc hành vi không xác định của C. Một bước oracle audit có kiểm soát vẫn cần thực hiện trước khi mở rộng kết luận nghiên cứu. Trong demo, chỉ các chương trình do dự án viết mới được dùng để chứng minh runner hoạt động.

---PAGE---

## 2.3 Chia tập và ngăn rò rỉ thông tin

Nếu chia ngẫu nhiên từng bài nộp, source gần như giống nhau hoặc các lần sửa liên tiếp của cùng sinh viên có thể xuất hiện ở cả train và validation. Khi đó mô hình dường như tổng quát hóa tốt nhưng thực tế đã nhìn thấy thông tin liên quan. Dự án khóa nhóm trên toàn corpus trước khi tạo các cohort theo bài tập. [1][2]

Các bài được nối thành thành phần liên thông khi cùng sinh viên hoặc có source không rỗng giống hệt nhau. Toàn bộ một thành phần được đưa vào cùng partition. Source rỗng được giữ để kiểm toán nhưng không được dùng làm dấu hiệu rằng các sinh viên khác nhau sao chép cùng chương trình. ID và đường dẫn chỉ phục vụ truy vết, không được đưa vào vector đặc trưng.

| Partition | Bài nộp | Sinh viên | Thành phần liên thông |
| Train | 6.088 | 167 | 154 |
| Validation | 1.569 | 51 | 51 |
| Sealed test | 950 | 28 | 28 |
| Tổng | 8.607 | 246 | 233 |

Split hiện tại dùng seed 42 và tách theo sinh viên trên các bài tập đã thấy. Đây chưa phải thiết kế mà cả họ bài toán ở test đều mới. Sealed test chưa được dùng để fit, gán cụm hoặc chấm chỉ số phương pháp; kiểm tra schema và provenance khi nhập dữ liệu không đồng nghĩa đánh giá mô hình trên test.

Các bước chọn đặc trưng, bỏ cột hằng và học cây giải thích phải dựa trên train. Sau khi đã khóa thiết kế, validation mới được dùng để quan sát hành vi ngoài train. Bản nộp đúng về sau, file sửa, nhãn chuyên gia và nhận xét giáo viên đều không thuộc feature. Ranh giới còn thiếu là phát hiện near-duplicate có đổi tên biến hoặc biến đổi hình thức; exact duplicate hiện tại chưa giải quyết hết trường hợp đó.

Việc giữ sealed test là một lựa chọn đánh giá, không phải thiếu chức năng của demo. Ứng dụng có thể hoàn tất nghiệm thu kỹ thuật trong khi quy trình nghiên cứu vẫn chờ nhãn độc lập và protocol đủ ổn định trước đánh giá cuối.

---PAGE---

# Chương 3 Phân tích và thiết kế hệ thống

## 3.1 Kiến trúc và ranh giới dữ liệu

Kiến trúc có hai luồng dùng chung ý tưởng biểu diễn nhưng khác nguồn bằng chứng. Luồng nghiên cứu đọc source và log kiểm thử lịch sử từ corpus công khai. Luồng ứng dụng nhận source mới của người dùng và thực thi trong Docker có giới hạn. Hai luồng không được mô tả như cùng một loại thí nghiệm: log cũ là quan sát được ghi lại, còn kết quả runner là thực thi mới trong môi trường hiện tại.

| Tầng xử lý | Vai trò chính | Đầu ra |
| Thu nhận bằng chứng | Adapter corpus hoặc runner C17 | Bản ghi source và test |
| Chuẩn hóa | Giữ trạng thái thiếu, lỗi và kết quả hợp lệ | Dữ liệu kiểm toán được |
| Biểu diễn | Rút trích test, cấu trúc AST, stdout | OAV và vector trọng số |
| Phân tích | Phân cụm, chọn đại diện, học cây giải thích | Cụm và luật |
| Trình bày | Tổng hợp, gợi ý, nhận xét, lưu báo cáo | Dashboard và JSON |

Trong ứng dụng, SQLite lưu tài khoản, lịch sử nộp, báo cáo và nhận xét. Báo cáo giữ snapshot của kết quả phân tích để người dùng có thể mở lại cùng bằng chứng. Gợi ý AI có vùng lưu riêng, bao gồm thông tin nguồn và trạng thái nháp. Cách tổ chức này hỗ trợ truy vết câu hỏi “kết luận này dựa trên dữ liệu nào và ai đã xác nhận?”. [3][6]

Trong nghiên cứu, hồ sơ chạy lưu cấu hình, seed, fingerprint đầu vào, môi trường và snapshot mã. Việc bàn giao dưới dạng thư mục không có .git vẫn giữ được hash và snapshot; commit Git khi không xác định được phải để trống thay vì bịa một mã commit. Kết quả cũ được giữ nguyên, các lần chạy mới dùng thư mục riêng.

Một nguyên tắc xuyên suốt là chú thích của người đánh giá không quay ngược vào đặc trưng phân cụm. Nếu tên nhóm, nhận xét hoặc bản sửa đúng được dùng làm feature, hệ thống có thể “học” chính thông tin cần đánh giá. Ranh giới này được giữ cả ở thiết kế corpus và ở luồng AI của ứng dụng.

---PAGE---

## 3.2 Biểu diễn Object Attribute Value

OAV là cách tổ chức mỗi bài nộp thành các quan sát có tên. Object là một submission; Attribute là đặc điểm được đo; Value là giá trị phân loại của đặc điểm đó. Cấu trúc này giúp người đọc lần từ vector máy học về bằng chứng gốc, thay vì chỉ nhìn một dãy số khó hiểu.

Với ví dụ luôn in 0 trong bài tổng từ 1 đến n, các thuộc tính có thể mô tả kết quả test, sự có mặt của vòng lặp và quan hệ giữa actual với expected. Bảng sau minh họa ý nghĩa OAV; tên thuộc tính cụ thể trong artifact được giữ theo extractor của dự án.

| Object | Attribute | Value minh họa | Căn cứ |
| Bài A | Test n=0 | pass | Actual và expected đều là 0 |
| Bài A | Test n=2 | fail | Actual=0, expected=3 |
| Bài A | Có vòng lặp | không | Source chỉ đọc n và in 0 |
| Bài A | Kiểu sai khác output | khác giá trị | Token output không khớp |

Một giá trị fail là quan sát về chương trình. Giá trị “có vòng lặp” là quan sát cú pháp. Không có cột nào trong ví dụ mang giá trị “sinh viên không hiểu vòng lặp”, vì đó là kết luận cần kiểm chứng chứ không phải dữ kiện trực tiếp. Nhãn do giảng viên hoặc AI viết được lưu ở tầng phản hồi sau phân cụm.

Các giá trị thiếu được biểu diễn tường minh. Không quan sát output khác với output rỗng đã quan sát; not_run khác với fail. Nếu các trường hợp này bị ép về một giá trị chung, khoảng cách có thể phản ánh cách thu thập dữ liệu thay vì hành vi của chương trình. Vì vậy, chuẩn hóa trạng thái là bước cần thiết trước khi áp dụng thuật toán.

OAV cũng giúp minh họa tính không hoàn hảo của biểu diễn. Hai chương trình có thể cùng trượt các test và cùng không có vòng lặp nhưng vẫn sai theo cơ chế khác nhau. Thêm đặc trưng stdout hoặc cấu trúc có thể phân biệt thêm một số trường hợp, song không bảo đảm rằng mọi chương trình cùng OAV có cùng quan niệm sai. [1][2]

---PAGE---

## 3.3 Đặc trưng từ test và cấu trúc mã

Nhóm đặc trưng test ghi lại kết quả ở từng ca kiểm thử. Đây là nguồn thông tin gần với yêu cầu bài toán vì oracle xác định output mong đợi cho input cụ thể. Tuy nhiên, một chữ ký pass/fail chỉ cho biết vị trí chương trình bị phát hiện sai trong bộ test đang có. Hai cơ chế khác nhau có thể tạo cùng chữ ký nếu bộ test chưa đủ khả năng phân biệt.

Nhóm đặc trưng cấu trúc được rút trích bằng tree-sitter và parser C. AST tổ chức các thành phần cú pháp của source, cho phép phát hiện sự có mặt của những cấu trúc như vòng lặp hoặc nhánh điều kiện. Phiên bản baseline hiện tại chủ yếu dùng chỉ báo sự hiện diện cú pháp; chưa có biểu diễn đầy đủ quan hệ định nghĩa–sử dụng hoặc liên kết biến. [2]

| Nguồn đặc trưng | Câu hỏi trả lời được | Giới hạn |
| Kết quả test | Chương trình sai ở đầu vào nào | Phụ thuộc độ phủ bộ test |
| AST presence | Có cấu trúc cú pháp nào xuất hiện | Không mô tả đầy đủ luồng dữ liệu |
| Kết hợp test và AST | Bài có biểu hiện và hình thức gần nhau không | Chưa trực tiếp xác định nguyên nhân |

Sự có mặt của vòng lặp không chứng minh phép tính đúng. Ngược lại, không có vòng lặp cũng không chứng minh chương trình sai: công thức n(n+1)/2 có thể giải bài tổng mà không lặp. Vì vậy, phản hồi phải luôn đặt đặc trưng cú pháp bên cạnh yêu cầu bài toán và kết quả test. Giảng viên cần xem source trước khi biến một thuộc tính thành kết luận sư phạm.

Các thuộc tính train không thay đổi giữa mọi bài không giúp phân biệt trong cohort đó. Dự án loại các cột hằng thuộc khối AST và stdout dựa trên train, rồi sử dụng quy tắc đã fit cho dữ liệu giữ lại. Nếu nhìn cả holdout để quyết định cột nào hữu ích, thông tin đánh giá sẽ ảnh hưởng thiết kế biểu diễn. Quy tắc fit trên train giữ rõ vai trò của từng tập.

---PAGE---

## 3.4 Đặc trưng stdout và trọng số

Stdout bổ sung thông tin mà một verdict fail có thể bỏ qua. Chẳng hạn, khác chữ trong thông báo và chọn nhầm nhánh đều có thể khiến test fail, nhưng quan hệ giữa actual và expected không giống nhau. Dự án bổ sung nhóm đặc trưng mô tả output để đối chiếu với baseline chỉ dùng test và AST. Output gốc vẫn được giữ làm bằng chứng, thay vì chỉ giữ đặc trưng đã rút gọn. [2]

Trong cấu hình combined_stdout của ứng dụng, khi các khối đều có mặt, tổng trọng số được phân bổ như bảng. Khi thiếu khối hoặc loại cột hằng, phần triển khai điều chỉnh theo các đặc trưng còn lại. Đây là cấu hình vận hành của baseline, chưa phải bộ trọng số được chứng minh tối ưu cho chẩn đoán.

| Khối | Tổng trọng số mặc định | Ý nghĩa |
| Test outcomes | 0,48 | Nhấn mạnh hành vi trên test |
| AST | 0,12 | Bổ sung dấu hiệu cấu trúc |
| Stdout | 0,40 | Bổ sung loại sai khác đầu ra |

Với các thuộc tính phân loại x và y, khoảng cách Hamming có trọng số cộng trọng số của thuộc tính có giá trị khác nhau. Nếu một thuộc tính có trọng số w, one-hot được nhân căn bậc hai của w/2. Hai giá trị khác nhau làm thay đổi hai vị trí one-hot, nên đóng góp vào bình phương khoảng cách Euclid là 2 × w/2 = w. Nhờ đó, cách mã hóa dùng cho K-means nhất quán với ý nghĩa khoảng cách đã chọn.

Ví dụ minh họa có hai thuộc tính trọng số 0,7 và 0,3. Hai bài chỉ khác thuộc tính thứ hai có khoảng cách 0,3; khác cả hai có khoảng cách 1,0. Con số nói về sự khác nhau trong biểu diễn, không phải xác suất hai sinh viên có quan niệm sai khác nhau.

Với output quá dài, một số phép tính similarity có thể tốn nhiều thời gian. Extractor đánh dấu trạng thái chưa tính khi vượt ngưỡng thay vì âm thầm bỏ dữ liệu hoặc suy ra một giá trị giả. Quyết định này giữ pipeline chạy có kiểm soát và làm rõ giới hạn của đặc trưng được sử dụng.

---PAGE---

## 3.5 Phân cụm không giám sát

Ứng dụng dùng K-means trên vector one-hot có trọng số. Người dùng chọn k bằng 2 hoặc 3; cấu hình app dùng seed 42 và n_init bằng 10. K-means tìm cách giảm tổng bình phương khoảng cách từ các điểm đến tâm cụm. Tâm là đối tượng toán học trong không gian vector, không nhất thiết là một chương trình có thật và không tự có tên lỗi dễ hiểu. [3]

Phần nghiên cứu offline đối chiếu thêm baseline nhóm theo chữ ký test chính xác và agglomerative clustering với average linkage trên khoảng cách Hamming có trọng số. Các biểu diễn gồm outcomes, combined, outcomes_stdout và combined_stdout. Đối chiếu nhiều cách biểu diễn giúp xem thay đổi đến từ nguồn đặc trưng hay từ thuật toán, thay vì gán toàn bộ kết quả cho K-means.

| Thành phần | Chức năng | Lưu ý diễn giải |
| K-means | Gom các vector gần nhau | k là tham số, không là số quan niệm sai thật |
| Exact signature | Nhóm bài có cùng chữ ký test | Baseline đơn giản để so sánh |
| Average linkage | Gom theo khoảng cách giữa nhóm | Phụ thuộc biểu diễn và quy tắc liên kết |
| Abstention | Không tạo kết quả khi thiếu điều kiện | Tránh ép chia nhóm vô nghĩa |

Một cụm có thể trộn nhiều cơ chế lỗi nếu đặc trưng hiện tại không phân biệt được chúng. Trong demo bài tổng, nhóm còn lại ngoài các chương trình in hằng có thể chứa chương trình in n, n² hoặc n(n−1)/2. Không nên đặt cho toàn nhóm một tên nguyên nhân quá cụ thể chỉ vì đã đọc một thành viên.

Số cụm nhỏ giúp giảng viên đọc tổng quan nhưng có thể gộp nhiều trường hợp. Số cụm lớn có thể làm nhóm nhỏ, thiếu support và khó giải thích. Hệ thống vì vậy cần hiển thị số mẫu và bằng chứng cùng với kết quả. Khi feature train giống hệt hoặc số mẫu phân biệt không đáp ứng k, việc từ chối phân cụm là hành vi đúng theo thiết kế, không phải một lỗi giao diện.

---PAGE---

## 3.6 Bài đại diện và dữ liệu giữ lại

Để giải thích một cụm bằng chương trình có thật, dự án dùng medoid: bài nằm gần các thành viên khác theo khoảng cách đã chọn. Medoid khác centroid của K-means. Giảng viên có thể mở source và test của medoid để bắt đầu xem xét, sau đó kiểm tra các bài còn lại để đánh giá mức đồng nhất về cơ chế.

Biểu diễn và cụm được fit trên train. Dữ liệu giữ lại được gán vào cụm theo medoid train gần nhất bằng Hamming có trọng số, áp dụng nhất quán cho các thuật toán trong pipeline. Vì vậy, không nên mô tả bước đánh giá của dự án là gọi K-means predict theo centroid nếu mã thực tế đang dùng medoid. [2][3]

| Đối tượng | Được học hoặc chọn từ đâu | Dùng để làm gì |
| Danh mục giá trị và cột hằng | Train | Cố định phép biến đổi dữ liệu |
| Cụm và medoid | Train | Tạo cấu trúc nhóm và bài đại diện |
| Cây giải thích | Train với ID cụm | Học các luật đơn giản |
| Holdout | Giữ ngoài bước fit | Quan sát gán cụm và fidelity ngoài train |

Trong app, holdout dự kiến khoảng một phần tư dữ liệu và phải tôn trọng nhóm sinh viên/source. Kích thước demo nhỏ nên mỗi thay đổi thành viên có thể làm kết quả biến động rõ. Các chỉ số cần được đọc cùng số mẫu thực tế, không chỉ nhìn một tỷ lệ phần trăm cao.

Ví dụ một luật có fidelity 100% trên một bài giữ lại chỉ cho biết cây và phép gán cụm đồng ý ở bài đó. Nó không tương đương 100% đúng trên sinh viên mới hoặc trên cơ chế lỗi. Để so sánh phương pháp nghiêm túc, cần tập đánh giá đủ lớn, nhiều seed và nhãn cơ chế độc lập.

Bài đại diện cũng không thay thế toàn bộ bằng chứng khi gọi AI. Phiên bản gợi ý lấy tối đa bốn mẫu, gồm đại diện và các OAV khác biệt, nhằm giảm việc chỉ nhìn một trường hợp. Đây vẫn là lấy mẫu có giới hạn; phần không được gửi có thể chứa ngoại lệ mà giảng viên cần kiểm tra khi duyệt nhận xét.

---PAGE---

## 3.7 Luật IF THEN và các chỉ số

Sau phân cụm, dự án dùng DecisionTreeClassifier với max_depth bằng 3 và min_samples_leaf bằng 2 để học cách dự đoán ID cụm từ đặc trưng. Mỗi đường từ gốc đến lá có thể viết thành luật IF–THEN. Độ sâu nhỏ giúp luật đọc được, đổi lại cây có thể không biểu diễn hết ranh giới phức tạp của thuật toán phân cụm. [1][3]

Một luật minh họa có dạng: IF một tập điều kiện về test và output thỏa mãn THEN dự đoán cụm 1. Trong demo cần đọc đúng luật đang hiện trên màn hình, vì điều kiện và ID cụm có thể thay đổi theo dữ liệu. Không nên học thuộc một luật minh họa rồi trình bày như kết quả cố định của mọi lần chạy.

| Chỉ số | Câu hỏi mà chỉ số trả lời | Không chứng minh được |
| Support | Bao nhiêu mẫu thỏa điều kiện luật | Nhóm có cùng niềm tin sai |
| Precision theo ID cụm | Trong các mẫu luật bao phủ, tỷ lệ thuộc cụm đích là bao nhiêu | Nhãn cơ chế đã đúng |
| Fidelity | Cây đồng ý với mục tiêu gán cụm đến mức nào | Độ chính xác misconception |
| Silhouette | Các điểm gần nhóm mình hơn nhóm khác đến mức nào | Giá trị sư phạm của nhóm |

Hai biểu diễn khác nhau có thể tạo hai hệ thống cụm khác nhau. Vì vậy, fidelity 1,0 ở cấu hình này và 0,5 ở cấu hình khác không trực tiếp xếp hạng khả năng chẩn đoán: hai cây đang bắt chước hai mục tiêu khác nhau. Kết quả có thể phản ánh ranh giới cụm dễ hay khó diễn tả bằng cây nhỏ.

Luật hữu ích vì tạo một lời giải thích ngắn cho giảng viên và chỉ ra điều kiện cần kiểm tra. Khi luật bao phủ ít mẫu hoặc trái với source đã đọc, giảng viên nên giữ kết luận thận trọng. Kết hợp luật với bài đại diện, test và số lượng thành viên giúp tránh biến một phép tóm tắt thống kê thành khẳng định về nhận thức người học.

---PAGE---

## 3.8 Từ nhóm tự động đến nhận xét giảng viên

Báo cáo JSON đã có nhóm vì thuật toán đã gán mỗi bài vào một cluster. Tuy nhiên, ID cụm và danh sách thành viên chưa trả lời giảng viên nên dạy lại điều gì. Phần nhận xét bổ sung lớp diễn giải sư phạm: đặt tên theo hiện tượng, ghi căn cứ và đề xuất câu hỏi hoặc hoạt động kiểm tra tiếp. Hai lớp dữ liệu có mục đích khác nhau nên cùng cần được lưu. [3][6]

| Trường nhận xét | Cách điền phù hợp | Điều cần tránh |
| Tên nhóm | Mô tả biểu hiện có căn cứ | Gắn nhãn năng lực hoặc thái độ |
| Loại nhận định | Cơ chế quan sát hoặc giả thuyết chưa xác nhận | Gọi mọi lỗi là misconception |
| Căn cứ | Trỏ tới source và test cụ thể | Viết chung chung không có dẫn chứng |
| Nội dung giảng lại | Đề xuất câu hỏi kiểm tra và hướng giải | Khẳng định nguyên nhân chỉ từ một mẫu |

Với nhóm chương trình in hằng trong demo, một nhận xét phù hợp là “Các mẫu đã xem in số cố định thay vì tính tổng theo n”. Căn cứ là source và output ở n=2, n=5. Nội dung kiểm tra có thể yêu cầu người học liệt kê các số phải cộng, dự đoán kết quả cho hai đầu vào rồi giải thích biến tổng được cập nhật ra sao. Đây là cách chuyển triệu chứng thành hoạt động dạy học có thể quan sát.

Nếu nhóm chứa cả n, n² và n(n−1)/2, nhận xét cần rộng hơn hoặc ghi rõ các nhóm con. Có thể viết “Các mẫu dùng biểu thức chưa phù hợp với yêu cầu tổng” và liệt kê ngoại lệ. Không nên khẳng định toàn nhóm cùng thiếu vòng lặp, vì giải đúng bằng công thức không cần vòng lặp.

Nhận xét đã lưu là đánh giá của người dùng ứng dụng tại thời điểm đó. Nó có giá trị vận hành và truy vết nhưng chưa tự trở thành nhãn chuyên gia độc lập cho benchmark. Nếu muốn xây gold cơ chế, cần quy trình gán nhãn riêng, tiêu chí nhất quán, nhiều người đánh giá và xử lý bất đồng trước khi dùng để chấm phương pháp.

---PAGE---

## 3.9 Gợi ý nhận xét bằng mô hình ngôn ngữ

Nút Gợi ý nhận xét hỗ trợ soạn thảo sau khi cụm đã được tạo. Backend lấy mô tả bài và bằng chứng có giới hạn của tối đa bốn bài mẫu trong nhóm, gọi nhà cung cấp đã cấu hình, kiểm tra cấu trúc câu trả lời rồi hiển thị bản nháp. Mô hình không quyết định lại thành viên cụm và nội dung trả về không được đưa vào đặc trưng phân cụm. [6]

Luồng thao tác gồm tạo gợi ý, xem dẫn chứng, điền vào bản nháp, sửa và lưu nhận xét giảng viên. Chỉ bấm Gợi ý nhận xét chưa phải duyệt nội dung. Chỉ bấm Điền vào bản nháp cũng chưa phải lưu. Cách tách này giúp người dùng giữ quyền kiểm tra và sửa lời giải thích trước khi ghi nhận đánh giá của mình.

| Trạng thái | Ý nghĩa |
| Gợi ý từ LLM | Nội dung do mô hình tạo, cần kiểm tra |
| Gợi ý local_rules | Nội dung theo luật cục bộ, không phải API AI |
| Draft | Chưa được coi là nhận xét đã xác nhận |
| Review đã lưu | Người dùng chủ động lưu sau khi xem và chỉnh sửa |

Hồ sơ local đã kiểm chứng provider Groq, model openai/gpt-oss-20b và phản hồi HTTP 200. Cấu hình, model và nguồn được hiển thị; cache giúp dùng lại gợi ý khi bằng chứng và cấu hình không đổi. Thành công của một API call chỉ chứng minh tích hợp hoạt động, không đánh giá độ đúng sư phạm của nội dung. [6]

Backend không gửi metadata tên tài khoản hoặc ID học viên trong payload gợi ý, nhưng source và output có thể tự chứa thông tin cá nhân. Việc gọi API vì vậy vẫn là gửi một phần dữ liệu chương trình ra ngoài. Khóa API được giữ ở cấu hình máy chủ, không đặt trong slide, báo cáo hay JSON xuất cho người học.

Khi API lỗi, người trình diễn có thể tiếp tục xem cụm, luật và điền nhận xét thủ công. Nếu không cấu hình API, nguồn local_rules được ghi rõ. Phản hồi AI có thể sai hoặc quá tự tin, nên phần căn cứ và câu hỏi kiểm tra tiếp cần được ưu tiên hơn một tên nhóm nghe có vẻ thuyết phục.

---PAGE---

## 3.10 Thiết kế ứng dụng AAI Learning

Ứng dụng cung cấp sáu bài luyện C17: tổng từ 1 đến n, trung bình hai số, phần tử lớn nhất, đếm số dương, hoán vị qua hàm và điểm với đường tròn. Học viên nộp source, xem từng test rồi sửa bài. Lịch sử giữ cả bài sai và bài đúng, giúp quan sát quá trình thao tác thay vì chỉ điểm số cuối. [3]

Vai trò giảng viên có tổng quan lớp, chọn bài, tạo nhóm lỗi và mở báo cáo đã lưu. Phạm vi phân tích dựa trên lần nộp hoàn tất gần nhất của mỗi học viên cho bài tương ứng. Học viên đã đạt toàn bộ test vẫn xuất hiện trong tổng quan nhưng không bị giữ trong cohort bài sai chỉ vì trước đó từng sai.

| Vai trò | Chức năng chính | Mục đích |
| Học viên | Nộp, chạy test, sửa, xem lịch sử | Hiểu kết quả chương trình |
| Giảng viên | Xem nhóm, source, OAV, luật, nhận xét | Tổng hợp vấn đề cần hỗ trợ |
| Hệ thống | Lưu snapshot, kiểm soát quyền, thực thi giới hạn | Giữ bằng chứng và trạng thái |

Đăng nhập phục vụ phân quyền và gắn lịch sử với người dùng. Phân cụm về mặt thuật toán không đòi hỏi giao diện đăng nhập; nhưng khi trình diễn nhiều người nộp bài và một giảng viên xem lớp, việc tách tài khoản giúp tránh lẫn dữ liệu và thao tác. Đây là quyết định thiết kế ứng dụng, không phải yêu cầu thêm đối với phương pháp học không giám sát.

Bản demo ở cổng 8767 dùng cơ sở dữ liệu riêng trong .cache/course-demo. App thường ở cổng 8766 dùng .cache/learning-app. Tám chương trình minh họa được chuẩn bị để tạo tình huống có thể lặp lại; tên DEMO nhắc người xem rằng đó không phải lớp học đã được quan sát trong nghiên cứu. Không nên sửa các fixture này trước buổi nghiệm thu nếu muốn giữ kết quả nhóm ổn định.

Báo cáo JSON hỗ trợ lưu hồ sơ máy đọc được. Các phần cụm, luật, gợi ý và nhận xét cần giữ trạng thái riêng, để khi mở lại có thể biết đâu là kết quả thuật toán và đâu là nội dung diễn giải của con người.

---PAGE---

## 3.11 Thực thi C và lưu bằng chứng

Source mới trong app được biên dịch và chạy bằng runner Docker có hạn mức. Chương trình người dùng không được thực thi trực tiếp như một tiến trình không giới hạn trên máy chủ ứng dụng. Runner phục vụ sáu bài luyện do dự án viết; không có tuyên bố rằng toàn bộ corpus C lịch sử đã được replay bằng cơ chế này. [3][5]

| Biện pháp | Cấu hình được ghi nhận |
| Kết nối mạng | Tắt trong container chạy bài |
| Tài khoản và hệ thống tệp | Non-root, read-only, không mount thư mục host |
| Quyền tiến trình | Bỏ capabilities, no-new-privileges |
| Tài nguyên | 256 MB RAM, 1 CPU, tối đa 32 PID |
| Giới hạn thời gian | CPU 2 giây, hard 3 giây; wall 5 giây mỗi test |
| Output và biên dịch | Stdout/stderr 64 KB; compile 20 giây |

Giới hạn wall time có cả thời gian khởi động container nên khác với thời gian CPU của chương trình. Khi vượt giới hạn hoặc lỗi thực thi, giao diện cần báo trạng thái tương ứng; không quy tất cả các trường hợp này thành sai kết quả. Phân biệt lỗi hạ tầng, lỗi chạy và sai output làm bằng chứng rõ hơn cho người học.

Việc chấm output dùng so sánh token bỏ khác biệt khoảng trắng theo thiết kế bài luyện, không phải so sánh chính xác mọi ký tự định dạng. Điều này cần được nhắc nếu người xem thử xuống dòng hoặc thêm khoảng trắng. Một chương trình pass toàn bộ test đã cho vẫn có thể sai ở đầu vào chưa được bộ test bao phủ.

Bằng chứng được lưu gồm source, kết quả từng test và lịch sử, nhờ đó tải lại trang không làm mất các lần nộp trước. Kiểm chứng browser đã đi qua cả bài sai và bản sửa đúng, sau đó kiểm tra lưu và mở lại nhận xét. Những kiểm tra này xác nhận hành vi phần mềm trong môi trường thử, không chứng minh hệ thống đã sẵn sàng cho triển khai công khai với quy mô lớn hoặc thay thế một đánh giá an toàn chuyên biệt.

---PAGE---

# Chương 4 Demo và đánh giá kết quả

## 4.1 Kết quả baseline trên dữ liệu công khai

C-Pack-IPAs có 675 lượt chạy theo thiết kế 25 bài × 9 biến thể × 3 seed. Hồ sơ kết quả ghi 624 lượt ok và 51 lượt abstained. Trong 51 lượt, có 42 lượt thiếu mẫu hoặc số biểu diễn khác nhau cho k=3 và 9 lượt feature train giống hệt nhau. Không ép tạo cụm trong những trường hợp này là một phần của quy trình đánh giá. [2]

| Hồ sơ | Quy mô lượt chạy | Kết quả và phạm vi |
| C-Pack-IPAs | 675 | 624 ok; 51 abstained |
| ITSP development | 81 | Có kết quả trên 3 bài đã được xem |
| Sealed test C-Pack | Chưa đánh giá phương pháp | Giữ cho đánh giá sau khi khóa thiết kế |
| Nhãn chuyên gia độc lập hoàn tất | 0 | Chưa có gold để chấm cơ chế lỗi |

Mỗi lượt là một cấu hình thí nghiệm, không phải một sinh viên hoặc một lần thử học tập. Vì vậy, không được viết “675 sinh viên được đánh giá” hoặc cộng 675 với 81 thành số người tham gia. Các lượt chạy trên cùng corpus cũng phụ thuộc nhau qua dữ liệu và cấu hình.

Hồ sơ baseline cuối đã kiểm toán fingerprint đầu vào, mã, danh mục cấu hình, membership split, medoid và support của luật. Một kiểm tra với checksum đầu vào bị sửa đã được từ chối. Các biện pháp này tăng khả năng truy vết và tái lập; chúng không thay thế thước đo chất lượng phân nhóm dựa trên nhãn độc lập.

Tổng thời gian trong lõi run_experiment của 675 lượt được ghi khoảng 274 giây trên môi trường local. Con số không gồm nhập dữ liệu, ghi file, tạo báo cáo giảng dạy và audit nên không dùng như thời gian end-to-end hoặc cam kết hiệu năng cho máy khác. Trong buổi bảo vệ, nên ưu tiên quy mô và trạng thái kết quả thay vì quảng bá tốc độ từ một phép đo chưa bao phủ toàn hệ thống.

Kết quả hiện có cho phép nói baseline đã vận hành trên dữ liệu công khai có kiểm toán. Nó chưa cho phép xếp hạng phương pháp theo độ đúng misconception hoặc tuyên bố tốt hơn các nghiên cứu khác.

---PAGE---

## 4.2 Stdout giúp phân biệt thêm biểu diễn

Một phân tích trên 48 bài train và validation của ba cohort ITSP xét 387 cặp bài trong cùng bài tập. Biểu diễn combined có 67 cặp trùng OAV hoàn toàn; thêm stdout còn 42 cặp. Như vậy, trong tập đang xét có 25 cặp trước đó trùng biểu diễn nay được phân biệt. Mức giảm tương đối là khoảng 37,3% số cặp trùng ban đầu. [2]

| Biểu diễn | Cặp trùng OAV | Diễn giải |
| Test và AST | 67 | Nhiều cặp chưa phân biệt được bằng hai nguồn này |
| Test, AST và stdout | 42 | Có thêm thông tin phân biệt một số cặp |
| Chênh lệch | 25 | Giảm collision, chưa phải tăng accuracy |

Một ví dụ đã có regression test là cặp 271173_buggy và 271188_buggy. Stdout giúp phân biệt lỗi chuỗi “Cicle” với output chọn thông báo “on the Circle”. Ví dụ cho thấy hai bài cùng có verdict sai có thể khác về biểu hiện đầu ra. Tuy nhiên, không suy ra rằng mọi cặp được tách thêm đều có cơ chế lỗi khác nhau hoặc rằng hai người học có quan niệm sai khác nhau.

Số collision nhỏ hơn là tín hiệu biểu diễn chi tiết hơn. Biểu diễn quá chi tiết cũng có thể tách các bài cùng cơ chế vì khác hình thức output. Muốn đánh giá ích lợi, cần đo cả khả năng phân biệt cơ chế khác nhau và khả năng giữ các trường hợp cùng cơ chế gần nhau, dựa trên nhãn độc lập.

Fidelity của cây không tăng đồng đều khi thêm stdout. Hồ sơ nêu ví dụ K-means seed 91 trên bài 2825: combined có validation fidelity 1,0 còn combined_stdout là 0,5. Do hai cấu hình tạo mục tiêu cụm khác nhau và validation nhỏ, kết quả này không đủ để kết luận stdout làm phương pháp tốt hơn hay kém hơn về chẩn đoán.

Kết luận vừa mức là stdout cung cấp tín hiệu bổ sung ngoài test và AST trong các trường hợp đã kiểm tra. Nghiên cứu tiếp theo cần đối chiếu tín hiệu này với biểu diễn quan hệ và can thiệp đã xác minh, sử dụng cùng dữ liệu, chi phí và tiêu chí đánh giá.

---PAGE---

## 4.3 Kiểm chứng phần mềm và tích hợp AI

Kiểm thử phần mềm trả lời liệu chức năng có hoạt động theo đặc tả trong các tình huống kiểm tra. Kiểm chứng phương pháp trả lời liệu nhóm tạo ra có phản ánh cơ chế lỗi hoặc hỗ trợ người dạy tốt hơn. Báo cáo giữ hai loại bằng chứng riêng để tránh dùng số test pass thay cho chất lượng nghiên cứu.

| Hồ sơ và thời điểm | Kết quả ghi nhận | Điều đã kiểm tra |
| Nghiệm thu local 27 tháng 9 | 186 tests và 3 subtests; 27 smoke | Pipeline và baseline ở phiên bản đó |
| Docker tại đợt nghiệm thu | 14 checks đạt | Chương trình fixture trong runner |
| Browser nghiệm thu | Luồng chính đạt | Sai 1/6, sửa 6/6, lưu và mở lại |
| Bổ sung Groq 27 tháng 9 | 193 tests và 3 subtests; Ruff đạt | Mã mới và kiểm thử offline |
| Groq và giao diện | HTTP 200; draft; nguồn Groq | Gọi API và hiển thị gợi ý |

Các bộ kiểm tra Docker và smoke nêu trong bảng thuộc hồ sơ nghiệm thu trước khi bổ sung Groq; không cộng dồn hoặc mô tả như toàn bộ đã được chạy lại ở cùng một phiên bản. Bộ offline mặc định bỏ qua các ca cần Docker. Việc ghi rõ thời điểm và phạm vi giúp người đọc đối chiếu đúng artifact. [5][6]

Kiểm chứng browser đã quan sát lịch sử được giữ sau tải lại, nhận xét được lưu và mở lại, giao diện mobile không tràn ngang trong luồng thử. Phần AI đã có kiểm tra nháp không tự duyệt và gợi ý được xuất riêng với review. Các tình huống giả lập trong bộ test bổ sung cho kiểm chứng API thật nhưng phải được gọi đúng là test mock khi sử dụng hồ sơ đó.

Trong snapshot demo tám bài, nhóm chương trình in số cố định có bốn thành viên. API đã gợi ý tên “Giá trị cố định thay vì tính tổng”. Đây là ví dụ gợi ý có thể đối chiếu với source, chưa phải kết luận do chuyên gia độc lập xác nhận. Từ thành công kỹ thuật của HTTP 200 không thể suy ra chất lượng của mọi nhận xét do model tạo trong tương lai.

---PAGE---

## 4.4 Chuẩn bị máy và mở demo

Kịch bản sau áp dụng cho gói bàn giao hiện tại trên Windows đã cài môi trường. Mở Docker Desktop và đợi Linux engine sẵn sàng. Tại thư mục AAI-handoff, mở PowerShell rồi chạy lệnh bên dưới. Script mở demo ở cổng 8767; cơ sở dữ liệu demo tách khỏi app thường. [4]

```powershell
./misconceptions-prototype/start_demo.ps1
```

Giữ cửa sổ terminal hoạt động và mở http://127.0.0.1:8767 trong trình duyệt. Lần đầu chuẩn bị dữ liệu có thể lâu hơn vì tám chương trình minh họa cần được thực thi; các lần sau sử dụng lịch sử đã lưu. Ctrl+C dừng server nhưng không xóa cơ sở dữ liệu. Nếu cổng đang bận, kiểm tra xem demo đã chạy trước khi mở thêm tiến trình.

Tài khoản demo học viên và giảng viên được ghi trong docs/demo_nghiem_thu.md của gói bàn giao. Dùng đúng tài khoản demo, không đưa tài khoản riêng hoặc API key lên màn chiếu. Trước buổi nghiệm thu, nên thử đăng nhập cả hai vai trò và mở báo cáo để xác nhận dữ liệu sẵn sàng.

| Kiểm tra trước khi trình bày | Dấu hiệu sẵn sàng |
| Docker | Engine chạy, image runner có sẵn |
| Server | Trang cổng 8767 mở được |
| Dữ liệu | Có tám mẫu DEMO của bài tổng |
| Vai trò giảng viên | Xem được nhóm, bài đại diện và luật |
| Tùy chọn AI | Hiển thị nguồn và trạng thái nháp đúng |

Nếu cần kiểm tra môi trường dự án, dùng doctor, check và smoke theo docs/harness.md. Các lệnh harness ở thư mục gốc là python scripts/harness.py doctor, python scripts/harness.py check và python scripts/harness.py smoke; môi trường thực thi dự án dùng interpreter trong misconceptions-prototype/.venv. [8]

Nên giữ ảnh và JSON của lần kiểm chứng gần nhất làm phương án dự phòng cho sự cố mạng hoặc API. Khi trình bày ảnh dự phòng, nói rõ đó là bằng chứng của lần chạy trước. Chức năng cốt lõi OAV, cụm, luật và nhận xét thủ công vẫn có thể demo mà không phụ thuộc thành công của một nhà cung cấp LLM.

---PAGE---

## 4.5 Demo học viên từ bài sai đến bản sửa

Đăng nhập vai trò học viên, chọn Tổng từ 1 đến n. Dán chương trình sau để bắt đầu từ một lỗi dễ hiểu. Với bộ test demo đã kiểm chứng, chương trình đạt 1/6 test vì trường hợp tổng rỗng n=0 cho kết quả 0, còn các đầu vào khác không được tính đúng. [4][5]

```c
#include <stdio.h>
int main(void) {
    int n;
    scanf("%d", &n);
    printf("0\n");
    return 0;
}
```

Mở test n=2 và chỉ ra expected=3 nhưng actual=0. Nói rõ rằng đây là bằng chứng chương trình không tính tổng cho đầu vào đó, chưa đủ để kết luận người viết không hiểu vòng lặp. Sau đó thay bằng chương trình cộng đủ từ 1 đến n dưới đây.

```c
#include <stdio.h>
int main(void) {
    int n;
    scanf("%d", &n);
    long long sum = 0;
    for (int i = 1; i <= n; i++) sum += i;
    printf("%lld\n", sum);
    return 0;
}
```

Chạy lại và kiểm tra kết quả kỳ vọng 6/6 test. Mở Hành trình của tôi để thấy cả lần sai và lần sửa. Tải lại trang để chứng minh lịch sử đã được lưu. Nếu trước đó tài khoản đã giải bài khác, tiến độ tổng có thể không còn là 1/6 bài; nên trình bày dựa trên trạng thái đang hiện thay vì hứa một con số cố định.

Việc từ 1/6 lên 6/6 trong kịch bản do người trình diễn nhập hai chương trình đã chuẩn bị là kiểm chứng chức năng. Không được dùng nó làm số liệu chứng minh người học tiến bộ nhờ hệ thống, vì chưa có thiết kế đo lường học tập hoặc nhóm đối chứng.

---PAGE---

## 4.6 Demo giảng viên và nhận xét từng nhóm

Chuyển sang tài khoản giảng viên, mở Lớp học và nhóm lỗi, chọn bài Tổng từ 1 đến n và k=2. Với tám fixture ban đầu, hồ sơ demo có hai nhóm. Nếu vừa nộp một bài đúng bằng tài khoản học viên, tài khoản đó vẫn có trong tổng quan nhưng không thuộc cohort bài sai hiện tại. Khi dữ liệu thay đổi, cần đọc số mẫu thực tế đang hiển thị. [4]

| Thao tác | Nội dung nên nói khi trình diễn |
| Mở bài đại diện | Đây là source thật và kết quả từng test |
| Mở OAV | Object là bài nộp; thuộc tính là test, AST, output |
| Đọc IF–THEN | Luật giải thích việc vào cụm, chưa chẩn đoán nhận thức |
| Gợi ý nhận xét | AI hỗ trợ soạn nháp từ các mẫu có giới hạn |
| Điền và sửa bản nháp | Giảng viên kiểm tra trước khi lưu |
| Lưu rồi tải lại | Chứng minh nhận xét được giữ trong báo cáo |

Ở nhóm in hằng, xem nhiều thành viên để xác nhận căn cứ. Có thể điền tên nhóm theo biểu hiện, ghi n=2 và n=5 làm ví dụ, rồi đề xuất yêu cầu học viên liệt kê các số được cộng. Nếu AI trả về một nhận định rộng hơn bằng chứng, chỉnh lại trước khi lưu. Nếu cụm trộn nhiều dạng biểu thức sai, ghi rõ phạm vi mẫu đã kiểm tra.

Cuối luồng, tải JSON và chỉ ra rằng phần cụm tồn tại độc lập với suggestions và reviews. Cluster lưu cấu trúc nhóm; suggestion lưu nguồn gợi ý và trạng thái; review lưu nhận xét đã chủ động ghi. Đây là câu trả lời trực tiếp cho thắc mắc vì sao JSON đã có nhóm mà vẫn cần phần nhận xét giảng viên.

Nếu API không phản hồi, giữ nguyên dữ liệu và tiếp tục nhận xét thủ công. Nếu chưa cấu hình khóa, có thể dùng gợi ý local_rules nhưng phải nói đúng nguồn. Không cần huấn luyện một model riêng để hoàn thành luồng nghiệm thu này; phân cụm và cây giải thích đã hoạt động độc lập với API tạo văn bản.

Kết thúc demo bằng việc mở lại báo cáo đã lưu, chỉ ra source dẫn chứng và nhắc rằng tên nhóm là diễn giải cần kiểm tra, còn bằng chứng test là phần người xem có thể trực tiếp đối chiếu.

---PAGE---

# Chương 5 Kết luận và hướng phát triển

## 5.1 Hạn chế và phạm vi kết luận

Hạn chế lớn nhất là chưa có nhãn cơ chế lỗi độc lập hoàn tất và chưa có bằng chứng trực tiếp về nhận thức người học. Các nhận xét của AI hoặc người sử dụng demo không thay thế được quy trình chuyên gia. Vì vậy, chưa báo cáo accuracy misconception, hiệu quả học tập hay kết luận phương pháp tốt hơn nghiên cứu trước. [2]

| Hạn chế | Ảnh hưởng | Hướng kiểm tra tiếp |
| AST mới ở mức presence | Bỏ sót quan hệ giữa biến và thao tác | Thêm biểu diễn def-use và binding |
| Log lịch sử chưa replay toàn bộ | Chưa xác minh hết oracle và hành vi C | Oracle audit trong runner cách ly |
| Chưa audit near-duplicate | Có thể còn liên hệ xuyên partition | So khớp có kiểm soát và cập nhật protocol |
| Chưa có gold độc lập | Không chấm được cơ chế đúng hay sai | Nhiều người gán nhãn và adjudication |
| Demo nhỏ và do dự án tạo | Không đại diện lớp học thật | Đánh giá riêng nếu nghiên cứu triển khai |

Các chỉ số nội tại cũng có giới hạn. Silhouette tốt có thể chỉ phản ánh một cách mã hóa tạo nhóm rõ; fidelity cao có thể do cây bắt chước được ID cụm; một cụm lớn không tự nghĩa là nhiều sinh viên có cùng quan niệm sai. Những chỉ số này nên phục vụ kiểm tra hành vi thuật toán, không thay thế thước đo gắn với câu hỏi nghiên cứu.

LLM thêm một nguồn sai số khác. Một đoạn văn trôi chảy có thể bỏ qua ngoại lệ hoặc biến giả thuyết thành khẳng định. Giới hạn số mẫu giúp kiểm soát chi phí nhưng làm model không thấy toàn bộ cụm. Do đó, nguồn, trạng thái nháp và dẫn chứng cần luôn được giữ cùng nội dung gợi ý.

Kết quả local cũng phụ thuộc môi trường, phiên bản thư viện và dữ liệu tại thời điểm chạy. Hồ sơ có fingerprint và snapshot để truy vết, nhưng việc tái lập vẫn cần đúng bộ dữ liệu và cấu hình. Bản bàn giao hiện tại chứa các bổ sung local; không mặc nhiên coi mọi thay đổi này đã có trên nhánh main của GitHub chỉ vì một PR trước đó đã merge.

---PAGE---

## 5.2 Hướng phát triển và kết luận chung

Đối với mục tiêu môn học, ưu tiên là giữ demo ổn định, giải thích đúng các bước và chuẩn bị bằng chứng có thể mở lại. Người trình bày cần nắm sự khác nhau giữa pass test, chất lượng cụm, fidelity của luật và xác nhận quan niệm sai. Một buổi trình diễn rõ ràng đi từ một bài sai cụ thể đến nhận xét có căn cứ sẽ thuyết phục hơn nhiều chỉ số không được giải thích.

Đối với hướng nghiên cứu, bước tiếp theo nên giải quyết khoảng trống bằng chứng trước khi tăng độ phức tạp mô hình. Cần kiểm toán oracle và môi trường thực thi corpus, sau đó xây tập nhãn cơ chế độc lập với nhiều người đánh giá. Tiêu chí gán nhãn phải phân biệt lỗi quan sát được và giả thuyết nhận thức, đồng thời lưu bất đồng thay vì ép mọi trường hợp thành một nhãn chắc chắn.

| Ưu tiên | Công việc đề xuất | Điều kiện để đánh giá |
| 1 | Oracle audit và kiểm tra dữ liệu trùng gần | Báo cáo lỗi và phạm vi corpus tin cậy |
| 2 | Gán nhãn cơ chế độc lập | Tiêu chí, nhiều người đánh giá, xử lý bất đồng |
| 3 | So sánh biểu diễn quan hệ với stdout | Cùng split, ngân sách, baseline và ablation |
| 4 | Can thiệp hoặc chỉnh sửa được kiểm chứng | Thay đổi dự đoán phải được chạy kiểm tra |
| 5 | Đánh giá sealed test và độ bền | Protocol đóng băng, khoảng tin cậy theo sinh viên |

Huấn luyện encoder, dùng model lớn hơn hoặc sinh adaptive probes là những phương tiện có thể cân nhắc sau khi đã có quy trình đánh giá. Các mục này trong protocol hiện là đề xuất chưa thực hiện; không đưa vào phần kết quả đã hoàn thành. Muốn phát biểu rằng hệ thống giúp người học tiến bộ cần một thiết kế nghiên cứu giáo dục riêng, không thể suy ra từ corpus offline.

Tại phạm vi hiện tại, đóng góp của dự án là hiện thực hóa chuỗi bằng chứng có thể truy vết từ bài lập trình sai, qua OAV và phân cụm, đến luật và phản hồi giảng dạy. Ứng dụng cho phép thử trực tiếp chuỗi đó và giữ vai trò kiểm tra của giảng viên khi dùng AI. Đây là kết luận phù hợp cho nghiệm thu đề 5; các kết luận sâu hơn được dành cho giai đoạn đánh giá tiếp theo.

---PAGE---

# Tài liệu tham khảo và hồ sơ bằng chứng

[1] Nhóm dự án AAI. Hợp đồng nghiên cứu và nghiệm thu đề 5. Tài liệu nội bộ trong gói bàn giao: docs/topic5-contract.md. Nguồn xác định phạm vi yêu cầu môn học và giới hạn phát biểu.

[2] Nhóm dự án AAI. Trạng thái nghiên cứu ngày 27 tháng 9 năm 2026. research/STATE.md. Hồ sơ kèm theo: research/data-audit/cpack-20260926.json; research/splits/cpack-v3.json; research/runs/cpack-summary-20260926.md; research/runs/itsp-stdout-final-20260926/summary.md và collision_audit.json. Nguồn cho số liệu corpus, baseline, collision và các phần chưa thực hiện.

[3] Nhóm dự án AAI. Hướng dẫn ứng dụng học viên và giảng viên. docs/learning_app.md; mã nguồn trong misconceptions-prototype/. Nguồn cho kiến trúc, thuật toán của app, vai trò và runner.

[4] Nhóm dự án AAI. Demo nghiệm thu đề 5. docs/demo_nghiem_thu.md; misconceptions-prototype/start_demo.ps1; misconceptions-prototype/scripts/prepare_learning_demo.py. Nguồn cho thao tác và fixture trình diễn.

[5] Nhóm dự án AAI. Hồ sơ nghiệm thu local ngày 27 tháng 9 năm 2026. docs/nghiem_thu_local_20260927.md; artifacts/course-acceptance-20260927/verification.json; browser/acceptance.json; smoke-final.txt và docker.txt trong cùng thư mục hồ sơ. Nguồn cho các kiểm tra ở đợt nghiệm thu trước bổ sung Groq.

[6] Nhóm dự án AAI. Hồ sơ gợi ý nhận xét và tích hợp Groq. artifacts/suggestion-acceptance-20260927/acceptance.json; artifacts/groq-acceptance-20260927/live-api-check.json; browser-check.json và groq-suggestion.png. Phân biệt kiểm tra mock với lần gọi Groq thật.

[7] C-Pack-IPAs. Kho dữ liệu công khai. https://github.com/pmorvalho/C-Pack-IPAs. Snapshot sử dụng: C-Pack-IPAs-26, commit 76901e1223b250a093a02d5e29113ad735c3d2b9. Số liệu trong báo cáo lấy từ audit của dự án tại [2], không coi README thay thế kiểm toán nhập dữ liệu.

[8] Nhóm dự án AAI. Hướng dẫn harness và tái lập. docs/harness.md; research/runs/cpack-reproduce-20260926.md. Kho mã nhóm: https://github.com/linhlinhlin/AAI. PR số 1 được ghi nhận merge tại commit ab1c5b63d9be579a17a8dd6adf6bdc5df6632a9d; các bổ sung local được đối chiếu riêng bằng hồ sơ [6].

Các tài liệu nội bộ trên được đọc trong snapshot bàn giao ngày 28 tháng 9 năm 2026. Báo cáo không trình bày một khảo sát đầy đủ về toàn bộ nghiên cứu liên quan và không sử dụng bảng so sánh SOTA khi chưa có thiết kế đánh giá tương ứng.

---PAGE---

# Phụ lục thuật ngữ và câu hỏi bảo vệ

| Thuật ngữ | Cách hiểu trong đề tài |
| Submission | Một lần nộp chương trình |
| Oracle | Kết quả mong đợi của test |
| OAV | Bài nộp, thuộc tính và giá trị quan sát |
| AST | Cấu trúc cú pháp dạng cây của source |
| Medoid | Bài có thật được chọn làm đại diện cụm |
| Fidelity | Mức mô hình giải thích đồng ý với mục tiêu cụm |
| Holdout | Dữ liệu giữ ngoài bước fit |
| Abstention | Từ chối tạo kết quả khi điều kiện không đủ |

**Vì sao đã có nhóm trong JSON vẫn cần nhận xét?** Nhóm là kết quả thuật toán. Nhận xét giải thích ý nghĩa, dẫn chứng và đề xuất giảng lại. Hai phần được lưu riêng để không nhầm kết quả tự động với đánh giá đã xem xét.

**Có cần API hoặc tự train model mới chạy được không?** Không. OAV, K-means và cây giải thích chạy độc lập. API chỉ hỗ trợ viết nháp nhận xét; thiếu API vẫn có thể dùng luật cục bộ hoặc điền thủ công.

**Fidelity 100% có nghĩa chẩn đoán đúng 100% không?** Không. Nó cho biết cây và phép gán cụm đồng ý trên các mẫu đang đánh giá. Muốn đo đúng cơ chế cần nhãn độc lập; muốn xác nhận quan niệm sai cần bằng chứng về nhận thức.

**Vì sao dùng K-means nhưng lại có cây quyết định?** K-means tạo nhóm không giám sát; cây học dự đoán ID nhóm để sinh luật dễ đọc. Cây là mô hình giải thích, không phải thuật toán phân cụm của hệ thống.

**Đã chứng minh cải thiện việc học chưa?** Chưa. Demo hai chương trình từ 1/6 lên 6/6 chỉ xác nhận luồng nộp và sửa. Đánh giá học tập cần người tham gia thật, thiết kế đo lường và phạm vi nghiên cứu riêng.

**Điểm cần làm tiếp có ý nghĩa nhất là gì?** Kiểm toán oracle, xây nhãn cơ chế độc lập rồi so sánh biểu diễn trên protocol đóng băng. Tăng kích thước LLM không thay thế những bằng chứng còn thiếu này.