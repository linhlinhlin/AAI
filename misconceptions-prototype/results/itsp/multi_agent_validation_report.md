# Multi-Agent Validation Report

Baseline yêu cầu: 20/09/2026. Đây là báo cáo AI-assisted validation; không phải human expert validation. Protocol thực thi được lưu nguyên văn tại [request_protocol.md](E:/AAI/misconceptions-prototype/results/itsp/multi_agent_validation/2026-09-20/request_protocol.md).

## 1. Status

**Final status: `BLOCKED`.**

```text
BLOCKED AT:
Preflight provenance gate, trong đợt audit độc lập đầu tiên.

REASON:
Hash của một nguồn đang được reviewer_sources.md tham chiếu không khớp
với nội dung file hiện tại. Kích hoạt quy tắc STOP tại mục 22 của protocol.

EVIDENCE:
Manifest: results/itsp/reviewer_sources.md, dòng 216
Source: docs/itsp_human_review_protocol.md
Expected SHA-256:
9fdba3fd66d512a1775699f0501eff0a5bcc3750a9196829a6db26c2fcd783bb
Actual SHA-256:
1cc8ce739a1497bf6d64c4621f5388f1ff7192272d23bca019bbcf6a491a2cd2

AFFECTED ARTIFACTS:
docs/itsp_human_review_protocol.md
results/itsp/reviewer_sources.md
Các kết luận audit phụ thuộc việc manifest trỏ đúng phiên bản protocol.

WHAT MUST HAPPEN BEFORE RESUMING:
Xác định phiên bản protocol thực sự dùng để tạo packet; giải thích và lưu
nguồn gốc thay đổi. Giữ snapshot/hash cũ, tạo bản provenance sửa đổi hoặc
khôi phục đúng snapshot theo bằng chứng. Kiểm tra lại dependency/hash,
rồi mới khởi động lại các nhánh và mở vòng annotation/evaluation.
Không chỉ thay expected hash bằng actual hash để làm kiểm tra thành PASS.
```

Sự kiện có máy đọc được: [stop_event.json](E:/AAI/misconceptions-prototype/results/itsp/multi_agent_validation/2026-09-20/stop_event.json). Hash mismatch xác nhận sự không nhất quán của tham chiếu phiên bản; chưa chứng minh raw code/test bị hỏng hoặc đã có hành vi gian lận.

## 2. Agent roster

Đã khởi tạo ba subagent có ngữ cảnh mới (`fork_turns=none`), không truyền nội dung các review trước. Mỗi nhánh được yêu cầu không đọc kết quả của nhánh khác. Giới hạn thực thi là ba subagent đồng thời, nên các vai trò còn lại được dự kiến chạy theo đợt và theo dependency.

| Vai trò | Agent/task | Trạng thái tại STOP |
|---|---|---|
| 0 — Lead / orchestrator | `/root` | Phát hiện mismatch, dừng các nhánh, lập báo cáo |
| 1 — Methodology auditor | `/root/methodology_auditor` | Đã chạy, bị ngắt; chưa có báo cáo cuối |
| 2 — Codebook reviewer | `/root/codebook_reviewer` | Đã chạy độc lập, bị ngắt; chưa có báo cáo cuối |
| 3 — Adversarial codebook reviewer | `/root/adversarial_codebook` | Đã chạy độc lập, bị ngắt; chưa có báo cáo cuối |
| 4 — Data / provenance auditor | Chưa khởi tạo | Dừng trước bước này; Lead chỉ làm preflight hash |
| 5 — Annotation QA | Chưa khởi tạo | Chưa thực hiện |
| 6A / 6B / 6C — Sample reviewers | Chưa khởi tạo | Chưa phát evidence, chưa annotation |
| 7 — Cross-reviewer | Chưa khởi tạo | Chưa có các review vòng 1 để đối chiếu |
| 8 — Cluster blindness auditor | Chưa khởi tạo | Chưa thực hiện |
| 9 — Cluster interpretation reviewer | Chưa khởi tạo | Chưa khóa vòng 1; không đủ điều kiện chạy |
| 10 — Scientific adversary | Chưa khởi tạo | Chưa thực hiện |
| 11 — Evaluation set designer | Chưa khởi tạo | Chưa khóa sampling rule |
| 12 — Evaluation set adversary | Chưa khởi tạo | Chưa có proposal để audit |
| 13 — Final integrity auditor | Chưa khởi tạo | Chưa được phép chứng nhận hoàn tất |

Không coi nhánh bị ngắt là hoàn thành, không gán PASS/ACCEPT thay agent và không tạo kết quả đồng thuận giả định.

## 3. Codebook review

Hai nhánh 2 và 3 được giao review độc lập cùng codebook và tài liệu phiếu trống; không được đọc annotation cũ, cluster packet hoặc báo cáo của nhau. Chưa có kết quả cuối trước STOP. Codebook hiện đọc được trong dữ liệu vẫn là `human-review-draft-v1`, `approved_by=null`. Không có phê duyệt mới được tạo.

## 4. Evidence audit

Lead đối chiếu 255 mục hash trong reviewer_sources.md với file hiện tại: 254 khớp, một mismatch ở human review protocol. Phép kiểm tra mục mismatch được lặp riêng để xác nhận trước khi ghi STOP.

Hash hiện tại của reviewer_sources.md là `16ec7e064f43030199bc0818410e28f97bff74f879294e72a82f3ed85514a168`. Nguồn này ghi hash cũ của protocol dù file protocol hiện tại có hash khác.

Packet từng đổi tiêu đề/cảnh báo vòng 2 đã có ghi chú và chuỗi nối từ audit lịch sử sang `validation_revision_2026-09-20.json`. Không dùng việc hash packet khác bản review trước làm lý do STOP; nguyên nhân STOP là tham chiếu nguồn protocol không khớp vừa nêu.

Chưa chạy audit nội dung đầy đủ của raw/JSONL/OAV/round1/round2 trong lượt này. Quá trình tạo baseline toàn repository được ngắt, chưa tạo ra snapshot hoàn chỉnh. Không tái sử dụng kết quả audit lịch sử như thể vừa kiểm tra toàn bộ trạng thái mới.

## 5. AI independent review

Chưa bắt đầu lượt review 17 mẫu mới. Không tạo AI label mới, không chuyển annotation cũ vào vòng mới. Kế hoạch trước STOP là cung cấp đề/source/reference/test/OAV đã loại cluster assignment; reference được phép hiển thị và phải ghi rõ điều kiện này. Nhãn AI sẽ dùng `reviewer_type=AI`, không nhập vào human ground truth.

## 6. Cross-review

Chưa thực hiện. Ba partition rời nhau không đồng nghĩa ba reviewer đã chấm từng mẫu; báo cáo sau này phải ghi người nào thực sự đọc mẫu nào. Những ô reviewer chưa chấm phải ghi không có quan sát, không được tạo 3/3 agreement. Peer review cần đối chiếu bằng chứng và giả thuyết thay thế thay vì majority vote.

## 7. Adversarial review

Nhánh adversarial codebook đã khởi động nhưng bị ngắt trước kết luận. Scientific adversary chưa chạy. Không dùng ý kiến Lead làm thay kết quả của các vai trò này.

## 8. Human validation status

**`HUMAN_VALIDATION_PENDING`. Human expert validation: NOT COMPLETED.**

File metrics hiện có ghi 0 completed human reviews, 0 adjudications, codebook chưa sẵn sàng. File `data/itsp/expert_annotations.json` có các record AI được nhận diện bằng `ai:` và các record pending; tên file không làm chúng trở thành nhãn chuyên gia thật. Đây là quan sát ban đầu, chưa thay thế QA toàn bộ schema/danh tính.

Không ghi `reviewer_type=human`, không ký `approved_by`, không gán `expert_validated=true`.

## 9. Adjudication status

Adjudication vẫn pending theo trạng thái hiện có. Không adjudicate bằng AI; không đổi label của người thật hoặc label AI cũ. Mọi bước đánh giá human tiếp theo vẫn cần người chịu trách nhiệm bên ngoài.

## 10. Metrics

Không tính metrics mới. Human purity/agreement hiện có vẫn null; không chuyển null thành 0. Số review đã hoàn tất bằng 0 là số đếm, khác việc gán một metric chưa xác định bằng 0.

Không tính Cohen's kappa giữa AI dưới tên expert agreement. Kiểm tra denominator toàn diện và audit human-only còn chưa hoàn tất.

## 11. Development exposure

Đã xác nhận repository có `results/itsp/development_exposure_manifest.json`, mô tả 59 development-exposed samples và trạng thái chưa chọn evaluation mới. Chưa hoàn tất đối chiếu toàn bộ ID/hash với mọi artifact đã dùng cho phát triển. Không kết luận 59 ID là danh sách exposure đầy đủ cho tất cả hoạt động lịch sử trước khi audit.

17 mẫu đã review cần được giữ trong phạm vi phát triển cho thí nghiệm feature mới; không đổi tên holdout cũ thành evaluation độc lập.

## 12. New evaluation set

Chưa thiết kế/khóa sampling rule, chưa đặt seed mới, chưa chọn mẫu, chưa tạo manifest evaluation. Không thực hiện sampling khi provenance gate đang BLOCKED. Không xem hoặc tuning trên evaluation mới trong lượt này.

## 13. Leakage audit

**Trạng thái: chưa đủ kiểm tra để phân loại toàn quy trình.** Không ghi NONE hoặc BLIND cho các bước chưa audit. Vòng sample review mới chưa được mở, nên chưa có reviewer sample mới bị phát cluster assignment trong lượt này. Các nhánh methodology/codebook không phải là vòng annotation mù.

Sau khi tiếp tục: kiểm tra allowlist và access log của từng sample reviewer; khóa hash kết quả vòng 1 trước mở assignments cho cluster reviewer. Fresh context và instruction isolation chỉ giảm truyền kết luận; không phải sandbox truy cập filesystem hay bảo đảm độc lập thống kê giữa các mô hình AI.

## 14. Scientific limitations

- Dừng sớm: chưa hoàn thành codebook critique, sample review, cross-review, cluster audit hoặc sampling design.
- Hash mismatch chưa được truy nguyên; stale manifest là một giả thuyết, không phải nguyên nhân đã xác nhận.
- AI review không xác nhận trạng thái nhận thức sinh viên, không thay nhãn human và không phê duyệt taxonomy.
- Không có ID sinh viên đáng tin thì chưa bảo đảm student-disjoint evaluation hoặc tỷ lệ sinh viên hiểu sai.
- Không có kết quả mới để tuyên bố structural improvement, chất lượng misconception hay vượt SOTA.
- Không gửi liên hệ, file hoặc tin nhắn cho chuyên gia bên ngoài.

## 15. Remaining blockers

1. **Blocker kích hoạt STOP:** nguồn protocol không khớp hash đang khai trong manifest reviewer.
2. **Gate human vẫn pending:** chưa có codebook được người thật duyệt, annotation độc lập và adjudication.
3. **Các dependency chưa thực hiện:** independent AI review → freeze → peer/cluster review; sampling proposal → adversarial audit → locked evaluation; final integrity audit.

AI-assisted validation preparation: **NOT COMPLETED** trong lượt này. Không dùng `AI_PREVALIDATION_COMPLETE` khi đã dừng trước các bước bắt buộc.

## 16. Recommended next actions

1. Đối chiếu thay đổi của human review protocol với snapshot/lịch sử sẵn có để xác định phiên bản đã dùng khi tạo packet. Nếu file được cập nhật hợp lệ, ghi changelog và quan hệ phiên bản; nếu manifest trỏ snapshot lịch sử, giữ nguyên snapshot đó và trỏ đúng vị trí.
2. Sau khi nguồn gốc thay đổi được giải quyết, tạo bản manifest/audit sửa đổi có provenance rõ; giữ audit cũ, không sửa nhãn hoặc chỉ thay hash để vượt gate.
3. Chạy lại provenance gate. Sau đó tiếp tục các nhánh bị ngắt bằng input đã khóa và băm hash; duy trì độc lập giữa hai codebook reviewers và các sample reviewers.
4. Chỉ phát cluster context sau freeze vòng 1; chỉ lấy evaluation sau khi sampling rule đã khóa và được adversary kiểm tra. Giữ human validation pending cho đến khi có bằng chứng người thật.

Các file tạo trong lượt này chỉ gồm bản sao protocol yêu cầu, sự kiện STOP và báo cáo này. Không sửa source, manifest hiện có, raw evidence, annotation hoặc kết quả baseline.
