# Benchmark cơ chế lỗi tự xây dựng (đề 5)

Thầy không cung cấp dữ liệu, nên nhóm tự chuẩn bị dữ liệu và nhãn đánh giá từ
nguồn công khai C-Pack-IPAs. Tài liệu này mô tả cách dựng dữ liệu, ý nghĩa của nhãn
và các giới hạn. Protocol đăng ký trước:
[`research/protocol-mechanism-v1.json`](../research/protocol-mechanism-v1.json).

## 1. Ba lớp dữ liệu

| Lớp | Cách tạo | Vai trò |
|---|---|---|
| Replay có cách ly | Biên dịch và chạy lại 8.607 bài C-Pack với cờ của khóa học, trong container không mạng, uid riêng, có giới hạn tài nguyên | Có đủ outcome và stdout cho mọi test, thay cho các ô `not_run`. Audit oracle đối chiếu verdict lịch sử |
| Nhãn từ bản sửa của chính sinh viên (`real`) | Ghép bài sai với lần nộp đạt kế tiếp của cùng sinh viên (cùng bài, cùng năm). Delta-debugging theo hunk, mỗi phép thử đều chạy thật, tìm tập thay đổi nhỏ nhất vẫn làm bài đạt | Nhãn cơ chế ở mức chương trình trên lỗi thật (nhãn bạc, *silver*) |
| Tiêm lỗi có kiểm soát (`injected`) | Một thay đổi cú pháp duy nhất trên bài đạt, không cảnh báo; chỉ giữ mutant biên dịch sạch và trượt ít nhất một test | Nhãn biết trước do cách tạo; kiểm tra có kiểm soát |

Bài nộp sau, bản sửa, nhãn và tên toán tử **không bao giờ** đi vào features phân cụm.
Mọi item thừa kế partition của bài gốc trong split khóa theo sinh viên/nguồn.

## 2. Taxonomy cơ chế (mức chương trình)

| Mã | Tên | Bản sửa tối thiểu thay đổi… | Giả thuyết quan niệm sai thường gặp (cần kiểm chứng thêm) |
|---|---|---|---|
| LOOP_BOUNDARY | Biên/điều khiển vòng lặp | điều kiện, khởi tạo hoặc bước nhảy của `for`/`while`/`do` | lệch một (`<` và `<=`), chỉ số bắt đầu 0/1 |
| BRANCH_CONDITION | Điều kiện rẽ nhánh | điều kiện `if`/`switch`/toán tử `?:` | biên so sánh, `&&` và `\|\|` |
| INITIALIZATION | Khởi tạo | giá trị khởi tạo khi khai báo, hoặc gán hằng ngoài vòng lặp | khởi tạo biến tích lũy, giá trị lớn nhất |
| COMPUTATION | Biểu thức tính toán | toán tử hoặc toán hạng trong phép gán, `return`, đối số in | công thức, độ ưu tiên toán tử |
| NUMERIC_TYPE | Kiểu số, chia nguyên | kiểu khai báo, ép kiểu, hằng thực, hàm toán học | chia nguyên, nhầm `int` với `float` |
| OUTPUT_FORMAT | Đặc tả định dạng in | đặc tả `%` trong chuỗi `printf` | độ chính xác `%.2f`, độ rộng `%02d` |
| OUTPUT_TEXT | Văn bản in ra | phần chữ của chuỗi in, hoặc lệnh chỉ in hằng | đọc sai đặc tả output, xuống dòng cuối |
| INPUT | Đọc dữ liệu | lời gọi `scanf`/`getchar`/… | định dạng đọc, EOF |
| STATEMENT_PLACEMENT | Vị trí câu lệnh/khối | câu lệnh hoặc dấu ngoặc bị di chuyển | đặt lại biến trong vòng lặp, in trong vòng lặp |
| MISSING_STATEMENT | Thiếu bước | thêm nguyên câu lệnh | thiếu cập nhật, thiếu nhánh |
| EXTRA_STATEMENT | Thừa bước | xóa nguyên câu lệnh | cập nhật hai lần, in thừa |
| CONTROL_FLOW | Luồng điều khiển | `break`/`continue`/`return` | thoát vòng lặp sớm |

Nhãn chính của một bài chỉ được dùng khi bản sửa tối thiểu thuộc **đúng một** loại
(không phải `OTHER` hay `MULTI`). Cột cuối là giả thuyết để giảng viên kiểm tra;
một thay đổi trong code không chứng minh sinh viên tin điều gì. Nhóm loại dựa trên
các nghiên cứu về lỗi logic của người mới học, như Ettles, Luxton-Reilly & Denny
(ACE 2018) và Qian & Lehman (TOCE 2017), cùng với cấu trúc cú pháp của C.

## 3. Biểu diễn so sánh

| Mã | Nội dung | Ghi chú |
|---|---|---|
| `outcomes` | OAV kết quả từng test: đúng cách đề bài mô tả | baseline chính |
| `exact_signature` | gom theo vector kết quả test giống hệt | baseline rẻ nhất |
| `structural`, `outcomes_stdout`, `combined_stdout` | biểu diễn sẵn có của repo | baseline mạnh nhất trước đây là `combined_stdout` |
| `deviation` | test + mô tả *cách* output lệch (lệch 1, cụt, sai độ chính xác, thiếu xuống dòng…) | đề xuất, không phụ thuộc bài |
| `evidence` | `deviation` + manh mối cấu trúc mã | đề xuất |
| `embedding` | Qwen3-Embedding-0.6B trên mã nguồn thô, chạy cục bộ | baseline neural đóng băng |

Luật IF–THEN: ILA (Tolun & Abu-Soud, 1998) và ILA-2 có hệ số phạt nhiễu
(Tolun et al., 1999) học từ nhãn của partition train, so với CART và lớp đa số.
Mẫu không khớp luật nào được trả về `abstain`, không bị gán mặc định.

## 4. Tái lập

Từ `misconceptions-prototype`, sau khi đã có `.cache/cpack-v3`:

```text
docker build -t aai-c-replay:1 sandbox-replay
python scripts/replay_cpack.py --data ../.cache/cpack-v3 --split-lock ../research/splits/cpack-v3.json --output ../.cache/cpack-replay-v1
python scripts/build_mechanism_benchmark.py --data ../.cache/cpack-v3 --replay ../.cache/cpack-replay-v1 --split-lock ../research/splits/cpack-v3.json --output ../.cache/mechanism-bench-v1
python scripts/run_mechanism_eval.py --partition validation ...
python scripts/run_mechanism_eval.py --partition test --penalty <giá trị chốt từ validation> ...
```

Runner replay tách khỏi runner của app học viên. Test mặc định không thực thi
corpus. Kiểm tra Docker của runner nghiên cứu chỉ chạy khi `AAI_RUN_DOCKER_TESTS=1`,
và chỉ trên chương trình do nhóm tự viết.

## 5. Giới hạn cần nói rõ

- Thứ tự `sub_NNN` được coi là thứ tự nộp trong cùng sinh viên, bài và năm.
- Delta-debugging ở mức dòng. Nhãn phụ thuộc bộ phân loại theo luật đã cố định trước.
  Mẫu audit do AI thực hiện không thay cho người chấm độc lập.
- Mutant tiêm lỗi sạch hơn lỗi thật và có phân bố do nhóm chọn. Không dùng tỷ lệ loại
  của bộ này để suy ra tỷ lệ lỗi trong lớp học.
- Chỉ một nguồn dữ liệu (C-Pack-IPAs, một khóa học). Kết luận chưa chuyển sang
  trường khác nếu chưa có dữ liệu mới.
