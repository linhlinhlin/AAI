# lab02-ex04--kmeans--combined_stdout--s42--c0

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 50; phân vùng: {'train': 37, 'validation': 13}.


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
    "test_id": "ex04_1",
    "n_cluster": 50,
    "n_observed": 50,
    "n_failed": 48,
    "n_not_run": 0,
    "failure_rate_observed": 0.96,
    "failure_rate_cluster": 0.96,
    "outcome_counts": {
      "fail": 48,
      "pass": 2
    }
  },
  {
    "test_id": "ex04_2",
    "n_cluster": 50,
    "n_observed": 50,
    "n_failed": 48,
    "n_not_run": 0,
    "failure_rate_observed": 0.96,
    "failure_rate_cluster": 0.96,
    "outcome_counts": {
      "fail": 48,
      "pass": 2
    }
  },
  {
    "test_id": "ex04_3",
    "n_cluster": 50,
    "n_observed": 50,
    "n_failed": 48,
    "n_not_run": 0,
    "failure_rate_observed": 0.96,
    "failure_rate_cluster": 0.96,
    "outcome_counts": {
      "fail": 48,
      "pass": 2
    }
  },
  {
    "test_id": "ex04_0",
    "n_cluster": 50,
    "n_observed": 50,
    "n_failed": 42,
    "n_not_run": 0,
    "failure_rate_observed": 0.84,
    "failure_rate_cluster": 0.84,
    "outcome_counts": {
      "fail": 42,
      "pass": 8
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex04_1:relation",
    "value": "different",
    "n": 46,
    "n_cluster": 50,
    "rate": 0.92,
    "cohort_rate": 0.5,
    "difference_from_cohort": 0.42000000000000004
  },
  {
    "feature": "stdout:ex04_3:relation",
    "value": "different",
    "n": 46,
    "n_cluster": 50,
    "rate": 0.92,
    "cohort_rate": 0.5,
    "difference_from_cohort": 0.42000000000000004
  },
  {
    "feature": "stdout:ex04_2:relation",
    "value": "different",
    "n": 46,
    "n_cluster": 50,
    "rate": 0.92,
    "cohort_rate": 0.5106382978723404,
    "difference_from_cohort": 0.40936170212765965
  },
  {
    "feature": "stdout:ex04_0:relation",
    "value": "different",
    "n": 35,
    "n_cluster": 50,
    "rate": 0.7,
    "cohort_rate": 0.3829787234042553,
    "difference_from_cohort": 0.31702127659574464
  },
  {
    "feature": "stdout:ex04_1:edit_band",
    "value": "large",
    "n": 25,
    "n_cluster": 50,
    "rate": 0.5,
    "cohort_rate": 0.26595744680851063,
    "difference_from_cohort": 0.23404255319148937
  },
  {
    "feature": "stdout:ex04_3:edit_band",
    "value": "large",
    "n": 24,
    "n_cluster": 50,
    "rate": 0.48,
    "cohort_rate": 0.2553191489361702,
    "difference_from_cohort": 0.2246808510638298
  },
  {
    "feature": "stdout:ex04_2:edit_band",
    "value": "large",
    "n": 24,
    "n_cluster": 50,
    "rate": 0.48,
    "cohort_rate": 0.26595744680851063,
    "difference_from_cohort": 0.21404255319148935
  },
  {
    "feature": "stdout:ex04_0:edit_band",
    "value": "large",
    "n": 23,
    "n_cluster": 50,
    "rate": 0.46,
    "cohort_rate": 0.2553191489361702,
    "difference_from_cohort": 0.20468085106382983
  },
  {
    "feature": "stdout:ex04_2:edit_band",
    "value": "medium",
    "n": 24,
    "n_cluster": 50,
    "rate": 0.48,
    "cohort_rate": 0.40425531914893614,
    "difference_from_cohort": 0.07574468085106384
  },
  {
    "feature": "stdout:ex04_3:edit_band",
    "value": "medium",
    "n": 24,
    "n_cluster": 50,
    "rate": 0.48,
    "cohort_rate": 0.40425531914893614,
    "difference_from_cohort": 0.07574468085106384
  },
  {
    "feature": "stdout:ex04_0:edit_band",
    "value": "__unknown__",
    "n": 8,
    "n_cluster": 50,
    "rate": 0.16,
    "cohort_rate": 0.0851063829787234,
    "difference_from_cohort": 0.0748936170212766
  },
  {
    "feature": "stdout:ex04_0:relation",
    "value": "__unknown__",
    "n": 8,
    "n_cluster": 50,
    "rate": 0.16,
    "cohort_rate": 0.0851063829787234,
    "difference_from_cohort": 0.0748936170212766
  },
  {
    "feature": "test:ex04_0",
    "value": "pass",
    "n": 8,
    "n_cluster": 50,
    "rate": 0.16,
    "cohort_rate": 0.0851063829787234,
    "difference_from_cohort": 0.0748936170212766
  },
  {
    "feature": "ast:c_update",
    "value": "0",
    "n": 46,
    "n_cluster": 50,
    "rate": 0.92,
    "cohort_rate": 0.851063829787234,
    "difference_from_cohort": 0.06893617021276599
  },
  {
    "feature": "stdout:ex04_1:edit_band",
    "value": "medium",
    "n": 23,
    "n_cluster": 50,
    "rate": 0.46,
    "cohort_rate": 0.39361702127659576,
    "difference_from_cohort": 0.06638297872340426
  },
  {
    "feature": "ast:c_for",
    "value": "0",
    "n": 47,
    "n_cluster": 50,
    "rate": 0.94,
    "cohort_rate": 0.8829787234042553,
    "difference_from_cohort": 0.05702127659574463
  },
  {
    "feature": "ast:c_subscript",
    "value": "0",
    "n": 45,
    "n_cluster": 50,
    "rate": 0.9,
    "cohort_rate": 0.851063829787234,
    "difference_from_cohort": 0.04893617021276597
  },
  {
    "feature": "stdout:ex04_0:edit_band",
    "value": "medium",
    "n": 18,
    "n_cluster": 50,
    "rate": 0.36,
    "cohort_rate": 0.32978723404255317,
    "difference_from_cohort": 0.03021276595744682
  },
  {
    "feature": "ast:c_while",
    "value": "0",
    "n": 48,
    "n_cluster": 50,
    "rate": 0.96,
    "cohort_rate": 0.9361702127659575,
    "difference_from_cohort": 0.0238297872340425
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 10,
    "n_cluster": 50,
    "rate": 0.2,
    "cohort_rate": 0.18085106382978725,
    "difference_from_cohort": 0.019148936170212766
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 50,
    "n_cluster": 50,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 49,
    "n_cluster": 50,
    "rate": 0.98,
    "cohort_rate": 0.9893617021276596,
    "difference_from_cohort": -0.009361702127659632
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 43,
    "n_cluster": 50,
    "rate": 0.86,
    "cohort_rate": 0.8723404255319149,
    "difference_from_cohort": -0.012340425531914945
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 47,
    "n_cluster": 50,
    "rate": 0.94,
    "cohort_rate": 0.9574468085106383,
    "difference_from_cohort": -0.0174468085106384
  }
]
```


## IF–THEN dự đoán cluster, không dự đoán gold

```json
[
  {
    "rule_id": 6,
    "if": [
      "stdout:ex04_3:relation=different"
    ],
    "then_cluster": 0,
    "train_support": 36,
    "train_precision": 1.0,
    "holdout_support": 11,
    "holdout_precision": 0.9090909090909091
  }
]
```


## Candidate chưa xác thực

```json
{
  "source": "local_heuristic_not_gold",
  "misconception_name": "Chưa đủ bằng chứng để đặt tên lỗi",
  "misconception_type": null,
  "reasoning": "Có 50 bài trong cụm. Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
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

sample_002, sample_025, sample_036, sample_040

## sample_002 — train — đại diện

```c
#include <stdio.h>



int main() {
	int x;
	int meio;
	int menor;
	printf("Introduza o primeiro inteiro:\n");
	scanf("%d", &meio);
	printf("Introduza o segundo inteiro:\n");
	scanf("%d", &x);
	if (x < meio) {
		menor = x;
	} else {
		menor = meio;
		meio = x;
	}
	printf("Introduza o terceiro inteiro:\n");
	scanf("%d", &x);
	if (x < menor) {
		printf("%d %d %d\n", x, menor, meio);
	} else if (x < meio) {
		printf("%d %d %d\n", menor, x, meio);
	} else {
		printf("%d %d %d\n", menor, meio, x);
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
  "source_sha256": "5defd7601bff42b843398a332c715826de905e8d8178e5ef9ab6aa0446dcfc61",
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
      "output": "Introduza o primeiro inteiro:\nIntroduza o segundo inteiro:\nIntroduza o terceiro inteiro:\n1 2 6\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "Introduza o primeiro inteiro:\nIntroduza o segundo inteiro:\nIntroduza o terceiro inteiro:\n2 6 10\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "Introduza o primeiro inteiro:\nIntroduza o segundo inteiro:\nIntroduza o terceiro inteiro:\n-8 -1 10\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "Introduza o primeiro inteiro:\nIntroduza o segundo inteiro:\nIntroduza o terceiro inteiro:\n7 20 100\n"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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


## sample_025 — validation — đại diện

```c

#include <stdio.h>

int main()
{
    int num1, num2, num3;

    scanf("%d %d %d", &num1, &num2, &num3);
    if(num1 <= num2 && num2 <= num3)
        printf("%d %d %d\n", num1, num2, num3);
    else if(num1 <= num3 && num3 <= num2)
        printf("%d %d %d\n", num1, num3, num2);
    else if(num2 <= num1 && num1 <= num3)
        printf("%d %d %d\n", num2, num1, num3);
    else if(num2 <= num3 && num3 <= num1)
        printf("%d %d %d\n", num2, num3, num2);
    else if(num3 <= num1 && num1 <= num2)
        printf("%d %d %d\n", num3, num1, num2);
    else 
        printf("%d %d %d\n", num3, num2, num1);
    
    return 0;    
}
```

```json
{
  "sample_id": "sample_025",
  "partition": "validation",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "ac7c39787791079aaa3b4f30a56b15cd62a49eaa16c1784e8e028642c939712d",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "pass",
    "ex04_2": "pass",
    "ex04_3": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": "1 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "pass",
    "test:ex04_2": "pass",
    "test:ex04_3": "pass",
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "medium",
    "stdout:ex04_1:relation": "__unknown__",
    "stdout:ex04_1:edit_band": "__unknown__",
    "stdout:ex04_2:relation": "__unknown__",
    "stdout:ex04_2:edit_band": "__unknown__",
    "stdout:ex04_3:relation": "__unknown__",
    "stdout:ex04_3:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "pass",
    "test:ex04_2": "pass",
    "test:ex04_3": "pass",
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


## sample_036 — train — đại diện

```c


#include <stdio.h>

int main(){

    int  num[3], counter, maior, menor, meio;
    scanf("%d%d%d", &num[0], &num[1], &num[2]);

    maior = num[0];
    menor = num[0];
    

    for (counter = 1; counter <3; counter++){
        if (num[counter] > maior)
            maior = num[counter]; 
    
        if (num[counter] < menor)
            menor = num[counter]; 
    }
 
    
    for (counter = 0; counter<3 ;counter++){
        if (num[counter]!= maior || num[counter]!= menor)
            meio = num[counter];
    }
    
    printf("%d %d %d\n", menor, meio, maior);
  
    return 0;
}
```

```json
{
  "sample_id": "sample_036",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "f61dca5eb2ba5593a9459c9185711fe7d8c8e82824807fe7535895de74c8cbf8",
  "outcomes": {
    "ex04_0": "pass",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 2 10\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 -8 10\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 7 100\n"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "pass",
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
    "stdout:ex04_0:relation": "__unknown__",
    "stdout:ex04_0:edit_band": "__unknown__",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex04_0": "pass",
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


## sample_040 — train — đại diện

```c

#include <stdio.h>

void swap(int nums[], int idx)
{
    int numA;
    numA = nums[idx];
    nums[idx] = nums[idx + 1];
    nums[idx + 1] = numA; 
}

int main()
{
    int nums[3];

    scanf("%d%d%d", &nums[0], &nums[1], &nums[2]);
    
    

    if (nums[0] >= nums [1])
    {
        swap(nums, 0);
    }
    
    if (nums[1] >= nums [2])
    {
        swap(nums, 1);
    }

     if (nums[0] >= nums [1])
    {
        swap(nums, 0);
    }
    
    printf("%d%d%d\n", nums[0], nums[1], nums[2]);
    return 0;
}



```

```json
{
  "sample_id": "sample_040",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "8fd2c5a18cae2d9e40a0d82fc1240b62f8eab3610dbacb9a618396ce63be92ef",
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
      "output": "126\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2610\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8-110\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "720100\n"
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
    "ast:c_subscript": "1",
    "ast:c_zero_index": "1",
    "ast:c_one_index": "1",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "medium",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
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
    "ast:c_subscript": "1",
    "ast:c_zero_index": "1",
    "ast:c_one_index": "1",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "1",
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

int main()
{
    int a,b,c;
    scanf("%d%d%d",&a,&b,&c);

    if (a < b && a < c)
    {
        if (b < c)
        {
            printf("%d",a);
            printf("%d",b);
            printf("%d",c);
        }
        else
        {
            printf("%d",a);
            printf("%d",c);
            printf("%d",b);
        }
    }
    if (b<a && b<c)
    {
        if (a<c)
        {
            printf("%d",b);
            printf("%d",a);
            printf("%d",c);
        }
        else
        {
            printf("%d",b);
            printf("%d",c);
            printf("%d",a);
        }
    }
    if (c<b && c<a)
    {
        if (a<b)
        {
            printf("%d",c);
            printf("%d",a);
            printf("%d",b);
        }
        else
        {
            printf("%d",c);
            printf("%d",b);
            printf("%d",a);
        }
        
    }
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
  "source_sha256": "72470fb90b90f867154939f3ef499c4c14073802db94fb61cd399e15b7f0a0f7",
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
      "output": "126"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2610"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8-110"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "720100"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "medium",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
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
	int n1, n2, n3, temp;
	
	printf("Insira 3 numeros: ");
	scanf("%d %d %d", &n1, &n2, &n3);

	if (n1 > n2)
	{
	temp = n1;
       	n1 = n2;
	n2 = temp;	
	}

	if (n1 > n3)
	{
	temp = n1;
	n1 = n3;
	n3 = temp;
	}

	if (n2 > n3)
	{
	temp = n2;
	n2 = n3;
	n3 = temp;
	}

	printf("%d %d %d\n", n1,n2,n3);
	
	return 0;}

```

```json
{
  "sample_id": "sample_003",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "49496ff35651131d2df68ad84ae7ccbe6dc43a66d58fab6c776212dd1a666e97",
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
      "output": "Insira 3 numeros: 1 2 6\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "Insira 3 numeros: 2 6 10\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "Insira 3 numeros: -8 -1 10\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "Insira 3 numeros: 7 20 100\n"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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



int main () {
    int a, b, c, aux;

    scanf("%d%d%d", &a, &b, &c);

    if (b < a) {
        aux = a;
        a = b;
        b = aux;
    }
    if (c < a) {
        aux = a;
        a = c;
        c = aux;
    }

    printf("%d %d %d", a, b, c);
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
  "source_sha256": "c294176084c147357950704dee9ba7ad8ae7e13523df7c6278a32ae86ffcda55",
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
      "output": "1 6 2"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 10 6"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 10 -1"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 100 20"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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


## sample_005 — train

```c
#include <stdio.h>

int main()
{
  int num1, num2, num3;

  scanf("%d%d%d", &num1, &num2, &num3);

  if (num1 <= num2)
    {
      if (num1 <= num3)
	{
	  if (num2 <= num3)
	    printf("%d\t%d\t%d\n", num1, num2, num3);
	  else
	    printf("%d\t%d\t%d\n", num1, num3, num2);
	}
    }
  else if (num2 <= num1)
    {
      if (num2 <= num3)
	{
	  if (num1 <= num3)
	    printf("%d\t%d\t%d\n", num2, num1, num3);
	  else
	    printf("%d\t%d\t%d\n", num2, num3, num1);
	}
    }
  else
    {
      if (num2 <= num1)
	printf("%d\t%d\t%d\n", num3, num2, num1);
      else
	printf("%d\t%d\t%d\n", num3, num1, num2);
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
  "source_sha256": "9f1355246b1505241cc4c096c3f9b4b0439187710e04c671033389951f7bf025",
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
      "output": "1\t2\t6\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": ""
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": ""
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": ""
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
    "stdout:ex04_0:edit_band": "medium",
    "stdout:ex04_1:relation": "empty",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "empty",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "empty",
    "stdout:ex04_3:edit_band": "large"
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


## sample_006 — train

```c
    #include <stdio.h>

    int x, y , z;

    int main(){

        scanf("%d%d%d", &x, &y, &z);

        if (x < y && y < z)
            printf("%d\t%d\t%d\n", x, y, z);
        else if (x < y && z < y)
            printf("%d\t%d\t%d\n", x, z, y);
        else if (y < x && x < z)
            printf("%d\t%d\t%d\n", y, x, z);
        else if (y < x && z < x)
            printf("%d\t%d\t%d\n", y, z, x);
        else if (z < x && x < y)
            printf("%d\t%d\t%d\n", z, x ,y);
        else
            printf("%d\t%d\t%d\n", z, y ,x);

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
  "source_sha256": "71a407961ba5038ce56e45bc573baf8452674ce697670916b28f2f641b11f546",
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
      "output": "1\t2\t6\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "6\t2\t10\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-1\t-8\t10\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "20\t7\t100\n"
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
    "stdout:ex04_0:edit_band": "medium",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
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


## sample_007 — validation

```c
#include <stdio.h>
#include <values.h>

int N, i;
float x, min, max, y;

int main()
{
    scanf("%d", &N);
    scanf("%f", &x);
    
    min = x;
    max = x;

    for(i = 2; i <= N; i += 1)
    {
        scanf("%f", &y);
        
        if(y < min)
            min = y;
        else if(y > max)
            max = y;       
    }

    printf("min: %f, max: %f\n", min, max);

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
  "source_sha256": "5e36f005bc08a538f88b480504d852fd8c7a77776d7a62262136a8274db64e65",
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
      "output": "min: 1.000000, max: 2.000000\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "min: 2.000000, max: 6.000000\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "min: -8.000000, max: -1.000000\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "min: 7.000000, max: 20.000000\n"
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
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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
	float n1, n2, n3;
	scanf("%f%f%f",&n1,&n2,&n3);
	if  ((n1 < n2) && (n1<n3)) printf("%f",n1);
	if  ((n2 < n1) && (n2<n3)) printf("%f",n2);
	if  ((n3 < n2) && (n3<n1)) printf("%f",n3);
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
  "source_sha256": "9d0a9f6d2f14bdd44af856d28c67cd34555529fdb2f0382027a44b81b303ed4a",
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
      "output": "1.000000"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2.000000"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8.000000"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7.000000"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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


## sample_009 — train

```c

#include <stdio.h>

int main() {
    int l, m, n;
    int aux;
    scanf("%d", &l);
    scanf("%d", &m);
    scanf("%d", &n);
    if (l > m) {
        aux = l;
        l = m;
        m = aux;
    }
    if (m > n) {
        aux = m;
        m = n;
        n = aux;
    }
    printf("%d %d %d\n", l, m, n);

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
  "source_sha256": "b046705e89734f80270cfabab3bd6c21260e2aab40de73697de4e411caaeb278",
  "outcomes": {
    "ex04_0": "pass",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "6 2 10\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-1 -8 10\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "20 7 100\n"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "pass",
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
    "stdout:ex04_0:relation": "__unknown__",
    "stdout:ex04_0:edit_band": "__unknown__",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex04_0": "pass",
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


## sample_010 — train

```c

#include <stdio.h>

int main(){

int a,b,c ;

printf("Insira 3 numeros por favor\n") ;    

scanf("%d%d%d" , &a, &b, &c );

if (a > b && a>c && c>b){

    printf ( "%d\t%d\t%d\n" , b , c , a);
}

else if (a >b && a > c && b >c ){

    printf ( "%d\t%d\t%d\n" , c , b , a);

}
else if (b>a && b>c && a>c){

    printf ( "%d\t%d\t%d\n" , c , a , b);

}
else if (b>a && b>c && c>a){

    printf ( "%d\t%d\t%d\n" , a , c , b);
}

else if (c>a && c>b && a>b){

    printf ( "%d\t%d\t%d\n" , b , a , c);
}

else if (c>a && c>b && a<b){

    printf ( "%d\t%d\t%d\n" , a , b , c);
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
  "source_sha256": "709b52a2e8fd908bf88fb749e25a9d587e8affbb7e13b30213af9f41bf160068",
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
      "output": "Insira 3 numeros por favor\n1\t2\t6\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "Insira 3 numeros por favor\n2\t6\t10\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "Insira 3 numeros por favor\n-8\t-1\t10\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "Insira 3 numeros por favor\n7\t20\t100\n"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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


## sample_011 — train

```c

#include <stdio.h>

int main()
{
    int num1, num2, num3, a, b, c;

    scanf("%d%d%d", &num1, &num2, &num3);

    a = num1 < num2 ? num1 : num2;
    a = a < num3 ? a : num3;

    if (a == num1)
    {
        b = num2 < num3 ? num2 : num3;
        c = num2 > num3 ? num2 : num3;
    }
    else if (a == num2)
    {
        b = num1 < num3 ? num1 : num3;
        c = num1 > num3 ? num1 : num3;
    }
    else
    {
        b = num1 < num2 ? num1 : num2;
        c = num1 > num2 ? num1 : num2;
    }

    printf("%d%d%d\n", a, b, c);

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
  "source_sha256": "5c1a88b9bc019cbb3248142ccb8bfc5767e7dc08d8fc983802b2558b982e7b77",
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
      "output": "126\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2610\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8-110\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "720100\n"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "medium",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
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

int main(){
    int num1_ex4, num2_ex4, num3_ex4 = 0;
    scanf("%d%d%d",&num1_ex4,&num2_ex4,&num3_ex4);
    if (num1_ex4 > num2_ex4){
        if (num2_ex4 > num3_ex4){
            printf("%d\t%d\t%d", num1_ex4, num2_ex4, num3_ex4);
            }
        else if (num3_ex4 > num1_ex4){
            printf("%d\t%d\t%d", num3_ex4, num1_ex4, num2_ex4);
        }
        else{
            printf("%d\t%d\t%d", num1_ex4, num3_ex4, num2_ex4);
        }
        }
    else{
        if (num1_ex4 > num3_ex4){
            printf("%d\t%d\t%d", num2_ex4, num1_ex4, num3_ex4);
        }
        else if(num3_ex4 > num2_ex4){
            printf("%d\t%d\t%d", num3_ex4, num2_ex4, num1_ex4);
        }
        else{
            printf("%d\t%d\t%d", num2_ex4, num3_ex4, num1_ex4);
        }
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
  "source_sha256": "ddfa50c6a44e4e2c9d8e126f5332bb8f6b5c924c0ccd689f448300d67582e332",
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
      "output": "6\t2\t1"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "10\t6\t2"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "10\t-1\t-8"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "100\t20\t7"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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
int main(){
    int maior, meio, min, n1, n2, n3;
    int m, n;
    scanf("%d %d %d", &n1, &n2, &n3);

    m = n1 > n2 ? n1 : n2;
    n = n1 < n2 ? n1 : n2;
    maior = m > n3 ? m : n3;
    meio = m < n3 ? m : n3;
    min = n < n3 ? n : n3;
    

    printf("%d\t%d\t%d\n", min, meio, maior);
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
  "source_sha256": "1d6b25cc3d27422f0974c055a0d03a3d49c0e6dea188a065e478b02eb1c676e4",
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
      "output": "1\t2\t6\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2\t2\t10\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8\t-8\t10\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7\t7\t100\n"
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
    "stdout:ex04_0:edit_band": "medium",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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


## sample_014 — validation

```c


#include <stdio.h>

int main(){
    int n1, n2, n3;

    scanf("%d %d %d", &n1, &n2, &n3);
    if ((n1<=n2) & (n2<=n3))
        printf("%d %d %d\n", n1, n2, n3);
    if ((n1==n2) & (n2<n3))
        printf("%d %d %d\n", n1, n2, n3);
    if ((n2==n3) & (n1<n2))
        printf("%d %d %d\n", n1, n2, n3);
    if ((n1<n3) & (n3<n2))
        printf("%d %d %d\n", n1, n3, n2);
    if ((n3<n1) & (n2>n3))
        printf("%d %d %d\n", n3, n1, n2);
    if ((n3<n2) & (n2<n1))
        printf("%d %d %d\n", n3, n2, n1);
    if ((n2<n1) & (n1<n3))
        printf("%d %d %d\n", n2, n1, n3);
    if ((n2<n3) & (n3<n1))
        printf("%d %d %d\n", n2, n3, n1);
    
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
  "source_sha256": "bfc8d7abf8cf1982491f42da3fad8ea12223f60f35945958b91d019562f4ff7b",
  "outcomes": {
    "ex04_0": "pass",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 10 6\n2 6 10\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 10 -1\n-8 -1 10\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 100 20\n7 20 100\n"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "pass",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "__unknown__",
    "stdout:ex04_0:edit_band": "__unknown__",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex04_0": "pass",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
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

int main(){
    int n1, n2, n3;

    scanf("%d %d %d", &n1, &n2, &n3);
    if ((n1<=n2) & (n2<=n3))
        printf("%d %d %d\n", n1, n2, n3);
    if ((n1<=n3) & (n3<n2))
        printf("%d %d %d\n", n1, n3, n2);
    if ((n3<=n1) & (n2>n3))
        printf("%d %d %d\n", n3, n1, n2);
    if ((n3<=n2) & (n2<n1))
        printf("%d %d %d\n", n3, n2, n1);
    if ((n2<=n1) & (n1<n3))
        printf("%d %d %d\n", n2, n1, n3);
    if ((n2<=n3) & (n3<n1))
        printf("%d %d %d\n", n2, n3, n1);
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
  "source_sha256": "f90d4029f114791a4fbeca7e5b32d58020fdba4a1fe1927f7476c0d0d72b9159",
  "outcomes": {
    "ex04_0": "pass",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 10 6\n2 6 10\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 10 -1\n-8 -1 10\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 100 20\n7 20 100\n"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "pass",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "__unknown__",
    "stdout:ex04_0:edit_band": "__unknown__",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex04_0": "pass",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
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

int main ()
{   int num1;
    int num2;
    int num3;
    int maior;
    int meio;
    int menor;
    scanf("%d%d%d", &num1, &num2, &num3);
    if (num1>num2 && num1>num3)
    {
        maior = num1;
        if (num2>num3)
        {
            meio = num2;
            menor = num3;
        };
        if (num3>num2)
        {
            menor = num2;
            meio = num3;
        };      
    };
     if (num2>num1 && num2>num3)
    {
        maior = num2;
        if (num1>num3)
        {
            meio = num1;
            menor = num3;
        };
        if (num3>num1)
        {
            menor = num1;
            meio = num3;
        };      
    };
     if (num3>num1 && num3>num2)
    {
        maior = num3;
        if (num1>num2)
        {
            meio = num1;
            menor = num2;
        };
        if (num2>num1)
        {
            menor = num1;
            meio = num2;
        };      
    }
    printf("%d\n%d\n%d\n", maior, meio, menor);
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
  "source_sha256": "87b6a42207e76287d3e45378af8741d25256618be03ff2ebc87817b1e324ffea",
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
      "output": "6\n2\n1\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "10\n6\n2\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "10\n-1\n-8\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "100\n20\n7\n"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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

int main ()
{   int num1;
    int num2;
    int num3;
    int maior;
    int meio;
    int menor;
    scanf("%d%d%d", &num1, &num2, &num3);
    if (num1>num2 && num1>num3)
    {
        maior = num1;
        if (num2>num3)
        {
            meio = num2;
            menor = num3;
        };
        if (num3>num2)
        {
            menor = num2;
            meio = num3;
        };      
    };
     if (num2>num1 && num2>num3)
    {
        maior = num2;
        if (num1>num3)
        {
            meio = num1;
            menor = num3;
        };
        if (num3>num1)
        {
            menor = num1;
            meio = num3;
        };      
    };
     if (num3>num1 && num3>num2)
    {
        maior = num3;
        if (num1>num2)
        {
            meio = num1;
            menor = num2;
        };
        if (num2>num1)
        {
            menor = num1;
            meio = num2;
        };      
    }
    printf("%d%d%d\n", menor, meio, maior);
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
  "source_sha256": "80ddfaf93e94668369d6e73ef4a6c9eb55eedc26146a90e122726957941173d7",
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
      "output": "126\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2610\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8-110\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "720100\n"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "medium",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
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


## sample_018 — train

```c


#include <stdio.h>
 int main ()
 {
    int v1, v2, v3, min, meio, max;
    printf("Introduza 3 números inteiros: \n");
    scanf("%d %d %d", &v1, &v2, &v3);

    if ((v1 < v2) && (v1 < v3))
    {
        min = v1;
    }
    if ((v2 < v1) && (v2 < v3))
    {
        min = v2;
    }
    if ((v3 < v1) && (v3 < v2))
    {
        min = v3;
    }
    if (min == v1)
    {
        if(v2 < v3)
        {
            meio = v2;
            max = v3;
        }
        else
        {
            meio = v3;
            max = v2;
        }
    }
    if (min == v2)
    {
        if (v1 < v3)
        {
            meio = v1;
            max = v3;
        }
        else
        {
            meio = v3;
            max = v1;
        }
        
    }
    if (min == v3)
    {
        if (v1 < v2)
        {
            meio = v1;
            max = v2;
        }
        
    }
    printf("%d %d %d", min, meio, max);  
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
  "source_sha256": "9ca7f47eba851335bb65c64f07007d7d8958f50a25d649d8835c66e8433774fc",
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
      "output": "Introduza 3 números inteiros: \n1 2 6"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "Introduza 3 números inteiros: \n2 0 32765"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "Introduza 3 números inteiros: \n-8 0 32767"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "Introduza 3 números inteiros: \n7 0 32764"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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


## sample_019 — train

```c


#include <stdio.h>
 int main ()
 {
    int v1, v2, v3, min, meio, max;

    printf("Introduza 3 números inteiros: \n");
    scanf("%d %d %d", &v1, &v2, &v3);

     if ((v1 < v2) && (v1 < v3))
    {
        min = v1;
    }
     if ((v2 < v1) && (v2 < v3))
    {
        min = v2;
    }
     if ((v3 < v1) && (v3 < v2))
    {
        min = v3;
    }
    if (min == v1)
    {
        if(v2 < v3)
        {
            meio = v2;
            max = v3;
        }
        else
        {
            meio = v3;
            max = v2;
        }
    }
    if (min == v2)
    {
        if (v1 < v3)
        {
            meio = v1;
            max = v3;
        }
        else
        {
            meio = v3;
            max = v1;
        }
        
    }
    if (min == v3)
    {
        if (v1 < v2)
        {
            meio = v1;
            max = v2;
        }
        
    }
    printf("%d\t%d\t%d\t", min, meio, max);  
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
  "source_sha256": "60693ea9d2865a6d089740cf8156358d09ab68677c2467a8114a06470bf864a1",
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
      "output": "Introduza 3 números inteiros: \n1\t2\t6\t"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "Introduza 3 números inteiros: \n2\t0\t32767\t"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "Introduza 3 números inteiros: \n-8\t0\t32765\t"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "Introduza 3 números inteiros: \n7\t0\t32766\t"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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


## sample_020 — train

```c


#include <stdio.h>
 int main ()
 {
    int v1, v2, v3, min, meio, max;

    printf("Introduza 3 números inteiros: \n");
    scanf("%d %d %d", &v1, &v2, &v3);

     if ((v1 < v2) && (v1 < v3))
    {
        min = v1;
    }
     if ((v2 < v1) && (v2 < v3))
    {
        min = v2;
    }
     if ((v3 < v1) && (v3 < v2))
    {
        min = v3;
    }

     if (min == v1)
    {
        if(v2 < v3)
        {
            meio = v2;
            max = v3;
        }
        else
        {
            meio = v3;
            max = v2;
        }
    }
     if (min == v2)
    {
        if (v1 < v3)
        {
            meio = v1;
            max = v3;
        }
        else
        {
            meio = v3;
            max = v1;
        }  
    }
     if (min == v3)
    {
        if (v1 < v2)
        {
            meio = v1;
            max = v2;
        }
        else
        {
            meio = v2;
            max = v1;
        }
    }
    printf("%d %d %d\n", min, meio, max);  
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
  "source_sha256": "112e395806fd3fcee7b4798d8eee1c44db33da9b702b69a97a121e328f26fa12",
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
      "output": "Introduza 3 números inteiros: \n1 2 6\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "Introduza 3 números inteiros: \n2 6 10\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "Introduza 3 números inteiros: \n-8 -1 10\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "Introduza 3 números inteiros: \n7 20 100\n"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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
 int main ()
 {
    int v1, v2, v3, min, meio, max;

    printf("Introduza 3 números inteiros: \n");
    scanf("%d %d %d", &v1, &v2, &v3);

     if ((v1 < v2) && (v1 < v3))
    {
        min = v1;
    }
     if ((v2 < v1) && (v2 < v3))
    {
        min = v2;
    }
     if ((v3 < v1) && (v3 < v2))
    {
        min = v3;
    }

     if (min == v1)
    {
        if(v2 < v3)
        {
            meio = v2;
            max = v3;
        }
        else
        {
            meio = v3;
            max = v2;
        }
    }
     if (min == v2)
    {
        if (v1 < v3)
        {
            meio = v1;
            max = v3;
        }
        else
        {
            meio = v3;
            max = v1;
        }  
    }
     if (min == v3)
    {
        if (v1 < v2)
        {
            meio = v1;
            max = v2;
        }
    }
    printf("%d %d %d\n", min, meio, max);  
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
  "source_sha256": "fc270db5de59610cecf03c240dc6c1d5f4a05c646edae6b426a798adebe80b64",
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
      "output": "Introduza 3 números inteiros: \n1 2 6\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "Introduza 3 números inteiros: \n2 0 32765\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "Introduza 3 números inteiros: \n-8 0 32767\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "Introduza 3 números inteiros: \n7 0 32767\n"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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
 int main ()
 {
    int v1, v2, v3, min, meio, max;

    printf("Introduza 3 números inteiros: \n");
    scanf("%d %d %d", &v1, &v2, &v3);

     if ((v1 < v2) && (v1 < v3))
    {
        min = v1;
    }
     if ((v2 < v1) && (v2 < v3))
    {
        min = v2;
    }
     if ((v3 < v1) && (v3 < v2))
    {
        min = v3;
    }

     if (min == v1)
    {
        if(v2 < v3)
        {
            meio = v2;
            max = v3;
        }
        else
        {
            meio = v3;
            max = v2;
        }
    }
     if (min == v2)
    {
        if (v1 < v3)
        {
            meio = v1;
            max = v3;
        }
        else
        {
            meio = v3;
            max = v1;
        }  
    }
     if (min == v3)
    {
        if (v1 < v2)
        {
            meio = v1;
            max = v2;
        }
    }
    printf("%d\t%d\t%d\n", min, meio, max);  
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
  "source_sha256": "d4f8efa082575cd1862a6cd122b742e9d0ac35d82811d7cddff18fe2c75be159",
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
      "output": "Introduza 3 números inteiros: \n1\t2\t6\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "Introduza 3 números inteiros: \n2\t0\t32765\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "Introduza 3 números inteiros: \n-8\t0\t32764\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "Introduza 3 números inteiros: \n7\t0\t32764\n"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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


## sample_023 — train

```c


#include <stdio.h>
 int main ()
 {
    int v1, v2, v3, min, meio, max;
    
    scanf("%d %d %d", &v1, &v2, &v3);

    if ((v1 < v2) && (v1 < v3))
    {
        min = v1;
    }
    if ((v2 < v1) && (v2 < v3))
    {
        min = v2;
    }
    if ((v3 < v1) && (v3 < v2))
    {
        min = v3;
    }
    if (min == v1)
    {
        if(v2 < v3)
        {
            meio = v2;
            max = v3;
        }
        else
        {
            meio = v3;
            max = v2;
        }
    }
    if (min == v2)
    {
        if (v1 < v3)
        {
            meio = v1;
            max = v3;
        }
        else
        {
            meio = v3;
            max = v1;
        }
        
    }
    if (min == v3)
    {
        if (v1 < v2)
        {
            meio = v1;
            max = v2;
        }
        
    }
    printf("%d %d %d", min, meio, max);  
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
  "source_sha256": "e19c68dbd7818161c93ddada251a61962269c1925450d876addc003036886663",
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
      "output": "2 0 32767"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 0 32766"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 0 32767"
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
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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


## sample_024 — train

```c


#include <stdio.h>
 int main ()
 {
    int v1, v2, v3, min, meio, max;

    printf("Introduza 3 números inteiros: \n");
    scanf("%d %d %d", &v1, &v2, &v3);

     if ((v1 < v2) && (v1 < v3))
    {
        min = v1;
    }
     if ((v2 < v1) && (v2 < v3))
    {
        min = v2;
    }
     if ((v3 < v1) && (v3 < v2))
    {
        min = v3;
    }

     if (min == v1)
    {
        if(v2 < v3)
        {
            meio = v2;
            max = v3;
        }
        else
        {
            meio = v3;
            max = v2;
        }
    }
     if (min == v2)
    {
        if (v1 < v3)
        {
            meio = v1;
            max = v3;
        }
        else
        {
            meio = v3;
            max = v1;
        }  
    }
     if (min == v3)
    {
        if (v1 < v2)
        {
            meio = v1;
            max = v2;
        }
        else
        {
            meio = v2;
            max = v1;
        }
    }
    printf("%d %d %d\n", min, meio, max);  
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
  "source_sha256": "112e395806fd3fcee7b4798d8eee1c44db33da9b702b69a97a121e328f26fa12",
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
      "output": "Introduza 3 números inteiros: \n1 2 6\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "Introduza 3 números inteiros: \n2 6 10\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "Introduza 3 números inteiros: \n-8 -1 10\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "Introduza 3 números inteiros: \n7 20 100\n"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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
            if (vetor[i] >= vetor[n])
            {
                stand = vetor[n];
                vetor[n] = vetor[i];
                vetor[i] = stand;
            } 
        }
    } 
    for (i = INICIO; i < LENGTH; i++)
        printf("%d\n", vetor[i]);
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
  "source_sha256": "203ed84541142eab4ca2ae22c9ad40b95d0e861429820a2cb71ea614b2f94f49",
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
      "output": "6\n2\n1\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "10\n6\n2\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "10\n-1\n-8\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "100\n20\n7\n"
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
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "1",
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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


## sample_027 — validation

```c

#include <stdio.h>

int main(){
    int a, b, c;

    printf("Introduza 3 numeros inteiros:\n");
    scanf("%d%d%d", &a, &b, &c);

    if (a > b) { int temp = a; a = b; b = temp; }
    if (b > c) { int temp = b; b = c; c = temp; }
    if (a > b) { int temp = a; a = b; b = temp; }

    printf("%d%d%d\n", a, b, c);
    return 0;    
}

```

```json
{
  "sample_id": "sample_027",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "261eb8902b263b949051008bacf0563658dc036eb276eb6b2c0ee9a5edb8f9e2",
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
      "output": "Introduza 3 numeros inteiros:\n126\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "Introduza 3 numeros inteiros:\n2610\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "Introduza 3 numeros inteiros:\n-8-110\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "Introduza 3 numeros inteiros:\n720100\n"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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

int main(){
    int a, b, c;
    
    scanf("%d%d%d", &a, &b, &c);

    if (a > b) { int temp = a; a = b; b = temp; }
    if (b > c) { int temp = b; b = c; c = temp; }
    if (a > b) { int temp = a; a = b; b = temp; }

    printf("%d%d%d\n", a, b, c);
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
  "source_sha256": "b52dd0870e025e0a92f9b47f4b6c3dac48d8aba8e8c08a01a76cd51f6c3d4f2d",
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
      "output": "126\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2610\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8-110\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "720100\n"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "medium",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
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


## sample_029 — validation

```c

#include <stdio.h>

int main(){
    int a, b, c, temp;
    scanf("%d%d%d", &a, &b, &c);

    if (a > b) {
        temp = a;
        a = b;
        b = temp;
    }
    if (b > c) {
        temp = b;
        b = c;
        c = temp;
    }
    if (a > b) {
        temp = a;
        a = b;
        b = temp;
    }

    printf("%d%d%d\n", a, b, c);
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
  "source_sha256": "d00bf5e346ac38c08958201362b3d7b47ff9672d05d9f3ed65422acfb6f3278a",
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
      "output": "126\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2610\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8-110\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "720100\n"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "medium",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
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


## sample_030 — validation

```c

#include <stdio.h>

int main () {

    int numUm,numDois,numTres;

    scanf("%d",&numUm);
    scanf("%d",&numDois);
    scanf("%d",&numTres);

    if (numUm < numDois) {
        if (numDois < numTres) {
            printf("%d %d %d\n",numUm,numDois,numTres);
            return 0;
        }

    }

    if (numUm > numDois) {
        if (numDois > numTres) {
            printf("%d %d %d\n",numTres,numDois,numUm);
        return 0;
        }

    }

    if (numDois < numUm) {
        if (numTres > numUm) {
            printf("%d %d %d\n",numDois,numUm,numTres);
            return 0;
        }

    }

    if (numDois > numUm) {
        if (numUm > numTres) {
            printf("%d %d %d\n",numUm,numTres,numDois);
            return 0;
        }

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
  "source_sha256": "1ddc3cd6ac65c61abd1041a3758d601095034ea9fffc8a8b13988580a3cca03e",
  "outcomes": {
    "ex04_0": "fail",
    "ex04_1": "pass",
    "ex04_2": "pass",
    "ex04_3": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex04_0",
      "input": "6 1 2",
      "expected": "1 2 6\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "pass",
    "test:ex04_2": "pass",
    "test:ex04_3": "pass",
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
    "stdout:ex04_0:relation": "empty",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "__unknown__",
    "stdout:ex04_1:edit_band": "__unknown__",
    "stdout:ex04_2:relation": "__unknown__",
    "stdout:ex04_2:edit_band": "__unknown__",
    "stdout:ex04_3:relation": "__unknown__",
    "stdout:ex04_3:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex04_0": "fail",
    "test:ex04_1": "pass",
    "test:ex04_2": "pass",
    "test:ex04_3": "pass",
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


## sample_031 — validation

```c

#include <stdio.h>

int main() {
    int num1,num2,num3;
    scanf("%d %d %d",&num1,&num2,&num3);
    if (num1>=num2&&num1>=num3)
    {
        if (num2>=num3)
        {
            printf("%d %d %d",num1,num2,num3);
        }
        else{
            printf("%d %d %d",num1,num3,num2);
        }
    }
    else if (num2>=num1&&num2>=num3)
    {
        if (num1>=num3)
        {
            printf("%d %d %d",num2,num1,num3);
        }
        else {
            printf("%d %d %d",num2,num3,num1);
        }
    }
    else{
        if (num2>=num1)
        {
            printf("%d %d %d",num3,num2,num1);
        }
        else{
            printf("%d %d %d",num3,num1,num2);
        }        
    }
    return 0;
    }
```

```json
{
  "sample_id": "sample_031",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "8a035847f2a05624ea8753a9945e0a6025bcc38778024fe035bfea4a07161e43",
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
      "output": "6 2 1"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "10 6 2"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "10 -1 -8"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "100 20 7"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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


## sample_032 — train

```c

#include <stdio.h>

int main()
{
    int x1,x2,x3,max,min,med;
    scanf("%d %d %d",&x1,&x2,&x3);
    max = x1>x2? (x1>x3? x1:x3) : (x2>x3? x2:x3);
    min = x1<x2? (x1<x3? x1:x3) : (x2<x3? x2:x3);
    med = x1<x2? (x1>x3?x1:x3) : (x2>x3?x2:x3);  
    printf(" max : %d\n",max);
    printf("med :%d\n",med);
    printf("min :%d\n",min);
    return printf("%d %d %d\n",min,med,max)== EOF ;
}
```

```json
{
  "sample_id": "sample_032",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "d3fecdc8a8d7c1d8bc10a78727c720b1ede453fa76ade5370e80fd1efa1716a9",
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
      "output": " max : 6\nmed :2\nmin :1\n1 2 6\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": " max : 10\nmed :6\nmin :2\n2 6 10\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": " max : 10\nmed :-1\nmin :-8\n-8 -1 10\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": " max : 100\nmed :20\nmin :7\n7 20 100\n"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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


## sample_033 — validation

```c

#include <stdio.h>
int main()
{
    int v1, v2, v3, intmd;

    scanf("%d%d%d", &v1, &v2, &v3);
    if (v1>v2)
    {
        intmd = v2;
        v2 = v1;
        v1 = intmd;
    }
    if (v2>v3)
    {
        intmd = v3;
        v3 = v2;
        v2 = intmd;
    }
    if (v1>v2)
    {
        intmd = v2;
        v2 = v1;
        v1 = intmd;
    }
    printf("%d%d%d", v1, v2 ,v3);
    return 0;
}
```

```json
{
  "sample_id": "sample_033",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "43f4a394a832821676e3780bdf45ee87e492ec4a5e47bbd16753605781bdd21a",
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
      "output": "126"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2610"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8-110"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "720100"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "medium",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
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


## sample_034 — train

```c


#include <stdio.h>

int main() {
    
    int a, b, c;
    int aux;

    scanf("%d%d%d",&a,&b,&c);

    if (b < a) {
        aux = a;
        a = b;
        b = aux;
    }

    if (c < b) {
        aux = b;
        b = c;
        c = aux;
    }

    printf("%d %d %d\n",a,b,c);
    
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
  "source_sha256": "756d7260f2a7fdbf919fcccc9d0c2aed6bae11ef495952a410f122c372b56873",
  "outcomes": {
    "ex04_0": "pass",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "6 2 10\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-1 -8 10\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "20 7 100\n"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "pass",
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
    "stdout:ex04_0:relation": "__unknown__",
    "stdout:ex04_0:edit_band": "__unknown__",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex04_0": "pass",
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


## sample_035 — validation

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
  "sample_id": "sample_035",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "f49c4fb585cc7b8c0a22f0fec550b668029b4e2884e7826195fe790fde87361c",
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
      "output": ""
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": ""
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": ""
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": ""
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
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "empty",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "empty",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "empty",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "empty",
    "stdout:ex04_3:edit_band": "large"
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


## sample_037 — train

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
    if(n3 < n1) printf("%d%d%d",n3,n1,n2); 

    else if(n3 < n2) printf("%d%d%d",n1,n3,n2);

    else printf("%d%d%d",n1,n2,n3);
    
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
  "source_sha256": "bb9682d2a7e83e176aecfe12d2973ee951735f2c36c4cac77e89abe42102322a",
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
      "output": "126"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2610"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8-110"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "720100"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "medium",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
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


## sample_038 — train

```c


#include <stdio.h>

int main() {

    int n1,n2,n3, aux;

    scanf("%d%d%d\n",&n1,&n2,&n3);
    
    if(n1 > n2) {
        aux = n1;
        n1 = n2;
        n2 = aux;
    }
    if(n3 < n1) printf("%d%d%d",n3,n1,n2);

    else if(n3 < n2) printf("%d%d%d",n1,n3,n2);

    else printf("%d%d%d",n1,n2,n3);
    
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
  "source_sha256": "d4a2bc8808fddd349071d1c68f74d73edae29a45e4dbe3dc1e305f37452943db",
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
      "output": "126"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2610"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8-110"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "720100"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "medium",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
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


## sample_039 — train

```c

#include <stdio.h>

int main() {
    int num_1, num_2, num_3, auxiliar;
    scanf("%d %d %d", &num_1,&num_2,&num_3);
    if (num_1>num_2) {
        auxiliar=num_1;
        num_1=num_2;
        num_2=auxiliar;
    }

    if (num_3>num_2) {
        printf("%d %d %d\n", num_1,num_2,num_3);
    } else {
        printf("%d %d %d\n", num_1,num_3,num_2);
    }

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
  "source_sha256": "53dd1e72d02b1bb051d59ac8f7ac7b596ef495b0b014cb25084f4bf50a21340b",
  "outcomes": {
    "ex04_0": "pass",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "6 2 10\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-1 -8 10\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "20 7 100\n"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "pass",
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
    "stdout:ex04_0:relation": "__unknown__",
    "stdout:ex04_0:edit_band": "__unknown__",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex04_0": "pass",
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


## sample_041 — train

```c

#include <stdio.h>

void swap(int nums[], int idx)
{
    int numA;
    numA = nums[idx];
    nums[idx] = nums[idx + 1];
    nums[idx + 1] = numA; 
}

int main()
{
    int nums[3];

    scanf("%d", &nums[0]);
    scanf("%d", &nums[1]);
    scanf("%d", &nums[2]);

    if (nums[0] >= nums [1])
    {
        swap(nums, 0);
    }
    
    if (nums[1] >= nums [2])
    {
        swap(nums, 1);
    }

     if (nums[0] >= nums [1])
    {
        swap(nums, 0);
    }
    
    printf("%d%d%d\n", nums[0], nums[1], nums[2]);
    return 0;
}



```

```json
{
  "sample_id": "sample_041",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "d44cce96065c3a31e3dceaa27d114e40d9008f977e74e581f5dab879f5f52c13",
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
      "output": "126\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2610\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8-110\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "720100\n"
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
    "ast:c_subscript": "1",
    "ast:c_zero_index": "1",
    "ast:c_one_index": "1",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "1",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "medium",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
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
    "ast:c_subscript": "1",
    "ast:c_zero_index": "1",
    "ast:c_one_index": "1",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "1",
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

int main(){
    int contador=1, num, meio=0,menor=0,maior=0;
    scanf("%d", &num);
    maior=num; 
    menor=num; 
    meio=num; 
    while (contador<3){
        
        scanf("%d", &num);
        if (maior<num){ 
            maior=num; 
        }
        if (menor>num){ 
            menor=num; 
        }
        else{
            meio=num;
        }
        contador ++;
    }

    printf("%d\t%d\t%d\n", menor,meio,maior);
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
  "source_sha256": "ee01c02ebcfc5e7ec46af3dad5759bb8adbd31f28c54e3d275239a957780d5b0",
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
      "output": "1\t2\t6\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2\t10\t10\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8\t10\t10\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7\t100\t100\n"
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
    "ast:c_update": "1",
    "stdout:ex04_0:relation": "whitespace",
    "stdout:ex04_0:edit_band": "medium",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
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

int main(){
    int contador=1, num, meio=0,menor=0,maior=0;
    scanf("%d", &num);
    maior=num; 
    menor=num; 
    meio=num; 
    while (contador<3){
        
        scanf("%d", &num);
        if (maior<num){ 
            maior=num; 
        }
        if (menor>num){ 
            menor=num; 
        }
        contador ++;
    }

    printf("%d\t%d\t%d\n", menor,meio,maior);
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
  "source_sha256": "98a0fbe0b14c2ce66161b201422de1609aa46d128f5bf45303ddf6fd05609cc8",
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
      "output": "1\t6\t6\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2\t10\t10\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8\t10\t10\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7\t100\t100\n"
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
    "ast:c_update": "1",
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
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

void swap(int* a, int* b){
    int temp=*a;
    *a=*b;
    *b=temp;
}

int main(){
    int a, b, c;
    scanf("%d%d%d", &a,&b,&c);
    if (a>b)swap(&a, &b);
    if (b>c)swap(&b, &c);
    if (a>c)swap(&a,&c);
    printf("%d %d %d\n", a, b,c);
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
  "source_sha256": "94b87bbe58b7ce4f3f6a46115e778e8bd39fd08b8f647b3587a9cd3ba215479d",
  "outcomes": {
    "ex04_0": "pass",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "6 2 10\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-1 -8 10\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "20 7 100\n"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "pass",
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
    "ast:c_pointer_declarator": "1",
    "ast:c_pointer_parameter": "1",
    "ast:c_array_parameter": "0",
    "ast:c_dereference": "1",
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "__unknown__",
    "stdout:ex04_0:edit_band": "__unknown__",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex04_0": "pass",
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
    "ast:c_pointer_declarator": "1",
    "ast:c_pointer_parameter": "1",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_dereference": "1",
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

int main() {
    int a, b, c;
    scanf("%d%d%d", &a, &b, &c);
    if (a<=b) {
        if (c<=b) {
            (a>=c) ? printf("%d%d%d\n", c, a, b) : printf("%d%d%d\n", a, c, b);
        } else {
            printf("%d%d%d\n", a, b, c);
        }
    } else {
        if (c<=a) {
            (b>=c) ? printf("%d%d%d\n", c, b, a) : printf("%d%d%d\n", b, c, a);
        } else {
            printf("%d%d%d\n", b, a, c);
        }
    }
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
  "source_sha256": "f37677f932d38fb96fcf4a86ef5b95c4b681f8b3005adc7fe6f669e76561c6de",
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
      "output": "126\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2610\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8-110\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "720100\n"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "medium",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
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


## sample_046 — train

```c

#include <stdio.h>

int main() {
    int n1,n2,n3;
    scanf("%d %d %d", &n1, &n2,& n3);
    if (n1<n2) {
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
  "sample_id": "sample_046",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "ef723abc2ee9e61fa08de5303f4153eed11b7c63ef4d6dc214e7e08d40d14176",
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
      "output": "2 6 1"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2 10 6"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8 10 -1"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "7 100 20"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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


## sample_047 — train

```c

#include<stdio.h>

int N, M, P;



int main () {
    printf("Introduza o primeiro número: ");
    scanf("%d", &N);        

    printf("Introduza o segundo número: ");
    scanf("%d", &M);

    printf("Introduza o terceiro número: ");
    scanf("%d", &P);

   if (N < M && M < P) {
        printf("%d\n%d\n%d\n", N, M, P);
    }
    else if (N < P && P < M) {
         printf("%d\n%d\n%d\n", N, P, M);
    }
     else {
         printf("%d\n%d\n%d\n", P, M, N);
    }

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
  "source_sha256": "b012d83011be655f41731e55b0a8cdac2beb7b507071fc53c77f74c43a556729",
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
      "output": "Introduza o primeiro número: Introduza o segundo número: Introduza o terceiro número: 2\n1\n6\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "Introduza o primeiro número: Introduza o segundo número: Introduza o terceiro número: 2\n6\n10\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "Introduza o primeiro número: Introduza o segundo número: Introduza o terceiro número: -8\n-1\n10\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "Introduza o primeiro número: Introduza o segundo número: Introduza o terceiro número: 7\n20\n100\n"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "large",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "large",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "large",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "large"
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


## sample_048 — train

```c


#include <stdio.h>

int main(){
    int num1, num2, num3;
    int list[3];

    scanf("%d %d %d", &num1, &num2, &num3);

    if (num1 < num2){
        if (num2 < num3){
            list[0] = num3;
            list[1] = num2;
            list[2] = num1;
        }
        else {
            list[0] = num2;
            list[1] = num3;
            list[2] = num1;
        }
    }
    else if (num1 < num3){
        list[0] = num3;
        list[1] = num1;
        list[2] = num2;
    }
    else {
        list[0] = num1;
        list[1] = num3;
        list[2] = num2;
    }

    printf("%d %d %d\n", list[2], list[1], list[0]);

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
  "source_sha256": "fbe3e07d52ae8bf5cb82d2f17d0f5b0f0cbf136a9d651386e648422e51fb0aed",
  "outcomes": {
    "ex04_0": "pass",
    "ex04_1": "fail",
    "ex04_2": "fail",
    "ex04_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "6 2 10\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-1 -8 10\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "20 7 100\n"
    }
  ],
  "clustering_oav": {
    "test:ex04_0": "pass",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
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
    "ast:c_update": "0",
    "stdout:ex04_0:relation": "__unknown__",
    "stdout:ex04_0:edit_band": "__unknown__",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex04_0": "pass",
    "test:ex04_1": "fail",
    "test:ex04_2": "fail",
    "test:ex04_3": "fail",
    "ast:c_for": "0",
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

int main() {
    int a,b,c,maior,menor,meio;
    scanf("%d%d%d",&a,&b,&c);
    maior=a;
    if(b>maior) maior = b;
    if(c>maior) maior = c;
    menor=a;
    if(b<menor) menor = b;
    if(c<menor) menor = c;
    meio=a;
    if (meio==maior) meio = b;
    if (meio==menor) meio = c;
    printf("%d%d%d\n",menor,meio,maior);
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
  "source_sha256": "d60f7e8d0eae3cb329f8ecb4e6e7f2c5825d3839bd1d5a63f86be39d11df1a69",
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
      "output": "126\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2610\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8-110\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "720100\n"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "medium",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
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


## sample_050 — train

```c

#include <stdio.h>

int main() {
    int a,b,c,maior,menor,meio;
    scanf("%d%d%d",&a,&b,&c);
    maior=a;
    if(b>maior) maior = b;
    if(c>maior) maior = c;
    menor=a;
    if(b<menor) menor = b;
    if(c<menor) menor = c;
    meio = a + b + c - maior - menor;
    printf("%d%d%d\n",menor,meio,maior);
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
  "source_sha256": "58b718cc45143e13aef566d498891cf91748085974612c3bb03e1669688c020b",
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
      "output": "126\n"
    },
    {
      "test_id": "ex04_1",
      "input": "10 6 2",
      "expected": "2 6 10\n",
      "output": "2610\n"
    },
    {
      "test_id": "ex04_2",
      "input": "10 -1 -8",
      "expected": "-8 -1 10\n",
      "output": "-8-110\n"
    },
    {
      "test_id": "ex04_3",
      "input": "100 20 7",
      "expected": "7 20 100\n",
      "output": "720100\n"
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
    "stdout:ex04_0:relation": "different",
    "stdout:ex04_0:edit_band": "medium",
    "stdout:ex04_1:relation": "different",
    "stdout:ex04_1:edit_band": "medium",
    "stdout:ex04_2:relation": "different",
    "stdout:ex04_2:edit_band": "medium",
    "stdout:ex04_3:relation": "different",
    "stdout:ex04_3:edit_band": "medium"
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
  "members/sample_014/tests/ex04_1",
  "members/sample_014/tests/ex04_2",
  "members/sample_014/tests/ex04_3",
  "members/sample_015/raw_code",
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
  "members/sample_028/tests/ex04_3",
  "members/sample_029/raw_code",
  "members/sample_029/tests/ex04_0",
  "members/sample_029/tests/ex04_1",
  "members/sample_029/tests/ex04_2",
  "members/sample_029/tests/ex04_3",
  "members/sample_030/raw_code",
  "members/sample_030/tests/ex04_0",
  "members/sample_031/raw_code",
  "members/sample_031/tests/ex04_0",
  "members/sample_031/tests/ex04_1",
  "members/sample_031/tests/ex04_2",
  "members/sample_031/tests/ex04_3",
  "members/sample_032/raw_code",
  "members/sample_032/tests/ex04_0",
  "members/sample_032/tests/ex04_1",
  "members/sample_032/tests/ex04_2",
  "members/sample_032/tests/ex04_3",
  "members/sample_033/raw_code",
  "members/sample_033/tests/ex04_0",
  "members/sample_033/tests/ex04_1",
  "members/sample_033/tests/ex04_2",
  "members/sample_033/tests/ex04_3",
  "members/sample_034/raw_code",
  "members/sample_034/tests/ex04_1",
  "members/sample_034/tests/ex04_2",
  "members/sample_034/tests/ex04_3",
  "members/sample_035/raw_code",
  "members/sample_035/tests/ex04_0",
  "members/sample_035/tests/ex04_1",
  "members/sample_035/tests/ex04_2",
  "members/sample_035/tests/ex04_3",
  "members/sample_036/raw_code",
  "members/sample_036/tests/ex04_1",
  "members/sample_036/tests/ex04_2",
  "members/sample_036/tests/ex04_3",
  "members/sample_037/raw_code",
  "members/sample_037/tests/ex04_0",
  "members/sample_037/tests/ex04_1",
  "members/sample_037/tests/ex04_2",
  "members/sample_037/tests/ex04_3",
  "members/sample_038/raw_code",
  "members/sample_038/tests/ex04_0",
  "members/sample_038/tests/ex04_1",
  "members/sample_038/tests/ex04_2",
  "members/sample_038/tests/ex04_3",
  "members/sample_039/raw_code",
  "members/sample_039/tests/ex04_1",
  "members/sample_039/tests/ex04_2",
  "members/sample_039/tests/ex04_3",
  "members/sample_040/raw_code",
  "members/sample_040/tests/ex04_0",
  "members/sample_040/tests/ex04_1",
  "members/sample_040/tests/ex04_2",
  "members/sample_040/tests/ex04_3",
  "members/sample_041/raw_code",
  "members/sample_041/tests/ex04_0",
  "members/sample_041/tests/ex04_1",
  "members/sample_041/tests/ex04_2",
  "members/sample_041/tests/ex04_3",
  "members/sample_042/raw_code",
  "members/sample_042/tests/ex04_0",
  "members/sample_042/tests/ex04_1",
  "members/sample_042/tests/ex04_2",
  "members/sample_042/tests/ex04_3",
  "members/sample_043/raw_code",
  "members/sample_043/tests/ex04_0",
  "members/sample_043/tests/ex04_1",
  "members/sample_043/tests/ex04_2",
  "members/sample_043/tests/ex04_3",
  "members/sample_044/raw_code",
  "members/sample_044/tests/ex04_1",
  "members/sample_044/tests/ex04_2",
  "members/sample_044/tests/ex04_3",
  "members/sample_045/raw_code",
  "members/sample_045/tests/ex04_0",
  "members/sample_045/tests/ex04_1",
  "members/sample_045/tests/ex04_2",
  "members/sample_045/tests/ex04_3",
  "members/sample_046/raw_code",
  "members/sample_046/tests/ex04_0",
  "members/sample_046/tests/ex04_1",
  "members/sample_046/tests/ex04_2",
  "members/sample_046/tests/ex04_3",
  "members/sample_047/raw_code",
  "members/sample_047/tests/ex04_0",
  "members/sample_047/tests/ex04_1",
  "members/sample_047/tests/ex04_2",
  "members/sample_047/tests/ex04_3",
  "members/sample_048/raw_code",
  "members/sample_048/tests/ex04_1",
  "members/sample_048/tests/ex04_2",
  "members/sample_048/tests/ex04_3",
  "members/sample_049/raw_code",
  "members/sample_049/tests/ex04_0",
  "members/sample_049/tests/ex04_1",
  "members/sample_049/tests/ex04_2",
  "members/sample_049/tests/ex04_3",
  "members/sample_050/raw_code",
  "members/sample_050/tests/ex04_0",
  "members/sample_050/tests/ex04_1",
  "members/sample_050/tests/ex04_2",
  "members/sample_050/tests/ex04_3"
]
```
