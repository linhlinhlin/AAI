# Hợp đồng dữ liệu v1/v2

## Cập nhật 19/09/2026: ID chưa biết và dữ liệu C

Schema v1 giữ nguyên yêu cầu `student_id` là chuỗi không rỗng. Schema v2 dùng cùng các trường,
nhưng cho phép `student_id: null` khi nguồn không cung cấp ID người học đáng tin cậy.
Không dùng ID bài làm để giả lập người học. Pipeline chỉ nối nhóm theo ID khi ID có thật;
vẫn nối source giống hệt và xuất `identity.split_guarantee` cùng cảnh báo nếu có ID thiếu.
Split này chưa chứng minh tổng quát hóa sang người học mới.

C đã có extractor tree-sitter với thuộc tính `ast:c_*`. Đây là chỉ báo cú pháp, không phải
kiểm tra biên dịch hoặc ngữ nghĩa; không mở rộng macro. Parse error được tách riêng trong
cả chế độ outcomes và combined để ablation dùng cùng tập mẫu. Python vẫn dùng AST chuẩn.
Test weight bằng 1 bỏ hoàn toàn AST khỏi cả clustering và cây giải thích.

ITSP adapter xuất manifest schema v2, JSONL bài sai và `review.jsonl` riêng chứa log gốc,
cờ nghi định dạng và đường dẫn bài sửa. Không đưa sidecar hoặc bản sửa đúng vào feature.
Các chi tiết v1 bên dưới vẫn áp dụng, trừ ngoại lệ null ID được nêu rõ cho v2.

Đây là schema nội bộ của prototype, không phải mô tả dataset giảng viên. Xem ví dụ chạy được trong `data/demo/`.

Manifest bắt buộc: `schema_version=1`, `dataset_name`, `provenance`, `problem_id`, `language`, `suite_version`, `test_ids` (danh sách ID duy nhất, không rỗng). Các trường mô tả thêm trong manifest được giữ trong báo cáo. Nên ghi compiler/runtime, hash đề bài và test suite, chính sách so sánh output, commit nguồn, ngày lấy dữ liệu và license.

Mỗi dòng JSONL phải có đúng các trường:

| Trường | Ý nghĩa / yêu cầu |
|---|---|
| submission_id | ID lần nộp duy nhất trong file |
| student_id | ID đã ẩn danh, nhất quán giữa các lần nộp; không phải feature |
| problem_id | Khớp manifest |
| language | Khớp manifest; Python AST hỗ trợ `python`, `python3`, `py` |
| source_code | Source dạng chuỗi không rỗng; không chạy code này |
| suite_version | Khớp manifest; không trộn kết quả của suite khác nhau |
| outcomes | Map test ID → pass/fail/runtime_error/timeout/not_run |
| provenance | Chuỗi mô tả nguồn, không phải feature |

Test vắng được adapter chuyển thành `not_run`; test ngoài manifest bị từ chối. `fail` nghĩa là chương trình chạy xong nhưng output không đạt oracle, không phải lỗi compiler. Không suy diễn outcome từ điểm tổng. Nếu không có test-level outcomes, dừng nhánh hành vi, xin log hoặc xây test suite riêng với giảng viên. Không tự bịa ma trận fail để đủ đầu vào.

Compile failure của C/C++ chưa có trường verdict riêng trong contract v1: ánh xạ outcomes thành `not_run`, ghi nguyên nhân trong provenance; mẫu sẽ bị loại khỏi clustering. Muốn thống kê chi tiết compiler cần mở rộng schema có phiên bản, không đổi ý nghĩa `fail`. Python parse error được phát hiện tĩnh. Thứ tự routing hiện thực xem `features.py` và regression tests.

## OAV

`(submission_123, test:boundary_empty, fail)` là quan sát từ test runner/log; `(submission_123, ast:range, 1)` chỉ nói có lời gọi tên `range` trong AST. Không đồng nghĩa vòng lặp sai biên, và tên này có thể bị shadow. `ast:parse=unsupported/error` không được biến thành tất cả flag FALSE. Artifact OAV là map object → attributes → values; một số thuộc tính AST hằng được bỏ khỏi vector sau train-fit. Raw source trong input giúp truy vết; chưa có source-span trong extractor.

## Thay dataset

1. Khảo sát một mẫu nhỏ với giảng viên: ngôn ngữ, đề, test suite, trạng thái thực thi, lịch sử, ID ẩn danh, quyền sử dụng.
2. Viết một script chuyển CSV/LMS/ProgSnap2 vào JSONL và manifest trên. Giữ nhãn chuyên gia trong file riêng; adapter từ chối đưa nhãn vào record phân cụm.
3. Chạy validation, thống kê routing và đối chiếu thủ công ít nhất 10 bài/outcome. Với ID không có, chưa được tuyên bố đánh giá tách theo sinh viên; không giả lập mỗi submission là một người.
4. Chạy một cohort nhỏ. Giữ nguyên `domain/features/pipeline`. Nếu cần ngôn ngữ khác, thêm extractor AST tương ứng và unit tests; thay adapter nguồn không đòi viết lại thuật toán.
5. Sau khi chốt protocol mới mở rộng số bài. Lưu cùng source hash trong một split, kiểm tra thêm near-duplicate/template và lịch sử nộp. Chọn một lần nộp theo chính sách định trước hoặc cân trọng số người học để người nộp nhiều không áp đảo.

## Gợi ý public-data prototype (chưa tải/chạy trong bản này)

Với C: chọn một bài nhỏ trong [C-Pack-IPAs](https://github.com/pmorvalho/C-Pack-IPAs), khóa commit, giữ LICENSE/attribution, lấy code/tests/reference và ID sinh viên từ cấu trúc repository đã xác minh. Nếu chưa có logs, replay bằng sandbox chuyên dụng trước khi adapter nhập kết quả. Không chạy code không tin cậy trực tiếp bằng `exec` hoặc subprocess trên máy cá nhân.

Một runner tương lai cần container/VM dùng một lần, không mạng, không mount dữ liệu cá nhân, non-root, read-only root, giới hạn CPU/RAM/PID/output/thời gian, compiler được khóa và kiểm tra reference trên suite. Timeout không phải bằng chứng vòng lặp vô hạn; hạn mức quá thấp cũng gây timeout. Runner là adapter cung cấp evidence, không thuộc lõi clustering. Không cung cấp một wrapper timeout rồi gọi đó là sandbox.
