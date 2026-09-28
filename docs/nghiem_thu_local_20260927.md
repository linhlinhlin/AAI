# Kết quả kiểm chứng bản demo local — 27/09/2026

Bản bàn giao đã được cài và kiểm tra tại `AAI-handoff` trên Windows,
Python 3.12.3. Đây là kết quả chạy mới trên máy này, tách khỏi hồ sơ nghiệm
thu lịch sử trong `research/learning-app/`.

| Kiểm tra | Kết quả | Bằng chứng |
|---|---|---|
| Môi trường Python | Cài theo requirements lock | [doctor](../artifacts/course-acceptance-20260927/doctor.txt) |
| Ruff và pytest offline | 186 passed, 3 subtests passed; 13 ca Docker bỏ qua | [check](../artifacts/course-acceptance-20260927/check-final.txt) |
| Research smoke | 27/27 có OAV, cụm, luật, phản hồi | [smoke](../artifacts/course-acceptance-20260927/smoke-final.txt) |
| Docker integration | 14 passed, code fixture tự viết | [Docker](../artifacts/course-acceptance-20260927/docker.txt) |
| Browser và Docker thật | 1/6 → 6/6; hai cụm; lưu/mở lại review; phiên và mobile đạt | [acceptance](../artifacts/course-acceptance-20260927/browser/acceptance.json) |
| Bản demo cho người dùng | Hai tài khoản vào được; học viên còn 0/6; hai cụm, luật, OAV có thật | [demo check](../artifacts/course-acceptance-20260927/demo-check.json) |
| Không ghi đè demo | Chạy lại script chuẩn bị bị từ chối; dữ liệu giữ nguyên | Kiểm tra trực tiếp trong phiên bàn giao |

Một check xây lệnh Docker xuất hiện ở cả suite offline và Docker; không cộng
các con số thành tổng test độc lập. Browser test dùng database fixture riêng.
Không thực thi corpus C lịch sử, không gọi API trả phí, không mở sealed test.

## Đã xử lý

- Cài `.venv`, Playwright Chromium và image `aai-c-runner:1`.
- Docker Desktop không khởi động do socket tạm `dockerInference` bị Windows
  từ chối truy cập. Khi không còn process Docker, đổi tên riêng thư mục
  `C:/Users/Admin/AppData/Local/Docker/run` thành bản backup có timestamp,
  sau đó mở lại Docker thành công. Không reset Docker hay xóa images/volumes.
  Lỗi tương tự có trong [issue Docker](https://github.com/docker/desktop-feedback/issues/527).
- Sửa fingerprint để bản ZIP không có `.git` chạy được smoke, vẫn giữ hash và
  snapshot; commit và dirty status là null. Hai regression tests mới đã qua.
- Thêm `start_demo.ps1` và script chuẩn bị tám chương trình demo trong
  `.cache/course-demo/`, tách database app thường.
- Cập nhật trạng thái PR đã merge và đường dẫn clone repo nhóm trong tài liệu.

## Bằng chứng và cách dùng

[Hướng dẫn demo](demo_nghiem_thu.md) có tài khoản, code sai/đúng, thao tác giảng
viên và tiêu chí mong đợi. [Manifest kiểm chứng](../artifacts/course-acceptance-20260927/verification.json)
ghi môi trường, kết quả và hash mã. Các artifact local nằm trong `artifacts/`
đã được Git-ignore; khi bàn giao kết quả, gửi riêng thư mục này nếu cần.

- [Ảnh học viên và bằng chứng test](../artifacts/course-acceptance-20260927/browser/02-student-evidence.png)
- [Ảnh lịch sử sai/sửa](../artifacts/course-acceptance-20260927/browser/03-progress.png)
- [Ảnh cụm/luật và review lưu lại](../artifacts/course-acceptance-20260927/browser/04-teacher-clusters.png)
- [Ảnh hai cụm trên database demo](../artifacts/course-acceptance-20260927/demo-teacher-ready.png)
- [Ảnh OAV trên database demo](../artifacts/course-acceptance-20260927/demo-oav.png)

Kết quả đáp ứng kiểm chứng luồng kỹ thuật của hợp đồng đề 5 tại local; việc
nghiệm thu chính thức thuộc giảng viên. Tám bài demo là chương trình tự viết,
không chứng minh chất lượng chẩn đoán quan niệm sai hay hiệu quả học tập.
Các sửa đổi trong phiên này ở bản local, chưa đưa lên GitHub.
