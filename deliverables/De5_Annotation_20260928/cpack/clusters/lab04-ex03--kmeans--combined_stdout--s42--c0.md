# lab04-ex03--kmeans--combined_stdout--s42--c0

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 19; phân vùng: {'validation': 8, 'train': 11}.


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
    "test_id": "ex03_1",
    "n_cluster": 19,
    "n_observed": 19,
    "n_failed": 19,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 19
    }
  },
  {
    "test_id": "ex03_2",
    "n_cluster": 19,
    "n_observed": 19,
    "n_failed": 19,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 19
    }
  },
  {
    "test_id": "ex03_0",
    "n_cluster": 19,
    "n_observed": 19,
    "n_failed": 17,
    "n_not_run": 0,
    "failure_rate_observed": 0.8947368421052632,
    "failure_rate_cluster": 0.8947368421052632,
    "outcome_counts": {
      "fail": 17,
      "pass": 2
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex03_2:relation",
    "value": "different",
    "n": 18,
    "n_cluster": 19,
    "rate": 0.9473684210526315,
    "cohort_rate": 0.8181818181818182,
    "difference_from_cohort": 0.1291866028708133
  },
  {
    "feature": "stdout:ex03_0:relation",
    "value": "different",
    "n": 16,
    "n_cluster": 19,
    "rate": 0.8421052631578947,
    "cohort_rate": 0.7272727272727273,
    "difference_from_cohort": 0.1148325358851674
  },
  {
    "feature": "stdout:ex03_2:edit_band",
    "value": "large",
    "n": 15,
    "n_cluster": 19,
    "rate": 0.7894736842105263,
    "cohort_rate": 0.6818181818181818,
    "difference_from_cohort": 0.10765550239234456
  },
  {
    "feature": "test:ex03_2",
    "value": "fail",
    "n": 19,
    "n_cluster": 19,
    "rate": 1.0,
    "cohort_rate": 0.9090909090909091,
    "difference_from_cohort": 0.09090909090909094
  },
  {
    "feature": "stdout:ex03_0:edit_band",
    "value": "medium",
    "n": 11,
    "n_cluster": 19,
    "rate": 0.5789473684210527,
    "cohort_rate": 0.5,
    "difference_from_cohort": 0.07894736842105265
  },
  {
    "feature": "stdout:ex03_1:edit_band",
    "value": "large",
    "n": 11,
    "n_cluster": 19,
    "rate": 0.5789473684210527,
    "cohort_rate": 0.5,
    "difference_from_cohort": 0.07894736842105265
  },
  {
    "feature": "test:ex03_0",
    "value": "fail",
    "n": 17,
    "n_cluster": 19,
    "rate": 0.8947368421052632,
    "cohort_rate": 0.8181818181818182,
    "difference_from_cohort": 0.07655502392344493
  },
  {
    "feature": "ast:c_while",
    "value": "0",
    "n": 16,
    "n_cluster": 19,
    "rate": 0.8421052631578947,
    "cohort_rate": 0.7727272727272727,
    "difference_from_cohort": 0.06937799043062198
  },
  {
    "feature": "stdout:ex03_1:edit_band",
    "value": "medium",
    "n": 7,
    "n_cluster": 19,
    "rate": 0.3684210526315789,
    "cohort_rate": 0.3181818181818182,
    "difference_from_cohort": 0.05023923444976075
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "0",
    "n": 12,
    "n_cluster": 19,
    "rate": 0.631578947368421,
    "cohort_rate": 0.5909090909090909,
    "difference_from_cohort": 0.04066985645933008
  },
  {
    "feature": "stdout:ex03_1:relation",
    "value": "different",
    "n": 18,
    "n_cluster": 19,
    "rate": 0.9473684210526315,
    "cohort_rate": 0.9090909090909091,
    "difference_from_cohort": 0.038277511961722466
  },
  {
    "feature": "stdout:ex03_0:edit_band",
    "value": "large",
    "n": 5,
    "n_cluster": 19,
    "rate": 0.2631578947368421,
    "cohort_rate": 0.22727272727272727,
    "difference_from_cohort": 0.035885167464114825
  },
  {
    "feature": "ast:c_array_parameter",
    "value": "0",
    "n": 17,
    "n_cluster": 19,
    "rate": 0.8947368421052632,
    "cohort_rate": 0.8636363636363636,
    "difference_from_cohort": 0.031100478468899517
  },
  {
    "feature": "ast:c_zero_index",
    "value": "1",
    "n": 3,
    "n_cluster": 19,
    "rate": 0.15789473684210525,
    "cohort_rate": 0.13636363636363635,
    "difference_from_cohort": 0.0215311004784689
  },
  {
    "feature": "stdout:ex03_2:edit_band",
    "value": "medium",
    "n": 3,
    "n_cluster": 19,
    "rate": 0.15789473684210525,
    "cohort_rate": 0.13636363636363635,
    "difference_from_cohort": 0.0215311004784689
  },
  {
    "feature": "ast:c_address_of",
    "value": "0",
    "n": 2,
    "n_cluster": 19,
    "rate": 0.10526315789473684,
    "cohort_rate": 0.09090909090909091,
    "difference_from_cohort": 0.014354066985645925
  },
  {
    "feature": "ast:c_for",
    "value": "0",
    "n": 1,
    "n_cluster": 19,
    "rate": 0.05263157894736842,
    "cohort_rate": 0.045454545454545456,
    "difference_from_cohort": 0.007177033492822962
  },
  {
    "feature": "ast:c_if",
    "value": "0",
    "n": 1,
    "n_cluster": 19,
    "rate": 0.05263157894736842,
    "cohort_rate": 0.045454545454545456,
    "difference_from_cohort": 0.007177033492822962
  },
  {
    "feature": "ast:c_subscript",
    "value": "0",
    "n": 1,
    "n_cluster": 19,
    "rate": 0.05263157894736842,
    "cohort_rate": 0.045454545454545456,
    "difference_from_cohort": 0.007177033492822962
  },
  {
    "feature": "stdout:ex03_0:edit_band",
    "value": "small",
    "n": 1,
    "n_cluster": 19,
    "rate": 0.05263157894736842,
    "cohort_rate": 0.045454545454545456,
    "difference_from_cohort": 0.007177033492822962
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 19,
    "n_cluster": 19,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 19,
    "n_cluster": 19,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 19,
    "n_cluster": 19,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 18,
    "n_cluster": 19,
    "rate": 0.9473684210526315,
    "cohort_rate": 0.9545454545454546,
    "difference_from_cohort": -0.0071770334928230595
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 18,
    "n_cluster": 19,
    "rate": 0.9473684210526315,
    "cohort_rate": 0.9545454545454546,
    "difference_from_cohort": -0.0071770334928230595
  },
  {
    "feature": "ast:c_subscript",
    "value": "1",
    "n": 18,
    "n_cluster": 19,
    "rate": 0.9473684210526315,
    "cohort_rate": 0.9545454545454546,
    "difference_from_cohort": -0.0071770334928230595
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 17,
    "n_cluster": 19,
    "rate": 0.8947368421052632,
    "cohort_rate": 0.9090909090909091,
    "difference_from_cohort": -0.014354066985645897
  }
]
```


## IF–THEN dự đoán cluster, không dự đoán gold

```json
[
  {
    "rule_id": 2,
    "if": [
      "stdout:ex03_2:relation=different"
    ],
    "then_cluster": 0,
    "train_support": 11,
    "train_precision": 1.0,
    "holdout_support": 7,
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
  "reasoning": "Có 19 bài trong cụm. Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
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

sample_005, sample_015, sample_002, sample_004

## sample_002 — validation — đại diện

```c
#include <stdio.h>

#define VECMAX 100
int main()
{
    int n, i, j, max = 0;
    int vect[VECMAX];
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        scanf("%d", &vect[i]);
        if (vect[i] > max)
            max = vect[i];
    }

    for (i = 0; i < max; i++)
    { 

        for (j = 0; j < n; j++)
        {

            if ((n - i - 1) < vect[j])
            {
                printf("*");
            }
            else
                printf(" ");
        }
        printf("\n");
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_002",
  "partition": "validation",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "800a4dccd5c9269c65b0bdbf9203345f2fe3843f5bcac8a33ae0e01ad5e03ba0",
  "outcomes": {
    "ex03_0": "pass",
    "ex03_1": "fail",
    "ex03_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_1",
      "input": "3 2 6 8",
      "expected": "  *\n  *\n **\n **\n **\n **\n***\n***\n",
      "output": " **\n***\n***\n***\n***\n***\n***\n***\n"
    },
    {
      "test_id": "ex03_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*       *\n**     **\n***   ***\n**** ****\n*********\n",
      "output": "         \n         \n         \n         \n*       *\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "pass",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "stdout:ex03_0:relation": "__unknown__",
    "stdout:ex03_0:edit_band": "__unknown__",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "large",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex03_0": "pass",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
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


## sample_004 — train — đại diện

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
          printf("* ");
      }
      else if (col == N)
        printf("-\n");
      else
        printf("- ");
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
  "sample_id": "sample_004",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "a6c9f08d6ad0f44c57801ade2dfeac346b9cb0bdbb3bcd7f2e9c043951ee6cc5",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3 1 2 3",
      "expected": "  *\n **\n***\n",
      "output": "* - *\n- * -\n* - *\n"
    },
    {
      "test_id": "ex03_1",
      "input": "3 2 6 8",
      "expected": "  *\n  *\n **\n **\n **\n **\n***\n***\n",
      "output": "* - *\n- * -\n* - *\n"
    },
    {
      "test_id": "ex03_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*       *\n**     **\n***   ***\n**** ****\n*********\n",
      "output": "* - - - - - - - *\n- * - - - - - * -\n- - * - - - * - -\n- - - * - * - - -\n- - - - * - - - -\n- - - * - * - - -\n- - * - - - * - -\n- * - - - - - * -\n* - - - - - - - *\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "large",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "large",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
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


## sample_005 — train — đại diện

```c

#include <stdio.h>
#define VECMAX 100

int main(){
    int l,c,num,mx = 0;
    int val[VECMAX];
    scanf("%d", &num);
    for(l = 0; l < num; l++){
        scanf("%d", &val[l]);
        mx = val[l] > mx ? val[l] : mx;
    }

    for(l = 0; l < mx; l++){
        for(c = 0; c < num; c++){
            if (val[c] < l)
                putchar(' ');
            else
                putchar('*');
        }
        putchar('\n');
    }

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
  "source_sha256": "84e81e5b26d210fed10a369e556bd48f3ebbedf5a992ef48b21ad5a9fb300a88",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3 1 2 3",
      "expected": "  *\n **\n***\n",
      "output": "***\n***\n **\n"
    },
    {
      "test_id": "ex03_1",
      "input": "3 2 6 8",
      "expected": "  *\n  *\n **\n **\n **\n **\n***\n***\n",
      "output": "***\n***\n***\n **\n **\n **\n **\n  *\n"
    },
    {
      "test_id": "ex03_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*       *\n**     **\n***   ***\n**** ****\n*********\n",
      "output": "*********\n*********\n**** ****\n***   ***\n**     **\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
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


## sample_015 — train — đại diện

```c

#include <stdio.h>

#define VECMAX 100

int max(int vec[], int n);

int main(){
    int n, j, i, mx;
    int vec[VECMAX];
    scanf("%d", &n);
    for (i=0; i<n; i++) scanf("%d", &vec[i]);
    mx = max(vec, n);
    for (i=mx; i>=1; i--){
        for (j=0; j<n; j++) putchar(vec[j]>i?'*':' ');
    putchar('\n');}
    return 0;
}

int max(int vec[], int n){
    int i=1;
    int mx=vec[0];
    while (i<n){
        if (vec[i]>mx) mx=vec[i];
    i++;
    }
return mx;
}
```

```json
{
  "sample_id": "sample_015",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "81544ae6594b557a7d893ae36688844d1a049704d96274066734e3ffaf0c84d7",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3 1 2 3",
      "expected": "  *\n **\n***\n",
      "output": "   \n  *\n **\n"
    },
    {
      "test_id": "ex03_1",
      "input": "3 2 6 8",
      "expected": "  *\n  *\n **\n **\n **\n **\n***\n***\n",
      "output": "   \n  *\n  *\n **\n **\n **\n **\n***\n"
    },
    {
      "test_id": "ex03_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*       *\n**     **\n***   ***\n**** ****\n*********\n",
      "output": "         \n*       *\n**     **\n***   ***\n**** ****\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "1",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_001 — validation

```c
#include <stdio.h>
#include <string.h>

#define MAX 100

int main()
{
  int i, size, result = 1; 
  char s[MAX];
  
  scanf("%s", s);
  size = strlen(s);
  
  for (i = 0; i < size; i++)
    if (s[i] != s[size - i - 1])
      result = 0;
      
  if (result)
    printf("yes\n");
  else
    printf("no\n");

  return 0;
}

```

```json
{
  "sample_id": "sample_001",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "f538550181d71a7cb60d36a346da9179bd9533d90f22c8cbe418c42b88028bdf",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3 1 2 3",
      "expected": "  *\n **\n***\n",
      "output": "yes\n"
    },
    {
      "test_id": "ex03_1",
      "input": "3 2 6 8",
      "expected": "  *\n  *\n **\n **\n **\n **\n***\n***\n",
      "output": "yes\n"
    },
    {
      "test_id": "ex03_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*       *\n**     **\n***   ***\n**** ****\n*********\n",
      "output": "yes\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "0",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "large",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "large",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
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
    "ast:c_address_of": "0",
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

#define VECMAX 100
int main()
{
    int n, i, j, max = 0;
    int vect[VECMAX];
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        scanf("%d", &vect[i]);
        if (vect[i] > max)
            max = vect[i];
    }


    for (i = 0; i < n; i++)
    { 

        for (j = 0; j < max; j++)
        {

            if ((n - i-1) < vect[j])
            {
                printf("*");
            }
            else
                printf(" ");
        }
        printf("\n");
    }
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
  "source_sha256": "b0f86c2b7e89915eb8b846765314c9a0ef25c3da042272097f7ff9c857bd8695",
  "outcomes": {
    "ex03_0": "pass",
    "ex03_1": "fail",
    "ex03_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_1",
      "input": "3 2 6 8",
      "expected": "  *\n  *\n **\n **\n **\n **\n***\n***\n",
      "output": " **     \n***     \n***     \n"
    },
    {
      "test_id": "ex03_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*       *\n**     **\n***   ***\n**** ****\n*********\n",
      "output": "     \n     \n     \n     \n*    \n**   \n***  \n**** \n*****\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "pass",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "stdout:ex03_0:relation": "__unknown__",
    "stdout:ex03_0:edit_band": "__unknown__",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "large",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex03_0": "pass",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
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


## sample_006 — train

```c

#include <stdio.h>
#define VECMAX 100

int main(){
    int l,c,num,mx = 0;
    int val[VECMAX];
    scanf("%d", &num);
    for(l = 0; l < num; l++){
        scanf("%d", &val[l]);
        mx = val[l] > mx ? val[l] : mx;
    }

    for(l = mx - 1; l < mx; l++){
        
        for(c = 0; c < num; c++){
            if (val[c] > l)
                putchar('*');
            else
                putchar(' ');
        }
        putchar('\n');
    }

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
  "source_sha256": "97c7cdcc89df07d8b9ebb71cdeca91f5bfcd3442706fef43ad7aa2112c050a0c",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3 1 2 3",
      "expected": "  *\n **\n***\n",
      "output": "  *\n"
    },
    {
      "test_id": "ex03_1",
      "input": "3 2 6 8",
      "expected": "  *\n  *\n **\n **\n **\n **\n***\n***\n",
      "output": "  *\n"
    },
    {
      "test_id": "ex03_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*       *\n**     **\n***   ***\n**** ****\n*********\n",
      "output": "*       *\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "large",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "large",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
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


## sample_007 — train

```c

#include <stdio.h>
#define VECMAX 100

int main(){
    int l,c,num,mx = 0;
    int val[VECMAX];
    scanf("%d", &num);
    for(l = 0; l < num; l++){
        scanf("%d", &val[l]);
        mx = val[l] > mx ? val[l] : mx;
    }

    for(l = 0; l < mx; l++){
        for(c = 0; c < num; c++){
            if (val[c] > l)
                putchar(' ');
            else
                putchar('*');
        }
        putchar('\n');
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
  "source_sha256": "5dfa04839b1a00a7b15d1c1a47147aa22060f88af487c4b736fd5a11236bb84c",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3 1 2 3",
      "expected": "  *\n **\n***\n",
      "output": "   \n*  \n** \n"
    },
    {
      "test_id": "ex03_1",
      "input": "3 2 6 8",
      "expected": "  *\n  *\n **\n **\n **\n **\n***\n***\n",
      "output": "   \n   \n*  \n*  \n*  \n*  \n** \n** \n"
    },
    {
      "test_id": "ex03_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*       *\n**     **\n***   ***\n**** ****\n*********\n",
      "output": "         \n    *    \n   ***   \n  *****  \n ******* \n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "large",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
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


## sample_008 — validation

```c

#include <stdio.h>

#define VECMAX 100

int main(){
    int n, i, j, v[VECMAX], max;

    scanf("%d", &n);
    for(i=0; i<n; i++){
        scanf("%d", &v[i]);
        if(i==0||v[i] > max)
            max = v[i];
    }
    
    for(i=1; i<=max; i++){
        for(j = 0; j<n; j++){
            if(v[j] >= i)
                putchar ('*');
            else
                putchar(' ');
        }
        putchar('\n'); 
    }
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
  "source_sha256": "1da35f715d9ddaaeeef3d918f28a4fe4667dcd188328bffb2ca51d7b2699dfa9",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3 1 2 3",
      "expected": "  *\n **\n***\n",
      "output": "***\n **\n  *\n"
    },
    {
      "test_id": "ex03_1",
      "input": "3 2 6 8",
      "expected": "  *\n  *\n **\n **\n **\n **\n***\n***\n",
      "output": "***\n***\n **\n **\n **\n **\n  *\n  *\n"
    },
    {
      "test_id": "ex03_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*       *\n**     **\n***   ***\n**** ****\n*********\n",
      "output": "*********\n**** ****\n***   ***\n**     **\n*       *\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
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


## sample_009 — validation

```c

#include <stdio.h>
#define VECMAX 100

int main(){
    char ok = 1;
    int vec[VECMAX], n, i;
    scanf("%d", &n);
    for(i = 0; i < n; i++){
        scanf("%d", &vec[i]);
    }
    do{
        ok = 0;
        for(i = 1; i <= n; i++){
            if(vec[n - i] > 0){
                putchar('*');
                vec[n - i]--;
                ok = ok || vec[n - i] > 0;
            }
            else
                putchar(' ');
        }
        putchar('\n');
    } while (ok);
    return 0;
}

```

```json
{
  "sample_id": "sample_009",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "4895caae51a455bdc5a81dc1e703d58479cde1fdd2fb749bc3073091c9fedb27",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3 1 2 3",
      "expected": "  *\n **\n***\n",
      "output": "***\n** \n*  \n"
    },
    {
      "test_id": "ex03_1",
      "input": "3 2 6 8",
      "expected": "  *\n  *\n **\n **\n **\n **\n***\n***\n",
      "output": "***\n***\n** \n** \n** \n** \n*  \n*  \n"
    },
    {
      "test_id": "ex03_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*       *\n**     **\n***   ***\n**** ****\n*********\n",
      "output": "*********\n**** ****\n***   ***\n**     **\n*       *\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "large",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
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
#define VECMAX 100

int main(){
    int n,i,j,max=0,vec[VECMAX];
    scanf("%d",&n);
    for(i=0;i<n;i++){
        scanf("%d",&vec[i]);
        if (vec[i] > max)
            max = vec[i];
    }
    for (i=0;i<max;i++){
        for(j=0;j<n;j++){
            if ((i-vec[j])<0)
                printf("*");
            else
                printf(" ");
        }
        printf("\n");
    }
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
  "source_sha256": "0045a7ec15078eabba7a875b855bcf4f688d4c18c317372d1f9812ec774a8cff",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3 1 2 3",
      "expected": "  *\n **\n***\n",
      "output": "***\n **\n  *\n"
    },
    {
      "test_id": "ex03_1",
      "input": "3 2 6 8",
      "expected": "  *\n  *\n **\n **\n **\n **\n***\n***\n",
      "output": "***\n***\n **\n **\n **\n **\n  *\n  *\n"
    },
    {
      "test_id": "ex03_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*       *\n**     **\n***   ***\n**** ****\n*********\n",
      "output": "*********\n**** ****\n***   ***\n**     **\n*       *\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
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

#define VECMAX 100

int main()
{
    int n, vec[VECMAX], i, j, max;
    
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        scanf("%d", &vec[i]);
    }
    
    max = vec[0];
    for (i = 0; i < n;i++) {
        if (vec[i] > max)
            max = vec[i];
    }
    for (i = 0; i < max; i++) {
        for (j = 0; j < n; j++)
            printf("%c", (vec[j] > n - i) ? '*' : ' ');
        printf("\n");
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
  "source_sha256": "f27bc8f7a4e3d10073d0723da11055827c6969582db92dab0998a77c9d38bd74",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3 1 2 3",
      "expected": "  *\n **\n***\n",
      "output": "   \n  *\n **\n"
    },
    {
      "test_id": "ex03_1",
      "input": "3 2 6 8",
      "expected": "  *\n  *\n **\n **\n **\n **\n***\n***\n",
      "output": " **\n **\n***\n***\n***\n***\n***\n***\n"
    },
    {
      "test_id": "ex03_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*       *\n**     **\n***   ***\n**** ****\n*********\n",
      "output": "         \n         \n         \n         \n         \n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "1",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "large",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "1",
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

#define VECMAX 100

int main()
{
    int n, i, j, v, max = 0;
    int vec[VECMAX];

    
    scanf("%d", &n);

    
    for(i = 0; i < n ; i++)
    {
        scanf("%d", &v);
        if(v > max)
            max = v;
        vec[i] = v;
    }

    for(j = 1; j <= max; j++)
    {
        for(i = 0; i < n; i++)
        {
            if(j <= vec[i])
            {
                putchar('*');
            }
            else
                putchar(' ');
        }
        putchar('\n');        
    }



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
  "source_sha256": "d0a9742db9de509a9a7f46a98bed1d3ac839e4b7b710f02395c62592f3c4b6cb",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3 1 2 3",
      "expected": "  *\n **\n***\n",
      "output": "***\n **\n  *\n"
    },
    {
      "test_id": "ex03_1",
      "input": "3 2 6 8",
      "expected": "  *\n  *\n **\n **\n **\n **\n***\n***\n",
      "output": "***\n***\n **\n **\n **\n **\n  *\n  *\n"
    },
    {
      "test_id": "ex03_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*       *\n**     **\n***   ***\n**** ****\n*********\n",
      "output": "*********\n**** ****\n***   ***\n**     **\n*       *\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
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


## sample_013 — train

```c

#include <stdio.h>

#define VECMAX 100

int main () {
    int n, v[VECMAX], i = 0, max = 0, j = 0;
    scanf("%d", &n);
    while (i < n) {
        scanf("%d", &v[i]);
        if (v[i] > max)
            max = v[i];
        i++;
    }
    i = 0;
    while (i < n) {
        v[i] -= 4;
        i++;
    }
    while (j < max) {
        i = 0;
        while (i < n) {
            if (v[i] == 0)
                printf("*");
            else {
                printf(" ");
                v[i]++;
            }
            i++;
        }
        printf("\n");
        j++;
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
  "source_sha256": "2b46e9f26e2e90a12b6c059e5e65e59208af5ea96ec3b6124761136fa7acdb9e",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3 1 2 3",
      "expected": "  *\n **\n***\n",
      "output": "   \n  *\n **\n"
    },
    {
      "test_id": "ex03_1",
      "input": "3 2 6 8",
      "expected": "  *\n  *\n **\n **\n **\n **\n***\n***\n",
      "output": "   \n   \n*  \n*  \n*  \n*  \n*  \n*  \n"
    },
    {
      "test_id": "ex03_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*       *\n**     **\n***   ***\n**** ****\n*********\n",
      "output": " *     * \n **   ** \n *** *** \n ******* \n ******* \n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "large",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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


## sample_014 — validation

```c


#include <stdio.h>

#define VECMAX 100

void imprimir_linha(int val, int altura);

int main() {
    int n, i, j, linha, numeros[VECMAX], max_val = 0;
    
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        scanf("%d", &numeros[i]);
        if (numeros[i] > max_val)
            max_val = numeros[i];
    }
    
    printf("%d\n", max_val);

    for (linha = 0; linha < max_val; linha++) {
        for (j = 0; j < n; j++) {
            if (max_val - linha > numeros[j])
                putchar(' ');
            else
                putchar('*');
        }
        putchar('\n');
    }

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
  "source_sha256": "1488cde1d07dccfed3488d9a026cac4cb569df122ace5dd8e02b3a0211c8cf93",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3 1 2 3",
      "expected": "  *\n **\n***\n",
      "output": "3\n  *\n **\n***\n"
    },
    {
      "test_id": "ex03_1",
      "input": "3 2 6 8",
      "expected": "  *\n  *\n **\n **\n **\n **\n***\n***\n",
      "output": "8\n  *\n  *\n **\n **\n **\n **\n***\n***\n"
    },
    {
      "test_id": "ex03_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*       *\n**     **\n***   ***\n**** ****\n*********\n",
      "output": "5\n*       *\n**     **\n***   ***\n**** ****\n*********\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "small",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "small",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
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


## sample_016 — validation

```c


#include <stdio.h>
#define VECMAX 100

int main ()
{
    int i, j, n, v[VECMAX], maior = 0;

    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        scanf("%d", &v[i]);
        if (v[i] > maior)
            maior = v[i];
    }

    for (i = maior; i > 0; i--)
    {
        for (j = 0; j < n; j++)
        {
            v[j] >= i ? putchar('*') : putchar(' ');
            j != n - 1 ? putchar(' ') : putchar('\n');
        }
    }
    
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
  "source_sha256": "cd3989ebe6ef7096d8793cd23abe50aae5ac119557d484531677df49b51dbfe2",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3 1 2 3",
      "expected": "  *\n **\n***\n",
      "output": "    *\n  * *\n* * *\n"
    },
    {
      "test_id": "ex03_1",
      "input": "3 2 6 8",
      "expected": "  *\n  *\n **\n **\n **\n **\n***\n***\n",
      "output": "    *\n    *\n  * *\n  * *\n  * *\n  * *\n* * *\n* * *\n"
    },
    {
      "test_id": "ex03_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*       *\n**     **\n***   ***\n**** ****\n*********\n",
      "output": "*               *\n* *           * *\n* * *       * * *\n* * * *   * * * *\n* * * * * * * * *\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
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


## sample_017 — validation

```c


#include <stdio.h>
#define VECMAX 100

int max(int vec[],int n){
    int i=1;
    int mx=vec[0];
    while (i<n){
        if(vec[i]>mx)
            mx=vec[i];
        i++;
    }
    return mx;
}

int main(){
    int n,i,j,mx;
    int vec[VECMAX];
    scanf("%d",&n);
    for (i=0;i<n;i++)
       scanf("%d", &vec[i]);
    mx=max(vec,n);
    for (i=mx;i<=1;i--){
        for(j=0;j<n;j++) putchar(vec[j]>=i?'*':' ');
        putchar('\n');
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
  "source_sha256": "ac2c71079f08026157f4c6bd5bfe34bbc3df4e17e35dd977ac1792cdf141ba8f",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3 1 2 3",
      "expected": "  *\n **\n***\n",
      "output": ""
    },
    {
      "test_id": "ex03_1",
      "input": "3 2 6 8",
      "expected": "  *\n  *\n **\n **\n **\n **\n***\n***\n",
      "output": ""
    },
    {
      "test_id": "ex03_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*       *\n**     **\n***   ***\n**** ****\n*********\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "1",
    "stdout:ex03_0:relation": "empty",
    "stdout:ex03_0:edit_band": "large",
    "stdout:ex03_1:relation": "empty",
    "stdout:ex03_1:edit_band": "large",
    "stdout:ex03_2:relation": "empty",
    "stdout:ex03_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "1",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "1",
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

    #define VECMAX 100

    int main () {
        int n, i, j, m = -1, v[VECMAX];

        scanf("%d", &n);
        for(i = 0; i < n; i++) {
            scanf("%d", &v[i]);
            m = m < v[i] ? v[i] : m;
        }

    for(i = 0; i < m; i++) {
        for(j = 0; j < n; j++) {
            putchar(v[j]-- > 0 ? '*': ' ');
        }
        putchar('\n');
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
  "source_sha256": "827e5fdc2dd095077b8985d728058140f1ad83cae0b9c2aeb7d2fddb34d78fe1",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3 1 2 3",
      "expected": "  *\n **\n***\n",
      "output": "***\n **\n  *\n"
    },
    {
      "test_id": "ex03_1",
      "input": "3 2 6 8",
      "expected": "  *\n  *\n **\n **\n **\n **\n***\n***\n",
      "output": "***\n***\n **\n **\n **\n **\n  *\n  *\n"
    },
    {
      "test_id": "ex03_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*       *\n**     **\n***   ***\n**** ****\n*********\n",
      "output": "*********\n**** ****\n***   ***\n**     **\n*       *\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "medium",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "medium",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_019 — train

```c

#include <stdio.h>
#include <string.h>
#define MAX 80
#define YES 1
#define NO 0

int main(){
    char palavra[MAX];
    int tamanho,i,estado=YES;
    scanf("%s",palavra);
    tamanho = strlen(palavra);
    for (i=0; i<tamanho/2; i++)
        if (palavra[i]!=palavra[tamanho-i-1]){
            estado=NO;
            break;
        }
    if(estado==YES)
        printf("yes\n");
    else
        printf("no\n");
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
  "source_sha256": "6f2d025ba9d4b6583680c16a90656e848d45d9f388a9d6b193f34cfb2226e837",
  "outcomes": {
    "ex03_0": "fail",
    "ex03_1": "fail",
    "ex03_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex03_0",
      "input": "3 1 2 3",
      "expected": "  *\n **\n***\n",
      "output": "yes\n"
    },
    {
      "test_id": "ex03_1",
      "input": "3 2 6 8",
      "expected": "  *\n  *\n **\n **\n **\n **\n***\n***\n",
      "output": "yes\n"
    },
    {
      "test_id": "ex03_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*       *\n**     **\n***   ***\n**** ****\n*********\n",
      "output": "yes\n"
    }
  ],
  "clustering_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "0",
    "stdout:ex03_0:relation": "different",
    "stdout:ex03_0:edit_band": "large",
    "stdout:ex03_1:relation": "different",
    "stdout:ex03_1:edit_band": "large",
    "stdout:ex03_2:relation": "different",
    "stdout:ex03_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex03_0": "fail",
    "test:ex03_1": "fail",
    "test:ex03_2": "fail",
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
    "ast:c_address_of": "0",
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
  "members/sample_001/tests/ex03_1",
  "members/sample_001/tests/ex03_2",
  "members/sample_002/raw_code",
  "members/sample_002/tests/ex03_1",
  "members/sample_002/tests/ex03_2",
  "members/sample_003/raw_code",
  "members/sample_003/tests/ex03_1",
  "members/sample_003/tests/ex03_2",
  "members/sample_004/raw_code",
  "members/sample_004/tests/ex03_0",
  "members/sample_004/tests/ex03_1",
  "members/sample_004/tests/ex03_2",
  "members/sample_005/raw_code",
  "members/sample_005/tests/ex03_0",
  "members/sample_005/tests/ex03_1",
  "members/sample_005/tests/ex03_2",
  "members/sample_006/raw_code",
  "members/sample_006/tests/ex03_0",
  "members/sample_006/tests/ex03_1",
  "members/sample_006/tests/ex03_2",
  "members/sample_007/raw_code",
  "members/sample_007/tests/ex03_0",
  "members/sample_007/tests/ex03_1",
  "members/sample_007/tests/ex03_2",
  "members/sample_008/raw_code",
  "members/sample_008/tests/ex03_0",
  "members/sample_008/tests/ex03_1",
  "members/sample_008/tests/ex03_2",
  "members/sample_009/raw_code",
  "members/sample_009/tests/ex03_0",
  "members/sample_009/tests/ex03_1",
  "members/sample_009/tests/ex03_2",
  "members/sample_010/raw_code",
  "members/sample_010/tests/ex03_0",
  "members/sample_010/tests/ex03_1",
  "members/sample_010/tests/ex03_2",
  "members/sample_011/raw_code",
  "members/sample_011/tests/ex03_0",
  "members/sample_011/tests/ex03_1",
  "members/sample_011/tests/ex03_2",
  "members/sample_012/raw_code",
  "members/sample_012/tests/ex03_0",
  "members/sample_012/tests/ex03_1",
  "members/sample_012/tests/ex03_2",
  "members/sample_013/raw_code",
  "members/sample_013/tests/ex03_0",
  "members/sample_013/tests/ex03_1",
  "members/sample_013/tests/ex03_2",
  "members/sample_014/raw_code",
  "members/sample_014/tests/ex03_0",
  "members/sample_014/tests/ex03_1",
  "members/sample_014/tests/ex03_2",
  "members/sample_015/raw_code",
  "members/sample_015/tests/ex03_0",
  "members/sample_015/tests/ex03_1",
  "members/sample_015/tests/ex03_2",
  "members/sample_016/raw_code",
  "members/sample_016/tests/ex03_0",
  "members/sample_016/tests/ex03_1",
  "members/sample_016/tests/ex03_2",
  "members/sample_017/raw_code",
  "members/sample_017/tests/ex03_0",
  "members/sample_017/tests/ex03_1",
  "members/sample_017/tests/ex03_2",
  "members/sample_018/raw_code",
  "members/sample_018/tests/ex03_0",
  "members/sample_018/tests/ex03_1",
  "members/sample_018/tests/ex03_2",
  "members/sample_019/raw_code",
  "members/sample_019/tests/ex03_0",
  "members/sample_019/tests/ex03_1",
  "members/sample_019/tests/ex03_2"
]
```
