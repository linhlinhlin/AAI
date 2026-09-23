# PROVENANCE RECONCILIATION — ĐỀ TÀI 5

Repository:

`E:/AAI/misconceptions-prototype`

Trạng thái hiện tại:

`BLOCKED`

Lý do:

`reviewer_sources.md` ghi SHA-256 của:

`docs/itsp_human_review_protocol.md`

là:

`9fdba3fd66d512a1775699f0501eff0a5bcc3750a9196829a6db26c2fcd783bb`

nhưng file hiện tại có:

`1cc8ce739a1497bf6d64c4621f5388f1ff7192272d23bca019bbcf6a491a2cd2`

## MỤC TIÊU

Không tiếp tục annotation/review/evaluation.

Không thay hash để làm audit PASS.

Không khôi phục file một cách mù quáng.

Nhiệm vụ duy nhất là xác định:

> Hash `9fd...` đại diện cho phiên bản protocol nào, được sử dụng ở giai đoạn nào, và file hiện tại `1cc...` là thay đổi hợp lệ hay là sai lệch ngoài kiểm soát.

---

# 1. BẢO TOÀN TRẠNG THÁI

Trước khi làm bất kỳ thay đổi nào:

* không sửa `reviewer_sources.md`;
* không sửa protocol hiện tại;
* không sửa annotation;
* không sửa packet;
* không sửa audit lịch sử.

Tạo một reconciliation workspace riêng:

`results/itsp/multi_agent_validation/2026-09-20/provenance_reconciliation/`

Ghi hash hiện tại của tất cả artifact liên quan.

---

# 2. XÁC ĐỊNH NGUỒN CỦA HASH CŨ

Tìm trong repository toàn bộ xuất hiện của:

`9fdba3fd66d512a1775699f0501eff0a5bcc3750a9196829a6db26c2fcd783bb`

Tìm:

* git history;
* commit;
* audit;
* packet manifest;
* ZIP metadata;
* validation revision;
* reviewer packet;
* README;
* provenance;
* generated artifact.

Mục tiêu là tìm evidence trực tiếp cho biết hash này thuộc version nào.

Không suy đoán chỉ từ timestamp.

---

# 3. GIT / FILE HISTORY

Nếu repository có git history, kiểm tra:

* commit chứa protocol version `9fd...`;
* commit thay đổi protocol thành `1cc...`;
* author/commit metadata;
* commit message;
* parent/child relationship;
* thời điểm thay đổi.

Nếu không có git history đầy đủ:

ghi rõ:

`git provenance unavailable`

và chuyển sang forensic file provenance.

---

# 4. RECONSTRUCT HASH CŨ

Nếu có thể xác định commit/version chứa hash cũ:

tái tạo bản protocol đó trong một file forensic riêng, ví dụ:

`protocol_snapshot_hash_9fd....md`

Không overwrite protocol hiện tại.

Kiểm tra SHA-256 của snapshot có đúng:

`9fdba3fd66d512a1775699f0501eff0a5bcc3750a9196829a6db26c2fcd783bb`

hay không.

Nếu không tái tạo được hash cũ:

ghi:

`OLD_VERSION_NOT_RECONSTRUCTABLE`

Không đoán.

---

# 5. DIFF HAI PHIÊN BẢN

Nếu reconstruct được cả hai version:

diff:

`9fd...` vs `1cc...`

Phân loại từng thay đổi:

### A — Editorial

Ví dụ:

* typo;
* formatting;
* heading;
* wording không thay đổi semantics.

### B — Protocol clarification

Ví dụ:

* bổ sung giải thích;
* không thay đổi eligibility;
* không thay đổi reviewer role;
* không thay đổi evidence requirement.

### C — Material protocol change

Ví dụ:

* thay đổi blind/unblind;
* thay đổi sample;
* thay đổi reviewer role;
* thay đổi adjudication;
* thay đổi metric;
* thay đổi inclusion/exclusion;
* thay đổi cluster visibility;
* thay đổi evaluation design.

Phải ghi rõ từng thay đổi.

---

# 6. KIỂM TRA PACKET DEPENDENCY

Xác định packet nào được tạo dựa trên version `9fd...`.

Kiểm tra:

* human review packet;
* round 2 packet;
* reviewer packet;
* README;
* codebook;
* annotations;
* audit.

Tạo dependency table:

| Artifact | Protocol hash | Status |
| -------- | ------------- | ------ |
| packet X | 9fd...        | ...    |
| packet Y | 1cc...        | ...    |
| audit Z  | ...           | ...    |

Không suy ra protocol hash của artifact nếu không có evidence.

---

# 7. QUYẾT ĐỊNH PROVENANCE

Chỉ được chọn một trong bốn trạng thái:

## `RESOLVED_SAME_SEMANTIC_VERSION`

Hai version khác hash nhưng khác biệt chỉ editorial/không material.

Có thể tiếp tục sau khi cập nhật provenance đúng cách.

## `RESOLVED_MATERIAL_REVISION`

Version hiện tại là revision material.

Phải:

* bảo tồn version cũ;
* ghi revision chain;
* xác định packet nào dùng version nào;
* không retroactively nói packet cũ dùng version mới.

Sau đó phải đánh giá lại packet có cần regenerate hay không.

## `UNRESOLVED`

Không đủ evidence để biết version nào được dùng.

Không được tiếp tục validation.

## `INTEGRITY_FAILURE`

Có evidence rằng artifact bị thay đổi ngoài provenance hợp lệ.

Dừng toàn bộ validation và báo cáo.

---

# 8. KHÔNG ĐƯỢC “FIX HASH”

TUYỆT ĐỐI KHÔNG làm:

```text
9fd... → 1cc...
```

chỉ để audit pass.

Chỉ cập nhật manifest khi đã xác định:

1. artifact hiện tại là version hợp lệ;
2. version cũ được bảo toàn;
3. revision chain được ghi;
4. packet dependency được xác định.

---

# 9. NẾU VERSION HIỆN TẠI LÀ REVISION HỢP LỆ

Tạo:

`results/itsp/validation_revision_<date>.json`

với:

```json
{
  "artifact": "docs/itsp_human_review_protocol.md",
  "previous_sha256": "...",
  "current_sha256": "...",
  "revision_status": "material|editorial",
  "previous_version_preserved": true,
  "change_summary": [],
  "packet_dependencies_checked": true,
  "review_required": true
}
```

Không xóa audit cũ.

---

# 10. SAU RECONCILIATION

Chạy lại:

```powershell
.venv/Scripts/python.exe -m pytest -q
.venv/Scripts/python.exe -m ruff check .
```

Sau đó chạy audit provenance tương ứng.

Chỉ chuyển trạng thái từ:

`BLOCKED`

sang:

`READY_FOR_MULTI_AGENT_PREFLIGHT`

nếu provenance đã được giải quyết.

---

# 11. QUY TẮC RESUME

Nếu:

`RESOLVED_SAME_SEMANTIC_VERSION`

→ có thể tiếp tục preflight.

Nếu:

`RESOLVED_MATERIAL_REVISION`

→ trước tiên xác định packet nào cần regenerate/re-audit.

Nếu:

`UNRESOLVED`

→ STOP.

Nếu:

`INTEGRITY_FAILURE`

→ STOP và không tạo annotation/evaluation.

---

# 12. OUTPUT

Tạo:

`results/itsp/multi_agent_validation/2026-09-20/provenance_reconciliation/reconciliation_report.md`

Bao gồm:

1. old hash;
2. current hash;
3. evidence tìm được;
4. old version reconstruction;
5. diff;
6. packet dependency;
7. semantic/material classification;
8. integrity assessment;
9. required remediation;
10. resume decision.

Cuối file phải có:

```text
RECONCILIATION STATUS:
...

VALIDATION RESUME:
YES / NO

REASON:
...
```

Không thực hiện bất kỳ annotation, adjudication hoặc evaluation sampling nào trong nhiệm vụ này.
