# ITSP prototype — công việc hoàn thành ngày 19/09/2026

Kiểm tra kỹ thuật mới nhất: **106 tests + 3 subtests pass; lint pass**. [Biên bản](../results/itsp/completion_verification.json). Đây là kiểm tra phần mềm, chưa phải human expert validation.

## Cập nhật hoàn thiện kỹ thuật — 20/09/2026

Đã [đối chiếu toàn bộ mục tiêu và phần còn thiếu](itsp_completion_review.md). Bổ sung intake hợp nhất phiếu chuyên gia vòng 1 có hash/provenance, không ghi đè snapshot hoặc tự adjudicate; scorer có coverage/nhãn đồng hạng theo cụm và công cụ xuất Markdown human-only. Từ chối assignment trùng/không hợp lệ. Baseline, feature và A/B/C giữ nguyên. Chưa có human annotation, expert purity/agreement vẫn null; bước cần chuyên gia và mẫu mới được ghi rõ, không tuyên bố đề tài đã hoàn tất.


**Bàn giao cập nhật 20/09/2026:** [Công việc hoàn thành, kết quả, giới hạn và bước tiếp theo](itsp_handoff_2026-09-20.md).

## Sau phản biện — 20/09/2026

Kiểm tra sau cập nhật: **93 tests + 3 subtests pass; lint pass**. Gói vòng 1 vượt audit đủ 72 file.

[Protocol kiểm chứng đã cập nhật](itsp_validation_revision.md): tách biểu hiện lỗi → cơ chế lỗi → giả thuyết misconception; giữ baseline và cây luật nông. ILA thuộc quy nạp luật, không gọi là clustering phi giám sát. Kiểm tra lại đủ 59 submissions: A=C ở seed42 (ARI=1 từng bài); vector combined của 271173/271188 trùng nhau. Chưa có bằng chứng cấu trúc hiện tại cải thiện phân hoạch; chưa phủ định mọi cấu trúc khác.

Đánh dấu toàn bộ 59 bài đã xuất hiện trong hồ sơ là dữ liệu phát triển/đã xem cho thí nghiệm feature mới; chưa chọn mẫu đánh giá độc lập mới hoặc triển khai feature quan hệ. Packet chính đã gắn nhãn “Vòng 2 — có hiển thị cụm”; gói vòng 1 giữ nguyên. Hai chuyên gia thật cần chốt codebook và chấm độc lập. Báo purity kèm coverage, No/Unclear và phân tích gộp/tách sai; chỉ số cặp cần nhãn cơ chế phù hợp, chưa tự tính trên AI. Expert validation tiếp tục chờ annotation, các metric vẫn null.


## Kiểm tra hồ sơ và hoàn thiện vòng 2

Đối chiếu lại gói vòng 1: đủ **17 mẫu, 51 file đề/source/bản sửa, 113 test records**, phiếu trống hợp lệ, ZIP khớp nội dung và link offline hoạt động. Codebook vẫn là dự thảo chờ chuyên gia xác nhận.

Bổ sung [gói vòng 2 offline](../results/itsp/human_review_round2_packet.zip) để khắc phục ngữ cảnh cụm dùng link nội bộ: **59 thành viên, 177 file đề/source/bản sửa, 395 test records**, mapping 17 phiếu và 27 cụm theo bài/A/B/C seed42. Chỉ phát sau khi khóa vòng 1. Không thêm mẫu annotation, không gán nhãn mới, không đổi thuật toán. Đã xác nhận 37 file nguồn/kết quả/annotation/gói vòng 1 giữ nguyên. [Biên bản kiểm tra](../results/itsp/review_handoff_audit.json).

Hồ sơ đủ để chuyển sang bước chuyên gia duyệt codebook và đánh giá độc lập; chưa có human annotation để hoàn tất expert validation. Chưa gửi hồ sơ hoặc liên hệ chuyên gia. Kiểm tra sau bàn giao: **64 tests + 3 subtests pass; lint pass**. Chạy lại scorer xác nhận 0 human reviews, 0 adjudication; expert purity/agreement vẫn null.


Quy trình hiện hành: [human review protocol](itsp_human_review_protocol.md). Codebook dự thảo đã có định nghĩa, ranh giới và quy tắc Unclear/đa nguyên nhân; cần chuyên gia chốt trước chấm. Không tính metric AI; mọi expert metric hiện null. Các số tests ở mốc lịch sử dưới đây thuộc từng lần kiểm tra; kết quả kiểm tra bàn giao mới nhất ghi trong packet audit.

## Bàn giao đánh giá độc lập — 19/09/2026

Đã tạo [bộ phiếu riêng cho chuyên gia](../results/itsp/human_review/README.md) gồm 17 hồ sơ (đề, source, bản sửa, log lịch sử) và `annotations.json` trống. Bộ bàn giao không chứa nhãn/giả thuyết AI, annotation AI trong codebook hoặc assignment cluster để hỗ trợ vòng đánh giá độc lập. Mỗi chuyên gia nhận một bản riêng; lưu kết quả vòng 1 trước khi cung cấp ngữ cảnh cụm ở vòng 2. Khi nhận file, đối chiếu ID và SHA-256 assignment, hợp nhất các lượt người đánh giá vào file human-only riêng, bảo tồn AI tham khảo và provenance ở file nội bộ; không thay AI bằng human chỉ bằng đổi reviewer_id.

Hiện có 17 AI reviews tham khảo nhưng **0 human reviews hoàn tất, 0 adjudication**; expert purity/agreement vẫn null. Cần người đánh giá thật và codebook được phê duyệt để hoàn tất validation. Chưa gửi phiếu cho bất kỳ ai; chỉ chuẩn bị file trong workspace. [Tải bộ phiếu ZIP](../results/itsp/human_review_packet.zip). Kiểm tra bàn giao: 17/17 log khớp dữ liệu hiện có, 51 file source/đề/bản sửa khớp SHA-256; ZIP không lỗi. **64 tests + 3 subtests pass; lint pass.**


## Expert validation — chờ annotation (19/09/2026)

Đã chuẩn bị [17 phiếu và hướng dẫn chuyên gia](itsp_expert_annotation_template.md), [file nhập annotation](../data/itsp/expert_annotations.json) và script `scripts/score_itsp_experts.py`. Hiện **0 lượt hoàn tất, 0 adjudication; cluster purity = null, agreement = null** trong [kết quả chấm](../results/itsp/expert_validation_metrics.json). Các giả thuyết kỹ thuật trước đây chỉ được đếm như AI tham khảo, không dùng tính purity/agreement.

Codebook và chính sách nhãn chờ chuyên gia thống nhất; chỉ tính purity theo loại trên mẫu Yes có loại đã adjudicate khi codebook được duyệt. Báo riêng từng bài/A/B/C, kèm mẫu số và coverage; No/Unclear không được coi là một loại misconception. Agreement gồm raw agreement và Cohen kappa theo cặp người đánh giá độc lập; thiếu cặp hoặc kappa không xác định giữ null. Ngữ cảnh cụm chỉ mở ở vòng hai. Chưa thể kết luận chất lượng misconception clustering hay OAV tốt hơn.

17 mẫu được chọn có chủ đích theo C gốc (9 medoid + 8 holdout xa nhất), không đại diện toàn cohort. ITSP không có student ID: không tạo ID giả, không tuyên bố unseen-student generalization. Chỉ bổ sung công cụ annotation/scoring ngoại tuyến, không thay đổi pipeline hoặc clustering A/B/C hiện có. Kiểm tra: **61 tests + 3 subtests pass**, `ruff check .` pass; SHA-256 xác nhận toàn bộ file source cũ và 27 kết quả A/B/C giữ nguyên.


## Cập nhật validation A/B/C

Đã bổ sung `structural` mode bằng thay đổi nhỏ ở FeatureSpace/pipeline/CLI; không đổi preprocessing,
schema, thuật toán hoặc thêm LLM/GNN. Chạy **27 lượt A/B/C trên cùng 59 mẫu** của ba bài cũ,
agglomerative average-linkage, k=3, seeds 7/42/91. Kiểm tra bằng assertion cùng routing/split;
A/C tái lập nguyên trạng các kết quả cũ. B chỉ dùng cấu trúc, không fallback sang test nếu hết feature.

- [Protocol đầy đủ](itsp_validation.md): baseline, 16 flags, distance, metrics, fairness và giới hạn.
- [Kết quả A/B/C](../results/itsp/abc_summary.md), [JSON/cluster sizes/statistics](../results/itsp/abc_summary.json).
- [Review đủ 17 mẫu](itsp_expert_review.md), [cluster A/B/C của từng mẫu](../results/itsp/abc_review_assignments.json).
- [Trạng thái purity/agreement](../results/itsp/expert_metric_readiness.json): null, vì 0 nhãn chuyên gia hoàn tất.

Seed42 A=C về phân hoạch; B có các cụm rất lệch và fidelity bằng majority baseline cả ba bài.
Không có bằng chứng OAV/structural tốt hơn. Sáu cụm C gốc ở 2825/2833 có nhiều cơ chế lỗi trong mẫu review;
B cũng trộn lỗi printf, output, công thức, input order và control flow trong các cụm lớn.
17 giả thuyết đều ghi rõ **assistant technical review**, không chuyển thành expert gold.
Mẫu lấy có chủ đích (9 medoid +8 holdout xa nhất) từ C, không đại diện toàn dataset.
Student ID vẫn null; không tuyên bố generalization theo người học chưa thấy.

Kiểm thử sau thay đổi: **48 tests +3 subtests pass**; lint được chạy sau khi sửa.
Chạy lại: `& .venv/Scripts/python.exe scripts/validate_itsp_abc.py`.
Phần còn thiếu để hoàn tất validation giáo dục: codebook đơn/đa nhãn và annotation độc lập của chuyên gia;
chưa tự chọn chính sách nhãn hoặc bịa purity. Các phần dưới ghi lại mốc tích hợp ITSP trước ablation này.

## Phạm vi và quyết định

ITSP là dataset công khai để thử pipeline, **không phải dữ liệu chính thức của giảng viên**.
Đã tải, kiểm tra, chuẩn hóa và chạy clustering thật; không chỉ lập kế hoạch.
Chưa có nhãn misconception do giảng viên xác nhận nên chưa thể báo độ chính xác chẩn đoán.

Áp dụng skill [karpathy-guidelines](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/skills/karpathy-guidelines/SKILL.md), đã có sẵn tại
`C:/Users/Admin/.codex/skills/karpathy-guidelines/SKILL.md`; không cài trùng.
Chia ba phần cho subagent: nhập/audit ITSP, extractor C, nghiên cứu/phản biện.
**Sonnet 4.6 không khả dụng trong danh sách model của phiên; dùng model kế thừa khả dụng.**
Agent chính tích hợp, đọc source/log/bản sửa, chạy kiểm thử và sửa các vấn đề review.

Ưu tiên CPU, không cần GPU/LLM trả phí, không cần Docker APR của ITSP, không thực thi code sinh viên.
Tham khảo nghiên cứu đến mốc yêu cầu; không tuyên bố khảo sát bao quát mọi SOTA hoặc đạt SOTA.

## Dữ liệu đã tải và audit

- Nguồn: [jyi/ITSP](https://github.com/jyi/ITSP), commit `0553f683f99403efb5ef440af826c1d229a52376`.
- Snapshot 2.368 file, 2.755.469 bytes, gồm `dataset/**`, README và LICENSE; không gồm APR toolkit.
- Mỗi file được kiểm tra Git blob SHA-1 và ghi SHA-256 trong `data/raw/itsp/provenance.json`.
- Adapter xác minh hash và tập file trước nhập, ghép test bằng **input + expected output**, không dựa vị trí.
- 661 bài sai thuộc 74 bài tập; nhập được 649, loại 12 do số test log khác suite công bố.
- 12 trường hợp bị loại: bài 3294 có 9 mẫu (4 so với 5 test), 2932 có 2 mẫu (6 so với 7),
  3105 có 1 mẫu (3 so với 4). Không giả định test còn thiếu đã pass/fail. Bài 3294 có 14 mẫu gốc,
  vẫn giữ 5 mẫu có log hợp lệ; cả 74 cohort đều còn dữ liệu.
- Trong 649 bài nhập: 648 qua routing, 1 parser failure tại `Lab-11/3299/305620_buggy.c`.
  Hàm `swap` dùng khai báo implicit-int kiểu cũ; parser không chấp nhận, **không chứng minh compile failure**.
- 40 bài nghi mọi test fail chỉ khác whitespace; 44 bài có ít nhất một test như vậy.
  Đây là heuristic xóa whitespace, có thể che mất ranh giới token; không dùng làm nhãn, không đổi verdict.
- 121 bài có ít nhất một output fail rỗng. Log WRONG_ANSWER không đủ để khẳng định kết thúc bình thường;
  pipeline giữ bằng chứng lịch sử, không tự gán timeout/runtime error.

Xem [audit đầy đủ](../data/itsp/audit.json). Bản sửa đúng chỉ nằm ở raw và được tham chiếu qua
`review.jsonl`; không dùng source sửa, diff, nhãn, danh tính hoặc comment log để tạo feature.

## Code và kiến trúc

`scripts/download_itsp.py` tải snapshot → `itsp.py` chuyển nguồn → manifest/JSONL chuẩn →
`domain.py` / `features.py` / `pipeline.py` → JSON kết quả. Thuật toán không đọc cấu trúc thư mục ITSP.
Không thêm database, service layer hoặc framework điều phối.

- **Schema v2:** cho phép `student_id: null`; v1 vẫn giữ kiểm tra cũ. Không giả ID bài làm thành người học.
- **Split:** nối source giống hệt; chỉ nối ID sinh viên khi có thật. Báo rõ không bảo đảm student-disjoint.
- **C feature:** tree-sitter C, 16 chỉ báo cú pháp về vòng lặp, điều kiện, chỉ số mảng, con trỏ và return.
  Parser không preprocessing, không phân tích alias/dataflow, không chứng minh lỗi; cả hai nhánh `#if`
  có thể xuất hiện. Python tiếp tục dùng AST chuẩn; C++/Java chưa có extractor.
- **Train-only:** bỏ feature cấu trúc hằng trên train; không nhìn holdout để chọn feature.
- **Khoảng cách:** categorical weighted Hamming; K-means dùng one-hot scale `sqrt(w/2)` và Euclidean.
- **Luật:** cây nông dự đoán ID cụm; báo fidelity và baseline cụm đa số được chọn từ train.
  ILA là hướng quy nạp có giám sát, chưa có đặc tả “ILA cải tiến” nên không gắn nhãn ILA cho cây.
- **Sửa review:** bỏ toàn bộ AST khi `test_weight=1`, tránh cây giải thích dùng feature có trọng số 0.
- **Holdout:** nearest training medoid cho mọi phương pháp, không phải `KMeans.predict`.

## Thí nghiệm đã chạy

Chọn ba cohort lớn nhất có ít nhất 12 mẫu eligible và 3 outcome signatures, không chọn theo điểm metric:

| Bài | Nội dung | Mẫu eligible | Test | Outcome signatures |
|---|---|---:|---:|---:|
| 2825 | Vị trí điểm so với đường tròn | 22 | 7 | 6 |
| 2812 | Dấu của số thực | 19 | 7 | 6 |
| 2833 | Đếm tam giác cạnh nguyên | 18 | 6 | 5 |

126 lần chạy: exact signatures; agglomerative và K-means với outcomes/combined,
k=2/3/4, seeds=7/42/91; thêm sensitivity trọng số test 0,6 thay 0,8 tại agglomerative combined k=3.
124 lần thành công, 2 lần abstain vì train không đủ mẫu đặc trưng khác nhau cho k=4.
Abstain được giữ trong báo cáo, không loại khỏi thống kê. Exact bỏ qua k.

Minh họa cấu hình định trước agglomerative, combined, k=3, test weight=0,8, seed=42:

| Bài | Silhouette train | Fidelity holdout | Majority fidelity |
|---|---:|---:|---:|
| 2825 | 0,696 | 0,833 | 0,500 |
| 2812 | 0,750 | 0,200 | 0,200 |
| 2833 | 0,678 | 0,800 | 0,600 |

**Chưa có bằng chứng cấu trúc đơn giản cải thiện chất lượng misconception.** Trong cấu hình minh họa,
fidelity outcomes-only bằng combined ở cả ba bài. Silhouette cao không chứng minh ý nghĩa sư phạm;
đặc biệt bài 2812 cho fidelity rất thấp dù silhouette khá cao. Holdout chỉ khoảng 5–6 mẫu/bài,
không có gold, không biết danh tính, nên không diễn giải như benchmark tổng quát hóa.
Các seed thay cả split và khởi tạo K-means: đây là độ nhạy thăm dò, không đo riêng optimizer stability.
Outcomes và combined cùng loại parser failure, vì vậy so sánh trên cùng tập parse được.

- [Bảng kết quả](../results/itsp/summary.md), [mọi lần chạy](../results/itsp/summary.json).
- [Tiêu chí và danh sách chọn bài](../results/itsp/selection.json).
- [Code/OAV/luật của medoid](../results/itsp/cluster_review.md).
- [Template chấm độc lập](../results/itsp/annotation_template.jsonl): 17 mẫu gồm medoid và mẫu holdout xa nhất từng cụm.
  Template chưa có nhãn; sao chép sang file riêng để chấm, vì chạy lại sẽ tạo lại template.
  Không cho chuyên gia đọc tên cụm/luật nếu cần annotation độc lập; tách nhãn khỏi feature.

## Đối chiếu thủ công và các giới hạn thực tế

Đã đọc 9 medoid của ba cohort, log test và các bản sửa liên quan; đây là review kỹ thuật,
không thay annotation chuyên gia. Chi tiết bài 2825: [case review](itsp_case_review.md).

Bài 2812:

- `270293_buggy`: mọi output thừa dấu chấm cuối; bản correct bỏ dấu chấm. Đề minh họa có dấu chấm
  nhưng oracle không có: cần ưu tiên mô tả bằng chứng, không kết luận sinh viên hiểu sai phép so sánh.
- `270277_buggy`: nhánh zero in thêm giá trị số; test zero fail nhưng test số khác pass.
- `270283_buggy`: `printf` chứa `%f` và `%n` nhưng thiếu đối số tương ứng; có hành vi không xác định.
  Log WRONG_ANSWER không biến lỗi này thành lỗi logic thuần túy.

Bài 2833:

- `271920_buggy`: `for(i=n;i>=1;i++)`; bản correct đổi `i++` thành `i--`. Log output rỗng;
  bằng chứng phù hợp lỗi hướng cập nhật, nhưng chưa có log runtime để xác nhận timeout.
- `271965_buggy`: ba vòng đều duyệt 1..N nên đếm cả hoán vị cạnh; bản correct dùng b từ a, c từ b.
  Output N=4 là 34 so với oracle 13, phù hợp giả thuyết đếm lặp.
- `271986_buggy`: có các phép gán `x=0`/`y=0`/`z=0` trong biểu thức điều kiện;
  bản correct bỏ cả điều kiện phụ. Nhiều cơ chế có thể cùng tồn tại, không quy mọi sai khác cho một lỗi duy nhất.

Heuristic whitespace không bắt được sai dấu câu/chính tả. Các feature presence hiện tại cũng không
phân biệt toán hạng, hướng cập nhật hay quan hệ giữa các biến. Hai bài khác lỗi vẫn có thể cùng OAV.
Không thêm heuristic gắn nhãn theo chính các mẫu vừa đọc: cần codebook và tập đánh giá độc lập trước.

## Chạy lại và thay dataset sau này

Kiểm chứng sau tích hợp: **43 tests và 3 subtests pass**, Ruff pass, `pip check` không phát hiện
dependency hỏng. Chạy CLI trên bài 2825 cho split, feature, assignments và luật trùng với batch runner.
Đã sửa và kiểm tra các vấn đề review nêu trên. Chi tiết trong [verification](verification.md).

Trong project, dùng môi trường Python 3.12 đã tạo:

```powershell
& .venv/Scripts/python.exe -m pip install -r requirements-lock.txt
& .venv/Scripts/python.exe -m pip install --no-deps --no-build-isolation -e .
& .venv/Scripts/python.exe scripts/download_itsp.py
& .venv/Scripts/python.exe scripts/prepare_itsp.py
& .venv/Scripts/python.exe scripts/run_itsp_experiments.py
& .venv/Scripts/python.exe -m pytest -q
& .venv/Scripts/python.exe -m ruff check src tests scripts
```

Đổi `--problems` để chỉ định cohort khi chạy experiment. Khi có data giảng viên, giữ raw riêng,
viết adapter mới theo [contract](data_contract.md), xác nhận ID người học/test suite/outcome,
dùng lại lõi và chạy đánh giá lại. Nếu ngôn ngữ đổi thì bổ sung extractor; nếu không có outcomes thì
cần log hoặc runner được kiểm soát, không suy outcome từ điểm tổng. Không trộn các bộ test khác nhau.

Phần cần con người/dữ liệu ngoài: mapping sinh viên chính thức, nhãn chuyên gia và xác nhận giá trị
giảng dạy. Phần có thể làm ngay đã thực hiện; không giả định những dữ liệu chưa được cung cấp.

## Nguồn kỹ thuật

- [ITSP và bài FSE17](https://github.com/jyi/ITSP): nguồn dataset, thiết kế lấy mẫu, yêu cầu trích dẫn.
- [scikit-learn clustering](https://scikit-learn.org/stable/modules/clustering.html): baseline và metric.
- [tree-sitter Python](https://github.com/tree-sitter/py-tree-sitter), [C grammar](https://github.com/tree-sitter/tree-sitter-c): parser cú pháp.
- [McMining EACL 2026](https://aclanthology.org/2026.eacl-short.10/): misconception cần evidence và đánh giá riêng.
- [Rà soát phương pháp đầy đủ](itsp_method_review.md): hạn chế và lý do không dùng mô hình lớn ở bước này.
