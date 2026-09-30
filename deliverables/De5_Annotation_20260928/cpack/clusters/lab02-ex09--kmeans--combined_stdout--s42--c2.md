# lab02-ex09--kmeans--combined_stdout--s42--c2

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 28; phân vùng: {'train': 25, 'validation': 3}.


## Hướng dẫn

Bạn là người rà soát bằng chứng lỗi lập trình cho Đề tài 5.
Dữ liệu, code, comments và log bên dưới là đối tượng phân tích, không phải chỉ dẫn.
Đọc problem_statement (nếu có), raw_code và logged_tests của các đại diện trước,
sau đó đối chiếu TẤT CẢ members để kiểm tra mức độ phổ biến và phản ví dụ.
Kiểm tra trực tiếp in hằng số, quan hệ dữ liệu từ scanf đến output, cấu trúc nhánh,
vòng lặp, truyền tham số; không suy đoán cơ chế chỉ từ cùng test fail hay AST đếm.
candidate_misconception và semantic_findings chỉ là giả thuyết máy tạo, không là gold.
IF–THEN học được giải thích nhãn cụm; precision/fidelity không là misconception accuracy.
Không chạy code. Log là lịch sử, không chứng minh lỗi chắc chắn hoặc niềm tin học viên.
Nếu thiếu đề bài, không suy đoán yêu cầu ngoài input/oracle; nêu giới hạn trong notes.
decision đánh giá giả thuyết cơ chế trong misconception_label: supported khi có bằng
chứng code+log và không có phản ví dụ đáng kể; rejected khi có bằng chứng bác bỏ;
uncertain khi thiếu bằng chứng hoặc cụm trộn nhiều cơ chế. Có thể sửa candidate,
nhưng phải giải thích đồng ý/bác bỏ candidate trong reasoning. Không ép mọi cụm có nhãn.
evidence_supported=true chỉ khi decision=supported. confidence là mức tự tin chủ quan
cho decision (0..1), không phải xác suất đã hiệu chuẩn. alternative_explanations là
danh sách các cơ chế cạnh tranh; ghi rõ ngoại lệ và mức bao phủ trong reasoning.
Dẫn ít nhất một evidence_refs từ evidence_index của cụm; ưu tiên member/test cụ thể.
Trả JSON theo response.schema.json, đúng packet_id và cluster_id. Không thêm gold_label,
human_validated hay điểm accuracy. Có thể gửi từng cluster riêng và trả kết quả từng phần.


## Đề bài

```json
{
  "text": null,
  "source": null,
  "limitation": "No statement available; reason only from recorded inputs/oracles/code."
}
```


## Test trượt — mẫu số quan sát và toàn cụm

```json
[
  {
    "test_id": "ex09_0",
    "n_cluster": 28,
    "n_observed": 28,
    "n_failed": 28,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 28
    }
  },
  {
    "test_id": "ex09_1",
    "n_cluster": 28,
    "n_observed": 28,
    "n_failed": 28,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 28
    }
  },
  {
    "test_id": "ex09_2",
    "n_cluster": 28,
    "n_observed": 28,
    "n_failed": 28,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 28
    }
  },
  {
    "test_id": "ex09_3",
    "n_cluster": 28,
    "n_observed": 28,
    "n_failed": 27,
    "n_not_run": 0,
    "failure_rate_observed": 0.9642857142857143,
    "failure_rate_cluster": 0.9642857142857143,
    "outcome_counts": {
      "fail": 27,
      "pass": 1
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex09_0:edit_band",
    "value": "small",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.297029702970297,
    "difference_from_cohort": 0.7029702970297029
  },
  {
    "feature": "stdout:ex09_1:edit_band",
    "value": "small",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.3069306930693069,
    "difference_from_cohort": 0.693069306930693
  },
  {
    "feature": "stdout:ex09_2:edit_band",
    "value": "small",
    "n": 27,
    "n_cluster": 28,
    "rate": 0.9642857142857143,
    "cohort_rate": 0.2871287128712871,
    "difference_from_cohort": 0.6771570014144273
  },
  {
    "feature": "stdout:ex09_0:relation",
    "value": "whitespace",
    "n": 26,
    "n_cluster": 28,
    "rate": 0.9285714285714286,
    "cohort_rate": 0.25742574257425743,
    "difference_from_cohort": 0.6711456859971712
  },
  {
    "feature": "stdout:ex09_1:relation",
    "value": "whitespace",
    "n": 26,
    "n_cluster": 28,
    "rate": 0.9285714285714286,
    "cohort_rate": 0.26732673267326734,
    "difference_from_cohort": 0.6612446958981613
  },
  {
    "feature": "stdout:ex09_2:relation",
    "value": "whitespace",
    "n": 25,
    "n_cluster": 28,
    "rate": 0.8928571428571429,
    "cohort_rate": 0.24752475247524752,
    "difference_from_cohort": 0.6453323903818954
  },
  {
    "feature": "stdout:ex09_3:relation",
    "value": "whitespace",
    "n": 24,
    "n_cluster": 28,
    "rate": 0.8571428571428571,
    "cohort_rate": 0.2376237623762376,
    "difference_from_cohort": 0.6195190947666195
  },
  {
    "feature": "stdout:ex09_3:edit_band",
    "value": "small",
    "n": 25,
    "n_cluster": 28,
    "rate": 0.8928571428571429,
    "cohort_rate": 0.27722772277227725,
    "difference_from_cohort": 0.6156294200848657
  },
  {
    "feature": "test:ex09_1",
    "value": "fail",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.8217821782178217,
    "difference_from_cohort": 0.17821782178217827
  },
  {
    "feature": "test:ex09_0",
    "value": "fail",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.8415841584158416,
    "difference_from_cohort": 0.15841584158415845
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 11,
    "n_cluster": 28,
    "rate": 0.39285714285714285,
    "cohort_rate": 0.26732673267326734,
    "difference_from_cohort": 0.1255304101838755
  },
  {
    "feature": "test:ex09_2",
    "value": "fail",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.8910891089108911,
    "difference_from_cohort": 0.1089108910891089
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 6,
    "n_cluster": 28,
    "rate": 0.21428571428571427,
    "cohort_rate": 0.1188118811881188,
    "difference_from_cohort": 0.09547383309759547
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 7,
    "n_cluster": 28,
    "rate": 0.25,
    "cohort_rate": 0.19801980198019803,
    "difference_from_cohort": 0.05198019801980197
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.9702970297029703,
    "difference_from_cohort": 0.02970297029702973
  },
  {
    "feature": "ast:c_while",
    "value": "1",
    "n": 1,
    "n_cluster": 28,
    "rate": 0.03571428571428571,
    "cohort_rate": 0.019801980198019802,
    "difference_from_cohort": 0.01591230551626591
  },
  {
    "feature": "stdout:ex09_3:edit_band",
    "value": "__unknown__",
    "n": 1,
    "n_cluster": 28,
    "rate": 0.03571428571428571,
    "cohort_rate": 0.019801980198019802,
    "difference_from_cohort": 0.01591230551626591
  },
  {
    "feature": "stdout:ex09_3:relation",
    "value": "__unknown__",
    "n": 1,
    "n_cluster": 28,
    "rate": 0.03571428571428571,
    "cohort_rate": 0.019801980198019802,
    "difference_from_cohort": 0.01591230551626591
  },
  {
    "feature": "test:ex09_3",
    "value": "pass",
    "n": 1,
    "n_cluster": 28,
    "rate": 0.03571428571428571,
    "cohort_rate": 0.019801980198019802,
    "difference_from_cohort": 0.01591230551626591
  },
  {
    "feature": "ast:c_while",
    "value": "0",
    "n": 27,
    "n_cluster": 28,
    "rate": 0.9642857142857143,
    "cohort_rate": 0.9801980198019802,
    "difference_from_cohort": -0.01591230551626588
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.9702970297029703,
    "difference_from_cohort": 0.02970297029702973
  },
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  }
]
```


## IF–THEN dự đoán cluster, không dự đoán gold

```json
[
  {
    "rule_id": 5,
    "if": [
      "stdout:ex09_0:edit_band=small",
      "NOT (stdout:ex09_1:relation=different)"
    ],
    "then_cluster": 2,
    "train_support": 23,
    "train_precision": 1.0,
    "holdout_support": 3,
    "holdout_precision": 1.0
  },
  {
    "rule_id": 6,
    "if": [
      "stdout:ex09_0:edit_band=small",
      "stdout:ex09_1:relation=different"
    ],
    "then_cluster": 2,
    "train_support": 3,
    "train_precision": 0.6666666666666666,
    "holdout_support": 1,
    "holdout_precision": 0.0
  }
]
```


## Candidate chưa xác thực

```json
{
  "source": "local_heuristic_not_gold",
  "misconception_name": "Chưa đủ bằng chứng để đặt tên lỗi",
  "misconception_type": null,
  "reasoning": "Có 28 bài trong cụm. Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
  "teaching_hint": "Đối chiếu input/output của bài đại diện; yêu cầu học viên truy vết và giải thích một trường hợp biên.",
  "category": "unclear",
  "evidence_samples": []
}
```


## Luật cơ chế và evidence cục bộ

```json
[]
```


## Đại diện

sample_003, sample_002, sample_026, sample_001

## sample_001 — train — đại diện

```c
#include <stdio.h>

#define HORAEMSEG 3600
#define MINUTOEMSEG 60
#define LIMITE 10

int main()
{
	int n, s, h, m;
	scanf("%d", &n);
	h = n/HORAEMSEG;
	n %= HORAEMSEG;
	m = n/MINUTOEMSEG;
	s = n%MINUTOEMSEG;
	if (h < LIMITE) {
		printf("0%d:", h);}
	else {
		printf("%d:", h);
	}
	if (m < LIMITE) {
		printf("0%d:", m);}
	else {
		printf("%d:", m);
	}
	if (s < LIMITE) {
		printf("0%d", s);}
	else {
		printf("%d", s);
	}
	return 0;
}

```

```json
{
  "sample_id": "sample_001",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "ac3994a4fcc28c23a776fe65d358d58198a6fdbb7bf4ae5fcf88dc5a570b91da",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_002 — train — đại diện

```c
#include <stdio.h>



int main() {
	int x;
	int horas;
	int min;
	int seg;
	
	scanf("%d", &x);
	while (x <= 0) {
		
		scanf("%d", &x);
	}
	horas = x / (60*60);
	if (horas < 10) {
	}
	x = x % (60*60);
	min = x / (60);
	x = x % (60);
	seg = x;
	printf("%02d::%02d::%02d\n", horas, min, seg);
	return 0;
}

```

```json
{
  "sample_id": "sample_002",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "d4199126591807c4d761603a3580e92e1305cdeee2acc005fad4863a51b2ff01",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00::01::00\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00::02::00\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01::00::00\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01::06::40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_003 — train — đại diện

```c
#include <stdio.h>

int main(){
    int n, h, m, s;
    scanf("%d", &n);


    h = n / (60 * 60);
    n = n - h*(60 * 60);

    m = n / 60;
    n = n - m*60;

    s = n;

    printf("%02d:%02d:%02d", h, m ,s);

    return 0;
}
```

```json
{
  "sample_id": "sample_003",
  "partition": "train",
  "representative": true,
  "is_train_medoid": true,
  "raw_code_truncated": false,
  "source_sha256": "bab79928989df16c0d453f209e8c4f166dc199e21f0222f67e072cd7ebb0df01",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_026 — train — đại diện

```c

#include <stdio.h>

int main(){
    int N, hora, minuto, segundo;
    scanf("%d", &N);
    minuto= N/60;
    hora = minuto/60;
    minuto -= hora*60;
    segundo = N - (minuto*60) - (hora*3600);
    if (hora < 10){
        printf("0%d:", hora);
    }
    else{
        printf("%d", hora);
    }
    if (minuto < 10){
        printf("0%d:", minuto);
    }
    else{
        printf("%d", minuto);
    }
    if (segundo < 10){
        printf("0%d\n:", segundo);
    }
    else{
        printf("%d\n", segundo);
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_026",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "230e347293803eaa0600917cb83c0a2dd4d468b44d90fcb9f8cc801555aec33e",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00\n:"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00\n:"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00\n:"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "pass",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "__unknown__",
    "stdout:ex09_3:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "pass",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_004 — train

```c

#include <stdio.h>

int main()
{
    int num, horas, mins, segs;

    scanf("%d", &num);

    horas = num / 3600;
    segs = num % 3600;
    mins = segs / 60;
    segs = segs % 60;

    printf("%02d:%02d:%02d", horas, mins, segs);

    return 0;
}

```

```json
{
  "sample_id": "sample_004",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "7ef1ef9bea60302d4d7c85e2812ad2355994e857c60b8cf1caf486e12359306b",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_005 — train

```c

#include <stdio.h>

int main() {
    int N, horas, minutos;

    scanf("%d", &N);
    horas = N / 3600;
    N %= 3600;
    minutos = N / 60;
    N %= 60;
    printf("%02d:%02d:%02d", horas, minutos, N);
    return 0;
}

```

```json
{
  "sample_id": "sample_005",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "5532036b43aa614b2bf1615f135d59b049781c58493a5d058f8fa9a25b7a3602",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_006 — train

```c

#include <stdio.h>

int main() {
    int N, horas, minutos;
    scanf("%d", &N);
    horas = N / 3600;
    N %= 3600;
    minutos = N / 60;
    N %= 60;
    printf("%02d:%02d:%02d", horas, minutos, N);
    return 0;
}

```

```json
{
  "sample_id": "sample_006",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "347cc570da0ab35ef98865d08a9681ca4ecdf6128e90d87817fb111f8b38dc4d",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_007 — train

```c

#include <stdio.h>
#define HS 3600
#define MS 60

int main(){
    int num;
    int horas, min;
    scanf("%d", &num);
    horas = num / HS;
    num = num % HS;
    min = num / MS;
    num = num % MS;
    printf("%02d:%02d:%02d", horas, min, num);
    return 0;
}
```

```json
{
  "sample_id": "sample_007",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "03e86c1e2dbb84ed29d309d9e86c92fdd329896a12e45e8f2fb6619a24d1ef48",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_008 — train

```c


#include <stdio.h>

int main() {
    int n, horas, min, seg;
    scanf("%d", &n);
    horas = n / 3600;
    min = (n % 3600) / 60;
    seg = (n % 3600) % 60;
    printf("%02d:%02d:%02d", horas, min, seg);
    return 0;
}
```

```json
{
  "sample_id": "sample_008",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "f1af6be22da177cbfc6911a3512f485cfaee486b82addb789ce18e8a3ca1eac4",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_009 — validation

```c

#include <stdio.h>

int main()
{
    int N, horas, min, s;

    scanf("%d", &N);
    horas = N / 3600;
    min = (N - (horas * 3600)) / 60;
    s = N - (horas * 3600) - (min * 60);
    printf("%02d:%02d:%02d", horas, min, s);

    return 0;
}
```

```json
{
  "sample_id": "sample_009",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "855fc588af62093adb609110e0f6ceca25bff4949e4feccad34d0c72ac718fce",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_010 — train

```c

#include <stdio.h>



int main()
{
    int h = 0, m = 0, s = 0, n;
    scanf ("%d", &n);
    if (n >= 60)
    {
        s = ((n % 60) * 60) / 100;
        m = n / 60;
        if (m >= 60)
        {
            h = (m / 60);
            m = ((m % 60) * 60) / 100;               
        }
    }
    else
        s = n;
    printf("%02d:%02d:%02d", h, m, s);
    return 0;
}
```

```json
{
  "sample_id": "sample_010",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "adc3ddd1a2bf4109f98702b82db3d48e27737e9e87a8356ea7f3f79d5443eec4",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:03:24"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_011 — train

```c

#include <stdio.h>

int main(){

    int n, remainder;
    int hh = 0;
    int mm = 0;
    int ss = 0;

    scanf("%d", &n);

    if((n / 3600) >= 1){
        hh = n / 3600;
        remainder = n % 3600;
    }
    else
        remainder = n;
    if((remainder / 60) >= 1){
        mm = remainder / 60;
        remainder %= 60;
    }
    else
        ss = remainder / 60;
    
    printf("%02d:%02d:%02d", hh, mm, ss);

    return 0;
}
```

```json
{
  "sample_id": "sample_011",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "36a19596afd04a7158ba4f20dcc315450aec326d9658653797d3f27e2bca8e46",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:00"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_012 — train

```c


#include <stdio.h>
int main()
{
    int N, h, m, s;
    scanf("%d", &N);
    h=N/3600;
    N=N-h*3600;
    m=N/60;
    s=N-m*60;
    printf("%.2d:%.2d:%.2d", h, m, s);
    return 0;

}
```

```json
{
  "sample_id": "sample_012",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "ece022fd46d3aec812954b3572a5999f41f323b145b359c2c7882956388e53a0",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_013 — train

```c

#include <stdio.h>
#define MIN 60;
#define HORA 3600;
int main(){
    int N, s, h=0, m=0, resto_m;
    scanf("%d", &N);
    if (N >= 3600){
        h = N/HORA;
        resto_m = N%HORA;
        m = resto_m/MIN;
        s = resto_m%MIN;
    }
    if (N<3600 && N>=60){ 
        h = 0;
        m = N/MIN;
        s = N%MIN;   
    }
    if (N < 60){
        h = m = 0;
        s = N;
    }
    if (h <= 9){
        if (m <= 9){
            if (s <= 9){
                printf("0%d:0%d:0%d", h, m, s);}
            else
                printf("0%d:0%d:%d", h, m, s);
        }
        else {
            if (s <= 9){
                printf("0%d:%d:0%d", h, m, s);}
            else
                printf("0%d:%d:%d", h, m, s);
        }    
    }
    else {
        if (m <= 9){
            if (s <= 9){
                printf("%d:0%d:0%d", h, m, s);}
            else
                printf("%d:0%d:%d", h, m, s);
        }
        else {
            if (s <= 9){
                printf("%d:%d:0%d", h, m, s);}
            else
                printf("%d:%d:%d", h, m, s);
        }
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_013",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "15b501534631abeff61adade11fa9ef7954e23151b523ac5083279babf7804ea",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_014 — train

```c


#include <stdio.h>

int main(){
    int n,h,m,s;
    scanf("%d", &n);
    h = (n-n%3600)/3600;
    m = (n%3600-((n%3600)%60))/60;
    s = ((n%3600)%60);
    if(h<10 && m<10 && s<10){
        printf("0%d:0%d:0%d",h,m,s);
        return 0;
    }
    if(h<10 && m<10){
        printf("0%d:0%d:%d",h,m,s);
        return 0;
    }
    if(h<10 && s<10){
        printf("0%d:%d:0%d",h,m,s);
        return 0;
    }
    if(m<10 && s<10){
        printf("%d:0%d:0%d",h,m,s);
        return 0; 
    }
    if(h<10){
        printf("0%d:%d:%d",h,m,s);
        return 0;
    }
    if(m<10){
        printf("%d:0%d:%d",h,m,s);
        return 0;
    }
    if(s<10){
        printf("%d:%d:0%d",h,m,s);
        return 0;
    }
    return 0;
}

```

```json
{
  "sample_id": "sample_014",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "dcc458dbcde71060a02ab45b386caad7cbd66373ad7545b6074522b1ec41d57f",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_015 — train

```c

#include <stdio.h>

int main()
{
    int horas, minutos, segundos;
    int n;
    scanf("%d", &n);
    horas = n / 3600;
    minutos = (n / 60) - horas * 60;
    segundos = n % 60;


    printf("%02d:%02d:%02d", horas, minutos, segundos);

    return 0;
}
```

```json
{
  "sample_id": "sample_015",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "2780c94c3d7b0e5710dd1614e5830ae3c4138cb516eb086e4d81f1ae29d95f4c",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_016 — train

```c

#include <stdio.h>

int main(){
    int time, h, m, s;

    scanf("%d", &time);
    h = time/3600;
    m = (time - h*3600 )/ 60;
    s = time - h*3600 - m*60;

    printf("%02d:%02d:%02d", h, m, s);
    return 0;
}
```

```json
{
  "sample_id": "sample_016",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "7af2c5c515cfb9b0222d6b007b8577442ddb8f998c76411ece3388cf75f4720c",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_017 — train

```c

#include <stdio.h>
int main()
{
    int valor, horas, minutos, segundos;
    scanf("%d", &valor);
    horas = valor / 3600; 
    minutos = (valor % 3600) / 60; 
    segundos = valor % 60;
    printf("%02d:%02d:%02d", horas, minutos, segundos);
    return 0;
}

```

```json
{
  "sample_id": "sample_017",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "a49a8a613518ecc6c927daeb6bc52c5c2183847ba86b372c3c3222497272b81b",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_018 — train

```c


#include <stdio.h>

int main(){

    int n, h = 0, min = 0, s = 0, res;

    scanf("%d", &n);

    if(n >= 3600){ 
        h = n / 3600; 
        res = n % 3600; 
        min = res / 60; 
        s = res % 60; 
        }
    else{ 
        min = n / 60;
        s = n % 60;
    }

    printf("%02d:%02d:%02d", h, min, s);
    return 0;
}
```

```json
{
  "sample_id": "sample_018",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "08339f7dfde14df094557739fe3eac1ae3eed9997f32efd27cc26639e988f066",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_019 — train

```c

#include <stdio.h>

int N, seg, min, horas;

int main () {
    scanf("%d", &N);

    horas = N / (60*60);
    N = N - (horas * 60*60);
    min = N / 60;
    seg = N - (min * 60);
    
    if (horas < 10) {
        if (min < 10) {
            if (seg < 10)
                printf("0%d:0%d:0%d", horas, min, seg);
            else
                printf("0%d:0%d:%d", horas, min, seg);
        }
        else {
            if (seg < 10)
                printf("0%d:%d:0%d", horas, min, seg);
            else
                printf("0%d:%d:%d", horas, min, seg);
        }
    }
    else {
        if (min < 10) {
            if (seg < 10)
                printf("%d:0%d:0%d", horas, min, seg);
            else
                printf("%d:0%d:%d", horas, min, seg);
        }
        else {
            if (seg < 10)
                printf("%d:%d:0%d", horas, min, seg);
            else
                printf("%d:%d:%d", horas, min, seg);
        }                    
    }

    return 0;
}
```

```json
{
  "sample_id": "sample_019",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "cb67f6717e7b6a6fe606dc0024dc34a67534bf28828234d84f6023a7d9fc4392",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_020 — train

```c


#include <stdio.h>

int main()
{
    int seg = 0, min = 0, hr = 0;
    scanf("%d",&seg);
    min = seg / 60;
    seg = seg % 60;
    hr = min / 60;
    min = min % 60;
    printf("%02d:%02d:%02d",hr,min,seg);
    return 0;
}
```

```json
{
  "sample_id": "sample_020",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "c8932452a840e2f67379e63a4b01b8936c0c798d7957bc6874b54c381c76b097",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_021 — train

```c
#include <stdio.h>

int main () {
	int N, HH, MM, SS;
	
	scanf("%d", &N);
	
	SS = N%60;
	N = (N-SS)/60;
	MM = N%60;
	HH = (N-MM)/60;

	printf("%02d:%02d:%02d", HH, MM, SS);
	
	return 0;	
}

```

```json
{
  "sample_id": "sample_021",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "56337d851ba94af1e467937a28605181a923b1a0fc6481ed2dc8b02583e2619f",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_022 — train

```c

#include <stdio.h>

int main(){
    int sec, min, min_em_sec, hour;
    int total_sec;

    scanf("%d",&total_sec);

    hour = total_sec / 3600;
    min_em_sec = total_sec % 3600; 
    
    min = min_em_sec / 60;
    sec = min_em_sec % 60;

    printf("%02d:%02d:%02d",hour,min,sec);

    return 0;
}
```

```json
{
  "sample_id": "sample_022",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "f3d8f0e9715f73868890cf8041ec20597f3b4f29c4f7503863ce4c51a8537a46",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_023 — validation

```c

#include <stdio.h>
#define DIVHORAS 3600
#define DIVMIN 60

int main(void){

    int horas,minutos,segundos;
    int n;
    int resto;

    scanf("%d",&n);

    horas = n / DIVHORAS;
    resto = n % DIVHORAS;
    minutos = resto / DIVMIN;
    segundos= resto % DIVMIN;


    
    printf("%2.2d:%2.2d:%2.2d",horas,minutos,segundos);


    return 0;
}
```

```json
{
  "sample_id": "sample_023",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "51ac9bd8c755efe8696f95c359c2dcb5398b7155944ca89fe8d83ba2c434a4d3",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_024 — train

```c

#include <stdio.h>
#define LIMITE 60

int main(){
    int m=0,h=0,s;
    scanf("%d",&s);
    if (s>=LIMITE){
        m=s/LIMITE;
        s=s%LIMITE;
    }
    if (m>=LIMITE){
        h=m/60;
        m=m%60;
    }
    printf("%02d:%02d:%02d",h,m,s);
    return 0;
}
```

```json
{
  "sample_id": "sample_024",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "e0f87ef936cf551aae4257a0d1d374f064a9bc93b1ed8738c7124e2a1249cc67",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_025 — train

```c

# include <stdio.h>

int main(){
    int seconds,minutes=0,hours=0;

    scanf("%d",&seconds);
    minutes = seconds/60;
    if (minutes>60)
        hours = minutes/60;
    minutes -= hours * 60;
    seconds -= (hours*3600 + minutes*60);

    if (hours<10)
        printf("0%d:",hours);
    else
        printf("%d:",hours);
    if (minutes<10)
        printf("0%d:",minutes);
    else
        printf("%d:",minutes);
    if (seconds<10)
        printf("0%d",seconds);
    else
        printf("%d",seconds);     
    
    return 0;
}
```

```json
{
  "sample_id": "sample_025",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "574e50bfd550a184e57d63cd26b28ae67aadf39f4f962f39b19171eba487a5d5",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "00:60:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_027 — train

```c

#include <stdio.h>

int main() {
    int segundos, horas, minutos, resto;
    scanf("%d", &resto);
    horas = resto / 3600;
    resto = resto % 3600;
    minutos = resto / 60;
    segundos = resto % 60;
    printf("%.2d:%.2d:%.2d", horas, minutos, segundos);
    return 0;
}
```

```json
{
  "sample_id": "sample_027",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "f97abca9ce22c1b85583b76e88805467e3dc395e19a45a77b1eb70e6d84ce7e0",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_028 — validation

```c

#include <stdio.h>
int main(){
    int s;
    scanf("%d",&s);
    printf("%02d:%02d:%02d",s/3600,(s % 3600)/60,(s%3600)%60);
    return 0;
}
```

```json
{
  "sample_id": "sample_028",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "44793381104125b59a37119b5caee3ebc57f7a9be5cd3ac18df4976574aeeb61",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "whitespace",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "whitespace",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "whitespace",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## Evidence refs hợp lệ

```json
[
  "test_statistics",
  "feature_statistics",
  "learned_if_then_rules",
  "semantic_findings",
  "problem_statement",
  "members/sample_001/raw_code",
  "members/sample_001/tests/ex09_0",
  "members/sample_001/tests/ex09_1",
  "members/sample_001/tests/ex09_2",
  "members/sample_001/tests/ex09_3",
  "members/sample_002/raw_code",
  "members/sample_002/tests/ex09_0",
  "members/sample_002/tests/ex09_1",
  "members/sample_002/tests/ex09_2",
  "members/sample_002/tests/ex09_3",
  "members/sample_003/raw_code",
  "members/sample_003/tests/ex09_0",
  "members/sample_003/tests/ex09_1",
  "members/sample_003/tests/ex09_2",
  "members/sample_003/tests/ex09_3",
  "members/sample_004/raw_code",
  "members/sample_004/tests/ex09_0",
  "members/sample_004/tests/ex09_1",
  "members/sample_004/tests/ex09_2",
  "members/sample_004/tests/ex09_3",
  "members/sample_005/raw_code",
  "members/sample_005/tests/ex09_0",
  "members/sample_005/tests/ex09_1",
  "members/sample_005/tests/ex09_2",
  "members/sample_005/tests/ex09_3",
  "members/sample_006/raw_code",
  "members/sample_006/tests/ex09_0",
  "members/sample_006/tests/ex09_1",
  "members/sample_006/tests/ex09_2",
  "members/sample_006/tests/ex09_3",
  "members/sample_007/raw_code",
  "members/sample_007/tests/ex09_0",
  "members/sample_007/tests/ex09_1",
  "members/sample_007/tests/ex09_2",
  "members/sample_007/tests/ex09_3",
  "members/sample_008/raw_code",
  "members/sample_008/tests/ex09_0",
  "members/sample_008/tests/ex09_1",
  "members/sample_008/tests/ex09_2",
  "members/sample_008/tests/ex09_3",
  "members/sample_009/raw_code",
  "members/sample_009/tests/ex09_0",
  "members/sample_009/tests/ex09_1",
  "members/sample_009/tests/ex09_2",
  "members/sample_009/tests/ex09_3",
  "members/sample_010/raw_code",
  "members/sample_010/tests/ex09_0",
  "members/sample_010/tests/ex09_1",
  "members/sample_010/tests/ex09_2",
  "members/sample_010/tests/ex09_3",
  "members/sample_011/raw_code",
  "members/sample_011/tests/ex09_0",
  "members/sample_011/tests/ex09_1",
  "members/sample_011/tests/ex09_2",
  "members/sample_011/tests/ex09_3",
  "members/sample_012/raw_code",
  "members/sample_012/tests/ex09_0",
  "members/sample_012/tests/ex09_1",
  "members/sample_012/tests/ex09_2",
  "members/sample_012/tests/ex09_3",
  "members/sample_013/raw_code",
  "members/sample_013/tests/ex09_0",
  "members/sample_013/tests/ex09_1",
  "members/sample_013/tests/ex09_2",
  "members/sample_013/tests/ex09_3",
  "members/sample_014/raw_code",
  "members/sample_014/tests/ex09_0",
  "members/sample_014/tests/ex09_1",
  "members/sample_014/tests/ex09_2",
  "members/sample_014/tests/ex09_3",
  "members/sample_015/raw_code",
  "members/sample_015/tests/ex09_0",
  "members/sample_015/tests/ex09_1",
  "members/sample_015/tests/ex09_2",
  "members/sample_015/tests/ex09_3",
  "members/sample_016/raw_code",
  "members/sample_016/tests/ex09_0",
  "members/sample_016/tests/ex09_1",
  "members/sample_016/tests/ex09_2",
  "members/sample_016/tests/ex09_3",
  "members/sample_017/raw_code",
  "members/sample_017/tests/ex09_0",
  "members/sample_017/tests/ex09_1",
  "members/sample_017/tests/ex09_2",
  "members/sample_017/tests/ex09_3",
  "members/sample_018/raw_code",
  "members/sample_018/tests/ex09_0",
  "members/sample_018/tests/ex09_1",
  "members/sample_018/tests/ex09_2",
  "members/sample_018/tests/ex09_3",
  "members/sample_019/raw_code",
  "members/sample_019/tests/ex09_0",
  "members/sample_019/tests/ex09_1",
  "members/sample_019/tests/ex09_2",
  "members/sample_019/tests/ex09_3",
  "members/sample_020/raw_code",
  "members/sample_020/tests/ex09_0",
  "members/sample_020/tests/ex09_1",
  "members/sample_020/tests/ex09_2",
  "members/sample_020/tests/ex09_3",
  "members/sample_021/raw_code",
  "members/sample_021/tests/ex09_0",
  "members/sample_021/tests/ex09_1",
  "members/sample_021/tests/ex09_2",
  "members/sample_021/tests/ex09_3",
  "members/sample_022/raw_code",
  "members/sample_022/tests/ex09_0",
  "members/sample_022/tests/ex09_1",
  "members/sample_022/tests/ex09_2",
  "members/sample_022/tests/ex09_3",
  "members/sample_023/raw_code",
  "members/sample_023/tests/ex09_0",
  "members/sample_023/tests/ex09_1",
  "members/sample_023/tests/ex09_2",
  "members/sample_023/tests/ex09_3",
  "members/sample_024/raw_code",
  "members/sample_024/tests/ex09_0",
  "members/sample_024/tests/ex09_1",
  "members/sample_024/tests/ex09_2",
  "members/sample_024/tests/ex09_3",
  "members/sample_025/raw_code",
  "members/sample_025/tests/ex09_0",
  "members/sample_025/tests/ex09_1",
  "members/sample_025/tests/ex09_2",
  "members/sample_025/tests/ex09_3",
  "members/sample_026/raw_code",
  "members/sample_026/tests/ex09_0",
  "members/sample_026/tests/ex09_1",
  "members/sample_026/tests/ex09_2",
  "members/sample_027/raw_code",
  "members/sample_027/tests/ex09_0",
  "members/sample_027/tests/ex09_1",
  "members/sample_027/tests/ex09_2",
  "members/sample_027/tests/ex09_3",
  "members/sample_028/raw_code",
  "members/sample_028/tests/ex09_0",
  "members/sample_028/tests/ex09_1",
  "members/sample_028/tests/ex09_2",
  "members/sample_028/tests/ex09_3"
]
```
