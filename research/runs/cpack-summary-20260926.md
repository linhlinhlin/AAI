# Đề 5 — ablation trên validation

Log lịch sử; test partition chưa đánh giá. Chưa có nhãn cơ chế độc lập.

Silhouette/fidelity mô tả hình học cụm và khả năng cây bắt chước cụm,
không phải độ chính xác phát hiện quan niệm sai.

## lab02-ex01

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 106, 3: 8, 2: 4, 1: 1}.

- IF NOT (test:ex01_0=pass) THEN cụm 0; train n=107, validation n=41, precision=1.0.
- IF test:ex01_0=pass AND NOT (test:ex01_2=fail) THEN cụm 3; train n=8, validation n=0, precision=None.
- IF test:ex01_0=pass AND test:ex01_2=fail THEN cụm 2; train n=4, validation n=2, precision=1.0.

### agglomerative / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 110, 2: 8, 1: 1}.

- IF NOT (test:ex01_2=fail) THEN cụm 2; train n=9, validation n=0, precision=None.
- IF test:ex01_2=fail THEN cụm 0; train n=110, validation n=43, precision=1.0.

### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {2: 106, 0: 12, 1: 1}.

- IF NOT (test:ex01_0=pass) AND NOT (ast:c_if=1) AND NOT (ast:c_while=1) THEN cụm 2; train n=9, validation n=1, precision=1.0.
- IF NOT (test:ex01_0=pass) AND NOT (ast:c_if=1) AND ast:c_while=1 THEN cụm 2; train n=5, validation n=1, precision=1.0.
- IF NOT (test:ex01_0=pass) AND ast:c_if=1 THEN cụm 2; train n=93, validation n=39, precision=1.0.
- IF test:ex01_0=pass THEN cụm 0; train n=12, validation n=2, precision=1.0.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 110, 1: 8, 2: 1}.

- IF NOT (test:ex01_2=fail) AND NOT (stdout:ex01_1:relation=different) THEN cụm 1; train n=2, validation n=0, precision=None.
- IF NOT (test:ex01_2=fail) AND stdout:ex01_1:relation=different THEN cụm 1; train n=7, validation n=0, precision=None.
- IF test:ex01_2=fail THEN cụm 0; train n=110, validation n=43, precision=1.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 110, 1: 8, 2: 1}.

- IF NOT (stdout:ex01_2:relation=__unknown__) THEN cụm 0; train n=110, validation n=43, precision=1.0.
- IF stdout:ex01_2:relation=__unknown__ AND NOT (stdout:ex01_1:relation=different) THEN cụm 1; train n=2, validation n=0, precision=None.
- IF stdout:ex01_2:relation=__unknown__ AND stdout:ex01_1:relation=different THEN cụm 1; train n=7, validation n=0, precision=None.

### kmeans / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 107, 1: 8, 2: 4}.

- IF NOT (test:ex01_0=pass) THEN cụm 0; train n=107, validation n=41, precision=1.0.
- IF test:ex01_0=pass AND NOT (test:ex01_2=pass) THEN cụm 2; train n=4, validation n=2, precision=1.0.
- IF test:ex01_0=pass AND test:ex01_2=pass THEN cụm 1; train n=8, validation n=0, precision=None.

### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 106, 1: 9, 2: 4}.

- IF NOT (test:ex01_0=pass) AND NOT (ast:c_if=1) AND NOT (ast:c_while=1) THEN cụm 0; train n=9, validation n=1, precision=1.0.
- IF NOT (test:ex01_0=pass) AND NOT (ast:c_if=1) AND ast:c_while=1 THEN cụm 0; train n=5, validation n=1, precision=1.0.
- IF NOT (test:ex01_0=pass) AND ast:c_if=1 THEN cụm 0; train n=93, validation n=39, precision=1.0.
- IF test:ex01_0=pass AND NOT (test:ex01_2=pass) THEN cụm 2; train n=4, validation n=2, precision=1.0.
- IF test:ex01_0=pass AND test:ex01_2=pass THEN cụm 1; train n=8, validation n=0, precision=None.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 63, 2: 13, 1: 43}.

- IF NOT (stdout:ex01_0:edit_band=large) AND NOT (stdout:ex01_0:relation=whitespace) AND NOT (stdout:ex01_1:edit_band=large) THEN cụm 2; train n=4, validation n=1, precision=0.0.
- IF NOT (stdout:ex01_0:edit_band=large) AND NOT (stdout:ex01_0:relation=whitespace) AND stdout:ex01_1:edit_band=large THEN cụm 2; train n=9, validation n=1, precision=0.0.
- IF NOT (stdout:ex01_0:edit_band=large) AND stdout:ex01_0:relation=whitespace THEN cụm 1; train n=43, validation n=16, precision=1.0.
- IF stdout:ex01_0:edit_band=large AND NOT (stdout:ex01_2:relation=different) THEN cụm 0; train n=3, validation n=1, precision=1.0.
- IF stdout:ex01_0:edit_band=large AND stdout:ex01_2:relation=different THEN cụm 0; train n=60, validation n=24, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 62, 1: 13, 0: 44}.

- IF NOT (stdout:ex01_0:relation=whitespace) AND NOT (test:ex01_0=pass) AND NOT (stdout:ex01_2:edit_band=large) THEN cụm 1; train n=2, validation n=0, precision=None.
- IF NOT (stdout:ex01_0:relation=whitespace) AND NOT (test:ex01_0=pass) AND stdout:ex01_2:edit_band=large THEN cụm 2; train n=61, validation n=25, precision=1.0.
- IF NOT (stdout:ex01_0:relation=whitespace) AND test:ex01_0=pass THEN cụm 1; train n=12, validation n=2, precision=1.0.
- IF stdout:ex01_0:relation=whitespace THEN cụm 0; train n=44, validation n=16, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/460 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab02-ex02

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 65, 3: 9, 2: 2, 1: 2}.

- IF NOT (test:ex02_0=pass) AND NOT (test:ex02_2=fail) AND NOT (test:ex02_1=pass) THEN cụm 1; train n=2, validation n=0, precision=None.
- IF NOT (test:ex02_0=pass) AND NOT (test:ex02_2=fail) AND test:ex02_1=pass THEN cụm 2; train n=2, validation n=1, precision=1.0.
- IF NOT (test:ex02_0=pass) AND test:ex02_2=fail THEN cụm 0; train n=65, validation n=25, precision=1.0.
- IF test:ex02_0=pass THEN cụm 3; train n=9, validation n=1, precision=1.0.

### agglomerative / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 67, 2: 9, 1: 2}.

- IF NOT (test:ex02_0=pass) AND NOT (test:ex02_1=pass) THEN cụm 0; train n=67, validation n=25, precision=1.0.
- IF NOT (test:ex02_0=pass) AND test:ex02_1=pass THEN cụm 1; train n=2, validation n=1, precision=1.0.
- IF test:ex02_0=pass THEN cụm 2; train n=9, validation n=1, precision=1.0.

### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 74, 1: 2, 2: 2}.

- IF NOT (test:ex02_2=fail) AND NOT (ast:c_update=0) THEN cụm 2; train n=2, validation n=0, precision=None.
- IF NOT (test:ex02_2=fail) AND ast:c_update=0 THEN cụm 1; train n=2, validation n=1, precision=1.0.
- IF test:ex02_2=fail THEN cụm 0; train n=74, validation n=26, precision=1.0.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 35, 0: 41, 1: 2}.

- IF NOT (stdout:ex02_0:relation=different) AND NOT (stdout:ex02_1:edit_band=medium) THEN cụm 0; train n=3, validation n=4, precision=0.0.
- IF NOT (stdout:ex02_0:relation=different) AND stdout:ex02_1:edit_band=medium THEN cụm 0; train n=39, validation n=8, precision=1.0.
- IF stdout:ex02_0:relation=different AND NOT (stdout:ex02_2:relation=__unknown__) THEN cụm 2; train n=33, validation n=15, precision=0.9333333333333333.
- IF stdout:ex02_0:relation=different AND stdout:ex02_2:relation=__unknown__ THEN cụm 2; train n=3, validation n=0, precision=None.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 35, 2: 41, 1: 2}.

- IF NOT (stdout:ex02_0:relation=different) AND NOT (stdout:ex02_1:edit_band=medium) THEN cụm 2; train n=3, validation n=4, precision=0.0.
- IF NOT (stdout:ex02_0:relation=different) AND stdout:ex02_1:edit_band=medium THEN cụm 2; train n=39, validation n=8, precision=1.0.
- IF stdout:ex02_0:relation=different AND NOT (stdout:ex02_2:edit_band=__unknown__) THEN cụm 0; train n=33, validation n=15, precision=0.9333333333333333.
- IF stdout:ex02_0:relation=different AND stdout:ex02_2:edit_band=__unknown__ THEN cụm 0; train n=3, validation n=0, precision=None.

### kmeans / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 67, 1: 9, 2: 2}.

- IF NOT (test:ex02_0=pass) AND NOT (test:ex02_1=pass) THEN cụm 0; train n=67, validation n=25, precision=1.0.
- IF NOT (test:ex02_0=pass) AND test:ex02_1=pass THEN cụm 2; train n=2, validation n=1, precision=1.0.
- IF test:ex02_0=pass THEN cụm 1; train n=9, validation n=1, precision=1.0.

### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 67, 1: 9, 2: 2}.

- IF NOT (test:ex02_0=pass) AND NOT (test:ex02_3=fail) THEN cụm 2; train n=2, validation n=1, precision=1.0.
- IF NOT (test:ex02_0=pass) AND test:ex02_3=fail THEN cụm 0; train n=67, validation n=25, precision=1.0.
- IF test:ex02_0=pass THEN cụm 1; train n=9, validation n=1, precision=1.0.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 36, 2: 9, 1: 33}.

- IF NOT (stdout:ex02_0:relation=different) AND NOT (stdout:ex02_0:edit_band=medium) THEN cụm 2; train n=9, validation n=1, precision=1.0.
- IF NOT (stdout:ex02_0:relation=different) AND stdout:ex02_0:edit_band=medium THEN cụm 1; train n=33, validation n=11, precision=0.8181818181818182.
- IF stdout:ex02_0:relation=different THEN cụm 0; train n=36, validation n=15, precision=0.9333333333333333.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 36, 2: 9, 1: 33}.

- IF NOT (stdout:ex02_0:relation=different) AND NOT (test:ex02_0=pass) THEN cụm 1; train n=33, validation n=11, precision=0.8181818181818182.
- IF NOT (stdout:ex02_0:relation=different) AND test:ex02_0=pass THEN cụm 2; train n=9, validation n=1, precision=1.0.
- IF stdout:ex02_0:relation=different THEN cụm 0; train n=36, validation n=15, precision=0.9333333333333333.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/370 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab02-ex03

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 44, 1: 4, 2: 4}.

- IF NOT (test:ex03_1=fail) THEN cụm 1; train n=4, validation n=2, precision=1.0.
- IF test:ex03_1=fail AND NOT (test:ex03_2=fail) THEN cụm 2; train n=4, validation n=1, precision=1.0.
- IF test:ex03_1=fail AND test:ex03_2=fail THEN cụm 0; train n=44, validation n=9, precision=1.0.

### agglomerative / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 44, 2: 4, 1: 4}.

- IF NOT (test:ex03_1=fail) THEN cụm 2; train n=4, validation n=2, precision=1.0.
- IF test:ex03_1=fail AND NOT (test:ex03_2=fail) THEN cụm 1; train n=4, validation n=1, precision=1.0.
- IF test:ex03_1=fail AND test:ex03_2=fail THEN cụm 0; train n=44, validation n=9, precision=1.0.

### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 44, 1: 4, 2: 4}.

- IF NOT (test:ex03_3=pass) AND NOT (test:ex03_2=pass) THEN cụm 0; train n=44, validation n=9, precision=1.0.
- IF NOT (test:ex03_3=pass) AND test:ex03_2=pass THEN cụm 2; train n=4, validation n=1, precision=1.0.
- IF test:ex03_3=pass THEN cụm 1; train n=4, validation n=2, precision=1.0.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 44, 2: 4, 1: 4}.

- IF NOT (test:ex03_3=fail) THEN cụm 2; train n=4, validation n=2, precision=1.0.
- IF test:ex03_3=fail AND NOT (test:ex03_2=fail) THEN cụm 1; train n=4, validation n=1, precision=1.0.
- IF test:ex03_3=fail AND test:ex03_2=fail THEN cụm 0; train n=44, validation n=9, precision=1.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 44, 1: 4, 2: 4}.

- IF NOT (stdout:ex03_2:edit_band=__unknown__) AND NOT (stdout:ex03_3:edit_band=__unknown__) THEN cụm 0; train n=44, validation n=9, precision=1.0.
- IF NOT (stdout:ex03_2:edit_band=__unknown__) AND stdout:ex03_3:edit_band=__unknown__ THEN cụm 1; train n=4, validation n=2, precision=1.0.
- IF stdout:ex03_2:edit_band=__unknown__ THEN cụm 2; train n=4, validation n=1, precision=1.0.

### kmeans / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 44, 1: 4, 2: 4}.

- IF NOT (test:ex03_1=fail) THEN cụm 1; train n=4, validation n=2, precision=1.0.
- IF test:ex03_1=fail AND NOT (test:ex03_2=fail) THEN cụm 2; train n=4, validation n=1, precision=1.0.
- IF test:ex03_1=fail AND test:ex03_2=fail THEN cụm 0; train n=44, validation n=9, precision=1.0.

### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 44, 2: 4, 1: 4}.

- IF NOT (test:ex03_3=pass) AND NOT (test:ex03_2=pass) THEN cụm 0; train n=44, validation n=9, precision=1.0.
- IF NOT (test:ex03_3=pass) AND test:ex03_2=pass THEN cụm 1; train n=4, validation n=1, precision=1.0.
- IF test:ex03_3=pass THEN cụm 2; train n=4, validation n=2, precision=1.0.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 18, 1: 30, 2: 4}.

- IF NOT (stdout:ex03_2:relation=whitespace) AND NOT (stdout:ex03_0:relation=__unknown__) THEN cụm 0; train n=18, validation n=7, precision=1.0.
- IF NOT (stdout:ex03_2:relation=whitespace) AND stdout:ex03_0:relation=__unknown__ THEN cụm 2; train n=4, validation n=1, precision=1.0.
- IF stdout:ex03_2:relation=whitespace THEN cụm 1; train n=30, validation n=4, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 18, 1: 30, 2: 4}.

- IF NOT (stdout:ex03_0:relation=whitespace) AND NOT (test:ex03_2=pass) THEN cụm 0; train n=18, validation n=7, precision=1.0.
- IF NOT (stdout:ex03_0:relation=whitespace) AND test:ex03_2=pass THEN cụm 2; train n=4, validation n=1, precision=1.0.
- IF stdout:ex03_0:relation=whitespace THEN cụm 1; train n=30, validation n=4, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

41/314 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

- Sai khác trình bày output; chưa có bằng chứng về lỗi khái niệm từ sai khác này (41 bài); cần người đánh giá.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab02-ex04

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 70, 1: 2, 2: 6}.

- IF NOT (test:ex04_0=pass) AND NOT (test:ex04_2=fail) THEN cụm 1; train n=2, validation n=2, precision=1.0.
- IF NOT (test:ex04_0=pass) AND test:ex04_2=fail THEN cụm 0; train n=70, validation n=12, precision=1.0.
- IF test:ex04_0=pass THEN cụm 2; train n=6, validation n=2, precision=1.0.

### agglomerative / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {2: 70, 1: 2, 0: 6}.

- IF NOT (test:ex04_0=pass) AND NOT (test:ex04_2=fail) THEN cụm 1; train n=2, validation n=2, precision=1.0.
- IF NOT (test:ex04_0=pass) AND test:ex04_2=fail THEN cụm 2; train n=70, validation n=12, precision=1.0.
- IF test:ex04_0=pass THEN cụm 0; train n=6, validation n=2, precision=1.0.

### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 70, 1: 2, 2: 6}.

- IF NOT (test:ex04_0=pass) AND NOT (test:ex04_2=pass) THEN cụm 0; train n=70, validation n=12, precision=1.0.
- IF NOT (test:ex04_0=pass) AND test:ex04_2=pass THEN cụm 1; train n=2, validation n=2, precision=1.0.
- IF test:ex04_0=pass THEN cụm 2; train n=6, validation n=2, precision=1.0.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 37, 2: 39, 1: 2}.

- IF NOT (stdout:ex04_3:relation=whitespace) AND NOT (test:ex04_1=pass) THEN cụm 0; train n=37, validation n=12, precision=1.0.
- IF NOT (stdout:ex04_3:relation=whitespace) AND test:ex04_1=pass THEN cụm 1; train n=2, validation n=2, precision=1.0.
- IF stdout:ex04_3:relation=whitespace THEN cụm 2; train n=39, validation n=2, precision=1.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 37, 2: 39, 1: 2}.

- IF NOT (stdout:ex04_1:relation=whitespace) AND NOT (stdout:ex04_1:edit_band=__unknown__) THEN cụm 0; train n=37, validation n=12, precision=1.0.
- IF NOT (stdout:ex04_1:relation=whitespace) AND stdout:ex04_1:edit_band=__unknown__ THEN cụm 1; train n=2, validation n=2, precision=1.0.
- IF stdout:ex04_1:relation=whitespace THEN cụm 2; train n=39, validation n=2, precision=1.0.

### kmeans / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 70, 2: 2, 1: 6}.

- IF NOT (test:ex04_0=pass) AND NOT (test:ex04_2=fail) THEN cụm 2; train n=2, validation n=2, precision=1.0.
- IF NOT (test:ex04_0=pass) AND test:ex04_2=fail THEN cụm 0; train n=70, validation n=12, precision=1.0.
- IF test:ex04_0=pass THEN cụm 1; train n=6, validation n=2, precision=1.0.

### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 70, 1: 2, 2: 6}.

- IF NOT (test:ex04_0=pass) AND NOT (test:ex04_2=pass) THEN cụm 0; train n=70, validation n=12, precision=1.0.
- IF NOT (test:ex04_0=pass) AND test:ex04_2=pass THEN cụm 1; train n=2, validation n=2, precision=1.0.
- IF test:ex04_0=pass THEN cụm 2; train n=6, validation n=2, precision=1.0.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 30, 0: 27, 1: 21}.

- IF NOT (stdout:ex04_0:edit_band=small) AND NOT (stdout:ex04_2:edit_band=large) AND NOT (stdout:ex04_1:edit_band=large) THEN cụm 2; train n=29, validation n=8, precision=0.875.
- IF NOT (stdout:ex04_0:edit_band=small) AND NOT (stdout:ex04_2:edit_band=large) AND stdout:ex04_1:edit_band=large THEN cụm 1; train n=3, validation n=0, precision=None.
- IF NOT (stdout:ex04_0:edit_band=small) AND stdout:ex04_2:edit_band=large THEN cụm 1; train n=18, validation n=5, precision=1.0.
- IF stdout:ex04_0:edit_band=small AND NOT (stdout:ex04_1:edit_band=small) THEN cụm 0; train n=2, validation n=1, precision=0.0.
- IF stdout:ex04_0:edit_band=small AND stdout:ex04_1:edit_band=small THEN cụm 0; train n=26, validation n=2, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 30, 0: 27, 1: 21}.

- IF NOT (stdout:ex04_0:edit_band=small) AND NOT (stdout:ex04_3:edit_band=large) AND NOT (stdout:ex04_1:edit_band=large) THEN cụm 2; train n=29, validation n=8, precision=0.875.
- IF NOT (stdout:ex04_0:edit_band=small) AND NOT (stdout:ex04_3:edit_band=large) AND stdout:ex04_1:edit_band=large THEN cụm 1; train n=3, validation n=0, precision=None.
- IF NOT (stdout:ex04_0:edit_band=small) AND stdout:ex04_3:edit_band=large THEN cụm 1; train n=18, validation n=5, precision=1.0.
- IF stdout:ex04_0:edit_band=small AND NOT (stdout:ex04_3:edit_band=small) THEN cụm 0; train n=2, validation n=1, precision=0.0.
- IF stdout:ex04_0:edit_band=small AND stdout:ex04_3:edit_band=small THEN cụm 0; train n=26, validation n=2, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/347 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab02-ex05

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 9, 1: 2}.

- IF NOT (test:ex05_0=fail) THEN cụm 1; train n=2, validation n=1, precision=1.0.
- IF test:ex05_0=fail THEN cụm 0; train n=9, validation n=2, precision=1.0.

### agglomerative / outcomes

Trạng thái: `abstained`; k_requires_more_training_rows_or_distinct_patterns

Quy mô cụm train: {}.


### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {1: 7, 0: 2, 2: 2}.

- IF NOT (ast:c_inclusive_comparison=0) AND NOT (ast:c_while=0) THEN cụm 1; train n=4, validation n=1, precision=1.0.
- IF NOT (ast:c_inclusive_comparison=0) AND ast:c_while=0 THEN cụm 1; train n=4, validation n=0, precision=None.
- IF ast:c_inclusive_comparison=0 THEN cụm 2; train n=3, validation n=2, precision=0.5.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 4, 0: 5, 1: 2}.

- IF NOT (stdout:ex05_2:edit_band=large) AND NOT (test:ex05_0=fail) THEN cụm 1; train n=2, validation n=1, precision=1.0.
- IF NOT (stdout:ex05_2:edit_band=large) AND test:ex05_0=fail THEN cụm 0; train n=5, validation n=1, precision=1.0.
- IF stdout:ex05_2:edit_band=large THEN cụm 2; train n=4, validation n=1, precision=1.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 4, 1: 5, 0: 2}.

- IF NOT (stdout:ex05_2:edit_band=medium) THEN cụm 2; train n=4, validation n=1, precision=1.0.
- IF stdout:ex05_2:edit_band=medium AND NOT (test:ex05_0=fail) THEN cụm 0; train n=2, validation n=1, precision=1.0.
- IF stdout:ex05_2:edit_band=medium AND test:ex05_0=fail THEN cụm 1; train n=5, validation n=1, precision=1.0.

### kmeans / outcomes

Trạng thái: `abstained`; k_requires_more_training_rows_or_distinct_patterns

Quy mô cụm train: {}.


### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 4, 1: 2, 2: 5}.

- IF NOT (ast:c_for=1) AND NOT (test:ex05_0=fail) THEN cụm 1; train n=2, validation n=1, precision=1.0.
- IF NOT (ast:c_for=1) AND test:ex05_0=fail THEN cụm 2; train n=5, validation n=2, precision=1.0.
- IF ast:c_for=1 THEN cụm 0; train n=4, validation n=0, precision=None.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 4, 1: 5, 2: 2}.

- IF NOT (stdout:ex05_2:edit_band=large) AND NOT (test:ex05_0=fail) THEN cụm 2; train n=2, validation n=1, precision=1.0.
- IF NOT (stdout:ex05_2:edit_band=large) AND test:ex05_0=fail THEN cụm 1; train n=5, validation n=1, precision=1.0.
- IF stdout:ex05_2:edit_band=large THEN cụm 0; train n=4, validation n=1, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 4, 2: 5, 0: 2}.

- IF NOT (stdout:ex05_2:edit_band=medium) THEN cụm 1; train n=4, validation n=1, precision=1.0.
- IF stdout:ex05_2:edit_band=medium AND NOT (test:ex05_0=fail) THEN cụm 0; train n=2, validation n=1, precision=1.0.
- IF stdout:ex05_2:edit_band=medium AND test:ex05_0=fail THEN cụm 2; train n=5, validation n=1, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/257 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab02-ex06

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {1: 5, 0: 24, 6: 4, 5: 9, 3: 6, 2: 1, 4: 1}.

- IF NOT (test:ex06_2=fail) AND NOT (test:ex06_0=pass) AND NOT (test:ex06_1=fail) THEN cụm 3; train n=6, validation n=0, precision=None.
- IF NOT (test:ex06_2=fail) AND NOT (test:ex06_0=pass) AND test:ex06_1=fail THEN cụm 1; train n=5, validation n=0, precision=None.
- IF NOT (test:ex06_2=fail) AND test:ex06_0=pass THEN cụm 5; train n=9, validation n=2, precision=1.0.
- IF test:ex06_2=fail AND NOT (test:ex06_1=pass) THEN cụm 0; train n=25, validation n=4, precision=1.0.
- IF test:ex06_2=fail AND test:ex06_1=pass THEN cụm 6; train n=5, validation n=0, precision=None.

### agglomerative / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 36, 1: 5, 2: 9}.

- IF NOT (test:ex06_0=pass) THEN cụm 0; train n=36, validation n=4, precision=1.0.
- IF test:ex06_0=pass AND NOT (test:ex06_2=pass) THEN cụm 1; train n=5, validation n=0, precision=None.
- IF test:ex06_0=pass AND test:ex06_2=pass THEN cụm 2; train n=9, validation n=2, precision=1.0.

### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 36, 1: 4, 2: 10}.

- IF NOT (test:ex06_0=pass) THEN cụm 0; train n=36, validation n=4, precision=1.0.
- IF test:ex06_0=pass AND NOT (test:ex06_1=pass) THEN cụm 2; train n=10, validation n=2, precision=1.0.
- IF test:ex06_0=pass AND test:ex06_1=pass THEN cụm 1; train n=4, validation n=0, precision=None.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 21, 2: 24, 1: 5}.

- IF NOT (test:ex06_2=fail) THEN cụm 0; train n=20, validation n=2, precision=1.0.
- IF test:ex06_2=fail AND NOT (test:ex06_0=fail) THEN cụm 1; train n=5, validation n=0, precision=None.
- IF test:ex06_2=fail AND test:ex06_0=fail AND NOT (stdout:ex06_2:edit_band=small) THEN cụm 2; train n=16, validation n=4, precision=1.0.
- IF test:ex06_2=fail AND test:ex06_0=fail AND stdout:ex06_2:edit_band=small THEN cụm 2; train n=9, validation n=0, precision=None.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 15, 1: 24, 0: 11}.

- IF NOT (test:ex06_2=pass) AND NOT (stdout:ex06_1:edit_band=__unknown__) AND NOT (ast:c_update=1) THEN cụm 1; train n=6, validation n=2, precision=1.0.
- IF NOT (test:ex06_2=pass) AND NOT (stdout:ex06_1:edit_band=__unknown__) AND ast:c_update=1 THEN cụm 1; train n=19, validation n=2, precision=1.0.
- IF NOT (test:ex06_2=pass) AND stdout:ex06_1:edit_band=__unknown__ THEN cụm 0; train n=5, validation n=0, precision=None.
- IF test:ex06_2=pass AND NOT (stdout:ex06_1:edit_band=small) THEN cụm 0; train n=6, validation n=0, precision=None.
- IF test:ex06_2=pass AND stdout:ex06_1:edit_band=small THEN cụm 2; train n=14, validation n=2, precision=1.0.

### kmeans / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {1: 29, 2: 11, 0: 10}.

- IF NOT (test:ex06_1=fail) THEN cụm 2; train n=11, validation n=0, precision=None.
- IF test:ex06_1=fail AND NOT (test:ex06_0=pass) THEN cụm 1; train n=29, validation n=4, precision=1.0.
- IF test:ex06_1=fail AND test:ex06_0=pass THEN cụm 0; train n=10, validation n=2, precision=1.0.

### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {2: 14, 1: 25, 0: 11}.

- IF NOT (test:ex06_2=pass) AND NOT (test:ex06_1=fail) THEN cụm 0; train n=5, validation n=0, precision=None.
- IF NOT (test:ex06_2=pass) AND test:ex06_1=fail THEN cụm 1; train n=25, validation n=4, precision=1.0.
- IF test:ex06_2=pass AND NOT (test:ex06_1=pass) THEN cụm 2; train n=14, validation n=2, precision=1.0.
- IF test:ex06_2=pass AND test:ex06_1=pass THEN cụm 0; train n=6, validation n=0, precision=None.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 14, 1: 25, 2: 11}.

- IF NOT (test:ex06_2=fail) AND NOT (stdout:ex06_1:relation=different) THEN cụm 2; train n=6, validation n=0, precision=None.
- IF NOT (test:ex06_2=fail) AND stdout:ex06_1:relation=different THEN cụm 0; train n=14, validation n=2, precision=1.0.
- IF test:ex06_2=fail AND NOT (stdout:ex06_1:relation=__unknown__) THEN cụm 1; train n=25, validation n=4, precision=1.0.
- IF test:ex06_2=fail AND stdout:ex06_1:relation=__unknown__ THEN cụm 2; train n=5, validation n=0, precision=None.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 14, 0: 25, 2: 11}.

- IF NOT (test:ex06_2=pass) AND NOT (stdout:ex06_1:edit_band=__unknown__) THEN cụm 0; train n=25, validation n=4, precision=1.0.
- IF NOT (test:ex06_2=pass) AND stdout:ex06_1:edit_band=__unknown__ THEN cụm 2; train n=5, validation n=0, precision=None.
- IF test:ex06_2=pass AND NOT (stdout:ex06_1:relation=__unknown__) THEN cụm 1; train n=14, validation n=2, precision=1.0.
- IF test:ex06_2=pass AND stdout:ex06_1:relation=__unknown__ THEN cụm 2; train n=6, validation n=0, precision=None.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/337 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab02-ex07

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 33, 2: 2, 1: 1}.

- IF NOT (test:ex07_1=fail) THEN cụm 2; train n=3, validation n=0, precision=None.
- IF test:ex07_1=fail THEN cụm 0; train n=33, validation n=19, precision=1.0.

### agglomerative / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 33, 1: 2, 2: 1}.

- IF NOT (test:ex07_1=fail) THEN cụm 1; train n=3, validation n=0, precision=None.
- IF test:ex07_1=fail THEN cụm 0; train n=33, validation n=19, precision=1.0.

### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 33, 1: 2, 2: 1}.

- IF NOT (test:ex07_0=fail) THEN cụm 1; train n=3, validation n=2, precision=0.0.
- IF test:ex07_0=fail THEN cụm 0; train n=33, validation n=17, precision=1.0.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 17, 2: 16, 0: 3}.

- IF NOT (stdout:ex07_0:edit_band=large) AND NOT (test:ex07_1=pass) THEN cụm 2; train n=16, validation n=10, precision=0.8.
- IF NOT (stdout:ex07_0:edit_band=large) AND test:ex07_1=pass THEN cụm 0; train n=3, validation n=0, precision=None.
- IF stdout:ex07_0:edit_band=large THEN cụm 1; train n=17, validation n=9, precision=1.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 17, 2: 16, 1: 3}.

- IF NOT (stdout:ex07_1:edit_band=large) AND NOT (stdout:ex07_0:relation=whitespace) THEN cụm 1; train n=3, validation n=0, precision=None.
- IF NOT (stdout:ex07_1:edit_band=large) AND stdout:ex07_0:relation=whitespace THEN cụm 2; train n=16, validation n=8, precision=1.0.
- IF stdout:ex07_1:edit_band=large THEN cụm 0; train n=17, validation n=11, precision=1.0.

### kmeans / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 33, 1: 2, 2: 1}.

- IF NOT (test:ex07_1=fail) THEN cụm 1; train n=3, validation n=0, precision=None.
- IF test:ex07_1=fail THEN cụm 0; train n=33, validation n=19, precision=1.0.

### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 12, 1: 21, 2: 3}.

- IF NOT (ast:c_while=0) AND NOT (test:ex07_0=pass) THEN cụm 1; train n=21, validation n=15, precision=1.0.
- IF NOT (ast:c_while=0) AND test:ex07_0=pass THEN cụm 2; train n=3, validation n=0, precision=None.
- IF ast:c_while=0 THEN cụm 0; train n=12, validation n=4, precision=1.0.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 17, 0: 16, 2: 3}.

- IF NOT (stdout:ex07_0:edit_band=large) AND NOT (test:ex07_1=pass) THEN cụm 0; train n=16, validation n=10, precision=0.8.
- IF NOT (stdout:ex07_0:edit_band=large) AND test:ex07_1=pass THEN cụm 2; train n=3, validation n=0, precision=None.
- IF stdout:ex07_0:edit_band=large THEN cụm 1; train n=17, validation n=9, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 17, 0: 16, 2: 3}.

- IF NOT (stdout:ex07_1:edit_band=large) AND NOT (stdout:ex07_0:relation=whitespace) THEN cụm 2; train n=3, validation n=0, precision=None.
- IF NOT (stdout:ex07_1:edit_band=large) AND stdout:ex07_0:relation=whitespace THEN cụm 0; train n=16, validation n=8, precision=1.0.
- IF stdout:ex07_1:edit_band=large THEN cụm 1; train n=17, validation n=11, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/274 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab02-ex08

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 59, 1: 1}.

- IF TRUE THEN cụm 0; train n=60, validation n=18, precision=0.9444444444444444.

### agglomerative / outcomes

Trạng thái: `abstained`; k_requires_more_training_rows_or_distinct_patterns

Quy mô cụm train: {}.


### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {2: 25, 0: 34, 1: 1}.

- IF NOT (ast:c_for=1) AND NOT (ast:c_strict_comparison=1) AND NOT (ast:c_inclusive_comparison=1) THEN cụm 0; train n=5, validation n=5, precision=1.0.
- IF NOT (ast:c_for=1) AND NOT (ast:c_strict_comparison=1) AND ast:c_inclusive_comparison=1 THEN cụm 0; train n=9, validation n=3, precision=1.0.
- IF NOT (ast:c_for=1) AND ast:c_strict_comparison=1 THEN cụm 0; train n=21, validation n=2, precision=1.0.
- IF ast:c_for=1 THEN cụm 2; train n=25, validation n=8, precision=0.875.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 28, 2: 31, 1: 1}.

- IF NOT (stdout:ex08_2:relation=whitespace) AND NOT (stdout:ex08_0:relation=different) THEN cụm 0; train n=2, validation n=2, precision=0.5.
- IF NOT (stdout:ex08_2:relation=whitespace) AND stdout:ex08_0:relation=different THEN cụm 0; train n=27, validation n=7, precision=1.0.
- IF stdout:ex08_2:relation=whitespace THEN cụm 2; train n=31, validation n=9, precision=1.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 28, 2: 31, 1: 1}.

- IF NOT (stdout:ex08_4:relation=different) THEN cụm 2; train n=31, validation n=10, precision=0.9.
- IF stdout:ex08_4:relation=different AND NOT (stdout:ex08_0:relation=different) THEN cụm 0; train n=2, validation n=1, precision=0.0.
- IF stdout:ex08_4:relation=different AND stdout:ex08_0:relation=different THEN cụm 0; train n=27, validation n=7, precision=0.8571428571428571.

### kmeans / outcomes

Trạng thái: `abstained`; k_requires_more_training_rows_or_distinct_patterns

Quy mô cụm train: {}.


### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 21, 1: 21, 2: 18}.

- IF NOT (ast:c_strict_comparison=0) AND NOT (ast:c_for=0) THEN cụm 0; train n=21, validation n=7, precision=1.0.
- IF NOT (ast:c_strict_comparison=0) AND ast:c_for=0 THEN cụm 1; train n=21, validation n=2, precision=1.0.
- IF ast:c_strict_comparison=0 THEN cụm 2; train n=18, validation n=9, precision=0.3333333333333333.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 13, 2: 16, 1: 31}.

- IF NOT (stdout:ex08_2:relation=whitespace) AND NOT (stdout:ex08_2:edit_band=large) AND NOT (stdout:ex08_0:edit_band=medium) THEN cụm 0; train n=2, validation n=2, precision=1.0.
- IF NOT (stdout:ex08_2:relation=whitespace) AND NOT (stdout:ex08_2:edit_band=large) AND stdout:ex08_0:edit_band=medium THEN cụm 0; train n=12, validation n=3, precision=1.0.
- IF NOT (stdout:ex08_2:relation=whitespace) AND stdout:ex08_2:edit_band=large THEN cụm 2; train n=15, validation n=4, precision=1.0.
- IF stdout:ex08_2:relation=whitespace THEN cụm 1; train n=31, validation n=9, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 13, 2: 16, 1: 31}.

- IF NOT (stdout:ex08_4:relation=different) THEN cụm 1; train n=31, validation n=10, precision=0.9.
- IF stdout:ex08_4:relation=different AND NOT (stdout:ex08_1:edit_band=large) AND NOT (stdout:ex08_0:edit_band=medium) THEN cụm 0; train n=2, validation n=3, precision=0.6666666666666666.
- IF stdout:ex08_4:relation=different AND NOT (stdout:ex08_1:edit_band=large) AND stdout:ex08_0:edit_band=medium THEN cụm 0; train n=12, validation n=3, precision=1.0.
- IF stdout:ex08_4:relation=different AND stdout:ex08_1:edit_band=large THEN cụm 2; train n=15, validation n=2, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/340 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab02-ex09

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 62, 4: 6, 6: 7, 5: 1, 2: 3, 1: 1, 3: 2}.

- IF NOT (test:ex09_1=fail) AND NOT (test:ex09_2=fail) THEN cụm 6; train n=7, validation n=1, precision=1.0.
- IF NOT (test:ex09_1=fail) AND test:ex09_2=fail AND NOT (test:ex09_0=fail) THEN cụm 4; train n=7, validation n=1, precision=1.0.
- IF NOT (test:ex09_1=fail) AND test:ex09_2=fail AND test:ex09_0=fail THEN cụm 3; train n=2, validation n=0, precision=None.
- IF test:ex09_1=fail AND NOT (test:ex09_2=pass) THEN cụm 0; train n=63, validation n=17, precision=1.0.
- IF test:ex09_1=fail AND test:ex09_2=pass THEN cụm 2; train n=3, validation n=0, precision=None.

### agglomerative / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 68, 1: 7, 2: 7}.

- IF NOT (test:ex09_0=pass) THEN cụm 0; train n=68, validation n=17, precision=1.0.
- IF test:ex09_0=pass AND NOT (test:ex09_2=fail) THEN cụm 2; train n=7, validation n=1, precision=1.0.
- IF test:ex09_0=pass AND test:ex09_2=fail THEN cụm 1; train n=7, validation n=1, precision=1.0.

### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 68, 1: 13, 2: 1}.

- IF NOT (test:ex09_0=pass) THEN cụm 0; train n=68, validation n=17, precision=1.0.
- IF test:ex09_0=pass AND NOT (ast:c_strict_comparison=0) THEN cụm 1; train n=3, validation n=1, precision=1.0.
- IF test:ex09_0=pass AND ast:c_strict_comparison=0 THEN cụm 1; train n=11, validation n=1, precision=1.0.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 42, 0: 26, 1: 14}.

- IF NOT (stdout:ex09_0:edit_band=small) AND NOT (test:ex09_0=fail) THEN cụm 1; train n=14, validation n=2, precision=1.0.
- IF NOT (stdout:ex09_0:edit_band=small) AND test:ex09_0=fail THEN cụm 2; train n=42, validation n=13, precision=0.9230769230769231.
- IF stdout:ex09_0:edit_band=small THEN cụm 0; train n=26, validation n=4, precision=1.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 44, 0: 24, 1: 14}.

- IF NOT (stdout:ex09_0:relation=different) AND NOT (stdout:ex09_0:relation=whitespace) AND NOT (stdout:ex09_1:edit_band=large) THEN cụm 1; train n=14, validation n=2, precision=1.0.
- IF NOT (stdout:ex09_0:relation=different) AND NOT (stdout:ex09_0:relation=whitespace) AND stdout:ex09_1:edit_band=large THEN cụm 2; train n=2, validation n=1, precision=0.0.
- IF NOT (stdout:ex09_0:relation=different) AND stdout:ex09_0:relation=whitespace THEN cụm 0; train n=23, validation n=3, precision=1.0.
- IF stdout:ex09_0:relation=different AND NOT (stdout:ex09_3:relation=different) THEN cụm 0; train n=2, validation n=0, precision=None.
- IF stdout:ex09_0:relation=different AND stdout:ex09_3:relation=different THEN cụm 2; train n=41, validation n=13, precision=0.9230769230769231.

### kmeans / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 68, 2: 7, 1: 7}.

- IF NOT (test:ex09_0=pass) THEN cụm 0; train n=68, validation n=17, precision=1.0.
- IF test:ex09_0=pass AND NOT (test:ex09_2=fail) THEN cụm 1; train n=7, validation n=1, precision=1.0.
- IF test:ex09_0=pass AND test:ex09_2=fail THEN cụm 2; train n=7, validation n=1, precision=1.0.

### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {1: 52, 0: 16, 2: 14}.

- IF NOT (ast:c_if=0) AND NOT (test:ex09_0=pass) THEN cụm 0; train n=16, validation n=4, precision=1.0.
- IF NOT (ast:c_if=0) AND test:ex09_0=pass THEN cụm 2; train n=6, validation n=1, precision=1.0.
- IF ast:c_if=0 AND NOT (test:ex09_0=fail) THEN cụm 2; train n=8, validation n=1, precision=1.0.
- IF ast:c_if=0 AND test:ex09_0=fail THEN cụm 1; train n=52, validation n=13, precision=1.0.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 45, 1: 23, 2: 14}.

- IF NOT (stdout:ex09_0:relation=different) AND NOT (stdout:ex09_0:relation=whitespace) AND NOT (stdout:ex09_2:edit_band=large) THEN cụm 2; train n=14, validation n=2, precision=1.0.
- IF NOT (stdout:ex09_0:relation=different) AND NOT (stdout:ex09_0:relation=whitespace) AND stdout:ex09_2:edit_band=large THEN cụm 0; train n=2, validation n=1, precision=1.0.
- IF NOT (stdout:ex09_0:relation=different) AND stdout:ex09_0:relation=whitespace THEN cụm 1; train n=23, validation n=3, precision=1.0.
- IF stdout:ex09_0:relation=different THEN cụm 0; train n=43, validation n=13, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 45, 2: 23, 1: 14}.

- IF NOT (stdout:ex09_0:relation=different) AND NOT (stdout:ex09_0:relation=whitespace) AND NOT (stdout:ex09_1:edit_band=large) THEN cụm 1; train n=14, validation n=2, precision=1.0.
- IF NOT (stdout:ex09_0:relation=different) AND NOT (stdout:ex09_0:relation=whitespace) AND stdout:ex09_1:edit_band=large THEN cụm 0; train n=2, validation n=1, precision=1.0.
- IF NOT (stdout:ex09_0:relation=different) AND stdout:ex09_0:relation=whitespace THEN cụm 2; train n=23, validation n=3, precision=1.0.
- IF stdout:ex09_0:relation=different THEN cụm 0; train n=43, validation n=13, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/295 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab02-ex10

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 18, 2: 2, 3: 3, 1: 1}.

- IF NOT (test:ex10_0=pass) THEN cụm 0; train n=19, validation n=7, precision=1.0.
- IF test:ex10_0=pass AND NOT (test:ex10_3=pass) THEN cụm 3; train n=3, validation n=2, precision=1.0.
- IF test:ex10_0=pass AND test:ex10_3=pass THEN cụm 2; train n=2, validation n=0, precision=None.

### agglomerative / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {2: 18, 0: 3, 1: 3}.

- IF NOT (test:ex10_0=pass) THEN cụm 2; train n=19, validation n=7, precision=1.0.
- IF test:ex10_0=pass AND NOT (test:ex10_3=pass) THEN cụm 1; train n=3, validation n=2, precision=1.0.
- IF test:ex10_0=pass AND test:ex10_3=pass THEN cụm 0; train n=2, validation n=0, precision=None.

### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {2: 18, 0: 3, 1: 3}.

- IF NOT (test:ex10_0=pass) AND NOT (ast:c_strict_comparison=1) THEN cụm 2; train n=11, validation n=2, precision=1.0.
- IF NOT (test:ex10_0=pass) AND ast:c_strict_comparison=1 AND NOT (ast:c_update=0) THEN cụm 2; train n=6, validation n=5, precision=1.0.
- IF NOT (test:ex10_0=pass) AND ast:c_strict_comparison=1 AND ast:c_update=0 THEN cụm 2; train n=2, validation n=0, precision=None.
- IF test:ex10_0=pass AND NOT (test:ex10_2=pass) THEN cụm 0; train n=2, validation n=0, precision=None.
- IF test:ex10_0=pass AND test:ex10_2=pass THEN cụm 1; train n=3, validation n=2, precision=1.0.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 18, 0: 3, 1: 3}.

- IF NOT (test:ex10_0=fail) AND NOT (test:ex10_3=pass) THEN cụm 1; train n=3, validation n=2, precision=1.0.
- IF NOT (test:ex10_0=fail) AND test:ex10_3=pass THEN cụm 0; train n=2, validation n=0, precision=None.
- IF test:ex10_0=fail AND NOT (stdout:ex10_3:edit_band=medium) AND NOT (stdout:ex10_1:edit_band=medium) THEN cụm 2; train n=2, validation n=5, precision=1.0.
- IF test:ex10_0=fail AND NOT (stdout:ex10_3:edit_band=medium) AND stdout:ex10_1:edit_band=medium THEN cụm 0; train n=2, validation n=0, precision=None.
- IF test:ex10_0=fail AND stdout:ex10_3:edit_band=medium THEN cụm 2; train n=15, validation n=2, precision=1.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 18, 2: 3, 1: 3}.

- IF NOT (test:ex10_0=fail) AND NOT (stdout:ex10_3:relation=__unknown__) THEN cụm 1; train n=3, validation n=2, precision=1.0.
- IF NOT (test:ex10_0=fail) AND stdout:ex10_3:relation=__unknown__ THEN cụm 2; train n=2, validation n=0, precision=None.
- IF test:ex10_0=fail AND NOT (stdout:ex10_3:edit_band=medium) AND NOT (stdout:ex10_2:edit_band=large) THEN cụm 0; train n=2, validation n=0, precision=None.
- IF test:ex10_0=fail AND NOT (stdout:ex10_3:edit_band=medium) AND stdout:ex10_2:edit_band=large THEN cụm 0; train n=2, validation n=5, precision=1.0.
- IF test:ex10_0=fail AND stdout:ex10_3:edit_band=medium THEN cụm 0; train n=15, validation n=2, precision=1.0.

### kmeans / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 18, 2: 3, 1: 3}.

- IF NOT (test:ex10_0=pass) THEN cụm 0; train n=19, validation n=7, precision=1.0.
- IF test:ex10_0=pass AND NOT (test:ex10_3=pass) THEN cụm 1; train n=3, validation n=2, precision=1.0.
- IF test:ex10_0=pass AND test:ex10_3=pass THEN cụm 2; train n=2, validation n=0, precision=None.

### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {1: 18, 0: 3, 2: 3}.

- IF NOT (test:ex10_0=pass) AND NOT (ast:c_strict_comparison=1) THEN cụm 1; train n=11, validation n=2, precision=1.0.
- IF NOT (test:ex10_0=pass) AND ast:c_strict_comparison=1 AND NOT (ast:c_update=0) THEN cụm 1; train n=6, validation n=5, precision=1.0.
- IF NOT (test:ex10_0=pass) AND ast:c_strict_comparison=1 AND ast:c_update=0 THEN cụm 1; train n=2, validation n=0, precision=None.
- IF test:ex10_0=pass AND NOT (test:ex10_2=pass) THEN cụm 0; train n=2, validation n=0, precision=None.
- IF test:ex10_0=pass AND test:ex10_2=pass THEN cụm 2; train n=3, validation n=2, precision=1.0.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 11, 0: 10, 1: 3}.

- IF NOT (stdout:ex10_2:relation=different) AND NOT (stdout:ex10_0:edit_band=medium) THEN cụm 1; train n=3, validation n=4, precision=0.5.
- IF NOT (stdout:ex10_2:relation=different) AND stdout:ex10_0:edit_band=medium THEN cụm 0; train n=10, validation n=1, precision=1.0.
- IF stdout:ex10_2:relation=different THEN cụm 2; train n=11, validation n=4, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 11, 0: 10, 1: 3}.

- IF NOT (stdout:ex10_1:relation=different) AND NOT (stdout:ex10_0:relation=__unknown__) THEN cụm 0; train n=10, validation n=3, precision=0.3333333333333333.
- IF NOT (stdout:ex10_1:relation=different) AND stdout:ex10_0:relation=__unknown__ THEN cụm 1; train n=3, validation n=2, precision=1.0.
- IF stdout:ex10_1:relation=different THEN cụm 2; train n=11, validation n=4, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/257 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab03-ex01

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 109, 1: 1}.

- IF TRUE THEN cụm 0; train n=110, validation n=26, precision=1.0.

### agglomerative / outcomes

Trạng thái: `abstained`; k_requires_more_training_rows_or_distinct_patterns

Quy mô cụm train: {}.


### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 108, 2: 1, 1: 1}.

- IF NOT (ast:c_for=0) THEN cụm 0; train n=105, validation n=16, precision=1.0.
- IF ast:c_for=0 AND NOT (ast:c_update=1) THEN cụm 0; train n=2, validation n=2, precision=0.0.
- IF ast:c_for=0 AND ast:c_update=1 THEN cụm 0; train n=3, validation n=8, precision=0.75.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 81, 0: 28, 1: 1}.

- IF NOT (stdout:ex01_1:relation=whitespace) AND NOT (stdout:ex01_0:relation=different) AND NOT (stdout:ex01_2:relation=different) THEN cụm 0; train n=4, validation n=0, precision=None.
- IF NOT (stdout:ex01_1:relation=whitespace) AND NOT (stdout:ex01_0:relation=different) AND stdout:ex01_2:relation=different THEN cụm 0; train n=2, validation n=0, precision=None.
- IF NOT (stdout:ex01_1:relation=whitespace) AND stdout:ex01_0:relation=different THEN cụm 0; train n=23, validation n=8, precision=1.0.
- IF stdout:ex01_1:relation=whitespace THEN cụm 2; train n=81, validation n=18, precision=1.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 81, 0: 28, 1: 1}.

- IF NOT (stdout:ex01_0:relation=whitespace) AND NOT (ast:c_for=1) THEN cụm 0; train n=3, validation n=4, precision=1.0.
- IF NOT (stdout:ex01_0:relation=whitespace) AND ast:c_for=1 THEN cụm 0; train n=26, validation n=4, precision=1.0.
- IF stdout:ex01_0:relation=whitespace THEN cụm 2; train n=81, validation n=18, precision=1.0.

### kmeans / outcomes

Trạng thái: `abstained`; k_requires_more_training_rows_or_distinct_patterns

Quy mô cụm train: {}.


### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 41, 2: 35, 1: 34}.

- IF NOT (ast:c_while=0) THEN cụm 1; train n=34, validation n=12, precision=1.0.
- IF ast:c_while=0 AND NOT (ast:c_if=1) THEN cụm 0; train n=41, validation n=4, precision=1.0.
- IF ast:c_while=0 AND ast:c_if=1 THEN cụm 2; train n=35, validation n=10, precision=1.0.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 73, 1: 29, 2: 8}.

- IF NOT (stdout:ex01_1:edit_band=small) AND NOT (stdout:ex01_0:relation=whitespace) THEN cụm 1; train n=28, validation n=8, precision=1.0.
- IF NOT (stdout:ex01_1:edit_band=small) AND stdout:ex01_0:relation=whitespace THEN cụm 2; train n=8, validation n=1, precision=0.0.
- IF stdout:ex01_1:edit_band=small AND NOT (stdout:ex01_0:edit_band=medium) THEN cụm 0; train n=70, validation n=15, precision=1.0.
- IF stdout:ex01_1:edit_band=small AND stdout:ex01_0:edit_band=medium THEN cụm 0; train n=4, validation n=2, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 73, 1: 29, 2: 8}.

- IF NOT (stdout:ex01_1:edit_band=small) AND NOT (stdout:ex01_1:relation=whitespace) THEN cụm 1; train n=28, validation n=8, precision=1.0.
- IF NOT (stdout:ex01_1:edit_band=small) AND stdout:ex01_1:relation=whitespace THEN cụm 2; train n=8, validation n=1, precision=0.0.
- IF stdout:ex01_1:edit_band=small AND NOT (ast:c_if=1) AND NOT (ast:c_while=0) THEN cụm 0; train n=13, validation n=4, precision=1.0.
- IF stdout:ex01_1:edit_band=small AND NOT (ast:c_if=1) AND ast:c_while=0 THEN cụm 0; train n=34, validation n=4, precision=1.0.
- IF stdout:ex01_1:edit_band=small AND ast:c_if=1 THEN cụm 0; train n=27, validation n=9, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/430 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab03-ex02

### exact / outcomes

Trạng thái: `abstained`; identical_training_features

Quy mô cụm train: {}.


### agglomerative / outcomes

Trạng thái: `abstained`; identical_training_features

Quy mô cụm train: {}.


### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {2: 4, 0: 167, 1: 4}.

- IF NOT (ast:c_inclusive_comparison=0) THEN cụm 0; train n=164, validation n=20, precision=0.95.
- IF ast:c_inclusive_comparison=0 AND NOT (ast:c_for=1) THEN cụm 1; train n=4, validation n=1, precision=1.0.
- IF ast:c_inclusive_comparison=0 AND ast:c_for=1 AND NOT (ast:c_if=1) THEN cụm 2; train n=4, validation n=0, precision=None.
- IF ast:c_inclusive_comparison=0 AND ast:c_for=1 AND ast:c_if=1 THEN cụm 0; train n=3, validation n=3, precision=1.0.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 122, 0: 52, 1: 1}.

- IF NOT (stdout:ex02_1:relation=whitespace) AND NOT (stdout:ex02_0:relation=different) AND NOT (stdout:ex02_2:edit_band=medium) THEN cụm 0; train n=3, validation n=1, precision=0.0.
- IF NOT (stdout:ex02_1:relation=whitespace) AND NOT (stdout:ex02_0:relation=different) AND stdout:ex02_2:edit_band=medium THEN cụm 0; train n=7, validation n=0, precision=None.
- IF NOT (stdout:ex02_1:relation=whitespace) AND stdout:ex02_0:relation=different THEN cụm 0; train n=43, validation n=7, precision=1.0.
- IF stdout:ex02_1:relation=whitespace THEN cụm 2; train n=122, validation n=16, precision=1.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 122, 0: 52, 1: 1}.

- IF NOT (stdout:ex02_1:relation=whitespace) AND NOT (ast:c_inclusive_comparison=1) AND NOT (stdout:ex02_2:edit_band=large) THEN cụm 0; train n=4, validation n=0, precision=None.
- IF NOT (stdout:ex02_1:relation=whitespace) AND NOT (ast:c_inclusive_comparison=1) AND stdout:ex02_2:edit_band=large THEN cụm 0; train n=3, validation n=1, precision=0.0.
- IF NOT (stdout:ex02_1:relation=whitespace) AND ast:c_inclusive_comparison=1 THEN cụm 0; train n=46, validation n=7, precision=1.0.
- IF stdout:ex02_1:relation=whitespace THEN cụm 2; train n=122, validation n=16, precision=1.0.

### kmeans / outcomes

Trạng thái: `abstained`; identical_training_features

Quy mô cụm train: {}.


### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {1: 48, 0: 98, 2: 29}.

- IF NOT (ast:c_if=0) AND NOT (ast:c_for=1) THEN cụm 2; train n=26, validation n=0, precision=None.
- IF NOT (ast:c_if=0) AND ast:c_for=1 THEN cụm 0; train n=98, validation n=15, precision=1.0.
- IF ast:c_if=0 AND NOT (ast:c_for=1) THEN cụm 2; train n=3, validation n=2, precision=0.5.
- IF ast:c_if=0 AND ast:c_for=1 THEN cụm 1; train n=48, validation n=7, precision=1.0.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 88, 2: 44, 0: 43}.

- IF NOT (stdout:ex02_1:edit_band=small) AND NOT (stdout:ex02_0:relation=whitespace) THEN cụm 2; train n=37, validation n=6, precision=1.0.
- IF NOT (stdout:ex02_1:edit_band=small) AND stdout:ex02_0:relation=whitespace THEN cụm 0; train n=41, validation n=5, precision=1.0.
- IF stdout:ex02_1:edit_band=small AND NOT (stdout:ex02_0:relation=different) AND NOT (stdout:ex02_2:edit_band=medium) THEN cụm 1; train n=87, validation n=11, precision=1.0.
- IF stdout:ex02_1:edit_band=small AND NOT (stdout:ex02_0:relation=different) AND stdout:ex02_2:edit_band=medium THEN cụm 0; train n=3, validation n=0, precision=None.
- IF stdout:ex02_1:edit_band=small AND stdout:ex02_0:relation=different THEN cụm 2; train n=7, validation n=2, precision=0.5.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 88, 1: 51, 2: 36}.

- IF NOT (stdout:ex02_1:relation=whitespace) AND NOT (stdout:ex02_2:edit_band=small) THEN cụm 1; train n=45, validation n=6, precision=1.0.
- IF NOT (stdout:ex02_1:relation=whitespace) AND stdout:ex02_2:edit_band=small AND NOT (ast:c_for=1) THEN cụm 0; train n=2, validation n=0, precision=None.
- IF NOT (stdout:ex02_1:relation=whitespace) AND stdout:ex02_2:edit_band=small AND ast:c_for=1 THEN cụm 1; train n=6, validation n=2, precision=0.5.
- IF stdout:ex02_1:relation=whitespace AND NOT (stdout:ex02_1:edit_band=small) THEN cụm 2; train n=34, validation n=5, precision=1.0.
- IF stdout:ex02_1:relation=whitespace AND stdout:ex02_1:edit_band=small AND NOT (stdout:ex02_2:edit_band=medium) THEN cụm 0; train n=85, validation n=11, precision=1.0.
- IF stdout:ex02_1:relation=whitespace AND stdout:ex02_1:edit_band=small AND stdout:ex02_2:edit_band=medium THEN cụm 2; train n=3, validation n=0, precision=None.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/448 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab03-ex03

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 92, 1: 1}.

- IF TRUE THEN cụm 0; train n=93, validation n=34, precision=0.9705882352941176.

### agglomerative / outcomes

Trạng thái: `abstained`; k_requires_more_training_rows_or_distinct_patterns

Quy mô cụm train: {}.


### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {2: 87, 0: 5, 1: 1}.

- IF NOT (ast:c_update=1) THEN cụm 0; train n=4, validation n=3, precision=1.0.
- IF ast:c_update=1 AND NOT (ast:c_for=0) AND NOT (ast:c_strict_comparison=1) THEN cụm 2; train n=47, validation n=10, precision=1.0.
- IF ast:c_update=1 AND NOT (ast:c_for=0) AND ast:c_strict_comparison=1 THEN cụm 2; train n=38, validation n=17, precision=0.9411764705882353.
- IF ast:c_update=1 AND ast:c_for=0 THEN cụm 2; train n=4, validation n=4, precision=0.0.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 50, 1: 40, 2: 3}.

- IF NOT (stdout:ex03_2:relation=whitespace) AND NOT (stdout:ex03_0:relation=empty) THEN cụm 1; train n=40, validation n=16, precision=0.9375.
- IF NOT (stdout:ex03_2:relation=whitespace) AND stdout:ex03_0:relation=empty THEN cụm 2; train n=3, validation n=1, precision=1.0.
- IF stdout:ex03_2:relation=whitespace THEN cụm 0; train n=50, validation n=17, precision=1.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 50, 1: 40, 2: 3}.

- IF NOT (stdout:ex03_1:relation=whitespace) AND NOT (stdout:ex03_2:relation=different) THEN cụm 2; train n=3, validation n=1, precision=1.0.
- IF NOT (stdout:ex03_1:relation=whitespace) AND stdout:ex03_2:relation=different THEN cụm 1; train n=40, validation n=16, precision=1.0.
- IF stdout:ex03_1:relation=whitespace THEN cụm 0; train n=50, validation n=17, precision=1.0.

### kmeans / outcomes

Trạng thái: `abstained`; k_requires_more_training_rows_or_distinct_patterns

Quy mô cụm train: {}.


### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {2: 33, 1: 47, 0: 13}.

- IF NOT (ast:c_strict_comparison=1) AND NOT (ast:c_for=0) THEN cụm 1; train n=47, validation n=10, precision=1.0.
- IF NOT (ast:c_strict_comparison=1) AND ast:c_for=0 THEN cụm 0; train n=5, validation n=7, precision=1.0.
- IF ast:c_strict_comparison=1 AND NOT (ast:c_while=1) THEN cụm 2; train n=33, validation n=15, precision=0.6666666666666666.
- IF ast:c_strict_comparison=1 AND ast:c_while=1 THEN cụm 0; train n=8, validation n=2, precision=1.0.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 49, 0: 37, 2: 7}.

- IF NOT (stdout:ex03_2:relation=whitespace) AND NOT (stdout:ex03_1:edit_band=large) THEN cụm 0; train n=37, validation n=15, precision=1.0.
- IF NOT (stdout:ex03_2:relation=whitespace) AND stdout:ex03_1:edit_band=large THEN cụm 2; train n=6, validation n=2, precision=1.0.
- IF stdout:ex03_2:relation=whitespace AND NOT (stdout:ex03_3:edit_band=small) THEN cụm 1; train n=2, validation n=0, precision=None.
- IF stdout:ex03_2:relation=whitespace AND stdout:ex03_3:edit_band=small THEN cụm 1; train n=48, validation n=17, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 49, 0: 37, 2: 7}.

- IF NOT (stdout:ex03_1:relation=whitespace) AND NOT (stdout:ex03_0:edit_band=large) THEN cụm 0; train n=37, validation n=15, precision=1.0.
- IF NOT (stdout:ex03_1:relation=whitespace) AND stdout:ex03_0:edit_band=large THEN cụm 2; train n=6, validation n=2, precision=1.0.
- IF stdout:ex03_1:relation=whitespace AND NOT (stdout:ex03_0:edit_band=small) THEN cụm 1; train n=2, validation n=2, precision=1.0.
- IF stdout:ex03_1:relation=whitespace AND stdout:ex03_0:edit_band=small THEN cụm 1; train n=48, validation n=15, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/343 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab03-ex04

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {21: 1, 26: 85, 10: 3, 3: 2, 17: 2, 0: 95, 15: 3, 29: 1, 16: 1, 11: 7, 27: 1, 2: 2, 31: 11, 12: 3, 18: 11, 28: 4, 4: 3, 19: 9, 5: 1, 22: 2, 7: 1, 13: 2, 24: 1, 23: 1, 25: 1, 8: 3, 1: 1, 9: 2, 30: 3, 20: 2, 14: 1, 6: 1}.

- IF NOT (test:ex04_0=pass) AND NOT (test:ex04_1=pass) AND NOT (test:ex04_2=pass) THEN cụm 0; train n=96, validation n=36, precision=1.0.
- IF NOT (test:ex04_0=pass) AND NOT (test:ex04_1=pass) AND test:ex04_2=pass THEN cụm 2; train n=4, validation n=0, precision=None.
- IF NOT (test:ex04_0=pass) AND test:ex04_1=pass AND NOT (test:ex04_7=fail) THEN cụm 8; train n=4, validation n=3, precision=0.6666666666666666.
- IF NOT (test:ex04_0=pass) AND test:ex04_1=pass AND test:ex04_7=fail THEN cụm 4; train n=7, validation n=0, precision=None.
- IF test:ex04_0=pass AND NOT (test:ex04_4=fail) AND NOT (test:ex04_3=pass) THEN cụm 26; train n=95, validation n=20, precision=0.85.
- IF test:ex04_0=pass AND NOT (test:ex04_4=fail) AND test:ex04_3=pass THEN cụm 31; train n=14, validation n=6, precision=0.16666666666666666.
- IF test:ex04_0=pass AND test:ex04_4=fail AND NOT (test:ex04_3=fail) THEN cụm 18; train n=16, validation n=8, precision=0.75.
- IF test:ex04_0=pass AND test:ex04_4=fail AND test:ex04_3=fail THEN cụm 19; train n=30, validation n=6, precision=0.6666666666666666.

### agglomerative / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 113, 1: 120, 2: 33}.

- IF NOT (test:ex04_1=pass) AND NOT (test:ex04_8=pass) THEN cụm 1; train n=114, validation n=38, precision=1.0.
- IF NOT (test:ex04_1=pass) AND test:ex04_8=pass THEN cụm 0; train n=2, validation n=0, precision=None.
- IF test:ex04_1=pass AND NOT (test:ex04_5=pass) AND NOT (test:ex04_7=pass) THEN cụm 1; train n=4, validation n=0, precision=None.
- IF test:ex04_1=pass AND NOT (test:ex04_5=pass) AND test:ex04_7=pass THEN cụm 2; train n=33, validation n=16, precision=1.0.
- IF test:ex04_1=pass AND test:ex04_5=pass AND NOT (test:ex04_0=fail) THEN cụm 0; train n=110, validation n=25, precision=1.0.
- IF test:ex04_1=pass AND test:ex04_5=pass AND test:ex04_0=fail THEN cụm 0; train n=3, validation n=0, precision=None.

### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 113, 1: 120, 2: 33}.

- IF NOT (test:ex04_1=fail) AND NOT (test:ex04_5=pass) AND NOT (test:ex04_7=fail) THEN cụm 2; train n=33, validation n=16, precision=1.0.
- IF NOT (test:ex04_1=fail) AND NOT (test:ex04_5=pass) AND test:ex04_7=fail THEN cụm 1; train n=4, validation n=0, precision=None.
- IF NOT (test:ex04_1=fail) AND test:ex04_5=pass AND NOT (test:ex04_0=fail) THEN cụm 0; train n=110, validation n=25, precision=1.0.
- IF NOT (test:ex04_1=fail) AND test:ex04_5=pass AND test:ex04_0=fail THEN cụm 0; train n=3, validation n=0, precision=None.
- IF test:ex04_1=fail AND NOT (test:ex04_8=fail) THEN cụm 0; train n=2, validation n=0, precision=None.
- IF test:ex04_1=fail AND test:ex04_8=fail THEN cụm 1; train n=114, validation n=38, precision=0.9473684210526315.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 113, 0: 120, 2: 33}.

- IF NOT (stdout:ex04_1:edit_band=__unknown__) AND NOT (stdout:ex04_8:relation=__unknown__) THEN cụm 0; train n=114, validation n=38, precision=1.0.
- IF NOT (stdout:ex04_1:edit_band=__unknown__) AND stdout:ex04_8:relation=__unknown__ THEN cụm 0; train n=2, validation n=0, precision=None.
- IF stdout:ex04_1:edit_band=__unknown__ AND NOT (stdout:ex04_5:relation=__unknown__) AND NOT (stdout:ex04_7:relation=different) THEN cụm 2; train n=33, validation n=16, precision=1.0.
- IF stdout:ex04_1:edit_band=__unknown__ AND NOT (stdout:ex04_5:relation=__unknown__) AND stdout:ex04_7:relation=different THEN cụm 0; train n=4, validation n=0, precision=None.
- IF stdout:ex04_1:edit_band=__unknown__ AND stdout:ex04_5:relation=__unknown__ AND NOT (stdout:ex04_4:edit_band=small) THEN cụm 1; train n=111, validation n=24, precision=1.0.
- IF stdout:ex04_1:edit_band=__unknown__ AND stdout:ex04_5:relation=__unknown__ AND stdout:ex04_4:edit_band=small THEN cụm 0; train n=2, validation n=1, precision=0.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 113, 0: 120, 2: 33}.

- IF NOT (test:ex04_1=fail) AND NOT (test:ex04_5=pass) AND NOT (stdout:ex04_7:edit_band=large) THEN cụm 2; train n=33, validation n=16, precision=1.0.
- IF NOT (test:ex04_1=fail) AND NOT (test:ex04_5=pass) AND stdout:ex04_7:edit_band=large THEN cụm 0; train n=4, validation n=0, precision=None.
- IF NOT (test:ex04_1=fail) AND test:ex04_5=pass AND NOT (stdout:ex04_4:edit_band=small) THEN cụm 1; train n=111, validation n=24, precision=1.0.
- IF NOT (test:ex04_1=fail) AND test:ex04_5=pass AND stdout:ex04_4:edit_band=small THEN cụm 0; train n=2, validation n=1, precision=0.0.
- IF test:ex04_1=fail AND NOT (stdout:ex04_8:edit_band=__unknown__) THEN cụm 0; train n=114, validation n=38, precision=0.9473684210526315.
- IF test:ex04_1=fail AND stdout:ex04_8:edit_band=__unknown__ THEN cụm 0; train n=2, validation n=0, precision=None.

### kmeans / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 113, 1: 120, 2: 33}.

- IF NOT (test:ex04_1=pass) AND NOT (test:ex04_8=pass) THEN cụm 1; train n=114, validation n=38, precision=1.0.
- IF NOT (test:ex04_1=pass) AND test:ex04_8=pass THEN cụm 0; train n=2, validation n=0, precision=None.
- IF test:ex04_1=pass AND NOT (test:ex04_5=pass) AND NOT (test:ex04_7=pass) THEN cụm 1; train n=4, validation n=0, precision=None.
- IF test:ex04_1=pass AND NOT (test:ex04_5=pass) AND test:ex04_7=pass THEN cụm 2; train n=33, validation n=16, precision=1.0.
- IF test:ex04_1=pass AND test:ex04_5=pass AND NOT (test:ex04_0=fail) THEN cụm 0; train n=110, validation n=25, precision=1.0.
- IF test:ex04_1=pass AND test:ex04_5=pass AND test:ex04_0=fail THEN cụm 0; train n=3, validation n=0, precision=None.

### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 113, 1: 120, 2: 33}.

- IF NOT (test:ex04_1=fail) AND NOT (test:ex04_5=pass) AND NOT (test:ex04_7=fail) THEN cụm 2; train n=33, validation n=16, precision=1.0.
- IF NOT (test:ex04_1=fail) AND NOT (test:ex04_5=pass) AND test:ex04_7=fail THEN cụm 1; train n=4, validation n=0, precision=None.
- IF NOT (test:ex04_1=fail) AND test:ex04_5=pass AND NOT (test:ex04_0=fail) THEN cụm 0; train n=110, validation n=25, precision=1.0.
- IF NOT (test:ex04_1=fail) AND test:ex04_5=pass AND test:ex04_0=fail THEN cụm 0; train n=3, validation n=0, precision=None.
- IF test:ex04_1=fail AND NOT (test:ex04_8=fail) THEN cụm 0; train n=2, validation n=0, precision=None.
- IF test:ex04_1=fail AND test:ex04_8=fail THEN cụm 1; train n=114, validation n=38, precision=0.9473684210526315.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 113, 1: 120, 2: 33}.

- IF NOT (stdout:ex04_1:edit_band=__unknown__) AND NOT (stdout:ex04_8:relation=__unknown__) THEN cụm 1; train n=114, validation n=38, precision=1.0.
- IF NOT (stdout:ex04_1:edit_band=__unknown__) AND stdout:ex04_8:relation=__unknown__ THEN cụm 0; train n=2, validation n=0, precision=None.
- IF stdout:ex04_1:edit_band=__unknown__ AND NOT (stdout:ex04_5:relation=__unknown__) AND NOT (stdout:ex04_7:relation=different) THEN cụm 2; train n=33, validation n=16, precision=1.0.
- IF stdout:ex04_1:edit_band=__unknown__ AND NOT (stdout:ex04_5:relation=__unknown__) AND stdout:ex04_7:relation=different THEN cụm 1; train n=4, validation n=0, precision=None.
- IF stdout:ex04_1:edit_band=__unknown__ AND stdout:ex04_5:relation=__unknown__ AND NOT (stdout:ex04_4:edit_band=small) THEN cụm 0; train n=111, validation n=24, precision=1.0.
- IF stdout:ex04_1:edit_band=__unknown__ AND stdout:ex04_5:relation=__unknown__ AND stdout:ex04_4:edit_band=small THEN cụm 0; train n=2, validation n=1, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 113, 2: 120, 0: 33}.

- IF NOT (test:ex04_1=fail) AND NOT (test:ex04_5=pass) AND NOT (stdout:ex04_7:edit_band=large) THEN cụm 0; train n=33, validation n=16, precision=1.0.
- IF NOT (test:ex04_1=fail) AND NOT (test:ex04_5=pass) AND stdout:ex04_7:edit_band=large THEN cụm 2; train n=4, validation n=0, precision=None.
- IF NOT (test:ex04_1=fail) AND test:ex04_5=pass AND NOT (stdout:ex04_4:edit_band=small) THEN cụm 1; train n=111, validation n=24, precision=1.0.
- IF NOT (test:ex04_1=fail) AND test:ex04_5=pass AND stdout:ex04_4:edit_band=small THEN cụm 1; train n=2, validation n=1, precision=1.0.
- IF test:ex04_1=fail AND NOT (stdout:ex04_8:edit_band=__unknown__) THEN cụm 2; train n=114, validation n=38, precision=0.9473684210526315.
- IF test:ex04_1=fail AND stdout:ex04_8:edit_band=__unknown__ THEN cụm 1; train n=2, validation n=0, precision=None.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/550 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab03-ex05

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 65, 1: 8, 2: 34}.

- IF NOT (test:ex05_1=fail) AND NOT (test:ex05_2=fail) THEN cụm 2; train n=34, validation n=2, precision=1.0.
- IF NOT (test:ex05_1=fail) AND test:ex05_2=fail THEN cụm 1; train n=8, validation n=1, precision=1.0.
- IF test:ex05_1=fail THEN cụm 0; train n=65, validation n=7, precision=1.0.

### agglomerative / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 65, 2: 8, 1: 34}.

- IF NOT (test:ex05_1=fail) AND NOT (test:ex05_2=fail) THEN cụm 1; train n=34, validation n=2, precision=1.0.
- IF NOT (test:ex05_1=fail) AND test:ex05_2=fail THEN cụm 2; train n=8, validation n=1, precision=1.0.
- IF test:ex05_1=fail THEN cụm 0; train n=65, validation n=7, precision=1.0.

### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {1: 65, 0: 8, 2: 34}.

- IF NOT (test:ex05_1=fail) AND NOT (test:ex05_2=pass) THEN cụm 0; train n=8, validation n=1, precision=1.0.
- IF NOT (test:ex05_1=fail) AND test:ex05_2=pass THEN cụm 2; train n=34, validation n=2, precision=1.0.
- IF test:ex05_1=fail THEN cụm 1; train n=65, validation n=7, precision=1.0.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 52, 0: 42, 1: 13}.

- IF NOT (stdout:ex05_0:relation=whitespace) AND NOT (test:ex05_1=pass) THEN cụm 1; train n=13, validation n=4, precision=1.0.
- IF NOT (stdout:ex05_0:relation=whitespace) AND test:ex05_1=pass THEN cụm 0; train n=42, validation n=3, precision=1.0.
- IF stdout:ex05_0:relation=whitespace THEN cụm 2; train n=52, validation n=3, precision=0.6666666666666666.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 52, 1: 42, 0: 13}.

- IF NOT (stdout:ex05_1:edit_band=small) AND NOT (stdout:ex05_1:relation=__unknown__) THEN cụm 0; train n=13, validation n=5, precision=1.0.
- IF NOT (stdout:ex05_1:edit_band=small) AND stdout:ex05_1:relation=__unknown__ THEN cụm 1; train n=42, validation n=3, precision=1.0.
- IF stdout:ex05_1:edit_band=small THEN cụm 2; train n=52, validation n=2, precision=1.0.

### kmeans / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 65, 2: 8, 1: 34}.

- IF NOT (test:ex05_1=fail) AND NOT (test:ex05_2=fail) THEN cụm 1; train n=34, validation n=2, precision=1.0.
- IF NOT (test:ex05_1=fail) AND test:ex05_2=fail THEN cụm 2; train n=8, validation n=1, precision=1.0.
- IF test:ex05_1=fail THEN cụm 0; train n=65, validation n=7, precision=1.0.

### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 65, 2: 8, 1: 34}.

- IF NOT (test:ex05_1=fail) AND NOT (test:ex05_2=pass) THEN cụm 2; train n=8, validation n=1, precision=1.0.
- IF NOT (test:ex05_1=fail) AND test:ex05_2=pass THEN cụm 1; train n=34, validation n=2, precision=1.0.
- IF test:ex05_1=fail THEN cụm 0; train n=65, validation n=7, precision=1.0.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 52, 1: 42, 2: 13}.

- IF NOT (stdout:ex05_0:relation=whitespace) AND NOT (test:ex05_1=pass) THEN cụm 2; train n=13, validation n=4, precision=1.0.
- IF NOT (stdout:ex05_0:relation=whitespace) AND test:ex05_1=pass THEN cụm 1; train n=42, validation n=3, precision=1.0.
- IF stdout:ex05_0:relation=whitespace THEN cụm 0; train n=52, validation n=3, precision=0.6666666666666666.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 52, 1: 42, 2: 13}.

- IF NOT (stdout:ex05_1:edit_band=small) AND NOT (stdout:ex05_1:relation=__unknown__) THEN cụm 2; train n=13, validation n=5, precision=1.0.
- IF NOT (stdout:ex05_1:edit_band=small) AND stdout:ex05_1:relation=__unknown__ THEN cụm 1; train n=42, validation n=3, precision=1.0.
- IF stdout:ex05_1:edit_band=small THEN cụm 0; train n=52, validation n=2, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/287 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab03-ex06

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 30, 7: 1, 4: 1, 6: 4, 1: 2, 5: 1, 8: 12, 2: 1, 3: 1}.

- IF NOT (test:ex06_4=pass) AND NOT (test:ex06_0=fail) THEN cụm 4; train n=2, validation n=0, precision=None.
- IF NOT (test:ex06_4=pass) AND test:ex06_0=fail THEN cụm 0; train n=31, validation n=4, precision=0.75.
- IF test:ex06_4=pass AND NOT (test:ex06_3=fail) THEN cụm 8; train n=13, validation n=4, precision=1.0.
- IF test:ex06_4=pass AND test:ex06_3=fail AND NOT (test:ex06_1=fail) THEN cụm 6; train n=5, validation n=6, precision=0.5.
- IF test:ex06_4=pass AND test:ex06_3=fail AND test:ex06_1=fail THEN cụm 1; train n=2, validation n=0, precision=None.

### agglomerative / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {1: 34, 0: 18, 2: 1}.

- IF NOT (test:ex06_1=pass) AND NOT (test:ex06_5=pass) THEN cụm 1; train n=32, validation n=3, precision=1.0.
- IF NOT (test:ex06_1=pass) AND test:ex06_5=pass THEN cụm 1; train n=2, validation n=0, precision=None.
- IF test:ex06_1=pass AND NOT (test:ex06_5=pass) THEN cụm 0; train n=2, validation n=4, precision=0.5.
- IF test:ex06_1=pass AND test:ex06_5=pass THEN cụm 0; train n=17, validation n=7, precision=1.0.

### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {1: 34, 0: 18, 2: 1}.

- IF NOT (test:ex06_1=fail) AND NOT (test:ex06_5=pass) THEN cụm 0; train n=2, validation n=4, precision=0.5.
- IF NOT (test:ex06_1=fail) AND test:ex06_5=pass THEN cụm 0; train n=17, validation n=7, precision=1.0.
- IF test:ex06_1=fail AND NOT (ast:c_inclusive_comparison=1) THEN cụm 1; train n=16, validation n=3, precision=1.0.
- IF test:ex06_1=fail AND ast:c_inclusive_comparison=1 AND NOT (ast:c_strict_comparison=1) THEN cụm 1; train n=13, validation n=0, precision=None.
- IF test:ex06_1=fail AND ast:c_inclusive_comparison=1 AND ast:c_strict_comparison=1 THEN cụm 1; train n=5, validation n=0, precision=None.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 34, 1: 18, 2: 1}.

- IF NOT (stdout:ex06_1:edit_band=__unknown__) AND NOT (stdout:ex06_0:relation=different) THEN cụm 0; train n=26, validation n=3, precision=1.0.
- IF NOT (stdout:ex06_1:edit_band=__unknown__) AND stdout:ex06_0:relation=different AND NOT (stdout:ex06_6:relation=different) THEN cụm 0; train n=2, validation n=0, precision=None.
- IF NOT (stdout:ex06_1:edit_band=__unknown__) AND stdout:ex06_0:relation=different AND stdout:ex06_6:relation=different THEN cụm 0; train n=6, validation n=0, precision=None.
- IF stdout:ex06_1:edit_band=__unknown__ AND NOT (stdout:ex06_5:edit_band=__unknown__) THEN cụm 0; train n=2, validation n=4, precision=0.0.
- IF stdout:ex06_1:edit_band=__unknown__ AND stdout:ex06_5:edit_band=__unknown__ THEN cụm 1; train n=17, validation n=7, precision=1.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 32, 0: 20, 2: 1}.

- IF NOT (stdout:ex06_4:relation=__unknown__) AND NOT (stdout:ex06_0:relation=different) THEN cụm 1; train n=25, validation n=3, precision=1.0.
- IF NOT (stdout:ex06_4:relation=__unknown__) AND stdout:ex06_0:relation=different AND NOT (ast:c_inclusive_comparison=1) THEN cụm 1; train n=6, validation n=1, precision=0.0.
- IF NOT (stdout:ex06_4:relation=__unknown__) AND stdout:ex06_0:relation=different AND ast:c_inclusive_comparison=1 THEN cụm 1; train n=2, validation n=0, precision=None.
- IF stdout:ex06_4:relation=__unknown__ THEN cụm 0; train n=20, validation n=10, precision=0.9.

### kmeans / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 33, 2: 7, 1: 13}.

- IF NOT (test:ex06_4=pass) THEN cụm 0; train n=33, validation n=4, precision=1.0.
- IF test:ex06_4=pass AND NOT (test:ex06_2=fail) THEN cụm 1; train n=13, validation n=7, precision=0.8571428571428571.
- IF test:ex06_4=pass AND test:ex06_2=fail THEN cụm 2; train n=7, validation n=3, precision=1.0.

### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 34, 2: 6, 1: 13}.

- IF NOT (test:ex06_1=fail) AND NOT (test:ex06_2=fail) THEN cụm 1; train n=13, validation n=8, precision=0.875.
- IF NOT (test:ex06_1=fail) AND test:ex06_2=fail THEN cụm 2; train n=6, validation n=3, precision=1.0.
- IF test:ex06_1=fail THEN cụm 0; train n=34, validation n=3, precision=1.0.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 15, 1: 18, 2: 20}.

- IF NOT (stdout:ex06_0:edit_band=medium) AND NOT (stdout:ex06_1:relation=__unknown__) THEN cụm 0; train n=14, validation n=1, precision=1.0.
- IF NOT (stdout:ex06_0:edit_band=medium) AND stdout:ex06_1:relation=__unknown__ AND NOT (stdout:ex06_5:edit_band=__unknown__) THEN cụm 0; train n=2, validation n=4, precision=0.0.
- IF NOT (stdout:ex06_0:edit_band=medium) AND stdout:ex06_1:relation=__unknown__ AND stdout:ex06_5:edit_band=__unknown__ THEN cụm 1; train n=17, validation n=7, precision=1.0.
- IF stdout:ex06_0:edit_band=medium THEN cụm 2; train n=20, validation n=2, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 15, 1: 18, 2: 20}.

- IF NOT (stdout:ex06_0:edit_band=medium) AND NOT (test:ex06_1=fail) AND NOT (stdout:ex06_6:relation=other_oracle) THEN cụm 1; train n=17, validation n=11, precision=1.0.
- IF NOT (stdout:ex06_0:edit_band=medium) AND NOT (test:ex06_1=fail) AND stdout:ex06_6:relation=other_oracle THEN cụm 0; train n=2, validation n=0, precision=None.
- IF NOT (stdout:ex06_0:edit_band=medium) AND test:ex06_1=fail THEN cụm 0; train n=14, validation n=1, precision=1.0.
- IF stdout:ex06_0:edit_band=medium THEN cụm 2; train n=20, validation n=2, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

19/268 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

- Sai khác trình bày output; chưa có bằng chứng về lỗi khái niệm từ sai khác này (19 bài); cần người đánh giá.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab03-ex07

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 38, 1: 2, 2: 8}.

- IF NOT (test:ex07_0=pass) THEN cụm 0; train n=38, validation n=5, precision=1.0.
- IF test:ex07_0=pass AND NOT (test:ex07_3=pass) THEN cụm 2; train n=8, validation n=0, precision=None.
- IF test:ex07_0=pass AND test:ex07_3=pass THEN cụm 1; train n=2, validation n=0, precision=None.

### agglomerative / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {1: 38, 2: 2, 0: 8}.

- IF NOT (test:ex07_0=pass) THEN cụm 1; train n=38, validation n=5, precision=1.0.
- IF test:ex07_0=pass AND NOT (test:ex07_3=pass) THEN cụm 0; train n=8, validation n=0, precision=None.
- IF test:ex07_0=pass AND test:ex07_3=pass THEN cụm 2; train n=2, validation n=0, precision=None.

### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 38, 2: 2, 1: 8}.

- IF NOT (test:ex07_0=fail) AND NOT (test:ex07_1=pass) THEN cụm 2; train n=2, validation n=0, precision=None.
- IF NOT (test:ex07_0=fail) AND test:ex07_1=pass THEN cụm 1; train n=8, validation n=0, precision=None.
- IF test:ex07_0=fail THEN cụm 0; train n=38, validation n=5, precision=1.0.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 38, 2: 2, 1: 8}.

- IF NOT (stdout:ex07_0:edit_band=__unknown__) THEN cụm 0; train n=38, validation n=5, precision=1.0.
- IF stdout:ex07_0:edit_band=__unknown__ AND NOT (test:ex07_3=pass) THEN cụm 1; train n=8, validation n=0, precision=None.
- IF stdout:ex07_0:edit_band=__unknown__ AND test:ex07_3=pass THEN cụm 2; train n=2, validation n=0, precision=None.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 38, 2: 2, 1: 8}.

- IF NOT (stdout:ex07_0:relation=__unknown__) THEN cụm 0; train n=38, validation n=5, precision=1.0.
- IF stdout:ex07_0:relation=__unknown__ AND NOT (stdout:ex07_1:edit_band=__unknown__) THEN cụm 2; train n=2, validation n=0, precision=None.
- IF stdout:ex07_0:relation=__unknown__ AND stdout:ex07_1:edit_band=__unknown__ THEN cụm 1; train n=8, validation n=0, precision=None.

### kmeans / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 38, 2: 2, 1: 8}.

- IF NOT (test:ex07_0=pass) THEN cụm 0; train n=38, validation n=5, precision=1.0.
- IF test:ex07_0=pass AND NOT (test:ex07_3=pass) THEN cụm 1; train n=8, validation n=0, precision=None.
- IF test:ex07_0=pass AND test:ex07_3=pass THEN cụm 2; train n=2, validation n=0, precision=None.

### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 38, 2: 2, 1: 8}.

- IF NOT (test:ex07_0=fail) AND NOT (test:ex07_1=pass) THEN cụm 2; train n=2, validation n=0, precision=None.
- IF NOT (test:ex07_0=fail) AND test:ex07_1=pass THEN cụm 1; train n=8, validation n=0, precision=None.
- IF test:ex07_0=fail THEN cụm 0; train n=38, validation n=5, precision=1.0.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 13, 2: 10, 0: 25}.

- IF NOT (stdout:ex07_0:relation=different) AND NOT (stdout:ex07_3:edit_band=medium) THEN cụm 2; train n=10, validation n=1, precision=0.0.
- IF NOT (stdout:ex07_0:relation=different) AND stdout:ex07_3:edit_band=medium THEN cụm 1; train n=13, validation n=2, precision=1.0.
- IF stdout:ex07_0:relation=different THEN cụm 0; train n=25, validation n=2, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 13, 2: 10, 0: 25}.

- IF NOT (stdout:ex07_0:relation=different) AND NOT (test:ex07_0=fail) THEN cụm 2; train n=10, validation n=0, precision=None.
- IF NOT (stdout:ex07_0:relation=different) AND test:ex07_0=fail THEN cụm 1; train n=13, validation n=3, precision=0.6666666666666666.
- IF stdout:ex07_0:relation=different THEN cụm 0; train n=25, validation n=2, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/242 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab04-ex01

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 11, 1: 1}.

- IF TRUE THEN cụm 0; train n=12, validation n=4, precision=1.0.

### agglomerative / outcomes

Trạng thái: `abstained`; k_requires_more_training_rows_or_distinct_patterns

Quy mô cụm train: {}.


### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {2: 5, 0: 6, 1: 1}.

- IF NOT (ast:c_inclusive_comparison=0) AND NOT (ast:c_subscript=1) THEN cụm 2; train n=2, validation n=0, precision=None.
- IF NOT (ast:c_inclusive_comparison=0) AND ast:c_subscript=1 THEN cụm 2; train n=5, validation n=2, precision=1.0.
- IF ast:c_inclusive_comparison=0 THEN cụm 0; train n=5, validation n=2, precision=1.0.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 8, 0: 3, 1: 1}.

- IF NOT (stdout:ex01_0:relation=different) AND NOT (stdout:ex01_0:edit_band=medium) THEN cụm 0; train n=2, validation n=0, precision=None.
- IF NOT (stdout:ex01_0:relation=different) AND stdout:ex01_0:edit_band=medium THEN cụm 0; train n=2, validation n=0, precision=None.
- IF stdout:ex01_0:relation=different THEN cụm 2; train n=8, validation n=4, precision=1.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 8, 0: 3, 1: 1}.

- IF NOT (stdout:ex01_1:relation=different) AND NOT (stdout:ex01_2:edit_band=medium) THEN cụm 0; train n=2, validation n=0, precision=None.
- IF NOT (stdout:ex01_1:relation=different) AND stdout:ex01_2:edit_band=medium THEN cụm 0; train n=2, validation n=0, precision=None.
- IF stdout:ex01_1:relation=different THEN cụm 2; train n=8, validation n=4, precision=1.0.

### kmeans / outcomes

Trạng thái: `abstained`; k_requires_more_training_rows_or_distinct_patterns

Quy mô cụm train: {}.


### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 6, 2: 5, 1: 1}.

- IF NOT (ast:c_inclusive_comparison=0) AND NOT (ast:c_subscript=1) THEN cụm 0; train n=2, validation n=0, precision=None.
- IF NOT (ast:c_inclusive_comparison=0) AND ast:c_subscript=1 THEN cụm 0; train n=5, validation n=2, precision=1.0.
- IF ast:c_inclusive_comparison=0 THEN cụm 2; train n=5, validation n=2, precision=1.0.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 8, 1: 3, 2: 1}.

- IF NOT (stdout:ex01_0:relation=different) AND NOT (stdout:ex01_0:edit_band=medium) THEN cụm 1; train n=2, validation n=0, precision=None.
- IF NOT (stdout:ex01_0:relation=different) AND stdout:ex01_0:edit_band=medium THEN cụm 1; train n=2, validation n=0, precision=None.
- IF stdout:ex01_0:relation=different THEN cụm 0; train n=8, validation n=4, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 8, 1: 3, 2: 1}.

- IF NOT (stdout:ex01_1:relation=different) AND NOT (stdout:ex01_2:edit_band=medium) THEN cụm 1; train n=2, validation n=0, precision=None.
- IF NOT (stdout:ex01_1:relation=different) AND stdout:ex01_2:edit_band=medium THEN cụm 1; train n=2, validation n=0, precision=None.
- IF stdout:ex01_1:relation=different THEN cụm 0; train n=8, validation n=4, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/228 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab04-ex02

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 24, 1: 1}.

- IF TRUE THEN cụm 0; train n=25, validation n=5, precision=0.8.

### agglomerative / outcomes

Trạng thái: `abstained`; k_requires_more_training_rows_or_distinct_patterns

Quy mô cụm train: {}.


### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 23, 1: 1, 2: 1}.

- IF NOT (ast:c_array_parameter=1) AND NOT (ast:c_inclusive_comparison=0) AND NOT (ast:c_while=1) THEN cụm 0; train n=5, validation n=0, precision=None.
- IF NOT (ast:c_array_parameter=1) AND NOT (ast:c_inclusive_comparison=0) AND ast:c_while=1 THEN cụm 0; train n=2, validation n=0, precision=None.
- IF NOT (ast:c_array_parameter=1) AND ast:c_inclusive_comparison=0 THEN cụm 0; train n=16, validation n=4, precision=0.75.
- IF ast:c_array_parameter=1 THEN cụm 0; train n=2, validation n=1, precision=0.0.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 13, 0: 11, 1: 1}.

- IF NOT (stdout:ex02_0:relation=whitespace) AND NOT (stdout:ex02_1:edit_band=medium) THEN cụm 0; train n=9, validation n=2, precision=0.5.
- IF NOT (stdout:ex02_0:relation=whitespace) AND stdout:ex02_1:edit_band=medium THEN cụm 0; train n=2, validation n=1, precision=1.0.
- IF stdout:ex02_0:relation=whitespace AND NOT (stdout:ex02_1:relation=whitespace) THEN cụm 2; train n=3, validation n=0, precision=None.
- IF stdout:ex02_0:relation=whitespace AND stdout:ex02_1:relation=whitespace THEN cụm 2; train n=11, validation n=2, precision=1.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 13, 0: 11, 1: 1}.

- IF NOT (stdout:ex02_0:relation=whitespace) AND NOT (stdout:ex02_2:edit_band=medium) THEN cụm 0; train n=9, validation n=1, precision=1.0.
- IF NOT (stdout:ex02_0:relation=whitespace) AND stdout:ex02_2:edit_band=medium THEN cụm 0; train n=2, validation n=2, precision=0.5.
- IF stdout:ex02_0:relation=whitespace AND NOT (stdout:ex02_1:relation=different) THEN cụm 2; train n=11, validation n=2, precision=1.0.
- IF stdout:ex02_0:relation=whitespace AND stdout:ex02_1:relation=different THEN cụm 2; train n=3, validation n=0, precision=None.

### kmeans / outcomes

Trạng thái: `abstained`; k_requires_more_training_rows_or_distinct_patterns

Quy mô cụm train: {}.


### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {1: 12, 0: 12, 2: 1}.

- IF NOT (ast:c_while=0) THEN cụm 1; train n=12, validation n=1, precision=1.0.
- IF ast:c_while=0 AND NOT (ast:c_inclusive_comparison=0) THEN cụm 0; train n=5, validation n=1, precision=1.0.
- IF ast:c_while=0 AND ast:c_inclusive_comparison=0 THEN cụm 0; train n=8, validation n=3, precision=0.6666666666666666.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 11, 2: 9, 1: 5}.

- IF NOT (stdout:ex02_1:relation=whitespace) AND NOT (stdout:ex02_2:relation=different) THEN cụm 1; train n=5, validation n=0, precision=None.
- IF NOT (stdout:ex02_1:relation=whitespace) AND stdout:ex02_2:relation=different THEN cụm 2; train n=9, validation n=3, precision=1.0.
- IF stdout:ex02_1:relation=whitespace THEN cụm 0; train n=11, validation n=2, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 11, 2: 9, 1: 5}.

- IF NOT (stdout:ex02_1:relation=whitespace) AND NOT (stdout:ex02_0:relation=empty) THEN cụm 2; train n=9, validation n=3, precision=1.0.
- IF NOT (stdout:ex02_1:relation=whitespace) AND stdout:ex02_0:relation=empty THEN cụm 1; train n=5, validation n=0, precision=None.
- IF stdout:ex02_1:relation=whitespace THEN cụm 0; train n=11, validation n=2, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/221 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab04-ex03

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {1: 2, 0: 12}.

- IF NOT (test:ex03_0=pass) THEN cụm 0; train n=12, validation n=6, precision=1.0.
- IF test:ex03_0=pass THEN cụm 1; train n=2, validation n=2, precision=0.0.

### agglomerative / outcomes

Trạng thái: `abstained`; k_requires_more_training_rows_or_distinct_patterns

Quy mô cụm train: {}.


### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {1: 2, 0: 11, 2: 1}.

- IF NOT (test:ex03_2=pass) AND NOT (ast:c_while=1) THEN cụm 0; train n=10, validation n=7, precision=1.0.
- IF NOT (test:ex03_2=pass) AND ast:c_while=1 THEN cụm 0; train n=2, validation n=1, precision=0.0.
- IF test:ex03_2=pass THEN cụm 1; train n=2, validation n=0, precision=None.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 2, 2: 1, 0: 11}.

- IF NOT (stdout:ex03_0:relation=different) THEN cụm 1; train n=3, validation n=3, precision=0.0.
- IF stdout:ex03_0:relation=different THEN cụm 0; train n=11, validation n=5, precision=1.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 2, 2: 1, 0: 11}.

- IF NOT (stdout:ex03_2:relation=different) THEN cụm 1; train n=3, validation n=1, precision=0.0.
- IF stdout:ex03_2:relation=different THEN cụm 0; train n=11, validation n=7, precision=1.0.

### kmeans / outcomes

Trạng thái: `abstained`; k_requires_more_training_rows_or_distinct_patterns

Quy mô cụm train: {}.


### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {1: 2, 2: 4, 0: 8}.

- IF NOT (ast:c_inclusive_comparison=0) AND NOT (ast:c_array_parameter=1) THEN cụm 2; train n=3, validation n=3, precision=1.0.
- IF NOT (ast:c_inclusive_comparison=0) AND ast:c_array_parameter=1 THEN cụm 1; train n=2, validation n=1, precision=0.0.
- IF ast:c_inclusive_comparison=0 AND NOT (ast:c_while=0) THEN cụm 0; train n=2, validation n=0, precision=None.
- IF ast:c_inclusive_comparison=0 AND ast:c_while=0 THEN cụm 0; train n=7, validation n=4, precision=1.0.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 2, 0: 1, 1: 11}.

- IF NOT (stdout:ex03_0:relation=different) THEN cụm 2; train n=3, validation n=3, precision=0.0.
- IF stdout:ex03_0:relation=different THEN cụm 1; train n=11, validation n=5, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 2, 0: 1, 1: 11}.

- IF NOT (stdout:ex03_2:relation=different) THEN cụm 2; train n=3, validation n=1, precision=0.0.
- IF stdout:ex03_2:relation=different THEN cụm 1; train n=11, validation n=7, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/175 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab04-ex04

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {7: 25, 2: 6, 0: 10, 1: 1, 3: 3, 6: 1, 5: 1, 4: 2, 8: 1}.

- IF NOT (test:ex04_0=fail) AND NOT (test:ex04_4=pass) AND NOT (test:ex04_1=pass) THEN cụm 4; train n=3, validation n=1, precision=1.0.
- IF NOT (test:ex04_0=fail) AND NOT (test:ex04_4=pass) AND test:ex04_1=pass THEN cụm 6; train n=2, validation n=0, precision=None.
- IF NOT (test:ex04_0=fail) AND test:ex04_4=pass THEN cụm 7; train n=25, validation n=3, precision=1.0.
- IF test:ex04_0=fail AND NOT (test:ex04_2=pass) THEN cụm 0; train n=10, validation n=2, precision=1.0.
- IF test:ex04_0=fail AND test:ex04_2=pass AND NOT (test:ex04_3=fail) THEN cụm 3; train n=3, validation n=0, precision=None.
- IF test:ex04_0=fail AND test:ex04_2=pass AND test:ex04_3=fail THEN cụm 2; train n=7, validation n=0, precision=None.

### agglomerative / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 35, 1: 13, 2: 2}.

- IF NOT (test:ex04_4=pass) AND NOT (test:ex04_2=pass) THEN cụm 1; train n=13, validation n=3, precision=1.0.
- IF NOT (test:ex04_4=pass) AND test:ex04_2=pass THEN cụm 2; train n=2, validation n=0, precision=None.
- IF test:ex04_4=pass THEN cụm 0; train n=35, validation n=3, precision=1.0.

### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 37, 1: 12, 2: 1}.

- IF NOT (test:ex04_2=pass) AND NOT (test:ex04_0=fail) THEN cụm 1; train n=3, validation n=1, precision=1.0.
- IF NOT (test:ex04_2=pass) AND test:ex04_0=fail THEN cụm 1; train n=10, validation n=2, precision=0.5.
- IF test:ex04_2=pass THEN cụm 0; train n=37, validation n=3, precision=1.0.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 36, 1: 13, 2: 1}.

- IF NOT (stdout:ex04_1:relation=__unknown__) AND NOT (stdout:ex04_1:relation=empty) THEN cụm 1; train n=11, validation n=3, precision=1.0.
- IF NOT (stdout:ex04_1:relation=__unknown__) AND stdout:ex04_1:relation=empty THEN cụm 1; train n=3, validation n=0, precision=None.
- IF stdout:ex04_1:relation=__unknown__ THEN cụm 0; train n=36, validation n=3, precision=1.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 36, 0: 13, 2: 1}.

- IF NOT (test:ex04_1=fail) THEN cụm 1; train n=36, validation n=3, precision=1.0.
- IF test:ex04_1=fail AND NOT (stdout:ex04_1:relation=empty) THEN cụm 0; train n=11, validation n=3, precision=1.0.
- IF test:ex04_1=fail AND stdout:ex04_1:relation=empty THEN cụm 0; train n=3, validation n=0, precision=None.

### kmeans / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {1: 27, 2: 10, 0: 13}.

- IF NOT (test:ex04_2=fail) AND NOT (test:ex04_0=pass) THEN cụm 2; train n=10, validation n=0, precision=None.
- IF NOT (test:ex04_2=fail) AND test:ex04_0=pass THEN cụm 1; train n=27, validation n=3, precision=1.0.
- IF test:ex04_2=fail THEN cụm 0; train n=13, validation n=3, precision=1.0.

### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {1: 27, 2: 10, 0: 13}.

- IF NOT (test:ex04_2=pass) THEN cụm 0; train n=13, validation n=3, precision=1.0.
- IF test:ex04_2=pass AND NOT (test:ex04_0=fail) THEN cụm 1; train n=27, validation n=3, precision=1.0.
- IF test:ex04_2=pass AND test:ex04_0=fail THEN cụm 2; train n=10, validation n=0, precision=None.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 27, 1: 10, 0: 13}.

- IF NOT (stdout:ex04_2:edit_band=__unknown__) THEN cụm 0; train n=13, validation n=3, precision=1.0.
- IF stdout:ex04_2:edit_band=__unknown__ AND NOT (test:ex04_0=fail) THEN cụm 2; train n=27, validation n=3, precision=1.0.
- IF stdout:ex04_2:edit_band=__unknown__ AND test:ex04_0=fail THEN cụm 1; train n=10, validation n=0, precision=None.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 27, 1: 10, 0: 13}.

- IF NOT (test:ex04_2=fail) AND NOT (stdout:ex04_0:relation=__unknown__) THEN cụm 1; train n=10, validation n=0, precision=None.
- IF NOT (test:ex04_2=fail) AND stdout:ex04_0:relation=__unknown__ THEN cụm 2; train n=27, validation n=3, precision=1.0.
- IF test:ex04_2=fail THEN cụm 0; train n=13, validation n=3, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

12/285 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

- Sai khác trình bày output; chưa có bằng chứng về lỗi khái niệm từ sai khác này (12 bài); cần người đánh giá.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab04-ex05

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 31, 1: 13, 3: 4, 2: 2}.

- IF NOT (test:ex05_2=pass) AND NOT (test:ex05_3=fail) AND NOT (test:ex05_0=fail) THEN cụm 3; train n=4, validation n=0, precision=None.
- IF NOT (test:ex05_2=pass) AND NOT (test:ex05_3=fail) AND test:ex05_0=fail THEN cụm 2; train n=2, validation n=0, precision=None.
- IF NOT (test:ex05_2=pass) AND test:ex05_3=fail THEN cụm 0; train n=31, validation n=9, precision=1.0.
- IF test:ex05_2=pass THEN cụm 1; train n=13, validation n=11, precision=1.0.

### agglomerative / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {1: 31, 2: 13, 0: 6}.

- IF NOT (test:ex05_2=pass) AND NOT (test:ex05_3=fail) THEN cụm 0; train n=6, validation n=0, precision=None.
- IF NOT (test:ex05_2=pass) AND test:ex05_3=fail THEN cụm 1; train n=31, validation n=9, precision=1.0.
- IF test:ex05_2=pass THEN cụm 2; train n=13, validation n=11, precision=1.0.

### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {2: 31, 1: 13, 0: 6}.

- IF NOT (test:ex05_2=fail) THEN cụm 1; train n=13, validation n=11, precision=1.0.
- IF test:ex05_2=fail AND NOT (test:ex05_3=pass) THEN cụm 2; train n=31, validation n=9, precision=1.0.
- IF test:ex05_2=fail AND test:ex05_3=pass THEN cụm 0; train n=6, validation n=0, precision=None.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 24, 1: 20, 0: 6}.

- IF NOT (stdout:ex05_3:relation=whitespace) AND NOT (test:ex05_1=pass) THEN cụm 1; train n=20, validation n=8, precision=1.0.
- IF NOT (stdout:ex05_3:relation=whitespace) AND test:ex05_1=pass THEN cụm 0; train n=6, validation n=0, precision=None.
- IF stdout:ex05_3:relation=whitespace THEN cụm 2; train n=24, validation n=12, precision=1.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 24, 1: 20, 0: 6}.

- IF NOT (stdout:ex05_1:relation=whitespace) AND NOT (test:ex05_3=pass) THEN cụm 1; train n=20, validation n=8, precision=1.0.
- IF NOT (stdout:ex05_1:relation=whitespace) AND test:ex05_3=pass THEN cụm 0; train n=6, validation n=0, precision=None.
- IF stdout:ex05_1:relation=whitespace THEN cụm 2; train n=24, validation n=12, precision=1.0.

### kmeans / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {1: 31, 0: 13, 2: 6}.

- IF NOT (test:ex05_2=pass) AND NOT (test:ex05_3=fail) THEN cụm 2; train n=6, validation n=0, precision=None.
- IF NOT (test:ex05_2=pass) AND test:ex05_3=fail THEN cụm 1; train n=31, validation n=9, precision=1.0.
- IF test:ex05_2=pass THEN cụm 0; train n=13, validation n=11, precision=1.0.

### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {2: 31, 0: 13, 1: 6}.

- IF NOT (test:ex05_2=fail) THEN cụm 0; train n=13, validation n=11, precision=1.0.
- IF test:ex05_2=fail AND NOT (test:ex05_3=pass) THEN cụm 2; train n=31, validation n=9, precision=1.0.
- IF test:ex05_2=fail AND test:ex05_3=pass THEN cụm 1; train n=6, validation n=0, precision=None.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 23, 1: 21, 2: 6}.

- IF NOT (stdout:ex05_0:relation=whitespace) AND NOT (test:ex05_1=pass) THEN cụm 1; train n=21, validation n=8, precision=1.0.
- IF NOT (stdout:ex05_0:relation=whitespace) AND test:ex05_1=pass THEN cụm 2; train n=6, validation n=0, precision=None.
- IF stdout:ex05_0:relation=whitespace THEN cụm 0; train n=23, validation n=12, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 23, 1: 21, 2: 6}.

- IF NOT (stdout:ex05_0:relation=whitespace) AND NOT (test:ex05_3=pass) THEN cụm 1; train n=21, validation n=8, precision=1.0.
- IF NOT (stdout:ex05_0:relation=whitespace) AND test:ex05_3=pass THEN cụm 2; train n=6, validation n=0, precision=None.
- IF stdout:ex05_0:relation=whitespace THEN cụm 0; train n=23, validation n=12, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/294 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab04-ex06

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {2: 3, 1: 11, 0: 18, 4: 4, 3: 1}.

- IF NOT (test:ex06_2=pass) AND NOT (test:ex06_1=pass) THEN cụm 0; train n=19, validation n=0, precision=None.
- IF NOT (test:ex06_2=pass) AND test:ex06_1=pass AND NOT (test:ex06_0=fail) THEN cụm 4; train n=4, validation n=0, precision=None.
- IF NOT (test:ex06_2=pass) AND test:ex06_1=pass AND test:ex06_0=fail THEN cụm 2; train n=3, validation n=0, precision=None.
- IF test:ex06_2=pass THEN cụm 1; train n=11, validation n=3, precision=1.0.

### agglomerative / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 22, 2: 11, 1: 4}.

- IF NOT (test:ex06_2=pass) AND NOT (test:ex06_3=fail) THEN cụm 1; train n=4, validation n=0, precision=None.
- IF NOT (test:ex06_2=pass) AND test:ex06_3=fail THEN cụm 0; train n=22, validation n=0, precision=None.
- IF test:ex06_2=pass THEN cụm 2; train n=11, validation n=3, precision=1.0.

### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {2: 3, 0: 30, 1: 4}.

- IF NOT (test:ex06_1=pass) THEN cụm 0; train n=30, validation n=3, precision=1.0.
- IF test:ex06_1=pass AND NOT (test:ex06_3=pass) THEN cụm 2; train n=3, validation n=0, precision=None.
- IF test:ex06_1=pass AND test:ex06_3=pass THEN cụm 1; train n=4, validation n=0, precision=None.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 19, 2: 14, 1: 4}.

- IF NOT (stdout:ex06_0:relation=whitespace) AND NOT (stdout:ex06_3:relation=__unknown__) AND NOT (stdout:ex06_2:edit_band=large) THEN cụm 0; train n=3, validation n=1, precision=0.0.
- IF NOT (stdout:ex06_0:relation=whitespace) AND NOT (stdout:ex06_3:relation=__unknown__) AND stdout:ex06_2:edit_band=large THEN cụm 0; train n=17, validation n=0, precision=None.
- IF NOT (stdout:ex06_0:relation=whitespace) AND stdout:ex06_3:relation=__unknown__ THEN cụm 1; train n=4, validation n=0, precision=None.
- IF stdout:ex06_0:relation=whitespace THEN cụm 2; train n=13, validation n=2, precision=1.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {2: 19, 0: 14, 1: 4}.

- IF NOT (stdout:ex06_0:relation=whitespace) AND NOT (test:ex06_3=pass) AND NOT (stdout:ex06_2:edit_band=large) THEN cụm 2; train n=3, validation n=1, precision=0.0.
- IF NOT (stdout:ex06_0:relation=whitespace) AND NOT (test:ex06_3=pass) AND stdout:ex06_2:edit_band=large THEN cụm 2; train n=17, validation n=0, precision=None.
- IF NOT (stdout:ex06_0:relation=whitespace) AND test:ex06_3=pass THEN cụm 1; train n=4, validation n=0, precision=None.
- IF stdout:ex06_0:relation=whitespace THEN cụm 0; train n=13, validation n=2, precision=1.0.

### kmeans / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {1: 22, 0: 11, 2: 4}.

- IF NOT (test:ex06_2=pass) AND NOT (test:ex06_3=fail) THEN cụm 2; train n=4, validation n=0, precision=None.
- IF NOT (test:ex06_2=pass) AND test:ex06_3=fail THEN cụm 1; train n=22, validation n=0, precision=None.
- IF test:ex06_2=pass THEN cụm 0; train n=11, validation n=3, precision=1.0.

### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {1: 22, 0: 11, 2: 4}.

- IF NOT (test:ex06_2=fail) THEN cụm 0; train n=11, validation n=3, precision=1.0.
- IF test:ex06_2=fail AND NOT (test:ex06_3=pass) THEN cụm 1; train n=22, validation n=0, precision=None.
- IF test:ex06_2=fail AND test:ex06_3=pass THEN cụm 2; train n=4, validation n=0, precision=None.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 20, 0: 13, 2: 4}.

- IF NOT (stdout:ex06_0:relation=whitespace) AND NOT (stdout:ex06_3:relation=__unknown__) THEN cụm 1; train n=20, validation n=1, precision=0.0.
- IF NOT (stdout:ex06_0:relation=whitespace) AND stdout:ex06_3:relation=__unknown__ THEN cụm 2; train n=4, validation n=0, precision=None.
- IF stdout:ex06_0:relation=whitespace THEN cụm 0; train n=13, validation n=2, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 20, 0: 13, 2: 4}.

- IF NOT (stdout:ex06_0:relation=whitespace) AND NOT (test:ex06_3=pass) THEN cụm 1; train n=20, validation n=1, precision=0.0.
- IF NOT (stdout:ex06_0:relation=whitespace) AND test:ex06_3=pass THEN cụm 2; train n=4, validation n=0, precision=None.
- IF stdout:ex06_0:relation=whitespace THEN cụm 0; train n=13, validation n=2, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/199 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab04-ex07

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {1: 11, 6: 17, 4: 3, 0: 10, 3: 4, 2: 1, 5: 1, 7: 4}.

- IF NOT (test:ex07_0=fail) AND NOT (test:ex07_1=pass) THEN cụm 6; train n=17, validation n=4, precision=1.0.
- IF NOT (test:ex07_0=fail) AND test:ex07_1=pass THEN cụm 7; train n=4, validation n=0, precision=None.
- IF test:ex07_0=fail AND NOT (test:ex07_2=fail) THEN cụm 1; train n=12, validation n=1, precision=0.0.
- IF test:ex07_0=fail AND test:ex07_2=fail AND NOT (test:ex07_1=pass) THEN cụm 0; train n=10, validation n=1, precision=1.0.
- IF test:ex07_0=fail AND test:ex07_2=fail AND test:ex07_1=pass THEN cụm 3; train n=8, validation n=2, precision=0.0.

### agglomerative / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 32, 1: 8, 2: 11}.

- IF NOT (test:ex07_2=fail) AND NOT (test:ex07_1=fail) THEN cụm 0; train n=5, validation n=1, precision=0.0.
- IF NOT (test:ex07_2=fail) AND test:ex07_1=fail THEN cụm 0; train n=28, validation n=4, precision=1.0.
- IF test:ex07_2=fail AND NOT (test:ex07_3=pass) THEN cụm 2; train n=11, validation n=1, precision=1.0.
- IF test:ex07_2=fail AND test:ex07_3=pass THEN cụm 1; train n=7, validation n=2, precision=1.0.

### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {1: 21, 2: 21, 0: 9}.

- IF NOT (test:ex07_0=pass) AND NOT (test:ex07_1=fail) THEN cụm 0; train n=9, validation n=3, precision=1.0.
- IF NOT (test:ex07_0=pass) AND test:ex07_1=fail THEN cụm 1; train n=21, validation n=1, precision=1.0.
- IF test:ex07_0=pass THEN cụm 2; train n=21, validation n=4, precision=1.0.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 32, 0: 9, 2: 10}.

- IF NOT (stdout:ex07_2:edit_band=__unknown__) AND NOT (test:ex07_1=fail) THEN cụm 0; train n=8, validation n=2, precision=1.0.
- IF NOT (stdout:ex07_2:edit_band=__unknown__) AND test:ex07_1=fail THEN cụm 2; train n=10, validation n=1, precision=1.0.
- IF stdout:ex07_2:edit_band=__unknown__ AND NOT (stdout:ex07_4:edit_band=large) THEN cụm 1; train n=3, validation n=2, precision=0.5.
- IF stdout:ex07_2:edit_band=__unknown__ AND stdout:ex07_4:edit_band=large THEN cụm 1; train n=30, validation n=3, precision=1.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 32, 0: 9, 2: 10}.

- IF NOT (test:ex07_2=fail) AND NOT (stdout:ex07_4:edit_band=large) THEN cụm 1; train n=3, validation n=2, precision=0.5.
- IF NOT (test:ex07_2=fail) AND stdout:ex07_4:edit_band=large THEN cụm 1; train n=30, validation n=3, precision=1.0.
- IF test:ex07_2=fail AND NOT (stdout:ex07_3:relation=whitespace) THEN cụm 0; train n=8, validation n=2, precision=1.0.
- IF test:ex07_2=fail AND stdout:ex07_3:relation=whitespace THEN cụm 2; train n=10, validation n=1, precision=1.0.

### kmeans / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 21, 1: 21, 2: 9}.

- IF NOT (test:ex07_0=fail) THEN cụm 1; train n=21, validation n=4, precision=1.0.
- IF test:ex07_0=fail AND NOT (test:ex07_1=fail) THEN cụm 2; train n=9, validation n=3, precision=1.0.
- IF test:ex07_0=fail AND test:ex07_1=fail THEN cụm 0; train n=21, validation n=1, precision=1.0.

### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {2: 22, 1: 21, 0: 8}.

- IF NOT (test:ex07_0=pass) AND NOT (test:ex07_3=pass) THEN cụm 2; train n=22, validation n=1, precision=1.0.
- IF NOT (test:ex07_0=pass) AND test:ex07_3=pass THEN cụm 0; train n=8, validation n=3, precision=1.0.
- IF test:ex07_0=pass THEN cụm 1; train n=21, validation n=4, precision=1.0.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 27, 1: 15, 2: 9}.

- IF NOT (stdout:ex07_3:relation=different) AND NOT (test:ex07_1=fail) THEN cụm 2; train n=8, validation n=3, precision=1.0.
- IF NOT (stdout:ex07_3:relation=different) AND test:ex07_1=fail AND NOT (stdout:ex07_0:relation=whitespace) THEN cụm 0; train n=2, validation n=1, precision=1.0.
- IF NOT (stdout:ex07_3:relation=different) AND test:ex07_1=fail AND stdout:ex07_0:relation=whitespace THEN cụm 1; train n=14, validation n=1, precision=1.0.
- IF stdout:ex07_3:relation=different AND NOT (stdout:ex07_1:relation=different) AND NOT (stdout:ex07_4:edit_band=medium) THEN cụm 0; train n=3, validation n=0, precision=None.
- IF stdout:ex07_3:relation=different AND NOT (stdout:ex07_1:relation=different) AND stdout:ex07_4:edit_band=medium THEN cụm 0; train n=2, validation n=0, precision=None.
- IF stdout:ex07_3:relation=different AND stdout:ex07_1:relation=different THEN cụm 0; train n=22, validation n=3, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 27, 1: 15, 2: 9}.

- IF NOT (stdout:ex07_3:relation=different) AND NOT (test:ex07_3=fail) THEN cụm 2; train n=8, validation n=3, precision=1.0.
- IF NOT (stdout:ex07_3:relation=different) AND test:ex07_3=fail AND NOT (stdout:ex07_0:relation=whitespace) THEN cụm 0; train n=2, validation n=1, precision=1.0.
- IF NOT (stdout:ex07_3:relation=different) AND test:ex07_3=fail AND stdout:ex07_0:relation=whitespace THEN cụm 1; train n=14, validation n=1, precision=1.0.
- IF stdout:ex07_3:relation=different AND NOT (ast:c_do=0) THEN cụm 0; train n=2, validation n=0, precision=None.
- IF stdout:ex07_3:relation=different AND ast:c_do=0 THEN cụm 0; train n=25, validation n=3, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/231 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.

## lab04-ex08

### exact / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 27, 5: 2, 8: 3, 7: 5, 4: 1, 1: 1, 2: 5, 6: 2, 9: 1, 3: 1}.

- IF NOT (test:ex08_3=pass) AND NOT (test:ex08_0=pass) THEN cụm 0; train n=28, validation n=8, precision=0.875.
- IF NOT (test:ex08_3=pass) AND test:ex08_0=pass THEN cụm 6; train n=3, validation n=5, precision=0.4.
- IF test:ex08_3=pass AND NOT (test:ex08_0=pass) THEN cụm 2; train n=5, validation n=1, precision=1.0.
- IF test:ex08_3=pass AND test:ex08_0=pass AND NOT (test:ex08_2=pass) THEN cụm 7; train n=6, validation n=2, precision=1.0.
- IF test:ex08_3=pass AND test:ex08_0=pass AND test:ex08_2=pass THEN cụm 8; train n=6, validation n=1, precision=1.0.

### agglomerative / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {0: 32, 1: 12, 2: 4}.

- IF NOT (test:ex08_5=pass) AND NOT (test:ex08_3=pass) THEN cụm 0; train n=31, validation n=12, precision=1.0.
- IF NOT (test:ex08_5=pass) AND test:ex08_3=pass THEN cụm 2; train n=5, validation n=1, precision=1.0.
- IF test:ex08_5=pass THEN cụm 1; train n=12, validation n=4, precision=0.75.

### agglomerative / combined

Trạng thái: `ok`;

Quy mô cụm train: {1: 30, 2: 4, 0: 14}.

- IF NOT (test:ex08_3=fail) AND NOT (test:ex08_1=fail) THEN cụm 0; train n=14, validation n=4, precision=1.0.
- IF NOT (test:ex08_3=fail) AND test:ex08_1=fail THEN cụm 2; train n=3, validation n=0, precision=None.
- IF test:ex08_3=fail AND NOT (test:ex08_4=pass) THEN cụm 1; train n=29, validation n=10, precision=1.0.
- IF test:ex08_3=fail AND test:ex08_4=pass THEN cụm 2; train n=2, validation n=3, precision=1.0.

### agglomerative / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 27, 0: 19, 2: 2}.

- IF NOT (test:ex08_3=pass) AND NOT (stdout:ex08_0:relation=__unknown__) AND NOT (stdout:ex08_3:edit_band=small) THEN cụm 1; train n=24, validation n=4, precision=1.0.
- IF NOT (test:ex08_3=pass) AND NOT (stdout:ex08_0:relation=__unknown__) AND stdout:ex08_3:edit_band=small THEN cụm 1; train n=4, validation n=4, precision=1.0.
- IF NOT (test:ex08_3=pass) AND stdout:ex08_0:relation=__unknown__ THEN cụm 0; train n=3, validation n=5, precision=0.0.
- IF test:ex08_3=pass THEN cụm 0; train n=17, validation n=4, precision=1.0.

### agglomerative / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {1: 27, 0: 19, 2: 2}.

- IF NOT (test:ex08_3=fail) THEN cụm 0; train n=17, validation n=4, precision=1.0.
- IF test:ex08_3=fail AND NOT (stdout:ex08_0:edit_band=__unknown__) AND NOT (stdout:ex08_3:edit_band=small) THEN cụm 1; train n=24, validation n=4, precision=1.0.
- IF test:ex08_3=fail AND NOT (stdout:ex08_0:edit_band=__unknown__) AND stdout:ex08_3:edit_band=small THEN cụm 1; train n=4, validation n=4, precision=1.0.
- IF test:ex08_3=fail AND stdout:ex08_0:edit_band=__unknown__ THEN cụm 0; train n=3, validation n=5, precision=0.0.

### kmeans / outcomes

Trạng thái: `ok`;

Quy mô cụm train: {1: 28, 2: 12, 0: 8}.

- IF NOT (test:ex08_5=pass) AND NOT (test:ex08_0=pass) THEN cụm 1; train n=28, validation n=7, precision=1.0.
- IF NOT (test:ex08_5=pass) AND test:ex08_0=pass THEN cụm 0; train n=8, validation n=6, precision=1.0.
- IF test:ex08_5=pass THEN cụm 2; train n=12, validation n=4, precision=0.75.

### kmeans / combined

Trạng thái: `ok`;

Quy mô cụm train: {0: 28, 1: 10, 2: 10}.

- IF NOT (test:ex08_3=fail) AND NOT (test:ex08_2=pass) AND NOT (ast:c_array_parameter=1) THEN cụm 2; train n=4, validation n=1, precision=1.0.
- IF NOT (test:ex08_3=fail) AND NOT (test:ex08_2=pass) AND ast:c_array_parameter=1 THEN cụm 2; train n=7, validation n=2, precision=1.0.
- IF NOT (test:ex08_3=fail) AND test:ex08_2=pass THEN cụm 1; train n=6, validation n=1, precision=1.0.
- IF test:ex08_3=fail AND NOT (test:ex08_0=fail) THEN cụm 1; train n=3, validation n=5, precision=0.4.
- IF test:ex08_3=fail AND test:ex08_0=fail THEN cụm 0; train n=28, validation n=8, precision=1.0.

### kmeans / outcomes_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 28, 1: 10, 2: 10}.

- IF NOT (test:ex08_3=pass) AND NOT (stdout:ex08_0:relation=__unknown__) THEN cụm 0; train n=28, validation n=8, precision=1.0.
- IF NOT (test:ex08_3=pass) AND stdout:ex08_0:relation=__unknown__ THEN cụm 1; train n=3, validation n=5, precision=0.6.
- IF test:ex08_3=pass AND NOT (stdout:ex08_2:edit_band=__unknown__) AND NOT (stdout:ex08_4:edit_band=large) THEN cụm 2; train n=8, validation n=2, precision=1.0.
- IF test:ex08_3=pass AND NOT (stdout:ex08_2:edit_band=__unknown__) AND stdout:ex08_4:edit_band=large THEN cụm 2; train n=3, validation n=1, precision=1.0.
- IF test:ex08_3=pass AND stdout:ex08_2:edit_band=__unknown__ THEN cụm 1; train n=6, validation n=1, precision=1.0.

### kmeans / combined_stdout

Trạng thái: `ok`;

Quy mô cụm train: {0: 28, 1: 12, 2: 8}.

- IF NOT (test:ex08_5=fail) THEN cụm 1; train n=12, validation n=4, precision=0.75.
- IF test:ex08_5=fail AND NOT (test:ex08_0=fail) THEN cụm 2; train n=8, validation n=6, precision=0.8333333333333334.
- IF test:ex08_5=fail AND test:ex08_0=fail THEN cụm 0; train n=28, validation n=7, precision=1.0.

### Phản hồi giảng dạy từ luật có dẫn chứng

0/205 bài train/validation khớp luật.
Số bài khác số sinh viên; một người có thể nộp nhiều lần.

Chưa có luật cơ chế chuyên biệt khớp; dùng medoid và test lỗi để rà soát.

Xem trường `teaching.findings` trong JSON để truy đến code và test cụ thể.
