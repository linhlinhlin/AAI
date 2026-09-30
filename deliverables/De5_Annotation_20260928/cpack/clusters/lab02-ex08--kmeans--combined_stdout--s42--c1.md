# lab02-ex08--kmeans--combined_stdout--s42--c1

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 21; phân vùng: {'train': 16, 'validation': 5}.


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
    "test_id": "ex08_0",
    "n_cluster": 21,
    "n_observed": 21,
    "n_failed": 21,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 21
    }
  },
  {
    "test_id": "ex08_1",
    "n_cluster": 21,
    "n_observed": 21,
    "n_failed": 21,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 21
    }
  },
  {
    "test_id": "ex08_2",
    "n_cluster": 21,
    "n_observed": 21,
    "n_failed": 21,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 21
    }
  },
  {
    "test_id": "ex08_3",
    "n_cluster": 21,
    "n_observed": 21,
    "n_failed": 21,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 21
    }
  },
  {
    "test_id": "ex08_4",
    "n_cluster": 21,
    "n_observed": 21,
    "n_failed": 21,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 21
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex08_3:edit_band",
    "value": "large",
    "n": 20,
    "n_cluster": 21,
    "rate": 0.9523809523809523,
    "cohort_rate": 0.28205128205128205,
    "difference_from_cohort": 0.6703296703296703
  },
  {
    "feature": "stdout:ex08_0:edit_band",
    "value": "large",
    "n": 19,
    "n_cluster": 21,
    "rate": 0.9047619047619048,
    "cohort_rate": 0.24358974358974358,
    "difference_from_cohort": 0.6611721611721612
  },
  {
    "feature": "stdout:ex08_2:edit_band",
    "value": "large",
    "n": 19,
    "n_cluster": 21,
    "rate": 0.9047619047619048,
    "cohort_rate": 0.24358974358974358,
    "difference_from_cohort": 0.6611721611721612
  },
  {
    "feature": "stdout:ex08_1:edit_band",
    "value": "large",
    "n": 18,
    "n_cluster": 21,
    "rate": 0.8571428571428571,
    "cohort_rate": 0.23076923076923078,
    "difference_from_cohort": 0.6263736263736264
  },
  {
    "feature": "stdout:ex08_4:edit_band",
    "value": "large",
    "n": 19,
    "n_cluster": 21,
    "rate": 0.9047619047619048,
    "cohort_rate": 0.28205128205128205,
    "difference_from_cohort": 0.6227106227106227
  },
  {
    "feature": "stdout:ex08_1:relation",
    "value": "different",
    "n": 20,
    "n_cluster": 21,
    "rate": 0.9523809523809523,
    "cohort_rate": 0.44871794871794873,
    "difference_from_cohort": 0.5036630036630036
  },
  {
    "feature": "stdout:ex08_2:relation",
    "value": "different",
    "n": 20,
    "n_cluster": 21,
    "rate": 0.9523809523809523,
    "cohort_rate": 0.47435897435897434,
    "difference_from_cohort": 0.478021978021978
  },
  {
    "feature": "stdout:ex08_3:relation",
    "value": "different",
    "n": 20,
    "n_cluster": 21,
    "rate": 0.9523809523809523,
    "cohort_rate": 0.47435897435897434,
    "difference_from_cohort": 0.478021978021978
  },
  {
    "feature": "stdout:ex08_4:relation",
    "value": "different",
    "n": 20,
    "n_cluster": 21,
    "rate": 0.9523809523809523,
    "cohort_rate": 0.47435897435897434,
    "difference_from_cohort": 0.478021978021978
  },
  {
    "feature": "stdout:ex08_0:relation",
    "value": "different",
    "n": 19,
    "n_cluster": 21,
    "rate": 0.9047619047619048,
    "cohort_rate": 0.4358974358974359,
    "difference_from_cohort": 0.46886446886446886
  },
  {
    "feature": "ast:c_for",
    "value": "0",
    "n": 16,
    "n_cluster": 21,
    "rate": 0.7619047619047619,
    "cohort_rate": 0.5769230769230769,
    "difference_from_cohort": 0.184981684981685
  },
  {
    "feature": "ast:c_update",
    "value": "0",
    "n": 6,
    "n_cluster": 21,
    "rate": 0.2857142857142857,
    "cohort_rate": 0.15384615384615385,
    "difference_from_cohort": 0.13186813186813184
  },
  {
    "feature": "ast:c_while",
    "value": "1",
    "n": 14,
    "n_cluster": 21,
    "rate": 0.6666666666666666,
    "cohort_rate": 0.5512820512820513,
    "difference_from_cohort": 0.11538461538461531
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "0",
    "n": 9,
    "n_cluster": 21,
    "rate": 0.42857142857142855,
    "cohort_rate": 0.34615384615384615,
    "difference_from_cohort": 0.0824175824175824
  },
  {
    "feature": "stdout:ex08_0:relation",
    "value": "empty",
    "n": 1,
    "n_cluster": 21,
    "rate": 0.047619047619047616,
    "cohort_rate": 0.01282051282051282,
    "difference_from_cohort": 0.0347985347985348
  },
  {
    "feature": "stdout:ex08_1:relation",
    "value": "empty",
    "n": 1,
    "n_cluster": 21,
    "rate": 0.047619047619047616,
    "cohort_rate": 0.01282051282051282,
    "difference_from_cohort": 0.0347985347985348
  },
  {
    "feature": "stdout:ex08_2:relation",
    "value": "empty",
    "n": 1,
    "n_cluster": 21,
    "rate": 0.047619047619047616,
    "cohort_rate": 0.01282051282051282,
    "difference_from_cohort": 0.0347985347985348
  },
  {
    "feature": "stdout:ex08_3:relation",
    "value": "empty",
    "n": 1,
    "n_cluster": 21,
    "rate": 0.047619047619047616,
    "cohort_rate": 0.01282051282051282,
    "difference_from_cohort": 0.0347985347985348
  },
  {
    "feature": "stdout:ex08_4:relation",
    "value": "empty",
    "n": 1,
    "n_cluster": 21,
    "rate": 0.047619047619047616,
    "cohort_rate": 0.01282051282051282,
    "difference_from_cohort": 0.0347985347985348
  },
  {
    "feature": "test:ex08_0",
    "value": "fail",
    "n": 21,
    "n_cluster": 21,
    "rate": 1.0,
    "cohort_rate": 0.9743589743589743,
    "difference_from_cohort": 0.02564102564102566
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_while",
    "value": "1",
    "n": 14,
    "n_cluster": 21,
    "rate": 0.6666666666666666,
    "cohort_rate": 0.5512820512820513,
    "difference_from_cohort": 0.11538461538461531
  },
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 21,
    "n_cluster": 21,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 20,
    "n_cluster": 21,
    "rate": 0.9523809523809523,
    "cohort_rate": 0.9871794871794872,
    "difference_from_cohort": -0.0347985347985349
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 12,
    "n_cluster": 21,
    "rate": 0.5714285714285714,
    "cohort_rate": 0.6538461538461539,
    "difference_from_cohort": -0.08241758241758246
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 15,
    "n_cluster": 21,
    "rate": 0.7142857142857143,
    "cohort_rate": 0.8461538461538461,
    "difference_from_cohort": -0.13186813186813184
  }
]
```


## IF–THEN dự đoán cluster, không dự đoán gold

```json
[
  {
    "rule_id": 2,
    "if": [
      "NOT (stdout:ex08_1:relation=whitespace)",
      "NOT (stdout:ex08_2:edit_band=medium)"
    ],
    "then_cluster": 1,
    "train_support": 15,
    "train_precision": 1.0,
    "holdout_support": 4,
    "holdout_precision": 1.0
  },
  {
    "rule_id": 4,
    "if": [
      "NOT (stdout:ex08_1:relation=whitespace)",
      "stdout:ex08_2:edit_band=medium",
      "NOT (stdout:ex08_0:edit_band=medium)"
    ],
    "then_cluster": 1,
    "train_support": 2,
    "train_precision": 0.5,
    "holdout_support": 2,
    "holdout_precision": 0.5
  }
]
```


## Candidate chưa xác thực

```json
{
  "source": "local_heuristic_not_gold",
  "misconception_name": "Chưa đủ bằng chứng để đặt tên lỗi",
  "misconception_type": null,
  "reasoning": "Có 21 bài trong cụm. Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
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

sample_002, sample_018, sample_003, sample_005

## sample_002 — train — đại diện

```c

#include <stdio.h>


int main() {
    int n;
    float total = 0.00;
    float num, media;

    scanf("%d", &n);

    while (n > 0) {
        scanf("%f", &num);
        total = total + num;
        n--;
    }

    media = (total)/(n);

    printf("%.2f\n", media);

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
  "source_sha256": "92eb8c3fca30dc271b325020ececc59b3553b7e1b38eec7178b9b1ec609dcade",
  "outcomes": {
    "ex08_0": "fail",
    "ex08_1": "fail",
    "ex08_2": "fail",
    "ex08_3": "fail",
    "ex08_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex08_0",
      "input": "2 3 3",
      "expected": "3.00\n",
      "output": "inf\n"
    },
    {
      "test_id": "ex08_1",
      "input": "2 2 3",
      "expected": "2.50\n",
      "output": "inf\n"
    },
    {
      "test_id": "ex08_2",
      "input": "3 1.5 2.7 3",
      "expected": "2.40\n",
      "output": "inf\n"
    },
    {
      "test_id": "ex08_3",
      "input": "4 6.8 2 1 0",
      "expected": "2.45\n",
      "output": "inf\n"
    },
    {
      "test_id": "ex08_4",
      "input": "3 -1.8 3.14 1",
      "expected": "0.78\n",
      "output": "inf\n"
    }
  ],
  "clustering_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "1",
    "stdout:ex08_0:relation": "different",
    "stdout:ex08_0:edit_band": "large",
    "stdout:ex08_1:relation": "different",
    "stdout:ex08_1:edit_band": "large",
    "stdout:ex08_2:relation": "different",
    "stdout:ex08_2:edit_band": "large",
    "stdout:ex08_3:relation": "different",
    "stdout:ex08_3:edit_band": "large",
    "stdout:ex08_4:relation": "different",
    "stdout:ex08_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
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


## sample_003 — train — đại diện

```c

#include<stdio.h>

int main(){

int N, contador;
float a , media, soma ;
printf("Quantos numeros quer inserir?\n" );

scanf("%d", &N) ;
contador =1;
soma = 0;
printf("Digite os numeros\n" );

while ( contador <= N ){

    scanf("%f", &a );

    soma = soma + a ;
    
    contador = contador + 1;
    
}

media = soma / N ;

printf("A media dos numeros inseridos é %.2f\n", media) ;

return 0 ;

}
```

```json
{
  "sample_id": "sample_003",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "cbbc9429f4ea2896472c4cce06a36d11f6cbd4d2b6ffbd643492fa5e7a9763d5",
  "outcomes": {
    "ex08_0": "fail",
    "ex08_1": "fail",
    "ex08_2": "fail",
    "ex08_3": "fail",
    "ex08_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex08_0",
      "input": "2 3 3",
      "expected": "3.00\n",
      "output": "Quantos numeros quer inserir?\nDigite os numeros\nA media dos numeros inseridos é 3.00\n"
    },
    {
      "test_id": "ex08_1",
      "input": "2 2 3",
      "expected": "2.50\n",
      "output": "Quantos numeros quer inserir?\nDigite os numeros\nA media dos numeros inseridos é 2.50\n"
    },
    {
      "test_id": "ex08_2",
      "input": "3 1.5 2.7 3",
      "expected": "2.40\n",
      "output": "Quantos numeros quer inserir?\nDigite os numeros\nA media dos numeros inseridos é 2.40\n"
    },
    {
      "test_id": "ex08_3",
      "input": "4 6.8 2 1 0",
      "expected": "2.45\n",
      "output": "Quantos numeros quer inserir?\nDigite os numeros\nA media dos numeros inseridos é 2.45\n"
    },
    {
      "test_id": "ex08_4",
      "input": "3 -1.8 3.14 1",
      "expected": "0.78\n",
      "output": "Quantos numeros quer inserir?\nDigite os numeros\nA media dos numeros inseridos é 0.78\n"
    }
  ],
  "clustering_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_update": "0",
    "stdout:ex08_0:relation": "different",
    "stdout:ex08_0:edit_band": "large",
    "stdout:ex08_1:relation": "different",
    "stdout:ex08_1:edit_band": "large",
    "stdout:ex08_2:relation": "different",
    "stdout:ex08_2:edit_band": "large",
    "stdout:ex08_3:relation": "different",
    "stdout:ex08_3:edit_band": "large",
    "stdout:ex08_4:relation": "different",
    "stdout:ex08_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_005 — validation — đại diện

```c


#include <stdio.h>

int main(){
    int n, i, contador=0;
    float x, media;

    scanf("%d", &n);
    for(i = 0; i < n; i++){
        scanf("%f", &x);
        contador += 1;
        if (i == 0)
          media = x;
        media = ((media + x)/contador);
    }
    printf("%.2f", media);
    
    return 0;
}
```

```json
{
  "sample_id": "sample_005",
  "partition": "validation",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "55708a290c571a64d9d5aaa98821f9657e1559928b82d401bc8fd8f4128869db",
  "outcomes": {
    "ex08_0": "fail",
    "ex08_1": "fail",
    "ex08_2": "fail",
    "ex08_3": "fail",
    "ex08_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex08_0",
      "input": "2 3 3",
      "expected": "3.00\n",
      "output": "4.50"
    },
    {
      "test_id": "ex08_1",
      "input": "2 2 3",
      "expected": "2.50\n",
      "output": "3.50"
    },
    {
      "test_id": "ex08_2",
      "input": "3 1.5 2.7 3",
      "expected": "2.40\n",
      "output": "1.95"
    },
    {
      "test_id": "ex08_3",
      "input": "4 6.8 2 1 0",
      "expected": "2.45\n",
      "output": "0.73"
    },
    {
      "test_id": "ex08_4",
      "input": "3 -1.8 3.14 1",
      "expected": "0.78\n",
      "output": "0.26"
    }
  ],
  "clustering_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "1",
    "stdout:ex08_0:relation": "different",
    "stdout:ex08_0:edit_band": "large",
    "stdout:ex08_1:relation": "different",
    "stdout:ex08_1:edit_band": "medium",
    "stdout:ex08_2:relation": "different",
    "stdout:ex08_2:edit_band": "large",
    "stdout:ex08_3:relation": "different",
    "stdout:ex08_3:edit_band": "large",
    "stdout:ex08_4:relation": "different",
    "stdout:ex08_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
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
    "ex08_0": "fail",
    "ex08_1": "fail",
    "ex08_2": "fail",
    "ex08_3": "fail",
    "ex08_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex08_0",
      "input": "2 3 3",
      "expected": "3.00\n",
      "output": ""
    },
    {
      "test_id": "ex08_1",
      "input": "2 2 3",
      "expected": "2.50\n",
      "output": ""
    },
    {
      "test_id": "ex08_2",
      "input": "3 1.5 2.7 3",
      "expected": "2.40\n",
      "output": ""
    },
    {
      "test_id": "ex08_3",
      "input": "4 6.8 2 1 0",
      "expected": "2.45\n",
      "output": ""
    },
    {
      "test_id": "ex08_4",
      "input": "3 -1.8 3.14 1",
      "expected": "0.78\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_update": "0",
    "stdout:ex08_0:relation": "empty",
    "stdout:ex08_0:edit_band": "large",
    "stdout:ex08_1:relation": "empty",
    "stdout:ex08_1:edit_band": "large",
    "stdout:ex08_2:relation": "empty",
    "stdout:ex08_2:edit_band": "large",
    "stdout:ex08_3:relation": "empty",
    "stdout:ex08_3:edit_band": "large",
    "stdout:ex08_4:relation": "empty",
    "stdout:ex08_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
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

#define PASSO 1

float N, num, media, soma = 0;
float inicial = 0;

int main(){

    scanf("%f", &N);
    while (inicial < N){
        scanf("%f", &num);
        soma += num;
        inicial += PASSO;
    }

    media = soma / N;
    printf("%2.f\n", media);

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
  "source_sha256": "de7d2d603d5cbf5e1e8e6e31b8dea9c0c3c8ae8fa6a42df4bad50f0e55fe816b",
  "outcomes": {
    "ex08_0": "fail",
    "ex08_1": "fail",
    "ex08_2": "fail",
    "ex08_3": "fail",
    "ex08_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex08_0",
      "input": "2 3 3",
      "expected": "3.00\n",
      "output": " 3\n"
    },
    {
      "test_id": "ex08_1",
      "input": "2 2 3",
      "expected": "2.50\n",
      "output": " 2\n"
    },
    {
      "test_id": "ex08_2",
      "input": "3 1.5 2.7 3",
      "expected": "2.40\n",
      "output": " 2\n"
    },
    {
      "test_id": "ex08_3",
      "input": "4 6.8 2 1 0",
      "expected": "2.45\n",
      "output": " 2\n"
    },
    {
      "test_id": "ex08_4",
      "input": "3 -1.8 3.14 1",
      "expected": "0.78\n",
      "output": " 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex08_0:relation": "different",
    "stdout:ex08_0:edit_band": "large",
    "stdout:ex08_1:relation": "different",
    "stdout:ex08_1:edit_band": "large",
    "stdout:ex08_2:relation": "different",
    "stdout:ex08_2:edit_band": "large",
    "stdout:ex08_3:relation": "different",
    "stdout:ex08_3:edit_band": "large",
    "stdout:ex08_4:relation": "different",
    "stdout:ex08_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
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


## sample_004 — train

```c

#include<stdio.h>

int main(){

int N, contador;
float a , media, soma ;
printf("Quantos numeros quer inserir?\n" );

scanf("%d", &N) ;
contador =1;
soma = 0;
printf("Digite os numeros\n" );

while ( contador <= N ){

    scanf("%f", &a );

    soma = soma + a ;
    
    contador = contador + 1;
    
}

media = soma / N ;

printf("A media dos numeros inseridos é %.2f\n", media) ;

return 0 ;

}
```

```json
{
  "sample_id": "sample_004",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "cbbc9429f4ea2896472c4cce06a36d11f6cbd4d2b6ffbd643492fa5e7a9763d5",
  "outcomes": {
    "ex08_0": "fail",
    "ex08_1": "fail",
    "ex08_2": "fail",
    "ex08_3": "fail",
    "ex08_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex08_0",
      "input": "2 3 3",
      "expected": "3.00\n",
      "output": "Quantos numeros quer inserir?\nDigite os numeros\nA media dos numeros inseridos é 3.00\n"
    },
    {
      "test_id": "ex08_1",
      "input": "2 2 3",
      "expected": "2.50\n",
      "output": "Quantos numeros quer inserir?\nDigite os numeros\nA media dos numeros inseridos é 2.50\n"
    },
    {
      "test_id": "ex08_2",
      "input": "3 1.5 2.7 3",
      "expected": "2.40\n",
      "output": "Quantos numeros quer inserir?\nDigite os numeros\nA media dos numeros inseridos é 2.40\n"
    },
    {
      "test_id": "ex08_3",
      "input": "4 6.8 2 1 0",
      "expected": "2.45\n",
      "output": "Quantos numeros quer inserir?\nDigite os numeros\nA media dos numeros inseridos é 2.45\n"
    },
    {
      "test_id": "ex08_4",
      "input": "3 -1.8 3.14 1",
      "expected": "0.78\n",
      "output": "Quantos numeros quer inserir?\nDigite os numeros\nA media dos numeros inseridos é 0.78\n"
    }
  ],
  "clustering_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_update": "0",
    "stdout:ex08_0:relation": "different",
    "stdout:ex08_0:edit_band": "large",
    "stdout:ex08_1:relation": "different",
    "stdout:ex08_1:edit_band": "large",
    "stdout:ex08_2:relation": "different",
    "stdout:ex08_2:edit_band": "large",
    "stdout:ex08_3:relation": "different",
    "stdout:ex08_3:edit_band": "large",
    "stdout:ex08_4:relation": "different",
    "stdout:ex08_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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

int main()
{
    int N, i;
    float sum = 0, val, media;

    printf("%s\n", "Introduza a quantidade de valores:"); 
    scanf("%d", &N);
    printf("%s\n", "Introduza os valores que deseja calcular a média: "); 

    for (i=0; i<N; i++){
        scanf("%f", &val);
        sum+=val;
    }
    media = sum/N;

    printf("A média destes valores é %.2f\n", media);

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
  "source_sha256": "d9e8277fad0321372b349f9bd269044fa480ecc49c4f613121641cd322a62dfe",
  "outcomes": {
    "ex08_0": "fail",
    "ex08_1": "fail",
    "ex08_2": "fail",
    "ex08_3": "fail",
    "ex08_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex08_0",
      "input": "2 3 3",
      "expected": "3.00\n",
      "output": "Introduza a quantidade de valores:\nIntroduza os valores que deseja calcular a média: \nA média destes valores é 3.00\n"
    },
    {
      "test_id": "ex08_1",
      "input": "2 2 3",
      "expected": "2.50\n",
      "output": "Introduza a quantidade de valores:\nIntroduza os valores que deseja calcular a média: \nA média destes valores é 2.50\n"
    },
    {
      "test_id": "ex08_2",
      "input": "3 1.5 2.7 3",
      "expected": "2.40\n",
      "output": "Introduza a quantidade de valores:\nIntroduza os valores que deseja calcular a média: \nA média destes valores é 2.40\n"
    },
    {
      "test_id": "ex08_3",
      "input": "4 6.8 2 1 0",
      "expected": "2.45\n",
      "output": "Introduza a quantidade de valores:\nIntroduza os valores que deseja calcular a média: \nA média destes valores é 2.45\n"
    },
    {
      "test_id": "ex08_4",
      "input": "3 -1.8 3.14 1",
      "expected": "0.78\n",
      "output": "Introduza a quantidade de valores:\nIntroduza os valores que deseja calcular a média: \nA média destes valores é 0.78\n"
    }
  ],
  "clustering_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "1",
    "stdout:ex08_0:relation": "different",
    "stdout:ex08_0:edit_band": "large",
    "stdout:ex08_1:relation": "different",
    "stdout:ex08_1:edit_band": "large",
    "stdout:ex08_2:relation": "different",
    "stdout:ex08_2:edit_band": "large",
    "stdout:ex08_3:relation": "different",
    "stdout:ex08_3:edit_band": "large",
    "stdout:ex08_4:relation": "different",
    "stdout:ex08_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
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


## sample_007 — train

```c


#include <stdio.h>

int main()
{
    int N, i;
    float sum = 0, val, media;

    printf("%s\n", "Introduza a quantidade de valores:"); 
    scanf("%d", &N);
    printf("%s\n", "Introduza os valores que deseja calcular a média: "); 

    for (i=0; i<N; i++){
        scanf("%f", &val);
        sum+=val;
    }
    media = sum/N;

    printf("A média destes valores é %.2f\n", media);

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
  "source_sha256": "d9e8277fad0321372b349f9bd269044fa480ecc49c4f613121641cd322a62dfe",
  "outcomes": {
    "ex08_0": "fail",
    "ex08_1": "fail",
    "ex08_2": "fail",
    "ex08_3": "fail",
    "ex08_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex08_0",
      "input": "2 3 3",
      "expected": "3.00\n",
      "output": "Introduza a quantidade de valores:\nIntroduza os valores que deseja calcular a média: \nA média destes valores é 3.00\n"
    },
    {
      "test_id": "ex08_1",
      "input": "2 2 3",
      "expected": "2.50\n",
      "output": "Introduza a quantidade de valores:\nIntroduza os valores que deseja calcular a média: \nA média destes valores é 2.50\n"
    },
    {
      "test_id": "ex08_2",
      "input": "3 1.5 2.7 3",
      "expected": "2.40\n",
      "output": "Introduza a quantidade de valores:\nIntroduza os valores que deseja calcular a média: \nA média destes valores é 2.40\n"
    },
    {
      "test_id": "ex08_3",
      "input": "4 6.8 2 1 0",
      "expected": "2.45\n",
      "output": "Introduza a quantidade de valores:\nIntroduza os valores que deseja calcular a média: \nA média destes valores é 2.45\n"
    },
    {
      "test_id": "ex08_4",
      "input": "3 -1.8 3.14 1",
      "expected": "0.78\n",
      "output": "Introduza a quantidade de valores:\nIntroduza os valores que deseja calcular a média: \nA média destes valores é 0.78\n"
    }
  ],
  "clustering_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "1",
    "stdout:ex08_0:relation": "different",
    "stdout:ex08_0:edit_band": "large",
    "stdout:ex08_1:relation": "different",
    "stdout:ex08_1:edit_band": "large",
    "stdout:ex08_2:relation": "different",
    "stdout:ex08_2:edit_band": "large",
    "stdout:ex08_3:relation": "different",
    "stdout:ex08_3:edit_band": "large",
    "stdout:ex08_4:relation": "different",
    "stdout:ex08_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
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


## sample_008 — train

```c


#include <stdio.h>

int main()
{
    int N, i;
    float sum = 0, val, media;

    printf("%s\n", "Introduza a quantidade de valores:"); 
    scanf("%d", &N);
    printf("%s\n", "Introduza os valores que deseja calcular a média: "); 

    for (i=0; i<N; i++){
        scanf("%f", &val);
        sum+=val;
    }
    media = sum/N;

    printf("A média destes valores é %.2f\n", media);

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
  "source_sha256": "314e8d0ed7619eee82fc9c85c55ddf02f10b2f189575fcda6d9782e91d0c5e27",
  "outcomes": {
    "ex08_0": "fail",
    "ex08_1": "fail",
    "ex08_2": "fail",
    "ex08_3": "fail",
    "ex08_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex08_0",
      "input": "2 3 3",
      "expected": "3.00\n",
      "output": "Introduza a quantidade de valores:\nIntroduza os valores que deseja calcular a média: \nA média destes valores é 3.00\n"
    },
    {
      "test_id": "ex08_1",
      "input": "2 2 3",
      "expected": "2.50\n",
      "output": "Introduza a quantidade de valores:\nIntroduza os valores que deseja calcular a média: \nA média destes valores é 2.50\n"
    },
    {
      "test_id": "ex08_2",
      "input": "3 1.5 2.7 3",
      "expected": "2.40\n",
      "output": "Introduza a quantidade de valores:\nIntroduza os valores que deseja calcular a média: \nA média destes valores é 2.40\n"
    },
    {
      "test_id": "ex08_3",
      "input": "4 6.8 2 1 0",
      "expected": "2.45\n",
      "output": "Introduza a quantidade de valores:\nIntroduza os valores que deseja calcular a média: \nA média destes valores é 2.45\n"
    },
    {
      "test_id": "ex08_4",
      "input": "3 -1.8 3.14 1",
      "expected": "0.78\n",
      "output": "Introduza a quantidade de valores:\nIntroduza os valores que deseja calcular a média: \nA média destes valores é 0.78\n"
    }
  ],
  "clustering_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "1",
    "stdout:ex08_0:relation": "different",
    "stdout:ex08_0:edit_band": "large",
    "stdout:ex08_1:relation": "different",
    "stdout:ex08_1:edit_band": "large",
    "stdout:ex08_2:relation": "different",
    "stdout:ex08_2:edit_band": "large",
    "stdout:ex08_3:relation": "different",
    "stdout:ex08_3:edit_band": "large",
    "stdout:ex08_4:relation": "different",
    "stdout:ex08_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
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


## sample_009 — train

```c


#include <stdio.h>

int main () {

    int num_v, counter;
    float val, soma = 0, media;

    scanf("%d", &num_v);
    
    scanf("%f", &val);
    for (counter = 1; counter < num_v; counter++) {
        scanf("%f", &val);
        soma += val;
    }

    media = soma / num_v;
    printf("%.2f", media);
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
  "source_sha256": "af0df9d197929366f0c837421961e88075827804204e7d26f6099762517b1e94",
  "outcomes": {
    "ex08_0": "fail",
    "ex08_1": "fail",
    "ex08_2": "fail",
    "ex08_3": "fail",
    "ex08_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex08_0",
      "input": "2 3 3",
      "expected": "3.00\n",
      "output": "1.50"
    },
    {
      "test_id": "ex08_1",
      "input": "2 2 3",
      "expected": "2.50\n",
      "output": "1.50"
    },
    {
      "test_id": "ex08_2",
      "input": "3 1.5 2.7 3",
      "expected": "2.40\n",
      "output": "1.90"
    },
    {
      "test_id": "ex08_3",
      "input": "4 6.8 2 1 0",
      "expected": "2.45\n",
      "output": "0.75"
    },
    {
      "test_id": "ex08_4",
      "input": "3 -1.8 3.14 1",
      "expected": "0.78\n",
      "output": "1.38"
    }
  ],
  "clustering_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "1",
    "stdout:ex08_0:relation": "different",
    "stdout:ex08_0:edit_band": "large",
    "stdout:ex08_1:relation": "different",
    "stdout:ex08_1:edit_band": "medium",
    "stdout:ex08_2:relation": "different",
    "stdout:ex08_2:edit_band": "large",
    "stdout:ex08_3:relation": "different",
    "stdout:ex08_3:edit_band": "large",
    "stdout:ex08_4:relation": "different",
    "stdout:ex08_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
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


## sample_010 — train

```c


#include <stdio.h>

int main(){
    int n;
    float valor,total,media;
    scanf("%d\n", &n);
    scanf("%f\n", &valor);
    total = valor;
    while(n>1){
        scanf("%f\n", &valor);
        total = total + valor;
        n--;
    }
    media = total / n;
    printf("%.2f", media);
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
  "source_sha256": "2f7a3dc59b0c90f9535b40e42f502d412592a974d931d667855a49998eaa6298",
  "outcomes": {
    "ex08_0": "fail",
    "ex08_1": "fail",
    "ex08_2": "fail",
    "ex08_3": "fail",
    "ex08_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex08_0",
      "input": "2 3 3",
      "expected": "3.00\n",
      "output": "6.00"
    },
    {
      "test_id": "ex08_1",
      "input": "2 2 3",
      "expected": "2.50\n",
      "output": "5.00"
    },
    {
      "test_id": "ex08_2",
      "input": "3 1.5 2.7 3",
      "expected": "2.40\n",
      "output": "7.20"
    },
    {
      "test_id": "ex08_3",
      "input": "4 6.8 2 1 0",
      "expected": "2.45\n",
      "output": "9.80"
    },
    {
      "test_id": "ex08_4",
      "input": "3 -1.8 3.14 1",
      "expected": "0.78\n",
      "output": "2.34"
    }
  ],
  "clustering_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "1",
    "stdout:ex08_0:relation": "different",
    "stdout:ex08_0:edit_band": "medium",
    "stdout:ex08_1:relation": "different",
    "stdout:ex08_1:edit_band": "large",
    "stdout:ex08_2:relation": "different",
    "stdout:ex08_2:edit_band": "large",
    "stdout:ex08_3:relation": "different",
    "stdout:ex08_3:edit_band": "large",
    "stdout:ex08_4:relation": "different",
    "stdout:ex08_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
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


## sample_011 — train

```c


#include <stdio.h>

int main(){
    int n;
    float valor,total,media;
    scanf("%d\n", &n);
    scanf("%f\n", &valor);
    total = valor;
    while(n>0){
        scanf("%f\n", &valor);
        total = total + valor;
        n--;
    }
    media = total / n;
    printf("%.2f", media);
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
  "source_sha256": "23a96544b9b6343fd079b3e84fb1438e37fd8e8bb2db968b9f7a0944134aa294",
  "outcomes": {
    "ex08_0": "fail",
    "ex08_1": "fail",
    "ex08_2": "fail",
    "ex08_3": "fail",
    "ex08_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex08_0",
      "input": "2 3 3",
      "expected": "3.00\n",
      "output": "inf"
    },
    {
      "test_id": "ex08_1",
      "input": "2 2 3",
      "expected": "2.50\n",
      "output": "inf"
    },
    {
      "test_id": "ex08_2",
      "input": "3 1.5 2.7 3",
      "expected": "2.40\n",
      "output": "inf"
    },
    {
      "test_id": "ex08_3",
      "input": "4 6.8 2 1 0",
      "expected": "2.45\n",
      "output": "inf"
    },
    {
      "test_id": "ex08_4",
      "input": "3 -1.8 3.14 1",
      "expected": "0.78\n",
      "output": "inf"
    }
  ],
  "clustering_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "1",
    "stdout:ex08_0:relation": "different",
    "stdout:ex08_0:edit_band": "large",
    "stdout:ex08_1:relation": "different",
    "stdout:ex08_1:edit_band": "large",
    "stdout:ex08_2:relation": "different",
    "stdout:ex08_2:edit_band": "large",
    "stdout:ex08_3:relation": "different",
    "stdout:ex08_3:edit_band": "large",
    "stdout:ex08_4:relation": "different",
    "stdout:ex08_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
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


## sample_012 — train

```c


#include <stdio.h>

int main(){
    int n;
    float valor,total,media;
    scanf("%d\n", &n);
    scanf("%f\n", &valor);
    total = valor;
    while(n>=0){
        scanf("%f\n", &valor);
        total = total + valor;
        n--;
    }
    media = total / n;
    printf("%.2f", media);
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
  "source_sha256": "70f21c36b6125e7258aef1dc7c6f5e1f7747aaf530dc3ead683ce2f4a1d17282",
  "outcomes": {
    "ex08_0": "fail",
    "ex08_1": "fail",
    "ex08_2": "fail",
    "ex08_3": "fail",
    "ex08_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex08_0",
      "input": "2 3 3",
      "expected": "3.00\n",
      "output": "-12.00"
    },
    {
      "test_id": "ex08_1",
      "input": "2 2 3",
      "expected": "2.50\n",
      "output": "-11.00"
    },
    {
      "test_id": "ex08_2",
      "input": "3 1.5 2.7 3",
      "expected": "2.40\n",
      "output": "-13.20"
    },
    {
      "test_id": "ex08_3",
      "input": "4 6.8 2 1 0",
      "expected": "2.45\n",
      "output": "-9.80"
    },
    {
      "test_id": "ex08_4",
      "input": "3 -1.8 3.14 1",
      "expected": "0.78\n",
      "output": "-4.34"
    }
  ],
  "clustering_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_update": "1",
    "stdout:ex08_0:relation": "different",
    "stdout:ex08_0:edit_band": "large",
    "stdout:ex08_1:relation": "different",
    "stdout:ex08_1:edit_band": "large",
    "stdout:ex08_2:relation": "different",
    "stdout:ex08_2:edit_band": "large",
    "stdout:ex08_3:relation": "different",
    "stdout:ex08_3:edit_band": "large",
    "stdout:ex08_4:relation": "different",
    "stdout:ex08_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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


## sample_013 — train

```c


#include <stdio.h>

int main(){
    int n;
    float valor,total,media;
    scanf("%d\n", &n);
    scanf("%f\n", &valor);
    total = valor;
    while(n>2){
        scanf("%f\n", &valor);
        total = total + valor;
        n=n-1;
    }
    media = total / n;
    printf("%.2f", media);
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
  "source_sha256": "caf5d2beb8e427470dda9aea61c2747bebdfd8325212c672d1deb642fbd901dc",
  "outcomes": {
    "ex08_0": "fail",
    "ex08_1": "fail",
    "ex08_2": "fail",
    "ex08_3": "fail",
    "ex08_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex08_0",
      "input": "2 3 3",
      "expected": "3.00\n",
      "output": "1.50"
    },
    {
      "test_id": "ex08_1",
      "input": "2 2 3",
      "expected": "2.50\n",
      "output": "1.00"
    },
    {
      "test_id": "ex08_2",
      "input": "3 1.5 2.7 3",
      "expected": "2.40\n",
      "output": "2.10"
    },
    {
      "test_id": "ex08_3",
      "input": "4 6.8 2 1 0",
      "expected": "2.45\n",
      "output": "4.90"
    },
    {
      "test_id": "ex08_4",
      "input": "3 -1.8 3.14 1",
      "expected": "0.78\n",
      "output": "0.67"
    }
  ],
  "clustering_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex08_0:relation": "different",
    "stdout:ex08_0:edit_band": "large",
    "stdout:ex08_1:relation": "different",
    "stdout:ex08_1:edit_band": "large",
    "stdout:ex08_2:relation": "different",
    "stdout:ex08_2:edit_band": "medium",
    "stdout:ex08_3:relation": "different",
    "stdout:ex08_3:edit_band": "large",
    "stdout:ex08_4:relation": "different",
    "stdout:ex08_4:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
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


## sample_014 — train

```c

#include <stdio.h>

int main()
{
    float media, numero, soma = 0, i = 0;
    int N;
    
    scanf("%d", &N);

    while( i <= N)
    {
        scanf("%f", &numero);

        soma = (soma + numero);
        i++;
    }


    media = soma / i;
    printf("%.2f", media);
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
  "source_sha256": "08ad6126af79b7e8c488fce4ed12418145b85b2497edde2c6baed00af0280be6",
  "outcomes": {
    "ex08_0": "fail",
    "ex08_1": "fail",
    "ex08_2": "fail",
    "ex08_3": "fail",
    "ex08_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex08_0",
      "input": "2 3 3",
      "expected": "3.00\n",
      "output": "3.00"
    },
    {
      "test_id": "ex08_1",
      "input": "2 2 3",
      "expected": "2.50\n",
      "output": "2.67"
    },
    {
      "test_id": "ex08_2",
      "input": "3 1.5 2.7 3",
      "expected": "2.40\n",
      "output": "2.55"
    },
    {
      "test_id": "ex08_3",
      "input": "4 6.8 2 1 0",
      "expected": "2.45\n",
      "output": "1.96"
    },
    {
      "test_id": "ex08_4",
      "input": "3 -1.8 3.14 1",
      "expected": "0.78\n",
      "output": "0.84"
    }
  ],
  "clustering_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_update": "1",
    "stdout:ex08_0:relation": "whitespace",
    "stdout:ex08_0:edit_band": "medium",
    "stdout:ex08_1:relation": "different",
    "stdout:ex08_1:edit_band": "large",
    "stdout:ex08_2:relation": "different",
    "stdout:ex08_2:edit_band": "large",
    "stdout:ex08_3:relation": "different",
    "stdout:ex08_3:edit_band": "large",
    "stdout:ex08_4:relation": "different",
    "stdout:ex08_4:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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


## sample_015 — validation

```c

#include <stdio.h>

int main() {
    int N, i = 1;
    float res, numero, acumulador = 0;

    printf("Digite a quantidade de números (N): ");
    scanf("%d", &N);

    while(i <= N){
        printf("Introduza o numero %d:\n:", i);
        scanf("%f", &numero);
        acumulador = acumulador + numero;
        i ++;
    }
    res = acumulador/N;
    printf("%f\n", res);
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
  "source_sha256": "e4b961777c6a1205686532d29a8f2ed0f51e46c898a17c89532e9d5812233ba4",
  "outcomes": {
    "ex08_0": "fail",
    "ex08_1": "fail",
    "ex08_2": "fail",
    "ex08_3": "fail",
    "ex08_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex08_0",
      "input": "2 3 3",
      "expected": "3.00\n",
      "output": "Digite a quantidade de números (N): Introduza o numero 1:\n:Introduza o numero 2:\n:3.000000\n"
    },
    {
      "test_id": "ex08_1",
      "input": "2 2 3",
      "expected": "2.50\n",
      "output": "Digite a quantidade de números (N): Introduza o numero 1:\n:Introduza o numero 2:\n:2.500000\n"
    },
    {
      "test_id": "ex08_2",
      "input": "3 1.5 2.7 3",
      "expected": "2.40\n",
      "output": "Digite a quantidade de números (N): Introduza o numero 1:\n:Introduza o numero 2:\n:Introduza o numero 3:\n:2.400000\n"
    },
    {
      "test_id": "ex08_3",
      "input": "4 6.8 2 1 0",
      "expected": "2.45\n",
      "output": "Digite a quantidade de números (N): Introduza o numero 1:\n:Introduza o numero 2:\n:Introduza o numero 3:\n:Introduza o numero 4:\n:2.450000\n"
    },
    {
      "test_id": "ex08_4",
      "input": "3 -1.8 3.14 1",
      "expected": "0.78\n",
      "output": "Digite a quantidade de números (N): Introduza o numero 1:\n:Introduza o numero 2:\n:Introduza o numero 3:\n:0.780000\n"
    }
  ],
  "clustering_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_update": "1",
    "stdout:ex08_0:relation": "different",
    "stdout:ex08_0:edit_band": "large",
    "stdout:ex08_1:relation": "different",
    "stdout:ex08_1:edit_band": "large",
    "stdout:ex08_2:relation": "different",
    "stdout:ex08_2:edit_band": "large",
    "stdout:ex08_3:relation": "different",
    "stdout:ex08_3:edit_band": "large",
    "stdout:ex08_4:relation": "different",
    "stdout:ex08_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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


## sample_016 — validation

```c

#include <stdio.h>

int main() {
    float media,num;
    int x;
    media = 0;
    x=0;
    while (scanf("%f", &num) == 1) {
        media= media + num;
        x++;
    }

    media=media/x;
    printf("%f\n", media);
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
  "source_sha256": "8c2151352a0ff5e0b5bc6d1a58c015715cb2802c9e44cd9eb9d2440336e1091f",
  "outcomes": {
    "ex08_0": "fail",
    "ex08_1": "fail",
    "ex08_2": "fail",
    "ex08_3": "fail",
    "ex08_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex08_0",
      "input": "2 3 3",
      "expected": "3.00\n",
      "output": "2.666667\n"
    },
    {
      "test_id": "ex08_1",
      "input": "2 2 3",
      "expected": "2.50\n",
      "output": "2.333333\n"
    },
    {
      "test_id": "ex08_2",
      "input": "3 1.5 2.7 3",
      "expected": "2.40\n",
      "output": "2.550000\n"
    },
    {
      "test_id": "ex08_3",
      "input": "4 6.8 2 1 0",
      "expected": "2.45\n",
      "output": "2.760000\n"
    },
    {
      "test_id": "ex08_4",
      "input": "3 -1.8 3.14 1",
      "expected": "0.78\n",
      "output": "1.335000\n"
    }
  ],
  "clustering_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_update": "1",
    "stdout:ex08_0:relation": "different",
    "stdout:ex08_0:edit_band": "large",
    "stdout:ex08_1:relation": "different",
    "stdout:ex08_1:edit_band": "large",
    "stdout:ex08_2:relation": "different",
    "stdout:ex08_2:edit_band": "large",
    "stdout:ex08_3:relation": "different",
    "stdout:ex08_3:edit_band": "large",
    "stdout:ex08_4:relation": "different",
    "stdout:ex08_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
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


## sample_017 — validation

```c

#include <stdio.h>

int main() {
    float media,num;
    int x;
    media = 0;
    x=0;
    while (scanf("%f", &num) == 1) {
        media= media + num;
        x++;
    }

    media=media/x;
    printf("%.2f\n", media);
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
  "source_sha256": "53927bf34e4eef1f6d3e25abb7dea09ffc6bf057f97ed3c1ad78f2442df9c423",
  "outcomes": {
    "ex08_0": "fail",
    "ex08_1": "fail",
    "ex08_2": "fail",
    "ex08_3": "fail",
    "ex08_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex08_0",
      "input": "2 3 3",
      "expected": "3.00\n",
      "output": "2.67\n"
    },
    {
      "test_id": "ex08_1",
      "input": "2 2 3",
      "expected": "2.50\n",
      "output": "2.33\n"
    },
    {
      "test_id": "ex08_2",
      "input": "3 1.5 2.7 3",
      "expected": "2.40\n",
      "output": "2.55\n"
    },
    {
      "test_id": "ex08_3",
      "input": "4 6.8 2 1 0",
      "expected": "2.45\n",
      "output": "2.76\n"
    },
    {
      "test_id": "ex08_4",
      "input": "3 -1.8 3.14 1",
      "expected": "0.78\n",
      "output": "1.34\n"
    }
  ],
  "clustering_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_update": "1",
    "stdout:ex08_0:relation": "different",
    "stdout:ex08_0:edit_band": "large",
    "stdout:ex08_1:relation": "different",
    "stdout:ex08_1:edit_band": "medium",
    "stdout:ex08_2:relation": "different",
    "stdout:ex08_2:edit_band": "medium",
    "stdout:ex08_3:relation": "different",
    "stdout:ex08_3:edit_band": "medium",
    "stdout:ex08_4:relation": "different",
    "stdout:ex08_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
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


## sample_019 — train

```c

#include <stdio.h>

typedef struct {
    int dia;
    int mes;
    int ano;
}DATE;
typedef struct{
    int hora;
    int minuto;
}TIME;

void elapsedTime(DATE data, TIME hora) {
    int minutosReturn;
    minutosReturn= hora.minuto + 60*hora.hora + (data.ano-2022)*525600 + (data.mes-01)*43829 + (data.dia-01)*1440;
    printf("%d\n",minutosReturn);
}

int main() {
    DATE data;
    TIME hora;
    scanf("%d-%d-%d %d:%d",&data.dia ,&data.mes, &data.ano, &hora.hora, &hora.minuto);
    elapsedTime(data,hora);
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
  "source_sha256": "649d0d20167ad57134d55e16677c1e1f7603bf7eea182fb1c092fc795c7927bc",
  "outcomes": {
    "ex08_0": "fail",
    "ex08_1": "fail",
    "ex08_2": "fail",
    "ex08_3": "fail",
    "ex08_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex08_0",
      "input": "2 3 3",
      "expected": "3.00\n",
      "output": "-1062805589\n"
    },
    {
      "test_id": "ex08_1",
      "input": "2 2 3",
      "expected": "2.50\n",
      "output": "-1062805589\n"
    },
    {
      "test_id": "ex08_2",
      "input": "3 1.5 2.7 3",
      "expected": "2.40\n",
      "output": "-1062804149\n"
    },
    {
      "test_id": "ex08_3",
      "input": "4 6.8 2 1 0",
      "expected": "2.45\n",
      "output": "-1062802709\n"
    },
    {
      "test_id": "ex08_4",
      "input": "3 -1.8 3.14 1",
      "expected": "0.78\n",
      "output": "-1062804149\n"
    }
  ],
  "clustering_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_update": "0",
    "stdout:ex08_0:relation": "different",
    "stdout:ex08_0:edit_band": "large",
    "stdout:ex08_1:relation": "different",
    "stdout:ex08_1:edit_band": "large",
    "stdout:ex08_2:relation": "different",
    "stdout:ex08_2:edit_band": "large",
    "stdout:ex08_3:relation": "different",
    "stdout:ex08_3:edit_band": "large",
    "stdout:ex08_4:relation": "different",
    "stdout:ex08_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
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


## sample_020 — train

```c


#include <stdio.h>

int main() {
    int numero, N, i = 0, soma = 0;
    double media;

    printf("introduz um numero inteiro que representa a quantidade do numeros inseridos: ");
    scanf("%d",&N);

    while (i < N){
        scanf("%d",&numero);
        soma = numero + soma;
        i++;
    }
    media = soma / N;
    printf("%.2f\n", media);

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
  "source_sha256": "4dfb7c3dd62c7f2c0aa28cb76067a8912bbea01b401dbce97db27d83fc6d747b",
  "outcomes": {
    "ex08_0": "fail",
    "ex08_1": "fail",
    "ex08_2": "fail",
    "ex08_3": "fail",
    "ex08_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex08_0",
      "input": "2 3 3",
      "expected": "3.00\n",
      "output": "introduz um numero inteiro que representa a quantidade do numeros inseridos: 3.00\n"
    },
    {
      "test_id": "ex08_1",
      "input": "2 2 3",
      "expected": "2.50\n",
      "output": "introduz um numero inteiro que representa a quantidade do numeros inseridos: 2.00\n"
    },
    {
      "test_id": "ex08_2",
      "input": "3 1.5 2.7 3",
      "expected": "2.40\n",
      "output": "introduz um numero inteiro que representa a quantidade do numeros inseridos: 1.00\n"
    },
    {
      "test_id": "ex08_3",
      "input": "4 6.8 2 1 0",
      "expected": "2.45\n",
      "output": "introduz um numero inteiro que representa a quantidade do numeros inseridos: 6.00\n"
    },
    {
      "test_id": "ex08_4",
      "input": "3 -1.8 3.14 1",
      "expected": "0.78\n",
      "output": "introduz um numero inteiro que representa a quantidade do numeros inseridos: -1.00\n"
    }
  ],
  "clustering_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "1",
    "stdout:ex08_0:relation": "different",
    "stdout:ex08_0:edit_band": "large",
    "stdout:ex08_1:relation": "different",
    "stdout:ex08_1:edit_band": "large",
    "stdout:ex08_2:relation": "different",
    "stdout:ex08_2:edit_band": "large",
    "stdout:ex08_3:relation": "different",
    "stdout:ex08_3:edit_band": "large",
    "stdout:ex08_4:relation": "different",
    "stdout:ex08_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
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

int main() {
    int N, i = 0;
    float numero,media, soma = 0;

    printf("introduz um numero inteiro que representa a quantidade do numeros inseridos: ");
    scanf("%d",&N);

    while (i < N){
        scanf("%f",&numero);
        soma = numero + soma;
        i++;
    }
    media = soma / N;
    printf("%.2f\n", media);

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
  "source_sha256": "31ce1d955926ed8521cba9de6d2291302ea168bb9dd485cb1ac87849a583e72c",
  "outcomes": {
    "ex08_0": "fail",
    "ex08_1": "fail",
    "ex08_2": "fail",
    "ex08_3": "fail",
    "ex08_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex08_0",
      "input": "2 3 3",
      "expected": "3.00\n",
      "output": "introduz um numero inteiro que representa a quantidade do numeros inseridos: 3.00\n"
    },
    {
      "test_id": "ex08_1",
      "input": "2 2 3",
      "expected": "2.50\n",
      "output": "introduz um numero inteiro que representa a quantidade do numeros inseridos: 2.50\n"
    },
    {
      "test_id": "ex08_2",
      "input": "3 1.5 2.7 3",
      "expected": "2.40\n",
      "output": "introduz um numero inteiro que representa a quantidade do numeros inseridos: 2.40\n"
    },
    {
      "test_id": "ex08_3",
      "input": "4 6.8 2 1 0",
      "expected": "2.45\n",
      "output": "introduz um numero inteiro que representa a quantidade do numeros inseridos: 2.45\n"
    },
    {
      "test_id": "ex08_4",
      "input": "3 -1.8 3.14 1",
      "expected": "0.78\n",
      "output": "introduz um numero inteiro que representa a quantidade do numeros inseridos: 0.78\n"
    }
  ],
  "clustering_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "1",
    "stdout:ex08_0:relation": "different",
    "stdout:ex08_0:edit_band": "large",
    "stdout:ex08_1:relation": "different",
    "stdout:ex08_1:edit_band": "large",
    "stdout:ex08_2:relation": "different",
    "stdout:ex08_2:edit_band": "large",
    "stdout:ex08_3:relation": "different",
    "stdout:ex08_3:edit_band": "large",
    "stdout:ex08_4:relation": "different",
    "stdout:ex08_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex08_0": "fail",
    "test:ex08_1": "fail",
    "test:ex08_2": "fail",
    "test:ex08_3": "fail",
    "test:ex08_4": "fail",
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
  "members/sample_001/tests/ex08_0",
  "members/sample_001/tests/ex08_1",
  "members/sample_001/tests/ex08_2",
  "members/sample_001/tests/ex08_3",
  "members/sample_001/tests/ex08_4",
  "members/sample_002/raw_code",
  "members/sample_002/tests/ex08_0",
  "members/sample_002/tests/ex08_1",
  "members/sample_002/tests/ex08_2",
  "members/sample_002/tests/ex08_3",
  "members/sample_002/tests/ex08_4",
  "members/sample_003/raw_code",
  "members/sample_003/tests/ex08_0",
  "members/sample_003/tests/ex08_1",
  "members/sample_003/tests/ex08_2",
  "members/sample_003/tests/ex08_3",
  "members/sample_003/tests/ex08_4",
  "members/sample_004/raw_code",
  "members/sample_004/tests/ex08_0",
  "members/sample_004/tests/ex08_1",
  "members/sample_004/tests/ex08_2",
  "members/sample_004/tests/ex08_3",
  "members/sample_004/tests/ex08_4",
  "members/sample_005/raw_code",
  "members/sample_005/tests/ex08_0",
  "members/sample_005/tests/ex08_1",
  "members/sample_005/tests/ex08_2",
  "members/sample_005/tests/ex08_3",
  "members/sample_005/tests/ex08_4",
  "members/sample_006/raw_code",
  "members/sample_006/tests/ex08_0",
  "members/sample_006/tests/ex08_1",
  "members/sample_006/tests/ex08_2",
  "members/sample_006/tests/ex08_3",
  "members/sample_006/tests/ex08_4",
  "members/sample_007/raw_code",
  "members/sample_007/tests/ex08_0",
  "members/sample_007/tests/ex08_1",
  "members/sample_007/tests/ex08_2",
  "members/sample_007/tests/ex08_3",
  "members/sample_007/tests/ex08_4",
  "members/sample_008/raw_code",
  "members/sample_008/tests/ex08_0",
  "members/sample_008/tests/ex08_1",
  "members/sample_008/tests/ex08_2",
  "members/sample_008/tests/ex08_3",
  "members/sample_008/tests/ex08_4",
  "members/sample_009/raw_code",
  "members/sample_009/tests/ex08_0",
  "members/sample_009/tests/ex08_1",
  "members/sample_009/tests/ex08_2",
  "members/sample_009/tests/ex08_3",
  "members/sample_009/tests/ex08_4",
  "members/sample_010/raw_code",
  "members/sample_010/tests/ex08_0",
  "members/sample_010/tests/ex08_1",
  "members/sample_010/tests/ex08_2",
  "members/sample_010/tests/ex08_3",
  "members/sample_010/tests/ex08_4",
  "members/sample_011/raw_code",
  "members/sample_011/tests/ex08_0",
  "members/sample_011/tests/ex08_1",
  "members/sample_011/tests/ex08_2",
  "members/sample_011/tests/ex08_3",
  "members/sample_011/tests/ex08_4",
  "members/sample_012/raw_code",
  "members/sample_012/tests/ex08_0",
  "members/sample_012/tests/ex08_1",
  "members/sample_012/tests/ex08_2",
  "members/sample_012/tests/ex08_3",
  "members/sample_012/tests/ex08_4",
  "members/sample_013/raw_code",
  "members/sample_013/tests/ex08_0",
  "members/sample_013/tests/ex08_1",
  "members/sample_013/tests/ex08_2",
  "members/sample_013/tests/ex08_3",
  "members/sample_013/tests/ex08_4",
  "members/sample_014/raw_code",
  "members/sample_014/tests/ex08_0",
  "members/sample_014/tests/ex08_1",
  "members/sample_014/tests/ex08_2",
  "members/sample_014/tests/ex08_3",
  "members/sample_014/tests/ex08_4",
  "members/sample_015/raw_code",
  "members/sample_015/tests/ex08_0",
  "members/sample_015/tests/ex08_1",
  "members/sample_015/tests/ex08_2",
  "members/sample_015/tests/ex08_3",
  "members/sample_015/tests/ex08_4",
  "members/sample_016/raw_code",
  "members/sample_016/tests/ex08_0",
  "members/sample_016/tests/ex08_1",
  "members/sample_016/tests/ex08_2",
  "members/sample_016/tests/ex08_3",
  "members/sample_016/tests/ex08_4",
  "members/sample_017/raw_code",
  "members/sample_017/tests/ex08_0",
  "members/sample_017/tests/ex08_1",
  "members/sample_017/tests/ex08_2",
  "members/sample_017/tests/ex08_3",
  "members/sample_017/tests/ex08_4",
  "members/sample_018/raw_code",
  "members/sample_018/tests/ex08_0",
  "members/sample_018/tests/ex08_1",
  "members/sample_018/tests/ex08_2",
  "members/sample_018/tests/ex08_3",
  "members/sample_018/tests/ex08_4",
  "members/sample_019/raw_code",
  "members/sample_019/tests/ex08_0",
  "members/sample_019/tests/ex08_1",
  "members/sample_019/tests/ex08_2",
  "members/sample_019/tests/ex08_3",
  "members/sample_019/tests/ex08_4",
  "members/sample_020/raw_code",
  "members/sample_020/tests/ex08_0",
  "members/sample_020/tests/ex08_1",
  "members/sample_020/tests/ex08_2",
  "members/sample_020/tests/ex08_3",
  "members/sample_020/tests/ex08_4",
  "members/sample_021/raw_code",
  "members/sample_021/tests/ex08_0",
  "members/sample_021/tests/ex08_1",
  "members/sample_021/tests/ex08_2",
  "members/sample_021/tests/ex08_3",
  "members/sample_021/tests/ex08_4"
]
```
