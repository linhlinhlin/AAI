# Đánh giá độc lập bằng nhãn giảng viên

Hệ thống đã có đường nhập và chấm nhãn độc lập. Hiện **chưa có nhãn giảng viên thật**.
Các nhận xét lưu sau khi xem dashboard hoặc gợi ý AI không tự trở thành gold.
Không cần API key để chạy bất kỳ bước đánh giá nào trong tài liệu này.

Nếu muốn gửi **từng cluster kèm candidate và rule cho AI**, dùng
[module annotation theo cluster](cluster_annotation.md). Gói đó có schema và intake riêng;
không trộn kết quả AI vào các phiếu giảng viên độc lập bên dưới.

## Phân biệt những gì đang được xác nhận

| Mức | Bằng chứng cần có | Kết quả có thể kết luận |
|---|---|---|
| Cụm và luật | OAV, split khóa, cụm train, validation, lá cây | Độ ổn định cụm; luật dự đoán ID cụm tốt tới đâu |
| Cơ chế lỗi | Code/test, codebook, hai người đánh giá độc lập, phân xử | Mức phù hợp giữa cụm/luật và cơ chế được giảng viên xác nhận |
| Misconception | Thêm lời giải thích người học và quan sát kiểm tra tiếp | Giả thuyết nhận thức có được bằng chứng hỗ trợ hay không |

Code sai không đủ để xác nhận niềm tin của sinh viên. Với public corpus không có
phỏng vấn/lời giải thích, giữ `cognitive_status: "unassessed"`.

## Các gói đã chuẩn bị trên máy này

- `.cache/teacher-validation-itsp-20260928`: 48 bài development ITSP.
- `.cache/teacher-validation-cpack-20260928`: pilot 150 bài, tối đa 3 train và
  3 validation cho mỗi bài tập C-Pack-IPAs. Đây là pilot nhỏ, không phải gold toàn corpus.

Trong mỗi thư mục:

| File | Ai nhận và làm gì |
|---|---|
| `evidence.json` | Hai người đánh giá nhận code, outcomes và log test gốc; không có ID cụm, luật hay AI |
| `reviewer_1.json`, `reviewer_2.json` | Mỗi người nhận một file và tự điền độc lập |
| `adjudication.json` | Người thứ ba xem hai bản nhận xét và phân xử, kể cả trường hợp đồng ý |
| `coordinator.json` | Chỉ điều phối viên giữ; liên kết case với bài nộp, partition và hash lượt chạy |

Không sửa `evidence.json`, `case_id`, `packet_id` hoặc ánh xạ coordinator sau khi
phát phiếu. Muốn đổi bằng chứng thì tạo packet mới. Người đánh giá vòng đầu
không được thấy cluster ID, kết quả thuật toán, bản nhận xét của người kia hay AI.
Code có thể chứa tên trong comment; điều phối viên cần kiểm tra quyền chia sẻ
trước khi gửi dữ liệu thật. Không đưa dữ liệu lớp học/nhãn cá nhân vào Git.

## Cách điền phiếu

### Giao diện offline

Mở `deliverables/De5_GanNhan/reviewer_1.html` hoặc gửi `reviewer_2.html` cho người
đánh giá thứ hai. Mỗi file có 48 bài ITSP development cùng packet đã chuẩn bị;
không phải bài demo lớp học. Chọn dòng code/test trực tiếp, điền bộ nhãn do người
phụ trách phê duyệt, chọn kết luận và tải JSON. Không có nhãn điền sẵn hoặc gọi AI.
Các JSON tải xuống là lượt đánh giá độc lập, chưa phải gold đã phân xử.
Xem `deliverables/De5_GanNhan/HUONG_DAN.md` để lưu/khôi phục nháp.

Tạo giao diện cho packet khác (dùng thư mục output mới):

```powershell
& .\misconceptions-prototype\.venv\Scripts\python.exe `
  misconceptions-prototype/scripts/create_annotation_editor.py `
  --packet .cache/teacher-validation-itsp-20260928 --output .cache/my-review-forms
```

Kiểm tra file đã tải trước khi nhập vào bước đánh giá:

```powershell
& .\misconceptions-prototype\.venv\Scripts\python.exe `
  misconceptions-prototype/scripts/create_annotation_editor.py `
  --packet .cache/teacher-validation-itsp-20260928 --check PATH_TO_REVIEWER_JSON
```

Lệnh kiểm tra dùng cùng `validate_form` với evaluator. Bản nháp `.draft.json`
phải mở lại bằng giao diện và xuất thành phiếu hợp lệ trước khi đánh giá.
Đánh giá nhận thức và phân xử vẫn dùng schema/quy trình bên dưới.

### Quy định của phiếu

1. Giảng viên và điều phối viên chốt codebook: `version`, `approved_by`, danh sách
   `labels`, `label_policy: "single_primary"`. Các phiếu phải dùng cùng codebook.
   Không chọn bộ nhãn theo kết quả cụm hoặc sealed test.
2. Mỗi giảng viên điền `reviewer_id` thật hoặc mã ẩn danh đã được điều phối viên
   xác minh; `annotation_source: "human"`, `independent_blind_review: true`.
3. Với từng case, chọn `status` theo bảng dưới, ghi `rationale`.
4. Người phân xử riêng điền `adjudication.json`, có `reviewer_id` khác hai người
   trên. `coordinator_verified_by` ghi người đã kiểm tra danh tính, tính độc lập
   và nguồn bằng chứng. Hệ thống kiểm tra cấu trúc, không thể tự chứng thực danh tính.

| status | Ý nghĩa | mechanism |
|---|---|---|
| `pending` | Chưa đọc; giữ nguyên các trường trống của template | `null` |
| `supported` | Có cơ chế chính được code/test hỗ trợ | Một nhãn trong codebook |
| `uncertain` | Chưa đủ bằng chứng | `null` |
| `multiple` | Nhiều cơ chế, chưa chọn được một cơ chế chính | `null` |
| `no_target_error` | Không quan sát được lỗi mục tiêu | `null` |

`supported` bắt buộc có `source_lines` (số dòng bắt đầu từ 1), `test_ids` tồn tại
trong log và lý do cụ thể. Không bịa ca kiểm thử chưa quan sát.
`multiple` được giữ để xem xét riêng, không ép thành một nhãn để tính điểm.
Schema v1 chỉ chấm single-primary; không hỗ trợ điểm multi-label.

`cognitive_status` nhận `unassessed`, `insufficient_evidence`, `supported` hoặc
`rejected`. Hai trạng thái sau cần **cả** `learner_explanation` và
`follow_up_observation` thật, có thể truy vết tới biên bản do điều phối viên giữ.
Không chép lời AI vào những trường này. Xác nhận nhận thức còn yêu cầu cơ chế lỗi
ở trạng thái `supported`.

## Chạy đánh giá

Mở PowerShell tại root dự án; dùng đúng `.venv`:

```powershell
$py = '.\misconceptions-prototype\.venv\Scripts\python.exe'
$packet = '.cache/teacher-validation-cpack-20260928'
& $py misconceptions-prototype/scripts/validate_topic5.py evaluate `
  --run research/runs/cpack-validation-20260928 `
  --packet $packet `
  --reviews "$packet/reviewer_1.json" "$packet/reviewer_2.json" `
  --adjudication "$packet/adjudication.json" `
  --output .cache/teacher-evaluation-round1.json
```

Chọn tên output mới cho mỗi lần chấm. Không có nhãn thì trả
`waiting_for_teacher_labels` và các điểm cần gold là `null`. Chạy với phiếu rỗng
chỉ kiểm tra luồng phần mềm, không phải kiểm chứng khoa học.

Khi có nhãn hợp lệ, output gồm:

- Raw agreement/Cohen kappa của từng cặp giảng viên trước phân xử; hàng đợi bất đồng.
- ARI và pairwise precision/recall/F1 giữa cụm validation và gold cơ chế.
- Coverage nhãn trên mẫu số toàn bộ bài validation được gán cụm. Thiếu/không chắc
  chắn không trở thành nhãn đúng hoặc sai mặc định.
- Precision cơ chế và coverage của từng luật. Ánh xạ `cluster → mechanism` chỉ
  dùng gold **train**; thiếu nhãn hoặc hòa phiếu thì không đưa ra dự đoán cơ chế.
- Đánh giá nhận thức riêng, chỉ trên các trường hợp có bằng chứng nhận thức được
  phân xử xác nhận. Không đồng nhất với kết quả cơ chế lỗi.

Pairwise precision có mẫu số là các cặp cùng cụm trong số bài đã có gold;
recall có mẫu số là các cặp cùng nhãn gold. Mẫu số bằng 0 được giữ `null`.
Không gộp cặp giữa hai bài toán khác nhau. Điểm trên pilot là mô tả mẫu đã đánh
giá, chưa có khoảng tin cậy theo sinh viên và chưa chứng minh ưu thế tổng quát.

## Tạo gói mới hoặc dùng dữ liệu do giảng viên cung cấp

Dữ liệu mới cần chuẩn hóa theo schema `manifest.json`, `submissions.jsonl`,
`review.jsonl` của adapter hiện có; giữ ID sinh viên nhất quán xuyên bài và phiên
bản test. Nhãn, bài sửa sau đó, nhận xét và đường dẫn không đi vào đặc trưng.
Khóa split **toàn bộ corpus** trước khi chia từng cohort; xem [harness](harness.md)
và [hợp đồng đề 5](topic5-contract.md). Dữ liệu thật đặt ngoài Git.

Sau khi có lượt chạy validation đã audit, tạo phiếu bằng:

```powershell
& $py misconceptions-prototype/scripts/validate_topic5.py prepare `
  --run research/runs/cpack-validation-20260928 `
  --data .cache/cpack-validation-20260928/dataset `
  --max-per-partition 20 `
  --output .cache/teacher-validation-round2
```

Lựa chọn bài theo thứ tự SHA256, không dựa vào cụm/nhãn; tăng cỡ mẫu trước khi
phát phiếu, tránh thêm bài theo kết quả chấm. Đề bài thiếu trong manifest phải
được điều phối viên cung cấp từ nguồn gốc, không suy ra từ lời giải đúng.

Các file annotation v1 cũ dành cho ba arm A/B/C của ITSP vẫn được xử lý bằng
`merge_itsp_annotations.py` / `check_itsp_review.py`. Không trộn hai loại packet.
