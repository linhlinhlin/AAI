# lab02-ex02--kmeans--combined_stdout--s42--c0

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 43; phân vùng: {'train': 33, 'validation': 10}.


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
    "n_cluster": 43,
    "n_observed": 43,
    "n_failed": 43,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 43
    }
  },
  {
    "test_id": "ex02_1",
    "n_cluster": 43,
    "n_observed": 43,
    "n_failed": 41,
    "n_not_run": 0,
    "failure_rate_observed": 0.9534883720930233,
    "failure_rate_cluster": 0.9534883720930233,
    "outcome_counts": {
      "fail": 41,
      "pass": 2
    }
  },
  {
    "test_id": "ex02_2",
    "n_cluster": 43,
    "n_observed": 43,
    "n_failed": 41,
    "n_not_run": 0,
    "failure_rate_observed": 0.9534883720930233,
    "failure_rate_cluster": 0.9534883720930233,
    "outcome_counts": {
      "fail": 41,
      "pass": 2
    }
  },
  {
    "test_id": "ex02_3",
    "n_cluster": 43,
    "n_observed": 43,
    "n_failed": 41,
    "n_not_run": 0,
    "failure_rate_observed": 0.9534883720930233,
    "failure_rate_cluster": 0.9534883720930233,
    "outcome_counts": {
      "fail": 41,
      "pass": 2
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex02_0:relation",
    "value": "whitespace",
    "n": 42,
    "n_cluster": 43,
    "rate": 0.9767441860465116,
    "cohort_rate": 0.41904761904761906,
    "difference_from_cohort": 0.5576965669988925
  },
  {
    "feature": "stdout:ex02_0:edit_band",
    "value": "medium",
    "n": 42,
    "n_cluster": 43,
    "rate": 0.9767441860465116,
    "cohort_rate": 0.4380952380952381,
    "difference_from_cohort": 0.5386489479512735
  },
  {
    "feature": "stdout:ex02_1:relation",
    "value": "whitespace",
    "n": 41,
    "n_cluster": 43,
    "rate": 0.9534883720930233,
    "cohort_rate": 0.4380952380952381,
    "difference_from_cohort": 0.5153931339977852
  },
  {
    "feature": "stdout:ex02_2:relation",
    "value": "whitespace",
    "n": 41,
    "n_cluster": 43,
    "rate": 0.9534883720930233,
    "cohort_rate": 0.4380952380952381,
    "difference_from_cohort": 0.5153931339977852
  },
  {
    "feature": "stdout:ex02_3:relation",
    "value": "whitespace",
    "n": 41,
    "n_cluster": 43,
    "rate": 0.9534883720930233,
    "cohort_rate": 0.4380952380952381,
    "difference_from_cohort": 0.5153931339977852
  },
  {
    "feature": "stdout:ex02_1:edit_band",
    "value": "medium",
    "n": 41,
    "n_cluster": 43,
    "rate": 0.9534883720930233,
    "cohort_rate": 0.4857142857142857,
    "difference_from_cohort": 0.4677740863787376
  },
  {
    "feature": "stdout:ex02_2:edit_band",
    "value": "small",
    "n": 35,
    "n_cluster": 43,
    "rate": 0.813953488372093,
    "cohort_rate": 0.38095238095238093,
    "difference_from_cohort": 0.4330011074197121
  },
  {
    "feature": "stdout:ex02_3:edit_band",
    "value": "medium",
    "n": 37,
    "n_cluster": 43,
    "rate": 0.8604651162790697,
    "cohort_rate": 0.6857142857142857,
    "difference_from_cohort": 0.17475083056478402
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 42,
    "n_cluster": 43,
    "rate": 0.9767441860465116,
    "cohort_rate": 0.8761904761904762,
    "difference_from_cohort": 0.1005537098560354
  },
  {
    "feature": "test:ex02_0",
    "value": "fail",
    "n": 43,
    "n_cluster": 43,
    "rate": 1.0,
    "cohort_rate": 0.9047619047619048,
    "difference_from_cohort": 0.09523809523809523
  },
  {
    "feature": "stdout:ex02_3:edit_band",
    "value": "small",
    "n": 4,
    "n_cluster": 43,
    "rate": 0.09302325581395349,
    "cohort_rate": 0.0380952380952381,
    "difference_from_cohort": 0.05492801771871539
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 9,
    "n_cluster": 43,
    "rate": 0.20930232558139536,
    "cohort_rate": 0.17142857142857143,
    "difference_from_cohort": 0.03787375415282393
  },
  {
    "feature": "ast:c_for",
    "value": "0",
    "n": 43,
    "n_cluster": 43,
    "rate": 1.0,
    "cohort_rate": 0.9809523809523809,
    "difference_from_cohort": 0.01904761904761909
  },
  {
    "feature": "ast:c_update",
    "value": "0",
    "n": 43,
    "n_cluster": 43,
    "rate": 1.0,
    "cohort_rate": 0.9809523809523809,
    "difference_from_cohort": 0.01904761904761909
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "0",
    "n": 9,
    "n_cluster": 43,
    "rate": 0.20930232558139536,
    "cohort_rate": 0.19047619047619047,
    "difference_from_cohort": 0.018826135105204894
  },
  {
    "feature": "stdout:ex02_1:edit_band",
    "value": "__unknown__",
    "n": 2,
    "n_cluster": 43,
    "rate": 0.046511627906976744,
    "cohort_rate": 0.02857142857142857,
    "difference_from_cohort": 0.017940199335548173
  },
  {
    "feature": "stdout:ex02_1:relation",
    "value": "__unknown__",
    "n": 2,
    "n_cluster": 43,
    "rate": 0.046511627906976744,
    "cohort_rate": 0.02857142857142857,
    "difference_from_cohort": 0.017940199335548173
  },
  {
    "feature": "stdout:ex02_3:edit_band",
    "value": "__unknown__",
    "n": 2,
    "n_cluster": 43,
    "rate": 0.046511627906976744,
    "cohort_rate": 0.02857142857142857,
    "difference_from_cohort": 0.017940199335548173
  },
  {
    "feature": "stdout:ex02_3:relation",
    "value": "__unknown__",
    "n": 2,
    "n_cluster": 43,
    "rate": 0.046511627906976744,
    "cohort_rate": 0.02857142857142857,
    "difference_from_cohort": 0.017940199335548173
  },
  {
    "feature": "test:ex02_1",
    "value": "pass",
    "n": 2,
    "n_cluster": 43,
    "rate": 0.046511627906976744,
    "cohort_rate": 0.02857142857142857,
    "difference_from_cohort": 0.017940199335548173
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 42,
    "n_cluster": 43,
    "rate": 0.9767441860465116,
    "cohort_rate": 0.8761904761904762,
    "difference_from_cohort": 0.1005537098560354
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 43,
    "n_cluster": 43,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 43,
    "n_cluster": 43,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 34,
    "n_cluster": 43,
    "rate": 0.7906976744186046,
    "cohort_rate": 0.8095238095238095,
    "difference_from_cohort": -0.018826135105204922
  }
]
```


## IF–THEN dự đoán cluster, không dự đoán gold

```json
[
  {
    "rule_id": 2,
    "if": [
      "NOT (stdout:ex02_0:relation=different)",
      "NOT (stdout:ex02_0:relation=__unknown__)"
    ],
    "then_cluster": 0,
    "train_support": 33,
    "train_precision": 1.0,
    "holdout_support": 11,
    "holdout_precision": 0.8181818181818182
  }
]
```


## Candidate chưa xác thực

```json
{
  "source": "local_heuristic_not_gold",
  "misconception_name": "Chưa đủ bằng chứng để đặt tên lỗi",
  "misconception_type": null,
  "reasoning": "Có 43 bài trong cụm. Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
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

sample_002, sample_006, sample_001, sample_033

## sample_001 — train — đại diện

```c
#include <stdio.h>

int main() {
    int N, M;
    scanf("%d %d", &N, &M);
    if(N <= M) 
        printf("%d \n%d \n", N, M); 
    else
        printf("%d \n%d \n", M, N);
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
  "source_sha256": "a317c0123a8994cbf9eb638cb0a9704bfaee368c6baa580cf261d9e1ae149888",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1 \n2 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2 \n6 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1 \n10 \n"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7 \n20 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "medium",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_002 — train — đại diện

```c


#include <stdio.h>



int main(){
    
    int N, M;
    
    scanf("%d%d",&M,&N);

    if(N<M){
        printf("%d\n%d",N,M);
    }
    else{
        printf("%d\n%d",M,N);
    }
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
  "source_sha256": "504d8c0b3b90e4027d1b2be85100b2ca66ff1d811e6e6f441814eb9aca1625aa",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_006 — train — đại diện

```c

#include <stdio.h>

int main()
{
    int num1, num2;

    scanf("%d%d", &num1, &num2);

    if (num2 > num1)
    {
        printf("%d\n%d", num1, num2);
    }
    else
    {
        printf("%d\n%d\n", num2, num1);
    }

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
  "source_sha256": "a112e9a562add11acccc941c563117f4a08d0569b7e7d6639428d2b2a010396f",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "pass",
    "ex02_2": "pass",
    "ex02_3": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "pass",
    "test:ex02_2": "pass",
    "test:ex02_3": "pass",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "__unknown__",
    "stdout:ex02_1:edit_band": "__unknown__",
    "stdout:ex02_2:relation": "__unknown__",
    "stdout:ex02_2:edit_band": "__unknown__",
    "stdout:ex02_3:relation": "__unknown__",
    "stdout:ex02_3:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "pass",
    "test:ex02_2": "pass",
    "test:ex02_3": "pass",
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


## sample_033 — train — đại diện

```c

#include <stdio.h>

int main(){
    int N, M;
    scanf("%d %d", &N, &M);
    printf("%d\n%d", (N<M ? N : M) , (N<M ? M : N));

    return 0;
}
```

```json
{
  "sample_id": "sample_033",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "1c12beba5f5effe841e025972f1cff151d7028037972e714e1132c3d7779a002",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_003 — train

```c


#include <stdio.h>

int main()
{
    int num1, num2;

    scanf("%d %d", &num1, &num2);
    if (num1 < num2)
    {
        printf("%d\n%d", num1, num2);
        return 0;
    }
     
    else 
    {
        printf("%d\n%d", num2, num1);
        return 0;
    }
    
}


```

```json
{
  "sample_id": "sample_003",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "5cffa5ef743865621afc79062ee55f43ea5b650f6bac77391ed19f31d8a871ba",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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

int main()
{
    int num1, num2;

    scanf("%d %d", &num1, &num2);
    if (num1 < num2)
    {
        printf("%d\n%d", num1, num2);
        return 0;
    }
     
    else 
    {
        printf("%d\n%d", num2, num1);
        return 0;
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
  "source_sha256": "70040a7abff62ca1e9dd4993be790d1d1fd53a314772e5115807353cbe1641fd",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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

int main(){

    int num1, num2;

    scanf("%d", &num1);
    scanf("%d", &num2);

    if (num1 > num2)
        printf("%d\n%d", num2, num1);
    
    else
        printf("%d\n%d", num1, num2);
 
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
  "source_sha256": "b65b1593e3580a93e839eb00e297a563769838544182052159fd9bb3862419e7",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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

int main()
{
    int num1, num2;

    scanf("%d%d", &num1, &num2);

    if (num2 > num1)
    {
        printf("%d\n%d", num1, num2);
    }
    else
    {
        printf("%d\n%d", num2, num1);
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
  "source_sha256": "405d12f2bddbe022da8fd2620187b17212295fac7313ea5d8458be3b62e27c0b",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_008 — train

```c

#include <stdio.h>

int main()
{
    int num1, num2;

    scanf("%d%d", &num1, &num2);

    if (num1 > num2)
    {
        printf("%d\n%d", num2, num1);
    }
    else
    {
        printf("%d\n%d", num1, num2);
    }

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
  "source_sha256": "3a9efbba686e34e510f3a9c8dd3c1946476ff79239dabf35175019f9e42bde34",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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

int main()
{
    int N, M;
    scanf("%d %d", &N, &M);
    if (M > N)
        printf("%d\n%d", N, M);
    else
        printf("%d\n%d", M, N);
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
  "source_sha256": "5ae7bfa375614ed4fd30f2f282ce918b9eaee2168415dc03d7e4f2a0887279ff",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_010 — train

```c

#include <stdio.h>

int main(){
    int x,y;
    scanf("%d %d", &x ,&y);
    if (x<=y)
    {
        printf("%d\n %d\n",x,y);
    }
    else{
        printf("%d\n %d\n",y,x);
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
  "source_sha256": "fcce86375df4c8f06771bcba97406d21c57e8b66fc5dfbdc64f1528665aa8fb3",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n 2\n"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n 6\n"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n 10\n"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n 20\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_011 — train

```c

#include <stdio.h>

int main(){
    int x,y;
    scanf("%d %d", &x ,&y);
    if (x<=y)
    {
        printf("%d\n %d\n",x,y);
    }
    else{
        printf("%d\n %d\n",y,x);
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
  "source_sha256": "b5e934fc0f0aa02e5c9b919740c81c63088a83e63a22cb1dd8dc904d7535cb83",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n 2\n"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n 6\n"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n 10\n"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n 20\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_012 — validation

```c

#include <stdio.h>

int main()
{
    int maior;
    int menor;
    scanf("%d%d", &maior, &menor);
    if (maior<menor)
    {
        printf("%d\n%d", maior, menor);
    }
    else 
    {
        printf("%d\n%d", menor, maior);
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
  "source_sha256": "9ae372b19996f77ac252754d3bcdc41188e7482fa8f588e49cdf08e032d18551",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_013 — validation

```c

#include <stdio.h>

int main()
{
    int num1;
    int num2;
    scanf("%d%d", &num1, &num2);
    if (num1<num2)
        printf("%d\n%d", num1, num2);
    
    if (num1>num2)
        printf("%d\n%d", num2, num1);
    
return 0;
}

```

```json
{
  "sample_id": "sample_013",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "fcaec173719b18e3a96f6e46fe0af79e087ee19b2089717739c13d57f896dfde",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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
    int maior;
    int menor;
    scanf("%d%d", &maior, &menor);
    if (maior<menor)
    {
        printf("%d\n%d", maior, menor);
    }
    else 
    {
        printf("%d\n%d", menor, maior);
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
  "source_sha256": "9ae372b19996f77ac252754d3bcdc41188e7482fa8f588e49cdf08e032d18551",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_015 — validation

```c

#include <stdio.h>

int main()
{
    int maior;
    int menor;
    scanf("%d%d", &maior, &menor);
    if (maior<menor)
    {
        printf("%d\n%d", maior, menor);
    }
    else 
    {
        printf("%d\n%d", menor, maior);
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
  "source_sha256": "cc7e5b56189067487334e47ea65108d8bea159b28f38bec10063abdbb95b8e5a",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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
    int maior = 0;
    int menor = 0;

    scanf("%d", &maior);
    scanf("%d", &menor);

    if(menor > maior){
        printf("%d \n", maior);
        printf("%d", menor);
    } 
    else {
        printf("%d \n", menor);
        printf("%d", maior);
    }

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
  "source_sha256": "71a20f87c171a20563bc9dc32ad67c9cd26d9340dd52498627ce2712b4f6450f",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1 \n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2 \n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1 \n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7 \n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "medium",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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

int main()
{
    int M, N;
    scanf("%d",&M);
    scanf("%d",&N);

    if (M < N)
    {
        printf("%d\n%d",M,N);
    }
    else
    {
        printf("%d\n%d\n",N,M);
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
  "source_sha256": "75f20115b10a50ba3e2d0671817bd67c4171dd02a6f82bf7a23f753c2bc1f423",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "pass",
    "ex02_2": "pass",
    "ex02_3": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "pass",
    "test:ex02_2": "pass",
    "test:ex02_3": "pass",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "__unknown__",
    "stdout:ex02_1:edit_band": "__unknown__",
    "stdout:ex02_2:relation": "__unknown__",
    "stdout:ex02_2:edit_band": "__unknown__",
    "stdout:ex02_3:relation": "__unknown__",
    "stdout:ex02_3:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "pass",
    "test:ex02_2": "pass",
    "test:ex02_3": "pass",
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


## sample_018 — train

```c

#include <stdio.h>
int main()
{
    int N, M;
    scanf("%d\t%d", &N, &M);
    if(N>M)
    {
        printf("%d\n", M);
        printf("%d", N);
    }
    else
    {
        printf("%d\n", N);
        printf("%d", M);
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
  "source_sha256": "8187755933243f17718e477db548044bfaf6417772d5635db8bf718fff525f19",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_019 — train

```c

#include <stdio.h>
int main()
{
    int N, M;
    scanf("%d\t%d", &N, &M);
    if(N>M)
    {
        printf("%d\n", M);
        printf("%d", N);
    }
    if(N<M)
    {
        printf("%d\n", N);
        printf("%d", M);
    }
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
  "source_sha256": "b8dd2f7cdb5e3797d601e5bbfab5fb627f690cc8bdba91e40b7e39b9086967f0",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_020 — train

```c

#include <stdio.h>
int main()
{
    int N, M;
    scanf("%d\t%d", &N, &M);
    if(N>M)
    {
        printf("%d\n", M);
        printf("%d", N);
    }
    if(M>N)
    {
        printf("%d\n", N);
        printf("%d", M);
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
  "source_sha256": "e5cd7b336dfb8b5e30386757eb8f00071f48714f5354dec845ca770a57f962be",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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
int main () {
    int M, N, menor, maior;
    scanf("%d%d", &M, &N);
    if (M < N) {
        menor = M;
        maior = N;
    }
    else {
        menor = N;
        maior = M;
    }
    printf("%d\n%d", menor, maior);
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
  "source_sha256": "440d8ffe3b92ff3664a66a35afbd726096e499fda4b36a6052e603be39ff4be9",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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

int main (){

    int N, M;

    scanf("%d %d", &N, &M);
    if (N < M)
        printf("%d \n %d\n", N, M);
    else
        printf("%d \n %d\n", M, N);
    
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
  "source_sha256": "45e3549131d6eaa78928c1320c64b5f68a73ce352a74ab0821acbff18c206ad2",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1 \n 2\n"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2 \n 6\n"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1 \n 10\n"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7 \n 20\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "medium",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_023 — train

```c

#include <stdio.h>

int main (){

    int N, M;

    scanf("%d %d", &N, &M);
    if (N < M)
        printf("%d \n %d", N, M);
    else
        printf("%d \n %d", M, N);
    
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
  "source_sha256": "70f35c9494c0826bcf7448aa48010b709378aabd6a28a4bf22fe32171c320d91",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1 \n 2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2 \n 6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1 \n 10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7 \n 20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "medium",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_024 — train

```c

#include <stdio.h>

int biggest(int N, int M){
    if (M>N)
    {
        printf("%d\n%d",N,M);
    }
    else{
        printf("%d\n%d",M,N);
    }
    return 0;
}
int main(){
    int N,M;
    scanf("%d %d", &N, &M);
    biggest(N,M);
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
  "source_sha256": "9d351b265d4a14f90c6e3c9f468e17a0359edee85ca55e634cab060febd2d3f7",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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

int main()
{
    int N, M;


    scanf("%d %d", &N, &M);

    if( N > M )
    {
        printf("%d\n", M);
        printf("\n");
        printf("%d\n", N);
    }
    else
    {
        printf("%d\n",N);
        printf("\n");
        printf("%d\n", M);
    }

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
  "source_sha256": "f602351de989ccf31d08a713b995ec0c9d3e8626bb0b1a8e206ab5075699c92b",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n\n2\n"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n\n6\n"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n\n10\n"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n\n20\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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

int main() {
    int num1, num2;

    scanf("%d %d", &num1, &num2);

    if (num1 >= num2) {
        printf("%d\n%d", num2,num1);
    } else {
        printf("%d\n%d", num1,num2);
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
  "source_sha256": "733db94a00f3d0305d2b0c7e0570d907518c3d0fa41210f61ed8349f12f127e7",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_027 — train

```c

#include <stdio.h>
int smallest (int a, int b)
{
    if (a > b)
        printf("%d\n%d", b, a);
    else
        printf("%d\n%d", a, b);
    return 0;
}
int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    smallest(a, b);
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
  "source_sha256": "87cb056e87e32c1d5a9acc40efe6fa234def19c5b9401a7f6dbe538b50da2c8c",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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

int main() 
{
    int a, b;
    scanf("%d %d", &a, &b);
    if (a < b)
        printf("%d\n%d", a, b);
    if (a > b)
        printf("%d\n%d", b, a);
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
  "source_sha256": "f4ecf1763bebf6bb5bbf06358f61da70ae17b29c4870459c9a2ed79b65d31be3",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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
int smallest(int a, int b) {
    if (a > b)
        return b;
    else
        return a;
}

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    printf("%d\n%d", smallest(a, b), a + b - smallest(a, b));
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
  "source_sha256": "53a5bb7b93cad2518536d8bf9bc4e66ee1d2231bfb576969e36f9a6c44884347",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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

int main()
{
    int M, N;
    scanf("%d %d",&M, &N);
    if(M < N) printf("%d\n%d",M,N);
    else printf("%d\n%d",N,M);
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
  "source_sha256": "601d2303da89c050227a476e78fb44c159f6bb7ee0390d1adf116139416accde",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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

int main(){
    int N, M;

    scanf("%d%d",&N,&M);

    if (N <= M){
        printf("%d\n%d",N,M);
    }
    else{
        printf("%d\n%d",M,N);
    }

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
  "source_sha256": "d1de180db789f563a6da257271c34fcae96c5d8a604be2ed7e235e700aaeb08e",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_032 — train

```c

#include <stdio.h>

int main() {
    int n, m;
    scanf("%d%d",&n,&m);
    if (n > m)
        printf("%d\n%d", m, n);
    else
        printf("%d\n%d", n, m);
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
  "source_sha256": "06d7f7115fe98497c07a6a66862ffc768dfe2380d953564b7cd7f3e1900d0d76",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_034 — train

```c

#include <stdio.h>

int main()
{
    int n, m, maior, menor;
    scanf("%d %d", &n, &m);
    if(n>m){
        maior = n;
        menor = m;
    }
    else{
        maior = m;
        menor = n;
    }
    printf("%d\n%d", menor, maior);
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
  "source_sha256": "4f81ad977b4489497b666eb6bbb3b27932b0cfcb95a0bc337ba278b8cdf874a3",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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

int main(){
    int n, m, maior, menor;
    scanf("%d %d", &n, &m);
    if(n>m){
        maior = n;
        menor = m;
    }
    else{
        maior = m;
        menor = n;
    }
    printf("%d\n%d", menor, maior);
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
  "source_sha256": "4aa65a80ae0a00a1d352dc567489ae6afe4e931ca2cc325799010a517ddd54f2",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_036 — train

```c

#include <stdio.h>

int main(){
    int n, m;
    scanf("%d %d", &n, &m);
    if (n >= m){
        printf("%d \n %d", m, n);
    }
    else printf("%d \n%d\n", n, m);

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
  "source_sha256": "7a1f2fe2c35f582480b31400f66f45793794f637267ec4d7e493833b6574ca3f",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1 \n2\n"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2 \n 6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1 \n 10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7 \n 20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "medium",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_037 — validation

```c


#include <stdio.h>

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    if (n > m)
        printf("%d\n%d", m, n);
    if (n < m)
        printf("%d\n%d", m, n);
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
  "source_sha256": "927a25e657e39f814bc0545a3c86e8b3abd76ea70c1060fc9af6db3d1aadf32d",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "2\n1"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "different",
    "stdout:ex02_0:edit_band": "large",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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

int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    if (n > m)
        printf("%d\n%d", m, n);
    else
        printf("%d\n%d", n, m);
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
  "source_sha256": "fd4aec4ee305028dc855976c3fd49e9d879a81afb47c838a89d0739c7df33f46",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_039 — validation

```c

#include <stdio.h>

int main(){

    int n, m, maior, menor;

    scanf("%d",&n);
    scanf("%d",&m);
    if (n<m) {
        menor=n;
        maior=m;
    } else {
        menor=m;
        maior=n;
    }

    printf("%d\n%d",menor,maior);
    return 0;
}
```

```json
{
  "sample_id": "sample_039",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "7d54dc433b517564c4d92125bcd49001a54572453bafe60e5476f3691595882b",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_040 — train

```c


#include <stdio.h>

int main()
{
    long prim, seg;

    scanf("%ld %ld", &prim, &seg);
    if (prim <= seg)
        printf("\n%ld\n%ld\n", prim, seg);
    else
        printf("\n%ld\n%ld\n", seg, prim);

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
  "source_sha256": "3d5db44f7731b2d3468c1960556655c65fe30897c6651990c9c6db80d87e4fb0",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "\n1\n2\n"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "\n2\n6\n"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "\n-1\n10\n"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "\n7\n20\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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

int main () {
    int maior, menor, inter;
    scanf("%d %d", &maior, &menor);
    if (menor > maior) {
        inter = maior;
        maior = menor;
        menor = inter;
    };
    printf("%d %d\n",menor, maior);
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
  "source_sha256": "af19e5bca546a093fddf9df923fac131e27009fa1931fe4e488b71a07e75abe3",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1 2\n"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2 6\n"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1 10\n"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7 20\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "medium",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_042 — train

```c

#include <stdio.h>

int main() {
    int N , M;
    scanf("%d %d", &N, &M);
    if (N <= M) 
        printf("%d\n%d", N, M);
    else 
        printf("%d\n%d", M, N);
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
  "source_sha256": "5c1106aad5b84ca0385b39b2ccd38c2f64cbfe36b974671472274d8154fa97e7",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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


## sample_043 — train

```c

#include <stdio.h>

int main() {
    int N , M;
    scanf("%d%d", &N, &M);
    if (N <= M) 
        printf("%d\n%d", N, M);
    else 
        printf("%d\n%d", M, N);
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
  "source_sha256": "906684a3666d9cafffe25add061e467c4bce9a4f515b818f08d69df27b26dccb",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail",
    "ex02_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "1 2",
      "expected": "1\n2\n",
      "output": "1\n2"
    },
    {
      "test_id": "ex02_1",
      "input": "6 2",
      "expected": "2\n6\n",
      "output": "2\n6"
    },
    {
      "test_id": "ex02_2",
      "input": "10 -1",
      "expected": "-1\n10\n",
      "output": "-1\n10"
    },
    {
      "test_id": "ex02_3",
      "input": "20 7",
      "expected": "7\n20\n",
      "output": "7\n20"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
    "ast:c_for": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small",
    "stdout:ex02_3:relation": "whitespace",
    "stdout:ex02_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "test:ex02_3": "fail",
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
  "members/sample_001/tests/ex02_0",
  "members/sample_001/tests/ex02_1",
  "members/sample_001/tests/ex02_2",
  "members/sample_001/tests/ex02_3",
  "members/sample_002/raw_code",
  "members/sample_002/tests/ex02_0",
  "members/sample_002/tests/ex02_1",
  "members/sample_002/tests/ex02_2",
  "members/sample_002/tests/ex02_3",
  "members/sample_003/raw_code",
  "members/sample_003/tests/ex02_0",
  "members/sample_003/tests/ex02_1",
  "members/sample_003/tests/ex02_2",
  "members/sample_003/tests/ex02_3",
  "members/sample_004/raw_code",
  "members/sample_004/tests/ex02_0",
  "members/sample_004/tests/ex02_1",
  "members/sample_004/tests/ex02_2",
  "members/sample_004/tests/ex02_3",
  "members/sample_005/raw_code",
  "members/sample_005/tests/ex02_0",
  "members/sample_005/tests/ex02_1",
  "members/sample_005/tests/ex02_2",
  "members/sample_005/tests/ex02_3",
  "members/sample_006/raw_code",
  "members/sample_006/tests/ex02_0",
  "members/sample_007/raw_code",
  "members/sample_007/tests/ex02_0",
  "members/sample_007/tests/ex02_1",
  "members/sample_007/tests/ex02_2",
  "members/sample_007/tests/ex02_3",
  "members/sample_008/raw_code",
  "members/sample_008/tests/ex02_0",
  "members/sample_008/tests/ex02_1",
  "members/sample_008/tests/ex02_2",
  "members/sample_008/tests/ex02_3",
  "members/sample_009/raw_code",
  "members/sample_009/tests/ex02_0",
  "members/sample_009/tests/ex02_1",
  "members/sample_009/tests/ex02_2",
  "members/sample_009/tests/ex02_3",
  "members/sample_010/raw_code",
  "members/sample_010/tests/ex02_0",
  "members/sample_010/tests/ex02_1",
  "members/sample_010/tests/ex02_2",
  "members/sample_010/tests/ex02_3",
  "members/sample_011/raw_code",
  "members/sample_011/tests/ex02_0",
  "members/sample_011/tests/ex02_1",
  "members/sample_011/tests/ex02_2",
  "members/sample_011/tests/ex02_3",
  "members/sample_012/raw_code",
  "members/sample_012/tests/ex02_0",
  "members/sample_012/tests/ex02_1",
  "members/sample_012/tests/ex02_2",
  "members/sample_012/tests/ex02_3",
  "members/sample_013/raw_code",
  "members/sample_013/tests/ex02_0",
  "members/sample_013/tests/ex02_1",
  "members/sample_013/tests/ex02_2",
  "members/sample_013/tests/ex02_3",
  "members/sample_014/raw_code",
  "members/sample_014/tests/ex02_0",
  "members/sample_014/tests/ex02_1",
  "members/sample_014/tests/ex02_2",
  "members/sample_014/tests/ex02_3",
  "members/sample_015/raw_code",
  "members/sample_015/tests/ex02_0",
  "members/sample_015/tests/ex02_1",
  "members/sample_015/tests/ex02_2",
  "members/sample_015/tests/ex02_3",
  "members/sample_016/raw_code",
  "members/sample_016/tests/ex02_0",
  "members/sample_016/tests/ex02_1",
  "members/sample_016/tests/ex02_2",
  "members/sample_016/tests/ex02_3",
  "members/sample_017/raw_code",
  "members/sample_017/tests/ex02_0",
  "members/sample_018/raw_code",
  "members/sample_018/tests/ex02_0",
  "members/sample_018/tests/ex02_1",
  "members/sample_018/tests/ex02_2",
  "members/sample_018/tests/ex02_3",
  "members/sample_019/raw_code",
  "members/sample_019/tests/ex02_0",
  "members/sample_019/tests/ex02_1",
  "members/sample_019/tests/ex02_2",
  "members/sample_019/tests/ex02_3",
  "members/sample_020/raw_code",
  "members/sample_020/tests/ex02_0",
  "members/sample_020/tests/ex02_1",
  "members/sample_020/tests/ex02_2",
  "members/sample_020/tests/ex02_3",
  "members/sample_021/raw_code",
  "members/sample_021/tests/ex02_0",
  "members/sample_021/tests/ex02_1",
  "members/sample_021/tests/ex02_2",
  "members/sample_021/tests/ex02_3",
  "members/sample_022/raw_code",
  "members/sample_022/tests/ex02_0",
  "members/sample_022/tests/ex02_1",
  "members/sample_022/tests/ex02_2",
  "members/sample_022/tests/ex02_3",
  "members/sample_023/raw_code",
  "members/sample_023/tests/ex02_0",
  "members/sample_023/tests/ex02_1",
  "members/sample_023/tests/ex02_2",
  "members/sample_023/tests/ex02_3",
  "members/sample_024/raw_code",
  "members/sample_024/tests/ex02_0",
  "members/sample_024/tests/ex02_1",
  "members/sample_024/tests/ex02_2",
  "members/sample_024/tests/ex02_3",
  "members/sample_025/raw_code",
  "members/sample_025/tests/ex02_0",
  "members/sample_025/tests/ex02_1",
  "members/sample_025/tests/ex02_2",
  "members/sample_025/tests/ex02_3",
  "members/sample_026/raw_code",
  "members/sample_026/tests/ex02_0",
  "members/sample_026/tests/ex02_1",
  "members/sample_026/tests/ex02_2",
  "members/sample_026/tests/ex02_3",
  "members/sample_027/raw_code",
  "members/sample_027/tests/ex02_0",
  "members/sample_027/tests/ex02_1",
  "members/sample_027/tests/ex02_2",
  "members/sample_027/tests/ex02_3",
  "members/sample_028/raw_code",
  "members/sample_028/tests/ex02_0",
  "members/sample_028/tests/ex02_1",
  "members/sample_028/tests/ex02_2",
  "members/sample_028/tests/ex02_3",
  "members/sample_029/raw_code",
  "members/sample_029/tests/ex02_0",
  "members/sample_029/tests/ex02_1",
  "members/sample_029/tests/ex02_2",
  "members/sample_029/tests/ex02_3",
  "members/sample_030/raw_code",
  "members/sample_030/tests/ex02_0",
  "members/sample_030/tests/ex02_1",
  "members/sample_030/tests/ex02_2",
  "members/sample_030/tests/ex02_3",
  "members/sample_031/raw_code",
  "members/sample_031/tests/ex02_0",
  "members/sample_031/tests/ex02_1",
  "members/sample_031/tests/ex02_2",
  "members/sample_031/tests/ex02_3",
  "members/sample_032/raw_code",
  "members/sample_032/tests/ex02_0",
  "members/sample_032/tests/ex02_1",
  "members/sample_032/tests/ex02_2",
  "members/sample_032/tests/ex02_3",
  "members/sample_033/raw_code",
  "members/sample_033/tests/ex02_0",
  "members/sample_033/tests/ex02_1",
  "members/sample_033/tests/ex02_2",
  "members/sample_033/tests/ex02_3",
  "members/sample_034/raw_code",
  "members/sample_034/tests/ex02_0",
  "members/sample_034/tests/ex02_1",
  "members/sample_034/tests/ex02_2",
  "members/sample_034/tests/ex02_3",
  "members/sample_035/raw_code",
  "members/sample_035/tests/ex02_0",
  "members/sample_035/tests/ex02_1",
  "members/sample_035/tests/ex02_2",
  "members/sample_035/tests/ex02_3",
  "members/sample_036/raw_code",
  "members/sample_036/tests/ex02_0",
  "members/sample_036/tests/ex02_1",
  "members/sample_036/tests/ex02_2",
  "members/sample_036/tests/ex02_3",
  "members/sample_037/raw_code",
  "members/sample_037/tests/ex02_0",
  "members/sample_037/tests/ex02_1",
  "members/sample_037/tests/ex02_2",
  "members/sample_037/tests/ex02_3",
  "members/sample_038/raw_code",
  "members/sample_038/tests/ex02_0",
  "members/sample_038/tests/ex02_1",
  "members/sample_038/tests/ex02_2",
  "members/sample_038/tests/ex02_3",
  "members/sample_039/raw_code",
  "members/sample_039/tests/ex02_0",
  "members/sample_039/tests/ex02_1",
  "members/sample_039/tests/ex02_2",
  "members/sample_039/tests/ex02_3",
  "members/sample_040/raw_code",
  "members/sample_040/tests/ex02_0",
  "members/sample_040/tests/ex02_1",
  "members/sample_040/tests/ex02_2",
  "members/sample_040/tests/ex02_3",
  "members/sample_041/raw_code",
  "members/sample_041/tests/ex02_0",
  "members/sample_041/tests/ex02_1",
  "members/sample_041/tests/ex02_2",
  "members/sample_041/tests/ex02_3",
  "members/sample_042/raw_code",
  "members/sample_042/tests/ex02_0",
  "members/sample_042/tests/ex02_1",
  "members/sample_042/tests/ex02_2",
  "members/sample_042/tests/ex02_3",
  "members/sample_043/raw_code",
  "members/sample_043/tests/ex02_0",
  "members/sample_043/tests/ex02_1",
  "members/sample_043/tests/ex02_2",
  "members/sample_043/tests/ex02_3"
]
```
