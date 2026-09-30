# Annotation theo cluster cho AI

Module `misconceptions.cluster_annotation` xuất evidence từ các run đã audit, không gọi API
và không chạy code C. Khác với gói giảng viên chấm độc lập từng bài trong
[teacher_validation.md](teacher_validation.md), AI ở đây thấy cluster, rule và candidate.
Kết quả chỉ là **AI review**, không được dùng làm gold độc lập hay tính misconception accuracy.

## Bộ dữ liệu để gửi

Gói xuất ngày 28/09/2026 ở `deliverables/De5_Annotation_20260928/`:

- `itsp/`: 5 cụm, 38 bài, có mô tả đề bài; nên bắt đầu ở đây.
- `cpack/`: 69 cụm, 2.151 bài; gói mở rộng có input/oracle/code nhưng thiếu đề bài gốc.
- Mỗi gói có `evidence.json` đầy đủ, `clusters/*.json` và `clusters/*.md` tự chứa code/log
  của cả cụm, `PROMPT.md`, `response.schema.json`, và danh sách chờ `response.template.json`.
- Mọi cluster đều `pending_annotation`; template có `result: null`. Chưa có phản hồi AI thực.

Gửi `PROMPT.md`, `response.schema.json` và **một cluster JSON hoặc Markdown** cho AI.
AI trả về JSON theo schema. Không gửi cả JSON và Markdown trùng nội dung cùng lúc.
Một số cụm C-Pack lớn: dùng AI có khả năng đọc file đầy đủ; nếu không đọc hết thì phải
ghi rõ giới hạn và trả `uncertain`, không giả vờ đã rà soát cả cụm.
Không cần API key khi xuất hoặc kiểm tra kết quả.

## Chính sách chọn cố định

Chọn K-means / `combined_stdout` / seed 42 ở từng bài, độc lập với silhouette,
fidelity hay số rule có vẻ khớp. Chỉ dùng train + validation từ corpus split lock.
Không lấy các phiên bản clustering khác để nhân bản cùng bài làm thành nhiều bằng chứng.

Điều kiện mặc định: ít nhất 4 bài, ít nhất 3 source khác nhau (so sánh source strip),
mọi thành viên có source và log đủ cho tất cả test trượt, ít nhất một test trượt ở
50% số bài trong cụm. Danh sách bị loại và lý do nằm trong README và `excluded_clusters`.
Đây là ngưỡng **khả năng xem xét**, không phải bằng chứng cụm có một misconception chung.
Không loại một cụm chỉ vì chưa có candidate hay nhiều cơ chế khác nhau.

Chọn tối đa 4 đại diện: medoid train trước, sau đó ưu tiên khác biệt OAV/outcome.
AI vẫn có toàn bộ thành viên để xem phản ví dụ. Mỗi bài có code gốc không cắt ngắn,
outcomes, input/expected/output, OAV đã dùng để phân cụm và OAV chẩn đoán lúc xuất.
ID sinh viên, ID bài gốc và đường dẫn source không xuất ra; comment trong source public
vẫn giữ nguyên nên không khẳng định đây là ẩn danh hoàn toàn.

Tỷ lệ trượt có hai mẫu số riêng: số test đã quan sát và tổng bài trong cụm.
`not_run`/thiếu kết quả không được coi là pass. `fail`, `runtime_error`, `timeout`
được tính là thất bại và vẫn có thống kê từng trạng thái. OAV nổi bật có tần suất
và chênh lệch so với toàn cohort train/validation; thống kê đầy đủ nằm trong JSON.

Luật cây IF–THEN có support/precision train và validation, chỉ giải thích cluster ID.
Luật cơ chế cục bộ có từng đoạn code, dòng và log liên quan, nhưng vẫn là giả thuyết.
Candidate tạo từ luật cục bộ phiên bản lúc xuất, không phải nhãn đã duyệt.
Statement ITSP chỉ lấy comment mô tả đề bài, không xuất lời giải đúng trong `Main.c`.
C-Pack chưa có statement và chưa replay để xác nhận suite lịch sử: AI phải nêu giới hạn này.

## Xuất lại

Chạy PowerShell từ thư mục repository, dùng thư mục output mới:

```powershell
$py = '.\misconceptions-prototype\.venv\Scripts\python.exe'
& $py misconceptions-prototype/scripts/export_cluster_annotations.py export `
  --run research/runs/itsp-validation-20260928 `
  --data misconceptions-prototype/data/itsp `
  --split-lock research/splits/itsp-development-v1.json `
  --output .cache/my-itsp-annotation

& $py misconceptions-prototype/scripts/export_cluster_annotations.py export `
  --run research/runs/cpack-validation-20260928 `
  --data .cache/cpack-validation-20260928/dataset `
  --split-lock research/splits/cpack-v3.json `
  --output .cache/my-cpack-annotation
```

Exporter kiểm tra split toàn corpus, hash report theo audit, snapshot mã nguồn của run,
hash manifest/source/evidence, và membership train/validation trước khi xuất.
Packet lưu fingerprint của dữ liệu, split, run và mã exporter. Không ghi đè run lịch sử.
Không dùng dữ liệu lớp học/live database. Bộ dữ liệu hiện tại là corpus public.

## Schema và tiếp nhận phản hồi

Envelope gồm `packet_id`, `annotation_source: "ai"`, `reviews: [...]`.
Mỗi review gồm `cluster_id`, `misconception_label`, `evidence_supported`, `confidence`,
`reasoning`, `alternative_explanations`, `decision`, `notes`, `evidence_refs`.

- `supported`: label có bằng chứng, `evidence_supported: true`; phải nêu phạm vi bao phủ.
- `rejected`: label được nêu bị bằng chứng bác bỏ, `evidence_supported: false`.
- `uncertain`: chưa kết luận được, `evidence_supported: false`; label có thể `null`.
- `confidence`: số hữu hạn 0–1 về decision, không phải xác suất đã hiệu chuẩn.
- `evidence_refs`: tham chiếu thật trong `evidence_index`, ví dụ
  `members/sample_001/raw_code`, `members/sample_001/tests/1`.

Nếu AI thay candidate, phải giải thích rõ candidate cũ sai/thiếu ở đâu trong reasoning.
Template chờ không cố điền giả một response hợp lệ; AI tạo response hoàn chỉnh theo schema.

Lưu phản hồi AI thành file riêng, rồi chạy (đường dẫn response chỉ là ví dụ):

```powershell
& $py misconceptions-prototype/scripts/export_cluster_annotations.py validate `
  --packet deliverables/De5_Annotation_20260928/itsp/evidence.json `
  --response .cache/ai-response-1.json .cache/ai-response-2.json `
  --output .cache/ai-reviews-checked.json
```

Có thể nhận từng phần; thêm `--require-complete` khi đã đủ tất cả cluster của gói.
Các file phải cùng packet, không được trùng cluster. Không trộn ITSP và C-Pack trong một lần.
Intake kiểm tra hash packet, schema/kiểu dữ liệu, ID, refs, confidence, consistency của decision.
Nó **không tự kiểm chứng reasoning của AI**. Output có
`status: ai_reviewed_pending_human_validation`, `human_validated: false`,
`mechanism_accuracy: null`; packet gốc vẫn pending. Gold chỉ đến từ luồng giảng viên
độc lập có adjudication, không từ việc đổi `annotation_source` trong file này.
