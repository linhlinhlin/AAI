# Phản biện hồ sơ Misconceptions Clustering — ITSP

Ngày thực hiện: 20/09/2026. Mốc tài liệu nghiên cứu: 19/09/2026. Đây là phản biện kỹ thuật/nghiên cứu do trợ lý thực hiện, không phải human annotation, không xác nhận codebook và không bổ sung ground truth.

**Kết luận: tiếp tục đề tài, nhưng cần sửa lớn thiết kế kiểm chứng trước khi tuyên bố đã phát hiện/gom cụm quan niệm sai lầm.** Hai file làm tốt nhiệm vụ lưu và trình bày bằng chứng. Điểm nghẽn nằm ở khả năng suy từ biểu hiện lỗi sang cơ chế lỗi và từ cơ chế lỗi sang nhận thức người học. Thêm thuật toán phức tạp chưa giải quyết được điểm nghẽn đó.

## 1. Phạm vi và những gì đã kiểm chứng

Đường dẫn người dùng ghi không tồn tại nguyên dạng. Hai tài liệu thực tế được review là [reviewer_packet.md](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md) và [reviewer_sources.md](E:/AAI/misconceptions-prototype/results/itsp/reviewer_sources.md). Skill [karpathy-guidelines](C:/Users/Admin/.codex/skills/karpathy-guidelines/SKILL.md) đã có sẵn; nội dung phù hợp bản GitHub được yêu cầu, không cần cài lại.

Đã đọc hướng dẫn, codebook và phân tích mã sai/bản sửa của cả 17 mẫu; kiểm tra máy toàn bộ bằng chứng nhúng của 59 submissions; đối chiếu extractor, clustering, scorer và protocol liên quan. Không chạy mã C, không fit lại clustering, không dùng các file AI annotation làm nguồn kết luận. Không thực hiện kiểm toán toàn bộ repository.

| Kiểm tra thực hiện trong lượt này | Kết quả |
|---|---:|
| Mục nguồn có SHA-256 đối chiếu lại | 255/255 khớp |
| SHA-256 packet so với manifest | Khớp |
| Phiếu chính / thành viên ngữ cảnh / ID duy nhất | 17 / 42 / 59 |
| Khối mã C nhúng đối chiếu raw, chỉ bỏ xuống dòng cuối | 135/135 khớp |
| Test của 17 phiếu / toàn bộ packet so với raw parser, canonical suite và JSONL | 113 / 395 khớp |
| Bộ OAV, weight, assignment, danh sách thành viên của 17 × 3 arm | 51/51 khớp |
| Liên kết nội bộ có đích | 551/551 |
| Phiếu reviewer còn trống | 17/17 |
| Audit sẵn có của gói chấm mù, gọi hàm không ghi lại report | Đạt; 72 file |
| CRC gói vòng 1 / vòng 2 | Đạt cả hai |

Kết quả máy lưu ở [reviewer_audit_2026-09-20.json](E:/AAI/misconceptions-prototype/results/itsp/reviewer_audit_2026-09-20.json). Các kiểm tra toàn vẹn chứng minh nội dung được xuất đúng từ nguồn hiện có; không chứng minh oracle đúng về sư phạm, log tái lập trên máy khác hoặc sinh viên có misconception.

Các điểm nên giữ: bảo toàn log lịch sử; phân biệt null/pending/Unclear; không suy student ID từ tên file; tách AI khỏi human labels; không coi paired correct là chứng cứ đã hiểu; codebook chưa duyệt được ghi đúng trạng thái; chia từng bài/test suite; không dùng nhãn người chấm để tạo feature. Đây là nền tảng tốt cho một nghiên cứu có thể kiểm tra lại.

## 2. Các vấn đề theo mức ưu tiên

### P1 — Đơn vị đang đo là bài làm và giả thuyết lỗi, chưa phải niềm tin của sinh viên

Điểm neo: [packet dòng 30](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:30), [dòng 75](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:75), [dòng 83](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:83).

Quy tắc Yes đã yêu cầu giải thích cạnh tranh, nhưng một chương trình vẫn có thể được viết bởi người hiểu đúng và sơ suất, hoặc bởi người hiểu sai. Hai chuyên gia đồng ý về lỗi không tự xác nhận trạng thái nhận thức. Không có ID sinh viên và lời giải thích của người học nên ITSP không giải quyết được phân biệt này một cách chắc chắn.

**Sửa tối thiểu:** định nghĩa biến đo là “bằng chứng phù hợp với một quan niệm sai lầm tiềm năng”. Lưu riêng mô tả cơ chế lỗi quan sát được với giả thuyết hiểu sai. Khi có dữ liệu lớp, bổ sung một câu hỏi dự đoán output/giải thích hoặc một bài chuyển giao cho những ca mơ hồ. Những lần nộp và lỗi tương tự phải liên kết được bằng ID ẩn danh trước khi nói về tính lặp lại ở một người học. McMining cũng coi kết quả suy từ mã là misconception tiềm năng, và khai thác nhiều bài của một sinh viên; đó là định hướng phù hợp, không phải lý do bỏ qua kiểm chứng nhận thức. [McMining, EACL 2026](https://aclanthology.org/2026.eacl-short.10/).

### P1 — Biểu diễn hiện tại không phân biệt được một số cơ chế quan trọng

Điểm neo: [giải thích OAV](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:77), [extractor C](E:/AAI/misconceptions-prototype/src/misconceptions/features.py:48).

16 chỉ báo là sự hiện diện cú pháp; sau lọc thuộc tính hằng theo train, seed42 chỉ còn 4/3/6 chỉ báo cấu trúc cho 2812/2825/2833. Chúng không mô tả liên kết `else`, số đối số `printf`, quan hệ biến vòng lặp–hướng cập nhật, hoặc phân biệt điều kiện duyệt và điều kiện hợp lệ.

Các phản ví dụ ngay trong packet:

- 271173 viết `Cicle`; 271188 in `on` thay vì `outside`. Cả hai fail tests 1, 2, 7 và có cùng OAV kết hợp hiện tại. Khoảng cách không thể phân biệt hai bài khi biểu diễn đầu vào giống nhau.
- 271912 thiếu chữ `s` trong chuỗi; 271920 dùng `i++` trong vòng đếm lùi. Cả hai fail toàn bộ suite và cùng cụm A/C=0, dù cơ chế rất khác.
- 271154 dùng `r` thay `r*r`; 271203 gắn `else` vào `if` thứ hai. Cùng cụm A/C=0 của bài 2825, không có nghĩa cùng nguyên nhân.

Tính lại ARI từ assignments đã lưu, trên train và holdout gộp của từng bài, cho A so với C ở seed42 đều bằng 1: 19/19, 22/22 và 18/18 bài có cùng phân hoạch. Đây là xác nhận độc lập một kết quả đã nêu đúng trong `abc_summary.md`, không phải phát hiện lỗi báo cáo. Nó chỉ cho thấy cấu trúc hiện tại chưa đổi phân hoạch tại cấu hình này; không chứng minh mọi đặc trưng cấu trúc đều vô ích.

**Sửa tối thiểu:** giữ baseline; thử ít đặc trưng quan hệ có vị trí nguồn, chọn từ giả thuyết chung: assignment trong điều kiện; cấu trúc liên kết `if/else`; quan hệ biến điều khiển–phép so sánh–hướng cập nhật; arity của lời gọi định dạng literal. Cờ phát hiện vẫn chỉ là bằng chứng, không gắn tên misconception tự động. Đặc trưng thiết kế sau khi xem 17 ca này phải đánh giá trên bài/mẫu mới, vì 17 ca đã trở thành tập phát triển. Chỉ xây CFG/dataflow đầy đủ nếu quy tắc nhỏ không đủ.

### P1 — Packet này phù hợp vòng xem cụm; không thay được vòng chấm mù

Điểm neo: [packet dòng 71–81](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:71).

File đã cảnh báo đúng rằng reviewer thấy cụm. Rủi ro thực tế là gửi nhầm tài liệu, hoặc chuyển kết quả Markdown sang JSON rồi đặt `independent_blind_review=true`. Không thể “đọc phần code trước” để khôi phục điều kiện mù khi cluster đã nằm trong cùng file.

**Sửa tối thiểu:** thêm nhãn nổi bật “VÒNG 2 — CÓ HIỂN THỊ CỤM” ở đầu file, kèm đường dẫn gói vòng 1. Gói chấm mù đã tồn tại và audit đạt; không cần xây lại. Nếu reviewer đã xem báo cáo này hoặc packet có cụm, không coi lượt chấm sau trên cùng mẫu là mù; dùng người chưa tiếp xúc hoặc mẫu mới. Lưu phạm vi bằng chứng từng vòng và snapshot bất biến. Đây là vấn đề điều phối, không phải thiếu công cụ.

### P1 — 17 mẫu chọn theo cụm C không đủ để so sánh chất lượng toàn cohort

Điểm neo: [packet dòng 75](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:75), [assignment có selection_reason](E:/AAI/misconceptions-prototype/results/itsp/abc_review_assignments.json:1), [scorer purity](E:/AAI/misconceptions-prototype/src/misconceptions/expert_validation.py:177).

Medoid/mẫu xa cụm hữu ích để tìm cơ chế thất bại, nhưng đây không phải mẫu xác suất. Scorer đã công bố đúng rằng purity chỉ tính trên adjudicated Yes có type, trong tập chọn. Tuy nhiên chỉ số đó có thể cao khi nhiều No/Unclear bị loại; purity cũng không phạt việc chia nhỏ một loại thành nhiều cụm. Không nên dùng làm endpoint chính để tuyên bố C tốt hơn A hoặc “độ chính xác nhận diện misconception”.

**Sửa tối thiểu:** dùng 17 mẫu cho phân tích định tính. Với 59 bài ngắn, cân nhắc hai người chấm toàn bộ nếu ngân sách cho phép; nếu không, lấy một mẫu đánh giá ngẫu nhiên/phân tầng theo bài đã khóa, dùng chung cho tất cả arm. Báo số Yes/No/Unclear, coverage, cụm nhỏ, số cơ chế bị gộp/split. Pairwise precision/recall trên nhãn cơ chế đủ rõ giúp nhìn cả gộp sai và tách sai; báo riêng độ bao phủ các cặp có nhãn. ARI chỉ dùng khi nhãn thật sự tạo một phân hoạch phù hợp. Không xem nhiều cặp dùng chung bài hay ba seed là quan sát độc lập. Chưa có ID sinh viên thì mọi kết quả generalization chỉ ở mức submission/source.

### P2 — “Cùng nguyên nhân” và type khái niệm đang ở hai độ hạt khác nhau

Điểm neo: [codebook dòng 38–55](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:38), [same_cluster_cause dòng 80](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:80).

Codebook đã nói rõ cùng type không đồng nghĩa cùng nguyên nhân, nhưng phép tính purity theo type không kiểm tra được mục tiêu “cùng bản chất lỗi logic”. Hai reviewer xem số thành viên khác nhau cũng có thể cùng ghi Yes mà đánh giá hai phạm vi khác nhau. Các ranh giới `C_IO_CONTRACT`/`NUMERIC_REPRESENTATION` và `MATH_MODEL`/`ENUMERATION_IDENTITY` cần ví dụ hiệu chỉnh ngoài tập đánh giá.

**Sửa tối thiểu:** giữ taxonomy cấp cao, thêm mô tả cơ chế ngắn và cấu trúc `members_reviewed`, `n_reviewed/n_cluster`; thống nhất cùng phạm vi khi tính agreement vòng 2. Với mẫu đa lỗi, lưu đủ cơ chế trong evidence trước khi chọn primary. Không ép No/Unclear thành một “loại lỗi” đồng nhất để tính purity. Chốt rõ đề tài bao gồm sai mô hình toán học/hiểu đề hay chỉ ngữ nghĩa ngôn ngữ; hiện taxonomy bao gồm cả hai.

### P2 — Provenance tốt, nhưng cách tái xuất và bàn giao cần rõ hơn

Điểm neo: [sources dòng 9](E:/AAI/misconceptions-prototype/results/itsp/reviewer_sources.md:9), [dòng 302](E:/AAI/misconceptions-prototype/results/itsp/reviewer_sources.md:302).

`reviewer_sources.md` là manifest nguồn, không phải related work; không cần biến bảng hash thành thư mục bài báo. Điểm thiếu là file này chưa chỉ ra entry point/lệnh tái xuất chính hai file Markdown, phiên bản exporter và môi trường. Hash giúp kiểm tra một snapshot, chưa đủ tái tạo snapshot đó. Các link `E:/AAI/...` dùng được trên máy này nhưng không giải quyết truy cập trên máy reviewer khác.

**Sửa tối thiểu:** bổ sung một khối provenance nhỏ: upstream URL/commit, suite versions, assignment hash, exporter entry point/version, command, environment lock, normalization policy, generated_at. Giữ link tuyệt đối cho bản workspace; bản gửi ngoài dùng gói offline đã có. Không cần cơ sở dữ liệu hay dịch vụ quản lý provenance.

## 3. Đọc từng mẫu: cơ chế thấy được và điều còn chưa biết

Bảng này là phân tích nghiên cứu, không phải phiếu Yes/No/Unclear của chuyên gia. Không đưa nó vào packet vòng 1. “Giả thuyết” dưới đây không xác nhận người học thực sự tin điều đó.

| Mẫu / ID / vị trí packet | Cơ chế thấy từ code và log | Diễn giải cần thận trọng |
|---|---|---|
| [01 — 270276](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:86) | `printf` nhánh dương thiếu đối số cho `%.4f`; bản sửa thêm `a`. | Lỗi hợp đồng lời gọi rõ; một nhánh sai vẫn có thể là sơ suất. Không giải thích output 0 như hành vi C bảo đảm. |
| [02 — 270277](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:470) | Nhánh zero in thêm giá trị `%f`. | Sai output contract, không phải bằng chứng về phân loại dấu. Bản correct có khoảng trắng đầu nhưng được ACCEPTED: không suy comparator lịch sử là so sánh byte tuyệt đối. |
| [03 — 270283](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:850) | `%.4f` và `%n` nằm trong chuỗi nhưng không có đối số tương ứng. | Có thể nhầm cách truyền biến vào format string; `%n` là conversion ghi qua con trỏ, không phải cách nội suy biến n. Không suy crash từ output rỗng. |
| [04 — 270285](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:1244) | Thêm dấu chấm theo ví dụ đề, oracle lại không có. | Mâu thuẫn đề/oracle là giải thích trực tiếp. Không quy thành thiếu hiểu biết của sinh viên. |
| [05 — 270293](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:1642) | Cùng vấn đề dấu chấm như mẫu 04. | Hai bài cùng lỗi output không chứng minh cùng một người, cũng không chứng minh một niềm tin sai. |
| [06 — 271154](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:2046) | Khoảng cách bình phương trừ r thay vì r². | Giả thuyết sai mô hình bán kính/khoảng cách; cũng có thể bỏ sót phép nhân. Cần hỏi giải thích công thức. |
| [07 — 271163](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:2429) | Thiếu dấu chấm ở output; bản sửa chỉ thêm dấu chấm. | Không có bằng chứng trong ca này để gán hiểu sai công thức khoảng cách. |
| [08 — 271173](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:2846) | `Cicle` thay `Circle` ở nhánh outside. | Lỗi chính tả trực tiếp giải thích các fail; hữu ích làm đối chứng âm với suy luận misconception. |
| [09 — 271188](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:3231) | Nhánh l>0 in `on`; biểu thức hình học đúng. | Có thể copy-paste chuỗi; không đủ kết luận hiểu sai hình học/nhánh. Cùng test signature mẫu 08, khác cơ chế. |
| [10 — 271203](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:3612) | `else` gắn `if(n>0)`, nên n<0 in cả inside và on. | Ứng viên hiểu sai tính loại trừ/liên kết nhánh; cần câu hỏi dự đoán luồng, không chỉ nhìn bản sửa. |
| [11 — 271213](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:4010) | `scanf` nhận x,y,x1,y1,r trong khi đề yêu cầu x,y,r,x1,y1. | Sai thứ tự dữ liệu, chưa đủ bằng chứng hiểu sai `scanf`. Thiếu `math.h` là vấn đề khai báo/phụ thuộc môi trường riêng; không suy compiler hiện đại sẽ chấp nhận như log cũ. |
| [12 — 271912](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:4421) | In `triangle` thay `triangles`. | Vòng duyệt đã dùng x≥y≥z; fail toàn suite không phản ánh sai đếm. |
| [13 — 271916](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:4810) | Duyệt mọi hoán vị, rồi hiệu chỉnh bằng `((count-n)/n)+n`. | Ứng viên sai đồng nhất đối tượng; cần giải thích tam giác thường/cân/đều có 6/3/1 hoán vị, không một hệ số chung. |
| [14 — 271920](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:5200) | `i=n; i>=1; i++` tăng thay vì giảm. | Với n dương, cập nhật đi xa điều kiện dừng và có nguy cơ tràn số nguyên có dấu. Một ký tự có thể là typo; log WRONG_ANSWER không xác nhận timeout. |
| [15 — 271965](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:5597) | Cả a,b,c đều duyệt 1..N, đếm các hoán vị. | Ứng viên nhầm tam giác với bộ ba có thứ tự; hiểu nhầm yêu cầu đề cũng là giả thuyết cạnh tranh. |
| [16 — 271975](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:5996) | Đặt `a<c+b` vào điều kiện while, dừng trước những c lớn hơn có thể hợp lệ. | Ứng viên nhầm điều kiện lọc với điều kiện tiếp tục duyệt. Truy vết a=3,b=2,c=1 cho thấy thoát trước c=2 dù (3,2,2) hợp lệ. |
| [17 — 271986](E:/AAI/misconceptions-prototype/results/itsp/reviewer_packet.md:6398) | Dùng assignment `x=0`, `y=0`, `z=0` trong biểu thức logic kiểm tra góc. | Có cả khả năng nhầm assignment/equality và mô hình điều kiện rườm rà. Bản sửa xóa cả if nên không cô lập được một cơ chế nhận thức duy nhất. |

Đối với mẫu 01/03, quy tắc thiếu đối số và conversion `%n` đối chiếu [WG14 N1570, §7.21.6.1 và §7.21.6.3](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1570.pdf). Log là hiện tượng đã quan sát; undefined behavior không cho phép suy một output tất định.

## 4. Đặt đề tài trong nghiên cứu đến 19/09/2026

Đây là rà soát có mục tiêu theo nguồn sơ cấp, không phải systematic review và không chứng minh một phương pháp dẫn đầu tuyệt đối. Ngày truy cập là 20/09/2026; các công trình chọn dưới đây được công bố trước hoặc tại cutoff. Trang tài liệu phần mềm/kho sống có thể tiếp tục thay đổi.

| Công trình / nguồn | Bài học áp dụng và giới hạn |
|---|---|
| [McMining — Al-Hossami & Bunescu, EACL 03/2026](https://aclanthology.org/2026.eacl-short.10/) và [PDF](https://aclanthology.org/2026.eacl-short.10.pdf) | Sát bài toán: mô tả niềm tin sai từ một/nhiều bài; benchmark có chèn misconception bằng mô hình. Học cách định nghĩa task, dùng đối chứng âm và nhiều bài/người; không dùng dữ liệu sinh làm xác nhận duy nhất cho lớp thật. |
| [AI-Augmented Instruction: Real-Time Misconception Detection — SIGCSE TS 02/2026, poster](https://sigcse2026.sigcse.org/details/sigcse-ts-2026-posters/160/AI-Augmented-Instruction-Real-Time-Misconception-Detection) | Đã có hướng LLM + sentence encoders + KMeans + dashboard cấp lớp từ nhóm Georgia Tech. Abstract nói pilot đang thực hiện; không coi là bằng chứng hiệu quả giảng dạy hoàn tất. Ý tưởng dashboard/gom lỗi tự thân chưa đủ mới. |
| [Pattern-based Knowledge Component Extraction — Hoq và cộng sự, EDM 2026](https://educationaldatamining.org/edm2026/proceedings/2026.EDM.full-papers.251/index.html) | SANN → subtree → VAE → clustering, có expert evaluation và student modeling. Gợi ý chuyển từ presence sang quan hệ/subtree có ý nghĩa. KC là đơn vị kiến thức, không đồng nhất misconception; chưa cần triển khai mô hình này với 59 mẫu. |
| [Identifying and Correcting Programming Language Behavior Misconceptions — Lu & Krishnamurthi, OOPSLA 2024](https://cs.brown.edu/people/sk/Publications/Papers/Published/lk-smol-tutor/paper.pdf) | Khai thác dự đoán hành vi và lời giải thích, diễn giải hiểu sai bằng mô hình ngữ nghĩa. Gợi ý một câu hỏi chẩn đoán ngắn để kiểm tra giả thuyết rút từ code. |
| [Conceptual Mutation Testing for Student Programming Misconceptions](https://arxiv.org/abs/2401.00021) | Gom các ví dụ/test do sinh viên viết sai với reference rồi tạo conceptual mutants. Dữ liệu khác bài code trượt test của đề tài; học cách tạo ví dụ phân biệt giả thuyết, không hoán đổi hai task. |
| [InvAASTCluster — công trình và mã nguồn tác giả](https://github.com/pmorvalho/InvAASTCluster) | Kết hợp invariants và AAST trên bài lập trình nhập môn, có ITSP/C-Pack. Đối chứng gần về program clustering; đồng nhất hành vi chương trình không đồng nghĩa đồng nhất hiểu sai. Dependency/runtime lớn hơn baseline hiện tại. |
| [ProgMiscon](https://progmiscon.org/) | Hỗ trợ diễn đạt taxonomy theo ngôn ngữ/khái niệm; không phải bộ nhãn chuẩn của 59 bài ITSP. |

Về dataset: giữ [ITSP](https://github.com/jyi/ITSP) làm pilot có code, đề, log và cặp sửa; provenance hiện có phù hợp vai trò này. Nếu cần kiểm chứng có ID người học xuyên bài, [C-Pack-IPAs](https://github.com/pmorvalho/C-Pack-IPAs) có 25 bài và ID ẩn danh nhất quán, thích hợp mở rộng C; phải chuẩn bị outcomes khi nguồn không có log đúng schema. [CodeInsight v1, 01/09/2026](https://arxiv.org/html/2609.00940v1) có hơn 3 triệu bài C++, ID, thời gian và outcomes từng test nhưng cần xin quyền theo departmental license; đây là preprint, chưa phải tài nguyên có thể mặc định tải ngay. CodeWorkout dùng trong bài EDM có lịch sử Java và điểm correctness; không suy điểm tổng thành vector test-level. Không đổi dataset chỉ vì quy mô lớn.

## 5. Phương án tối giản nên theo

**Câu hỏi nghiên cứu đề nghị:** “Trong cùng bài lập trình, đặc trưng lỗi có thể kiểm tra từ test và cấu trúc mã có giúp giảng viên gom các cơ chế lỗi đáng dạy lại chính xác hơn và nhanh hơn baseline chữ ký test không?” Sau đó mới kiểm tra những cơ chế nào phản ánh hiểu sai bằng chứng bổ sung từ người học.

Pipeline giữ dạng: nhập bằng chứng → kiểm tra schema/suite → trích OAV → gom cụm theo bài → xuất exemplar/phản ví dụ → người duyệt → tổng hợp phản hồi. Chỉ số và nhãn chuyên gia ở bước đánh giá riêng.

1. **Baseline bắt buộc:** nhóm exact test signatures. Nó rẻ, dễ giải thích và bộc lộ trực tiếp giới hạn test suite.
2. **Phương pháp chính:** weighted Hamming trên thuộc tính categorical, average-linkage như đã có. Dùng một ngân sách nhỏ k/trọng số được chốt trên tập phát triển. Không chọn cấu hình theo purity của tập cuối.
3. **Cải tiến nhỏ:** thêm vài đặc trưng quan hệ, kiểm tra tương đương cú pháp như `i++`/`i=i+1`; không chỉ thêm thật nhiều cờ. Lưu evidence span và trường unknown khi quy tắc không áp dụng.
4. **Luật giải thích:** cây nông hiện có là đủ cho bước đầu. `IF evidence THEN cluster` đo fidelity của phân hoạch, chưa là luật về nhận thức. Nếu chuyển sang nhãn chuyên gia thì phải có tập đánh giá riêng.
5. **Macro-feedback:** hiển thị số bài và, khi có ID, số sinh viên duy nhất; ví dụ đại diện, cơ chế có bằng chứng, uncertainty, câu hỏi chẩn đoán và đề xuất giảng lại. Không hiển thị “x% sinh viên hiểu sai” từ x% submissions.

Hai chỉnh sửa cho đề cương ban đầu: [ILA gốc](https://www.sciencedirect.com/science/article/abs/pii/S0957417497000894) là quy nạp luật phân loại từ ví dụ có lớp, không phải clustering phi giám sát. [KMeans](https://scikit-learn.org/1.9/modules/generated/sklearn.cluster.KMeans.html) dùng centroid và objective bình phương Euclid; không thay metric sang Hamming rồi giữ nguyên cập nhật trung bình. Average-linkage với khoảng cách tiền tính phù hợp hơn categorical OAV. C truyền tham số theo giá trị, kể cả giá trị con trỏ; ví dụ hoán vị phải mô tả “thay đổi đối tượng bên gọi thông qua con trỏ”, tránh dạy sai thành cơ chế tham chiếu của C++.

## 6. Clean Code và Clean Architecture trong phạm vi đã xem

`domain.py` độc lập dataset; adapters chịu trách nhiệm I/O; features trích bằng chứng; pipeline xử lý phân hoạch và surrogate; expert_validation xử lý nhãn/metrics. Hướng phụ thuộc nhìn chung hợp lý cho prototype. Giữ cấu trúc module này, chưa cần service, repository interface, DI container hoặc framework mới.

Ba cải tiến thực dụng khi triển khai vòng kế tiếp:

- `route_submission` gọi extractor rồi fit/transform lại trích AST. Tính OAV một lần theo submission trong một lần chạy sẽ giảm xử lý lặp và giúp provenance nhất quán; chỉ ưu tiên nếu profiling cho thấy đáng kể.
- Scorer phải giữ tách biệt agreement trước adjudication, purity có điều kiện và agreement sau khi thấy cụm. Thêm cơ chế/phạm vi review như trên trước khi mở rộng metric.
- Tách logic xuất packet khỏi lệnh CLI, dùng allowlist rõ và validator đối chiếu output với source. Giữ lockfile/version khi tái lập. Không sửa các file evidence gốc để làm dữ liệu đẹp hơn.

Hamming hiện tích lũy từng feature, tránh tensor n×n×d. Một ma trận float64 300×300 khoảng 0,72 MB; CPU đủ cho phân tích một cohort vài trăm bài. Con số này chỉ là bộ nhớ ma trận, không phải benchmark tổng RAM/thời gian. Lớp 300 sinh viên có thể có hàng nghìn lần nộp; phải chốt đơn vị lấy mẫu/thời điểm thay vì đồng nhất 300 sinh viên với 300 rows.

Kiểm thử cần thiết nếu có sửa: fixture cho lỗi mapping test/oracle, unknown khác false, quan hệ AST và phản ví dụ, chống đưa correct/label vào feature, khóa vòng review, mẫu số metric và tính tái lập packet. Lượt review này không sửa implementation nên không chạy lại toàn bộ test suite; đã thực hiện các audit liên quan trực tiếp ở mục 1.

## 7. Thứ tự làm tiếp và tiêu chí dừng

| Ưu tiên | Việc cụ thể | Hoàn tất khi |
|---|---|---|
| 1 | Chốt định nghĩa misconception tiềm năng, phạm vi toán/ngôn ngữ, codebook với người phụ trách; đánh dấu rõ packet vòng 2 | Reviewer thống nhất protocol và provenance vòng chấm; chưa tự tạo nhãn |
| 2 | Hai reviewer chấm độc lập gói mù; giữ 17 ca làm phân tích khám phá | Có phiếu gốc, scope, agreement trước adjudication và trường hợp bất đồng |
| 3 | Tạo tập đánh giá mới/cố định, baseline exact/A/C; thử ít feature quan hệ | Báo cùng tập đánh giá, coverage, gộp/tách sai; không tuning trên nhãn cuối |
| 4 | Thử báo cáo với giảng viên trên các nhóm bài tương đương, hoán đổi thứ tự xem khi phù hợp | Đo thời gian nhận diện nhóm lỗi, chất lượng chủ đề cần giảng lại, số mở bài và mức bỏ sót; tránh học thuộc cùng ca giữa hai điều kiện |
| 5 | Bổ sung câu hỏi chẩn đoán/transfer trên dữ liệu lớp có ID | Có bằng chứng vượt ra ngoài một lần fail trước khi gọi là misconception đã xác nhận |

Giới hạn nguồn lực nên dùng làm nguyên tắc dừng: nếu feature mới không cải thiện chất lượng nhóm hoặc thời gian review trên mẫu chưa dùng thiết kế, giữ baseline đơn giản. Chỉ thêm LLM/embedding khi đã chỉ ra ca baseline thất bại và có nhãn độc lập để đánh giá phần cải thiện.

Tên bài phù hợp với bằng chứng hiện tại: **“Gom cụm mẫu lỗi lập trình từ kết quả kiểm thử và cấu trúc mã để hỗ trợ phản hồi cấp lớp: một nghiên cứu thăm dò trên ITSP.”** Khi có xác nhận độc lập và dữ liệu nhận thức, có thể nâng thành nghiên cứu về phát hiện quan niệm sai lầm tiềm năng. Đóng góp nên nhắm vào chất lượng bằng chứng, chi phí review và giá trị phản hồi; chưa nên tuyên bố thuật toán gom cụm ngữ nghĩa mới hoặc vượt SOTA.
