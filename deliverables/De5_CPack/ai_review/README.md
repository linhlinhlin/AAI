# C-Pack-IPAs — 150 nhãn AI để người dùng kiểm tra

Mở `index.html`. Thứ tự bài trùng phiếu C-Pack 150 bài đã tạo trước đó.
Không phải 48 bài ITSP và không phải toàn bộ 2.151 thành viên của 69 cụm.

AI đã đọc code và log từng bài, đề xuất nhãn cơ chế/sai khác, lý do và cách kiểm tra.
Phân loại: 114 `supported`, 30 `multiple`, 6 `uncertain`. Đây là nhận định AI,
không phải số nhãn đã được người dùng duyệt hay độ chính xác.
Mọi `gold_label` vẫn null, `human_validated` false, `cognitive_status` unassessed.

## Bạn kiểm tra

1. Lọc theo bài tập hoặc mức nhận định. Nên xem trước “Cần kiểm tra thêm” và “Nhiều lỗi”.
2. Đọc dấu hiệu và mở code/log gốc. Chuỗi JSON làm rõ `\n`, `\t` và output rỗng.
3. Chọn Đồng ý, Sửa nhãn, Không đồng ý hoặc Chưa đủ bằng chứng cho từng bài.
   Khi sửa/bác bỏ, ghi lý do. Chưa xem bài nào thì giữ Chưa kiểm tra.
4. Nhập tên/mã người kiểm tra, bấm **Tải kết quả kiểm tra** rồi gửi lại file
   `cpack_ket_qua_kiem_tra.json` để tiếp nhận. Không có nút tự duyệt cả bộ.
5. Nháp tự lưu trên trình duyệt; mở lại chọn Khôi phục nháp. Tải JSON trước khi đổi
   máy hoặc xóa dữ liệu trình duyệt. Bản HTML không tự ghi nhãn vào file nguồn.

JSON kết quả có schema `cpack_assisted_human_review_v1`, gắn `packet_id`, hash bản
AI đã xem, `case_id`, quyết định và nhãn sửa. Đây là **người kiểm tra sau khi xem AI**,
không phải phiếu chấm mù và không tự phân xử. Việc tải file chưa tự cập nhật gold
hoặc cơ sở dữ liệu app. Các bài chưa xem vẫn pending.

## Truy vết và giới hạn

- `nhan_ai.json` dùng schema `ai_case_review_v1`, nguồn AI được giữ rõ ràng.
- Packet: `.cache/teacher-validation-cpack-20260928/evidence.json`, có fingerprint,
  SHA256 file, hash source từng bài, số dòng/test và toàn bộ code/log không cắt.
- Các câu NẾU–VÀ–THÌ là diễn giải do AI viết, không phải một lần quy nạp luật mới.
- Không chạy code C, không gọi API bên ngoài, không sử dụng sealed test hay nhãn
  của ITSP. Không đưa nhãn vào đặc trưng phân cụm.
- Gói thiếu đề bài gốc, chưa replay xác nhận tương ứng suite lịch sử. Những trường
  hợp code thực hiện tác vụ khác oracle được giữ uncertain, cần kiểm tra ánh xạ.
- Trường hợp hành vi không xác định không được diễn giải thành output tất định;
  sai khoảng trắng không được tự gọi là hiểu lầm thuật toán.
- Các lỗi tiềm ẩn ngoài test có sẵn được nêu riêng, không bịa test đã chạy.
- Phiếu chấm mù `../reviewer_1.html` và `../reviewer_2.html` giữ nguyên. Người đã
  xem bản AI không xác nhận mình chấm mù cùng những bài này.

Trên app: mở thư viện C-Pack → **AI gán nhãn · 150 bài để kiểm tra** để xem nhãn
và bằng chứng. Giao diện offline này có thêm ô phản hồi và xuất kết quả kiểm tra.
