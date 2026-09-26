# AAI Learning — app học viên và giảng viên

App chạy thực tế trên máy local tại `http://127.0.0.1:8766`, dùng tài khoản,
SQLite và Docker Linux. Màn hình nghiên cứu cũ vẫn dùng cổng 8765. Hai app không
chia sẻ phiên đăng nhập; app học viên không mở API của bàn nghiên cứu cũ.

## Cài và chạy

Cài Python 3.12 theo [harness](harness.md), mở Docker Desktop với Linux engine.
Từ `misconceptions-prototype`:

```powershell
& .venv/Scripts/python.exe scripts/setup_learning.py
./start_learning.ps1
```

Linux dùng `.venv/bin/python scripts/setup_learning.py`, rồi
`.venv/bin/python -m misconceptions.learning_web`. Không cần GPU hoặc API LLM.
Image gốc được khóa digest; compiler/package hệ điều hành lấy từ Debian khi
build, nên hai lần build khác ngày có thể tạo image ID khác. Mỗi lượt chấm giữ
image ID thực thi, hash source, executable, suite và stdout.

Người học mở địa chỉ app và chọn **Đăng ký học viên**. Dữ liệu mới bắt đầu rỗng;
không tạo sinh viên giả trong lớp của người dùng. Để tạo giảng viên đầu tiên,
chủ máy mở đường dẫn **Teacher setup** in trong terminal khởi động. Token một
lần dùng được lưu tại `.cache/learning-app/teacher-setup-token.txt` ở repo root;
chỉ tài khoản đầu tiên được tạo qua token này có vai trò teacher. Không gửi
token hoặc database lên Git. Không có mật khẩu mặc định.

## Học viên sử dụng

1. Chọn một trong sáu bài C17: tổng, trung bình, cực đại, đếm, hoán vị, đường tròn.
2. Viết code, có thể ghi điều đang thử thay đổi, bấm **Chạy kiểm thử**.
3. Xem từng input, expected, output, lỗi biên dịch/thực thi và gợi ý kiểm tra.
4. Sửa rồi nộp lại. Lịch sử lưu source của từng lần nộp, ghi chú và kết quả;
   **Hành trình của tôi** giúp mở lại và tải bằng chứng JSON.

Test của các bài này được tác giả dự án viết và công khai để luyện tập, không
phải hidden tests, không phải dữ liệu C-Pack/ITSP. Chấm so sánh các token UTF-8,
bỏ khác biệt khoảng trắng. Số `đạt/tổng` chỉ phản ánh các test đã chạy.
Output sai encoding giữ byte gốc dạng base64 và hash, không dùng ký tự thay thế
làm một bài sai thông thường đủ điều kiện phân cụm.

## Giảng viên sử dụng đúng chuỗi đề 5

Tab **Lớp học & nhóm lỗi** có số người đã nộp/đạt/cần hỗ trợ theo từng bài.
Mỗi phân tích chọn lần nộp đã chấm gần nhất của mỗi người theo cùng suite.

- **Object:** ID bài nộp. **Attribute–Value:** test, chỉ báo AST và stdout.
- K-means không giám sát trên one-hot có trọng số; giữ pipeline train/holdout
  theo nhóm sinh viên/source, không dùng nhãn nhận xét để tạo feature.
- Đại diện và thành viên của cụm mở được source, input, expected, actual, OAV.
- Cây độ sâu 3 sinh luật IF–THEN dự đoán ID cụm, với support/precision ở phần
  xây dựng/giữ lại. Không gọi fidelity là độ chính xác quan niệm sai.
- Giảng viên ghi tên nhóm, căn cứ và nội dung giảng lại. Review lưu nối tiếp,
  có tài khoản phụ trách và thời điểm; JSON xuất gồm cả snapshot và lịch sử review.

Khi ít hơn 4 bài sai đủ điều kiện, thiếu nhóm độc lập hoặc không đủ kiểu đặc
trưng cho k, hệ thống **abstain** và vẫn hiển thị bằng chứng từng bài. Không tự
thêm mẫu giả để biểu đồ có cụm. Bài đúng/compile error/runtime error vẫn nằm
trong mẫu số lớp học và được giải thích tình trạng.

Phân tích này là exploratory classroom analysis trên dữ liệu luyện tập mới,
không thay thế đánh giá locked test trong [protocol nghiên cứu](../research/protocol.json).
Review trên dashboard không phải gold chấm mù độc lập.

## Thực thi và dữ liệu

Compiler và từng test chạy trong container mới, non-root, không network,
không host mount, root filesystem chỉ đọc, cap-drop ALL, no-new-privileges,
default seccomp, 256 MB RAM, một CPU, 32 processes. Test có giới hạn CPU 2 giây
(hard 3), wall clock 5 giây gồm khởi động container, stdout/stderr tối đa 64 KB
mỗi luồng. Biên dịch có giới hạn riêng 20 giây wall clock/10 giây CPU.
Hết hạn thì xóa đúng container do lượt chạy đó tạo, không prune Docker chung.
Không thực thi code C trên host nếu Docker không sẵn sàng.

Oracle chỉ được đối chiếu ở server; executable nhận input của test tương ứng.
Lỗi hạ tầng là `system_error`, không biến thành kết luận học viên làm sai.
SQLite giữ phiên bản bài nộp; khởi động lại đánh dấu lượt dở dang là gián đoạn.
Cookie HttpOnly/SameSite, CSRF, kiểm tra origin/host và ownership nằm ở server.
Password được lưu PBKDF2-HMAC-SHA256 với salt riêng; session có hạn 12 giờ.

Database nằm trong `.cache/learning-app/`, đã Git-ignore. Sao lưu SQLite bằng
SQLite backup API hoặc dừng app trước khi sao lưu file; có WAL khi đang chạy.
Bản nháp editor nằm trên trình duyệt theo tài khoản/bài; dùng hồ sơ trình duyệt
riêng trên máy dùng chung. Bài đã nộp được lưu ở server.

Bản này triển khai **local có nhiều tài khoản**, chưa triển khai công khai.
Nếu vận hành lớp từ xa cần HTTPS/reverse proxy, cấu hình origin/cookie Secure,
vòng đời tài khoản và phục hồi mật khẩu, quota theo lớp, retention/consent,
và runner ở máy tách biệt (ưu tiên gVisor/VM cho môi trường đối kháng). Docker
ở đây là lớp cách ly có giới hạn, không phải cam kết an toàn tuyệt đối cho một
dịch vụ Internet công cộng. Không chỉ đổi bind sang `0.0.0.0` để đưa lên mạng.

## Kiểm chứng

```powershell
# Offline: auth, ownership, CSRF, persistence, no-fabricated-evidence, pipeline
& .venv/Scripts/python.exe ../scripts/harness.py check
# Thực thi C do dự án tự viết (không chạy historical student corpus)
$env:AAI_RUN_DOCKER_TESTS = '1'
& .venv/Scripts/python.exe -m pytest -q tests/test_learning_sandbox.py
Remove-Item Env:AAI_RUN_DOCKER_TESTS
# Browser thật + Docker thật + database kiểm thử riêng, output phải chưa tồn tại
& .venv/Scripts/python.exe -m pip install -r requirements-web-test.txt
& .venv/Scripts/python.exe -m playwright install chromium
& .venv/Scripts/python.exe -X utf8 scripts/learning_browser_smoke.py --output ../artifacts/learning-browser-check
```

Browser test có tài khoản/program tự viết, kiểm tra sai → sửa → đạt, đăng nhập
lại, lịch sử, teacher clusters, luật, xem OAV, lưu review và layout mobile.
Đây là nghiệm thu phần mềm; không phải nghiên cứu hiệu quả học tập trên người.
[Kết quả đã chạy và ảnh nghiệm thu ngày 27/09](../research/learning-app/README.md).

Thiết lập cách ly tham chiếu tài liệu Docker chính thức:
[run](https://docs.docker.com/engine/containers/run/),
[resource constraints](https://docs.docker.com/engine/containers/resource_constraints/),
[default seccomp](https://docs.docker.com/engine/security/seccomp/).
