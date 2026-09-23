# Codebook dự thảo cho đánh giá độc lập

Phiên bản: `human-review-draft-v1`. **Chưa được chuyên gia phê duyệt.** Đây là tài liệu hướng dẫn do trợ lý chuẩn bị để chuyên gia sửa/chốt; không phải taxonomy đã được kiểm chứng. Không chứa annotation AI, gợi ý nhãn theo submission, cluster ID hoặc lời giải cho 17 phiếu. Các loại dưới đây là các nhóm khái niệm tổng quát, không được suy ngược từ số cụm.

## Quyết định trước, loại sau

| Quyết định | Điều kiện sử dụng | Không được suy diễn |
|---|---|---|
| Yes | Code thể hiện một quy tắc sai về khái niệm; truy vết/test phù hợp với quy tắc đó, và reviewer giải thích vì sao evidence nghiêng về hiểu sai. | Một test fail tự nó không đủ chứng minh misconception. |
| No | Evidence ủng hộ lỗi thao tác, chính tả, định dạng, bài chưa hoàn thiện hoặc bất nhất đề/oracle, không cho thấy quy tắc khái niệm sai. | Không có nghĩa người học không bao giờ có hiểu sai. |
| Unclear | Đã xem nhưng evidence không đủ phân biệt hiểu sai với sơ suất, hoặc có các giải thích cạnh tranh chưa phân giải. | Không dùng làm ký hiệu cho phiếu chưa đọc. |

Một lần sửa đúng hoặc nhiều test fail từ cùng một dòng code không phải bằng chứng độc lập về nhận thức. Nêu giả thuyết thay thế, không cố biến mọi bug thành misconception. Không dùng kết quả cụm để đổi quyết định vòng 1.

## Các loại khái niệm đề xuất

Chỉ chọn type khi `misconception=Yes`. Mỗi mã là một nhóm khái niệm; mô tả cơ chế cụ thể trong evidence. Cùng type chưa có nghĩa cùng nguyên nhân cụ thể.

| Mã | Định nghĩa / bao gồm | Loại trừ và ranh giới |
|---|---|---|
| C_IO_CONTRACT | Hiểu sai cách lời gọi nhập/xuất ghép định dạng, giá trị, địa chỉ hoặc thứ tự dữ liệu. | Chuỗi thông báo sai chính tả/thiếu dấu câu đơn thuần; chỉ đọc nhầm một trường input khi chưa có bằng chứng hiểu sai. |
| C_EXPRESSION_SEMANTICS | Hiểu sai ý nghĩa, kiểu, độ ưu tiên hoặc hiệu ứng phụ của toán tử/biểu thức C. | Công thức toán học sai dù các toán tử C được dùng đúng: MATH_MODEL. |
| C_BRANCH_SELECTION | Hiểu sai phạm vi nhánh, liên kết điều kiện hoặc tính loại trừ giữa các nhánh. | Biểu thức điều kiện sai do ngữ nghĩa toán tử: C_EXPRESSION_SEMANTICS; chỉ in nhầm chuỗi chưa đủ. |
| C_ITERATION_MODEL | Hiểu sai khởi tạo, cập nhật, phạm vi thân vòng, điều kiện tiếp tục/dừng hoặc khả năng duyệt đủ ứng viên. | Chỉ đếm lặp các đối tượng tương đương dù vòng chạy đúng dự kiến: ENUMERATION_IDENTITY. Một ký tự cập nhật sai có thể chỉ là sơ suất. |
| MATH_MODEL | Hiểu sai đại lượng, quan hệ, điều kiện hoặc công thức toán học cần mô hình hóa trong đề. | Cú pháp/toán tử C sai; lỗi format; đếm các biểu diễn tương đương dùng ENUMERATION_IDENTITY. |
| ENUMERATION_IDENTITY | Hiểu sai khi nào hai ứng viên biểu diễn cùng một đối tượng và cách loại trùng/hiệu chỉnh số lần đếm. | Bỏ ứng viên vì dừng duyệt sớm: C_ITERATION_MODEL; kiểm tra tính hợp lệ hình học sai: MATH_MODEL. |
| NUMERIC_REPRESENTATION | Hiểu sai cách biểu diễn số, chuyển kiểu, chia nguyên, giới hạn hay độ chính xác làm thay đổi giá trị tính toán. | Số chữ số được in khác yêu cầu nhưng giá trị tính đúng không tự chứng minh loại này. |
| OTHER_CONCEPT | Có evidence về một quy tắc khái niệm sai nằm ngoài các nhóm trên. Phải đặt tên khái niệm và định nghĩa trong evidence. | Không dùng để che thiếu evidence; trường hợp chưa xác định type có thể giữ Yes/type null. |

## Nhiều lỗi và nhãn chính

Ghi mọi cơ chế có evidence. Đề xuất `single_primary`: chọn khái niệm giải thích nguyên nhân trực tiếp tạo failure đã dẫn chứng; không chọn theo cluster, tần suất nhãn hoặc nhãn AI. Nếu hai cơ chế cùng cần thiết và không có cơ sở ưu tiên, giữ Yes/type null, mô tả cả hai để adjudication xử lý. Không nối hai mã thành một type mới. Nếu chuyên gia muốn đa nhãn, cần protocol riêng; scorer hiện chưa hỗ trợ purity đa nhãn.

Trước khi tính TYPE purity, chuyên gia phải xem các trường hợp OTHER_CONCEPT và chốt chúng có đủ đồng nhất để là một loại hay cần tách. Không gom các khái niệm không liên quan thành OTHER_CONCEPT chỉ để có coverage cao. Nếu chưa chốt được, adjudication type giữ null, loại khỏi mẫu số và công bố số thiếu type.

## Chốt trước vòng chấm

Người điều phối mời chuyên gia sửa định nghĩa và chốt cùng một phiên bản trước khi chấm 17 mẫu, không cung cấp nhãn tham khảo hoặc ví dụ từ chính 17 mẫu để hiệu chỉnh người chấm. Sau khi được người thật xác nhận, người điều phối điền `approved_by`, phiên bản cuối, `label_policy=single_primary` và danh sách mã đã duyệt trong bản phiếu phân phối. Ghi tên/mã người duyệt, ngày, phiên bản và hash codebook vào biên bản riêng. Không coi bản dự thảo này là đã được duyệt.

Nếu đổi taxonomy sau khi đã chấm, giữ bản gốc. Khi cần agreement theo loại mới, tổ chức chấm lại độc lập theo phiên bản mới hoặc báo không đủ điều kiện; không sửa hồi tố hai người về cùng nhãn rồi tính agreement.
