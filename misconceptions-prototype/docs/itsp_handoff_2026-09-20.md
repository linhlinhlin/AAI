# Bàn giao Đề 5 — Misconceptions Clustering

Kiểm tra kỹ thuật mới nhất: **106 tests + 3 subtests pass; lint pass**. [Biên bản](../results/itsp/completion_verification.json). Đây là kiểm tra phần mềm, chưa phải human expert validation.

## Cập nhật hoàn thiện kỹ thuật — 20/09/2026

Đã [đối chiếu toàn bộ mục tiêu và phần còn thiếu](itsp_completion_review.md). Bổ sung intake hợp nhất phiếu chuyên gia vòng 1 có hash/provenance, không ghi đè snapshot hoặc tự adjudicate; scorer có coverage/nhãn đồng hạng theo cụm và công cụ xuất Markdown human-only. Từ chối assignment trùng/không hợp lệ. Baseline, feature và A/B/C giữ nguyên. Chưa có human annotation, expert purity/agreement vẫn null; bước cần chuyên gia và mẫu mới được ghi rõ, không tuyên bố đề tài đã hoàn tất.


**Cập nhật: 20/09/2026.** Thư mục dự án hiện tại: `E:/AAI/misconceptions-prototype`.

## 1. Trạng thái cần nắm ngay

Đã có prototype ITSP, thực nghiệm A/B/C, hồ sơ bằng chứng và bộ phiếu cho chuyên gia. **Chưa hoàn tất expert validation:** 0 human reviews hoàn tất, 0 adjudication; codebook chưa được chuyên gia phê duyệt. Cluster purity, raw agreement và Cohen’s kappa của expert validation đều `null`, không phải 0.

Kết luận được phép: pipeline phân nhóm **biểu hiện lỗi** và cung cấp dấu hiệu cấu trúc để phân tích. Chưa chứng minh các nhóm là **quan niệm sai lầm của người học**, chưa chứng minh phần cấu trúc hiện tại cải thiện clustering. Không dùng AI annotation làm ground truth.

Dữ liệu chính thức từ giảng viên chưa có. ITSP chỉ là prototype công khai, không phải dataset mặc định của đề tài. Chưa gửi phiếu hoặc liên hệ chuyên gia từ công việc này.

## 2. Các phần đã hoàn thành

| Phần việc | Kết quả và phạm vi |
|---|---|
| Thu thập ITSP | Snapshot từ jyi/ITSP, commit `0553f683f99403efb5ef440af826c1d229a52376`; lưu dữ liệu gốc và provenance. |
| Import và routing | 661 bài sai/74 bài tập; nhập 649, loại 12 do số test không khớp suite; 648 eligible, 1 parser failure. Không chạy code C của sinh viên; sử dụng log lịch sử. |
| Chuẩn hóa dữ liệu | Manifest, submission JSONL và review JSONL theo cohort; giữ raw source, bản sửa cùng cặp, test input/expected/actual. Student ID thiếu giữ null. |
| Biểu diễn OAV | Thuộc tính test categorical và 16 cờ cú pháp C từ tree-sitter. Chỉ giữ feature cấu trúc biến thiên trên train; không dùng bản sửa, ID hoặc expert label làm feature. |
| Baseline và clustering | Exact test signatures; weighted Hamming + average-linkage; K-means one-hot có trọng số là đối chứng lịch sử. Cây surrogate nông mô tả cluster, không phải bộ chẩn đoán misconception. |
| Thực nghiệm ban đầu | 126 lượt cấu hình cũ: 124 thành công, 2 abstain; lưu kết quả theo từng bài. |
| Ablation A/B/C | 27 lượt trên cùng 59 bài thuộc 2812, 2825, 2833; A=test-only, B=structural-only, C=combined; k=3, seeds 7/42/91. Routing/split và điều kiện khác giữ giống nhau. |
| Review 17 mẫu | 9 medoid train + 8 holdout xa medoid nhất theo C gốc; đã phân tích evidence và giả thuyết kỹ thuật, không coi là nhãn chuyên gia. |
| Công cụ annotation | Phiếu misconception Yes/No/Unclear, type, confidence, evidence, cùng nguyên nhân A/B/C; schema/ID/hash validation và scorer purity/agreement/kappa. |
| Phân biệt AI/human | Nhãn AI được giữ dưới dạng tham khảo nội bộ; có kiểm tra nguồn annotation, không dùng AI tính expert metrics hoặc thay adjudication. |
| Hồ sơ vòng 1 | ZIP offline, 17 mẫu, 51 file đề/source/bản sửa, 113 test records, codebook dự thảo, phiếu trống; 72 file vượt audit. Không chứa assignment cụm hay nhãn AI. |
| Hồ sơ vòng 2 | ZIP offline, 59 bài ngữ cảnh, 177 file đề/source/bản sửa, 395 test records và mapping 17 mẫu; chỉ phát sau khi khóa vòng 1. |
| Audit bằng chứng | Audit reviewer packet ghi 255 mục nguồn khớp hash, 135 khối C, 395 test records, 51 bộ OAV/trọng số/cụm/thành viên khớp nguồn. Đây là audit dữ liệu xuất, không xác nhận misconception. |
| Sửa thiết kế kiểm chứng | Tách ba tầng evidence; đánh dấu packet có hiển thị cụm; ghi 59 bài đã xem vào manifest phát triển; quy định đánh giá mới, coverage, gộp sai/tách sai và giới hạn suy luận. |

## 3. Kết quả thực nghiệm và giới hạn

- Kiểm tra toàn bộ 59 bài ở seed42: A và C cùng phân hoạch trong cả ba bài, ARI=1 mỗi bài. **Chưa thấy lợi ích phân hoạch của combined ở cấu hình này**; không suy rằng mọi structural feature đều vô ích.
- Hai mẫu 2825/271173 (`Cicle`) và 2825/271188 (`on` thay `outside`) có cùng combined OAV. Biểu diễn hiện tại thiếu thông tin phân biệt chúng; thay thuật toán không tự tạo thêm thông tin nguyên nhân.
- 16 flags hiện tại chỉ biểu thị cú pháp xuất hiện, chưa mã hóa quan hệ nhánh, assignment trong condition hay hướng cập nhật vòng lặp.
- Silhouette/stability đánh giá phân hoạch; surrogate fidelity đo mức cây bắt chước nhãn cụm. Các metric này không chứng minh tính đúng của misconception.
- 17 mẫu có chủ đích theo C, phù hợp phân tích ca; không đại diện toàn lớp hoặc tần suất lỗi. Purity chỉ trên adjudicated Yes có type phải đi cùng mẫu số, coverage và No/Unclear/pending.
- Không có student ID; split theo source không bảo đảm độc lập sinh viên. Không tạo ID giả, không báo unseen-student generalization hoặc tỷ lệ sinh viên hiểu sai.
- Log lịch sử, bản sửa và code đơn lẻ chưa đủ phân biệt mọi trường hợp sơ suất với hiểu sai bền vững. Cần chuyên gia nêu bằng chứng và nguyên nhân thay thế; nếu thiếu giữ Unclear.

## 4. Bản đồ tài liệu và artifact

| Mục đích | File |
|---|---|
| Đọc thiết kế kiểm chứng mới trước | [itsp_validation_revision.md](itsp_validation_revision.md) |
| Điều phối người chấm, nhận/merge/adjudicate/chấm metric | [itsp_human_review_protocol.md](itsp_human_review_protocol.md) |
| Baseline, feature, distance, split, metrics A/B/C | [itsp_validation.md](itsp_validation.md) |
| Nhật ký công việc chi tiết, gồm các mốc cũ | [itsp_progress.md](itsp_progress.md) |
| Báo cáo kết quả tổng hợp | [summary.md](../results/itsp/summary.md), [abc_summary.md](../results/itsp/abc_summary.md) |
| Phân tích 17 ca, không phải human labels | [itsp_expert_review.md](itsp_expert_review.md) |
| Phản biện khoa học | [reviewer_assessment_2026-09-20.md](reviewer_assessment_2026-09-20.md) |
| Gửi người chấm vòng 1 | [human_review_packet.zip](../results/itsp/human_review_packet.zip), [README](../results/itsp/human_review/README.md), [CODEBOOK dự thảo](../results/itsp/human_review/CODEBOOK.md) |
| Gửi vòng 2 sau khi khóa vòng 1 | [human_review_round2_packet.zip](../results/itsp/human_review_round2_packet.zip) |
| Packet tổng hợp có hiển thị cụm | [reviewer_packet.md](../results/itsp/reviewer_packet.md), [reviewer_sources.md](../results/itsp/reviewer_sources.md) |
| Mapping cố định 17 mẫu | [abc_review_assignments.json](../results/itsp/abc_review_assignments.json) |
| Phiếu trắng vòng 1 | [annotations.json](../results/itsp/human_review/annotations.json) |
| File nội bộ có AI reviews — không gửi chấm mù | [expert_annotations.json](../data/itsp/expert_annotations.json) |
| Trạng thái expert metrics | [expert_validation_metrics.json](../results/itsp/expert_validation_metrics.json) |
| 59 bài đã xem, không dùng làm test độc lập mới | [development_exposure_manifest.json](../results/itsp/development_exposure_manifest.json) |
| Audit gói vòng 1/vòng 2 | [human_review_packet_audit.json](../results/itsp/human_review_packet_audit.json), [review_handoff_audit.json](../results/itsp/review_handoff_audit.json) |
| Audit reviewer và nối provenance sau đổi tiêu đề | [reviewer_audit_2026-09-20.json](../results/itsp/reviewer_audit_2026-09-20.json), [validation_revision_2026-09-20.json](../results/itsp/validation_revision_2026-09-20.json) |

Audit reviewer ban đầu tham chiếu hash packet **trước** khi thêm cảnh báo vòng 2. File validation_revision lưu hash trước/sau và xác nhận phần evidence không thay đổi. Không sửa audit lịch sử để giả vờ nó kiểm tra phiên bản mới.

## 5. Code và dữ liệu để tiếp quản

- `src/misconceptions/domain.py`: mô hình dữ liệu chung; `adapters.py`: đọc/chuẩn hóa input.
- `itsp.py`: import ITSP; `features.py`: OAV/feature extraction; `pipeline.py`: routing/split/clustering/explanation; `cli.py`: giao diện lệnh.
- `expert_validation.py`: kiểm tra annotation và tính metric, tách khỏi clustering.
- `data/raw/itsp/`: snapshot nguồn. `data/itsp/cohorts/<problem>/`: manifest/submissions/review theo bài.
- `results/itsp/abc/`: 27 kết quả A/B/C đã lưu. Không ghi đè để thay kết quả lịch sử khi thử feature mới.
- `scripts/check_itsp_review.py` kiểm tra AI review đã đóng băng; **không** phải chứng nhận human validation.

Khi có dữ liệu giảng viên: triển khai adapter vào schema chung rồi kiểm tra test coverage, source, ID và routing; tái sử dụng feature/pipeline. Không giả định dataset mới có cùng test IDs, ngôn ngữ hoặc student ID với ITSP; chỉ tái sử dụng phần phù hợp sau audit.

## 6. Lệnh tiếp quản

Chạy ở thư mục gốc dự án. Môi trường hiện có dùng Python 3.12; package yêu cầu Python >=3.11. Khi chuyển máy, tạo venv mới và cài package/dev dependencies theo README; không sao chép venv Windows sang môi trường khác. Dependency ranges không phải lockfile tái lập tuyệt đối. Một số provenance chứa đường dẫn máy cũ: giữ snapshot lịch sử, kiểm tra/điều chỉnh đường dẫn ở bản làm việc khi chuyển máy. Hai gói ZIP reviewer dùng link offline.

```powershell
# Kiểm tra toàn bộ code hiện có
.venv/Scripts/python.exe -m pytest -q
.venv/Scripts/python.exe -m ruff check .

# Audit gói chấm mù; lệnh cập nhật JSON audit
.venv/Scripts/python.exe scripts/audit_human_review_packet.py

# Validate phiếu trắng, không ghi metric
.venv/Scripts/python.exe scripts/score_itsp_experts.py --annotations results/itsp/human_review/annotations.json --validate-only
```

Với file nhận thật, thay đường dẫn annotations bằng file chuyên gia. Sau merge vào file human-only theo protocol:

```powershell
# Chỉ chạy khi human_annotations.json thực sự đã được tạo từ phiếu người thật
.venv/Scripts/python.exe scripts/score_itsp_experts.py --annotations data/itsp/human_annotations.json --validate-only
.venv/Scripts/python.exe scripts/score_itsp_experts.py --annotations data/itsp/human_annotations.json --output results/itsp/human_validation_metrics.json
```

`human_annotations.json` ở trên là đích làm việc theo protocol, không phải tuyên bố đã có nhãn. File `expert_annotations.json` hiện chứa tham khảo AI: bảo tồn provenance, không đổi reviewer_id AI thành human. Chỉ đồng bộ kết quả chuyên gia vào file tổng hợp sau khi có nhãn/biên bản thống nhất; bản tính metric ưu tiên human-only.

## 7. Việc tiếp theo và điều kiện bắt đầu

1. **Người phụ trách + hai chuyên gia thật:** chốt codebook, phạm vi toán học/C, quy tắc primary type, OTHER_CONCEPT và reviewer IDs. Chưa có phê duyệt thì không tự điền approved_by.
2. **Chấm độc lập vòng 1:** mỗi người nhận bản riêng, đủ 17 mẫu; lưu file nhận nguyên trạng/hash. Kiểm tra ID, schema, codebook, completeness và điều kiện mù. Unclear không thay pending.
3. **Vòng 2 và adjudication:** khóa vòng 1 rồi mới cung cấp cụm; ghi members_reviewed và n_reviewed/n_cluster trong evidence. Chuyên gia giải quyết bất đồng; không dùng AI làm người phân xử. Giữ lượt độc lập để tính agreement.
4. **Validation thực tế:** tính purity trên nhãn adjudicated phù hợp, raw agreement/kappa trên các cặp độc lập hợp lệ; báo coverage, cluster sizes, mixed causes và outliers. Mẫu số không xác định giữ null.
5. **Thử nghiệm feature mới sau khi chốt thiết kế:** chọn và khóa mẫu chưa xem, ngân sách review, phạm vi bài và tiêu chí đánh giá. 59 bài đã xem là tập phát triển. Thử ít feature quan hệ, lần lượt; không tuning bằng nhãn cuối.
6. **Đánh giá gộp/tách sai:** pairwise precision/recall mới là đề xuất trong protocol, chưa triển khai/chạy. Chỉ làm khi nhãn cơ chế đủ rõ, cùng quy tắc và có coverage; không ép đa lỗi thành một phân hoạch.
7. **Chốt báo cáo:** cập nhật summary/expert_review/progress và Discussion/Limitations từ dữ liệu thực tế. Nếu cấu trúc không cải thiện, báo đúng; không đổi giả thuyết thành kết quả mong muốn.

Chưa triển khai feature quan hệ mới, chưa chọn tập kiểm chứng mới, chưa thêm LLM/GNN hoặc thuật toán clustering phức tạp. Giữ exact signatures + weighted Hamming/average-linkage + cây nông. ILA nếu cần nằm ở quy nạp luật, không là clustering phi giám sát.

## 8. Kiểm tra gần nhất và tiêu chí hoàn tất

Mốc kiểm tra code gần nhất đã ghi trong `validation_revision_2026-09-20.json`: **93 tests + 3 subtests pass; Ruff pass**. Những số 48/61/63/64 trong nhật ký là các mốc lịch sử, không cộng lại. Lượt bàn giao này chỉ cập nhật Markdown và kiểm tra liên kết, không thay code hoặc chạy lại thí nghiệm.

Phần kỹ thuật chuẩn bị đã hoàn thành trong phạm vi hiện tại. Expert validation chỉ hoàn tất khi có người chấm thật, codebook được xác nhận, provenance annotation đầy đủ và kết quả/giới hạn được báo đúng. Không coi hồ sơ đủ, test pass hoặc AI review là thay thế cho bước này.
