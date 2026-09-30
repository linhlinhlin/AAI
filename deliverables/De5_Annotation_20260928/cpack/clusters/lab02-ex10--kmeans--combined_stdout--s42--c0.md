# lab02-ex10--kmeans--combined_stdout--s42--c0

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 5; phân vùng: {'train': 3, 'validation': 2}.


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
    "test_id": "ex10_3",
    "n_cluster": 5,
    "n_observed": 5,
    "n_failed": 5,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 5
    }
  },
  {
    "test_id": "ex10_0",
    "n_cluster": 5,
    "n_observed": 5,
    "n_failed": 0,
    "n_not_run": 0,
    "failure_rate_observed": 0.0,
    "failure_rate_cluster": 0.0,
    "outcome_counts": {
      "pass": 5
    }
  },
  {
    "test_id": "ex10_1",
    "n_cluster": 5,
    "n_observed": 5,
    "n_failed": 0,
    "n_not_run": 0,
    "failure_rate_observed": 0.0,
    "failure_rate_cluster": 0.0,
    "outcome_counts": {
      "pass": 5
    }
  },
  {
    "test_id": "ex10_2",
    "n_cluster": 5,
    "n_observed": 5,
    "n_failed": 0,
    "n_not_run": 0,
    "failure_rate_observed": 0.0,
    "failure_rate_cluster": 0.0,
    "outcome_counts": {
      "pass": 5
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex10_1:edit_band",
    "value": "__unknown__",
    "n": 5,
    "n_cluster": 5,
    "rate": 1.0,
    "cohort_rate": 0.15151515151515152,
    "difference_from_cohort": 0.8484848484848485
  },
  {
    "feature": "stdout:ex10_1:relation",
    "value": "__unknown__",
    "n": 5,
    "n_cluster": 5,
    "rate": 1.0,
    "cohort_rate": 0.15151515151515152,
    "difference_from_cohort": 0.8484848484848485
  },
  {
    "feature": "stdout:ex10_2:edit_band",
    "value": "__unknown__",
    "n": 5,
    "n_cluster": 5,
    "rate": 1.0,
    "cohort_rate": 0.15151515151515152,
    "difference_from_cohort": 0.8484848484848485
  },
  {
    "feature": "stdout:ex10_2:relation",
    "value": "__unknown__",
    "n": 5,
    "n_cluster": 5,
    "rate": 1.0,
    "cohort_rate": 0.15151515151515152,
    "difference_from_cohort": 0.8484848484848485
  },
  {
    "feature": "test:ex10_1",
    "value": "pass",
    "n": 5,
    "n_cluster": 5,
    "rate": 1.0,
    "cohort_rate": 0.15151515151515152,
    "difference_from_cohort": 0.8484848484848485
  },
  {
    "feature": "test:ex10_2",
    "value": "pass",
    "n": 5,
    "n_cluster": 5,
    "rate": 1.0,
    "cohort_rate": 0.15151515151515152,
    "difference_from_cohort": 0.8484848484848485
  },
  {
    "feature": "stdout:ex10_0:edit_band",
    "value": "__unknown__",
    "n": 5,
    "n_cluster": 5,
    "rate": 1.0,
    "cohort_rate": 0.21212121212121213,
    "difference_from_cohort": 0.7878787878787878
  },
  {
    "feature": "stdout:ex10_0:relation",
    "value": "__unknown__",
    "n": 5,
    "n_cluster": 5,
    "rate": 1.0,
    "cohort_rate": 0.21212121212121213,
    "difference_from_cohort": 0.7878787878787878
  },
  {
    "feature": "test:ex10_0",
    "value": "pass",
    "n": 5,
    "n_cluster": 5,
    "rate": 1.0,
    "cohort_rate": 0.21212121212121213,
    "difference_from_cohort": 0.7878787878787878
  },
  {
    "feature": "stdout:ex10_3:relation",
    "value": "different",
    "n": 5,
    "n_cluster": 5,
    "rate": 1.0,
    "cohort_rate": 0.5454545454545454,
    "difference_from_cohort": 0.4545454545454546
  },
  {
    "feature": "stdout:ex10_3:edit_band",
    "value": "large",
    "n": 3,
    "n_cluster": 5,
    "rate": 0.6,
    "cohort_rate": 0.3333333333333333,
    "difference_from_cohort": 0.26666666666666666
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 1,
    "n_cluster": 5,
    "rate": 0.2,
    "cohort_rate": 0.030303030303030304,
    "difference_from_cohort": 0.1696969696969697
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 1,
    "n_cluster": 5,
    "rate": 0.2,
    "cohort_rate": 0.06060606060606061,
    "difference_from_cohort": 0.1393939393939394
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 5,
    "n_cluster": 5,
    "rate": 1.0,
    "cohort_rate": 0.8787878787878788,
    "difference_from_cohort": 0.12121212121212122
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "0",
    "n": 3,
    "n_cluster": 5,
    "rate": 0.6,
    "cohort_rate": 0.48484848484848486,
    "difference_from_cohort": 0.11515151515151512
  },
  {
    "feature": "test:ex10_3",
    "value": "fail",
    "n": 5,
    "n_cluster": 5,
    "rate": 1.0,
    "cohort_rate": 0.9090909090909091,
    "difference_from_cohort": 0.09090909090909094
  },
  {
    "feature": "ast:c_while",
    "value": "0",
    "n": 1,
    "n_cluster": 5,
    "rate": 0.2,
    "cohort_rate": 0.15151515151515152,
    "difference_from_cohort": 0.04848484848484849
  },
  {
    "feature": "ast:c_do",
    "value": "0",
    "n": 5,
    "n_cluster": 5,
    "rate": 1.0,
    "cohort_rate": 0.9696969696969697,
    "difference_from_cohort": 0.030303030303030276
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "0",
    "n": 5,
    "n_cluster": 5,
    "rate": 1.0,
    "cohort_rate": 0.9696969696969697,
    "difference_from_cohort": 0.030303030303030276
  },
  {
    "feature": "ast:c_update",
    "value": "0",
    "n": 1,
    "n_cluster": 5,
    "rate": 0.2,
    "cohort_rate": 0.18181818181818182,
    "difference_from_cohort": 0.018181818181818188
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 5,
    "n_cluster": 5,
    "rate": 1.0,
    "cohort_rate": 0.8787878787878788,
    "difference_from_cohort": 0.12121212121212122
  },
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 5,
    "n_cluster": 5,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 4,
    "n_cluster": 5,
    "rate": 0.8,
    "cohort_rate": 0.8181818181818182,
    "difference_from_cohort": -0.018181818181818188
  },
  {
    "feature": "ast:c_while",
    "value": "1",
    "n": 4,
    "n_cluster": 5,
    "rate": 0.8,
    "cohort_rate": 0.8484848484848485,
    "difference_from_cohort": -0.048484848484848464
  }
]
```


## IF–THEN dự đoán cluster, không dự đoán gold

```json
[
  {
    "rule_id": 2,
    "if": [
      "NOT (stdout:ex10_1:relation=different)",
      "NOT (test:ex10_1=fail)"
    ],
    "then_cluster": 0,
    "train_support": 3,
    "train_precision": 1.0,
    "holdout_support": 2,
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
  "reasoning": "Có 5 bài trong cụm. Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
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

sample_004, sample_001, sample_002, sample_003

## sample_001 — train — đại diện

```c


#include <stdio.h>

int main(void) {

    int num, acumuladornumdig, acumuladordig, soma;
    scanf("%d", &num);
    acumuladordig = num % 10;
    soma = 0;
    for (acumuladornumdig = 0; acumuladordig != 0; acumuladornumdig++){
        num = num / 10;
        soma += acumuladordig;
        acumuladordig = num % 10;
    }
    
    printf("%d\n%d\n", acumuladornumdig, soma);
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
  "source_sha256": "4a01cb24ee046989d1f734234d05aa74f86784645e7a3703f0791e67297eacef",
  "outcomes": {
    "ex10_0": "pass",
    "ex10_1": "pass",
    "ex10_2": "pass",
    "ex10_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex10_3",
      "input": "10",
      "expected": "2\n1\n",
      "output": "0\n0\n"
    }
  ],
  "clustering_oav": {
    "test:ex10_0": "pass",
    "test:ex10_1": "pass",
    "test:ex10_2": "pass",
    "test:ex10_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex10_0:relation": "__unknown__",
    "stdout:ex10_0:edit_band": "__unknown__",
    "stdout:ex10_1:relation": "__unknown__",
    "stdout:ex10_1:edit_band": "__unknown__",
    "stdout:ex10_2:relation": "__unknown__",
    "stdout:ex10_2:edit_band": "__unknown__",
    "stdout:ex10_3:relation": "different",
    "stdout:ex10_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex10_0": "pass",
    "test:ex10_1": "pass",
    "test:ex10_2": "pass",
    "test:ex10_3": "fail",
    "ast:c_for": "1",
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

int main() {

    int value, num = 0, soma = 0, var, dig;

    scanf("%d", &value);
    var = value;

    if (value < 10)
        printf("1\n%d\n", value);
    else
        while (var > 10) {
            dig = var % 10;
            soma += dig;
            num++;
            var = var / 10;
    }

    printf("%d\n%d\n", num + 1, soma + var);

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
  "source_sha256": "582ec4637e177f0463efc4d91bf38514d8aa1ace7e1481c6a95f2ed5d1a31e20",
  "outcomes": {
    "ex10_0": "pass",
    "ex10_1": "pass",
    "ex10_2": "pass",
    "ex10_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex10_3",
      "input": "10",
      "expected": "2\n1\n",
      "output": "1\n10\n"
    }
  ],
  "clustering_oav": {
    "test:ex10_0": "pass",
    "test:ex10_1": "pass",
    "test:ex10_2": "pass",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex10_0:relation": "__unknown__",
    "stdout:ex10_0:edit_band": "__unknown__",
    "stdout:ex10_1:relation": "__unknown__",
    "stdout:ex10_1:edit_band": "__unknown__",
    "stdout:ex10_2:relation": "__unknown__",
    "stdout:ex10_2:edit_band": "__unknown__",
    "stdout:ex10_3:relation": "different",
    "stdout:ex10_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex10_0": "pass",
    "test:ex10_1": "pass",
    "test:ex10_2": "pass",
    "test:ex10_3": "fail",
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


## sample_003 — validation — đại diện

```c

#include <stdio.h>

int main () {

    int soma = 0;
    int caracteres = 0;

    int numero;

    scanf("%d", &numero);

    while (numero % 10 != 0) {

        caracteres += 1;
        soma += numero % 10;

        numero /= 10;
    }

    printf("%d\n%d\n",caracteres,soma);

    return 0;
}
```

```json
{
  "sample_id": "sample_003",
  "partition": "validation",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "c478a2edda697b1b0ea1fa714175ba0667a5f5b3476dfc0ae2d0c69497ab0329",
  "outcomes": {
    "ex10_0": "pass",
    "ex10_1": "pass",
    "ex10_2": "pass",
    "ex10_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex10_3",
      "input": "10",
      "expected": "2\n1\n",
      "output": "0\n0\n"
    }
  ],
  "clustering_oav": {
    "test:ex10_0": "pass",
    "test:ex10_1": "pass",
    "test:ex10_2": "pass",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex10_0:relation": "__unknown__",
    "stdout:ex10_0:edit_band": "__unknown__",
    "stdout:ex10_1:relation": "__unknown__",
    "stdout:ex10_1:edit_band": "__unknown__",
    "stdout:ex10_2:relation": "__unknown__",
    "stdout:ex10_2:edit_band": "__unknown__",
    "stdout:ex10_3:relation": "different",
    "stdout:ex10_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex10_0": "pass",
    "test:ex10_1": "pass",
    "test:ex10_2": "pass",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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


## sample_004 — train — đại diện

```c


#include <stdio.h>

int main(){
    int num, soma;
    int contador = 0, dig;

    scanf("%d",&num);
    dig = num % 10;
    num = num / 10;

    while (dig != 0){
        contador++;
        soma += dig;

        dig = num % 10;
        num = num / 10;
    } 
    printf("%d\n%d\n",contador,soma);

    return 0;
}
```

```json
{
  "sample_id": "sample_004",
  "partition": "train",
  "representative": true,
  "is_train_medoid": true,
  "raw_code_truncated": false,
  "source_sha256": "4e823f7faa6e894109686e7573b9be4bb6f08939e14b41e6eef6ffb0ebab5b48",
  "outcomes": {
    "ex10_0": "pass",
    "ex10_1": "pass",
    "ex10_2": "pass",
    "ex10_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex10_3",
      "input": "10",
      "expected": "2\n1\n",
      "output": "0\n0\n"
    }
  ],
  "clustering_oav": {
    "test:ex10_0": "pass",
    "test:ex10_1": "pass",
    "test:ex10_2": "pass",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex10_0:relation": "__unknown__",
    "stdout:ex10_0:edit_band": "__unknown__",
    "stdout:ex10_1:relation": "__unknown__",
    "stdout:ex10_1:edit_band": "__unknown__",
    "stdout:ex10_2:relation": "__unknown__",
    "stdout:ex10_2:edit_band": "__unknown__",
    "stdout:ex10_3:relation": "different",
    "stdout:ex10_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex10_0": "pass",
    "test:ex10_1": "pass",
    "test:ex10_2": "pass",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_005 — validation

```c

#include<stdio.h>
int main(){
    int n, i = 1, s = 0;
    scanf("%d", &n);
    while (n > 10) {
        i++;
        s+= n % 10;
        n = n / 10;
    } printf("%d\n%d\n", i, s+n);
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
  "source_sha256": "783ff5ad089fcfa78efeeb306688948d7429d3c2036b5896aaea02ce4cd7bc25",
  "outcomes": {
    "ex10_0": "pass",
    "ex10_1": "pass",
    "ex10_2": "pass",
    "ex10_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex10_3",
      "input": "10",
      "expected": "2\n1\n",
      "output": "1\n10\n"
    }
  ],
  "clustering_oav": {
    "test:ex10_0": "pass",
    "test:ex10_1": "pass",
    "test:ex10_2": "pass",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex10_0:relation": "__unknown__",
    "stdout:ex10_0:edit_band": "__unknown__",
    "stdout:ex10_1:relation": "__unknown__",
    "stdout:ex10_1:edit_band": "__unknown__",
    "stdout:ex10_2:relation": "__unknown__",
    "stdout:ex10_2:edit_band": "__unknown__",
    "stdout:ex10_3:relation": "different",
    "stdout:ex10_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex10_0": "pass",
    "test:ex10_1": "pass",
    "test:ex10_2": "pass",
    "test:ex10_3": "fail",
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


## Evidence refs hợp lệ

```json
[
  "test_statistics",
  "feature_statistics",
  "learned_if_then_rules",
  "semantic_findings",
  "problem_statement",
  "members/sample_001/raw_code",
  "members/sample_001/tests/ex10_3",
  "members/sample_002/raw_code",
  "members/sample_002/tests/ex10_3",
  "members/sample_003/raw_code",
  "members/sample_003/tests/ex10_3",
  "members/sample_004/raw_code",
  "members/sample_004/tests/ex10_3",
  "members/sample_005/raw_code",
  "members/sample_005/tests/ex10_3"
]
```
