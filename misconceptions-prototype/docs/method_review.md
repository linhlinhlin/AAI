# Phản biện phương pháp và kế hoạch đánh giá

Phạm vi tra cứu: nguồn gốc thuật toán, tài liệu chính thức và nghiên cứu công bố không muộn hơn **19/09/2026**; đây là rà soát có mục tiêu, không phải systematic review đầy đủ. Đã đọc và áp dụng `karpathy-guidelines`: nêu giả định, chọn baseline nhỏ, tiêu chí kiểm chứng rõ. Nội dung dưới đây phân biệt thiết kế đề xuất và những đánh giá chỉ thực hiện được sau khi có dữ liệu thật; không tuyên bố đã chứng minh hiệu quả giáo dục.

## 1. Điều cần sửa trong phát biểu đề tài

**Bài làm sai không đồng nhất với quan niệm sai lầm.** Một lỗi có thể là sơ suất, đọc nhầm đề, thiếu kỹ năng kiểm thử hoặc hiểu sai khái niệm; hai chương trình cho cùng đầu ra sai có thể có nguyên nhân khác nhau. Vì vậy hệ thống trước hết tạo *cụm biểu hiện lỗi*, sau đó giảng viên kiểm chứng giả thuyết misconception. Nghiên cứu của [Kaczmarczyk và cộng sự, SIGCSE 2010](https://publish.illinois.edu/glherman/files/2016/03/2010-SIGCSE-Programming-Misconceptions.pdf) khai thác phỏng vấn và phân tích định tính, cho thấy cần bằng chứng về cách suy nghĩ ngoài kết quả chạy chương trình.

[ILA, Tolun & Abu-Soud, 1998](https://www.sciencedirect.com/science/article/abs/pii/S0957417497000894) sinh luật từ ví dụ có lớp. ILA không phải giải thuật gom cụm phi giám sát. Đặt ILA ở bước giải thích nhãn cụm hoặc học nhãn chuyên gia; nếu gọi “ILA cải tiến” phải định nghĩa cải tiến, objective, pseudocode và so sánh với bản gốc. Prototype nên dùng cây quyết định nông rồi trích đường đi thành luật vì dễ kiểm tra, sẵn trong scikit-learn.

Ví dụ hoán vị phải phụ thuộc ngôn ngữ: C truyền đối số theo giá trị kể cả đối số con trỏ; muốn đổi biến của bên gọi phải truyền địa chỉ và ghi qua con trỏ. C++ có kiểu tham chiếu. Python dùng object sharing; đổi binding cục bộ không đổi binding bên gọi, còn mutation đối tượng có thể quan sát được. Không dùng AST Python để kết luận “chưa hiểu truyền tham chiếu bằng con trỏ”.

## 2. OAV và đơn vị phân tích

Object là một lần nộp, không phải một sinh viên. Attributes gồm outcome từng test và dấu hiệu cấu trúc; values là categorical. Metadata như student_id, submission_id, điểm tổng, nhãn giảng viên, tên mutation không được đưa vào khoảng cách. Cohort phải cùng `problem_id`, ngôn ngữ và phiên bản test suite; compiler/runtime cũng cần ghi provenance. Cụm của bài A không mang cùng nghĩa với cụm có cùng số ID của bài B.

Outcome cần phân biệt `pass`, `wrong_answer`, `runtime_error`, `timeout`, `not_run`/thiếu, và compile failure ở cấp bài. Không biến test chưa chạy thành fail. Nếu nền tảng dừng ở lỗi đầu tiên, quan sát còn lại bị censoring, không phải bằng chứng rằng tất cả test đều sai. Tách bài không có outcome quan sát được, bài biên dịch thất bại và bài pass toàn bộ khỏi phân tích lỗi logic, hoặc báo riêng rõ ràng. Dữ liệu thiếu source không được biểu diễn như “không có vòng lặp”. Parse error không phải thuộc tính FALSE cho mọi cấu trúc.

AST flags như có `range`, toán tử `<`/`<=`, có return hoặc mutation chỉ là dấu hiệu; sự xuất hiện không xác định lỗi biên, luồng dữ liệu hay semantics. Ghi định nghĩa từng flag và AST node nguồn; đối chiếu vài chương trình thủ công. Không suy diễn con trỏ, aliasing hay semantics liên thủ tục từ regex. Dùng plugin extractor riêng nếu dữ liệu thật là C/C++/Java; adapter nguồn không nên chứa clustering.

Số test lớn có thể lấn át AST. Phân phối một ngân sách trọng số cho nhóm test, một ngân sách cho nhóm structure; trọng số mỗi nhóm cộng về ngân sách đó. Khi nhiều test gần trùng nhau, gom theo phân vùng input/khái niệm do người ra đề xác định hoặc giảm trọng số, tránh một dạng lỗi được đếm quá nhiều lần. Không dùng nhãn test để chỉnh trọng số sau khi xem kết quả trên tập kiểm thử giữ lại.

## 3. Kiểm tra toán học clustering

Với thuộc tính categorical và trọng số dương, dùng

`d(x,y) = sum_j w_j * 1[x_j != y_j] / sum_j w_j`.

Đây là weighted Hamming trên toàn bộ vector, không phải Euclidean trên mã số category. Cần kiểm thử `d(x,x)=0`, đối xứng, không âm, giới hạn [0,1], và ví dụ tay có trọng số không đều. Bỏ feature trọng số 0 khỏi exact signature; hai vector khác nhau chỉ ở feature 0 phải có khoảng cách 0.

Missing như một category giữ công thức đơn giản, nhưng có thể gom cụm theo cách chạy test thay vì lỗi. Phải thống kê missingness theo cụm. Nếu sau này bỏ qua chiều thiếu theo từng cặp, mẫu số phụ thuộc cặp và bất đẳng thức tam giác có thể không còn đúng; khi không có chiều chung phải abstain, không trả về 0. Phiên bản đầu nên yêu cầu độ phủ test đủ thay vì thêm metric phức tạp.

Average linkage với ma trận khoảng cách tiền tính phù hợp; Ward yêu cầu Euclidean và không nên ghép với Hamming tùy ý. Average linkage lấy trung bình khoảng cách mọi cặp giữa hai cụm theo [tài liệu chính thức](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html). So sánh exact test-outcome signatures là baseline cần thiết: thuật toán phức tạp phải giúp giảng viên hơn việc nhóm cùng kết quả test.

K-means tối thiểu hóa tổng bình phương khoảng cách tới centroid; không cung cấp lựa chọn Hamming tùy ý trong [KMeans API](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html). Với full one-hot cho feature j, hai category khác nhau có bình phương khoảng cách bằng 2. Do đó scale block bằng `sqrt(w_j/2)` để mismatch đóng góp `w_j`; scale `sqrt(w_j)` chỉ khác hệ số toàn cục 2 nếu mọi block giống nhau. Scale trực tiếp `w_j` tạo **bình phương trọng số**, sai nếu muốn đóng góp tuyến tính. Không drop category đầu, vì phá tính đối xứng giữa category.

Vocabulary phải fit trên train hoặc lấy từ schema outcome cố định đã biết trước. `handle_unknown='ignore'` biến category mới thành vector 0; khoảng cách tới category đã biết khi đó bằng nửa khoảng cách mismatch thông thường. Phải ghi tỷ lệ unknown và abstain/routing khi cần, hoặc dùng explicit unknown bucket thiết kế trước. Đây là hệ quả của [OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html), không phải chứng cứ mẫu mới giống một cụm.

Agglomerative không có predict tự nhiên. Gán mẫu mới theo medoid train đã đóng băng là **quy tắc triển khai bổ sung**, không tương đương refit hierarchical clustering hoặc average-linkage insertion. Báo riêng độ trung thành của medoid với nhãn train; ghi khoảng cách/margin cho mẫu mới và hiệu chỉnh ngưỡng từ validation. Không trình bày cluster ID là nhãn misconception có xác suất đã hiệu chuẩn.

## 4. Luật, nhiều lỗi và bằng chứng chuyên gia

Cây nông học `features -> cluster_id` là surrogate. Độ chính xác của nó đo fidelity với clustering, không đo đúng misconception. Luật cần support train/test, fidelity/precision, coverage, số điều kiện và các phản ví dụ; leaf purity trên train không phải confidence về nhận thức. Dùng câu “thuộc cụm biểu hiện C; giả thuyết cần duyệt” cho tới khi có nhãn chuyên gia. Threshold numeric trên feature one-hot nên chuyển thành điều kiện có/không rõ nghĩa.

[RIPPER, Cohen 1995](https://www.cs.cmu.edu/~wcohen/pubs-r.html) là lựa chọn rule induction để thử khi cần tập luật gọn có pruning; chưa cần thêm thư viện trong prototype. ILA/RIPPER học từ nhãn cụm vẫn chỉ giải thích nhãn giả. Sau khi có nhãn chuyên gia, có thể học luật trực tiếp từ nhãn ấy và đánh giá tách biệt.

Một lần nộp có thể chứa nhiều lỗi; hard clustering chỉ mô tả pattern tổng hợp. Cho phép annotator ghi danh sách misconception, “nhiều lỗi”, “không đủ bằng chứng”, “sơ suất”, confidence và đoạn code/test chứng minh. Khi có đủ nhãn, benchmark multi-label one-vs-rest/rules trước khi dùng mô hình latent phức tạp. Không ép các nhãn khác nhau thành một lớp chỉ để tính ARI.

## 5. Đánh giá không rò rỉ

1. Giữ cùng sinh viên và các bài có exact-source hash giống nhau trong cùng split bằng connected components. Quan hệ bắc cầu phải được giữ: A chung sinh viên với B, B chung source với C thì cả ba cùng nhóm. Nếu một component chiếm gần hết dữ liệu, báo không đủ split; không lén quay về random rows. Exact hash chưa ngăn near-duplicate sau đổi tên biến; bổ sung audit clone hoặc nhóm lớp/lần học khi có dữ liệu.
2. Fit vocabulary, feature selection, weights học từ dữ liệu, chọn k và surrogate chỉ từ train/validation. Chốt cấu hình trước khi mở heldout. Với thống kê mô tả toàn lớp có thể cluster toàn bộ dữ liệu, nhưng không gọi chỉ số trên dữ liệu đó là khả năng tổng quát hóa.
3. Không có gold labels: báo kích thước cụm, singleton, độ phủ, missingness, silhouette trên **đúng metric**, số mẫu và chất lượng exemplar. Silhouette chỉ định nghĩa khi `2 <= n_clusters <= n_samples-1`; trường hợp khác trả N/A, không thay bằng 0. [Hướng dẫn clustering scikit-learn](https://scikit-learn.org/stable/modules/clustering.html) phân biệt đánh giá nội tại và đối chiếu nhãn.
4. Độ ổn định: thay seed, bootstrap theo **student/component**, thay một phần test hoặc nhiễu outcome hợp lý; so sánh ARI trên cùng tập mẫu chung hoặc tập anchor được gán bằng quy tắc cố định. Không so trực tiếp cluster IDs giữa hai lần chạy. Ổn định cao vẫn có thể chỉ là nhóm theo phong cách code hoặc mức độ thiếu dữ liệu.
5. Có gold labels: hai người chấm độc lập mẫu ngẫu nhiên và mẫu medoid/biên/outlier, giữ blind với nhãn cụm khi chấm; giải quyết bất đồng sau chấm. Báo Cohen kappa từng nhãn nhị phân hoặc thước đo agreement phù hợp, prevalence và số unknown. ARI/NMI trên subset nhãn đơn rõ ràng; multi-label báo micro/macro F1, per-label precision/recall và Jaccard sau mapping chỉ học từ train. Purity một mình thiên vị nhiều cụm.
6. Đánh giá sư phạm: giảng viên đọc exemplar và luật, đo thời gian tổng hợp lỗi so với baseline signature, tỷ lệ cụm có thể dùng để giảng lại, tỷ lệ giải thích sai. Muốn kết luận học tốt hơn phải có thiết kế can thiệp/pre-post phù hợp; không suy ra từ silhouette.

Ablation tối thiểu: exact signatures; outcomes-only; AST-only; combined equal/block weights; K-means vs average-linkage; có/không test thiếu. Cố định split và ngân sách chọn tham số. Báo mean/spread qua vài group split khi số nhóm đủ; confidence interval bootstrap theo sinh viên, không theo submission độc lập. Synthetic fixture chỉ kiểm chứng đường đi kỹ thuật và các phản ví dụ đã thiết kế, không phải ước lượng chất lượng trên sinh viên thật.

## 6. Cập nhật nghiên cứu và ngân sách thực tế

[Conceptual Mutation Testing for Student Programming Misconceptions](https://arxiv.org/abs/2401.00021) (arXiv nộp 28/12/2023) hữu ích để thiết kế mutation theo sai cách hiểu đề và test phân biệt chúng. Mutation tạo ra dữ liệu có giả thuyết nguyên nhân, không chứng minh sinh viên có mental model đó. [Tilanterä & Korhonen, công bố 08/03/2026](https://research.aalto.fi/fi/publications/data-structures-and-algorithms-misconceptions-in-concept-inventor-2/) tổng hợp 92 misconceptions/difficulties về DSA trong concept inventories: nguồn xây codebook và câu hỏi kiểm chứng, không phải dataset submissions đã gán nhãn cho đề tài này.

Không có bằng chứng ở các nguồn trên rằng một mô hình embedding/LLM cụ thể là SOTA cho đúng dữ liệu chưa được cung cấp. Bước tiến thực tế là test có khả năng phân biệt lỗi, provenance rõ, nhãn chuyên gia và split đúng. Embedding code/LLM chỉ đáng thêm khi baseline thất bại đã được phân tích, có budget và thử nghiệm cho thấy cải thiện; kiểm soát model version, prompt và rò rỉ nhãn nếu dùng.

Ngân sách khởi đầu đề xuất, chưa phải benchmark đo thực tế: CPU, RAM 8–16 GB, 500–2.000 submissions/cohort, vài chục đến vài trăm features, 2–8 giá trị k, 3–5 group splits. Ma trận float64 n*n riêng nó tốn `8*n*n` bytes: 2.000 mẫu ≈32 MB, 10.000 ≈800 MB, chưa tính bản sao và linkage. Tránh broadcast tạm kích thước n*n*p; cộng khoảng cách theo feature hoặc theo block. Đặt giới hạn n và báo lỗi rõ trước cấp phát. Với dữ liệu lớn hơn, baseline signature vẫn hữu ích; cân nhắc MiniBatchKMeans hoặc lấy mẫu train/medoids có audit coverage. Giới hạn thread CPU và ghi wall time/peak memory trước khi nâng độ phức tạp.

## 7. Điều kiện chấp nhận prototype

- Chạy được offline trên fixture ghi rõ synthetic; không chạy source sinh viên không tin cậy trên host.
- Adapter mới đưa về cùng schema, validation từ chối outcome/language/cohort không hợp lệ; thay data không sửa clustering.
- Test hồi quy bắt được leakage bắc cầu, unknown category, all-missing, all-identical, một nhóm, số cụm ngoài miền, trọng số không hợp lệ, AST syntax error và luật support thấp.
- Artifact ghi dataset provenance, hash/config, seed, cohort, phiên bản dependencies và số mẫu bị loại.
- Báo cáo tách technical smoke test, clustering quality, surrogate fidelity và misconception validity; phần chưa có dữ liệu để đo phải ghi rõ.
