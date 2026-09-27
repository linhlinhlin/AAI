# Misconceptions Clustering — nghiên cứu đề 5

**Hiện tại (27/09/2026):** nhóm tự tìm dữ liệu; không chờ dataset giảng viên.
Xem [harness](../docs/harness.md), [tiêu chí đề 5](../docs/topic5-contract.md)
và [trạng thái nghiên cứu](../research/STATE.md). Các mục có ngày bên dưới mô tả
lịch sử prototype; hướng hiện tại có thêm C-Pack-IPAs, split toàn corpus và
baseline stdout. Đã có app học viên và giảng viên chạy local nhiều tài khoản.

## App học viên và giảng viên

Mở Docker Desktop Linux engine. Từ thư mục này, chạy
`& .venv/Scripts/python.exe scripts/setup_learning.py`, sau đó
`./start_learning.ps1` và mở **http://127.0.0.1:8766**.
Đăng ký học viên, làm bài C17, chạy test thật, sửa bài và xem lịch sử.
Tài khoản giảng viên xem lớp, OAV, cụm lỗi, luật IF–THEN và lưu nhận xét.
[Cài đặt, tạo giảng viên, kiểm chứng và giới hạn](../docs/learning_app.md).
App chưa được triển khai công khai; chưa có nghiên cứu hiệu quả học tập trên người.

## Bàn nghiên cứu và kiểm thử

Tại thư mục project, chạy `& .venv/Scripts/python.exe -m misconceptions.web --port 8765`,
rồi mở **http://127.0.0.1:8765**. Giao diện tiếng Việt có chạy thí nghiệm, xem cụm/OAV/luật,
so sánh A/B/C, nhập dữ liệu, xử lý annotation, kiểm tra kỹ thuật và kho báo cáo.
Chức năng chưa triển khai được vô hiệu hóa. [Hướng dẫn test từng bước](docs/web_workbench.md).
Kết quả web được lưu riêng trong `results/web_runs/`.

**Bàn giao cập nhật 20/09/2026:** [Công việc hoàn thành, kết quả, giới hạn và bước tiếp theo](docs/itsp_handoff_2026-09-20.md).

## Human expert review — sẵn sàng bàn giao

**0/17 human expert annotations; purity, raw agreement và Cohen’s kappa: chưa xác định/null.** 17 AI reviews chỉ là tham khảo nội bộ, không phải ground truth hoặc expert-validated; không tính purity/agreement từ AI.

- Gửi chuyên gia: [human_review_packet.zip](results/itsp/human_review_packet.zip), [hướng dẫn](results/itsp/human_review/README.md), [codebook dự thảo](results/itsp/human_review/CODEBOOK.md).
- Điều phối nội bộ: [validate → merge/adjudication → metrics → Results/Discussion](docs/itsp_human_review_protocol.md).
- [Kết quả rà soát gói](results/itsp/human_review_packet_audit.json). Chốt codebook với người thật trước chấm; vòng 1 không phát nhãn AI, cluster hoặc báo cáo tham khảo. Gói mới chỉ chuẩn bị, chưa gửi.

## Cập nhật ITSP — 19/09/2026

Đã tích hợp dataset công khai ITSP và extractor cú pháp C. **Chưa nhận dữ liệu chính thức của giảng viên.**
Đọc [nhật ký triển khai ITSP](docs/itsp_progress.md), [rà soát phương pháp](docs/itsp_method_review.md)
và [kết quả thực nghiệm](results/itsp/summary.md). Dữ liệu demo tổng hợp bên dưới vẫn dùng để kiểm thử hồi quy.

Chạy trong thư mục project, sau bước cài môi trường bên dưới (cần Git để tải snapshot):

```powershell
& .venv/Scripts/python.exe scripts/download_itsp.py
& .venv/Scripts/python.exe scripts/prepare_itsp.py
& .venv/Scripts/python.exe scripts/run_itsp_experiments.py
```

Pipeline đọc log test có sẵn; không thực thi code sinh viên. Schema v2 biểu diễn ID người học
không có bằng `null`. ITSP chỉ cho phép đánh giá thăm dò với split chống trùng source chính xác,
**không bảo đảm độc lập theo sinh viên**. Luật dự đoán ID cụm, chưa phải nhãn misconception đã xác nhận.

**Kết luận:** nên bắt đầu bằng gom cụm *biểu hiện lỗi* theo từng bài tập, dùng kết quả từng test và dấu hiệu cấu trúc đơn giản, rồi để giảng viên xác nhận giả thuyết misconception. Không đủ cơ sở suy ra một niềm tin sai chỉ từ một bài làm sai. ILA thuộc bước quy nạp luật có giám sát; không đặt ILA vào nhóm thuật toán clustering.

Phạm vi nghiên cứu: nguồn kiểm tra đến **19/09/2026**. Chưa nhận dataset giảng viên; không giả định ngôn ngữ, format hoặc nhãn của dataset đó. Bản demo dùng **52 fixture tổng hợp** để kiểm thử; thí nghiệm ITSP dùng dữ liệu công khai riêng. Python và C đã có extractor cú pháp, không phải yêu cầu đối với dữ liệu tương lai.

## Đọc gì trước?

- [Báo cáo đề xuất và pipeline](docs/research_plan.md): câu hỏi nghiên cứu, kiến trúc, thí nghiệm, chuyển dữ liệu.
- [Khảo sát nguồn và dataset](docs/research_sources.md): McMining 2026, CodeInsight 2026, EDM 2025, C-Pack-IPAs, CodeWorkout, CodeNet.
- [Phản biện phương pháp](docs/method_review.md): toán học, leakage, giới hạn suy luận và kế hoạch đánh giá.
- [Hợp đồng dữ liệu](docs/data_contract.md): cách thay nguồn dữ liệu mà giữ lõi pipeline.
- [Kết quả kiểm tra](docs/verification.md): các kiểm tra đã chạy, lỗi đã sửa và giới hạn còn lại.

## Chạy lại trên Windows PowerShell

Yêu cầu Python 3.11 trở lên; bản này được kiểm tra bằng Python 3.12. Chạy trong thư mục project:

```powershell
py -m venv .venv
& .venv/Scripts/python.exe -m pip install -r requirements-lock.txt
& .venv/Scripts/python.exe -m pip install --no-deps --no-build-isolation -e .
& .venv/Scripts/python.exe scripts/make_demo.py
& .venv/Scripts/python.exe -m misconceptions.cli --manifest data/demo/manifest.json --submissions data/demo/submissions.jsonl --method agglomerative --k 3 --output results/demo_report.json
& .venv/Scripts/python.exe scripts/run_ablation.py
& .venv/Scripts/python.exe -m pytest -q
& .venv/Scripts/python.exe -m ruff check src tests scripts
```

Linux/macOS: dùng `python3 -m venv .venv` và `.venv/bin/python` thay đường dẫn executable. `requirements-lock.txt` ghi phiên bản đã kiểm tra, không có hash wheel và không cam kết cùng binary trên mọi OS.

## Đã triển khai

- Adapter JSONL/manifest có validation; cohort cùng bài, ngôn ngữ, test suite.
- OAV outcome categorical + bảy dấu hiệu AST Python hoặc 16 dấu hiệu cú pháp C; bỏ feature hằng theo train.
- Tách parse error, chưa chạy đủ test, lỗi thực thi và pass toàn bộ.
- Chia train/holdout theo connected components cùng sinh viên (khi biết ID) hoặc source giống hệt; ITSP thiếu ID nên chưa bảo đảm độc lập người học.
- Exact signatures, average-linkage weighted Hamming, K-means trên one-hot có trọng số.
- Medoid đại diện, silhouette, luật cây nông, support/precision và fidelity trên holdout.
- Artifact JSON có OAV, assignments, lý do loại mẫu, seed và provenance.
- Thí nghiệm ablation nhỏ và kiểm thử hồi quy.

## Chưa triển khai có chủ đích

Pipeline offline không chạy code sinh viên hoặc gọi API trả phí. Web có cấu hình LLM tùy chọn và đã có giao diện. Chưa có phân tích ngữ nghĩa/alias/con trỏ đầy đủ, extractor C++/Java, nhãn misconception thật hay triển khai production. Ngôn ngữ chưa hỗ trợ vẫn có thể chạy outcomes và AST được đánh dấu unknown.

Không dùng các chỉ số fixture để báo “độ chính xác phát hiện misconception”. Các biến thể đổi tên trong demo là near-duplicate cố ý; guard exact-source không loại được tất cả near-duplicates. Cần protocol nghiêm ngặt hơn trên dữ liệu thật.

## Skill và phối hợp

Đã cài và đọc [karpathy-guidelines](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/skills/karpathy-guidelines/SKILL.md), qua skill-installer. Áp dụng: nêu giả định, thiết kế nhỏ, không thêm framework thiếu nhu cầu, kiểm chứng bằng test. Đã chia nghiên cứu, lõi thuật toán và phản biện cho subagent, sau đó tích hợp và review. **Sonnet 4.6 không khả dụng trong phiên; các subagent dùng model kế thừa khả dụng, không mạo nhận Sonnet.**
