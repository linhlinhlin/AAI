# Gói AI review cluster — Đề tài 5

69 cluster đủ điều kiện; 6 cluster/run bị loại. Tất cả pending_annotation.

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
| [lab02-ex01--kmeans--combined_stdout--s42--c0](clusters/lab02-ex01--kmeans--combined_stdout--s42--c0.md) | 90 | Thiếu |
| [lab02-ex01--kmeans--combined_stdout--s42--c1](clusters/lab02-ex01--kmeans--combined_stdout--s42--c1.md) | 59 | Thiếu |
| [lab02-ex01--kmeans--combined_stdout--s42--c2](clusters/lab02-ex01--kmeans--combined_stdout--s42--c2.md) | 13 | Thiếu |
| [lab02-ex02--kmeans--combined_stdout--s42--c0](clusters/lab02-ex02--kmeans--combined_stdout--s42--c0.md) | 43 | Thiếu |
| [lab02-ex02--kmeans--combined_stdout--s42--c1](clusters/lab02-ex02--kmeans--combined_stdout--s42--c1.md) | 52 | Thiếu |
| [lab02-ex02--kmeans--combined_stdout--s42--c2](clusters/lab02-ex02--kmeans--combined_stdout--s42--c2.md) | 10 | Thiếu |
| [lab02-ex03--kmeans--combined_stdout--s42--c0](clusters/lab02-ex03--kmeans--combined_stdout--s42--c0.md) | 35 | Thiếu |
| [lab02-ex03--kmeans--combined_stdout--s42--c1](clusters/lab02-ex03--kmeans--combined_stdout--s42--c1.md) | 24 | Thiếu |
| [lab02-ex03--kmeans--combined_stdout--s42--c2](clusters/lab02-ex03--kmeans--combined_stdout--s42--c2.md) | 5 | Thiếu |
| [lab02-ex04--kmeans--combined_stdout--s42--c0](clusters/lab02-ex04--kmeans--combined_stdout--s42--c0.md) | 50 | Thiếu |
| [lab02-ex04--kmeans--combined_stdout--s42--c1](clusters/lab02-ex04--kmeans--combined_stdout--s42--c1.md) | 28 | Thiếu |
| [lab02-ex04--kmeans--combined_stdout--s42--c2](clusters/lab02-ex04--kmeans--combined_stdout--s42--c2.md) | 16 | Thiếu |
| [lab02-ex05--kmeans--combined_stdout--s42--c1](clusters/lab02-ex05--kmeans--combined_stdout--s42--c1.md) | 6 | Thiếu |
| [lab02-ex05--kmeans--combined_stdout--s42--c2](clusters/lab02-ex05--kmeans--combined_stdout--s42--c2.md) | 5 | Thiếu |
| [lab02-ex06--kmeans--combined_stdout--s42--c0](clusters/lab02-ex06--kmeans--combined_stdout--s42--c0.md) | 28 | Thiếu |
| [lab02-ex06--kmeans--combined_stdout--s42--c1](clusters/lab02-ex06--kmeans--combined_stdout--s42--c1.md) | 16 | Thiếu |
| [lab02-ex06--kmeans--combined_stdout--s42--c2](clusters/lab02-ex06--kmeans--combined_stdout--s42--c2.md) | 12 | Thiếu |
| [lab02-ex07--kmeans--combined_stdout--s42--c1](clusters/lab02-ex07--kmeans--combined_stdout--s42--c1.md) | 24 | Thiếu |
| [lab02-ex07--kmeans--combined_stdout--s42--c2](clusters/lab02-ex07--kmeans--combined_stdout--s42--c2.md) | 28 | Thiếu |
| [lab02-ex08--kmeans--combined_stdout--s42--c0](clusters/lab02-ex08--kmeans--combined_stdout--s42--c0.md) | 40 | Thiếu |
| [lab02-ex08--kmeans--combined_stdout--s42--c1](clusters/lab02-ex08--kmeans--combined_stdout--s42--c1.md) | 21 | Thiếu |
| [lab02-ex08--kmeans--combined_stdout--s42--c2](clusters/lab02-ex08--kmeans--combined_stdout--s42--c2.md) | 17 | Thiếu |
| [lab02-ex09--kmeans--combined_stdout--s42--c0](clusters/lab02-ex09--kmeans--combined_stdout--s42--c0.md) | 57 | Thiếu |
| [lab02-ex09--kmeans--combined_stdout--s42--c1](clusters/lab02-ex09--kmeans--combined_stdout--s42--c1.md) | 16 | Thiếu |
| [lab02-ex09--kmeans--combined_stdout--s42--c2](clusters/lab02-ex09--kmeans--combined_stdout--s42--c2.md) | 28 | Thiếu |
| [lab02-ex10--kmeans--combined_stdout--s42--c0](clusters/lab02-ex10--kmeans--combined_stdout--s42--c0.md) | 5 | Thiếu |
| [lab02-ex10--kmeans--combined_stdout--s42--c1](clusters/lab02-ex10--kmeans--combined_stdout--s42--c1.md) | 11 | Thiếu |
| [lab02-ex10--kmeans--combined_stdout--s42--c2](clusters/lab02-ex10--kmeans--combined_stdout--s42--c2.md) | 17 | Thiếu |
| [lab03-ex01--kmeans--combined_stdout--s42--c0](clusters/lab03-ex01--kmeans--combined_stdout--s42--c0.md) | 8 | Thiếu |
| [lab03-ex01--kmeans--combined_stdout--s42--c1](clusters/lab03-ex01--kmeans--combined_stdout--s42--c1.md) | 91 | Thiếu |
| [lab03-ex01--kmeans--combined_stdout--s42--c2](clusters/lab03-ex01--kmeans--combined_stdout--s42--c2.md) | 37 | Thiếu |
| [lab03-ex02--kmeans--combined_stdout--s42--c0](clusters/lab03-ex02--kmeans--combined_stdout--s42--c0.md) | 59 | Thiếu |
| [lab03-ex02--kmeans--combined_stdout--s42--c1](clusters/lab03-ex02--kmeans--combined_stdout--s42--c1.md) | 99 | Thiếu |
| [lab03-ex02--kmeans--combined_stdout--s42--c2](clusters/lab03-ex02--kmeans--combined_stdout--s42--c2.md) | 41 | Thiếu |
| [lab03-ex03--kmeans--combined_stdout--s42--c0](clusters/lab03-ex03--kmeans--combined_stdout--s42--c0.md) | 9 | Thiếu |
| [lab03-ex03--kmeans--combined_stdout--s42--c1](clusters/lab03-ex03--kmeans--combined_stdout--s42--c1.md) | 52 | Thiếu |
| [lab03-ex03--kmeans--combined_stdout--s42--c2](clusters/lab03-ex03--kmeans--combined_stdout--s42--c2.md) | 66 | Thiếu |
| [lab03-ex04--kmeans--combined_stdout--s42--c0](clusters/lab03-ex04--kmeans--combined_stdout--s42--c0.md) | 156 | Thiếu |
| [lab03-ex04--kmeans--combined_stdout--s42--c1](clusters/lab03-ex04--kmeans--combined_stdout--s42--c1.md) | 49 | Thiếu |
| [lab03-ex04--kmeans--combined_stdout--s42--c2](clusters/lab03-ex04--kmeans--combined_stdout--s42--c2.md) | 140 | Thiếu |
| [lab03-ex05--kmeans--combined_stdout--s42--c0](clusters/lab03-ex05--kmeans--combined_stdout--s42--c0.md) | 18 | Thiếu |
| [lab03-ex05--kmeans--combined_stdout--s42--c1](clusters/lab03-ex05--kmeans--combined_stdout--s42--c1.md) | 45 | Thiếu |
| [lab03-ex05--kmeans--combined_stdout--s42--c2](clusters/lab03-ex05--kmeans--combined_stdout--s42--c2.md) | 54 | Thiếu |
| [lab03-ex06--kmeans--combined_stdout--s42--c0](clusters/lab03-ex06--kmeans--combined_stdout--s42--c0.md) | 22 | Thiếu |
| [lab03-ex06--kmeans--combined_stdout--s42--c1](clusters/lab03-ex06--kmeans--combined_stdout--s42--c1.md) | 29 | Thiếu |
| [lab03-ex06--kmeans--combined_stdout--s42--c2](clusters/lab03-ex06--kmeans--combined_stdout--s42--c2.md) | 16 | Thiếu |
| [lab03-ex07--kmeans--combined_stdout--s42--c0](clusters/lab03-ex07--kmeans--combined_stdout--s42--c0.md) | 28 | Thiếu |
| [lab03-ex07--kmeans--combined_stdout--s42--c1](clusters/lab03-ex07--kmeans--combined_stdout--s42--c1.md) | 15 | Thiếu |
| [lab03-ex07--kmeans--combined_stdout--s42--c2](clusters/lab03-ex07--kmeans--combined_stdout--s42--c2.md) | 10 | Thiếu |
| [lab04-ex01--kmeans--combined_stdout--s42--c1](clusters/lab04-ex01--kmeans--combined_stdout--s42--c1.md) | 12 | Thiếu |
| [lab04-ex02--kmeans--combined_stdout--s42--c0](clusters/lab04-ex02--kmeans--combined_stdout--s42--c0.md) | 13 | Thiếu |
| [lab04-ex02--kmeans--combined_stdout--s42--c1](clusters/lab04-ex02--kmeans--combined_stdout--s42--c1.md) | 12 | Thiếu |
| [lab04-ex02--kmeans--combined_stdout--s42--c2](clusters/lab04-ex02--kmeans--combined_stdout--s42--c2.md) | 5 | Thiếu |
| [lab04-ex03--kmeans--combined_stdout--s42--c0](clusters/lab04-ex03--kmeans--combined_stdout--s42--c0.md) | 19 | Thiếu |
| [lab04-ex04--kmeans--combined_stdout--s42--c0](clusters/lab04-ex04--kmeans--combined_stdout--s42--c0.md) | 10 | Thiếu |
| [lab04-ex04--kmeans--combined_stdout--s42--c1](clusters/lab04-ex04--kmeans--combined_stdout--s42--c1.md) | 16 | Thiếu |
| [lab04-ex04--kmeans--combined_stdout--s42--c2](clusters/lab04-ex04--kmeans--combined_stdout--s42--c2.md) | 30 | Thiếu |
| [lab04-ex05--kmeans--combined_stdout--s42--c0](clusters/lab04-ex05--kmeans--combined_stdout--s42--c0.md) | 29 | Thiếu |
| [lab04-ex05--kmeans--combined_stdout--s42--c1](clusters/lab04-ex05--kmeans--combined_stdout--s42--c1.md) | 35 | Thiếu |
| [lab04-ex05--kmeans--combined_stdout--s42--c2](clusters/lab04-ex05--kmeans--combined_stdout--s42--c2.md) | 6 | Thiếu |
| [lab04-ex06--kmeans--combined_stdout--s42--c0](clusters/lab04-ex06--kmeans--combined_stdout--s42--c0.md) | 4 | Thiếu |
| [lab04-ex06--kmeans--combined_stdout--s42--c1](clusters/lab04-ex06--kmeans--combined_stdout--s42--c1.md) | 20 | Thiếu |
| [lab04-ex06--kmeans--combined_stdout--s42--c2](clusters/lab04-ex06--kmeans--combined_stdout--s42--c2.md) | 16 | Thiếu |
| [lab04-ex07--kmeans--combined_stdout--s42--c0](clusters/lab04-ex07--kmeans--combined_stdout--s42--c0.md) | 31 | Thiếu |
| [lab04-ex07--kmeans--combined_stdout--s42--c1](clusters/lab04-ex07--kmeans--combined_stdout--s42--c1.md) | 16 | Thiếu |
| [lab04-ex07--kmeans--combined_stdout--s42--c2](clusters/lab04-ex07--kmeans--combined_stdout--s42--c2.md) | 12 | Thiếu |
| [lab04-ex08--kmeans--combined_stdout--s42--c0](clusters/lab04-ex08--kmeans--combined_stdout--s42--c0.md) | 37 | Thiếu |
| [lab04-ex08--kmeans--combined_stdout--s42--c1](clusters/lab04-ex08--kmeans--combined_stdout--s42--c1.md) | 13 | Thiếu |
| [lab04-ex08--kmeans--combined_stdout--s42--c2](clusters/lab04-ex08--kmeans--combined_stdout--s42--c2.md) | 15 | Thiếu |

## Các cụm loại và lý do

```json
[
  {
    "cluster_id": "lab02-ex05--kmeans--combined_stdout--s42--c0",
    "n_submissions": 3,
    "reasons": [
      "cluster_too_small"
    ],
    "n_incomplete": 0
  },
  {
    "cluster_id": "lab02-ex07--kmeans--combined_stdout--s42--c0",
    "n_submissions": 3,
    "reasons": [
      "cluster_too_small"
    ],
    "n_incomplete": 0
  },
  {
    "cluster_id": "lab04-ex01--kmeans--combined_stdout--s42--c0",
    "n_submissions": 3,
    "reasons": [
      "cluster_too_small"
    ],
    "n_incomplete": 0
  },
  {
    "cluster_id": "lab04-ex01--kmeans--combined_stdout--s42--c2",
    "n_submissions": 1,
    "reasons": [
      "cluster_too_small",
      "fewer_than_3_distinct_sources"
    ],
    "n_incomplete": 0
  },
  {
    "cluster_id": "lab04-ex03--kmeans--combined_stdout--s42--c1",
    "n_submissions": 2,
    "reasons": [
      "cluster_too_small",
      "fewer_than_3_distinct_sources"
    ],
    "n_incomplete": 0
  },
  {
    "cluster_id": "lab04-ex03--kmeans--combined_stdout--s42--c2",
    "n_submissions": 1,
    "reasons": [
      "cluster_too_small",
      "fewer_than_3_distinct_sources"
    ],
    "n_incomplete": 0
  }
]
```

