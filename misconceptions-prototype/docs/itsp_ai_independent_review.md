# Đối chiếu AI độc lập — chỉ dành cho người điều phối

Không gửi báo cáo này, file AI mới/cũ hoặc thứ tự ưu tiên có lý do cho người chấm trước khi khóa vòng độc lập. Người đã xem nhãn AI không được tự khai chấm mù. AI không phải expert ground truth.

Đã đọc 17 hồ sơ / 68 file evidence / 113 test lịch sử, không chạy code C. Kết quả mới: **6 Yes, 8 No, 3 Unclear**. **3 bất đồng quyết định**. Sáu mẫu cùng Yes khác chuỗi type nhưng tương ứng cùng nhóm khái niệm theo ánh xạ tạm thời; thêm một khác type là hệ quả Yes → Unclear. Không tính purity/agreement/kappa từ AI.

Bản AI độc lập đã được ghi và hash trước khi mở AI cũ: `6e159b2db8975a1f4d6d70a85cc464ba319148b238ed24a27a47db3a20ed27bd`. Hash là dấu kiểm tra toàn vẹn, không phải bằng chứng mật mã độc lập về thứ tự thời gian; thứ tự thao tác nằm trong lịch sử task.

## Ưu tiên human

P1: 3 bất đồng quyết định. P2: 7 mẫu còn mơ hồ, có giả thuyết cạnh tranh hoặc xung đột đề/oracle. P3: 7 mẫu còn lại vẫn cần chấm. Tất cả 17 đều thuộc tập review; ưu tiên không có nghĩa loại mẫu. Danh sách dùng để điều phối/adjudication sau khóa vòng 1, không làm đáp án gợi ý trước vòng mù.

| Ưu tiên | Submission | AI cũ → mới | Human cần kiểm tra |
|---|---|---|---|
| P1 | itsp-2825-271154_buggy | Yes → Unclear | Ưu tiên phân biệt công thức power of point sai với thiếu một toán hạng; yêu cầu lý do nếu chọn Yes. |
| P1 | itsp-2825-271188_buggy | Unclear → No | Kiểm tra liệu có bằng chứng ngoài literal để gán MATH_MODEL hoặc C_BRANCH_SELECTION; không suy từ bản sửa thêm điều kiện. |
| P1 | itsp-2825-271213_buggy | Unclear → No | Xác nhận lỗi ánh xạ input theo đề; chỉ gán C_IO_CONTRACT khi có thêm evidence về cách scanf hoạt động. |
| P2 | itsp-2812-270276_buggy | Unclear → Unclear | Reviewer cần giải thích vì sao thiếu đối số một lần đủ hoặc chưa đủ cho Yes; nếu cần hỏi người học cách printf lấy giá trị. |
| P2 | itsp-2812-270283_buggy | Yes → Yes | Kiểm tra ranh giới nhầm format/biến với lỗi sao chép; nếu evidence nhận thức chưa đủ, human có thể chọn Unclear. |
| P2 | itsp-2812-270285_buggy | No → No | Đối chiếu đề với oracle và ghi bất nhất; không coi 0/7 là hiểu sai. |
| P2 | itsp-2812-270293_buggy | No → No | Xác nhận cùng vấn đề đề/oracle, không suy ra lỗi chọn nhánh. |
| P2 | itsp-2825-271203_buggy | Yes → Yes | Human cần đánh giá thiếu từ khóa đơn lẻ có đủ evidence hiểu sai liên kết else hay phải Unclear. |
| P2 | itsp-2833-271920_buggy | Unclear → Unclear | Ưu tiên kiểm tra ranh giới typo/iteration misconception; không đổi log WRONG_ANSWER thành TIMEOUT. |
| P2 | itsp-2833-271986_buggy | Yes → Yes | Kiểm tra precedence và side effect; cân nhắc Yes với Unclear nếu cho rằng lỗi copy đủ giải thích. |
| P3 | itsp-2812-270277_buggy | No → No | Xác nhận chỉ khác chuỗi output; không gán C_IO_CONTRACT chỉ vì test fail. |
| P3 | itsp-2825-271163_buggy | No → No | Xác nhận khác biệt literal; không gán misconception từ số test thất bại. |
| P3 | itsp-2825-271173_buggy | No → No | Kiểm tra chuỗi output; không cần suy diễn quy tắc khái niệm. |
| P3 | itsp-2833-271912_buggy | No → No | Tách đúng số đếm khỏi sai literal. |
| P3 | itsp-2833-271916_buggy | Yes → Yes | Yêu cầu giải thích số hoán vị theo loại tam giác, không gán NUMERIC_REPRESENTATION chỉ vì có phép chia nguyên. |
| P3 | itsp-2833-271965_buggy | Yes → Yes | Phân biệt đếm bộ có thứ tự với đếm tam giác; không gán lỗi cơ chế vòng lặp khi vòng đã chạy đúng phạm vi viết ra. |
| P3 | itsp-2833-271975_buggy | Yes → Yes | Trace c=1 rồi c=2 bằng tay; chốt C_ITERATION_MODEL theo ranh giới codebook với MATH_MODEL. |

## Ba bất đồng cần phân giải

- **271154, Yes → Unclear:** thống nhất lỗi d²−r. AI cũ coi comment “power of point” hỗ trợ hiểu sai đại lượng; AI mới cho rằng chưa phân biệt với bỏ sót `*r`. Human quyết định ngưỡng bằng chứng, không bỏ phiếu giữa AI.
- **271188, Unclear → No:** thống nhất nhánh ngoài in sai literal. AI mới đặt trọng lượng lớn hơn vào công thức và cấu trúc nhánh đúng; AI cũ giữ khả năng nhầm ánh xạ dấu/vị trí.
- **271213, Unclear → No:** thống nhất thứ tự input sai. AI mới áp dụng ranh giới codebook “đọc nhầm trường chưa chứng minh hiểu sai I/O”; AI cũ cho rằng vẫn chưa loại trừ misconception scanf.

## Ranh giới type

Các mã cơ chế cũ không nằm trong danh sách type dự thảo, nên không so sánh chuỗi trực tiếp như bất đồng khái niệm. Bảng dưới chỉ là ánh xạ diễn giải sau khóa AI mới; human phải tự chốt taxonomy.

| Type AI cũ | Nhóm codebook dự thảo |
|---|---|
| printf_format_argument_contract | C_IO_CONTRACT |
| squared_distance_radius_mismatch | MATH_MODEL |
| independent_if_else_binding | C_BRANCH_SELECTION |
| invalid_permutation_correction | ENUMERATION_IDENTITY |
| ordered_vs_unordered_triangle_count | ENUMERATION_IDENTITY |
| candidate_filter_as_loop_guard | C_ITERATION_MODEL |
| assignment_in_boolean_equality_test | C_EXPRESSION_SEMANTICS |

Hai cơ chế hiệu chỉnh hoán vị sai và không loại trùng cùng ENUMERATION_IDENTITY nhưng không mặc nhiên cùng nguyên nhân cụ thể. Chênh lệch confidence được lưu từng mẫu trong JSON, không làm trọng số và không phải bất đồng decision.

## Toàn vẹn và kiểm tra

`expert_annotations.json` vốn đã chứa 17 AI records; chúng được giữ nguyên. 17 human slots và 17 adjudications vẫn pending/null. Không chuyển toàn bộ file sang null hoặc xóa lịch sử AI. Không thay clustering, assignments, metrics hoặc kết quả A/B/C.

- Tests: `64 passed, 3 subtests passed`.
- Lint: `ruff check .` — All checks passed.
- Xem [hướng dẫn thực hiện human review](itsp_human_review_steps.md) và [JSON đối chiếu](../results/itsp/ai_independent_review_comparison.json).
