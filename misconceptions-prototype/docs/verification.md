# Kết quả thực hiện và review

## Bổ sung validation A/B/C — 19/09/2026

Toàn bộ suite sau thay đổi: **48 passed, 3 subtests passed**. Năm test mới kiểm tra structural-only
không chứa outcome, trọng số/Hamming–one-hot, không fallback khi cấu trúc hằng, train-only selection,
split/routing đồng nhất và ARI so baseline outcome thật với cả agglomerative/K-means.
27 lượt A/B/C đều ok; assertion xác minh A/C khớp kết quả cũ và giữ nguyên 17 mẫu/template review.
Review độc lập xác nhận toàn bộ 27 ARI baseline và các split; xem [protocol validation](itsp_validation.md).
Các con số 43 tests/126 lượt trong phần dưới thuộc mốc ITSP trước bổ sung structural-only.

Kiểm tra ngày **19/09/2026**, Windows, Python 3.12. Phiên bản thư viện chính đã chạy: NumPy 2.5.3, SciPy 1.18.1, scikit-learn 1.9.1; dependency đầy đủ ở `requirements-lock.txt`. Tất cả kiểm tra dưới đây thực sự được chạy trong phiên, không phải kết quả dự kiến.

## Phần mềm

- `pytest -q`: **43 passed, 3 subtests passed** sau tích hợp ITSP. Bao gồm OAV không chứa danh tính/nguồn nhãn, missing ≠ pass, unknown AST, lựa chọn feature chỉ trên train, Hamming/one-hot tương đương, group transitivity, chống leakage qua record bị loại, determinism cả ba phương pháp, abstention, routing bài đúng, schema/duplicate, nullable ID v2, parser C, mapping log không theo thứ tự, từ chối log sai và provenance bị sửa/thêm file, CLI thay nguồn.
- `ruff check src tests scripts`: **All checks passed**; đã format code.
- `pip install --no-deps --no-build-isolation -e .`: thành công; entrypoint module chạy được sau cài đặt.
- `pip check`: **No broken requirements found**.
- CLI ghi `results/demo_report.json`: thành công, có config, input/manifest SHA-256, package versions và evidence.
- `scripts/run_ablation.py`: 12 lượt chạy thành công, 4 cấu hình × 3 seed (7, 42, 91).

## ITSP công khai — bổ sung cùng ngày

Môi trường thêm tree-sitter 0.26.0, tree-sitter-c 0.24.2. Download khóa commit và kiểm tra 2.368 file;
prepare xác minh toàn bộ hash và tập file. 649/661 bài nhập, 648 eligible, 1 parser failure, 12 bài
loại vì số test không khớp. Cả 74 cohort đều còn dữ liệu; bài 3294 giữ 5/14 mẫu.

`scripts/run_itsp_experiments.py`: 126 lần chạy trên 2825/2812/2833; 124 ok, 2 abstained theo kiểm tra
k/độ đa dạng train. JSON có input/manifest hash, package versions, routing, identity limitation,
assignments, OAV, medoid và rule fidelity so với baseline majority. Template annotation chưa có nhãn.
CLI chạy trực tiếp trên 2825 cho split, features, assignments và explanation giống batch runner;
đã kiểm tra bằng assertion trên hai artifact JSON. Template annotation chứa 17 mẫu cần chuyên gia duyệt.

Đã đọc 9 medoid và các phản ví dụ: [nhật ký ITSP](itsp_progress.md), [case review 2825](itsp_case_review.md).
Phát hiện/sửa bổ sung: không giả danh tính từ assignment-ID; không nối tất cả null ID thành một nhóm;
không cho AST trọng số 0 vào cây luật; loại raw file ngoài provenance; giữ bằng chứng lỗi output/runtime
không rõ trong audit. Không chạy code sinh viên hoặc xác nhận nhãn misconception.

## Kết quả fixture, không phải benchmark giáo dục

52 record = 48 mẫu sai có đầy đủ outcome + 1 thiếu test + 1 runtime + 1 đúng + 1 parse error. Seed 42 chia 36 train/12 holdout trong cohort đủ evidence. Dữ liệu là ba công thức lỗi với biến thể đổi tên, nên không có độ đa dạng của code sinh viên thật.

| Cấu hình | Số cụm ở cả 3 seed | Silhouette train | Fidelity luật holdout |
|---|---:|---:|---:|
| Exact outcomes | 2 | 1,0 | 1,0 |
| Agglomerative outcomes, k=2 | 2 | 1,0 | 1,0 |
| Agglomerative combined, k=3 | 3 | 1,0 | 1,0 |
| K-means combined, k=3 | 3 | 1,0 | 1,0 |

**Điểm 1,0 ở đây không phải 100% chính xác phát hiện misconception.** Các mẫu cùng công thức gần như trùng nhau, chữ ký trong mỗi nhóm đồng nhất. `square` và `odd_only` trùng outcome trên sáu test mặc dù output sai/cơ chế khác nhau. AST `range` giúp phân biệt hai mẫu trong fixture nhưng không chứng minh khái quát hóa. k của các cấu hình được đặt để minh họa, không được chọn bởi một benchmark độc lập. Kết quả ITSP được lưu riêng, không trộn với fixture.

Cross-split ARI trên 26 mẫu train chung giữa seed 7 và 42 bằng 1,0 trong cả bốn cấu hình; đây là kiểm tra độ nhạy nhỏ, không phải bootstrap stability trên quần thể. Thời gian pipeline mỗi lượt khoảng 0,01–0,11 giây sau import trên máy phiên này; không gồm cài môi trường, thu thập dữ liệu, biên dịch hay chạy test. Xem giá trị chính xác ở `results/ablation_summary.json`.

## Các vấn đề đã phát hiện và sửa

1. **Leakage qua record bị loại:** tính connected components sau filtering có thể cắt mất một cầu nối student/source. Đã tính groups trên toàn bộ input trước khi chọn eligible; có test hồi quy.
2. **AST bị parse nhiều lần trong transform:** chuyển sang trích một lần mỗi record rồi lấy thuộc tính.
3. **Baseline exact bị trộn geometry AST khi gán holdout:** exact dùng hiệu lực `outcomes`; cấu hình hiệu lực được ghi.
4. **Nhầm parse error thành missing:** routing ưu tiên parse error để thống kê chính xác.
5. **Thiếu metadata tái lập:** ghi k, split fraction, test weight, feature mode, metric silhouette, seed, package và hash input trong CLI artifact.
6. **Distinct patterns trên feature trọng số 0:** đếm trên các chiều có trọng số dương để không chấp nhận k giả tạo.
7. **Manifest không phải object:** adapter từ chối bằng ValueError; thêm regression test.

Review phương pháp còn sửa cách dùng ILA, phân biệt Hamming với K-means và không gán cluster ID thành misconception. Tham khảo `method_review.md` để thấy lập luận độc lập và các đề xuất chưa triển khai; tài liệu đó là phản biện thiết kế, không phải danh sách tính năng đã có.

## Giới hạn còn lại

Chưa kiểm nghiệm hiệu quả sư phạm, chưa có expert labels, extractor C++/Java, phân tích ngữ nghĩa C, runner sandbox, source-span evidence, ngưỡng OOD/từ chối gán holdout, hoặc kiểm soát near-duplicate đầy đủ. ITSP thiếu ID người học nên không loại được leakage theo sinh viên; phải chốt mapping và chính sách chọn attempt khi có dữ liệu chính thức. Chưa có nhận diện multi-bug; chưa tune k/trọng số trên validation; chưa đánh giá bất định với confidence interval.

Đây là prototype offline có ranh giới rõ, không phải công cụ tự động chẩn đoán sinh viên. Không cần các chức năng còn thiếu để xác minh pipeline và chuẩn bị thay dataset; cần bổ sung chúng theo evidence và nhu cầu của dữ liệu thật.
