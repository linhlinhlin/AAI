# MULTI-AGENT RESEARCH VALIDATION PROTOCOL

## Đề tài 5 — Misconceptions Clustering

Repository:

`E:/AAI/misconceptions-prototype`

Ngày baseline:

`20/09/2026`

---

# 0. VAI TRÒ VÀ MỤC TIÊU

Bạn là **Lead Research Agent**, chịu trách nhiệm điều phối toàn bộ quá trình validation trong repository.

Người nghiên cứu chính đang bận và **không trực tiếp review từng mẫu**.

Do đó, hãy sử dụng nhiều subagent với vai trò độc lập để:

1. audit protocol;
2. review codebook;
3. review evidence;
4. kiểm tra annotation;
5. adversarially challenge kết luận;
6. kiểm tra leakage;
7. kiểm tra sampling/evaluation design;
8. tổng hợp recommendation.

## QUY TẮC CỰC KỲ QUAN TRỌNG

Các subagent AI **không được tự nhận là human expert**.

Không được ghi:

* `reviewer_type = human`
* `expert_validated = true`
* `approved_by = <AI agent>`
* human agreement
* Cohen's kappa giữa AI agents dưới tên expert agreement
* human adjudication

trừ khi dữ liệu thực sự đến từ người chấm chuyên gia bên ngoài.

AI review chỉ được ghi dưới:

`reviewer_type = AI`

và phải bảo toàn provenance.

---

# 1. KIẾN TRÚC SUBAGENT

Tạo tối thiểu các vai trò sau.

## Agent 0 — LEAD / ORCHESTRATOR

Nhiệm vụ:

* đọc protocol;
* chia task;
* quản lý artifact;
* kiểm tra dependency;
* tổng hợp kết quả;
* quyết định khi nào cần STOP;
* không tự đóng vai expert.

Agent 0 không được tự tạo final expert label chỉ vì các subagent AI đồng thuận.

---

## Agent 1 — METHODOLOGY AUDITOR

Nhiệm vụ:

Review:

* `itsp_validation_revision.md`
* `itsp_human_review_protocol.md`
* `itsp_validation.md`
* `itsp_progress.md`

Kiểm tra:

* protocol có nhất quán không;
* thứ tự các bước có leakage không;
* expert validation có bị trộn với AI review không;
* metric có đúng denominator không;
* evaluation set có nguy cơ contamination không.

Output:

```text
METHOD
PASS / BLOCK

Findings:
...

Required changes:
...
```

---

# 2. AGENT 2 — CODEBOOK REVIEWER

Đọc:

`results/itsp/human_review/CODEBOOK.md`

Review độc lập:

* định nghĩa misconception;
* Yes/No/Unclear;
* primary type;
* OTHER_CONCEPT;
* confidence;
* evidence;
* multi-error;
* coding mistake vs misconception;
* insufficient evidence;
* adjudication rule.

Không xem recommendation của Agent 3 trước khi hoàn tất.

Output:

```text
CODEBOOK REVIEW

Definition clarity:
...

Ambiguities:
...

Potential disagreement cases:
...

Required revisions:
...

Recommendation:
ACCEPT / REVISE / BLOCK
```

---

# 3. AGENT 3 — ADVERSARIAL CODEBOOK REVIEWER

Agent này phải có nhiệm vụ **phản biện**, không cố tìm đồng thuận.

Tìm:

* định nghĩa circular;
* label leakage;
* taxonomy overlap;
* ambiguous examples;
* cases where two reasonable reviewers can disagree;
* cases where coding mistake bị nhầm thành misconception;
* cases where a test failure alone không đủ chứng minh misconception;
* cases where cluster context có thể gây confirmation bias.

Không đọc kết quả của Agent 2 trước khi hoàn tất.

Output:

```text
ADVERSARIAL CODEBOOK REVIEW

Critical ambiguity:
...

Counterexamples:
...

Potential reviewer disagreement:
...

Severity:
LOW / MEDIUM / HIGH / BLOCKER

Recommendation:
...
```

---

# 4. AGENT 4 — DATA / PROVENANCE AUDITOR

Kiểm tra:

* raw source;
* manifests;
* hashes;
* submission JSONL;
* review JSONL;
* test records;
* OAV;
* cluster assignments;
* reviewer packet.

Đặc biệt kiểm tra:

* 17 review samples;
* 59 development-exposed samples;
* packet round 1;
* packet round 2;
* provenance sau khi packet thay đổi.

Không đánh giá misconception.

Nhiệm vụ chỉ là:

> “Evidence có đúng là evidence của sample đó không?”

Output:

```text
PROVENANCE AUDIT

Samples checked:
...

Hash consistency:
PASS/FAIL

Missing evidence:
...

Leakage:
NONE / POSSIBLE / CONFIRMED

Recommendation:
...
```

---

# 5. AGENT 5 — ANNOTATION CONSISTENCY REVIEWER

Nếu đã có AI annotation:

Review AI annotation về:

* schema;
* completeness;
* consistency;
* evidence linkage;
* type consistency;
* confidence consistency.

NHƯNG:

Agent này tuyệt đối không biến AI annotation thành expert ground truth.

Nếu có human annotation thật, Agent 5 chỉ được QA format và consistency; không được sửa human label.

Output:

```text
ANNOTATION QA

Schema:
PASS/FAIL

Completeness:
...

Evidence linkage:
...

Potential inconsistencies:
...

No human labels modified:
TRUE
```

---

# 6. AGENT 6 — INDEPENDENT SAMPLE REVIEWER

Đây là agent chuyên đọc **17 mẫu**.

Chia 17 mẫu thành các partition độc lập, ví dụ:

* Agent 6A: samples 1–6
* Agent 6B: samples 7–12
* Agent 6C: samples 13–17

Nếu framework hỗ trợ nhiều subagent, tạo ba instance hoàn toàn độc lập.

Mỗi instance phải đọc:

* assignment;
* student source;
* corrected/reference source nếu protocol cho phép;
* test inputs;
* expected;
* actual;
* OAV;
* relevant structural features.

Đánh giá theo codebook nhưng ghi rõ:

`reviewer_type = AI`

Mỗi sample phải có:

```text
misconception:
YES / NO / UNCLEAR

type:
...

confidence:
...

evidence:
...

alternative_explanation:
...

why_not_other_label:
...
```

Đặc biệt bắt buộc:

`alternative_explanation`

để chống confirmation bias.

---

# 7. AGENT 7 — CROSS-REVIEWER / PEER REVIEW AGENT

Sau khi Agent 6A/B/C hoàn thành, Agent 7 được cung cấp các review của họ.

Nhiệm vụ:

Không đơn giản majority vote.

Phải tìm:

* disagreement;
* unsupported inference;
* evidence asymmetry;
* label drift;
* codebook ambiguity;
* reviewer overconfidence;
* cases where all AI reviewers may have made the same assumption.

Output:

```text
PEER REVIEW REPORT

Sample:
...

Reviewer A:
...

Reviewer B:
...

Reviewer C:
...

Agreement:
...

Evidence supports:
...

Evidence does not support:
...

Most defensible status:
...

Human expert required:
YES
```

`Most defensible status` chỉ là AI research recommendation, **không phải expert ground truth**.

---

# 8. AGENT 8 — CLUSTER BLINDNESS AUDITOR

Nhiệm vụ đặc biệt quan trọng.

Kiểm tra xem reviewer có vô tình biết cluster assignment trước khi independent review hay không.

Phân loại:

```text
BLIND
PARTIALLY_BLIND
NON-BLIND
UNKNOWN
```

Nếu independent round 1 đã nhìn cluster:

→ đánh dấu contamination.

Không được gọi đó là independent expert agreement.

---

# 9. AGENT 9 — CLUSTER INTERPRETATION REVIEWER

Chỉ chạy **sau khi round-1 AI review đã khóa**.

Agent này được cung cấp:

* cluster assignments;
* cluster members;
* test signatures;
* structural features;
* review evidence.

Nhiệm vụ:

Đánh giá:

* cluster có homogeneous mechanism không;
* mixed causes;
* outliers;
* over-clustering;
* under-clustering;
* cluster interpretation có vượt quá evidence không.

Không được thay đổi round-1 labels.

Output:

```text
CLUSTER REVIEW

Cluster:
...

Common observable behavior:
...

Possible mechanism:
...

Mixed causes:
...

Outliers:
...

Evidence strength:
LOW / MEDIUM / HIGH

Misconception claim justified:
YES / NO / UNCLEAR
```

---

# 10. AGENT 10 — ADVERSARIAL SCIENTIFIC REVIEWER

Agent này đóng vai **reviewer khó tính của một bài báo**.

Đọc toàn bộ:

* pipeline;
* A/B/C;
* expert validation protocol;
* AI reviews;
* cluster analysis;
* proposed conclusions.

Tìm các lỗi:

### Overclaim

Ví dụ:

> “Cluster represents misconception.”

nếu evidence chỉ cho thấy:

> “Cluster represents similar error manifestations.”

### Leakage

Ví dụ:

* reviewer nhìn cluster trước round 1;
* evaluation sample từng được tuning;
* AI labels dùng để chọn evaluation sample.

### Circularity

Ví dụ:

> feature được thiết kế từ giả thuyết misconception → cluster → rồi cluster được dùng làm evidence cho chính misconception đó.

### Selection bias

Ví dụ:

> chọn mẫu vì nó thể hiện cluster rõ.

### Metric misuse

Ví dụ:

* purity không đủ denominator;
* kappa dùng sai population;
* 0 thay cho null.

Output:

```text
SCIENTIFIC REVIEW

Major threats:
...

Minor threats:
...

Unsupported claims:
...

Required corrections:
...

Publication-risk level:
LOW / MEDIUM / HIGH
```

---

# 11. AGENT 11 — EVALUATION SET DESIGNER

Agent này KHÔNG được biết kết quả cuối cùng của evaluation set khi thiết kế sampling rule.

Đọc:

`development_exposure_manifest.json`

Xác định:

* 59 bài development exposure;
* 17 reviewed samples;
* mọi artifact đã dùng để development;
* các sample cần loại khỏi holdout.

Sau đó đề xuất sampling rule.

Sampling rule phải được khóa trước khi xem kết quả evaluation.

Ví dụ:

```text
population:
all eligible submissions not in development exposure

exclusion:
development exposure + parser failures + insufficient provenance

sampling:
stratified random sampling

strata:
problem × observable test-failure profile

seed:
<fixed seed>

n:
<predefined>
```

Không chọn mẫu vì kết quả cluster đẹp.

---

# 12. AGENT 12 — EVALUATION SET ADVERSARY

Review sampling proposal của Agent 11.

Tìm:

* contamination;
* cherry-picking;
* post-hoc stratification;
* hidden use of expert labels;
* hidden use of cluster quality;
* sample overlap;
* same-source leakage;
* student-level leakage.

Output:

```text
EVALUATION AUDIT

Leakage:
...

Selection bias:
...

Overlap:
...

Independence:
...

Recommendation:
LOCK / REVISE / BLOCK
```

---

# 13. AGENT 13 — FINAL INTEGRITY AUDITOR

Chạy cuối cùng.

Kiểm tra toàn bộ repository.

Checklist:

### Human validation

* [ ] Human annotations thực sự tồn tại
* [ ] Human reviewer IDs hợp lệ
* [ ] Codebook expert-approved
* [ ] Round 1 preserved
* [ ] Adjudication separate
* [ ] AI not used as ground truth

### Metrics

* [ ] human-only
* [ ] correct denominator
* [ ] coverage reported
* [ ] null preserved
* [ ] no fabricated zero

### Dataset

* [ ] raw source preserved
* [ ] provenance valid
* [ ] no fake student IDs

### Evaluation

* [ ] 59 development-exposed samples excluded
* [ ] 17 reviewed samples excluded where appropriate
* [ ] sampling rule locked
* [ ] seed recorded
* [ ] manifest hashed

### Reporting

* [ ] cluster ≠ automatically misconception
* [ ] structural improvement not claimed without evidence
* [ ] negative findings retained
* [ ] limitations updated

---

# 14. CƠ CHẾ REVIEW LẪN NHAU

Không được chạy tất cả agent theo một chuỗi mà agent sau chỉ kiểm tra output của agent trước.

Phải có **independent branches**.

Thiết kế tối thiểu:

```text
                    ┌── Methodology Auditor
                    │
                    ├── Codebook Reviewer
                    │
                    ├── Adversarial Codebook Reviewer
                    │
Raw Evidence ────────┼── Provenance Auditor
                    │
                    ├── Sample Reviewer A
                    ├── Sample Reviewer B
                    └── Sample Reviewer C
                              │
                              ▼
                     Cross-Reviewer Agent
                              │
                              ▼
                    Adversarial Reviewer
                              │
                              ▼
                     Lead Agent synthesis
```

Các agent độc lập phải hoàn thành trước khi được phép xem output của nhau.

---

# 15. NGUYÊN TẮC KHÔNG DÙNG MAJORITY VOTE MỘT CÁCH MÁY MÓC

Không được viết:

> 3/3 AI agents nói YES → expert validation = YES.

Thay vào đó:

> 3 AI agents independently identified evidence consistent with X.

Sau đó:

> Human expert validation required.

AI consensus chỉ là **triangulated AI evidence**.

Không gọi là expert agreement.

---

# 16. HUMAN REVIEW GATE

Đây là gate bắt buộc.

Nếu không có human annotations thật:

```text
HUMAN VALIDATION STATUS = PENDING
```

Không được chuyển thành:

```text
COMPLETE
```

dù:

* 3 AI reviewers đồng ý;
* 10 AI reviewers đồng ý;
* codebook đã được AI review;
* tất cả tests pass.

---

# 17. NẾU KHÔNG CÓ CHUYÊN GIA THẬT

Nếu hiện tại hoàn toàn không có expert nào tham gia, hãy hoàn tất tối đa phần:

### AI-assisted validation preparation

bao gồm:

* codebook critique;
* adversarial review;
* evidence audit;
* AI independent review;
* cross-review;
* cluster audit;
* evaluation-set design;
* leakage audit.

Nhưng kết luận cuối phải là:

```text
Human expert validation: NOT COMPLETED
AI-assisted validation preparation: COMPLETED
```

Không được gọi đây là:

> expert validation completed.

---

# 18. ADJUDICATION POLICY

Nếu có human annotations thật:

AI agents chỉ được:

* phát hiện disagreement;
* chuẩn bị evidence;
* chỉ ra ambiguity;
* đưa ra alternative explanations;
* kiểm tra consistency.

AI không được tự quyết định adjudication thay human adjudicator.

Human adjudicator phải quyết định:

* final Yes/No/Unclear;
* final type;
* final evidence interpretation.

AI có thể audit quyết định sau đó nhưng không được ghi đè.

---

# 19. NEW EVALUATION SET

Sau khi validation protocol được khóa:

1. đọc development exposure manifest;
2. tạo exclusion list;
3. xác định candidate pool;
4. khóa sampling rule;
5. chọn sample bằng fixed seed;
6. tạo manifest;
7. hash manifest;
8. chạy leakage audit;
9. khóa evaluation set.

Không chạy feature tuning trên evaluation set.

---

# 20. FINAL REPORT

Tạo:

`results/itsp/multi_agent_validation_report.md`

Cấu trúc:

```text
# Multi-Agent Validation Report

## 1. Status

## 2. Agent roster

## 3. Codebook review

## 4. Evidence audit

## 5. AI independent review

## 6. Cross-review

## 7. Adversarial review

## 8. Human validation status

## 9. Adjudication status

## 10. Metrics

## 11. Development exposure

## 12. New evaluation set

## 13. Leakage audit

## 14. Scientific limitations

## 15. Remaining blockers

## 16. Recommended next actions
```

---

# 21. FINAL STATUS ENUM

Chỉ được sử dụng một trong:

```text
AI_PREVALIDATION_COMPLETE
HUMAN_VALIDATION_PENDING
HUMAN_VALIDATION_IN_PROGRESS
HUMAN_VALIDATION_COMPLETE
BLOCKED
```

Không sử dụng:

```text
EXPERT_VALIDATED
```

nếu không có expert human evidence.

---

# 22. QUY TẮC STOP

Lead Agent phải STOP ngay nếu phát hiện:

* AI annotation bị ghi thành human;
* reviewer leakage;
* cluster information xuất hiện trong blind round;
* human annotation bị overwrite;
* provenance/hash mismatch;
* evaluation sample nằm trong development exposure;
* codebook chưa được approved nhưng pipeline đang dùng nó để tạo “final expert labels”;
* thiếu denominator nhưng metric vẫn được tính;
* agent cố biến consensus AI thành expert consensus.

Khi STOP, xuất:

```text
BLOCKED AT:
...

REASON:
...

EVIDENCE:
...

AFFECTED ARTIFACTS:
...

WHAT MUST HAPPEN BEFORE RESUMING:
...
```

---

# 23. NGUYÊN TẮC CUỐI CÙNG

Mục tiêu của multi-agent system không phải là tạo ra nhiều AI votes nhất.

Mục tiêu là:

1. giảm lỗi phương pháp;
2. phát hiện confirmation bias;
3. phát hiện leakage;
4. kiểm tra provenance;
5. chuẩn bị evidence cho human expert;
6. bảo vệ evaluation set;
7. làm cho kết luận khoa học audit được.

**AI agents có thể review lẫn nhau, phản biện lẫn nhau và audit lẫn nhau. Nhưng AI consensus không được đổi tên thành human expert validation.**
