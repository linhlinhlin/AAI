# Bộ phiếu đánh giá độc lập — 17 bài ITSP

Bộ này không chứa nhãn AI, giả thuyết nguyên nhân, nhãn chuyên gia khác hoặc assignment clustering. Gửi riêng một bản sao cho mỗi người đánh giá; không dùng chung file khi đánh giá độc lập. Chưa có nhãn nào được điền.

## Bắt đầu

1. Giải nén ZIP, mở README này; mọi link hồ sơ phải mở được offline.
2. Đọc [CODEBOOK.md](CODEBOOK.md). Đây là bản dự thảo không có nhãn theo mẫu; thống nhất phiên bản và quy tắc nhãn chính với người điều phối **trước khi chấm**. Không xem nhãn tham khảo hay trao đổi quyết định từng mẫu với người khác.
3. Nhận mã reviewer riêng. Sao chép `annotations.json` thành `annotations_<reviewer_id>_round1.json`, lưu UTF-8 và chỉ sửa các trường hướng dẫn bên dưới. Không dùng trình soạn thảo tự đổi dấu ngoặc kép thành dấu ngoặc thông minh.
4. Đọc từng đề/buggy/log trước, ghi suy luận ban đầu rồi đối chiếu bản sửa. Ghi nếu bản sửa làm thay đổi suy luận. Main.c có cả lời giải tham chiếu gốc; gói này không mù với lời giải, chỉ mù với nhãn/cluster.

Không có deadline hay reviewer ID giả định trong gói. Người điều phối cung cấp lịch và kênh trả file riêng.

## Vòng 1: đánh giá từng bài

Mở đề, source lỗi, bản sửa cùng cặp và log ở bảng dưới. Log là kết quả lịch sử của dataset, không phải kết quả chạy lại; bản sửa được cung cấp như bằng chứng, không chứng minh người học đã hiểu một khái niệm. Không chạy code để điền phiếu.

Điền `annotations.json`, đúng submission ID, trong `reviews`:

- `reviewer_id`: mã người đánh giá thật, không phải mã sinh viên; không dùng tiền tố `ai:`.
- `misconception`: Yes / No / Unclear. Yes khi bằng chứng ủng hộ hiểu sai khái niệm; No khi đánh giá không phải misconception; Unclear khi đã xem nhưng chưa đủ phân biệt hiểu sai với sơ suất. Chưa xem giữ null.
- `misconception_type`: một mã thuộc codebook chung đã chốt nếu Yes; có thể null nếu chưa phân loại được hoặc nhiều cơ chế ngang nhau. No/Unclear luôn null. Không tự duyệt codebook hoặc thêm mã giữa vòng chấm; ghi đề xuất trong evidence.
- `confidence`: số nguyên 1–5 (rất thấp, thấp, vừa, cao, rất cao), mức tự tin vào quyết định của mình.
- `evidence`: dòng code, test cụ thể và lý do; ghi nhận xung đột đề/oracle, lỗi đồng thời hoặc bằng chứng còn thiếu.
- `independent_blind_review`: chỉ đổi thành true nếu chưa xem nhãn AI, nhãn người khác hoặc cluster trước khi hoàn tất vòng này. Nếu đã xem, giữ false và ghi rõ trong evidence.
- `status`: complete khi đã điền reviewer_id, decision, confidence và evidence. Giữ pending nếu chưa xong.

Giữ nguyên `same_cause_as_cluster` (A/B/C đều null), `adjudication` và codebook đã được người điều phối phân phối ở vòng 1. Không thay submission ID, problem ID hoặc assignments_sha256.

## Điền Unclear và kiểm tra trước khi trả

Unclear vẫn là phiếu **complete** nếu đã xem đủ nhưng chưa phân giải được. Điền reviewer_id, `misconception="Unclear"`, `misconception_type=null`, confidence và evidence gồm: điều quan sát chắc chắn; các nguyên nhân thay thế; evidence còn thiếu. Confidence đo mức chắc chắn vào quyết định Unclear, không phải xác suất người học hiểu sai; vì vậy Unclear không bắt buộc confidence thấp. Không điền nhãn theo số test fail để tránh Unclear.

Ví dụ cấu trúc phiếu (chỉ minh họa cú pháp, không phải annotation cho bất kỳ hồ sơ nào):

```json
{
  "status": "complete",
  "reviewer_id": "<ma-nguoi-danh-gia-thuc>",
  "misconception": "Unclear",
  "misconception_type": null,
  "confidence": 3,
  "evidence": "Thay bằng dòng code, test ID/input/expected/actual, giải thích cạnh tranh và evidence còn thiếu.",
  "independent_blind_review": false,
  "same_cause_as_cluster": {"A": null, "B": null, "C": null}
}
```

Ví dụ giữ false có chủ ý: chỉ reviewer tự xác nhận điều kiện mù mới đặt true. Không sao chép placeholder evidence vào phiếu thật. Null là giá trị JSON không có dấu ngoặc kép. Confidence phải là số nguyên 1–5 (High 4–5, Medium 3, Low 1–2), không dùng chữ trong JSON.

Trước khi trả: kiểm đủ 17 submission ID không trùng/thiếu; cùng mã reviewer trong các phiếu; No/Unclear không có type; mọi complete có evidence cụ thể; các mục chưa đọc còn pending/null; không thay adjudication; không tự điền A/B/C. Nếu thiếu thời gian, gửi bản chưa hoàn tất với pending đúng thực tế và báo số phiếu còn thiếu. Trả file JSON, mã reviewer, phiên bản codebook, xác nhận điều kiện độc lập và những vấn đề về đề/oracle qua kênh người điều phối cung cấp. Giữ một bản sao nguyên trạng.

## Vòng 2 và bàn giao

Gửi lại bản đã điền cho người điều phối để lưu bản vòng 1 trước khi mở ngữ cảnh cluster. Vòng 2 sẽ nhận danh sách thành viên cụm riêng; điền A/B/C bằng Yes / Partially / No, hoặc null nếu chưa đủ ngữ cảnh. Yes: cùng nguyên nhân thực chất với tất cả thành viên đã đánh giá; Partially: chỉ một phần hoặc nhiều nguyên nhân; No: không có nguyên nhân chung phù hợp. Ghi rõ phạm vi đã xem.

Giữ nguyên các lượt độc lập khi thảo luận nhãn thống nhất. Codebook, chính sách nhãn chính và adjudication phải do chuyên gia xác nhận. Agreement giữa người đánh giá cần ít nhất hai người đánh giá các mẫu chung; một người không đủ tính inter-rater agreement.

## Hồ sơ

| Bài / Submission | Đề | Source | Bản sửa | Log |
|---|---|---|---|---|
| 2812 / itsp-2812-270276_buggy | [đề](itsp-2812-270276_buggy/Main.c) | [source](itsp-2812-270276_buggy/buggy.c) | [bản sửa](itsp-2812-270276_buggy/paired_correct.c) | [log](itsp-2812-270276_buggy/logged_tests.json) |
| 2812 / itsp-2812-270277_buggy | [đề](itsp-2812-270277_buggy/Main.c) | [source](itsp-2812-270277_buggy/buggy.c) | [bản sửa](itsp-2812-270277_buggy/paired_correct.c) | [log](itsp-2812-270277_buggy/logged_tests.json) |
| 2812 / itsp-2812-270283_buggy | [đề](itsp-2812-270283_buggy/Main.c) | [source](itsp-2812-270283_buggy/buggy.c) | [bản sửa](itsp-2812-270283_buggy/paired_correct.c) | [log](itsp-2812-270283_buggy/logged_tests.json) |
| 2812 / itsp-2812-270285_buggy | [đề](itsp-2812-270285_buggy/Main.c) | [source](itsp-2812-270285_buggy/buggy.c) | [bản sửa](itsp-2812-270285_buggy/paired_correct.c) | [log](itsp-2812-270285_buggy/logged_tests.json) |
| 2812 / itsp-2812-270293_buggy | [đề](itsp-2812-270293_buggy/Main.c) | [source](itsp-2812-270293_buggy/buggy.c) | [bản sửa](itsp-2812-270293_buggy/paired_correct.c) | [log](itsp-2812-270293_buggy/logged_tests.json) |
| 2825 / itsp-2825-271154_buggy | [đề](itsp-2825-271154_buggy/Main.c) | [source](itsp-2825-271154_buggy/buggy.c) | [bản sửa](itsp-2825-271154_buggy/paired_correct.c) | [log](itsp-2825-271154_buggy/logged_tests.json) |
| 2825 / itsp-2825-271163_buggy | [đề](itsp-2825-271163_buggy/Main.c) | [source](itsp-2825-271163_buggy/buggy.c) | [bản sửa](itsp-2825-271163_buggy/paired_correct.c) | [log](itsp-2825-271163_buggy/logged_tests.json) |
| 2825 / itsp-2825-271173_buggy | [đề](itsp-2825-271173_buggy/Main.c) | [source](itsp-2825-271173_buggy/buggy.c) | [bản sửa](itsp-2825-271173_buggy/paired_correct.c) | [log](itsp-2825-271173_buggy/logged_tests.json) |
| 2825 / itsp-2825-271188_buggy | [đề](itsp-2825-271188_buggy/Main.c) | [source](itsp-2825-271188_buggy/buggy.c) | [bản sửa](itsp-2825-271188_buggy/paired_correct.c) | [log](itsp-2825-271188_buggy/logged_tests.json) |
| 2825 / itsp-2825-271203_buggy | [đề](itsp-2825-271203_buggy/Main.c) | [source](itsp-2825-271203_buggy/buggy.c) | [bản sửa](itsp-2825-271203_buggy/paired_correct.c) | [log](itsp-2825-271203_buggy/logged_tests.json) |
| 2825 / itsp-2825-271213_buggy | [đề](itsp-2825-271213_buggy/Main.c) | [source](itsp-2825-271213_buggy/buggy.c) | [bản sửa](itsp-2825-271213_buggy/paired_correct.c) | [log](itsp-2825-271213_buggy/logged_tests.json) |
| 2833 / itsp-2833-271912_buggy | [đề](itsp-2833-271912_buggy/Main.c) | [source](itsp-2833-271912_buggy/buggy.c) | [bản sửa](itsp-2833-271912_buggy/paired_correct.c) | [log](itsp-2833-271912_buggy/logged_tests.json) |
| 2833 / itsp-2833-271916_buggy | [đề](itsp-2833-271916_buggy/Main.c) | [source](itsp-2833-271916_buggy/buggy.c) | [bản sửa](itsp-2833-271916_buggy/paired_correct.c) | [log](itsp-2833-271916_buggy/logged_tests.json) |
| 2833 / itsp-2833-271920_buggy | [đề](itsp-2833-271920_buggy/Main.c) | [source](itsp-2833-271920_buggy/buggy.c) | [bản sửa](itsp-2833-271920_buggy/paired_correct.c) | [log](itsp-2833-271920_buggy/logged_tests.json) |
| 2833 / itsp-2833-271965_buggy | [đề](itsp-2833-271965_buggy/Main.c) | [source](itsp-2833-271965_buggy/buggy.c) | [bản sửa](itsp-2833-271965_buggy/paired_correct.c) | [log](itsp-2833-271965_buggy/logged_tests.json) |
| 2833 / itsp-2833-271975_buggy | [đề](itsp-2833-271975_buggy/Main.c) | [source](itsp-2833-271975_buggy/buggy.c) | [bản sửa](itsp-2833-271975_buggy/paired_correct.c) | [log](itsp-2833-271975_buggy/logged_tests.json) |
| 2833 / itsp-2833-271986_buggy | [đề](itsp-2833-271986_buggy/Main.c) | [source](itsp-2833-271986_buggy/buggy.c) | [bản sửa](itsp-2833-271986_buggy/paired_correct.c) | [log](itsp-2833-271986_buggy/logged_tests.json) |

Mẫu được chọn có chủ đích, không đại diện toàn cohort. Dataset thiếu student ID; submission ID chỉ định danh bài làm. Không suy rộng sang unseen student.
