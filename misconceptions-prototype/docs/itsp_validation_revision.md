# Kiểm chứng sau phản biện — 20/09/2026

## Kết luận hiện tại

Pipeline phân nhóm biểu hiện lỗi theo test và các dấu hiệu cú pháp. Chưa xác nhận những nhóm đó là quan niệm sai lầm của người học. Kiểm tra lại 59 submissions cho thấy A và C cùng phân hoạch ở seed42: ARI=1 riêng cả ba bài; không có bằng chứng cấu hình cấu trúc hiện tại cải thiện phân hoạch tại seed này. Không suy từ đó rằng mọi đặc trưng cấu trúc đều vô ích.

Hai bài 2825/271173 và 2825/271188 có vector combined OAV giống nhau trong kết quả hiện tại. Biểu diễn không chứa thông tin phân biệt hai bài; thuật toán có thể tách tùy ý khi hòa khoảng cách nhưng đó không phải bằng chứng nhận ra nguyên nhân khác nhau.

## Ba tầng bằng chứng

| Tầng | Evidence | Phát biểu được phép |
|---|---|---|
| Biểu hiện | Input, expected/actual, verdict lịch sử | Có cùng/khác mẫu test fail hoặc output |
| Cơ chế | Truy vết code, vị trí và điều kiện gây lỗi, bản sửa đối chiếu | Chuyên gia đề xuất/xác nhận cơ chế lỗi trong bài làm |
| Misconception | Giải thích của chuyên gia về quy tắc hiểu sai, bằng chứng và giả thuyết thay thế; nếu cần, giải thích của người học | Misconception tiềm năng trong phạm vi evidence; không chẩn đoán chắc chắn nhận thức từ một bài sai |

No và Unclear không là hai cơ chế lỗi đồng nhất. Unclear là quyết định sau khi đã xem nhưng evidence chưa phân giải được; pending là chưa chấm. Bản sửa đúng không tự chứng minh hiểu biết. Nếu cần thêm giải thích của người học nhưng dataset không có, giữ giới hạn hoặc Unclear, không tạo evidence.

## Protocol human review

Tái sử dụng [quy trình hiện hành](itsp_human_review_protocol.md) và gói vòng 1 riêng. Hai người thật chốt cùng codebook trước chấm: phạm vi toán học/ngữ nghĩa C, mức chi tiết của type, cơ chế chính khi đa lỗi, và xử lý OTHER_CONCEPT. Không tự ký duyệt. Mỗi người chấm độc lập; khóa bản gốc trước mở cụm; bất đồng chuyển chuyên gia adjudicate, không dùng AI quyết định thay.

Trong evidence vòng 2 ghi cơ chế ngắn, danh sách submission ID thực sự đã xem (`members_reviewed`), `n_reviewed/n_cluster`, và mẫu trái nguyên nhân. Đây là nội dung trong trường evidence hiện có, chưa đổi schema. So sánh same-cause agreement chỉ khi hai người xem cùng phạm vi; scorer chưa tự kiểm tra nội dung tự do này nên người điều phối phải đối chiếu trước khi diễn giải metric.

Packet chính đã gắn nhãn vòng 2 trên đầu. Không gửi packet này để chấm mù. Annotation AI chỉ là tham khảo nội bộ, không ground truth.

## Mẫu phát triển và mẫu đánh giá mới

[Manifest dữ liệu đã xem](../results/itsp/development_exposure_manifest.json) ghi đủ 59 submissions trong hồ sơ. Đây là danh sách loại trừ bảo thủ cho thí nghiệm đặc trưng mới; không đổi split và kết quả baseline lịch sử. 17 mẫu vẫn dùng được cho phân tích ca và expert review, nhưng không làm test độc lập để chọn feature.

Chưa chọn tập mới, chưa đặt cỡ mẫu hoặc seed mới. Trước thí nghiệm tiếp theo cần chốt với người phụ trách: ngân sách chấm, bài tập/phạm vi, tiêu chí chọn mẫu và taxonomy. Chọn ngẫu nhiên hoặc phân tầng theo bài trong phần chưa xem phù hợp, lưu danh sách và seed trước khi đọc nhãn. Loại exact-source trùng với dữ liệu đã xem; kiểm tra gần trùng khi khả thi và công bố giới hạn. Bài mới có test khác phải xử lý theo cohort; không ghép test ID giữa đề. Nếu không đủ mẫu chưa xem cùng phạm vi, báo thay đổi bài toán hoặc chờ dataset giảng viên; không gọi holdout cũ là dữ liệu mới.

Chốt feature, trọng số và k từ tập phát triển trước khi mở nhãn đánh giá mới. Dùng cùng mẫu/routing/split cho mọi arm. Không dùng correct source, nhãn expert hay ID làm feature. Không tuning sau khi đọc nhãn cuối; mọi vòng chỉnh sửa sau đó cần tập đánh giá khác hoặc được báo là khám phá.

## Thử nghiệm quan hệ tối thiểu — chưa triển khai

Giữ exact test signatures, weighted Hamming + average linkage và cây surrogate nông. Khi protocol được chốt, thử lần lượt từng đặc trưng nhỏ rồi kết hợp, luôn có A/B/C đối chứng trên cùng dữ liệu:

- Liên kết if/else: phân biệt else gắn với if nào và các nhánh độc lập/chuỗi else-if.
- Assignment nằm trong điều kiện: kiểm tra quan hệ AST của assignment với condition, không chỉ có ký tự `=` toàn file.
- Hướng cập nhật vòng lặp: quan hệ biến điều khiển, điều kiện và bước cập nhật; không suy lỗi chỉ từ có `++`/`--`; trường hợp phức tạp ghi unknown theo protocol.

Các đặc trưng này là dấu hiệu quan hệ cú pháp, không nhãn lỗi. Không đảm bảo phân biệt cặp lỗi chuỗi output 271173/271188; muốn phân biệt cần thiết kế và kiểm tra representation phù hợp, không thêm heuristic theo ID hai mẫu.

ILA chỉ xét ở bước quy nạp luật nếu cần; cluster ID là pseudo-label để giải thích phân hoạch. Cây/luật có fidelity cao không đồng nghĩa chẩn đoán misconception chính xác. Không thêm thuật toán clustering mới, LLM hay GNN ở giai đoạn này.

## Báo cáo để tránh purity gây hiểu nhầm

Báo riêng từng bài/arm: tổng mẫu đã chọn, hoàn tất, Yes/No/Unclear/pending, typed Yes, adjudication, coverage và cluster sizes. Purity theo type chỉ dùng adjudicated Yes có type thuộc codebook được duyệt; luôn báo tử số/mẫu số và coverage trên toàn mẫu. Cụm một positive có purity=1 không chứng minh cụm đồng nhất.

Bổ sung phân tích gộp sai/tách sai khi chuyên gia đã thống nhất nhãn cơ chế có thể so sánh; không suy nhãn cơ chế từ tên type rộng. Trên cùng các cặp đủ nhãn trong từng bài: TP=cùng cụm/cùng nhãn; FP=cùng cụm/khác nhãn (gộp sai); FN=khác cụm/cùng nhãn (tách sai). Pairwise precision=TP/(TP+FP), recall=TP/(TP+FN); mẫu số 0 giữ null. Báo TP/FP/FN, số cặp đủ nhãn trên tổng cặp ứng viên và tỷ lệ mẫu có nhãn. Với đa lỗi chưa chốt quan hệ tương đương, giữ phân tích ca; không ép thành phân hoạch để tính ARI.

Đây là chỉ số bổ sung được đề xuất, chưa triển khai/chạy hoặc có giá trị thực nghiệm. Nhiều cặp chung một submission và ba seed không độc lập; không coi chúng là số quan sát độc lập để suy ý nghĩa thống kê. Agreement dùng lượt độc lập trước adjudication; purity dùng nhãn thống nhất, hai nguồn khác nhau.

## Điều kiện kết luận

Chỉ nói feature mới cải thiện trong phạm vi tập đánh giá đã khóa nếu có bằng chứng human phù hợp, coverage đủ minh bạch, giảm gộp/tách sai và không đánh đổi bị che bởi loại nhiều No/Unclear. Không mặc định chỉ cần silhouette/purity tăng. Khi bằng chứng mâu thuẫn hoặc mẫu ít, báo chưa đủ kết luận. Không có student ID: không báo tỷ lệ sinh viên hiểu sai, độ chính xác chẩn đoán hay generalization sang unseen student.

Hiện expert purity/raw agreement/kappa vẫn null. Các phần phụ thuộc xác nhận codebook, nhãn và ngân sách mẫu mới đang chờ người phụ trách; không xem chúng là đã hoàn tất.
