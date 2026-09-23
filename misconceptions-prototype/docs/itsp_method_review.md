# ITSP: rà soát dữ liệu và phương pháp

Ngày rà soát: **19/09/2026**. Phạm vi: nguồn sơ cấp và code prototype; đây là rà soát có mục tiêu, không phải systematic review hoặc chứng minh SOTA. ITSP chỉ là **dữ liệu công khai cho prototype**, không thay thế dataset chính thức chưa được giảng viên cung cấp. Các mục dưới là kết luận phương pháp và tiêu chí kiểm tra; số liệu chạy thực tế nằm trong báo cáo thực nghiệm riêng.

## 1. Những điều nguồn gốc xác nhận

[README ITSP](https://github.com/jyi/ITSP) mô tả 661 chương trình C, đề bài/lời giải trong `Main.c`, input/output test và cặp `*_buggy.c`–`*_correct.c`. Số trong tên file được gọi là **assignment-ID**, không phải ID sinh viên toàn cục. Comment đầu file lưu kết quả test. Vì vậy không suy diễn `270010` là một người học duy nhất xuyên suốt nhiều bài.

[Bài báo ESEC/FSE 2017, mục 3](https://abhikrc.com/pdf/FSE17.pdf) lấy mẫu cặp chương trình sai và phiên bản đúng sau đó của cùng sinh viên; loại trường hợp không biên dịch được. Đây là tập đã được chọn theo khả năng có lời giải đúng về sau, không phải toàn bộ lịch sử bài làm của lớp. Suy luận của dự án: không dùng tỷ lệ cụm trên ITSP để khẳng định tỷ lệ misconception của cả lớp; cũng không dùng nó để đánh giá nhận diện lỗi biên dịch.

## 2. Nhập dữ liệu: ưu tiên bằng chứng có thể kiểm tra

- Giữ raw snapshot, commit, hash và đường dẫn file nguồn; không cần tải bộ APR/Docker để đọc dữ liệu. Không chạy source sinh viên chỉ để trích AST hoặc nhập comment log.
- Ghép test bằng input **và** expected output, không mặc định thứ tự comment là thứ tự file test. Nếu nhiều test có nội dung giống nhau, phải phát hiện ambiguity, giữ audit và áp dụng quy tắc nhất quán; không lựa chọn ngẫu nhiên.
- Verdict lịch sử là một quan sát đã lưu, không phải phép chạy lại đã xác minh. Thiếu log là `not_run`; không tạo outcome từ điểm tổng. Không suy runtime error từ chuỗi output rỗng.
- Giữ nguyên verdict fail; nếu output chỉ khác whitespace, gắn cờ ứng viên lỗi định dạng trong audit riêng. Không tự đổi thành pass khi chưa có chính sách oracle chính thức. [Mẫu 270010](https://raw.githubusercontent.com/jyi/ITSP/master/dataset/Lab-3/2810/270010_buggy.c) minh họa việc cần kiểm tra output cụ thể thay vì chỉ nhìn nhãn fail.
- Không dùng code `correct`, diff sai–đúng hoặc tên lỗi tự gán làm feature đầu vào; những dữ liệu này dành cho người duyệt sau phân cụm. Correct ở đây nghĩa là pass test được cung cấp, không bảo đảm đúng mọi input.
- Khi ID sinh viên không có, đánh dấu rõ grouping là assignment/source. Không gọi heldout này là student-disjoint, và không đưa unknown ID chung vào mọi dòng khiến toàn bộ dataset thành một nhóm. Muốn đánh giá người học mới cần mapping chính thức.

## 3. OAV và cấu trúc C

Object là lần nộp. Thuộc tính gồm trạng thái từng test và chỉ báo cú pháp được định nghĩa rõ. Metadata, tên file, ID, comment verdict, code sửa đúng và nhãn chuyên gia không tham gia khoảng cách. Mỗi cohort có cùng bài/ngôn ngữ/test suite; không gom chung các bài chỉ vì cùng chủ đề vòng lặp.

Đã chọn [tree-sitter C](https://github.com/tree-sitter/tree-sitter-c) và [Python bindings](https://github.com/tree-sitter/py-tree-sitter) để đọc cây cú pháp mà không chạy compiler hoặc code sinh viên. Cây này là CST; chỉ trích sự hiện diện của 16 cấu trúc cú pháp, giữ tiền tố `ast:c_` để tương thích API feature. Không mở rộng macro, có thể thấy code ở cả hai nhánh `#if`; điều kiện tiền xử lý không được tính là so sánh runtime. Parse failure là bất tương thích/không chắc chắn của parser, không tự chứng minh lỗi biên dịch. Outcomes-only và combined cùng loại parse error nên kết quả là ablation trên cùng tập parse được, cần báo coverage.

Chỉ báo có vòng lặp, `<=`, mảng, con trỏ hay dereference là **bằng chứng cú pháp**, không tự chứng minh lỗi biên hoặc hiểu sai truyền tham số. C truyền đối số theo giá trị; địa chỉ cũng được truyền theo giá trị, và ghi qua con trỏ mới có thể thay đổi đối tượng của bên gọi. Tránh mô tả sai rằng C tự có cơ chế truyền tham chiếu như C++.

Ngân sách trọng số theo block giúp nhiều test không lấn át cấu trúc. Bắt đầu outcomes-only rồi combined; nếu cấu trúc không thêm giá trị qua đọc exemplar/ablation thì giữ baseline đơn giản. Parse failure không được mã hóa thành mọi thuộc tính bằng 0. Cũng cần báo coverage: loại mẫu khó parse có thể làm thí nghiệm chỉ còn những bài dễ.

## 4. Thuật toán và quy tắc giải thích

Khoảng cách categorical dùng `sum(w_j * [x_j != y_j]) / sum(w_j)`. Average-linkage nhận được ma trận khoảng cách tiền tính; Ward yêu cầu hình học Euclidean. [API AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html)

K-means tối ưu khoảng cách bình phương tới centroid, không phải K-means với Hamming tùy ý. Với one-hot đầy đủ, scale block bằng `sqrt(w_j/2)` làm một mismatch đóng góp `w_j` vào bình phương khoảng cách giữa hai điểm. Đây là kiểm tra toán học của dự án; không đồng nhất objective centroid với linkage/Hamming. [API KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)

Nhóm exact test signatures là baseline cần giữ. Cây quyết định nông học `features -> cluster_id` cung cấp luật surrogate dễ đọc; precision của luật chỉ là fidelity với nhãn cụm. ILA là hướng quy nạp luật có lớp, không nên được gọi là clustering phi giám sát. Tài liệu tổng quát và nguồn ILA đã lưu trong `method_review.md`; trang nhà xuất bản ILA bị 403 ở lần kiểm tra này, không tuyên bố đã đọc lại toàn văn.

Code hiện tại dùng nearest training medoid cho holdout, kể cả K-means: đó là chính sách gán bổ sung, không phải `KMeans.predict`. Cần báo tie/margin và nhận diện mẫu xa cụm. Chưa có ngưỡng được hiệu chỉnh thì báo khoảng cách, không đưa xác suất chẩn đoán.

## 5. Đánh giá đúng câu hỏi nghiên cứu

1. Cố định grouping, seed, ngân sách chọn k và trọng số; fit trên train. Khi không có ID người học thật, ghi giới hạn assignment/source split cạnh chỉ số.
2. Báo số mẫu trước/sau routing, số test, số signatures, parse coverage, cụm nhỏ và medoid. Silhouette dùng metric tương ứng; trường hợp không đủ cụm trả N/A. [Hướng dẫn scikit-learn](https://scikit-learn.org/stable/modules/clustering.html)
3. So sánh outcomes-only và combined cùng split. ARI so với exact signatures đo mức giống baseline, **không đo accuracy misconception**. ARI không phụ thuộc việc đánh số nhãn cụm. [API adjusted_rand_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html)
4. Đọc tối thiểu một medoid và một phản ví dụ/mẫu biên mỗi cụm; đối chiếu đề, test, code và phiên bản sửa. Ghi giả thuyết, bằng chứng, uncertainty và khả năng nhiều lỗi cùng tồn tại.
5. Tên misconception chỉ được xác nhận sau annotation chuyên gia. Tập nhãn phải ở file riêng, có “không đủ bằng chứng”, “nhiều lỗi” và “sơ suất”. Muốn tuyên bố giá trị giảng dạy phải đo khả năng giảng viên dùng báo cáo, không suy từ silhouette.

## 6. Cập nhật nghiên cứu đến mốc yêu cầu

[McMining, EACL tháng 3/2026](https://aclanthology.org/2026.eacl-short.10/) nghiên cứu khai phá misconception và các cách dùng LLM. Đây là nguồn sát bài toán để tham khảo codebook/evaluation; không là bằng chứng rằng phải thêm LLM cho ITSP hoặc rằng luật surrogate đã nhận diện đúng nhận thức. Với nguồn lực hạn chế, ưu tiên chất lượng mapping test, AST kiểm chứng được, baseline và annotation nhỏ. Chỉ thử embedding/LLM sau khi chỉ rõ baseline thất bại ở đâu và đo được cải thiện trên nhãn độc lập.

Các trang tài liệu `stable` có thể thay đổi sau ngày đọc; phiên bản môi trường và lockfile trong dự án mới quyết định API chạy thực tế. Không nâng thư viện chỉ để khớp số phiên bản trên website.

## 7. Thay bằng dữ liệu giảng viên

Giữ adapter ITSP ở biên hệ thống, chuyển về manifest/JSONL chung; domain, feature-space, clustering và rule induction không phụ thuộc đường dẫn Lab của ITSP. Khi có data chính thức: xác nhận ngôn ngữ, ID, suite, oracle, runtime và lịch sử trước; viết adapter nguồn mới, giữ raw riêng và chạy lại validation. Cần extractor mới khi đổi ngôn ngữ, nhưng không cần viết lại toàn bộ pipeline. Không gộp raw hai nguồn vào một cohort trước khi xác minh tương thích.

Các ranh giới nhỏ theo module là đủ cho prototype. Không cần service, plugin registry, vector database, hệ thống triển khai phân tán hoặc APR để hoàn thành thí nghiệm này.
