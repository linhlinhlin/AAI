# Bản AI gán nhãn thử

Mở `index.html` bằng Chrome/Edge. Có 48 bài theo đúng thứ tự phiếu ITSP trước đó,
lọc theo đề, mở code/test để kiểm tra. Bản Markdown: `nhan_ai.md`.
JSON: `nhan_ai.json`, schema riêng `ai_case_review_v1`, không phải schema phiếu con người
và cũng không phải response schema của module annotation theo cluster.

## Cách hiểu

- AI đã đọc code và log để đề xuất nhãn cơ chế lỗi, diễn đạt thành NẾU–VÀ–THÌ.
- Đây là lời giải thích do AI viết, không phải một lần chạy thuật toán quy nạp mới.
  Luật cây do hệ thống học và các report lịch sử vẫn giữ nguyên.
- `supported` chỉ có nghĩa AI tìm thấy căn cứ trong code/log, không phải con người
  đã xác nhận. Bài có nhiều cơ chế giữ `decision: multiple`.
- `annotation_source: ai`, `gold_standard: false`, `human_validated: false`,
  `gold_label: null`, `cognitive_status: unassessed`. Không dùng bộ này để tuyên bố
  độ chính xác misconception với gold độc lập.
- Không giả danh giảng viên, không thêm tên người duyệt, không điền vào phiếu chấm mù.
  JSON này bị bộ tiếp nhận phiếu con người từ chối.
- Các nhận xét trước đó của AI/cluster đã xuất hiện trong hội thoại, nên đây không
  phải lượt đánh giá độc lập. Việc người dùng đã xem bản này phải được tính đến
  nếu sau đó tổ chức chấm mù.

## Phạm vi bằng chứng

Nguồn: `.cache/teacher-validation-itsp-20260928/evidence.json`, gắn bằng `packet_id`
và `case_id`. Có toàn bộ code/log gốc trong JSON, số dòng và test tham chiếu.
Chỉ phân tích log lịch sử, không chạy C, không gọi API ngoài, không mở sealed test.
Gói chưa có đề bài gốc; nhãn phụ thuộc quy ước input/output cần được người phụ trách
đối chiếu. Đặc biệt bài 2812 có bất nhất dấu chấm giữa ví dụ đề và oracle đã được
ghi nhận trong `deliverables/ai_studio_code.review.md`.

Giọng văn được viết tự nhiên để trình bày và trao đổi chuyên môn. Nguồn tác giả
vẫn được ghi rõ là AI. Chưa có số đo accuracy hoặc nhãn gold nào được tạo thêm.
