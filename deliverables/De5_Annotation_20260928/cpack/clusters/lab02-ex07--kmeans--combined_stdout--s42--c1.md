# lab02-ex07--kmeans--combined_stdout--s42--c1

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 24; phân vùng: {'train': 16, 'validation': 8}.


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
    "test_id": "ex07_0",
    "n_cluster": 24,
    "n_observed": 24,
    "n_failed": 24,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 24
    }
  },
  {
    "test_id": "ex07_1",
    "n_cluster": 24,
    "n_observed": 24,
    "n_failed": 24,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 24
    }
  },
  {
    "test_id": "ex07_2",
    "n_cluster": 24,
    "n_observed": 24,
    "n_failed": 24,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 24
    }
  },
  {
    "test_id": "ex07_3",
    "n_cluster": 24,
    "n_observed": 24,
    "n_failed": 24,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 24
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex07_0:edit_band",
    "value": "medium",
    "n": 24,
    "n_cluster": 24,
    "rate": 1.0,
    "cohort_rate": 0.43636363636363634,
    "difference_from_cohort": 0.5636363636363637
  },
  {
    "feature": "stdout:ex07_0:relation",
    "value": "whitespace",
    "n": 24,
    "n_cluster": 24,
    "rate": 1.0,
    "cohort_rate": 0.43636363636363634,
    "difference_from_cohort": 0.5636363636363637
  },
  {
    "feature": "stdout:ex07_1:edit_band",
    "value": "medium",
    "n": 24,
    "n_cluster": 24,
    "rate": 1.0,
    "cohort_rate": 0.43636363636363634,
    "difference_from_cohort": 0.5636363636363637
  },
  {
    "feature": "stdout:ex07_1:relation",
    "value": "whitespace",
    "n": 24,
    "n_cluster": 24,
    "rate": 1.0,
    "cohort_rate": 0.43636363636363634,
    "difference_from_cohort": 0.5636363636363637
  },
  {
    "feature": "stdout:ex07_2:relation",
    "value": "whitespace",
    "n": 24,
    "n_cluster": 24,
    "rate": 1.0,
    "cohort_rate": 0.43636363636363634,
    "difference_from_cohort": 0.5636363636363637
  },
  {
    "feature": "stdout:ex07_3:edit_band",
    "value": "medium",
    "n": 24,
    "n_cluster": 24,
    "rate": 1.0,
    "cohort_rate": 0.43636363636363634,
    "difference_from_cohort": 0.5636363636363637
  },
  {
    "feature": "stdout:ex07_3:relation",
    "value": "whitespace",
    "n": 24,
    "n_cluster": 24,
    "rate": 1.0,
    "cohort_rate": 0.43636363636363634,
    "difference_from_cohort": 0.5636363636363637
  },
  {
    "feature": "stdout:ex07_2:edit_band",
    "value": "medium",
    "n": 24,
    "n_cluster": 24,
    "rate": 1.0,
    "cohort_rate": 0.45454545454545453,
    "difference_from_cohort": 0.5454545454545454
  },
  {
    "feature": "ast:c_while",
    "value": "1",
    "n": 20,
    "n_cluster": 24,
    "rate": 0.8333333333333334,
    "cohort_rate": 0.7090909090909091,
    "difference_from_cohort": 0.12424242424242427
  },
  {
    "feature": "test:ex07_0",
    "value": "fail",
    "n": 24,
    "n_cluster": 24,
    "rate": 1.0,
    "cohort_rate": 0.9090909090909091,
    "difference_from_cohort": 0.09090909090909094
  },
  {
    "feature": "ast:c_for",
    "value": "0",
    "n": 20,
    "n_cluster": 24,
    "rate": 0.8333333333333334,
    "cohort_rate": 0.7454545454545455,
    "difference_from_cohort": 0.08787878787878789
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 24,
    "n_cluster": 24,
    "rate": 1.0,
    "cohort_rate": 0.9454545454545454,
    "difference_from_cohort": 0.054545454545454564
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 24,
    "n_cluster": 24,
    "rate": 1.0,
    "cohort_rate": 0.9454545454545454,
    "difference_from_cohort": 0.054545454545454564
  },
  {
    "feature": "test:ex07_1",
    "value": "fail",
    "n": 24,
    "n_cluster": 24,
    "rate": 1.0,
    "cohort_rate": 0.9454545454545454,
    "difference_from_cohort": 0.054545454545454564
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 24,
    "n_cluster": 24,
    "rate": 1.0,
    "cohort_rate": 0.9636363636363636,
    "difference_from_cohort": 0.036363636363636376
  },
  {
    "feature": "test:ex07_2",
    "value": "fail",
    "n": 24,
    "n_cluster": 24,
    "rate": 1.0,
    "cohort_rate": 0.9636363636363636,
    "difference_from_cohort": 0.036363636363636376
  },
  {
    "feature": "test:ex07_3",
    "value": "fail",
    "n": 24,
    "n_cluster": 24,
    "rate": 1.0,
    "cohort_rate": 0.9636363636363636,
    "difference_from_cohort": 0.036363636363636376
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 9,
    "n_cluster": 24,
    "rate": 0.375,
    "cohort_rate": 0.34545454545454546,
    "difference_from_cohort": 0.02954545454545454
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "0",
    "n": 11,
    "n_cluster": 24,
    "rate": 0.4583333333333333,
    "cohort_rate": 0.45454545454545453,
    "difference_from_cohort": 0.0037878787878787845
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 13,
    "n_cluster": 24,
    "rate": 0.5416666666666666,
    "cohort_rate": 0.5454545454545454,
    "difference_from_cohort": -0.0037878787878787845
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_while",
    "value": "1",
    "n": 20,
    "n_cluster": 24,
    "rate": 0.8333333333333334,
    "cohort_rate": 0.7090909090909091,
    "difference_from_cohort": 0.12424242424242427
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 24,
    "n_cluster": 24,
    "rate": 1.0,
    "cohort_rate": 0.9454545454545454,
    "difference_from_cohort": 0.054545454545454564
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 24,
    "n_cluster": 24,
    "rate": 1.0,
    "cohort_rate": 0.9454545454545454,
    "difference_from_cohort": 0.054545454545454564
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 24,
    "n_cluster": 24,
    "rate": 1.0,
    "cohort_rate": 0.9636363636363636,
    "difference_from_cohort": 0.036363636363636376
  },
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 24,
    "n_cluster": 24,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 13,
    "n_cluster": 24,
    "rate": 0.5416666666666666,
    "cohort_rate": 0.5454545454545454,
    "difference_from_cohort": -0.0037878787878787845
  }
]
```


## IF–THEN dự đoán cluster, không dự đoán gold

```json
[
  {
    "rule_id": 2,
    "if": [
      "NOT (stdout:ex07_1:edit_band=large)",
      "NOT (stdout:ex07_0:edit_band=__unknown__)"
    ],
    "then_cluster": 1,
    "train_support": 16,
    "train_precision": 1.0,
    "holdout_support": 8,
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
  "reasoning": "Có 24 bài trong cụm. Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
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

sample_002, sample_008, sample_001, sample_004

## sample_001 — train — đại diện

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
    printf("%d", divisores);
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
  "source_sha256": "a25a181e6b75c91817963a5e46724da3f04112b37fc2d0627c68a2de101a98bd",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


## sample_002 — train — đại diện

```c
#include <stdio.h>

int N, contador = 1, passo = 1;

int main(){ 

    scanf("%d", &N);
     while (passo <= N / 2){
         if (N % passo == 0)
            contador += 1;
        passo ++;
     }

     printf("%d", contador);

     return 0;

}
```

```json
{
  "sample_id": "sample_002",
  "partition": "train",
  "representative": true,
  "is_train_medoid": true,
  "raw_code_truncated": false,
  "source_sha256": "ca569f463eb444c7a8c41f52871b5916c1f4094548825abd175ad11596378dd0",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


## sample_004 — validation — đại diện

```c


#include <stdio.h>

int main(){
    int n, divisor, contador = 0;
    scanf("%d", &n);
    divisor = n;
    while (divisor > 0){
        if (n % divisor == 0)
            contador++;
        divisor--;
    }
    printf("%d", contador);
    return 0;
}
```

```json
{
  "sample_id": "sample_004",
  "partition": "validation",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "931afb2162e24bcdac94041bec98b4e3bd7e99256f6cfcf697a6948fb3d28609",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


## sample_008 — validation — đại diện

```c

#include <stdio.h>

int main()
{
    int num,i, res=0;
    scanf("%d",&num);
    for(i=num; i>0; i--)
    {
        if (num%i ==0)
            res++;
    };
    printf("%d", res);
    return 0;
}
```

```json
{
  "sample_id": "sample_008",
  "partition": "validation",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "f9e8c37b24265ca3350c2343f757e7e6b61ba7f8ad6ef34e97d55af065868083",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


## sample_003 — train

```c


#include <stdio.h>

int main(){
    
    int N, V, Cont;
    scanf("%d",&N);
    
    V = 1;
    Cont = 0;
    
    while(V<=N){
        if(N%V==0){
            Cont++;
        }
        V++;
    }
    printf("%d",Cont);
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
  "source_sha256": "245badc632d1a7bf63b7d8924d9a697c7de8fda197f5dd9ec6a23b43085c665e",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


## sample_005 — validation

```c


#include <stdio.h>

int main(){
    int n, divisor, contador = 0;
    scanf("%d", &n);
    divisor = n;
    while (divisor > 0){
        if (n % divisor == 0)
            contador++;
        divisor--;
    }
    printf("%d", contador);
    return 0;
}
```

```json
{
  "sample_id": "sample_005",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "931afb2162e24bcdac94041bec98b4e3bd7e99256f6cfcf697a6948fb3d28609",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


## sample_006 — train

```c

#include <stdio.h>

int main () {
    int con = 1, N, ex = 1;
    scanf("%d", &N);
    while(N > ex){
        if (N % ex == 0){
            con ++;
            ex ++;
        }
        else
        ex++;
    }
    printf("%d",con);
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
  "source_sha256": "31145e842ec09d62ab55f40f2b381c7b74082748374e9f941a6f26b6d60f6542",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


## sample_007 — train

```c

#include <stdio.h>

int main(){
    int n, contador, i;
    contador=1;
    scanf("%d",&n);
    for(i = 2; i <= n; i++)
    {
        if (n%i==0)
        {
            contador++;
        }
        
    }
    printf("%d", contador);
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
  "source_sha256": "1f408444bc4323035087c5fc7a1a38cabaf4cbe6e39e0f2b1c8f529e208536b8",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


## sample_009 — train

```c


#include <stdio.h>

int main () 
{

int N, i = 1, numdiv = 0; 

scanf("%d", &N); 

while (i <= N) 
{
    if ((N%i) == 0)
    {
        numdiv++;
    }
    i++;
}
printf("%d", numdiv);
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
  "source_sha256": "43552f4bdafbb7a2ff06cdd10db7a8265b341ad4c26b0e9ffa9dd43aad21729d",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


#include <stdio.h>

int main () 
{

int N, i = 1, numdiv = 0; 

scanf("%d", &N);

while (i <= N) 
{
    if ((N%i) == 0)
    {
        numdiv++;
    }
i++;
}
printf("%d", numdiv);
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
  "source_sha256": "8054f9de4e6e978b023c4bcd4821c27e77df671885c05076c06aa5dcbd561379",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


## sample_011 — train

```c


#include <stdio.h>

int main(void) {

    int num, i, numdiv;
    scanf("%d", &num);
    numdiv = 0;

    i = 1;
    while (i <= num){
        if (num % i == 0)
            numdiv++;
        i++;
    }
    printf("%d", numdiv);    
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
  "source_sha256": "05ce470e122a5034c56d2acd4299e3aaa24e1ab68b0fe4c2ea2871bb04f17941",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


## sample_012 — train

```c


#include <stdio.h>

int main () {

    int v;
    int counter, num_div = 0;

    scanf("%d", &v);

    for (counter = 1; counter <= v; counter++) {
        if (v % counter == 0) {
            num_div++;
        }
    }
    printf("%d", num_div);
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
  "source_sha256": "18401c74493445961978577b8b61453987800e5826e3ba70ab69f64c7dc42eb8",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


## sample_013 — train

```c

#include <stdio.h>
int main () {
    int N, den = 1, div = 0;
    scanf("%d", &N);
    while (den <= N){
        if (N%den == 0){
            div++;
        }
        den++;       
    }
    printf("%d", div);
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
  "source_sha256": "eb8d4b048d91f796f0840d37d2c3f6505416d6f8864da5c7868a2416f8e9ed21",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


## sample_014 — train

```c

#include <stdio.h>

int main(){
    
    int N, contador_div=0, i=1;
    scanf("%d", &N);

    while (i <= N){
        if ((N % i) == 0)
            contador_div ++;
        i++;
    }
    printf("%d \n", contador_div);
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
  "source_sha256": "4f09001d09d7de981e81a45a18c9a4db8c66645f3cb84da07f127a706b8c3eb6",
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
      "output": "4 \n"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2 \n"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2 \n"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4 \n"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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

int main()
{
    int N, divisor = 1, contador = 0;

    scanf("%d", &N);

    while ( divisor <= N)
    {
        if ( N % divisor == 0)
        {
            contador++;
        }
        divisor++;
    }
    printf("%d", contador);
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
  "source_sha256": "79c3a9eda0bbb15f2ed36f8f4ec8a71d17a86f920b4cbe14bdd14b5abc80deaa",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


## sample_016 — train

```c

#include <stdio.h>

int main(){
    int n, i = 1, contador = 0;

    scanf("%d", &n);
    while (i <= n){
        if (n % i == 0){
            contador++;
        }
        i++;
    }
    printf("%d", contador);
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
  "source_sha256": "202da02c8cbf5aa28603d643d733fb84275bafcc8a31f230349e89a308973a2a",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


## sample_017 — validation

```c

#include <stdio.h>
int main()
{
    int n,cont=0,i;
    scanf("%d",&n);
    i=n;
    while(i>0)
    {
        if(n%i==0)
        {
            cont++;
        }
        i--;
    }
    printf("%d",cont);
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
  "source_sha256": "ba5c162ce21ed7dd2044e9bd6706bb5a00dc1951a701feca5f7137cf8b04427b",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


## sample_018 — validation

```c

#include <stdio.h>
int main()
{
    int n,cont,i;

    scanf("%d",&n);
    i=n;
    while(i>0)
    {
        if(n%i==0)
        {
            cont++;
        }
        i--;
    }
    printf("%d",cont);
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
  "source_sha256": "25313af6af047b0a7b96bd85735a74dab91379deb4f818e48236bb4611d930a7",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


## sample_019 — validation

```c

#include <stdio.h>
int main()
{
    int n,i;
    int cont=0;

    scanf("%d",&n);
    i=n;
    while(i>0)
    {
        if(n%i==0)
        {
            cont++;
        }
        --i;
    }
    printf("%d",cont);
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
  "source_sha256": "e183d2283091e7ae4fd26ad6ccdf7895991b8728f615a76f0f4d9851eeda5751",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


## sample_020 — validation

```c

#include <stdio.h>
int main()
{
    int n,cont=0,i;

    scanf("%d",&n);
    i=n;
    while(i>0)
    {
        if(n%i==0)
        {
            cont++;
        }
        i--;
    }
    printf("%d",cont);
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
  "source_sha256": "8c7045f1b182d29438fdbf144b6a3f82cda2912db2379cdf1604449112bec147",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


## sample_021 — validation

```c

#include <stdio.h>
int main()
{
    int n,cont=0,i;

    
    scanf("%d",&n);
    i=n;
    while(i>0)
    {
        if(n%i==0)
        {
            cont++;
        }
        i--;
    }
    printf("%d",cont);
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
  "source_sha256": "677cc0c94ac8b4ab188174c9474004fd83ccd3b3e6037be99dcd86afa88584e5",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


## sample_022 — train

```c

#include <stdio.h>

int main(){
    int num, aux;
    int contador;

    scanf("%d",&num);
    aux = num;

    while (aux >= 1){
        
        if (num % aux == 0){
            contador++;
        }
        aux--;
    }

    printf("%d",contador);

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
  "source_sha256": "3509b8b5ec167197fc1267dbf6095812e4b6513e91f07fbfcfe100361ed4ec18",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


## sample_023 — train

```c

#include <stdio.h>

int main() {
    int n, contador = 0, numeros = 1;
    scanf("%d", &n);
    while (n + 1 != numeros) {
        if (n % numeros == 0)
            contador++;
        numeros++;
    }
    printf("%d", contador);
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
  "source_sha256": "e7b57195e92403ee1b5221a93b9b21461d494c16d93eadd6ec6264c8f1510e1f",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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


## sample_024 — train

```c

#include <stdio.h>

int main() {
    int n, contador = 0, numeros = 1;
    scanf("%d", &n);
    while (n + 1 != numeros) {
        if (n % numeros == 0)
            contador++;
        numeros++;
    }
    printf("%d", contador);
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
  "source_sha256": "e7b57195e92403ee1b5221a93b9b21461d494c16d93eadd6ec6264c8f1510e1f",
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
      "output": "4"
    },
    {
      "test_id": "ex07_1",
      "input": "5",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_2",
      "input": "13",
      "expected": "2\n",
      "output": "2"
    },
    {
      "test_id": "ex07_3",
      "input": "10",
      "expected": "4\n",
      "output": "4"
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
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
  "members/sample_011/tests/ex07_0",
  "members/sample_011/tests/ex07_1",
  "members/sample_011/tests/ex07_2",
  "members/sample_011/tests/ex07_3",
  "members/sample_012/raw_code",
  "members/sample_012/tests/ex07_0",
  "members/sample_012/tests/ex07_1",
  "members/sample_012/tests/ex07_2",
  "members/sample_012/tests/ex07_3",
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
  "members/sample_024/tests/ex07_3"
]
```
