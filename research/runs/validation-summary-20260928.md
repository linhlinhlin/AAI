# Kiểm chứng baseline, ablation và luật — 28/09/2026

Đã chạy theo [protocol đóng băng trước thí nghiệm](../course-validation-protocol.json). Đây là nghiên cứu development/validation từ log lịch sử. Không chạy lại corpus C, không mở sealed test, không có nhãn giảng viên thật.

## Thiết kế

Exact test signature là đối chứng. K-means và average-linkage được chạy với outcomes, structural, combined, outcomes_stdout, combined_stdout; k=3; seed 7/42/91. Tất cả dùng cùng split lock toàn corpus. Đặc trưng và cây sâu tối đa 3 được fit trên train; validation gán theo medoid train bằng weighted Hamming, kể cả K-means. Không dùng centroid cho holdout; cần giữ điểm này khi diễn giải kết quả.

Thêm ablation structural giúp kiểm tra vai trò riêng của AST presence. Đây chưa phải AST quan hệ/def-use. Luật IF–THEN dự đoán ID cụm; precision/fidelity không phải độ đúng cơ chế lỗi hay nhận thức người học.

## Kết quả

### ITSP

99 lượt: **93 ok**, **6 abstained**. [Diagnostics](itsp-validation-20260928/diagnostics.json) · [Audit toàn vẹn](itsp-validation-20260928/integrity_audit.json) · [Manifest](itsp-validation-20260928/run_manifest.json).

| Thuật toán | Biểu diễn | Lượt ok | Fidelity luật | Baseline cụm đa số | Tỷ lệ hòa khoảng cách |
|---|---|---:|---:|---:|---:|
| agglomerative | combined | 9 | 0.778 | 0.444 | 0.389 |
| agglomerative | combined_stdout | 9 | 0.611 | 0.833 | 0.000 |
| agglomerative | outcomes | 9 | 1.000 | 0.667 | 0.167 |
| agglomerative | outcomes_stdout | 9 | 0.611 | 0.833 | 0.000 |
| agglomerative | structural | 6 | 0.833 | 0.833 | 0.000 |
| exact | outcomes | 9 | 0.667 | 0.444 | 0.000 |
| kmeans | combined | 9 | 0.722 | 0.556 | 0.167 |
| kmeans | combined_stdout | 9 | 0.611 | 0.833 | 0.000 |
| kmeans | outcomes | 9 | 0.889 | 0.444 | 0.167 |
| kmeans | outcomes_stdout | 9 | 0.556 | 0.833 | 0.000 |
| kmeans | structural | 6 | 0.889 | 0.833 | 0.000 |

19/93 lượt có fidelity thấp hơn baseline cụm đa số của chính lượt đó. Bảng lấy trung bình không trọng số trên các problem/seed có kết quả; không phải các quan sát thống kê độc lập. Không so trực tiếp fidelity giữa các biểu diễn để kết luận biểu diễn nào chẩn đoán tốt hơn, vì đích cụm thay đổi.

6 lượt structural abstain ở bài 2825 do không đủ biểu diễn train khác nhau cho k=3. ITSP thiếu định danh sinh viên và đã được dùng để phát triển; không dùng làm benchmark sinh viên độc lập. ARI giữa seed bằng 1 ở các cặp có kết quả, nhưng validation rất nhỏ nên không suy rộng.

### C-Pack-IPAs

825 lượt: **774 ok**, **51 abstained**. [Diagnostics](cpack-validation-20260928/diagnostics.json) · [Audit toàn vẹn](cpack-validation-20260928/integrity_audit.json) · [Manifest](cpack-validation-20260928/run_manifest.json).

| Thuật toán | Biểu diễn | Lượt ok | Fidelity luật | Baseline cụm đa số | Tỷ lệ hòa khoảng cách |
|---|---|---:|---:|---:|---:|
| agglomerative | combined | 75 | 0.926 | 0.687 | 0.022 |
| agglomerative | combined_stdout | 75 | 0.929 | 0.563 | 0.009 |
| agglomerative | outcomes | 51 | 0.981 | 0.669 | 0.028 |
| agglomerative | outcomes_stdout | 75 | 0.920 | 0.563 | 0.020 |
| agglomerative | structural | 75 | 0.952 | 0.784 | 0.091 |
| exact | outcomes | 72 | 0.934 | 0.722 | 0.024 |
| kmeans | combined | 75 | 0.947 | 0.566 | 0.044 |
| kmeans | combined_stdout | 75 | 0.935 | 0.530 | 0.019 |
| kmeans | outcomes | 51 | 0.985 | 0.639 | 0.042 |
| kmeans | outcomes_stdout | 75 | 0.921 | 0.531 | 0.025 |
| kmeans | structural | 75 | 0.933 | 0.475 | 0.078 |

25/774 lượt có fidelity thấp hơn baseline cụm đa số của chính lượt đó. Bảng lấy trung bình không trọng số trên các problem/seed có kết quả; không phải các quan sát thống kê độc lập. Không so trực tiếp fidelity giữa các biểu diễn để kết luận biểu diễn nào chẩn đoán tốt hơn, vì đích cụm thay đổi.

K-means combined_stdout: ARI validation giữa seed trung bình trên 25 bài = **0.962**, thấp nhất = **0.498**. Độ ổn định cao không xác nhận ý nghĩa của cụm. 42 lượt không đủ mẫu/biểu diễn khác nhau cho k=3; 9 lượt có đặc trưng train giống hệt.

## Đánh giá giảng viên

Hai gói chưa điền đã tạo: ITSP 48 bài; C-Pack-IPAs 150 bài (tối đa 3 train + 3 validation/bài tập, thứ tự hash độc lập cụm). Gói nằm trong `.cache/teacher-validation-itsp-20260928` và `.cache/teacher-validation-cpack-20260928` tại root dự án. C-Pack là pilot nhỏ, không đại diện toàn corpus; có thể tạo gói mới lớn hơn trước khi gán nhãn.

Hai lần chạy evaluator với mẫu chưa điền đều trả `waiting_for_teacher_labels`. Không thay thế bằng AI hoặc nhận xét đã xem dashboard. ARI/pairwise precision/recall/F1 với gold, precision cơ chế của luật và đánh giá nhận thức đều chưa có giá trị. Luật chỉ ánh xạ cụm sang cơ chế bằng gold train; hòa phiếu hoặc thiếu gold train thì abstain.

Xem [hướng dẫn nhập nhãn, phân xử và chạy đánh giá](../../docs/teacher_validation.md). Các fixture nhãn trong test chỉ kiểm tra phần mềm, không phải nhãn giảng viên.

## Kết luận và bước nghiên cứu tiếp

1. Pipeline có thể tái lập và audit; baseline đơn giản vẫn cần thiết. Chưa có bằng chứng rằng thêm stdout/AST luôn cải thiện chẩn đoán.
2. Thu nhãn độc lập trước khi chọn mô hình theo chất lượng cơ chế. Không sửa feature bằng việc xem sealed test.
3. Với mục tiêu công bố, còn cần khoảng tin cậy theo sinh viên/thành phần liên thông, kiểm tra near-duplicate, cross-problem, oracle audit và protocol final. Chưa thực hiện các mục này trong đợt kiểm chứng môn học.
4. Xác nhận misconception cần lời giải thích của người học và kiểm tra tiếp, không chỉ code sai. Nếu chưa thu được thì giữ `unassessed`.

## Nguồn định nghĩa chỉ số

- [scikit-learn: clustering evaluation](https://scikit-learn.org/stable/modules/clustering.html#clustering-performance-evaluation): ARI so hai phân hoạch, không phụ thuộc số hiệu nhãn.
- [scikit-learn: DecisionTreeClassifier.apply](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html): truy lá cây để kiểm tra membership, support và precision từng luật.
