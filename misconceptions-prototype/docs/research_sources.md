# Nguồn nghiên cứu và quyết định phương pháp

Ngày rà soát: **19/09/2026**. Chỉ dùng tài liệu công bố không muộn hơn mốc này; ngày crawler không phải ngày xuất bản. Các repository là trạng thái đọc tại ngày rà soát, chưa phải snapshot lịch sử đã đóng băng. Đây là khảo sát có mục tiêu, không tuyên bố tổng quan hệ thống đầy đủ hoặc xác lập một mô hình SOTA tuyệt đối. Chưa có dữ liệu chính thức từ giảng viên; không nguồn nào dưới đây được coi là dataset của đề tài.

## 1. Những kết quả gần bài toán nhất

### McMining — EACL, tháng 3/2026

Al-Hossami và Bunescu nghiên cứu suy luận misconception từ một hoặc nhiều cặp đề bài–code. Benchmark có 67 misconception, 1.063 mẫu biểu hiện misconception và các mẫu đối chứng. **Code lỗi được tạo bằng McInject trên lời giải đúng**, không phải toàn bộ là bài sai thu trực tiếp từ sinh viên. Nhiều bài của cùng người học có thể cung cấp bằng chứng mạnh hơn một lỗi đơn lẻ. Giới hạn: đánh giá phần lớn dựa vào LLM judge; biểu hiện trong code có thể mơ hồ. Không lấy điểm benchmark này làm hiệu quả trên lớp học thật. [Bài EACL 2026](https://aclanthology.org/2026.eacl-short.10/), [toàn văn](https://aclanthology.org/2026.eacl-short.10.pdf).

Kho McMiner công bố code theo MIT, ngân hàng misconception và dữ liệu nguồn có xuất xứ riêng; không suy ra MIT thay thế mọi điều khoản nguồn. Phù hợp làm bộ từ vựng/rubric và stress test giả lập; không bắt buộc dùng API LLM ở prototype CPU. [Repository tác giả](https://github.com/taisazero/mcminer).

### Logical errors — EDM, tháng 7/2025

Hoq và cộng sự dùng SANN biểu diễn subtree AST, huấn luyện bằng correctness và kiểm tra các vùng lỗi bằng chuyên gia. Dữ liệu CodeWorkout Java; đây không phải thuật toán gom cụm phi giám sát. Công trình phân biệt lỗi khái niệm, chiến lược và lỗi cú pháp vẫn biên dịch được, đồng thời thừa nhận khó suy ra bất cẩn hay hiểu sai đề từ code. Bài học phù hợp: có bằng chứng cấu trúc và người gán nhãn; không mặc định attention chính là nguyên nhân. Chưa cần tái tạo SANN khi chưa có dữ liệu và baseline. [Toàn văn hội nghị](https://educationaldatamining.org/EDM2025/proceedings/2025.EDM.long-papers.85/index.html).

### Conceptual Mutation Testing — Programming, 2024

Prasad, Greenman, Nelson và Krishnamurthi (Brown và cộng tác viên) gom nhóm **test do sinh viên viết nhưng thất bại trên chương trình đúng**, rồi chuyển nhóm thành conceptual mutants. Đây là hiểu sai đặc tả bài tập, khác với chỉ gom code sai hoặc hiểu sai ngữ nghĩa ngôn ngữ. Kết quả gợi ý thiết kế test chẩn đoán theo khái niệm, thay vì mutation cú pháp tùy ý. Không tuyên bố mutant tự động tương đương misconception thật. [Trang công trình tác giả](https://static.cs.brown.edu/~sk/Publications/Papers/Published/pgnk-conceptual-examplar/).

### ProgMiscon — ITiCSE 2021 và kho sống

Kho do nhóm nghiên cứu duy trì tổ chức misconception theo ngôn ngữ và khái niệm, có liên hệ tài liệu giảng dạy. Dùng để soạn rubric, giữ tên khái niệm nhất quán; không xem đây là corpus bài làm có nhãn. Một niềm tin sai phải được diễn giải trong đúng ngôn ngữ: C truyền giá trị kể cả giá trị con trỏ; C++ có tham số tham chiếu. [Programming Misconceptions](https://progmiscon.org/).

## 2. Dataset có thể dùng cho prototype

| Nguồn | Dữ liệu/bằng chứng sẵn có | Hạn chế và vai trò hợp lý |
|---|---|---|
| C-Pack-IPAs, APR 2024; preprint 2022 | Bài sinh viên thật bằng C90; 25 bài tập; code đúng/sai logic/sai biên dịch; mô tả đề, test I/O, reference implementation; ID sinh viên ẩn danh nhất quán. | Không có nhãn misconception được xác nhận. Có tests không có nghĩa đã có ma trận outcome từng lần chạy; cần replay an toàn hoặc log đánh giá. Ưu tiên thử một bài nhỏ nếu chọn C. |
| CodeWorkout, bản Spring/Fall 2019 | Bài Java, lịch sử submission, điểm correctness; các bản được công bố qua CSEDM/DataShop, thường dùng ProgSnap2. | Không suy ra vector test-ID pass/fail từ điểm tổng hợp. Phù hợp nghiên cứu cấu trúc/lịch sử; chỉ chạy baseline test-level khi xác minh trường dữ liệu hoặc có test suite. |
| IBM Project CodeNet, 2021 | Code thật từ AIZU/AtCoder, verdict, ID người dùng/bài, metadata; một số sample I/O. | Verdict Wrong Answer không phải misconception; sample I/O không phải toàn bộ hidden tests; quy mô và miền thi đấu không ưu tiên cho bước đầu. |
| CodeInsight, preprint 01/09/2026 | Hơn 3 triệu submission C++, 3.286 sinh viên; timestamps, outcome từng test. Tác giả mô tả cung cấp đề, tests và grading scripts cho người được duyệt. | **Phải xin quyền**, departmental license cho giáo dục; không giả định tải ngay. Không có tuyên bố nhãn misconception. Khác CodeInsight Stack Overflow 2024. |
| McMining, 2026 | Ngân hàng misconception và code mô phỏng có mục tiêu. | Dùng stress test; phải đánh dấu synthetic và tách khỏi đánh giá dữ liệu thật. |

Nguồn và điều kiện tiếp cận:

- **C-Pack-IPAs:** repository công khai, [README chính thức](https://github.com/pmorvalho/C-Pack-IPAs) và [LICENSE.md MIT](https://raw.githubusercontent.com/pmorvalho/C-Pack-IPAs/main/LICENSE.md). README nêu chỉ giữ bài của sinh viên đồng ý dùng cho học thuật, bỏ comments. Đóng băng commit và giữ attribution nếu tải về.
- **CodeWorkout:** [trang dataset CSEDM](https://sites.google.com/ncsu.edu/csedm-dc-2021/dataset), [DataShop Spring 2019](https://pslcdatashop.web.cmu.edu/Files?datasetId=3458). Trang CSEDM không tải được nội dung trong phiên này; việc có bản công khai và cấu trúc được đối chiếu bằng [KC-Finder, EDM 2023](https://educationaldatamining.org/edm2023/proceedings/2023.EDM-long-papers.3/). Chưa xác minh license của file dataset; **AGPL của nền tảng và CC BY-NC-SA của bài tập không tự động là license bài sinh viên**. [License nền tảng](https://codeworkout.cs.vt.edu/home/license).
- **CodeNet:** [repository IBM](https://github.com/IBM/Project_CodeNet) công bố tooling Apache-2.0. Khi tải dataset cần kiểm tra license đi kèm archive riêng. README mô tả trường `accuracy` chỉ là số test pass của AIZU, không phải danh sách outcome từng test. Không tải toàn bộ archive lớn chỉ để thử pipeline.
- **CodeInsight:** [arXiv v1, 01/09/2026](https://arxiv.org/html/2609.00940v1), [điểm truy cập dataset do bài báo dẫn](https://huggingface.co/datasets/CodeInsightTeam/code_insights_csv). Đây là preprint tại cutoff; không suy diễn đã peer review. License CC trên bài báo không thay departmental license của dataset. Chưa yêu cầu quyền hay tải data trong phần khảo sát này.

## 3. Sửa hai nhầm lẫn thuật toán trong đề xuất ban đầu

**ILA không phải thuật toán clustering.** Bài gốc trình bày induction các luật IF–THEN từ ví dụ huấn luyện để phân loại. Có thể dùng cluster ID làm pseudo-label để sinh luật mô tả cụm, nhưng kết quả chỉ giải thích phân vùng; không tự biến thành nhãn misconception. Nếu yêu cầu bắt buộc ILA cải tiến, phải chỉ rõ bản thuật toán, objective, và baseline thay vì tự đặt tên cho heuristic. [ILA: an inductive learning algorithm for rule extraction, 1998](https://www.sciencedirect.com/science/article/abs/pii/S0957417497000894).

**Lựa chọn của đề tài, không phải tuyên bố từ paper:** với OAV chủ yếu categorical/binary, khởi đầu bằng nhóm chữ ký lỗi và khoảng cách Hamming có trọng số trên thuộc tính, rồi average-linkage hoặc medoid. K-means tiêu chuẩn tối ưu bình phương Euclid; không thay tên metric thành Hamming mà giữ cập nhật trung bình. Nếu cần K-means làm đối chứng: one-hot, chuẩn hóa trọng số nhóm, nêu rõ hình học Euclid và kiểm tra độ nhạy với số cụm.

## 4. Hàm ý cho pipeline ít tài nguyên

Các đề xuất dưới đây là tổng hợp thiết kế cho đề tài, chưa phải kết quả thực nghiệm:

1. Giữ object là một submission; OAV là bằng chứng quan sát: test ID, trạng thái, lớp input chẩn đoán, predicate AST có địa chỉ nguồn. Nhãn misconception và ID sinh viên không được đưa vào khoảng cách.
2. Chỉ so sánh trong cùng bài, ngôn ngữ và phiên bản tests; tách compile/runtime failure để không gán lỗi cú pháp thành logic.
3. Phân biệt `missing/not_run` với `pass/fail`. Hai bản thiếu cùng test không phải bằng chứng hiểu sai giống nhau. Báo coverage quan sát và từ chối kết luận khi không đủ overlap.
4. Cân trọng số giữa nhóm tests và nhóm cấu trúc; loại thuộc tính hằng, không để nhiều test tương đương áp đảo một khái niệm. Chạy ablation tests-only, structure-only, combined.
5. Bắt đầu từ một bài và vài chục/vài trăm submission. CPU + file JSONL/CSV + thư viện chuẩn/scikit-learn đủ để kiểm tra giả thuyết; chưa cần vector database, graph neural network hay fine-tuning.
6. Luật `IF evidence THEN cluster` phải có support, precision, coverage và độ ổn định trên sinh viên giữ lại. Luật misconception chỉ được chấp nhận khi chuyên gia kiểm tra; lưu trạng thái `candidate/confirmed/rejected/uncertain`.
7. Giữ mẫu đúng làm đối chứng ngoài cụm bài sai. Một bài sai có nhiều nguyên nhân; cho phép nhiều nhãn hoặc chưa đủ bằng chứng. Theo dõi nhiều bài của cùng sinh viên giúp kiểm tra tính lặp lại, nhưng không dùng mọi lần nộp như người học độc lập.
8. Đánh giá nội tại (silhouette, stability) không đo độ đúng giáo dục. Khi có nhãn: hai người chấm độc lập một tập nhỏ, agreement, pairwise precision/recall; ARI/NMI chỉ khi ground truth là phân hoạch phù hợp. Tách theo sinh viên, kiểm tra duplicates và khóa test set trước tuning.

Để thay dataset không viết lại hệ thống: adapter chỉ chuyển nguồn vào schema chung; core nhận submissions/OAV, không biết layout nguồn. Có thể học cách lưu sự kiện và code states từ [ProgSnap2 — bài ITiCSE 2020](https://ayaankazerouni.org/papers/2020/iticse20-progsnap2.pdf) và [spec/example chính thức](https://github.com/CSSPLICE/progsnap2). Không cần triển khai toàn bộ tiêu chuẩn nếu chỉ nhận JSONL; cần lưu provenance, suite version, missingness, learner ID ẩn danh và nguồn nhãn.

## 5. Điều gì được phép kết luận trước khi có data giảng viên?

Smoke test tổng hợp chỉ xác minh phần mềm chạy và metric/rule tính đúng. Prototype công khai kiểm tra khả năng vận hành trên miền cụ thể. Cả hai **không chứng minh** tỷ lệ misconception, hiệu quả giảng dạy, độ chính xác trên lớp mục tiêu hay lợi thế SOTA. Tiêu chí thành công ban đầu là tái lập được kết quả, thay adapter được, không leakage, và xuất bằng chứng đủ để giảng viên kiểm tra. Sau khi nhận data thật mới quyết định ngôn ngữ, taxonomy, ngưỡng clustering và thí nghiệm đánh giá chính thức.
