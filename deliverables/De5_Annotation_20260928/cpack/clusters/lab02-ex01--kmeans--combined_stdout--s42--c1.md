# lab02-ex01--kmeans--combined_stdout--s42--c1

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 59; phân vùng: {'train': 43, 'validation': 16}.


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
    "test_id": "ex01_0",
    "n_cluster": 59,
    "n_observed": 59,
    "n_failed": 59,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 59
    }
  },
  {
    "test_id": "ex01_1",
    "n_cluster": 59,
    "n_observed": 59,
    "n_failed": 59,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 59
    }
  },
  {
    "test_id": "ex01_2",
    "n_cluster": 59,
    "n_observed": 59,
    "n_failed": 59,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 59
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex01_0:edit_band",
    "value": "medium",
    "n": 59,
    "n_cluster": 59,
    "rate": 1.0,
    "cohort_rate": 0.37037037037037035,
    "difference_from_cohort": 0.6296296296296297
  },
  {
    "feature": "stdout:ex01_0:relation",
    "value": "whitespace",
    "n": 59,
    "n_cluster": 59,
    "rate": 1.0,
    "cohort_rate": 0.37037037037037035,
    "difference_from_cohort": 0.6296296296296297
  },
  {
    "feature": "stdout:ex01_2:edit_band",
    "value": "medium",
    "n": 59,
    "n_cluster": 59,
    "rate": 1.0,
    "cohort_rate": 0.37037037037037035,
    "difference_from_cohort": 0.6296296296296297
  },
  {
    "feature": "stdout:ex01_2:relation",
    "value": "whitespace",
    "n": 59,
    "n_cluster": 59,
    "rate": 1.0,
    "cohort_rate": 0.37037037037037035,
    "difference_from_cohort": 0.6296296296296297
  },
  {
    "feature": "stdout:ex01_1:relation",
    "value": "whitespace",
    "n": 59,
    "n_cluster": 59,
    "rate": 1.0,
    "cohort_rate": 0.38271604938271603,
    "difference_from_cohort": 0.617283950617284
  },
  {
    "feature": "stdout:ex01_1:edit_band",
    "value": "medium",
    "n": 59,
    "n_cluster": 59,
    "rate": 1.0,
    "cohort_rate": 0.4012345679012346,
    "difference_from_cohort": 0.5987654320987654
  },
  {
    "feature": "test:ex01_0",
    "value": "fail",
    "n": 59,
    "n_cluster": 59,
    "rate": 1.0,
    "cohort_rate": 0.9135802469135802,
    "difference_from_cohort": 0.0864197530864198
  },
  {
    "feature": "ast:c_while",
    "value": "1",
    "n": 12,
    "n_cluster": 59,
    "rate": 0.2033898305084746,
    "cohort_rate": 0.12345679012345678,
    "difference_from_cohort": 0.0799330403850178
  },
  {
    "feature": "ast:c_for",
    "value": "0",
    "n": 57,
    "n_cluster": 59,
    "rate": 0.9661016949152542,
    "cohort_rate": 0.9012345679012346,
    "difference_from_cohort": 0.06486712701401964
  },
  {
    "feature": "test:ex01_2",
    "value": "fail",
    "n": 59,
    "n_cluster": 59,
    "rate": 1.0,
    "cohort_rate": 0.9444444444444444,
    "difference_from_cohort": 0.05555555555555558
  },
  {
    "feature": "ast:c_if",
    "value": "0",
    "n": 8,
    "n_cluster": 59,
    "rate": 0.13559322033898305,
    "cohort_rate": 0.10493827160493827,
    "difference_from_cohort": 0.030654948734044785
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "0",
    "n": 49,
    "n_cluster": 59,
    "rate": 0.8305084745762712,
    "cohort_rate": 0.808641975308642,
    "difference_from_cohort": 0.02186649926762918
  },
  {
    "feature": "ast:c_one_index",
    "value": "1",
    "n": 2,
    "n_cluster": 59,
    "rate": 0.03389830508474576,
    "cohort_rate": 0.012345679012345678,
    "difference_from_cohort": 0.021552626072400084
  },
  {
    "feature": "ast:c_zero_index",
    "value": "1",
    "n": 2,
    "n_cluster": 59,
    "rate": 0.03389830508474576,
    "cohort_rate": 0.012345679012345678,
    "difference_from_cohort": 0.021552626072400084
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 10,
    "n_cluster": 59,
    "rate": 0.1694915254237288,
    "cohort_rate": 0.14814814814814814,
    "difference_from_cohort": 0.021343377275580666
  },
  {
    "feature": "test:ex01_1",
    "value": "fail",
    "n": 59,
    "n_cluster": 59,
    "rate": 1.0,
    "cohort_rate": 0.9876543209876543,
    "difference_from_cohort": 0.012345679012345734
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 52,
    "n_cluster": 59,
    "rate": 0.8813559322033898,
    "cohort_rate": 0.8765432098765432,
    "difference_from_cohort": 0.004812722326846597
  },
  {
    "feature": "ast:c_address_of",
    "value": "0",
    "n": 1,
    "n_cluster": 59,
    "rate": 0.01694915254237288,
    "cohort_rate": 0.012345679012345678,
    "difference_from_cohort": 0.004603473530027203
  },
  {
    "feature": "ast:c_subscript",
    "value": "1",
    "n": 2,
    "n_cluster": 59,
    "rate": 0.03389830508474576,
    "cohort_rate": 0.030864197530864196,
    "difference_from_cohort": 0.0030341075538815668
  },
  {
    "feature": "ast:c_subscript",
    "value": "0",
    "n": 57,
    "n_cluster": 59,
    "rate": 0.9661016949152542,
    "cohort_rate": 0.9691358024691358,
    "difference_from_cohort": -0.00303410755388156
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 52,
    "n_cluster": 59,
    "rate": 0.8813559322033898,
    "cohort_rate": 0.8765432098765432,
    "difference_from_cohort": 0.004812722326846597
  },
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 59,
    "n_cluster": 59,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 58,
    "n_cluster": 59,
    "rate": 0.9830508474576272,
    "cohort_rate": 0.9876543209876543,
    "difference_from_cohort": -0.004603473530027102
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 51,
    "n_cluster": 59,
    "rate": 0.864406779661017,
    "cohort_rate": 0.8950617283950617,
    "difference_from_cohort": -0.03065494873404473
  }
]
```


## IF–THEN dự đoán cluster, không dự đoán gold

```json
[
  {
    "rule_id": 5,
    "if": [
      "NOT (stdout:ex01_0:edit_band=large)",
      "stdout:ex01_0:relation=whitespace"
    ],
    "then_cluster": 1,
    "train_support": 43,
    "train_precision": 1.0,
    "holdout_support": 16,
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
  "reasoning": "Có 59 bài trong cụm. Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
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

sample_001, sample_020, sample_054, sample_002

## sample_001 — train — đại diện

```c
#include <stdio.h>

int main(){
    int x, y, z, maior;
    scanf("%d %d %d", &x, &y, &z);
    if(x > y && x > z)
        maior = x;
    else if(y > x && y > z)
        maior = y;
    else
        maior = z;
    printf("%d", maior);
    return 0;
}
```

```json
{
  "sample_id": "sample_001",
  "partition": "train",
  "representative": true,
  "is_train_medoid": true,
  "raw_code_truncated": false,
  "source_sha256": "9a4bd4595854a5f061b9e49eeda1ab02fc748314c4f93619416120c26e40aa9c",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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



int main () {

  int num, max, contador;
  max = 0;

  for (contador = 0; contador < 3; contador++){
    scanf("%d", &num);
    if (num > max) {
      max = num;
    }
  }
  printf("%d", max);
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
  "source_sha256": "1e56e2c8742dfa63525b8642402292b18b213f0a57d89990640fd2ee589bf721",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
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


## sample_020 — train — đại diện

```c




#include <stdio.h>

int main()
{
    int input [3];
    int output = 0;
    int i = 1;

    scanf("%d %d %d", &input[0], &input[1], &input[2]);
    output = input[0];

    while(i<=2){
        if(input[i] > output)
            output = input[i];

        i++;
    }

    printf("%d", output);

    return 0;
}
```

```json
{
  "sample_id": "sample_020",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "2e4127a4a0a8b42cc15f3108052b028fb6a0119a590d48bfd21369249d886ee5",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "1",
    "ast:c_one_index": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "1",
    "ast:c_one_index": "1",
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


## sample_054 — train — đại diện

```c

#include <stdio.h>

int main() {
    int num, nummax, contador = 1;
    scanf("%d", &num);
    nummax = num;
    while (contador <= 3) {
        contador++;
        scanf("%d", &num);
        if (num > nummax) {
            nummax = num;
        }

    }
    printf("%d", nummax);
    return 0;
}
```

```json
{
  "sample_id": "sample_054",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "6af93ecc757338d03da40295b217dc9ffb621c5ec188491d14c57dd39b7a7b66",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_003 — train

```c
#include <stdio.h>

int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    if (a <= b) {
        if (b <= c) {
            printf("%d", c);
        }
        else{
            printf("%d", b);
        }
    } 
    else {
        if (a <= c) {
            printf("%d", c);
        }
        else {
            printf("%d", a);
        }
    }

    return 0;
}
```

```json
{
  "sample_id": "sample_003",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "a1acde703994486f1e1ed447d9a857c4d1a90e329570da60da9d094f95015570",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
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


## sample_004 — train

```c
#include <stdio.h>

int x, y, z;

int main(){

    scanf("%d%d%d", &x, &y, &z);
    
    if (x>y && x>z)
        printf("%d", x);
    
    else if (y>x && y>z)
        printf("%d", y);
    
    else 
        printf("%d", z);

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
  "source_sha256": "6ad05fa900dff1051625add8100cc32b45f0a9cf4b2d828aa7a8c4ad10c788cc",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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

int main() {
    int n1, n2, n3, n4;
    scanf("%d %d %d",&n1,&n2,&n3);
    if (n1>n2 && n1>n3)
        n4 = n1;
    else if(n2>n1 && n2>n3)
        n4 = n2;
    else n4 = n3;
    printf("%d",n4);
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
  "source_sha256": "e5f263cbef1c66ba4666626b069ef65938ab2e9b411b2b568ab0c87df000a87e",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_006 — train

```c
#include <stdio.h>

int main() {
    int n1, n2, n3, n4;
    scanf("%d %d %d",&n1,&n2,&n3);
    if (n1>n2 && n1>n3)
        n4 = n1;
    else if(n2>n1 && n2>n3)
        n4 = n2;
    else n4 = n3;
    printf("%d",n4);

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
  "source_sha256": "b0bec4f32d42d1a46302762f3622524c36639d05442a7857a35ad6c61955b792",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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

int main() {
    int num1, num2, num3, maior;
    
    scanf("%d %d %d", &num1, &num2, &num3);
    
    maior = num1;
    
    while (num2 > maior) {
        maior = num2;
    }
    
    while (num3 > maior) {
        maior = num3;
    }
    
    printf("%d", maior);
    
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
  "source_sha256": "9b6d5ca6ad82adc164409fab0db8f6767832afb95f21df48c4c02fd519e656fa",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_008 — train

```c


#include <stdio.h>

int main() {
    int num1, num2, num3, maior;
    
    scanf("%d %d %d", &num1, &num2, &num3);
    
    maior = num1;
    
    while (num2 > maior) {
        maior = num2;
    }
    
    while (num3 > maior) {
        maior = num3;
    }
    
    printf("%d", maior);
    
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
  "source_sha256": "e11e1a42b41702ed6a271bc29b38c131be9b50b4f04aaaf2bc46cf98e08da41f",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_009 — train

```c


#include <stdio.h>

int main() {
    int num1, num2, num3, maior;
    
    scanf("%d %d %d", &num1, &num2, &num3);
    
    maior = num1;
    
    while (num2 > maior) {
        maior = num2;
    }
    
    while (num3 > maior) {
        maior = num3;
    }
    
    printf("%d", maior);
    
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
  "source_sha256": "e11e1a42b41702ed6a271bc29b38c131be9b50b4f04aaaf2bc46cf98e08da41f",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_010 — train

```c

#include <stdio.h>

int main()
{
    int num1, num2, num3, max;

    scanf("%d%d%d", &num1, &num2, &num3);

    max = num1 > num2 ? num1 : num2;
    max = num3 > max ? num3 : max;

    printf("%d", max);

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
  "source_sha256": "e634d048c254d753eb9235ed05a3cf448fc21b9a422a848e4ea57cc42c544067",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_011 — train

```c

#include <stdio.h>

int main()
{
    int max;
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    max = a;
    if (b > max)
        max = b;
    if (c > max)
        max = c;
    printf("%d", max);
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
  "source_sha256": "5f45deaefc94095ba2e330f817be68aaea3d41645c3f6b33bc2087dc0d23d9d3",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_012 — train

```c

#include <stdio.h>

int main()
{
    int max = 0;
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    if (a > max)
        max = a;
    if (b > max)
        max = b;
    if (c > max)
        max = c;
    printf("%d", max);
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
  "source_sha256": "56ea4b9f33be5c89496e711bb5ff272c02d82e911349043162cfdaa3ff65875a",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_013 — train

```c

#include <stdio.h>

int main(){
    int a,b,c;
    scanf("%d %d %d", &a, &b, &c);
    if(a<b){
        if(b<c){
            printf("%d",c);
        }
        else{
            printf("%d",b);
        }
    }
    else{
        if(a<c){
            printf("%d",c);
        }
        else{
            printf("%d",a);
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
  "source_sha256": "6e381719eca2c45b63a6dc22f4151dcda456a5313af0a3a47e63bd9c38a8cd55",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_014 — validation

```c

#include <stdio.h>

int main()
{
    int i;
    int maximo;
    int numero;
    i=0;
    scanf("%d", &maximo);
    while (i<2)
    {
        scanf( "%d", &numero);
        if (numero> maximo)
        {
            maximo= numero;
        }
        ++i;
    }
    printf("%d", maximo);
    return 0;
} 
```

```json
{
  "sample_id": "sample_014",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "a7b00d78e0326a52b853ce4f6de980422e9916b0b6e49b15e1837e36ca223b18",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_015 — validation

```c

#include <stdio.h>


int main()
{
    int num1;
    int num2;
    int num3;
    scanf("%d%d%d",&num1, &num2, &num3);
    if (num1>num2 && num1>num3)
    {
        printf("%d", num1);
    }
    if (num2>num1 && num2>num3)
    {
        printf("%d", num2);
    }
    if (num3>num2 && num1<num3)
    {
        printf("%d", num3);
    }
    return 0;
} 

```

```json
{
  "sample_id": "sample_015",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "fb73d1f50db9768e6975c61c2b2275ccf0bf21d7d7dae728ee43b7485ea1c6b5",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_016 — validation

```c

#include <stdio.h>


int main()
{
    int i;
    int maximo;
    int numero;
    i=0;
    scanf("%d", &maximo);
    while (i<2)
    {
        scanf( "%d", &numero);
        if (numero> maximo)
        {
            maximo= numero;
        }
        ++i;
    }
    printf("%d", maximo);
    return 0;
} 
```

```json
{
  "sample_id": "sample_016",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "36cf7f329c80016d802aab3fffe57a193dac54105bb51d2abeb3d3762c4824cc",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_017 — validation

```c

#include <stdio.h>

int main()
{
    int um, dois, tres, maior = 0;
    scanf("%d %d %d", &um, &dois, &tres);
    if(um >= dois && um >= tres)
        maior = um;
    else if(dois >= um && dois >= tres)
        maior = dois;
    else
        maior = tres;
    printf("%d", maior);
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
  "source_sha256": "bed31898d56be5d8f89d3da7d5c8f982ef886cc51c3493117d630f707af458fc",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
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


## sample_018 — validation

```c

#include <stdio.h>

int main()
{
    int um, dois, tres, maior = 0;
    scanf("%d %d %d", &um, &dois, &tres);
    if(um >= dois && um >= tres)
        maior = um;
    else if(dois >= um && dois >= tres)
        maior = dois;
    else
        maior = tres;
    printf("%d", maior);
    return 0;
    
}
```

```json
{
  "sample_id": "sample_018",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "9eb3e0c79e547c92ee9bda026f6acda476637d9d9029cd0bc41bb1711f79c5c4",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
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


## sample_019 — train

```c


#include <stdio.h>

int main()
{
    int input = 0;
    int output = 0;
    int i = 0;

    scanf("%d", &input);
    output = input;

    while(i<2){
        scanf("%d", &input);
        if(input > output)
            output = input;

        i++;
    }

    printf("%d", output);

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
  "source_sha256": "a666745eed54a4cf1ab609e8c77844efa31bebc27286837ce6bfd0eb84148843",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_021 — train

```c




#include <stdio.h>

int main()
{
    int input [3];
    int output = 0;
    int i = 1;

    scanf("%d %d %d", &input[0], &input[1], &input[2]);
    output = input[0];

    while(i<=2){
        if(input[i] > output)
            output = input[i];

        i++;
    }

    printf("%d \n", output);

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
  "source_sha256": "74c6d3fbb499fb173f03bcb8023d44946cf0f5f2a899de976dedd5222b8bfa7e",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3 \n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6 \n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3 \n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "1",
    "ast:c_one_index": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "1",
    "ast:c_one_index": "1",
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


## sample_022 — train

```c




#include <stdio.h>

int main()
{
    int input = 0;
    int output = 0;
    int i = 0;

    scanf("%d", &input);
    output = input;

    while(i<2){
        scanf("%d", &input);
        if(input > output)
            output = input;

        i++;
    }

    printf("%d", output);

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
  "source_sha256": "99e6fb880f538c8eb3be7a1347f8e71ca8f42740af82cc5b073a311e0b765aca",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_023 — train

```c


#include <stdio.h>

int main(void) {

    int num1;
    int num2;
    int num3;

    scanf("%d %d %d", &num1, &num2, &num3);
    if(num1 > num2 && num1 > num3)
        printf("%d", num1);
    else if(num2 > num1 && num2 > num3)
        printf("%d", num2);
    else if(num3 > num1 && num3 > num2)
        printf("%d", num3);
    else
        printf("nenhum número é maior do que os outros dois");
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
  "source_sha256": "93f3130f90bcb09454769012603484f25a444646a545ec84f602306a2bdf7b23",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_024 — validation

```c

#include <stdio.h>

int main()
{
    int primeiro, segundo , terceiro;
    scanf("%d",&primeiro);
    scanf("%d",&segundo);
    scanf("%d",&terceiro);
    
    if (primeiro > segundo && primeiro > terceiro)
    {
        printf("%d",primeiro);
        return 0;
    }
    if (primeiro < segundo && segundo > terceiro)
    {
        printf("%d",segundo);
        return 0;
    }
    if (primeiro < terceiro && segundo < terceiro)
    {
        printf("%d",terceiro);
        return 0;
    }
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
  "source_sha256": "e7549f2cdad3b61845b4c63a07260884d7dc37e248a470e6aa5460f3113f1de3",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_025 — validation

```c

#include <stdio.h>

int main()
{
    int primeiro, segundo , terceiro;
    scanf("%d",&primeiro);
    scanf("%d",&segundo);
    scanf("%d",&terceiro);
    
    if (primeiro > segundo && primeiro > terceiro)
    {
        printf("%d",primeiro);
    }
    if (primeiro < segundo && segundo > terceiro)
    {
        printf("%d",segundo);
    }
    if (primeiro < terceiro && segundo < terceiro)
    {
        printf("%d",terceiro);
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_025",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "4315d471971b548130d2f18b4badcd0791ad23b014205af7929c6ae24289b45f",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_026 — validation

```c

#include <stdio.h>

int main()
{
    int primeiro, segundo , terceiro;
    scanf("%d",&primeiro);
    scanf("%d",&segundo);
    scanf("%d",&terceiro);
    
    if (primeiro > segundo && segundo > terceiro)
    {
        printf("%d",primeiro);
    }
    if (primeiro < segundo && segundo > terceiro)
    {
        printf("%d",segundo);
    }
    if (primeiro < terceiro && segundo < terceiro)
    {
        printf("%d",terceiro);
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_026",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "86d80cd1d1e43e9ee009d9bfd27bae32a119d31f673bb9087236613538f38493",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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

int main () {

    int v1, v2, v3;

    scanf("%d%d%d", &v1, &v2, &v3);

    if ((v2 - v1) < 0) {
        if ((v3 - v1) < 0) {
            printf("%d", v1);
        }
        else {
            printf("%d", v3);
        }
    }
    else {
        if ((v3 - v2) < 0) {
            printf("%d", v2);
        }
        else {
            printf("%d", v3);
        }
    }
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
  "source_sha256": "00a76803047db894c2460c0493b6b74789a29925891f60039aa6b7807c25cbec",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_028 — train

```c


#include <stdio.h>

int main () {

    int v1, v2, v3;
    int maior;

    scanf("%d%d%d", &v1, &v2, &v3);

    maior = v1;
    
    if (v2 > maior) {
        maior = v2;
    }
    if (v3 > maior) {
        maior = v3;
    }
    printf("%d", maior);
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
  "source_sha256": "ee4cab1568862da324d8499635e62b75db45cb551781e6fa636e96c3d9cad7ac",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_029 — train

```c

#include <stdio.h>
int main() {
    int a, b, c; 
    scanf("%d %d %d", &a, &b, &c);
    if (a>b && a>c) {
        printf("%d", a);
    }
    if (b>a && b>c){
        printf("%d", b);
    }
    if (c>a && c>b){
        printf("%d", c);
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_029",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "64436255a1078511a04282a2a5a4ce818695dbcc881b4fbfe4bbfc19046ed21a",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_030 — train

```c

#include <stdio.h>
int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    if (a>b && a>c) {
        printf("%d", a);
    }
    if (b>a && b>c){
        printf("%d", b);
    }
    if (c>a && c>b){
        printf("%d", c);
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_030",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "4300df15bfe60e8ac039c3df02cd068eae1553f9001561fb27b786df35b4b22c",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_031 — train

```c

#include <stdio.h>

int main (){
    
    int v1, v2, v3, maximo;
    scanf("%d %d %d", &v1, &v2, &v3);

    if(v1>v2)
        maximo=v1;
    else
        maximo=v2;

    if(v3>maximo)
        maximo=v3;
    else
        maximo=maximo;
    
    printf("%d \n", maximo);
    return 0;
}
```

```json
{
  "sample_id": "sample_031",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "22d7bf7128ad8bb0378dae1f0afb36c995fe43fe6dffba5e42d9ec201cf23e5f",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3 \n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6 \n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3 \n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_032 — train

```c

#include <stdio.h>

int main()
{
    int maior, numero1, numero2, numero3;

    scanf("%d%d%d", &numero1, &numero2, &numero3);
    
    if (numero1 >= numero2 && numero1 >= numero3) {
        maior = numero1;
    } else if (numero2 >= numero1 && numero2 >= numero3) {
        maior = numero2;
    } else {
        maior = numero3;
    }

    printf("%d", maior);
    return 0;
}

```

```json
{
  "sample_id": "sample_032",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "857c11e61c457296ccb2d60c02fd8e1ce3d00a47261bf0440a830d3ab21d18b2",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
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


## sample_033 — train

```c

#include <stdio.h>

int biggest(int num1, int num2, int num3) {
    if ((num1 > num2) && (num1 > num3)) {
        return num1;
    }
    else if ((num2 > num1) && (num2 > num3)) {
        return num2;
    }
    else {
        return num3;
    }
}

int main() {
    int num1, num2, num3;
  
    
    
    scanf("%d %d %d", &num1,&num2,&num3);

    printf("%d", biggest(num1, num2, num3));
  
    return 0;
}

```

```json
{
  "sample_id": "sample_033",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "243012b16ad3f0d172f02e492a6c4cb494e97a8fb7f8d76a2a406a2e323d0b30",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_034 — validation

```c

#include <stdio.h>

int main()
{
    int a, b, c;
    scanf("%d %d %d",&a,&b,&c);
    if (a<b)
    {
        if (b<c)
        {
            printf("%d",c);
        } 
        else
        {
            printf("%d",b);
        }

    }
    else if(a>c)
    {
        printf ("%d",a);
    }
   
    else{
        printf("%d",c);
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_034",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "79c25e3b9894c005cbb65d743642f7d58c02c6b37ae5c042870df9767609d291",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_035 — train

```c


#include <stdio.h>

int main() {
    int n1, n2, n3, res, end;
    scanf("%d %d %d", &n1,&n2, &n3);
    
    res = (n1>n2) ? (n1) : (n2);
    end = (n3>res) ? (n3) : (res);
    
    printf("%d",end);
    return 0;
}

```

```json
{
  "sample_id": "sample_035",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "459c573462b321dd2663c74f6fab07f1997ee779adbd290fc671417b0539fc3d",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_036 — validation

```c
#include <stdio.h>

int main() {
    
    int numUm, numDois, numTres;
    
    scanf("%d", &numUm);
    scanf("%d", &numDois);
    scanf("%d", &numTres);

    if (numUm > numDois && numUm > numTres) {
        printf("%d", numUm);
    } else if (numDois > numTres) {
        printf("%d", numDois);
    } else {
        printf("%d", numTres);
    }

    return 0;
}

```

```json
{
  "sample_id": "sample_036",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "1b274eb64a2c7c53102f11472bc42b719d09d5fbfaf8bd7d8718e56ad31d6ee1",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_037 — validation

```c

#include <stdio.h>
int num1;
int num2;
int num3;
int maxNum;

int main() {
    scanf("%d %d %d", &num1, &num2, &num3);
    maxNum = num1;
    if (maxNum < num2)
        maxNum = num2;
    if (num3 > maxNum)
        maxNum = num3;
    printf("%d", maxNum);
    return 0;
}
```

```json
{
  "sample_id": "sample_037",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "ef65075bd36e4b627d84dad554dbf2a1af7250951fedcfbd895ac7031948eb8f",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_038 — validation

```c

#include <stdio.h>
int num1;
int num2;
int num3;
int maxNum;

int main() {
    scanf("%d %d %d", &num1, &num2, &num3);
    
    maxNum = num1;
    if (maxNum < num2)
        maxNum = num2;
    if (num3 > maxNum)
        maxNum = num3;
    printf("%d",maxNum);
    return 0;
}
```

```json
{
  "sample_id": "sample_038",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "9b5c84b98d14c4549efffe85e85173c3ab6a17dc895c0d4f9243328eef0e79e0",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_039 — train

```c

#include <stdio.h>

int main()
{
    int maior, num1, num2, num3;
    scanf("%d%d%d", &num1, &num2, &num3);
    maior = num1 > num2 ? num1 : num2;
    maior = num3 > maior ? num3 : maior;
    printf("%d", maior);
    return 0;
}
```

```json
{
  "sample_id": "sample_039",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "f748cbc942a4ac0d7091b0dd9e377eaa1b282b64da56aa949390131193f1dbac",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_040 — train

```c

#include <stdio.h>

int main(){
    int n1, n2, n3;
    scanf("%d %d %d", &n1, &n2, &n3);

    if (n1 >= n2) {
        if (n1>=n3){
            printf("%d", n1);
        }
        else {
            printf("%d", n3);
        }
    }
    else { 
        if (n2>=n3){
            printf("%d", n2);
        }
        else {
            printf("%d", n3);
        }
    }
    return 0;
}

```

```json
{
  "sample_id": "sample_040",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "ade2cc70add012ec745bfaf8fc6a066c24be2bdf99683e056a5bbd369d7c9c79",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
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


## sample_041 — validation

```c

#include <stdio.h>



int main()
{
    int num1, num2, num3;

    scanf("%d%d%d", &num1, &num2, &num3);
    if (num1>num2)
    {
        if (num1>num3)
        {
            printf("%d", num1);
        }
        else
        {
            printf("%d", num3); 
        }
    }
    else
    {
        if (num2>num3)
        {
            printf("%d", num2);
        }
        else
        {
            printf("%d", num3); 
        }
    }

    return 0;
}
```

```json
{
  "sample_id": "sample_041",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "d9cbd929dca17be2eec318b83042eea9a8c9eb1ebe8f99a7344b25a87514140a",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_042 — validation

```c

#include <stdio.h>



int main()
{
    int num1, num2, num3;

    scanf("%d", &num1);
    scanf("%d", &num2);
    scanf("%d", &num3);
    if (num1>num2)
    {
        if (num1>num3)
        {
            printf("%d", num1);
        }
        else
        {
            printf("%d", num3); 
        }
    }
    else
    {
        if (num2>num3)
        {
            printf("%d", num2);
        }
        else
        {
            printf("%d", num3); 
        }
    }

    return 0;
}
```

```json
{
  "sample_id": "sample_042",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "7ab8e8f3ddd5785a64b2aded489d4390c8699ca76be2bc874b7542585715aded",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_043 — validation

```c

#include <stdio.h>



int main()
{
    int num1, num2, num3;

    scanf("%d %d %d", &num1, &num2, &num3);
    if (num1>num2)
    {
        if (num1>num3)
        {
            printf("%d", num1);
        }
        else
        {
            printf("%d", num3); 
        }
    }
    else
    {
        if (num2>num3)
        {
            printf("%d", num2);
        }
        else
        {
            printf("%d", num3); 
        }
    }

    return 0;
}
```

```json
{
  "sample_id": "sample_043",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "987ca639f89e48d0c232546500c077718105892a61e5a7550bcfc188f6cf6d6c",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_044 — train

```c

#include <stdio.h>

int main() {
  int x, y, z, maior;
  scanf("%d %d %d", &x, &y, &z);
  if (x > y && x > z) {
    maior = x;
  } else {
    if (y > x && y > z) {
      maior = y;
    } else {
      if (z > x && z > y) {
        maior = z;
      }
    }
  }
  printf("%d", maior);
  return 0;
}

```

```json
{
  "sample_id": "sample_044",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "b98656a05c50a98faa854425c0b4ee50a5c6fecfbbc486f0c4d9d269b76e995a",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_045 — train

```c


#include <stdio.h>

int main (){
    int counter;
    int bigger;
    int num;
    scanf("%d",&num);
    bigger=num;
    for (counter=1; counter<3 ;counter++){
        scanf("%d",&num);
        if (num>bigger){
            bigger=num;
        } 
    }
    printf("%d \n", bigger);
    return 0;
}
```

```json
{
  "sample_id": "sample_045",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "49e303755144a4f19ab7270892e46045aaac620789d638291efc4792adde41f3",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3 \n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6 \n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3 \n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
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


## sample_046 — train

```c


#include <stdio.h>

int main(){

    int maior, num1, num2, num3;

    scanf("%d%d%d", &num1, &num2, &num3);

    if (num1 > num2){
        if (num1 > num3)
            maior = num1;
        else
            maior = num3;
    }
    else{
        if (num2 > num3)
            maior = num2;
        else
            maior = num3;
    }

    printf("%d", maior);
    
    return 0;
}

```

```json
{
  "sample_id": "sample_046",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "935212b8a33d456443730688425888df5a21f70d7e7122098bca5870a68bd1f1",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_047 — train

```c

#include <stdio.h>

int num1, num2, num3, num_maior;

int main() { 
    scanf("%d%d%d", &num1, &num2, &num3);

    if (num1 >= num2) 
        num_maior = num1;
    
    else 
        num_maior = num2;
    
    if (num3 >= num_maior) 
        num_maior = num3;

    printf("%d", num_maior);
    return 0;
}
```

```json
{
  "sample_id": "sample_047",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "df17d20cb0c3fb3a76bb6b6c4b56da89407b8163984aea9dcc50460434bb7514",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
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


## sample_048 — train

```c

#include <stdio.h>

int main()
{
    int n_1, n_2, n_3;

    scanf("%d %d %d", &n_1, &n_2, &n_3);

    if (n_1>n_2 && n_1>n_3) {
        printf("%d", n_1);
    } else if (n_2>n_1 && n_2>n_3) {
        printf("%d", n_2);
    } else {
        printf("%d", n_3);
    }

    return 0;
}
```

```json
{
  "sample_id": "sample_048",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "15e0fce37bdf832989a20658bbc0df5524842b6888627c5b430acd3091913090",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_049 — train

```c


#include <stdio.h>

int main()
{
    int a, b, c;
    int maior;
    scanf("%d %d %d",&a, &b, &c);
    if(a < b)
    {
        maior = b;
    } else maior = a;
    if(maior < c)
    {
        maior = c;
    }
    printf("%d",maior);
    return 0;
}
```

```json
{
  "sample_id": "sample_049",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "8e9b891b17939c6c78eeac69d6d25b6c5821a181225b547793f5d01f346b7d1d",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_050 — train

```c
#include <stdio.h>

int main() {
	int x, y, z, maior;
	
	scanf("%d %d %d", &x, &y, &z);
	
	maior = (x>y && x>z) ? x : ((y>z) ? y : z);
	
	printf("%d", maior);
	
	return 0;
} 

```

```json
{
  "sample_id": "sample_050",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "00a1b837302769dca07fbc2d36a09f7fc608d510845fc68a80e5934c3edef49b",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_051 — train

```c
#include <stdio.h>

int main() {
	int x, y, z, maior;
	
	scanf("%d%d%d", &x, &y, &z);
	
	maior = (x>y && x>z) ? x : ((y>z) ? y : z);
	
	printf("%d", maior);
	
	return 0;
} 

```

```json
{
  "sample_id": "sample_051",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "12b78966441fa7a8410106b8174cae39e066ad006bb9ec2fafedc80e7319dc2f",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_052 — train

```c


#include <stdio.h>

int main(){
    int num1,num2,num3;

    scanf("%d%d%d",&num1,&num2,&num3);
    if (num1 > num2){
        num2 = num1;
    }
    if (num2 > num3){
        num3 = num2;
    }
    printf("%d",num3);

    return 0;
}
```

```json
{
  "sample_id": "sample_052",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "1fec1f73edd7510b1f9bdab7ca05eec5f085076a547ef656a13b2e5aafb07bbb",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_053 — validation

```c
#include <stdio.h>

int main()
{
    int v1, v2, v3;
    scanf("%d %d %d", &v1, &v2, &v3);
    if (v1 > v2) {
        if (v1 > v3)
        {
            printf("%d", v1);
        }
        else
        {
            printf("%d", v3);
        }
    }
    else
    {
        if (v2 > v3)
        {
            printf("%d", v2);
        }
        else
        {
            printf("%d", v3);
        }
    }
    return 0;
    
}
```

```json
{
  "sample_id": "sample_053",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "f32864389bbb410547501f56bbe50dfe976b8af54e00f80b6ad051f98ec8f13f",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_055 — train

```c

#include <stdio.h>

int main() {
    int num, nummax, contador;
    contador = 1;
    scanf("%d", &num);
    nummax = num;
    while (contador < 3) {
        contador++;
        scanf("%d", &num);
        if (num > nummax) {
            nummax = num;
        }

    }
    printf("%d", nummax);
    return 0;
}
```

```json
{
  "sample_id": "sample_055",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "cee4d08e0abf8afb46b15d13a125f2d195dcb32cc0427ad231be35a81d01045d",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_056 — train

```c

#include <stdio.h>

int main() {
    int num_maior = '0',c;

    while((c=getchar()) != EOF){
            if (c > num_maior)
                num_maior = c;
    }
    putchar(num_maior);
    return 0;
}
    




```

```json
{
  "sample_id": "sample_056",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "70a0c7fe23b45a0c18becce8bdaa23a50b2ead0d54c6a0858b5a71ee6bf1a5a7",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "0",
    "ast:c_update": "0",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_057 — train

```c

#include <stdio.h>

int main()
{
    int n1, n2, n3, maior;
    scanf("%d %d %d",&n1,&n2,&n3);
    maior = n1;
    if(n2>maior){
        maior = n2;
    }
    if(n3>maior){
        maior=n3;
    }

    printf("%d \n",maior);
    return 0;
}
```

```json
{
  "sample_id": "sample_057",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "c6b78e662fcbcbb8e696eb3c968e42b29a25e34d92cc3d6024b4712c216fa710",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3 \n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6 \n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3 \n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_058 — train

```c


#include <stdio.h>

int main()
{
    long maior, prim, seg, terc;

    scanf("%ld %ld %ld", &prim, &seg, &terc);
    maior = prim;
    if (seg > maior)
        maior = seg;
    if (terc > maior)
        maior = terc;
    printf("\n%ld\n", maior);
    
    return 0;
}
```

```json
{
  "sample_id": "sample_058",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "ee162d0b200494c9e571e7deea3f55e00534ad40327bf8b393e93c07e1506980",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "\n3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "\n6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "\n3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_059 — train

```c

#include <stdio.h>

int main () {
    int x,y,z;
    scanf("%d %d %d", &x, &y, &z);
    if (x>=y && x>=z)
        printf("%d \n", x);
    else if (y>=z && y>=x)
        printf("%d", y);
    else
        printf("%d", z);
    return 0;
}
```

```json
{
  "sample_id": "sample_059",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "50bfd4d8d91bc7f1d2c2b32b8f78c715023b1596461b67292eaf950f181b2779",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6 \n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
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
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
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


## Evidence refs hợp lệ

```json
[
  "test_statistics",
  "feature_statistics",
  "learned_if_then_rules",
  "semantic_findings",
  "problem_statement",
  "members/sample_001/raw_code",
  "members/sample_001/tests/ex01_0",
  "members/sample_001/tests/ex01_1",
  "members/sample_001/tests/ex01_2",
  "members/sample_002/raw_code",
  "members/sample_002/tests/ex01_0",
  "members/sample_002/tests/ex01_1",
  "members/sample_002/tests/ex01_2",
  "members/sample_003/raw_code",
  "members/sample_003/tests/ex01_0",
  "members/sample_003/tests/ex01_1",
  "members/sample_003/tests/ex01_2",
  "members/sample_004/raw_code",
  "members/sample_004/tests/ex01_0",
  "members/sample_004/tests/ex01_1",
  "members/sample_004/tests/ex01_2",
  "members/sample_005/raw_code",
  "members/sample_005/tests/ex01_0",
  "members/sample_005/tests/ex01_1",
  "members/sample_005/tests/ex01_2",
  "members/sample_006/raw_code",
  "members/sample_006/tests/ex01_0",
  "members/sample_006/tests/ex01_1",
  "members/sample_006/tests/ex01_2",
  "members/sample_007/raw_code",
  "members/sample_007/tests/ex01_0",
  "members/sample_007/tests/ex01_1",
  "members/sample_007/tests/ex01_2",
  "members/sample_008/raw_code",
  "members/sample_008/tests/ex01_0",
  "members/sample_008/tests/ex01_1",
  "members/sample_008/tests/ex01_2",
  "members/sample_009/raw_code",
  "members/sample_009/tests/ex01_0",
  "members/sample_009/tests/ex01_1",
  "members/sample_009/tests/ex01_2",
  "members/sample_010/raw_code",
  "members/sample_010/tests/ex01_0",
  "members/sample_010/tests/ex01_1",
  "members/sample_010/tests/ex01_2",
  "members/sample_011/raw_code",
  "members/sample_011/tests/ex01_0",
  "members/sample_011/tests/ex01_1",
  "members/sample_011/tests/ex01_2",
  "members/sample_012/raw_code",
  "members/sample_012/tests/ex01_0",
  "members/sample_012/tests/ex01_1",
  "members/sample_012/tests/ex01_2",
  "members/sample_013/raw_code",
  "members/sample_013/tests/ex01_0",
  "members/sample_013/tests/ex01_1",
  "members/sample_013/tests/ex01_2",
  "members/sample_014/raw_code",
  "members/sample_014/tests/ex01_0",
  "members/sample_014/tests/ex01_1",
  "members/sample_014/tests/ex01_2",
  "members/sample_015/raw_code",
  "members/sample_015/tests/ex01_0",
  "members/sample_015/tests/ex01_1",
  "members/sample_015/tests/ex01_2",
  "members/sample_016/raw_code",
  "members/sample_016/tests/ex01_0",
  "members/sample_016/tests/ex01_1",
  "members/sample_016/tests/ex01_2",
  "members/sample_017/raw_code",
  "members/sample_017/tests/ex01_0",
  "members/sample_017/tests/ex01_1",
  "members/sample_017/tests/ex01_2",
  "members/sample_018/raw_code",
  "members/sample_018/tests/ex01_0",
  "members/sample_018/tests/ex01_1",
  "members/sample_018/tests/ex01_2",
  "members/sample_019/raw_code",
  "members/sample_019/tests/ex01_0",
  "members/sample_019/tests/ex01_1",
  "members/sample_019/tests/ex01_2",
  "members/sample_020/raw_code",
  "members/sample_020/tests/ex01_0",
  "members/sample_020/tests/ex01_1",
  "members/sample_020/tests/ex01_2",
  "members/sample_021/raw_code",
  "members/sample_021/tests/ex01_0",
  "members/sample_021/tests/ex01_1",
  "members/sample_021/tests/ex01_2",
  "members/sample_022/raw_code",
  "members/sample_022/tests/ex01_0",
  "members/sample_022/tests/ex01_1",
  "members/sample_022/tests/ex01_2",
  "members/sample_023/raw_code",
  "members/sample_023/tests/ex01_0",
  "members/sample_023/tests/ex01_1",
  "members/sample_023/tests/ex01_2",
  "members/sample_024/raw_code",
  "members/sample_024/tests/ex01_0",
  "members/sample_024/tests/ex01_1",
  "members/sample_024/tests/ex01_2",
  "members/sample_025/raw_code",
  "members/sample_025/tests/ex01_0",
  "members/sample_025/tests/ex01_1",
  "members/sample_025/tests/ex01_2",
  "members/sample_026/raw_code",
  "members/sample_026/tests/ex01_0",
  "members/sample_026/tests/ex01_1",
  "members/sample_026/tests/ex01_2",
  "members/sample_027/raw_code",
  "members/sample_027/tests/ex01_0",
  "members/sample_027/tests/ex01_1",
  "members/sample_027/tests/ex01_2",
  "members/sample_028/raw_code",
  "members/sample_028/tests/ex01_0",
  "members/sample_028/tests/ex01_1",
  "members/sample_028/tests/ex01_2",
  "members/sample_029/raw_code",
  "members/sample_029/tests/ex01_0",
  "members/sample_029/tests/ex01_1",
  "members/sample_029/tests/ex01_2",
  "members/sample_030/raw_code",
  "members/sample_030/tests/ex01_0",
  "members/sample_030/tests/ex01_1",
  "members/sample_030/tests/ex01_2",
  "members/sample_031/raw_code",
  "members/sample_031/tests/ex01_0",
  "members/sample_031/tests/ex01_1",
  "members/sample_031/tests/ex01_2",
  "members/sample_032/raw_code",
  "members/sample_032/tests/ex01_0",
  "members/sample_032/tests/ex01_1",
  "members/sample_032/tests/ex01_2",
  "members/sample_033/raw_code",
  "members/sample_033/tests/ex01_0",
  "members/sample_033/tests/ex01_1",
  "members/sample_033/tests/ex01_2",
  "members/sample_034/raw_code",
  "members/sample_034/tests/ex01_0",
  "members/sample_034/tests/ex01_1",
  "members/sample_034/tests/ex01_2",
  "members/sample_035/raw_code",
  "members/sample_035/tests/ex01_0",
  "members/sample_035/tests/ex01_1",
  "members/sample_035/tests/ex01_2",
  "members/sample_036/raw_code",
  "members/sample_036/tests/ex01_0",
  "members/sample_036/tests/ex01_1",
  "members/sample_036/tests/ex01_2",
  "members/sample_037/raw_code",
  "members/sample_037/tests/ex01_0",
  "members/sample_037/tests/ex01_1",
  "members/sample_037/tests/ex01_2",
  "members/sample_038/raw_code",
  "members/sample_038/tests/ex01_0",
  "members/sample_038/tests/ex01_1",
  "members/sample_038/tests/ex01_2",
  "members/sample_039/raw_code",
  "members/sample_039/tests/ex01_0",
  "members/sample_039/tests/ex01_1",
  "members/sample_039/tests/ex01_2",
  "members/sample_040/raw_code",
  "members/sample_040/tests/ex01_0",
  "members/sample_040/tests/ex01_1",
  "members/sample_040/tests/ex01_2",
  "members/sample_041/raw_code",
  "members/sample_041/tests/ex01_0",
  "members/sample_041/tests/ex01_1",
  "members/sample_041/tests/ex01_2",
  "members/sample_042/raw_code",
  "members/sample_042/tests/ex01_0",
  "members/sample_042/tests/ex01_1",
  "members/sample_042/tests/ex01_2",
  "members/sample_043/raw_code",
  "members/sample_043/tests/ex01_0",
  "members/sample_043/tests/ex01_1",
  "members/sample_043/tests/ex01_2",
  "members/sample_044/raw_code",
  "members/sample_044/tests/ex01_0",
  "members/sample_044/tests/ex01_1",
  "members/sample_044/tests/ex01_2",
  "members/sample_045/raw_code",
  "members/sample_045/tests/ex01_0",
  "members/sample_045/tests/ex01_1",
  "members/sample_045/tests/ex01_2",
  "members/sample_046/raw_code",
  "members/sample_046/tests/ex01_0",
  "members/sample_046/tests/ex01_1",
  "members/sample_046/tests/ex01_2",
  "members/sample_047/raw_code",
  "members/sample_047/tests/ex01_0",
  "members/sample_047/tests/ex01_1",
  "members/sample_047/tests/ex01_2",
  "members/sample_048/raw_code",
  "members/sample_048/tests/ex01_0",
  "members/sample_048/tests/ex01_1",
  "members/sample_048/tests/ex01_2",
  "members/sample_049/raw_code",
  "members/sample_049/tests/ex01_0",
  "members/sample_049/tests/ex01_1",
  "members/sample_049/tests/ex01_2",
  "members/sample_050/raw_code",
  "members/sample_050/tests/ex01_0",
  "members/sample_050/tests/ex01_1",
  "members/sample_050/tests/ex01_2",
  "members/sample_051/raw_code",
  "members/sample_051/tests/ex01_0",
  "members/sample_051/tests/ex01_1",
  "members/sample_051/tests/ex01_2",
  "members/sample_052/raw_code",
  "members/sample_052/tests/ex01_0",
  "members/sample_052/tests/ex01_1",
  "members/sample_052/tests/ex01_2",
  "members/sample_053/raw_code",
  "members/sample_053/tests/ex01_0",
  "members/sample_053/tests/ex01_1",
  "members/sample_053/tests/ex01_2",
  "members/sample_054/raw_code",
  "members/sample_054/tests/ex01_0",
  "members/sample_054/tests/ex01_1",
  "members/sample_054/tests/ex01_2",
  "members/sample_055/raw_code",
  "members/sample_055/tests/ex01_0",
  "members/sample_055/tests/ex01_1",
  "members/sample_055/tests/ex01_2",
  "members/sample_056/raw_code",
  "members/sample_056/tests/ex01_0",
  "members/sample_056/tests/ex01_1",
  "members/sample_056/tests/ex01_2",
  "members/sample_057/raw_code",
  "members/sample_057/tests/ex01_0",
  "members/sample_057/tests/ex01_1",
  "members/sample_057/tests/ex01_2",
  "members/sample_058/raw_code",
  "members/sample_058/tests/ex01_0",
  "members/sample_058/tests/ex01_1",
  "members/sample_058/tests/ex01_2",
  "members/sample_059/raw_code",
  "members/sample_059/tests/ex01_0",
  "members/sample_059/tests/ex01_1",
  "members/sample_059/tests/ex01_2"
]
```
