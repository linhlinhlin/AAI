# lab03-ex01--kmeans--combined_stdout--s42--c1

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 91; phân vùng: {'validation': 18, 'train': 73}.


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
    "n_cluster": 91,
    "n_observed": 91,
    "n_failed": 91,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 91
    }
  },
  {
    "test_id": "ex01_1",
    "n_cluster": 91,
    "n_observed": 91,
    "n_failed": 91,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 91
    }
  },
  {
    "test_id": "ex01_2",
    "n_cluster": 91,
    "n_observed": 91,
    "n_failed": 91,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 91
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex01_1:edit_band",
    "value": "small",
    "n": 90,
    "n_cluster": 91,
    "rate": 0.989010989010989,
    "cohort_rate": 0.6691176470588235,
    "difference_from_cohort": 0.31989334195216557
  },
  {
    "feature": "stdout:ex01_0:edit_band",
    "value": "small",
    "n": 84,
    "n_cluster": 91,
    "rate": 0.9230769230769231,
    "cohort_rate": 0.625,
    "difference_from_cohort": 0.29807692307692313
  },
  {
    "feature": "stdout:ex01_0:relation",
    "value": "whitespace",
    "n": 91,
    "n_cluster": 91,
    "rate": 1.0,
    "cohort_rate": 0.7279411764705882,
    "difference_from_cohort": 0.2720588235294118
  },
  {
    "feature": "stdout:ex01_1:relation",
    "value": "whitespace",
    "n": 91,
    "n_cluster": 91,
    "rate": 1.0,
    "cohort_rate": 0.7279411764705882,
    "difference_from_cohort": 0.2720588235294118
  },
  {
    "feature": "stdout:ex01_2:relation",
    "value": "whitespace",
    "n": 91,
    "n_cluster": 91,
    "rate": 1.0,
    "cohort_rate": 0.7279411764705882,
    "difference_from_cohort": 0.2720588235294118
  },
  {
    "feature": "stdout:ex01_2:edit_band",
    "value": "small",
    "n": 90,
    "n_cluster": 91,
    "rate": 0.989010989010989,
    "cohort_rate": 0.7279411764705882,
    "difference_from_cohort": 0.26106981254040085
  },
  {
    "feature": "ast:c_while",
    "value": "0",
    "n": 67,
    "n_cluster": 91,
    "rate": 0.7362637362637363,
    "cohort_rate": 0.6617647058823529,
    "difference_from_cohort": 0.07449903038138339
  },
  {
    "feature": "ast:c_if",
    "value": "0",
    "n": 54,
    "n_cluster": 91,
    "rate": 0.5934065934065934,
    "cohort_rate": 0.5220588235294118,
    "difference_from_cohort": 0.07134776987718161
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 75,
    "n_cluster": 91,
    "rate": 0.8241758241758241,
    "cohort_rate": 0.7867647058823529,
    "difference_from_cohort": 0.03741111829347121
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 91,
    "n_cluster": 91,
    "rate": 1.0,
    "cohort_rate": 0.9705882352941176,
    "difference_from_cohort": 0.02941176470588236
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 77,
    "n_cluster": 91,
    "rate": 0.8461538461538461,
    "cohort_rate": 0.8235294117647058,
    "difference_from_cohort": 0.022624434389140302
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 83,
    "n_cluster": 91,
    "rate": 0.9120879120879121,
    "cohort_rate": 0.8897058823529411,
    "difference_from_cohort": 0.022382029734970943
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 90,
    "n_cluster": 91,
    "rate": 0.989010989010989,
    "cohort_rate": 0.9705882352941176,
    "difference_from_cohort": 0.01842275371687141
  },
  {
    "feature": "ast:c_do",
    "value": "0",
    "n": 89,
    "n_cluster": 91,
    "rate": 0.978021978021978,
    "cohort_rate": 0.9705882352941176,
    "difference_from_cohort": 0.0074337427278603485
  },
  {
    "feature": "test:ex01_0",
    "value": "fail",
    "n": 91,
    "n_cluster": 91,
    "rate": 1.0,
    "cohort_rate": 0.9926470588235294,
    "difference_from_cohort": 0.007352941176470562
  },
  {
    "feature": "test:ex01_1",
    "value": "fail",
    "n": 91,
    "n_cluster": 91,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "test:ex01_2",
    "value": "fail",
    "n": 91,
    "n_cluster": 91,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_do",
    "value": "1",
    "n": 2,
    "n_cluster": 91,
    "rate": 0.02197802197802198,
    "cohort_rate": 0.029411764705882353,
    "difference_from_cohort": -0.007433742727860373
  },
  {
    "feature": "ast:c_update",
    "value": "0",
    "n": 1,
    "n_cluster": 91,
    "rate": 0.01098901098901099,
    "cohort_rate": 0.029411764705882353,
    "difference_from_cohort": -0.01842275371687136
  },
  {
    "feature": "ast:c_for",
    "value": "0",
    "n": 8,
    "n_cluster": 91,
    "rate": 0.08791208791208792,
    "cohort_rate": 0.11029411764705882,
    "difference_from_cohort": -0.0223820297349709
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 75,
    "n_cluster": 91,
    "rate": 0.8241758241758241,
    "cohort_rate": 0.7867647058823529,
    "difference_from_cohort": 0.03741111829347121
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 91,
    "n_cluster": 91,
    "rate": 1.0,
    "cohort_rate": 0.9705882352941176,
    "difference_from_cohort": 0.02941176470588236
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 77,
    "n_cluster": 91,
    "rate": 0.8461538461538461,
    "cohort_rate": 0.8235294117647058,
    "difference_from_cohort": 0.022624434389140302
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 83,
    "n_cluster": 91,
    "rate": 0.9120879120879121,
    "cohort_rate": 0.8897058823529411,
    "difference_from_cohort": 0.022382029734970943
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 90,
    "n_cluster": 91,
    "rate": 0.989010989010989,
    "cohort_rate": 0.9705882352941176,
    "difference_from_cohort": 0.01842275371687141
  },
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 91,
    "n_cluster": 91,
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
      "stdout:ex01_1:edit_band=small",
      "NOT (ast:c_if=0)"
    ],
    "then_cluster": 1,
    "train_support": 27,
    "train_precision": 1.0,
    "holdout_support": 9,
    "holdout_precision": 1.0
  },
  {
    "rule_id": 7,
    "if": [
      "stdout:ex01_1:edit_band=small",
      "ast:c_if=0",
      "NOT (ast:c_while=1)"
    ],
    "then_cluster": 1,
    "train_support": 34,
    "train_precision": 0.9705882352941176,
    "holdout_support": 4,
    "holdout_precision": 1.0
  },
  {
    "rule_id": 8,
    "if": [
      "stdout:ex01_1:edit_band=small",
      "ast:c_if=0",
      "ast:c_while=1"
    ],
    "then_cluster": 1,
    "train_support": 13,
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
  "reasoning": "Có 91 bài trong cụm. Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
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

sample_006, sample_003, sample_020, sample_008

## sample_003 — validation — đại diện

```c
#include <stdio.h>
#include <stdlib.h>
void quadrado(int N)
{
    int i, j, *arr;
    arr = malloc(N * sizeof(int));
    for (i = 0; i < N; i++)
    {
        arr[i] = i + 1;
    }
    for (i = 0; i < N; i++)
    {
        for (j = 0; j < N; j++)
        {
            printf("%d\t", arr[j]);
            arr[j]++;
        }
        if (i != N - 1)
        {
            printf("\n");
        }
    }
    free(arr);
}

int main()
{
    int N;
    scanf("%d", &N);

    while (N < 2)
    {
        scanf("%d", &N);
    }

    quadrado(N);
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
  "source_sha256": "459b07b5086b3fa946d5b296f8ad09a2f7467a08f25ecc3c656353a258f7d2f0",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "1",
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


void quadrado(int N)
{
	int i, j;

	for(i = 0; i < N; i++)
	{
		for(j = 1; j <= N; j++)
		{
			printf("%d\t", i + j);
		}
		printf("\n");
	}
}

int main()
{
	int in;
	scanf("%d", &in);

	quadrado(in);

	return 0;
}

```

```json
{
  "sample_id": "sample_006",
  "partition": "train",
  "representative": true,
  "is_train_medoid": true,
  "raw_code_truncated": false,
  "source_sha256": "b40527b8a5f39a69f3f93498fc40c770bd0b35a930bbb7cbc12ea28512c3319e",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_008 — train — đại diện

```c
#include <stdio.h>

void quadrado(int N);

int main()
{
	int N = 0;

	scanf("%d", &N);
	while (N <= 2);
	quadrado(N);
	return 0;
}

void quadrado(int N)
{	int valor, digito, contador;
	for (digito = 1; digito <= N; digito++)
	{	valor = digito;
		contador = 1;
		do{
			printf("%d\t", valor);
			valor++;
			contador++;
		} while (contador <= N);
		putchar('\n');
	}
}
```

```json
{
  "sample_id": "sample_008",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "db8418602785951621841b6d1fedbd85d03cd4970113dbe9b983f69aaa4a132e",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "1",
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


## sample_020 — train — đại diện

```c
# include <stdio.h>


void quadrado(int N){
    int largura=1,comprimento=1,num=1;
    while(largura<=N){
        while(comprimento<=N){
            printf("%d\t",num);
            num+=1;
            comprimento+=1;
        }
        printf("\n");
        comprimento=1;
        largura+=1;
        num=largura;
    }

}
int main(){
    int N;
    scanf("%d",&N);
    quadrado(N);
    return 0;
}
```

```json
{
  "sample_id": "sample_020",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "13ea828dc9ff5bc72fe68ba2925f857aa9a966a258f866789aca469707656a73",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_001 — validation

```c
#include <stdio.h>
#include <stdlib.h>
void quadrado(int N)
{
    int i, j, *arr;
    arr = malloc(N * sizeof(int));
    for (i = 0; i < N; i++)
    {
        arr[i] = i + 1;
    }
    for (i = 0; i < N; i++)
    {
        for (j = 0; j < N; j++)
        {
            if (j != N - 1)
            {
                printf("%d\t", arr[j]);
            }
            else
            {
                printf("%d", arr[j]);
            }
            arr[j]++;
        }
        if (i != N - 1)
        {
            printf("\n");
        }
    }
    free(arr);
}

int main()
{
    int N;
    scanf("%d", &N);

    if (N >= 2)
    {
        quadrado(N);
    }

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
  "source_sha256": "c7d550b0483511a78efb118845bab509efbbd01e13a7c4e38036d96a5e970ad3",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\n2\t3\t4\n3\t4\t5"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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
    "ast:c_pointer_declarator": "1",
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


## sample_002 — validation

```c
#include <stdio.h>
#include <stdlib.h>
void quadrado(int N)
{
    int i, j, *arr;
    arr = malloc(N * sizeof(int));
    for (i = 0; i < N; i++)
    {
        arr[i] = i + 1;
    }
    for (i = 0; i < N; i++)
    {
        for (j = 0; j < N; j++)
        {
            printf("%d\t", arr[j]);
            arr[j]++;
        }
        if (i != N - 1)
        {
            printf("\n");
        }
    }
    free(arr);
}

int main()
{
    int N;
    scanf("%d", &N);

    if (N >= 2)
    {
        quadrado(N);
    }

    return 0;
}

```

```json
{
  "sample_id": "sample_002",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "e341903ed5dd8ca232c8252259e1f1540576bb31dffb611add62aed85bdeb498",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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
    "ast:c_pointer_declarator": "1",
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

void quadrado(int N)
{
    int i = 1, j, k;

    for (j = 1; j <= N; j++)
    {
        for (k = 0; k < N; k++)
        {
            printf("%d\t", i);
            i++;
        }
        i = j + 1;
        printf("\n");
    }
}

int main()
{
    int N;
    scanf("%d", &N);

    while (N < 2)
    {
        scanf("%d", &N);
    }

    quadrado(N);
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
  "source_sha256": "d68bff9c327c8057691ce7990fdf0e3985a76ad40192987a28b046c599eed9ab",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_005 — validation

```c
#include <stdio.h>
#include <stdlib.h>
void quadrado(int N)
{
    int i, j, *arr;
    arr = malloc(N * sizeof(int));
    for (i = 0; i < N; i++)
    {
        arr[i] = i + 1;
    }
    for (i = 0; i < N; i++)
    {
        for (j = 0; j < N; j++)
        {
            printf("%d\t", arr[j]);
            arr[j]++;
        }
        printf("\n");
    }
    free(arr);
}

int main()
{
    int N;
    scanf("%d", &N);

    if (N >= 2)
    {
        quadrado(N);
    }

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
  "source_sha256": "fe50f08f88c6df83ae77107bac1b5dff8ef02da0013d8ed5fe17dab83faad3de",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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
    "ast:c_pointer_declarator": "1",
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


void quadrado(int N)
{
	int i, j;

	for(i = 0; i < N; i++)
	{
		for(j = 1; j <= N; j++)
		{
			printf("%d\t", i + j);
		}
		printf("\n");
	}
}

int main()
{
	int in;
	scanf("%d", &in);

	if(in >= 2) quadrado(in);

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
  "source_sha256": "e4755d8fc5c157bdba4f350ed7c82396f8e48c23dc32abf6a92a9a460ae7956b",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_009 — train

```c
#include <stdio.h>


void quadrado(int N)  {

 int i,j, k = 0;

 for (i=1; i <= N; i++) {

  k ++;

  for(j = k ; j <= N + k -1; j ++) {
  
   printf("%d\t", j); }
  
  printf("\n");} 
}


int main() {
 
 int N;

 scanf("%d",&N);
 
 quadrado(N);

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
  "source_sha256": "871e4e3321bd3d21a076a42c7b5cba943edf5774791f7e33cb26d04af316ed64",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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



void quadrado(int N)
{
    int a, i;
    for(i = 1; i <= N; i++)
    {
        for (a = i; a < N + i; a++)
        {
            printf("%d\t", a);
        }
        printf("\n");
    }
}

int main()
{
    int N;
    scanf("%d", &N);
    quadrado(N);
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
  "source_sha256": "cc8e4d9d1ceffd70e5dbadb0fa498bdf4e76b9280bc3f1cfd3b8c93ffe134691",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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



void quadrado(int n){
    int ad, linha;
        for(linha =1;linha <= n; ++linha){
            for(ad=0; ad < n; ++ad)
                printf("%d\t", linha+ad);
            printf("\n");
            }
}

int main(){
    int n;
    scanf("%d", &n);
    if (n >=2)
        quadrado(n);
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
  "source_sha256": "2b77e188217e29b0f221d78a2ca21eeea7fb59c40c2ed14aec9326e42df92992",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_012 — train

```c
#include <stdio.h>

int main(){
    int n, ad, linha;
    scanf("%d", &n);
    if (n >=2){
        for(linha =1;linha <= n; ++linha){
            for(ad=0; ad < n; ++ad)
                printf("%d\t", linha+ad);
            printf("\n");
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
  "source_sha256": "0cb434f59da3af0e0b7ceca076d16d89fbb53281d2f6f02792a228c1305d0ea6",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_013 — train

```c
#include <stdio.h>

void quadrado(int n);

int main(){
    int n;
    scanf("%d\n", &n);
    if (n >=2)
        quadrado(n);
    return 0;
}


void quadrado(int n){
    int ad, linha;
        for(linha =1;linha <= n; ++linha){
            for(ad=0; ad < n; ++ad)
                printf("%d\t", linha+ad);
            printf("\n");
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
  "source_sha256": "5cf27d32dff6cc32930b5238364df9398af83eb623fe2b68532c9251ce21ae39",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_014 — train

```c
#include <stdio.h>

void quadrado(int N){

    int i, j;
    for (i = 1; i <= N; ++i){
        for (j = i; j < N + i; ++j){
            printf("%d\t", j);
        }
        printf("\n");
    }

}

int main(){
    int N;
    scanf("%d", &N);
    
    quadrado(N);

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
  "source_sha256": "cec103c6f2599b670522c15f8e47a4d7fc380fa73f81e216e8990c56e6934eeb",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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

int main()
{
    int n, count_cols, count_linhas, v_inicial;
    scanf("%d", &n);
    if (n < 2)
    {
        return -1;
    }
    count_cols = count_linhas = 1;
    v_inicial = 1;
    while (count_cols <= n)
    {

        printf("%d", v_inicial);
        count_linhas = 1;
        while (count_linhas < n)
        {
            printf("       %d", count_linhas + v_inicial);
            count_linhas++;
        }
        printf("\n");
        count_cols++;
        v_inicial++;
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
  "source_sha256": "e5612005dda3c56cbabe904a43e6e26dc53222dcf1c9584bf244da19162ff1fb",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1       2       3\n2       3       4\n3       4       5\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1       2       3       4\n2       3       4       5\n3       4       5       6\n4       5       6       7\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1       2       3       4       5       6       7       8\n2       3       4       5       6       7       8       9\n3       4       5       6       7       8       9       10\n4       5       6       7       8       9       10       11\n5       6       7       8       9       10       11       12\n6       7       8       9       10       11       12       13\n7       8       9       10       11       12       13       14\n8       9       10       11       12       13       14       15\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_016 — train

```c
#include <stdio.h>

int main()
{
    int N, N1 = 1, cont;
    scanf("%d", &N);
    for (cont = 1; cont <= N; cont++)
    {
        for (N1 = cont; N1 <= (N - 1 + cont); N1++)
        {
            printf("%d\t", N1);
        }
        printf("\n");
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
  "source_sha256": "3f03a7b4308dae9ed2a15e7ea5c969883fcddcbc2c0d72dee408139ac2fd8b15",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_017 — train

```c
#include <stdio.h>
void quadrado(int N)
{
    int N1 = 1, cont;
    scanf("%d", &N);
    for (cont = 1; cont <= N; cont++)
    {
        for (N1 = cont; N1 <= (N - 1 + cont); N1++)
        {
            printf("%d\t", N1);
        }
        printf("\n");
    }
}
int main()
{
    int N;
    scanf("%d", &N);
    quadrado(N);
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
  "source_sha256": "b20303daff365ada3bd746811fbcb35b56a8a1216d5f31d2c6c92582af3a7dda",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_018 — train

```c
#include <stdio.h>


void quadrado(int n)
{
    int row, col;
    for (row = 0; row < n; row++)
    {
        for (col = 0; col < n; col++)
        {
            printf("%d\t", row + col + 1);
        }
        printf("\n");
    }

    return;
}

int main()
{
    int n;
    scanf("%d", &n);
    if (n >= 2)
        quadrado(n);
    return 0;
}





#define FORA 0
#define DENTRO 1
#define ESC 2




```

```json
{
  "sample_id": "sample_018",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "768b28ac0ab5283aa00f34761f7009cc06cb79ec71e894a23803d6040725f752",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_019 — train

```c
#include <stdio.h>


void quadrado(int n)
{
	int i, j;

	for(i = 1; i <= n; i++) {
		for(j = i; j < n+i; j++)
			printf("%d\t", j);
		printf("\n");
	}
}

int main()
{
	int n;
	scanf("%d", &n);
	if (n < 2) return 1;

	quadrado(n);
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
  "source_sha256": "c9fc6311f46c4989d5ad535712b76404e70dd607241d01d26508fdfcfdc0eed8",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_021 — train

```c
#include <stdio.h>

void quadrado (int N) {
    int  i, z;
  
    if (N >= 2) {
  
        for (i = 1; i<=N; i++) {
            for (z = i; z < i+N; z++)
                printf("%d\t", z);
            printf("\n");
        }
    }
    return;
}


int main () {
    int N;
    scanf("%d",&N);
    quadrado(N);
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
  "source_sha256": "2825e853bfd8d0f421b324e22a1bf58ca5e3cad1c4660d60689d794642d5f843",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_022 — train

```c

#include <stdio.h>

void quadrado(int n);

int main() {

    int N;
    scanf("%d", &N);

    quadrado(N);

    return 0;
}

void quadrado(int n) {
    int i, j;
    int k = 0;

    for (j = 1; j <= n; j++) {
        for (i = 1 + k; i <= n+k; i++) {
            printf("%d\t", i);
            if (i == n + k) {
              printf("\n");  
            }
        }
        k++;  
    }
}
```

```json
{
  "sample_id": "sample_022",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "38bdeed1fb12aefad8212ee47a06b104acecbc27273b4185570d6ab501db576a",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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

void quadrado(int n);

int main() {

    int N;
    scanf("%d", &N);

    quadrado(N);

    return 0;
}

void quadrado(int n) {
    int i, j;
    int k = 0;

    for (j = 1; j <= n; j++) {
        for (i = 1 + k; i <= n+k; i++) {
            printf("%d\t", i);
        }
        k++;
        printf("\n");
    }
}
```

```json
{
  "sample_id": "sample_023",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "a6778deab28e965494ff1bb9fa31c7daf02d38b46d9340a3b99a26b1c250a13a",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_024 — validation

```c


#include <stdio.h>

void quadrado(int n){
    int i, j, estado = 0;
    for (j = 1; n >= j; j++){
        for (i = 1; n >= i; i++){
            printf("%d\t", i + estado);
        }
        estado ++;
        printf("\n");
    }
}

int main(){
    int n;
    scanf("%d",&n);
    quadrado(n);
    return 0;
}
```

```json
{
  "sample_id": "sample_024",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "863bb1c39b53496ee3877dd566cba664a3b81ba1bc7a5dbccf5e267a10848e7a",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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

void quadrado(int N){
    int inicial, num;
    for (inicial = 1; inicial <= N; inicial++){
        for (num = inicial; num < inicial + N; num++){
            printf("%d\t", num);
        }
        printf("\n");
    }
}


int main(){
    int N;
    scanf("%d\n", &N);
    while(N<2)
        scanf("%d\n", &N);
    quadrado(N);
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
  "source_sha256": "2a4675c3308bbb10ad9e7af0d4afbda589b0a75fbc743f17fb6db4457952fa1a",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_026 — train

```c

#include <stdio.h>

void quadrado(int N) {
    int i=1,num=N,voltas=0;
    while (N<2) {
        scanf("%d",&N);
    }
    for(;N>0;N--){
        for(;i<=(num+voltas);i++) {
            printf("%d\t",i);
        }
        voltas+=1;
        i=voltas+1;
        printf("\n");
    } 
}
int main (){
    int N;
    scanf("%d",&N);
    quadrado(N);
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
  "source_sha256": "c87733bbb0ae896e6401f1483a38a9690f67bcabb9c65bd4a7960fb31c1e9183",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_027 — train

```c

#include <stdio.h>

void quadrado(int N) {
    int i=1,num=N,voltas=0;
    while (N<2) {
        scanf("%d",&N);
    }
    for(;N>0;N--){
        for(;i<=(num+voltas);i++) {
            printf("%d\t",i);
        }
        voltas+=1;
        i=voltas+1;
        printf("\n");
    } 
}
int main (){
    int M;
    scanf("%d",&M);
    quadrado(M);
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
  "source_sha256": "689bdb18ec41789ca6e4f6c605b39fc3cea93a3a8c4cb333c365525073dd2339",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_028 — train

```c

#include<stdio.h>

void quadrado(int N){
    int i,j, aux=0;

    for(i=0;i<N;i++){ 
        for(j=0;j<N;j++){ 
            aux=i+j+1;
            printf("%d\t",aux);
            if(j==N-1)
                printf("\n");
        }
    }
}  


int main(){

int N;
    scanf("%d",&N);

    if(N>=2)
        quadrado(N);
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
  "source_sha256": "9a00f1d9e87dff6cc4b14326eb208e039915800870f834061b375825673d7bc5",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_029 — train

```c

#include <stdio.h>

void quadrado(){

    int contador, n, i, num=1;
    scanf("%d", &n);
    for (contador = 1; contador <= n; contador++){
        num = contador;
        for (i = 1; i <= n; i++){
            printf("%d\t", num);
            num++;
        }
    printf("\n");
    }   

}

int main(){
    
    quadrado();
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
  "source_sha256": "c2be7bc68464933905618240e293df42295d4add59858d2802e5b9a45fb7cfde",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_030 — train

```c

#include<stdio.h>
#define minimo 2
void quadrado ( int N){

int i, j ; 
for (i = 0 ; i<N ; i++){
    for ( j= 0; j < N ; j++){        

        printf("%d\t" , (1+i+j) );
    }

    printf("\n");
}
}

int main (){

int N;
scanf("%d", &N);
while ( N < minimo){
scanf("%d", &N);
}
quadrado (N);

return 0 ;

}

```

```json
{
  "sample_id": "sample_030",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "b69b5097ac2ed0a8568247c759b6c67de229192462979ad6001fe8db4b55d92a",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
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


## sample_031 — train

```c

#include<stdio.h>
#define minimo 2
void quadrado ( int N){

int i, j ; 
for (i = 1 ; i<=N ; i++){
    for ( j= i; j <= i + N-1 ; j++){       

        printf("%d\t" , j );
    }

    printf("\n");
}
}

int main (){

int N;
scanf("%d", &N);
while ( N < minimo){
scanf("%d", &N);


}
quadrado (N);

return 0 ;

}

```

```json
{
  "sample_id": "sample_031",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "2e6e90f2aab1b3ec6778b9f0f72a5e6e2b004464c5d15a06c44c21ff87b26d70",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_032 — train

```c


#include <stdio.h>

void quadrado (int N) {
    int i, j;
    for (i = 0; i < N; i++) {
        for (j = (i + 1); j <= (N + i); j++)
            printf("%d\t", j); 
        printf("\n");
    }
}    

int main() {
    int N;
    scanf("%d", &N);
    quadrado (N);
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
  "source_sha256": "654cbd65d81c1622c859d88a43541153b6479c7f8d911cdfc29165024b06579f",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_033 — validation

```c


#include <stdio.h>

void quadrado(int N){
    int i, j;

    for (i=1; i<=N; i++){
        for (j=1; j<=N; j++){
            printf("%d\t", j+(i-1));
        }
        printf("\n");
    }
}

int main(){
    int N;

    scanf("%d", &N);
    quadrado(N);
    
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
  "source_sha256": "43b2e246d663a76be664a9ecc2c4463b17d8048c5108880a5e42c4051983c68a",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_034 — train

```c

#include <stdio.h>

void quadrado(int N);

int main(){

    int N;
    scanf("%d", &N);
    
    while (N < 2){
        scanf("%d", &N);
    }
    quadrado(N);
    return 0;
}

void quadrado(int N){

    int i, j, n = 0;

    for (i = 0; i < N; i++){
        for (j = n; j < (N + i); j++){
            printf("%d\t", j + 1);
        }
        n++;
        printf("\n");
    }
}

```

```json
{
  "sample_id": "sample_034",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "a8d34b88c089e6c965b5f5d98d3f57fcbf573aa07ae2ee386c9d2b289960b981",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
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


## sample_035 — validation

```c

#include <stdio.h>

int main()
{
    int numero;
    int colunas=0; 
    int linhas=0;
    int variavel=1;
    scanf("%d", &numero);

    while (linhas<numero)
    {
        while (colunas<numero)
        {
            printf("%d\t",variavel++);
            ++colunas;
        };
    variavel=variavel-numero+1;
    ++linhas;
    colunas=0;
    printf("\n");
    }
    printf("\n");
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
  "source_sha256": "47727c4367eed91a118ab8f66b278a2077168c2142b9eb162526939edddd4c57",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_036 — validation

```c

#include <stdio.h>

int main()
{
    int numero;
    int colunas=0; 
    int linhas=0;
    int variavel=1;
    scanf("%d", &numero);

    while (linhas<numero)
    {
        while (colunas<numero)
        {
            if (colunas+1==numero)
            {
                printf("%d",variavel++);
                ++colunas;
            }
            else
            {
                printf("%d\t",variavel++);
                ++colunas;
            }
        };
    variavel=variavel-numero+1;
    ++linhas;
    colunas=0;
    printf("\n");
    }
    printf("\n");
    return 0;
}





```

```json
{
  "sample_id": "sample_036",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "ded156f3c027b2ac9042b17b8402bb0f8a2ce144814e7136aee7e5a3cbb29029",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\n2\t3\t4\n3\t4\t5\n\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_037 — validation

```c

#include <stdio.h>

int main()
{
    int numero;
    int colunas=0; 
    int linhas=0;
    int variavel=1;
    scanf("%d", &numero);

    while (linhas<numero)
    {
        while (colunas<numero)
        {
            if (colunas+1==numero)
            {
                printf("%d",variavel++);
                ++colunas;
            }
            else
            {
                printf("%d\t",variavel++);
                ++colunas;
            }
        };
    variavel=variavel-numero+1;
    ++linhas;
    colunas=0;
    printf("\n");
    }
    printf("\n");
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
  "source_sha256": "ce82b10c00e5c5663c3f19f87d283cec59dedcbb56663ede2a31a65eb7f6a7e9",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\n2\t3\t4\n3\t4\t5\n\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_038 — validation

```c

#include <stdio.h>

int main()
{
    int numero;
    int colunas=0; 
    int linhas=0;
    int variavel=1;
    scanf("%d", &numero);

    while (linhas<numero)
    {
        while (colunas<numero)
        {
            printf("%d\t",variavel++);
            ++colunas;
        };
    variavel=variavel-numero+1;
    ++linhas;
    colunas=0;
    printf("\n");
    }
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
  "source_sha256": "3b99178b5fc365d2ad862960b432047020864b16ee31497c8cfe5e5dc915f47b",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_039 — train

```c


#include <stdio.h>

void quadrado(int N){
    int l, c;
    for (l = 0; l < N; l++){
        for (c = 0; c < N; c++)
        {
            printf("%d\t", l+c+1);
        }
        printf("\n");
    }    
    
}

int main()
{
    int N;
    scanf("%d", &N);

    if (N >= 2)
    {
        quadrado(N);
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
  "source_sha256": "a913a34126843b5526a8bdc51dd012ce1ed5cbba44c39e7067330dbc7ff3cd14",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_040 — train

```c


#include <stdio.h>

int main(void) {

    int i, num, j;
    scanf("%d", &num);

    for(j = 0; j < num; j++) {
        for(i = 0; i < num; i++)
            printf("%d\t", j + i + 1);
        i = 0;
        printf("\n");
    } 
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
  "source_sha256": "3cdd375d7c33dd49e82ae6d258e084df6577193d2e16469ce73708bbed8341d9",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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

void quadrado(int N) {

    int i, j;

    for(j = 0; j < N; j++) {
        for(i = 0; i < N; i++)
            printf("%d\t", j + i + 1);
        i = 0;
        printf("\n");
    } 
}


int main() {
    int N;
    scanf("%d", &N);
    quadrado(N);
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
  "source_sha256": "cb0b2635e40f15ddeb565b445cf051ce39ac80768d5f800cda6c6c181124146b",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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

int main(void) {

    int i, num, j;
    scanf("%d", &num);

    for(j = 0; j < num; j++) {
        for(i = 0; i < num; i++)
            printf("%d\t", j + i + 1);
        i = 0;
        printf("\n");
    } 
    printf("\n");
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
  "source_sha256": "ba3b435024526bf97b9830c006128b4e56224d1039442caf2963c69f11d4f818",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_043 — validation

```c


#include <stdio.h>

int main()
{
    int s , linha, colona, conta1 = 1, conta2 = 1;
    scanf("%d",&s);

    linha = s;
    colona = s;

    while (conta1 <= colona)
    {
        while (conta2 <= linha)
        {
            printf("%d\t",conta2);
            conta2 ++;
        }
        printf("\n");
        conta1 ++;
        linha ++;
        conta2 = conta1;
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_043",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "99eaea82840eef783705a3c9ef861e577e6a050aed5da569195a7aaf39a3b960",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_044 — train

```c

#include <stdio.h>



void quadrado(int n)
{
    int i, j;
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("%d\t", i+j+1);
        }
        printf("\n");
    }
    return;
}

int main()
{
    int n;
    scanf("%d", &n);
    while (n < 2)
        scanf("%d", &n);
    quadrado(n);
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
  "source_sha256": "6b108af07a210bc36da50b650fd31153092ef501c0ce5d469959470f8567d640",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
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


## sample_045 — train

```c

#include <stdio.h>


void quadrado(int n){
    int i, j;

    for(i = 1; i <= n; i++){
        printf("\n");
        for(j = i; j < n + i; j++)
            printf("%d\t", j);
    }
}

int main(){
    
    int n;

    scanf("%d", &n);
    quadrado(n);

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
  "source_sha256": "8543672faead8a5a3f0ac085f9a25ec36491db6deea90049a601aff980925590",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "\n1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "\n1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "\n1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


void quadrado(int n){
    int i, j;

    for(i = 1; i <= n; i++){
        printf("\n");
        for(j = i; j < n + i; j++)
            printf("%d\t", j);
    }
}

int main(){
    
    int n;

    scanf("%d", &n);
    quadrado(n);
    printf("\n");

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
  "source_sha256": "599f64ec770f0ce138f084847b519ffbf6e8efe7959b1bba1e664751bb92ba50",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "\n1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "\n1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "\n1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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

void quadrado(int n){
    int i, j;

    for(i = 1; i <= n; i++){
        printf("\n");
        for(j = i; j < n + i; j++)
            printf("%d\t", j);
    }
}

int main(){
    
    int n;

    scanf("%d", &n);
    quadrado(n);

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
  "source_sha256": "757cf9b31e91bc28c648552376462779b7dc4cc78a27d4e98e7f80cbaee30cc1",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "\n1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "\n1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "\n1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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

void quadrado(int N) {

    int i, j, v = 1; 

    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            printf("%d\t", v);
            v++;
        }
        v -= (N - 1);
        printf("\n");
    }
}

int main () {
    
    int N;

    do {
        scanf("%d", &N);
    } while (N < 2);

    quadrado(N);
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
  "source_sha256": "68cc288a1e02737d0a79114e3222c3ba195b3cc0801a00faba6fd3324560e003",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "1",
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


## sample_049 — train

```c


#include <stdio.h>

void quadrado(int N){
    int i, j;

    for(i=0 ; i < N ; i++){        
        for( j=1 ; j <= N ; j++){     
            printf("%d\t", j+i);   
        }
        printf("\n");                
    }
}

int main(){
    int N;
    scanf("%d",&N);

    if (N >= 2)
        quadrado (N);
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
  "source_sha256": "0a0ea3739991a5390d2677084cc4693b42e1e46990e34ab0e4ffe54981048cb9",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_050 — train

```c


#include <stdio.h>


void quadrado(int n);


int main() {
    int n;
    
    scanf("%d", &n);
    quadrado(n);
    
    return 0;
}

void quadrado( int n) {
    int i, j;
    
    for ( i = 1; i <= n; i++)
    {
        for (j = i; j < n+i; j++)
        {
            printf("%d\t", j);
        }
        printf("\n");
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
  "source_sha256": "6a8fbd815b7bf1df4da81fad2d91e78c9a8df06e9acb3885a70e71919bce8d18",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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
int main() {
    int n,i,j;
    
    scanf("%d", &n);

    ;
    
    for ( i = 1; i <= n; i++)
    {
        for (j = i; j < n + i; j++)
        {
            printf("%d\t", j);
        }
        printf("\n");
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
  "source_sha256": "f0297d1d7a49bf04a50088dd72a848a9b4fa66efd7ec76c11512f7badc9cd711",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


void quadrado(int n);


int main() {
    int n;
    
    scanf("%d", &n);
    
    quadrado(n);
    
    return 0;
}

void quadrado( int n) {
    int i,j;
    
    for ( i = 1; i <= n; i++)
    {
        for (j = i; j < n + i; j++)
        {
            printf("%d", j);
            if (j < n + i)
            {
                printf("\t");
            }
            
        }
        if (i < n)
        {
                printf("\n");
        }
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
  "source_sha256": "fc6f2f9ecc184b09310abe8a6999f1275965d5bbd90c69196c1bc1a869001670",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_053 — train

```c


#include <stdio.h>
int main() {
    int n, i, j;
    
    scanf("%d", &n);

    ;
    
    for ( i = 1; i <= n; i++)
    {
        for (j = i; j < n + i; j++)
        {
            printf("%d\t", j);
        }
        printf("\n");
    }

    return 0;
}
```

```json
{
  "sample_id": "sample_053",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "5e6d9adfadb47d410072e2ea6880eac09e0122bd8e5532cc6781e719a2d9666e",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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
#include <string.h>


void quadrado(int n);


int main() {
    int n;
    
    scanf("%d", &n);
    quadrado(n);
    
    return 0;
}

void quadrado( int n) {
    int i, j;
    char line[60]= "";
    char aux[10];
    
    for ( i = 1; i <= n; i++)
    {
        for (j = i; j < n + i; j++)
        {
            sprintf(aux, "%d\t",j);
            strcat(line,aux);
            
        }
        printf("%s\n", line);
        memset(line, 0, sizeof(line));
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
  "source_sha256": "928bc96fd3a068daa0caf1b8f97013685ae40464ff610ca2983af66a119f27cf",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


void quadrado(int n);


int main() {
    int n;
    
    scanf("%d", &n);
    quadrado(n);
    
    return 0;
}

void quadrado( int n) {
    int i,j;
    
    for ( i = 1; i <= n; i++)
    {
        for (j = i; j < n + i; j++)
        {
            printf("%d\t", j);
        }
        printf("\n");
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
  "source_sha256": "3cb906ea15278a6c77a6e616ad082b0c0f0d350f82b97ab57e95a9e38f3a6d10",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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

void quadrado(int N) {
    int i, j=0;

    while (j < N){
        for (i = 1; i <= N; ++i) {
        printf("%d\t", i+j);
        }
        printf("\n");
        j++;
    }
}

int main() {
    int N;

    scanf("%d", &N);

    if (N >= 2) {
        quadrado(N);
    }

    return 0;
}
```

```json
{
  "sample_id": "sample_056",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "a889a0d95db458c4d0a0a232805536c95975eef593b4a92f0a99a33febcb03c2",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_057 — train

```c
#include <stdio.h>

void quadrado(int n) {
    int i, j;
    for (i = 1; i <= n; i++) {
        for (j = i; j < i + n; j++) {
            printf("%d\t", j);
        }
        printf("\n");
    }
}

int main() {
    int n;
    scanf("%d", &n);
    quadrado(n);
    return 0;
}

```

```json
{
  "sample_id": "sample_057",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "c4763b0cf13c8597e139878d132c79162e47f66fe5b49821716499c763368e7c",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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

void quadrado(int n) {

    int i, j;

    for (i=1; i<=n; i++) {
        for (j=i; j<(n+i); j++) {
            printf("%d\t",j);
        }
        printf("\n");
    }
}

int main() {
    
    int n;

    scanf("%d",&n);
    quadrado(n);
    
    return 0;
}

```

```json
{
  "sample_id": "sample_058",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "c217bad3aae44f6feb48bd9ffbd3b2226b143bb2be537f9b64ffe2fba4e2a5e4",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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
void quadrado(int numero)
{
    int limite = numero, contador = 1, i;
    while (contador <= limite){
        for (i = contador; i < contador + numero; i++){
            printf("%d\t", i);
        }
        printf("\n");
        contador++;
    }
    
}
int main()
{
    int numero;
    scanf("%d", &numero);
    quadrado(numero);
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
  "source_sha256": "4b44762341f262ec71f3df2afd92ddb9102708ff6c78effce0a5113f7b3f1a89",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_060 — train

```c


#include <stdio.h>


int main(){

    int N;
    void quadrado();

    scanf("%d", &N);
    quadrado(N);

    return 0;
}

void quadrado(int N){

    int i,j, Novo_N;

    Novo_N = N;
    for(i = 1; i <= N; i++){
        for( j = i; j<= Novo_N; j++){
            printf("%d\t", j);
        }
        printf("\n");
        Novo_N++;
    }
    
}
```

```json
{
  "sample_id": "sample_060",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "8f7134c93b6c77e9f55d80d3185be95d67634289f6e9378878753a845fef136c",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_061 — train

```c

#include <stdio.h>

void quadrado(int num) {
    int linha, col;
    for (linha = 1; linha <= num; linha++) {
        for (col = linha; col <= (num + linha - 1); col++) {
            printf("%d\t", col);
        }
        printf("\n");
    }
}

int main() {
    int num;
    scanf("%d", &num);
    quadrado(num);

    return 0;
}
```

```json
{
  "sample_id": "sample_061",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "c60373611d4988c8a902eaa80f4de5c88ff56a3c54ac3b07cb4fe7703161106a",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_062 — validation

```c

#include <stdio.h>

void quadrado(int N);

int main () {
    int N;
    scanf("%d", &N);
    quadrado(N);
    return 0;
}

void quadrado(int N) {
    int i0, j0, j1;
    for (i0 = 1; i0 <= N; i0++) {
        j1 = i0;
        for (j0 = 0; j0 < N; j0++) {
            
            printf("%d\t", j1);
            j1++;
        }
        printf("\n");
    }
    return;
}
```

```json
{
  "sample_id": "sample_062",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "18a42d0858d0a1a53d31cd8324934724840d63517d4fed26d2a8493a7239b1ee",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_063 — train

```c

#include <stdio.h>

void quadrado(int N){
    int i,n;
    int N_copy = N;
    int n_copy=1;
    for (i = 0; i< N; i++){
        for(n = n_copy;n<=N_copy;n++){
            printf("%d\t", n);
        }
        N_copy++;
        n_copy++;
        printf("\n");    
    }
   
    
}

int main(){
    int N;
    scanf("%d",&N);
    printf("\n");
    while (N< 2) {
        printf("Invalid number try again :\n");
        scanf("%d",&N);}
    quadrado(N);
    return 0;
}

```

```json
{
  "sample_id": "sample_063",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "e7a0a1d912f7cd7a4098e1ed65ba74ffd290fdb66f9179f28c0c90746d5c511b",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "\n1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "\n1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "\n1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_064 — train

```c

#include <stdio.h>

void quadrado(int N){
    int linha, coluna;
    for (linha = 0; linha < N; linha++){
        for (coluna = linha + 1; coluna <= (N + linha); coluna++){
            printf("%d\t", coluna);
        }
        printf("\n");
    }
}

int main(){
    int N;

    scanf("%d", &N);

    quadrado(N);

    return 0;
}
```

```json
{
  "sample_id": "sample_064",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "5cc4e2c92301ef5f250a7807e1323943914d10958547534587586d5954941e3f",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_065 — train

```c

#include <stdio.h>

void quadrado(int N){
    int linha, coluna;
    if (N < 2){
        printf("Digite um número maior que 2\n");
        return;
    }
    for (linha = 0; linha < N; linha++){
        for (coluna = linha + 1; coluna <= (N + linha); coluna++){
            printf("%d\t", coluna);
        }
        printf("\n");
    }
}

int main(){
    int N;

    scanf("%d", &N);

    quadrado(N);

    return 0;
}
```

```json
{
  "sample_id": "sample_065",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "e021ac974853bab89b59265eacc0b5ba108327cd29b91cc553d9d1c8cd9c5cc0",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_066 — train

```c

#include <stdio.h>

void quadrado(int N) {
  int i, j;

  for(i = 1; i <= N; i++) {
    for(j = i; j < (N+i); j++) {
      printf("%d\t", j);
    }
    printf("\n");
  }
}

int main() {
  int N;

  scanf("%d", &N);
  quadrado(N);
  
  return 0;
}
```

```json
{
  "sample_id": "sample_066",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "7298f797d4338484834bc8d5a519cdfb8d890b98000d766f6a83ea14c5e19a72",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_067 — train

```c

#include <stdio.h>

void quadrado(int N){
    int i,j;
    for(i=0;i<N;i++){
        for(j=0;j<N;j++){
            printf("%d\t",i+j+1);
        }
        printf("\n");
    }
}

int main(){
    int N;
    scanf("%d",&N);
    if (N<2)
        return 1;
    quadrado(N);
    return 0;
}
```

```json
{
  "sample_id": "sample_067",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "58733df7f93a0845c981d5473ee291e3a6578b846484dd6dcf397be77b02a865",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_068 — train

```c

#include <stdio.h>

void quadrado(int N) {
    int i, j, N_inc = N;
    for (i = 1; i <= N; i++) {
        if (i >= 2) {
            N_inc++;
            printf("\n");
        }
        for (j = i; j <= N_inc; j++) {
            printf("%d\t", j);
        }
    }
    printf("\n");
}

int main() {
    int N;
    scanf("%d", &N);
    if (N >= 2) {
        quadrado(N);
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_068",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "b8fcb6d7ea661220cd1bfcd8469982443e9b56b26b53fa05a7c17449011eeb44",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_069 — train

```c

#include <stdio.h>

void quadrado(int N) {
    int i, j, N_inc = N;
    for (i = 1; i <= N; i++) {
        if (i >= 2) {
            N_inc++;
            printf("\n");
        }
        for (j = i; j <= N_inc; j++) {
            printf("%d\t", j);
        }
    }
}

int main() {
    int N;
    scanf("%d", &N);
    if (N >= 2) {
        quadrado(N);
        printf("\n");
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_069",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "5db64c03724c1a677cc736f5f2db12c3a02d015a8960daa04c6a57f317591735",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_070 — train

```c

#include <stdio.h>

void quadrado(int N) {
    int i, j, N_inc = N;
    for (i = 1; i <= N; i++) {
        if (i >= 2) {
            N_inc++;
            printf("\n");
        }
        for (j = i; j <= N_inc; j++) {
            printf("%d\t", j);
        }
    }
}

int main() {
    int N;
    scanf("%d", &N);
    if (N >= 2) {
        quadrado(N);
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_070",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "0dd05e6cf5260dc1c69ebb46b21f5b2db2bd9a0ee2961a31684bb5b38e9cf23c",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_071 — train

```c

#include <stdio.h>

void quadrado(int length){
    int first_value_line,to_sum;

    for (first_value_line = 1; first_value_line <= length; first_value_line++)
    {
        for(to_sum = 0; to_sum < length; to_sum++)
            printf("%d\t",first_value_line + to_sum);

        printf("\n");
    }
}

int main(){
    int length;
    scanf("%d",&length);
    quadrado(length);
    return 0;
}
```

```json
{
  "sample_id": "sample_071",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "4305039ec7cb1407bf443a82b315d01d061c0cd712ce9f7f26ec7c26384e52c7",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_072 — train

```c

#include <stdio.h>

void quadrado(int N)
{
    int linha, i;

    for (linha = 0; linha < N; linha++)
    {
        for (i = 1; i <= N; i++)
        {
            printf("%d\t", (i + linha));
        } 
        printf("\n");
    }
}

int main()
{
    int n;

    scanf("%d", &n);
    quadrado(n);
    return 0;
}
```

```json
{
  "sample_id": "sample_072",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "0ae7ca65b8c70d607de71bf7cfc14fb2e486cc0b72a1cd12ad87f51c6edc1cf7",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_073 — train

```c

#include <stdio.h>

void quadrado(int N){
    int i, j, k = 1;
    for(i=1; i<=N; i++){
        for(j=k; j<(N+k); j++){
            printf("%d\t", j);
        }
        printf("\n");
        k++;
    }
}

int main(){
    int N;
    scanf("%d", &N);
    while(N < 2){
        scanf("%d", &N);
    }
    quadrado(N);
    return 0;
}


```

```json
{
  "sample_id": "sample_073",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "a3b98bae7f630dd0cd97aa24b1c1f98e9c3f5102bfaeefe89bef25bf329fd2d2",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_074 — train

```c

#include <stdio.h>

void quadrado(int N){

    int cont, looper;
    cont = 1;
    while (cont <= N){
        for (looper=cont; looper < N+cont; looper++){
            printf("%d\t", looper);
        }
        printf("\n");
        cont++;
    }

}

int main(){
    int N;
    N = 0;
    while (N<2){
        scanf("%d", &N);
    }
    quadrado(N);
    return 0;
}

```

```json
{
  "sample_id": "sample_074",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "b98ed6ab243a3e8b0cbd313497959fb67a3502ed1ab267c1a73ec3ba3d1ba296",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_075 — train

```c

#include <stdio.h>

void quadrado(int N){

    int cont, looper;
    cont = 1;
    while (cont <= N){
        for (looper=cont; looper < N+cont; looper++){
            if (looper != N+cont){
                printf("%d\t", looper);
            }
            else{
                printf("%d", looper);
            }
        }
        printf("\n");
        cont++;
    }

}

int main(){
    int N;
    N = 0;
    while (N<2){
        scanf("%d", &N);
    }
    quadrado(N);
    return 0;
}

```

```json
{
  "sample_id": "sample_075",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "19cbda6949e3abbfda9ef207e391ccdb8faef79379c5a45c905af0f91b725397",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_076 — train

```c
#include <stdio.h>

void quadrado(int N){

    int i, j;

    for (i=0; i < N; i++){
        for (j=0; j < N; j++){
            printf("%d\t", i + j + 1);
            if (j == N - 1){
                printf("\n");
            }
        }
    }
}

int main(){

    int N;
    scanf("%d", &N);

    quadrado(N);
    
    return 0;
}
```

```json
{
  "sample_id": "sample_076",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "c515f7c6aaa2bf6bd2fd8f282fcaa77e845a151940771067177703cae910abb0",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_077 — validation

```c

#include <stdio.h>

int main(){

    int i, j, N;

    scanf("%d", &N);

    for(i = 0; i < N; i++){
        for (j = 1; j <= N; j++){
            printf("%d\t", i + j);
        }
        printf("\n");
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_077",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "53417df933874d99b0ca12061fe42b6aa1c7b692247ce57850b4f9edaeddba4e",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_078 — train

```c


#include <stdio.h>

void quadrado(int N) {
    int n2, starter = 1, starter2 = 1, n3;
    n2 = N;
    n3 = N;
    if (N >= 2) {
        while (N > 0) {
            starter = starter2;
            while (n2 > 0) {
                printf("%d\t", starter);
                starter ++;
                n2--;
            }
            printf("\n");
            starter2 ++;
            N--;
            n2 = n3;
        }
    }
}

int main () {
    int N;
    scanf("%d", &N);
    quadrado(N);
    return 0;
}


```

```json
{
  "sample_id": "sample_078",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "38c425a2dafca3a88d2b323e95089709ee358d6755e0e19a71b70003ca7e4ee8",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_079 — train

```c

#include <stdio.h>

void quadrado(int N){
    int i, j;
    if (N >= 2){
        for (i = 1; i <= N; i++){
            for (j = i; j < N + i; j++){
                printf("%d\t", j);
            }
            printf("\n");
        }
    }
}

int main(){
    int N;
    scanf("%d", &N);
    quadrado(N);
    return 0;
}
```

```json
{
  "sample_id": "sample_079",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "5669fecf95b430c53e941319310213d74e2a90c2e80aff10315b88d797f59322",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_080 — train

```c

#include <stdio.h>
void quadrado(int N){
    int i, j;
    if (N >= 2){
        for (i = 1; i <= N; i++){
            for (j = i; j < N + i; j++){
                printf("%d\t", j);
            }
            printf("\n");
        }
    }
}

int main(){
    int N;
    scanf("%d", &N);
    quadrado(N);
    return 0;
}
```

```json
{
  "sample_id": "sample_080",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "3c2b6434f44aa171dba5f6d854603044d6e874dbeedaa5cd449444d43d2a9418",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_081 — train

```c

#include <stdio.h>

void quadrado(int N){
    int i, j;
    if (N >= 2){
        for (i = 1; i <= N; i++){
            for (j = i; j < N + i; j++){
                printf("%d\t", j);
            }
            printf("\n");
        }
    }
}

int main(){
    int N;
    scanf("%d", &N);
    quadrado(N);
    return 0;
}
```

```json
{
  "sample_id": "sample_081",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "5669fecf95b430c53e941319310213d74e2a90c2e80aff10315b88d797f59322",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_082 — train

```c

#include <stdio.h>
void quadrado(int N){
    int i, j;
    if (N >= 2){
        for (i = 1; i <= N; i++){
            for (j = i; j < N + i; j++){
                printf("%d\t", j);
            }
            printf("\n");
        }
    }
}

int main(){
    int N;
    scanf("%d", &N);
    quadrado(N);
    return 0;
}
```

```json
{
  "sample_id": "sample_082",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "3c2b6434f44aa171dba5f6d854603044d6e874dbeedaa5cd449444d43d2a9418",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_083 — train

```c

#include <stdio.h>
void quadrado(int N){
    int i, j;
    if (N >= 2){
        for (i = 1; i <= N; i++){
            for (j = i; j < N + i; j++){
                printf("%d\t", j);
            }
            printf("\n");
        }
    }
}

int main(){
    int N;
    scanf("%d", &N);
    quadrado(N);
    return 0;
}
```

```json
{
  "sample_id": "sample_083",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "3c2b6434f44aa171dba5f6d854603044d6e874dbeedaa5cd449444d43d2a9418",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_084 — train

```c

#include <stdio.h>
void quadrado(int N) {
    int i, l;    

    for(l = 1; l <= N; l++) {
        for(i = l; i < N + l; i++) {
            printf("%d\t", i);
        }
        printf("\n");
    }
}

int main() {
    int N;
    
    scanf("%d", &N);
    
    if (N >= 2) {
        quadrado(N);
    }
    
    return 0;
}
```

```json
{
  "sample_id": "sample_084",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "cc4569063620fbef2b9c0dc2702707a7c8ee329857f0c66f9ff275c41ff62a0a",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_085 — validation

```c


#include <stdio.h>

void quadrado(int n) {
    int i, a;

    if (n <= 1) return;
    for (i= 1; i <= n; i++) {
        for (a = i; a < n + i; a++) {
            printf("%d\t", a);
        }
        printf("\n");
    }
}

int main() {
    int n;
    
    scanf("%d", &n);
    quadrado(n);
    return 0;
}

```

```json
{
  "sample_id": "sample_085",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "13998caef026bcc61bc6d77c1fb272c2ddf65404cace9b100d8c7abeba7a39ca",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_086 — validation

```c


#include <stdio.h>

void quadrado(int n) {
    int i, a;

    if (n <= 1) return;
    for (i= 1; i <= n; i++) {
        for (a = i; a < n + i; a++) {
            printf("%d\t", a);
        }
        printf("\n");
    }
}

int main() {
    int n;
    
    scanf("%d", &n);
    quadrado(n);
    return 0;
}
```

```json
{
  "sample_id": "sample_086",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "d0eafc16c018a465ab6565891cd1c28042dbac1309698c5f45839c9aa6f81619",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_087 — train

```c

#include <stdio.h>

void quadrado(int N){
  int i, j;
  for(i = 0; i < N; i++){
    for(j = 1; j <= N; j++){
        printf("%d\t", j+i);
      }
    printf("\n");
    }
}


int main(){
    int N;
    scanf("%d", &N);

    quadrado(N);
    return 0;
}

```

```json
{
  "sample_id": "sample_087",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "fa616c4202ac89aa7f3edd5541781b80f762f93d12ff8727842efd04117d7ebb",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_088 — train

```c


#include <stdio.h>

int main() {
    int N,linha,col;
    scanf("%d",&N);

    for (linha = 0; linha < N; ++linha) {
        for (col = 1; col <= N; ++col) {
            printf("%d\t",linha + col);
        }
        printf("\n");
    }

    return 0;
}
```

```json
{
  "sample_id": "sample_088",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "43d41dc642d075c198c7ddeae437768f3b924bef48d7dd07d91ed31489b1be42",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_089 — train

```c

#include <stdio.h>

void quadrado(int n){
    int i, j;
    for(i=0;i<n;i++){
        for(j=1;j<=n;j++){
            printf("%d\t",j+i);
        }
        printf("\n");
    }
}

int main(){
    int n;
    scanf("%d",&n);
    quadrado(n);

    return 0;
}
```

```json
{
  "sample_id": "sample_089",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "0ba9f976c6e5025477e18ad3451a26bc247e1f2cf7b008d34ddcd78de22caae1",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_090 — train

```c

#include <stdio.h>

void quadrado(int N) {
    int i,j,v;
    for (i=1;i<=N;i++) {
        v=i;
        for (j=0;j<N;j++) {
            printf("%d\t",v);
            v++;
        }
        printf("\n");
    }
}

int main() {
    int N;
    scanf("%d",&N);
    quadrado(N);
    return 0;
}


```

```json
{
  "sample_id": "sample_090",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "30d2ba5220c50e068e156f92445c7f719cc7958190fe11be545f193cc9c31f27",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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


## sample_091 — validation

```c


#include<stdio.h>
void quadrado (int N){

    int i, j;

    for (i = 1; i <= N; i++) {
        for (j = 0; j <= N - 1; j++) { 
            printf("%d\t", i + j);
        }

        printf("\n");
    }
}

int main() {
    int n;
    scanf("%d", &n);
    if (n < 2) {
        printf("Erro: O valor de N deve ser maior ou igual a 2.\n");
    } else {
        quadrado(n);
    }

    return 0;
}
```

```json
{
  "sample_id": "sample_091",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "7dc5ed2da9fce0d5ef4f8a2dffdc4c03a8575270cda535d80a4009a058da479b",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "3",
      "expected": "1\t2\t3\n2\t3\t4\n3\t4\t5\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "whitespace",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "small"
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
  "members/sample_012/tests/ex01_2",
  "members/sample_013/raw_code",
  "members/sample_013/tests/ex01_0",
  "members/sample_013/tests/ex01_1",
  "members/sample_013/tests/ex01_2",
  "members/sample_014/raw_code",
  "members/sample_014/tests/ex01_0",
  "members/sample_014/tests/ex01_1",
  "members/sample_014/tests/ex01_2",
  "members/sample_015/raw_code",
  "members/sample_015/tests/ex01_0",
  "members/sample_015/tests/ex01_1",
  "members/sample_015/tests/ex01_2",
  "members/sample_016/raw_code",
  "members/sample_016/tests/ex01_0",
  "members/sample_016/tests/ex01_1",
  "members/sample_016/tests/ex01_2",
  "members/sample_017/raw_code",
  "members/sample_017/tests/ex01_0",
  "members/sample_017/tests/ex01_1",
  "members/sample_017/tests/ex01_2",
  "members/sample_018/raw_code",
  "members/sample_018/tests/ex01_0",
  "members/sample_018/tests/ex01_1",
  "members/sample_018/tests/ex01_2",
  "members/sample_019/raw_code",
  "members/sample_019/tests/ex01_0",
  "members/sample_019/tests/ex01_1",
  "members/sample_019/tests/ex01_2",
  "members/sample_020/raw_code",
  "members/sample_020/tests/ex01_0",
  "members/sample_020/tests/ex01_1",
  "members/sample_020/tests/ex01_2",
  "members/sample_021/raw_code",
  "members/sample_021/tests/ex01_0",
  "members/sample_021/tests/ex01_1",
  "members/sample_021/tests/ex01_2",
  "members/sample_022/raw_code",
  "members/sample_022/tests/ex01_0",
  "members/sample_022/tests/ex01_1",
  "members/sample_022/tests/ex01_2",
  "members/sample_023/raw_code",
  "members/sample_023/tests/ex01_0",
  "members/sample_023/tests/ex01_1",
  "members/sample_023/tests/ex01_2",
  "members/sample_024/raw_code",
  "members/sample_024/tests/ex01_0",
  "members/sample_024/tests/ex01_1",
  "members/sample_024/tests/ex01_2",
  "members/sample_025/raw_code",
  "members/sample_025/tests/ex01_0",
  "members/sample_025/tests/ex01_1",
  "members/sample_025/tests/ex01_2",
  "members/sample_026/raw_code",
  "members/sample_026/tests/ex01_0",
  "members/sample_026/tests/ex01_1",
  "members/sample_026/tests/ex01_2",
  "members/sample_027/raw_code",
  "members/sample_027/tests/ex01_0",
  "members/sample_027/tests/ex01_1",
  "members/sample_027/tests/ex01_2",
  "members/sample_028/raw_code",
  "members/sample_028/tests/ex01_0",
  "members/sample_028/tests/ex01_1",
  "members/sample_028/tests/ex01_2",
  "members/sample_029/raw_code",
  "members/sample_029/tests/ex01_0",
  "members/sample_029/tests/ex01_1",
  "members/sample_029/tests/ex01_2",
  "members/sample_030/raw_code",
  "members/sample_030/tests/ex01_0",
  "members/sample_030/tests/ex01_1",
  "members/sample_030/tests/ex01_2",
  "members/sample_031/raw_code",
  "members/sample_031/tests/ex01_0",
  "members/sample_031/tests/ex01_1",
  "members/sample_031/tests/ex01_2",
  "members/sample_032/raw_code",
  "members/sample_032/tests/ex01_0",
  "members/sample_032/tests/ex01_1",
  "members/sample_032/tests/ex01_2",
  "members/sample_033/raw_code",
  "members/sample_033/tests/ex01_0",
  "members/sample_033/tests/ex01_1",
  "members/sample_033/tests/ex01_2",
  "members/sample_034/raw_code",
  "members/sample_034/tests/ex01_0",
  "members/sample_034/tests/ex01_1",
  "members/sample_034/tests/ex01_2",
  "members/sample_035/raw_code",
  "members/sample_035/tests/ex01_0",
  "members/sample_035/tests/ex01_1",
  "members/sample_035/tests/ex01_2",
  "members/sample_036/raw_code",
  "members/sample_036/tests/ex01_0",
  "members/sample_036/tests/ex01_1",
  "members/sample_036/tests/ex01_2",
  "members/sample_037/raw_code",
  "members/sample_037/tests/ex01_0",
  "members/sample_037/tests/ex01_1",
  "members/sample_037/tests/ex01_2",
  "members/sample_038/raw_code",
  "members/sample_038/tests/ex01_0",
  "members/sample_038/tests/ex01_1",
  "members/sample_038/tests/ex01_2",
  "members/sample_039/raw_code",
  "members/sample_039/tests/ex01_0",
  "members/sample_039/tests/ex01_1",
  "members/sample_039/tests/ex01_2",
  "members/sample_040/raw_code",
  "members/sample_040/tests/ex01_0",
  "members/sample_040/tests/ex01_1",
  "members/sample_040/tests/ex01_2",
  "members/sample_041/raw_code",
  "members/sample_041/tests/ex01_0",
  "members/sample_041/tests/ex01_1",
  "members/sample_041/tests/ex01_2",
  "members/sample_042/raw_code",
  "members/sample_042/tests/ex01_0",
  "members/sample_042/tests/ex01_1",
  "members/sample_042/tests/ex01_2",
  "members/sample_043/raw_code",
  "members/sample_043/tests/ex01_0",
  "members/sample_043/tests/ex01_1",
  "members/sample_043/tests/ex01_2",
  "members/sample_044/raw_code",
  "members/sample_044/tests/ex01_0",
  "members/sample_044/tests/ex01_1",
  "members/sample_044/tests/ex01_2",
  "members/sample_045/raw_code",
  "members/sample_045/tests/ex01_0",
  "members/sample_045/tests/ex01_1",
  "members/sample_045/tests/ex01_2",
  "members/sample_046/raw_code",
  "members/sample_046/tests/ex01_0",
  "members/sample_046/tests/ex01_1",
  "members/sample_046/tests/ex01_2",
  "members/sample_047/raw_code",
  "members/sample_047/tests/ex01_0",
  "members/sample_047/tests/ex01_1",
  "members/sample_047/tests/ex01_2",
  "members/sample_048/raw_code",
  "members/sample_048/tests/ex01_0",
  "members/sample_048/tests/ex01_1",
  "members/sample_048/tests/ex01_2",
  "members/sample_049/raw_code",
  "members/sample_049/tests/ex01_0",
  "members/sample_049/tests/ex01_1",
  "members/sample_049/tests/ex01_2",
  "members/sample_050/raw_code",
  "members/sample_050/tests/ex01_0",
  "members/sample_050/tests/ex01_1",
  "members/sample_050/tests/ex01_2",
  "members/sample_051/raw_code",
  "members/sample_051/tests/ex01_0",
  "members/sample_051/tests/ex01_1",
  "members/sample_051/tests/ex01_2",
  "members/sample_052/raw_code",
  "members/sample_052/tests/ex01_0",
  "members/sample_052/tests/ex01_1",
  "members/sample_052/tests/ex01_2",
  "members/sample_053/raw_code",
  "members/sample_053/tests/ex01_0",
  "members/sample_053/tests/ex01_1",
  "members/sample_053/tests/ex01_2",
  "members/sample_054/raw_code",
  "members/sample_054/tests/ex01_0",
  "members/sample_054/tests/ex01_1",
  "members/sample_054/tests/ex01_2",
  "members/sample_055/raw_code",
  "members/sample_055/tests/ex01_0",
  "members/sample_055/tests/ex01_1",
  "members/sample_055/tests/ex01_2",
  "members/sample_056/raw_code",
  "members/sample_056/tests/ex01_0",
  "members/sample_056/tests/ex01_1",
  "members/sample_056/tests/ex01_2",
  "members/sample_057/raw_code",
  "members/sample_057/tests/ex01_0",
  "members/sample_057/tests/ex01_1",
  "members/sample_057/tests/ex01_2",
  "members/sample_058/raw_code",
  "members/sample_058/tests/ex01_0",
  "members/sample_058/tests/ex01_1",
  "members/sample_058/tests/ex01_2",
  "members/sample_059/raw_code",
  "members/sample_059/tests/ex01_0",
  "members/sample_059/tests/ex01_1",
  "members/sample_059/tests/ex01_2",
  "members/sample_060/raw_code",
  "members/sample_060/tests/ex01_0",
  "members/sample_060/tests/ex01_1",
  "members/sample_060/tests/ex01_2",
  "members/sample_061/raw_code",
  "members/sample_061/tests/ex01_0",
  "members/sample_061/tests/ex01_1",
  "members/sample_061/tests/ex01_2",
  "members/sample_062/raw_code",
  "members/sample_062/tests/ex01_0",
  "members/sample_062/tests/ex01_1",
  "members/sample_062/tests/ex01_2",
  "members/sample_063/raw_code",
  "members/sample_063/tests/ex01_0",
  "members/sample_063/tests/ex01_1",
  "members/sample_063/tests/ex01_2",
  "members/sample_064/raw_code",
  "members/sample_064/tests/ex01_0",
  "members/sample_064/tests/ex01_1",
  "members/sample_064/tests/ex01_2",
  "members/sample_065/raw_code",
  "members/sample_065/tests/ex01_0",
  "members/sample_065/tests/ex01_1",
  "members/sample_065/tests/ex01_2",
  "members/sample_066/raw_code",
  "members/sample_066/tests/ex01_0",
  "members/sample_066/tests/ex01_1",
  "members/sample_066/tests/ex01_2",
  "members/sample_067/raw_code",
  "members/sample_067/tests/ex01_0",
  "members/sample_067/tests/ex01_1",
  "members/sample_067/tests/ex01_2",
  "members/sample_068/raw_code",
  "members/sample_068/tests/ex01_0",
  "members/sample_068/tests/ex01_1",
  "members/sample_068/tests/ex01_2",
  "members/sample_069/raw_code",
  "members/sample_069/tests/ex01_0",
  "members/sample_069/tests/ex01_1",
  "members/sample_069/tests/ex01_2",
  "members/sample_070/raw_code",
  "members/sample_070/tests/ex01_0",
  "members/sample_070/tests/ex01_1",
  "members/sample_070/tests/ex01_2",
  "members/sample_071/raw_code",
  "members/sample_071/tests/ex01_0",
  "members/sample_071/tests/ex01_1",
  "members/sample_071/tests/ex01_2",
  "members/sample_072/raw_code",
  "members/sample_072/tests/ex01_0",
  "members/sample_072/tests/ex01_1",
  "members/sample_072/tests/ex01_2",
  "members/sample_073/raw_code",
  "members/sample_073/tests/ex01_0",
  "members/sample_073/tests/ex01_1",
  "members/sample_073/tests/ex01_2",
  "members/sample_074/raw_code",
  "members/sample_074/tests/ex01_0",
  "members/sample_074/tests/ex01_1",
  "members/sample_074/tests/ex01_2",
  "members/sample_075/raw_code",
  "members/sample_075/tests/ex01_0",
  "members/sample_075/tests/ex01_1",
  "members/sample_075/tests/ex01_2",
  "members/sample_076/raw_code",
  "members/sample_076/tests/ex01_0",
  "members/sample_076/tests/ex01_1",
  "members/sample_076/tests/ex01_2",
  "members/sample_077/raw_code",
  "members/sample_077/tests/ex01_0",
  "members/sample_077/tests/ex01_1",
  "members/sample_077/tests/ex01_2",
  "members/sample_078/raw_code",
  "members/sample_078/tests/ex01_0",
  "members/sample_078/tests/ex01_1",
  "members/sample_078/tests/ex01_2",
  "members/sample_079/raw_code",
  "members/sample_079/tests/ex01_0",
  "members/sample_079/tests/ex01_1",
  "members/sample_079/tests/ex01_2",
  "members/sample_080/raw_code",
  "members/sample_080/tests/ex01_0",
  "members/sample_080/tests/ex01_1",
  "members/sample_080/tests/ex01_2",
  "members/sample_081/raw_code",
  "members/sample_081/tests/ex01_0",
  "members/sample_081/tests/ex01_1",
  "members/sample_081/tests/ex01_2",
  "members/sample_082/raw_code",
  "members/sample_082/tests/ex01_0",
  "members/sample_082/tests/ex01_1",
  "members/sample_082/tests/ex01_2",
  "members/sample_083/raw_code",
  "members/sample_083/tests/ex01_0",
  "members/sample_083/tests/ex01_1",
  "members/sample_083/tests/ex01_2",
  "members/sample_084/raw_code",
  "members/sample_084/tests/ex01_0",
  "members/sample_084/tests/ex01_1",
  "members/sample_084/tests/ex01_2",
  "members/sample_085/raw_code",
  "members/sample_085/tests/ex01_0",
  "members/sample_085/tests/ex01_1",
  "members/sample_085/tests/ex01_2",
  "members/sample_086/raw_code",
  "members/sample_086/tests/ex01_0",
  "members/sample_086/tests/ex01_1",
  "members/sample_086/tests/ex01_2",
  "members/sample_087/raw_code",
  "members/sample_087/tests/ex01_0",
  "members/sample_087/tests/ex01_1",
  "members/sample_087/tests/ex01_2",
  "members/sample_088/raw_code",
  "members/sample_088/tests/ex01_0",
  "members/sample_088/tests/ex01_1",
  "members/sample_088/tests/ex01_2",
  "members/sample_089/raw_code",
  "members/sample_089/tests/ex01_0",
  "members/sample_089/tests/ex01_1",
  "members/sample_089/tests/ex01_2",
  "members/sample_090/raw_code",
  "members/sample_090/tests/ex01_0",
  "members/sample_090/tests/ex01_1",
  "members/sample_090/tests/ex01_2",
  "members/sample_091/raw_code",
  "members/sample_091/tests/ex01_0",
  "members/sample_091/tests/ex01_1",
  "members/sample_091/tests/ex01_2"
]
```
