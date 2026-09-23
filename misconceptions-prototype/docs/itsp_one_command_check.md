# Kiểm tra ITSP bằng một lệnh

Chạy từ bất kỳ thư mục nào trong PowerShell trên máy hiện tại:

```powershell
& E:/AAI/misconceptions-prototype/.venv/Scripts/python.exe E:/AAI/misconceptions-prototype/scripts/check_itsp_review.py
```

Lệnh dùng môi trường Python sẵn có của dự án, tự xác định thư mục làm việc,
chạy toàn bộ pytest và Ruff, validate schema expert bằng `--validate-only`,
kiểm tra 17 hồ sơ/68 evidence files/113 historical tests và tính lại danh sách
bất đồng từ hai nguồn AI. Kiểm tra SHA-256 523 file gốc trước và sau tests
để phát hiện thay đổi expert annotations, pipeline hoặc kết quả A/B/C.
Các test âm chủ động sửa dữ liệu trong bộ nhớ/thư mục tạm để kiểm tra rằng
evidence giả, thiếu mẫu, sai nhãn đối chiếu hoặc chuyển AI thành human bị từ chối.

Cuối terminal có trạng thái ĐẠT/KHÔNG ĐẠT, kết quả tests/lint, số nhãn AI
và ba mẫu cần human ưu tiên kèm câu hỏi cụ thể. Exit code 0 nghĩa là mọi
kiểm tra tự động đạt; exit code 1 nghĩa là có ít nhất một lỗi. Các bước khác
vẫn chạy nếu một bước thất bại. Mỗi subprocess có timeout 5 phút.

Báo cáo của lần chạy hiện tại được ghi đè tại
`results/itsp/ai_review_check_latest.json`, gồm giờ chạy, kết quả và lỗi chi tiết.
Lệnh không ghi lại annotations, không chạy clustering, không chạy code C của
người học và không tính expert metrics. Pytest/Ruff có thể tạo cache thông thường.

**ĐẠT chỉ xác nhận dữ liệu và kiểm tra kỹ thuật; không chứng minh nhãn AI đúng.**
Human validation vẫn pending, expert purity/agreement/kappa vẫn null.
Hash phát hiện thay đổi so với snapshot đã lưu, không xác thực mật mã rằng
review được chấm mù hoặc xác nhận chất lượng nhận thức. Không sửa baseline để
làm kiểm tra xanh. Khi có human annotation hoặc thay đổi hợp lệ về sau, snapshot
này có thể báo lỗi; cần kiểm tra nguồn thay đổi và thiết lập quy trình mới rõ ràng.

Không gửi output có nhãn AI cho người chấm mù. Khi có thời gian thực hiện human
review, dùng [hướng dẫn từng bước](itsp_human_review_steps.md).
