# lab03-ex01--kmeans--combined_stdout--s42--c0

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 8; phân vùng: {'train': 8}.


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
    "n_cluster": 8,
    "n_observed": 8,
    "n_failed": 8,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 8
    }
  },
  {
    "test_id": "ex01_1",
    "n_cluster": 8,
    "n_observed": 8,
    "n_failed": 8,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 8
    }
  },
  {
    "test_id": "ex01_2",
    "n_cluster": 8,
    "n_observed": 8,
    "n_failed": 8,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 8
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex01_0:edit_band",
    "value": "medium",
    "n": 8,
    "n_cluster": 8,
    "rate": 1.0,
    "cohort_rate": 0.19852941176470587,
    "difference_from_cohort": 0.8014705882352942
  },
  {
    "feature": "stdout:ex01_2:edit_band",
    "value": "medium",
    "n": 7,
    "n_cluster": 8,
    "rate": 0.875,
    "cohort_rate": 0.16176470588235295,
    "difference_from_cohort": 0.7132352941176471
  },
  {
    "feature": "stdout:ex01_1:edit_band",
    "value": "medium",
    "n": 6,
    "n_cluster": 8,
    "rate": 0.75,
    "cohort_rate": 0.19117647058823528,
    "difference_from_cohort": 0.5588235294117647
  },
  {
    "feature": "stdout:ex01_0:relation",
    "value": "whitespace",
    "n": 8,
    "n_cluster": 8,
    "rate": 1.0,
    "cohort_rate": 0.7279411764705882,
    "difference_from_cohort": 0.2720588235294118
  },
  {
    "feature": "stdout:ex01_1:relation",
    "value": "whitespace",
    "n": 8,
    "n_cluster": 8,
    "rate": 1.0,
    "cohort_rate": 0.7279411764705882,
    "difference_from_cohort": 0.2720588235294118
  },
  {
    "feature": "stdout:ex01_2:relation",
    "value": "whitespace",
    "n": 8,
    "n_cluster": 8,
    "rate": 1.0,
    "cohort_rate": 0.7279411764705882,
    "difference_from_cohort": 0.2720588235294118
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 8,
    "n_cluster": 8,
    "rate": 1.0,
    "cohort_rate": 0.8235294117647058,
    "difference_from_cohort": 0.17647058823529416
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "0",
    "n": 3,
    "n_cluster": 8,
    "rate": 0.375,
    "cohort_rate": 0.21323529411764705,
    "difference_from_cohort": 0.16176470588235295
  },
  {
    "feature": "ast:c_while",
    "value": "1",
    "n": 4,
    "n_cluster": 8,
    "rate": 0.5,
    "cohort_rate": 0.3382352941176471,
    "difference_from_cohort": 0.16176470588235292
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 8,
    "n_cluster": 8,
    "rate": 1.0,
    "cohort_rate": 0.8897058823529411,
    "difference_from_cohort": 0.11029411764705888
  },
  {
    "feature": "stdout:ex01_1:edit_band",
    "value": "large",
    "n": 2,
    "n_cluster": 8,
    "rate": 0.25,
    "cohort_rate": 0.13970588235294118,
    "difference_from_cohort": 0.11029411764705882
  },
  {
    "feature": "ast:c_if",
    "value": "0",
    "n": 5,
    "n_cluster": 8,
    "rate": 0.625,
    "cohort_rate": 0.5220588235294118,
    "difference_from_cohort": 0.1029411764705882
  },
  {
    "feature": "ast:c_do",
    "value": "1",
    "n": 1,
    "n_cluster": 8,
    "rate": 0.125,
    "cohort_rate": 0.029411764705882353,
    "difference_from_cohort": 0.09558823529411764
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 8,
    "n_cluster": 8,
    "rate": 1.0,
    "cohort_rate": 0.9705882352941176,
    "difference_from_cohort": 0.02941176470588236
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 8,
    "n_cluster": 8,
    "rate": 1.0,
    "cohort_rate": 0.9705882352941176,
    "difference_from_cohort": 0.02941176470588236
  },
  {
    "feature": "test:ex01_0",
    "value": "fail",
    "n": 8,
    "n_cluster": 8,
    "rate": 1.0,
    "cohort_rate": 0.9926470588235294,
    "difference_from_cohort": 0.007352941176470562
  },
  {
    "feature": "test:ex01_1",
    "value": "fail",
    "n": 8,
    "n_cluster": 8,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "test:ex01_2",
    "value": "fail",
    "n": 8,
    "n_cluster": 8,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_do",
    "value": "0",
    "n": 7,
    "n_cluster": 8,
    "rate": 0.875,
    "cohort_rate": 0.9705882352941176,
    "difference_from_cohort": -0.09558823529411764
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 3,
    "n_cluster": 8,
    "rate": 0.375,
    "cohort_rate": 0.47794117647058826,
    "difference_from_cohort": -0.10294117647058826
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 8,
    "n_cluster": 8,
    "rate": 1.0,
    "cohort_rate": 0.8235294117647058,
    "difference_from_cohort": 0.17647058823529416
  },
  {
    "feature": "ast:c_while",
    "value": "1",
    "n": 4,
    "n_cluster": 8,
    "rate": 0.5,
    "cohort_rate": 0.3382352941176471,
    "difference_from_cohort": 0.16176470588235292
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 8,
    "n_cluster": 8,
    "rate": 1.0,
    "cohort_rate": 0.8897058823529411,
    "difference_from_cohort": 0.11029411764705888
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 8,
    "n_cluster": 8,
    "rate": 1.0,
    "cohort_rate": 0.9705882352941176,
    "difference_from_cohort": 0.02941176470588236
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 8,
    "n_cluster": 8,
    "rate": 1.0,
    "cohort_rate": 0.9705882352941176,
    "difference_from_cohort": 0.02941176470588236
  },
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 8,
    "n_cluster": 8,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 5,
    "n_cluster": 8,
    "rate": 0.625,
    "cohort_rate": 0.7867647058823529,
    "difference_from_cohort": -0.16176470588235292
  }
]
```


## IF–THEN dự đoán cluster, không dự đoán gold

```json
[
  {
    "rule_id": 3,
    "if": [
      "NOT (stdout:ex01_1:edit_band=small)",
      "stdout:ex01_2:relation=whitespace"
    ],
    "then_cluster": 0,
    "train_support": 8,
    "train_precision": 1.0,
    "holdout_support": 1,
    "holdout_precision": 0.0
  }
]
```


## Candidate chưa xác thực

```json
{
  "source": "local_heuristic_not_gold",
  "misconception_name": "Chưa đủ bằng chứng để đặt tên lỗi",
  "misconception_type": null,
  "reasoning": "Có 8 bài trong cụm. Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
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

sample_005, sample_003, sample_001, sample_002

## sample_001 — train — đại diện

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
			printf("%d ", valor);
			valor++;
			contador++;
		} while (contador <= N);
		putchar('\n');
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
  "source_sha256": "095a4400aa5dff8d8da94047ee44ff21e377a8c42d05eeac80641dc9774a860a",
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
      "output": "1 2 3 \n2 3 4 \n3 4 5 \n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1 2 3 4 \n2 3 4 5 \n3 4 5 6 \n4 5 6 7 \n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1 2 3 4 5 6 7 8 \n2 3 4 5 6 7 8 9 \n3 4 5 6 7 8 9 10 \n4 5 6 7 8 9 10 11 \n5 6 7 8 9 10 11 12 \n6 7 8 9 10 11 12 13 \n7 8 9 10 11 12 13 14 \n8 9 10 11 12 13 14 15 \n"
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
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
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


## sample_002 — train — đại diện

```c


#include <stdio.h>

void quadrado (int N) {
    int i, j;
    for (i = 0; i < N; i++) {
        for (j = (i + 1); j <= (N + i); j++)
            printf("%d\t", j); 
        printf("\t\n");
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
  "sample_id": "sample_002",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "ee3aef0b5dde5a9e64df36dcede74254f271e254b81afcbbbcf9dbfeb60694be",
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
      "output": "1\t2\t3\t\t\n2\t3\t4\t\t\n3\t4\t5\t\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\t\n2\t3\t4\t5\t\t\n3\t4\t5\t6\t\t\n4\t5\t6\t7\t\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\t\n2\t3\t4\t5\t6\t7\t8\t9\t\t\n3\t4\t5\t6\t7\t8\t9\t10\t\t\n4\t5\t6\t7\t8\t9\t10\t11\t\t\n5\t6\t7\t8\t9\t10\t11\t12\t\t\n6\t7\t8\t9\t10\t11\t12\t13\t\t\n7\t8\t9\t10\t11\t12\t13\t14\t\t\n8\t9\t10\t11\t12\t13\t14\t15\t\t\n"
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
    "stdout:ex01_1:edit_band": "medium",
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


## sample_003 — train — đại diện

```c


#include <stdio.h>

void quadrado (int N){

    int i = 1, contador = 0;
    while (i<=N)
    {
        for(contador=i; contador<i+N; contador++){
            if(contador == i+N-1){
                printf("%d", contador);
            }
            else
                printf("%d ", contador);
        }
        printf("\n");
        i++;
    }
    
}

int main(){

    int N=0;

    scanf("%d", &N);

    quadrado(N);

    return 0;
}
```

```json
{
  "sample_id": "sample_003",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "5a13b4128ba69d1016ea751b2ee4eac2d1da945af5049ec45d4cfd782c2d485b",
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
      "output": "1 2 3\n2 3 4\n3 4 5\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1 2 3 4\n2 3 4 5\n3 4 5 6\n4 5 6 7\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1 2 3 4 5 6 7 8\n2 3 4 5 6 7 8 9\n3 4 5 6 7 8 9 10\n4 5 6 7 8 9 10 11\n5 6 7 8 9 10 11 12\n6 7 8 9 10 11 12 13\n7 8 9 10 11 12 13 14\n8 9 10 11 12 13 14 15\n"
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
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
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


## sample_005 — train — đại diện

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
        for (j = i; j <= n+i-1; j++)
        {
            printf("%d \t ", j);
        }
        printf("\n");
    }
    
    
}
```

```json
{
  "sample_id": "sample_005",
  "partition": "train",
  "representative": true,
  "is_train_medoid": true,
  "raw_code_truncated": false,
  "source_sha256": "64ac9e507b5ad3426f9fbf6247628be8ed4dbe205e084555bcc2cf14bd296d32",
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
      "output": "1 \t 2 \t 3 \t \n2 \t 3 \t 4 \t \n3 \t 4 \t 5 \t \n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1 \t 2 \t 3 \t 4 \t \n2 \t 3 \t 4 \t 5 \t \n3 \t 4 \t 5 \t 6 \t \n4 \t 5 \t 6 \t 7 \t \n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1 \t 2 \t 3 \t 4 \t 5 \t 6 \t 7 \t 8 \t \n2 \t 3 \t 4 \t 5 \t 6 \t 7 \t 8 \t 9 \t \n3 \t 4 \t 5 \t 6 \t 7 \t 8 \t 9 \t 10 \t \n4 \t 5 \t 6 \t 7 \t 8 \t 9 \t 10 \t 11 \t \n5 \t 6 \t 7 \t 8 \t 9 \t 10 \t 11 \t 12 \t \n6 \t 7 \t 8 \t 9 \t 10 \t 11 \t 12 \t 13 \t \n7 \t 8 \t 9 \t 10 \t 11 \t 12 \t 13 \t 14 \t \n8 \t 9 \t 10 \t 11 \t 12 \t 13 \t 14 \t 15 \t \n"
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
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
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

void quadrado (int N){

    int i = 1, contador = 0;
    while (i<=N)
    {
        for(contador=i; contador<i+N; contador++){
            printf("%d ", contador);
        }
        printf("\n");
        i++;
    }
    
}

int main(){

    int N=0;

    scanf("%d", &N);

    quadrado(N);

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
  "source_sha256": "f4e53d2eadd88312b21cf0387bdd34e4be0e97678f97f7c6e50524609735af73",
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
      "output": "1 2 3 \n2 3 4 \n3 4 5 \n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1 2 3 4 \n2 3 4 5 \n3 4 5 6 \n4 5 6 7 \n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1 2 3 4 5 6 7 8 \n2 3 4 5 6 7 8 9 \n3 4 5 6 7 8 9 10 \n4 5 6 7 8 9 10 11 \n5 6 7 8 9 10 11 12 \n6 7 8 9 10 11 12 13 \n7 8 9 10 11 12 13 14 \n8 9 10 11 12 13 14 15 \n"
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
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
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


## sample_006 — train

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
        for (j = i; j <= n+i-1; j++)
        {
            printf("%d \t ", j);
        }
        printf("\n");
    }
    
    
}
```

```json
{
  "sample_id": "sample_006",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "7f7e629095d6a712a819af5bfd8abf55c5556121ccb40562658186e9d4f16689",
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
      "output": "1 \t 2 \t 3 \t \n2 \t 3 \t 4 \t \n3 \t 4 \t 5 \t \n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1 \t 2 \t 3 \t 4 \t \n2 \t 3 \t 4 \t 5 \t \n3 \t 4 \t 5 \t 6 \t \n4 \t 5 \t 6 \t 7 \t \n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1 \t 2 \t 3 \t 4 \t 5 \t 6 \t 7 \t 8 \t \n2 \t 3 \t 4 \t 5 \t 6 \t 7 \t 8 \t 9 \t \n3 \t 4 \t 5 \t 6 \t 7 \t 8 \t 9 \t 10 \t \n4 \t 5 \t 6 \t 7 \t 8 \t 9 \t 10 \t 11 \t \n5 \t 6 \t 7 \t 8 \t 9 \t 10 \t 11 \t 12 \t \n6 \t 7 \t 8 \t 9 \t 10 \t 11 \t 12 \t 13 \t \n7 \t 8 \t 9 \t 10 \t 11 \t 12 \t 13 \t 14 \t \n8 \t 9 \t 10 \t 11 \t 12 \t 13 \t 14 \t 15 \t \n"
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
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
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


## sample_007 — train

```c


#include <stdio.h>


void quadrado(int n){
	int i,j;
	
	for(i = 1; i <= n; i++){
		for (j = 1; j <= n; j++){
			printf("%d\t", i + j - 1);
			if (j != n) putchar('\t');	
		}
		
		putchar('\n'); 
	} 
}


int main(){
	int n;
	scanf("%d", &n);
	
	while(n < 2){
		scanf("%d", &n);
	}
	quadrado(n);
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
  "source_sha256": "8767da01c3bd18d843fe1e594adbb9ce0949ab69306b7a443c11538bc4f3f1e8",
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
      "output": "1\t\t2\t\t3\t\n2\t\t3\t\t4\t\n3\t\t4\t\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t\t2\t\t3\t\t4\t\n2\t\t3\t\t4\t\t5\t\n3\t\t4\t\t5\t\t6\t\n4\t\t5\t\t6\t\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t\t2\t\t3\t\t4\t\t5\t\t6\t\t7\t\t8\t\n2\t\t3\t\t4\t\t5\t\t6\t\t7\t\t8\t\t9\t\n3\t\t4\t\t5\t\t6\t\t7\t\t8\t\t9\t\t10\t\n4\t\t5\t\t6\t\t7\t\t8\t\t9\t\t10\t\t11\t\n5\t\t6\t\t7\t\t8\t\t9\t\t10\t\t11\t\t12\t\n6\t\t7\t\t8\t\t9\t\t10\t\t11\t\t12\t\t13\t\n7\t\t8\t\t9\t\t10\t\t11\t\t12\t\t13\t\t14\t\n8\t\t9\t\t10\t\t11\t\t12\t\t13\t\t14\t\t15\t\n"
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
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
    "stdout:ex01_2:edit_band": "medium"
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


## sample_008 — train

```c

#include <stdio.h>

void quadrado(int n)
{
    int i, j;
    for (i = 1; i <= n; i++){
        for (j = 0; j < n; j++){
            if (j) putchar('\t');
            printf("%d\t", i + j);
        }
        putchar('\n');
    }
}
int main()
{
    int n;
    scanf("%d", &n);
    if (n < 2) {
        printf("Número inválido!\n");
        return 1;
    }
    quadrado(n);
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
  "source_sha256": "4a60024ee776b041f2a69c665f7f7dfa2f6e2a07bbd9908af5761fbbb2a00ac1",
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
      "output": "1\t\t2\t\t3\t\n2\t\t3\t\t4\t\n3\t\t4\t\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t\t2\t\t3\t\t4\t\n2\t\t3\t\t4\t\t5\t\n3\t\t4\t\t5\t\t6\t\n4\t\t5\t\t6\t\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t\t2\t\t3\t\t4\t\t5\t\t6\t\t7\t\t8\t\n2\t\t3\t\t4\t\t5\t\t6\t\t7\t\t8\t\t9\t\n3\t\t4\t\t5\t\t6\t\t7\t\t8\t\t9\t\t10\t\n4\t\t5\t\t6\t\t7\t\t8\t\t9\t\t10\t\t11\t\n5\t\t6\t\t7\t\t8\t\t9\t\t10\t\t11\t\t12\t\n6\t\t7\t\t8\t\t9\t\t10\t\t11\t\t12\t\t13\t\n7\t\t8\t\t9\t\t10\t\t11\t\t12\t\t13\t\t14\t\n8\t\t9\t\t10\t\t11\t\t12\t\t13\t\t14\t\t15\t\n"
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
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "whitespace",
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
  "members/sample_008/tests/ex01_2"
]
```
