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
