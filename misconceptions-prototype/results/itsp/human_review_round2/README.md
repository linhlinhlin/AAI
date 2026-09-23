# Hồ sơ đối chiếu cụm — chỉ dùng ở vòng 2

Gói này chứa 59 bài làm để đối chiếu ngữ cảnh; chỉ 17 mẫu trong [review_assignments.json](review_assignments.json) cần điền phiếu. Không mở hoặc gửi kèm trước khi khóa annotation độc lập vòng 1. Không có nhãn AI hoặc gợi ý nguyên nhân theo mẫu trong gói.

1. Người điều phối lưu file vòng 1 nguyên trạng, hash và thời điểm nhận. Chuyên gia tạo bản sao làm việc vòng 2, giữ nguyên decision/type/confidence và tuyên bố độc lập của vòng 1.
2. Tra submission ID của 17 mẫu trong mapping để tìm cluster riêng A/B/C. Mở [ngữ cảnh đầy đủ](cluster_context.md) rồi đọc source/log/bản sửa của các thành viên. Tất cả đường dẫn hoạt động offline. Không chạy source sinh viên.
3. Chỉ bổ sung `same_cause_as_cluster` A/B/C: Yes nếu cùng nguyên nhân thực chất với tất cả thành viên đã đánh giá; Partially nếu chỉ một phần/cụm nhiều nguyên nhân; No nếu không có nguyên nhân chung phù hợp. Chưa xem đủ ngữ cảnh giữ null. Đây là đánh giá của chuyên gia, không được suy từ số test fail hoặc khoảng cách.
4. Giữ nguyên phần evidence vòng 1, bổ sung đoạn có tiền tố `Vòng 2:` ghi phạm vi thành viên đã xem, nguyên nhân cụ thể, trường hợp khác nguyên nhân và giới hạn. Không dùng nhãn cụm để sửa lại kết luận độc lập.
5. Trả file vòng 2 riêng. Người điều phối đối chiếu với snapshot vòng 1 trước khi hợp nhất. Adjudication chỉ thực hiện sau các lượt độc lập, do chuyên gia thật xác nhận; không tự điền trong bước đối chiếu cụm.

Số cụm giống nhau giữa A/B/C không đảm bảo cùng thành viên; cluster ID không phải misconception label. Không tạo student ID và không suy rộng sang unseen student. Main.c chứa cả mô tả và chương trình tham chiếu; log/bản sửa được cung cấp như bằng chứng lịch sử, không chứng minh trạng thái nhận thức.
