# AAI Lab

App local cho đề 5: gom bài C sai theo cách chúng trượt test, mô tả mỗi nhóm bằng
bằng chứng và luật NẾU–THÌ, rồi để giảng viên xác nhận giả thuyết lỗi. Không có
tài khoản hay trang đăng nhập; app chỉ nhận kết nối từ chính máy đang chạy.

## Chạy

Từ thư mục `misconceptions-prototype`:

```powershell
./start_lab.ps1                        # mở http://127.0.0.1:8770
./start_lab.ps1 -Port 8771 -NoBrowser
```

Lần đầu, script tạo `.venv`, cài thư viện và dựng image Docker `aai-c-runner:1`
nếu còn thiếu. Chỉ màn **Chạy thử** cần Docker Desktop; ba màn còn lại chạy được
khi không có Docker. Dữ liệu app nằm ở `.cache/lab/lab.sqlite3` (không đưa lên Git);
xóa file này để quay về lớp mẫu ban đầu.

## Bốn màn hình

| Màn hình | Dùng để | Dữ liệu |
|---|---|---|
| Lớp học | Xem nhóm lỗi của từng bài, bằng chứng, luật, gợi ý dạy lại; đánh giá từng nhóm | Lớp mẫu 48 bài của 18 học viên mẫu (code nhóm tự viết, chấm thật trong Docker) và bài thêm từ Chạy thử |
| Chạy thử | Chạy bài C trong Docker cách ly, xem từng test và giả thuyết, thêm bài vào lớp | 6 bài luyện tập, test công khai |
| Dữ liệu C-Pack | Cùng cách phân tích trên 25 bài của C-Pack-IPAs, đối chiếu nhãn kiểm chứng | `.cache/cpack-v3`, `.cache/cpack-replay-v2` ([cách tạo](mechanism-benchmark.md)) |
| Nghiên cứu | Câu hỏi, dữ liệu, giả thuyết H1–H5, ARI, luật ILA-2, giới hạn | `research/runs/` đã commit |

## Một nhóm lỗi được tạo thế nào

1. Mỗi học viên lấy bài nộp mới nhất; bài đạt mọi test không vào phân tích.
2. Mỗi bài được biểu diễn bằng OAV độ lệch đã đăng ký trong protocol: kết quả từng
   test (trọng số 0,3), cách output lệch ở từng test (0,4) và độ lệch tổng hợp (0,3).
3. K-means (seed 42) trên one-hot có trọng số; k tự chọn theo silhouette trong 2–6,
   hoặc do giảng viên chọn. Cần ít nhất 4 bài sai có cách trượt khác nhau.
4. ILA-2 (hệ số phạt 1,0, tối đa 2 điều kiện) học một luật NẾU–THÌ phân biệt mỗi
   nhóm với các nhóm còn lại của chính lớp đó; app hiện độ chính xác và độ phủ.
5. Giả thuyết cơ chế chỉ hiện khi một luật viết tay (riêng của bài, hoặc chung cho C)
   hay một trong 14 luật ILA-2 đóng băng học từ C-Pack khớp ít nhất nửa nhóm. Khi các
   bài khớp những luật khác nhau, app báo **Trộn N giả thuyết** và liệt kê từng luật
   thay vì đặt một tên chung cho nhóm.

Bằng chứng của nhóm chỉ hiện khi đúng với ít nhất 60% số bài. Nhãn kiểm chứng C-Pack
chỉ dùng để đối chiếu, không tham gia gom nhóm hay chọn giả thuyết.

## An toàn

- Máy chủ chỉ nghe `127.0.0.1`, từ chối Host và Origin lạ; mọi yêu cầu ghi phải có
  header `X-AAI-Lab: 1` và nội dung JSON, nên trang web khác không điều khiển được app.
- CSP `default-src 'self'`, không có script inline; code và tên do người dùng nhập
  luôn được hiển thị dưới dạng văn bản.
- Code chỉ chạy trong container không mạng, chỉ đọc, giới hạn CPU, bộ nhớ và số tiến
  trình. Chỉ bài vừa được chính máy chủ chạy mới thêm được vào lớp.

## Kiểm tra đã chạy

- `tests/test_lab.py`: nhóm lỗi của lớp mẫu, nhóm trộn cơ chế, luật hoán vị, thêm bài
  vào lớp đúng một lần, đánh giá theo nhóm, biên HTTP (Host, Origin, header, kích thước).
- Playwright ở 1440 px và 390 px, giao diện sáng và tối: không lỗi console, không cuộn
  ngang. Đi hết luồng bằng bàn phím: skip link, chọn nhóm bằng phím mũi tên, hộp bài nộp
  giữ và trả focus, editor Tab/Shift+Tab/Esc/Ctrl+Enter, lỗi nhập tên hiện cạnh ô nhập.

## Giới hạn

Lớp mẫu là bài minh họa tự viết, không phải bài của sinh viên thật. Giả thuyết là gợi ý
cần giảng viên xác nhận, không phải chẩn đoán niềm tin của người học. App dành cho một
người dùng trên một máy; chưa triển khai qua mạng.

Các app cũ (bàn nghiên cứu cổng 8765, app học viên và giảng viên cổng 8766) vẫn được giữ
để tham khảo và tái lập hồ sơ trước đây.
