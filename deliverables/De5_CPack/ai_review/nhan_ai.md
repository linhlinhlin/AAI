# C-Pack-IPAs — 150 nhãn AI đề xuất

Chờ người dùng kiểm tra; chưa phải gold. Phạm vi: 150 bài pilot, không phải toàn bộ 2.151 bài theo cụm. Code và log lịch sử, không chạy lại C. Đề gốc còn thiếu. Các câu NẾU–VÀ–THÌ là AI diễn giải bằng chứng, không phải luật quy nạp mới.

## Bài 1 · lab03-ex07

**Không đặt lại số đang đọc sau dấu phép toán** · Có căn cứ code/log

NẾU aux được ghép chữ số nhưng không trở về 0 sau + hoặc − VÀ test ex07_0 ghi nhận output "89\n" thay vì "9\n" THÌ gợi ý: Không đặt lại số đang đọc sau dấu phép toán.

Sau khi cộng số 8 vào res, aux vẫn bằng 8. Đọc tiếp 1 làm aux thành 81 nên phép 8 + 1 cho 89. Các biểu thức sau tiếp tục nối dính chữ số.

Giảng lại / kiểm tra: Đặt aux = 0 sau khi chốt một toán hạng; truy vết 8 + 1.

Dòng: [14, 15, 17, 18, 22, 24]; test: ['ex07_0', 'ex07_1', 'ex07_2', 'ex07_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 2 · lab02-ex02

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex02_0 ghi nhận output "1\n2" thay vì "1\n2\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [11, 15]; test: ['ex02_0', 'ex02_1', 'ex02_2', 'ex02_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 3 · lab02-ex05

**Thừa khoảng trắng cuối dòng** · Có căn cứ code/log

NẾU code in dấu cách sau phần tử cuối hoặc đệm thêm chỗ trống bên phải VÀ test ex05_0 ghi nhận output "1 \n" thay vì "1\n" THÌ gợi ý: Thừa khoảng trắng cuối dòng.

So sánh từng dòng cho thấy phần nội dung khớp oracle, nhưng còn khoảng trắng trước ký tự xuống dòng. Đây là sai khác trình bày ở các test đã có.

Giảng lại / kiểm tra: Chỉ in dấu phân cách giữa hai phần tử; bỏ phần đệm cuối dòng nếu oracle không yêu cầu.

Dòng: [15]; test: ['ex05_0', 'ex05_1', 'ex05_2', 'ex05_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 4 · lab04-ex04

**In thêm dữ liệu kiểm tra ngoài đáp án** · Có căn cứ code/log

NẾU code in chuỗi đầu vào, chỉ số, tổng trung gian hoặc độ dài bên cạnh kết quả VÀ test ex04_0 ghi nhận output "adeus\nno\n" thay vì "no\n" THÌ gợi ý: In thêm dữ liệu kiểm tra ngoài đáp án.

Log có những dòng phụ khớp với lệnh in kiểm tra trong code. Phần đáp án phía sau không làm cho toàn bộ output khớp oracle.

Giảng lại / kiểm tra: Bỏ lệnh in kiểm tra và chỉ giữ output đề yêu cầu.

Dòng: [16, 27, 29]; test: ['ex04_0', 'ex04_1', 'ex04_2', 'ex04_3', 'ex04_4'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 5 · lab03-ex04

**Đổi xuống dòng thành dấu cách và tự thêm xuống dòng cuối** · Nhiều lỗi cùng xuất hiện

NẾU nhánh phân cách luôn printf một dấu cách, rồi cuối chương trình in thêm xuống dòng VÀ test ex04_0 ghi nhận output "1 2 3\n" thay vì "1 2 3" THÌ gợi ý: Đổi xuống dòng thành dấu cách và tự thêm xuống dòng cuối.

Test có 101 xuống dòng 0 bị biến thành 101 0; các test khác cũng có thêm newline so với oracle. Code không giữ nguyên loại dấu phân cách.

Giảng lại / kiểm tra: In lại đúng ký tự phân cách đã đọc và chỉ thêm newline nếu đặc tả yêu cầu.

Dòng: [18, 20, 27]; test: ['ex04_0', 'ex04_1', 'ex04_2', 'ex04_3', 'ex04_4', 'ex04_5', 'ex04_6', 'ex04_7', 'ex04_8'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 6 · lab02-ex07

**Bỏ sót ước là chính số n** · Có căn cứ code/log

NẾU vòng đếm chỉ thử các số từ 1 đến n/2 VÀ test ex07_0 ghi nhận output "3\n" thay vì "4\n" THÌ gợi ý: Bỏ sót ước là chính số n.

Các ước nhỏ được đếm nhưng n không được thử. Ví dụ 8 có các ước 1, 2, 4, 8; code chỉ đếm ba ước đầu.

Giảng lại / kiểm tra: Tính cả n, hoặc duyệt đến n và kiểm tra số dư.

Dòng: [10, 13, 15, 17]; test: ['ex07_0', 'ex07_1', 'ex07_2', 'ex07_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 7 · lab02-ex10

**Dừng tách chữ số quá sớm tại giá trị 10** · Có căn cứ code/log

NẾU vòng lặp dùng điều kiện n > 10 thay vì tiếp tục xử lý cả 10 VÀ test ex10_3 ghi nhận output "1\n10\n" thay vì "2\n1\n" THÌ gợi ý: Dừng tách chữ số quá sớm tại giá trị 10.

Khi số còn lại là 10, vòng lặp không chạy. Code xem 10 như một chữ số, nên báo một chữ số và tổng bằng 10.

Giảng lại / kiểm tra: Dùng điều kiện xử lý đúng biên 10; thử 10 và 100.

Dòng: [6, 8, 9, 10]; test: ['ex10_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 8 · lab02-ex02

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex02_0 ghi nhận output "1\n2" thay vì "1\n2\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [12, 18]; test: ['ex02_0', 'ex02_1', 'ex02_2', 'ex02_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 9 · lab04-ex03

**Đảo chiều điều kiện của vòng vẽ từ trên xuống** · Có căn cứ code/log

NẾU i bắt đầu ở giá trị lớn nhất nhưng điều kiện lại là i <= 1 VÀ test ex03_0 ghi nhận output "" thay vì "  *\n **\n***\n" THÌ gợi ý: Đảo chiều điều kiện của vòng vẽ từ trên xuống.

Ở các test, chiều cao lớn nhất lớn hơn 1 nên điều kiện sai ngay từ đầu. Phần vẽ không chạy và log rỗng.

Giảng lại / kiểm tra: Với i giảm dần, kiểm tra i >= 1.

Dòng: [25, 26, 27, 28]; test: ['ex03_0', 'ex03_1', 'ex03_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 10 · lab02-ex03

**Thừa lời nhắc và ký hiệu trong thông báo** · Có căn cứ code/log

NẾU printf có câu hướng dẫn, dấu chấm hoặc ký hiệu >> ngoài yes/no VÀ test ex03_0 ghi nhận output "Introduza dois inteiros positivos.\nyes.\n" thay vì "yes\n" THÌ gợi ý: Thừa lời nhắc và ký hiệu trong thông báo.

Code xuất nhiều ký tự mà oracle không yêu cầu. Sai khác này đủ làm test fail dù kết luận chia hết có thể đúng.

Giảng lại / kiểm tra: Giữ stdout đúng yes hoặc no kèm xuống dòng.

Dòng: [6, 9, 11]; test: ['ex03_0', 'ex03_1', 'ex03_2', 'ex03_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 11 · lab02-ex03

**Sai chữ hoa/chữ thường trong yes/no** · Có căn cứ code/log

NẾU chuỗi thông báo dùng chữ hoa trong khi oracle dùng chữ thường VÀ test ex03_0 ghi nhận output "YES\n" thay vì "yes\n" THÌ gợi ý: Sai chữ hoa/chữ thường trong yes/no.

Phép kiểm tra chia hết cho kết luận tương ứng với log; khác biệt là YES/NO hoặc Yes/No thay cho yes/no.

Giảng lại / kiểm tra: Giữ phép kiểm tra và sửa đúng chuỗi thông báo.

Dòng: [8]; test: ['ex03_0', 'ex03_1', 'ex03_2', 'ex03_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 12 · lab02-ex07

**Đếm số lần phân tích thừa số thay vì số lượng ước** · Có căn cứ code/log

NẾU code chia dần num cho currentdiv và tăng counter mỗi lần chia VÀ test ex07_3 ghi nhận output "3\n" thay vì "4\n" THÌ gợi ý: Đếm số lần phân tích thừa số thay vì số lượng ước.

Với 10, hai lần chia cho 2 rồi 5 làm bộ đếm từ 1 lên 3; oracle cần bốn ước 1, 2, 5, 10. Hai đại lượng không giống nhau.

Giảng lại / kiểm tra: Liệt kê ước của 10 để phân biệt đếm ước với đếm thừa số.

Dòng: [5, 7, 8, 9, 10]; test: ['ex07_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 13 · lab02-ex07

**In bộ đếm giữa vòng lặp và bỏ sót ước n** · Nhiều lỗi cùng xuất hiện

NẾU printf nằm trong while, còn miền thử ước chỉ đến n/2 VÀ test ex07_0 ghi nhận output "1\n2\n2\n3\n" thay vì "4\n" THÌ gợi ý: In bộ đếm giữa vòng lặp và bỏ sót ước n.

Output là một dãy tổng tạm thời. Ngay cả tổng cuối cũng thiếu ước n, nên có cả lỗi vị trí in và lỗi miền duyệt.

Giảng lại / kiểm tra: Đưa lệnh in ra sau vòng và tính cả ước n.

Dòng: [12, 14, 15, 17]; test: ['ex07_0', 'ex07_1', 'ex07_2', 'ex07_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 14 · lab04-ex03

**Đảo điều kiện in sao và cách duyệt độ cao** · Có căn cứ code/log

NẾU khi val[c] > l code in khoảng trắng, còn l tăng từ 0 VÀ test ex03_0 ghi nhận output "   \n*  \n** \n" thay vì "  *\n **\n***\n" THÌ gợi ý: Đảo điều kiện in sao và cách duyệt độ cao.

Dòng đầu luôn trống với dữ liệu dương. Các hàng sau tạo phần bù của cột cần vẽ, khác biểu đồ đi từ đỉnh xuống trong oracle.

Giảng lại / kiểm tra: Duyệt mức cao từ max đến 1; in sao khi chiều cao cột đạt mức đó.

Dòng: [14, 16, 17, 19]; test: ['ex03_0', 'ex03_1', 'ex03_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 15 · lab02-ex02

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex02_1 ghi nhận output "2\n6" thay vì "2\n6\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [12, 16]; test: ['ex02_1', 'ex02_2', 'ex02_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 16 · lab03-ex03

**Thừa khoảng trắng cuối dòng** · Có căn cứ code/log

NẾU code in dấu cách sau phần tử cuối hoặc đệm thêm chỗ trống bên phải VÀ test ex03_0 ghi nhận output "* - * \n- * - \n* - * \n" thay vì "* - *\n- * -\n* - *\n" THÌ gợi ý: Thừa khoảng trắng cuối dòng.

So sánh từng dòng cho thấy phần nội dung khớp oracle, nhưng còn khoảng trắng trước ký tự xuống dòng. Đây là sai khác trình bày ở các test đã có.

Giảng lại / kiểm tra: Chỉ in dấu phân cách giữa hai phần tử; bỏ phần đệm cuối dòng nếu oracle không yêu cầu.

Dòng: [13, 16, 20]; test: ['ex03_0', 'ex03_1', 'ex03_2', 'ex03_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 17 · lab02-ex09

**Tính giây từ số phút thay vì phần dư của tổng giây** · Có căn cứ code/log

NẾU s được gán m/60 + m%60 VÀ test ex09_0 ghi nhận output "00:01:01\n" thay vì "00:01:00\n" THÌ gợi ý: Tính giây từ số phút thay vì phần dư của tổng giây.

Đầu vào 60 cho phút bằng 1 và giây cũng bằng 1. Phần giây phải lấy từ N % 60, không phải từ số phút.

Giảng lại / kiểm tra: Tách giờ, phút, giây bằng thương và số dư đúng đơn vị.

Dòng: [11, 12, 13]; test: ['ex09_0', 'ex09_1', 'ex09_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 18 · lab04-ex07

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex07_0 ghi nhận output "ol deus" thay vì "ol deus\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [42]; test: ['ex07_0', 'ex07_1', 'ex07_2', 'ex07_3', 'ex07_4'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 19 · lab02-ex05

**In dãy theo thứ tự giảm thay vì tăng** · Có căn cứ code/log

NẾU vòng lặp in v rồi giảm v đến 0 VÀ test ex05_1 ghi nhận output "2\n1\n" thay vì "1\n2\n" THÌ gợi ý: In dãy theo thứ tự giảm thay vì tăng.

Với đầu vào 3, log là 3, 2, 1 trong khi oracle là 1, 2, 3.

Giảng lại / kiểm tra: Dùng biến chạy từ 1 tới giới hạn nhập.

Dòng: [7, 9, 10]; test: ['ex05_1', 'ex05_2', 'ex05_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 20 · lab02-ex05

**In thừa lời nhắc nhập dữ liệu** · Có căn cứ code/log

NẾU code in lời nhắc hoặc nhãn mô tả ngoài kết quả VÀ test ex05_0 ghi nhận output "Escreva um numero: \n1\n" thay vì "1\n" THÌ gợi ý: In thừa lời nhắc nhập dữ liệu.

Các dòng hướng dẫn nhập xuất hiện trong stdout nhưng không thuộc đáp án. Cần phân biệt giao diện tương tác với output nộp cho hệ thống chấm.

Giảng lại / kiểm tra: Bỏ lời nhắc khỏi stdout nộp bài; đối chiếu lại các test.

Dòng: [6, 10]; test: ['ex05_0', 'ex05_1', 'ex05_2', 'ex05_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 21 · lab04-ex02

**Dùng chỉ số và điều kiện lặp chưa khởi tạo** · Có căn cứ code/log

NẾU i và l được đọc trước khi có giá trị ban đầu VÀ test ex02_0 ghi nhận output "" thay vì "***\n **\n  *\n" THÌ gợi ý: Dùng chỉ số và điều kiện lặp chưa khởi tạo.

i dùng làm chỉ số tab khi nhập, còn l dùng ngay trong điều kiện while. Không có phép gán ban đầu cho hai biến này; không thể xem output rỗng là một kết quả xác định của thuật toán.

Giảng lại / kiểm tra: Khởi tạo i và l trước lần dùng đầu tiên; kiểm tra giới hạn mảng.

Dòng: [9, 15, 16, 20, 21]; test: ['ex02_0', 'ex02_1', 'ex02_2'].

Có sử dụng giá trị chưa khởi tạo. Log rỗng không đủ xác định chương trình crash hay bỏ qua vòng lặp.

## Bài 22 · lab02-ex03

**Thừa lời nhắc và ký hiệu trong thông báo** · Có căn cứ code/log

NẾU printf có câu hướng dẫn, dấu chấm hoặc ký hiệu >> ngoài yes/no VÀ test ex03_0 ghi nhận output " introduza os valores de N e M \n\n >>yes \n\n" thay vì "yes\n" THÌ gợi ý: Thừa lời nhắc và ký hiệu trong thông báo.

Code xuất nhiều ký tự mà oracle không yêu cầu. Sai khác này đủ làm test fail dù kết luận chia hết có thể đúng.

Giảng lại / kiểm tra: Giữ stdout đúng yes hoặc no kèm xuống dòng.

Dòng: [11, 20, 24]; test: ['ex03_0', 'ex03_1', 'ex03_2', 'ex03_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 23 · lab04-ex03

**Dừng vẽ theo cột thấp nhất, làm thiếu hàng đáy** · Có căn cứ code/log

NẾU vòng vẽ tăng mọi phần tử và dừng khi tất cả vượt max VÀ test ex03_1 ghi nhận output "  *\n  *\n **\n **\n **\n **\n***\n" thay vì "  *\n  *\n **\n **\n **\n **\n***\n***\n" THÌ gợi ý: Dừng vẽ theo cột thấp nhất, làm thiếu hàng đáy.

Log test 3 2 6 8 thiếu một hàng ***. Tuy nhiên, truy vết đoạn code này cho dãy ban đầu [2,6,8] cho điều kiện dừng sau bảy lần in, trong khi oracle cần tám hàng: điều kiện dừng phụ thuộc min của mảng chứ không cố định max hàng.

Giảng lại / kiểm tra: Đếm số hàng cần in bằng một biến mức cao riêng, không tăng dữ liệu đầu vào.

Dòng: [58, 68, 70, 76]; test: ['ex03_1'].

Điểm cần kiểm tra là cách tính số hàng: max − min + 1 bằng 7 ở test này, không phải max = 8.

## Bài 24 · lab04-ex07

**Đọc ký tự cần xóa trước khi đọc chuỗi** · Có căn cứ code/log

NẾU scanf lấy ký tự đầu của input làm n rồi mới đọc phần còn lại VÀ test ex07_0 ghi nhận output "la adeus\n" thay vì "ol deus\n" THÌ gợi ý: Đọc ký tự cần xóa trước khi đọc chuỗi.

Với ola adeus rồi ký tự a, code lấy o làm ký tự cần xóa và chỉ đọc la adeus. Thứ tự đọc không khớp input test.

Giảng lại / kiểm tra: Đọc trọn dòng chuỗi trước, rồi đọc ký tự cần xóa.

Dòng: [9, 10, 19, 20]; test: ['ex07_0', 'ex07_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 25 · lab04-ex01

**Code thực hiện tác vụ khác với oracle của bài** · Cần kiểm tra thêm

NẾU code xử lý palindrome, phân loại tam giác, min/max hoặc vẽ kim tự tháp thay vì tác vụ thể hiện trong test VÀ test ex01_0 ghi nhận output "yes\n" thay vì "*\n**\n***\n" THÌ gợi ý: Code thực hiện tác vụ khác với oracle của bài.

Output và cấu trúc code cho thấy một tác vụ khác hẳn bộ test: đây có thể là nộp nhầm bài hoặc ánh xạ dữ liệu sai. Gói thiếu đề gốc nên chưa kết luận đó là lỗi kiến thức của người học.

Giảng lại / kiểm tra: Kiểm tra lại đề, mã bài và nguồn ghép test trước khi gán nhãn cơ chế.

Dòng: [20, 25, 34, 39]; test: ['ex01_0', 'ex01_1', 'ex01_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 26 · lab02-ex04

**Thừa khoảng trắng đầu dòng và thiếu xuống dòng cuối** · Có căn cứ code/log

NẾU mỗi số được in với dấu cách đứng trước, không in newline sau cùng VÀ test ex04_0 ghi nhận output " 1 2 6" thay vì "1 2 6\n" THÌ gợi ý: Thừa khoảng trắng đầu dòng và thiếu xuống dòng cuối.

Các số đã sắp xếp đúng trong log được cung cấp, nhưng dòng bắt đầu bằng khoảng trắng và không kết thúc bằng newline. Code dùng so sánh chặt còn cần kiểm tra riêng trường hợp bằng nhau chưa có trong log.

Giảng lại / kiểm tra: Sửa định dạng; bổ sung kiểm tra giá trị bằng nhau khi có đặc tả.

Dòng: [12, 13, 14, 18, 19, 20, 27, 28, 29, 33, 34, 35, 42, 43, 44, 48, 49, 50]; test: ['ex04_0', 'ex04_1', 'ex04_2', 'ex04_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 27 · lab04-ex01

**Duyệt quá n phần tử và in thừa lời nhắc** · Nhiều lỗi cùng xuất hiện

NẾU vòng xuất dùng j <= n dù chỉ nhập các chỉ số 0 đến n−1 VÀ test ex01_0 ghi nhận output "Insira um número: Insira o 1º número: Insira o 2º número: Insira o 3º número: *\n**\n***\n\n" thay vì "*\n**\n***\n" THÌ gợi ý: Duyệt quá n phần tử và in thừa lời nhắc.

Code đọc arr[n] chưa được nhập, thêm một hàng ngoài n hàng cần có; stdout còn có lời nhắc. Không coi giá trị tình cờ của arr[n] là 0 ổn định.

Giảng lại / kiểm tra: Sửa j < n và bỏ các lời nhắc stdout.

Dòng: [9, 13, 17, 18, 20]; test: ['ex01_0', 'ex01_1', 'ex01_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 28 · lab03-ex06

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex06_0 ghi nhận output "no" thay vì "no\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [11, 13]; test: ['ex06_0', 'ex06_1', 'ex06_2', 'ex06_3', 'ex06_4', 'ex06_5', 'ex06_6'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 29 · lab03-ex05

**Bộ lọc trong dấu nháy làm mất dấu câu** · Có căn cứ code/log

NẾU nhánh in ký tự thường chỉ chấp nhận chữ cái và dấu cách VÀ test ex05_3 ghi nhận output "Disse \"ola como estai\"\nfoo bar\n\\\\\\\\\n" thay vì "Disse: \"ola, como estai?\"\nfoo bar\n////\\\\***\\\\\n" THÌ gợi ý: Bộ lọc trong dấu nháy làm mất dấu câu.

Log mất dấu hai chấm, dấu phẩy, dấu hỏi và các ký hiệu /, * bên trong chuỗi. Chúng không phải dấu đóng chuỗi hay escape nên không nên bị bỏ chỉ vì không phải chữ cái.

Giảng lại / kiểm tra: Trong chuỗi, giữ mọi ký tự thường và xử lý riêng dấu nháy/escape.

Dòng: [30, 32, 37, 38]; test: ['ex05_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 30 · lab02-ex08

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex08_0 ghi nhận output "3.00" thay vì "3.00\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [18]; test: ['ex08_0', 'ex08_1', 'ex08_2', 'ex08_3', 'ex08_4'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 31 · lab03-ex04

**Không xuất số 0 còn chờ khi gặp EOF, đồng thời thừa newline** · Nhiều lỗi cùng xuất hiện

NẾU code chỉ chốt chuỗi toàn số 0 khi gặp ký tự phân cách VÀ test ex04_0 ghi nhận output "1 2 3\n" thay vì "1 2 3" THÌ gợi ý: Không xuất số 0 còn chờ khi gặp EOF, đồng thời thừa newline.

Ở input kết thúc bằng 000, số cuối bị mất. Lệnh in cuối chỉ thêm newline chứ không chốt giá trị 0 đang chờ; nhiều log khác cũng dư newline.

Giảng lại / kiểm tra: Sau vòng đọc, kiểm tra trạng thái còn chờ số 0 trước khi kết thúc.

Dòng: [26, 27, 39, 41, 42]; test: ['ex04_0', 'ex04_1', 'ex04_2', 'ex04_3', 'ex04_4', 'ex04_5', 'ex04_6', 'ex04_7', 'ex04_8'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 32 · lab03-ex05

**Sai trạng thái đọc chuỗi và để hở các ô của bộ đệm** · Nhiều lỗi cùng xuất hiện

NẾU dấu cách đưa estado về FORA, còn i tăng cả khi không ghi s[i] VÀ test ex05_0 ghi nhận output "entrou" thay vì "foo\n" THÌ gợi ý: Sai trạng thái đọc chuỗi và để hở các ô của bộ đệm.

Chuỗi có khoảng trắng bị cắt trạng thái; các vị trí không được gán trong s làm printf đọc dữ liệu chưa xác định. Ngoài ra còn in dòng debug entrou.

Giảng lại / kiểm tra: Tách trạng thái trong/ngoài chuỗi và escape; chỉ tăng chỉ số khi thực sự ghi một ký tự.

Dòng: [20, 21, 30, 54, 56, 58, 61]; test: ['ex05_0', 'ex05_1', 'ex05_2', 'ex05_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 33 · lab02-ex01

**Code thực hiện tác vụ khác với oracle của bài** · Cần kiểm tra thêm

NẾU code xử lý palindrome, phân loại tam giác, min/max hoặc vẽ kim tự tháp thay vì tác vụ thể hiện trong test VÀ test ex01_0 ghi nhận output "? ? ? Não é triângulo" thay vì "3\n" THÌ gợi ý: Code thực hiện tác vụ khác với oracle của bài.

Output và cấu trúc code cho thấy một tác vụ khác hẳn bộ test: đây có thể là nộp nhầm bài hoặc ánh xạ dữ liệu sai. Gói thiếu đề gốc nên chưa kết luận đó là lỗi kiến thức của người học.

Giảng lại / kiểm tra: Kiểm tra lại đề, mã bài và nguồn ghép test trước khi gán nhãn cơ chế.

Dòng: [7, 9, 11, 14, 18, 22, 26, 29]; test: ['ex01_0', 'ex01_1', 'ex01_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 34 · lab02-ex04

**Thừa khoảng trắng cuối dòng** · Có căn cứ code/log

NẾU code in dấu cách sau phần tử cuối hoặc đệm thêm chỗ trống bên phải VÀ test ex04_0 ghi nhận output "1 2 6 \n" thay vì "1 2 6\n" THÌ gợi ý: Thừa khoảng trắng cuối dòng.

So sánh từng dòng cho thấy phần nội dung khớp oracle, nhưng còn khoảng trắng trước ký tự xuống dòng. Đây là sai khác trình bày ở các test đã có.

Giảng lại / kiểm tra: Chỉ in dấu phân cách giữa hai phần tử; bỏ phần đệm cuối dòng nếu oracle không yêu cầu.

Dòng: [27, 28]; test: ['ex04_0', 'ex04_1', 'ex04_2', 'ex04_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 35 · lab03-ex07

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex07_0 ghi nhận output "9" thay vì "9\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [39]; test: ['ex07_0', 'ex07_1', 'ex07_2', 'ex07_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 36 · lab03-ex07

**Đọc ký tự xuống dòng như một chữ số và in thêm dòng trống** · Nhiều lỗi cùng xuất hiện

NẾU strToInt không dừng ở newline, sau đó đưa ký tự đó vào phép ghép số VÀ test ex07_0 ghi nhận output "\n20\n" thay vì "9\n" THÌ gợi ý: Đọc ký tự xuống dòng như một chữ số và in thêm dòng trống.

Trong 8 + 1 xuống dòng, ký tự newline được chuyển thành 2 bởi charToDecimal, nên số cuối thành 12 và tổng thành 20. printf còn thêm newline trước kết quả.

Giảng lại / kiểm tra: Chỉ ghép ký tự 0–9, dừng đúng newline/EOF và bỏ dòng trống đầu.

Dòng: [15, 20, 26, 27, 28]; test: ['ex07_0', 'ex07_1', 'ex07_2', 'ex07_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 37 · lab04-ex08

**Tìm chữ số lớn nhất thay vì số nguyên lớn nhất** · Có căn cứ code/log

NẾU code duyệt từng ký tự và giữ max của c − 0 VÀ test ex08_2 ghi nhận output "9\n" thay vì "9988888888888888888888\n" THÌ gợi ý: Tìm chữ số lớn nhất thay vì số nguyên lớn nhất.

Hai số dài trong input đều bị rút thành một chữ số 9. Không có bước so sánh giá trị của hai chuỗi số nguyên.

Giảng lại / kiểm tra: So sánh hai số dạng chuỗi sau khi chuẩn hóa, không lấy max của từng chữ số.

Dòng: [6, 7, 8, 10]; test: ['ex08_2', 'ex08_3', 'ex08_4', 'ex08_5'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 38 · lab04-ex06

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex06_0 ghi nhận output "OLA ADEUS" thay vì "OLA ADEUS\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [20]; test: ['ex06_0', 'ex06_1', 'ex06_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 39 · lab02-ex05

**Tăng biến trước khi in làm mất số 1, đồng thời thiếu dấu phân cách** · Nhiều lỗi cùng xuất hiện

NẾU i bắt đầu ở 1 nhưng tăng lên trước printf VÀ test ex05_0 ghi nhận output "" thay vì "1\n" THÌ gợi ý: Tăng biến trước khi in làm mất số 1, đồng thời thiếu dấu phân cách.

Input 1 không in gì; input 3 in 23 thay vì ba dòng 1, 2, 3. Bài 101 còn gọi scanf thừa trong vòng dù input chỉ có một giới hạn.

Giảng lại / kiểm tra: In từ 1 đến n, mỗi số một dòng, không đọc lại giới hạn trong vòng.

Dòng: [8, 9, 10, 11]; test: ['ex05_0', 'ex05_1', 'ex05_2', 'ex05_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 40 · lab03-ex03

**Thừa khoảng trắng cuối dòng** · Có căn cứ code/log

NẾU code in dấu cách sau phần tử cuối hoặc đệm thêm chỗ trống bên phải VÀ test ex03_0 ghi nhận output "* - * \n- * - \n* - * \n" thay vì "* - *\n- * -\n* - *\n" THÌ gợi ý: Thừa khoảng trắng cuối dòng.

So sánh từng dòng cho thấy phần nội dung khớp oracle, nhưng còn khoảng trắng trước ký tự xuống dòng. Đây là sai khác trình bày ở các test đã có.

Giảng lại / kiểm tra: Chỉ in dấu phân cách giữa hai phần tử; bỏ phần đệm cuối dòng nếu oracle không yêu cầu.

Dòng: [20, 24, 27]; test: ['ex03_0', 'ex03_1', 'ex03_2', 'ex03_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 41 · lab02-ex10

**Chưa triển khai phần xử lý và in kết quả** · Có căn cứ code/log

NẾU main chỉ kết thúc bằng return, không có phần giải bài VÀ test ex10_0 ghi nhận output "" thay vì "2\n3\n" THÌ gợi ý: Chưa triển khai phần xử lý và in kết quả.

Code hiện là khung chưa hoàn thiện; các log đều rỗng. Không có đủ thông tin để gán một hiểu lầm thuật toán cụ thể.

Giảng lại / kiểm tra: Viết các bước xử lý đầu vào rồi bổ sung tính toán và output.

Dòng: [13]; test: ['ex10_0', 'ex10_1', 'ex10_2', 'ex10_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 42 · lab03-ex04

**Đặt sai trạng thái sau khi chốt một nhóm số 0** · Nhiều lỗi cùng xuất hiện

NẾU sau khi đọc dấu phân cách của nhóm số 0, code vẫn đặt teste = 1 VÀ test ex04_0 ghi nhận output "1 2 3\n" thay vì "1 2 3" THÌ gợi ý: Đặt sai trạng thái sau khi chốt một nhóm số 0.

Số kế tiếp bị xem là đang ở giữa một số nên các số 0 đầu không bị bỏ; log 000 027770 vẫn còn 027770. Cuối chương trình còn dư newline.

Giảng lại / kiểm tra: Sau dấu phân cách phải về trạng thái đầu số; đối chiếu cả trường hợp EOF.

Dòng: [11, 12, 19, 21, 23, 30]; test: ['ex04_0', 'ex04_1', 'ex04_2', 'ex04_3', 'ex04_4', 'ex04_5', 'ex04_6', 'ex04_7', 'ex04_8'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 43 · lab04-ex04

**In thêm dữ liệu kiểm tra ngoài đáp án** · Có căn cứ code/log

NẾU code in chuỗi đầu vào, chỉ số, tổng trung gian hoặc độ dài bên cạnh kết quả VÀ test ex04_0 ghi nhận output "2/2-------0------\n2/2-------1------\nno\n" thay vì "no\n" THÌ gợi ý: In thêm dữ liệu kiểm tra ngoài đáp án.

Log có những dòng phụ khớp với lệnh in kiểm tra trong code. Phần đáp án phía sau không làm cho toàn bộ output khớp oracle.

Giảng lại / kiểm tra: Bỏ lệnh in kiểm tra và chỉ giữ output đề yêu cầu.

Dòng: [26, 34, 36]; test: ['ex04_0', 'ex04_1', 'ex04_2', 'ex04_4'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 44 · lab02-ex07

**Bỏ sót ước là chính số n** · Có căn cứ code/log

NẾU vòng đếm chỉ thử các số từ 1 đến n/2 VÀ test ex07_0 ghi nhận output "3\n" thay vì "4\n" THÌ gợi ý: Bỏ sót ước là chính số n.

Các ước nhỏ được đếm nhưng n không được thử. Ví dụ 8 có các ước 1, 2, 4, 8; code chỉ đếm ba ước đầu.

Giảng lại / kiểm tra: Tính cả n, hoặc duyệt đến n và kiểm tra số dư.

Dòng: [12, 14, 15, 18]; test: ['ex07_0', 'ex07_1', 'ex07_2', 'ex07_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 45 · lab04-ex02

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex02_0 ghi nhận output "***\n **\n  *" thay vì "***\n **\n  *\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [22, 27, 32]; test: ['ex02_0', 'ex02_1', 'ex02_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 46 · lab04-ex08

**Không dừng sau chữ số khác nhau đầu tiên khi so sánh hai số** · Có căn cứ code/log

NẾU printf nằm trong vòng so sánh từng vị trí mà không return hoặc break VÀ test ex08_4 ghi nhận output "9988888888888888888887\n9988888888888888888887\n9988888888888888888887\n9988888888888888888887\n9988888888888888888887\n9988888888888888888887\n9988888888888888888887\n9988888888888888888887\n9988888888888888888887\n9988888888888888888887\n9988888888888888888887\n9988888888888888888887\n9988888888888888888887\n9988888888888888888887\n9988888888888888888887\n9988888888888888888887\n9988888888888888888887\n9988888888888888888887\n9988888888888888888887\n9988888888888888888887\n9988888888888888888887\n9988888888888888888887\n" thay vì "9988888888888888888887\n" THÌ gợi ý: Không dừng sau chữ số khác nhau đầu tiên khi so sánh hai số.

Mỗi cặp chữ số khác nhau lại in một lần. Log hai số dài lặp cùng đáp án nhiều dòng; các vị trí sau không nên được quyết định lại thứ tự đã xác lập.

Giảng lại / kiểm tra: Quyết định tại chữ số khác nhau đầu tiên rồi kết thúc so sánh.

Dòng: [23, 24, 25, 26, 27, 40, 41, 42, 43, 44]; test: ['ex08_4', 'ex08_5'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 47 · lab04-ex02

**Đảo chiều so sánh độ cao khi vẽ cột** · Có căn cứ code/log

NẾU code in sao khi vec[j] <= i VÀ test ex02_0 ghi nhận output "*  \n** \n***\n" thay vì "***\n **\n  *\n" THÌ gợi ý: Đảo chiều so sánh độ cao khi vẽ cột.

Chiều cao nhỏ bắt đầu có sao trước rồi số sao tăng dần, trái với oracle cần hàng đầu đầy sao và giảm dần.

Giảng lại / kiểm tra: Với mức i tăng từ 1, in sao khi chiều cao >= i.

Dòng: [31, 35]; test: ['ex02_0', 'ex02_1', 'ex02_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 48 · lab04-ex05

**In thừa một dòng trống cuối output** · Có căn cứ code/log

NẾU code in newline dù chuỗi hoặc nhánh trước đã kết thúc bằng newline VÀ test ex05_2 ghi nhận output "Hello world!\n\n" thay vì "Hello world!\n" THÌ gợi ý: In thừa một dòng trống cuối output.

Log khớp nội dung nhưng có thêm một newline ở cuối. Bài dùng fgets cần chú ý newline đã nằm trong chuỗi.

Giảng lại / kiểm tra: Bảo đảm output chỉ kết thúc bằng số newline mà oracle yêu cầu.

Dòng: [29]; test: ['ex05_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 49 · lab04-ex08

**Đổi số nguyên dài sang kiểu số có giới hạn gây mất giá trị** · Nhiều lỗi cùng xuất hiện

NẾU chuỗi dài được đổi sang long qua lũy thừa int, rồi hiệu gán vào int VÀ test ex08_4 ghi nhận output "0000000000000000000000\n" thay vì "9988888888888888888887\n" THÌ gợi ý: Đổi số nguyên dài sang kiểu số có giới hạn gây mất giá trị.

Số có 22 chữ số không được biểu diễn an toàn bằng các kiểu đang dùng. pot còn bắt đầu ở bậc comp thay vì comp−1. Log chọn chuỗi zero thay vì số lớn.

Giảng lại / kiểm tra: So sánh độ dài và chữ số sau chuẩn hóa thay vì ép số dài vào int/long.

Dòng: [18, 30, 37, 43, 44, 49]; test: ['ex08_4', 'ex08_5'].

Có nguy cơ tràn số nguyên có dấu; không coi giá trị tràn hay kết quả lịch sử là hành vi xác định.

## Bài 50 · lab04-ex01

**Tăng nhầm biến của vòng ngoài trong vòng in sao** · Nhiều lỗi cùng xuất hiện

NẾU vòng j lại cập nhật i++, đồng thời nhập tới VECMAX thay vì n VÀ test ex01_0 ghi nhận output "********\n" thay vì "*\n**\n***\n" THÌ gợi ý: Tăng nhầm biến của vòng ngoài trong vòng in sao.

j không tiến tới điều kiện dừng; i thay đổi làm code đọc phần tử khác trong lúc in cùng một hàng. Số lần nhập cũng vượt lượng dữ liệu trong test.

Giảng lại / kiểm tra: Sửa cập nhật thành j++, giới hạn nhập bằng n và kiểm tra scanf.

Dòng: [10, 11, 12, 13, 14]; test: ['ex01_0', 'ex01_1', 'ex01_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 51 · lab03-ex07

**In thừa dòng trống trước kết quả** · Có căn cứ code/log

NẾU printf bắt đầu bằng newline trước số kết quả VÀ test ex07_0 ghi nhận output "\n9\n" thay vì "9\n" THÌ gợi ý: In thừa dòng trống trước kết quả.

Các giá trị biểu thức trong log đã khớp; khác biệt là một dòng trống ở đầu.

Giảng lại / kiểm tra: Bỏ newline đứng trước %d.

Dòng: [15]; test: ['ex07_0', 'ex07_1', 'ex07_2', 'ex07_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 52 · lab04-ex05

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex05_0 ghi nhận output "ola adeus" thay vì "ola adeus\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [15]; test: ['ex05_0', 'ex05_1', 'ex05_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 53 · lab03-ex04

**Không xuất số 0 còn chờ khi gặp EOF, đồng thời thừa newline** · Nhiều lỗi cùng xuất hiện

NẾU code chỉ chốt chuỗi toàn số 0 khi gặp ký tự phân cách VÀ test ex04_0 ghi nhận output "1 2 3\n" thay vì "1 2 3" THÌ gợi ý: Không xuất số 0 còn chờ khi gặp EOF, đồng thời thừa newline.

Ở input kết thúc bằng 000, số cuối bị mất. Lệnh in cuối chỉ thêm newline chứ không chốt giá trị 0 đang chờ; nhiều log khác cũng dư newline.

Giảng lại / kiểm tra: Sau vòng đọc, kiểm tra trạng thái còn chờ số 0 trước khi kết thúc.

Dòng: [16, 17, 18, 25, 27, 39]; test: ['ex04_0', 'ex04_1', 'ex04_2', 'ex04_3', 'ex04_4', 'ex04_5', 'ex04_6', 'ex04_7', 'ex04_8'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 54 · lab03-ex07

**Không kết thúc bộ đệm chuỗi và ghép cả newline vào số** · Nhiều lỗi cùng xuất hiện

NẾU s không được thêm ký tự kết thúc sau khi lọc khoảng trắng, còn vòng ghép số nhận cả newline VÀ test ex07_0 ghi nhận output "-20\n" thay vì "9\n" THÌ gợi ý: Không kết thúc bộ đệm chuỗi và ghép cả newline vào số.

Chuỗi s có thể bị đọc qua phần đã ghi. Ngay trong dữ liệu hợp lệ, newline cuối fgets cũng đi vào phép trừ 0 và ghép số; điều kiện dùng || để loại hai toán tử luôn đúng.

Giảng lại / kiểm tra: Thêm s[j] = 0, nhận riêng chữ số 0–9 và kiểm tra lại điều kiện loại toán tử.

Dòng: [13, 15, 19, 25, 26, 28, 32]; test: ['ex07_0', 'ex07_1', 'ex07_2', 'ex07_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 55 · lab02-ex10

**Dừng tách chữ số quá sớm tại giá trị 10** · Có căn cứ code/log

NẾU vòng lặp dùng điều kiện n > 10 thay vì tiếp tục xử lý cả 10 VÀ test ex10_3 ghi nhận output "1\n10\n" thay vì "2\n1\n" THÌ gợi ý: Dừng tách chữ số quá sớm tại giá trị 10.

Khi số còn lại là 10, vòng lặp không chạy. Code xem 10 như một chữ số, nên báo một chữ số và tổng bằng 10.

Giảng lại / kiểm tra: Dùng điều kiện xử lý đúng biên 10; thử 10 và 100.

Dòng: [15, 16, 19, 22]; test: ['ex10_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 56 · lab02-ex06

**Dùng %n thay cho %d để nhập số lượng** · Nhiều lỗi cùng xuất hiện

NẾU scanf dùng %n nên ghi số ký tự đã đọc, không đọc số n trong input VÀ test ex06_0 ghi nhận output "min: 3.000000, max: 3.000000\n" thay vì "min: 1.500000, max: 3.000000\n" THÌ gợi ý: Dùng %n thay cho %d để nhập số lượng.

n nhận 0 ở đầu input. Lần scanf tiếp theo đọc chính số lượng làm val, nên min/max thành 3 hoặc 4 như log. Code còn thiếu giảm n trong while và so min với max.

Giảng lại / kiểm tra: Đổi sang %d, kiểm tra số lượt đọc và tách cập nhật min/max.

Dòng: [10, 12, 14, 16, 20, 21]; test: ['ex06_0', 'ex06_1', 'ex06_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 57 · lab04-ex06

**Loại nhầm hai biên a và z khi đổi chữ hoa** · Có căn cứ code/log

NẾU điều kiện dùng a < s[i] < z theo hai phép so sánh chặt VÀ test ex06_0 ghi nhận output "OLA aDEUS\n" thay vì "OLA ADEUS\n" THÌ gợi ý: Loại nhầm hai biên a và z khi đổi chữ hoa.

Chữ a trong các test vẫn là chữ thường, trong khi các chữ nằm giữa được đổi. Cùng điều kiện này cũng bỏ z.

Giảng lại / kiểm tra: Dùng >= a và <= z; test thêm hai ký tự biên.

Dòng: [24, 25]; test: ['ex06_0', 'ex06_1', 'ex06_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 58 · lab04-ex05

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex05_0 ghi nhận output "ola adeus" thay vì "ola adeus\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [21]; test: ['ex05_0', 'ex05_1', 'ex05_2', 'ex05_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 59 · lab03-ex06

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex06_0 ghi nhận output "no" thay vì "no\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [12, 14]; test: ['ex06_0', 'ex06_1', 'ex06_2', 'ex06_3', 'ex06_4', 'ex06_5', 'ex06_6'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 60 · lab04-ex06

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex06_0 ghi nhận output "OLA ADEUS" thay vì "OLA ADEUS\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [19]; test: ['ex06_0', 'ex06_1', 'ex06_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 61 · lab03-ex04

**Quên chốt nhóm toàn số 0 khi hết input** · Có căn cứ code/log

NẾU chỉ in 0 trong nhánh gặp ký tự khác 0 ở vòng đọc VÀ test ex04_3 ghi nhận output "101\n" thay vì "101\n0" THÌ gợi ý: Quên chốt nhóm toàn số 0 khi hết input.

Khi EOF xuất hiện ngay sau 0 hoặc 000, code thoát vòng trước khi in số 0 đang chờ. Log mất số cuối.

Giảng lại / kiểm tra: Xử lý trạng thái còn chờ một lần nữa sau vòng đọc.

Dòng: [12, 15, 16, 17, 22]; test: ['ex04_3', 'ex04_8'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 62 · lab02-ex05

**In thừa lời nhắc nhập dữ liệu** · Có căn cứ code/log

NẾU code in lời nhắc hoặc nhãn mô tả ngoài kết quả VÀ test ex05_0 ghi nhận output "Introduza um numero inteiro:\n1\n" thay vì "1\n" THÌ gợi ý: In thừa lời nhắc nhập dữ liệu.

Các dòng hướng dẫn nhập xuất hiện trong stdout nhưng không thuộc đáp án. Cần phân biệt giao diện tương tác với output nộp cho hệ thống chấm.

Giảng lại / kiểm tra: Bỏ lời nhắc khỏi stdout nộp bài; đối chiếu lại các test.

Dòng: [8, 12]; test: ['ex05_0', 'ex05_1', 'ex05_2', 'ex05_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 63 · lab02-ex01

**In thừa lời nhắc nhập dữ liệu** · Có căn cứ code/log

NẾU code in lời nhắc hoặc nhãn mô tả ngoài kết quả VÀ test ex01_0 ghi nhận output "Introduza o primeiro número: Introduza o segundo número: Introduza o terceiro número: O maior número é: 3\n" thay vì "3\n" THÌ gợi ý: In thừa lời nhắc nhập dữ liệu.

Các dòng hướng dẫn nhập xuất hiện trong stdout nhưng không thuộc đáp án. Cần phân biệt giao diện tương tác với output nộp cho hệ thống chấm.

Giảng lại / kiểm tra: Bỏ lời nhắc khỏi stdout nộp bài; đối chiếu lại các test.

Dòng: [9, 12, 15, 26]; test: ['ex01_0', 'ex01_1', 'ex01_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 64 · lab03-ex02

**Thừa dấu cách cuối hàng và thiếu newline cuối hình** · Có căn cứ code/log

NẾU mỗi số thường được in kèm dấu cách, còn newline bị bỏ ở hàng cuối VÀ test ex02_0 ghi nhận output "    1 \n  1 2 1 \n1 2 3 2 1" thay vì "    1\n  1 2 1\n1 2 3 2 1\n" THÌ gợi ý: Thừa dấu cách cuối hàng và thiếu newline cuối hình.

Các hàng trên dư dấu cách; hàng cuối thiếu newline. Hình số trong log vẫn cùng thứ tự với oracle.

Giảng lại / kiểm tra: In dấu cách giữa các số và kết thúc mọi hàng bằng newline.

Dòng: [22, 25, 28, 31, 32]; test: ['ex02_0', 'ex02_1', 'ex02_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 65 · lab03-ex01

**Thừa ký tự tab sau phần tử cuối mỗi dòng** · Có căn cứ code/log

NẾU lệnh in luôn thêm tab, kể cả ở cột cuối VÀ test ex01_0 ghi nhận output "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n" thay vì "1\t2\t3\n2\t3\t4\n3\t4\t5\n" THÌ gợi ý: Thừa ký tự tab sau phần tử cuối mỗi dòng.

Các con số và thứ tự đều khớp log, nhưng mỗi dòng có thêm tab ngay trước xuống dòng.

Giảng lại / kiểm tra: Ở cột cuối chỉ xuống dòng; dùng tab cho các cột còn lại.

Dòng: [17, 20]; test: ['ex01_0', 'ex01_1', 'ex01_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 66 · lab02-ex03

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex03_0 ghi nhận output "yes" thay vì "yes\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [9, 11]; test: ['ex03_0', 'ex03_1', 'ex03_2', 'ex03_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 67 · lab04-ex07

**Bỏ qua ký tự vừa dịch sang sau khi xóa** · Có căn cứ code/log

NẾU sau khi dịch trái chuỗi, chỉ số i vẫn tăng ngay VÀ test ex07_1 ghi nhận output "d\n" thay vì "\n" THÌ gợi ý: Bỏ qua ký tự vừa dịch sang sau khi xóa.

Nếu có hai ký tự cần xóa liền nhau, ký tự thứ hai dịch vào vị trí i nhưng không được xét lại. Log ddd còn d, nhiều a còn khoảng một nửa.

Giảng lại / kiểm tra: Giữ nguyên i sau khi xóa hoặc dùng hai chỉ số đọc/ghi.

Dòng: [12, 13, 14, 15]; test: ['ex07_1', 'ex07_3', 'ex07_4'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 68 · lab04-ex02

**Dùng chỉ số và điều kiện lặp chưa khởi tạo** · Có căn cứ code/log

NẾU i và l được đọc trước khi có giá trị ban đầu VÀ test ex02_0 ghi nhận output "" thay vì "***\n **\n  *\n" THÌ gợi ý: Dùng chỉ số và điều kiện lặp chưa khởi tạo.

i dùng làm chỉ số tab khi nhập, còn l dùng ngay trong điều kiện while. Không có phép gán ban đầu cho hai biến này; không thể xem output rỗng là một kết quả xác định của thuật toán.

Giảng lại / kiểm tra: Khởi tạo i và l trước lần dùng đầu tiên; kiểm tra giới hạn mảng.

Dòng: [9, 15, 16, 20, 21]; test: ['ex02_0', 'ex02_1', 'ex02_2'].

Có sử dụng giá trị chưa khởi tạo. Log rỗng không đủ xác định chương trình crash hay bỏ qua vòng lặp.

## Bài 69 · lab02-ex10

**Dừng theo chữ số 0 và cộng vào biến chưa khởi tạo** · Nhiều lỗi cùng xuất hiện

NẾU điều kiện while kiểm tra dig != 0, còn soma chưa được gán 0 VÀ test ex10_3 ghi nhận output "0\n0\n" thay vì "2\n1\n" THÌ gợi ý: Dừng theo chữ số 0 và cộng vào biến chưa khởi tạo.

Input 10 có chữ số cuối là 0 nên vòng không chạy, bỏ luôn chữ số 1 phía trước. Giá trị soma khi in cũng không được bảo đảm.

Giảng lại / kiểm tra: Khởi tạo tổng, lặp theo phần số còn lại thay vì giá trị chữ số vừa lấy.

Dòng: [6, 10, 13, 15, 17, 18]; test: ['ex10_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 70 · lab04-ex08

**Chưa triển khai phần xử lý và in kết quả** · Có căn cứ code/log

NẾU main chỉ kết thúc bằng return, không có phần giải bài VÀ test ex08_0 ghi nhận output "" thay vì "1\n" THÌ gợi ý: Chưa triển khai phần xử lý và in kết quả.

Code hiện là khung chưa hoàn thiện; các log đều rỗng. Không có đủ thông tin để gán một hiểu lầm thuật toán cụ thể.

Giảng lại / kiểm tra: Viết các bước xử lý đầu vào rồi bổ sung tính toán và output.

Dòng: [10]; test: ['ex08_0', 'ex08_1', 'ex08_2', 'ex08_3', 'ex08_4', 'ex08_5'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 71 · lab04-ex01

**Thừa khoảng trắng cuối dòng** · Có căn cứ code/log

NẾU code in dấu cách sau phần tử cuối hoặc đệm thêm chỗ trống bên phải VÀ test ex01_0 ghi nhận output "*  \n** \n***\n" thay vì "*\n**\n***\n" THÌ gợi ý: Thừa khoảng trắng cuối dòng.

So sánh từng dòng cho thấy phần nội dung khớp oracle, nhưng còn khoảng trắng trước ký tự xuống dòng. Đây là sai khác trình bày ở các test đã có.

Giảng lại / kiểm tra: Chỉ in dấu phân cách giữa hai phần tử; bỏ phần đệm cuối dòng nếu oracle không yêu cầu.

Dòng: [23, 24]; test: ['ex01_0', 'ex01_1', 'ex01_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 72 · lab03-ex04

**In chữ O thay số 0 và không chốt số cuối tại EOF** · Nhiều lỗi cùng xuất hiện

NẾU nhánh ZERO in O, còn sau vòng đọc không xử lý trạng thái ZERO VÀ test ex04_3 ghi nhận output "101\n" thay vì "101\n0" THÌ gợi ý: In chữ O thay số 0 và không chốt số cuối tại EOF.

Log có O giữa các số và mất nhóm toàn zero ở cuối input. Đây là hai lỗi độc lập.

Giảng lại / kiểm tra: Sửa ký tự in thành 0 và chốt trạng thái ZERO khi gặp EOF.

Dòng: [31, 32, 33, 40, 43]; test: ['ex04_3', 'ex04_4', 'ex04_5', 'ex04_6', 'ex04_8'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 73 · lab02-ex03

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex03_0 ghi nhận output "yes" thay vì "yes\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [10, 14]; test: ['ex03_0', 'ex03_1', 'ex03_2', 'ex03_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 74 · lab02-ex09

**Chưa đệm số 0 để in thời gian đủ hai chữ số** · Có căn cứ code/log

NẾU printf dùng %d cho giờ, phút và giây VÀ test ex09_0 ghi nhận output "0:1:0\n" thay vì "00:01:00\n" THÌ gợi ý: Chưa đệm số 0 để in thời gian đủ hai chữ số.

Log cho các thành phần thời gian đúng giá trị, nhưng 0:1:0 khác mẫu 00:01:00.

Giảng lại / kiểm tra: Dùng %02d cho từng thành phần thời gian.

Dòng: [14]; test: ['ex09_0', 'ex09_1', 'ex09_2', 'ex09_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 75 · lab02-ex01

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex01_0 ghi nhận output "3" thay vì "3\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [15, 19, 26, 30]; test: ['ex01_0', 'ex01_1', 'ex01_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 76 · lab04-ex03

**Vẽ các hàng biểu đồ ngược thứ tự** · Có căn cứ code/log

NẾU mức j đi từ 1 lên max thay vì từ max xuống 1 VÀ test ex03_0 ghi nhận output "***\n **\n  *\n" thay vì "  *\n **\n***\n" THÌ gợi ý: Vẽ các hàng biểu đồ ngược thứ tự.

Các hàng xuất hiện theo thứ tự đảo ngược oracle: hàng đầy sao ở đầu thay vì ở đáy.

Giảng lại / kiểm tra: Duyệt mức cao giảm dần khi cần vẽ từ đỉnh xuống.

Dòng: [23, 27, 29]; test: ['ex03_0', 'ex03_1', 'ex03_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 77 · lab04-ex01

**In lại các số thay vì vẽ số lượng dấu sao** · Có căn cứ code/log

NẾU vòng xuất chỉ printf từng vec[i] VÀ test ex01_0 ghi nhận output "1 2 3 " thay vì "*\n**\n***\n" THÌ gợi ý: In lại các số thay vì vẽ số lượng dấu sao.

Test cần mỗi giá trị thành một hàng dấu sao, nhưng code in trực tiếp dãy số. Có thể phần vẽ còn chưa viết.

Giảng lại / kiểm tra: Thêm vòng lặp cho từng hàng và in đúng số sao tương ứng.

Dòng: [21, 23]; test: ['ex01_0', 'ex01_1', 'ex01_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 78 · lab03-ex01

**Không cộng độ lệch theo hàng khi in bảng số** · Có căn cứ code/log

NẾU mỗi hàng đều in lại j từ 1 tới N VÀ test ex01_0 ghi nhận output "1\t2\t3\n1\t2\t3\n1\t2\t3\n" thay vì "1\t2\t3\n2\t3\t4\n3\t4\t5\n" THÌ gợi ý: Không cộng độ lệch theo hàng khi in bảng số.

Log lặp hàng 1,2,3 thay vì tăng điểm bắt đầu ở các hàng sau.

Giảng lại / kiểm tra: In i+j với i bắt đầu từ 0, giữ đúng dấu phân cách.

Dòng: [9, 10, 11, 12, 14]; test: ['ex01_0', 'ex01_1', 'ex01_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 79 · lab02-ex09

**Chưa đệm số 0 để in thời gian đủ hai chữ số** · Có căn cứ code/log

NẾU printf dùng %d cho giờ, phút và giây VÀ test ex09_0 ghi nhận output "0:1:0\n" thay vì "00:01:00\n" THÌ gợi ý: Chưa đệm số 0 để in thời gian đủ hai chữ số.

Log cho các thành phần thời gian đúng giá trị, nhưng 0:1:0 khác mẫu 00:01:00.

Giảng lại / kiểm tra: Dùng %02d cho từng thành phần thời gian.

Dòng: [14]; test: ['ex09_0', 'ex09_1', 'ex09_2', 'ex09_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 80 · lab02-ex01

**So với số đầu thay vì giá trị lớn nhất hiện tại** · Nhiều lỗi cùng xuất hiện

NẾU điều kiện num >= num1 dùng mốc cố định dù maior đã thay đổi VÀ test ex01_0 ghi nhận output "Escreva um numero inteiro:Escreva um numero inteiro:Escreva um numero inteiro:3\n" thay vì "3\n" THÌ gợi ý: So với số đầu thay vì giá trị lớn nhất hiện tại.

Với −1,3,1, sau khi maior là 3 thì 1 vẫn lớn hơn −1 nên ghi đè maior thành 1. Output còn có lời nhắc.

Giảng lại / kiểm tra: So với maior mỗi lần cập nhật và bỏ lời nhắc stdout.

Dòng: [6, 11, 13, 15]; test: ['ex01_0', 'ex01_1', 'ex01_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 81 · lab04-ex04

**Dùng chuỗi chưa khởi tạo khi scanf thất bại ở input rỗng** · Có căn cứ code/log

NẾU scanf %s không được kiểm tra trước khi gọi strlen hoặc kiểm tra đối xứng VÀ test ex04_3 ghi nhận output "no\n" thay vì "yes\n" THÌ gợi ý: Dùng chuỗi chưa khởi tạo khi scanf thất bại ở input rỗng.

Input rỗng không cung cấp token cho scanf; mảng ký tự chưa có chuỗi hợp lệ nhưng vẫn bị sử dụng. Log no chỉ là quan sát của lần chạy lịch sử.

Giảng lại / kiểm tra: Khởi tạo chuỗi rỗng và xử lý giá trị trả về của hàm đọc.

Dòng: [9, 17, 19, 20]; test: ['ex04_3'].

Chưa có trace thực thi; không kết luận output no là hành vi xác định khi đọc bộ nhớ chưa khởi tạo.

## Bài 82 · lab03-ex02

**Thừa khoảng trắng cuối dòng** · Có căn cứ code/log

NẾU code in dấu cách sau phần tử cuối hoặc đệm thêm chỗ trống bên phải VÀ test ex02_0 ghi nhận output "    1     \n  1 2 1   \n1 2 3 2 1 \n" thay vì "    1\n  1 2 1\n1 2 3 2 1\n" THÌ gợi ý: Thừa khoảng trắng cuối dòng.

So sánh từng dòng cho thấy phần nội dung khớp oracle, nhưng còn khoảng trắng trước ký tự xuống dòng. Đây là sai khác trình bày ở các test đã có.

Giảng lại / kiểm tra: Chỉ in dấu phân cách giữa hai phần tử; bỏ phần đệm cuối dòng nếu oracle không yêu cầu.

Dòng: [9, 11, 13, 15, 16]; test: ['ex02_0', 'ex02_1', 'ex02_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 83 · lab04-ex06

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex06_0 ghi nhận output "OLA ADEUS" thay vì "OLA ADEUS\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [19]; test: ['ex06_0', 'ex06_1', 'ex06_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 84 · lab04-ex06

**Đổi chữ đầu từ thành chữ thường thay vì đổi toàn chuỗi thành chữ hoa** · Có căn cứ code/log

NẾU hàm chỉ xét chữ hoa ở đầu từ và cộng 32 VÀ test ex06_0 ghi nhận output "oLA aDEUS\n" thay vì "OLA ADEUS\n" THÌ gợi ý: Đổi chữ đầu từ thành chữ thường thay vì đổi toàn chuỗi thành chữ hoa.

Oracle yêu cầu toàn bộ ký tự chữ thành chữ hoa. Code lại làm ngược chiều và chỉ tác động đầu từ.

Giảng lại / kiểm tra: Duyệt mọi ký tự thường a–z và đổi sang chữ hoa.

Dòng: [16, 20, 21, 23]; test: ['ex06_0', 'ex06_1', 'ex06_2', 'ex06_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 85 · lab03-ex03

**Thiếu dấu cách giữa các ký hiệu của hình chữ X** · Có căn cứ code/log

NẾU printf in từng ký hiệu liền nhau VÀ test ex03_0 ghi nhận output "*-*\n-*-\n*-*\n" thay vì "* - *\n- * -\n* - *\n" THÌ gợi ý: Thiếu dấu cách giữa các ký hiệu của hình chữ X.

Vị trí sao trong log tương ứng với oracle, nhưng các cột dính nhau thay vì cách một dấu cách.

Giảng lại / kiểm tra: Thêm dấu cách giữa cột, không thêm sau cột cuối.

Dòng: [9]; test: ['ex03_0', 'ex03_1', 'ex03_2', 'ex03_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 86 · lab03-ex07

**Chưa triển khai phần xử lý và in kết quả** · Có căn cứ code/log

NẾU main chỉ kết thúc bằng return, không có phần giải bài VÀ test ex07_0 ghi nhận output "" thay vì "9\n" THÌ gợi ý: Chưa triển khai phần xử lý và in kết quả.

Code hiện là khung chưa hoàn thiện; các log đều rỗng. Không có đủ thông tin để gán một hiểu lầm thuật toán cụ thể.

Giảng lại / kiểm tra: Viết các bước xử lý đầu vào rồi bổ sung tính toán và output.

Dòng: [10]; test: ['ex07_0', 'ex07_1', 'ex07_2', 'ex07_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 87 · lab03-ex06

**In thêm dữ liệu kiểm tra ngoài đáp án** · Có căn cứ code/log

NẾU code in chuỗi đầu vào, chỉ số, tổng trung gian hoặc độ dài bên cạnh kết quả VÀ test ex06_0 ghi nhận output "8\nno\n" thay vì "no\n" THÌ gợi ý: In thêm dữ liệu kiểm tra ngoài đáp án.

Log có những dòng phụ khớp với lệnh in kiểm tra trong code. Phần đáp án phía sau không làm cho toàn bộ output khớp oracle.

Giảng lại / kiểm tra: Bỏ lệnh in kiểm tra và chỉ giữ output đề yêu cầu.

Dòng: [12, 13]; test: ['ex06_0', 'ex06_1', 'ex06_2', 'ex06_3', 'ex06_4', 'ex06_5', 'ex06_6'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 88 · lab04-ex07

**Dùng sai chỉ số khi nén chuỗi để xóa ký tự** · Có căn cứ code/log

NẾU code kiểm tra s[i] nhưng sao chép s[i+delta], và duyệt tới VECMAX thay vì hết chuỗi VÀ test ex07_0 ghi nhận output "ol aeus\n" thay vì "ol deus\n" THÌ gợi ý: Dùng sai chỉ số khi nén chuỗi để xóa ký tự.

Ký tự được xét không còn là ký tự sẽ được chép nên nhiều ký tự cần xóa vẫn còn. Vòng lặp còn đọc ngoài phần chuỗi hợp lệ, thậm chí ngoài mảng khi i+delta quá lớn.

Giảng lại / kiểm tra: Dùng chỉ số đọc và ghi riêng; dừng tại ký tự kết thúc chuỗi.

Dòng: [32, 34, 36, 38]; test: ['ex07_0', 'ex07_1', 'ex07_3', 'ex07_4'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 89 · lab02-ex04

**Điều kiện sắp xếp chồng lấn làm in hai kết quả** · Có căn cứ code/log

NẾU các if độc lập có miền điều kiện giao nhau và thiếu quan hệ giữa n1 với n2 ở một nhánh VÀ test ex04_1 ghi nhận output "2 10 6\n2 6 10\n" thay vì "2 6 10\n" THÌ gợi ý: Điều kiện sắp xếp chồng lấn làm in hai kết quả.

Input 10,6,2 đồng thời đi qua nhánh in 2,10,6 và nhánh in 2,6,10. Dùng & ở đây không phải nguyên nhân chính vì hai vế đều là giá trị so sánh 0/1.

Giảng lại / kiểm tra: Thiết kế các trường hợp loại trừ nhau hoặc dùng thuật toán đổi chỗ ba số.

Dòng: [13, 14, 15, 16]; test: ['ex04_1', 'ex04_2', 'ex04_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 90 · lab03-ex02

**Thiếu dấu cách giữa số và sai bề rộng căn lề** · Có căn cứ code/log

NẾU code in các số liền nhau và chỉ dùng n−i dấu cách đầu dòng VÀ test ex02_0 ghi nhận output "  1\n 121\n12321\n" thay vì "    1\n  1 2 1\n1 2 3 2 1\n" THÌ gợi ý: Thiếu dấu cách giữa số và sai bề rộng căn lề.

Oracle dùng một dấu cách giữa các số và 2(n−i) khoảng trống bên trái. Log hiện bị co hẹp và các số dính nhau.

Giảng lại / kiểm tra: Tính độ rộng theo cả ký tự số lẫn dấu phân cách.

Dòng: [11, 12, 15, 18]; test: ['ex02_0', 'ex02_1', 'ex02_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 91 · lab02-ex07

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex07_0 ghi nhận output "4" thay vì "4\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [18]; test: ['ex07_0', 'ex07_1', 'ex07_2', 'ex07_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 92 · lab02-ex06

**Dùng else if khiến min không được cập nhật khi max thay đổi** · Nhiều lỗi cùng xuất hiện

NẾU kiểm tra min nằm ở nhánh else của kiểm tra max VÀ test ex06_0 ghi nhận output "min:340282346638528859811704183484516925440.000000 max:3.000000" thay vì "min: 1.500000, max: 3.000000\n" THÌ gợi ý: Dùng else if khiến min không được cập nhật khi max thay đổi.

Với dãy tăng 1.5,2.7,3, mỗi phần tử cập nhật max nên min vẫn giữ FLT_MAX. Mẫu output còn thiếu dấu cách, dấu phẩy và newline.

Giảng lại / kiểm tra: Khởi tạo min/max từ phần tử đầu hoặc kiểm tra hai điều kiện độc lập; sửa mẫu in.

Dòng: [9, 19, 20, 22, 23, 27]; test: ['ex06_0', 'ex06_1', 'ex06_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 93 · lab04-ex08

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex08_0 ghi nhận output "1" thay vì "1\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [16, 19]; test: ['ex08_0', 'ex08_1', 'ex08_2', 'ex08_3', 'ex08_4', 'ex08_5'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 94 · lab04-ex06

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex06_0 ghi nhận output "OLA ADEUS" thay vì "OLA ADEUS\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [10, 13]; test: ['ex06_0', 'ex06_1', 'ex06_2', 'ex06_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 95 · lab02-ex09

**Chưa đệm số 0 để in thời gian đủ hai chữ số** · Có căn cứ code/log

NẾU printf dùng %d cho giờ, phút và giây VÀ test ex09_0 ghi nhận output "0:1:0\n" thay vì "00:01:00\n" THÌ gợi ý: Chưa đệm số 0 để in thời gian đủ hai chữ số.

Log cho các thành phần thời gian đúng giá trị, nhưng 0:1:0 khác mẫu 00:01:00.

Giảng lại / kiểm tra: Dùng %02d cho từng thành phần thời gian.

Dòng: [13]; test: ['ex09_0', 'ex09_1', 'ex09_2', 'ex09_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 96 · lab02-ex01

**Thiếu newline; cách tìm max theo ký tự cần kiểm tra thêm** · Cần kiểm tra thêm

NẾU code lấy ký tự có mã lớn nhất rồi putchar một lần VÀ test ex01_0 ghi nhận output "3" thay vì "3\n" THÌ gợi ý: Thiếu newline; cách tìm max theo ký tự cần kiểm tra thêm.

Các log hiện có chỉ chứng minh thiếu newline vì kết quả số đều tình cờ là một chữ số. Cách đọc này không ghép số nhiều chữ số và không xử lý dấu như số nguyên.

Giảng lại / kiểm tra: Sửa newline, đồng thời kiểm tra đặc tả và thử input nhiều chữ số trước khi xác nhận thuật toán.

Dòng: [5, 7, 8, 9, 11]; test: ['ex01_0', 'ex01_1', 'ex01_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 97 · lab04-ex08

**Kiểm tra phần tử mảng trước khi nhập và dùng int cho số quá dài** · Nhiều lỗi cùng xuất hiện

NẾU điều kiện for đọc c[i] chưa khởi tạo rồi mới scanf VÀ test ex08_0 ghi nhận output "0" thay vì "1\n" THÌ gợi ý: Kiểm tra phần tử mảng trước khi nhập và dùng int cho số quá dài.

Vòng nhập có thể không chạy hoặc đi sai vì điều kiện phụ thuộc dữ liệu chưa có. Các số 22 chữ số trong test cũng không phù hợp cách nhập bằng %d.

Giảng lại / kiểm tra: Đọc hai chuỗi số có giới hạn độ dài rồi so sánh sau chuẩn hóa.

Dòng: [5, 6, 7, 8, 9, 13]; test: ['ex08_0', 'ex08_1', 'ex08_2', 'ex08_3', 'ex08_4', 'ex08_5'].

Output 0 trong log không làm cho việc đọc giá trị chưa khởi tạo trở thành xác định.

## Bài 98 · lab02-ex01

**Chọn số thứ hai rồi bỏ qua số thứ ba khi tìm max** · Nhiều lỗi cùng xuất hiện

NẾU nhánh segundo > primeiro kết thúc việc chọn mà không so tiếp terceiro VÀ test ex01_0 ghi nhận output "Insira três números O maior número é 2 \n" thay vì "3\n" THÌ gợi ý: Chọn số thứ hai rồi bỏ qua số thứ ba khi tìm max.

Input 1,2,3 nhận 2 vì điều kiện đầu đúng. Code còn in lời nhắc và nhãn ngoài đáp án.

Giảng lại / kiểm tra: Cập nhật max lần lượt với cả ba giá trị rồi in riêng kết quả.

Dòng: [9, 12, 13, 15, 21]; test: ['ex01_0', 'ex01_1', 'ex01_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 99 · lab03-ex01

**Thừa ký tự tab sau phần tử cuối mỗi dòng** · Có căn cứ code/log

NẾU lệnh in luôn thêm tab, kể cả ở cột cuối VÀ test ex01_0 ghi nhận output "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n" thay vì "1\t2\t3\n2\t3\t4\n3\t4\t5\n" THÌ gợi ý: Thừa ký tự tab sau phần tử cuối mỗi dòng.

Các con số và thứ tự đều khớp log, nhưng mỗi dòng có thêm tab ngay trước xuống dòng.

Giảng lại / kiểm tra: Ở cột cuối chỉ xuống dòng; dùng tab cho các cột còn lại.

Dòng: [16, 22]; test: ['ex01_0', 'ex01_1', 'ex01_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 100 · lab03-ex03

**Thừa khoảng trắng cuối dòng** · Có căn cứ code/log

NẾU code in dấu cách sau phần tử cuối hoặc đệm thêm chỗ trống bên phải VÀ test ex03_0 ghi nhận output "* - * \n- * - \n* - * \n" thay vì "* - *\n- * -\n* - *\n" THÌ gợi ý: Thừa khoảng trắng cuối dòng.

So sánh từng dòng cho thấy phần nội dung khớp oracle, nhưng còn khoảng trắng trước ký tự xuống dòng. Đây là sai khác trình bày ở các test đã có.

Giảng lại / kiểm tra: Chỉ in dấu phân cách giữa hai phần tử; bỏ phần đệm cuối dòng nếu oracle không yêu cầu.

Dòng: [8, 9]; test: ['ex03_0', 'ex03_1', 'ex03_2', 'ex03_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 101 · lab02-ex05

**Tăng biến trước khi in làm mất số 1, đồng thời thiếu dấu phân cách** · Nhiều lỗi cùng xuất hiện

NẾU i bắt đầu ở 1 nhưng tăng lên trước printf VÀ test ex05_0 ghi nhận output "" thay vì "1\n" THÌ gợi ý: Tăng biến trước khi in làm mất số 1, đồng thời thiếu dấu phân cách.

Input 1 không in gì; input 3 in 23 thay vì ba dòng 1, 2, 3. Bài 101 còn gọi scanf thừa trong vòng dù input chỉ có một giới hạn.

Giảng lại / kiểm tra: In từ 1 đến n, mỗi số một dòng, không đọc lại giới hạn trong vòng.

Dòng: [8, 9, 10, 11]; test: ['ex05_0', 'ex05_1', 'ex05_2', 'ex05_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 102 · lab04-ex07

**Đọc chuỗi bằng %s vào một biến char đơn** · Có căn cứ code/log

NẾU scanf dùng %s nhưng địa chỉ nhận là &c của một char VÀ test ex07_0 ghi nhận output "\n" thay vì "ol deus\n" THÌ gợi ý: Đọc chuỗi bằng %s vào một biến char đơn.

Ngay cả input một ký tự cũng cần thêm ô cho ký tự kết thúc chuỗi. Lời gọi ghi vượt vùng của c, có thể làm hỏng dữ liệu lân cận; log chỉ còn newline.

Giảng lại / kiểm tra: Dùng định dạng đọc một ký tự phù hợp, và xử lý newline còn trong chuỗi fgets.

Dòng: [23, 24, 25, 27]; test: ['ex07_0', 'ex07_2', 'ex07_4'].

Có ghi vượt bộ nhớ; không kết luận chắc ô nào bị ghi đè chỉ từ log.

## Bài 103 · lab04-ex03

**Code thực hiện tác vụ khác với oracle của bài** · Cần kiểm tra thêm

NẾU code xử lý palindrome, phân loại tam giác, min/max hoặc vẽ kim tự tháp thay vì tác vụ thể hiện trong test VÀ test ex03_0 ghi nhận output "yes\n" thay vì "  *\n **\n***\n" THÌ gợi ý: Code thực hiện tác vụ khác với oracle của bài.

Output và cấu trúc code cho thấy một tác vụ khác hẳn bộ test: đây có thể là nộp nhầm bài hoặc ánh xạ dữ liệu sai. Gói thiếu đề gốc nên chưa kết luận đó là lỗi kiến thức của người học.

Giảng lại / kiểm tra: Kiểm tra lại đề, mã bài và nguồn ghép test trước khi gán nhãn cơ chế.

Dòng: [19, 21]; test: ['ex03_0', 'ex03_1', 'ex03_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 104 · lab04-ex07

**Bỏ qua ký tự vừa dịch sang sau khi xóa** · Có căn cứ code/log

NẾU sau khi dịch trái chuỗi, chỉ số i vẫn tăng ngay VÀ test ex07_1 ghi nhận output "d\n" thay vì "\n" THÌ gợi ý: Bỏ qua ký tự vừa dịch sang sau khi xóa.

Nếu có hai ký tự cần xóa liền nhau, ký tự thứ hai dịch vào vị trí i nhưng không được xét lại. Log ddd còn d, nhiều a còn khoảng một nửa.

Giảng lại / kiểm tra: Giữ nguyên i sau khi xóa hoặc dùng hai chỉ số đọc/ghi.

Dòng: [39, 40, 42, 43, 50]; test: ['ex07_1', 'ex07_3', 'ex07_4'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 105 · lab03-ex03

**Bỏ phần đuôi và xuống dòng ở hàng giữa của hình kích thước lẻ** · Có căn cứ code/log

NẾU điều kiện loại hàng giữa khỏi cả khối in phía phải và kết thúc hàng VÀ test ex03_0 ghi nhận output "* - *\n- * * - *\n" thay vì "* - *\n- * -\n* - *\n" THÌ gợi ý: Bỏ phần đuôi và xuống dòng ở hàng giữa của hình kích thước lẻ.

Ở N lẻ, code in phần đầu hàng giữa nhưng bỏ các dấu gạch bên phải và newline. Hàng kế tiếp bị nối vào cùng dòng.

Giảng lại / kiểm tra: Xử lý riêng sao giữa nhưng vẫn in đủ phần bên phải và newline.

Dòng: [24, 26, 28, 31, 33, 39]; test: ['ex03_0', 'ex03_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 106 · lab02-ex09

**Đổi giây sang giờ bằng 360 thay vì 3600** · Nhiều lỗi cùng xuất hiện

NẾU giờ và phần dư đều chia cho 360 VÀ test ex09_0 ghi nhận output "0:1:0\n" thay vì "00:01:00\n" THÌ gợi ý: Đổi giây sang giờ bằng 360 thay vì 3600.

Input 3600 bị tính thành 10 giờ. Ngoài sai đơn vị, output chưa đệm số 0 cho đủ hai chữ số.

Giảng lại / kiểm tra: Dùng 3600 giây cho một giờ và %02d khi in.

Dòng: [8, 9, 13]; test: ['ex09_0', 'ex09_1', 'ex09_2', 'ex09_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 107 · lab04-ex01

**In thừa lời nhắc nhập dữ liệu** · Có căn cứ code/log

NẾU code in lời nhắc hoặc nhãn mô tả ngoài kết quả VÀ test ex01_0 ghi nhận output "Introduza um inteiro positivo menor que 100.\nIntroduza um inteiro positivo. 1/3\nIntroduza um inteiro positivo. 2/3\nIntroduza um inteiro positivo. 3/3\n*\n**\n***\n" thay vì "*\n**\n***\n" THÌ gợi ý: In thừa lời nhắc nhập dữ liệu.

Các dòng hướng dẫn nhập xuất hiện trong stdout nhưng không thuộc đáp án. Cần phân biệt giao diện tương tác với output nộp cho hệ thống chấm.

Giảng lại / kiểm tra: Bỏ lời nhắc khỏi stdout nộp bài; đối chiếu lại các test.

Dòng: [7, 10, 15, 16]; test: ['ex01_0', 'ex01_1', 'ex01_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 108 · lab04-ex02

**Chèn dấu cách giữa các cột sao không có trong oracle** · Có căn cứ code/log

NẾU mỗi cột lại được nối bằng một dấu cách phụ VÀ test ex02_0 ghi nhận output "* * *\n  * *\n    *\n" thay vì "***\n **\n  *\n" THÌ gợi ý: Chèn dấu cách giữa các cột sao không có trong oracle.

Biểu đồ được giãn ngang, kể cả các cột rỗng vốn đã là một dấu cách. Oracle chỉ cần ký tự của từng cột đứng sát nhau.

Giảng lại / kiểm tra: Bỏ dấu cách phân cách cột, giữ một newline sau mỗi hàng.

Dòng: [23, 24]; test: ['ex02_0', 'ex02_1', 'ex02_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 109 · lab03-ex02

**Thừa khoảng trắng cuối dòng** · Có căn cứ code/log

NẾU code in dấu cách sau phần tử cuối hoặc đệm thêm chỗ trống bên phải VÀ test ex02_0 ghi nhận output "    1 \n  1 2 1 \n1 2 3 2 1 \n" thay vì "    1\n  1 2 1\n1 2 3 2 1\n" THÌ gợi ý: Thừa khoảng trắng cuối dòng.

So sánh từng dòng cho thấy phần nội dung khớp oracle, nhưng còn khoảng trắng trước ký tự xuống dòng. Đây là sai khác trình bày ở các test đã có.

Giảng lại / kiểm tra: Chỉ in dấu phân cách giữa hai phần tử; bỏ phần đệm cuối dòng nếu oracle không yêu cầu.

Dòng: [13, 14, 19, 20, 25, 26, 28]; test: ['ex02_0', 'ex02_1', 'ex02_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 110 · lab03-ex05

**Chưa triển khai phần xử lý và in kết quả** · Có căn cứ code/log

NẾU main chỉ kết thúc bằng return, không có phần giải bài VÀ test ex05_0 ghi nhận output "" thay vì "foo\n" THÌ gợi ý: Chưa triển khai phần xử lý và in kết quả.

Code hiện là khung chưa hoàn thiện; các log đều rỗng. Không có đủ thông tin để gán một hiểu lầm thuật toán cụ thể.

Giảng lại / kiểm tra: Viết các bước xử lý đầu vào rồi bổ sung tính toán và output.

Dòng: [10]; test: ['ex05_0', 'ex05_1', 'ex05_2', 'ex05_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 111 · lab04-ex04

**Dùng chuỗi chưa khởi tạo khi scanf thất bại ở input rỗng** · Có căn cứ code/log

NẾU scanf %s không được kiểm tra trước khi gọi strlen hoặc kiểm tra đối xứng VÀ test ex04_3 ghi nhận output "no\n" thay vì "yes\n" THÌ gợi ý: Dùng chuỗi chưa khởi tạo khi scanf thất bại ở input rỗng.

Input rỗng không cung cấp token cho scanf; mảng ký tự chưa có chuỗi hợp lệ nhưng vẫn bị sử dụng. Log no chỉ là quan sát của lần chạy lịch sử.

Giảng lại / kiểm tra: Khởi tạo chuỗi rỗng và xử lý giá trị trả về của hàm đọc.

Dòng: [9, 17, 18, 20]; test: ['ex04_3'].

Chưa có trace thực thi; không kết luận output no là hành vi xác định khi đọc bộ nhớ chưa khởi tạo.

## Bài 112 · lab02-ex02

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex02_0 ghi nhận output "1\n2" thay vì "1\n2\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [11, 15]; test: ['ex02_0', 'ex02_1', 'ex02_2', 'ex02_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 113 · lab02-ex07

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex07_0 ghi nhận output "4" thay vì "4\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [19]; test: ['ex07_0', 'ex07_1', 'ex07_2', 'ex07_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 114 · lab02-ex02

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex02_0 ghi nhận output "1\n2" thay vì "1\n2\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [13, 16]; test: ['ex02_0', 'ex02_1', 'ex02_2', 'ex02_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 115 · lab04-ex03

**Dùng số cột thay chiều cao lớn nhất để tính mức hàng** · Có căn cứ code/log

NẾU điều kiện dựa vào n − i − 1 thay vì max − i VÀ test ex03_1 ghi nhận output " **\n***\n***\n***\n***\n***\n***\n***\n" thay vì "  *\n  *\n **\n **\n **\n **\n***\n***\n" THÌ gợi ý: Dùng số cột thay chiều cao lớn nhất để tính mức hàng.

Khi n khác max, ngưỡng in sao lệch hẳn. Test có 3 cột, max 8 bị in đầy sao quá sớm; test có 9 cột, max 5 có nhiều hàng trống.

Giảng lại / kiểm tra: Tách số cột n khỏi mức cao đang vẽ.

Dòng: [17, 23]; test: ['ex03_1', 'ex03_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 116 · lab04-ex04

**Quét quá ký tự kết thúc khi tìm độ dài chuỗi** · Nhiều lỗi cùng xuất hiện

NẾU vòng tìm m đi đến MAX và không dừng ở ký tự kết thúc đầu tiên VÀ test ex04_1 ghi nhận output "no\n" thay vì "yes\n" THÌ gợi ý: Quét quá ký tự kết thúc khi tìm độ dài chuỗi.

m có thể bị ghi lại bởi vùng chưa khởi tạo sau chuỗi, khiến chỉ số đối xứng sai. Vòng kiểm tra còn bỏ sót cặp giữa khi dùng i < m/2.

Giảng lại / kiểm tra: Dừng ngay tại kết thúc chuỗi hoặc dùng strlen; duyệt đúng các cặp đối xứng.

Dòng: [12, 13, 14, 16, 17]; test: ['ex04_1', 'ex04_2', 'ex04_3', 'ex04_4'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 117 · lab02-ex08

**In sáu chữ số thập phân thay vì hai** · Có căn cứ code/log

NẾU printf dùng %f không chỉ định độ chính xác VÀ test ex08_0 ghi nhận output "3.000000\n" thay vì "3.00\n" THÌ gợi ý: In sáu chữ số thập phân thay vì hai.

Giá trị trung bình trong log phù hợp, nhưng output 3.000000 khác mẫu 3.00.

Giảng lại / kiểm tra: Dùng %.2f kèm newline.

Dòng: [15]; test: ['ex08_0', 'ex08_1', 'ex08_2', 'ex08_3', 'ex08_4'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 118 · lab02-ex08

**Biến tổng chưa khởi tạo và định dạng thập phân chưa đúng** · Nhiều lỗi cùng xuất hiện

NẾU soma được cộng dồn trước khi gán giá trị ban đầu; printf dùng %f VÀ test ex08_0 ghi nhận output "3.000000\n" thay vì "3.00\n" THÌ gợi ý: Biến tổng chưa khởi tạo và định dạng thập phân chưa đúng.

Log tình cờ cho phần số đúng nhưng có sáu chữ số thập phân. Code vẫn đọc soma chưa khởi tạo, nên không thể xác nhận thuật toán ổn định từ các kết quả đó.

Giảng lại / kiểm tra: Khởi tạo soma = 0 và dùng %.2f.

Dòng: [7, 12, 14]; test: ['ex08_0', 'ex08_1', 'ex08_2', 'ex08_3', 'ex08_4'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 119 · lab02-ex10

**Giảm số từng đơn vị thay vì tách từng chữ số** · Nhiều lỗi cùng xuất hiện

NẾU vòng lặp --n và cộng n/10, đồng thời i chưa khởi tạo VÀ test ex10_0 ghi nhận output "12\n3\n" thay vì "2\n3\n" THÌ gợi ý: Giảm số từng đơn vị thay vì tách từng chữ số.

Code chạy theo giá trị của số, không theo số chữ số. Input 123 cho số đếm 123 và tổng 708 trong log.

Giảng lại / kiểm tra: Khởi tạo biến đếm; lấy n%10 rồi chia n cho 10 mỗi lượt.

Dòng: [5, 7, 8, 9, 10]; test: ['ex10_0', 'ex10_1', 'ex10_2', 'ex10_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 120 · lab02-ex06

**Chỉ đọc ba giá trị dù n có thể lớn hơn ba** · Có căn cứ code/log

NẾU scanf nhận n và đúng ba số thực rồi chỉ sắp xếp ba số đó VÀ test ex06_1 ghi nhận output "min: 1.000000, max: 6.800000\n" thay vì "min: 0.000000, max: 6.800000\n" THÌ gợi ý: Chỉ đọc ba giá trị dù n có thể lớn hơn ba.

Với bốn số 6.8,2,1,0, giá trị cuối 0 không được đọc nên min thành 1.

Giảng lại / kiểm tra: Duyệt đủ n số và cập nhật min/max theo từng lần nhập.

Dòng: [7, 8, 14, 20]; test: ['ex06_1'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 121 · lab02-ex04

**Code thực hiện tác vụ khác với oracle của bài** · Cần kiểm tra thêm

NẾU code xử lý palindrome, phân loại tam giác, min/max hoặc vẽ kim tự tháp thay vì tác vụ thể hiện trong test VÀ test ex04_0 ghi nhận output "min: 1.000000, max: 2.000000\n" thay vì "1 2 6\n" THÌ gợi ý: Code thực hiện tác vụ khác với oracle của bài.

Output và cấu trúc code cho thấy một tác vụ khác hẳn bộ test: đây có thể là nộp nhầm bài hoặc ánh xạ dữ liệu sai. Gói thiếu đề gốc nên chưa kết luận đó là lỗi kiến thức của người học.

Giảng lại / kiểm tra: Kiểm tra lại đề, mã bài và nguồn ghép test trước khi gán nhãn cơ chế.

Dòng: [25]; test: ['ex04_0', 'ex04_1', 'ex04_2', 'ex04_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 122 · lab03-ex05

**Một ký tự làm đổi trạng thái nhiều lần trong các if độc lập** · Có căn cứ code/log

NẾU các if sau tiếp tục xét estado vừa bị if trước thay đổi VÀ test ex05_0 ghi nhận output "\nfoo\n" thay vì "foo\n" THÌ gợi ý: Một ký tự làm đổi trạng thái nhiều lần trong các if độc lập.

Dấu nháy mở đặt estado=1 rồi ngay lập tức thỏa nhánh đóng, sinh newline đầu. Việc in không được giới hạn rõ bởi trạng thái trong chuỗi; xử lý escape cũng bị tác động.

Giảng lại / kiểm tra: Mỗi ký tự chỉ thực hiện một chuyển trạng thái; tách nhánh bằng else if hoặc switch.

Dòng: [8, 11, 14, 17, 19, 21, 22]; test: ['ex05_0', 'ex05_1', 'ex05_2', 'ex05_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 123 · lab03-ex02

**Thừa khoảng trắng cuối dòng** · Có căn cứ code/log

NẾU code in dấu cách sau phần tử cuối hoặc đệm thêm chỗ trống bên phải VÀ test ex02_0 ghi nhận output "    1 \n  1 2 1 \n1 2 3 2 1 \n" thay vì "    1\n  1 2 1\n1 2 3 2 1\n" THÌ gợi ý: Thừa khoảng trắng cuối dòng.

So sánh từng dòng cho thấy phần nội dung khớp oracle, nhưng còn khoảng trắng trước ký tự xuống dòng. Đây là sai khác trình bày ở các test đã có.

Giảng lại / kiểm tra: Chỉ in dấu phân cách giữa hai phần tử; bỏ phần đệm cuối dòng nếu oracle không yêu cầu.

Dòng: [10, 15, 20, 23]; test: ['ex02_0', 'ex02_1', 'ex02_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 124 · lab03-ex02

**Thừa khoảng trắng cuối dòng** · Có căn cứ code/log

NẾU code in dấu cách sau phần tử cuối hoặc đệm thêm chỗ trống bên phải VÀ test ex02_0 ghi nhận output "    1 \n  1 2 1 \n1 2 3 2 1 \n" thay vì "    1\n  1 2 1\n1 2 3 2 1\n" THÌ gợi ý: Thừa khoảng trắng cuối dòng.

So sánh từng dòng cho thấy phần nội dung khớp oracle, nhưng còn khoảng trắng trước ký tự xuống dòng. Đây là sai khác trình bày ở các test đã có.

Giảng lại / kiểm tra: Chỉ in dấu phân cách giữa hai phần tử; bỏ phần đệm cuối dòng nếu oracle không yêu cầu.

Dòng: [10, 14, 17, 19]; test: ['ex02_0', 'ex02_1', 'ex02_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 125 · lab02-ex04

**Tính sai phần tử giữa và dùng tab thay dấu cách** · Nhiều lỗi cùng xuất hiện

NẾU meio được gán min(m,n3) mà không xét giá trị nhỏ còn lại VÀ test ex04_0 ghi nhận output "1\t2\t6\n" thay vì "1 2 6\n" THÌ gợi ý: Tính sai phần tử giữa và dùng tab thay dấu cách.

Với 10,6,2, code cho phần tử giữa là 2 thay vì 6. Output còn dùng tab trong khi oracle yêu cầu dấu cách.

Giảng lại / kiểm tra: Sắp xếp ba số bằng các phép đổi chỗ rồi in bằng dấu cách.

Dòng: [8, 9, 10, 11, 12, 15]; test: ['ex04_0', 'ex04_1', 'ex04_2', 'ex04_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 126 · lab03-ex06

**Chỉ in khi gặp dấu phân cách, quên xử lý EOF** · Có căn cứ code/log

NẾU printf nằm trong nhánh gặp space, tab hoặc newline VÀ test ex06_0 ghi nhận output "" thay vì "no\n" THÌ gợi ý: Chỉ in khi gặp dấu phân cách, quên xử lý EOF.

Các input kết thúc ngay sau chữ số, không có ký tự phân cách. Code thoát vòng ở EOF mà chưa in kết luận.

Giảng lại / kiểm tra: Chốt kết quả một lần khi kết thúc input.

Dòng: [7, 13, 15, 16, 18]; test: ['ex06_0', 'ex06_1', 'ex06_2', 'ex06_3', 'ex06_4', 'ex06_5', 'ex06_6'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 127 · lab03-ex05

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex05_0 ghi nhận output "foo" thay vì "foo\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [10, 15, 22]; test: ['ex05_0', 'ex05_1', 'ex05_2', 'ex05_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 128 · lab03-ex01

**Thừa ký tự tab sau phần tử cuối mỗi dòng** · Có căn cứ code/log

NẾU lệnh in luôn thêm tab, kể cả ở cột cuối VÀ test ex01_0 ghi nhận output "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n" thay vì "1\t2\t3\n2\t3\t4\n3\t4\t5\n" THÌ gợi ý: Thừa ký tự tab sau phần tử cuối mỗi dòng.

Các con số và thứ tự đều khớp log, nhưng mỗi dòng có thêm tab ngay trước xuống dòng.

Giảng lại / kiểm tra: Ở cột cuối chỉ xuống dòng; dùng tab cho các cột còn lại.

Dòng: [18, 19]; test: ['ex01_0', 'ex01_1', 'ex01_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 129 · lab04-ex05

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex05_0 ghi nhận output "ola adeus" thay vì "ola adeus\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [14]; test: ['ex05_0', 'ex05_1', 'ex05_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 130 · lab02-ex03

**Sai chữ hoa/chữ thường trong yes/no** · Có căn cứ code/log

NẾU chuỗi thông báo dùng chữ hoa trong khi oracle dùng chữ thường VÀ test ex03_0 ghi nhận output "Yes\n" thay vì "yes\n" THÌ gợi ý: Sai chữ hoa/chữ thường trong yes/no.

Phép kiểm tra chia hết cho kết luận tương ứng với log; khác biệt là YES/NO hoặc Yes/No thay cho yes/no.

Giảng lại / kiểm tra: Giữ phép kiểm tra và sửa đúng chuỗi thông báo.

Dòng: [8, 12]; test: ['ex03_0', 'ex03_1', 'ex03_2', 'ex03_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 131 · lab03-ex06

**Cộng mã ký tự thay vì giá trị chữ số** · Có căn cứ code/log

NẾU m cộng trực tiếp n lấy từ getchar VÀ test ex06_6 ghi nhận output "no\n" thay vì "yes\n" THÌ gợi ý: Cộng mã ký tự thay vì giá trị chữ số.

Mỗi ký tự số mang mã ký tự, không phải giá trị 0–9. Test nhiều chữ số 9 cho no dù tổng chữ số chia hết cho 9.

Giảng lại / kiểm tra: Với ký tự số hợp lệ, cộng n − 0 theo hằng ký tự; dùng int nhận getchar.

Dòng: [5, 8, 9, 12]; test: ['ex06_6'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 132 · lab04-ex04

**Tính sai độ dài, chỉ số đối xứng và điều kiện palindrome** · Nhiều lỗi cùng xuất hiện

NẾU len tăng hai lần, so sánh dùng s[len−i] và phép < VÀ test ex04_0 ghi nhận output "yes" thay vì "no\n" THÌ gợi ý: Tính sai độ dài, chỉ số đối xứng và điều kiện palindrome.

Code không kiểm tra hai ký tự đối xứng bằng nhau: vị trí đầu phải ghép với len−1, không phải len. Kết quả còn bị ghi đè từng lượt, is_palindrome không được khởi tạo và output thiếu newline.

Giảng lại / kiểm tra: Tính độ dài một lần, khởi tạo kết quả và dừng khi một cặp khác nhau.

Dòng: [8, 10, 15, 16, 17, 19, 22]; test: ['ex04_0', 'ex04_1', 'ex04_2', 'ex04_3', 'ex04_4'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 133 · lab03-ex01

**Thừa ký tự tab sau phần tử cuối mỗi dòng** · Có căn cứ code/log

NẾU lệnh in luôn thêm tab, kể cả ở cột cuối VÀ test ex01_0 ghi nhận output "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n" thay vì "1\t2\t3\n2\t3\t4\n3\t4\t5\n" THÌ gợi ý: Thừa ký tự tab sau phần tử cuối mỗi dòng.

Các con số và thứ tự đều khớp log, nhưng mỗi dòng có thêm tab ngay trước xuống dòng.

Giảng lại / kiểm tra: Ở cột cuối chỉ xuống dòng; dùng tab cho các cột còn lại.

Dòng: [22, 25]; test: ['ex01_0', 'ex01_1', 'ex01_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 134 · lab02-ex06

**Cập nhật min/max nằm ngoài vòng đọc** · Có căn cứ code/log

NẾU for chỉ nhập các số, hai if cập nhật nằm sau vòng VÀ test ex06_2 ghi nhận output "min: -1.800000, max: 1.000000\n" thay vì "min: -1.800000, max: 3.140000\n" THÌ gợi ý: Cập nhật min/max nằm ngoài vòng đọc.

Các giá trị giữa bị đọc rồi ghi đè mà không được xét. Dãy −1.8,3.14,1 mất giá trị lớn nhất 3.14 và cho max=1.

Giảng lại / kiểm tra: Đưa hai phép cập nhật vào trong vòng, ngay sau lần đọc thành công.

Dòng: [14, 16, 17, 18, 22]; test: ['ex06_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 135 · lab02-ex06

**Khởi tạo cực trị bằng số lượng và bỏ qua phần tử cuối** · Nhiều lỗi cùng xuất hiện

NẾU min/max nhận C, còn vòng kiểm tra X trước khi đọc giá trị tiếp theo VÀ test ex06_1 ghi nhận output "min: 1.000000, max: 6.800000\n" thay vì "min: 0.000000, max: 6.800000\n" THÌ gợi ý: Khởi tạo cực trị bằng số lượng và bỏ qua phần tử cuối.

Giá trị cuối được đọc ở cuối lượt cuối rồi không được xét. Test kết thúc bằng 0 vì vậy cho min=1; khởi tạo bằng C cũng không đại diện dữ liệu.

Giảng lại / kiểm tra: Khởi tạo min/max bằng phần tử đầu và xét đủ các phần tử còn lại.

Dòng: [11, 12, 14, 16, 20, 24, 25]; test: ['ex06_1'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 136 · lab02-ex09

**Chưa đệm số 0 để in thời gian đủ hai chữ số** · Có căn cứ code/log

NẾU printf dùng %d cho giờ, phút và giây VÀ test ex09_0 ghi nhận output "0:1:0\n" thay vì "00:01:00\n" THÌ gợi ý: Chưa đệm số 0 để in thời gian đủ hai chữ số.

Log cho các thành phần thời gian đúng giá trị, nhưng 0:1:0 khác mẫu 00:01:00.

Giảng lại / kiểm tra: Dùng %02d cho từng thành phần thời gian.

Dòng: [14]; test: ['ex09_0', 'ex09_1', 'ex09_2', 'ex09_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 137 · lab04-ex05

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex05_0 ghi nhận output "ola adeus" thay vì "ola adeus\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [19]; test: ['ex05_0', 'ex05_1', 'ex05_2', 'ex05_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 138 · lab03-ex01

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex01_0 ghi nhận output "1\t2\t3\n2\t3\t4\n3\t4\t5" thay vì "1\t2\t3\n2\t3\t4\n3\t4\t5\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [17, 21, 27]; test: ['ex01_0', 'ex01_1', 'ex01_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 139 · lab02-ex08

**Thiếu ký tự xuống dòng ở cuối output** · Có căn cứ code/log

NẾU đường in kết quả không bảo đảm ký tự xuống dòng cuối cùng VÀ test ex08_0 ghi nhận output "3.00" thay vì "3.00\n" THÌ gợi ý: Thiếu ký tự xuống dòng ở cuối output.

Trong các log có sẵn, nội dung và thứ tự ký tự đã khớp; output chỉ thiếu một ký tự xuống dòng ở cuối. Không cần đổi thuật toán chỉ để sửa sai khác này.

Giảng lại / kiểm tra: Bổ sung xuống dòng cuối output; với fgets, kiểm tra xem chuỗi đã chứa xuống dòng hay chưa để tránh in hai lần.

Dòng: [16]; test: ['ex08_0', 'ex08_1', 'ex08_2', 'ex08_3', 'ex08_4'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 140 · lab03-ex05

**In thừa một dòng trống cuối output** · Có căn cứ code/log

NẾU code in newline dù chuỗi hoặc nhánh trước đã kết thúc bằng newline VÀ test ex05_0 ghi nhận output "foo\n\n" thay vì "foo\n" THÌ gợi ý: In thừa một dòng trống cuối output.

Log khớp nội dung nhưng có thêm một newline ở cuối. Bài dùng fgets cần chú ý newline đã nằm trong chuỗi.

Giảng lại / kiểm tra: Bảo đảm output chỉ kết thúc bằng số newline mà oracle yêu cầu.

Dòng: [26, 31, 38, 44, 59]; test: ['ex05_0', 'ex05_1', 'ex05_2', 'ex05_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 141 · lab03-ex06

**Chia số trước khi lấy chữ số làm mất chữ số cuối** · Có căn cứ code/log

NẾU vòng lặp chia n cho 10 rồi mới cộng n%10 VÀ test ex06_3 ghi nhận output "no\n" thay vì "yes\n" THÌ gợi ý: Chia số trước khi lấy chữ số làm mất chữ số cuối.

Với 891, chữ số 1 bị bỏ trước khi cộng nên tổng chỉ còn 17; log cho no thay vì yes. Với số kết thúc bằng 1 khác, kết luận cũng có thể đảo chiều.

Giảng lại / kiểm tra: Lấy n%10 trước rồi mới chia n cho 10.

Dòng: [10, 11, 12, 15]; test: ['ex06_3', 'ex06_5'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 142 · lab04-ex02

**Code thực hiện tác vụ khác với oracle của bài** · Cần kiểm tra thêm

NẾU code xử lý palindrome, phân loại tam giác, min/max hoặc vẽ kim tự tháp thay vì tác vụ thể hiện trong test VÀ test ex02_0 ghi nhận output "    1\n  1 2 1\n1 2 3 2 1\n" thay vì "***\n **\n  *\n" THÌ gợi ý: Code thực hiện tác vụ khác với oracle của bài.

Output và cấu trúc code cho thấy một tác vụ khác hẳn bộ test: đây có thể là nộp nhầm bài hoặc ánh xạ dữ liệu sai. Gói thiếu đề gốc nên chưa kết luận đó là lỗi kiến thức của người học.

Giảng lại / kiểm tra: Kiểm tra lại đề, mã bài và nguồn ghép test trước khi gán nhãn cơ chế.

Dòng: [10, 14, 15, 19, 20]; test: ['ex02_0', 'ex02_1', 'ex02_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 143 · lab02-ex06

**In min/max giữa vòng lặp và đọc thừa một giá trị** · Nhiều lỗi cùng xuất hiện

NẾU đã đọc phần tử đầu nhưng vẫn lặp n lần, printf nằm trong while VÀ test ex06_0 ghi nhận output "min: 1.500000, max: 2.700000\nmin: 1.500000, max: 3.000000\nmin: 1.500000, max: 3.000000\n" thay vì "min: 1.500000, max: 3.000000\n" THÌ gợi ý: In min/max giữa vòng lặp và đọc thừa một giá trị.

Output chứa nhiều cặp cực trị tạm thời, có thêm lượt đọc sau khi hết dữ liệu. Oracle chỉ yêu cầu một cặp cuối.

Giảng lại / kiểm tra: Lặp n−1 lần còn lại và in sau vòng; kiểm tra scanf.

Dòng: [9, 12, 13, 18, 19]; test: ['ex06_0', 'ex06_1', 'ex06_2'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 144 · lab02-ex10

**Thừa lời nhắc nhập và thiếu newline cuối** · Có căn cứ code/log

NẾU stdout có câu Escreva um numero trước hai kết quả, dòng cuối không có newline VÀ test ex10_0 ghi nhận output "Escreva um numero\n2\n3" thay vì "2\n3\n" THÌ gợi ý: Thừa lời nhắc nhập và thiếu newline cuối.

Số chữ số và tổng chữ số trong log phù hợp; sai khác đang thấy thuộc phần trình bày. soma là biến toàn cục nên được khởi tạo bằng 0, không phải lỗi chưa khởi tạo.

Giảng lại / kiểm tra: Bỏ lời nhắc và thêm newline sau tổng.

Dòng: [2, 5, 16]; test: ['ex10_0', 'ex10_1', 'ex10_2', 'ex10_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 145 · lab02-ex04

**In thừa lời nhắc và ghép các số không có dấu cách** · Có căn cứ code/log

NẾU printf kết quả dùng %d%d%d VÀ test ex04_0 ghi nhận output "Introduza 3 numeros inteiros:\n126\n" thay vì "1 2 6\n" THÌ gợi ý: In thừa lời nhắc và ghép các số không có dấu cách.

Ba số đã được đổi chỗ nhưng bị nối thành 126 thay vì 1 2 6, đồng thời còn dòng hướng dẫn nhập.

Giảng lại / kiểm tra: Bỏ lời nhắc và dùng dấu cách giữa ba số.

Dòng: [7, 14]; test: ['ex04_0', 'ex04_1', 'ex04_2', 'ex04_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 146 · lab02-ex08

**Nhầm độ rộng trường với số chữ số thập phân** · Có căn cứ code/log

NẾU định dạng là %2.f thay vì %.2f VÀ test ex08_0 ghi nhận output " 3\n" thay vì "3.00\n" THÌ gợi ý: Nhầm độ rộng trường với số chữ số thập phân.

%2.f đặt độ rộng tối thiểu là 2 và độ chính xác thập phân là 0. Vì vậy log có số nguyên được làm tròn và khoảng đệm, không có hai chữ số thập phân.

Giảng lại / kiểm tra: Phân biệt width và precision của printf; sửa thành %.2f.

Dòng: [18]; test: ['ex08_0', 'ex08_1', 'ex08_2', 'ex08_3', 'ex08_4'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 147 · lab02-ex08

**Tính cả số lượng n như một phần tử của dãy** · Nhiều lỗi cùng xuất hiện

NẾU vòng scanf cộng mọi số từ đầu input tới EOF VÀ test ex08_0 ghi nhận output "2.666667\n" thay vì "3.00\n" THÌ gợi ý: Tính cả số lượng n như một phần tử của dãy.

Input 2,3,3 được tính trung bình của cả ba số thành 2.666667 thay vì trung bình hai số 3. Output cũng chưa dùng hai chữ số thập phân.

Giảng lại / kiểm tra: Đọc riêng n, cộng đúng n giá trị phía sau và in %.2f.

Dòng: [9, 10, 11, 14, 15]; test: ['ex08_0', 'ex08_1', 'ex08_2', 'ex08_3', 'ex08_4'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 148 · lab03-ex03

**Thừa khoảng trắng cuối dòng** · Có căn cứ code/log

NẾU code in dấu cách sau phần tử cuối hoặc đệm thêm chỗ trống bên phải VÀ test ex03_0 ghi nhận output "* - * \n- * - \n* - * \n" thay vì "* - *\n- * -\n* - *\n" THÌ gợi ý: Thừa khoảng trắng cuối dòng.

So sánh từng dòng cho thấy phần nội dung khớp oracle, nhưng còn khoảng trắng trước ký tự xuống dòng. Đây là sai khác trình bày ở các test đã có.

Giảng lại / kiểm tra: Chỉ in dấu phân cách giữa hai phần tử; bỏ phần đệm cuối dòng nếu oracle không yêu cầu.

Dòng: [21, 23, 24, 28]; test: ['ex03_0', 'ex03_1', 'ex03_2', 'ex03_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 149 · lab04-ex05

**In thêm dữ liệu kiểm tra ngoài đáp án** · Có căn cứ code/log

NẾU code in chuỗi đầu vào, chỉ số, tổng trung gian hoặc độ dài bên cạnh kết quả VÀ test ex05_0 ghi nhận output "ola adeus\n9\n" thay vì "ola adeus\n" THÌ gợi ý: In thêm dữ liệu kiểm tra ngoài đáp án.

Log có những dòng phụ khớp với lệnh in kiểm tra trong code. Phần đáp án phía sau không làm cho toàn bộ output khớp oracle.

Giảng lại / kiểm tra: Bỏ lệnh in kiểm tra và chỉ giữ output đề yêu cầu.

Dòng: [20, 21]; test: ['ex05_0', 'ex05_1', 'ex05_2', 'ex05_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.

## Bài 150 · lab02-ex02

**Đảo thứ tự cần sắp xếp và viết /n thay cho ký tự xuống dòng** · Nhiều lỗi cùng xuất hiện

NẾU nhánh in số lớn trước và chuỗi dùng /n VÀ test ex02_0 ghi nhận output "2/n 1" thay vì "1\n2\n" THÌ gợi ý: Đảo thứ tự cần sắp xếp và viết /n thay cho ký tự xuống dòng.

Input 1,2 cho 2/n 1: vừa sai thứ tự tăng dần, vừa in nguyên hai ký tự / và n.

Giảng lại / kiểm tra: In số nhỏ trước; dùng escape xuống dòng với dấu gạch chéo ngược.

Dòng: [9, 11, 15]; test: ['ex02_0', 'ex02_1', 'ex02_2', 'ex02_3'].

Nhãn chỉ mô tả cơ chế hoặc sai khác thấy trong code/log, chưa chứng minh người học hiểu sai khái niệm. Chưa chạy lại C.
