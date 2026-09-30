# lab04-ex01--kmeans--combined_stdout--s42--c1

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 12; phân vùng: {'train': 8, 'validation': 4}.


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
    "n_cluster": 12,
    "n_observed": 12,
    "n_failed": 12,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 12
    }
  },
  {
    "test_id": "ex01_1",
    "n_cluster": 12,
    "n_observed": 12,
    "n_failed": 12,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 12
    }
  },
  {
    "test_id": "ex01_2",
    "n_cluster": 12,
    "n_observed": 12,
    "n_failed": 12,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 12
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex01_0:relation",
    "value": "different",
    "n": 12,
    "n_cluster": 12,
    "rate": 1.0,
    "cohort_rate": 0.75,
    "difference_from_cohort": 0.25
  },
  {
    "feature": "stdout:ex01_1:relation",
    "value": "different",
    "n": 12,
    "n_cluster": 12,
    "rate": 1.0,
    "cohort_rate": 0.75,
    "difference_from_cohort": 0.25
  },
  {
    "feature": "stdout:ex01_0:edit_band",
    "value": "large",
    "n": 11,
    "n_cluster": 12,
    "rate": 0.9166666666666666,
    "cohort_rate": 0.6875,
    "difference_from_cohort": 0.22916666666666663
  },
  {
    "feature": "stdout:ex01_1:edit_band",
    "value": "large",
    "n": 10,
    "n_cluster": 12,
    "rate": 0.8333333333333334,
    "cohort_rate": 0.625,
    "difference_from_cohort": 0.20833333333333337
  },
  {
    "feature": "stdout:ex01_2:edit_band",
    "value": "large",
    "n": 10,
    "n_cluster": 12,
    "rate": 0.8333333333333334,
    "cohort_rate": 0.625,
    "difference_from_cohort": 0.20833333333333337
  },
  {
    "feature": "stdout:ex01_2:relation",
    "value": "different",
    "n": 12,
    "n_cluster": 12,
    "rate": 1.0,
    "cohort_rate": 0.8125,
    "difference_from_cohort": 0.1875
  },
  {
    "feature": "ast:c_array_parameter",
    "value": "0",
    "n": 10,
    "n_cluster": 12,
    "rate": 0.8333333333333334,
    "cohort_rate": 0.75,
    "difference_from_cohort": 0.08333333333333337
  },
  {
    "feature": "ast:c_while",
    "value": "0",
    "n": 12,
    "n_cluster": 12,
    "rate": 1.0,
    "cohort_rate": 0.9375,
    "difference_from_cohort": 0.0625
  },
  {
    "feature": "test:ex01_0",
    "value": "fail",
    "n": 12,
    "n_cluster": 12,
    "rate": 1.0,
    "cohort_rate": 0.9375,
    "difference_from_cohort": 0.0625
  },
  {
    "feature": "test:ex01_1",
    "value": "fail",
    "n": 12,
    "n_cluster": 12,
    "rate": 1.0,
    "cohort_rate": 0.9375,
    "difference_from_cohort": 0.0625
  },
  {
    "feature": "ast:c_if",
    "value": "0",
    "n": 6,
    "n_cluster": 12,
    "rate": 0.5,
    "cohort_rate": 0.4375,
    "difference_from_cohort": 0.0625
  },
  {
    "feature": "ast:c_subscript",
    "value": "0",
    "n": 2,
    "n_cluster": 12,
    "rate": 0.16666666666666666,
    "cohort_rate": 0.125,
    "difference_from_cohort": 0.04166666666666666
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 11,
    "n_cluster": 12,
    "rate": 0.9166666666666666,
    "cohort_rate": 0.875,
    "difference_from_cohort": 0.04166666666666663
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 7,
    "n_cluster": 12,
    "rate": 0.5833333333333334,
    "cohort_rate": 0.5625,
    "difference_from_cohort": 0.02083333333333337
  },
  {
    "feature": "test:ex01_2",
    "value": "fail",
    "n": 12,
    "n_cluster": 12,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "0",
    "n": 5,
    "n_cluster": 12,
    "rate": 0.4166666666666667,
    "cohort_rate": 0.4375,
    "difference_from_cohort": -0.020833333333333315
  },
  {
    "feature": "ast:c_subscript",
    "value": "1",
    "n": 10,
    "n_cluster": 12,
    "rate": 0.8333333333333334,
    "cohort_rate": 0.875,
    "difference_from_cohort": -0.04166666666666663
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "0",
    "n": 1,
    "n_cluster": 12,
    "rate": 0.08333333333333333,
    "cohort_rate": 0.125,
    "difference_from_cohort": -0.04166666666666667
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 6,
    "n_cluster": 12,
    "rate": 0.5,
    "cohort_rate": 0.5625,
    "difference_from_cohort": -0.0625
  },
  {
    "feature": "ast:c_array_parameter",
    "value": "1",
    "n": 2,
    "n_cluster": 12,
    "rate": 0.16666666666666666,
    "cohort_rate": 0.25,
    "difference_from_cohort": -0.08333333333333334
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 11,
    "n_cluster": 12,
    "rate": 0.9166666666666666,
    "cohort_rate": 0.875,
    "difference_from_cohort": 0.04166666666666663
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 7,
    "n_cluster": 12,
    "rate": 0.5833333333333334,
    "cohort_rate": 0.5625,
    "difference_from_cohort": 0.02083333333333337
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 12,
    "n_cluster": 12,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 12,
    "n_cluster": 12,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 12,
    "n_cluster": 12,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 11,
    "n_cluster": 12,
    "rate": 0.9166666666666666,
    "cohort_rate": 0.9375,
    "difference_from_cohort": -0.02083333333333337
  },
  {
    "feature": "ast:c_subscript",
    "value": "1",
    "n": 10,
    "n_cluster": 12,
    "rate": 0.8333333333333334,
    "cohort_rate": 0.875,
    "difference_from_cohort": -0.04166666666666663
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 6,
    "n_cluster": 12,
    "rate": 0.5,
    "cohort_rate": 0.5625,
    "difference_from_cohort": -0.0625
  }
]
```


## IF–THEN dự đoán cluster, không dự đoán gold

```json
[
  {
    "rule_id": 4,
    "if": [
      "stdout:ex01_0:relation=different"
    ],
    "then_cluster": 1,
    "train_support": 8,
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
  "reasoning": "Có 12 bài trong cụm. Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
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

sample_008, sample_010, sample_003, sample_001

## sample_001 — train — đại diện

```c
#include <stdio.h>

void quadrado(int n);

int main(){
    int n;
    scanf("%d", &n);
    if (n >=2)
        quadrado(n);
    return 0;
}


void quadrado(int n){
    int ad, linha;
        for(linha =1;linha <= n; ++linha){
            for(ad=0; ad < n; ++ad)
                if (ad < n-1)
                printf("%d\t", linha+ad);
                else
                printf("%d", linha+ad);
            printf("\n");
            }
}
           
```

```json
{
  "sample_id": "sample_001",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "455450e2d2e6d5db36475753d2179394484f30fe00ce37fb274474dcc30cb9d2",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3 1 2 3",
      "expected": "*\n**\n***\n",
      "output": "1\t2\t3\n2\t3\t4\n3\t4\t5\n"
    },
    {
      "test_id": "ex01_1",
      "input": "3 2 6 8",
      "expected": "**\n******\n********\n",
      "output": "1\t2\t3\n2\t3\t4\n3\t4\t5\n"
    },
    {
      "test_id": "ex01_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*****\n****\n***\n**\n*\n**\n***\n****\n*****\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t9\n2\t3\t4\t5\t6\t7\t8\t9\t10\n3\t4\t5\t6\t7\t8\t9\t10\t11\n4\t5\t6\t7\t8\t9\t10\t11\t12\n5\t6\t7\t8\t9\t10\t11\t12\t13\n6\t7\t8\t9\t10\t11\t12\t13\t14\n7\t8\t9\t10\t11\t12\t13\t14\t15\n8\t9\t10\t11\t12\t13\t14\t15\t16\n9\t10\t11\t12\t13\t14\t15\t16\t17\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_array_parameter": "0",
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_003 — validation — đại diện

```c
#include <stdio.h>
#include <string.h>

#define MAX 80

int main()
{
    char s[MAX];
    int l, i;
    
    scanf("%s", s);
    l = strlen(s);

    if(l % 2 == 0) 
    {
        for(i = 0; i <= (l / 2) - 1; i++)
        {
            if(s[i] != s[l - i - 1])
            {
                printf("no\n");
                return 0;
            }
        }

        printf("yes\n");
        return 0;
    }
    else 
    {
        for(i = 0; i <= (l - 3) / 2; i++)
        {
            if(s[i] != s[l - i - 1])
            {
                printf("no\n");
                return 0;
            }
        }

        printf("yes\n");
        return 0;
    }
}
```

```json
{
  "sample_id": "sample_003",
  "partition": "validation",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "17af6153796cf577234f38b0186557cfe7239c6221ce15acf213fe66cef06ee1",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3 1 2 3",
      "expected": "*\n**\n***\n",
      "output": "yes\n"
    },
    {
      "test_id": "ex01_1",
      "input": "3 2 6 8",
      "expected": "**\n******\n********\n",
      "output": "yes\n"
    },
    {
      "test_id": "ex01_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*****\n****\n***\n**\n*\n**\n***\n****\n*****\n",
      "output": "yes\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "0",
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
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


## sample_008 — train — đại diện

```c

#include <stdio.h>

#define VECMAX 100

int main()
{
    int i,n, vec[VECMAX];
    scanf("%d", &n);

    if (n > VECMAX)
    {
        return 1;
    }

    for(i = 0; i<n; i++)
    {
        scanf("%d", &vec[i]);
    }

    for(i = 0; i <= n-1 ; i++)
    {
        printf("%d ", vec[i]);
    }

    return 0;
}
```

```json
{
  "sample_id": "sample_008",
  "partition": "train",
  "representative": true,
  "is_train_medoid": true,
  "raw_code_truncated": false,
  "source_sha256": "43dca3797b60e0cca56f28c42980138601643463eb1eb43249cc1f4475a763d7",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3 1 2 3",
      "expected": "*\n**\n***\n",
      "output": "1 2 3 "
    },
    {
      "test_id": "ex01_1",
      "input": "3 2 6 8",
      "expected": "**\n******\n********\n",
      "output": "2 6 8 "
    },
    {
      "test_id": "ex01_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*****\n****\n***\n**\n*\n**\n***\n****\n*****\n",
      "output": "5 4 3 2 1 2 3 4 5 "
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "0",
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_010 — train — đại diện

```c

#include <stdio.h>
#define VECMAX 100 

void print_piramide(int array[VECMAX], int n) {
    int i,j;
    for (i=0;i<n;i++) {
        for (j=0;j<array[i];j++) {
            putchar('*');

        }
    }
}

int main() {
    int n,array[VECMAX],i;
    scanf("%d", &n);
    for(i=0;i<n;i++) {
        scanf("%d",&array[i]);
    }
    print_piramide(array,n);
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
  "source_sha256": "10950d2fc26fa7be2ba3bd848f9922f0b2da6d392611aef2921034446dcba314",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3 1 2 3",
      "expected": "*\n**\n***\n",
      "output": "******"
    },
    {
      "test_id": "ex01_1",
      "input": "3 2 6 8",
      "expected": "**\n******\n********\n",
      "output": "****************"
    },
    {
      "test_id": "ex01_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*****\n****\n***\n**\n*\n**\n***\n****\n*****\n",
      "output": "*****************************"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_002 — train

```c
#include <stdio.h>

#define VECMAX 100



int main() {
	int valores[VECMAX], n, i, j;

	printf("Insira quantos números quer inserir -> ");
	scanf("%d", &n);
	for (i = 0; (i < n && i < VECMAX); i++) {
		printf("Insira o %dº número -> ", i + 1);
		scanf("%d", &valores[i]);
	}
	for (i = 0; i < n; i++) {
		for (j = 0; j < valores[i]; j++)
			printf("*");
		printf("\n");
	}

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
  "source_sha256": "bca1e6e2c0250bd9d7cb58ec4d682a0f74ce57f73771b7de5ea04da4c1d00411",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3 1 2 3",
      "expected": "*\n**\n***\n",
      "output": "Insira quantos números quer inserir -> Insira o 1º número -> Insira o 2º número -> Insira o 3º número -> *\n**\n***\n"
    },
    {
      "test_id": "ex01_1",
      "input": "3 2 6 8",
      "expected": "**\n******\n********\n",
      "output": "Insira quantos números quer inserir -> Insira o 1º número -> Insira o 2º número -> Insira o 3º número -> **\n******\n********\n"
    },
    {
      "test_id": "ex01_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*****\n****\n***\n**\n*\n**\n***\n****\n*****\n",
      "output": "Insira quantos números quer inserir -> Insira o 1º número -> Insira o 2º número -> Insira o 3º número -> Insira o 4º número -> Insira o 5º número -> Insira o 6º número -> Insira o 7º número -> Insira o 8º número -> Insira o 9º número -> *****\n****\n***\n**\n*\n**\n***\n****\n*****\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "0",
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_004 — validation

```c
#include <stdio.h>

#define VECMAX 100
int main(){
    int graf[VECMAX], n, i, j;
    
    printf("Introduza um inteiro positivo menor que 100.\n");
    scanf("%d", &n);
    for(i = 0; i < n; i++){
        printf("Introduza um inteiro positivo. %d/%d\n", i + 1, n);
        scanf("%d", &graf[i]);
    }
    for(i = 0; i < n; i++){
        for(j = 0; j < graf[i]; j++)
            printf("*");
        printf("\n");
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_004",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "713895201909f77a5d068f41aded6f624ea77f7d393044ea13a608ab8110cc79",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3 1 2 3",
      "expected": "*\n**\n***\n",
      "output": "Introduza um inteiro positivo menor que 100.\nIntroduza um inteiro positivo. 1/3\nIntroduza um inteiro positivo. 2/3\nIntroduza um inteiro positivo. 3/3\n*\n**\n***\n"
    },
    {
      "test_id": "ex01_1",
      "input": "3 2 6 8",
      "expected": "**\n******\n********\n",
      "output": "Introduza um inteiro positivo menor que 100.\nIntroduza um inteiro positivo. 1/3\nIntroduza um inteiro positivo. 2/3\nIntroduza um inteiro positivo. 3/3\n**\n******\n********\n"
    },
    {
      "test_id": "ex01_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*****\n****\n***\n**\n*\n**\n***\n****\n*****\n",
      "output": "Introduza um inteiro positivo menor que 100.\nIntroduza um inteiro positivo. 1/9\nIntroduza um inteiro positivo. 2/9\nIntroduza um inteiro positivo. 3/9\nIntroduza um inteiro positivo. 4/9\nIntroduza um inteiro positivo. 5/9\nIntroduza um inteiro positivo. 6/9\nIntroduza um inteiro positivo. 7/9\nIntroduza um inteiro positivo. 8/9\nIntroduza um inteiro positivo. 9/9\n*****\n****\n***\n**\n*\n**\n***\n****\n*****\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "0",
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_005 — train

```c
#include <stdio.h>

int main()
{
  int N, row, col, passo = 0;

  scanf("%d", &N);
  for (row = 0; row < N; row++)
  {
    for (col = 1; col <= N; col++)
    {
      if (col == N)
        printf("%d\n", col + passo);
      else
        printf("%d\t", col + passo);
    }
    passo++;
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
  "source_sha256": "6fc5056b466c71794953336de4d62e2b4ae68fc024d7b3a8a0d02b74a4bda8e7",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3 1 2 3",
      "expected": "*\n**\n***\n",
      "output": "1\t2\t3\n2\t3\t4\n3\t4\t5\n"
    },
    {
      "test_id": "ex01_1",
      "input": "3 2 6 8",
      "expected": "**\n******\n********\n",
      "output": "1\t2\t3\n2\t3\t4\n3\t4\t5\n"
    },
    {
      "test_id": "ex01_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*****\n****\n***\n**\n*\n**\n***\n****\n*****\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t9\n2\t3\t4\t5\t6\t7\t8\t9\t10\n3\t4\t5\t6\t7\t8\t9\t10\t11\n4\t5\t6\t7\t8\t9\t10\t11\t12\n5\t6\t7\t8\t9\t10\t11\t12\t13\n6\t7\t8\t9\t10\t11\t12\t13\t14\n7\t8\t9\t10\t11\t12\t13\t14\t15\n8\t9\t10\t11\t12\t13\t14\t15\t16\n9\t10\t11\t12\t13\t14\t15\t16\t17\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_array_parameter": "0",
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
#include<stdio.h>
#define VECMAX 100

int max( int v[], int n){
    int i, m = 0;

    for ( i = 0; i < n; i++)
        if (v[i] > m)
            m = v[i];
    
    return m;
    
}


int main(){
    int n, m, l,i,c;
    int v[VECMAX];

    printf("qual o n? dp introduz n numeros\n");
    scanf("%d",&n);
    printf("\n");
    for ( i = 0; i < n; i++)
        scanf("%d",&v[i]);
    
    m = max(v,n);


    for (l = 0; l < n ; l++){
        for ( c = 1; c <= m; c++){
            if (v[l] >= c)
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
  "source_sha256": "0bd64952140a56291a5b17407932d1880a197f13f1c20591bec403190ebf2ac5",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3 1 2 3",
      "expected": "*\n**\n***\n",
      "output": "qual o n? dp introduz n numeros\n\n*  \n** \n***\n"
    },
    {
      "test_id": "ex01_1",
      "input": "3 2 6 8",
      "expected": "**\n******\n********\n",
      "output": "qual o n? dp introduz n numeros\n\n**      \n******  \n********\n"
    },
    {
      "test_id": "ex01_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*****\n****\n***\n**\n*\n**\n***\n****\n*****\n",
      "output": "qual o n? dp introduz n numeros\n\n*****\n**** \n***  \n**   \n*    \n**   \n***  \n**** \n*****\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "different",
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
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
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


## sample_007 — validation

```c
#include <stdio.h>

#define VECMAX 100

int main()
{
    int n, i, j, arr[VECMAX];

    printf("Insira um número: ");
    scanf("%d", &n);

    for (j = 0; j < n; j++) {
        printf("Insira o %dº número: ", j+1);
        scanf("%d", &arr[j]);
    }

    for (j = 0; j <= n; j++) {
        for (i = 0; i < arr[j]; i++)
            printf("*");
        printf("\n");
    }

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
  "source_sha256": "6c6c8b3239c49c0c6105785b8d812b4434c59d72ac537e7db963ff143632e55c",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3 1 2 3",
      "expected": "*\n**\n***\n",
      "output": "Insira um número: Insira o 1º número: Insira o 2º número: Insira o 3º número: *\n**\n***\n\n"
    },
    {
      "test_id": "ex01_1",
      "input": "3 2 6 8",
      "expected": "**\n******\n********\n",
      "output": "Insira um número: Insira o 1º número: Insira o 2º número: Insira o 3º número: **\n******\n********\n\n"
    },
    {
      "test_id": "ex01_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*****\n****\n***\n**\n*\n**\n***\n****\n*****\n",
      "output": "Insira um número: Insira o 1º número: Insira o 2º número: Insira o 3º número: Insira o 4º número: Insira o 5º número: Insira o 6º número: Insira o 7º número: Insira o 8º número: Insira o 9º número: *****\n****\n***\n**\n*\n**\n***\n****\n*****\n\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "0",
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_009 — train

```c

#include <stdio.h>

#define VECMAX 100

int main()
{
    int i,n, vec[VECMAX];
    scanf("%d", &n);

    if (n > VECMAX)
    {
        return 1;
    }

    for(i = 0; i<n; i++)
    {
        scanf("%d", &vec[i]);
    }

    for(i = 0; i <= n-1 ; i++){
        printf("%d ", vec[i]);
    }

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
  "source_sha256": "8d6195a9ad38374f728100babf701c87f148c349ed76c9c7aa006add1d302c48",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3 1 2 3",
      "expected": "*\n**\n***\n",
      "output": "1 2 3 "
    },
    {
      "test_id": "ex01_1",
      "input": "3 2 6 8",
      "expected": "**\n******\n********\n",
      "output": "2 6 8 "
    },
    {
      "test_id": "ex01_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*****\n****\n***\n**\n*\n**\n***\n****\n*****\n",
      "output": "5 4 3 2 1 2 3 4 5 "
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "0",
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_011 — train

```c


#include<stdio.h>

#define VECMAX 100

int main(){
    int n, v[VECMAX],i,j;
    scanf("%d", &n);
    for (i=0;i<VECMAX;i++)
        scanf("%d", &v[i]); 
    for (i=0; i<n; i++){
        for (j=0; j<v[i];i++)
            putchar('*');
        putchar('\n'); 
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
  "source_sha256": "813d6a295d067786111daddb3366af454b6e42fcdb71c832febbcac0edcc6be3",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3 1 2 3",
      "expected": "*\n**\n***\n",
      "output": "********\n"
    },
    {
      "test_id": "ex01_1",
      "input": "3 2 6 8",
      "expected": "**\n******\n********\n",
      "output": "********\n"
    },
    {
      "test_id": "ex01_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*****\n****\n***\n**\n*\n**\n***\n****\n*****\n",
      "output": "*********\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "0",
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_012 — validation

```c

#include <stdio.h>
#define VECMAX 100

int main(){
    int n,i,j;
    int vec[VECMAX];
    scanf("%d",&n);
    for (i=0;i<n;i++)
        scanf("%d", &vec[i]);
    for (i=0;i<n;i++){
        for (j=0;j<vec[j];j++)
            putchar('*');
        putchar('\n');
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_012",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "8fa0b6e47896ee2241dcf44d8e723b4c3d169674ab7e664deb22b22d8a03bf9d",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3 1 2 3",
      "expected": "*\n**\n***\n",
      "output": "********\n********\n********\n"
    },
    {
      "test_id": "ex01_1",
      "input": "3 2 6 8",
      "expected": "**\n******\n********\n",
      "output": "********\n********\n********\n"
    },
    {
      "test_id": "ex01_2",
      "input": "9 5 4 3 2 1 2 3 4 5",
      "expected": "*****\n****\n***\n**\n*\n**\n***\n****\n*****\n",
      "output": "***\n***\n***\n***\n***\n***\n***\n***\n***\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "0",
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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
  "members/sample_012/tests/ex01_2"
]
```
