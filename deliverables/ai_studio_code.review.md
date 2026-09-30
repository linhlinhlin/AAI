# Rà soát phản hồi AI Studio

Nguồn: [ai_studio_code.json](ai_studio_code.json).
Đối chiếu [packet ITSP](De5_Annotation_20260928/itsp/evidence.json), code và log lịch sử;
không thực thi lại C, không dùng nhãn giảng viên. Đây cũng là rà soát do AI thực hiện,
không phải adjudication của con người hay gold label.

## Kết quả kiểm tra

**PASS cấu trúc:** đúng packet ID, đủ 5 cluster, không trùng ID, các evidence_refs tồn tại,
confidence nằm trong khoảng hợp lệ và decision nhất quán với evidence_supported.
[Bản intake](ai_studio_code.checked.json) giữ nguyên nhận xét gốc của AI với trạng thái
`ai_reviewed_pending_human_validation`. PASS này không chứng minh nội dung đúng.

**Cần đánh giá lại nội dung cả 5 cụm trước khi sử dụng kết luận ở mức toàn cụm.**
Một số nhận xét đúng cho nhóm con, nhưng AI bỏ qua phản ví dụ và suy rộng quá mức.
Không sửa file phản hồi gốc, không đổi packet hay tự gán gold.

## 2812 / cluster 0 — 8 bài

AI quy lỗi cho so sánh chính xác `float == 0` và logic phân loại dấu. Nhận xét này
không được dẫn chứng hỗ trợ như một cơ chế chung:

- `sample_003/004/005`: nhánh phân loại dấu phù hợp với input/log; khác biệt quan sát
  là **thừa dấu chấm cuối câu**, không phải thiếu dấu chấm. Test 4 của sample_003:
  expected `0.0000 is positive`, output `0.0000 is positive.`.
- `sample_001`: chỉ kiểm tra `a == -12`, rồi gọi mọi giá trị khác là zero. Test 3,
  input `1`, output `1.0000 is zero`. Đây là kiểm tra một giá trị cụ thể thay vì dấu.
- `sample_002`: `printf("%.4f is positive,%n")` không cung cấp đối số cho các conversion;
  code có lỗi gọi hàm, không thể diễn giải các output lịch sử thành hành vi xác định.
- `sample_006`: chỉ in số, không có thông báo phân loại.
- `sample_007`: in số hai lần, định dạng không đúng.
- `sample_008`: viết `scanf("%f,&a")`, đưa `&a` vào chuỗi thay vì truyền địa chỉ đối số;
  log ghi output rỗng. Không suy ra chắc chắn crash chỉ từ log này.

Đối với bài phân biệt số âm/zero/dương đọc trực tiếp, `a == 0` tự nó không là lỗi.
Test có `0.0000001` và `-0.0000001`, oracle vẫn phân biệt dương/âm; thay bằng một
ngưỡng epsilon tùy ý có thể làm mất chính sự phân biệt mà đề yêu cầu.

Ngoài ra, ví dụ trong statement có dấu chấm nhưng oracle log bài 2812 không có.
Phải ghi nhận sự không nhất quán statement/oracle, không diễn giải lỗi chấm format
thành bằng chứng học viên không hiểu số thực.

## 2825 / cluster 0 — 11 bài

Nhận xét presentation phù hợp với nhiều bài nhưng câu “tất cả đều chỉ sai format” sai:

- `sample_001/002/003/004/007/009`: thiếu dấu chấm cuối câu trong các log.
- `sample_006/010/011`: `circle` thay vì `Circle`.
- `sample_008`: in thêm dòng debug, ví dụ test 1 có `6.700747 demo` trước thông báo.
- **`sample_005`: scanf thiếu `&` cho các biến float; toàn bộ log output rỗng.**
  Đây là phản ví dụ trực tiếp với kết luận cụm chỉ sai presentation.

Có bằng chứng về khác biệt trình bày ở 10/11 bài theo đối chiếu code/log, nhưng
không được từ đó khẳng định mọi logic đều đúng trên mọi đầu vào hoặc cụm đồng nhất.
Con số này là rà soát hiện tại của AI, không thay thế số khớp của luật cục bộ trong packet.

## 2825 / cluster 1 — 7 bài

Nhận xét về nhánh gắn sai else được hỗ trợ cho **sample_003 và sample_004 (2/7 bài)**:
test 4/5 in cả `Point is inside the Circle.` và `Point is on the Circle.`.
`else` thuộc if thứ hai; không phải mọi chuỗi if độc lập đều sai.

Các bài còn lại có cơ chế khác:

- `sample_001`: thiếu trường hợp trên đường tròn.
- `sample_002`: dùng khoảng cách bình phương trừ `r`, thay vì `r*r`.
- `sample_005`: tính khoảng cách bình phương `c` rồi so sánh với `r`; biến căn bậc hai
  `d` không được sử dụng trong điều kiện.
- `sample_006`: nhánh on thiếu dấu chấm cuối câu; test inside/outside pass.
- `sample_007`: tính `k` nhưng kiểm tra `r` thay vì `k`.

Không đủ căn cứ gán một cơ chế if/else chung cho cả 7 bài, càng không đủ để kết luận
“nhầm lẫn về tính loại trừ” như niềm tin thật của học viên.

## 2825 / cluster 2 — 4 bài

Đây là bài vị trí điểm so với đường tròn, không phải bài tam giác. Nhãn AI đã trộn
ngữ cảnh bài tập và bỏ qua lỗi nhập liệu:

- `sample_001`: nhánh outside in `Cicle` thay vì `Circle`; test 1/2/7 fail,
  các test inside/on pass. Không có bằng chứng lỗi nhánh cho bài này từ các log đã cho.
- `sample_002`: nhánh else của trường hợp outside in thông báo on; test 1/2/7 fail.
- `sample_003/004`: scanf nhận thứ tự `x y x1 y1 r`, trong khi đề là `x y r x1 y1`.
  Cần chỉ ra hoán đổi vai trò dữ liệu đầu vào thay vì gọi chung là sai if/else.

Do có nhiều cơ chế, không nên giữ decision supported cho giả thuyết một lỗi logic chung.

## 2833 / cluster 1 — 8 bài

Cụm này có ít nhất bốn dạng lỗi quan sát khác nhau:

- `sample_001/002/008`: số đếm khớp oracle trong cả 6 test, nhưng in `triangle`
  thay vì `triangles`. **3/8 bài này không hỗ trợ nhận xét “thuật toán đếm sai”.**
- `sample_003/004/005`: duyệt độc lập cả ba cạnh từ 1 đến N, đếm các hoán vị riêng
  thay vì mỗi bộ cạnh không thứ tự một lần. Test N=4 cho 34 thay vì 13.
  Bất đẳng thức dùng `&&` trong các bài này không phải điểm sai được bằng chứng chỉ ra.
- `sample_006`: dùng `||` giữa các bất đẳng thức, đồng thời duyệt bộ ba có thứ tự;
  test N=4 cho 64, N=3 cho 27.
- `sample_007`: dấu `;` ngay sau các vòng for làm thân vòng lặp rỗng;
  log mọi test đều in số đếm 1.

Câu “tất cả trượt ngoại trừ test 2” cũng không đúng: sample_001/002/008 trượt cả
test 2 vì chuỗi output. Confidence 0.95 là điểm AI tự khai báo, không phải độ chính xác đo được.

## Hướng gửi lại AI

Gửi tài liệu này cùng packet ITSP gốc và response.schema.json. Có thể dùng chỉ dẫn:

> Rà soát lại 5 nhận xét trước đó. Lập bảng từng sample_id với cơ chế quan sát,
> code cụ thể, test input/expected/output, và phản ví dụ với nhãn chung. Kiểm tra
> thứ tự/tham số scanf, đối số printf, từng ký tự output và phạm vi gắn else.
> Không coi float == 0 hay nhiều if độc lập là lỗi mặc định. Đối chiếu statement
> với oracle và ghi rõ khi chúng mâu thuẫn. Với bài đếm tam giác, tách số đếm khỏi
> chuỗi trình bày; phân biệt đếm hoán vị, toán tử OR, thân for rỗng và lỗi chính tả.
> Sau đó trả JSON đúng schema, nêu số bài hỗ trợ/tổng bài và các sample phản ví dụ
> trong reasoning. Nếu không có một cơ chế chung được hỗ trợ, trả uncertain;
> nếu bác bỏ nhãn cụ thể, ghi đúng nhãn bị bác bỏ với rejected. Không gán gold,
> không suy ra niềm tin học viên chỉ từ code. Không sao chép nhận định trong tài liệu
> rà soát này như gold; hãy tự đối chiếu lại code và log được dẫn.

File trả lại nên có tên mới để giữ provenance của phản hồi đầu tiên. Sau khi nhận,
chạy intake lại rồi rà soát nội dung; không đổi trạng thái human_validated.
