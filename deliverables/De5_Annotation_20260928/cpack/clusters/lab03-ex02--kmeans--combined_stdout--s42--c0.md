# lab03-ex02--kmeans--combined_stdout--s42--c0

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 59; phân vùng: {'train': 51, 'validation': 8}.


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
    "test_id": "ex02_0",
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
    "test_id": "ex02_1",
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
    "test_id": "ex02_2",
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
    "feature": "stdout:ex02_1:relation",
    "value": "different",
    "n": 57,
    "n_cluster": 59,
    "rate": 0.9661016949152542,
    "cohort_rate": 0.2964824120603015,
    "difference_from_cohort": 0.6696192828549528
  },
  {
    "feature": "stdout:ex02_2:relation",
    "value": "different",
    "n": 57,
    "n_cluster": 59,
    "rate": 0.9661016949152542,
    "cohort_rate": 0.2964824120603015,
    "difference_from_cohort": 0.6696192828549528
  },
  {
    "feature": "stdout:ex02_0:relation",
    "value": "different",
    "n": 50,
    "n_cluster": 59,
    "rate": 0.847457627118644,
    "cohort_rate": 0.25125628140703515,
    "difference_from_cohort": 0.5962013457116089
  },
  {
    "feature": "stdout:ex02_2:edit_band",
    "value": "large",
    "n": 28,
    "n_cluster": 59,
    "rate": 0.4745762711864407,
    "cohort_rate": 0.1407035175879397,
    "difference_from_cohort": 0.333872753598501
  },
  {
    "feature": "stdout:ex02_0:edit_band",
    "value": "medium",
    "n": 37,
    "n_cluster": 59,
    "rate": 0.6271186440677966,
    "cohort_rate": 0.4120603015075377,
    "difference_from_cohort": 0.2150583425602589
  },
  {
    "feature": "stdout:ex02_1:edit_band",
    "value": "large",
    "n": 17,
    "n_cluster": 59,
    "rate": 0.288135593220339,
    "cohort_rate": 0.08542713567839195,
    "difference_from_cohort": 0.20270845754194705
  },
  {
    "feature": "stdout:ex02_1:edit_band",
    "value": "medium",
    "n": 33,
    "n_cluster": 59,
    "rate": 0.559322033898305,
    "cohort_rate": 0.36180904522613067,
    "difference_from_cohort": 0.19751298867217437
  },
  {
    "feature": "stdout:ex02_0:edit_band",
    "value": "large",
    "n": 14,
    "n_cluster": 59,
    "rate": 0.23728813559322035,
    "cohort_rate": 0.07035175879396985,
    "difference_from_cohort": 0.1669363767992505
  },
  {
    "feature": "ast:c_for",
    "value": "0",
    "n": 17,
    "n_cluster": 59,
    "rate": 0.288135593220339,
    "cohort_rate": 0.15577889447236182,
    "difference_from_cohort": 0.13235669874797718
  },
  {
    "feature": "ast:c_while",
    "value": "1",
    "n": 27,
    "n_cluster": 59,
    "rate": 0.4576271186440678,
    "cohort_rate": 0.33668341708542715,
    "difference_from_cohort": 0.12094370155864065
  },
  {
    "feature": "stdout:ex02_2:edit_band",
    "value": "medium",
    "n": 23,
    "n_cluster": 59,
    "rate": 0.3898305084745763,
    "cohort_rate": 0.3065326633165829,
    "difference_from_cohort": 0.08329784515799338
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "0",
    "n": 8,
    "n_cluster": 59,
    "rate": 0.13559322033898305,
    "cohort_rate": 0.07537688442211055,
    "difference_from_cohort": 0.060216335916872504
  },
  {
    "feature": "ast:c_address_of",
    "value": "0",
    "n": 2,
    "n_cluster": 59,
    "rate": 0.03389830508474576,
    "cohort_rate": 0.010050251256281407,
    "difference_from_cohort": 0.023848053828464354
  },
  {
    "feature": "stdout:ex02_0:relation",
    "value": "empty",
    "n": 2,
    "n_cluster": 59,
    "rate": 0.03389830508474576,
    "cohort_rate": 0.010050251256281407,
    "difference_from_cohort": 0.023848053828464354
  },
  {
    "feature": "stdout:ex02_1:relation",
    "value": "empty",
    "n": 2,
    "n_cluster": 59,
    "rate": 0.03389830508474576,
    "cohort_rate": 0.010050251256281407,
    "difference_from_cohort": 0.023848053828464354
  },
  {
    "feature": "stdout:ex02_2:relation",
    "value": "empty",
    "n": 2,
    "n_cluster": 59,
    "rate": 0.03389830508474576,
    "cohort_rate": 0.010050251256281407,
    "difference_from_cohort": 0.023848053828464354
  },
  {
    "feature": "ast:c_if",
    "value": "0",
    "n": 18,
    "n_cluster": 59,
    "rate": 0.3050847457627119,
    "cohort_rate": 0.3015075376884422,
    "difference_from_cohort": 0.0035772080742697
  },
  {
    "feature": "ast:c_update",
    "value": "0",
    "n": 1,
    "n_cluster": 59,
    "rate": 0.01694915254237288,
    "cohort_rate": 0.01507537688442211,
    "difference_from_cohort": 0.0018737756579507714
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "0",
    "n": 6,
    "n_cluster": 59,
    "rate": 0.1016949152542373,
    "cohort_rate": 0.10050251256281408,
    "difference_from_cohort": 0.0011924026914232194
  },
  {
    "feature": "test:ex02_0",
    "value": "fail",
    "n": 59,
    "n_cluster": 59,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
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
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 53,
    "n_cluster": 59,
    "rate": 0.8983050847457628,
    "cohort_rate": 0.8994974874371859,
    "difference_from_cohort": -0.0011924026914231778
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 58,
    "n_cluster": 59,
    "rate": 0.9830508474576272,
    "cohort_rate": 0.9849246231155779,
    "difference_from_cohort": -0.0018737756579507714
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 41,
    "n_cluster": 59,
    "rate": 0.6949152542372882,
    "cohort_rate": 0.6984924623115578,
    "difference_from_cohort": -0.0035772080742696444
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 57,
    "n_cluster": 59,
    "rate": 0.9661016949152542,
    "cohort_rate": 0.9899497487437185,
    "difference_from_cohort": -0.023848053828464333
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 51,
    "n_cluster": 59,
    "rate": 0.864406779661017,
    "cohort_rate": 0.9246231155778895,
    "difference_from_cohort": -0.06021633591687248
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 42,
    "n_cluster": 59,
    "rate": 0.711864406779661,
    "cohort_rate": 0.8442211055276382,
    "difference_from_cohort": -0.13235669874797718
  }
]
```


## IF–THEN dự đoán cluster, không dự đoán gold

```json
[
  {
    "rule_id": 2,
    "if": [
      "NOT (stdout:ex02_1:relation=whitespace)",
      "NOT (stdout:ex02_2:edit_band=small)"
    ],
    "then_cluster": 0,
    "train_support": 45,
    "train_precision": 1.0,
    "holdout_support": 6,
    "holdout_precision": 1.0
  },
  {
    "rule_id": 4,
    "if": [
      "NOT (stdout:ex02_1:relation=whitespace)",
      "stdout:ex02_2:edit_band=small",
      "NOT (stdout:ex02_0:relation=whitespace)"
    ],
    "then_cluster": 0,
    "train_support": 6,
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

sample_002, sample_028, sample_007, sample_041

## sample_002 — train — đại diện

```c
#include <stdio.h>

void piramide (int N)  {
 
 #define ESPACOS 4
 #define NUMEROS 1
 int i, espacos = ESPACOS, j, numeros = NUMEROS, k;

 for (i = 1; i <= N; i++) {

   for (j = 0; j < espacos; j++)  {

    printf(" "); }

  espacos --;

  for (k=1 ; k<= numeros; k++)  {
 
   if ( k <= i) {
    printf ("%d", k); }

   else  {
    
    printf("%d", i - (k-i));} }

  numeros += 2; 
  printf ("\n"); }
}


int main()  {

 int N;

 scanf ("%d", &N);
 piramide(N);
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
  "source_sha256": "c6c8626b63d1dd743838b7732bd422338052c042854305328f4c3b77d7cecdca",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1\n   121\n  12321\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "    1\n   121\n  12321\n 1234321\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "    1\n   121\n  12321\n 1234321\n123454321\n12345654321\n1234567654321\n123456787654321\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_007 — train — đại diện

```c
#include <stdio.h>



void piramide(int N) {
  int i = 0, j = 0, num = 0;

  while (i++ < N) {
    while (j++ < N - i)
      printf(" ");
    while (num++ < i)
      printf("%d", num);
    num--;
    while (--num > 0)
      printf("%d", num);
    printf("\n");
    j = 0;
    num = 0;
  }
}

int main() {
  int N;
  scanf("%d", &N);
  piramide(N);

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
  "source_sha256": "858e61e7bc2b3fe3aa773ab1f9bbb1d3495d6ca3a9a535650cafc58608da9808",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "  1\n 121\n12321\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "   1\n  121\n 12321\n1234321\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "       1\n      121\n     12321\n    1234321\n   123454321\n  12345654321\n 1234567654321\n123456787654321\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_028 — validation — đại diện

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
  "sample_id": "sample_028",
  "partition": "validation",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "bd724a04012cc2ef4f046773dc88dee01a870b6f98ddb52a202137bb823bcc3a",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": ""
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": ""
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "0",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "empty",
    "stdout:ex02_0:edit_band": "large",
    "stdout:ex02_1:relation": "empty",
    "stdout:ex02_1:edit_band": "large",
    "stdout:ex02_2:relation": "empty",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_041 — train — đại diện

```c

#include <stdio.h>

void piramide(int N);


int main()
{


    return 0;
}

void piramide(int N)
{
    int l, c;

    for(l = 0; l < N ; l++)
    {
        for(c = 0; c < N+N; c++)
        {
            
        }
    }
}
```

```json
{
  "sample_id": "sample_041",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "7dfb90aff5706f050859b8427bb8f8b62f25727840dd33b5535bf79e05268ceb",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": ""
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": ""
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "0",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "empty",
    "stdout:ex02_0:edit_band": "large",
    "stdout:ex02_1:relation": "empty",
    "stdout:ex02_1:edit_band": "large",
    "stdout:ex02_2:relation": "empty",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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
    "ast:c_address_of": "0",
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

void piramide(int N)
{
	int i, j;

	for(i = 0; i < N; i++)
	{
		for(j = 1; j < N-i; j++)
			printf(" ");
		for(j = 1; j < 1+i; j++)
			printf("%d", j);
		for(j = 1+i; j > 0; j--)
			printf("%d", j);
		printf("\n");
	}
}

int main()
{
	int in;
	scanf("%d", &in);

	piramide(in);

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
  "source_sha256": "bdb33ede76869c7ca64bca3126f81a161685542137ee563e518a6aa8cc0c99f9",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "  1\n 121\n12321\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "   1\n  121\n 12321\n1234321\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "       1\n      121\n     12321\n    1234321\n   123454321\n  12345654321\n 1234567654321\n123456787654321\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_003 — train

```c
#include <stdio.h>




void piramide(int N)
{
    int i, j, k;
    for (i = 1; i<= N; i++)
    {
        for(j = 0; j < N - i; j++)
        {
            printf(" ");
            printf(" ");
        }
        
        for(j = 1; j <= i; j++)
        {
            printf("%d", j);
            printf(" ");
        }

        for(k = i - 1; k >= 1; --k)
        {
            printf("%d", k);
        }
    printf("\n");
    }
}


int main()
{
    int N;
    scanf("%d", &N);
    piramide(N);
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
  "source_sha256": "863d982ba6d53b8a74bace7332fd10c6ba6e339b9431e2c7198c0c2457fd2127",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1\n1 2 3 21\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1\n  1 2 3 21\n1 2 3 4 321\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1\n          1 2 3 21\n        1 2 3 4 321\n      1 2 3 4 5 4321\n    1 2 3 4 5 6 54321\n  1 2 3 4 5 6 7 654321\n1 2 3 4 5 6 7 8 7654321\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_004 — train

```c
#include <stdio.h>

void piramide(int n)
{
 int linhas,coluna,col=0,espacos;
 for (linhas=1; linhas<=n; linhas++)
 {
  espacos = n-linhas;
  for (; espacos !=0; espacos--)
     printf("  ");
  col = linhas;
  for(coluna=1;coluna<=(linhas*2 -1); coluna++)
  {
   if (coluna<=n)
      printf ("%d ",coluna);
   else
      {
      col--;
      printf ("%d ", col);
      }
  }
  printf("\n");
 }
 return;
}


int main()
{
 int n;
 scanf("%d",&n);
 if (n>=2)
 {
  piramide(n);
 } 
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
  "source_sha256": "3aeda1ac70e7cfc73458f76bbedde2bccf70324b534b7a17c51d0da203db2af3",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 3 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 3 \n  1 2 3 4 2 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 3 \n          1 2 3 4 5 \n        1 2 3 4 5 6 7 \n      1 2 3 4 5 6 7 8 4 \n    1 2 3 4 5 6 7 8 5 4 3 \n  1 2 3 4 5 6 7 8 6 5 4 3 2 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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

void piramide(int n)
{
 int linhas,coluna,col=0,espacos;
 for (linhas=1; linhas<=n; linhas++)
 {
  espacos = n-linhas;
  for (; espacos !=0; espacos--)
     printf("  ");
  col = linhas;
  for(coluna=1;coluna<=(linhas*2 -1); coluna++)
  {
   if (coluna<=n)
      printf ("%d ",coluna);
   else
      {
      col--;
      if (coluna==(linhas*2 -1))
          printf ("%d", col);
      else
          printf ("%d ",col);
      }
  }
  printf("\n");
 }
 return;
}


int main()
{
 int n;
 scanf("%d",&n);
 if (n>=2)
 {
  piramide(n);
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
  "source_sha256": "130e3f2cdd16c65d466316068ce23161b274c7488a64ee0be7b27142e775a4d3",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 3 \n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 3 \n  1 2 3 4 2\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 3 \n          1 2 3 4 5 \n        1 2 3 4 5 6 7 \n      1 2 3 4 5 6 7 8 4\n    1 2 3 4 5 6 7 8 5 4 3\n  1 2 3 4 5 6 7 8 6 5 4 3 2\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_006 — train

```c

#include <stdio.h>

void piramide(int n)
{
	int i, j;
	for(i = 1; i <= n; i++){
		for(j = 1; j <= 2 * (n - i); j++){
			printf(" ");}
		for(j = 2; j <= i; j++){
			printf("%d ", j);}
		for(j = i - 1; j > 1; j--){
			printf("%d ", j);}
		printf("1\n");
		}
}

int main()
{
	int n;
	scanf("%d", &n);
	piramide(n);
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
  "source_sha256": "1b958d759813bdd94d21b4b9a3bc33399aa31c9db4865b10a23fa699151a89d8",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1\n  2 1\n2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1\n    2 1\n  2 3 2 1\n2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1\n            2 1\n          2 3 2 1\n        2 3 4 3 2 1\n      2 3 4 5 4 3 2 1\n    2 3 4 5 6 5 4 3 2 1\n  2 3 4 5 6 7 6 5 4 3 2 1\n2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_008 — validation

```c
#include <stdio.h>

void piramide(int N);

int main()
{
    int N;
   
    scanf("%d", &N);
   
    piramide(N);
   
    return 0;
}

void piramide(int N)
{
    int i, j;
   
    for(i = 1; i <= N; i++)
    {
        for(j = 1; j <= 2 * (N - i); j++)
            putchar(' ');
       
        for(j = 1; j <= i; j++)
        {
            if((i == j) == 1)
                printf("%d", j);
            else
                printf("%d ", j);
        }
       
        for(j = i - 1; j >= 1; j--)
            printf("%d ", j);
        
        printf("\n");
    }
}
```

```json
{
  "sample_id": "sample_008",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "59c9055598baebf25de2cd66fe180f199423cfab218302bbd513bd8ba3cb5844",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1\n  1 21 \n1 2 32 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1\n    1 21 \n  1 2 32 1 \n1 2 3 43 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1\n            1 21 \n          1 2 32 1 \n        1 2 3 43 2 1 \n      1 2 3 4 54 3 2 1 \n    1 2 3 4 5 65 4 3 2 1 \n  1 2 3 4 5 6 76 5 4 3 2 1 \n1 2 3 4 5 6 7 87 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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

void cruz (int N)
{
  int row, col, passo = 0;

  for (row = 0; row < N; row++)
  {
    for (col = 1; col <= N; col++)
    {
      if ((col - passo == 1) || (col + passo == N))
      {
        if (col == N)
          printf("*\n");
        else 
          printf("*");
      }
      else if (col == N)
        printf("-\n");
      else
        printf("-");
    }
    passo++;
  }

}


int main()
{
  int N;

  scanf("%d", &N);

  cruz(N);

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
  "source_sha256": "c62650d0b01820f4eb7eb395aedf0a74344f1cdcc540e8b47dfc5e3f47108d73",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "large",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "large",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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

void piramide(int N){
    int i,j,k;
    for (j = 1;j<=N;j++) {
        int X = j; 
        for (i = N-j;i>0;i--)
            printf("  ");
        for (k = 1;k<= j*2-1;k++){
            if (k>j){
                X--;
                printf("%d ",X);
            }
            else
                printf("%d ",k);
        }
        printf("\n");
    }   
}

int main(){
    int N = 0;
    while (N<2) {
        printf("qual é o tamanho da piramide? (>= 2): ");
        scanf("%d",&N);
    }
    piramide(N);
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
  "source_sha256": "0554030d9d38a39a6a617e2fe9a684e86679d78cb59fa8d652a0e31bbebc2b31",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "qual é o tamanho da piramide? (>= 2):     1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "qual é o tamanho da piramide? (>= 2):       1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "qual é o tamanho da piramide? (>= 2):               1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "large",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
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


## sample_011 — validation

```c


#include <stdio.h>

void piramide(int);

int main(){
    int n;
    scanf("%d", &n);
    piramide(n);
    return 0;
}

void piramide(int n){
    int c,l;
    for (l = 1; l <= n; l++){
        for (c = 1; c <= n+l-1; c++){
            if (n >= c && c > n-l)
                printf("%d", c+l-5);
            else if (c > n)
                printf("%d", l-c+5);
            else
                putchar(' ');
        }
        putchar('\n');
    }
}
```

```json
{
  "sample_id": "sample_011",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "98cf4c2bcada3027001b617f4b69ac698b5a0ba4904a7c231fdb01ed673faa04",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "  -1\n -103\n-10143\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "   0\n  012\n 01232\n0123432\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "       4\n      45-2\n     456-1-2\n    45670-1-2\n   4567810-1-2\n  456789210-1-2\n 456789103210-1-2\n456789101143210-1-2\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "large",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "large",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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

#include<stdio.h>
void piramide(int n){
    int i,j, k;

    for(i=1;i<=n;i++){
        for(j=1;j<=2*n-1;j++){
            for(k=1;k<=(n-j)*2;k++)
                printf("*");
            for(n=1;n<=j;n++)
                printf("%d",n);
            for(n=j-1; n>0;n--)
                printf("%d",n);
        }
        printf("\n"); 
    }
}

int main(){
    int n;
    scanf("%d",&n);
    printf(" ");
    if(n>=2)
        piramide(n);
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
  "source_sha256": "7d428ab9b8ccc07fb8997ad8ed1c03d20b5cfeb70274a57d2290a374f679e69b",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": " ****1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": " ******1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": " **************1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "large",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "large",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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

void piramide(int n)
{
    int key = n;
    int i, j, k;
    while (key > 0)
    {
        for (i = 1; i <= (2*key)-2; i++)
        {
            printf(" ");
        }
        for (j = 1; j <= n - key + 1; j++)
        {
            if ((j == 1) && (j == n - key + 1))
                printf("%d ", j);
        }
        for (k = n - key; k >= 1; k--)
        {
            if (k != 1)
                printf("%d ", k);
            else
                printf("%d", k);
        }
        printf("\n");
        key--;
    }
}

int main()
{
    int n;
    scanf("%d", &n);
    if (n < 2)
        return -1;
    piramide(n);
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
  "source_sha256": "87b122411c63b08377870b6bf707fdd7d3d7839ccb2108ec68285da89cffcb55",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1\n2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1\n  2 1\n3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1\n          2 1\n        3 2 1\n      4 3 2 1\n    5 4 3 2 1\n  6 5 4 3 2 1\n7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "large",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
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


## sample_014 — train

```c

#include <stdio.h>

void piramide(int n)
{
    int keep = n;
    int i, j, k;
    while (keep > 0)
    {
        for (i = 1; i <= (2*keep)-2; i++)
        {
            printf(" ");
        }
        for (j = 1; j <= n - keep + 1; j++)
        {
            if ((j == 1) && (j == n - keep + 1))
                printf("%d ", j);
        }
        for (k = n - keep; k >= 1; k--)
        {
            if (k != 1)
                printf("%d ", k);
            else
                printf("%d", k);
        }
        printf("\n");
        keep--;
    }
}

int main()
{
    int n;
    scanf("%d", &n);
    if (n < 2)
        return -1;
    piramide(n);
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
  "source_sha256": "453e82540638eafe600385fa9a005cb566f8e60a9212241115fb5829c196a55e",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1\n2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1\n  2 1\n3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1\n          2 1\n        3 2 1\n      4 3 2 1\n    5 4 3 2 1\n  6 5 4 3 2 1\n7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "large",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
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


## sample_015 — train

```c

#include <stdio.h>
void piramide(int n){
    int l, c;
    for (l = 0; l < n; l++){
        for (c = 0;((c < n)||(c > n)); c++){
            if (c > 0)
                putchar(' ');
            if ((l + 2 - n + c) > 0)
                printf("%d",l + 2 - n + c);
            else
                putchar(' ');
        }
        for (c--; c > 0; c--){
            if ((l + 1 - n + c) > 0)
                printf("%d", l + 1 - n + c);
        }
        printf("\n");
    }
}

int main(){
    int n;
    scanf("%d",&n);
    piramide(n);
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
  "source_sha256": "acec2aaf183c9cb54c9560088efb084eefb7763f0ffa40951e199ad8e90d7227",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1\n  1 21\n1 2 321\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1\n    1 21\n  1 2 321\n1 2 3 4321\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1\n            1 21\n          1 2 321\n        1 2 3 4321\n      1 2 3 4 54321\n    1 2 3 4 5 654321\n  1 2 3 4 5 6 7654321\n1 2 3 4 5 6 7 87654321\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_016 — train

```c

#include <stdio.h>
void piramide(int n){
    int l, c;
    for (l = 0; l < n; l++){
        for (c = 0; c < n; c++){
            if (c > 0)
                putchar(' ');
            if ((l + 2 - n + c) > 0)
                printf("%d",l + 2 - n + c);
            else
                putchar(' ');
        }
        for (c--; c > 0; c--){
            if ((l + 1 - n + c) > 0)
                printf("%d", l + 1 - n + c);
        }
        printf("\n");
    }
}

int main(){
    int n;
    scanf("%d",&n);
    piramide(n);
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
  "source_sha256": "48fcce8cd9f6e372aa9c93b575893da8f6907af2c19de4e24165fa086ca594ce",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1\n  1 21\n1 2 321\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1\n    1 21\n  1 2 321\n1 2 3 4321\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1\n            1 21\n          1 2 321\n        1 2 3 4321\n      1 2 3 4 54321\n    1 2 3 4 5 654321\n  1 2 3 4 5 6 7654321\n1 2 3 4 5 6 7 87654321\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_017 — train

```c

#include <stdio.h>
void piramide(int n){
    int l, c;
    for (l = 0; l < n; l++){
        for (c = 0;((c < n)||(c > n)); c++){
            if (c > 0)
                putchar(' ');
            if ((l + 2 - n + c) > 0) {
                printf("%d",l + 2 - n + c);
            } else {
                putchar(' ');
            }
        }
        for (c--; c > 0; c--){
            if ((l + 1 - n + c) > 0){
                printf("%d", l + 1 - n + c);
            }
        }
        printf("\n");
    }
}

int main(){
    int n;
    scanf("%d",&n);
    piramide(n);
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
  "source_sha256": "c1388324ee6c9b4f005cf07761f32c7fedfb7fca759c25fd02ace8e002febc1e",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1\n  1 21\n1 2 321\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1\n    1 21\n  1 2 321\n1 2 3 4321\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1\n            1 21\n          1 2 321\n        1 2 3 4321\n      1 2 3 4 54321\n    1 2 3 4 5 654321\n  1 2 3 4 5 6 7654321\n1 2 3 4 5 6 7 87654321\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_018 — train

```c

#include <stdio.h>

int main(){
    int n,i,j,k,m;
    scanf("%d", &n);
    for ( j = 1; j<=n; j++)
    {
        k=1;
        m=j;
        for ( i = 0; i <= n-j; i++)
        {
            printf(" ");
        }
        while (k<=j)
        {
            printf("%d",k);
            k++;
        }
        while (m-->1)
        {
            printf("%d",m);
        }
        printf("\n");
    }
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
  "source_sha256": "fb45c7831814094c5e0169eabd1a6cdb74f2eeaf4fae444c34df9399344c8cc8",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "   1\n  121\n 12321\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "    1\n   121\n  12321\n 1234321\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "        1\n       121\n      12321\n     1234321\n    123454321\n   12345654321\n  1234567654321\n 123456787654321\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_019 — train

```c


#include <stdio.h>

void piramide(int N) {

    int i, j, n;

    for (i = 1; i <= N; i++) {
        for (j = 1; j <= N - i; j++)
            printf(" ");

        for (n = 1; n <= i; n++)
            printf("%d", n);

        for (n = i - 1; n >= 1; n--)
            printf("%d", n);

        printf("\n");
    }
}

int main () {

    int N;

    while (N < 2)
        scanf("%d", &N);

    piramide(N);
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
  "source_sha256": "6f7f3bbe1f8a1b76211bf5308439db7fafe0ac85bbe969c94108d8fe0b61a84d",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "  1\n 121\n12321\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "   1\n  121\n 12321\n1234321\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "       1\n      121\n     12321\n    1234321\n   123454321\n  12345654321\n 1234567654321\n123456787654321\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_020 — train

```c


#include <stdio.h>

void piramide(int N) {

    int i, j, n;

    for (i = 1; i <= N; i++) {
        for (j = 1; j <= N - i; j++)
            printf(" ");

        for (n = 1; n <= i; n++)
            printf("%d", n);

        for (n = i - 1; n >= 1; n--)
            printf("%d", n);

        for (j = N + i; j <= (2 * N - 1); j++)
            printf(" ");

        printf("\n");
    }
}

int main () {

    int N;

    while (N < 2)
        scanf("%d\n", &N);

    piramide(N);
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
  "source_sha256": "c788ef9286cf6056d1277e3b73d1d5957b1951c1814033714e92738adff22e9f",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "  1  \n 121 \n12321\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "   1   \n  121  \n 12321 \n1234321\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "       1       \n      121      \n     12321     \n    1234321    \n   123454321   \n  12345654321  \n 1234567654321 \n123456787654321\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_021 — train

```c


#include <stdio.h>

void piramide(int N) {

    int i, j, n;

    for (i = 1; i <= N; i++) {
        for (j = 1; j <= N - i; j++)
            printf(" ");

        for (n = 1; n <= i; n++)
            printf("%d", n);

        for (n = i - 1; n >= 1; n--)
            printf("%d", n);

        printf("\n");
    }
}

int main () {

    int N;

    scanf("%d", &N);
    piramide(N);

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
  "source_sha256": "2ac9e86e6947532aaf7105bd66962ce6265b2fd87c09af7a090a0ae36d196824",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "  1\n 121\n12321\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "   1\n  121\n 12321\n1234321\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "       1\n      121\n     12321\n    1234321\n   123454321\n  12345654321\n 1234567654321\n123456787654321\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_022 — train

```c


#include <stdio.h>

void piramide(int N) {

    int i, j, n;

    for (i = 1; i <= N; i++) {
        for (j = 1; j <= N - i; j++)
            printf(" ");

        for (n = 1; n <= i; n++)
            printf("%d", n);

        for (n = i - 1; n >= 1; n--)
            printf("%d", n);

        for (j = N + i; j <= (2 * N - 1); j++)
            printf(" ");

        printf("\n");
    }
}

int main () {

    int N;

    while (N < 2)
        scanf("%d", &N);

    piramide(N);
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
  "source_sha256": "be1a4ac29441e148ad93d0e8ed3f84246c7fabef9149d25c0a794292373a1b86",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "  1  \n 121 \n12321\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "   1   \n  121  \n 12321 \n1234321\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "       1       \n      121      \n     12321     \n    1234321    \n   123454321   \n  12345654321  \n 1234567654321 \n123456787654321\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_023 — train

```c

#include <stdio.h>

void piramide(int N)
{
    int i, j;
    for(i=1; i<=N; i++)
    {
        for(j=1; j<=(N-i); j++)
        {
            putchar(' ');
        }
        for(j=1; j<=i; j++)
        {
            printf("%d", j);
        }
        for(j=i-1; j>0; j--)
        {
            printf("%d", j);
        }
        putchar('\n');
    }
}

int main()
{
    int N;
    scanf("%d", &N);
    if(N>=2)
    {
        piramide(N);
    }
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
  "source_sha256": "720625b46336910189dc431dc10e2aba885946ed35d70a92f4684abdd4d2efa8",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "  1\n 121\n12321\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "   1\n  121\n 12321\n1234321\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "       1\n      121\n     12321\n    1234321\n   123454321\n  12345654321\n 1234567654321\n123456787654321\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_024 — train

```c

#include <stdio.h>

void piramide(int N) {
    int i, j;
    for (i = 1; i <= N; ++i) {
        for (j = N - 1; j > 0; --j) 
            printf("  ");

        for (j = 0; j < i; ++j)
            printf(" %d", j);




        for (j = 0; j < i; ++j) 
            printf("%d", i);
        putchar('\n');
    }
}


int main() {
    int N;
    scanf("%d", &N);
    piramide(N);

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
  "source_sha256": "1d1b593e38b1b4434c531096f832f0260222bf791992986a4ac170d3289ec846",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "     01\n     0 122\n     0 1 2333\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       01\n       0 122\n       0 1 2333\n       0 1 2 34444\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               01\n               0 122\n               0 1 2333\n               0 1 2 34444\n               0 1 2 3 455555\n               0 1 2 3 4 5666666\n               0 1 2 3 4 5 67777777\n               0 1 2 3 4 5 6 788888888\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "large",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "large",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_025 — validation

```c

#include <stdio.h>
int main()
{
    int Num;
    int NumeroEscrito=1;
    int NumeroColuna=1;
    int NumEspacos;
    int NumEspacosEscritos;
    scanf ("%d",&Num);
    NumEspacos=Num;
    NumEspacosEscritos=1;
    while (NumeroColuna<=Num)
    {
        while (NumEspacosEscritos<NumEspacos)
        {
            printf("\t");
            NumEspacosEscritos++;
        }

        while (NumeroEscrito<NumeroColuna)
        {
            printf("%d\t",NumeroEscrito);
            NumeroEscrito++;
        }
        while (NumeroEscrito>0)
        {
            printf("%d\t",NumeroEscrito);
            NumeroEscrito--;
        }
        printf("\n");
        NumEspacos--;
        NumeroColuna++;
        
        
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
  "source_sha256": "1e0620eb0006a05a26aa209071d411479ab56a70fe582293da1863d7b0f28e76",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "\t\t1\t\n0\t1\t2\t1\t\n0\t1\t2\t3\t2\t1\t\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "\t\t\t1\t\n0\t1\t2\t1\t\n0\t1\t2\t3\t2\t1\t\n0\t1\t2\t3\t4\t3\t2\t1\t\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "\t\t\t\t\t\t\t1\t\n0\t1\t2\t1\t\n0\t1\t2\t3\t2\t1\t\n0\t1\t2\t3\t4\t3\t2\t1\t\n0\t1\t2\t3\t4\t5\t4\t3\t2\t1\t\n0\t1\t2\t3\t4\t5\t6\t5\t4\t3\t2\t1\t\n0\t1\t2\t3\t4\t5\t6\t7\t6\t5\t4\t3\t2\t1\t\n0\t1\t2\t3\t4\t5\t6\t7\t8\t7\t6\t5\t4\t3\t2\t1\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "large",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "large",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_026 — train

```c

#include <stdio.h>

void piramide (int n)
{
    int i=1,j;

    while (i<=n)
    {
        for (j=1; j<=2*(n-i); printf("_"), j++);
        for (j=1; j<=i; j++)
        {
            printf("%d",j);
            if (j != i)
                printf("_");
        }
        for (j=i-1; j>=1;printf("_%d",j--));
        printf("\n");
        i++;
    
    }
}

int main()
{

    int n;
    scanf("%d", &n);
    piramide(n);
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
  "source_sha256": "21f0ea5e8111d0a5af0a5e0ba3bebf91debf66b72560a15b91a2aca363e399b6",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "____1\n__1_2_1\n1_2_3_2_1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "______1\n____1_2_1\n__1_2_3_2_1\n1_2_3_4_3_2_1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "______________1\n____________1_2_1\n__________1_2_3_2_1\n________1_2_3_4_3_2_1\n______1_2_3_4_5_4_3_2_1\n____1_2_3_4_5_6_5_4_3_2_1\n__1_2_3_4_5_6_7_6_5_4_3_2_1\n1_2_3_4_5_6_7_8_7_6_5_4_3_2_1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "large",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "large",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
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


## sample_027 — train

```c


#include <stdio.h>

void piramide(int n) {

    int i, j;
    int num;

    for (i=1; i<=n; i++) {
        num = 1;
        for (j=1; j<n+i-1; j++) {

            if (j > n-i && j < n+i-1) {
                printf("%d ",num);
                num++;
            }
            else {
                printf("  ");
            }
        }
        
        printf("%d\n",num);
    }
}

int main() {

    int n;

    scanf("%d",&n);
    piramide(n);

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
  "source_sha256": "266d4a0990ce622d223bba1b30a260ae30178ee10954d6bceb352c5181548467",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1\n  1 2 3\n1 2 3 4 5\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1\n    1 2 3\n  1 2 3 4 5\n1 2 3 4 5 6 7\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1\n            1 2 3\n          1 2 3 4 5\n        1 2 3 4 5 6 7\n      1 2 3 4 5 6 7 8 9\n    1 2 3 4 5 6 7 8 9 10 11\n  1 2 3 4 5 6 7 8 9 10 11 12 13\n1 2 3 4 5 6 7 8 9 10 11 12 13 14 15\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_029 — validation

```c

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

void piramide(int N){
    int i, j, d = 0;
    for(i = 1; i <= N; i++){
        d = 1;
        for(j = 1; j <= N + i - 1; j++){
            if(j < N && j >= N - i + 1){ 
                printf("%d", d++);
            }
            else if(j >= N){
                printf("%d", d--);
            }
            else{putchar(' ');}
            putchar(j < N + i - 1 ? ' ' : '\n');
        }
        printf("%d\n", j);
    }
}

int main(){
    int N;
    scanf("%d", &N);
    if(N >= 2){
        piramide(N);
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_029",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "e01364659447b2bd03800dc4820fcda7df8b261641801c9df0d3fd4289bbbc83",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1\n4\n  1 2 1\n5\n1 2 3 2 1\n6\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1\n5\n    1 2 1\n6\n  1 2 3 2 1\n7\n1 2 3 4 3 2 1\n8\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1\n9\n            1 2 1\n10\n          1 2 3 2 1\n11\n        1 2 3 4 3 2 1\n12\n      1 2 3 4 5 4 3 2 1\n13\n    1 2 3 4 5 6 5 4 3 2 1\n14\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n15\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n16\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_030 — train

```c

#include <stdio.h>

int main(){

    int N;
    void piramide();

    scanf("%d", &N);
    piramide(N);

    return 0;

}

void piramide(int N){

    int i, incial = 1;
    
    while (incial <= N)
    {
    
        for(i = 0; i < (N-incial)*2; i++)
            printf(" ");

        for(i = 1; i <= incial; i++){
            printf("%d", i);
            if (i != incial)
                printf(" ");
        }
            
        
        for(i -= 2; i > 0; i--){
            printf("%d", i);
            if (i != 1)
                printf(" ");
        }
        
        for(i = 0; i < (N-incial)*2; i++)
            printf(" ");
        printf("\n");
        incial++;
    }
    
}
```

```json
{
  "sample_id": "sample_030",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "3adcf148daf77b33208316c9c7f6f19bc0c7eab7fc164fcdc74e9ad3d580e3d4",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1    \n  1 21  \n1 2 32 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1      \n    1 21    \n  1 2 32 1  \n1 2 3 43 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1              \n            1 21            \n          1 2 32 1          \n        1 2 3 43 2 1        \n      1 2 3 4 54 3 2 1      \n    1 2 3 4 5 65 4 3 2 1    \n  1 2 3 4 5 6 76 5 4 3 2 1  \n1 2 3 4 5 6 7 87 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
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


## sample_031 — train

```c

#include <stdio.h>

void piramide (int N) {
    int linha, col, i;
    for (linha = 1; linha <= N; linha++) {
        i = 0;
        for (col = 1; col <= (N + linha - 1); col++) {
            if (col > (N - linha)){
                if (col <= N)
                    printf("%d", ++i);
                else
                    printf("%d", --i);
            }
            else {
                printf(" ");
            }
        }
        printf("\n");
    }
}

int main () {
    int N;
    scanf("%d", &N);
    piramide(N);

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
  "source_sha256": "22dc2b16ad1e8e1b62c1d5d9812cd99c9668d89a8b025c9ee48d27252879c0d0",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "  1\n 121\n12321\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "   1\n  121\n 12321\n1234321\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "       1\n      121\n     12321\n    1234321\n   123454321\n  12345654321\n 1234567654321\n123456787654321\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_032 — train

```c

#include <stdio.h>

void piramide (int N) {
    int linha, col, i;
    for (linha = 1; linha <= N; linha++) {
        i = 0;
        for (col = 1; col <= (N + linha - 1); col++) {
            if (col > (N - linha)){
                if (col <= N)
                    printf("%d", ++i);
                else if (col < (2*N - 1))
                    printf("%d", --i);
                else 
                    printf("%d\n", --i);
            }
            else {
                printf(" ");
            }
        }
        printf("\n");
    }
}

int main () {
    int N;
    scanf("%d", &N);
    piramide(N);

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
  "source_sha256": "eecd2e5a04738d461d471283f8313d327cf175ee5f94547dc607d800e365462f",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "  1\n 121\n12321\n\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "   1\n  121\n 12321\n1234321\n\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "       1\n      121\n     12321\n    1234321\n   123454321\n  12345654321\n 1234567654321\n123456787654321\n\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_033 — train

```c

#include <stdio.h>

void piramide (int num) {
    int linha, col, i;
    for (linha = 1; linha <= num; linha++) {
        i = 0;
        for (col = 1; col <= (num + linha - 1); col++) {
            if (col > (num - linha)){
                if (col <= num)
                    printf("%d", ++i);
                else if (col < (2*num - 1))
                    printf("%d", --i);
                else 
                    printf("%d\n", --i);
            }
            else {
                printf(" ");
            }
        }
        printf("\n");
    }
}

int main () {
    int num;
    scanf("%d", &num);
    piramide(num);

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
  "source_sha256": "517d47a5bc91c88af2c4bede40402d6fb0d8ce5b7f3b68086dcdd95ca9b7c903",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "  1\n 121\n12321\n\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "   1\n  121\n 12321\n1234321\n\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "       1\n      121\n     12321\n    1234321\n   123454321\n  12345654321\n 1234567654321\n123456787654321\n\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_034 — train

```c


#include <stdio.h>

void piramide(int N){
    int l,c;
    for (l=0;l<N;l++) {
        for(c=0; c<N-l-1;c++) {
            printf("  ");
        }
        for(c=0; c<l;c++) {
            printf("%d", c+1);
        }
        printf("%d",l+1);

        for(c=0; c<l;c++) {
            printf("%d", l+1-1-c);

        putchar('\n');


        }
        
    }
}

int main() {
    int H;
    scanf("%d", &H);
    piramide(H);
    return 0;
}



```

```json
{
  "sample_id": "sample_034",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "a004d06b3f17585067a0428350baf5fe0e3a942aba108707c510550de67f7054",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1  121\n1232\n1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1    121\n  1232\n1\n12343\n2\n1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1            121\n          1232\n1\n        12343\n2\n1\n      123454\n3\n2\n1\n    1234565\n4\n3\n2\n1\n  12345676\n5\n4\n3\n2\n1\n123456787\n6\n5\n4\n3\n2\n1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_035 — train

```c

#include <stdio.h>
void piramide(int N) {
   int i, j, spaces;
   for (i = 1; i<=N; i++){
      spaces = 0;
     while(spaces < (N-i)*2) {
        printf(" ");
        spaces++;
     }
        for (j = 1; j<=i; j++) {
        printf("%d ", j);
     }
        for (j = 1; j < 1; j++) {
        printf("%d ", i - j);
    }
     printf("\n");
    }
}
int main() {
    int N;
    scanf("%d", &N);
    piramide(N);
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
  "source_sha256": "b7f05a1121d14701cea907c7893c11e57c45c7d565548481cb13318f0aae2f3d",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 \n1 2 3 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 \n  1 2 3 \n1 2 3 4 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 \n          1 2 3 \n        1 2 3 4 \n      1 2 3 4 5 \n    1 2 3 4 5 6 \n  1 2 3 4 5 6 7 \n1 2 3 4 5 6 7 8 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_036 — train

```c

#include <stdio.h>
void piramide(int N) {
   int i, j, spaces;
   for (i = 1; i<=N; i++){
    spaces = 0;
    while(spaces < (N-i)* 2) {
        printf(" ");
        spaces++;
    }
    for (j = 1; j<=i; j++) {
        printf("%d ", j);
    }
    for (j = 1; j < 1; j++) {
    printf("%d ", i - j);
    }
     printf("\n");
   }
   }
int main() {
    int N;
    scanf("%d", &N);
    piramide(N);
    return 0;
}

```

```json
{
  "sample_id": "sample_036",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "47f0c7142a9463dd033cf7db18c48bd4eb58f497cf47fbc664648859e93e7a56",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 \n1 2 3 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 \n  1 2 3 \n1 2 3 4 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 \n          1 2 3 \n        1 2 3 4 \n      1 2 3 4 5 \n    1 2 3 4 5 6 \n  1 2 3 4 5 6 7 \n1 2 3 4 5 6 7 8 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_037 — validation

```c

#include <stdio.h>

void piramide(int N) {
    int i, j, k, l;

    for (i = 0; i <= N; i++) {
        for (j = 0; j > i; j--) {
            printf("  ");
        }
        for (k = 0; k <= i; k++) {
            printf("%d", k);
            if (k < i) printf(" ");
        }
        for (l = i - 1; l >= 1; l--) {
            printf("%d", l);
        }
        putchar('\n');
    }
}

int main() {
    int N;
    
    scanf("%d", &N);

    piramide(N);
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
  "source_sha256": "e22d2a63c9995acf328b7325682bdc02ffa269a7f72211ec3d2d8e10305a1357",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "0\n0 1\n0 1 21\n0 1 2 321\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "0\n0 1\n0 1 21\n0 1 2 321\n0 1 2 3 4321\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "0\n0 1\n0 1 21\n0 1 2 321\n0 1 2 3 4321\n0 1 2 3 4 54321\n0 1 2 3 4 5 654321\n0 1 2 3 4 5 6 7654321\n0 1 2 3 4 5 6 7 87654321\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "large",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "large",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_038 — validation

```c

#include <stdio.h>

void piramide(int N) {
    int i, j, k, l;

    for (i = 1; i <= N; i++) {
        for (j = N; j > i; j--) {
            printf("  ");
        }
        for (k = 0; k <= i; k++) {
            printf("%d", k);
            if (k < i) printf(" ");
        }
        for (l = i - 1; l >= 1; l--) {
            printf("%d", l);
        }
        putchar('\n');
    }
}

int main() {
    int N;
    
    scanf("%d", &N);

    piramide(N);
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
  "source_sha256": "180a45aa2e31eb51982a6087161db06db533d2edb4bf75c65b0a62eb9ab83169",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    0 1\n  0 1 21\n0 1 2 321\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      0 1\n    0 1 21\n  0 1 2 321\n0 1 2 3 4321\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              0 1\n            0 1 21\n          0 1 2 321\n        0 1 2 3 4321\n      0 1 2 3 4 54321\n    0 1 2 3 4 5 654321\n  0 1 2 3 4 5 6 7654321\n0 1 2 3 4 5 6 7 87654321\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_039 — train

```c

#include <stdio.h>

void piramide(int N){
    int lin, col, colneg, espaco;
    if (N < 2){
        printf("Digite um número maior que 2\n");
        return;
    }
    for (lin = 1; lin <= N; lin++){
        for (espaco = 1; espaco <= (2*(N - lin)); espaco++)
                printf(" ");
        for (col = 1; col <= lin; col++)
            printf("%d ", col);
        for (colneg = lin - 1; colneg >= 1; colneg--)
            printf("%d ", colneg);
        printf("\n");
    }
}

int main(){
    int N;

    printf("Digite um numero maior que 2\n");
    scanf("%d", &N);

    piramide(N);

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
  "source_sha256": "49abb705a1c77b4b83723b246cfb0ee4605bedf2654a50d16f0451e3fca0a11b",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "Digite um numero maior que 2\n    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "Digite um numero maior que 2\n      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "Digite um numero maior que 2\n              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_040 — train

```c

#include <stdio.h>

void piramide(int N);


int main()
{
    int N;

    scanf("%d", &N);

    piramide(N);

    return 0;
}

void piramide(int N)
{
    int l, c, number;

    for(l = 0; l < N ; l++)
    {
        number = 1;
        for(c = 1; c <= N + l; c++)
        {
            if(c >= N)
                printf("%d", number--);
            else if (c >= N - l)
                printf("%d", number++);
            else 
                printf(" ");
        }
        printf("\n");
    }
}
```

```json
{
  "sample_id": "sample_040",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "175254b2a8ca59c4ac1133ebcd1635a3a5e94773872d14b753e71b5f31e3827d",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "  1\n 121\n12321\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "   1\n  121\n 12321\n1234321\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "       1\n      121\n     12321\n    1234321\n   123454321\n  12345654321\n 1234567654321\n123456787654321\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_042 — validation

```c


#include <stdio.h>

void piramide(int n) {
    int i, a, b, espacos;
    
    if (n <= 1) return;

    for (i = 1; i <= n; i++) {
        for (espacos = n - i; espacos > 0; espacos--){
            printf(" ");
        }
        for (a = 1; a <= i; a++) {
            printf("%d", a);
        }
        for (b = i -1; b >= 1; b--) {
            printf("%d", b);
        }
        printf("\n");
    }
}

int main() {
    int n;

    scanf("%d", &n);
    piramide(n);
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
  "source_sha256": "26aac60f22e3ec1229f7c345225faa7025836b3da1787f7fdd5186dca836dfe1",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "  1\n 121\n12321\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "   1\n  121\n 12321\n1234321\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "       1\n      121\n     12321\n    1234321\n   123454321\n  12345654321\n 1234567654321\n123456787654321\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_043 — train

```c

#include <stdio.h>

void piramide(int N){
    int linha,coluna,numero=1;
    for (linha=0; linha<N; linha++){
        for (coluna=0; coluna<=N-linha; coluna++){
            printf(" ");
        }
        for (coluna= 1;coluna<=linha;coluna++){
            printf("%d",numero);
            numero++;
        }

        for (coluna=linha-1;coluna>=1;coluna--){ 
        
            printf("%d",numero);
            numero--;
        }
        }
        printf("\n");
    }

int main(){
    int N;
    scanf("%d",&N);
    piramide(N);
    return 0;
}

```

```json
{
  "sample_id": "sample_043",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "95477b466b7b6a4edbcfee26b1a221caf31a92a5bc9e49219d1f4466777a5372",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "       1  234\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "         1   234  34565\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "                 1       234      34565     4567876    5678910987   6789101112111098  7891011121314131211109\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "large",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "large",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_044 — train

```c

#include <stdio.h>

void piramide(int N){
    int linha,coluna,numero=1;
    for (linha=1; linha<=N; linha++){
        for (coluna=0; coluna<N-linha; coluna++){
            putchar(' ');
        }
        for (coluna=0; coluna<linha; coluna++){
            printf("%d",numero);
            numero++;
            if (coluna<linha-1){
                putchar(' ');
            }
        }
        printf("\n");
    }
}
int main(){
    int N;
    scanf("%d",&N);
    piramide(N);
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
  "source_sha256": "f643c192eb92c89eeab3d4ab427f19e8e921e1cd139822a171c2257e2303b876",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "  1\n 2 3\n4 5 6\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "   1\n  2 3\n 4 5 6\n7 8 9 10\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "       1\n      2 3\n     4 5 6\n    7 8 9 10\n   11 12 13 14 15\n  16 17 18 19 20 21\n 22 23 24 25 26 27 28\n29 30 31 32 33 34 35 36\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "large",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "large",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_045 — train

```c

#include <stdio.h>

void piramide(int N);

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
    return 0;
}

void piramide(int N) {
    int i = 0, e = 1, num = 1;
    while(i < N) {
        if(e==1 && i != 2*N-i) {
            printf("  ");
            ++e;
        }
        while(e < N-i) {
            printf("  ");
            ++e;
        }
        while(N-i <= e && e <= N) {
            printf("%2d", num);
            ++num;
            ++e;
        }
        num = num - 2;
        while(N < e && e < N+i) {
            printf("%2d", num);
            --num;
            ++e;
        }
        if(e == N+i) {
            (i == N-i) ? printf("%d\n", num) : printf("%2d", num);
            ++e;
        }
        while(N+i < e && e < 2*N-1) {
            printf("  ");
            ++e;
        }
        if(e == 2*N-1)
            printf("  \n");
        e = 1;
        num = 1;
        ++i;
    }
}
```

```json
{
  "sample_id": "sample_045",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "afcec2c06225acec5da0d9a8f775b603a2e400761b964130bdd8552f0d5cdeae",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "     1    \n   1 2 1  \n   1 2 1 0"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1      \n     1 2 1    \n   1 2 3 21\n  \n   1 2 3 2 1 0"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1              \n             1 2 1            \n           1 2 3 2 1          \n         1 2 3 4 3 2 1        \n       1 2 3 4 5 4 3 21\n      \n     1 2 3 4 5 6 5 4 3 2 1    \n   1 2 3 4 5 6 7 6 5 4 3 2 1  \n   1 2 3 4 5 6 7 6 5 4 3 2 1 0"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "large",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_046 — train

```c

#include <stdio.h>

void piramide(int N);

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
    return 0;
}

void piramide(int N) {
    int i = 0, e = 1, num = 1;
    while(i < N) {
        while(e < N-i) {
            printf("  ");
            ++e;
        }
        while(N-i <= e && e <= N) {
            printf("%2d", num);
            ++num;
            ++e;
        }
        num = num - 2;
        while(N < e && e < N+i) {
            printf("%2d", num);
            --num;
            ++e;
        }
        if(e == N+i) {
            (i == N-i) ? printf("%d\n", num) : printf("%2d", num);
            ++e;
        }
        while(N+i < e && e < 2*N-1) {
            printf("  ");
            ++e;
        }
        if(e == 2*N-1)
            printf(" \n");
        e = 1;
        num = 1;
        ++i;
    }
}
```

```json
{
  "sample_id": "sample_046",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "bd270d5fa9bb9400b99278987aa1aac73e01d75d2767a6a247e085d9c07008e7",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "     1   \n   1 2 1 \n 1 2 3 2 1"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1     \n     1 2 1   \n   1 2 3 21\n \n 1 2 3 4 3 2 1"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1             \n             1 2 1           \n           1 2 3 2 1         \n         1 2 3 4 3 2 1       \n       1 2 3 4 5 4 3 21\n     \n     1 2 3 4 5 6 5 4 3 2 1   \n   1 2 3 4 5 6 7 6 5 4 3 2 1 \n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_047 — train

```c

#include <stdio.h>

void piramide(int N);

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
    return 0;
}

void piramide(int N) {
    int i = 0, e = 1, num = 1;
    while(i < N) {
        while(e < N-i) {
            printf("  ");
            ++e;
        }
        while(N-i <= e && e <= N) {
            printf("%2d", num);
            ++num;
            ++e;
        }
        num = num - 2;
        while(N < e && e < N+i) {
            printf("%2d", num);
            --num;
            ++e;
        }
        if(e == N+i) {
            (i == N-i) ? printf("%d\n", num) : printf("%2d", num);
            ++e;
        }
        while(N+i < e && e < 2*N-1) {
            printf("  ");
            ++e;
        }
        if(e == 2*N-1)
            printf("  \n");
        e = 1;
        num = 1;
        ++i;
    }
}
```

```json
{
  "sample_id": "sample_047",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "1b16e9ceb692a9274e28364e5ea4edd41a923a0972c9844ab440fbb463912f74",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "     1    \n   1 2 1  \n 1 2 3 2 1"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1      \n     1 2 1    \n   1 2 3 21\n  \n 1 2 3 4 3 2 1"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1              \n             1 2 1            \n           1 2 3 2 1          \n         1 2 3 4 3 2 1        \n       1 2 3 4 5 4 3 21\n      \n     1 2 3 4 5 6 5 4 3 2 1    \n   1 2 3 4 5 6 7 6 5 4 3 2 1  \n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_048 — train

```c

#include <stdio.h>

void piramide(int N);

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
    return 0;
}

void piramide(int N) {
    int i = 0, e = 1, num = 1;
    while(i < N) {
        while(e < N-i) {
            printf(" ");
            ++e;
        }
        while(N-i <= e && e <= N) {
            printf("%d", num);
            ++num;
            ++e;
        }
        num = num - 2;
        while(N < e && e <= N+i) {
            (i == N-1) ? printf("%d\n", num) : printf("%d", num);
            --num;
            ++e;
        }
        while(N+i < e && e < 2*N-1) {
            printf(" ");
            ++e;
        }
        if(e == 2*N-1)
            printf(" \n");
        e = 1;
        num = 1;
        ++i;
    }
}
```

```json
{
  "sample_id": "sample_048",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "7ba6ef0723bb2629acb44ffc0543b79c673584aadddb65f93dc878c0c3e1179f",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "  1  \n 121 \n1232\n1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "   1   \n  121  \n 12321 \n12343\n2\n1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "       1       \n      121      \n     12321     \n    1234321    \n   123454321   \n  12345654321  \n 1234567654321 \n123456787\n6\n5\n4\n3\n2\n1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "large",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_049 — train

```c

#include <stdio.h>

void piramide(int N);

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
    return 0;
}

void piramide(int N) {
    int i = 0, e = 1, num = 1;
    while(i < N) {
        while(e < N-i) {
            printf("  ");
            ++e;
        }
        while(N-i <= e && e <= N) {
            printf("%2d", num);
            ++num;
            ++e;
        }
        num = num - 2;
        while(N < e && e < N+i) {
            printf("%2d", num);
            --num;
            ++e;
        }
        if(e == N+i) {
            (i == N-i) ? printf("%d\n", num) : printf("%2d", num);
            ++e;
        }
        while(N+i < e && e < 2*N-1) {
            printf("  ");
            ++e;
        }
        if(e == 2*N-1)
            printf(" \n");
        e = 1;
        num = 1;
        ++i;
    }
}
```

```json
{
  "sample_id": "sample_049",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "bd270d5fa9bb9400b99278987aa1aac73e01d75d2767a6a247e085d9c07008e7",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "     1   \n   1 2 1 \n 1 2 3 2 1"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1     \n     1 2 1   \n   1 2 3 21\n \n 1 2 3 4 3 2 1"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1             \n             1 2 1           \n           1 2 3 2 1         \n         1 2 3 4 3 2 1       \n       1 2 3 4 5 4 3 21\n     \n     1 2 3 4 5 6 5 4 3 2 1   \n   1 2 3 4 5 6 7 6 5 4 3 2 1 \n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_050 — train

```c

#include <stdio.h>

void piramide(int N);

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
    return 0;
}

void piramide(int N) {
    int i = 0, e = 1, num = 1;
    while(i < N) {
        if(e == 1 && i != 2*N-1) {
            printf(" ");
            ++e;
        }
        while(e < N-i) {
            printf("  ");
            ++e;
        }
        while(N-i <= e && e <= N) {
            (e == 1) ? printf("%d", num) : printf("%2d", num);
            ++num;
            ++e;
        }
        num = num - 2;
        while(N < e && e < N+i) {
            printf("%2d", num);
            --num;
            ++e;
        }
        if(e == N+i) {
            (i == N-i) ? printf("%d\n", num) : printf("%2d", num);
            ++e;
        }
        while(N+i < e && e < 2*N-1) {
            printf("  ");
            ++e;
        }
        if(e == 2*N-1)
            printf("  \n");
        e = 1;
        num = 1;
        ++i;
    }
}
```

```json
{
  "sample_id": "sample_050",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "071b47f44043f84e3d8d2799336b740fd182bf37e84b99cca46768162359f6eb",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1    \n  1 2 1  \n  1 2 1 0"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1      \n    1 2 1    \n  1 2 3 21\n  \n  1 2 3 2 1 0"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1              \n            1 2 1            \n          1 2 3 2 1          \n        1 2 3 4 3 2 1        \n      1 2 3 4 5 4 3 21\n      \n    1 2 3 4 5 6 5 4 3 2 1    \n  1 2 3 4 5 6 7 6 5 4 3 2 1  \n  1 2 3 4 5 6 7 6 5 4 3 2 1 0"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_051 — train

```c

#include <stdio.h>

void piramide(int N);

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
    return 0;
}

void piramide(int N) {
    int i = 0, e = 1, num = 1;
    while(i < N) {
        while(e < N-i) {
            printf("  ");
            ++e;
        }
        while(N-i <= e && e <= N) {
            printf("%2d", num);
            ++num;
            ++e;
        }
        num = num - 2;
        while(N < e && e < N+i) {
            printf("%2d", num);
            --num;
            ++e;
        }
        if(e == N+i) {
            (i == N-i) ? printf("%d\n", num) : printf("%2d", num);
            ++e;
        }
        while(N+i < e && e < 2*N-1) {
            printf("  ");
            ++e;
        }
        if(e == 2*N-1)
            printf("  \n");
        e = 1;
        num = 1;
        ++i;
    }
}
```

```json
{
  "sample_id": "sample_051",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "1b16e9ceb692a9274e28364e5ea4edd41a923a0972c9844ab440fbb463912f74",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "     1    \n   1 2 1  \n 1 2 3 2 1"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1      \n     1 2 1    \n   1 2 3 21\n  \n 1 2 3 4 3 2 1"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1              \n             1 2 1            \n           1 2 3 2 1          \n         1 2 3 4 3 2 1        \n       1 2 3 4 5 4 3 21\n      \n     1 2 3 4 5 6 5 4 3 2 1    \n   1 2 3 4 5 6 7 6 5 4 3 2 1  \n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_052 — train

```c

#include <stdio.h>

void piramide(int N);

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
    return 0;
}

void piramide(int N) {
    int i = 0, e = 1, num = 1;
    while(i < N) {
        while(e < N-i) {
            (e == 1) ? printf(" ") : printf("  ");
            ++e;
        }
        while(N-i <= e && e <= N) {
            (e == 1) ? printf("%d", num) : printf("%2d", num);
            ++num;
            ++e;
        }
        num = num - 2;
        while(N < e && e < N+i) {
            printf("%2d", num);
            --num;
            ++e;
        }
        if(e == N+i) {
            (i == N-i) ? printf("%d\n", num) : printf("%2d", num);
            ++e;
        }
        while(N+i < e && e < 2*N-1) {
            printf("  ");
            ++e;
        }
        if(e == 2*N-1)
            printf("  \n");
        e = 1;
        num = 1;
        ++i;
    }
}
```

```json
{
  "sample_id": "sample_052",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "ddb7672ccd5fdc693aa7e2d0f07c76f19e49a2bfde4c5410a2d60e55deac2da4",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1    \n  1 2 1  \n1 2 3 2 1"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1      \n    1 2 1    \n  1 2 3 21\n  \n1 2 3 4 3 2 1"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1              \n            1 2 1            \n          1 2 3 2 1          \n        1 2 3 4 3 2 1        \n      1 2 3 4 5 4 3 21\n      \n    1 2 3 4 5 6 5 4 3 2 1    \n  1 2 3 4 5 6 7 6 5 4 3 2 1  \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_053 — train

```c

#include <stdio.h>

void piramide(int N);

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
    return 0;
}

void piramide(int N) {
    int i = 0, e = 1, num = 1;
    while(i < N) {
        if(e==1) {
            printf(" ");
            ++e;
        }
        while(e> 1 && e < N-i) {
            printf("  ");
            ++e;
        }
        while(N-i <= e && e <= N) {
            printf("%2d", num);
            ++num;
            ++e;
        }
        num = num - 2;
        while(N < e && e < N+i) {
            printf("%2d", num);
            --num;
            ++e;
        }
        if(e == N+i) {
            (i == N-i) ? printf("%d\n", num) : printf("%2d", num);
            ++e;
        }
        while(N+i < e && e < 2*N-1) {
            printf("  ");
            ++e;
        }
        if(e == 2*N-1)
            printf("  \n");
        e = 1;
        num = 1;
        ++i;
    }
}
```

```json
{
  "sample_id": "sample_053",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "cbf10b6eb7d00edb5ff4214b4e20b95a5f35b0c7c4f8276b4a214aaf46e79e00",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1    \n  1 2 1  \n  1 2 1 0"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1      \n    1 2 1    \n  1 2 3 21\n  \n  1 2 3 2 1 0"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1              \n            1 2 1            \n          1 2 3 2 1          \n        1 2 3 4 3 2 1        \n      1 2 3 4 5 4 3 21\n      \n    1 2 3 4 5 6 5 4 3 2 1    \n  1 2 3 4 5 6 7 6 5 4 3 2 1  \n  1 2 3 4 5 6 7 6 5 4 3 2 1 0"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_054 — train

```c

#include <stdio.h>

void piramide(int N);

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
    return 0;
}

void piramide(int N) {
    int i = 0, e = 1, num = 1;
    while(i < N) {
        if(e==1 && i != 2*N-i) {
            printf(" ");
            ++e;
        }
        while(e > 1 && e < N-i) {
            printf("  ");
            ++e;
        }
        while(N-i <= e && e <= N) {
            printf("%2d", num);
            ++num;
            ++e;
        }
        num = num - 2;
        while(N < e && e < N+i) {
            printf("%2d", num);
            --num;
            ++e;
        }
        if(e == N+i) {
            (i == N-i) ? printf("%d\n", num) : printf("%2d", num);
            ++e;
        }
        while(N+i < e && e < 2*N-1) {
            printf("  ");
            ++e;
        }
        if(e == 2*N-1)
            printf("  \n");
        e = 1;
        num = 1;
        ++i;
    }
}
```

```json
{
  "sample_id": "sample_054",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "635e43f038d7cf6e4b658571566777d8b3b7a45ed12bb06846d066d472627a84",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1    \n  1 2 1  \n  1 2 1 0"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1      \n    1 2 1    \n  1 2 3 21\n  \n  1 2 3 2 1 0"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1              \n            1 2 1            \n          1 2 3 2 1          \n        1 2 3 4 3 2 1        \n      1 2 3 4 5 4 3 21\n      \n    1 2 3 4 5 6 5 4 3 2 1    \n  1 2 3 4 5 6 7 6 5 4 3 2 1  \n  1 2 3 4 5 6 7 6 5 4 3 2 1 0"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_055 — train

```c

#include <stdio.h>

void piramide(int N);

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
    return 0;
}

void piramide(int N) {
    int i = 0, e = 1, num = 1;
    while(i < N) {
        while(e < N-i) {
            printf("  ");
            ++e;
        }
        while(N-i <= e && e <= N) {
            (e == 1) ? printf("%d", num) : printf("%2d", num);
            ++num;
            ++e;
        }
        num = num - 2;
        while(N < e && e < N+i) {
            printf("%2d", num);
            --num;
            ++e;
        }
        if(e == N+i) {
            (i == N-i) ? printf("%d\n", num) : printf("%2d", num);
            ++e;
        }
        while(N+i < e && e < 2*N-1) {
            printf("  ");
            ++e;
        }
        if(e == 2*N-1)
            printf("  \n");
        e = 1;
        num = 1;
        ++i;
    }
}
```

```json
{
  "sample_id": "sample_055",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "356dc4ed476ed11daf4a6315e5d3f3d02d13b7416482ce5895964edd1f1b18a1",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "     1    \n   1 2 1  \n1 2 3 2 1"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1      \n     1 2 1    \n   1 2 3 21\n  \n1 2 3 4 3 2 1"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1              \n             1 2 1            \n           1 2 3 2 1          \n         1 2 3 4 3 2 1        \n       1 2 3 4 5 4 3 21\n      \n     1 2 3 4 5 6 5 4 3 2 1    \n   1 2 3 4 5 6 7 6 5 4 3 2 1  \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_056 — train

```c

#include <stdio.h>

void piramide(int N);

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
    return 0;
}

void piramide(int N) {
    int i = 0, e = 1, num = 1;
    while(i < N) {
        while(e < N-i) {
            printf(" ");
            ++e;
        }
        while(N-i <= e && e <= N) {
            printf("%d", num);
            ++num;
            ++e;
        }
        --num;
        while(N < e && e <= N+i) {
            (i == N-1) ? printf("%d\n", num) : printf("%d", num);
            --num;
            ++e;
        }
        while(N+i < e && e < 2*N-1) {
            printf(" ");
            ++e;
        }
        if(e == 2*N-1)
            printf(" \n");
        e = 1;
        num = 1;
        ++i;
    }
}
```

```json
{
  "sample_id": "sample_056",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "76d859e74fa29a7f5e62516d1f382b1e8e5afa92761672ab3d53699d21e219e4",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "  1  \n 122 \n1233\n2\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "   1   \n  122  \n 12332 \n12344\n3\n2\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "       1       \n      122      \n     12332     \n    1234432    \n   123455432   \n  12345665432  \n 1234567765432 \n123456788\n7\n6\n5\n4\n3\n2\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "large",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "large",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_057 — train

```c

#include <stdio.h>

void piramide(int N);

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
    return 0;
}

void piramide(int N) {
    int i = 0, e = 1, num = 1;
    while(i < N) {
        while(e < N-i) {
            printf(" ");
            ++e;
        }
        while(N-i <= e && e <= N) {
            printf("%d", num);
            ++num;
            ++e;
        }
        num = num - 2;
        while(N < e && e < N+i) {
            printf("%d", num);
            --num;
            ++e;
        }
        if(e == N+i) {
            (i == N-i) ? printf("%d\n", num) : printf("%d", num);
            ++e;
        }
        while(N+i < e && e < 2*N-1) {
            printf(" ");
            ++e;
        }
        if(e == 2*N-1)
            printf(" \n");
        e = 1;
        num = 1;
        ++i;
    }
}
```

```json
{
  "sample_id": "sample_057",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "8614b934430485a3a6b633c9b860e336fbbe21c24119d0f5cf65f9214e65f1fa",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "  1  \n 121 \n12321"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "   1   \n  121  \n 12321\n \n1234321"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "       1       \n      121      \n     12321     \n    1234321    \n   123454321\n   \n  12345654321  \n 1234567654321 \n123456787654321"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "large",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "large",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_058 — train

```c

#include <stdio.h>

void piramide(int N);

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
    return 0;
}

void piramide(int N) {
    int i = 0, e = 1, num = 1;
    while(i < N) {
        while(e < N-i) {
            (e == 1) ? printf("%c", ' ') : printf("%2c", ' ');
            ++e;
        }
        while(N-i <= e && e <= N) {
            (e == 1) ? printf("%d", num) : printf("%2d", num);
            ++num;
            ++e;
        }
        num = num - 2;
        while(N < e && e < N+i) {
            printf("%2d", num);
            --num;
            ++e;
        }
        if(e == N+i) {
            (i == N-i) ? printf("%d\n", num) : printf("%2d", num);
            ++e;
        }
        while(N+i < e && e < 2*N-1) {
            printf("%2c", ' ');
            ++e;
        }
        if(e == 2*N-1)
            printf("%2c\n", ' ');
        e = 1;
        num = 1;
        ++i;
    }
}
```

```json
{
  "sample_id": "sample_058",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "1fb0942f3fd66a9f5bbc25c32724f943c219aa08c767e12fb68485626442f486",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1    \n  1 2 1  \n1 2 3 2 1"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1      \n    1 2 1    \n  1 2 3 21\n  \n1 2 3 4 3 2 1"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1              \n            1 2 1            \n          1 2 3 2 1          \n        1 2 3 4 3 2 1        \n      1 2 3 4 5 4 3 21\n      \n    1 2 3 4 5 6 5 4 3 2 1    \n  1 2 3 4 5 6 7 6 5 4 3 2 1  \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_059 — train

```c

#include <stdio.h>

void piramide(int n){
    int i, j, s;
    for(i = 1; i <= n; i++){
        for(s = 0; s < n - i; s++){
            printf(" ");
        }
        for(j = 1; j <= i ; j++){
            printf("%d", j);
        }
        for(j = i - 1; j >=1 ; j--){
            printf("%d", j);
        }
        printf("\n");
    }
}

int main(){
    int n;
    scanf("%d", &n);
    piramide(n);
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
  "source_sha256": "94e4bf19f9d9b2ec65d044d68c0966e84bcaf7ddc61a9bd6ee7b2d1b3e98b393",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "  1\n 121\n12321\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "   1\n  121\n 12321\n1234321\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "       1\n      121\n     12321\n    1234321\n   123454321\n  12345654321\n 1234567654321\n123456787654321\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## Evidence refs hợp lệ

```json
[
  "test_statistics",
  "feature_statistics",
  "learned_if_then_rules",
  "semantic_findings",
  "problem_statement",
  "members/sample_001/raw_code",
  "members/sample_001/tests/ex02_0",
  "members/sample_001/tests/ex02_1",
  "members/sample_001/tests/ex02_2",
  "members/sample_002/raw_code",
  "members/sample_002/tests/ex02_0",
  "members/sample_002/tests/ex02_1",
  "members/sample_002/tests/ex02_2",
  "members/sample_003/raw_code",
  "members/sample_003/tests/ex02_0",
  "members/sample_003/tests/ex02_1",
  "members/sample_003/tests/ex02_2",
  "members/sample_004/raw_code",
  "members/sample_004/tests/ex02_0",
  "members/sample_004/tests/ex02_1",
  "members/sample_004/tests/ex02_2",
  "members/sample_005/raw_code",
  "members/sample_005/tests/ex02_0",
  "members/sample_005/tests/ex02_1",
  "members/sample_005/tests/ex02_2",
  "members/sample_006/raw_code",
  "members/sample_006/tests/ex02_0",
  "members/sample_006/tests/ex02_1",
  "members/sample_006/tests/ex02_2",
  "members/sample_007/raw_code",
  "members/sample_007/tests/ex02_0",
  "members/sample_007/tests/ex02_1",
  "members/sample_007/tests/ex02_2",
  "members/sample_008/raw_code",
  "members/sample_008/tests/ex02_0",
  "members/sample_008/tests/ex02_1",
  "members/sample_008/tests/ex02_2",
  "members/sample_009/raw_code",
  "members/sample_009/tests/ex02_0",
  "members/sample_009/tests/ex02_1",
  "members/sample_009/tests/ex02_2",
  "members/sample_010/raw_code",
  "members/sample_010/tests/ex02_0",
  "members/sample_010/tests/ex02_1",
  "members/sample_010/tests/ex02_2",
  "members/sample_011/raw_code",
  "members/sample_011/tests/ex02_0",
  "members/sample_011/tests/ex02_1",
  "members/sample_011/tests/ex02_2",
  "members/sample_012/raw_code",
  "members/sample_012/tests/ex02_0",
  "members/sample_012/tests/ex02_1",
  "members/sample_012/tests/ex02_2",
  "members/sample_013/raw_code",
  "members/sample_013/tests/ex02_0",
  "members/sample_013/tests/ex02_1",
  "members/sample_013/tests/ex02_2",
  "members/sample_014/raw_code",
  "members/sample_014/tests/ex02_0",
  "members/sample_014/tests/ex02_1",
  "members/sample_014/tests/ex02_2",
  "members/sample_015/raw_code",
  "members/sample_015/tests/ex02_0",
  "members/sample_015/tests/ex02_1",
  "members/sample_015/tests/ex02_2",
  "members/sample_016/raw_code",
  "members/sample_016/tests/ex02_0",
  "members/sample_016/tests/ex02_1",
  "members/sample_016/tests/ex02_2",
  "members/sample_017/raw_code",
  "members/sample_017/tests/ex02_0",
  "members/sample_017/tests/ex02_1",
  "members/sample_017/tests/ex02_2",
  "members/sample_018/raw_code",
  "members/sample_018/tests/ex02_0",
  "members/sample_018/tests/ex02_1",
  "members/sample_018/tests/ex02_2",
  "members/sample_019/raw_code",
  "members/sample_019/tests/ex02_0",
  "members/sample_019/tests/ex02_1",
  "members/sample_019/tests/ex02_2",
  "members/sample_020/raw_code",
  "members/sample_020/tests/ex02_0",
  "members/sample_020/tests/ex02_1",
  "members/sample_020/tests/ex02_2",
  "members/sample_021/raw_code",
  "members/sample_021/tests/ex02_0",
  "members/sample_021/tests/ex02_1",
  "members/sample_021/tests/ex02_2",
  "members/sample_022/raw_code",
  "members/sample_022/tests/ex02_0",
  "members/sample_022/tests/ex02_1",
  "members/sample_022/tests/ex02_2",
  "members/sample_023/raw_code",
  "members/sample_023/tests/ex02_0",
  "members/sample_023/tests/ex02_1",
  "members/sample_023/tests/ex02_2",
  "members/sample_024/raw_code",
  "members/sample_024/tests/ex02_0",
  "members/sample_024/tests/ex02_1",
  "members/sample_024/tests/ex02_2",
  "members/sample_025/raw_code",
  "members/sample_025/tests/ex02_0",
  "members/sample_025/tests/ex02_1",
  "members/sample_025/tests/ex02_2",
  "members/sample_026/raw_code",
  "members/sample_026/tests/ex02_0",
  "members/sample_026/tests/ex02_1",
  "members/sample_026/tests/ex02_2",
  "members/sample_027/raw_code",
  "members/sample_027/tests/ex02_0",
  "members/sample_027/tests/ex02_1",
  "members/sample_027/tests/ex02_2",
  "members/sample_028/raw_code",
  "members/sample_028/tests/ex02_0",
  "members/sample_028/tests/ex02_1",
  "members/sample_028/tests/ex02_2",
  "members/sample_029/raw_code",
  "members/sample_029/tests/ex02_0",
  "members/sample_029/tests/ex02_1",
  "members/sample_029/tests/ex02_2",
  "members/sample_030/raw_code",
  "members/sample_030/tests/ex02_0",
  "members/sample_030/tests/ex02_1",
  "members/sample_030/tests/ex02_2",
  "members/sample_031/raw_code",
  "members/sample_031/tests/ex02_0",
  "members/sample_031/tests/ex02_1",
  "members/sample_031/tests/ex02_2",
  "members/sample_032/raw_code",
  "members/sample_032/tests/ex02_0",
  "members/sample_032/tests/ex02_1",
  "members/sample_032/tests/ex02_2",
  "members/sample_033/raw_code",
  "members/sample_033/tests/ex02_0",
  "members/sample_033/tests/ex02_1",
  "members/sample_033/tests/ex02_2",
  "members/sample_034/raw_code",
  "members/sample_034/tests/ex02_0",
  "members/sample_034/tests/ex02_1",
  "members/sample_034/tests/ex02_2",
  "members/sample_035/raw_code",
  "members/sample_035/tests/ex02_0",
  "members/sample_035/tests/ex02_1",
  "members/sample_035/tests/ex02_2",
  "members/sample_036/raw_code",
  "members/sample_036/tests/ex02_0",
  "members/sample_036/tests/ex02_1",
  "members/sample_036/tests/ex02_2",
  "members/sample_037/raw_code",
  "members/sample_037/tests/ex02_0",
  "members/sample_037/tests/ex02_1",
  "members/sample_037/tests/ex02_2",
  "members/sample_038/raw_code",
  "members/sample_038/tests/ex02_0",
  "members/sample_038/tests/ex02_1",
  "members/sample_038/tests/ex02_2",
  "members/sample_039/raw_code",
  "members/sample_039/tests/ex02_0",
  "members/sample_039/tests/ex02_1",
  "members/sample_039/tests/ex02_2",
  "members/sample_040/raw_code",
  "members/sample_040/tests/ex02_0",
  "members/sample_040/tests/ex02_1",
  "members/sample_040/tests/ex02_2",
  "members/sample_041/raw_code",
  "members/sample_041/tests/ex02_0",
  "members/sample_041/tests/ex02_1",
  "members/sample_041/tests/ex02_2",
  "members/sample_042/raw_code",
  "members/sample_042/tests/ex02_0",
  "members/sample_042/tests/ex02_1",
  "members/sample_042/tests/ex02_2",
  "members/sample_043/raw_code",
  "members/sample_043/tests/ex02_0",
  "members/sample_043/tests/ex02_1",
  "members/sample_043/tests/ex02_2",
  "members/sample_044/raw_code",
  "members/sample_044/tests/ex02_0",
  "members/sample_044/tests/ex02_1",
  "members/sample_044/tests/ex02_2",
  "members/sample_045/raw_code",
  "members/sample_045/tests/ex02_0",
  "members/sample_045/tests/ex02_1",
  "members/sample_045/tests/ex02_2",
  "members/sample_046/raw_code",
  "members/sample_046/tests/ex02_0",
  "members/sample_046/tests/ex02_1",
  "members/sample_046/tests/ex02_2",
  "members/sample_047/raw_code",
  "members/sample_047/tests/ex02_0",
  "members/sample_047/tests/ex02_1",
  "members/sample_047/tests/ex02_2",
  "members/sample_048/raw_code",
  "members/sample_048/tests/ex02_0",
  "members/sample_048/tests/ex02_1",
  "members/sample_048/tests/ex02_2",
  "members/sample_049/raw_code",
  "members/sample_049/tests/ex02_0",
  "members/sample_049/tests/ex02_1",
  "members/sample_049/tests/ex02_2",
  "members/sample_050/raw_code",
  "members/sample_050/tests/ex02_0",
  "members/sample_050/tests/ex02_1",
  "members/sample_050/tests/ex02_2",
  "members/sample_051/raw_code",
  "members/sample_051/tests/ex02_0",
  "members/sample_051/tests/ex02_1",
  "members/sample_051/tests/ex02_2",
  "members/sample_052/raw_code",
  "members/sample_052/tests/ex02_0",
  "members/sample_052/tests/ex02_1",
  "members/sample_052/tests/ex02_2",
  "members/sample_053/raw_code",
  "members/sample_053/tests/ex02_0",
  "members/sample_053/tests/ex02_1",
  "members/sample_053/tests/ex02_2",
  "members/sample_054/raw_code",
  "members/sample_054/tests/ex02_0",
  "members/sample_054/tests/ex02_1",
  "members/sample_054/tests/ex02_2",
  "members/sample_055/raw_code",
  "members/sample_055/tests/ex02_0",
  "members/sample_055/tests/ex02_1",
  "members/sample_055/tests/ex02_2",
  "members/sample_056/raw_code",
  "members/sample_056/tests/ex02_0",
  "members/sample_056/tests/ex02_1",
  "members/sample_056/tests/ex02_2",
  "members/sample_057/raw_code",
  "members/sample_057/tests/ex02_0",
  "members/sample_057/tests/ex02_1",
  "members/sample_057/tests/ex02_2",
  "members/sample_058/raw_code",
  "members/sample_058/tests/ex02_0",
  "members/sample_058/tests/ex02_1",
  "members/sample_058/tests/ex02_2",
  "members/sample_059/raw_code",
  "members/sample_059/tests/ex02_0",
  "members/sample_059/tests/ex02_1",
  "members/sample_059/tests/ex02_2"
]
```
