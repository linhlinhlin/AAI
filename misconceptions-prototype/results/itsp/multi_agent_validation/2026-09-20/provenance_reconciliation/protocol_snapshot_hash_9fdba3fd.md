# Điều phối human expert review — ITSP

Trạng thái hiện tại: **0/17 mẫu có human review hoàn tất, 0 adjudication; purity, raw agreement và Cohen’s kappa đều null**. 17 lượt AI chỉ là tham khảo nội bộ, không phải ground truth và không được gửi kèm vòng chấm mù. Chưa gửi file hay liên hệ chuyên gia.

## Trước khi gửi

Gửi riêng [human_review_packet.zip](../results/itsp/human_review_packet.zip) cho từng chuyên gia. Gói chứa README, CODEBOOK dự thảo, annotations.json trống và 17 hồ sơ nguồn. Chuyên gia có thể mở toàn bộ evidence offline. `Main.c` gốc chứa cả mô tả và chương trình tham chiếu; `paired_correct.c` cũng là evidence được cung cấp cho mọi reviewer như nhau. Đây là đánh giá có bản sửa tham chiếu, không phải điều kiện chỉ xem buggy code. Mù ở đây là mù với nhãn AI, nhãn người khác và cluster.

Chốt codebook cùng chuyên gia trước vòng chấm như hướng dẫn trong gói; không tự ký duyệt. Dùng reviewer ID ổn định, không có tiền tố `ai:`, lưu danh sách người thật tương ứng ở nơi riêng. Muốn inter-rater agreement cần ít nhất hai chuyên gia chấm độc lập cùng mẫu, cùng codebook. Không cho họ xem `data/itsp/expert_annotations.json`, báo cáo AI, metrics, assignments hay context cụm trước khi khóa vòng 1.

17 mẫu có chủ đích, không phải mẫu ngẫu nhiên của 59 submissions. Không thay tập mẫu hoặc clustering để cải thiện purity. Dữ liệu không có student ID; không diễn giải thành generalization sang người học mới.

## 1. Nhận và validate — chưa tính metric

Lưu mỗi file nhận được nguyên trạng vào thư mục riêng theo reviewer/vòng, ghi SHA-256, thời điểm nhận và phiên bản codebook. Không ghi đè file nhận cũ. Kiểm tra người gửi là reviewer thật; tự động đọc prefix không xác thực được danh tính.

Chạy từ thư mục dự án với đường dẫn file nhận thực tế:

```powershell
.venv/Scripts/python.exe scripts/score_itsp_experts.py --annotations received/reviewer_01/round1.json --validate-only
```

Lệnh chỉ kiểm tra schema, đúng tập ID, problem ID, giá trị enum và SHA-256 assignment; không ghi metrics. Đối chiếu thêm bằng người điều phối: một reviewer nhất quán/file, đủ 17 phiếu hay ghi rõ coverage thiếu; không có AI record; đúng codebook đã chốt; pending không bị coi là Unclear; evidence có dòng code/test và không sao chép đáp án. Vòng 1 phải để same-cause A/B/C null và adjudication pending. Tuyên bố độc lập phải do reviewer xác nhận, không tự đổi false thành true. Chuyển lại reviewer nếu lỗi; không tự suy ra nhãn để hoàn tất phiếu.

## 2. Merge, khóa vòng độc lập, vòng cụm và adjudication

Tạo bản làm việc **human-only** `data/itsp/human_annotations.json` từ phiếu của chuyên gia; không lấy codebook AI làm mặc định. Merge theo `(submission_id, reviewer_id)`, không theo vị trí dòng. Một reviewer chỉ có một rating trên mỗi mẫu ở snapshot dùng tính agreement; trùng khóa hoặc hai giá trị khác nhau phải giải quyết bằng version/file nguồn, không tự ghi đè. Chỉ thêm các review người thật và codebook đã duyệt; giữ từng review ban đầu, cả các trường hợp No/Unclear. Lưu bảng provenance ánh xạ mỗi rating tới file nhận/hash.

Validate bản merge. Lưu snapshot vòng 1 bất biến; kiểm tra các quyết định/type/confidence/evidence của từng reviewer khớp bản nhận. Sau đó mới phát riêng assignment và [cluster context](../results/itsp/expert_cluster_context.md) cùng source/log/correct của toàn bộ thành viên được liên kết (59 mẫu). Đã có [gói vòng 2 offline](../results/itsp/human_review_round2_packet.zip), gồm mapping 17 mẫu, ngữ cảnh A/B/C và evidence đủ 59 thành viên. Chỉ phát sau khi khóa vòng 1; không gửi kèm gói chấm độc lập. 177 file đề/source/bản sửa, 395 test records và toàn bộ link đã được đối chiếu; không cần truy cập workspace để mở evidence. Không phát báo cáo AI. Vòng 2 bổ sung same-cause và evidence phạm vi; không sửa quyết định độc lập. Giữ snapshot vòng 2 và vòng 1 riêng để kiểm tra điều này.

Các chuyên gia thảo luận sau khi khóa lượt độc lập. Chỉ người thật chịu trách nhiệm mới điền `adjudication` với reviewer_id, quyết định, type, confidence, evidence giải thích bất đồng. Adjudication không phải một reviewer độc lập thứ ba và không thay thế hai lượt gốc. Bất đồng chưa giải quyết: giữ adjudication pending; đã xét nhưng evidence không đủ: complete/Unclear/type null. Nếu có nhiều cơ chế không chọn được nhãn chính, Yes/type null là hợp lệ. Không ép cụm thành một misconception.

## 3. Purity, rồi raw agreement, rồi Cohen’s kappa

Sau khi validate bản human-only và kiểm tra khóa lượt gốc:

```powershell
.venv/Scripts/python.exe scripts/score_itsp_experts.py --annotations data/itsp/human_annotations.json --validate-only
.venv/Scripts/python.exe scripts/score_itsp_experts.py --annotations data/itsp/human_annotations.json --output results/itsp/human_validation_metrics.json
```

Scorer ghi các chỉ số cùng một lần nhưng dùng nguồn khác nhau. Thứ tự đọc/báo cáo:

1. **Purity theo type**: chỉ adjudication Yes có type thuộc codebook human đã duyệt, riêng mỗi bài và A/B/C. Công thức `sum_c max_t n(c,t) / N_typed_yes`. Báo numerator/denominator, coverage từng cụm, số Yes/No/Unclear/pending và Yes chưa có type. Không dùng tất cả 17 làm mẫu số khi đã loại các quyết định không phải Yes. Chưa đủ điều kiện thì null.
2. **Raw agreement**: giao các review complete, `independent_blind_review=true` của từng cặp người trên cùng bài, trước adjudication. Decision gồm Yes/No/Unclear; type chỉ xét cặp cùng Yes có type theo codebook. `matches / n_paired`. Không dùng adjudication để tăng agreement. Báo số cặp mẫu và phân bố nhãn; cùng một reviewer chấm lại không thành người thứ hai.
3. **Cohen’s kappa**: danh nghĩa, không trọng số, trên cùng cặp và mẫu số với raw agreement: `(p_o-p_e)/(1-p_e)`, `p_e=sum_t p_left(t)*p_right(t)`. Không có cặp giữ null; nếu `p_e=1`, kappa null dù raw agreement có thể bằng 1. Confidence không là trọng số. Không gộp cluster ID giữa các bài hoặc đối chiếu trực tiếp ID với misconception type.

Same-cause agreement A/B/C là đồng thuận vòng 2 sau khi thấy cluster, phải báo riêng với nhãn misconception vòng 1. Scorer hiện chỉ xét same-cause từ các cặp đủ điều kiện độc lập vòng 1; không tự nới điều kiện để có thêm cặp. Các cặp reviewer dùng codebook khác nhau không được gộp tính type agreement.

## 4. Cập nhật Results/Discussion

**Results hiện tại:** human review 0/17, adjudication 0/17; purity/raw agreement/kappa null. Chỉ có thực nghiệm phân hoạch, fidelity với cluster và AI review tham khảo. Silhouette, stability, ARI giữa các phân hoạch và fidelity không đo đúng misconception.

**Discussion hiện tại:** quan sát kỹ thuật cho thấy có thể trộn nhiều cơ chế lỗi; chưa có xác nhận giáo dục. Không tuyên bố OAV tốt hơn, clustering đã được expert-validated hay AI là ground truth.

Khi có dữ liệu, cập nhật `docs/itsp_validation.md`, `docs/itsp_progress.md`, README và báo cáo kết quả cùng ngày/hash input, phiên bản codebook, số người/mẫu, phần adjudicated, per-problem/A/B/C metrics, coverage và các bất đồng chưa giải quyết. Tách bảng AI tham khảo khỏi bảng human. Không thay null bằng 0; không báo purity toàn cohort từ 17 mẫu có chủ đích. Nêu hạn chế taxonomy, coverage thấp, singleton, tính không mù, không có student ID và sai khác đề/oracle. Chỉ gọi là human expert validation trong đúng phạm vi đã được người thật đánh giá, không mặc nhiên là ground truth tuyệt đối.
