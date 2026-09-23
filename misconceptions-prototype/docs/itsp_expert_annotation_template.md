# Phiếu expert annotation — 17 mẫu ITSP

**Bàn giao vòng độc lập:** dùng [bộ phiếu không chứa nhãn AI](../results/itsp/human_review/README.md), phát một bản riêng cho mỗi chuyên gia. File chính có nhãn AI nên chỉ người điều phối mở khi hợp nhất kết quả.

Trạng thái: **chờ human expert**, chưa có human expert labels. Đã bổ sung 17 AI reviews (prefix `ai:`) ngày 19/09/2026; không phải ground truth. Slot human và adjudication vẫn pending; bảng trống dưới đây dành cho human review. Kết quả AI được báo riêng trong `ai_annotation` của metric JSON và trong `itsp_expert_review.md`. File nhập chính thức: [expert_annotations.json](../data/itsp/expert_annotations.json). Không nhập vào template lịch sử `results/itsp/annotation_template.jsonl`.

Tài liệu này dành cho điều phối nội bộ. Để chấm mù, chỉ gửi `human_review_packet.zip`, không gửi JSON chính đang chứa AI reviews. Xem [quy trình nhận và xử lý file](itsp_human_review_protocol.md).

## Quy trình

1. Mỗi chuyên gia đọc đề `Main.c`, source lỗi, log từng test và bản sửa cùng cặp. Không đọc `itsp_expert_review.md`, `review_hypotheses.json`, kết quả cụm hay annotation của người khác trước khi hoàn tất vòng độc lập. Nếu đã xem, giữ `independent_blind_review=false`; lượt đó không dùng tính inter-rater agreement độc lập.
2. Điền một đối tượng `reviews` cho mỗi người/mẫu; sao chép slot trống nếu có người thứ hai. `reviewer_id` là mã của người đánh giá thật, **không phải student ID**. Chưa đánh giá giữ `status=pending` và các trường `null`. Chỉ đặt `complete` khi có decision, confidence, reviewer_id và evidence. Không dùng `Unclear` thay cho chưa đánh giá.
3. Chuyên gia thống nhất codebook và quy tắc chọn nhãn chính trước khi tính purity theo loại. `approved_by` và `label_policy` vẫn null; `version` và `misconception_types` hiện chứa codebook human dự thảo tổng quát, chưa được chuyên gia phê duyệt. Định nghĩa nằm trong `results/itsp/human_review/CODEBOOK.md`, không chứa nhãn AI theo mẫu. Script hỗ trợ `single_primary` khi chuyên gia chấp thuận; nếu cần đa nhãn, dừng tính purity và thống nhất protocol riêng, không tự ép thành một nhãn. `Yes` chưa xác định được loại có thể để type `null`, được báo thiếu coverage.
4. Khóa vòng đánh giá độc lập, rồi mở [toàn bộ thành viên các cụm](../results/itsp/expert_cluster_context.md) và [mapping 17 mẫu](../results/itsp/abc_review_assignments.json). Điền `same_cause_as_cluster` riêng A/B/C. Sau đó thảo luận, ghi kết luận thống nhất vào `adjudication`, kèm người chịu trách nhiệm và evidence; không ghi đè các lượt độc lập. Một chuyên gia chưa đủ tính inter-rater agreement.

## Các trường trên mỗi phiếu

| Trường | Giá trị / cách hiểu |
|---|---|
| misconception | `Yes`: bằng chứng ủng hộ hiểu sai khái niệm; `No`: chuyên gia đánh giá không phải misconception; `Unclear`: đã xem nhưng chưa đủ bằng chứng phân biệt hiểu sai với sơ suất. |
| misconception_type | Mã loại do chuyên gia thống nhất; chưa biết giữ `null`; No/Unclear luôn `null`. Không lấy giả thuyết của trợ lý làm nhãn. |
| confidence | Số nguyên 1–5: 1 rất thấp, 2 thấp, 3 vừa, 4 cao, 5 rất cao; tự tin vào quyết định đã ghi, không phải xác suất. |
| evidence | Dòng code, test input/expected/actual, giải thích và nguyên nhân thay thế; ghi xung đột đề/oracle nếu có. |
| same_cause_as_cluster | Mỗi A/B/C: `Yes` nếu cùng nguyên nhân thực chất với tất cả thành viên đã xem của cụm; `Partially` nếu chỉ một phần/cụm nhiều nguyên nhân; `No` nếu không có nguyên nhân chung phù hợp. Chưa xem đủ ngữ cảnh giữ `null`; evidence ghi phạm vi đã xem. |

Không thể suy ra chắc chắn trạng thái nhận thức từ một bài sai. Không thực thi code sinh viên để điền phiếu này.

## Danh sách 17 phiếu — vòng độc lập không hiện cluster

Dấu `—` bên dưới là ô chưa điền, tương ứng `null` trong JSON.

| Bài / Submission | Source / bản sửa / đề / log | Misconception | Loại | Confidence | Cùng nguyên nhân A/B/C (vòng 2) |
|---|---|---|---|---|---|
| 2812 / itsp-2812-270276_buggy | [source](../data/raw/itsp/dataset/Lab-3/2812/270276_buggy.c) / [sửa](../data/raw/itsp/dataset/Lab-3/2812/270276_correct.c) / [đề](../data/raw/itsp/dataset/Lab-3/2812/Main.c) / [log](../data/itsp/cohorts/2812/review.jsonl) | — | — | — | — / — / — |
| 2812 / itsp-2812-270277_buggy | [source](../data/raw/itsp/dataset/Lab-3/2812/270277_buggy.c) / [sửa](../data/raw/itsp/dataset/Lab-3/2812/270277_correct.c) / [đề](../data/raw/itsp/dataset/Lab-3/2812/Main.c) / [log](../data/itsp/cohorts/2812/review.jsonl) | — | — | — | — / — / — |
| 2812 / itsp-2812-270283_buggy | [source](../data/raw/itsp/dataset/Lab-3/2812/270283_buggy.c) / [sửa](../data/raw/itsp/dataset/Lab-3/2812/270283_correct.c) / [đề](../data/raw/itsp/dataset/Lab-3/2812/Main.c) / [log](../data/itsp/cohorts/2812/review.jsonl) | — | — | — | — / — / — |
| 2812 / itsp-2812-270285_buggy | [source](../data/raw/itsp/dataset/Lab-3/2812/270285_buggy.c) / [sửa](../data/raw/itsp/dataset/Lab-3/2812/270285_correct.c) / [đề](../data/raw/itsp/dataset/Lab-3/2812/Main.c) / [log](../data/itsp/cohorts/2812/review.jsonl) | — | — | — | — / — / — |
| 2812 / itsp-2812-270293_buggy | [source](../data/raw/itsp/dataset/Lab-3/2812/270293_buggy.c) / [sửa](../data/raw/itsp/dataset/Lab-3/2812/270293_correct.c) / [đề](../data/raw/itsp/dataset/Lab-3/2812/Main.c) / [log](../data/itsp/cohorts/2812/review.jsonl) | — | — | — | — / — / — |
| 2825 / itsp-2825-271154_buggy | [source](../data/raw/itsp/dataset/Lab-4/2825/271154_buggy.c) / [sửa](../data/raw/itsp/dataset/Lab-4/2825/271154_correct.c) / [đề](../data/raw/itsp/dataset/Lab-4/2825/Main.c) / [log](../data/itsp/cohorts/2825/review.jsonl) | — | — | — | — / — / — |
| 2825 / itsp-2825-271163_buggy | [source](../data/raw/itsp/dataset/Lab-4/2825/271163_buggy.c) / [sửa](../data/raw/itsp/dataset/Lab-4/2825/271163_correct.c) / [đề](../data/raw/itsp/dataset/Lab-4/2825/Main.c) / [log](../data/itsp/cohorts/2825/review.jsonl) | — | — | — | — / — / — |
| 2825 / itsp-2825-271173_buggy | [source](../data/raw/itsp/dataset/Lab-4/2825/271173_buggy.c) / [sửa](../data/raw/itsp/dataset/Lab-4/2825/271173_correct.c) / [đề](../data/raw/itsp/dataset/Lab-4/2825/Main.c) / [log](../data/itsp/cohorts/2825/review.jsonl) | — | — | — | — / — / — |
| 2825 / itsp-2825-271188_buggy | [source](../data/raw/itsp/dataset/Lab-4/2825/271188_buggy.c) / [sửa](../data/raw/itsp/dataset/Lab-4/2825/271188_correct.c) / [đề](../data/raw/itsp/dataset/Lab-4/2825/Main.c) / [log](../data/itsp/cohorts/2825/review.jsonl) | — | — | — | — / — / — |
| 2825 / itsp-2825-271203_buggy | [source](../data/raw/itsp/dataset/Lab-4/2825/271203_buggy.c) / [sửa](../data/raw/itsp/dataset/Lab-4/2825/271203_correct.c) / [đề](../data/raw/itsp/dataset/Lab-4/2825/Main.c) / [log](../data/itsp/cohorts/2825/review.jsonl) | — | — | — | — / — / — |
| 2825 / itsp-2825-271213_buggy | [source](../data/raw/itsp/dataset/Lab-4/2825/271213_buggy.c) / [sửa](../data/raw/itsp/dataset/Lab-4/2825/271213_correct.c) / [đề](../data/raw/itsp/dataset/Lab-4/2825/Main.c) / [log](../data/itsp/cohorts/2825/review.jsonl) | — | — | — | — / — / — |
| 2833 / itsp-2833-271912_buggy | [source](../data/raw/itsp/dataset/Lab-4/2833/271912_buggy.c) / [sửa](../data/raw/itsp/dataset/Lab-4/2833/271912_correct.c) / [đề](../data/raw/itsp/dataset/Lab-4/2833/Main.c) / [log](../data/itsp/cohorts/2833/review.jsonl) | — | — | — | — / — / — |
| 2833 / itsp-2833-271916_buggy | [source](../data/raw/itsp/dataset/Lab-4/2833/271916_buggy.c) / [sửa](../data/raw/itsp/dataset/Lab-4/2833/271916_correct.c) / [đề](../data/raw/itsp/dataset/Lab-4/2833/Main.c) / [log](../data/itsp/cohorts/2833/review.jsonl) | — | — | — | — / — / — |
| 2833 / itsp-2833-271920_buggy | [source](../data/raw/itsp/dataset/Lab-4/2833/271920_buggy.c) / [sửa](../data/raw/itsp/dataset/Lab-4/2833/271920_correct.c) / [đề](../data/raw/itsp/dataset/Lab-4/2833/Main.c) / [log](../data/itsp/cohorts/2833/review.jsonl) | — | — | — | — / — / — |
| 2833 / itsp-2833-271965_buggy | [source](../data/raw/itsp/dataset/Lab-4/2833/271965_buggy.c) / [sửa](../data/raw/itsp/dataset/Lab-4/2833/271965_correct.c) / [đề](../data/raw/itsp/dataset/Lab-4/2833/Main.c) / [log](../data/itsp/cohorts/2833/review.jsonl) | — | — | — | — / — / — |
| 2833 / itsp-2833-271975_buggy | [source](../data/raw/itsp/dataset/Lab-4/2833/271975_buggy.c) / [sửa](../data/raw/itsp/dataset/Lab-4/2833/271975_correct.c) / [đề](../data/raw/itsp/dataset/Lab-4/2833/Main.c) / [log](../data/itsp/cohorts/2833/review.jsonl) | — | — | — | — / — / — |
| 2833 / itsp-2833-271986_buggy | [source](../data/raw/itsp/dataset/Lab-4/2833/271986_buggy.c) / [sửa](../data/raw/itsp/dataset/Lab-4/2833/271986_correct.c) / [đề](../data/raw/itsp/dataset/Lab-4/2833/Main.c) / [log](../data/itsp/cohorts/2833/review.jsonl) | — | — | — | — / — / — |

## Tính metric khi có annotation

Chạy tại thư mục dự án:

```powershell
.venv/Scripts/python.exe scripts/score_itsp_experts.py
```

Kết quả: `results/itsp/expert_validation_metrics.json`. Script chỉ đọc annotation và assignment đã đóng băng (kiểm tra SHA-256), không chạy hoặc thay đổi pipeline clustering.

- **Purity theo loại misconception** tính riêng từng bài và A/B/C: tổng số nhãn loại chiếm đa số trong mỗi cụm / tổng mẫu `Yes` có loại đã adjudicate theo codebook được duyệt. No, Unclear, pending và Yes chưa có loại bị loại khỏi mẫu số; luôn đọc coverage, decision counts và số mẫu từng cụm cùng purity. Đây là purity trên tập con positive có nhãn của 17 mẫu, không phải purity toàn cohort. Chưa đủ dữ liệu giữ `null`, không thay bằng 0.
- **Agreement** tính theo từng cặp người và từng bài trên giao các mẫu hoàn tất độc lập: tỷ lệ trùng nhãn và Cohen kappa danh nghĩa, không trọng số. Decision bao gồm Unclear; agreement về loại chỉ dùng cặp cùng Yes có loại theo codebook. Cùng nguyên nhân tính riêng A/B/C ở vòng 2, là đồng thuận về cụm đã thấy, không phải annotation misconception mù. Không có cặp giữ `null`; kappa mẫu số bằng 0 giữ `null` dù raw agreement có thể là 1. Confidence không làm trọng số.
- 17 mẫu gồm 9 medoid train và 8 holdout xa medoid nhất theo C gốc, có thiên lệch lựa chọn; không ước lượng tần suất lỗi, không chứng minh OAV tốt hơn. ITSP thiếu student ID; không tạo ID giả và không đánh giá unseen-student generalization.
