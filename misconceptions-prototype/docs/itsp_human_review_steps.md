# Human còn cần làm gì sau AI review

Tài liệu thao tác cho người điều phối, theo [protocol](itsp_human_review_protocol.md). AI đã giúp chỉ ra dòng code, test và điểm cần phân giải; người thật vẫn phải tự chấm đủ 17 hồ sơ. AI không ký duyệt codebook, không điền adjudication và không thay thế reviewer thứ hai.

## 1. Chọn người và bảo vệ vòng độc lập

- Nếu muốn raw agreement/Cohen’s kappa, mời ít nhất hai người có khả năng đọc C và đánh giá misconception, chấm độc lập cùng 17 mẫu. Một người vẫn có thể review nhưng không đủ inter-rater agreement.
- Dùng ID ổn định, ví dụ reviewer_01/reviewer_02 sau khi đã phân công người thật. Giữ danh sách danh tính ở nơi riêng; ID không có tiền tố ai: không tự chứng minh là người thật.
- Chỉ gửi `results/itsp/human_review_packet.zip`. Không gửi expert_annotations.json, AI review mới, báo cáo ưu tiên, metrics, assignments hoặc packet vòng 2.
- Nếu bạn đã đọc kết quả AI trong task này, nên làm người điều phối. Nếu bạn tự chấm, khai `independent_blind_review=false`; không tính lượt đó như một lượt mù. Có thể chọn hai reviewer chưa xem nhãn để có cặp độc lập.
- Không yêu cầu reviewer “xác nhận AI đúng”. Để họ quyết định và ghi evidence của chính mình. Bảng ưu tiên có nhãn chỉ dùng nội bộ điều phối và sau khi đã khóa vòng 1.

## 2. Chốt codebook trước khi chấm

Giải nén ZIP vào thư mục mới. Mời chuyên gia đọc CODEBOOK.md, thống nhất Yes/No/Unclear, ranh giới các type và `single_primary`. Không dùng nhãn hay ví dụ có đáp án từ chính 17 mẫu để hiệu chỉnh người chấm.

Bản hiện tại là human-review-draft-v1, chưa được phê duyệt. Sau khi người thật xác nhận, cập nhật bản codebook phân phối và phần `codebook` trong bản sao annotations.json: approved_by, version, label_policy=single_primary và các mã đã duyệt. Ghi người duyệt, ngày và SHA-256 codebook trong biên bản. Không tự ký thay họ, không sửa file expert_annotations.json gốc. Mỗi reviewer nhận cùng phiên bản đã chốt và một file phiếu riêng.

## 3. Reviewer thao tác trên mỗi hồ sơ

1. Mở Main.c để đọc đề. File này có cả lời giải tham chiếu; điều kiện review có tham chiếu đã được công bố.
2. Đọc buggy.c và toàn bộ logged_tests.json. Ghi đầu vào, expected, actual và dòng gây hành vi. Log là lịch sử dataset, không phải lần chạy mới. Theo packet, không chạy code C để điền phiếu.
3. Truy vết bằng tay một test thất bại, đối chiếu test pass nếu giúp loại trừ giả thuyết. Tách “code sai ở đâu” khỏi “evidence nào cho thấy hiểu sai khái niệm”.
4. Ghi nhận định ban đầu rồi đọc paired_correct.c. Ghi rõ bản sửa có đổi nhận định không. Bản sửa thành công không chứng minh nhận thức của người học.
5. Chọn Yes khi có evidence về quy tắc khái niệm sai; No khi evidence ủng hộ lỗi thao tác/format/chính tả/chưa hoàn thiện hoặc đề/oracle; Unclear khi đã đọc nhưng không phân giải được. Không biến thiếu dữ liệu thành No.
6. Nếu Yes, chọn một type đã chốt; nếu không chọn được nhãn chính, có thể để type null và giải thích. No/Unclear phải type null.
7. Điền confidence 1–5 về quyết định, evidence gồm dòng code + test + cơ chế + giải thích cạnh tranh/evidence thiếu. Unclear có thể confidence cao vì chắc chắn rằng hiện chưa đủ evidence.
8. Điền reviewer_id thật, status=complete khi đủ trường. Chưa đọc giữ pending/null. Chỉ tự xác nhận independent_blind_review=true khi thực sự chưa xem nhãn AI/người khác/cluster trước khi hoàn tất.
9. Giữ same_cause_as_cluster A/B/C null và adjudication pending/null. Không đổi submission_id, problem_id, assignments_sha256. Lặp lại đủ 17 mẫu và kiểm tra không thiếu/trùng ID.

Nếu không có student ID hoặc không liên hệ được người học, ghi rõ thiếu bằng chứng và giữ Unclear khi cần; không tạo lời giải thích của người học. Confidence không phải trọng số tính agreement.

## 4. Nhận file, validate và khóa vòng 1

Lưu bản nhận nguyên trạng vào đường dẫn mới riêng theo reviewer/vòng; không ghi đè lần nhận trước. Ghi giờ nhận, người gửi, codebook version/hash, file hash và xác nhận độc lập của chính reviewer.

Ví dụ sau khi thực sự nhận file (chạy PowerShell từ thư mục dự án):

```powershell
Set-Location E:/AAI/misconceptions-prototype
Get-FileHash -Algorithm SHA256 received/reviewer_01/round1.json
.venv/Scripts/python.exe scripts/score_itsp_experts.py --annotations received/reviewer_01/round1.json --validate-only
.venv/Scripts/python.exe scripts/score_itsp_experts.py --annotations received/reviewer_02/round1.json --validate-only
```

`--validate-only` không tính hoặc ghi metrics. Ngoài schema, người điều phối phải kiểm tra: người thật, cùng reviewer ID trong file, coverage đủ 17 hoặc khai rõ thiếu, cùng codebook, evidence tự viết, không có AI record, trạng thái và điều kiện mù đúng thực tế. Scorer không xác thực danh tính hay chất lượng lý giải. File có lỗi phải trả reviewer sửa, lưu phiên bản mới, không tự điền nhãn cho họ.

Tạo bản làm việc human-only `data/itsp/human_annotations.json` từ các phiếu thật. Merge bằng `(submission_id, reviewer_id)`, giữ nguyên quyết định/type/confidence/evidence của từng người, không lấy nhãn AI làm mặc định. Không gộp hai version của một người thành hai reviewer. Nếu trùng khóa, đối chiếu nguồn/version và yêu cầu giải quyết. Lưu bảng provenance từng rating → file/hash nhận.

Validate bản merge và lưu snapshot bất biến riêng, ví dụ `received/snapshots/human_round1_locked.json`; hash và lưu an toàn trước khi phát context. Không thay null bằng nhãn để hoàn tất coverage. Chỉ snapshot working copy mới được bổ sung ở vòng sau.

## 5. Sau khóa vòng 1: ngữ cảnh cụm và ưu tiên adjudication

Phát riêng `results/itsp/human_review_round2_packet.zip`: có context A/B/C và evidence 59 thành viên. Reviewer bổ sung same-cause cho từng arm, giữ nguyên decision/type/confidence/evidence vòng độc lập trong snapshot gốc; lưu nhận định vòng cụm ở phiên bản vòng 2 và ghi rõ phần evidence bổ sung.

- Yes: cùng nguyên nhân thực chất với tất cả thành viên đã đánh giá trong phạm vi ghi rõ.
- Partially: chỉ một phần cùng nguyên nhân hoặc cụm trộn cơ chế.
- No: không có cơ chế chung phù hợp.
- null: chưa đủ context hoặc chưa đánh giá; không ép thành No.

Đây là đánh giá sau khi thấy cluster; báo riêng với misconception vòng 1. Không phát AI như đáp án vòng 2. Sau khi khóa các lượt human, người điều phối có thể dùng báo cáo ưu tiên để yêu cầu kiểm tra lại evidence trong adjudication; ghi rõ việc tiếp xúc AI ở giai đoạn này, không sửa hồi tố các lượt mù.

Trong [báo cáo điều phối AI](itsp_ai_independent_review.md), P1 có 3 mẫu bất đồng, P2 có 7 mẫu còn vấn đề cần chú ý, P3 có 7 mẫu vẫn phải chấm. Đây chỉ là cách phân bổ thời gian thảo luận, không phải bộ mẫu mới, không phải bỏ phiếu AI. Ưu tiên bất đồng giữa chính human và chất lượng evidence khi có dữ liệu thật, kể cả mẫu AI cùng nhãn.

Người thật chịu trách nhiệm mới điền adjudication: reviewer_id, decision, type, confidence, evidence giải thích quyết định và bất đồng. Giữ tất cả lượt ban đầu. Chưa giải quyết thì pending; đã xét nhưng không đủ evidence thì complete/Unclear/type null. Yes/type null hợp lệ nếu nhiều cơ chế không chọn được chính. Adjudicator không phải một independent rater bổ sung.

## 6. Chỉ tính metrics khi có dữ liệu human phù hợp

Sau validate, kiểm tra provenance và đối chiếu snapshot vòng 1/vòng 2:

```powershell
.venv/Scripts/python.exe scripts/score_itsp_experts.py --annotations data/itsp/human_annotations.json --validate-only
.venv/Scripts/python.exe scripts/score_itsp_experts.py --annotations data/itsp/human_annotations.json --output results/itsp/human_validation_metrics.json
```

Chỉ chạy lệnh tính metrics với bản human-only đã kiểm tra, không truyền file AI độc lập và không trộn hai AI thành hai experts. Đọc purity theo adjudicated Yes có type đã duyệt; raw agreement/kappa theo cặp người thật chấm mù cùng mẫu trước adjudication. Báo mẫu số, coverage và codebook version. Một reviewer, thiếu cặp đủ điều kiện hoặc chưa chốt codebook thì các chỉ số tương ứng chưa tính được; giữ null theo điều kiện scorer. Kappa cũng null khi p_e=1.

Cập nhật Results/Discussion và README sau khi có human thực tế, giữ rõ 17 mẫu được chọn có chủ đích, không đại diện 59 submissions và không suy rộng sang người học mới. Không đổi clustering/A/B/C để cải thiện chỉ số.

## Điều kiện hoàn tất phần human

Có codebook được người thật duyệt; phiếu và provenance của người thật; snapshot khóa lượt độc lập; vòng cụm riêng nếu cần same-cause; adjudication hoặc danh sách còn pending rõ ràng; metric đủ điều kiện với coverage trung thực. Hiện chưa có các human annotations đó: 0/17 human complete, 0/17 adjudicated, expert purity/raw agreement/kappa vẫn null. AI review chỉ giảm công rà evidence và tìm điểm tranh luận, không thay thế việc quyết định của người thật.
