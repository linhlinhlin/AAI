# Validation khoa học ITSP: baseline và ablation A/B/C

## Sau phản biện — 20/09/2026

[Protocol kiểm chứng đã cập nhật](itsp_validation_revision.md): tách biểu hiện lỗi → cơ chế lỗi → giả thuyết misconception; giữ baseline và cây luật nông. ILA thuộc quy nạp luật, không gọi là clustering phi giám sát. Kiểm tra lại đủ 59 submissions: A=C ở seed42 (ARI=1 từng bài); vector combined của 271173/271188 trùng nhau. Chưa có bằng chứng cấu trúc hiện tại cải thiện phân hoạch; chưa phủ định mọi cấu trúc khác.

Đánh dấu toàn bộ 59 bài đã xuất hiện trong hồ sơ là dữ liệu phát triển/đã xem cho thí nghiệm feature mới; chưa chọn mẫu đánh giá độc lập mới hoặc triển khai feature quan hệ. Packet chính đã gắn nhãn “Vòng 2 — có hiển thị cụm”; gói vòng 1 giữ nguyên. Hai chuyên gia thật cần chốt codebook và chấm độc lập. Báo purity kèm coverage, No/Unclear và phân tích gộp/tách sai; chỉ số cặp cần nhãn cơ chế phù hợp, chưa tự tính trên AI. Expert validation tiếp tục chờ annotation, các metric vẫn null.


Ngày 19/09/2026. Mục tiêu là kiểm chứng biểu diễn và giới hạn suy luận trên prototype công khai.
Không thêm LLM/GNN, thuật toán mới hoặc feature được thiết kế theo 17 mẫu đã duyệt.
Chưa có dữ liệu giảng viên và expert gold nên validation nhận diện misconception **chưa hoàn tất**.

## Results/Discussion — trạng thái human validation hiện hành

Human review **0/17**, adjudication **0/17**; purity, raw agreement và Cohen’s kappa đều **null**, không phải 0. AI annotations chỉ là tham khảo kỹ thuật nội bộ; không tính metric trên AI hay coi AI là ground truth. Các kết quả A/B/C bên dưới đánh giá phân hoạch và surrogate fidelity, không chứng minh khả năng nhận diện misconception.

Gói vòng 1 đã chuẩn bị riêng với phiếu trống, codebook dự thảo định nghĩa rõ và evidence đầy đủ, không chứa nhãn AI/cluster. Chuyên gia chốt codebook trước chấm; chưa tự ký phê duyệt và chưa gửi file. [Gói gửi chuyên gia](../results/itsp/human_review_packet.zip) · [Audit gói](../results/itsp/human_review_packet_audit.json) · [Quy trình sau khi nhận phiếu](itsp_human_review_protocol.md).

Discussion cần giữ giới hạn: 17 mẫu lấy có chủ đích, không có student ID, khác biệt đề/oracle, khả năng nhiều nguyên nhân cùng cụm, và chưa có đồng thuận con người. Chỉ cập nhật kết luận validation sau khi có nhãn human thực tế theo protocol; không suy rộng purity của subset positive ra toàn cohort.

## 1. Baseline đã có trước thay đổi

- **Exact outcome signatures:** các bài cùng vector test pass/fail thuộc cùng nhóm. k không điều khiển baseline này.
- **Agglomerative outcomes-only:** average linkage trên ma trận weighted Hamming; baseline chính để so structural.
- **K-means:** đối chứng cũ dùng one-hot có trọng số, `n_init=10`. Giữ nguyên, không trộn kết quả của nó
  vào ablation mới chỉ thay feature. 126 thí nghiệm cũ vẫn lưu nguyên vẹn.
- **Rule baseline:** luôn dự đoán cụm đông nhất trong train, đo trên nhãn holdout do nearest medoid gán.
  Không chọn cụm đa số từ holdout.

## 2. OAV và feature thực tế

OAV là biểu diễn object–attribute–value: object là submission, thuộc tính có thể là test hoặc cấu trúc.
Vì vậy so sánh này là **hai nguồn feature**, không phải “OAV versus không OAV”.

- Test: `test:<id>` là categorical. Trên các mẫu eligible đã chọn chỉ còn pass/fail;
  Hamming trên chúng tương đương dùng bit `fail=1, pass=0`. Không dùng điểm tổng hoặc input/output text làm feature.
- C structural: 16 flags `ast:c_for`, `while`, `do`, `if`, `inclusive_comparison`, `strict_comparison`,
  `subscript`, `zero_index`, `one_index`, `pointer_declarator`, `pointer_parameter`, `array_parameter`,
  `address_of`, `dereference`, `update`, `return` (mọi tên đều có tiền tố `ast:c_`).
- Mỗi flag là 0/1, unknown khi không trích được; chỉ là sự hiện diện cú pháp toàn chương trình.
  Không mã hóa biểu thức cụ thể, tên biến, literal output, số lần xuất hiện hay semantics.
- tree-sitter C không chạy/preprocess code; bỏ header log trước phân tích. Parser error không tự là compile error.
- Chỉ giữ flag cấu trúc biến thiên trên **train**. Khi B không còn feature, abstain rõ ràng,
  không chuyển ngầm sang test features. Feature chỉ xuất hiện ở holdout không được chọn lại.
- Không dùng ID/nguồn, bản sửa đúng, expert labels hoặc giả thuyết review trong vector.

## 3. Protocol cố định và điều kiện so sánh

Tái sử dụng đúng ba cohort đã chọn trước: 2825 (22), 2812 (19), 2833 (18), tổng 59 bài eligible.
Không gộp test của các đề khác nhau vào một không gian. 649 bài nhập toàn dataset đã được audit từ mốc trước;
ablation này không tuyên bố chạy trên cả 649 bài hoặc đại diện đủ 74 bài tập.

| Điều kiện | A | B | C |
|---|---|---|---|
| Feature | Test-failure only | Structural only | Test + structural |
| Tổng trọng số test/cấu trúc | 1/0 | 0/1 | 0,8/0,2 |
| Trong mỗi block | Chia đều | Chia đều | Chia đều |
| Khoảng cách | Weighted Hamming | Weighted Hamming | Weighted Hamming |
| Clustering | Average-linkage agglomerative | Như A | Như A |
| k | 3 | 3 | 3 |
| Seeds | 7,42,91 | Như A | Như A |
| Train/holdout và routing | Cùng danh sách ID | Như A | Như A |
| Cây giải thích | depth=3, min leaf=2 | Như A | Như A |

Giữ k=3 và trọng số C=0,8 từ cấu hình minh họa cũ; không tối ưu sau khi xem kết quả.
Seed của agglomerative ở đây thay split và cây surrogate; agglomerative không có khởi tạo ngẫu nhiên.
Holdout 25% theo `GroupShuffleSplit` là theo nhóm source, không nhất thiết đúng 25% số hàng nói chung.
Train/holdout thực tế ở seed42 là 16/6,14/5,13/5.

Routing giống nhau, kể cả B: chọn bài có fail, test đầy đủ và parser không lỗi. B không dùng outcome
để tính khoảng cách, nhưng tập mẫu vẫn được chọn dựa trên lỗi test để giữ đúng bài toán và so sánh công bằng.
Không diễn giải B như clustering mọi chương trình mà hoàn toàn không cần test.

Script kiểm tra mọi split/routing A/B/C bằng assertion; A và C phải tái lập đúng features, assignments,
split và luật của kết quả cũ, đồng thời input hash khớp. Hash danh sách chọn bài và template review được lưu.

**Thiếu student ID:** giữ `student_id=null`; chỉ chống trùng source chính xác. Không phát hiện hết near-duplicate,
không biết các submission của cùng người và **không tuyên bố unseen-student generalization**.

## 4. Metric và cách đọc

- Silhouette train tính trên weighted Hamming của **từng không gian feature**; trả null nếu không xác định.
  Giá trị A/B/C khác geometry, không phải thước xếp hạng trực tiếp chất lượng misconception.
- Số input/eligible/train/holdout, số feature, số cluster, kích thước cluster train/holdout/tổng và singleton train.
- Rule fidelity train/holdout, baseline majority từ train; fidelity mô phỏng nhãn cluster, không phải accuracy lỗi.
- Khoảng cách holdout tới medoid và số tie; số cluster train vẫn có thể là 3 khi mọi holdout vào một cụm.
- ARI so với exact signatures train lấy từ outcomes thật ngay cả khi B không có test feature.
- ARI giữa phân hoạch A/B/C trên cùng train đo mức giống nhau, **không phải expert agreement**.
- Mean/min/max qua ba seed chỉ là độ nhạy mô tả. Không có kiểm định ý nghĩa, CI hoặc bằng chứng ba split độc lập.

Holdout gán bằng medoid train đóng băng, không re-cluster hay re-fit feature. Các luật có pseudo-label;
một cây dự đoán tốt cụm lớn không chứng minh misconception đúng.

## 5. Kết quả và diễn giải có giới hạn

27/27 lượt chạy có kết quả (3 bài × 3 cấu hình × 3 seed), mỗi lượt 3 cụm.
Xem [bảng đầy đủ](../results/itsp/abc_summary.md) và [JSON](../results/itsp/abc_summary.json).

- **Seed42:** A và C có cùng phân hoạch train cả ba bài (ARI=1), và cùng assignments holdout.
  Thêm structural flags ở trọng số 0,2 chưa thay nhóm trong cấu hình này.
- **Các seed khác:** A/C khác ở 2825 seed7 (ARI≈0,755) và 2833 seed91 (≈0,301), các trường hợp còn lại ARI=1.
  Có thay phân hoạch không có nghĩa là cải thiện; chưa có gold để quyết định.
- **B rất lệch kích thước:** seed42 là 14/1/1, 11/2/1, 11/1/1 theo thứ tự ba bài.
  2825 và 2812 gán mọi holdout vào cụm đa số nên fidelity=1 và majority=1.
  2833 fidelity=0,8 cũng bằng majority=0,8. Không suy B thắng vì fidelity cao hơn.
- Silhouette seed42 A/B/C lần lượt: 2825 = 0,742/0,875/0,696;
  2812 = 0,869/0,722/0,750; 2833 = 0,923/0,621/0,678.
  B cao nhất ở 2825 nhưng kèm hai singleton và nhiều lỗi khác nhau cùng cụm lớn.
- **Không kết luận OAV/structural tốt hơn.** Dữ liệu hiện cho thấy các flag presence còn thô,
  thêm chúng có thể giữ nguyên hoặc đổi phân hoạch mà chưa chứng minh giá trị sư phạm.
  Cũng chưa đủ để kết luận cấu trúc nói chung vô ích; chỉ kiểm tra extractor/weight hiện tại.

## 6. 17 mẫu: trạng thái validation ngoài

Mẫu được chọn bởi **C seed42 cũ**: 9 medoid train +8 holdout xa medoid nhất trong từng cụm có holdout.
Tie chọn ID lớn nhất từ điển, không random. 2812 có một cụm không có holdout nên chỉ có 5 mẫu;
2825/2833 mỗi bài 6. Script tái dựng chính xác tập mẫu và kiểm tra template không bị sửa.

Đã đọc đủ 17 source/log/bản sửa, ghi lỗi quan sát và misconception dự kiến với uncertainty;
đó là nhận xét kỹ thuật của trợ lý, không phải annotation chuyên gia. Xem [phân tích từng mẫu](itsp_expert_review.md).
Sáu cụm gốc ở 2825/2833 chứa nhiều cơ chế lỗi trong phần mẫu đã duyệt.

Giữ cùng 17 ID khi so A/B/C giúp đối chiếu, nhưng không loại thiên lệch do chọn mẫu từ C.
Ở seed42, B dồn 16/17 mẫu này vào cụm 0 **của từng bài riêng biệt**, chỉ 271975 vào B/2833/2.
Các cụm B khác không có mẫu review nên không thể đánh giá purity của chúng.

Purity và agreement hiện **N/A/null**, không phải 0. Cần codebook được thống nhất và annotation con người;
quyết định đơn nhãn/đa nhãn ảnh hưởng lớn đến methodology nên phải được giảng viên chốt trước khi tính.
Đã chuẩn bị công thức purity, quy trình chấm độc lập/adjudication và điều kiện raw agreement/Cohen kappa
trong tài liệu review. Không dùng 17 giả thuyết trợ lý làm gold, không ép nhiều nguyên nhân thành một nhãn.

## 7. Tái lập

```powershell
& .venv/Scripts/python.exe scripts/validate_itsp_abc.py
& .venv/Scripts/python.exe -m pytest -q
& .venv/Scripts/python.exe -m ruff check src tests scripts
```

Script giữ các file JSON thí nghiệm cũ và template review; tạo `results/itsp/abc/`,
`abc_summary.json/md`, `abc_review_assignments.json`, `expert_metric_readiness.json`,
và cập nhật phần có marker trong `results/itsp/summary.md`.
Nếu chạy lại runner 126 cấu hình cũ, chạy tiếp validation script để tái tạo phần A/B/C trong summary.

CLI mới hỗ trợ `--feature-mode structural`. Không đổi schema dữ liệu, downloader, preprocessing hay thuật toán.
5 test mới kiểm tra feature B không chứa test, trọng số/geometry, abstain khi cấu trúc hằng,
train-only selection, split đồng nhất và exact baseline đúng cho B. Kết quả toàn bộ: **48 tests +3 subtests pass**.
