# Từ luật phân cụm đến giả thuyết cơ chế lỗi

## Quyết định triển khai

Luật cây quyết định hiện có được huấn luyện với **cluster ID**. Vì vậy đổi câu
“THÌ cụm 2” thành một misconception sẽ thay đổi ý nghĩa mà không có bằng chứng.
Hướng được chọn cho prototype là **bộ luật chuyên môn dựa trên AST và log test**,
hiển thị song song với luật phân cụm được dịch sang tiếng Việt.

| Hướng | Ưu điểm | Hạn chế | Quyết định |
|---|---|---|---|
| Chỉ dịch tên feature | Rẻ, dễ đọc, giữ nguyên ý nghĩa | Không suy ra cơ chế lỗi | Dùng cho luật giải thích cụm |
| LLM tự đặt tên cụm | Diễn đạt linh hoạt | Cần đánh giá độ đúng, chi phí và kiểm soát suy diễn | Chưa chọn làm bộ kết luận |
| AST + log + luật chuyên môn | Chạy CPU, bằng chứng xác định, kiểm thử âm được | Coverage hẹp; phải viết detector cho từng cơ chế | Chọn cho bước hiện tại |
| Học luật từ nhãn chuyên gia | Có thể đo chất lượng dự đoán misconception | Chưa có ground truth đủ dùng | Bước sau khi có nhãn độc lập |

Đây là lựa chọn phù hợp tài nguyên và tình trạng dữ liệu, không phải tuyên bố đạt SOTA.
Không đổi thuật toán phân cụm, feature space, split hoặc scorer annotation.

## Những luật đang hỗ trợ

- `C_BRANCH_ATTACHMENT`: AST có hai if liên tiếp, else thuộc if thứ hai; log thất bại
  của bài phân loại vị trí đường tròn chứa nhiều thông báo vị trí. Đề xuất kiểm tra
  nhầm quan hệ nhánh; có thể chỉ là sơ suất thiếu `else`. Chưa có tracing để chứng minh
  quan hệ nhân quả giữa đoạn code và output; code khác cũng có thể góp phần tạo output.
- `C_SWAP_BY_VALUE`: nhận diện hẹp hàm `void f(int a,int b)` (hoặc float/double cùng kiểu),
  thân thẳng `T temp=a; a=b; b=temp;`, lời gọi trực tiếp bằng hai identifier và log
  hai số nguyên khác nhau: expected đảo thứ tự, actual giữ nguyên input. Tên hàm/biến
  có thể đổi. Không hỗ trợ mọi biến thể swap, macro, alias hay luồng gọi gián tiếp.
  Output không phải trace trạng thái ngay sau lời gọi: phải xem vị trí in/gán lại biến.
- `OUTPUT_PRESENTATION`: chuỗi trong source và log chỉ khác hoa/thường, khoảng trắng,
  hoặc dấu chấm cuối thông báo đường tròn. Đây là vấn đề trình bày, không được tính
  thành misconception; không xóa dấu âm, dấu thập phân hoặc dấu câu tùy ý để so sánh.

Không dùng paired-correct code, annotation AI hoặc nhãn chuyên gia để sinh các giả thuyết.
Luật hiện được viết thủ công, chưa phải luật misconception được quy nạp từ dữ liệu.
Phần quy nạp cây quyết định vẫn chỉ dự đoán cluster ID. Chưa có precision/recall
về misconception; số bài khớp và phân bố train/holdout/cụm chỉ mô tả coverage.
Các giả thuyết này không được đưa vào làm ground truth để đánh giá chính clustering.

## Cách thử trên web

1. Tải lại http://127.0.0.1:8765, chọn **2825**, chạy và mở **Luật giải thích**.
2. Xem phần **Luật gợi ý cơ chế lỗi** phía trên. Mở từng bài để xem dòng code và
   input/expected/actual, giả thuyết thay thế và gợi ý giảng lại.
3. Phần **Luật giải thích cách phân cụm** phía dưới có tên ca test dễ đọc và ký hiệu
   gốc trong mục mở rộng. Phủ định “không đạt điều kiện pass” không bị đổi thành fail:
   chưa chạy, timeout và unknown là các trạng thái khác nhau.
4. Chọn **demo_swap_by_value**, chạy và mở Luật giải thích để xem ví dụ truyền tham trị.
   Hai bài này là fixture tổng hợp, output suy ra thủ công, **không phải log thực thi
   hoặc dữ liệu sinh viên**. Không đủ mẫu để phân cụm; luật cơ chế vẫn hiển thị.
5. Dataset không có log hoặc không khớp detector sẽ ghi rõ thiếu bằng chứng/chưa có luật.

## Dữ liệu riêng và CLI

Có thể nhập thêm `review.jsonl` tùy chọn bên cạnh manifest và submissions trên web:

```json
{"submission_id":"s1","logged_tests":[{"test_id":"1","input":"2 7","expected":"7 2","output":"2 7","verdict":"WRONG_ANSWER"}]}
```

Mỗi dòng một submission; test ID phải thuộc outcomes và không trùng. Input/oracle
phải thống nhất giữa các bài cùng test ID. `verdict` tùy chọn; nếu có phải khớp outcome.
Người cung cấp chịu trách nhiệm về nguồn log, vì validation không xác thực đã thực thi.
CLI tự đọc `review.jsonl` cạnh submissions hoặc nhận `--evidence <path>`.
Kết quả có `teaching.version`, hash bộ luật, hash evidence, chi tiết source và log;
provenance hiện có lưu hash manifest/submissions. Kết quả cũ không được sửa hồi tố.

## Cơ sở tham khảo

- [scikit-learn: cấu trúc cây quyết định](https://scikit-learn.org/1.8/auto_examples/tree/plot_unveil_tree_structure.html):
  đường đi trong cây giải thích các quyết định dự đoán của cây. Khi target là cluster ID,
  nó không tự trở thành nhãn hiểu sai. Đây là lý do giữ hai phần giải thích riêng.
- [Ureel & Wallace, SIGCSE 2019 — Automated Critique of Early Programming Antipatterns](https://cserg.cs.mtu.edu/publications/ureel2019sigcse.pdf):
  WebTA kết hợp mẫu mã, AST, test và hướng dẫn theo bài tập để phản hồi lỗi thường gặp.
  Prototype áp dụng nguyên tắc ghép bằng chứng và lời giải thích; không sao chép hoặc
  khẳng định tái hiện đầy đủ hệ thống WebTA.
- [Lu & Krishnamurthi, 2024 — Identifying and Correcting Programming Language Behavior Misconceptions](https://doi.org/10.1145/3649823):
  dùng để định hướng phân biệt hành vi ngôn ngữ và quan niệm của người học. Một mẫu lỗi
  đơn lẻ vẫn cần kiểm chứng trước khi kết luận về nhận thức.

Các nguồn trên xuất bản trước mốc 19/09/2026. Danh sách là cơ sở cho quyết định này,
không phải tổng quan đầy đủ mọi nghiên cứu đến mốc đó.
