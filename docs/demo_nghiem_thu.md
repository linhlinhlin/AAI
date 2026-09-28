# Demo nghiệm thu đề 5

Bản demo chạy local ở **http://127.0.0.1:8767**. Tám chương trình C minh họa
được chạy thật trong Docker để có dữ liệu xem OAV, phân cụm và luật.
Các tài khoản có tên DEMO, không phải sinh viên thật. Đây là kiểm chứng chức
năng môn học, không phải kết quả đánh giá khoa học hay hiệu quả học tập.

[Kết quả kiểm chứng local và ảnh nghiệm thu](nghiem_thu_local_20260927.md).

## Mở demo trên máy đã cài

Mở Docker Desktop, đợi Linux engine sẵn sàng. Mở PowerShell tại thư mục
`AAI-handoff`, chạy:

```powershell
./misconceptions-prototype/start_demo.ps1
```

Giữ terminal mở, vào **http://127.0.0.1:8767**. Lần đầu tạo dữ liệu mất vài
phút; lần sau mở lại lịch sử đã lưu. Ctrl+C dừng app, không xóa dữ liệu.
Nếu cổng bận vì demo đã chạy, mở địa chỉ trước; không mở hai server cùng database.

| Vai trò | Tên đăng nhập | Mật khẩu demo |
|---|---|---|
| Học viên tự thử | `demo_student` | `Demo-AAI-2026!` |
| Giảng viên | `demo_teacher` | `Demo-AAI-2026!` |

Đây là tài khoản riêng của demo local, không phải tài khoản trong
`PRIVATE_ACCOUNTS.md`. Database demo nằm tại `.cache/course-demo/`;
app thường ở cổng 8766 dùng `.cache/learning-app/`. Dữ liệu demo không nhập
vào ITSP/C-Pack hoặc sealed test.

## Kịch bản 10 phút

### 1. Học viên: bài sai → bằng chứng → sửa bài

1. Đăng nhập `demo_student`, chọn **Tổng từ 1 đến n**.
2. Dán chương trình dưới đây để luôn có cùng điểm bắt đầu, kể cả khi trình
   duyệt đã lưu bản nháp từ lần demo trước:

```c
#include <stdio.h>
int main(void) {
    int n;
    scanf("%d", &n);
    printf("0\n");
    return 0;
}
```

3. Bấm **Chạy kiểm thử**, chờ **Đã chấm xong.** Kỳ vọng **1/6 test đạt**.
   Mở các test: n=0 có expected=0, n=2 có expected=3 nhưng actual=0.
4. Dán bản sửa sau, ghi chú “Cộng đủ từ 1 đến n”, chạy lại:

```c
#include <stdio.h>
int main(void) {
    int n;
    scanf("%d", &n);
    long long sum = 0;
    for (int i = 1; i <= n; i++) sum += i;
    printf("%lld\n", sum);
    return 0;
}
```

5. Kỳ vọng **6/6 test đạt** và tiến độ **1 / 6** nếu chưa giải bài khác.
6. Mở **Hành trình của tôi**: có cả lần sai và lần sửa; tải bằng chứng JSON.
   Tải lại trang hoặc đăng xuất/đăng nhập, lịch sử vẫn còn. Mỗi lần demo thêm
   hai bài nộp; hệ thống không xóa lịch sử cũ.

### 2. Giảng viên: OAV → cụm → luật → nhận xét

1. Đăng xuất, đăng nhập `demo_teacher`.
2. Mở **Lớp học & nhóm lỗi**, chọn phân tích **Tổng từ 1 đến n**, giữ **k=2**.
3. Với tám bài minh họa ban đầu, kỳ vọng có **2 cụm** và luật IF–THEN.
   Học viên demo vừa đạt 6/6 vẫn ở tổng quan lớp nhưng không vào nhóm bài sai.
4. Mở bài đại diện: chỉ ra source, input, expected, actual và bảng OAV.
   Ví dụ Object là ID bài nộp, Attribute là `test:t1`, Value là `pass` hoặc `fail`.
5. Đọc một luật IF–THEN thực tế trên màn hình, chỉ ra support và fidelity.
   Giải thích: cây đang dự đoán ID cụm, không đo độ đúng của quan niệm sai.
6. Điền tên nhóm, căn cứ theo bài đại diện và nội dung giảng lại. Ví dụ nội
   dung: “Yêu cầu liệt kê các số được cộng khi n=2 và n=5”. Không gán cùng một
   nguyên nhân cho cả cụm khi chưa kiểm tra các thành viên.
7. Lưu nhận xét, tải lại trang, mở báo cáo đã lưu và kiểm tra nhận xét còn đó.
   Xuất JSON để lưu bằng chứng nghiệm thu.

Các fixture `demo_fixture_1` đến `demo_fixture_8` được giữ nguyên để demo cụm
ổn định. Nếu tự đăng nhập và sửa chúng, kết quả phân cụm có thể thay đổi.

### Gợi ý nhận xét cho từng nhóm

1. Bấm **Gợi ý nhận xét** ở nhóm cần xem. Hệ thống hiện bản gợi ý gồm tên
   nhóm, căn cứ, nội dung giảng lại và nguồn gợi ý.
2. Nếu đã cấu hình API, nút gửi mô tả bài cùng code/test/OAV của tối đa bốn
   bài mẫu trong nhóm tới nhà cung cấp đã chọn. Không gửi metadata tên tài
   khoản/ID học viên; code và output vẫn là dữ liệu được gửi đi.
3. Bấm **Điền vào bản nháp** để thay nội dung các ô nhận xét bằng gợi ý.
   Xem bài dẫn chứng, sửa nếu cần, rồi **Lưu nhận xét giảng viên**.
4. Chỉ tạo/điền gợi ý chưa phải duyệt nhận xét. JSON xuất có `suggestions`
   riêng với `status=draft`, nguồn/model và ánh xạ mẫu dẫn chứng; nhận xét
   được giảng viên lưu nằm ở `reviews`. Kết quả phân cụm không đổi.

Chưa có API key/model: nút vẫn đưa gợi ý từ **bộ luật cục bộ**, ghi rõ không
phải AI. Nếu API lỗi, hiển thị lỗi và giữ nguyên các ô đang nhập. Gợi ý cùng
báo cáo/nhóm/cấu hình được dùng lại để tránh gọi API nhiều lần.

#### Cấu hình API trên máy

Mở `misconceptions-prototype/.env` bằng trình soạn thảo trên máy. Không gửi
key vào chat hoặc commit file này. Điền model có quyền dùng trong tài khoản
và key tương ứng với một trong các cấu hình:

| Nhà cung cấp | `MISCONCEPTIONS_LLM_PROVIDER` | Biến key |
|---|---|---|
| Gemini | `gemini` | `GEMINI_API_KEY` |
| OpenAI | `openai` | `OPENAI_API_KEY` |
| Claude | `anthropic` | `ANTHROPIC_API_KEY` |
| Groq | `groq` | `GROQ_API_KEY` |

Groq dùng endpoint riêng `https://api.groq.com/openai/v1/chat/completions`.
Không đặt key Groq trong `GEMINI_API_KEY`. Model `llama3-8b-8192` đã ngừng
hoạt động; chọn model hiện có trong tài khoản. `openai/gpt-oss-20b` hỗ trợ
JSON schema strict trên Groq; tên model có tiền tố `openai/` nhưng provider
vẫn là `groq`, không cần key OpenAI. Các model Groq khác dùng JSON object,
và app vẫn kiểm tra schema/dẫn chứng trước khi chấp nhận gợi ý.

`MISCONCEPTIONS_LLM_MODEL` phải có giá trị; key nằm phía server, không gửi
ra trình duyệt hay JSON báo cáo. Sau khi sửa `.env`, dừng và mở lại app.
Kiểm thử mặc định dùng phản hồi giả lập, không gọi API trả phí. Chỉ khi có
key/model và bấm nút thì app mới gọi nhà cung cấp.

### 3. Thử tình huống không đủ bằng chứng

- Chọn một bài chưa có bài nộp, chẳng hạn **Hoán vị qua hàm**, rồi phân tích.
  Kỳ vọng hệ thống giải thích thiếu dữ liệu, không tự sinh cụm.
- Trong tài khoản học viên, thử code `int main(void) { syntax error }`.
  Kỳ vọng lỗi biên dịch, không hiển thị như đã chạy và trượt cả sáu test.
- Quay lại bản sửa đúng để kết thúc demo ở trạng thái dễ kiểm tra.

## Đối chiếu tiêu chí nghiệm thu

| Tiêu chí | Thao tác/bằng chứng |
|---|---|
| Bài sai và kết quả test | Chạy bản in 0; xem 1/6, expected/actual |
| OAV | Giảng viên mở bằng chứng bài đại diện |
| Phân cụm không giám sát | K-means k=2 trên tám bài C minh họa |
| Luật sản xuất | Đọc IF–THEN, support và fidelity từ cây giải thích |
| Phản hồi giảng dạy | Lưu, mở lại nhận xét và nội dung giảng lại |
| Lịch sử và tính tái lập | Mở hai lần nộp, tải JSON, tải lại trang |
| Thiếu bằng chứng | Phân tích bài chưa có đủ bài nộp, không tạo cụm giả |

## Cài lần đầu trên máy khác

Yêu cầu Python 3.12 và Docker Desktop Linux engine. Từ root dự án:

```powershell
py -3.12 -m venv misconceptions-prototype/.venv
& misconceptions-prototype/.venv/Scripts/python.exe -m pip install -r misconceptions-prototype/requirements-lock.txt
& misconceptions-prototype/.venv/Scripts/python.exe -m pip install --no-deps --no-build-isolation -e misconceptions-prototype
& misconceptions-prototype/.venv/Scripts/python.exe misconceptions-prototype/scripts/setup_learning.py
./misconceptions-prototype/start_demo.ps1
```

Nếu PowerShell chặn script, không cần đổi execution policy toàn máy. Dùng:

```powershell
# Chỉ chạy bước chuẩn bị khi chưa có .cache/course-demo/demo_manifest.json
& misconceptions-prototype/.venv/Scripts/python.exe -X utf8 misconceptions-prototype/scripts/prepare_learning_demo.py
& misconceptions-prototype/.venv/Scripts/python.exe -X utf8 -m misconceptions.learning_web --port 8767 --data-dir .cache/course-demo
```

Nếu báo chưa có Docker/runner, mở Docker Desktop và chạy lại `setup_learning.py`.
Nếu chuẩn bị demo thất bại giữa chừng, script giữ dữ liệu để kiểm tra và từ
chối ghi đè. Dừng mọi app dùng demo, sao lưu/đổi tên riêng thư mục
`.cache/course-demo`, rồi chạy chuẩn bị lại; không xóa database app thường.

Kiểm tra phần mềm: các lệnh `doctor/check/smoke` trong [harness](harness.md).
Kiểm tra Docker/trình duyệt bằng fixture riêng: [hướng dẫn app](learning_app.md#kiểm-chứng).
