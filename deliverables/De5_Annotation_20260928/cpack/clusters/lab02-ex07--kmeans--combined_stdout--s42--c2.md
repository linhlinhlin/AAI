# lab02-ex07--kmeans--combined_stdout--s42--c2

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 28; phân vùng: {'train': 17, 'validation': 11}.


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
    "test_id": "ex07_1",
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
    "test_id": "ex07_2",
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
    "test_id": "ex07_0",
    "n_cluster": 28,
    "n_observed": 28,
    "n_failed": 26,
    "n_not_run": 0,
    "failure_rate_observed": 0.9285714285714286,
    "failure_rate_cluster": 0.9285714285714286,
    "outcome_counts": {
      "fail": 26,
      "pass": 2
    }
  },
  {
    "test_id": "ex07_3",
    "n_cluster": 28,
    "n_observed": 28,
    "n_failed": 26,
    "n_not_run": 0,
    "failure_rate_observed": 0.9285714285714286,
    "failure_rate_cluster": 0.9285714285714286,
    "outcome_counts": {
      "fail": 26,
      "pass": 2
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex07_1:edit_band",
    "value": "large",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.509090909090909,
    "difference_from_cohort": 0.49090909090909096
  },
  {
    "feature": "stdout:ex07_0:edit_band",
    "value": "large",
    "n": 26,
    "n_cluster": 28,
    "rate": 0.9285714285714286,
    "cohort_rate": 0.4727272727272727,
    "difference_from_cohort": 0.4558441558441559
  },
  {
    "feature": "stdout:ex07_2:edit_band",
    "value": "large",
    "n": 27,
    "n_cluster": 28,
    "rate": 0.9642857142857143,
    "cohort_rate": 0.509090909090909,
    "difference_from_cohort": 0.45519480519480526
  },
  {
    "feature": "stdout:ex07_2:relation",
    "value": "different",
    "n": 23,
    "n_cluster": 28,
    "rate": 0.8214285714285714,
    "cohort_rate": 0.41818181818181815,
    "difference_from_cohort": 0.40324675324675324
  },
  {
    "feature": "stdout:ex07_3:edit_band",
    "value": "large",
    "n": 26,
    "n_cluster": 28,
    "rate": 0.9285714285714286,
    "cohort_rate": 0.5272727272727272,
    "difference_from_cohort": 0.4012987012987014
  },
  {
    "feature": "stdout:ex07_1:relation",
    "value": "different",
    "n": 22,
    "n_cluster": 28,
    "rate": 0.7857142857142857,
    "cohort_rate": 0.4,
    "difference_from_cohort": 0.3857142857142857
  },
  {
    "feature": "stdout:ex07_0:relation",
    "value": "different",
    "n": 21,
    "n_cluster": 28,
    "rate": 0.75,
    "cohort_rate": 0.38181818181818183,
    "difference_from_cohort": 0.36818181818181817
  },
  {
    "feature": "stdout:ex07_3:relation",
    "value": "different",
    "n": 21,
    "n_cluster": 28,
    "rate": 0.75,
    "cohort_rate": 0.43636363636363634,
    "difference_from_cohort": 0.31363636363636366
  },
  {
    "feature": "ast:c_while",
    "value": "0",
    "n": 12,
    "n_cluster": 28,
    "rate": 0.42857142857142855,
    "cohort_rate": 0.2909090909090909,
    "difference_from_cohort": 0.13766233766233765
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 10,
    "n_cluster": 28,
    "rate": 0.35714285714285715,
    "cohort_rate": 0.2545454545454545,
    "difference_from_cohort": 0.10259740259740263
  },
  {
    "feature": "stdout:ex07_0:relation",
    "value": "empty",
    "n": 5,
    "n_cluster": 28,
    "rate": 0.17857142857142858,
    "cohort_rate": 0.09090909090909091,
    "difference_from_cohort": 0.08766233766233766
  },
  {
    "feature": "stdout:ex07_1:relation",
    "value": "empty",
    "n": 5,
    "n_cluster": 28,
    "rate": 0.17857142857142858,
    "cohort_rate": 0.09090909090909091,
    "difference_from_cohort": 0.08766233766233766
  },
  {
    "feature": "stdout:ex07_2:relation",
    "value": "empty",
    "n": 5,
    "n_cluster": 28,
    "rate": 0.17857142857142858,
    "cohort_rate": 0.09090909090909091,
    "difference_from_cohort": 0.08766233766233766
  },
  {
    "feature": "stdout:ex07_3:relation",
    "value": "empty",
    "n": 5,
    "n_cluster": 28,
    "rate": 0.17857142857142858,
    "cohort_rate": 0.09090909090909091,
    "difference_from_cohort": 0.08766233766233766
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 17,
    "n_cluster": 28,
    "rate": 0.6071428571428571,
    "cohort_rate": 0.5454545454545454,
    "difference_from_cohort": 0.06168831168831168
  },
  {
    "feature": "test:ex07_1",
    "value": "fail",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.9454545454545454,
    "difference_from_cohort": 0.054545454545454564
  },
  {
    "feature": "ast:c_if",
    "value": "0",
    "n": 3,
    "n_cluster": 28,
    "rate": 0.10714285714285714,
    "cohort_rate": 0.05454545454545454,
    "difference_from_cohort": 0.052597402597402594
  },
  {
    "feature": "ast:c_update",
    "value": "0",
    "n": 3,
    "n_cluster": 28,
    "rate": 0.10714285714285714,
    "cohort_rate": 0.05454545454545454,
    "difference_from_cohort": 0.052597402597402594
  },
  {
    "feature": "test:ex07_2",
    "value": "fail",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.9636363636363636,
    "difference_from_cohort": 0.036363636363636376
  },
  {
    "feature": "ast:c_address_of",
    "value": "0",
    "n": 2,
    "n_cluster": 28,
    "rate": 0.07142857142857142,
    "cohort_rate": 0.03636363636363636,
    "difference_from_cohort": 0.03506493506493506
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 17,
    "n_cluster": 28,
    "rate": 0.6071428571428571,
    "cohort_rate": 0.5454545454545454,
    "difference_from_cohort": 0.06168831168831168
  },
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 26,
    "n_cluster": 28,
    "rate": 0.9285714285714286,
    "cohort_rate": 0.9636363636363636,
    "difference_from_cohort": -0.03506493506493502
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 25,
    "n_cluster": 28,
    "rate": 0.8928571428571429,
    "cohort_rate": 0.9454545454545454,
    "difference_from_cohort": -0.05259740259740253
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 25,
    "n_cluster": 28,
    "rate": 0.8928571428571429,
    "cohort_rate": 0.9454545454545454,
    "difference_from_cohort": -0.05259740259740253
  },
  {
    "feature": "ast:c_while",
    "value": "1",
    "n": 16,
    "n_cluster": 28,
    "rate": 0.5714285714285714,
    "cohort_rate": 0.7090909090909091,
    "difference_from_cohort": -0.1376623376623377
  }
]
```


## IF–THEN dự đoán cluster, không dự đoán gold

```json
[
  {
    "rule_id": 4,
    "if": [
      "stdout:ex07_1:edit_band=large"
    ],
    "then_cluster": 2,
    "train_support": 17,
    "train_precision": 1.0,
    "holdout_support": 11,
    "holdout_precision": 1.0
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

sample_003, sample_011, sample_018, sample_016

## sample_003 — train — đại diện

```c
#include <stdio.h>
int main()
{
 int N,cont;
 scanf ("%d",&N);

 for (cont = 1; cont<=N; cont++)
   {
     if (N%cont == 0)
         {
          printf ("%d\n",cont);
         } 
   }

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
  "source_sha256": "e6dc571f8aa16d5f88d7156763eb4ea6b90d36eb4fe4c6e457a6ae37f99b0103",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": "1\n2\n4\n8\n"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "1\n5\n"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "1\n13\n"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "1\n2\n5\n10\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "1",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_011 — validation — đại diện

```c


#include <stdio.h>

int main () {
	int n, counter = 2, i;
	scanf("%d", &n);
	if (n <= 0) return 1;
	if (n == 1) {
		printf("%d\n", 1);
		return 0;
	}
	for (i = 1; i < (n / 2); i++) {
		if ((n % i) == 0)
			counter++;
	}
	printf("%d\n", counter);
	return 0;
}
```

```json
{
  "sample_id": "sample_011",
  "partition": "validation",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "57ddca563d875324c3b31d4105e83b8d8ef30b865e53eb09b9c531a55b612e9c",
  "outcomes": {
    "ex07_0": "pass",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "3\n"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "3\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "pass",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "__unknown__",
    "stdout:ex07_0:edit_band": "__unknown__",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "__unknown__",
    "stdout:ex07_3:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex07_0": "pass",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "ast:c_for": "1",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_016 — train — đại diện

```c

#include <stdio.h>
int main(){
    int contador = 0, divisores = 1;
    int num;
    float resto;
    scanf("%d", &num);
    resto = num % divisores;
    while (divisores < num){
        if (resto == 0.0)
            contador++;
        divisores++;
    }
    printf("%d\n", contador);
    return 0;
}
```

```json
{
  "sample_id": "sample_016",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "991ca0411c12a83664e19438173c2e86313926301911f6bd0eff62cb72ef651e",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": "7\n"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "4\n"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "12\n"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "9\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "other_oracle",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_018 — train — đại diện

```c

#include <stdio.h>

int main()
{
    
    return 0;
}

```

```json
{
  "sample_id": "sample_018",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "ce5edfbc66ad1cf94d74c5714ca131707e5685eb9ca5ff6db612a994787989e6",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": ""
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": ""
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": ""
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "0",
    "ast:c_update": "0",
    "stdout:ex07_0:relation": "empty",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "empty",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "empty",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "empty",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
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
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_001 — train

```c
#include <stdio.h>



int main() {
    int N, contador, divisores;
    divisores = 0;

    scanf("%d", &N);
    for (contador = 1; contador <= N; contador++) {
        if ((N % contador) == 0) {
            divisores++;
        }
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_001",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "37524c6d9d71038a59eb91bd487ca214b99ebda68d84763824d56a3e21e45ad7",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": ""
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": ""
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": ""
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "empty",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "empty",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "empty",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "empty",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "1",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_002 — train

```c
#include <stdio.h>



int main()
{
    int n, i;
    scanf("%d", &n);
    for (i=1; i<n; i++)
    {
        if (n/i == 0)
            printf("%d", i);
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_002",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "f2fb44477329ee0295279e8834037f48bf130fb3b74ecef56204697ae2763c03",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": ""
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": ""
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": ""
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "empty",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "empty",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "empty",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "empty",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "1",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_004 — train

```c
#include <stdio.h>

int main(){
    int n, i;
    scanf("%d", &n);
    for(i = 1; i <= n / 2; ++i){
        if (n % i == 0){
            printf("%d\n", i);
        }
    }
    printf("%d\n", n);
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
  "source_sha256": "d1ae428f615a406d1bfdded717c7a09a679cebf21fa895ff43c5a36a986440c6",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": "1\n2\n4\n8\n"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "1\n5\n"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "1\n13\n"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "1\n2\n5\n10\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "1",
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
    "ast:c_update": "1",
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
  int n, count = 0;

  scanf("%d", &n);
  while (count++ <= n)
    if (n % count == 0)
      printf("%d\n", n);

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
  "source_sha256": "f31f5a7131410841a9607101a35c4da23bbcbc913d90d854d11d730ebdfb5562",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": "8\n8\n8\n8\n"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "5\n5\n"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "13\n13\n"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "10\n10\n10\n10\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_006 — validation

```c
#include <stdio.h>

int main()
{
    int n, div = 0, i = 1;
    printf("Introduza um inteiro positivo.\n");
    scanf("%d", &n);
    while(i <= n){
        if(n % i == 0)
            ++div;
        ++i;
    }
    printf("%d", div);
    return 0;
}
```

```json
{
  "sample_id": "sample_006",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "9e4c389db57338de3d094398b83ddec3b444a1913d762316f0e81fd7ee73ea9c",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": "Introduza um inteiro positivo.\n4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "Introduza um inteiro positivo.\n2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "Introduza um inteiro positivo.\n2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "Introduza um inteiro positivo.\n4"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_007 — validation

```c
#include <stdio.h>

int main()
{
    int n, div = 0, i = 1;
    printf("Introduza um inteiro positivo.\n");
    scanf("%d", &n);
    while(i <= n){
        if(n % i == 0)
            ++div;
        ++i;
    }
    printf("O seu número tem %d divisor(es)\n", div);
    return 0;
}
```

```json
{
  "sample_id": "sample_007",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "a260bc16088509e7673172170f66d8ce794e0749178fd20c4333928f1415c069",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": "Introduza um inteiro positivo.\nO seu número tem 4 divisor(es)\n"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "Introduza um inteiro positivo.\nO seu número tem 2 divisor(es)\n"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "Introduza um inteiro positivo.\nO seu número tem 2 divisor(es)\n"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "Introduza um inteiro positivo.\nO seu número tem 4 divisor(es)\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_008 — validation

```c
#include <stdio.h>

int main()
{
    int n, div = 0, i = 1;
    printf("Introduza um inteiro positivo.\n");
    scanf("%d", &n);
    while(i <= n){
        if(n % i == 0)
            ++div;
        ++i;
    }
    printf("%d\n", div);
    return 0;
}
```

```json
{
  "sample_id": "sample_008",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "fbcd21e605f22526e094c8132c7bd2a2e2d74f98399889c0d8e6541c60839d39",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": "Introduza um inteiro positivo.\n4\n"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "Introduza um inteiro positivo.\n2\n"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "Introduza um inteiro positivo.\n2\n"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "Introduza um inteiro positivo.\n4\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_009 — train

```c


#include <stdio.h>

int main(){
    
    int N, V;
    scanf("%d",&N);
    
    V = 1;
    
    while(V<=N){
        if(N%V==0){
            printf("%d\n",V);
        }
        V++;
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_009",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "0b87055ff9b4cea3792c449d821feb3ddcc1879bf67a22966ab352237b77fffb",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": "1\n2\n4\n8\n"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "1\n5\n"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "1\n13\n"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "1\n2\n5\n10\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_010 — train

```c

#include<stdio.h>

int main (){

int a, b, contador ;

contador = 1;
b = 0 ;

printf("Insira o numero pff\n");

scanf("%d", &a) ;

while ( contador <= a){

    if ( a % contador == 0 ){
       
        b = b +1 ;


    }

    contador = contador + 1 ;

}

printf ( "o numero de divisores de %d é %d\n " , a , b );

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
  "source_sha256": "395c182dc69e2ad82d4d70c0ef1476330dfa61b056bf3faba1eee1c29864b5d2",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": "Insira o numero pff\no numero de divisores de 8 é 4\n "
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "Insira o numero pff\no numero de divisores de 5 é 2\n "
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "Insira o numero pff\no numero de divisores de 13 é 2\n "
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "Insira o numero pff\no numero de divisores de 10 é 4\n "
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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


## sample_012 — validation

```c



#include <stdio.h>

int main () {
	int n, counter = 2, i;
	scanf("%d", &n);
	if (n <= 0) return 1;
	if (n == 1) {
		printf("%d\n", 1);
		return 0;
	}
	for (i = 1; i < (n / 2); i++) {
		if ((n % i) == 0)
			counter++;
	}
	printf("%d\n", counter);
	return 0;
}
```

```json
{
  "sample_id": "sample_012",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "e6273d88045a25a147cac8140aa8440cfd3c12531dcdb8e445715c89dc5f7004",
  "outcomes": {
    "ex07_0": "pass",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "3\n"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "3\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "pass",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "__unknown__",
    "stdout:ex07_0:edit_band": "__unknown__",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "__unknown__",
    "stdout:ex07_3:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex07_0": "pass",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "ast:c_for": "1",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_013 — train

```c

#include <stdio.h>

int main()
{
    int num1, primos, i;

    scanf("%d", &num1);
    primos = 0;

    for (i = num1 / 2; i > 0; i--)
    {
        if (num1 % i == 0)
        {
            primos++;
        }
    }

    printf("%d\n", primos);

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
  "source_sha256": "3f0868b583d99da35a71aa6a46d9f00824ab9adef3ef38b267344803af473d7a",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": "3\n"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "1\n"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "1\n"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "3\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "1",
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
    "ast:c_update": "1",
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
    int contador = 0, divisores = 1;
    int num;
    float resto;
    scanf("%d", &num);        
    resto = num % divisores;
    while (divisores <= num){
        if (resto == 0.0)
            contador++;
        divisores++;
    }
    printf("%d\n", contador);
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
  "source_sha256": "ea82959e959d359baf6ace19e62fb77808308053fcaa41ce0f57d781ab253b3c",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": "8\n"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "5\n"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "13\n"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "10\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_015 — train

```c

#include <stdio.h>
int main(){
    int contador = 0, divisores = 1;
    int num;
    float resto;
    scanf("%d", &num);
    resto = num % divisores;
    while (divisores <= num){
        if (resto == 0.0)
            contador++;
        divisores++;
    }
    printf("%d\n", contador);
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
  "source_sha256": "4bd3b730e5b64b53bbf77d594a70799709fc0a0f25e959de446110f8aa6ad73d",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": "8\n"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "5\n"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "13\n"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "10\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_update": "1",
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
    int N, i, d;
    d=0;
    scanf("%d", &N);
    i=N;
    while (--i)
    {
        if (N%i==0)
        {
            d++;
        }
    }
    printf("%d", d);
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
  "source_sha256": "6a6d3a226ddb6b769fd57ac712f42648a0d70ea1595dd5d1383d34f0778afcac",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": "3"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "1"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "1"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_019 — validation

```c

#include <stdio.h>
int main(){
    int N, i = 1, contador = 0;
    
    printf("Introduza um numero inteiro:\n");
    scanf("%d", &N);

    while(i <= N){
        if(N % i == 0){
            contador++;
        }
        i++;
    }
    printf("%d\n", contador);
    return 0;
}
```

```json
{
  "sample_id": "sample_019",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "17a23d1159953467069fb697cf2808e0f4b36f54c8338156f9333a95b3317234",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": "Introduza um numero inteiro:\n4\n"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "Introduza um numero inteiro:\n2\n"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "Introduza um numero inteiro:\n2\n"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "Introduza um numero inteiro:\n4\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_020 — validation

```c

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main(){
    return 0;
}
```

```json
{
  "sample_id": "sample_020",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "f49c4fb585cc7b8c0a22f0fec550b668029b4e2884e7826195fe790fde87361c",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": ""
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": ""
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": ""
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "0",
    "ast:c_update": "0",
    "stdout:ex07_0:relation": "empty",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "empty",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "empty",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "empty",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
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
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_021 — validation

```c

#include <stdio.h>

int main() {
    int n, contador, total;
    
    contador = 1;
    total = 0;

    scanf("%d", &n);

    while (contador <= (n/2)) {
        if (!(n % contador)) {
            ++total;
        }
    ++contador;
    }
    printf("%d\n", total);
    return 0;
}
```

```json
{
  "sample_id": "sample_021",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "5a1337c17ec4cf9c709da6fa7c3761b4102f012dab2d631592b19ee6a0cd9325",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": "3\n"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "1\n"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "1\n"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "3\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_022 — validation

```c

#include <stdio.h>

int main() {
    int n, contador, total;
    
    contador = 0;
    total = 0;

    scanf("%d", &n);

    while (contador <= (n/2)) {
        ++contador;
        if (!(n % contador)) {
            ++total;
        }
    }
    printf("%d\n", total);
    return 0;
}
```

```json
{
  "sample_id": "sample_022",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "461dc11efbea44452224b6d1c93456903576e336e2b34030de411ae77ee0eeb3",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": "3\n"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "1\n"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "1\n"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "3\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_023 — validation

```c

#include <stdio.h>

int main() {
    int n, contador, total;
    
    contador = 0;
    total = 0;

    scanf("%d", &n);

    while (contador < (n/2)) {
        ++contador;
        if (!(n % contador)) {
            ++total;
        }
    printf("%d\n", total);
    }
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
  "source_sha256": "0caa6ba671dd821260852ab6f954c776b54655673a3e00f4b5c2755442bf830f",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": "1\n2\n2\n3\n"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "1\n1\n"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "1\n1\n1\n1\n1\n1\n"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "1\n2\n2\n2\n3\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_024 — validation

```c

#include <stdio.h>

int main() {
    int n, contador, total;
    
    contador = 0;
    total = 0;

    scanf("%d", &n);

    while (contador < (n/2)) {
        ++contador;
        if (!(n % contador)) {
            ++total;
        }
    }
    printf("%d\n", total);
    return 0;
}
```

```json
{
  "sample_id": "sample_024",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "24e0bb2d967e49a17528e57127d2adb7ff864efd5a47b01caefb4a57e5cc1152",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": "3\n"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "1\n"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "1\n"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "3\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_025 — train

```c


#include <stdio.h>

int main() 
{
    int contador, n, contador2;
    scanf("%d", &n);
    contador = n + 1;
    contador2 = 0;
        while (contador--) {
            printf("%d asj\n", contador);
            if (contador != 0 && n % contador == 0) {
                printf("%d a\n", contador);
                printf("%d\n o", contador2);
                contador2 ++;
        }
    }
    printf("%d\n", contador2);
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
  "source_sha256": "f273b38d42a76dc6e3d4073afa368c74a0285bf37c2e9834082d9360a908bee9",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": "8 asj\n8 a\n0\n o7 asj\n6 asj\n5 asj\n4 asj\n4 a\n1\n o3 asj\n2 asj\n2 a\n2\n o1 asj\n1 a\n3\n o0 asj\n4\n"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "5 asj\n5 a\n0\n o4 asj\n3 asj\n2 asj\n1 asj\n1 a\n1\n o0 asj\n2\n"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "13 asj\n13 a\n0\n o12 asj\n11 asj\n10 asj\n9 asj\n8 asj\n7 asj\n6 asj\n5 asj\n4 asj\n3 asj\n2 asj\n1 asj\n1 a\n1\n o0 asj\n2\n"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "10 asj\n10 a\n0\n o9 asj\n8 asj\n7 asj\n6 asj\n5 asj\n5 a\n1\n o4 asj\n3 asj\n2 asj\n2 a\n2\n o1 asj\n1 a\n3\n o0 asj\n4\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_026 — train

```c

#include <stdio.h>

int main(){
    int N,i,divisores=0;
    scanf("%d",&N);

    for(i=1;i<N;i++){
        if(N%i==0){
            divisores++;
        }
    }
    printf("%d\n",divisores);
    return 0;
}
```

```json
{
  "sample_id": "sample_026",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "683848b092e0e2942e32f9089444483a4480e54e23f11a19ae401334715ed465",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": "3\n"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "1\n"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "1\n"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "3\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "1",
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
    "ast:c_update": "1",
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
    int n, i;

    scanf("%d", &n);
    for(i = 1; i <=n; i++)
        printf("%d\n", i);
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
  "source_sha256": "34f77322d6a5d92b4c6c656f1dde18d26981bf86f1a31a4dcb32e72c768ebfd4",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": "1\n2\n3\n4\n5\n6\n7\n8\n"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "1\n2\n3\n4\n5\n"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "different",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_028 — train

```c

#include <stdio.h>

int main ()
{
    int i, n, cont;
    cont = 0;
    
    scanf("%d",&n);
    for (i = n; i > 0;i--)
    {
        if ((n % i) == 0)
            cont++;
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_028",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "ec91ed0e9beb427ae08b1deb80299b275256f37df0d22c85a5223b86fdcdc1d0",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8",
      "expected": "4\n",
      "output": ""
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": ""
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": ""
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "empty",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "empty",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "empty",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "empty",
    "stdout:ex07_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "1",
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
    "ast:c_update": "1",
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
  "members/sample_001/tests/ex07_0",
  "members/sample_001/tests/ex07_1",
  "members/sample_001/tests/ex07_2",
  "members/sample_001/tests/ex07_3",
  "members/sample_002/raw_code",
  "members/sample_002/tests/ex07_0",
  "members/sample_002/tests/ex07_1",
  "members/sample_002/tests/ex07_2",
  "members/sample_002/tests/ex07_3",
  "members/sample_003/raw_code",
  "members/sample_003/tests/ex07_0",
  "members/sample_003/tests/ex07_1",
  "members/sample_003/tests/ex07_2",
  "members/sample_003/tests/ex07_3",
  "members/sample_004/raw_code",
  "members/sample_004/tests/ex07_0",
  "members/sample_004/tests/ex07_1",
  "members/sample_004/tests/ex07_2",
  "members/sample_004/tests/ex07_3",
  "members/sample_005/raw_code",
  "members/sample_005/tests/ex07_0",
  "members/sample_005/tests/ex07_1",
  "members/sample_005/tests/ex07_2",
  "members/sample_005/tests/ex07_3",
  "members/sample_006/raw_code",
  "members/sample_006/tests/ex07_0",
  "members/sample_006/tests/ex07_1",
  "members/sample_006/tests/ex07_2",
  "members/sample_006/tests/ex07_3",
  "members/sample_007/raw_code",
  "members/sample_007/tests/ex07_0",
  "members/sample_007/tests/ex07_1",
  "members/sample_007/tests/ex07_2",
  "members/sample_007/tests/ex07_3",
  "members/sample_008/raw_code",
  "members/sample_008/tests/ex07_0",
  "members/sample_008/tests/ex07_1",
  "members/sample_008/tests/ex07_2",
  "members/sample_008/tests/ex07_3",
  "members/sample_009/raw_code",
  "members/sample_009/tests/ex07_0",
  "members/sample_009/tests/ex07_1",
  "members/sample_009/tests/ex07_2",
  "members/sample_009/tests/ex07_3",
  "members/sample_010/raw_code",
  "members/sample_010/tests/ex07_0",
  "members/sample_010/tests/ex07_1",
  "members/sample_010/tests/ex07_2",
  "members/sample_010/tests/ex07_3",
  "members/sample_011/raw_code",
  "members/sample_011/tests/ex07_1",
  "members/sample_011/tests/ex07_2",
  "members/sample_012/raw_code",
  "members/sample_012/tests/ex07_1",
  "members/sample_012/tests/ex07_2",
  "members/sample_013/raw_code",
  "members/sample_013/tests/ex07_0",
  "members/sample_013/tests/ex07_1",
  "members/sample_013/tests/ex07_2",
  "members/sample_013/tests/ex07_3",
  "members/sample_014/raw_code",
  "members/sample_014/tests/ex07_0",
  "members/sample_014/tests/ex07_1",
  "members/sample_014/tests/ex07_2",
  "members/sample_014/tests/ex07_3",
  "members/sample_015/raw_code",
  "members/sample_015/tests/ex07_0",
  "members/sample_015/tests/ex07_1",
  "members/sample_015/tests/ex07_2",
  "members/sample_015/tests/ex07_3",
  "members/sample_016/raw_code",
  "members/sample_016/tests/ex07_0",
  "members/sample_016/tests/ex07_1",
  "members/sample_016/tests/ex07_2",
  "members/sample_016/tests/ex07_3",
  "members/sample_017/raw_code",
  "members/sample_017/tests/ex07_0",
  "members/sample_017/tests/ex07_1",
  "members/sample_017/tests/ex07_2",
  "members/sample_017/tests/ex07_3",
  "members/sample_018/raw_code",
  "members/sample_018/tests/ex07_0",
  "members/sample_018/tests/ex07_1",
  "members/sample_018/tests/ex07_2",
  "members/sample_018/tests/ex07_3",
  "members/sample_019/raw_code",
  "members/sample_019/tests/ex07_0",
  "members/sample_019/tests/ex07_1",
  "members/sample_019/tests/ex07_2",
  "members/sample_019/tests/ex07_3",
  "members/sample_020/raw_code",
  "members/sample_020/tests/ex07_0",
  "members/sample_020/tests/ex07_1",
  "members/sample_020/tests/ex07_2",
  "members/sample_020/tests/ex07_3",
  "members/sample_021/raw_code",
  "members/sample_021/tests/ex07_0",
  "members/sample_021/tests/ex07_1",
  "members/sample_021/tests/ex07_2",
  "members/sample_021/tests/ex07_3",
  "members/sample_022/raw_code",
  "members/sample_022/tests/ex07_0",
  "members/sample_022/tests/ex07_1",
  "members/sample_022/tests/ex07_2",
  "members/sample_022/tests/ex07_3",
  "members/sample_023/raw_code",
  "members/sample_023/tests/ex07_0",
  "members/sample_023/tests/ex07_1",
  "members/sample_023/tests/ex07_2",
  "members/sample_023/tests/ex07_3",
  "members/sample_024/raw_code",
  "members/sample_024/tests/ex07_0",
  "members/sample_024/tests/ex07_1",
  "members/sample_024/tests/ex07_2",
  "members/sample_024/tests/ex07_3",
  "members/sample_025/raw_code",
  "members/sample_025/tests/ex07_0",
  "members/sample_025/tests/ex07_1",
  "members/sample_025/tests/ex07_2",
  "members/sample_025/tests/ex07_3",
  "members/sample_026/raw_code",
  "members/sample_026/tests/ex07_0",
  "members/sample_026/tests/ex07_1",
  "members/sample_026/tests/ex07_2",
  "members/sample_026/tests/ex07_3",
  "members/sample_027/raw_code",
  "members/sample_027/tests/ex07_0",
  "members/sample_027/tests/ex07_1",
  "members/sample_027/tests/ex07_2",
  "members/sample_027/tests/ex07_3",
  "members/sample_028/raw_code",
  "members/sample_028/tests/ex07_0",
  "members/sample_028/tests/ex07_1",
  "members/sample_028/tests/ex07_2",
  "members/sample_028/tests/ex07_3"
]
```
