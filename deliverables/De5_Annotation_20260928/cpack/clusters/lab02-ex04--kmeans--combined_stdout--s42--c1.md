# lab02-ex04--kmeans--combined_stdout--s42--c1

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 28; phân vùng: {'train': 26, 'validation': 2}.


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
    "test_id": "ex04_0",
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
    "test_id": "ex04_1",
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
    "test_id": "ex04_2",
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
    "test_id": "ex04_3",
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
    "feature": "stdout:ex04_1:edit_band",
    "value": "small",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.2978723404255319,
    "difference_from_cohort": 0.7021276595744681
  },
  {
    "feature": "stdout:ex04_3:edit_band",
    "value": "small",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.2978723404255319,
    "difference_from_cohort": 0.7021276595744681
  },
  {
    "feature": "stdout:ex04_2:edit_band",
    "value": "small",
    "n": 27,
    "n_cluster": 28,
    "rate": 0.9642857142857143,
    "cohort_rate": 0.2872340425531915,
    "difference_from_cohort": 0.6770516717325228
  },
  {
    "feature": "stdout:ex04_0:edit_band",
    "value": "small",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.32978723404255317,
    "difference_from_cohort": 0.6702127659574468
  },
  {
    "feature": "stdout:ex04_1:relation",
    "value": "whitespace",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.43617021276595747,
    "difference_from_cohort": 0.5638297872340425
  },
  {
    "feature": "stdout:ex04_3:relation",
    "value": "whitespace",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.43617021276595747,
    "difference_from_cohort": 0.5638297872340425
  },
  {
    "feature": "stdout:ex04_2:relation",
    "value": "whitespace",
    "n": 27,
    "n_cluster": 28,
    "rate": 0.9642857142857143,
    "cohort_rate": 0.425531914893617,
    "difference_from_cohort": 0.5387537993920972
  },
  {
    "feature": "stdout:ex04_0:relation",
    "value": "whitespace",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.5,
    "difference_from_cohort": 0.5
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 8,
    "n_cluster": 28,
    "rate": 0.2857142857142857,
    "cohort_rate": 0.14893617021276595,
    "difference_from_cohort": 0.13677811550151975
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 7,
    "n_cluster": 28,
    "rate": 0.25,
    "cohort_rate": 0.11702127659574468,
    "difference_from_cohort": 0.13297872340425532
  },
  {
    "feature": "ast:c_subscript",
    "value": "1",
    "n": 7,
    "n_cluster": 28,
    "rate": 0.25,
    "cohort_rate": 0.14893617021276595,
    "difference_from_cohort": 0.10106382978723405
  },
  {
    "feature": "test:ex04_0",
    "value": "fail",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.9148936170212766,
    "difference_from_cohort": 0.08510638297872342
  },
  {
    "feature": "ast:c_while",
    "value": "1",
    "n": 3,
    "n_cluster": 28,
    "rate": 0.10714285714285714,
    "cohort_rate": 0.06382978723404255,
    "difference_from_cohort": 0.04331306990881459
  },
  {
    "feature": "test:ex04_1",
    "value": "fail",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.9574468085106383,
    "difference_from_cohort": 0.04255319148936165
  },
  {
    "feature": "test:ex04_2",
    "value": "fail",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.9574468085106383,
    "difference_from_cohort": 0.04255319148936165
  },
  {
    "feature": "test:ex04_3",
    "value": "fail",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.9574468085106383,
    "difference_from_cohort": 0.04255319148936165
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "0",
    "n": 24,
    "n_cluster": 28,
    "rate": 0.8571428571428571,
    "cohort_rate": 0.8191489361702128,
    "difference_from_cohort": 0.03799392097264431
  },
  {
    "feature": "ast:c_array_parameter",
    "value": "0",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.9680851063829787,
    "difference_from_cohort": 0.03191489361702127
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 25,
    "n_cluster": 28,
    "rate": 0.8928571428571429,
    "cohort_rate": 0.8723404255319149,
    "difference_from_cohort": 0.020516717325227973
  },
  {
    "feature": "ast:c_one_index",
    "value": "1",
    "n": 3,
    "n_cluster": 28,
    "rate": 0.10714285714285714,
    "cohort_rate": 0.09574468085106383,
    "difference_from_cohort": 0.011398176291793308
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 25,
    "n_cluster": 28,
    "rate": 0.8928571428571429,
    "cohort_rate": 0.8723404255319149,
    "difference_from_cohort": 0.020516717325227973
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 28,
    "n_cluster": 28,
    "rate": 1.0,
    "cohort_rate": 0.9893617021276596,
    "difference_from_cohort": 0.010638297872340385
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 27,
    "n_cluster": 28,
    "rate": 0.9642857142857143,
    "cohort_rate": 0.9574468085106383,
    "difference_from_cohort": 0.006838905775075954
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
      "NOT (stdout:ex04_3:relation=different)",
      "stdout:ex04_3:edit_band=small"
    ],
    "then_cluster": 1,
    "train_support": 26,
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

sample_001, sample_006, sample_005, sample_007

## sample_001 — train — đại diện

```c
# include <stdio.h>

int main ()
{
    int a, b, c;
    scanf ("%d%d%d", &a, &b, &c);

    if (a > b && a > c)
        if (b > c)
            printf ("%d %d %d", c,b,a);
        else 
            printf ("%d %d %d", b,c,a);
        
    else if (b > a && b > c )
        if (a > c) 
            printf ("%d %d %d", c,a,b);
        else
            printf ("%d %d %d", a, c, b);
    else
        if (a > b)
            printf ("%d %d %d", b, a ,c);
        else 
            printf ("%d %d %d", a, b, c);   

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
  "source_sha256": "79eb168937f82b065150896a04db2d54a04ca97e4f77dc59db902709f12a129d",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
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


## sample_005 — train — đại diện

```c

#include <stdio.h>

int main()
{
    int x, y, z;
    int temp_x, temp_y, temp_z;
    scanf("%d %d %d", &x, &y, &z);
    temp_x = x;
    temp_y = y;
    temp_z = z;
    while (temp_x >= 0 || temp_y >= 0 || temp_z >= 0)
    {
        if (temp_x == 0)
            printf("%d ", x);
        if (temp_y == 0)
            printf("%d ", y);
        if (temp_z == 0)
            printf("%d ", z);
        temp_x--;
        temp_y--;
        temp_z--;
    }
    printf("\n");
    return 0;
}
```

```json
{
  "sample_id": "sample_005",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "c059082341b3343dbd4065e9bd1ce5f811d157c695c9d52b32aa0467305924aa",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6 \n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10 \n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "10 \n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100 \n"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "1",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
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


## sample_006 — train — đại diện

```c



#include <stdio.h>

int main()
{
    int n [3];
    int i = 0;
    int aux;
    int ordenado = 0;

    scanf("%d %d %d", &n[0], &n[1], &n[2]);
    
    while(!ordenado){
        ordenado = 1;
        for(i=0; i < 2; i++){
            if(n[i] > n[i+1]){
                aux = n[i+1];
                n[i+1]= n[i];
                n[i] = aux;
                ordenado = 0;
            }
        }
    }

    for(i=0; i <= 2; i ++){
        printf("%d ", n[i]);
    }
    printf("\n");
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
  "source_sha256": "dcf33fc90b2f11a8500a93a221c4b6f71d11175b46891e60acdf3047220ecbf0",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6 \n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10 \n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10 \n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100 \n"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "1",
    "ast:c_one_index": "1",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "1",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "1",
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


## sample_007 — train — đại diện

```c

#include <stdio.h>



#define INICIO 0
#define LENGTH 3

int main()
{
    int i, n, vetor[LENGTH], stand;
    for (i = INICIO; i < LENGTH; i++)
        scanf("%d", &vetor[i]);
    for (i = INICIO; i < LENGTH; i++)
    {
        for (n = INICIO; n < LENGTH; n++)
        {
            if (vetor[i] < vetor[n])
            {
                stand = vetor[n];
                vetor[n] = vetor[i];
                vetor[i] = stand;
            } 
        }
    } 
    for (i = INICIO; i < LENGTH; i++)
    {
        if (i == LENGTH)
            printf("%d", vetor[i]);
        else
            printf("%d ", vetor[i]);
    }
    printf("\n");
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
  "source_sha256": "5fb89e64d9cdae22f9310bda5c8a839a98651d5fd0561fce6ca1ad0ac31a2e0c",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6 \n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10 \n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10 \n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100 \n"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "1",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
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
	int n1, n2, n3, tmp;

	scanf("%d", &n1);
	scanf("%d", &n2);
	scanf("%d", &n3);

	if(n2 > n3)
	{
		tmp = n3;
		n3 = n2;
		n2 = tmp;
	}
	if(n1 > n2)
	{
		tmp = n2;
		n2 = n1;
		n1 = tmp;
	}
	if(n2 > n3)
	{
		tmp = n3;
		n3 = n2;
		n2 = tmp;
	}

	printf("%d %d %d", n1, n2, n3);

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
  "source_sha256": "0dc998112ca25232b2aa146fa1de59cddfc5ccc123536d5aeda15f47cd612091",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
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


## sample_003 — train

```c
#include <stdio.h>

int main() {
    int a, b, c;
    int x;
    scanf("%d%d%d", &a, &b, &c);
    if (a>b){
        x=a;
        a=b;
        b=x;
    }
    if (a>c){
        x=a;
        a=c;
        c=x;
    }
    if (b>c){
        x=b;
        b=c;
        c=x;
    }
    printf("%d %d %d",a,b,c);
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
  "source_sha256": "c0eb36de61d6c8d9233c0cd5c1fed94abba89012dd28214824214d83a4b0bbaa",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
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

int main(){
    int num1, num2, num3;
    scanf("%d\n%d\n%d", &num1, &num2, &num3);
    if (num1 <= num2 && num1<=num3){
        if (num2<=num3){
            printf("%d %d %d", num1, num2, num3);
            return 0;
        }
        else{
            printf("%d %d %d", num1, num3, num2);   
            return 0;
        }
    }

    else if (num2 <= num3 && num2 <= num1){
        if (num1<=num3){
            printf("%d %d %d", num2, num1, num3);
            return 0;
        }
        else{
            printf("%d %d %d", num2, num3, num1);
            return 0;
        }
    }
    else{
        if(num2<=num1){
            printf("%d %d %d", num3, num2, num1);
            return 0;
        }
        else{
            printf("%d %d %d", num3, num1, num2);
            return 0;
        }
    }
}
```

```json
{
  "sample_id": "sample_004",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "807efed08edad35d91534e176fee86e150559271a4ecbc46db361e81281f8006",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
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



#define INICIO 0
#define LENGTH 3

int main()
{
    int i, n, vetor[LENGTH], stand;
    for (i = INICIO; i < LENGTH; i++)
        scanf("%d", &vetor[i]);
    for (i = INICIO; i < LENGTH; i++)
    {
        for (n = INICIO; n < LENGTH; n++)
        {
            if (vetor[i] < vetor[n])
            {
                stand = vetor[n];
                vetor[n] = vetor[i];
                vetor[i] = stand;
            } 
        }
    } 
    for (i = INICIO; i < LENGTH; i++)
        printf("%d ", vetor[i]);
    printf("\n");
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
  "source_sha256": "dafe5624d14ac1d726c45ba3c32f1480cbe07b8bc37a77ee592317fbac9f2876",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6 \n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10 \n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10 \n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100 \n"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "1",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
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



#define INICIO 0
#define LENGTH 3

int main()
{
    int i, n, vetor[LENGTH], stand;
    for (i = INICIO; i < LENGTH; i++)
        scanf("%d", &vetor[i]);
    for (i = INICIO; i < LENGTH; i++)
    {
        for (n = INICIO; n < LENGTH; n++)
        {
            if (vetor[i] < vetor[n])
            {
                stand = vetor[n];
                vetor[n] = vetor[i];
                vetor[i] = stand;
            } 
        }
    } 
    for (i = INICIO; i < LENGTH; i++)
        printf("%d ", vetor[i]);
    printf("\n");
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
  "source_sha256": "dafe5624d14ac1d726c45ba3c32f1480cbe07b8bc37a77ee592317fbac9f2876",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6 \n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10 \n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10 \n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100 \n"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "1",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
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
#define LENGTH 3

int main()
{
    int i, n, vetor[LENGTH], stand;
    for (i = INICIO; i < LENGTH; i++)
        scanf("%d", &vetor[i]);
    for (i = INICIO; i < LENGTH; i++)
    {
        for (n = INICIO; n < LENGTH; n++)
        {
            if (vetor[i] < vetor[n])
            {
                stand = vetor[n];
                vetor[n] = vetor[i];
                vetor[i] = stand;
            } 
        }
    } 
    for (i = INICIO; i < LENGTH; i++)
        printf("%d ", vetor[i]);
    printf("\n");
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
  "source_sha256": "dafe5624d14ac1d726c45ba3c32f1480cbe07b8bc37a77ee592317fbac9f2876",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6 \n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10 \n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10 \n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100 \n"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "1",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
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
int main()
{
    int N, M, W;
    scanf("%d %d %d", &N, &M, &W);
    if(N>M && N>W)
    {
        if (M>W)
        {
            printf("%d %d %d", W, M, N);
        }
        else
        {
            printf("%d %d %d", M, W, N);
        }
    }
    if(M>N && M>W)
    {
        if (N>W)
        {
            printf("%d %d %d", W, N, M);
        }
        else 
        {
            printf("%d %d %d", N, W, M);
        }
    }
    if(W>N && W>M)
    {
        if (N>M)
        {
            printf("%d %d %d", M, N, W);
        }
        else
        {
            printf("%d %d %d", N, M, W);
        }
    }
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
  "source_sha256": "ccc8d3062f8e97b50e4081760caa96da53074bfe8a1560cd691aa7290dccee36",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
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
int main () {
    int A, B, C, menor, medio, maior;
    scanf("%d %d %d", &A, &B, &C);
    if (A > B && A > C) {
        maior = A;
        if (B > C){
            medio = B;
            menor = C;}
        else {
            medio = C;
            menor = B;}
    }
    if (B > A && B > C){
        maior = B;
        if (C > A){
            medio = C;
            menor = A;}
        else{
            medio = A;
            menor = C;}
    }
    if (C > A && C > B){
        maior = C;
        if (B > A){
            medio = B;
            menor = A;}
        else{
            medio = A;
            menor = B;}
    }
    printf("%d %d %d", menor, medio, maior);
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
  "source_sha256": "dd7242c1c292825c8d8dde28b51c6ec7a2aaaf741f0175b82343db0d4a63b86a",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
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
int main () {
    int A, B, C, menor, medio, maior;
    scanf("%d%d%d", &A, &B, &C);
    if (A > B && A > C) {
        maior = A;
        if (B > C){
            medio = B;
            menor = C;
        }
        else {
            medio = C;
            menor = B;
        }
    }
    if (B > A && B > C){
        maior = B;
        if (C > A){
            medio = C;
            menor = A;
        }
        else{
            medio = A;
            menor = C;
        }
    }
    if (C > A && C > B){
        maior = C;
        if (B > A){
            medio = B;
            menor = A;
        }
        else{
            medio = A;
            menor = B;
        }
    }
    printf("%d %d %d", menor, medio, maior);
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
  "source_sha256": "37fc5034ebd42fa692aa0d6bc7ba9ddf17f82e28df4fdbf465cd1029ce4ba863",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
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


## sample_014 — train

```c

#include <stdio.h>
int main () {
    int A, B, C, menor, medio, maior;
    scanf("%d %d %d", &A, &B, &C);
    if (A > B && A > C) {
        maior = A;
        if (B > C){
            medio = B;
            menor = C;
        }
        else {
            medio = C;
            menor = B;
        }
    }
    if (B > A && B > C){
        maior = B;
        if (C > A){
            medio = C;
            menor = A;
        }
        else{
            medio = A;
            menor = C;
        }
    }
    if (C > A && C > B){
        maior = C;
        if (B > A){
            medio = B;
            menor = A;
        }
        else{
            medio = A;
            menor = B;
        }
    }
    printf("%d %d %d", menor, medio, maior);
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
  "source_sha256": "890e3336a531ff647d0fb6c03ec1ae6b138c5c3cdaedb49aa49c334979ad9fe7",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
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

void le_imprime_3_ordenado() {

    int num1, num2, num3;

    scanf("%d%d%d", &num1, &num2, &num3);

    if (num1 > num2) {
        if (num2 > num3) {
            printf("%d %d %d", num3, num2, num1);
        }
        else if (num3 > num1) {
            printf("%d %d %d", num2, num1, num3);
        }
        else {
            printf("%d %d %d", num2, num3, num1);
        }
    }
    else { 
        if (num1 > num3) {
            printf("%d %d %d", num3, num1, num2);
        }
        else if (num3 > num2) {
            printf("%d %d %d", num1, num2, num3);
        }
        else {
            printf("%d %d %d", num1, num3, num2);
        }
    }


}

int main() {

    le_imprime_3_ordenado();

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
  "source_sha256": "1d02ad592373a63c1d7f6327e705aa32c61b6b0eade2e805b444ea597069f4b5",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
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


## sample_016 — train

```c

#include <stdio.h>

int main()
{
    int num1, num2, num3, aux;
    scanf("%d%d%d", &num1, &num2, &num3);
    if (num1 > num2) {
        aux = num1;
        num1 = num2;
        num2 = aux;
    }
    if (num3 < num1)
        printf("%d %d %d", num3, num1, num2);
    else if (num3 < num2)
        printf("%d %d %d", num1, num3, num2);
    else
        printf("%d %d %d", num1, num2, num3);
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
  "source_sha256": "9c90b08b8db81a03a7251dbd9df72911e07960ff0eeee8e9b34792f30a1bf316",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
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


## sample_017 — validation

```c

#include <stdio.h>

int main() {
    int num1,num2,num3;
    scanf("%d %d %d",&num1,&num2,&num3);
    if (num1>=num2&&num1>=num3)
    {
        if (num2>=num3)
        {
            printf("%d %d %d",num3,num2,num1);
        }
        else{
            printf("%d %d %d",num2,num3,num1);
        }
    }
    else if (num2>=num1&&num2>=num3)
    {
        if (num1>=num3)
        {
            printf("%d %d %d",num3,num1,num2);
        }
        else {
            printf("%d %d %d",num1,num3,num2);
        }
    }
    else{
        if (num2>=num1)
        {
            printf("%d %d %d",num1,num2,num3);
        }
        else{
            printf("%d %d %d",num2,num1,num3);
        }        
    }
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
  "source_sha256": "30337f5bae209e99665a7598d655d2bffb048db5e43a3341ffc5e0f9e82078fd",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
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


## sample_018 — train

```c


#include <stdio.h>

int main(){
	int inputs[3], temp, i, j;
	scanf("%d %d %d", &inputs[0], &inputs[1], &inputs[2]);
	for(i = 0; i<3; i++) {
		for (j=i+1; j<3; j++) {
			if (inputs[i] > inputs[j]) {
				temp = inputs[i];
				inputs[i] = inputs[j];
				inputs[j] = temp;
			}
		}
	}
	for(i=0; i<3; i++) {
		printf("%d ",inputs[i]);
	}
	printf("\n");
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
  "source_sha256": "32ae014c5469f6dc3c5739bfd179a8f09f6a8ed3583276c40e93f5d6992c0981",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6 \n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10 \n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10 \n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100 \n"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "1",
    "ast:c_one_index": "1",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "1",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
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


## sample_019 — train

```c


#include <stdio.h>

int main(){
	int inputs[3], temp, i, j;
	scanf("%d %d %d", &inputs[0], &inputs[1], &inputs[2]);
	for(i = 0; i<3; i++) {
		for (j=i+1; j<3; j++) {
			if (inputs[i] > inputs[j]) {
				temp = inputs[i];
				inputs[i] = inputs[j];
				inputs[j] = temp;
			}
		}
	}
	for(i=0; i<3; i++) {
		printf("%d ",inputs[i]);
	}
	printf("\n");
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
  "source_sha256": "04202ed335f913123e6fe0a5e341939a2b88ce589be37f55ef73acbca8728ea6",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6 \n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10 \n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10 \n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100 \n"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "1",
    "ast:c_one_index": "1",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "1",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
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


## sample_020 — train

```c

#include <stdio.h>
int main() 
{
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    if (a < b && a < c){
        if (b < c)
            printf("%d %d %d", a, b, c);
        else
            printf("%d %d %d", a, c, b);
    } 
    if (b < a && b < c){
        if (a < c)
            printf("%d %d %d", b, a, c);
        else
            printf("%d %d %d", b, c, a);
    } 
    if (c < b && c < a){
        if (a < b)
            printf("%d %d %d", c, a, b);
        else
            printf("%d %d %d", c, b, a);
    } 
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
  "source_sha256": "5ad2a3a61b9e97a3ff2eba7fcd4eb1256117d90b3d703eb28bc79ba2156067ab",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
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


## sample_021 — train

```c


#include <stdio.h>

int main() {

    int n1,n2,n3, aux;

    scanf("%d%d%d",&n1,&n2,&n3);
    
    if(n1 > n2) {
        aux = n1;
        n1 = n2;
        n2 = aux;
    }
    if(n3 < n1) printf("%d %d %d",n3,n1,n2); 

    else if(n3 < n2) printf("%d %d %d",n1,n3,n2);

    else printf("%d %d %d",n1,n2,n3);
    
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
  "source_sha256": "91ca54ae7575b8c62c3be2e9d1a199b278bacbef9eab470cef363fa5b59d8514",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
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


## sample_022 — train

```c
#include <stdio.h>

int main() {
	int x, y, z, maior, meio, menor;
	
	scanf("%d%d%d", &x, &y, &z);
	
	(x > y && x > z) ? (maior = x, ((y > z) ? (meio = y, menor = z) : (meio = z, menor = y))) : 
	((y > z && y > x) ? (maior = y, ((z > x) ? (meio = z, menor = x) : (meio = x, menor = z))) : 
	((maior = z, ((x > y) ? (meio = x, menor = y) : (meio = y, menor = x)))));
	
	printf("%d %d %d", menor, meio, maior);
	
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
  "source_sha256": "03cc3386cb2fb9caf9f77fea490af9440d141a52979f38c72615d541a6cfeec7",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
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


## sample_023 — train

```c

#include <stdio.h>

int main(){
    int n1, n2, n3;
    int help, change = 1;

    scanf("%d%d%d",&n1,&n2,&n3);

    while (change == 1){        
        change = 0;

        if (n3 < n2){
            change = 1;
            help = n3;
            n3 = n2;
            n2 = help;
        }
        if (n2 < n1){
            change = 1;
            help = n2;
            n2 = n1;
            n1 = help;
        }
    }

    printf("%d %d %d",n1,n2,n3);
    
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
  "source_sha256": "08fbd5bcec15cda1a958c09a7246ebec5af152c2c309c99a73002666f8b3e127",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
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


## sample_024 — train

```c

#include<stdio.h>

int main() {
    int n1, n2, n3;
    scanf("%d %d %d", &n1, &n2, &n3);
    if (n1 < n2) {
        if (n3 > n2) {
            printf("%d %d %d", n1, n2, n3);
        }
        else if (n1 > n3) {
            printf("%d %d %d", n3, n1, n2);
        }
        else {
            printf("%d %d %d", n1, n3, n2);
        }
    }
    else {
        
        if (n3 > n1) {
            printf("%d %d %d", n2, n1, n3);
        }
        else if (n3 < n2) {
            printf("%d %d %d", n3, n2, n1);
        }
        else {
            printf("%d %d %d", n2, n3, n1);
        }
    }
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
  "source_sha256": "ab9d231c8e7dfc3a03445cd50cd37e7437538b7a54ea5980b4724365df6a339e",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
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


## sample_025 — train

```c

#include <stdio.h>

int main() {
    int num, num2, num3, min, max, mid;
    scanf("%d %d %d", &num, &num2, &num3);
    if (num > num2) {
        if (num > num3) {
            max = num;
            if (num2 > num3) {
                mid = num2;
                min = num3;
            } else {
                mid = num3;
                min = num2;
            }
        } else {
            max = num3;
            mid = num;
            min = num2;
        }
    } else {
        if (num2 > num3) {
            max = num2;
            if (num > num3) {
                mid = num;
                min = num3;
            } else {
                mid = num3;
                min = num;
            }
        } else {
            max = num3;
            mid = num2;
            min = num;
        }
    }
    printf("%d %d %d", min, mid, max);

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
  "source_sha256": "d04383de32362537f9fd7b8a554a2b26613795b7c8ce04d347db6c705c02a23a",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
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


## sample_026 — train

```c

#include <stdio.h>

int main() {
    int n1,n2,n3;
    scanf("%d %d %d", &n1, &n2,& n3);
    if (n1>n2) {
        int aux = n1;
        n1 = n2;
        n2 = aux;
    }
    if (n3 < n1) printf("%d %d %d",n3,n1,n2);
    else if (n3 > n2) printf("%d %d %d",n1,n2,n3);
    else printf("%d %d %d",n1,n3,n2);
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
  "source_sha256": "cd4cfa25a2e8062adbca33b6574080f5956c1fd43082f06aa68b2c0b6a287770",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
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
    int n1,n2,n3,aux;
    scanf("%d %d %d", &n1, &n2,& n3);
    if (n1>n2) {
        aux = n1;
        n1 = n2;
        n2 = aux;
    }
    if (n3 < n1) printf("%d %d %d",n3,n1,n2);
    else if (n3 > n2) printf("%d %d %d",n1,n2,n3);
    else printf("%d %d %d",n1,n3,n2);
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
  "source_sha256": "878319c7c3b0f001cd646a2f6ef2d5252f8b60be6a8fa23ca1b402989a641333",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
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


## sample_028 — validation

```c

#include <stdio.h>

int main () {
    int a, b, c, sup, inf, soma, inter;

    scanf("%d %d %d", &a, &b, &c);
    soma = a + b + c;
    sup = a;
    inf = a; 
    if (b>a)
        sup = b;
        else {
            inf = b;
        }
    if (c>sup)
        sup = c;
    if ( c< inf)
        inf = c;
    inter = soma - (sup + inf);
    printf("%d %d %d", inf, inter, sup);
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
  "source_sha256": "2488e111fda3232ac6a29da55e3fa490a05f7fa27090d37f13c4a0a9cd8a25f8",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 6"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 6 10"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -1 10"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 20 100"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "small",
    "stdout:ex04_1:relation": "whitespace",
    "stdout:ex04_1:edit_band": "small",
    "stdout:ex04_2:relation": "whitespace",
    "stdout:ex04_2:edit_band": "small",
    "stdout:ex04_3:relation": "whitespace",
    "stdout:ex04_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
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


## Evidence refs hợp lệ

```json
[
  "test_statistics",
  "feature_statistics",
  "learned_if_then_rules",
  "semantic_findings",
  "problem_statement",
  "members/sample_001/raw_code",
  "members/sample_001/tests/ex04_0",
  "members/sample_001/tests/ex04_1",
  "members/sample_001/tests/ex04_2",
  "members/sample_001/tests/ex04_3",
  "members/sample_002/raw_code",
  "members/sample_002/tests/ex04_0",
  "members/sample_002/tests/ex04_1",
  "members/sample_002/tests/ex04_2",
  "members/sample_002/tests/ex04_3",
  "members/sample_003/raw_code",
  "members/sample_003/tests/ex04_0",
  "members/sample_003/tests/ex04_1",
  "members/sample_003/tests/ex04_2",
  "members/sample_003/tests/ex04_3",
  "members/sample_004/raw_code",
  "members/sample_004/tests/ex04_0",
  "members/sample_004/tests/ex04_1",
  "members/sample_004/tests/ex04_2",
  "members/sample_004/tests/ex04_3",
  "members/sample_005/raw_code",
  "members/sample_005/tests/ex04_0",
  "members/sample_005/tests/ex04_1",
  "members/sample_005/tests/ex04_2",
  "members/sample_005/tests/ex04_3",
  "members/sample_006/raw_code",
  "members/sample_006/tests/ex04_0",
  "members/sample_006/tests/ex04_1",
  "members/sample_006/tests/ex04_2",
  "members/sample_006/tests/ex04_3",
  "members/sample_007/raw_code",
  "members/sample_007/tests/ex04_0",
  "members/sample_007/tests/ex04_1",
  "members/sample_007/tests/ex04_2",
  "members/sample_007/tests/ex04_3",
  "members/sample_008/raw_code",
  "members/sample_008/tests/ex04_0",
  "members/sample_008/tests/ex04_1",
  "members/sample_008/tests/ex04_2",
  "members/sample_008/tests/ex04_3",
  "members/sample_009/raw_code",
  "members/sample_009/tests/ex04_0",
  "members/sample_009/tests/ex04_1",
  "members/sample_009/tests/ex04_2",
  "members/sample_009/tests/ex04_3",
  "members/sample_010/raw_code",
  "members/sample_010/tests/ex04_0",
  "members/sample_010/tests/ex04_1",
  "members/sample_010/tests/ex04_2",
  "members/sample_010/tests/ex04_3",
  "members/sample_011/raw_code",
  "members/sample_011/tests/ex04_0",
  "members/sample_011/tests/ex04_1",
  "members/sample_011/tests/ex04_2",
  "members/sample_011/tests/ex04_3",
  "members/sample_012/raw_code",
  "members/sample_012/tests/ex04_0",
  "members/sample_012/tests/ex04_1",
  "members/sample_012/tests/ex04_2",
  "members/sample_012/tests/ex04_3",
  "members/sample_013/raw_code",
  "members/sample_013/tests/ex04_0",
  "members/sample_013/tests/ex04_1",
  "members/sample_013/tests/ex04_2",
  "members/sample_013/tests/ex04_3",
  "members/sample_014/raw_code",
  "members/sample_014/tests/ex04_0",
  "members/sample_014/tests/ex04_1",
  "members/sample_014/tests/ex04_2",
  "members/sample_014/tests/ex04_3",
  "members/sample_015/raw_code",
  "members/sample_015/tests/ex04_0",
  "members/sample_015/tests/ex04_1",
  "members/sample_015/tests/ex04_2",
  "members/sample_015/tests/ex04_3",
  "members/sample_016/raw_code",
  "members/sample_016/tests/ex04_0",
  "members/sample_016/tests/ex04_1",
  "members/sample_016/tests/ex04_2",
  "members/sample_016/tests/ex04_3",
  "members/sample_017/raw_code",
  "members/sample_017/tests/ex04_0",
  "members/sample_017/tests/ex04_1",
  "members/sample_017/tests/ex04_2",
  "members/sample_017/tests/ex04_3",
  "members/sample_018/raw_code",
  "members/sample_018/tests/ex04_0",
  "members/sample_018/tests/ex04_1",
  "members/sample_018/tests/ex04_2",
  "members/sample_018/tests/ex04_3",
  "members/sample_019/raw_code",
  "members/sample_019/tests/ex04_0",
  "members/sample_019/tests/ex04_1",
  "members/sample_019/tests/ex04_2",
  "members/sample_019/tests/ex04_3",
  "members/sample_020/raw_code",
  "members/sample_020/tests/ex04_0",
  "members/sample_020/tests/ex04_1",
  "members/sample_020/tests/ex04_2",
  "members/sample_020/tests/ex04_3",
  "members/sample_021/raw_code",
  "members/sample_021/tests/ex04_0",
  "members/sample_021/tests/ex04_1",
  "members/sample_021/tests/ex04_2",
  "members/sample_021/tests/ex04_3",
  "members/sample_022/raw_code",
  "members/sample_022/tests/ex04_0",
  "members/sample_022/tests/ex04_1",
  "members/sample_022/tests/ex04_2",
  "members/sample_022/tests/ex04_3",
  "members/sample_023/raw_code",
  "members/sample_023/tests/ex04_0",
  "members/sample_023/tests/ex04_1",
  "members/sample_023/tests/ex04_2",
  "members/sample_023/tests/ex04_3",
  "members/sample_024/raw_code",
  "members/sample_024/tests/ex04_0",
  "members/sample_024/tests/ex04_1",
  "members/sample_024/tests/ex04_2",
  "members/sample_024/tests/ex04_3",
  "members/sample_025/raw_code",
  "members/sample_025/tests/ex04_0",
  "members/sample_025/tests/ex04_1",
  "members/sample_025/tests/ex04_2",
  "members/sample_025/tests/ex04_3",
  "members/sample_026/raw_code",
  "members/sample_026/tests/ex04_0",
  "members/sample_026/tests/ex04_1",
  "members/sample_026/tests/ex04_2",
  "members/sample_026/tests/ex04_3",
  "members/sample_027/raw_code",
  "members/sample_027/tests/ex04_0",
  "members/sample_027/tests/ex04_1",
  "members/sample_027/tests/ex04_2",
  "members/sample_027/tests/ex04_3",
  "members/sample_028/raw_code",
  "members/sample_028/tests/ex04_0",
  "members/sample_028/tests/ex04_1",
  "members/sample_028/tests/ex04_2",
  "members/sample_028/tests/ex04_3"
]
```
