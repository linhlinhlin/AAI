# Provenance reconciliation — Đề tài 5

Ngày: 20/09/2026. Phạm vi duy nhất: đối chiếu phiên bản protocol và dependency của hồ sơ; không tiếp tục annotation, adjudication, sample review hoặc evaluation sampling.

## 1. Old hash và current hash

Artifact: `docs/itsp_human_review_protocol.md`.

| Phiên bản | SHA-256 | Kích thước |
|---|---|---:|
| Snapshot nguồn lịch sử | `9fdba3fd66d512a1775699f0501eff0a5bcc3750a9196829a6db26c2fcd783bb` | 8.682 bytes |
| Protocol đang dùng trong workspace | `1cc8ce739a1497bf6d64c4621f5388f1ff7192272d23bca019bbcf6a491a2cd2` | 9.344 bytes |

Trước sửa đã hash 777 artifact trong docs, scripts, src, tests, results/itsp, data/itsp và README, loại caches và workspace reconciliation. Danh sách nằm trong [before_hashes.json](E:/AAI/misconceptions-prototype/results/itsp/multi_agent_validation/2026-09-20/provenance_reconciliation/before_hashes.json). Đây không phải hash toàn bộ cây raw/vendor lớn; các nguồn raw được tham chiếu trong manifest đã được kiểm tra qua 255 mục nguồn.

## 2. Evidence tìm được và giới hạn lịch sử

`git rev-parse --show-toplevel` trả về “not a git repository”. **git provenance unavailable**: không có commit, tác giả, commit message hay quan hệ parent/child để xác thực thay đổi. Không suy những thông tin này từ timestamp.

Tìm exact hash bằng `rg` trên repository, gồm hidden files, loại `.venv`, `.git` và các bản sao reconciliation, cho thấy:

- `results/itsp/reviewer_sources.md:216` khai protocol hash **9fd…** là nguồn dùng biên soạn hướng dẫn reviewer packet.
- `results/itsp/ai_review_integrity_baseline.json:516` ghi cùng đường dẫn protocol và cùng hash **9fd…**. Đây là bằng chứng protocol cũ hiện diện ở giai đoạn đóng băng baseline toàn vẹn AI review; không phải chứng cứ người thật duyệt codebook.
- `multi_agent_validation_report.md` và `stop_event.json` lặp lại cặp hash trong sự kiện STOP. Chúng là dẫn xuất của phát hiện mismatch, không phải chứng cứ độc lập về lúc tạo protocol.
- Hash **1cc…** không được tìm thấy trong bản ghi revision có trước STOP qua tìm kiếm này. Nội dung `docs/itsp_completion_review.md`, các script merge/report và `completion_verification.json` đối chiếu được với phần hướng dẫn mới, nhưng không xác nhận danh tính người sửa hay thời điểm chính xác của thao tác.

Đã xem danh mục ZIP workspace cha `E:/AAI/misconceptions-prototype.zip` và hai ZIP review: không có member chứa file human review protocol. Hai ZIP review cũng không có hash 9fd…/1cc… hoặc tham chiếu tên protocol trong các member Markdown/JSON; archive comment trống. ZIP metadata không được dùng để suy version.

## 3. Old version reconstruction

Tách phần byte đứng trước mục mới “Công cụ intake và báo cáo đã bổ sung”, giữ một CRLF kết thúc như được hash lịch sử xác nhận, thu được chính xác 8.682 bytes có SHA-256 **9fd…**. Protocol hiện tại bắt đầu bằng toàn bộ byte của snapshot này.

Đây là tái dựng nội dung bằng kiểm chứng hash, không phải bản lấy từ commit. Không đoán lại câu chữ hoặc sửa protocol hiện tại. Các cách kết thúc newline ở ranh giới section được kiểm tra; bản khớp hash dùng CRLF gốc.

- [Snapshot 9fd…](E:/AAI/misconceptions-prototype/results/itsp/multi_agent_validation/2026-09-20/provenance_reconciliation/protocol_snapshot_hash_9fdba3fd.md).
- [Snapshot 1cc…](E:/AAI/misconceptions-prototype/results/itsp/multi_agent_validation/2026-09-20/provenance_reconciliation/protocol_snapshot_current_1cc8ce73.md).
- [Cách tái dựng và record nguồn](E:/AAI/misconceptions-prototype/results/itsp/multi_agent_validation/2026-09-20/provenance_reconciliation/old_snapshot_origin.json).

## 4. Diff và phân loại từng thay đổi

[Unified diff](E:/AAI/misconceptions-prototype/results/itsp/multi_agent_validation/2026-09-20/provenance_reconciliation/protocol_revision.diff) chỉ có một đoạn thêm cuối file, tổng 662 bytes; không có xóa hoặc sửa nội dung cũ.

| Thay đổi | Loại | Cơ sở |
|---|---|---|
| Thêm dòng trống và tiêu đề mục công cụ | A — Editorial | Chỉ trình bày |
| Liên kết `itsp_completion_review.md` và script merge | B — Protocol clarification | Cụ thể hóa thao tác intake đã mô tả ở mục 1–2 bản cũ |
| Nhắc một reviewer/file, codebook đã duyệt giống nhau | B | Các yêu cầu đã có trong bản cũ; không thêm eligibility mới trong văn bản này |
| Output mới/provenance, không tự adjudicate | B | Triển khai yêu cầu lưu nguồn, không ghi đè, người thật adjudicate vốn đã có |
| Round1 bất biến; vòng2/adjudication trên bản sao | B | Không đổi thứ tự mở cụm hoặc quyền sửa lượt độc lập |
| Liên kết script xuất bảng từng cụm, loại AI, không tạo ground truth | B | Làm rõ công cụ báo cáo; không đổi công thức, mẫu số hoặc đối tượng human-only đã quy định |

Không thấy thay đổi loại C trong diff hai phiên bản **tài liệu này**. Việc có script mới và scorer được mở rộng là thay đổi implementation có biên bản riêng; kết luận tương đương ngữ nghĩa của protocol không chứng nhận toàn bộ implementation hay chất lượng nghiên cứu.

## 5. Packet dependency

| Artifact | Protocol hash được chứng minh | Trạng thái và giới hạn |
|---|---|---|
| `reviewer_packet.md` | **9fd…**, nguồn được manifest khai | Manifest nêu rõ hướng dẫn được biên soạn từ protocol/README. Đây là dependency được khai báo, không phải execution trace của exporter. Revision tiêu đề packet có biên bản riêng. |
| `human_review_packet.zip` | **UNKNOWN** lúc tạo | Hash ZIP vẫn khớp baseline AI và handoff audit. Không nhúng protocol/version hash; không suy là 9fd… chỉ vì đồng xuất hiện trong baseline. |
| `human_review_round2_packet.zip` | **UNKNOWN** lúc tạo | Hash ZIP khớp baseline lịch sử; không có binding tới version protocol. |
| README/CODEBOOK/annotations trống vòng 1 | **UNKNOWN** lúc tạo | Bytes hiện tại khớp baseline và nội dung ZIP; draft codebook vẫn chưa duyệt. |
| `data/itsp/ai_independent_review.json` | **UNKNOWN** đối với protocol | Có binding riêng tới packet/codebook; không tự biến binding đó thành protocol hash. |
| `data/itsp/expert_annotations.json` | **UNKNOWN** đối với protocol | Có assignment/codebook metadata, không chứng minh version protocol đã dùng. |
| `ai_review_integrity_baseline.json` | Ghi nhận **9fd…** tại thời điểm snapshot | Chứng minh nội dung được hash tại giai đoạn baseline, không chứng minh mọi artifact được sinh từ cùng version. |
| Human packet audit / handoff audit | **UNKNOWN** đối với protocol | Các audit hash ZIP/evidence/assignment; không khóa hash protocol tạo packet. |
| `validation_revision_2026-09-20.json` | Không khóa protocol revision này | Giải thích thay đổi tiêu đề packet; không được dùng để chứng nhận phần thêm intake. |
| Completion docs/verification | **UNKNOWN** về hash protocol | Corroborate việc bổ sung công cụ; không đủ chứng minh author/commit hay generation dependency. |

[Bảng dependency kèm hash artifact](E:/AAI/misconceptions-prototype/results/itsp/multi_agent_validation/2026-09-20/provenance_reconciliation/packet_dependencies.json) giữ các trường UNKNOWN dưới dạng null có giải thích. Không gán 1cc… hồi tố cho packet cũ.

## 6. Semantic/material classification

**`RESOLVED_SAME_SEMANTIC_VERSION`** đối với mismatch đang xử lý. Hash 9fd… đại diện bản protocol đầy đủ trước khi thêm mục công cụ; hash 1cc… là cùng quy tắc nghiên cứu với hướng dẫn vận hành bổ sung.

Trong revision JSON, `revision_status="editorial"` dùng theo enum hai giá trị được yêu cầu; trường `semantic_classification="B_protocol_clarification_non_material"` nói rõ đây chủ yếu là clarification, không đơn thuần typo. `review_required=true` vẫn được giữ.

## 7. Integrity assessment

Mismatch phát sinh vì manifest đang dẫn một đường dẫn mutable nhưng giữ hash của nội dung lịch sử. Đã tìm được nội dung cũ đúng hash và xác định đầy đủ delta; không thấy bằng chứng sửa raw/annotation/packet ngoài kiểm soát trong phạm vi đối chiếu này. Không có bằng chứng để kết luận `INTEGRITY_FAILURE`.

Nguồn gốc byte và sự tương thích ngữ nghĩa đã xác định; danh tính tác giả và commit của thay đổi vẫn chưa biết. Đây là giới hạn forensic provenance, không được lấp bằng metadata giả.

## 8. Remediation đã thực hiện

1. Giữ nguyên protocol hiện tại, cả hai packet ZIP, reviewer packet, annotations và audit lịch sử.
2. Bảo tồn bản manifest trước sửa tại [reviewer_sources_before.md](E:/AAI/misconceptions-prototype/results/itsp/multi_agent_validation/2026-09-20/provenance_reconciliation/reviewer_sources_before.md).
3. Sửa duy nhất đích link của mục protocol trong manifest sang snapshot lịch sử khớp **9fd…**; **giữ nguyên hash 9fd…**. Thêm ghi chú phân biệt snapshot nguồn và protocol hiện tại. Không làm thao tác `9fd… → 1cc…` để vượt audit.
4. Ghi [validation_revision_2026-09-20_provenance.json](E:/AAI/misconceptions-prototype/results/itsp/validation_revision_2026-09-20_provenance.json), gồm chuỗi hash protocol và hash manifest trước/sau. Dùng hậu tố `_provenance` để không ghi đè `validation_revision_2026-09-20.json` đã tồn tại.

Không cần regenerate packet chỉ vì clarification này: không đổi sample/evidence/blinding/metric requirements; các gói cũ được re-audit. Khi sửa substantive protocol trong tương lai cần khóa version mới và tái đánh giá dependency.

## 9. Verification sau reconciliation

- `.venv/Scripts/python.exe -m pytest -q`: **106 passed, 3 subtests passed**.
- `.venv/Scripts/python.exe -m ruff check .`: **All checks passed**.
- Manifest nguồn đã sửa: **255/255 hash khớp**.
- Kiểm tra snapshot: 9fd… và 1cc… đều khớp; current protocol không bị sửa.
- Gọi hàm audit round1 hiện có, không chạy entry point ghi đè audit cũ: đạt, **72 file**.
- CRC và so từng member ZIP với folder tương ứng: round1 **72 file**, round2 **240 file**, đều khớp byte.
- Đối chiếu 777 artifact trước nhiệm vụ: chỉ `reviewer_sources.md` thay đổi có chủ đích; 776 artifact còn lại giữ nguyên.

[Provenance audit](E:/AAI/misconceptions-prototype/results/itsp/multi_agent_validation/2026-09-20/provenance_reconciliation/provenance_audit.json). Tests chỉ xác nhận kiểm tra phần mềm hiện có, không xác nhận human validation. Audit lịch sử vẫn áp dụng cho snapshot lịch sử; hash manifest mới được quản lý bằng record mới, không sửa lại lịch sử.

## 10. Resume decision

**`READY_FOR_MULTI_AGENT_PREFLIGHT`**, chỉ có nghĩa đã giải quyết blocker provenance này và có thể khởi động lại preflight. Báo cáo BLOCKED và stop event trước được giữ nguyên như lịch sử; record reconciliation/revision mới là phần nối tiếp, không phủ nhận sự kiện STOP đã xảy ra.

Không khởi động lại agent, không annotation, không adjudication và không evaluation sampling trong nhiệm vụ này. Human validation vẫn pending. Preflight tiếp theo phải dùng snapshot link trong manifest đã reconciled, không coi protocol 1cc… là nguồn sinh packet lịch sử.

```text
RECONCILIATION STATUS:
RESOLVED_SAME_SEMANTIC_VERSION

VALIDATION RESUME:
YES

REASON:
Đã tái dựng đúng old hash, xác nhận delta chỉ editorial/clarification,
giữ dependency chưa biết là UNKNOWN, bảo tồn các phiên bản và audit cũ,
sửa link tới snapshot lịch sử đúng hash và hoàn tất tests/lint/provenance audit.
YES chỉ cho phép quay lại multi-agent preflight; chưa tiếp tục validation thực tế.
```
