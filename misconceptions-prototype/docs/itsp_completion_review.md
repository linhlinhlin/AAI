# Đối chiếu mục tiêu cuối và hoàn thiện kỹ thuật — 20/09/2026

Kiểm tra kỹ thuật mới nhất: **106 tests + 3 subtests pass; lint pass**. [Biên bản](../results/itsp/completion_verification.json). Đây là kiểm tra phần mềm, chưa phải human expert validation.

## Kết luận rà soát

Đã đối chiếu mô hình Submission/adapters, importer ITSP, FeatureSpace, split/clustering/cây luật, scorer và protocol review với ba phần của Đề 5: hình thức hóa OAV, gom cụm bài sai và sinh luật giải thích. **Prototype kỹ thuật đã có; chứng minh các cụm là misconception của người học chưa hoàn tất.** Điểm thiếu chính là evidence con người và tập kiểm chứng phù hợp, không phải thiếu một thuật toán clustering phức tạp.

| Yêu cầu cuối | Hiện trạng | Phần còn thiếu / điều kiện hoàn tất |
|---|---|---|
| Thay dataset mà không viết lại core | Submission/schema/adapters tách khỏi pipeline; JSON theo cohort; thiếu student ID được giữ null | Dataset giảng viên chưa có. Audit và adapter đặc thù khi nhận; không thể viết đúng mapper khi chưa biết schema thật. |
| OAV bám test fail | Test outcomes + 16 flags C; routing/parser và provenance có kiểm thử | Feature hiện tại thô; các feature quan hệ là thí nghiệm sau khi chốt thiết kế, không giả định có lợi. |
| Gom cụm phi giám sát | Exact signatures, weighted Hamming/average linkage; baseline K-means cũ | Đã chạy A/B/C; A=C seed42 ở cả ba bài. Chưa có bằng chứng cải thiện misconception clustering. |
| Gán bài chưa dùng fit vào nhóm | Holdout gán nearest train medoid, có tie policy | Đây là assignment vào cluster, không là phân loại misconception đã được xác thực. |
| Sinh luật | Cây depth=3, min leaf=2, support/precision/fidelity so nhãn cụm | Kết luận luật là cluster ID. Chỉ diễn giải thành misconception sau expert validation; ILA là quy nạp luật nếu thật sự cần. |
| Annotation chuyên gia | 17 phiếu, codebook draft, hai gói evidence offline, protocol | Cần hai người thật duyệt codebook và chấm; 0 human review/0 adjudication hiện tại. |
| Nhận nhiều file chuyên gia | **Đã bổ sung merge round-one có provenance và hàng đợi bất đồng** | Người điều phối xác thực danh tính, điều kiện mù, phiên bản và phạm vi review; công cụ không thay việc xác nhận này. |
| Phân tích expert theo cụm | **Đã bổ sung cluster details và xuất Markdown** | Chờ annotation để có nhãn/type counts; không tự suy cơ chế từ taxonomy rộng. |
| Kết luận khoa học | Đã quy định coverage, No/Unclear, gộp/tách sai và dữ liệu phát triển | Human annotation, lựa chọn mẫu mới và quy tắc nhãn cơ chế chưa chốt; pairwise mechanism metrics chưa triển khai. |
| Tái lập/bàn giao | Scripts, raw snapshot, kết quả, test suite và hướng dẫn | Bảo tồn hash/version khi thay dữ liệu; không dùng audit cũ như chứng nhận cho file đã đổi. |

## Các phần kỹ thuật hoàn thiện trong lượt này

### Nhập annotation vòng 1

`src/misconceptions/annotation_intake.py` và `scripts/merge_itsp_annotations.py` hợp nhất theo submission ID, không theo vị trí dòng. Mỗi file một reviewer thật, cùng codebook đã duyệt và cùng assignments SHA-256. Kiểm tra đầy đủ tập mẫu, từ chối reviewer lặp, AI records, codebook khác, annotation vòng 2 lẫn vào vòng 1 hoặc adjudication đã điền. Phiếu chưa hoàn tất được giữ đúng trạng thái; slot hoàn toàn trống không được tự gán reviewer.

Input không bị sửa. Output phải là file mới, không ghi đè snapshot có sẵn. Lưu đường dẫn và SHA-256 từng file nguồn cùng reviewer ID. Khi có bất đồng decision/type, lập queue để người thật giải quyết; kể cả hai người đồng ý, adjudication vẫn pending đến khi người có trách nhiệm xác nhận. Không bỏ phiếu đa số, không lấy confidence làm trọng số adjudication.

Lệnh mẫu (chỉ chạy khi file người thật tồn tại):

```powershell
.venv/Scripts/python.exe scripts/merge_itsp_annotations.py received/reviewer1_round1.json received/reviewer2_round1.json --output data/itsp/human_annotations_round1.json
.venv/Scripts/python.exe scripts/score_itsp_experts.py --annotations data/itsp/human_annotations_round1.json --validate-only
```

Lưu file round1 bất biến. Làm vòng 2/adjudication ở bản sao riêng, giữ nguyên lượt độc lập. Merge script chỉ phục vụ intake vòng 1, không tự hợp nhất các phiên bản vòng 2 và không xác nhận con người thay người điều phối. Các tên reviewer/file trong lệnh chỉ minh họa, không tạo reviewer ID thật.

### Báo cáo theo cụm

Scorer bổ sung tử số purity và `cluster_details` cho từng bài/A/B/C: mẫu được review trong cụm, decision counts, typed Yes, coverage, type counts, toàn bộ modal types khi hòa và cờ nhiều type quan sát được. Không chọn nhãn thắng khi hòa, không gọi cờ nhiều type là chứng minh mixed-cause, không tự gán outlier. Coverage chỉ trên tập mẫu review, không trên toàn cluster ITSP. Cụm không có mẫu review không được diễn giải là đồng nhất.

`scripts/report_itsp_experts.py` tính lại từ annotation và assignment có hash hợp lệ, loại AI rồi xuất Markdown mới, không ghi đè file cũ:

```powershell
.venv/Scripts/python.exe scripts/report_itsp_experts.py --annotations data/itsp/human_annotations_adjudicated.json --output results/itsp/human_cluster_review_final.md
```

File adjudicated là bản cần người thật xác nhận trong tương lai, chưa được tạo bằng giả định. [Báo cáo hiện tại](../results/itsp/human_cluster_review_2026-09-20.md) đã xuất từ dữ liệu hiện có: 0 human reviews, 0 adjudication, purity/agreement null. Các type/modal labels vẫn trống.

### Kiểm tra dữ liệu và hồi quy

Đã bổ sung từ chối assignment trùng ID, rỗng hoặc nhãn cụm không phải số nguyên không âm đủ A/B/C. Kiểm thử mới bao gồm merge khi thứ tự ID khác, bảo toàn input, pending, bất đồng, codebook khác, AI, reviewer trùng, nhầm vòng review, snapshot overwrite, purity với cụm chưa có nhãn và modal labels hòa. Nhãn trong tests là fixture tổng hợp, không được ghi vào dataset thật.

Không đổi feature extraction, routing, split, thuật toán, rule induction, 27 kết quả A/B/C, annotation thật hoặc gói reviewer. Module scorer chỉ thêm kiểm tra/chi tiết báo cáo; không thay công thức purity/kappa.

## Những việc chưa thể tự hoàn tất

1. **Codebook và ground truth:** cần hai chuyên gia thật duyệt taxonomy, xác nhận review độc lập và giải quyết bất đồng. Không tự tạo nhãn, người duyệt hoặc chữ ký; AI không thay người thật.
2. **Cơ chế lỗi:** cần chốt độ chi tiết và cách xử lý đa lỗi trước khi tính gộp/tách sai theo cặp. Nhãn type rộng chưa tự là mechanism label. Same-cause agreement còn cần người điều phối kiểm tra hai người đã xem cùng tập thành viên (ghi trong evidence).
3. **Kiểm chứng feature mới:** 59 bài đã xem là development/exposed. Cần chốt ngân sách/chủ đề/cỡ mẫu và tập chưa xem, sau đó mới thử ít feature quan hệ theo protocol. Không gọi holdout cũ là đánh giá độc lập mới.
4. **Dataset chính thức:** cần dữ liệu và schema thật từ giảng viên để kiểm tra khả năng chuyển dữ liệu và phạm vi khái quát hóa.
5. **Kết luận cuối:** chỉ sau các bước trên mới có thể kết luận mức độ gom cụm misconception và tác dụng của cấu trúc. Nếu không có cải thiện, báo kết quả âm. Không cần thêm UI/LLM/GNN hoặc thuật toán mới để che khoảng trống evidence.

Chưa thể đánh dấu toàn bộ đề tài hoàn tất. Các bước kỹ thuật có thể chuẩn bị mà không giả định nhãn đã được bổ sung; các quyết định khoa học có tác động lớn giữ chờ người phụ trách, theo yêu cầu không tự suy đoán methodology.
