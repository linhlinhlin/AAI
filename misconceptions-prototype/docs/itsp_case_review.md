# Duyệt thủ công ITSP 2825: vị trí điểm so với đường tròn

Ngày: **19/09/2026**. Đây là đối chiếu code, đề bài, log lịch sử và bản sửa; **không chạy chương trình sinh viên**, không có nhãn chuyên gia và không xác nhận trạng thái nhận thức của người học.

Nguồn raw: `data/raw/itsp/dataset/Lab-4/2825/`, commit `0553f683f99403efb5ef440af826c1d229a52376`. Đã đọc `Main.c`, ba medoid và các phản ví dụ nêu dưới, cùng bản `*_correct.c` tương ứng. Kết quả được duyệt là `results/itsp/2825/agglomerative_combined_k3_w0.8_seed42.json`, không chọn cấu hình theo chất lượng nội dung cụm.

## Đề và kết quả thí nghiệm

Input là tâm `(x,y)`, bán kính `r`, điểm `(x1,y1)` dạng float; output phân loại inside/on/outside với chuỗi chính xác theo đề. Test 1, 2, 7 là outside; 3, 6 là on; 4, 5 là inside. Các test phân biệt nhánh kết quả, nhưng nhiều lỗi khác nhau vẫn có thể tạo cùng pass/fail signature.

Cohort có 22 bài được routing eligible; split 16 train/6 holdout, không có ID sinh viên. Cụm train có kích thước **5, 1, 10** lần lượt ID 0, 1, 2. Silhouette train khoảng **0,696**, surrogate fidelity holdout **5/6**, majority baseline **3/6**. Những chỉ số này mô tả phân hoạch/luật trên feature, không phải accuracy chẩn đoán misconception.

## Bằng chứng từ từng cụm

| Cụm | Bài | Quan sát cụ thể | Bản sửa / đối chiếu |
|---|---|---|---|
| 0, medoid | `271154_buggy.c` | Tính tổng bình phương chênh tọa độ rồi trừ `r`, không phải `r*r`; pass 1,2,7, fail 3,4,5,6 | `271154_correct.c` thay `-r` bằng `-r*r`; log sau sửa pass 7/7 |
| 0, cùng vector | `271211_buggy.c` | Đã tính `d=sqrtf(c)` nhưng so sánh `c` với `r` | Bản sửa đổi hai điều kiện từ `c` sang `d`; không phải cùng thao tác sửa với medoid |
| 0, cùng vector | `271228_buggy.c` | Tính `k = distance_squared-r*r` nhưng ba điều kiện kiểm tra `r` thay vì `k`; tất cả bán kính test dương nên log luôn outside | Bản sửa dùng `k` ở cả ba điều kiện. Không nên đặt tên toàn cụm là “quên bình phương bán kính” |
| 1, medoid, train singleton | `271173_buggy.c` | Ba test outside fail vì in `Cicle` thay vì `Circle`; bốn test còn lại pass | Bản sửa chỉ sửa chữ thiếu trong string literal; bằng chứng là lỗi nội dung output, chưa phải hiểu sai hình học |
| 1, holdout, khoảng cách 0 | `271188_buggy.c` | Cùng outcome và feature như medoid, nhưng nhánh outside in “on the Circle.” | Bản sửa thêm điều kiện `l>0` và in outside. Cùng vector không bảo đảm cùng lỗi cụ thể; không thể suy typo từ cụm |
| 2, medoid | `271163_buggy.c` | Cả bảy output chọn đúng từ inside/on/outside theo log nhưng thiếu dấu chấm cuối câu; fail 7/7 | Bản sửa thêm dấu chấm vào ba string literal; code tính khoảng cách và điều kiện giữ nguyên |
| 2, cùng vector với medoid | `271209_buggy.c` | Dùng `circle` thay vì `Circle` ở ba string literal; fail 7/7 | Bản sửa đổi chữ hoa C; không sửa công thức hoặc điều kiện |
| 2, bài khác | `271206_buggy.c` | `scanf` nhận `x,y,r,x1,y1` thay vì địa chỉ; thiếu cả năm dấu `&`. Log output rỗng và verdict WRONG_ANSWER ở mọi test | Bản sửa bổ sung địa chỉ cùng một số thay đổi trình bày/tính toán. Đây là lỗi đối số `scanf` có nguy cơ hành vi không xác định, **không có bằng chứng runtime để khẳng định crash** |

Các nhận xét trên là lỗi cụ thể nhìn thấy trong code và log. Chưa đủ căn cứ gọi chúng là quan niệm sai lầm bền vững; ví dụ dùng nhầm tên biến có thể là sơ suất, và sửa string literal có thể là lỗi gõ.

## Nhiễu output bị heuristic hiện tại bỏ sót

Trong `data/itsp/cohorts/2825/review.jsonl`, **không bài nào trong 22 bài có `formatting_suspected_test_ids` khác rỗng**. Điều đó chỉ nói heuristic xóa whitespace không phát hiện được; không có nghĩa dataset không chứa lỗi định dạng/nội dung output.

Ba ví dụ đã xác minh mà heuristic bỏ sót:

- `271163`: thiếu dấu chấm, 7/7 test fail.
- `271209`: khác chữ hoa/thường, 7/7 test fail.
- `271173`: lỗi chính tả `Cicle`, 3/7 test fail.

Không tự chuẩn hóa bỏ mọi dấu câu/chữ hoa hoặc fuzzy-match rồi chuyển verdict thành pass: cách đó có thể che lỗi nội dung thật, đặc biệt câu inside và outside có dạng gần giống nhau. Cách đơn giản hiện tại là giữ nguyên verdict, trình bày expected/actual và ghi annotation sau duyệt. Nếu thêm heuristic trong tương lai, phải là cờ chẩn đoán riêng có test phản ví dụ, không đổi oracle gốc.

## Giới hạn của feature và luật hiện tại

Ba thuộc tính cấu trúc còn biến thiên trên train là có so sánh inclusive, có so sánh strict và có address-of; còn 7 thuộc tính outcome. Bộ feature không biểu diễn biểu thức `r` so với `r*r`, biến thật được dùng trong điều kiện, hoặc nội dung chuỗi output. Vì vậy không phân biệt được các cặp cùng vector ở bảng trên. Sự hiện diện của `&` ở đâu đó cũng không xác nhận từng đối số `scanf` đúng; không gán nhãn “hiểu con trỏ” từ một flag toàn chương trình.

Luật surrogate chỉ dùng test 1 và test 4. Nhánh `test:1=fail AND NOT(test:4=fail)` có train precision **0,5** và holdout precision **0,5**; không nên trình bày mọi luật là bằng chứng mạnh. Cụm 1 chỉ có một mẫu train, dù medoid trông rõ ràng khi đọc code.

Routing `eligible` nghĩa là log đầy đủ, có fail, không có verdict runtime/timeout rõ ràng và parser chấp nhận cú pháp. `271206` cho thấy eligible **không** bảo đảm an toàn bộ nhớ hay lỗi thuần logic: nguồn lịch sử có thể chỉ ghi WRONG_ANSWER. Phải giữ cụm lỗi output và dấu hiệu lỗi thực thi trong hồ sơ duyệt trước khi giảng viên diễn giải.

## Kết luận sử dụng cho prototype

Cohort này chứng minh pipeline tạo được cụm và truy vết lỗi cụ thể, đồng thời cung cấp phản ví dụ rõ cho việc đồng nhất cụm với misconception. Giữ làm case study giới hạn của outcome + chỉ báo cú pháp. Trước đánh giá giáo dục, cần người duyệt tách lỗi output, lỗi chọn biến/công thức và lỗi đối số hàm theo bằng chứng; sau đó mới quyết định có cần feature biểu thức/call-site đơn giản. Không sửa thuật toán chỉ để làm đẹp silhouette của 22 bài này.
