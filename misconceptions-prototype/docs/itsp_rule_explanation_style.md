# Rule Style Guide — Vietnamese Rule Explanation Grammar

**Trạng thái:** quy ước chính thức trong dự án. **Phiên bản:** `vi-rule-v1`.
**Ngày:** 22/09/2026. Áp dụng cho mọi luật gợi ý cơ chế lỗi trên UI và báo cáo mới.
Đây là chuẩn diễn đạt của dự án, không phải taxonomy được chuyên gia phê duyệt.

## 1. Mục tiêu và cơ sở phương pháp

Định nghĩa một dạng tiếng Việt có kiểm soát, giới hạn cấu trúc câu, từ vựng và ý nghĩa
được phép diễn đạt. Mục tiêu là giảm mơ hồ và giúp người đọc phân biệt quan sát với suy luận.
Đây là CNL chuyên biệt ở mức mẫu câu và hợp đồng dữ liệu; chưa có parser ngữ nghĩa tiếng Việt,
chứng minh đơn nghĩa hình thức hoặc nghiên cứu người dùng xác nhận hiệu quả của phiên bản này.

- **Kuhn (2014), A Survey and Classification of Controlled Natural Languages.** CNL hạn chế
  ngôn ngữ tự nhiên theo mục tiêu cụ thể. Dự án vận dụng nguyên tắc kiểm soát từ vựng/cấu trúc,
  không tuyên bố một bộ heading tự nó tạo thành ngôn ngữ logic hình thức.
  [MIT Press, DOI](https://doi.org/10.1162/COLI_a_00168),
  [bản trên ACL Anthology](https://aclanthology.org/J14-1005/).
- **Kuhn, The Understandability of OWL Statements in Controlled English.** Nghiên cứu so sánh
  cách trình bày OWL và controlled English trong phạm vi thí nghiệm của tác giả. Kết quả về
  khả năng hiểu/học là động lực để kiểm nghiệm UI của dự án, không phải bằng chứng tiếng Việt
  hoặc luật misconception ở đây đã dễ hiểu hơn.
  [Bản nghiên cứu trên Semantic Web Journal](https://www.semantic-web-journal.net/sites/default/files/swj167_1.pdf).
- **Ribeiro, Singh & Guestrin (2018), Anchors.** Quy tắc giải thích prediction có điều kiện và
  phạm vi áp dụng. Dự án tham khảo cách tách điều kiện, kết luận và phạm vi, **không triển khai
  Anchors**, không kế thừa bảo đảm xác suất/high precision của thuật toán đó. Điều kiện nhận diện
  ở đây đủ để kích hoạt template, không đủ để chứng minh misconception hay quan hệ nhân quả.
  [Bài báo AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/11491).
- **ONS và UK DfE:** dùng từ nhất quán, câu ngắn, heading rõ, giải thích thuật ngữ khi xuất hiện
  lần đầu. Đây là nguyên tắc thiết kế nội dung được điều chỉnh sang tiếng Việt, không áp dụng
  máy móc thang điểm readability tiếng Anh.
  [ONS](https://service-manual.ons.gov.uk/content/writing-for-users/plain-language),
  [DfE](https://design.education.gov.uk/content-design/plain-language).

Các trang hướng dẫn web được truy cập ngày 22/09/2026; không khẳng định nội dung hiện tại của
chúng là bản lưu đúng ngày 19/09/2026. Các công trình nghiên cứu nêu trên có trước mốc này.

## 2. Grammar bắt buộc

Mọi rule phải có đúng sáu thành phần, theo thứ tự:

```text
[TITLE]

Code pattern
- [Quan sát cấu trúc mã]

Behavioral pattern
- [Quan sát hành vi từ test/log]

Hypothesis
- Có thể [cơ chế cần kiểm tra].

Caveat
- [Giới hạn bằng chứng hoặc giải thích thay thế].

Suggested follow-up
- [Hành động kiểm tra hoặc giảng lại cụ thể].
```

Trên UI tiếng Việt dùng ánh xạ cố định:

| Thành phần | Heading trên UI | Trường dữ liệu |
|---|---|---|
| TITLE | Tiêu đề rule | `title` |
| Code pattern | Mẫu cấu trúc mã | `code_pattern` |
| Behavioral pattern | Mẫu hành vi quan sát | `behavioral_pattern` |
| Hypothesis | Giả thuyết | `hypothesis` |
| Caveat | Giới hạn suy luận | `caveat` |
| Suggested follow-up | Bước kiểm tra tiếp theo | `suggested_follow_up` |

Tiêu đề là chuỗi không rỗng. Năm trường còn lại là danh sách chuỗi không rỗng, mỗi bullet
một ý. Validator tại `src/misconceptions/rule_style.py` kiểm tra đủ trường, kiểu dữ liệu và
tiền tố “Có thể ” của giả thuyết. Nó không kiểm tra độ đúng của nội dung; review con người
và test detector vẫn bắt buộc. Cả ba rule hiện có dùng chung renderer và contract này.

## 3. Từ vựng và ngữ nghĩa được phép

| Vị trí | Mẫu diễn đạt | Không được suy diễn |
|---|---|---|
| Code pattern | “mã có…”, “hàm nhận…”, “else thuộc…” | Có một cấu trúc không tự chứng minh cấu trúc sai |
| Behavioral pattern | “log ghi…”, “expected… trong khi actual…” | Không gọi output là trạng thái bộ nhớ hoặc trace |
| Hypothesis | “Có thể người viết…”, “Có thể lỗi nằm ở…” | Không viết “Sinh viên chắc chắn/chưa hiểu…” như sự thật |
| Caveat | “Có thể chỉ là…”, “Chưa có…”, “Cần kiểm tra…” | Không giấu nguyên nhân thay thế hoặc thiếu bằng chứng |
| Suggested follow-up | “Truy vết…”, “Đối chiếu…”, “Yêu cầu giải thích…” | Không hứa một thay đổi sẽ sửa mọi test |

- `bài` là submission, không đổi thành `sinh viên` khi chưa xác minh danh tính.
- `Cluster` là cụm bài theo đặc trưng, không đồng nhất với loại misconception.
- `số bài khớp` là số thỏa điều kiện detector, không phải precision hoặc độ tin cậy.
- `tập xây dựng` (train) và `tập giữ lại` (holdout) được giải thích khi cần.
- `chưa xác định` tương ứng null/unknown; không hiển thị thành 0, “không có lỗi” hoặc “sai”.
- `không ghi nhận` một dấu hiệu không đồng nghĩa chứng minh dấu hiệu không tồn tại ngoài
  phạm vi extractor. `NOT(pass)` không được đổi thành `fail` vì còn trạng thái chưa chạy/lỗi.
- Quan hệ giữa bullet trong Code pattern và Behavioral pattern là **VÀ**. Nếu cần HOẶC,
  ghi rõ trong một bullet với phạm vi đóng; không dùng dấu `/` để che mơ hồ.
- Giữ nguyên input, expected, actual và đoạn code; không tự dịch/sửa dữ liệu gốc cho đẹp.

## 4. Bằng chứng có ngữ cảnh

**Evidence 1 — [loại cấu trúc]**: mô tả vai trò đoạn code; sau đó hiển thị từng đoạn và
vị trí dòng để đối chiếu. Ví dụ “cấu trúc điều khiển if–else”. Hai đoạn dòng 13–14 và
15–18 cùng thuộc bằng chứng cấu trúc. Không đổi đoạn code thứ hai thành “output thực tế”.

**Evidence 2 — output thực tế trong log**: bảng ca kiểm thử, đầu vào, kết quả mong đợi,
output thực tế. Nêu rõ là log có sẵn, không phải thực thi mới. Chỉ dùng danh xưng này khi
có log; fixture phải được nhận diện là tổng hợp trong ngữ cảnh dataset.

Dòng tính từ mã đã chuẩn hóa, bắt đầu bằng 1. Không bỏ tham chiếu dòng khi thêm context.
Không dùng đoạn code từ bài khác hoặc lấy medoid làm bằng chứng cho mọi thành viên cụm.

## 5. Trình bày số liệu và dữ liệu kỹ thuật

| Không hiển thị mặc định | Thay bằng |
|---|---|
| `Phân bố cụm: {"0": 2}` | **Phân bố:** Cluster 0 — 2 bài |
| `{"None": 1}` | Chưa gán cụm — 1 bài |
| `eligible`, `no_failure` | Đủ điều kiện; Không có test trượt |
| `ast:c_pointer_parameter=1` | Tham số con trỏ: Có |
| `null`, `__unknown__` | Chưa xác định |

JSON, mã feature gốc, hash và các bản ghi gốc vẫn được giữ trong file tải về hoặc mục
**Dữ liệu kỹ thuật để đối chiếu (JSON)** thu gọn. Kho báo cáo là nơi đọc artifact gốc,
được phép hiện nội dung máy đọc khi người dùng chủ động mở file.
Không dịch submission ID, test ID hoặc source code. Cần giải thích thuật ngữ thay vì đổi số liệu.

## 6. Ví dụ chuẩn

**Hai nhánh if có thể cùng tạo thông báo**

**Mẫu cấu trúc mã**
- Mã có hai if liên tiếp; else thuộc if thứ hai.

**Mẫu hành vi quan sát**
- Một test yêu cầu một vị trí nhưng output chứa nhiều vị trí.

**Giả thuyết**
- Có thể người viết nhầm quan hệ if–else và tính loại trừ giữa các nhánh.

**Giới hạn suy luận**
- Có thể chỉ thiếu từ khóa else do sơ suất; chưa chứng minh người viết hiểu sai.

**Bước kiểm tra tiếp theo**
- Yêu cầu người viết truy vết từng if với input đã trượt.

Phân bố: Cluster 0 — 2 bài. Số liệu này mô tả lượt demo, không là một phần cố định của template.

## 7. Quy trình thêm rule thứ 4 đến thứ 50

1. Định nghĩa rõ phạm vi ngôn ngữ/cấu trúc/test mà detector hỗ trợ.
2. Viết đủ sáu trường; tách quan sát khỏi giả thuyết; thêm nguyên nhân thay thế.
3. Dùng contract `vi-rule-v1`; không viết renderer riêng hoặc nhét HTML vào nội dung.
4. Có test dương, test âm gần giống, thiếu log và trường hợp không đủ bằng chứng.
5. Kiểm tra UI: nhãn có nghĩa, sáu phần đúng thứ tự, context evidence, ký tự đặc biệt được escape.
6. Reviewer rà nội dung với code/log; validator chỉ hỗ trợ kiểm tra cấu trúc.
7. Đổi phiên bản khi đổi contract; lưu hash nguồn và không sửa báo cáo lịch sử hồi tố.

Luật phân cụm có target cluster ID vẫn dùng NẾU–THÌ và ghi rõ target, không tự chuyển
sang grammar chẩn đoán misconception. Để đánh giá style guide, cần thí nghiệm với người dùng:
độ đúng khi giải thích lại, thời gian tìm evidence và tỷ lệ nhầm giả thuyết với kết luận.
Chưa công bố các kết quả đó cho dự án này.

### Bổ sung: luồng giảng viên và mapping

Trong [luồng giảng viên](teacher_dashboard_flow.md), target cluster ID được lưu trong vùng
kỹ thuật; vế THÌ hiển thị tên nhãn đã mapping cho đúng lượt chạy và arm. Trạng thái nháp,
xác nhận hoặc chưa xác định phải đi kèm. Đây là phép ánh xạ tên nhóm, không phải bằng chứng
nhân quả mới. Vế NẾU hiển thị bảng OAV; phủ định được giữ bằng quan hệ ≠.
Bộ luật chuyên môn vẫn giữ đủ sáu phần ở trên và có bảng OAV nhận diện riêng.
