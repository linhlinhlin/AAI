# AI annotation cho 17 mẫu ITSP — chờ human expert validation

## Sau phản biện — 20/09/2026

[Protocol kiểm chứng đã cập nhật](itsp_validation_revision.md): tách biểu hiện lỗi → cơ chế lỗi → giả thuyết misconception; giữ baseline và cây luật nông. ILA thuộc quy nạp luật, không gọi là clustering phi giám sát. Kiểm tra lại đủ 59 submissions: A=C ở seed42 (ARI=1 từng bài); vector combined của 271173/271188 trùng nhau. Chưa có bằng chứng cấu trúc hiện tại cải thiện phân hoạch; chưa phủ định mọi cấu trúc khác.

Đánh dấu toàn bộ 59 bài đã xuất hiện trong hồ sơ là dữ liệu phát triển/đã xem cho thí nghiệm feature mới; chưa chọn mẫu đánh giá độc lập mới hoặc triển khai feature quan hệ. Packet chính đã gắn nhãn “Vòng 2 — có hiển thị cụm”; gói vòng 1 giữ nguyên. Hai chuyên gia thật cần chốt codebook và chấm độc lập. Báo purity kèm coverage, No/Unclear và phân tích gộp/tách sai; chỉ số cặp cần nhãn cơ chế phù hợp, chưa tự tính trên AI. Expert validation tiếp tục chờ annotation, các metric vẫn null.


Ngày 19/09/2026. **17/17 AI annotation hoàn tất; human expert annotation: 0/17, adjudication: 0/17. Đây không phải ground truth, gold standard hay kết quả expert-validated.** Reviewer duy nhất: `ai:codex:2026-09-19`.

Đã đọc ba đề `Main.c`, toàn bộ source buggy/correct và test log của 17 mẫu; sau khi hình thành quyết định từ code và failure, đối chiếu assignment A/B/C seed42 và code/log/diff của đủ 59 thành viên trong [cluster context](../results/itsp/expert_cluster_context.md). Không chạy code sinh viên. Đã tiếp xúc review cũ trước khi đánh giá theo yêu cầu nên **không tuyên bố đánh giá mù**, tất cả `independent_blind_review=false`. Cluster ID chỉ dùng ở bước đối chiếu nguyên nhân, không phải bằng chứng quyết định misconception.

## Quy ước annotation và schema

Giữ schema v1 của [expert_annotations.json](../data/itsp/expert_annotations.json): `has_misconception` được lưu bằng trường hiện có `misconception`; `reasoning` nằm trong `evidence`. Confidence: High = 4–5, Medium = 3, Low = 1–2. Confidence nói mức tin cậy vào quyết định, không chứng minh trạng thái nhận thức. `No` là lỗi chuỗi/typo hoặc xung đột đề–oracle trong phạm vi evidence; không khẳng định người học không có bất kỳ hiểu sai nào. `Unclear` là đã đánh giá nhưng không phân biệt được sơ suất với misconception. `Yes` là giả thuyết AI được code/test hỗ trợ, vẫn có nguyên nhân thay thế ghi trong evidence.

Giữ slot human `pending` và mọi `adjudication` `pending`; thêm riêng một review AI mỗi mẫu. Prefix `ai:` phân biệt reviewer AI trong schema hiện không có trường nguồn riêng. Codebook hiện là `human-review-draft-v1`, chứa định nghĩa tổng quát trong gói human review, không chứa annotation AI. `approved_by=null`, `label_policy=null`: chưa được con người phê duyệt. Các type trong AI reviews được bảo tồn như ghi chú tham khảo lịch sử, không dùng làm taxonomy human hay đầu vào metric. Không tính purity/agreement từ AI trong báo cáo hiện hành.

Mỗi phiếu đặt review AI hoàn tất ở đầu `reviews`, tiếp theo là slot human còn pending. `evidence` đã bổ sung đường dẫn source/correct/đề/log và toàn bộ `failed_test_ids` đối chiếu log gốc. Bốn mẫu Unclear (270276, 271188, 271213, 271920) ghi cụ thể evidence cần từ người học để phân biệt sơ suất và misconception; đây là kết luận đã hoàn tất, không phải thiếu annotation. Việc bổ sung truy vết không tạo reviewer mới, không thay quyết định hoặc confidence, và không bổ sung dữ liệu human giả định.

## Bảng AI annotation

Chi tiết dòng code, input/expected/actual, diff bản sửa, nguyên nhân thay thế và ngữ cảnh cụm nằm trong từng `evidence` ở JSON. `—` là type null theo schema cho No/Unclear. Các giá trị A/B/C dưới đây là `same_cause_as_cluster`, không phải cluster ID.

| Bài / submission | Has misconception | Misconception type | Confidence | A | B | C |
|---|---|---|---|---|---|---|
| 2812 / 270276 | Unclear | — | Medium (3/5) | Partially | Partially | Partially |
| 2812 / 270277 | No | — | High (4/5) | No | Partially | No |
| 2812 / 270283 | Yes | printf_format_argument_contract | Medium (3/5) | Partially | Partially | Partially |
| 2812 / 270285 | No | — | High (5/5) | Partially | Partially | Partially |
| 2812 / 270293 | No | — | High (5/5) | Partially | Partially | Partially |
| 2825 / 271154 | Yes | squared_distance_radius_mismatch | Medium (3/5) | Partially | Partially | Partially |
| 2825 / 271163 | No | — | High (5/5) | Partially | Partially | Partially |
| 2825 / 271173 | No | — | High (5/5) | No | Partially | No |
| 2825 / 271188 | Unclear | — | Medium (3/5) | No | Partially | No |
| 2825 / 271203 | Yes | independent_if_else_binding | Medium (3/5) | Partially | Partially | Partially |
| 2825 / 271213 | Unclear | — | Medium (3/5) | Partially | Partially | Partially |
| 2833 / 271912 | No | — | High (5/5) | Partially | Partially | Partially |
| 2833 / 271916 | Yes | invalid_permutation_correction | High (4/5) | No | Partially | No |
| 2833 / 271920 | Unclear | — | Medium (3/5) | No | Partially | No |
| 2833 / 271965 | Yes | ordered_vs_unordered_triangle_count | High (4/5) | Partially | Partially | Partially |
| 2833 / 271975 | Yes | candidate_filter_as_loop_guard | High (4/5) | Partially | No | Partially |
| 2833 / 271986 | Yes | assignment_in_boolean_equality_test | Medium (3/5) | No | Partially | No |

Tổng: **7 Yes, 6 No, 4 Unclear**. Các loại đề xuất lần lượt biểu diễn: hợp đồng format/đối số printf; so khoảng cách bình phương với bán kính; liên kết else với if; hiệu chỉnh bội số hoán vị sai; đếm có thứ tự thay cho không thứ tự; dùng điều kiện lọc làm điều kiện dừng; gán thay so sánh trong biểu thức boolean. Hai trường hợp dấu chấm 270285/270293 được gán No vì mô tả đề có dấu chấm nhưng oracle không có.

## Mixed causes sau khi xem đầy đủ thành viên

`Partially` ghi nhận cụm trộn nguyên nhân, không đồng nghĩa cùng misconception. `No` dùng khi không tìm thấy cơ chế chung cụ thể với các thành viên còn lại (ví dụ 270277 so với 270297, hay 271975 so với 271983 ở B). Không có phiếu `Yes` về same-cause: các cụm chứa 17 mẫu đều có phản ví dụ. Các mẫu bổ sung chỉ là evidence ngữ cảnh, không được thêm vào mẫu số purity hoặc coi là đã có phiếu annotation.

| Bài | Cụm A/C và số thành viên toàn cụm | Bằng chứng mixed-cause |
|---|---|---|
| 2812 | 0 (12) | Nhóm dấu chấm 270285/270293 đối lập hard-code -12 ở 270280, thiếu phân loại ở 270330 và sai scanf ở 270357. |
| 2812 | 1 (2) | 270277 in thừa số; 270297 dùng `a=='0'`, input 0 cho output rỗng. |
| 2812 | 2 (5) | Thiếu đối số printf ở 270276/270283/270296; 270272 sai phạm vi nhánh; 270305 chỉ thừa dấu chấm nhánh dương. |
| 2825 | 0 (7) | 271154/271211 sai đại lượng so sánh; 271203/271205 sai else; 271152 thiếu on; 271216 sai dấu chấm; 271228 dùng r thay k. |
| 2825 | 1 (2) | 271173 typo Cicle; 271188 dùng thông báo on cho outside. |
| 2825 | 2 (13) | Dấu chấm, chữ hoa, debug output, scanf thiếu địa chỉ ở 271206 và thứ tự input sai ở 271213/271220. |
| 2833 | 0 (6) | Thiếu s ở 271912/271927/271993; hướng vòng sai ở 271920; bài chưa triển khai ở 271989; thiếu tiền tố ở 272004. |
| 2833 | 1 (2) | 271916 hiệu chỉnh hoán vị; 271986 gán trong kiểm tra góc. |
| 2833 | 2 (10) | Đếm hoán vị, dừng sớm, OR thay AND, dấu ; sau for và cập nhật count sai phạm vi. |

A/C có cùng membership trong ngữ cảnh này: cả 9 cụm của mỗi cấu hình có bằng chứng mixed-cause khi xem toàn bộ thành viên. Kết luận cũ chỉ dựa trên 17 mẫu tìm được 6 cụm; không còn đủ để mô tả toàn cụm bài 2812.

B/2812/0 (16 thành viên), B/2825/0 (20) và B/2833/0 (15) đều mixed-cause. **B/2833/2 cũng mixed-cause**: 271975 dừng sớm, trong khi 271983 vừa dùng OR vừa đếm hoán vị; N=4 lần lượt in 10 và 64 thay 13. Bốn cụm B này chứa các mẫu được annotation; không dùng kết luận đó làm tỷ lệ toàn bộ cụm B.

## Human validation: chưa có metric

**Human review 0/17, adjudication 0/17; purity, raw agreement và Cohen’s kappa đều null (không phải 0).** 17 AI annotations phía trên chỉ là tham khảo kỹ thuật nội bộ. Các số purity AI từng được tạo trong lượt thăm dò trước đã được rút khỏi báo cáo hiện hành; scorer không còn tính các số đó. Không dùng AI làm ground truth hoặc bằng chứng expert validation.

[Metric JSON](../results/itsp/expert_validation_metrics.json) báo số record theo nguồn và các chỉ số human chưa đủ điều kiện. [Protocol human review](itsp_human_review_protocol.md) quy định validate → merge/khóa vòng độc lập/adjudication → purity → raw agreement → kappa → Results/Discussion. Agreement phải dùng các lượt độc lập trước adjudication, không dùng nhãn đã thống nhất.

Chỉ phát [gói human riêng](../results/itsp/human_review_packet.zip) ở vòng 1; không gửi tài liệu AI này hoặc JSON chứa AI cho chuyên gia. Codebook cần người thật phê duyệt trước chấm. Tính độc lập không thể được tạo bằng đổi reviewer_id hay coi lượt AI đọc lại là reviewer thứ hai.

## Kiểm tra sau cập nhật

- `.venv/Scripts/python.exe scripts/score_itsp_experts.py`: thành công; hash assignment khớp bản đóng băng, human metrics null và 17 AI reviews ở mục riêng.
- `.venv/Scripts/python.exe -m pytest -q`: **64 passed, 3 subtests passed**.
- `.venv/Scripts/python.exe -m ruff check .`: **All checks passed**.
- Kiểm tra schema v1, đúng 17 ID, 17 review AI hoàn tất, 17 slot human và adjudication pending, mọi rating A/B/C có giá trị; hash annotation trong metric khớp file hiện tại.
- Chỉ thay annotation, tài liệu, báo cáo và phần tách nguồn của scorer offline cùng tests tương ứng. Không đổi pipeline, feature, thuật toán hoặc assignment clustering; không thêm LLM/GNN vào pipeline.

## Chọn mẫu và khả năng suy rộng

Đối chiếu `scripts/run_itsp_experiments.py` và ba kết quả `agglomerative_combined_k3_w0.8_seed42.json`: lấy toàn bộ 9 medoid train (3/bài), thêm mẫu holdout xa medoid nhất trong mỗi cụm có holdout (8 mẫu). Khi khoảng cách bằng nhau, chọn ID lớn nhất theo thứ tự từ điển qua `max((distance, sid))`; đây là quy tắc định danh, không phải ngẫu nhiên. Bài 2812: 3 medoid + 2 holdout vì cụm 1 không có holdout. Bài 2825 và 2833: mỗi bài 3+3. Đối chiếu tập ID đúng 17 mẫu trong template, không thêm các phản ví dụ ngoài mẫu từ case review.

Đây là lấy mẫu có chủ đích theo **cấu hình combined cũ**, thiên về tâm cụm train và trường hợp holdout xa nhất. Không đại diện phân bố tần suất lỗi của 59 mẫu eligible, không độc lập với clustering, không đủ ước lượng purity toàn cohort. Dùng cùng 17 ID khi so A/B/C không loại bỏ thiên lệch ưu tiên cấu hình đã dùng để chọn mẫu; không dùng nó để chọn feature/weight rồi báo như test độc lập. Không có student ID, do đó không tuyên bố unseen-student generalization.

## Evidence kỹ thuật từng mẫu

Cluster trong bảng là ID **cấu hình gốc**, chỉ có ý nghĩa trong từng bài; không đồng nhất số cụm giữa bài hoặc A/B/C. `M`: medoid train; `H`: mẫu holdout xa nhất. Dữ liệu máy đọc và đường dẫn đầy đủ: [review_hypotheses.json](../results/itsp/review_hypotheses.json).

| Bài / submission | Cụm | Vai trò | Lỗi quan sát và bằng chứng | Misconception dự kiến / giới hạn |
|---|---:|---|---|---|
| 2812 / [270276](../data/raw/itsp/dataset/Lab-3/2812/270276_buggy.c) / [correct](../data/raw/itsp/dataset/Lab-3/2812/270276_correct.c) | 2 | H | Nhánh dương gọi printf("%.4f is positive") thiếu a; bản sửa thêm a. Input 1: expected 1.0000, actual 0.0000; 101 cũng sai; log pass 5/7. | Có thể chưa hiểu đối số tương ứng format printf; cũng có thể bỏ sót khi gõ. Thiếu đối số variadic có hành vi không xác định; không khẳng định giá trị output ổn định. |
| 2812 / [270277](../data/raw/itsp/dataset/Lab-3/2812/270277_buggy.c) / [correct](../data/raw/itsp/dataset/Lab-3/2812/270277_correct.c) | 1 | M | Nhánh zero in "%f input is zero"; bản sửa bỏ %f. Hai input zero in 0.000000 trước thông báo; log pass 5/7. | Chưa đủ bằng chứng misconception. Bằng chứng lỗi output contract, chưa có bằng chứng hiểu sai phép so sánh zero. |
| 2812 / [270283](../data/raw/itsp/dataset/Lab-3/2812/270283_buggy.c) / [correct](../data/raw/itsp/dataset/Lab-3/2812/270283_correct.c) | 2 | M | Hai nhánh khác zero có %.4f và %n nhưng không truyền đối số, thêm dấu phẩy; bản sửa bỏ ,%n và thêm n. Các test khác zero sai; log pass 2/7. | Có thể nhầm cách dùng printf/format specifier. Nhiều lỗi đồng thời; %n không phải newline và đòi hỏi con trỏ hợp lệ. Không xác nhận crash hay hiểu lầm bền vững. |
| 2812 / [270285](../data/raw/itsp/dataset/Lab-3/2812/270285_buggy.c) / [correct](../data/raw/itsp/dataset/Lab-3/2812/270285_correct.c) | 0 | H | Cả ba chuỗi output thừa dấu chấm so với oracle; bản sửa chỉ bỏ dấu chấm. Giá trị số và từ chỉ dấu đúng trong cả bảy log; pass 0/7. | Chưa đủ bằng chứng misconception. Main.c mô tả và ví dụ có dấu chấm nhưng oracle không có; không quy lỗi này thành misconception. |
| 2812 / [270293](../data/raw/itsp/dataset/Lab-3/2812/270293_buggy.c) / [correct](../data/raw/itsp/dataset/Lab-3/2812/270293_correct.c) | 0 | M | Cả ba chuỗi output thừa dấu chấm so với oracle; bản sửa chỉ bỏ dấu chấm. Giá trị số và từ chỉ dấu đúng trong cả bảy log; pass 0/7. | Chưa đủ bằng chứng misconception. Main.c mô tả và ví dụ có dấu chấm nhưng oracle không có; không quy lỗi này thành misconception. |
| 2825 / [271154](../data/raw/itsp/dataset/Lab-4/2825/271154_buggy.c) / [correct](../data/raw/itsp/dataset/Lab-4/2825/271154_correct.c) | 0 | M | s = (x-x1)^2 + (y-y1)^2 - r; bản sửa thay -r bằng -r*r. Bốn test inside/on bị in outside, ba test outside pass; pass 3/7. | Có thể nhầm khoảng cách bình phương với bán kính khi so sánh. Có bằng chứng sai công thức; chưa đủ để phân biệt hiểu sai với thiếu phép nhân khi gõ. |
| 2825 / [271163](../data/raw/itsp/dataset/Lab-4/2825/271163_buggy.c) / [correct](../data/raw/itsp/dataset/Lab-4/2825/271163_correct.c) | 2 | M | Cả ba chuỗi output thiếu dấu chấm; bản sửa thêm dấu chấm. Đúng từ inside/on/outside ở cả bảy log nhưng pass 0/7. | Chưa đủ bằng chứng misconception. Lỗi output contract; không phải bằng chứng hiểu sai hình học. |
| 2825 / [271173](../data/raw/itsp/dataset/Lab-4/2825/271173_buggy.c) / [correct](../data/raw/itsp/dataset/Lab-4/2825/271173_correct.c) | 1 | M | Nhánh outside in Cicle thay vì Circle; bản sửa đổi đúng từ này. Ba test outside fail; bốn test inside/on pass. | Chưa đủ bằng chứng misconception. Lỗi chính tả; không tự gán nhãn misconception. |
| 2825 / [271188](../data/raw/itsp/dataset/Lab-4/2825/271188_buggy.c) / [correct](../data/raw/itsp/dataset/Lab-4/2825/271188_correct.c) | 1 | H | Nhánh else khi l>0 in on thay vì outside; bản sửa thêm l>0 và in outside. Ba test outside in on; pass 4/7. | Có thể nhầm ánh xạ dấu của biểu thức với vị trí ngoài đường tròn. Công thức và các nhánh còn lại đúng; có thể lỗi copy/paste string, không chứng minh nhầm khái niệm. |
| 2825 / [271203](../data/raw/itsp/dataset/Lab-4/2825/271203_buggy.c) / [correct](../data/raw/itsp/dataset/Lab-4/2825/271203_correct.c) | 0 | H | Hai if độc lập; else gắn với if(n>0), nên n<0 in cả inside và on. Bản sửa thành chuỗi loại trừ nhau. Hai input inside in Inside+On nối nhau; pass 5/7. | Có thể chưa hiểu else gắn với if gần nhất và sự khác nhau giữa if độc lập/else-if. Suy luận control flow từ source và log; chưa có xác nhận từ người học. |
| 2825 / [271213](../data/raw/itsp/dataset/Lab-4/2825/271213_buggy.c) / [correct](../data/raw/itsp/dataset/Lab-4/2825/271213_correct.c) | 2 | H | scanf đọc x,y,x1,y1,r thay vì x,y,r,x1,y1; bản sửa đổi thứ tự ba địa chỉ cuối. Input 0 0 5 3 7: expected outside, actual inside; pass 2/7. | Có thể nhầm ánh xạ thứ tự trường input sang biến. Có thể chỉ là sơ suất; cả hai bản thiếu include math.h cho sqrt, không xác nhận tính portable của build lịch sử. |
| 2833 / [271912](../data/raw/itsp/dataset/Lab-4/2833/271912_buggy.c) / [correct](../data/raw/itsp/dataset/Lab-4/2833/271912_correct.c) | 0 | H | Chuỗi in triangle thay vì triangles; bản sửa chỉ thêm s. Cả sáu giá trị đếm khớp oracle, nhưng pass 0/6. | Chưa đủ bằng chứng misconception. Lỗi output contract; không phải bằng chứng sai tổ hợp. |
| 2833 / [271916](../data/raw/itsp/dataset/Lab-4/2833/271916_buggy.c) / [correct](../data/raw/itsp/dataset/Lab-4/2833/271916_correct.c) | 1 | H | Duyệt ba cạnh độc lập 1..n rồi sửa count=((count-n)/n)+n; bản sửa bỏ công thức và dùng b từ a, c từ b. N=4: 11 thay vì 13; N=5:17 thay vì22; pass3/6. | Có thể nhầm loại hoán vị khi đếm tổ hợp; hệ số lặp phụ thuộc cạnh bằng nhau, không thể chia cho n. Khác cơ chế cụ thể với đếm mọi hoán vị không hiệu chỉnh; nhãn cần codebook quyết định mức độ chi tiết. |
| 2833 / [271920](../data/raw/itsp/dataset/Lab-4/2833/271920_buggy.c) / [correct](../data/raw/itsp/dataset/Lab-4/2833/271920_correct.c) | 0 | M | Vòng ngoài for(i=n;i>=1;i++) tăng i thay vì giảm; bản sửa đổi sang i--. Output rỗng ở cả sáu test; log WRONG_ANSWER, pass0/6. | Có thể chưa hiểu quan hệ hướng cập nhật và điều kiện dừng vòng lặp. Không khẳng định timeout: log không có verdict timeout và signed overflow có thể dẫn tới hành vi không xác định. |
| 2833 / [271965](../data/raw/itsp/dataset/Lab-4/2833/271965_buggy.c) / [correct](../data/raw/itsp/dataset/Lab-4/2833/271965_correct.c) | 2 | M | Ba vòng đều 1..N nên đếm các hoán vị cạnh; bản sửa dùng b từ a và c từ b. N=4:34 thay vì13; chỉ N=1 pass, tổng1/6. | Có thể nhầm bộ ba có thứ tự với tam giác không phân biệt hoán vị cạnh. Lỗi đếm được củng cố bởi diff; chưa chứng minh hiểu lầm bền vững. |
| 2833 / [271975](../data/raw/itsp/dataset/Lab-4/2833/271975_buggy.c) / [correct](../data/raw/itsp/dataset/Lab-4/2833/271975_correct.c) | 2 | H | while(c<=b && a<c+b) dừng trước khi c lớn hơn có thể hợp lệ; bản sửa đưa a<c+b vào if trong vòng. N=4:10 thay vì13; N=3:6 thay vì7; pass2/6. | Có thể nhầm điều kiện chọn phần tử với điều kiện duyệt hết ứng viên. Phân tích tĩnh: khi guard false ở c=1, ứng viên lớn hơn bị bỏ qua; không thực thi chương trình. |
| 2833 / [271986](../data/raw/itsp/dataset/Lab-4/2833/271986_buggy.c) / [correct](../data/raw/itsp/dataset/Lab-4/2833/271986_correct.c) | 1 | M | Điều kiện phụ có x=0/y=0/z=0 thay vì so sánh, cùng nhiều nhánh lọc góc; bản sửa bỏ toàn bộ điều kiện phụ. N=5:21 thay vì22; N=7:49 thay vì50; pass4/6. | Có thể nhầm phép gán với so sánh hoặc lọc sai trường hợp góc vuông. Diff xóa cả điều kiện nên chưa cô lập nguyên nhân; không gán một nhãn duy nhất hay khẳng định sửa == là đủ. |

## Quan sát lịch sử chỉ trên 17 mẫu (trước khi mở rộng ngữ cảnh)

- **2825, cụm 0:** 271154 sai công thức bán kính bình phương; 271203 sai cấu trúc if/else. **Cụm 1:** 271173 typo Cicle; 271188 chọn sai thông báo nhánh outside, có thể copy/paste. **Cụm 2:** 271163 thiếu dấu chấm; 271213 đọc sai thứ tự input.
- **2833, cụm 0:** 271920 sai hướng cập nhật vòng lặp; 271912 chỉ sai từ triangle. Hai mẫu có khoảng cách feature bằng 0 nhưng nguyên nhân khác nhau. **Cụm 1:** 271986 điều kiện gán/lọc góc; 271916 hiệu chỉnh hoán vị bằng công thức sai. **Cụm 2:** 271965 đếm hoán vị; 271975 dừng vòng trước ứng viên hợp lệ.
- **2812, cụm 0:** hai mẫu cùng lỗi dấu chấm so với oracle. **Cụm 1:** chỉ một mẫu được chọn, không thể đánh giá sự đồng nhất. **Cụm 2:** cả hai liên quan thiếu đối số printf, nhưng 270283 còn có %n và dấu phẩy; không gọi hai mẫu là cùng một misconception đã xác nhận.

Như vậy có bằng chứng định tính nhiều cơ chế trong 6 cụm (ba cụm của mỗi bài 2825/2833) ở tập đã duyệt. Đây không phải tỷ lệ cụm không thuần của toàn dataset. Các cặp 2825/1 và 2833/0 cho thấy khoảng cách 0 không bảo đảm cùng lỗi. Các nhãn kỹ thuật ở JSON dùng để truy vết quan sát, không dùng làm ground truth hay tính purity.

## Mapping A/B/C đã đóng băng

### Đối chiếu A/B/C, cùng 17 mẫu, seed42

Đây là assignment từ [ablation cố định](../results/itsp/abc_review_assignments.json),
không phải nhãn lỗi. Mỗi số cluster chỉ có nghĩa trong cặp (bài, cấu hình); không so số ID giữa cấu hình.

| Bài | Submission | A | B | C |
|---|---|---:|---:|---:|
| 2812 | 270276 | 2 | 0 | 2 |
| 2812 | 270277 | 1 | 0 | 1 |
| 2812 | 270283 | 2 | 0 | 2 |
| 2812 | 270285 | 0 | 0 | 0 |
| 2812 | 270293 | 0 | 0 | 0 |
| 2825 | 271154 | 0 | 0 | 0 |
| 2825 | 271163 | 2 | 0 | 2 |
| 2825 | 271173 | 1 | 0 | 1 |
| 2825 | 271188 | 1 | 0 | 1 |
| 2825 | 271203 | 0 | 0 | 0 |
| 2825 | 271213 | 2 | 0 | 2 |
| 2833 | 271912 | 0 | 0 | 0 |
| 2833 | 271916 | 1 | 0 | 1 |
| 2833 | 271920 | 0 | 0 | 0 |
| 2833 | 271965 | 2 | 0 | 2 |
| 2833 | 271975 | 2 | 2 | 2 |
| 2833 | 271986 | 1 | 0 | 1 |

Ở seed42, A/C cùng assignments; sáu cụm có cơ chế khác nhau đã nêu cũng là phản ví dụ cho A.
B gom cả 5 mẫu 2812 vào cụm 0, cả 6 mẫu 2825 vào cụm 0, 5/6 mẫu 2833 vào cụm 0 của từng bài.
Cụm B/2812/0 trộn thiếu đối số printf và output punctuation; B/2825/0 trộn công thức, typo,
if/else, input order; B/2833/0 trộn typo, hướng cập nhật và cơ chế đếm/lọc.
Không có mẫu review của các cụm B nhỏ còn lại (trừ B/2833/2), nên không kết luận về sự đồng nhất của chúng.
Fidelity B seed42 bằng majority ở cả ba bài; không chuyển kết quả đó thành bằng chứng về misconception.

