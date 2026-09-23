# Giới thiệu dự án và kịch bản demo cho thành viên mới

Kịch bản khoảng 15–20 phút. Các số liệu dưới đây được chạy lại trên web ngày 22/09/2026,
với dữ liệu hiện có và cấu hình ghi rõ bên dưới. Đây là kết quả demo, không phải đánh giá
độ chính xác nhận diện misconception hoặc hiệu quả giảng dạy.

## 1. Nói mục tiêu bằng ngôn ngữ đời thường

“Giảng viên có nhiều bài lập trình sai, không thể đọc lần lượt mọi bài trước mỗi buổi học.
Nhóm đang xây công cụ gom các bài có biểu hiện lỗi giống nhau, chỉ ra bằng chứng và đề xuất
cơ chế lỗi để giảng viên quyết định cần giảng lại điều gì.”

Misconception là quan niệm sai về cách chương trình hoạt động. Một bài sai có thể do
quan niệm sai, nhưng cũng có thể do gõ nhầm, thiếu dấu chấm hoặc chưa hoàn thành bài.
Hệ thống không coi mọi test fail là misconception.

Đầu vào gồm source và kết quả test **đã có**, được tách theo cùng bài tập, ngôn ngữ và
test suite. Dữ liệu ITSP là dữ liệu công khai; demo tổng hợp là fixture để kiểm thử.
Web hiện không biên dịch hoặc chạy chương trình sinh viên.

## 2. Hiểu hai luồng xử lý

```text
Source + outcomes ──> OAV ──> chia train/holdout ──> gom cụm
                                                    │
                                                    └─> học luật dự đoán cluster ID

Source + log input/expected/actual ──> luật chuyên môn ──> giả thuyết cơ chế lỗi
                                                            │
                                         đối chiếu phân bố trong các cụm
                                                            │
                                                  giảng viên xác nhận
```

Hai luồng cùng được hiển thị trong một báo cáo nhưng không đồng nghĩa:

- **Luật phân cụm** được cây quyết định học để giải thích cluster ID.
- **Luật chuyên môn** được viết thủ công, khớp cấu trúc mã và bằng chứng test để đề xuất
  một cơ chế. Chúng chưa phải nhãn chuyên gia hoặc luật misconception tự học.

OAV là Object–Attribute–Value: ví dụ `(bài S, kết quả test 4, fail)` hoặc
`(bài S, có tham số con trỏ, có)`. AST là cấu trúc cú pháp của code, giúp nhận diện
lệnh và quan hệ giữa các lệnh. “Có vòng lặp” tự nó không có nghĩa vòng lặp bị sai.

Train là phần dùng xây cụm và học luật. Holdout là phần giữ lại để gán theo đại diện
cụm train. Với ITSP thiếu student ID, không khẳng định hai phần độc lập theo sinh viên.

## 3. Demo chính: bài phân loại vị trí điểm so với đường tròn

Mở http://127.0.0.1:8765. Nếu trang còn trạng thái cũ, tải lại một lần trước khi demo.

### Bước A — Mục 01: Thí nghiệm

Chọn:

| Trường trên web | Giá trị |
|---|---|
| Bộ dữ liệu / bài tập | 2825 · C |
| Thuật toán | Average-linkage · Hamming |
| Nguồn đặc trưng | Test + cấu trúc (C) |
| Số cụm k | 3 |
| Random seed | 42 |
| Trọng số test | 80% |
| Tỷ lệ holdout | 25% |

Bấm **Chạy thí nghiệm**. Kết quả: **22 bài đủ điều kiện, 3 cụm, silhouette train ≈ 0,696**.
Có 16 bài train và 6 bài holdout ở lượt này.

Nói: “Đây là 22 bài làm, không nhất thiết 22 sinh viên. Tôi đã yêu cầu k=3;
hệ thống không tự khám phá rằng lớp có đúng ba misconception. Silhouette mô tả
mức tách biệt của cụm theo đặc trưng/khoảng cách đang dùng; 0,696 không phải 69,6% đúng.”

Trong tab **Cụm & bài làm**, nền xanh đánh dấu medoid: một bài đại diện về khoảng cách
trong cụm. Ký hiệu **H** là holdout. Medoid không phải đáp án đúng; cluster ID chỉ là số
định danh, không phải mức độ nghiêm trọng hoặc một tên lỗi cố định giữa các lượt chạy.

### Bước B — Mục 02: Dữ liệu & OAV

Bấm **Mở dữ liệu đang chọn**. Trong ô **Tìm submission ID**, nhập `271203`, rồi bấm **Xem**.
Hộp chi tiết hiển thị source, OAV và log test. Với test 4:

```text
Input:    3.0 4.0 5.0 5.6 6.2
Expected: Point is inside the Circle.
Actual:   Point is inside the Circle.Point is on the Circle.
```

Giải thích: “Expected là output mong đợi của ca test; actual là output trong log.
Chương trình đã in hai kết luận khác nhau cho một điểm.”

Đối chiếu đoạn mã:

```c
if (n < 0)
    printf("Point is inside the Circle.");
if (n > 0)
    printf("Point is outside the Circle.");
else
    printf("Point is on the Circle.");
```

Khi n âm, if đầu in `inside`. if thứ hai sai, nên else của chính if thứ hai in `on`.
`else` không thuộc if đầu. Đây là cách truy vết đoạn code để giải thích output; web
không thực thi tracing. Việc người viết thực sự hiểu sai hay chỉ quên `else` vẫn cần hỏi lại.

Đóng hộp chi tiết. Khu vực **Nhập bộ dữ liệu riêng** dùng manifest, submissions và
review.jsonl tùy chọn. Người mới chưa cần upload để thực hiện demo này.

### Bước C — Mục 01 → tab Luật giải thích

Mở **Luật gợi ý cơ chế lỗi**, tìm “Nghi vấn nhầm quan hệ if–else…”. Mở bài
`itsp-2825-271203_buggy`: có dòng code, bảng test, giả thuyết thay thế và gợi ý giảng lại.

Nói: “Hệ thống ghép bằng chứng cấu trúc với hành vi quan sát được. Nó đề xuất nội dung
cần kiểm tra lại với sinh viên, chứ chưa kết luận sinh viên có quan niệm sai.”

Ở cấu hình demo:

| Quan sát | Số bài | Cách diễn giải |
|---|---:|---|
| Mẫu nhánh độc lập kèm output nhiều thông báo | 2 | Giả thuyết cần xác nhận |
| Sai khác trình bày output | 10 | Không tự coi là lỗi khái niệm |
| Chưa có luật khớp | 10 | Bộ nhận diện chưa bao phủ, không có nghĩa bài đúng |

Tổng 12/22 bài khớp ít nhất một luật là **coverage trên tập này**, không phải độ chính xác.

Cuộn xuống **Luật giải thích cách phân cụm**. Các câu NẾU–THÌ ở đây dự đoán cluster ID.
Fidelity cho biết cây luật tái hiện cách gán cụm đến mức nào; không đánh giá hiểu sai thật.
Mở **Ký hiệu gốc để đối chiếu** nếu cần nối câu tiếng Việt với feature gốc.

### Bước D — Mục 03: So sánh A / B / C

Giữ cấu hình trên, bấm **Chạy A / B / C**:

| Arm | Dữ liệu dùng gom cụm | Silhouette train | Fidelity holdout / majority |
|---|---|---:|---:|
| A | Chỉ kết quả test | 0,742 | 0,833 / 0,5 |
| B | Chỉ cấu trúc code | 0,875 | 1 / 1 |
| C | Test và cấu trúc | 0,696 | 0,833 / 0,5 |

Nói: “Đây là thí nghiệm bỏ/bổ sung nhóm đặc trưng để xem kết quả thay đổi ra sao.
Không kết luận B tốt nhất chỉ vì silhouette cao: không gian đặc trưng khác nhau.
B có fidelity 1 nhưng majority baseline cũng 1, nên chỉ nhìn con số 1 dễ đánh giá quá cao.”

## 4. Demo minh họa đề tài: hoán vị truyền tham trị

Quay lại **01 Thí nghiệm**, chọn **demo_swap_by_value · C**, bấm chạy rồi mở **Luật giải thích**.

Trang thông báo không đủ bài để phân cụm là đúng: đây chỉ có hai fixture tổng hợp.
Phần luật cơ chế vẫn hoạt động độc lập. Có một bài khớp luật truyền tham trị:

```c
void swap(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
}
```

Mở bằng chứng: input `2 7`, expected `7 2`, actual `2 7`.

Nói: “Hàm đổi hai bản sao cục bộ a và b; các biến ở hàm gọi chưa được đổi.
Muốn tác động các biến gốc trong C có thể truyền địa chỉ và giải tham chiếu.
C vẫn truyền giá trị của con trỏ, không tự chuyển sang cơ chế truyền tham chiếu.”

Mẫu dùng con trỏ đúng không bị gán luật này. Nhấn mạnh đây là ví dụ tổng hợp có output
suy ra thủ công, không phải bài sinh viên hay log chạy mới; không dùng để chứng minh
độ chính xác trên dữ liệu thực. Detector hiện chỉ nhận diện một số dạng swap đơn giản.

## 5. Các mục còn lại và quy trình xác nhận

| Mục trên web | Demo thao tác | Điều cần giải thích |
|---|---|---|
| 04 Hồ sơ reviewer | Mở codebook, chỉ vị trí tải ZIP và xử lý annotation | Dành cho 17 mẫu ITSP cố định, không phải tự chấm mọi cụm mới. Người chấm vòng 1 dùng ZIP riêng để tránh thấy cụm/nhãn AI. |
| 05 Kiểm tra kỹ thuật | Bấm Chạy tests hoặc Chạy lint | Kiểm tra phần mềm, không chứng minh giả thuyết giáo dục đúng. |
| 06 Kho báo cáo | Tìm `web_runs`, mở/tải file của lượt vừa chạy | Kết quả được lưu riêng; có cấu hình, hash và evidence để đối chiếu. |
| 07 Chức năng sắp có | Chỉ các nút đang vô hiệu hóa | Sandbox chạy code, detector ngữ nghĩa tổng quát, ILA và một số luồng đánh giá chưa hoàn thiện. |

Các luật cần được kiểm tra bằng đánh giá độc lập của giảng viên. Không dùng nhãn do
chính bộ luật tạo ra để tính độ đúng của chính hệ thống. Muốn tuyên bố hữu ích cho lớp
300+ sinh viên còn cần đo khả năng mở rộng, thời gian giảng viên và hiệu quả phản hồi.

## 6. Thành viên kỹ thuật bắt đầu đọc đâu?

| File | Vai trò |
|---|---|
| src/misconceptions/adapters.py | Đọc và kiểm tra hợp đồng dữ liệu |
| src/misconceptions/features.py | Trích OAV/cú pháp và biểu diễn đặc trưng |
| src/misconceptions/pipeline.py | Chia tập, gom cụm, gán holdout, học luật giải thích cụm |
| src/misconceptions/semantic_rules.py | Các mẫu cơ chế lỗi và diễn đạt điều kiện |
| src/misconceptions/teaching_report.py | Đọc evidence và ghép báo cáo giảng dạy |
| src/misconceptions/web.py và web_assets/ | API local và giao diện |
| tests/ | Kiểm thử core, evidence, annotation và web |

Chạy lại server nếu cần:

```powershell
cd E:/AAI/misconceptions-prototype
& .venv/Scripts/python.exe -m misconceptions.web --port 8765
```

## 7. Bài nói lại trong một phút

“Dự án giúp giảng viên xem nhiều bài lập trình sai theo nhóm. Nó đọc source và log test,
mã hóa thành đặc trưng rồi gom các bài có biểu hiện giống nhau. Một cây quyết định giải
thích cách chia cụm; một bộ luật chuyên môn riêng kết hợp cấu trúc mã với expected/actual
để gợi ý cơ chế lỗi. Ví dụ hai if độc lập có thể in hai thông báo cho cùng một điểm, còn
hàm swap dùng tham số thường chỉ đổi bản sao cục bộ. Giao diện cho xem bằng chứng,
so sánh cách gom cụm và xuất báo cáo. Cụm chưa phải misconception, còn giả thuyết cần
giảng viên xác nhận. Prototype hiện khai thác log đã có và chỉ hỗ trợ một số mẫu lỗi.”

Tự kiểm tra: người mới cần trả lời được (1) tại sao test fail chưa chứng minh hiểu sai,
(2) hai loại luật khác nhau ở đâu, (3) k=3 có nghĩa gì, (4) vì sao silhouette không phải
accuracy, và (5) phải mở đâu để kiểm tra bằng chứng cho một kết luận.

Ảnh từ lượt demo kiểm chứng:

- [Cụm bài 2825](../results/manual_test/onboarding_clusters.png)
- [Bằng chứng luật if–else](../results/manual_test/onboarding_branch_rule.png)
- [Bằng chứng demo hoán vị](../results/manual_test/onboarding_swap_rule.png)
