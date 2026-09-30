# Bộ dữ liệu annotation Đề tài 5 — gửi AI đánh giá

**74 cluster đang chờ annotation**, không có gold label tự gán và chưa có phản hồi AI thật.
Tổng 2.189 bài thuộc train/validation của corpus public, không dùng dữ liệu lớp học/live.

| Gói | Cluster được chọn | Số bài | Cluster bị loại | Ngữ cảnh đề bài |
|---|---:|---:|---:|---|
| [ITSP — bắt đầu ở đây](itsp/README.md) | 5 | 38 | 4 | Có mô tả đề bài gốc |
| [C-Pack — mở rộng](cpack/README.md) | 69 | 2.151 | 6 | Có input/oracle, chưa có đề bài gốc |

## Cách gửi cho AI

1. Chọn gói ITSP trước, mở danh sách cluster trong README của gói.
2. Gửi [prompt ITSP](itsp/PROMPT.md), [schema kết quả](itsp/response.schema.json)
   và **một file** trong `itsp/clusters/` (JSON hoặc Markdown).
3. Yêu cầu AI trả JSON theo schema, giữ đúng `packet_id` và `cluster_id`.
4. Lưu phản hồi thành file riêng rồi kiểm tra bằng lệnh dưới đây.
5. Lặp lại các cụm còn lại. Với C-Pack, dùng prompt/schema/packet ID của gói C-Pack.

File khởi đầu nhỏ, có 4 bài và đầy đủ statement:
[ITSP 2825, cluster 2](itsp/clusters/2825--kmeans--combined_stdout--s42--c2.md).
Mỗi file cluster giữ **toàn bộ** raw_code, test input/expected/output và OAV của thành viên.
Tối đa 4 bài được đánh dấu đại diện, không có nghĩa các bài còn lại được phép bỏ qua.
Một số cụm C-Pack lớn; nếu AI không đọc hết dữ liệu thì phải khai báo giới hạn và uncertain.

Muốn lấy toàn bộ dữ liệu một gói:
[ITSP evidence.json](itsp/evidence.json) hoặc [C-Pack evidence.json](cpack/evidence.json).
Không cần gửi cả gói vào một lần chat; không cần API key để tạo/kiểm tra packet.

## Nhận kết quả

Từ repository root, PowerShell (đường dẫn phản hồi là ví dụ, không có kết quả AI giả lập kèm theo):

```powershell
$py = '.\misconceptions-prototype\.venv\Scripts\python.exe'
& $py misconceptions-prototype/scripts/export_cluster_annotations.py validate `
  --packet deliverables/De5_Annotation_20260928/itsp/evidence.json `
  --response .cache/ai-response-1.json .cache/ai-response-2.json `
  --output .cache/ai-reviews-checked.json
```

Thêm `--require-complete` khi đã đủ 5 cụm ITSP (hoặc đủ 69 cụm C-Pack).
Không trộn hai packet; không lặp cluster ID giữa các phản hồi.
Output giữ `annotation_source: ai`, `human_validated: false`, `mechanism_accuracy: null`.
File evidence gốc luôn giữ `pending_annotation` để bảo toàn snapshot.

`response.template.json` là danh sách chờ với `result: null`, **không phải kết quả đã chấm**.
AI tạo kết quả dựa trên `response.schema.json`, gồm các trường được yêu cầu và
`evidence_refs` để kiểm tra nguồn dẫn chứng. `supported/rejected/uncertain` đánh giá
cơ chế nêu trong `misconception_label`, không chứng minh niềm tin thật của sinh viên.

## Điều kiện chọn và giới hạn

Chọn cố định K-means / combined_stdout / seed 42, không chọn lần chạy có điểm đẹp nhất.
Tối thiểu 4 bài, 3 source khác nhau, đủ code/log mọi test trượt, có test trượt ở >=50% bài.
10 cụm bị loại vì quá nhỏ (một số đồng thời có ít hơn 3 source); chi tiết trong từng README.
Tỷ lệ dựa trên số **bài nộp**, không mặc định là các sinh viên độc lập.
Thiếu/not_run không được xem là pass. Candidate, AST pattern và rule đều có thể sai.

Clustering OAV và IF–THEN giữ từ run đã audit; chẩn đoán AST/log được chạy lại khi xuất
và có fingerprint mã nguồn riêng. Chỉ phân tích log lịch sử, không chạy lại C.
Không xuất lời giải đúng, nhãn giảng viên hay sealed test; statement ITSP chỉ lấy comment đầu file.
C-Pack thiếu đề bài và chưa kiểm chứng lại sự tương ứng suite lịch sử bằng replay:
AI phải nêu các giả định, không suy ra yêu cầu ngoài input/oracle.

Chi tiết tái tạo và tiêu chí kiểm tra: [docs/cluster_annotation.md](../../docs/cluster_annotation.md).
