# Đề 5 — ablation trên validation

Log lịch sử; test partition chưa đánh giá. Chưa có nhãn cơ chế độc lập.

Silhouette/fidelity mô tả hình học cụm và khả năng cây bắt chước cụm,
không phải độ chính xác phát hiện quan niệm sai.

## 2812

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {1: 1, 3: 1, 2: 1, 0: 6, 4: 2}.

- IF NOT (test:1=fail) AND NOT (test:2=pass) THEN cụm 2; train n=2, validation n=1, precision=0.0.
- IF NOT (test:1=fail) AND test:2=pass THEN cụm 4; train n=2, validation n=0, precision=None.
- IF test:1=fail THEN cụm 0; train n=7, validation n=1, precision=0.0.

### agglomerative / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 3, 1: 1, 2: 7}.

- IF NOT (test:7=pass) AND NOT (test:1=fail) THEN cụm 1; train n=2, validation n=1, precision=1.0.
- IF NOT (test:7=pass) AND test:1=fail THEN cụm 2; train n=6, validation n=0, precision=None.
- IF test:7=pass THEN cụm 0; train n=3, validation n=1, precision=1.0.

### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 3, 1: 1, 2: 7}.

- IF NOT (test:7=pass) AND NOT (test:1=pass) THEN cụm 2; train n=6, validation n=0, precision=None.
- IF NOT (test:7=pass) AND test:1=pass THEN cụm 1; train n=2, validation n=1, precision=1.0.
- IF test:7=pass THEN cụm 0; train n=3, validation n=1, precision=1.0.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 3, 1: 1, 0: 7}.

- IF NOT (stdout:2:relation=exact) AND NOT (stdout:2:edit_band=medium) THEN cụm 0; train n=6, validation n=1, precision=0.0.
- IF NOT (stdout:2:relation=exact) AND stdout:2:edit_band=medium THEN cụm 0; train n=2, validation n=0, precision=None.
- IF stdout:2:relation=exact THEN cụm 2; train n=3, validation n=1, precision=0.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 3, 1: 1, 0: 7}.

- IF NOT (stdout:2:relation=exact) AND NOT (stdout:5:relation=different) THEN cụm 0; train n=2, validation n=1, precision=0.0.
- IF NOT (stdout:2:relation=exact) AND stdout:5:relation=different THEN cụm 0; train n=6, validation n=0, precision=None.
- IF stdout:2:relation=exact THEN cụm 2; train n=3, validation n=1, precision=0.0.

### kmeans / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 3, 2: 1, 1: 7}.

- IF NOT (test:7=pass) AND NOT (test:1=fail) THEN cụm 1; train n=2, validation n=1, precision=0.0.
- IF NOT (test:7=pass) AND test:1=fail THEN cụm 1; train n=6, validation n=0, precision=None.
- IF test:7=pass THEN cụm 0; train n=3, validation n=1, precision=1.0.

### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 3, 2: 1, 1: 7}.

- IF NOT (test:7=pass) AND NOT (test:1=pass) THEN cụm 1; train n=6, validation n=0, precision=None.
- IF NOT (test:7=pass) AND test:1=pass THEN cụm 1; train n=2, validation n=1, precision=0.0.
- IF test:7=pass THEN cụm 0; train n=3, validation n=1, precision=1.0.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 3, 2: 1, 1: 7}.

- IF NOT (stdout:2:relation=exact) AND NOT (stdout:2:edit_band=medium) THEN cụm 1; train n=6, validation n=1, precision=0.0.
- IF NOT (stdout:2:relation=exact) AND stdout:2:edit_band=medium THEN cụm 1; train n=2, validation n=0, precision=None.
- IF stdout:2:relation=exact THEN cụm 0; train n=3, validation n=1, precision=0.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 3, 2: 1, 1: 7}.

- IF NOT (stdout:2:relation=exact) AND NOT (stdout:5:relation=different) THEN cụm 1; train n=2, validation n=1, precision=0.0.
- IF NOT (stdout:2:relation=exact) AND stdout:5:relation=different THEN cụm 1; train n=6, validation n=0, precision=None.
- IF stdout:2:relation=exact THEN cụm 0; train n=3, validation n=1, precision=0.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/13 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## 2825

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 9, 4: 2, 3: 3, 2: 2, 5: 2, 1: 2}.

- IF NOT (test:7=pass) AND NOT (test:5=fail) THEN cụm 2; train n=2, validation n=0, precision=None.
- IF NOT (test:7=pass) AND test:5=fail THEN cụm 0; train n=9, validation n=2, precision=1.0.
- IF test:7=pass AND NOT (test:4=pass) AND NOT (test:6=pass) THEN cụm 3; train n=3, validation n=0, precision=None.
- IF test:7=pass AND NOT (test:4=pass) AND test:6=pass THEN cụm 5; train n=2, validation n=0, precision=None.
- IF test:7=pass AND test:4=pass AND NOT (test:2=pass) THEN cụm 1; train n=2, validation n=0, precision=None.
- IF test:7=pass AND test:4=pass AND test:2=pass THEN cụm 4; train n=2, validation n=0, precision=None.

### agglomerative / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {1: 11, 0: 7, 2: 2}.

- IF NOT (test:1=fail) THEN cụm 0; train n=7, validation n=0, precision=None.
- IF test:1=fail AND NOT (test:5=fail) THEN cụm 2; train n=2, validation n=0, precision=None.
- IF test:1=fail AND test:5=fail THEN cụm 1; train n=11, validation n=2, precision=1.0.

### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {1: 11, 0: 7, 2: 2}.

- IF NOT (test:1=fail) THEN cụm 0; train n=7, validation n=0, precision=None.
- IF test:1=fail AND NOT (test:5=pass) THEN cụm 1; train n=11, validation n=2, precision=1.0.
- IF test:1=fail AND test:5=pass THEN cụm 2; train n=2, validation n=0, precision=None.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 9, 0: 9, 1: 2}.

- IF NOT (stdout:7:edit_band=zero) AND NOT (test:4=fail) THEN cụm 1; train n=2, validation n=0, precision=None.
- IF NOT (stdout:7:edit_band=zero) AND test:4=fail THEN cụm 2; train n=9, validation n=2, precision=1.0.
- IF stdout:7:edit_band=zero THEN cụm 0; train n=9, validation n=0, precision=None.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 9, 0: 9, 1: 2}.

- IF NOT (test:7=pass) AND NOT (stdout:3:relation=exact) THEN cụm 2; train n=9, validation n=2, precision=1.0.
- IF NOT (test:7=pass) AND stdout:3:relation=exact THEN cụm 1; train n=2, validation n=0, precision=None.
- IF test:7=pass THEN cụm 0; train n=9, validation n=0, precision=None.

### kmeans / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {1: 11, 2: 7, 0: 2}.

- IF NOT (test:1=fail) THEN cụm 2; train n=7, validation n=0, precision=None.
- IF test:1=fail AND NOT (test:5=fail) THEN cụm 0; train n=2, validation n=0, precision=None.
- IF test:1=fail AND test:5=fail THEN cụm 1; train n=11, validation n=2, precision=1.0.

### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {1: 11, 2: 7, 0: 2}.

- IF NOT (test:1=fail) THEN cụm 2; train n=7, validation n=0, precision=None.
- IF test:1=fail AND NOT (test:5=pass) THEN cụm 1; train n=11, validation n=2, precision=1.0.
- IF test:1=fail AND test:5=pass THEN cụm 0; train n=2, validation n=0, precision=None.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 9, 0: 7, 1: 4}.

- IF NOT (test:2=fail) THEN cụm 0; train n=7, validation n=0, precision=None.
- IF test:2=fail AND NOT (test:4=fail) THEN cụm 1; train n=4, validation n=0, precision=None.
- IF test:2=fail AND test:4=fail THEN cụm 2; train n=9, validation n=2, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 9, 0: 7, 1: 4}.

- IF NOT (stdout:2:edit_band=zero) AND NOT (test:4=fail) THEN cụm 1; train n=4, validation n=0, precision=None.
- IF NOT (stdout:2:edit_band=zero) AND test:4=fail THEN cụm 2; train n=9, validation n=2, precision=1.0.
- IF stdout:2:edit_band=zero THEN cụm 0; train n=7, validation n=0, precision=None.

### Phản hồi giảng dạy từ luật có dẫn chứng

12/22 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

- Nghi vấn nhầm quan hệ if–else và tính loại trừ giữa các nhánh (2 bài); cần người đánh giá.
- Sai khác trình bày output; chưa có bằng chứng về lỗi khái niệm từ sai khác này (10 bài); cần người đánh giá.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## 2833

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {3: 1, 0: 3, 2: 2, 1: 4}.

- IF NOT (test:2=fail) AND NOT (test:6=pass) THEN cụm 1; train n=4, validation n=1, precision=1.0.
- IF NOT (test:2=fail) AND test:6=pass THEN cụm 2; train n=3, validation n=0, precision=None.
- IF test:2=fail THEN cụm 0; train n=3, validation n=2, precision=1.0.

### agglomerative / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {2: 1, 0: 7, 1: 2}.

- IF NOT (test:6=pass) THEN cụm 0; train n=7, validation n=3, precision=1.0.
- IF test:6=pass THEN cụm 1; train n=3, validation n=0, precision=None.

### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 3, 1: 6, 2: 1}.

- IF NOT (test:6=pass) AND NOT (test:2=fail) THEN cụm 1; train n=4, validation n=1, precision=1.0.
- IF NOT (test:6=pass) AND test:2=fail THEN cụm 1; train n=3, validation n=2, precision=0.0.
- IF test:6=pass THEN cụm 0; train n=3, validation n=0, precision=None.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 3, 1: 2, 0: 5}.

- IF NOT (stdout:6:edit_band=small) AND NOT (test:6=fail) THEN cụm 2; train n=3, validation n=0, precision=None.
- IF NOT (stdout:6:edit_band=small) AND test:6=fail THEN cụm 1; train n=2, validation n=0, precision=None.
- IF stdout:6:edit_band=small THEN cụm 0; train n=5, validation n=3, precision=1.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 3, 1: 2, 0: 5}.

- IF NOT (stdout:6:edit_band=small) AND NOT (stdout:2:edit_band=zero) THEN cụm 1; train n=2, validation n=0, precision=None.
- IF NOT (stdout:6:edit_band=small) AND stdout:2:edit_band=zero THEN cụm 2; train n=3, validation n=0, precision=None.
- IF stdout:6:edit_band=small THEN cụm 0; train n=5, validation n=3, precision=1.0.

### kmeans / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 3, 2: 3, 1: 4}.

- IF NOT (test:6=pass) AND NOT (test:2=fail) THEN cụm 1; train n=4, validation n=1, precision=1.0.
- IF NOT (test:6=pass) AND test:2=fail THEN cụm 2; train n=3, validation n=2, precision=1.0.
- IF test:6=pass THEN cụm 0; train n=3, validation n=0, precision=None.

### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 3, 1: 3, 2: 4}.

- IF NOT (test:2=fail) AND NOT (test:6=fail) THEN cụm 0; train n=3, validation n=0, precision=None.
- IF NOT (test:2=fail) AND test:6=fail THEN cụm 2; train n=4, validation n=1, precision=1.0.
- IF test:2=fail THEN cụm 1; train n=3, validation n=2, precision=1.0.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 3, 2: 2, 1: 5}.

- IF NOT (stdout:6:edit_band=small) AND NOT (test:6=fail) THEN cụm 0; train n=3, validation n=0, precision=None.
- IF NOT (stdout:6:edit_band=small) AND test:6=fail THEN cụm 2; train n=2, validation n=0, precision=None.
- IF stdout:6:edit_band=small THEN cụm 1; train n=5, validation n=3, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 3, 2: 2, 1: 5}.

- IF NOT (stdout:6:edit_band=small) AND NOT (stdout:2:edit_band=zero) THEN cụm 2; train n=2, validation n=0, precision=None.
- IF NOT (stdout:6:edit_band=small) AND stdout:2:edit_band=zero THEN cụm 0; train n=3, validation n=0, precision=None.
- IF stdout:6:edit_band=small THEN cụm 1; train n=5, validation n=3, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/13 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.
