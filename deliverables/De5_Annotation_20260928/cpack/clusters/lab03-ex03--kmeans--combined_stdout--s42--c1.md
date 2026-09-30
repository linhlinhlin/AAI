# lab03-ex03--kmeans--combined_stdout--s42--c1

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 52; phân vùng: {'validation': 15, 'train': 37}.


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
    "test_id": "ex03_0",
    "n_cluster": 52,
    "n_observed": 52,
    "n_failed": 52,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 52
    }
  },
  {
    "test_id": "ex03_2",
    "n_cluster": 52,
    "n_observed": 52,
    "n_failed": 52,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 52
    }
  },
  {
    "test_id": "ex03_1",
    "n_cluster": 52,
    "n_observed": 52,
    "n_failed": 51,
    "n_not_run": 0,
    "failure_rate_observed": 0.9807692307692307,
    "failure_rate_cluster": 0.9807692307692307,
    "outcome_counts": {
      "pass": 1,
      "fail": 51
    }
  },
  {
    "test_id": "ex03_3",
    "n_cluster": 52,
    "n_observed": 52,
    "n_failed": 51,
    "n_not_run": 0,
    "failure_rate_observed": 0.9807692307692307,
    "failure_rate_cluster": 0.9807692307692307,
    "outcome_counts": {
      "pass": 1,
      "fail": 51
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex03_0:relation",
    "value": "different",
    "n": 52,
    "n_cluster": 52,
    "rate": 1.0,
    "cohort_rate": 0.4409448818897638,
    "difference_from_cohort": 0.5590551181102362
  },
  {
    "feature": "stdout:ex03_2:relation",
    "value": "different",
    "n": 52,
    "n_cluster": 52,
    "rate": 1.0,
    "cohort_rate": 0.4409448818897638,
    "difference_from_cohort": 0.5590551181102362
  },
  {
    "feature": "stdout:ex03_1:relation",
    "value": "different",
    "n": 51,
    "n_cluster": 52,
    "rate": 0.9807692307692307,
    "cohort_rate": 0.4409448818897638,
    "difference_from_cohort": 0.539824348879467
  },
  {
    "feature": "stdout:ex03_3:relation",
    "value": "different",
    "n": 51,
    "n_cluster": 52,
    "rate": 0.9807692307692307,
    "cohort_rate": 0.4409448818897638,
    "difference_from_cohort": 0.539824348879467
  },
  {
    "feature": "stdout:ex03_0:edit_band",
    "value": "medium",
    "n": 49,
    "n_cluster": 52,
    "rate": 0.9423076923076923,
    "cohort_rate": 0.4094488188976378,
    "difference_from_cohort": 0.5328588734100546
  },
  {
    "feature": "stdout:ex03_1:edit_band",
    "value": "medium",
    "n": 48,
    "n_cluster": 52,
    "rate": 0.9230769230769231,
    "cohort_rate": 0.3937007874015748,
    "difference_from_cohort": 0.5293761356753484
  },
  {
    "feature": "stdout:ex03_2:edit_band",
    "value": "medium",
    "n": 46,
    "n_cluster": 52,
    "rate": 0.8846153846153846,
    "cohort_rate": 0.3779527559055118,
    "difference_from_cohort": 0.5066626287098728
  },
  {
    "feature": "stdout:ex03_3:edit_band",
    "value": "medium",
    "n": 42,
    "n_cluster": 52,
    "rate": 0.8076923076923077,
    "cohort_rate": 0.33070866141732286,
    "difference_from_cohort": 0.47698364627498485
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 29,
    "n_cluster": 52,
    "rate": 0.5576923076923077,
    "cohort_rate": 0.4566929133858268,
    "difference_from_cohort": 0.10099939430648092
  },
  {
    "feature": "ast:c_while",
    "value": "1",
    "n": 14,
    "n_cluster": 52,
    "rate": 0.2692307692307692,
    "cohort_rate": 0.1968503937007874,
    "difference_from_cohort": 0.0723803755299818
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 34,
    "n_cluster": 52,
    "rate": 0.6538461538461539,
    "cohort_rate": 0.6299212598425197,
    "difference_from_cohort": 0.02392489400363418
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 52,
    "n_cluster": 52,
    "rate": 1.0,
    "cohort_rate": 0.9763779527559056,
    "difference_from_cohort": 0.023622047244094446
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 47,
    "n_cluster": 52,
    "rate": 0.9038461538461539,
    "cohort_rate": 0.8818897637795275,
    "difference_from_cohort": 0.021956390066626308
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 50,
    "n_cluster": 52,
    "rate": 0.9615384615384616,
    "cohort_rate": 0.9448818897637795,
    "difference_from_cohort": 0.01665657177468205
  },
  {
    "feature": "stdout:ex03_1:edit_band",
    "value": "__unknown__",
    "n": 1,
    "n_cluster": 52,
    "rate": 0.019230769230769232,
    "cohort_rate": 0.007874015748031496,
    "difference_from_cohort": 0.011356753482737736
  },
  {
    "feature": "stdout:ex03_1:relation",
    "value": "__unknown__",
    "n": 1,
    "n_cluster": 52,
    "rate": 0.019230769230769232,
    "cohort_rate": 0.007874015748031496,
    "difference_from_cohort": 0.011356753482737736
  },
  {
    "feature": "test:ex03_1",
    "value": "pass",
    "n": 1,
    "n_cluster": 52,
    "rate": 0.019230769230769232,
    "cohort_rate": 0.007874015748031496,
    "difference_from_cohort": 0.011356753482737736
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 49,
    "n_cluster": 52,
    "rate": 0.9423076923076923,
    "cohort_rate": 0.937007874015748,
    "difference_from_cohort": 0.005299818291944258
  },
  {
    "feature": "stdout:ex03_3:edit_band",
    "value": "__unknown__",
    "n": 1,
    "n_cluster": 52,
    "rate": 0.019230769230769232,
    "cohort_rate": 0.015748031496062992,
    "difference_from_cohort": 0.00348273773470624
  },
  {
    "feature": "stdout:ex03_3:relation",
    "value": "__unknown__",
    "n": 1,
    "n_cluster": 52,
    "rate": 0.019230769230769232,
    "cohort_rate": 0.015748031496062992,
    "difference_from_cohort": 0.00348273773470624
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 29,
    "n_cluster": 52,
    "rate": 0.5576923076923077,
    "cohort_rate": 0.4566929133858268,
    "difference_from_cohort": 0.10099939430648092
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 34,
    "n_cluster": 52,
    "rate": 0.6538461538461539,
    "cohort_rate": 0.6299212598425197,
    "difference_from_cohort": 0.02392489400363418
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 52,
    "n_cluster": 52,
    "rate": 1.0,
    "cohort_rate": 0.9763779527559056,
    "difference_from_cohort": 0.023622047244094446
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 47,
    "n_cluster": 52,
    "rate": 0.9038461538461539,
    "cohort_rate": 0.8818897637795275,
    "difference_from_cohort": 0.021956390066626308
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 50,
    "n_cluster": 52,
    "rate": 0.9615384615384616,
    "cohort_rate": 0.9448818897637795,
    "difference_from_cohort": 0.01665657177468205
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 49,
    "n_cluster": 52,
    "rate": 0.9423076923076923,
    "cohort_rate": 0.937007874015748,
    "difference_from_cohort": 0.005299818291944258
  },
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 52,
    "n_cluster": 52,
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
    "rule_id": 2,
    "if": [
      "NOT (stdout:ex03_0:relation=whitespace)",
      "NOT (stdout:ex03_0:edit_band=large)"
    ],
    "then_cluster": 1,
    "train_support": 37,
    "train_precision": 1.0,
    "holdout_support": 15,
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
  "reasoning": "Có 52 bài trong cụm. Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
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

sample_009, sample_001, sample_010, sample_006

## sample_001 — validation — đại diện

```c
#include <stdio.h>

void cruz(int N)
{
  int l = 1, i;
  while (l <= N / 2)   
  {
    for (i = l - 1; i > 0; i--)   
      printf("- ");
    printf("* ");
    for (i = N - 2*l; i > 0; i--)   
      printf("- ");
    if (l == 1)
      printf("*\n");
    else
    {
      printf("* ");
      for (i = l - 1; i > 1; i--)   
        printf("- ");
      printf("-\n");
    }
    ++l;
  }
  while (l <= N)   
  {
    for (i = N - l; i > 0; i--)   
      printf("- ");
    printf("* ");
    for (i = 2*(l - 1) - N; i > 0; i--)   
      printf("- ");
    if ((N % 2 == 0) || (l != N / 2 + 1)) {  
      if (l == N)
        printf("*\n");
      else
      {
        printf("* ");
        for (i = N - l; i > 1; i--)   
          printf("- ");
        printf("-\n");
      } }
    ++l;
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
  "sample_id": "sample_001",
  "partition": "validation",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "a9c40552fa283fd0e582cc7707ed4b8cfdfe3bf1fa5b9ca68e8ef705a1b8c406",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "pass",
    "ex03_2": "fail",
    "ex03_3": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "* - *\n- * * - *\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "* - - - *\n- * - * -\n- - * - * - * -\n* - - - *\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "pass",
    "test:ex03_2": "fail",
    "test:ex03_3": "pass",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "small",
    "stdout:ex03_1:relation": "__unknown__",
    "stdout:ex03_1:edit_band": "__unknown__",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "small",
    "stdout:ex03_3:relation": "__unknown__",
    "stdout:ex03_3:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "pass",
    "test:ex03_2": "fail",
    "test:ex03_3": "pass",
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


## sample_006 — train — đại diện

```c
#include <stdio.h>



void cruz(int N) {
  int i = 0, j = 0;
  while (i++ < N) {
    while (j++ < N) {
      if (j == i || j == N - i + 1)
        printf("*");
      else
        printf("-");
    }
    printf("\n");
    j = 0;
  }
}

int main() {
  int N;
  scanf("%d", &N);
  cruz(N);

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
  "source_sha256": "eb057a9c6f110ec8063006fdaa4b79d550a67b93ec3f1cb751e2149f0ed03831",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_009 — train — đại diện

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
  "representative": true,
  "is_train_medoid": true,
  "raw_code_truncated": false,
  "source_sha256": "c62650d0b01820f4eb7eb395aedf0a74344f1cdcc540e8b47dfc5e3f47108d73",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_010 — train — đại diện

```c
# include <stdio.h>

void cruz(int N){
    int largura=1,comprimento=1;
    while(comprimento<=N){
        while (largura<=N){
            if (largura==comprimento || largura==(N-comprimento)+1){
                printf("*");
            }
            else{
                printf("-");
            }
            largura+=1;
        }
        comprimento+=1;
        largura=1;
        printf("\n");
    }
}

int main(){
    int N;
    scanf("%d",&N);
    cruz(N);
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
  "source_sha256": "90e6ba0fd1e8fc7ff074914dd8f5a019405446d40cd32008eca43943e24b3e90",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_002 — train

```c
#include <stdio.h>

#define SIMBOLO '-'
#define SEPARADOR '*'
#define LINHA_INICIAL 1
#define COLUNA_INICIAL 1


void cruz(int n)
{
	int linha;
	int coluna;

	for (linha = LINHA_INICIAL; linha <= n; linha++) 
	{
		for (coluna = COLUNA_INICIAL; coluna <= n ; coluna++)
		{
			if (linha == coluna || (n-linha+1) == coluna ||  coluna-n+1 == linha || coluna-n+1 == linha-n+1) {			
				putchar(SEPARADOR);}
			else {
				putchar(SIMBOLO);}
		}
		putchar('\n');
	}
}

int main()
{
	int n;
	scanf("%d", &n);
	cruz(n);
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
  "source_sha256": "6e1afa112c169aa8626c28e36fc099643fa8c28ec57c8557d4b12bdc80ff7a74",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_003 — validation

```c
#include <stdio.h>

void cruz(int N)
{
	int col_prim_cruz, col_seg_cruz;
	int linha_n, col_n;

	col_prim_cruz = 1;
	col_seg_cruz = N;

	for (linha_n = 1; linha_n <= N; ++linha_n)
	{
		for(col_n = 1; col_n <= N; ++col_n)
		{
			if ((col_n == col_prim_cruz) || (col_n == col_seg_cruz))
				printf("*");
			else
				printf("-");
		}

		printf("\n");

		
		++col_prim_cruz;
		--col_seg_cruz;

	}


}

int main()
{
	int n;

	scanf("%d", &n);
	cruz(n);

	return 0;
}
```

```json
{
  "sample_id": "sample_003",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "1ecd6590a8211e16b1f5e6690f12c14035b51e7445a188dd3c01c871b2a2e6cd",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_004 — train

```c
#include <stdio.h>

#define asterisco '*'
#define hifen '-'

void cruz(int N) {
    int metade, contador, contador_colunas, pos_esq = 0, pos_dir = N - 1;

    metade = N / 2;


    for (contador = 0; contador < N; contador++) {
        for (contador_colunas = 0; contador_colunas < N; contador_colunas++) {
            if ((contador_colunas == pos_esq) || (contador_colunas == pos_dir)) {
                printf("%c", asterisco);
            } else {
                printf("%c", hifen);
            }
        }
        printf("\n");
        if (contador < metade) {
            pos_esq++;
            pos_dir--;
        }
        else {
            pos_esq--;
            pos_dir++;
        }
    }

}

int main() {
    int N;

    scanf("%d", &N);
    
    cruz(N);

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
  "source_sha256": "262b90f32c7813da7d1b6e3c93ac983d4058bc128d0c31c039d96ea9f24ae847",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n-**-\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n---**---\n--*--*--\n-*----*-\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_005 — train

```c
#include <stdio.h>

void cruz (int N)  {

 int i, j, cont = 1;

 for ( i = 1; i<= N ; i++)  {

  for (j = 1; j <= N ; j++)  {

   if ( j== N - cont + 1 || j == cont) {
     printf ( "*");  }

   else  {
    printf("-");  }}

  printf("\n");
  cont ++;
 }
} 
int main ()  {
 int N;
 scanf("%d", &N);
 cruz(N);
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
  "source_sha256": "9fc4716f01df291cf3aecaae0942cb0b37a0fd908a1400fe3a5dbcccce052e63",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_007 — validation

```c
#include <stdio.h>

void cruz(int n){
    int i = 1, j;
    while(i <= n){
        for(j = 1; j <=n; j++){
            if(j == i || j == (n + 1 - i))
                printf("* ");
            else
                printf("- ");
        }
        printf("\n");
        i++;
    }
    return;
}


int main(){
    int n;
    printf("Introduza um número.\n");
    scanf("%d", &n);
    cruz(n);
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
  "source_sha256": "ba177a958e299910b1d87920912cab6235ddf318d57309be4ee124e8fe80bb6e",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "Introduza um número.\n* - * \n- * - \n* - * \n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "Introduza um número.\n* - - * \n- * * - \n- * * - \n* - - * \n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "Introduza um número.\n* - - - * \n- * - * - \n- - * - - \n- * - * - \n* - - - * \n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "Introduza um número.\n* - - - - - - * \n- * - - - - * - \n- - * - - * - - \n- - - * * - - - \n- - - * * - - - \n- - * - - * - - \n- * - - - - * - \n* - - - - - - * \n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_008 — validation

```c
#include <stdio.h>

void cruz(int n){
    int i = 1, j;
    while(i <= n){
        for(j = 1; j <=n; j++){
            if(j == i || j == (n + 1 - i)){
                if(j == n)
                    printf("*");
                else
                    printf("* ");
            }

            else{
                if(j == n)
                    printf("-");
                else
                    printf("- ");
            }
        }
        printf("\n");
        i++;
    }
    return;
}


int main(){
    int n;
    printf("Introduza um número.\n");
    scanf("%d", &n);
    cruz(n);
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
  "source_sha256": "1486c638d7dc0fd8b0aeddfb4685bfcb57a06bcecabe7904d2a195e809a48d6a",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "Introduza um número.\n* - *\n- * -\n* - *\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "Introduza um número.\n* - - *\n- * * -\n- * * -\n* - - *\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "Introduza um número.\n* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "Introduza um número.\n* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_011 — train

```c

#include <stdio.h>

void cruz(int n);

int main() {

    int N;
    scanf("%d", &N);
    cruz(N);
    return 0;
}

void cruz(int n) {

    int i, j;

    for (j = 1; j <= n; j++) {
        for (i = 1; i <= n; i++) {
            if (i == j || i == n-j+1) {
                putchar('*');
            } else {
                putchar('-');
            }
        }
        putchar('\n');
    }

}

```

```json
{
  "sample_id": "sample_011",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "f150c984f7a8f79b473e8d7d4f826d70b80e3d636cab2807414ade23e70d957b",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_012 — train

```c

#include <stdio.h>

void cruz(int n);

int main() {

    int N;
    scanf("%d", &N);
    cruz(N);
    return 0;

}

void cruz(int n) {

    int i, j;

    for (j = 1; j <= n; j++) {
        for (i = 1; i <= n; i++) {
            if (i == j || i == n-j+1) {
                putchar('*');
            } else {
                putchar('-');
            }
        }
        putchar('\n');
    }
}

```

```json
{
  "sample_id": "sample_012",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "59af3f1f5ecefbee338cec1bf82cdb00a8270ec43cd1b03ac57333b8b4373473",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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

void cruz(int n);

int main() {

    int N;
    scanf("%d", &N);
    cruz(N);
    return 0;

}

void cruz(int n) {

    int i, j;

    for (j = 1; j <= n; j++) {
        for (i = 1; i <= n; i++) {
            if (i == j || i == n-j+1) {
                putchar('*');
            } else {
                putchar('-');
            }
        }
        putchar('\n');
    }
    
}

```

```json
{
  "sample_id": "sample_013",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "1177aae46e2a855e1518766f39168b9f2577e4b0a2e8095b0639fac9b6e5afb4",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_014 — validation

```c


#include <stdio.h>

void cruz(int);

int main(){
    int n;
    scanf("%d", &n);
    cruz(n);
    return 0;
}

void cruz(int n){
    int i, j;
    for (i = 1; n >= i; i++){
        for (j = 1; n >= j; j++){
            if (j == i)
                putchar('*');
            else if ( i + j - 1 == n)
                putchar('*');
            else
                putchar('-');
        }
        putchar('\n');
    }
}
```

```json
{
  "sample_id": "sample_014",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "6d6c846f172da45c7c4a4b8f519f7c05f12437cc553bb63970009599c460a98f",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_015 — train

```c

#include <stdio.h>

void cruz(int N){
    int a, b;
    for (a = 0; a < N; a++){
        for(b=0; b<N; b++){
            if (a==b || a+b == N-1)
                printf("*");
            else
                printf("-");
        }
        printf("\n"); 
    }

}

int main(){
    int N;
    scanf("%d", &N);
    cruz(N);
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
  "source_sha256": "6c96c914c469a23087a5afa39a933ee135d545472efba33bcb3ce804b3892156",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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

#include<stdio.h>

void cruz(int N){
    int i,j;
    for(i=0; i<N; i++){
        for(j=0; j<N; j++){
            (i==j || i == (N-1)-j) ? printf("*") : printf("-");
            if(j==N-1)
                printf("\n");
        }
    }
}

int main(){
    int N;
    scanf("%d",&N);
    cruz(N);
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
  "source_sha256": "a8983f5692908bf4bb1a6b9c7856fd7da48ec364159a0099ee06e413b42bb6e5",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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
#define minimo 2 
void cruz (int N ){
int l, c;

for (l=0 ; l<N ; l++){
    for (c=0 ; c<N ; c ++){
        if (l == c || (l+c)== N-1){
            putchar('*');
            
        }
        else {
            putchar('-');
           
        }
        
       
    }
    putchar('\n');
}
}

int main (){

int N;
scanf("%d", &N);
while ( N < minimo){
scanf("%d", &N);
}
cruz (N);

return 0 ;

}
```

```json
{
  "sample_id": "sample_017",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "0404927d6e5c5eb5bc59abf5c288d10fbc56f03b504902dd57bfbbeae307c3c0",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
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


## sample_018 — train

```c

#include <stdio.h>

void cruz(int N);


int main(){
    int N;
    scanf("%d", &N);
    cruz(N);
    return 0;
}

void cruz(int N){
    int i,j, minus, plus;
    minus = N;
    plus = 1;
    for (i = 0; i < N; i++){
        for (j = 1; j <= N; j++){
            if (j == plus || j == minus)
            putchar('*');
            else
            putchar('-');
        }
        plus++;
        minus -= 1;
        printf("\n");
    }
}
```

```json
{
  "sample_id": "sample_018",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "2a47820609e1d85eced6401217ccaa7d73630f64d43d9458c348f9ce01cb062c",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_019 — validation

```c


#include <stdio.h>

void printLine(int, int);
void cruz(int);

int main() {
    int N;
    scanf("%d", &N);
    cruz(N);
    return 0;
}

void printLine(int buffer, int lineSize) {
    int i, midBuffer = lineSize - buffer * 2 - 2;
    for (i = 0; i < buffer; i++)
        printf("-");
    printf("*");
    if (midBuffer < 0) {
        for (i = 0; i < buffer; i++)
            printf("-");
        return;
    }
    for (i = 0; i < midBuffer; i++)
        printf("-");
    printf("*");
    for (i = 0; i < buffer; i++)
        printf("-");
}

void cruz(int N) {
    int i;
    for (i = 0; i < ((N / 2) + (N % 2)); i++) {
        printLine(i, N);
        printf("\n");
    }
    for (i = (N / 2) - 1; i > 0; i--) {
        printLine(i, N);
        printf("\n");
    }
    printLine(i, N);
}

```

```json
{
  "sample_id": "sample_019",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "fb9aa580cb1c567558835f66815e46584682113f41865b39b5fd436cd0d58ead",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_020 — validation

```c


#include <stdio.h>

void printLine(int, int);
void cruz(int);

int main() {
    int N;
    scanf("%d", &N);
    cruz(N);
    return 0;
}

void printLine(int buffer, int lineSize) {
    int i, midBuffer = lineSize - buffer * 2 - 2;
    for (i = 0; i < buffer; i++)
        printf("-");
    printf("*");
    if (midBuffer < 0) {
        for (i = 0; i < buffer; i++)
            printf("-");
        printf("\n");
        return;
    }
    for (i = 0; i < midBuffer; i++)
        printf("-");
    printf("*");
    for (i = 0; i < buffer; i++)
        printf("-");
    printf("\n");
    return;
}

void cruz(int N) {
    int i;
    for (i = 0; i < ((N / 2) + (N % 2)); i++) {
        printLine(i, N);
    }
    for (i = (N / 2) - 1; i >= 0; i--) {
        printLine(i, N);
    }
    return;
}
```

```json
{
  "sample_id": "sample_020",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "2ab8d5df1c2f015bb1ad5c94995a0873f3c3f7344bdbe24eace78566ddead6ea",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_021 — validation

```c


#include <stdio.h>

void printLine(int, int);
void cruz(int);

int main() {
    int N;
    scanf("%d", &N);
    cruz(N);
    return 0;
}

void printLine(int buffer, int lineSize) {
    int i, midBuffer = lineSize - buffer * 2 - 2;
    for (i = 0; i < buffer; i++)
        printf("-");
    printf("*");
    if (midBuffer < 0) {
        for (i = 0; i < buffer; i++)
            printf("-");
        printf("\n");
        return;
    }
    for (i = 0; i < midBuffer; i++)
        printf("-");
    printf("*");
    for (i = 0; i < buffer; i++)
        printf("-");
    printf("\n");
    return;
}

void cruz(int N) {
    int i;
    for (i = 0; i < ((N / 2) + (N % 2)); i++) {
        printLine(i, N);
    }
    for (i = (N / 2) - 1; i >= 0; i--) {
        printLine(i, N);
    }
    return;
}

```

```json
{
  "sample_id": "sample_021",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "0cc7192ce2ddbbba5d0e9577145855e8828d2b12a7b24843bd3316259776e575",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_022 — validation

```c


#include <stdio.h>

void printLine(int, int);
void cruz(int);

int main() {
    int N;
    scanf("%d", &N);
    cruz(N);
    return 0;
}

void printLine(int buffer, int lineSize) {
    int i, midBuffer = lineSize - buffer * 2 - 2;
    for (i = 0; i < buffer; i++)
        printf("-");
    printf("*");
    if (midBuffer < 0) {
        for (i = 0; i < buffer; i++)
            printf("-");
        return;
    }
    for (i = 0; i < midBuffer; i++)
        printf("-");
    printf("*");
    for (i = 0; i < buffer; i++)
        printf("-");
}

void cruz(int N) {
    int i;
    for (i = 0; i < ((N / 2) + (N % 2)); i++) {
        printLine(i, N);
        printf("\n");
    }
    for (i = (N / 2) - 1; i >= 0; i--) {
        printLine(i, N);
        printf("\n");
    }
}
```

```json
{
  "sample_id": "sample_022",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "7e5fb25a641c2f362ca82552338516ddc1aba85ce2c3d0b87bbf78f4b107aa79",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_023 — validation

```c


#include <stdio.h>

void cruz(int N){
    int i,j;

    for (i=0; i<N; i++){
        for (j=0; j<N; j++){
            if ((j==i) || (j==((N-1)-i)))
                printf("*");
            else
                printf("-");
        }
        printf("\n");
    }
}

int main(){
    int N;

    scanf("%d", &N);
    cruz(N);

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
  "source_sha256": "2e68b27af123ac0d91d39d75e6db730afcc1b3a9b082967687fe271c38d3662d",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_024 — train

```c


#include <stdio.h>

void cruz (int N){

    int i = 1, contador = 1;
    while (i<=N)
    {
        for(contador=1; contador<=N; contador++){
            if(contador == i || contador==N-i+1)
                printf("*");
            else
                printf("-");
        }
        printf("\n");
        i++;
    }
    
}

int main(){

    int N=0;

    scanf("%d", &N);

    cruz(N);

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
  "source_sha256": "073fc6aa418f79d801670d3bfe6bb8bd08b11ba41f215e8b0d786e82103b393a",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_025 — train

```c


#include <stdio.h>

void cruz(int N) {

    int i, j, k = 1;

    for (i = 1; i <= N; i++) {
        for (j = 1; j <= N; j++)
            if (j == k || j == ((N + 1) - k))
                printf("*");
            else
                printf("-");
        k++;
        printf("\n");
    }
}

int main () {

    int N;

    scanf("%d", &N);
    cruz(N);
    
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
  "source_sha256": "0e536926e640cb4b718be1f8ce090588eea334b56b343297e06e2b908f8cd536",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_026 — train

```c


#include <stdio.h>

void cruz(int N){
    int l, c;

    for(l=1; l <= N; l++){
        for(c=1; c <= N; c++){
            if (c == l || (c + l) == (N+1)) 
                printf("*");               
            else
                printf("-");
        }
        printf("\n");
    } 
}

int main(){
    int N;
    scanf ("%d", &N);

    cruz(N);
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
  "source_sha256": "d03b5e748187a6534760b87f4037b91ca12fca55a9f29ac5e54c8b0822338e04",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_027 — train

```c


#include <stdio.h>

void cruz(int N){
    int l, c;

    for(l=1; l <= N; l++){
        for(c=1; c <= N; c++){
            if (c == l || (c + l) == (N+1)) 
                printf("*");
            else
                printf("-");
        }
        printf("\n");
    } 
}

int main(){
    int N;
    scanf ("%d", &N);

    cruz(N);
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
  "source_sha256": "2f04498212a4035310e7a84ef04dda5340bac728357016659599ce2655137501",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_028 — train

```c

#include <stdio.h>
void cruz(int N);
int main(){
    int N;
    scanf("%d",&N);
    cruz(N);
    return 0;
}
    void cruz(int N)
    {
        int c = 0, h = 0;
        N = N - 1;
        while (h <= N){
            while (c <= N)
            {
            if ((c == h)||(c == N-h)){
                printf("*");
            }
            else{
                printf("-");
            }
            c++;
            }
            c = 0;
            h++;
            printf("\n");
        }
    }
```

```json
{
  "sample_id": "sample_028",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "693898102eccd1d5229492c75014a84affbf07fd830f6acc077066ad8e35c496",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_029 — validation

```c

#include <stdio.h>

void cruz(int N){
    int i, j;
    
    for(i = 1; i <= N; i++) {
        for(j = 1; j <= N; j++) {
            printf("%c", (j == i || j == N - (i - 1)? '*' : '-'));
        }
        printf("\n");
    }
}

int main(){
    int N;
    scanf("%d", &N);
    cruz(N);
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
  "source_sha256": "0ec00128d4b8075285ae77984507485d84b4d25194f0610c630fd146a1a70d4d",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_030 — validation

```c
#include <stdio.h>

int main() {
    int N, Cruz_L, Cruz_R, Linhas = 1, Posicao;

    scanf("%d", &N);

    Cruz_L = 1;
    Cruz_R = N;

    while (Linhas <= N) {
        Posicao = 1; 
        
        while (Posicao <= N) {
            if (Posicao == Cruz_L || Posicao == Cruz_R) {
                printf("*");
            } else {
                printf("-");
            }

            Posicao += 1;
        }

        Cruz_L += 1;
        Cruz_R -= 1;
        Linhas += 1;
        printf("\n");
    }

    return 0;
}

```

```json
{
  "sample_id": "sample_030",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "66c75a752f2d912523ac4e9b33ae7665a7c0a6aac3ded359eff0c739b2847183",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_031 — train

```c


#include <stdio.h>

void cruz(int n) {

    int i, j;

    for (i=0; i<n; i++) {
        
        for (j=0; j<n; j++) {

            if (i == j || i+j == n-1) {
                printf("*");
            }
            else {
                printf("-");
            }
        }
        printf("\n");
    }
}

int main() {

    int n;

    scanf("%d",&n);
    cruz(n);

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
  "source_sha256": "dcf8c5a771fc99de3847282e71031bb4aca4682d858f28f8de481e8de1b04cae",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_032 — train

```c


#include <stdio.h>

void cruz(int n) {

    int i, j;

    for (i=0; i<n; i++) {
        
        for (j=0; j<n-1; j++) {

            if (i == j || i+j == n-1) {
                printf("* ");
            }
            else {
                printf("- ");
            }
        }

        if (i == 1 || i == n-1) {
            printf("*\n");
        }
        else
            printf("-\n");

    }
}

int main() {

    int n;

    scanf("%d",&n);
    cruz(n);

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
  "source_sha256": "9f826b5c44f19648e783069cc309718ce1546eb7a5ad1150a971e385b1b33c1f",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "* - -\n- * *\n* - *\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "* - - -\n- * * *\n- * * -\n* - - *\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "* - - - -\n- * - * *\n- - * - -\n- * - * -\n* - - - *\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "* - - - - - - -\n- * - - - - * *\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "small",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "small",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_033 — train

```c


#include <stdio.h>

void cruz(int n) {

    int i, j;

    for (i=0; i<n; i++) {
        
        for (j=0; j<n; j++) {

            if (i == j || i+j == n-1) {
                putchar('*');
            }
            else {
                putchar('-');
            }
        }
        putchar('\n');
    }
}

int main() {

    int n;

    scanf("%d",&n);
    cruz(n);

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
  "source_sha256": "0af959718512298f0fd56bd0efad7ed80e86ccc4496725d3c4ada2cc94ee99e7",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_034 — validation

```c

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

void cruz(int N){
    int i, j;
    for(i = 0; i < N; i++){
        for(j = 0; j < N; j++){
            if(i == j || i + j == N){
                putchar('*');
            }
            else{
                putchar('-');
            }

            if(j == N - 1){
                putchar('\n');
            }
            else{
                putchar(' ');
            }
        }
    }
}

int main(){
    int N;
    scanf("%d", &N);
    cruz(N);
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
  "source_sha256": "83ebafc3417d2162958048acccc45230843c7eaa9318dfa1716f181cbb2fb538",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "* - -\n- * *\n- * *\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "* - - -\n- * - *\n- - * -\n- * - *\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "* - - - -\n- * - - *\n- - * * -\n- - * * -\n- * - - *\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "* - - - - - - -\n- * - - - - - *\n- - * - - - * -\n- - - * - * - -\n- - - - * - - -\n- - - * - * - -\n- - * - - - * -\n- * - - - - - *\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_035 — train

```c

#include <stdio.h>

void cruz(int num) {
    int linha, col;
    for (linha = 1; linha <= num; linha++) {
        for (col = 1; col <= num; col++) {
            if (col == linha || col == (num - linha + 1))
                printf("*");
            else
                printf("-");
        }
        printf("\n");
    }
}

int main () {
    int num;
    scanf("%d", &num);
    cruz(num);

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
  "source_sha256": "945408188a6e5ee412da5f20d73f8ef1a1ea91023c781057c6c4dd5937a566ed",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_036 — train

```c

#include <stdio.h>

void cruz(int num) {
    int linha, col;
    for (linha = 1; linha <= num; linha++) {
        for (col = 1; col <= num; col++) {
            if (col == linha || col == (num - linha + 1))
                printf("*");
            else
                printf("-");
        }
        if (linha != num)
            printf("\n");
    }
}

int main () {
    int num;
    scanf("%d", &num);
    cruz(num);

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
  "source_sha256": "fdd4037798af8a49ec474cf0e9a733d9ccb42ebcbe6575f98d73f5221ca9504b",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_037 — train

```c

#include <stdio.h>

void cruz(int num) {
    int linha, col;
    for (linha = 1; linha <= num; linha++) {
        for (col = 1; col <= num; col++) {
            if (col == linha || col == (num - linha + 1))
                printf("*");
            else
                printf("-");
        }
        printf("\n");
    }
}

int main () {
    int num;
    scanf("%d", &num);
    cruz(num);

   return 0; 
}


```

```json
{
  "sample_id": "sample_037",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "945408188a6e5ee412da5f20d73f8ef1a1ea91023c781057c6c4dd5937a566ed",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_038 — train

```c

#include <stdio.h>

void cruz(int N) {
    int i,j;
    for (i=0;i<N;i++) {
        for (j=0;j<N;j++) {
            if (i==j) {
                printf("* ");
            } 
            
                
                else if (i+j==N-1) {
                printf("*");
            }else {
                printf("- ");
            } }
        putchar('\n');
    }
} 


int main() {
    int N;
    scanf("%d",&N);
    cruz(N);
    return 0;
}
```

```json
{
  "sample_id": "sample_038",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "4b46b68b118df156d55c2140b801cf52bc317a0a77bfa41458ac022b52937338",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "* - *\n- * - \n*- * \n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "* - - *\n- * *- \n- ** - \n*- - * \n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "* - - - *\n- * - *- \n- - * - - \n- *- * - \n*- - - * \n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "* - - - - - - *\n- * - - - - *- \n- - * - - *- - \n- - - * *- - - \n- - - ** - - - \n- - *- - * - - \n- *- - - - * - \n*- - - - - - * \n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "small",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "small",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_039 — train

```c


#include <stdio.h>

void cruz(int N){
    int i;
    int base = 0;
    while(base<N){
        for (i=0; i<N; i++){
            if(i==base || i==N-base-1)
                printf("*");
            else
                printf("-");
            if(i==N-1)
                printf("\n");
        }
        base++;
    }
}

int main(){
    int N;
    scanf("%d", &N);
    cruz(N);
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
  "source_sha256": "e409b7b62ade43fe10603d41656ad57687aeea9013a3c6d3f29164fc825c5f10",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
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


## sample_040 — train

```c


#include <stdio.h>

void cruz (int n) {
    int count = 0, linha = 1, p_estrela = 1, u_estrela = n, guardar_n = n ;
    while (count < guardar_n) {
        linha = 1;
        while (linha < n + 1){
            if ((linha == u_estrela && linha == n)) {
                printf("*\n");
            }            
            else if (linha == p_estrela || linha == u_estrela) {
                printf("* ");
            }
            else if (linha == n)
                printf("-\n");
            else
                printf("- ");
            linha++;
        }
        p_estrela++;
        u_estrela--;
        count++;
    }
    printf("\b\n");
}

int main () {
    int n;
    scanf("%d", &n);
    cruz(n);
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
  "source_sha256": "f354f82b003bfbde8223d0cabe87278aa991f573db48c7872cfeb4b616274128",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "* - *\n- * -\n* - * \b\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "* - - *\n- * * -\n- * * -\n* - - * \b\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - * \b\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - * \b\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "small",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "small",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "small",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_041 — train

```c

#include <stdio.h>


void cruz(int N);

int main(){
    int n;

    scanf("%d", &n);
    cruz(n);

    return 0;
}

void cruz(int N){
    int row, col;

    
    for (row=0; row<N; row++){
        for (col=0; col<N; col++){
            
            if (col==row || col==((N)-row-1)){
                printf("*");
            } else {
                printf("-");
            }
        }
        
        printf("\n");
    }
}
```

```json
{
  "sample_id": "sample_041",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "8088b3cdb262dd976971a995a097be6a3636e00c236c3e894d8d2163a194e729",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_042 — train

```c
#include <stdio.h>

void cruz(int n){    
    int i, j;

    for (i = 0; i < n; i++){
        for (j = 0; j < n; j++){
            if (j==i|| j == n - i - 1){
                printf("*");
            }
            else printf("-");
        }
        printf("\n");
    }
}

int main(){
    int n;

    scanf("%d", &n);
    cruz(n);

    return 0;
}
```

```json
{
  "sample_id": "sample_042",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "f471b7702b72077778bbef4ce2cf7258a786ba674c765f3d207b39a71696b775",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_043 — train

```c


#include <stdio.h>
#define MAX N
#define METADE (N/2)+1


void cruz(int N){
    int i,j;
    int min=1;
    for (i=1; i<=N; i++){
        for (j=1; j<=N ;j++){
            if (i==min){
                if(j==min){
                    printf("* ");
                }
                if(j==MAX){
                    printf("*");
                }
                if(j!=MAX && j!=min){
                    printf("- ");
                }
                if(j==N){
                    printf("\n");
                }
            }
            
        }  
        min++;
        MAX--;      
    }
}



int main(){
    int N;
    scanf("%d", &N);
    cruz(N);
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
  "source_sha256": "cebfab763dde027af8f3e90745345c3c86f3b39a35b7907b662854ee2eb67914",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "* - *\n- * *\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "* - - *\n- * *\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "* - - - *\n- * - *\n- - * *\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "* - - - - - - *\n- * - - - - *\n- - * - - *\n- - - * *\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_044 — validation

```c

#include <stdio.h>

void cruz(int N){
    int i, j;

    for(i = 0; i < N; i++){
        for (j = 1; j <= N; j++){
            if (j == (i + 1) || j + i == N){
                printf("* ");
            }
            else{
                printf("- ");
            }
        }
        printf("\b\n");
    }
}




int main(){
    int N;

    scanf("%d", &N);

    cruz(N);

    return 0;
}
```

```json
{
  "sample_id": "sample_044",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "3129f161b3aac50c9e2b2d0ef32a79307a055b73df66bc649c562ee1911f6646",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "* - * \b\n- * - \b\n* - * \b\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "* - - * \b\n- * * - \b\n- * * - \b\n* - - * \b\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "* - - - * \b\n- * - * - \b\n- - * - - \b\n- * - * - \b\n* - - - * \b\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "* - - - - - - * \b\n- * - - - - * - \b\n- - * - - * - - \b\n- - - * * - - - \b\n- - - * * - - - \b\n- - * - - * - - \b\n- * - - - - * - \b\n* - - - - - - * \b\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "small",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_045 — validation

```c

#include <stdio.h>

void cruz(int N){
    int i, j;

    for(i = 0; i < N; i++){
        for (j = 1; j <= N; j++){
            if (j == (i + 1) || j + i == N){
                printf("%c ", '*');
            }
            else{
                printf("%c ", '-');
            }
        }
        printf("\b\n");
    }
}




int main(){
    int N;

    scanf("%d", &N);

    cruz(N);

    return 0;
}
```

```json
{
  "sample_id": "sample_045",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "29001d8a0b106f4a0d954aebd818ddf407fe424cb449e3ca9f0d2d65373d2a49",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "* - * \b\n- * - \b\n* - * \b\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "* - - * \b\n- * * - \b\n- * * - \b\n* - - * \b\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "* - - - * \b\n- * - * - \b\n- - * - - \b\n- * - * - \b\n* - - - * \b\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "* - - - - - - * \b\n- * - - - - * - \b\n- - * - - * - - \b\n- - - * * - - - \b\n- - - * * - - - \b\n- - * - - * - - \b\n- * - - - - * - \b\n* - - - - - - * \b\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "small",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_046 — train

```c

#include <stdio.h>

void cruz(int n){
    int i,j;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            if(j==i ||j==n-i-1){
                printf("*");
            }else{
                printf("-");
            }
        }
        printf("\n");
    }
}

int main(){
    int n;
    scanf("%d",&n);
    cruz(n);

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
  "source_sha256": "c49e68376e1ee37f99d62f834b2e2721a8bc25e20136d606cbd6d9c12253696a",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_047 — train

```c

#include <stdio.h>

void cruz(int n) {
    int i, j;
    for(i = 1; i <= n; i++){
        for(j = 1; j<= n; j++){
            if(j == i || j == (n - i + 1)){
                printf("* ");
            }else{
                printf("- ");
            }
        }
        printf("\b\n");
        
    }

}


int main() {
    int n;
    scanf("%d", &n);
    cruz(n);
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
  "source_sha256": "66d84b2d3002695d5a2aa84090a322dd3a91f9160c79239a99982d33932240ce",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "* - * \b\n- * - \b\n* - * \b\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "* - - * \b\n- * * - \b\n- * * - \b\n* - - * \b\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "* - - - * \b\n- * - * - \b\n- - * - - \b\n- * - * - \b\n* - - - * \b\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "* - - - - - - * \b\n- * - - - - * - \b\n- - * - - * - - \b\n- - - * * - - - \b\n- - - * * - - - \b\n- - * - - * - - \b\n- * - - - - * - \b\n* - - - - - - * \b\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "small",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_048 — train

```c

#include <stdio.h>

void cruz(int N)
{
    int i, j;

    for(j = 0; j < N; j++)
    {
        for(i = 0; i < N; i++)
        {   
            if(i == j)
            {
                printf("*");
            }

            else if(i == ((N - 1) - j))
            {
                printf("*");
            }
            else
            {
                printf("-");
            }
        }
        printf("\n");
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
  "sample_id": "sample_048",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "246b1c144d3b56500619ace8aca25582fa17d3bc78d6b9ba52ebb20d5f896a63",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_049 — train

```c

#include <stdio.h>

int main(){
    int n, i, l=1, r;
    scanf("%d", &n);
    r=n;
    while (l<=n){
        for (i=1; i<n; i++) printf("%c", i==l||i==r?'*':'-');
    printf("%c\n", i==l||i==r?'*':'-');
    l++;
    r--;
}
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
  "source_sha256": "69f5f3f600a265d76a23f02b0478668d55444babdc6ab2dd3f9fb2eb15cbb19c",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_050 — train

```c


#include <stdio.h>

int main() {
    int n,r,l,j; 
    scanf("%d", &n);
    if (n<=0)
        return 0;
    l=1;
    r = n;
    while (l<=n){
        for (j=1;j<n;j++)
            printf("%c", j==l || j == r ? '*': '-');
        printf("%c\n", j==l || j == r ? '*': '-');
        l++;
        r--;
    }
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
  "source_sha256": "8856f2e27b0fbc958d3538101cf8199f02ee790dc5ccb843168f185248f1f194",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_051 — train

```c

#include <stdio.h>

int main(){
    int n,i,j;
    scanf("%d",&n);
    for (i=1; i<=n; i++){
        for (j=1; j<=n; j++){
            if (j == i || j == n-i+1)
                putchar('*');
            else
                putchar('-');
        }
        putchar('\n');
    }
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
  "source_sha256": "988b0de2644e64bed1dad820314fa44c94491d1ad9c330d37b007e3e6ea68f29",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "*-*\n-*-\n*-*\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "*--*\n-**-\n-**-\n*--*\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "*---*\n-*-*-\n--*--\n-*-*-\n*---*\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "*------*\n-*----*-\n--*--*--\n---**---\n---**---\n--*--*--\n-*----*-\n*------*\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## sample_052 — train

```c

#include <stdio.h>

int main(){
    int n,l,r,j;
    scanf("%d",&n);
    l=1;
    r=n;
    while(l<=n){
        for(j=1;j<n;j++){
            printf("%c ",j==l||j==r?'*':'-');
            printf("%c\n",j==l?'*':'-');
        }
        l++;
        r--;
    }
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
  "source_sha256": "343b909b2d5bcc8ea658204a7389e29ff2a96aca2b3785f448660c9465f7d0f1",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail",
    "ex03_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3",
      "expected": "* - *\n- * -\n* - *\n",
      "output": "* *\n- -\n- -\n* *\n* -\n- -\n"
    },
    {
      "test_id": "ex03_1",
      "input": "4",
      "expected": "* - - *\n- * * -\n- * * -\n* - - *\n",
      "output": "* *\n- -\n- -\n- -\n* *\n* -\n- -\n* -\n* *\n* -\n- -\n- -\n"
    },
    {
      "test_id": "ex03_2",
      "input": "5",
      "expected": "* - - - *\n- * - * -\n- - * - -\n- * - * -\n* - - - *\n",
      "output": "* *\n- -\n- -\n- -\n- -\n* *\n- -\n* -\n- -\n- -\n* *\n- -\n- -\n* -\n- -\n* *\n* -\n- -\n- -\n- -\n"
    },
    {
      "test_id": "ex03_3",
      "input": "8",
      "expected": "* - - - - - - *\n- * - - - - * -\n- - * - - * - -\n- - - * * - - -\n- - - * * - - -\n- - * - - * - -\n- * - - - - * -\n* - - - - - - *\n",
      "output": "* *\n- -\n- -\n- -\n- -\n- -\n- -\n- -\n* *\n- -\n- -\n- -\n- -\n* -\n- -\n- -\n* *\n- -\n- -\n* -\n- -\n- -\n- -\n- -\n* *\n* -\n- -\n- -\n- -\n- -\n- -\n* -\n* *\n- -\n- -\n- -\n- -\n* -\n- -\n- -\n* *\n- -\n- -\n* -\n- -\n- -\n- -\n- -\n* *\n* -\n- -\n- -\n- -\n- -\n- -\n- -\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium",
    "stdout:ex03_3:relation": "different",
    "stdout:ex03_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "test:ex03_3": "fail",
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


## Evidence refs hợp lệ

```json
[
  "test_statistics",
  "feature_statistics",
  "learned_if_then_rules",
  "semantic_findings",
  "problem_statement",
  "members/sample_001/raw_code",
  "members/sample_001/tests/ex03_0",
  "members/sample_001/tests/ex03_2",
  "members/sample_002/raw_code",
  "members/sample_002/tests/ex03_0",
  "members/sample_002/tests/ex03_1",
  "members/sample_002/tests/ex03_2",
  "members/sample_002/tests/ex03_3",
  "members/sample_003/raw_code",
  "members/sample_003/tests/ex03_0",
  "members/sample_003/tests/ex03_1",
  "members/sample_003/tests/ex03_2",
  "members/sample_003/tests/ex03_3",
  "members/sample_004/raw_code",
  "members/sample_004/tests/ex03_0",
  "members/sample_004/tests/ex03_1",
  "members/sample_004/tests/ex03_2",
  "members/sample_004/tests/ex03_3",
  "members/sample_005/raw_code",
  "members/sample_005/tests/ex03_0",
  "members/sample_005/tests/ex03_1",
  "members/sample_005/tests/ex03_2",
  "members/sample_005/tests/ex03_3",
  "members/sample_006/raw_code",
  "members/sample_006/tests/ex03_0",
  "members/sample_006/tests/ex03_1",
  "members/sample_006/tests/ex03_2",
  "members/sample_006/tests/ex03_3",
  "members/sample_007/raw_code",
  "members/sample_007/tests/ex03_0",
  "members/sample_007/tests/ex03_1",
  "members/sample_007/tests/ex03_2",
  "members/sample_007/tests/ex03_3",
  "members/sample_008/raw_code",
  "members/sample_008/tests/ex03_0",
  "members/sample_008/tests/ex03_1",
  "members/sample_008/tests/ex03_2",
  "members/sample_008/tests/ex03_3",
  "members/sample_009/raw_code",
  "members/sample_009/tests/ex03_0",
  "members/sample_009/tests/ex03_1",
  "members/sample_009/tests/ex03_2",
  "members/sample_009/tests/ex03_3",
  "members/sample_010/raw_code",
  "members/sample_010/tests/ex03_0",
  "members/sample_010/tests/ex03_1",
  "members/sample_010/tests/ex03_2",
  "members/sample_010/tests/ex03_3",
  "members/sample_011/raw_code",
  "members/sample_011/tests/ex03_0",
  "members/sample_011/tests/ex03_1",
  "members/sample_011/tests/ex03_2",
  "members/sample_011/tests/ex03_3",
  "members/sample_012/raw_code",
  "members/sample_012/tests/ex03_0",
  "members/sample_012/tests/ex03_1",
  "members/sample_012/tests/ex03_2",
  "members/sample_012/tests/ex03_3",
  "members/sample_013/raw_code",
  "members/sample_013/tests/ex03_0",
  "members/sample_013/tests/ex03_1",
  "members/sample_013/tests/ex03_2",
  "members/sample_013/tests/ex03_3",
  "members/sample_014/raw_code",
  "members/sample_014/tests/ex03_0",
  "members/sample_014/tests/ex03_1",
  "members/sample_014/tests/ex03_2",
  "members/sample_014/tests/ex03_3",
  "members/sample_015/raw_code",
  "members/sample_015/tests/ex03_0",
  "members/sample_015/tests/ex03_1",
  "members/sample_015/tests/ex03_2",
  "members/sample_015/tests/ex03_3",
  "members/sample_016/raw_code",
  "members/sample_016/tests/ex03_0",
  "members/sample_016/tests/ex03_1",
  "members/sample_016/tests/ex03_2",
  "members/sample_016/tests/ex03_3",
  "members/sample_017/raw_code",
  "members/sample_017/tests/ex03_0",
  "members/sample_017/tests/ex03_1",
  "members/sample_017/tests/ex03_2",
  "members/sample_017/tests/ex03_3",
  "members/sample_018/raw_code",
  "members/sample_018/tests/ex03_0",
  "members/sample_018/tests/ex03_1",
  "members/sample_018/tests/ex03_2",
  "members/sample_018/tests/ex03_3",
  "members/sample_019/raw_code",
  "members/sample_019/tests/ex03_0",
  "members/sample_019/tests/ex03_1",
  "members/sample_019/tests/ex03_2",
  "members/sample_019/tests/ex03_3",
  "members/sample_020/raw_code",
  "members/sample_020/tests/ex03_0",
  "members/sample_020/tests/ex03_1",
  "members/sample_020/tests/ex03_2",
  "members/sample_020/tests/ex03_3",
  "members/sample_021/raw_code",
  "members/sample_021/tests/ex03_0",
  "members/sample_021/tests/ex03_1",
  "members/sample_021/tests/ex03_2",
  "members/sample_021/tests/ex03_3",
  "members/sample_022/raw_code",
  "members/sample_022/tests/ex03_0",
  "members/sample_022/tests/ex03_1",
  "members/sample_022/tests/ex03_2",
  "members/sample_022/tests/ex03_3",
  "members/sample_023/raw_code",
  "members/sample_023/tests/ex03_0",
  "members/sample_023/tests/ex03_1",
  "members/sample_023/tests/ex03_2",
  "members/sample_023/tests/ex03_3",
  "members/sample_024/raw_code",
  "members/sample_024/tests/ex03_0",
  "members/sample_024/tests/ex03_1",
  "members/sample_024/tests/ex03_2",
  "members/sample_024/tests/ex03_3",
  "members/sample_025/raw_code",
  "members/sample_025/tests/ex03_0",
  "members/sample_025/tests/ex03_1",
  "members/sample_025/tests/ex03_2",
  "members/sample_025/tests/ex03_3",
  "members/sample_026/raw_code",
  "members/sample_026/tests/ex03_0",
  "members/sample_026/tests/ex03_1",
  "members/sample_026/tests/ex03_2",
  "members/sample_026/tests/ex03_3",
  "members/sample_027/raw_code",
  "members/sample_027/tests/ex03_0",
  "members/sample_027/tests/ex03_1",
  "members/sample_027/tests/ex03_2",
  "members/sample_027/tests/ex03_3",
  "members/sample_028/raw_code",
  "members/sample_028/tests/ex03_0",
  "members/sample_028/tests/ex03_1",
  "members/sample_028/tests/ex03_2",
  "members/sample_028/tests/ex03_3",
  "members/sample_029/raw_code",
  "members/sample_029/tests/ex03_0",
  "members/sample_029/tests/ex03_1",
  "members/sample_029/tests/ex03_2",
  "members/sample_029/tests/ex03_3",
  "members/sample_030/raw_code",
  "members/sample_030/tests/ex03_0",
  "members/sample_030/tests/ex03_1",
  "members/sample_030/tests/ex03_2",
  "members/sample_030/tests/ex03_3",
  "members/sample_031/raw_code",
  "members/sample_031/tests/ex03_0",
  "members/sample_031/tests/ex03_1",
  "members/sample_031/tests/ex03_2",
  "members/sample_031/tests/ex03_3",
  "members/sample_032/raw_code",
  "members/sample_032/tests/ex03_0",
  "members/sample_032/tests/ex03_1",
  "members/sample_032/tests/ex03_2",
  "members/sample_032/tests/ex03_3",
  "members/sample_033/raw_code",
  "members/sample_033/tests/ex03_0",
  "members/sample_033/tests/ex03_1",
  "members/sample_033/tests/ex03_2",
  "members/sample_033/tests/ex03_3",
  "members/sample_034/raw_code",
  "members/sample_034/tests/ex03_0",
  "members/sample_034/tests/ex03_1",
  "members/sample_034/tests/ex03_2",
  "members/sample_034/tests/ex03_3",
  "members/sample_035/raw_code",
  "members/sample_035/tests/ex03_0",
  "members/sample_035/tests/ex03_1",
  "members/sample_035/tests/ex03_2",
  "members/sample_035/tests/ex03_3",
  "members/sample_036/raw_code",
  "members/sample_036/tests/ex03_0",
  "members/sample_036/tests/ex03_1",
  "members/sample_036/tests/ex03_2",
  "members/sample_036/tests/ex03_3",
  "members/sample_037/raw_code",
  "members/sample_037/tests/ex03_0",
  "members/sample_037/tests/ex03_1",
  "members/sample_037/tests/ex03_2",
  "members/sample_037/tests/ex03_3",
  "members/sample_038/raw_code",
  "members/sample_038/tests/ex03_0",
  "members/sample_038/tests/ex03_1",
  "members/sample_038/tests/ex03_2",
  "members/sample_038/tests/ex03_3",
  "members/sample_039/raw_code",
  "members/sample_039/tests/ex03_0",
  "members/sample_039/tests/ex03_1",
  "members/sample_039/tests/ex03_2",
  "members/sample_039/tests/ex03_3",
  "members/sample_040/raw_code",
  "members/sample_040/tests/ex03_0",
  "members/sample_040/tests/ex03_1",
  "members/sample_040/tests/ex03_2",
  "members/sample_040/tests/ex03_3",
  "members/sample_041/raw_code",
  "members/sample_041/tests/ex03_0",
  "members/sample_041/tests/ex03_1",
  "members/sample_041/tests/ex03_2",
  "members/sample_041/tests/ex03_3",
  "members/sample_042/raw_code",
  "members/sample_042/tests/ex03_0",
  "members/sample_042/tests/ex03_1",
  "members/sample_042/tests/ex03_2",
  "members/sample_042/tests/ex03_3",
  "members/sample_043/raw_code",
  "members/sample_043/tests/ex03_0",
  "members/sample_043/tests/ex03_1",
  "members/sample_043/tests/ex03_2",
  "members/sample_043/tests/ex03_3",
  "members/sample_044/raw_code",
  "members/sample_044/tests/ex03_0",
  "members/sample_044/tests/ex03_1",
  "members/sample_044/tests/ex03_2",
  "members/sample_044/tests/ex03_3",
  "members/sample_045/raw_code",
  "members/sample_045/tests/ex03_0",
  "members/sample_045/tests/ex03_1",
  "members/sample_045/tests/ex03_2",
  "members/sample_045/tests/ex03_3",
  "members/sample_046/raw_code",
  "members/sample_046/tests/ex03_0",
  "members/sample_046/tests/ex03_1",
  "members/sample_046/tests/ex03_2",
  "members/sample_046/tests/ex03_3",
  "members/sample_047/raw_code",
  "members/sample_047/tests/ex03_0",
  "members/sample_047/tests/ex03_1",
  "members/sample_047/tests/ex03_2",
  "members/sample_047/tests/ex03_3",
  "members/sample_048/raw_code",
  "members/sample_048/tests/ex03_0",
  "members/sample_048/tests/ex03_1",
  "members/sample_048/tests/ex03_2",
  "members/sample_048/tests/ex03_3",
  "members/sample_049/raw_code",
  "members/sample_049/tests/ex03_0",
  "members/sample_049/tests/ex03_1",
  "members/sample_049/tests/ex03_2",
  "members/sample_049/tests/ex03_3",
  "members/sample_050/raw_code",
  "members/sample_050/tests/ex03_0",
  "members/sample_050/tests/ex03_1",
  "members/sample_050/tests/ex03_2",
  "members/sample_050/tests/ex03_3",
  "members/sample_051/raw_code",
  "members/sample_051/tests/ex03_0",
  "members/sample_051/tests/ex03_1",
  "members/sample_051/tests/ex03_2",
  "members/sample_051/tests/ex03_3",
  "members/sample_052/raw_code",
  "members/sample_052/tests/ex03_0",
  "members/sample_052/tests/ex03_1",
  "members/sample_052/tests/ex03_2",
  "members/sample_052/tests/ex03_3"
]
```
