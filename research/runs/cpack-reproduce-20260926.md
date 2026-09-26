# Tái lập C-Pack-IPAs baseline — 26/09/2026

Gói `cpack-baselines-20260926.zip` chứa dữ liệu đã chuẩn hóa (`dataset/`), đầy
đủ 675 artifact và snapshot mã (`run/`), cùng `split_lock.json`. Dữ liệu giữ
nguyên byte của các input đã dùng, để hash không phụ thuộc cách Git đổi newline
trên Windows/Linux. README và giấy phép MIT nguồn nằm trong `dataset/`.

Nguồn: [C-Pack-IPAs](https://github.com/pmorvalho/C-Pack-IPAs), commit
`76901e1223b250a093a02d5e29113ad735c3d2b9`.
Trích dẫn dataset: [Orvalho, Janota & Manquinho, APR 2024](https://doi.org/10.1145/3643788.3648010).
Chỉ sử dụng canonical `all_submissions`; bản sửa tương lai không làm feature.

Từ thư mục chứa gói, dùng Git và một môi trường Python 3.12 riêng:

```text
python -m zipfile -e cpack-baselines-20260926.zip bundle
git clone https://github.com/linhlinhlin/AAI.git AAI-repro
git -C AAI-repro checkout 3c67734c25236b7fdcd9d84b8d4c2fa589add36e
python -m zipfile -e bundle/run/code_snapshot.zip AAI-repro
cd AAI-repro
python -m pip install -r misconceptions-prototype/requirements-lock.txt
python -m pip install --no-deps --no-build-isolation -e misconceptions-prototype
python scripts/audit_run.py --data ../bundle/dataset --split-lock ../bundle/split_lock.json --run ../bundle/run
python misconceptions-prototype/scripts/run_topic5.py --data ../bundle/dataset --split-lock ../bundle/split_lock.json --output ../rerun
```

Snapshot mã ghi đè các file thực nghiệm trong **checkout mới dùng tái lập**.
Đầu vào, implementation hashes, packages, seed và k được lưu trong manifest.
Base commit là nền của snapshot; code nghiên cứu tại thời điểm chạy còn thay
đổi chưa commit. Không cần compiler C, GPU hoặc API key; chỉ đọc log lịch sử.
Thời gian chạy và sai khác số thực giữa binary/platform cần được ghi lại khi
tái lập, không mặc định byte-identical cho output sinh mới.

675 lượt = 25 bài × 9 biến thể × 3 seeds. 624 `ok`, 51 `abstained`: 42 lượt
không đủ mẫu/biểu diễn khác nhau cho k=3, 9 lượt có feature train giống hệt.
Test partition chưa được fit hoặc chấm. Không có nhãn cơ chế độc lập: các chỉ
số hiện tại không chứng minh độ chính xác misconception hoặc SOTA.

Audit kiểm tra hashes, đủ configurations, split membership, medoid, rule
support và trạng thái xác nhận. Nó kiểm tra tính toàn vẹn artifact, không phải
chứng nhận kết luận khoa học. `release_manifest.json` ngoài ZIP ghi checksum gói.
