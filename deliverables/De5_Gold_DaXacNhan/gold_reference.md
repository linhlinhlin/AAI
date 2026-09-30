# Bộ nhãn tham chiếu đã xác nhận

48 nhãn cơ chế lỗi do AI đề xuất, đã được người dùng kiểm tra và chấp thuận trong hội thoại. Dùng làm bộ tham chiếu của dự án. Đây là một lượt xác nhận có xem gợi ý AI, chưa phải gold từ hai người chấm mù và phân xử. Chưa xác nhận nhận thức người học; chưa tính accuracy.

Bài 14 giữ nhiều cơ chế; không ép thành một lỗi chính để chấm single-primary. Các giới hạn code/log và đề/oracle vẫn được giữ.

## Bài 1 · Đề 2833

**Nhãn đã xác nhận:** Cập nhật biến lặp ngược chiều dừng

NẾU vòng lặp bắt đầu từ n, kiểm tra i >= 1 nhưng lại tăng i VÀ các test ghi nhận không có output THÌ: Cập nhật biến lặp ngược chiều dừng.

Ở vòng ngoài, i++ làm i đi xa điều kiện dừng thay vì tiến về 0. Lệnh in nằm sau vòng lặp nên không có đường kết thúc bình thường trước khi có thể tràn số nguyên.

**Giới hạn bằng chứng:** Log chỉ ghi output rỗng, không đủ kết luận đã timeout hay crash. Không gọi đây là vòng lặp vô hạn xác định vì tràn int có hành vi không xác định.

## Bài 2 · Đề 2833

**Nhãn đã xác nhận:** Đếm trùng tam giác khi đổi thứ tự ba cạnh

NẾU cả ba cạnh đều được duyệt độc lập từ 1 đến N, không loại hoán vị trùng VÀ N = 4 cho số đếm 34 thay vì 13 trong log THÌ: Đếm trùng tam giác khi đổi thứ tự ba cạnh.

Các bộ cạnh đổi chỗ vẫn đi qua ba vòng lặp và đều được cộng vào tổng. Bộ ba cạnh của cùng một tam giác vì thế bị đếm nhiều lần.

**Giới hạn bằng chứng:** Nhãn dựa trên cấu trúc duyệt và oracle lịch sử. Gói chấm từng bài thiếu đề gốc; cần đối chiếu quy ước tam giác không phân biệt thứ tự trước khi duyệt nhãn.

## Bài 3 · Đề 2812

**Nhãn đã xác nhận:** Thiếu ngoặc nhọn {} gom nhóm lệnh và else tương ứng

NẾU if(a<0) chỉ điều khiển một lệnh in, còn các lệnh in thông báo nằm ngoài nhánh VÀ output có cả thông báo âm và dương cho cùng một số THÌ: Thiếu ngoặc nhọn {} gom nhóm lệnh và else tương ứng.

Thụt lề không tạo thành khối lệnh trong C. Khi a khác 0, các dòng in negative và positive vẫn chạy; log số âm cho thấy hai thông báo nối nhau.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 4 · Đề 2833

**Nhãn đã xác nhận:** Đếm trùng tam giác khi đổi thứ tự ba cạnh

NẾU cả ba cạnh đều được duyệt độc lập từ 1 đến N, không loại hoán vị trùng VÀ N = 4 cho số đếm 34 thay vì 13 trong log THÌ: Đếm trùng tam giác khi đổi thứ tự ba cạnh.

Các bộ cạnh đổi chỗ vẫn đi qua ba vòng lặp và đều được cộng vào tổng. Bộ ba cạnh của cùng một tam giác vì thế bị đếm nhiều lần.

**Giới hạn bằng chứng:** Nhãn dựa trên cấu trúc duyệt và oracle lịch sử. Gói chấm từng bài thiếu đề gốc; cần đối chiếu quy ước tam giác không phân biệt thứ tự trước khi duyệt nhãn.

## Bài 5 · Đề 2812

**Nhãn đã xác nhận:** Chuỗi printf có định dạng nhưng thiếu đối số

NẾU printf có cả %.4f và %d nhưng chỉ truyền một giá trị VÀ test số dương xuất hiện thêm một số nguyên ngoài đáp án THÌ: Chuỗi printf có định dạng nhưng thiếu đối số.

Nhánh số dương thiếu đối số tương ứng với %d. Con số thừa trong log không phải kết quả tính toán hợp lệ của bài.

**Giới hạn bằng chứng:** printf thiếu đối số gây hành vi không xác định; không khẳng định số thừa sẽ luôn giống log.

## Bài 6 · Đề 2825

**Nhãn đã xác nhận:** Bỏ sót trường hợp điểm nằm trên đường tròn

NẾU code chỉ chia thành bên trong và nhánh else bên ngoài VÀ test trên biên bị in thành bên ngoài THÌ: Bỏ sót trường hợp điểm nằm trên đường tròn.

Giá trị bằng 0 của bình phương khoảng cách trừ bình phương bán kính rơi vào else. Hai test trên đường tròn vì vậy nhận thông báo outside.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 7 · Đề 2812

**Nhãn đã xác nhận:** Chỉ in giá trị nhập, chưa in kết quả phân loại

NẾU chương trình đọc số rồi chỉ printf số đó VÀ output thiếu thông báo âm, dương hoặc zero mà oracle yêu cầu THÌ: Chỉ in giá trị nhập, chưa in kết quả phân loại.

Bài đã đọc được dữ liệu nhưng chưa có phần phân loại và in thông báo. Đây không phải lỗi in hằng số: giá trị in vẫn phụ thuộc đầu vào.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 8 · Đề 2825

**Nhãn đã xác nhận:** Gắn else vào if thứ hai, khiến một điểm nhận hai kết luận

NẾU hai if độc lập kiểm tra trong/ngoài, còn else gắn với if kiểm tra bên ngoài VÀ test điểm bên trong in cả inside và on THÌ: Gắn else vào if thứ hai, khiến một điểm nhận hai kết luận.

Khi điểm ở bên trong, if đầu in inside. if thứ hai sai nên else của nó tiếp tục in on. Cần một chuỗi nhánh loại trừ nhau.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 9 · Đề 2825

**Nhãn đã xác nhận:** Thiếu địa chỉ biến khi gọi scanf

NẾU scanf dùng %f nhưng truyền giá trị x, y, r, x1, y1 thay cho địa chỉ các biến VÀ các log không ghi nhận output THÌ: Thiếu địa chỉ biến khi gọi scanf.

scanf cần địa chỉ nơi ghi dữ liệu. Lời gọi hiện tại truyền các biến float chưa được nhập thay vì &x, &y, &r, &x1, &y1.

**Giới hạn bằng chứng:** Lỗi đối số được thấy trực tiếp trong code. Output rỗng không đủ chứng minh crash; lời gọi này có hành vi không xác định.

## Bài 10 · Đề 2825

**Nhãn đã xác nhận:** Thiếu dấu chấm cuối thông báo

NẾU chuỗi printf không có dấu chấm cuối câu VÀ output ghi nhận khớp nội dung phân loại nhưng thiếu dấu chấm so với oracle THÌ: Thiếu dấu chấm cuối thông báo.

Khác biệt nhìn thấy trong các test là dấu chấm cuối câu. Không có căn cứ từ sai khác này để kết luận học viên chưa hiểu công thức khoảng cách.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 11 · Đề 2833

**Nhãn đã xác nhận:** Đếm trùng tam giác khi đổi thứ tự ba cạnh

NẾU cả ba cạnh đều được duyệt độc lập từ 1 đến N, không loại hoán vị trùng VÀ N = 4 cho số đếm 34 thay vì 13 trong log THÌ: Đếm trùng tam giác khi đổi thứ tự ba cạnh.

Các bộ cạnh đổi chỗ vẫn đi qua ba vòng lặp và đều được cộng vào tổng. Bộ ba cạnh của cùng một tam giác vì thế bị đếm nhiều lần.

**Giới hạn bằng chứng:** Nhãn dựa trên cấu trúc duyệt và oracle lịch sử. Gói chấm từng bài thiếu đề gốc; cần đối chiếu quy ước tam giác không phân biệt thứ tự trước khi duyệt nhãn.

## Bài 12 · Đề 2833

**Nhãn đã xác nhận:** Dùng điều kiện lọc làm điều kiện dừng vòng lặp (vòng lặp bị ngắt sớm)

NẾU vòng while của cạnh c vừa kiểm tra giới hạn vừa yêu cầu a < c+b ngay từ c=1 VÀ N = 4 chỉ đếm 10 thay vì 13 THÌ: Dùng điều kiện lọc làm điều kiện dừng vòng lặp (vòng lặp bị ngắt sớm).

Một c nhỏ chưa tạo tam giác không có nghĩa các c lớn hơn đều không tạo được. Khi điều kiện sai ngay đầu vòng, code bỏ qua các giá trị c tiếp theo có thể hợp lệ.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 13 · Đề 2812

**Nhãn đã xác nhận:** In thừa giá trị số ở nhánh zero

NẾU nhánh a == 0 in thêm %f trước thông báo VÀ test zero nhận 0.000000 input is zero thay vì input is zero THÌ: In thừa giá trị số ở nhánh zero.

Bài đã đi đúng nhánh zero, nhưng mẫu output của nhánh này không yêu cầu in giá trị a.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 14 · Đề 2833

**Nhãn đã xác nhận:** Dùng HOẶC thay cho VÀ và đếm cả các hoán vị cạnh

NẾU ba bất đẳng thức tam giác nối bằng ||, đồng thời ba cạnh duyệt độc lập VÀ N = 4 cho 64, tức mọi bộ ba đều được đếm THÌ: Dùng HOẶC thay cho VÀ và đếm cả các hoán vị cạnh.

Chỉ cần một bất đẳng thức đúng là code cộng tổng, trong khi điều kiện tam giác cần cả ba. Ngoài ra, miền duyệt hiện tại vẫn đếm các hoán vị như những bộ khác nhau.

**Giới hạn bằng chứng:** Có ít nhất hai cơ chế lỗi cùng hiện diện. Không ép bài này thành nhãn một lỗi duy nhất.

## Bài 15 · Đề 2812

**Nhãn đã xác nhận:** Kiểm tra một giá trị mẫu thay vì phân loại theo dấu

NẾU code chỉ xét a == -12 và gọi mọi giá trị còn lại là zero VÀ đầu vào 1 lại được in là zero THÌ: Kiểm tra một giá trị mẫu thay vì phân loại theo dấu.

Điều kiện hiện tại nhận riêng -12 chứ không nhận mọi số âm. Nhánh else cũng gộp cả số dương, số âm khác và số 0.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 16 · Đề 2833

**Nhãn đã xác nhận:** Bài mới đọc đầu vào, chưa tính và chưa in kết quả

NẾU main chỉ scanf rồi return VÀ mọi test ghi nhận output rỗng THÌ: Bài mới đọc đầu vào, chưa tính và chưa in kết quả.

Không có vòng duyệt, phép đếm hoặc lệnh in nào sau khi đọc N. Có thể đây là bài đang làm dở; chưa thể suy ra học viên hiểu sai khái niệm cụ thể.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 17 · Đề 2825

**Nhãn đã xác nhận:** Đọc nhầm thứ tự bán kính và tọa độ điểm

NẾU scanf gán ba giá trị cuối lần lượt vào x1, y1, r VÀ test 0 0 5 3 7 bị phân loại bên trong thay vì bên ngoài THÌ: Đọc nhầm thứ tự bán kính và tọa độ điểm.

Cách đọc khiến 5 trở thành x1 và 7 trở thành bán kính. Theo thứ tự x, y, r, x1, y1 thể hiện trong bộ test, khoảng cách phải được tính cho điểm (3,7) với bán kính 5.

**Giới hạn bằng chứng:** Cần đối chiếu thứ tự input với đề gốc vì packet này thiếu statement. Bài 17 còn gọi sqrt mà không include math.h; không bỏ qua vấn đề khai báo khi sửa code.

## Bài 18 · Đề 2825

**Nhãn đã xác nhận:** Khác chữ hoa/chữ thường trong thông báo

NẾU printf dùng circle với chữ c thường VÀ oracle yêu cầu Circle với chữ C hoa THÌ: Khác chữ hoa/chữ thường trong thông báo.

Sai khác quan sát được là cách viết Circle, không phải vị trí trong/ngoài/trên đường tròn ở các test đã ghi nhận.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 19 · Đề 2825

**Nhãn đã xác nhận:** Quên bỏ dòng in debug

NẾU code in khoảng cách kèm chữ demo trước khi in kết luận VÀ output có thêm một dòng không nằm trong đáp án THÌ: Quên bỏ dòng in debug.

Lệnh printf phục vụ kiểm tra tạm vẫn còn trong bài nộp. Ví dụ test đầu in thêm 6.700747 demo trước thông báo outside.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 20 · Đề 2833

**Nhãn đã xác nhận:** Sai từ trong mẫu output: triangle thay vì triangles

NẾU chuỗi in dùng triangle ở số ít VÀ số đếm trong log khớp oracle nhưng phần chữ thiếu s THÌ: Sai từ trong mẫu output: triangle thay vì triangles.

Không nên gán lỗi đếm tổ hợp cho bài này chỉ vì toàn bộ test fail. Phần số đếm đã khớp ở các test ghi nhận; sai khác nằm ở từ triangles.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 21 · Đề 2833

**Nhãn đã xác nhận:** Sai từ trong mẫu output: triangle thay vì triangles

NẾU chuỗi in dùng triangle ở số ít VÀ số đếm trong log khớp oracle nhưng phần chữ thiếu s THÌ: Sai từ trong mẫu output: triangle thay vì triangles.

Không nên gán lỗi đếm tổ hợp cho bài này chỉ vì toàn bộ test fail. Phần số đếm đã khớp ở các test ghi nhận; sai khác nằm ở từ triangles.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 22 · Đề 2825

**Nhãn đã xác nhận:** Thiếu dấu chấm cuối thông báo

NẾU chuỗi printf không có dấu chấm cuối câu VÀ output ghi nhận khớp nội dung phân loại nhưng thiếu dấu chấm so với oracle THÌ: Thiếu dấu chấm cuối thông báo.

Khác biệt nhìn thấy trong các test là dấu chấm cuối câu. Không có căn cứ từ sai khác này để kết luận học viên chưa hiểu công thức khoảng cách.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 23 · Đề 2812

**Nhãn đã xác nhận:** Thừa dấu chấm so với oracle chấm bài

NẾU một hoặc nhiều chuỗi printf có dấu chấm cuối câu VÀ log mong đợi cùng nội dung nhưng không có dấu chấm THÌ: Thừa dấu chấm so với oracle chấm bài.

Các nhánh đang phân loại dấu phù hợp với test; sai khác được trích dẫn là dấu chấm. Bài 33 chỉ thêm dấu chấm ở nhánh dương.

**Giới hạn bằng chứng:** Tài liệu rà soát trước đó ghi nhận ví dụ đề 2812 có dấu chấm nhưng oracle không có. Đây là bất nhất cần kiểm chứng, không phải bằng chứng chắc chắn học viên sai kiến thức.

## Bài 24 · Đề 2825

**Nhãn đã xác nhận:** Thiếu dấu chấm cuối thông báo

NẾU chuỗi printf không có dấu chấm cuối câu VÀ output ghi nhận khớp nội dung phân loại nhưng thiếu dấu chấm so với oracle THÌ: Thiếu dấu chấm cuối thông báo.

Khác biệt nhìn thấy trong các test là dấu chấm cuối câu. Không có căn cứ từ sai khác này để kết luận học viên chưa hiểu công thức khoảng cách.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 25 · Đề 2825

**Nhãn đã xác nhận:** So sánh bình phương khoảng cách với bán kính chưa bình phương

NẾU code dùng d² nhưng đối chiếu trực tiếp với r VÀ điểm trên đường tròn bán kính 5 bị báo là ở ngoài THÌ: So sánh bình phương khoảng cách với bán kính chưa bình phương.

Hai vế đang khác đại lượng: d² phải so với r², hoặc d so với r. Ở test 3, d² = 25 và r = 5, nên phép so sánh hiện tại làm lệch kết luận.

**Giới hạn bằng chứng:** Bài 46 có tính sqrtf(c) vào d nhưng không dùng d để so sánh, đồng thời thiếu math.h. Nhãn này mô tả sai khác công thức thấy trong code/log, không chứng minh niềm tin của người học.

## Bài 26 · Đề 2833

**Nhãn đã xác nhận:** Thoát vòng duyệt ngay khi gặp một bộ cạnh chưa hợp lệ

NẾU k đang tăng dần nhưng else lại break khi j+k <= i VÀ số đếm nhỏ hơn oracle, như N = 4 cho 10 thay vì 13 THÌ: Thoát vòng duyệt ngay khi gặp một bộ cạnh chưa hợp lệ.

Một k nhỏ không thỏa chưa loại được những k lớn hơn. break bỏ luôn các bộ phía sau nên bài bị thiếu trường hợp.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 27 · Đề 2812

**Nhãn đã xác nhận:** Đặt biến vào chuỗi định dạng thay vì truyền đối số printf

NẾU chuỗi printf có %.4f và %n nhưng không truyền đối số tương ứng VÀ giá trị in trong log không khớp số đầu vào THÌ: Đặt biến vào chuỗi định dạng thay vì truyền đối số printf.

%n không có nghĩa là in biến tên n; đó là một conversion khác, cần con trỏ để ghi số ký tự đã in. Cả %.4f lẫn %n ở đây đều không có đối số.

**Giới hạn bằng chứng:** Lời gọi thiếu đối số có hành vi không xác định. Không suy ra mọi lần chạy đều in 0 từ log lịch sử.

## Bài 28 · Đề 2812

**Nhãn đã xác nhận:** Nhầm số 0 với ký tự 0 khi so sánh

NẾU biến số thực được so sánh với '0' thay vì 0 VÀ các test nhập zero không có thông báo THÌ: Nhầm số 0 với ký tự 0 khi so sánh.

'0' là hằng ký tự, không phải giá trị số 0. Khi a bằng 0, hai nhánh >0 và <0 đều sai; điều kiện cuối cũng không nhận đúng zero.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 29 · Đề 2812

**Nhãn đã xác nhận:** Đưa &a vào chuỗi scanf thay vì truyền địa chỉ đối số

NẾU lời gọi là scanf("%f,&a") và không có đối số nhận dữ liệu VÀ log không ghi nhận output THÌ: Đưa &a vào chuỗi scanf thay vì truyền địa chỉ đối số.

Phần &a nằm trong dấu nháy nên không cung cấp địa chỉ biến cho %f. Cần viết scanf("%f", &a).

**Giới hạn bằng chứng:** Đây là lỗi đối số trực tiếp; không suy đoán nguyên nhân kết thúc tiến trình chỉ từ output rỗng.

## Bài 30 · Đề 2825

**Nhãn đã xác nhận:** Tính độ lệch vị trí nhưng lại rẽ nhánh theo bán kính

NẾU code tính k = d² − r² rồi dùng dấu của r trong if VÀ cả điểm bên trong và trên biên đều bị in là bên ngoài khi r dương THÌ: Tính độ lệch vị trí nhưng lại rẽ nhánh theo bán kính.

Bán kính dương không cho biết điểm đang ở trong hay ngoài. Biến k đã tính đúng đại lượng cần xét nhưng bị bỏ qua khi rẽ nhánh.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 31 · Đề 2825

**Nhãn đã xác nhận:** Thiếu dấu chấm cuối thông báo

NẾU chuỗi printf không có dấu chấm cuối câu VÀ output ghi nhận khớp nội dung phân loại nhưng thiếu dấu chấm so với oracle THÌ: Thiếu dấu chấm cuối thông báo.

Khác biệt nhìn thấy trong các test là dấu chấm cuối câu. Không có căn cứ từ sai khác này để kết luận học viên chưa hiểu công thức khoảng cách.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 32 · Đề 2825

**Nhãn đã xác nhận:** Thiếu dấu chấm cuối thông báo

NẾU chuỗi printf không có dấu chấm cuối câu VÀ output ghi nhận khớp nội dung phân loại nhưng thiếu dấu chấm so với oracle THÌ: Thiếu dấu chấm cuối thông báo.

Khác biệt nhìn thấy trong các test là dấu chấm cuối câu. Không có căn cứ từ sai khác này để kết luận học viên chưa hiểu công thức khoảng cách.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 33 · Đề 2812

**Nhãn đã xác nhận:** Thừa dấu chấm so với oracle chấm bài

NẾU một hoặc nhiều chuỗi printf có dấu chấm cuối câu VÀ log mong đợi cùng nội dung nhưng không có dấu chấm THÌ: Thừa dấu chấm so với oracle chấm bài.

Các nhánh đang phân loại dấu phù hợp với test; sai khác được trích dẫn là dấu chấm. Bài 33 chỉ thêm dấu chấm ở nhánh dương.

**Giới hạn bằng chứng:** Tài liệu rà soát trước đó ghi nhận ví dụ đề 2812 có dấu chấm nhưng oracle không có. Đây là bất nhất cần kiểm chứng, không phải bằng chứng chắc chắn học viên sai kiến thức.

## Bài 34 · Đề 2825

**Nhãn đã xác nhận:** Gõ sai Circle thành Cicle ở nhánh bên ngoài

NẾU printf của nhánh outside viết Cicle VÀ test bên ngoài khác oracle đúng một chữ r THÌ: Gõ sai Circle thành Cicle ở nhánh bên ngoài.

Log vẫn cho kết luận outside nhưng thông báo bị sai chính tả. Chưa có căn cứ coi đây là lỗi công thức hình học.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 35 · Đề 2833

**Nhãn đã xác nhận:** Dấu chấm phẩy sau for làm thân vòng lặp rỗng

NẾU mỗi câu for kết thúc ngay bằng dấu ; trước khối ngoặc nhọn VÀ nhiều input khác nhau đều chỉ cho số đếm 1 THÌ: Dấu chấm phẩy sau for làm thân vòng lặp rỗng.

Khối đếm phía dưới không còn là thân của các vòng for. Nó chỉ chạy sau khi các vòng rỗng đã kết thúc, nên không duyệt từng bộ cạnh như dự định.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 36 · Đề 2812

**Nhãn đã xác nhận:** Thừa dấu chấm so với oracle chấm bài

NẾU một hoặc nhiều chuỗi printf có dấu chấm cuối câu VÀ log mong đợi cùng nội dung nhưng không có dấu chấm THÌ: Thừa dấu chấm so với oracle chấm bài.

Các nhánh đang phân loại dấu phù hợp với test; sai khác được trích dẫn là dấu chấm. Bài 33 chỉ thêm dấu chấm ở nhánh dương.

**Giới hạn bằng chứng:** Tài liệu rà soát trước đó ghi nhận ví dụ đề 2812 có dấu chấm nhưng oracle không có. Đây là bất nhất cần kiểm chứng, không phải bằng chứng chắc chắn học viên sai kiến thức.

## Bài 37 · Đề 2833

**Nhãn đã xác nhận:** Sai từ trong mẫu output: triangle thay vì triangles

NẾU chuỗi in dùng triangle ở số ít VÀ số đếm trong log khớp oracle nhưng phần chữ thiếu s THÌ: Sai từ trong mẫu output: triangle thay vì triangles.

Không nên gán lỗi đếm tổ hợp cho bài này chỉ vì toàn bộ test fail. Phần số đếm đã khớp ở các test ghi nhận; sai khác nằm ở từ triangles.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 38 · Đề 2825

**Nhãn đã xác nhận:** Gắn else vào if thứ hai, khiến một điểm nhận hai kết luận

NẾU hai if độc lập kiểm tra trong/ngoài, còn else gắn với if kiểm tra bên ngoài VÀ test điểm bên trong in cả inside và on THÌ: Gắn else vào if thứ hai, khiến một điểm nhận hai kết luận.

Khi điểm ở bên trong, if đầu in inside. if thứ hai sai nên else của nó tiếp tục in on. Cần một chuỗi nhánh loại trừ nhau.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 39 · Đề 2825

**Nhãn đã xác nhận:** Đọc nhầm thứ tự bán kính và tọa độ điểm

NẾU scanf gán ba giá trị cuối lần lượt vào x1, y1, r VÀ test 0 0 5 3 7 bị phân loại bên trong thay vì bên ngoài THÌ: Đọc nhầm thứ tự bán kính và tọa độ điểm.

Cách đọc khiến 5 trở thành x1 và 7 trở thành bán kính. Theo thứ tự x, y, r, x1, y1 thể hiện trong bộ test, khoảng cách phải được tính cho điểm (3,7) với bán kính 5.

**Giới hạn bằng chứng:** Cần đối chiếu thứ tự input với đề gốc vì packet này thiếu statement. Bài 17 còn gọi sqrt mà không include math.h; không bỏ qua vấn đề khai báo khi sửa code.

## Bài 40 · Đề 2833

**Nhãn đã xác nhận:** Khử trùng số đếm bằng một công thức không phù hợp

NẾU code đếm các hoán vị rồi thay tổng bằng ((count-n)/n)+n VÀ N = 4 cho 11 thay vì 13 dù một vài input nhỏ vẫn đúng THÌ: Khử trùng số đếm bằng một công thức không phù hợp.

Số hoán vị không cố định theo n: ba cạnh khác nhau, hai cạnh bằng nhau và ba cạnh bằng nhau có số lần lặp khác nhau. Chia tổng theo n không loại trùng đúng cho mọi trường hợp.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 41 · Đề 2825

**Nhãn đã xác nhận:** Thiếu dấu chấm riêng ở nhánh trên đường tròn

NẾU nhánh on in chuỗi không có dấu chấm cuối VÀ chỉ các test trên biên khác oracle ở dấu câu THÌ: Thiếu dấu chấm riêng ở nhánh trên đường tròn.

Bài đã nhận đúng trường hợp trên đường tròn trong log. Lỗi quan sát được nằm ở chuỗi thông báo của nhánh đó.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 42 · Đề 2825

**Nhãn đã xác nhận:** Nhánh bên ngoài in nhầm thông báo trên đường tròn

NẾU else sau l<0 và l==0 vẫn in on VÀ test điểm bên ngoài bị báo là nằm trên đường tròn THÌ: Nhánh bên ngoài in nhầm thông báo trên đường tròn.

Cấu trúc đã dành nhánh cuối cho l>0, nhưng chuỗi in bị lặp từ nhánh l==0. Có thể là lỗi sao chép; chưa đủ căn cứ kết luận học viên không hiểu hình học.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 43 · Đề 2825

**Nhãn đã xác nhận:** Khác chữ hoa/chữ thường trong thông báo

NẾU printf dùng circle với chữ c thường VÀ oracle yêu cầu Circle với chữ C hoa THÌ: Khác chữ hoa/chữ thường trong thông báo.

Sai khác quan sát được là cách viết Circle, không phải vị trí trong/ngoài/trên đường tròn ở các test đã ghi nhận.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 44 · Đề 2825

**Nhãn đã xác nhận:** Khác chữ hoa/chữ thường trong thông báo

NẾU printf dùng circle với chữ c thường VÀ oracle yêu cầu Circle với chữ C hoa THÌ: Khác chữ hoa/chữ thường trong thông báo.

Sai khác quan sát được là cách viết Circle, không phải vị trí trong/ngoài/trên đường tròn ở các test đã ghi nhận.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 45 · Đề 2812

**Nhãn đã xác nhận:** Thừa dấu chấm so với oracle chấm bài

NẾU một hoặc nhiều chuỗi printf có dấu chấm cuối câu VÀ log mong đợi cùng nội dung nhưng không có dấu chấm THÌ: Thừa dấu chấm so với oracle chấm bài.

Các nhánh đang phân loại dấu phù hợp với test; sai khác được trích dẫn là dấu chấm. Bài 33 chỉ thêm dấu chấm ở nhánh dương.

**Giới hạn bằng chứng:** Tài liệu rà soát trước đó ghi nhận ví dụ đề 2812 có dấu chấm nhưng oracle không có. Đây là bất nhất cần kiểm chứng, không phải bằng chứng chắc chắn học viên sai kiến thức.

## Bài 46 · Đề 2825

**Nhãn đã xác nhận:** So sánh bình phương khoảng cách với bán kính chưa bình phương

NẾU code dùng d² nhưng đối chiếu trực tiếp với r VÀ điểm trên đường tròn bán kính 5 bị báo là ở ngoài THÌ: So sánh bình phương khoảng cách với bán kính chưa bình phương.

Hai vế đang khác đại lượng: d² phải so với r², hoặc d so với r. Ở test 3, d² = 25 và r = 5, nên phép so sánh hiện tại làm lệch kết luận.

**Giới hạn bằng chứng:** Bài 46 có tính sqrtf(c) vào d nhưng không dùng d để so sánh, đồng thời thiếu math.h. Nhãn này mô tả sai khác công thức thấy trong code/log, không chứng minh niềm tin của người học.

## Bài 47 · Đề 2812

**Nhãn đã xác nhận:** In số hai lần và dùng mẫu định dạng không thống nhất

NẾU code in số trước if rồi lại in số trong nhánh âm/dương VÀ log có hai giá trị số nối nhau, hoặc thêm số trước thông báo zero THÌ: In số hai lần và dùng mẫu định dạng không thống nhất.

Lệnh in trước chuỗi if luôn chạy. Các nhánh sau lại in giá trị lần nữa bằng %f, nên output vừa lặp số vừa khác số chữ số thập phân.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.

## Bài 48 · Đề 2825

**Nhãn đã xác nhận:** Thiếu dấu chấm cuối thông báo

NẾU chuỗi printf không có dấu chấm cuối câu VÀ output ghi nhận khớp nội dung phân loại nhưng thiếu dấu chấm so với oracle THÌ: Thiếu dấu chấm cuối thông báo.

Khác biệt nhìn thấy trong các test là dấu chấm cuối câu. Không có căn cứ từ sai khác này để kết luận học viên chưa hiểu công thức khoảng cách.

**Giới hạn bằng chứng:** Đây là cơ chế lỗi AI đề xuất từ code và log đã có; chưa xác nhận người học hiểu sai khái niệm nào.
