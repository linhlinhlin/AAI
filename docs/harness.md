# Harness nghiên cứu AAI

Harness gồm hướng dẫn theo ngữ cảnh, skill cho thực nghiệm và các kiểm tra chạy
được. Mã lõi tiếp tục dùng NumPy/scikit-learn/tree-sitter của repo; không cần GPU
cho giai đoạn baseline. Môi trường lớn hơn chỉ cần khi bắt đầu encoder/LLM hoặc
can thiệp thực thi có sandbox.

## Cài đặt

Tại thư mục `AAI`, PowerShell:

```powershell
py -3.12 -m venv misconceptions-prototype/.venv
$aaiPython = (Resolve-Path misconceptions-prototype/.venv/Scripts/python.exe).Path
& $aaiPython -m pip install -r misconceptions-prototype/requirements-lock.txt
& $aaiPython -m pip install --no-deps --no-build-isolation -e misconceptions-prototype
& $aaiPython scripts/harness.py doctor
& $aaiPython scripts/harness.py check
& $aaiPython scripts/harness.py smoke
```

Linux/Kaggle: dùng Python 3.12 và `.venv/bin/python`; các script không phụ thuộc
PowerShell. `check` chạy Ruff + pytest offline. `smoke` dùng thư mục tạm, khóa
split ITSP trên toàn corpus rồi chạy 27 cấu hình của ba bài 2812/2825/2833; không
ghi đè dữ liệu hay kết quả nghiên cứu cũ. GitHub Actions gọi chính các lệnh này.
CI chưa được xác nhận trên GitHub cho tới khi workflow thực sự chạy ở đó.

## Lấy dữ liệu và khóa split

Từ `misconceptions-prototype`, với Python của môi trường đã cài:

```text
python scripts/download_cpack.py --output ../.cache/cpack-raw
python scripts/prepare_cpack.py --raw ../.cache/cpack-raw --output ../.cache/cpack-v3
python scripts/lock_splits.py --data ../.cache/cpack-v3 --output ../research/splits/cpack-v3.json
```

Downloader khóa release `C-Pack-IPAs-26` vào commit
`76901e1223b250a093a02d5e29113ad735c3d2b9`, chỉ checkout canonical originals,
tests và mô tả bài. Adapter giữ sinh viên xuyên năm, lịch sử lần nộp, compilation
status, verdict lịch sử, stdout thực sự có file và hash nguồn. README/giấy phép
được lưu cùng dữ liệu nhập. Không biên dịch hoặc thực thi mã C.

Accepted thường không lưu stdout: không tự điền oracle làm output. Test sai
thiếu file output chuyển sang `not_run`, đồng thời giữ verdict gốc trong audit;
bài đó không đủ bằng chứng cho baseline thống nhất. Lỗi metadata vẫn giữ source
và ID để không mất cầu nối chống leakage. “Presentation Error” vẫn là failure
của chấm bài, không phải nhãn quan niệm sai.

Log có marker `@@` cho timeout, giới hạn output, signal và exit code khác 0.
Adapter giữ các trạng thái thực thi đó; `Internal Error` của hệ thống chấm là
`not_run`. Stdout không phải UTF-8 được ghi audit và hash byte gốc, không thay
byte lỗi bằng ký tự giả để làm feature. Source rỗng giữ nguyên trong schema v2
để audit ID, nhưng sự vắng mặt code không nối hai sinh viên thành nhóm duplicate.
`dataset_complete.json` là dấu hoàn tất kèm hash các file nhập: import dở dang
hoặc dữ liệu bị sửa không thể dùng tạo split.

Split dùng hash thành phần liên thông để phân bổ mục tiêu 70/15/15 theo group;
số bài thực tế không nhất thiết theo tỷ lệ này. File lock kiểm tra corpus hash,
toàn bộ ID, tính độc lập thành phần và chính sách xác định. Nếu corpus đổi, tạo
phiên bản dữ liệu và lock mới. Lock không tự ghi đè. Cùng lock cho mọi ablation.
Các bài pass và lỗi biên dịch vẫn tham gia nối group trước lọc điều kiện thí nghiệm.

## Chạy nghiên cứu

```text
python scripts/run_topic5.py --data ../.cache/cpack-v3 --split-lock ../research/splits/cpack-v3.json --problems lab02-ex01 lab03-ex02 lab04-ex01 --output ../artifacts/cpack-pilot
```

Đây là pilot ba nhóm bài, không phải benchmark công bố. Bỏ `--problems` để chạy
toàn bộ cohort. Runner chỉ dùng train và validation, chưa có tùy chọn mở test.
Muốn đánh giá cuối cần đóng băng protocol và thêm đường đánh giá riêng được kiểm
tra; không đổi tên validation thành test sau khi đã xem kết quả.

Các baseline: exact pass/fail signature; average-linkage weighted Hamming và
K-means với `outcomes`, `combined`, `outcomes_stdout`, `combined_stdout`. Mỗi
configuration dùng seeds 7/42/91, k=3, split seed 42. Không chọn k/seed theo
validation trong runner. “Exact” bỏ qua k. Holdout của K-means theo medoid train,
giữ chính sách hiện có; không gọi đó là dự đoán nearest-centroid nguyên bản.

Stdout dùng hai mô tả cố định trên mỗi log: quan hệ với oracle (exact,
whitespace, empty, khớp oracle khác được quan sát trong suite, different) và
band sai khác ký tự từ SequenceMatcher (0, ≤0.1, ≤0.4, lớn hơn). Oracle khác chỉ
lấy từ định nghĩa test trong log của chính bài; thiếu định nghĩa là giới hạn
coverage. Nếu expected hoặc actual vượt 4.096 ký tự, band là
`not_computed_large_output`; vẫn giữ log gốc và tính quan hệ với oracle. Giới
hạn này ngăn SequenceMatcher có chi phí bậc hai trên output lặp dài; nó không
được diễn giải là output sai hay similarity thấp. Đây là similarity heuristic,
không phải khoảng cách edit Levenshtein
hay suy luận ngữ nghĩa. Thiếu stdout của test pass vẫn unknown. Cột hằng chỉ bỏ
theo train; vocabulary descriptor cố định, không học từ holdout.

Khi stdout có cột thay đổi, block này nhận 0.4 tổng trọng số, các block cũ nhân
0.6. Combined với AST hoạt động: test 0.48, AST 0.12, stdout 0.4. Nếu AST hằng,
test nhận 0.6; nếu stdout hằng, giữ trọng số baseline cũ. Mọi trọng số thực nằm
trong artifact. K-means dùng one-hot nhân căn bậc hai của w/2, nên squared
Euclidean giữa hai bản ghi bằng weighted Hamming của chúng.

Mỗi run ghi `run_manifest.json` (base commit, dirty state, hash mọi source và
script, requirements, protocol, split, seeds/k), `code_snapshot.zip` giữ đúng mã
đã chạy kể cả thay đổi chưa commit, hash input/evidence và phiên
bản Python/package. JSON mỗi cấu hình chứa routes, split, OAV, assignments,
medoid, luật cây và teaching findings. `summary.md` nối các kết quả thành báo
cáo đọc được. Thư mục output phải mới; kết quả cũ không bị ghi đè. Dữ liệu bulk
và exploratory runs nằm trong `.cache/`, `artifacts/` đã được Git ignore; báo
cáo chọn để bàn giao nằm trong `research/runs/`.

Kiểm tra một run đã hoàn tất, từ repository root:

```text
python scripts/audit_run.py --data .cache/cpack-v3 --split-lock research/splits/cpack-v3.json --run artifacts/cpack-baselines-20260926-final
```

Audit đối chiếu đủ configuration, checksum input/snapshot, membership split,
medoid và tổng support luật; kết quả là `integrity_audit.json`. Đây là kiểm
tra tính toàn vẹn artifact, không thay thế đánh giá khoa học bằng nhãn độc lập.

## Chỉ dẫn cho agent

`AGENTS.md` cung cấp mục tiêu và ranh giới đặc thù của nghiên cứu; `CLAUDE.md`
trỏ về cùng nguồn. `.agents/skills/aai-experiment/SKILL.md` chỉ kích hoạt khi
thiết kế/chạy/review thí nghiệm. Mở Codex từ `AAI` hoặc bên trong repo để tự
khám phá AGENTS và skill. Với chat đang đứng ở thư mục cha `BaiLinh`, dùng hướng
dẫn workspace tại đó hoặc đọc skill qua đường dẫn; repo con không được hứa là
tự động khám phá từ thư mục cha. Không thay cấu hình cá nhân hoặc model của nhóm.

Áp dụng hai nguồn người dùng yêu cầu:

- [Anthropic: large codebases](https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start): context gọn, tài liệu theo nhu cầu, tự động hóa các kiểm tra xác định. Ở repo này, script và CI cung cấp phần kiểm tra đó; chưa cấu hình native agent hooks.
- [OpenAI: rethinking skills and prompts for GPT-6 Astra](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): skill có phạm vi rõ, tránh bắt đọc toàn bộ tài liệu mỗi lần sửa và định nghĩa điểm hoàn thành bằng artifact/check cụ thể.
- [AGENTS discovery](https://developers.openai.com/codex/guides/agents-md/) và [skill discovery](https://developers.openai.com/codex/skills/): file ở repository root, skill dưới `.agents/skills`; không cần cài global plugin.

Xem lại hướng dẫn khi đổi model lớn hoặc khi một quy tắc liên tục gây chậm/sai;
xóa điều đã được code kiểm tra thay vì bổ sung thêm lời nhắc trùng lặp.
