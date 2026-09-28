# Kịch bản demo tính năng — Misconceptions Clustering

Phiên bản: 28/09/2026, sau cập nhật rule in hằng số và raw_code cho LLM.
Thời lượng chính: khoảng 15 phút. Một người trình bày và thao tác được.

## 1. Kết quả rà soát trước khi demo

Phần mềm đủ luồng để trình diễn môn học: bài sai → bằng chứng test/code → OAV
→ clustering → luật IF–THEN → gợi ý và nhận xét giảng viên → lịch sử/JSON.
Mã hiện tại khớp hash của bản đã kiểm chứng; Docker C17 sẵn sàng; database demo
có 8 bài mẫu và không có bài đang chạy tại thời điểm rà soát.

Kiểm tra gần nhất: **235 tests + 3 subtests pass**, **27/27 smoke**; kiểm tra
Chromium + Docker thật pass. Suite offline bỏ qua 13 test cần Docker; kết quả
browser/Docker được ghi riêng. Không cần chạy lại 924 cấu hình trên sân khấu.

Những việc còn lại cần nói đúng:

| Việc | Có chặn demo chức năng không? | Cách xử lý |
|---|---|---|
| Chưa có nhãn giảng viên thật cho đánh giá mới | Không | Trình diễn phiếu và evaluator ở trạng thái chờ; không nói đã xác nhận accuracy misconception |
| Chưa có lời giải thích người học/quan sát kiểm tra tiếp | Không | Giữ cognitive_status chưa được đánh giá |
| Chưa gọi lại Groq/Gemini thật sau prompt mới | Không | Phần AI tùy chọn; kết quả local đã kiểm chứng; không hứa AI luôn trả lời đúng |
| DOCX/PPTX cũ còn số liệu trước đợt kiểm chứng mới | Cần đồng bộ trước khi nộp/thuyết trình bằng các file đó | Dùng bảng số liệu cuối tài liệu này; không giới thiệu file cũ là bản kết quả mới nhất |

## 2. Chuẩn bị trước giờ thuyết trình

1. Mở Docker Desktop và chờ Linux engine sẵn sàng.
2. Nếu app cũ đang chạy, Ctrl+C tại terminal của app để nạp mã mới.
3. Mở PowerShell tại `E:\Applications\AAI-ban-giao-rieng\AAI-handoff`:

```powershell
./misconceptions-prototype/start_demo.ps1
```

4. Mở `http://127.0.0.1:8767`, tải lại trang. Giữ terminal mở.
5. Dùng tài khoản demo sau; đây là tài khoản minh họa, không phải tài khoản riêng:

| Vai trò | Tài khoản | Mật khẩu demo |
|---|---|---|
| Học viên | `demo_student` | `Demo-AAI-2026!` |
| Giảng viên | `demo_teacher` | `Demo-AAI-2026!` |

6. Mở sẵn file này và [bảng kết quả nghiên cứu](../../research/runs/validation-summary-20260928.md).
7. Giữ nguyên `demo_fixture_1` đến `demo_fixture_8`. Mỗi lần diễn tập sẽ thêm lịch
   sử của `demo_student`; không xóa database để “làm sạch” demo.
8. Phần AI là tùy chọn. Không mở `.env` hay gõ API key trên màn chiếu. Nếu API
   chưa dùng được, vẫn thực hiện đầy đủ demo bằng gợi ý cục bộ.

## 3. Timeline và lời nói

### 00:00–00:45 — Giới thiệu bài toán

**Màn hình:** trang đăng nhập.

**Nói:**

> “Đề tài của nhóm là phân cụm các bài lập trình sai để hỗ trợ giảng viên nhìn
> thấy những nhóm biểu hiện lỗi thường gặp. Hệ thống kết nối code và test với
> OAV, cụm lỗi, luật IF–THEN và nội dung cần giảng lại. Các tài khoản DEMO ở đây
> là dữ liệu minh họa; không phải sinh viên thật.”

### 00:45–01:15 — Đăng nhập và vai trò

**Thao tác:** đăng nhập `demo_student`, mở **Luyện tập**, chọn **Tổng từ 1 đến n**.
Chỉ nhanh danh sách sáu bài và trạng thái **Sẵn sàng chạy C17**.

**Nói:**

> “Tài khoản giúp giữ lịch sử từng người. Học viên xem bài của mình, còn giảng
> viên được xem tổng hợp của lớp. Việc đăng nhập phục vụ quản lý dữ liệu; lõi
> khai phá nằm ở các bước phân tích sau.”

**Cần thấy:** đề bài, editor, bộ test công khai; học viên không có tab phân tích lớp.

### 01:15–03:00 — Nộp bài sai và xem bằng chứng

**Thao tác:** dán chính xác chương trình sau. Ghi chú tùy chọn: “Đọc n nhưng
mới in một giá trị cố định.” Bấm **Chạy kiểm thử** và chờ **Đã chấm xong.**

```c
#include <stdio.h>
int main(void) {
    int n;
    scanf("%d", &n);
    printf("0\n");
    return 0;
}
```

**Cần thấy:** **1/6 test đạt**. Chỉ test `n=0` đúng; với `n=2`, expected là `3`
nhưng actual là `0`. Mở bằng chứng OAV và tìm `is_hardcoded_output = true`.

**Nói:**

> “Chương trình có đọc n, nhưng lệnh in không dùng n hay một kết quả tính từ n.
> Nó luôn in 0. Hệ thống không chỉ thông báo sai: chúng ta thấy input, expected,
> actual và đoạn code liên quan. Rule cục bộ nhận diện output hằng khi AST phù
> hợp và có ít nhất hai test fail.”

**Điểm nhấn:** đây là mô tả lỗi quan sát được, chưa khẳng định học viên có niềm
tin sai nào. Không đọc toàn bộ JSON trong lúc trình bày.

### 03:00–04:00 — Sửa bài và chạy lại

**Thao tác:** thay bằng code sau, ghi chú “Cộng đủ các số từ 1 đến n”, chạy lại.

```c
#include <stdio.h>
int main(void) {
    int n;
    scanf("%d", &n);
    long long sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    printf("%lld\n", sum);
    return 0;
}
```

**Cần thấy:** **6/6 test đạt**. Nếu chưa giải bài khác, tiến độ là **1 / 6**.

**Nói:**

> “Sau khi tính tổng theo đầu vào, chương trình vượt qua bộ test hiện có. Điều
> này xác nhận kết quả trên các ca kiểm thử, chưa tự chứng minh học viên hiểu
> hoàn toàn khái niệm.”

### 04:00–04:45 — Lịch sử và bằng chứng có thể xuất

**Thao tác:** mở **Hành trình của tôi**, chỉ hai lần nộp mới nhất: một lần sai,
một lần đúng. Mở lại lần sai, tải JSON nếu cần. Tải lại trang để cho thấy lịch sử còn.

**Nói:**

> “Các lần thử không bị ghi đè. Giảng viên có thể đối chiếu trước và sau sửa;
> bằng chứng JSON giúp kiểm tra lại quá trình demo.”

**Lưu ý:** nếu diễn tập nhiều lần thì lịch sử nhiều hơn hai dòng; không nói hệ
thống chỉ có hai bài nộp. Kết thúc bước này với bài đúng là lần nộp mới nhất.

### 04:45–06:00 — Góc nhìn giảng viên và phân cụm

**Thao tác:** đăng xuất; đăng nhập `demo_teacher`; mở **Lớp học & nhóm lỗi**.
Ở bài **Tổng từ 1 đến n**, giữ `k=2`, bấm **Xem nhóm lỗi** để tạo báo cáo mới.

**Cần thấy:** hai cụm từ tám bài mẫu sai nếu các fixture chưa bị sửa. Học viên
vừa đạt 6/6 vẫn có trong tổng quan nhưng bài đúng mới nhất không vào cụm bài sai.

**Nói:**

> “Phân tích lớp lấy lần nộp đã chấm gần nhất của mỗi học viên cho từng bài.
> K-means gom các biểu hiện tương tự từ test, AST và stdout; đây là phân cụm
> không giám sát. Việc có hai cụm không có nghĩa chỉ tồn tại hai misconception.”

### 06:00–07:00 — Giải thích OAV bằng một bài thật trên màn hình

**Thao tác:** mở bài có dấu **đại diện** trong nhóm in hằng số. Chỉ dòng
`printf`, test fail và bảng OAV.

**Nói:**

> “Object là bài nộp này. Attribute có thể là trạng thái một test hoặc dấu hiệu
> trong code; Value là giá trị cụ thể như fail. Cờ is_hardcoded_output là OAV
> chẩn đoán được bổ sung để giải thích mẫu in hằng số.”

> “Cờ chẩn đoán này chưa được tự đưa vào vector clustering đã đóng băng. Nhờ
> vậy chúng em không thay đổi các kết quả baseline cũ mà không chạy lại thí nghiệm.”

**Lưu ý:** số thứ tự cụm không phải tên lỗi cố định; chọn theo nội dung code và
kết quả gợi ý, không chỉ dựa vào chữ “Nhóm 1”.

### 07:00–08:00 — Luật IF–THEN và phạm vi ý nghĩa

**Thao tác:** đóng bằng chứng; kéo tới **Luật IF–THEN giải thích các cụm**.
Đọc nguyên một điều kiện đang hiện, cụm đích, support và tỷ lệ dự đoán đúng ID cụm.

**Nói:**

> “Sau khi phân cụm, cây quyết định học cách giải thích ID cụm bằng điều kiện
> IF–THEN. Support là số bài khớp luật; fidelity đo mức cây bắt chước phân cụm.
> Chỉ số này không phải độ chính xác nhận diện misconception.”

> “Cần phân biệt cây giải thích cụm được học từ dữ liệu với rule nhận diện in
> hằng số do nhóm viết và kiểm tra bằng AST/test.”

**Không học thuộc một điều kiện cố định:** luật có thể khác giữa các báo cáo.

### 08:00–09:15 — Gợi ý cục bộ và nhận diện in hằng số

**Thao tác:** bấm **Gợi ý nhận xét** ở nhóm gồm các mẫu in `1`, `3`, `15`, `5050`.

**Cần thấy:** nguồn **Bộ luật cục bộ**, nhãn **In hằng số / Chưa tính toán theo
đầu vào**, căn cứ **4/4 bài** với bộ demo nguyên trạng. Chưa có nhận xét nào được tự lưu.

**Nói:**

> “Phần này không cần API key. Hệ thống kiểm tra code của toàn bộ thành viên
> nhóm trước khi đưa ra nhãn mặc định. Ở nhóm này, cả bốn bài đều in một đáp án
> cố định và trượt nhiều test.”

**Thao tác thêm:** bấm gợi ý ở nhóm còn lại.

**Nói:**

> “Nếu chỉ một trong bốn bài khớp rule, hệ thống ghi rõ 1/4 và giữ nhận định
> nhóm hỗn hợp. Nó không lấy một bài để kết luận cho cả nhóm.”

### 09:15–10:15 — AI hỗ trợ diễn giải, không quyết định nhãn đúng

**Thao tác tùy chọn:** chọn **Diễn giải bằng AI** ở nhóm in hằng số nếu đã cấu
hình dịch vụ. Chỉ dành khoảng một phút cho bước này.

**Nếu thành công, nói:**

> “Model nhận raw_code đầy đủ của tối đa bốn bài đại diện cùng test và OAV.
> Prompt yêu cầu soi trực tiếp scanf và printf trước khi kết luận không rõ lỗi.
> Với rule in hằng số đã có bằng chứng, AI chỉ bổ sung cách giảng lại; không
> được xóa nhãn đó bằng một nhận xét mơ hồ.”

**Nếu lỗi hoặc chưa có key, nói:**

> “Dịch vụ AI hiện chưa trả được kết quả. Hệ thống báo rõ lỗi và giữ bản cục bộ,
> nên giảng viên vẫn tiếp tục được. AI là phần hỗ trợ, không phải điều kiện để
> chức năng phân tích và nhận xét hoạt động.”

Không sửa key/model ngay trên màn chiếu. Không cố gây lỗi bằng cách đổi `.env`
trong lúc demo. Lỗi model/API đã có kiểm thử giả lập và browser acceptance riêng.

### 10:15–11:30 — Giảng viên duyệt, lưu và xuất báo cáo

**Thao tác:** ở nhóm in hằng số, bấm **Điền vào bản nháp**. Chỉnh nội dung
giảng lại thành câu phù hợp, ví dụ:

> “Với n=2 và n=5, hãy liệt kê các số được cộng, tính tổng, rồi giải thích vì sao
> một đáp án cố định không đúng cho cả hai đầu vào.”

Bấm **Lưu nhận xét giảng viên**. Tải lại trang; mở báo cáo vừa tạo trong danh
sách báo cáo đã lưu. Kiểm tra nội dung còn nguyên. Bấm **Tải báo cáo JSON**.

**Nói:**

> “Giảng viên quyết định nội dung cuối cùng. Gợi ý chỉ điền bản nháp sau khi
> được chọn; chưa tự lưu. Nhận xét lưu trên dashboard là phản hồi giảng dạy,
> không tự trở thành nhãn độc lập để đánh giá thuật toán.”

### 11:30–12:15 — Trường hợp thiếu dữ liệu

**Thao tác:** chọn một bài chưa có bài nộp, chẳng hạn **Hoán vị qua hàm**, bấm
**Xem nhóm lỗi**. Nếu đã thử bài này trước đó, chọn bài khác đang có 0 bài.

**Cần thấy:** thông báo chưa đủ cơ sở phân cụm; không tự sinh học viên hoặc cụm.

**Nói:**

> “Khi dữ liệu không đủ, hệ thống từ chối tạo cụm và giữ lại bằng chứng hiện
> có. Không có cụm không đồng nghĩa là cả lớp không có lỗi.”

### 12:15–13:30 — Bằng chứng nghiên cứu ngoài dữ liệu demo

**Thao tác:** mở [báo cáo baseline/ablation](../../research/runs/validation-summary-20260928.md).
Chỉ bảng kết quả và phần độ ổn định; không mở hàng trăm JSON trong lúc nói.

**Nói:**

> “Ngoài dữ liệu minh họa, nhóm đã kiểm tra 11 biến thể với ba seed trên dữ
> liệu công khai. ITSP có 99 lượt, C-Pack-IPAs có 825 lượt. Các trường hợp không
> đủ điều kiện được ghi abstain, không ép tạo cụm.”

> “Chúng em đối chiếu luật với baseline chọn cụm đông nhất và đo ổn định giữa
> các seed. Có lượt luật còn kém baseline, nên chưa thể nói thêm đặc trưng luôn
> làm chẩn đoán tốt hơn. Các kết quả này dùng train/validation; sealed test
> chưa được dùng để chọn hay đánh giá mô hình.”

### 13:30–14:30 — Quy trình xác thực giảng viên

**Thao tác:** mở [hướng dẫn giảng viên](../../docs/teacher_validation.md), chỉ
file evidence, hai phiếu độc lập và phiếu phân xử. Đây là luồng offline bằng
JSON/CLI, chưa phải màn hình nhập gold trong app.

Nếu cần chứng minh trạng thái thật, mở:
`research/runs/cpack-validation-20260928/teacher-evaluation-pending.json`.
Chỉ `status: waiting_for_teacher_labels` và chỉ số cần gold đang là `null`.

**Nói:**

> “Hai giảng viên xem code và test mà không thấy kết quả cụm hay gợi ý AI;
> một người riêng phân xử. Nhãn cơ chế phải có dẫn chứng. Muốn xác nhận
> misconception còn cần lời giải thích của người học và kiểm tra tiếp.”

> “Hiện chưa có nhãn giảng viên thật cho đợt đánh giá này. Vì vậy hệ thống để
> trống các chỉ số cần gold, thay vì dùng nhãn AI hoặc số kiểm thử phần mềm
> để khẳng định chất lượng nhận diện.”

### 14:30–15:00 — Kết thúc

**Màn hình:** quay lại báo cáo giảng viên có nhãn in hằng số.

**Nói:**

> “Nhóm đã xây dựng được chuỗi từ bài sai và test đến OAV, cụm, luật và phản
> hồi có bằng chứng. Gợi ý cục bộ vẫn hoạt động khi dịch vụ AI lỗi. Phần tiếp
> theo là thu nhãn giảng viên độc lập để đánh giá chất lượng cơ chế lỗi và
> thu thêm bằng chứng người học để xác nhận misconception.”

## 4. Nếu chỉ có 7 phút

| Phút | Nội dung giữ lại |
|---|---|
| 0–1 | Giới thiệu, đăng nhập học viên |
| 1–2,5 | Nộp bài in 0, xem 1/6, sửa và xem 6/6 |
| 2,5–4 | Đăng nhập giảng viên, tạo hai cụm, mở OAV và một luật |
| 4–5,5 | Gợi ý cục bộ đúng nhãn, điền bản nháp, lưu |
| 5,5–6,5 | Bảng nghiên cứu và trạng thái chờ nhãn thật |
| 6,5–7 | Giới hạn, kết thúc |

Bỏ gọi AI thật, demo mobile và phần thiếu dữ liệu trong bản rút gọn. Không bỏ
phần phân biệt fidelity với accuracy misconception.

## 5. Tính năng mở rộng khi giảng viên hỏi

- **Đăng ký:** dùng tài khoản học viên mới, không dùng tên trùng; chỉ thao tác
  nếu có thêm thời gian. Không phát sinh tài khoản giảng viên qua đăng ký công khai.
- **Gợi ý luyện tập:** vào một bài, bấm mở gợi ý từng bước; đây là hướng dẫn
  luyện tập, khác nút gợi ý nhận xét của giảng viên.
- **Lỗi biên dịch:** nộp `int main(void) { syntax error }`, chỉ trạng thái lỗi
  biên dịch. Sau đó nộp lại bản đúng để lần gần nhất không làm thay đổi demo lớp.
- **Sáu bài:** tổng, trung bình, lớn nhất trong mảng, đếm số dương, hoán vị qua
  hàm, vị trí điểm so với đường tròn. Không hứa bộ rule nhận diện mọi lỗi ở mọi bài.
- **Mobile:** thu hẹp cửa sổ trình duyệt, chỉ editor và bảng test; không cần
  thực hiện lại toàn bộ quy trình đăng nhập/nộp bài.
- **Chấm nhãn:** dùng lệnh evaluate trong hướng dẫn giảng viên. Chạy phiếu
  trống vẫn chỉ là kiểm tra luồng, không phải có thêm dữ liệu đánh giá thật.

## 6. Xử lý trục trặc trong lúc demo

| Tình huống | Thao tác và lời giải thích |
|---|---|
| Cổng 8767 bận | Mở địa chỉ đang chạy; nếu là bản cũ, dừng đúng terminal của app rồi chạy lại. Không mở hai server chung database |
| Docker chưa sẵn sàng | Mở Docker, bấm kiểm tra lại môi trường. Trong lúc chờ, xem báo cáo đã lưu; không gọi đó là lần chạy test mới |
| Gợi ý còn hiện kết quả cũ | Tải lại trang sau khi khởi động lại app, bấm Gợi ý nhận xét; tạo báo cáo mới để có OAV mới |
| Không ra nhãn 4/4 như kịch bản | Xem đúng nhóm và source; kiểm tra fixture có bị sửa không. Đọc tỷ lệ thực tế, không ép nhãn theo số thứ tự cụm |
| API chậm/lỗi | Giữ bản cục bộ, tiếp tục lưu nhận xét. Không bấm gọi liên tục; có cooldown chống lặp |
| Lịch sử có nhiều lần thử | Giải thích dữ liệu được giữ qua các buổi; chỉ hai lần vừa nộp mới nhất |
| Thiếu thời gian | Dùng bản 7 phút; không chạy lại full research matrix |

## 7. Câu hỏi thường gặp và câu trả lời ngắn

**Vì sao phải đăng nhập?** Để tách lịch sử người học và quyền xem lớp. Nó không
phải thuật toán clustering.

**Tại sao báo cáo JSON đã chia nhóm mà vẫn cần nhận xét?** Cụm là kết quả máy
gom biểu hiện; nhận xét là diễn giải và hành động giảng dạy do con người duyệt.

**Có phải AI phân cụm không?** Không. K-means/average-linkage phân cụm từ đặc
trưng; LLM hỗ trợ diễn đạt sau đó.

**Luật có học từ nhãn misconception không?** Cây hiện học ID cụm. Các rule cơ
chế viết tay được ghi riêng. Đánh giá bằng gold giảng viên là một bước độc lập.

**235 test pass có nghĩa dự đoán đúng 100% không?** Không. Đó là kiểm tra phần
mềm. Chưa có gold thật để khẳng định accuracy misconception.

**Nhận diện in hằng số có bao quát mọi chương trình C không?** Không. Rule
hẹp ưu tiên tránh kết luận sai; cấu trúc chưa hỗ trợ có thể không được nhận diện.

**Không có mạng có demo được không?** Có, nếu Python và Docker image đã cài
sẵn. Kiểm thử, clustering, rule cục bộ và lưu lịch sử chạy local; gọi LLM cần mạng.

## 8. Số liệu dùng khi đồng bộ slide/báo cáo cũ

| Nội dung | Kết quả mới nhất | Cách gọi chính xác |
|---|---:|---|
| Kiểm tra phần mềm | 235 tests + 3 subtests | 13 Docker tests được bỏ qua trong suite offline; browser/Docker riêng pass |
| Research smoke | 27/27 | Kiểm tra pipeline nhẹ, không phải benchmark accuracy |
| ITSP validation | 99 lượt: 93 ok, 6 abstained | 3 bài development × 11 biến thể × 3 seed |
| C-Pack validation | 825 lượt: 774 ok, 51 abstained | 25 bài × 11 biến thể × 3 seed |
| ARI ổn định K-means combined_stdout trên C-Pack | Trung bình 0,962; thấp nhất theo bài 0,498 | So phân hoạch validation giữa seed, không phải ARI với gold giảng viên |
| Nhãn giảng viên thật mới | 0 | Không thay bằng nhãn AI hoặc fixture kiểm thử |
| Phiếu đã chuẩn bị | ITSP 48 bài; C-Pack pilot 150 bài | Đây là số bài chờ đánh giá, chưa phải số nhãn thật |

DOCX/PPTX đã tạo trước đợt nâng cấp còn các số 193 tests, 81 lượt ITSP hoặc
675 lượt C-Pack. Chúng là kết quả lịch sử, không sai nếu ghi đúng thời điểm;
không trình bày chúng như số liệu mới nhất. Đợt này cung cấp kịch bản mới bằng
Markdown; các file Word/PowerPoint cũ chưa được biên tập lại.

Nguồn kiểm chứng: [manifest kiểm tra mới nhất](../../research/runs/hardcoded-verification-20260928/verification.json),
[báo cáo nghiên cứu](../../research/runs/validation-summary-20260928.md),
[phân tích lỗi in hằng số](../../docs/hardcoded_output_diagnosis.md),
[quy trình nhãn giảng viên](../../docs/teacher_validation.md).
