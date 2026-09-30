# Gói AI review cluster — Đề tài 5

5 cluster đủ điều kiện; 4 cluster/run bị loại. Tất cả pending_annotation.

Gửi PROMPT.md + response.schema.json + một file clusters/*.json hoặc *.md cho AI. evidence.json là toàn bộ dữ liệu, không cần gửi cả bộ trong một lần. JSON và Markdown từng cụm đều có toàn bộ code/log thành viên, không cắt ngắn.

response.template.json là danh sách CHỜ (result=null), không phải response đã hoàn thành. AI phải trả cấu trúc response.schema.json. Có thể nhận từng phần; dùng --require-complete khi kiểm tra lần cuối. Kết quả AI được lưu riêng, không tự gán gold hay ghi đè packet.

Selection policy:
```json
{
  "method": "kmeans",
  "feature_mode": "combined_stdout",
  "seed": 42,
  "min_cluster_size": 4,
  "min_distinct_sources": 3,
  "required_failed_log_coverage": 1.0,
  "min_common_failure_rate_cluster": 0.5,
  "representatives": "medoid then diverse OAV/outcomes, max 4",
  "ranking": "problem and cluster ID, no quality-score selection"
}
```

## Giới hạn

- Historical logs, no fresh execution or cognitive evidence.
- AI sees clusters/candidates: not independent blind human validation.
- No sealed test members, correct repairs or reviewer labels exported.
- Clustering OAV is archived; diagnostic OAV/rules are computed at export.
- Missing/not_run outcomes are not passes; rates include denominators.
- Counts/rates describe submissions, not independent students or beliefs.
- C-Pack oracle/suite correspondence has not been replay-verified.
- IDs and paths omitted; raw public source comments are preserved.

## Danh sách cụm

| Cluster | Số bài | Đề bài |
|---|---:|---|
| [2812--kmeans--combined_stdout--s42--c0](clusters/2812--kmeans--combined_stdout--s42--c0.md) | 8 | Có |
| [2825--kmeans--combined_stdout--s42--c0](clusters/2825--kmeans--combined_stdout--s42--c0.md) | 11 | Có |
| [2825--kmeans--combined_stdout--s42--c1](clusters/2825--kmeans--combined_stdout--s42--c1.md) | 7 | Có |
| [2825--kmeans--combined_stdout--s42--c2](clusters/2825--kmeans--combined_stdout--s42--c2.md) | 4 | Có |
| [2833--kmeans--combined_stdout--s42--c1](clusters/2833--kmeans--combined_stdout--s42--c1.md) | 8 | Có |

## Các cụm loại và lý do

```json
[
  {
    "cluster_id": "2812--kmeans--combined_stdout--s42--c1",
    "n_submissions": 3,
    "reasons": [
      "cluster_too_small"
    ],
    "n_incomplete": 0
  },
  {
    "cluster_id": "2812--kmeans--combined_stdout--s42--c2",
    "n_submissions": 2,
    "reasons": [
      "cluster_too_small",
      "fewer_than_3_distinct_sources"
    ],
    "n_incomplete": 0
  },
  {
    "cluster_id": "2833--kmeans--combined_stdout--s42--c0",
    "n_submissions": 2,
    "reasons": [
      "cluster_too_small",
      "fewer_than_3_distinct_sources"
    ],
    "n_incomplete": 0
  },
  {
    "cluster_id": "2833--kmeans--combined_stdout--s42--c2",
    "n_submissions": 3,
    "reasons": [
      "cluster_too_small"
    ],
    "n_incomplete": 0
  }
]
```

