# Rà soát phản hồi cập nhật — 29/09/2026

PASS cấu trúc: đủ 5 cụm ITSP, packet ID và evidence_refs hợp lệ. Chưa đạt về nội dung.
Bản response.original.json bảo toàn đúng bytes file cập nhật. response.checked.json
chỉ xác nhận cấu trúc; không có gold label hay xác thực giảng viên. Báo cáo này cũng
là rà soát bởi AI, không phải adjudication của con người. Không chạy lại code C.

## Các điểm đã cải thiện

Đã nhận ra các cụm trộn nhiều cơ chế; nêu phản ví dụ scanf ở 2825/c0, phạm vi 2/7
bài cho lỗi nhánh ở 2825/c1, lỗi thứ tự input ở 2825/c2 và bốn nhóm lỗi ở 2833/c1.
Không còn quy toàn bộ cụm đếm tam giác thành một lỗi thuật toán duy nhất.

## Các điểm phải sửa

### 2812/c0

- `Cicle` không xuất hiện trong bất kỳ code thành viên nào của cụm này. Đây là lỗi
  thuộc 2825/c2/sample_001. Nhận xét đã bị lẫn evidence giữa các cụm.
- sample_003/004/005 THỪA dấu chấm so với oracle, không phải thiếu dấu chấm.
  Ví dụ sample_003/test 1: expected `-12.0000 is negative`, output
  `-12.0000 is negative.`. Statement có dấu chấm: cần giữ cảnh báo lệch statement/oracle.
- alternative_explanations vẫn khẳng định float == 0 là lỗi kỹ thuật. Với nhiệm vụ
  phân biệt dấu của số được nhập trực tiếp, không có căn cứ cho khẳng định này.
  Test 4/5 dùng ±0.0000001 và oracle vẫn phân biệt dương/âm. Không tự thay bằng epsilon.
- Không có một cơ chế misconception chung đã được hỗ trợ; nên để uncertain/false
  ở cấp cụm, còn các lỗi từng bài phải mô tả riêng với số bài hỗ trợ và phản ví dụ.

### 2825/c0

- rejected hợp lý nếu giả thuyết đang bác bỏ là “TOÀN BỘ cụm chỉ sai presentation”.
  Cần ghi rõ phạm vi này trong misconception_label; không bác bỏ việc 10/11 bài có
  khác biệt trình bày được code/log hỗ trợ.
- Bổ sung sample_008 in thêm dòng debug, không chỉ dấu chấm/hoa thường.
- sample_005 thiếu địa chỉ đối số scanf là lỗi kiểu/đối số, có hành vi không xác định,
  không nên gọi là lỗi cú pháp. Log rỗng là quan sát, không chứng minh một hậu quả
  runtime tất định của lỗi này. Trong C, con trỏ cũng được truyền theo giá trị.

### 2825/c1

- 2/7 bài khớp cơ chế là đúng, nhưng decision=supported cho nhãn cơ chế toàn cụm
  không phù hợp chính ghi chú “chỉ áp dụng cho 2 bài”. Theo prompt của packet, dùng
  uncertain/false cho cơ chế chung khi cụm trộn nhiều cơ chế.
- Nêu chính xác else gắn với if thứ hai; không quy mọi chuỗi if độc lập là sai.
  sample_003/004 test 4/5 in đồng thời inside và on.
- Bổ sung refs test nói trên để người đọc kiểm tra hành vi, không chỉ refs raw_code.

### 2825/c2

- sample_001 có nhánh phân loại phù hợp với các test đã cho, lỗi quan sát là chuỗi
  `Cicle`. Không gộp bài này với sample_002 thành “lỗi logic nhánh”.
- sample_002 chọn nhánh outside nhưng in nhầm thông báo on.
- sample_003/004 nhận input theo x y x1 y1 r thay vì x y r x1 y1.
- Phân bố quan sát: 1/4 chính tả, 1/4 thông báo sai tại nhánh outside, 2/4 sai thứ tự
  nhận input. Không có một cơ chế chung: dùng uncertain/false cho mục tiêu này.

### 2833/c1

- Phân nhóm hiện tại cơ bản khớp code/log: 3/8 chỉ khác triangle/triangles trong
  các test đã cho, 3/8 đếm bộ cạnh có thứ tự, 1/8 dùng OR đồng thời duyệt bộ ba có
  thứ tự, 1/8 có dấu chấm phẩy tạo thân for rỗng.
- Nhãn “đa dạng lỗi” là một tóm tắt cụm hỗn hợp, không phải một misconception đã
  được xác nhận. Nếu decision vẫn đánh giá một cơ chế chung theo prompt hiện tại,
  dùng uncertain/false. Có thể giữ toàn bộ mô tả các nhóm con trong reasoning.
- Thêm refs log của mỗi nhóm; các refs hiện tại chỉ có raw_code.

## Chỉ dẫn sửa lần tiếp theo

Trả lại cùng packet_id/cluster_id và schema gốc. Với 2812/c0, 2825/c1,
2825/c2, 2833/c1, giữ thông tin từng nhóm con nhưng đặt uncertain/false khi đánh giá
một cơ chế chung. 2825/c0 có thể giữ rejected/false nếu ghi rõ nhãn bị bác bỏ là
“tất cả bài chỉ sai presentation”. Sửa các sự kiện cụ thể nêu trên, thêm dẫn chứng
code VÀ test. Không gọi float == 0 là lỗi mặc định; không trộn sample ID giữa cụm;
không suy ra niềm tin học viên hay nguyên nhân tất định từ log lịch sử.

Không cần sửa clustering để ép các cụm thành đồng nhất chỉ nhằm phù hợp nhãn AI.
Giữ trường hợp mixed/uncertain là kết quả đánh giá có ý nghĩa. Các đề xuất ở đây
cần được kiểm tra lại với packet, không được dùng như gold.
