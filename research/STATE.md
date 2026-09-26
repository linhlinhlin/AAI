# Trạng thái nghiên cứu — 26/09/2026

**Đã triển khai harness và nền thực nghiệm offline cho đề 5.** Mục tiêu bài báo
vẫn là khám phá cơ chế lỗi có bằng chứng, với quan niệm sai là giả thuyết cần
xác nhận. Kết quả hiện tại chưa chứng minh SOTA hay niềm tin thật của người học.

## Phần đã chạy được

| Thành phần | Bằng chứng |
|---|---|
| Hướng dẫn làm việc | [AGENTS](../AGENTS.md), [skill thực nghiệm](../.agents/skills/aai-experiment/SKILL.md), CLAUDE.md cùng nguồn chỉ dẫn |
| Kiểm tra xác định | `scripts/harness.py doctor/check/smoke`; CI gọi cùng entrypoint |
| Tiêu chí môn học | [Hợp đồng đề 5](../docs/topic5-contract.md): OAV → phân cụm → IF–THEN → phản hồi giảng dạy |
| Dữ liệu tự tìm | ITSP có sẵn; đã nhập toàn bộ canonical originals C-Pack-IPAs-26 |
| Chống leakage | Lock toàn corpus, nối sinh viên xuyên năm/bài và exact nonempty source trước khi chia cohort |
| Baseline mới | `outcomes_stdout`, `combined_stdout`; đối chiếu exact, outcomes và combined cũ |
| Tái lập | Hash input, evidence, split, source; seed/k; Python/packages; lưu code snapshot kể cả mã chưa commit |
| Kiểm chứng phần mềm | **175 tests + 3 subtests pass**, Ruff pass; **27/27 smoke configurations pass**; skill validator pass |

[Log kiểm tra](verification-20260926.txt), [smoke](smoke-20260926.txt). Các kiểm tra chạy local trên Windows,
Python 3.12.14. Workflow GitHub Actions cũng chạy trên Linux; xem trạng thái
từng commit tại [CI của nhánh bàn giao](https://github.com/meiiie/AAI/actions?query=branch%3Aresearch%2Ftopic5-harness).
Lần CI đầu phát hiện Git đổi line ending của assignment JSON cũ làm sai hash;
`.gitattributes` đã giữ CRLF của file đó theo checksum gốc, không đổi hồ sơ
hay nới lỏng kiểm tra. Chi tiết cài đặt và cách tái lập: [harness](../docs/harness.md).

## C-Pack-IPAs: dữ liệu thực đã nhập

Nguồn [C-Pack-IPAs](https://github.com/pmorvalho/C-Pack-IPAs), release
`C-Pack-IPAs-26`, commit `76901e1223b250a093a02d5e29113ad735c3d2b9`.
Chỉ dùng `all_submissions`; không cộng các bản lặp ở correct/incorrect hoặc
bản sửa `_fixed`. 8.607 submissions, 246 ID sinh viên ẩn danh, 25 bài tập,
106 cặp input/oracle. README nguồn xác nhận ID nhất quán xuyên bài và xuyên năm.

| Routing sau nhập | Số bài |
|---|---:|
| Có failure và đủ điều kiện baseline | 2.392 |
| Không có failure quan sát | 3.600 |
| Thiếu bằng chứng/không chạy được test đầy đủ | 2.136 |
| Lỗi thực thi hoặc vượt hạn mức | 267 |
| Parse error | 212 |
| Tổng | 8.607 |

Không còn metadata không đọc được. 193 output test thuộc 61 submissions không
phải UTF-8 được audit và giữ hash byte gốc; không thay byte lỗi bằng ký tự giả.
Không có failure bị thiếu file stdout trong snapshot này. Accepted không lưu
stdout vẫn giữ verdict pass, không tự chép expected thành actual. Marker `@@`
được xử lý cho timeout, output limit, signal và nonzero exit; Internal Error
của hệ thống chấm là chưa quan sát được kết quả.

Source rỗng được giữ để audit ID; không dùng sự vắng mặt code làm bằng chứng
duplicate giữa hai sinh viên. Các lần nộp không đủ điều kiện vẫn tham gia nối
nhóm sinh viên/source có nội dung. Chưa có audit near-duplicate đổi tên.

[Audit máy đọc được](data-audit/cpack-20260926.json).
Dữ liệu chuẩn hóa local: `../.cache/cpack-v3/`; chỉ import hoàn tất, còn đúng
hash trong `dataset_complete.json`, mới được dùng để khóa split.

| Partition | Submissions | Sinh viên | Thành phần liên thông |
|---|---:|---:|---:|
| Train | 6.088 | 167 | 154 |
| Validation | 1.569 | 51 | 51 |
| Test | 950 | 28 | 28 |

[Split lock](splits/cpack-v3.json), seed 42. Đây là split độc lập theo sinh
viên trên các bài đã thấy, chưa phải problem-family-disjoint. Test chỉ được
kiểm tra schema/provenance/kích thước log để nhập dữ liệu; chưa được fit, gán cụm hoặc chấm
chỉ số phương pháp. Không coi raw count submissions là số quan sát thống kê
độc lập vì có nhiều lần nộp của cùng người.

## Kết quả thực nghiệm hiện có

ITSP: **81/81 configurations có kết quả**, gồm 3 bài development × 9 biến thể
thuật toán/biểu diễn × 3 seeds. [Báo cáo](runs/itsp-stdout-final-20260926/summary.md),
[manifest và snapshot mã](runs/itsp-stdout-final-20260926/run_manifest.json).
ITSP thiếu ID sinh viên và đã được xem khi thiết kế, nên không dùng làm test
độc lập hay bằng chứng tổng quát hóa sang sinh viên mới.

Trên 48 bài train+validation của ba cohort ITSP, 387 cặp trong cùng bài:
OAV combined có 67 cặp trùng hoàn toàn; thêm stdout còn 42 cặp. Xem
[collision audit với hash đầu vào](runs/itsp-stdout-final-20260926/collision_audit.json).
Đây là số va chạm biểu diễn, không phải số chẩn đoán sai. Cặp
`271173_buggy` / `271188_buggy` có regression test chứng minh stdout phân biệt
được lỗi chuỗi “Cicle” với output chọn thông báo “on the Circle”. Chưa được suy
ra rằng mọi cặp tách thêm đều có cơ chế lỗi khác nhau.

Stdout cũng không làm fidelity cây tăng đồng đều: ví dụ K-means seed 91 trên
2825, combined có fidelity validation 1.0, combined_stdout là 0.5. Hai giá trị
dùng mục tiêu cụm khác nhau và tập validation nhỏ; chúng không xếp hạng chất
lượng chẩn đoán. Đây là lý do cần gold cơ chế và đánh giá rule coverage/precision
thay vì chọn biểu diễn theo một chỉ số nội tại.

C-Pack-IPAs: **675 lượt hoàn tất**, 25 bài × 9 biến thể × 3 seeds trên cùng
split lock. **624 ok, 51 abstained**: 42 lượt không đủ mẫu/biểu diễn khác nhau
cho k=3; 9 lượt có feature train giống hệt. Không ép tạo cụm khi bằng chứng
không đủ. [Báo cáo đầy đủ](runs/cpack-summary-20260926.md),
[audit toàn vẹn](runs/cpack-integrity-20260926.json),
[gói dữ liệu + kết quả + mã](runs/cpack-baselines-20260926.zip),
[cách tái lập](runs/cpack-reproduce-20260926.md).

675 lượt C-Pack-IPAs và 81 lượt ITSP cuối đều qua audit input/code hashes,
configuration inventory, split membership, medoid và rule support. Một bản
sao cố ý sửa checksum input cũng đã bị từ chối. Các lượt thăm dò trước bản
cuối được giữ riêng; chúng không phải bảng kết quả hiện tại.

Một số log stdout vượt 327.000 ký tự. Extractor cuối giữ nguyên bằng chứng,
nhưng với expected/actual dài hơn 4.096 ký tự sẽ ghi band
`not_computed_large_output` thay vì chạy similarity có chi phí bậc hai. Đây là
trạng thái chưa tính similarity, không phải kết luận lỗi. Tổng thời gian trong
lõi `run_experiment` của 675 lượt là khoảng 274 giây trên môi trường local;
con số này không gồm nhập dữ liệu, tạo báo cáo giảng dạy, ghi file và audit.

## Ranh giới giữa baseline và đóng góp bài báo

Phần mềm hiện tại thực hiện đầy đủ chuỗi kỹ thuật yêu cầu của đề 5. Clustering
là không giám sát; cây IF–THEN học cách dự đoán ID cụm. ILA không bị gọi nhầm
là phân cụm. Các luật cơ chế viết tay và phản hồi giảng dạy có trạng thái ứng
viên, kèm nguồn/test khi khớp; không phải nhãn đánh giá độc lập.

Hồ sơ ITSP vẫn có **0 annotation chuyên gia thật hoàn tất**. Không dùng AI
reviews làm gold. Baseline AST hiện là presence indicators, chưa phải biểu
diễn binding/def-use đầy đủ. Chưa thực hiện replay C có sandbox, kiểm chứng
candidate edits, adaptive probes, huấn luyện encoder, hoặc đánh giá locked test.

[Protocol](protocol.json) mô tả thiết kế toàn bộ hướng bài báo, gồm cả phần
chưa triển khai; trường `proposal_not_executed` áp dụng cho thí nghiệm đầy đủ
đó. STATE này ghi riêng phần baseline đã thực thi. [Khảo sát](literature/bao_cao_nghien_cuu.md)
và [sổ nguồn](literature/nguon_nghien_cuu.csv) giữ cutoff 26/09/2026.

Quyết định nghiên cứu tiếp theo: kiểm tra liệu cấu trúc quan hệ và can thiệp
được xác minh có phân biệt cơ chế tốt hơn baseline stdout ở cùng chi phí và
coverage. Cần thiết lập runner Linux có sandbox và oracle audit, rồi xây gold
cơ chế bằng review độc lập trước khi chốt so sánh chính. Encoder/LLM trên GPU
thuê là một phương tiện ở giai đoạn đó; tăng kích thước model chưa thay thế
được bằng chứng còn thiếu. Không cần hệ thống sinh viên đang vận hành để làm
benchmark offline; tuyên bố về hiệu quả học tập cần dữ liệu nghiên cứu khác.

Checkout làm việc nằm ở `AAI/`, branch `research/topic5-harness`, dựa trên
`3c67734c25236b7fdcd9d84b8d4c2fa589add36e`. Đã đẩy lên
[fork meiiie/AAI](https://github.com/meiiie/AAI/tree/research/topic5-harness)
và mở [draft PR #1 về repo nhóm](https://github.com/linhlinhlin/AAI/pull/1),
chưa merge vào `main`. Tài khoản bàn giao chỉ có quyền đọc repo nhóm. Bản bàn
giao giữ nguyên snapshot mã và các kết quả đã ghi; CI có trạng thái theo commit.
