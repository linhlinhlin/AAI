# Luồng giảng viên: K-means → OAV → gắn nhãn → phản hồi lớp

## Luồng đã triển khai

1. **Giảng viên Dashboard:** chọn một bộ bài cùng đề/ngôn ngữ/test suite, bấm Phân tích bài làm.
   Mặc định web/API web và CLI là K-means trên one-hot có trọng số, sử dụng hình học Euclid.
   HAC và exact signatures chỉ là baseline trong Advanced Settings. ILA chưa được triển khai.
   Core và script nghiên cứu cũ có thể vẫn gọi baseline; không đổi tên HAC thành K-means.
2. **Tổng quan lớp:** hiển thị phạm vi dữ liệu, số bài có/chưa có nhãn nhóm xác nhận.
3. **Gắn nhãn nhóm:** đọc source/log của các thành viên, xem gợi ý detector và đặt tên lỗi.
   Chọn misconception, lỗi khác hoặc nhóm hỗn hợp; lưu trạng thái nháp/xác nhận.
   Xác nhận yêu cầu tên người phụ trách, căn cứ và hành động tiếp theo.
4. **Luật giải thích:** NẾU là bảng Object–Attribute–quan hệ–Value; THÌ là tên nhãn nhóm.
   Nhóm chưa gắn nhãn ghi “Chưa xác định — cần giảng viên gắn nhãn”. Không tự phát minh tên.
   Nhãn nháp hiển thị rõ nháp, không được tính trong biểu đồ nhãn xác nhận.
5. **Tổng quan lớp:** biểu đồ thanh phân bố nhãn xác nhận và nội dung cần kiểm tra/giảng lại.
6. **Kho báo cáo:** tìm web_runs; “Mở dashboard” trên kết quả phân tích/gắn nhãn để khôi phục.
   Với A/B/C, mở file phân tích mặc định arm C; file mapping khôi phục đúng arm đã gắn nhãn.

## Ý nghĩa của mapping

Mapping gắn với file kết quả bất biến, hash nguồn và arm, không chỉ số cluster. Mỗi lần lưu
tạo snapshot riêng có người phụ trách và thời điểm; không ghi đè thí nghiệm hay nhãn lần trước.
Thí nghiệm mới luôn bắt đầu chưa gắn nhãn. Tên người phụ trách là khai báo trong ứng dụng local,
không phải xác thực danh tính. Mapping này không sửa 17 annotation chấm mù hoặc dùng làm gold
để tự đánh giá chính mô hình. Gợi ý từ máy chỉ điền **nháp**, người dùng phải xem xét riêng.

Một cluster có thể chứa nhiều cơ chế. Trạng thái “nhóm hỗn hợp” được giữ riêng, không ép thành
một misconception. Gắn nhãn toàn nhóm cũng không chứng minh mọi bài hoặc mọi sinh viên có lỗi đó.
Các luật cây dự đoán nhãn nhóm thông qua mapping; chưa phải classifier misconception được huấn
luyện và đánh giá trên ground truth độc lập. Fidelity kỹ thuật vẫn đo cluster ID.

## OAV

Điều kiện cây được chuyển có bảo toàn ý nghĩa, ví dụ:

| Object | Attribute | Quan hệ | Value |
|---|---|---|---|
| Bài đang xét | Kết quả ca kiểm thử 1 | ≠ | Đạt |
| Bài đang xét | Có câu lệnh if | = | Có |

Các hàng kết hợp bằng VÀ. Không thay NOT(pass) thành fail vì có các trạng thái khác.
Đối tượng bài làm là hợp lệ; không tự tạo tên hàm check_point hoặc kiểu trả về khi extractor
chưa xác định. Bộ luật chuyên môn có các OAV riêng như “hàm hoán vị — kiểu trả về — void”,
chỉ xuất hiện khi detector khớp. OAV chuyên môn chưa được dùng để huấn luyện K-means.

## Mẫu số trên dashboard

- Phần trăm bài = số bài thuộc nhóm đã gắn nhãn đó / **tất cả bài của dataset đang chọn**.
  Cả bài pass toàn bộ, parse error, thiếu test và chưa có nhãn đều thuộc mẫu số.
- Cùng nhãn và cùng loại ở nhiều cụm được cộng gộp. Nháp không tính vào nhãn xác nhận.
- Chỉ khi mọi bài có student ID mới tính tỷ lệ người học: đếm ID duy nhất có ít nhất một
  bài trong nhóm / tổng ID duy nhất trong dataset. Một người có thể có nhiều loại lỗi;
  do đó dùng bar chart, không pie chart đòi hỏi các phần loại trừ nhau.
- ITSP thiếu ID: tỷ lệ sinh viên là chưa xác định. Không lấy số submissions làm số sinh viên.
- Dataset của một bài không nhất thiết đại diện cả lớp. Muốn kết luận “% cả lớp” phải có
  danh sách lớp, phạm vi lấy mẫu và quy tắc chọn bài nộp được xác nhận.
- Các chỉ số silhouette/holdout/fidelity nằm trong vùng nghiên cứu mở rộng. Hành động giảng lại
  do giảng viên nhập; không tự suy ra hiệu quả can thiệp từ thống kê nhóm.

## Đối chiếu nguồn lý thuyết

- [Minsky, 1974, A Framework for Representing Knowledge](https://www.mit.edu/~dxh/marvin/web.media.mit.edu/~minsky/papers/Frames/frames.html)
  cung cấp nền tảng frame/slot; OAV ở đây là biểu diễn kỹ thuật của dự án lấy cảm hứng từ
  đối tượng–thuộc tính–giá trị, không tuyên bố Minsky định nghĩa nguyên schema OAV này.
- Trích dẫn “Rule Extraction from Clustering (Diederich/Andrews)” chưa đủ để xác minh bài cụ thể.
  Nguồn tìm được là Andrews, Diederich & Tickle (1995), *Survey and critique of techniques for
  extracting rules from trained artificial neural networks*, về mạng nơ-ron, không phải mô tả
  thuật toán trích luật từ K-means. Chưa dùng nó làm chứng cứ cho thuật toán hiện tại.
- Trích dẫn “Khirasaria et al., 2020” chưa xác minh được. Nguồn phù hợp xác minh được là
  [Khosravi et al. (2022), Explainable Artificial Intelligence in education](https://doi.org/10.1016/j.caeai.2022.100074),
  [bản lưu tại Monash](https://researchmgt.monash.edu/ws/portalfiles/portal/398846132/381591443_oa.pdf).
  Bài này thảo luận XAI theo nhu cầu/ngữ cảnh giáo dục; không chứng minh dashboard hiện tại
  có độ chính xác hoặc hiệu quả giảng dạy đã được đánh giá.
- [Rule Style Guide của dự án](itsp_rule_explanation_style.md) tiếp tục áp dụng cho giả thuyết
  cơ chế. Luật dự đoán nhãn nhóm có target và trạng thái mapping riêng như mô tả ở trên.

## Kiểm chứng

Tests kiểm tra mặc định K-means, phủ định OAV, mẫu số có bài ngoài cụm, student deduplication,
thiếu danh tính, nhãn nháp, nhóm không hợp lệ, gom cùng nhãn và snapshot không sửa nguồn.
Kiểm tra trình duyệt dùng nhãn thử nghiệm trên dữ liệu tổng hợp; không xác nhận misconception
thật cho ITSP. Nhãn khoa học vẫn cần quy trình đánh giá con người độc lập.
