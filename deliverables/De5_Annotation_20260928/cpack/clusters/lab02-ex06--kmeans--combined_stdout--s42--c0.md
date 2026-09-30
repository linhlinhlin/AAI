# lab02-ex06--kmeans--combined_stdout--s42--c0

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 28; phân vùng: {'train': 24, 'validation': 4}.


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
    "test_id": "ex06_0",
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
    "test_id": "ex06_1",
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
    "test_id": "ex06_2",
    "n_cluster": 28,
    "n_observed": 28,
    "n_failed": 28,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 28
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "test:ex06_2",
    "value": "fail",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.6071428571428571,
    "difference_from_cohort": 0.3928571428571429
  },
  {
    "feature": "test:ex06_0",
    "value": "fail",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.7142857142857143,
    "difference_from_cohort": 0.2857142857142857
  },
  {
    "feature": "stdout:ex06_2:relation",
    "value": "different",
    "n": 18,
    "n_cluster": 28,
    "rate": 0.6428571428571429,
    "cohort_rate": 0.42857142857142855,
    "difference_from_cohort": 0.21428571428571436
  },
  {
    "feature": "stdout:ex06_0:edit_band",
    "value": "large",
    "n": 11,
    "n_cluster": 28,
    "rate": 0.39285714285714285,
    "cohort_rate": 0.19642857142857142,
    "difference_from_cohort": 0.19642857142857142
  },
  {
    "feature": "stdout:ex06_1:edit_band",
    "value": "large",
    "n": 11,
    "n_cluster": 28,
    "rate": 0.39285714285714285,
    "cohort_rate": 0.19642857142857142,
    "difference_from_cohort": 0.19642857142857142
  },
  {
    "feature": "test:ex06_1",
    "value": "fail",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.8035714285714286,
    "difference_from_cohort": 0.1964285714285714
  },
  {
    "feature": "stdout:ex06_2:edit_band",
    "value": "large",
    "n": 10,
    "n_cluster": 28,
    "rate": 0.35714285714285715,
    "cohort_rate": 0.17857142857142858,
    "difference_from_cohort": 0.17857142857142858
  },
  {
    "feature": "stdout:ex06_2:edit_band",
    "value": "medium",
    "n": 10,
    "n_cluster": 28,
    "rate": 0.35714285714285715,
    "cohort_rate": 0.17857142857142858,
    "difference_from_cohort": 0.17857142857142858
  },
  {
    "feature": "stdout:ex06_0:relation",
    "value": "different",
    "n": 18,
    "n_cluster": 28,
    "rate": 0.6428571428571429,
    "cohort_rate": 0.5357142857142857,
    "difference_from_cohort": 0.1071428571428572
  },
  {
    "feature": "stdout:ex06_0:relation",
    "value": "empty",
    "n": 6,
    "n_cluster": 28,
    "rate": 0.21428571428571427,
    "cohort_rate": 0.10714285714285714,
    "difference_from_cohort": 0.10714285714285714
  },
  {
    "feature": "stdout:ex06_1:relation",
    "value": "empty",
    "n": 6,
    "n_cluster": 28,
    "rate": 0.21428571428571427,
    "cohort_rate": 0.10714285714285714,
    "difference_from_cohort": 0.10714285714285714
  },
  {
    "feature": "stdout:ex06_2:relation",
    "value": "empty",
    "n": 6,
    "n_cluster": 28,
    "rate": 0.21428571428571427,
    "cohort_rate": 0.10714285714285714,
    "difference_from_cohort": 0.10714285714285714
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "0",
    "n": 22,
    "n_cluster": 28,
    "rate": 0.7857142857142857,
    "cohort_rate": 0.6785714285714286,
    "difference_from_cohort": 0.1071428571428571
  },
  {
    "feature": "stdout:ex06_1:edit_band",
    "value": "medium",
    "n": 5,
    "n_cluster": 28,
    "rate": 0.17857142857142858,
    "cohort_rate": 0.08928571428571429,
    "difference_from_cohort": 0.08928571428571429
  },
  {
    "feature": "ast:c_if",
    "value": "0",
    "n": 5,
    "n_cluster": 28,
    "rate": 0.17857142857142858,
    "cohort_rate": 0.10714285714285714,
    "difference_from_cohort": 0.07142857142857144
  },
  {
    "feature": "stdout:ex06_0:relation",
    "value": "whitespace",
    "n": 4,
    "n_cluster": 28,
    "rate": 0.14285714285714285,
    "cohort_rate": 0.07142857142857142,
    "difference_from_cohort": 0.07142857142857142
  },
  {
    "feature": "stdout:ex06_1:relation",
    "value": "whitespace",
    "n": 4,
    "n_cluster": 28,
    "rate": 0.14285714285714285,
    "cohort_rate": 0.07142857142857142,
    "difference_from_cohort": 0.07142857142857142
  },
  {
    "feature": "stdout:ex06_2:relation",
    "value": "whitespace",
    "n": 4,
    "n_cluster": 28,
    "rate": 0.14285714285714285,
    "cohort_rate": 0.07142857142857142,
    "difference_from_cohort": 0.07142857142857142
  },
  {
    "feature": "ast:c_address_of",
    "value": "0",
    "n": 3,
    "n_cluster": 28,
    "rate": 0.10714285714285714,
    "cohort_rate": 0.05357142857142857,
    "difference_from_cohort": 0.05357142857142857
  },
  {
    "feature": "stdout:ex06_0:edit_band",
    "value": "medium",
    "n": 3,
    "n_cluster": 28,
    "rate": 0.10714285714285714,
    "cohort_rate": 0.05357142857142857,
    "difference_from_cohort": 0.05357142857142857
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_while",
    "value": "1",
    "n": 15,
    "n_cluster": 28,
    "rate": 0.5357142857142857,
    "cohort_rate": 0.48214285714285715,
    "difference_from_cohort": 0.05357142857142855
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
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 25,
    "n_cluster": 28,
    "rate": 0.8928571428571429,
    "cohort_rate": 0.9107142857142857,
    "difference_from_cohort": -0.017857142857142794
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 21,
    "n_cluster": 28,
    "rate": 0.75,
    "cohort_rate": 0.7678571428571429,
    "difference_from_cohort": -0.017857142857142905
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 25,
    "n_cluster": 28,
    "rate": 0.8928571428571429,
    "cohort_rate": 0.9464285714285714,
    "difference_from_cohort": -0.05357142857142849
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 23,
    "n_cluster": 28,
    "rate": 0.8214285714285714,
    "cohort_rate": 0.8928571428571429,
    "difference_from_cohort": -0.07142857142857151
  }
]
```


## IF–THEN dự đoán cluster, không dự đoán gold

```json
[
  {
    "rule_id": 3,
    "if": [
      "NOT (stdout:ex06_0:relation=__unknown__)",
      "NOT (stdout:ex06_2:relation=__unknown__)",
      "NOT (ast:c_inclusive_comparison=0)"
    ],
    "then_cluster": 0,
    "train_support": 7,
    "train_precision": 0.8571428571428571,
    "holdout_support": 0,
    "holdout_precision": null
  },
  {
    "rule_id": 4,
    "if": [
      "NOT (stdout:ex06_0:relation=__unknown__)",
      "NOT (stdout:ex06_2:relation=__unknown__)",
      "ast:c_inclusive_comparison=0"
    ],
    "then_cluster": 0,
    "train_support": 18,
    "train_precision": 1.0,
    "holdout_support": 4,
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

sample_005, sample_018, sample_003, sample_007

## sample_003 — train — đại diện

```c
#include <stdio.h>

int main()
{

    int N, cont = 1, l, min, max;

    scanf("%d", &N);
    scanf("%d", &min);
    scanf("%d", &max);

    if (min > max){        
        l = max;
        max = min;
        min = l;
    }

    while (cont <= N-2){
        scanf("%d", &l);
        if (l < min)
            min = l;
        else if (l > max)
            max = l;
        cont++;
    }

    printf("min: %d, max: %d\n", min, max);
    return 0;
}
```

```json
{
  "sample_id": "sample_003",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "6fabbd19457f6eb31c601af26e8f293a605d12741e409d5ea04a719ba171ae2a",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "min: 1, max: 32764\n"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "min: 6, max: 32764\n"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "min: -1, max: 32766\n"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex06_0:relation": "different",
    "stdout:ex06_0:edit_band": "medium",
    "stdout:ex06_1:relation": "different",
    "stdout:ex06_1:edit_band": "large",
    "stdout:ex06_2:relation": "different",
    "stdout:ex06_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_005 — train — đại diện

```c

#include <stdio.h>

int main()
{
    int num1, i;
    float num2, min, max;

    scanf("%d", &num1);

    for (i = 0; i < num1; i++)
    {
        if (i == 0)
        {
            scanf("%f", &num2);
            min = num2;
            max = num2;
        }
        else
        {
            if (min > num2)
            {
                min = num2;
            }
            else if (max < num2)
            {
                max = num2;
            }
        }
    }

    printf("min: %f, max: %f\n", min, max);

    return 0;
}

```

```json
{
  "sample_id": "sample_005",
  "partition": "train",
  "representative": true,
  "is_train_medoid": true,
  "raw_code_truncated": false,
  "source_sha256": "9a92cfc0b7883152394cf131b732aafa25c4a5609b0a5789f40fe097db921268",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "min: 1.500000, max: 1.500000\n"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "min: 6.800000, max: 6.800000\n"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "min: -1.800000, max: -1.800000\n"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex06_0:relation": "different",
    "stdout:ex06_0:edit_band": "small",
    "stdout:ex06_1:relation": "different",
    "stdout:ex06_1:edit_band": "small",
    "stdout:ex06_2:relation": "different",
    "stdout:ex06_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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


## sample_007 — train — đại diện

```c


#include <stdio.h>

int main ()
{
    int N, i = 0;
    float numintrod;

    scanf("%d", &N);

    while (i < N)
    {
        scanf("%f", &numintrod);
        i = i + numintrod;
    }
     return 0;
    
}
```

```json
{
  "sample_id": "sample_007",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "11a2e851481edf1a91bf8c60c2c4add5389bd1a6903a144b8bc92c92d5e5e507",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": ""
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": ""
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex06_0:relation": "empty",
    "stdout:ex06_0:edit_band": "large",
    "stdout:ex06_1:relation": "empty",
    "stdout:ex06_1:edit_band": "large",
    "stdout:ex06_2:relation": "empty",
    "stdout:ex06_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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


## sample_018 — validation — đại diện

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
  "sample_id": "sample_018",
  "partition": "validation",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "f49c4fb585cc7b8c0a22f0fec550b668029b4e2884e7826195fe790fde87361c",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": ""
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": ""
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "0",
    "ast:c_update": "0",
    "stdout:ex06_0:relation": "empty",
    "stdout:ex06_0:edit_band": "large",
    "stdout:ex06_1:relation": "empty",
    "stdout:ex06_1:edit_band": "large",
    "stdout:ex06_2:relation": "empty",
    "stdout:ex06_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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
  int count = 0, i;
  float n, max, min;

  scanf("%d", &i);

  while (count++ < i) {
    scanf("%f", &n);

    if (count == 1) {
      max = n;
      min = n;
    }
    else if (n > max)
      max = n;
    else if (n < min)
      min = n;
  }

  printf("\nmin: %f, max: %f\n", min, max);

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
  "source_sha256": "656a9ce089301e803d590688d6b5e23f771822efff45be93da96652f40c3f3c1",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "\nmin: 1.500000, max: 3.000000\n"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "\nmin: 0.000000, max: 6.800000\n"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "\nmin: -1.800000, max: 3.140000\n"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex06_0:relation": "whitespace",
    "stdout:ex06_0:edit_band": "small",
    "stdout:ex06_1:relation": "whitespace",
    "stdout:ex06_1:edit_band": "small",
    "stdout:ex06_2:relation": "whitespace",
    "stdout:ex06_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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


## sample_002 — train

```c
#include <stdio.h>

int main() {
    int n;
    float x, min, max;

    scanf("%d", &n);
    scanf("%f", &x);

    min = x;
    
    max = x;

    while (--n > 0) {
        scanf("%f", &x);

        if (x > max)
            max = x;
        
        else if (x < min)
            min = x;
    }

    printf("min: %.1f, max: %.1f\n", min, max);
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
  "source_sha256": "ab18f722b4088b86b3e986a09333ae3dc3d3385722b0afac775c673c16eb50f8",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "min: 1.5, max: 3.0\n"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "min: 0.0, max: 6.8\n"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "min: -1.8, max: 3.1\n"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex06_0:relation": "different",
    "stdout:ex06_0:edit_band": "medium",
    "stdout:ex06_1:relation": "different",
    "stdout:ex06_1:edit_band": "medium",
    "stdout:ex06_2:relation": "different",
    "stdout:ex06_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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


## sample_004 — train

```c

#include<stdio.h>

int main(){

int N, contador;
float a , min , max;
printf("Quantos numeros quer inserir?\n" );

scanf("%d", &N) ;
max = -9999 ;    
min = 9999 ;


printf("Digite os numeros\n" );
for (contador = 1 ; contador <= N ; contador++){

    

    scanf ("%f" , &a );

    if ( a > max){

        max = a ;

    }

    else if ( a < min ){

        min = a;
    }

}

printf("min: %f, max: %f\n", min, max);

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
  "source_sha256": "947db9cb89e6360a68db09995a4938cae5fc4b65e25c2cd2c5fa4272ea32db0f",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "Quantos numeros quer inserir?\nDigite os numeros\nmin: 9999.000000, max: 3.000000\n"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "Quantos numeros quer inserir?\nDigite os numeros\nmin: 0.000000, max: 6.800000\n"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "Quantos numeros quer inserir?\nDigite os numeros\nmin: 1.000000, max: 3.140000\n"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex06_0:relation": "different",
    "stdout:ex06_0:edit_band": "large",
    "stdout:ex06_1:relation": "different",
    "stdout:ex06_1:edit_band": "large",
    "stdout:ex06_2:relation": "different",
    "stdout:ex06_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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


## sample_006 — train

```c

#include <stdio.h>

int main()
{
    int num1, i;
    float num2, min, max;

    scanf("%d", &num1);

    for (i = 0; i < num1; i++)
    {
        if (i == 0)
        {
            scanf("%f", &num2);
            min = num2;
            max = num2;
        }
        else
        {
            if (min < num2)
            {
                min = num2;
            }
            else if (max > num2)
            {
                max = num2;
            }
        }
    }

    printf("min: %f, max: %f\n", min, max);

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
  "source_sha256": "d7a6c8e51a1a778f7e4352a183f553cde8af4116b844244dc7d30f441f0fd692",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "min: 1.500000, max: 1.500000\n"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "min: 6.800000, max: 6.800000\n"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "min: -1.800000, max: -1.800000\n"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex06_0:relation": "different",
    "stdout:ex06_0:edit_band": "small",
    "stdout:ex06_1:relation": "different",
    "stdout:ex06_1:edit_band": "small",
    "stdout:ex06_2:relation": "different",
    "stdout:ex06_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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


## sample_008 — train

```c


#include <stdio.h>

int main(void) {

    float min, max, num1, num2, num3, num4, num5, num6, num7;

    scanf("%f %f %f %f %f %f %f", &num1, &num2, &num3, &num4, &num5, &num6, &num7);
    max = num1;
    min = num1;
    if (max < num2)
        max = num2;
    if (max < num3)
        max = num3;
    if (max < num4)
        max = num4;
    if (max < num5)
        max = num5;
    if (max < num6)
        max = num6;
    if (max < num7)
        max = num7;
    if (min > num2)
        min = num2;
    if (min > num3)
        min = num3;
    if (min > num4)
        min = num4;
    if (min > num5)
        min = num5;
    if (min > num6)
        min = num6;
    if (min > num7)
        min = num7;
    printf("min: %f, max: %f\n", min, max);
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
  "source_sha256": "a3faa3b33817324c9066a9a98b150c60ae436abe36fe629f9ae6299462787bdb",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "min: -0.000000, max: 3.000000\n"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "min: -0.000000, max: 6.800000\n"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "min: -483947788107776.000000, max: 3.140000\n"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex06_0:relation": "different",
    "stdout:ex06_0:edit_band": "small",
    "stdout:ex06_1:relation": "different",
    "stdout:ex06_1:edit_band": "small",
    "stdout:ex06_2:relation": "different",
    "stdout:ex06_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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


## sample_009 — train

```c

#include <stdio.h>



#define INICIO 1
#define ZERO 0

int main()
{
    int n, i;
    float min = ZERO, max = ZERO, num;
    scanf("%d", &n);
    for(i = INICIO; i <= n; i++)
    {
        scanf("%f", &num);
        if (i == INICIO)
            max = num;
        else if (i > INICIO && num < max)
        {
            max = min;
            min = num;
        }
    }
    printf("min: %f, max: %f\n", min, max);
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
  "source_sha256": "faa9f6918af7a08ddd276be7a00b1189c7bb7a379ade217518bb0b0681f31f85",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "min: 0.000000, max: 1.500000\n"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "min: 2.000000, max: 0.000000\n"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "min: 0.000000, max: -1.800000\n"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex06_0:relation": "different",
    "stdout:ex06_0:edit_band": "medium",
    "stdout:ex06_1:relation": "different",
    "stdout:ex06_1:edit_band": "medium",
    "stdout:ex06_2:relation": "different",
    "stdout:ex06_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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


## sample_010 — train

```c

#include <stdio.h>



#define INICIO 0

int main()
{
    int n, i;
    float min, max, num;
    scanf("%d", &n);
    for(i = INICIO; i <= n; i++)
    {
        scanf("%f", &num);
        if(num > min)
            max = num;
        else
            min = num;
    }
    printf("min: %f, max: %f\n", min, max);
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
  "source_sha256": "8fc36371fb7c913c34f6758aa0825bc8e4beb5f4044b8de68a414759c49d791d",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "min: 0.000000, max: 3.000000\n"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "min: 0.000000, max: 1.000000\n"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "min: -1.800000, max: 1.000000\n"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex06_0:relation": "different",
    "stdout:ex06_0:edit_band": "small",
    "stdout:ex06_1:relation": "different",
    "stdout:ex06_1:edit_band": "small",
    "stdout:ex06_2:relation": "different",
    "stdout:ex06_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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


## sample_011 — train

```c

#include <stdio.h>



#define INICIO 1
#define ZERO 0

int main()
{
    int n, i;
    float min, max = ZERO, num;
    scanf("%d", &n);
    for(i = INICIO; i <= n; i++)
    {
        scanf("%f", &num);
        if (i == INICIO)
            min = num;
        else if (num < min && min > max)
        {
            max = min;
            min = num;
        }
    }
    printf("min: %f, max: %f\n", min, max);
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
  "source_sha256": "cc98858db242f0955be42feb0ca0563e3510cc95cde3fd9dc1144827e400d52f",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "min: 1.500000, max: 0.000000\n"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "min: 2.000000, max: 6.800000\n"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "min: -1.800000, max: 0.000000\n"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex06_0:relation": "different",
    "stdout:ex06_0:edit_band": "small",
    "stdout:ex06_1:relation": "different",
    "stdout:ex06_1:edit_band": "small",
    "stdout:ex06_2:relation": "different",
    "stdout:ex06_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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


## sample_012 — train

```c

#include <stdio.h>

int main() 
{
    int contador;
    float maior, menor = 10e100, numero;

    scanf("%d", &contador);

    while (contador > 0) 
    {
        scanf("%f", &numero);
        if (numero >= maior)
        {
            maior = numero;
        } 
        
        if (numero <= menor)
        {
            menor = numero;
        }
        
        contador--;   
    }

    printf("min: %f, max: %f", menor, maior);
    
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
  "source_sha256": "efa1ff52227741013b526bd0034590af3d66c325ee6d5f38d38a43d448c3b43e",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "min: 1.500000, max: 3.000000"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "min: 0.000000, max: 6.800000"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "min: -1.800000, max: 3.140000"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex06_0:relation": "whitespace",
    "stdout:ex06_0:edit_band": "small",
    "stdout:ex06_1:relation": "whitespace",
    "stdout:ex06_1:edit_band": "small",
    "stdout:ex06_2:relation": "whitespace",
    "stdout:ex06_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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

int main(){
    int n, valor, menor, maior;
    scanf("%d\n", &n);
    scanf("%d\n", &valor);
    menor=valor;
    maior=valor;
    while(n>0){
        scanf("%d\n", &valor);
        if(valor>maior)
            maior=valor;
        if(valor<menor)
            menor=valor;
        n--;
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
  "source_sha256": "6c1830570d96d69fc1ea3b9dd620965b44f9cdc999dc8cc109f439e12fdbfd34",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": ""
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": ""
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex06_0:relation": "empty",
    "stdout:ex06_0:edit_band": "large",
    "stdout:ex06_1:relation": "empty",
    "stdout:ex06_1:edit_band": "large",
    "stdout:ex06_2:relation": "empty",
    "stdout:ex06_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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


## sample_014 — train

```c


#include <stdio.h>

int main(){
    int n;
    float valor, min, max;
    scanf("%d\n", &n);
    scanf("%f\n", &valor);
    min=valor;
    max=valor;
    while(n>0){
        scanf("%f\n", &valor);
        if(valor>max)
            max=valor;
        if(valor<min)
            min=valor;
        n--;
    printf("min: %f, max: %f\n", min, max);
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
  "source_sha256": "c4d1cde78afe822296a9241ebb587be87883ca529633e770bcf1ac9552a009b0",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "min: 1.500000, max: 2.700000\nmin: 1.500000, max: 3.000000\nmin: 1.500000, max: 3.000000\n"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "min: 2.000000, max: 6.800000\nmin: 1.000000, max: 6.800000\nmin: 0.000000, max: 6.800000\nmin: 0.000000, max: 6.800000\n"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "min: -1.800000, max: 3.140000\nmin: -1.800000, max: 3.140000\nmin: -1.800000, max: 3.140000\n"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex06_0:relation": "different",
    "stdout:ex06_0:edit_band": "large",
    "stdout:ex06_1:relation": "different",
    "stdout:ex06_1:edit_band": "large",
    "stdout:ex06_2:relation": "different",
    "stdout:ex06_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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


## sample_015 — train

```c


#include <stdio.h>

int main(){
    int n, valor, menor, maior;
    scanf("%d\n", &n);
    scanf("%d\n", &valor);
    menor=maior=valor;
    while(n>0){
        scanf("%d\n", &valor);
        if(valor>maior)
            valor = maior;
        if(valor<menor)
            valor = menor;
        n--;
    }
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
  "source_sha256": "4a61c3944308ace05b577e880b4f82297b463dbd6ddcddf89817b231df72a850",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": ""
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": ""
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex06_0:relation": "empty",
    "stdout:ex06_0:edit_band": "large",
    "stdout:ex06_1:relation": "empty",
    "stdout:ex06_1:edit_band": "large",
    "stdout:ex06_2:relation": "empty",
    "stdout:ex06_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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


## sample_016 — train

```c


#include <stdio.h>

int main() {

    int n, i;
    float max , min, atual;

    scanf("%d", &n);
    scanf("%f", &atual);
    min = max =  atual;

    for (i = 0; i < n; i++) {
        scanf("%f", &atual);
        if (atual > max) {
            max = atual;
        }
        else if (atual < min) {
            min = atual;
        }
    }

    printf("min: %f max: %f", min, max);

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
  "source_sha256": "bd5a7739768e9b76213ac9ce8beea376665554113a87e91e51b2b15424e58389",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "min: 1.500000 max: 3.000000"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "min: 0.000000 max: 6.800000"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "min: -1.800000 max: 3.140000"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex06_0:relation": "different",
    "stdout:ex06_0:edit_band": "small",
    "stdout:ex06_1:relation": "different",
    "stdout:ex06_1:edit_band": "small",
    "stdout:ex06_2:relation": "different",
    "stdout:ex06_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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


## sample_017 — validation

```c

#include <stdio.h>

int main() {
    float max, min, num;

    scanf("%f", &num);
    max = min = num;

    while (scanf("%f", &num) < 1) {
        if (num > max) {
            max = num;
        }
        if (num < min) {
            min = num;
        }
    }

    printf("min: %f, max: %f\n", min, max);

    return 0;
}

```

```json
{
  "sample_id": "sample_017",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "d7f2f50bfebb43dace3c0312a6cfecebcb4aa8fca576eff7f1c2b6b544a9adb1",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "min: 3.000000, max: 3.000000\n"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "min: 4.000000, max: 4.000000\n"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "min: 3.000000, max: 3.000000\n"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex06_0:relation": "different",
    "stdout:ex06_0:edit_band": "small",
    "stdout:ex06_1:relation": "different",
    "stdout:ex06_1:edit_band": "medium",
    "stdout:ex06_2:relation": "different",
    "stdout:ex06_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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
int main(){
    int size,counter=1;
    float current,max,min;
    scanf("%d",&size);
    scanf("%f",&current);
    min=current;
    max=current;
    for(;counter<size;counter++){
        scanf("%f",&current);
        if (current>max)
            max=current;
        if (current<min)
            min=current;
        
    }
    printf("min: %3.6f, max; %3.6f\n",min,max);
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
  "source_sha256": "9c91b620bdbc0fbb8f7a3b1098f4e41c14cf19013adfba40068b8530060e04b9",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "min: 1.500000, max; 3.000000\n"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "min: 0.000000, max; 6.800000\n"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "min: -1.800000, max; 3.140000\n"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex06_0:relation": "different",
    "stdout:ex06_0:edit_band": "small",
    "stdout:ex06_1:relation": "different",
    "stdout:ex06_1:edit_band": "small",
    "stdout:ex06_2:relation": "different",
    "stdout:ex06_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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


## sample_020 — train

```c


#include <stdio.h>
#include <float.h>

float greater(float n1, float n2){
    return (n1 > n2) ? n1: n2;
}
float smaller(float n1, float n2){
    return (n1 < n2) ? n1: n2;
}

int main() {

    int n;
    float min = FLT_MAX, max = -FLT_MAX, curr;
    scanf("%d",&n);

    while(n--){
        scanf("%f",&curr);
        min = smaller(min, curr);
        max = greater(max, curr);
    }
    printf("min: %f, max: %f",min,max);
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
  "source_sha256": "a89da79ddd50b71dc2cfdfb5a9310f078ce7337a69ad896377fcd89058a4f496",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "min: 1.500000, max: 3.000000"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "min: 0.000000, max: 6.800000"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "min: -1.800000, max: 3.140000"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex06_0:relation": "whitespace",
    "stdout:ex06_0:edit_band": "small",
    "stdout:ex06_1:relation": "whitespace",
    "stdout:ex06_1:edit_band": "small",
    "stdout:ex06_2:relation": "whitespace",
    "stdout:ex06_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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


## sample_021 — train

```c

#include <stdio.h>

float min, max, num_temp;
int num;

int main () {
    scanf("%f", &min);
    max = min;
    while (scanf("%f", &num_temp) == 0) {
        if (min > num_temp)
            min = num_temp;
        else if (max < num_temp)
            max = num_temp;
    }
    printf("min: %f, max: %f\n", min, max);
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
  "source_sha256": "fd9f939d069a5da2d0d6e4a9d585e7cb6ed4199c662e1218f1dec7f7186336f2",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "min: 3.000000, max: 3.000000\n"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "min: 4.000000, max: 4.000000\n"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "min: 3.000000, max: 3.000000\n"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex06_0:relation": "different",
    "stdout:ex06_0:edit_band": "small",
    "stdout:ex06_1:relation": "different",
    "stdout:ex06_1:edit_band": "medium",
    "stdout:ex06_2:relation": "different",
    "stdout:ex06_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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
    "ast:c_update": "0",
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
    int quantity, i;
    float max, min, num;

    printf("Introduza a quantidade de números: ");
    scanf("%d", &quantity);

    printf("Intoduza um número: ");
    scanf("%f", &max); 
    min = max;
    for (i = 1; i < quantity; i++) {
       printf("Intoduza um número: ");
        scanf("%f", &num); 
        if (num > max) {
            max = num;
        }
        if (num < min) {
            min = num;
        }
    }
    printf("min: %f, max: %f\n", min, max);
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
  "source_sha256": "0527e1709c4bc36a5bee782f5661c590202309e23f328cc4e58fe8fbc03f92ea",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "Introduza a quantidade de números: Intoduza um número: Intoduza um número: Intoduza um número: min: 1.500000, max: 3.000000\n"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "Introduza a quantidade de números: Intoduza um número: Intoduza um número: Intoduza um número: Intoduza um número: min: 0.000000, max: 6.800000\n"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "Introduza a quantidade de números: Intoduza um número: Intoduza um número: Intoduza um número: min: -1.800000, max: 3.140000\n"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex06_0:relation": "different",
    "stdout:ex06_0:edit_band": "large",
    "stdout:ex06_1:relation": "different",
    "stdout:ex06_1:edit_band": "large",
    "stdout:ex06_2:relation": "different",
    "stdout:ex06_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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


## sample_023 — train

```c

#include <stdio.h>
#include <values.h>

int main()
{
    
    int N;
    float max = -FLT_MAX, min = FLT_MAX, valores;

    
    scanf("%d", &N);

    
    while( N--)
    {
        scanf("%f", &valores);

        if(valores > max)
            max = valores;
        
        else if( valores < min)
            min = valores;

    }

    printf("min:%f max:%f", min, max);  


    return 0;
}
```

```json
{
  "sample_id": "sample_023",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "ab3ab26eab8c9f24bcb831c379146d4b1256b284c4b5ed65c40ad8ab27f59a9a",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "min:340282346638528859811704183484516925440.000000 max:3.000000"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "min:0.000000 max:6.800000"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "min:1.000000 max:3.140000"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex06_0:relation": "different",
    "stdout:ex06_0:edit_band": "large",
    "stdout:ex06_1:relation": "different",
    "stdout:ex06_1:edit_band": "small",
    "stdout:ex06_2:relation": "different",
    "stdout:ex06_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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


## sample_024 — train

```c

#include <stdio.h>
#include <values.h>

int main()
{
    
    int N;
    float max = FLT_MAX, min = -FLT_MAX, valores;

    
    scanf("%d", &N);
    
    
    while( N--)
    {
        scanf("%f", &valores);

        if(valores > max)
            max = valores;
        
        else if( valores < min)
            min = valores;

    }

    printf("min:%f max:%f", min, max);  


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
  "source_sha256": "db150d93fdbc23eaac6c82e8236591225d362c61bf3bb03141bf3ec685f704e0",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "min:-340282346638528859811704183484516925440.000000 max:340282346638528859811704183484516925440.000000"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "min:-340282346638528859811704183484516925440.000000 max:340282346638528859811704183484516925440.000000"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "min:-340282346638528859811704183484516925440.000000 max:340282346638528859811704183484516925440.000000"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex06_0:relation": "different",
    "stdout:ex06_0:edit_band": "large",
    "stdout:ex06_1:relation": "different",
    "stdout:ex06_1:edit_band": "large",
    "stdout:ex06_2:relation": "different",
    "stdout:ex06_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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

int main() {
    
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
  "source_sha256": "64d25e6aedb365482dc2769e2e5f6c311b1c3ff23379a9f5c9885a5ebf44ad16",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": ""
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": ""
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "0",
    "ast:c_update": "0",
    "stdout:ex06_0:relation": "empty",
    "stdout:ex06_0:edit_band": "large",
    "stdout:ex06_1:relation": "empty",
    "stdout:ex06_1:edit_band": "large",
    "stdout:ex06_2:relation": "empty",
    "stdout:ex06_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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


## sample_026 — train

```c

#include <stdio.h>

int main()
{
    int n;
    float min, max, val;
    scanf("%d", &n);
    scanf("%f",&val);
    min = max = val;
    while(--n)
        {
            scanf("%f", &val);
            if(val < min)
                min = val;
            if(val > max)
                max = val;
        }
    printf("min: %f, max: %f", min, max);
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
  "source_sha256": "52597af6cedc7e922c2418a64f6a51c64dc392eb3d6fb7790b83097bf760cfe1",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "min: 1.500000, max: 3.000000"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "min: 0.000000, max: 6.800000"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "min: -1.800000, max: 3.140000"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex06_0:relation": "whitespace",
    "stdout:ex06_0:edit_band": "small",
    "stdout:ex06_1:relation": "whitespace",
    "stdout:ex06_1:edit_band": "small",
    "stdout:ex06_2:relation": "whitespace",
    "stdout:ex06_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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


## sample_027 — validation

```c


#include <stdio.h>

int main(){

    int n;
    double val,max,min;

    scanf("%n",&n);

    scanf("%lf",&val);
    min=max=val;
    n--;

    while (n>0){
        scanf("%lf",&val);
        if (val>max)
            max=val;
        else if (val<max)
            min=val;
    }

    printf("min: %f, max: %f\n", min, max);

    return 0;
}
```

```json
{
  "sample_id": "sample_027",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "8422dcbdcd6abd6d99b40d47415f3c9b2070d7d4c7c142bf32435fe99c3a1f4d",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": "min: 3.000000, max: 3.000000\n"
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": "min: 4.000000, max: 4.000000\n"
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": "min: 3.000000, max: 3.000000\n"
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex06_0:relation": "different",
    "stdout:ex06_0:edit_band": "small",
    "stdout:ex06_1:relation": "different",
    "stdout:ex06_1:edit_band": "medium",
    "stdout:ex06_2:relation": "different",
    "stdout:ex06_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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


## sample_028 — train

```c

#include <stdio.h>

int main() {

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
  "source_sha256": "a394a64700d59d01c4cd4546d63a88bbf7e268632b1649e6b84780a7d19b18f6",
  "outcomes": {
    "ex06_0": "fail",
    "ex06_1": "fail",
    "ex06_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex06_0",
      "input": "3 1.5 2.7 3",
      "expected": "min: 1.500000, max: 3.000000\n",
      "output": ""
    },
    {
      "test_id": "ex06_1",
      "input": "4 6.8 2 1 0",
      "expected": "min: 0.000000, max: 6.800000\n",
      "output": ""
    },
    {
      "test_id": "ex06_2",
      "input": "3 -1.8 3.14 1",
      "expected": "min: -1.800000, max: 3.140000\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "0",
    "ast:c_update": "0",
    "stdout:ex06_0:relation": "empty",
    "stdout:ex06_0:edit_band": "large",
    "stdout:ex06_1:relation": "empty",
    "stdout:ex06_1:edit_band": "large",
    "stdout:ex06_2:relation": "empty",
    "stdout:ex06_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex06_0": "fail",
    "test:ex06_1": "fail",
    "test:ex06_2": "fail",
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


## Evidence refs hợp lệ

```json
[
  "test_statistics",
  "feature_statistics",
  "learned_if_then_rules",
  "semantic_findings",
  "problem_statement",
  "members/sample_001/raw_code",
  "members/sample_001/tests/ex06_0",
  "members/sample_001/tests/ex06_1",
  "members/sample_001/tests/ex06_2",
  "members/sample_002/raw_code",
  "members/sample_002/tests/ex06_0",
  "members/sample_002/tests/ex06_1",
  "members/sample_002/tests/ex06_2",
  "members/sample_003/raw_code",
  "members/sample_003/tests/ex06_0",
  "members/sample_003/tests/ex06_1",
  "members/sample_003/tests/ex06_2",
  "members/sample_004/raw_code",
  "members/sample_004/tests/ex06_0",
  "members/sample_004/tests/ex06_1",
  "members/sample_004/tests/ex06_2",
  "members/sample_005/raw_code",
  "members/sample_005/tests/ex06_0",
  "members/sample_005/tests/ex06_1",
  "members/sample_005/tests/ex06_2",
  "members/sample_006/raw_code",
  "members/sample_006/tests/ex06_0",
  "members/sample_006/tests/ex06_1",
  "members/sample_006/tests/ex06_2",
  "members/sample_007/raw_code",
  "members/sample_007/tests/ex06_0",
  "members/sample_007/tests/ex06_1",
  "members/sample_007/tests/ex06_2",
  "members/sample_008/raw_code",
  "members/sample_008/tests/ex06_0",
  "members/sample_008/tests/ex06_1",
  "members/sample_008/tests/ex06_2",
  "members/sample_009/raw_code",
  "members/sample_009/tests/ex06_0",
  "members/sample_009/tests/ex06_1",
  "members/sample_009/tests/ex06_2",
  "members/sample_010/raw_code",
  "members/sample_010/tests/ex06_0",
  "members/sample_010/tests/ex06_1",
  "members/sample_010/tests/ex06_2",
  "members/sample_011/raw_code",
  "members/sample_011/tests/ex06_0",
  "members/sample_011/tests/ex06_1",
  "members/sample_011/tests/ex06_2",
  "members/sample_012/raw_code",
  "members/sample_012/tests/ex06_0",
  "members/sample_012/tests/ex06_1",
  "members/sample_012/tests/ex06_2",
  "members/sample_013/raw_code",
  "members/sample_013/tests/ex06_0",
  "members/sample_013/tests/ex06_1",
  "members/sample_013/tests/ex06_2",
  "members/sample_014/raw_code",
  "members/sample_014/tests/ex06_0",
  "members/sample_014/tests/ex06_1",
  "members/sample_014/tests/ex06_2",
  "members/sample_015/raw_code",
  "members/sample_015/tests/ex06_0",
  "members/sample_015/tests/ex06_1",
  "members/sample_015/tests/ex06_2",
  "members/sample_016/raw_code",
  "members/sample_016/tests/ex06_0",
  "members/sample_016/tests/ex06_1",
  "members/sample_016/tests/ex06_2",
  "members/sample_017/raw_code",
  "members/sample_017/tests/ex06_0",
  "members/sample_017/tests/ex06_1",
  "members/sample_017/tests/ex06_2",
  "members/sample_018/raw_code",
  "members/sample_018/tests/ex06_0",
  "members/sample_018/tests/ex06_1",
  "members/sample_018/tests/ex06_2",
  "members/sample_019/raw_code",
  "members/sample_019/tests/ex06_0",
  "members/sample_019/tests/ex06_1",
  "members/sample_019/tests/ex06_2",
  "members/sample_020/raw_code",
  "members/sample_020/tests/ex06_0",
  "members/sample_020/tests/ex06_1",
  "members/sample_020/tests/ex06_2",
  "members/sample_021/raw_code",
  "members/sample_021/tests/ex06_0",
  "members/sample_021/tests/ex06_1",
  "members/sample_021/tests/ex06_2",
  "members/sample_022/raw_code",
  "members/sample_022/tests/ex06_0",
  "members/sample_022/tests/ex06_1",
  "members/sample_022/tests/ex06_2",
  "members/sample_023/raw_code",
  "members/sample_023/tests/ex06_0",
  "members/sample_023/tests/ex06_1",
  "members/sample_023/tests/ex06_2",
  "members/sample_024/raw_code",
  "members/sample_024/tests/ex06_0",
  "members/sample_024/tests/ex06_1",
  "members/sample_024/tests/ex06_2",
  "members/sample_025/raw_code",
  "members/sample_025/tests/ex06_0",
  "members/sample_025/tests/ex06_1",
  "members/sample_025/tests/ex06_2",
  "members/sample_026/raw_code",
  "members/sample_026/tests/ex06_0",
  "members/sample_026/tests/ex06_1",
  "members/sample_026/tests/ex06_2",
  "members/sample_027/raw_code",
  "members/sample_027/tests/ex06_0",
  "members/sample_027/tests/ex06_1",
  "members/sample_027/tests/ex06_2",
  "members/sample_028/raw_code",
  "members/sample_028/tests/ex06_0",
  "members/sample_028/tests/ex06_1",
  "members/sample_028/tests/ex06_2"
]
```
