# lab02-ex01--kmeans--combined_stdout--s42--c2

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 13; phân vùng: {'train': 13}.


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
    "test_id": "ex01_1",
    "n_cluster": 13,
    "n_observed": 13,
    "n_failed": 12,
    "n_not_run": 0,
    "failure_rate_observed": 0.9230769230769231,
    "failure_rate_cluster": 0.9230769230769231,
    "outcome_counts": {
      "fail": 12,
      "pass": 1
    }
  },
  {
    "test_id": "ex01_2",
    "n_cluster": 13,
    "n_observed": 13,
    "n_failed": 4,
    "n_not_run": 0,
    "failure_rate_observed": 0.3076923076923077,
    "failure_rate_cluster": 0.3076923076923077,
    "outcome_counts": {
      "pass": 9,
      "fail": 4
    }
  },
  {
    "test_id": "ex01_0",
    "n_cluster": 13,
    "n_observed": 13,
    "n_failed": 1,
    "n_not_run": 0,
    "failure_rate_observed": 0.07692307692307693,
    "failure_rate_cluster": 0.07692307692307693,
    "outcome_counts": {
      "pass": 12,
      "fail": 1
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex01_0:edit_band",
    "value": "__unknown__",
    "n": 12,
    "n_cluster": 13,
    "rate": 0.9230769230769231,
    "cohort_rate": 0.08641975308641975,
    "difference_from_cohort": 0.8366571699905034
  },
  {
    "feature": "stdout:ex01_0:relation",
    "value": "__unknown__",
    "n": 12,
    "n_cluster": 13,
    "rate": 0.9230769230769231,
    "cohort_rate": 0.08641975308641975,
    "difference_from_cohort": 0.8366571699905034
  },
  {
    "feature": "test:ex01_0",
    "value": "pass",
    "n": 12,
    "n_cluster": 13,
    "rate": 0.9230769230769231,
    "cohort_rate": 0.08641975308641975,
    "difference_from_cohort": 0.8366571699905034
  },
  {
    "feature": "stdout:ex01_2:edit_band",
    "value": "__unknown__",
    "n": 9,
    "n_cluster": 13,
    "rate": 0.6923076923076923,
    "cohort_rate": 0.05555555555555555,
    "difference_from_cohort": 0.6367521367521367
  },
  {
    "feature": "stdout:ex01_2:relation",
    "value": "__unknown__",
    "n": 9,
    "n_cluster": 13,
    "rate": 0.6923076923076923,
    "cohort_rate": 0.05555555555555555,
    "difference_from_cohort": 0.6367521367521367
  },
  {
    "feature": "test:ex01_2",
    "value": "pass",
    "n": 9,
    "n_cluster": 13,
    "rate": 0.6923076923076923,
    "cohort_rate": 0.05555555555555555,
    "difference_from_cohort": 0.6367521367521367
  },
  {
    "feature": "stdout:ex01_1:relation",
    "value": "different",
    "n": 11,
    "n_cluster": 13,
    "rate": 0.8461538461538461,
    "cohort_rate": 0.5925925925925926,
    "difference_from_cohort": 0.2535612535612536
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 4,
    "n_cluster": 13,
    "rate": 0.3076923076923077,
    "cohort_rate": 0.09876543209876543,
    "difference_from_cohort": 0.20892687559354228
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "0",
    "n": 4,
    "n_cluster": 13,
    "rate": 0.3076923076923077,
    "cohort_rate": 0.12345679012345678,
    "difference_from_cohort": 0.18423551756885093
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 4,
    "n_cluster": 13,
    "rate": 0.3076923076923077,
    "cohort_rate": 0.14814814814814814,
    "difference_from_cohort": 0.15954415954415957
  },
  {
    "feature": "ast:c_while",
    "value": "0",
    "n": 13,
    "n_cluster": 13,
    "rate": 1.0,
    "cohort_rate": 0.8765432098765432,
    "difference_from_cohort": 0.12345679012345678
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 4,
    "n_cluster": 13,
    "rate": 0.3076923076923077,
    "cohort_rate": 0.19135802469135801,
    "difference_from_cohort": 0.1163342830009497
  },
  {
    "feature": "stdout:ex01_1:edit_band",
    "value": "large",
    "n": 9,
    "n_cluster": 13,
    "rate": 0.6923076923076923,
    "cohort_rate": 0.5864197530864198,
    "difference_from_cohort": 0.10588793922127249
  },
  {
    "feature": "stdout:ex01_1:edit_band",
    "value": "__unknown__",
    "n": 1,
    "n_cluster": 13,
    "rate": 0.07692307692307693,
    "cohort_rate": 0.012345679012345678,
    "difference_from_cohort": 0.06457739791073125
  },
  {
    "feature": "stdout:ex01_1:relation",
    "value": "__unknown__",
    "n": 1,
    "n_cluster": 13,
    "rate": 0.07692307692307693,
    "cohort_rate": 0.012345679012345678,
    "difference_from_cohort": 0.06457739791073125
  },
  {
    "feature": "test:ex01_1",
    "value": "pass",
    "n": 1,
    "n_cluster": 13,
    "rate": 0.07692307692307693,
    "cohort_rate": 0.012345679012345678,
    "difference_from_cohort": 0.06457739791073125
  },
  {
    "feature": "ast:c_if",
    "value": "0",
    "n": 2,
    "n_cluster": 13,
    "rate": 0.15384615384615385,
    "cohort_rate": 0.10493827160493827,
    "difference_from_cohort": 0.04890788224121559
  },
  {
    "feature": "ast:c_subscript",
    "value": "0",
    "n": 13,
    "n_cluster": 13,
    "rate": 1.0,
    "cohort_rate": 0.9691358024691358,
    "difference_from_cohort": 0.030864197530864224
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 13,
    "n_cluster": 13,
    "rate": 1.0,
    "cohort_rate": 0.9876543209876543,
    "difference_from_cohort": 0.012345679012345734
  },
  {
    "feature": "ast:c_one_index",
    "value": "0",
    "n": 13,
    "n_cluster": 13,
    "rate": 1.0,
    "cohort_rate": 0.9876543209876543,
    "difference_from_cohort": 0.012345679012345734
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 13,
    "n_cluster": 13,
    "rate": 1.0,
    "cohort_rate": 0.9876543209876543,
    "difference_from_cohort": 0.012345679012345734
  },
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 13,
    "n_cluster": 13,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 11,
    "n_cluster": 13,
    "rate": 0.8461538461538461,
    "cohort_rate": 0.8950617283950617,
    "difference_from_cohort": -0.04890788224121556
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 9,
    "n_cluster": 13,
    "rate": 0.6923076923076923,
    "cohort_rate": 0.8765432098765432,
    "difference_from_cohort": -0.18423551756885093
  }
]
```


## IF–THEN dự đoán cluster, không dự đoán gold

```json
[
  {
    "rule_id": 3,
    "if": [
      "NOT (stdout:ex01_0:edit_band=large)",
      "NOT (stdout:ex01_0:relation=whitespace)",
      "NOT (stdout:ex01_1:edit_band=medium)"
    ],
    "then_cluster": 2,
    "train_support": 9,
    "train_precision": 1.0,
    "holdout_support": 2,
    "holdout_precision": 0.0
  },
  {
    "rule_id": 4,
    "if": [
      "NOT (stdout:ex01_0:edit_band=large)",
      "NOT (stdout:ex01_0:relation=whitespace)",
      "stdout:ex01_1:edit_band=medium"
    ],
    "then_cluster": 2,
    "train_support": 4,
    "train_precision": 0.75,
    "holdout_support": 0,
    "holdout_precision": null
  }
]
```


## Candidate chưa xác thực

```json
{
  "source": "local_heuristic_not_gold",
  "misconception_name": "Chưa đủ bằng chứng để đặt tên lỗi",
  "misconception_type": null,
  "reasoning": "Có 13 bài trong cụm. Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
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

sample_003, sample_009, sample_006, sample_010

## sample_003 — train — đại diện

```c

#include<stdio.h>

int main(){
    int v1, v2, v3, maximo;
    scanf("%d%d%d", &v1, &v2, &v3);

    if(v1<v2 && v3<v2)
    maximo = v2;

    if(v1>v2 && v3>v2)
    maximo = v1;

    if(v1<v2 && v3>v2)
    maximo = v3;

    printf("%d\n", maximo);
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
  "source_sha256": "1744e1bb3b96d1fa01ca5392c8af97cd9b61234b5209e2a6039ed6c6da9c8eda",
  "outcomes": {
    "ex01_0": "pass",
    "ex01_1": "fail",
    "ex01_2": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "0\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "pass",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex01_0:relation": "__unknown__",
    "stdout:ex01_0:edit_band": "__unknown__",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "__unknown__",
    "stdout:ex01_2:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "pass",
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


## sample_006 — train — đại diện

```c

#include <stdio.h>

int main() 
{
    int n1, n2, n3;
    scanf("%d%d%d", &n1, &n2, &n3);

    if (n1 >= n2 && n1 >= n3) {
        printf("%d/n", n1);
    }
    else if (n2 >= n3 && n2 >= n3) {
        printf("%d/n", n2);
    }
    else {
        printf("%d\n", n3);
    }
    return 0;
}




```

```json
{
  "sample_id": "sample_006",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "9658238a25d0793995e50a544b63ebd27998cf9d8d9354dc9fb37855c3453f64",
  "outcomes": {
    "ex01_0": "pass",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6/n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3/n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex01_0:relation": "__unknown__",
    "stdout:ex01_0:edit_band": "__unknown__",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_009 — train — đại diện

```c

# include <stdio.h>

int main()
{
    int valor1, valor2, valor3 ;
    scanf("%d %d %d",&valor1, &valor2, &valor3);
    return printf("%d\n", valor1>valor2 ? (valor1 > valor3? valor1 : valor2 > valor3? valor2 : valor3): valor2) == EOF;
 
    
}
```

```json
{
  "sample_id": "sample_009",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "176573a818df503af4cccc771eeea4ed4204b239f8e6d233f10613cb000dd252",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "pass",
    "ex01_2": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "2\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "pass",
    "test:ex01_2": "pass",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "__unknown__",
    "stdout:ex01_1:edit_band": "__unknown__",
    "stdout:ex01_2:relation": "__unknown__",
    "stdout:ex01_2:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "pass",
    "test:ex01_2": "pass",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_010 — train — đại diện

```c


#include <stdio.h>

int main(){

    int i, maior, num;

    maior =scanf("%d", &num);

    for (i = 0; i < 3; i++){

        scanf("%d", &num);

        if (num > maior)
            maior = num;
    }

    printf("%d\n", num);

    return 0;
}

```

```json
{
  "sample_id": "sample_010",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "4a07643fb7e911cba672f7e2f3b8711738f01df4b5c577f934e21c883cfb820e",
  "outcomes": {
    "ex01_0": "pass",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "1\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "1\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "__unknown__",
    "stdout:ex01_0:edit_band": "__unknown__",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_001 — train

```c
#include <stdio.h>

int main()
{
	int i, n, maior = scanf("%d", &n);
	for(i = 0; i < 2; i++)
	{
		scanf("%d", &n);
		maior = n > maior ? n : maior;
	}
	printf("%d\n", maior);
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
  "source_sha256": "7731cb1426cb50f96b408965c840e897e091a70eb91ca7d962e06dd6f45e5317",
  "outcomes": {
    "ex01_0": "pass",
    "ex01_1": "fail",
    "ex01_2": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "2\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "pass",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "__unknown__",
    "stdout:ex01_0:edit_band": "__unknown__",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "__unknown__",
    "stdout:ex01_2:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "pass",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_002 — train

```c
#include <stdio.h>

int main()
{
	int n,i,z;
	scanf("%d",&n);
	scanf("%d\n",&i);
	scanf("%d\n",&z);
	if (n>i && n>z)
	printf("%d\n",n);
	if (i>z)
	printf("%d\n",i);
	else
	printf("%d\n",z);
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
  "source_sha256": "701b9a654dc278ca39f0b8de683bfc6fecf0b1b9fe0a189aa373777aaea44216",
  "outcomes": {
    "ex01_0": "pass",
    "ex01_1": "fail",
    "ex01_2": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6\n2\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "pass",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex01_0:relation": "__unknown__",
    "stdout:ex01_0:edit_band": "__unknown__",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "__unknown__",
    "stdout:ex01_2:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "pass",
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

#include<stdio.h>

int main(){
    int v1, v2, v3, maximo;
    scanf("%d%d%d", &v1, &v2, &v3);

    if(v1<v2 && v3<v2)
    maximo = v2;

    if(v1>v2 && v3>v2)
    maximo = v1;

    if(v1<v2 && v3>v2)
    maximo = v3;

    printf("%d\n", maximo);
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
  "source_sha256": "1744e1bb3b96d1fa01ca5392c8af97cd9b61234b5209e2a6039ed6c6da9c8eda",
  "outcomes": {
    "ex01_0": "pass",
    "ex01_1": "fail",
    "ex01_2": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "0\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "pass",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex01_0:relation": "__unknown__",
    "stdout:ex01_0:edit_band": "__unknown__",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "__unknown__",
    "stdout:ex01_2:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "pass",
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


## sample_005 — train

```c

#include <stdio.h>

int main(){
    
    int num1, num2, num3;

    scanf("%d %d %d", &num1, &num2, &num3);

    if ((num1 > num2) & (num1 > num3)){
        printf("%d\n", num1);
    }
    if ((num2 > num1) & (num2 > num3)){
        printf("%d\n", num2);
    }
    else{
        printf("%d\n", num3);
    }
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
  "source_sha256": "2f48386faa58478ec547ca79f53e28a20e92a11d9af1f391b825ca9325b134c3",
  "outcomes": {
    "ex01_0": "pass",
    "ex01_1": "fail",
    "ex01_2": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6\n1\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "pass",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex01_0:relation": "__unknown__",
    "stdout:ex01_0:edit_band": "__unknown__",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "__unknown__",
    "stdout:ex01_2:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "pass",
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


## sample_007 — train

```c

#include <stdio.h>

int main() 
{
    int n1, n2, n3;
    scanf("%d%d%d", &n1, &n2, &n3);

    if (n1 >= n2 && n1 >= n3) {
        printf("%d/n", n1);
    }
    else if (n2 >= n3 && n2 >= n3) {
        printf("%d/n", n2);
    }
    else {
        printf("%d\n", n3);
    }
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
  "source_sha256": "38cf4150228067eef43da721e1a643ced03b4db4115f592d937fc662d823edd2",
  "outcomes": {
    "ex01_0": "pass",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6/n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3/n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex01_0:relation": "__unknown__",
    "stdout:ex01_0:edit_band": "__unknown__",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_008 — train

```c

#include <stdio.h>

int main() 
{
    int n1, n2, n3;
    scanf("%d%d%d", &n1, &n2, &n3);

    if (n1 >= n2 && n1 >= n3) {
        printf("%d/n", n1);
    }
    else if (n2 >= n3 && n2 >= n3) {
        printf("%d\n", n2);
    }
    else {
        printf("%d\n", n3);
    }
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
  "source_sha256": "be046e02aefec897eaa0e6fea3b686651b08e0b04e2f1c23825112b311887575",
  "outcomes": {
    "ex01_0": "pass",
    "ex01_1": "fail",
    "ex01_2": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6/n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "pass",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex01_0:relation": "__unknown__",
    "stdout:ex01_0:edit_band": "__unknown__",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "__unknown__",
    "stdout:ex01_2:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "pass",
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

    int i, maior, num;

    scanf("%d", &maior);

    for (i = 0; i < 3; i++){

        scanf("%d", &num);

        if (num > maior)
            maior = num;
    }

    printf("%d\n", num);

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
  "source_sha256": "f627a7d7f6fc460530ff3d776d5c9d2103809068be17bf7403a7e3b3e8305238",
  "outcomes": {
    "ex01_0": "pass",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "1\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "1\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "__unknown__",
    "stdout:ex01_0:edit_band": "__unknown__",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_012 — train

```c

#include <stdio.h>

int main () {
    int x,y,z;
    scanf("%d %d %d", &x, &y, &z);
    if (x>=y && x>=z)
        printf("%d \n", x);
    else if (y>=z && y>=x)
        printf("%d\n", y);
    else
        printf("%d\n", z);
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
  "source_sha256": "e65d83937cd7f216117f375fe1879ae1b43b961acfb32cba3e2e1d595347760c",
  "outcomes": {
    "ex01_0": "pass",
    "ex01_1": "fail",
    "ex01_2": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6 \n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "pass",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex01_0:relation": "__unknown__",
    "stdout:ex01_0:edit_band": "__unknown__",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "__unknown__",
    "stdout:ex01_2:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "pass",
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


## sample_013 — train

```c


#include <stdio.h>
#define QUANTIDADE 3

int main ()
{
    int x, max, i;

    for(i = 0; i < QUANTIDADE; i++)
    {
        scanf("%d",&x);
        if (i == 1)
            max = x;
        else
        {
            if (x > max)
                max = x;
        }
    }

    printf("%d\n", max);
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
  "source_sha256": "af5bc090e9c77210d247a96954fbc3e427703f669bf539fc3748c9cd1f40431f",
  "outcomes": {
    "ex01_0": "pass",
    "ex01_1": "fail",
    "ex01_2": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "2\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "pass",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "__unknown__",
    "stdout:ex01_0:edit_band": "__unknown__",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "__unknown__",
    "stdout:ex01_2:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "pass",
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
  "members/sample_001/tests/ex01_1",
  "members/sample_002/raw_code",
  "members/sample_002/tests/ex01_1",
  "members/sample_003/raw_code",
  "members/sample_003/tests/ex01_1",
  "members/sample_004/raw_code",
  "members/sample_004/tests/ex01_1",
  "members/sample_005/raw_code",
  "members/sample_005/tests/ex01_1",
  "members/sample_006/raw_code",
  "members/sample_006/tests/ex01_1",
  "members/sample_006/tests/ex01_2",
  "members/sample_007/raw_code",
  "members/sample_007/tests/ex01_1",
  "members/sample_007/tests/ex01_2",
  "members/sample_008/raw_code",
  "members/sample_008/tests/ex01_1",
  "members/sample_009/raw_code",
  "members/sample_009/tests/ex01_0",
  "members/sample_010/raw_code",
  "members/sample_010/tests/ex01_1",
  "members/sample_010/tests/ex01_2",
  "members/sample_011/raw_code",
  "members/sample_011/tests/ex01_1",
  "members/sample_011/tests/ex01_2",
  "members/sample_012/raw_code",
  "members/sample_012/tests/ex01_1",
  "members/sample_013/raw_code",
  "members/sample_013/tests/ex01_1"
]
```
