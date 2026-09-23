# ITSP — kết quả thí nghiệm

Kiểm tra kỹ thuật mới nhất: **106 tests + 3 subtests pass; lint pass**. [Biên bản](completion_verification.json). Đây là kiểm tra phần mềm, chưa phải human expert validation.

## Cập nhật hoàn thiện kỹ thuật — 20/09/2026

Đã [đối chiếu toàn bộ mục tiêu và phần còn thiếu](../../docs/itsp_completion_review.md). Bổ sung intake hợp nhất phiếu chuyên gia vòng 1 có hash/provenance, không ghi đè snapshot hoặc tự adjudicate; scorer có coverage/nhãn đồng hạng theo cụm và công cụ xuất Markdown human-only. Từ chối assignment trùng/không hợp lệ. Baseline, feature và A/B/C giữ nguyên. Chưa có human annotation, expert purity/agreement vẫn null; bước cần chuyên gia và mẫu mới được ghi rõ, không tuyên bố đề tài đã hoàn tất.


## Sau phản biện — 20/09/2026

[Protocol kiểm chứng đã cập nhật](../../docs/itsp_validation_revision.md): tách biểu hiện lỗi → cơ chế lỗi → giả thuyết misconception; giữ baseline và cây luật nông. ILA thuộc quy nạp luật, không gọi là clustering phi giám sát. Kiểm tra lại đủ 59 submissions: A=C ở seed42 (ARI=1 từng bài); vector combined của 271173/271188 trùng nhau. Chưa có bằng chứng cấu trúc hiện tại cải thiện phân hoạch; chưa phủ định mọi cấu trúc khác.

Đánh dấu toàn bộ 59 bài đã xuất hiện trong hồ sơ là dữ liệu phát triển/đã xem cho thí nghiệm feature mới; chưa chọn mẫu đánh giá độc lập mới hoặc triển khai feature quan hệ. Packet chính đã gắn nhãn “Vòng 2 — có hiển thị cụm”; gói vòng 1 giữ nguyên. Hai chuyên gia thật cần chốt codebook và chấm độc lập. Báo purity kèm coverage, No/Unclear và phân tích gộp/tách sai; chỉ số cặp cần nhãn cơ chế phù hợp, chưa tự tính trên AI. Expert validation tiếp tục chờ annotation, các metric vẫn null.


## Kiểm tra hồ sơ và hoàn thiện vòng 2

Đối chiếu lại gói vòng 1: đủ **17 mẫu, 51 file đề/source/bản sửa, 113 test records**, phiếu trống hợp lệ, ZIP khớp nội dung và link offline hoạt động. Codebook vẫn là dự thảo chờ chuyên gia xác nhận.

Bổ sung [gói vòng 2 offline](human_review_round2_packet.zip) để khắc phục ngữ cảnh cụm dùng link nội bộ: **59 thành viên, 177 file đề/source/bản sửa, 395 test records**, mapping 17 phiếu và 27 cụm theo bài/A/B/C seed42. Chỉ phát sau khi khóa vòng 1. Không thêm mẫu annotation, không gán nhãn mới, không đổi thuật toán. Đã xác nhận 37 file nguồn/kết quả/annotation/gói vòng 1 giữ nguyên. [Biên bản kiểm tra](review_handoff_audit.json).

Hồ sơ đủ để chuyển sang bước chuyên gia duyệt codebook và đánh giá độc lập; chưa có human annotation để hoàn tất expert validation. Chưa gửi hồ sơ hoặc liên hệ chuyên gia. Kiểm tra sau bàn giao: **64 tests + 3 subtests pass; lint pass**. Chạy lại scorer xác nhận 0 human reviews, 0 adjudication; expert purity/agreement vẫn null.


## Bàn giao đánh giá độc lập — 19/09/2026

Đã tạo [bộ phiếu riêng cho chuyên gia](human_review/README.md) gồm 17 hồ sơ (đề, source, bản sửa, log lịch sử) và `annotations.json` trống. Bộ bàn giao không chứa nhãn/giả thuyết AI, codebook AI hoặc assignment cluster để hỗ trợ vòng đánh giá độc lập. Mỗi chuyên gia nhận một bản riêng; lưu kết quả vòng 1 trước khi cung cấp ngữ cảnh cụm ở vòng 2. Khi nhận file, đối chiếu ID và SHA-256 assignment, hợp nhất các lượt người đánh giá vào file chính, giữ nguyên nhãn AI và provenance; không thay AI bằng human chỉ bằng đổi reviewer_id.

Hiện có 17 AI reviews tham khảo nhưng **0 human reviews hoàn tất, 0 adjudication**; expert purity/agreement vẫn null. Cần người đánh giá thật và codebook được phê duyệt để hoàn tất validation. Chưa gửi phiếu cho bất kỳ ai; chỉ chuẩn bị file trong workspace. [Tải bộ phiếu ZIP](human_review_packet.zip). Kiểm tra bàn giao: 17/17 log khớp dữ liệu hiện có, 51 file source/đề/bản sửa khớp SHA-256; ZIP không lỗi. **63 tests + 3 subtests pass; lint pass.**


## Expert validation — chờ annotation (19/09/2026)

Đã chuẩn bị [17 phiếu và hướng dẫn chuyên gia](../../docs/itsp_expert_annotation_template.md), [file nhập annotation](../../data/itsp/expert_annotations.json) và script `scripts/score_itsp_experts.py`. Hiện **0 lượt hoàn tất, 0 adjudication; cluster purity = null, agreement = null** trong [kết quả chấm](expert_validation_metrics.json). Các giả thuyết kỹ thuật trước đây không phải expert labels và không được đưa vào scorer.

Codebook và chính sách nhãn chờ chuyên gia thống nhất; chỉ tính purity theo loại trên mẫu Yes có loại đã adjudicate khi codebook được duyệt. Báo riêng từng bài/A/B/C, kèm mẫu số và coverage; No/Unclear không được coi là một loại misconception. Agreement gồm raw agreement và Cohen kappa theo cặp người đánh giá độc lập; thiếu cặp hoặc kappa không xác định giữ null. Ngữ cảnh cụm chỉ mở ở vòng hai. Chưa thể kết luận chất lượng misconception clustering hay OAV tốt hơn.

17 mẫu được chọn có chủ đích theo C gốc (9 medoid + 8 holdout xa nhất), không đại diện toàn cohort. ITSP không có student ID: không tạo ID giả, không tuyên bố unseen-student generalization. Chỉ bổ sung công cụ annotation/scoring ngoại tuyến, không thay đổi pipeline hoặc clustering A/B/C hiện có. Kiểm tra: **61 tests + 3 subtests pass**, `ruff check .` pass; SHA-256 xác nhận toàn bộ file source cũ và 27 kết quả A/B/C giữ nguyên.


Không dùng silhouette hoặc fidelity để tuyên bố độ chính xác misconception.
Mỗi dòng dưới đây là seed=42; JSON giữ toàn bộ seeds 7, 42, 91 và mọi lần abstain.
Exact bỏ qua k; trọng số trong bảng là cấu hình. Outcomes-only luôn dành toàn bộ trọng số cho test.

| Bài | Thuật toán | Feature | k | Trọng số test | Trạng thái | Silhouette train | Fidelity holdout | Majority |
|---|---|---|---:|---:|---|---:|---:|---:|
| 2825 | exact | outcomes | 2 | 1.0 | ok | 0.750 | 0.500 | 0.333 |
| 2825 | agglomerative | outcomes | 2 | 0.8 | ok | 0.517 | 0.833 | 0.833 |
| 2825 | agglomerative | outcomes | 3 | 0.8 | ok | 0.742 | 0.833 | 0.500 |
| 2825 | agglomerative | outcomes | 4 | 0.8 | ok | 0.704 | 0.667 | 0.500 |
| 2825 | agglomerative | combined | 2 | 0.8 | ok | 0.480 | 0.833 | 0.833 |
| 2825 | agglomerative | combined | 3 | 0.8 | ok | 0.696 | 0.833 | 0.500 |
| 2825 | agglomerative | combined | 4 | 0.8 | ok | 0.650 | 0.667 | 0.500 |
| 2825 | kmeans | outcomes | 2 | 0.8 | ok | 0.711 | 1.000 | 0.667 |
| 2825 | kmeans | outcomes | 3 | 0.8 | ok | 0.742 | 0.833 | 0.500 |
| 2825 | kmeans | outcomes | 4 | 0.8 | ok | 0.704 | 0.667 | 0.500 |
| 2825 | kmeans | combined | 2 | 0.8 | ok | 0.669 | 1.000 | 0.667 |
| 2825 | kmeans | combined | 3 | 0.8 | ok | 0.696 | 0.833 | 0.500 |
| 2825 | kmeans | combined | 4 | 0.8 | ok | 0.639 | 0.833 | 0.333 |
| 2825 | agglomerative | combined | 3 | 0.6 | ok | 0.633 | 0.833 | 0.500 |
| 2812 | exact | outcomes | 2 | 1.0 | ok | 0.857 | 0.200 | 0.200 |
| 2812 | agglomerative | outcomes | 2 | 0.8 | ok | 0.919 | 0.800 | 0.800 |
| 2812 | agglomerative | outcomes | 3 | 0.8 | ok | 0.869 | 0.200 | 0.200 |
| 2812 | agglomerative | outcomes | 4 | 0.8 | ok | 0.857 | 0.200 | 0.200 |
| 2812 | agglomerative | combined | 2 | 0.8 | ok | 0.865 | 0.800 | 0.800 |
| 2812 | agglomerative | combined | 3 | 0.8 | ok | 0.750 | 0.200 | 0.200 |
| 2812 | agglomerative | combined | 4 | 0.8 | ok | 0.697 | 0.200 | 0.200 |
| 2812 | kmeans | outcomes | 2 | 0.8 | ok | 0.919 | 0.800 | 0.800 |
| 2812 | kmeans | outcomes | 3 | 0.8 | ok | 0.869 | 0.200 | 0.200 |
| 2812 | kmeans | outcomes | 4 | 0.8 | ok | 0.857 | 0.200 | 0.200 |
| 2812 | kmeans | combined | 2 | 0.8 | ok | 0.865 | 0.800 | 0.800 |
| 2812 | kmeans | combined | 3 | 0.8 | ok | 0.750 | 0.200 | 0.200 |
| 2812 | kmeans | combined | 4 | 0.8 | ok | 0.697 | 0.200 | 0.200 |
| 2812 | agglomerative | combined | 3 | 0.6 | ok | 0.676 | 0.600 | 0.800 |
| 2833 | exact | outcomes | 2 | 1.0 | ok | 0.923 | 0.800 | 0.600 |
| 2833 | agglomerative | outcomes | 2 | 0.8 | ok | 0.780 | 0.800 | 0.800 |
| 2833 | agglomerative | outcomes | 3 | 0.8 | ok | 0.923 | 0.800 | 0.600 |
| 2833 | agglomerative | outcomes | 4 | 0.8 | abstained | — | — | — |
| 2833 | agglomerative | combined | 2 | 0.8 | ok | 0.690 | 0.800 | 0.800 |
| 2833 | agglomerative | combined | 3 | 0.8 | ok | 0.678 | 0.800 | 0.600 |
| 2833 | agglomerative | combined | 4 | 0.8 | ok | 0.708 | 0.800 | 0.600 |
| 2833 | kmeans | outcomes | 2 | 0.8 | ok | 0.712 | 1.000 | 0.800 |
| 2833 | kmeans | outcomes | 3 | 0.8 | ok | 0.923 | 0.800 | 0.600 |
| 2833 | kmeans | outcomes | 4 | 0.8 | abstained | — | — | — |
| 2833 | kmeans | combined | 2 | 0.8 | ok | 0.560 | 1.000 | 0.800 |
| 2833 | kmeans | combined | 3 | 0.8 | ok | 0.678 | 0.800 | 0.600 |
| 2833 | kmeans | combined | 4 | 0.8 | ok | 0.708 | 0.800 | 0.600 |
| 2833 | agglomerative | combined | 3 | 0.6 | ok | 0.534 | 0.800 | 0.800 |

<!-- ABC_VALIDATION_START -->
## Validation A/B/C trên cùng dữ liệu

Giữ 59 mẫu thuộc ba bài cũ; agglomerative average-linkage, k=3, seeds 7/42/91, holdout 25% theo nhóm source.
A = test only; B = structural only; C = test 0,8 + structural 0,2. Feature cấu trúc hằng chỉ bỏ theo train.
OAV là cách biểu diễn, không phải đồng nghĩa với structural. Không có ID sinh viên hoặc expert gold.
Silhouette dùng không gian riêng từng cấu hình; không xếp hạng chất lượng misconception bằng các số này.

Bảng seed=42 (cấu hình minh họa có sẵn, không chọn lại theo kết quả):

| Bài | Arm | Input/eligible | Train/holdout | Features | Clusters | Kích thước train | Silhouette | Fidelity / majority |
|---|---|---|---|---:|---:|---|---:|---|
| 2825 | A | 22/22 | 16/6 | 7 | 3 | {0: 5, 1: 1, 2: 10} | 0.742 | 0.833 / 0.500 |
| 2825 | B | 22/22 | 16/6 | 3 | 3 | {0: 14, 1: 1, 2: 1} | 0.875 | 1.000 / 1.000 |
| 2825 | C | 22/22 | 16/6 | 10 | 3 | {0: 5, 1: 1, 2: 10} | 0.696 | 0.833 / 0.500 |
| 2812 | A | 19/19 | 14/5 | 7 | 3 | {0: 11, 1: 2, 2: 1} | 0.869 | 0.200 / 0.200 |
| 2812 | B | 19/19 | 14/5 | 4 | 3 | {0: 11, 1: 2, 2: 1} | 0.722 | 1.000 / 1.000 |
| 2812 | C | 19/19 | 14/5 | 11 | 3 | {0: 11, 1: 2, 2: 1} | 0.750 | 0.200 / 0.200 |
| 2833 | A | 18/18 | 13/5 | 6 | 3 | {0: 5, 1: 1, 2: 7} | 0.923 | 0.800 / 0.600 |
| 2833 | B | 18/18 | 13/5 | 6 | 3 | {0: 11, 1: 1, 2: 1} | 0.621 | 0.800 / 0.800 |
| 2833 | C | 18/18 | 13/5 | 12 | 3 | {0: 5, 1: 1, 2: 7} | 0.678 | 0.800 / 0.600 |

### Độ nhạy qua 3 seed

Mean [min, max] là mô tả ba split, không phải confidence interval hoặc ba lớp độc lập.

| Bài | Arm | Runs ok/total | Silhouette mean [min,max] | Holdout fidelity mean [min,max] |
|---|---|---|---|---|
| 2825 | A | 3/3 | 0.731 [0.721, 0.742] | 0.889 [0.833, 1.000] |
| 2825 | B | 3/3 | 0.875 [0.875, 0.875] | 1.000 [1.000, 1.000] |
| 2825 | C | 3/3 | 0.688 [0.675, 0.696] | 0.889 [0.833, 1.000] |
| 2812 | A | 3/3 | 0.790 [0.723, 0.869] | 0.733 [0.200, 1.000] |
| 2812 | B | 3/3 | 0.764 [0.722, 0.821] | 1.000 [1.000, 1.000] |
| 2812 | C | 3/3 | 0.709 [0.668, 0.750] | 0.667 [0.200, 1.000] |
| 2833 | A | 3/3 | 0.897 [0.885, 0.923] | 0.933 [0.800, 1.000] |
| 2833 | B | 3/3 | 0.717 [0.621, 0.808] | 0.867 [0.800, 1.000] |
| 2833 | C | 3/3 | 0.618 [0.451, 0.724] | 0.800 [0.800, 0.800] |

### Diễn giải

Seed42: A và C cho cùng phân hoạch train/holdout cả ba bài; B tạo cụm train lớn kèm cụm nhỏ/singleton.
Fidelity B seed42 bằng baseline majority cả ba bài (1,0; 1,0; 0,8), nên điểm cao không chứng minh chẩn đoán tốt.
A/C khác phân hoạch ở 2825 seed7 và 2833 seed91; chưa có gold để xác định thay đổi nào hữu ích.
Không kết luận structural/OAV tốt hơn. Giới hạn áp dụng cho feature presence và trọng số hiện tại.
[Protocol, feature, metric và limitations](../../docs/itsp_validation.md).

[JSON đầy đủ](abc_summary.json) · [Assignments 17 mẫu](abc_review_assignments.json) · [Phân tích review](../../docs/itsp_expert_review.md) · [Điều kiện tính purity/agreement](expert_metric_readiness.json)

Purity và agreement chuyên gia hiện là N/A: 17 mẫu vẫn chờ annotation; không dùng giả thuyết của trợ lý làm gold.
Train partition ARI trong JSON chỉ đo mức giống nhau giữa phân hoạch; không phải inter-rater agreement.
<!-- ABC_VALIDATION_END -->
