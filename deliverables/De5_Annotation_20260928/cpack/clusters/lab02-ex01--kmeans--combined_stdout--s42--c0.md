# lab02-ex01--kmeans--combined_stdout--s42--c0

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 90; phân vùng: {'train': 63, 'validation': 27}.


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
    "test_id": "ex01_2",
    "n_cluster": 90,
    "n_observed": 90,
    "n_failed": 90,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 90
    }
  },
  {
    "test_id": "ex01_1",
    "n_cluster": 90,
    "n_observed": 90,
    "n_failed": 89,
    "n_not_run": 0,
    "failure_rate_observed": 0.9888888888888889,
    "failure_rate_cluster": 0.9888888888888889,
    "outcome_counts": {
      "fail": 89,
      "pass": 1
    }
  },
  {
    "test_id": "ex01_0",
    "n_cluster": 90,
    "n_observed": 90,
    "n_failed": 88,
    "n_not_run": 0,
    "failure_rate_observed": 0.9777777777777777,
    "failure_rate_cluster": 0.9777777777777777,
    "outcome_counts": {
      "fail": 88,
      "pass": 2
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex01_0:edit_band",
    "value": "large",
    "n": 87,
    "n_cluster": 90,
    "rate": 0.9666666666666667,
    "cohort_rate": 0.5432098765432098,
    "difference_from_cohort": 0.4234567901234568
  },
  {
    "feature": "stdout:ex01_2:edit_band",
    "value": "large",
    "n": 89,
    "n_cluster": 90,
    "rate": 0.9888888888888889,
    "cohort_rate": 0.5740740740740741,
    "difference_from_cohort": 0.41481481481481486
  },
  {
    "feature": "stdout:ex01_0:relation",
    "value": "different",
    "n": 85,
    "n_cluster": 90,
    "rate": 0.9444444444444444,
    "cohort_rate": 0.5308641975308642,
    "difference_from_cohort": 0.4135802469135802
  },
  {
    "feature": "stdout:ex01_2:relation",
    "value": "different",
    "n": 87,
    "n_cluster": 90,
    "rate": 0.9666666666666667,
    "cohort_rate": 0.5617283950617284,
    "difference_from_cohort": 0.4049382716049382
  },
  {
    "feature": "stdout:ex01_1:edit_band",
    "value": "large",
    "n": 86,
    "n_cluster": 90,
    "rate": 0.9555555555555556,
    "cohort_rate": 0.5864197530864198,
    "difference_from_cohort": 0.3691358024691358
  },
  {
    "feature": "stdout:ex01_1:relation",
    "value": "different",
    "n": 85,
    "n_cluster": 90,
    "rate": 0.9444444444444444,
    "cohort_rate": 0.5925925925925926,
    "difference_from_cohort": 0.35185185185185186
  },
  {
    "feature": "test:ex01_0",
    "value": "fail",
    "n": 88,
    "n_cluster": 90,
    "rate": 0.9777777777777777,
    "cohort_rate": 0.9135802469135802,
    "difference_from_cohort": 0.06419753086419755
  },
  {
    "feature": "test:ex01_2",
    "value": "fail",
    "n": 90,
    "n_cluster": 90,
    "rate": 1.0,
    "cohort_rate": 0.9444444444444444,
    "difference_from_cohort": 0.05555555555555558
  },
  {
    "feature": "ast:c_update",
    "value": "0",
    "n": 80,
    "n_cluster": 90,
    "rate": 0.8888888888888888,
    "cohort_rate": 0.8518518518518519,
    "difference_from_cohort": 0.03703703703703698
  },
  {
    "feature": "ast:c_while",
    "value": "0",
    "n": 82,
    "n_cluster": 90,
    "rate": 0.9111111111111111,
    "cohort_rate": 0.8765432098765432,
    "difference_from_cohort": 0.03456790123456788
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 83,
    "n_cluster": 90,
    "rate": 0.9222222222222223,
    "cohort_rate": 0.8950617283950617,
    "difference_from_cohort": 0.02716049382716057
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 81,
    "n_cluster": 90,
    "rate": 0.9,
    "cohort_rate": 0.8765432098765432,
    "difference_from_cohort": 0.023456790123456805
  },
  {
    "feature": "ast:c_one_index",
    "value": "0",
    "n": 90,
    "n_cluster": 90,
    "rate": 1.0,
    "cohort_rate": 0.9876543209876543,
    "difference_from_cohort": 0.012345679012345734
  },
  {
    "feature": "ast:c_zero_index",
    "value": "0",
    "n": 90,
    "n_cluster": 90,
    "rate": 1.0,
    "cohort_rate": 0.9876543209876543,
    "difference_from_cohort": 0.012345679012345734
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 10,
    "n_cluster": 90,
    "rate": 0.1111111111111111,
    "cohort_rate": 0.09876543209876543,
    "difference_from_cohort": 0.012345679012345678
  },
  {
    "feature": "stdout:ex01_0:relation",
    "value": "empty",
    "n": 2,
    "n_cluster": 90,
    "rate": 0.022222222222222223,
    "cohort_rate": 0.012345679012345678,
    "difference_from_cohort": 0.009876543209876545
  },
  {
    "feature": "stdout:ex01_1:relation",
    "value": "empty",
    "n": 2,
    "n_cluster": 90,
    "rate": 0.022222222222222223,
    "cohort_rate": 0.012345679012345678,
    "difference_from_cohort": 0.009876543209876545
  },
  {
    "feature": "stdout:ex01_2:relation",
    "value": "empty",
    "n": 2,
    "n_cluster": 90,
    "rate": 0.022222222222222223,
    "cohort_rate": 0.012345679012345678,
    "difference_from_cohort": 0.009876543209876545
  },
  {
    "feature": "ast:c_subscript",
    "value": "1",
    "n": 3,
    "n_cluster": 90,
    "rate": 0.03333333333333333,
    "cohort_rate": 0.030864197530864196,
    "difference_from_cohort": 0.002469135802469137
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "0",
    "n": 73,
    "n_cluster": 90,
    "rate": 0.8111111111111111,
    "cohort_rate": 0.808641975308642,
    "difference_from_cohort": 0.0024691358024691024
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 83,
    "n_cluster": 90,
    "rate": 0.9222222222222223,
    "cohort_rate": 0.8950617283950617,
    "difference_from_cohort": 0.02716049382716057
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 81,
    "n_cluster": 90,
    "rate": 0.9,
    "cohort_rate": 0.8765432098765432,
    "difference_from_cohort": 0.023456790123456805
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 89,
    "n_cluster": 90,
    "rate": 0.9888888888888889,
    "cohort_rate": 0.9876543209876543,
    "difference_from_cohort": 0.0012345679012346622
  },
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 90,
    "n_cluster": 90,
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
    "rule_id": 7,
    "if": [
      "stdout:ex01_0:edit_band=large",
      "NOT (stdout:ex01_2:relation=different)"
    ],
    "then_cluster": 0,
    "train_support": 3,
    "train_precision": 0.6666666666666666,
    "holdout_support": 1,
    "holdout_precision": 1.0
  },
  {
    "rule_id": 8,
    "if": [
      "stdout:ex01_0:edit_band=large",
      "stdout:ex01_2:relation=different"
    ],
    "then_cluster": 0,
    "train_support": 60,
    "train_precision": 1.0,
    "holdout_support": 24,
    "holdout_precision": 1.0
  }
]
```


## Candidate chưa xác thực

```json
{
  "source": "local_heuristic_not_gold",
  "misconception_name": "Có dấu hiệu: In hằng số / Chưa tính toán theo đầu vào",
  "misconception_type": null,
  "category": "mixed",
  "reasoning": "1/90 bài có lệnh in hằng/biến hằng, không phụ thuộc input, và trượt ít nhất hai test.",
  "teaching_hint": "Thử hai giá trị n khác nhau; tính tổng từ 1 đến n rồi in kết quả thay cho hằng số.",
  "evidence_samples": []
}
```


## Luật cơ chế và evidence cục bộ

```json
[
  {
    "rule_id": "C_HARDCODED_OUTPUT",
    "submission_id": "sample_013",
    "if_vi": [
      "AST cho thấy output hằng, không phụ thuộc giá trị nhập",
      "ít nhất hai test quan sát được bị trượt"
    ],
    "then_vi": "In hằng số / Chưa tính toán theo đầu vào",
    "category": "observed_error",
    "status": "candidate_requires_human_review",
    "source": [
      {
        "line_start": 4,
        "line_end": 4,
        "code": "printf(\"Hello world!\\n\")"
      }
    ],
    "explanation": {
      "title": "In hằng số / Chưa tính toán theo đầu vào",
      "code_pattern": [
        "AST cho thấy output hằng, không phụ thuộc giá trị nhập"
      ],
      "behavioral_pattern": [
        "ít nhất hai test quan sát được bị trượt"
      ],
      "hypothesis": [
        "Có thể người viết mới in một đáp án cố định và chưa triển khai tính toán theo input."
      ],
      "caveat": [
        "Đây là mẫu code quan sát được, chưa chứng minh nhận thức của người học."
      ],
      "suggested_follow_up": [
        "Với hai giá trị n khác nhau, truy vết tổng từ 1 đến n rồi thay hằng số bằng kết quả tính."
      ]
    },
    "conditions_oav": [
      {
        "object": "Bài làm",
        "attribute": "is_hardcoded_output",
        "operator": "=",
        "value": "True"
      },
      {
        "object": "Kết quả kiểm thử",
        "attribute": "Có ít nhất hai test fail quan sát được",
        "operator": "=",
        "value": "Có"
      }
    ],
    "tests": [
      {
        "test_id": "ex01_0",
        "input": "1 2 3",
        "expected": "3\n",
        "output": "Hello world!\n"
      },
      {
        "test_id": "ex01_1",
        "input": "6 2 1",
        "expected": "6\n",
        "output": "Hello world!\n"
      },
      {
        "test_id": "ex01_2",
        "input": "-1 3 1",
        "expected": "3\n",
        "output": "Hello world!\n"
      }
    ],
    "alternative": "Đây là mẫu code quan sát được, chưa chứng minh nhận thức của người học.",
    "suggestion": "Với hai giá trị n khác nhau, truy vết tổng từ 1 đến n rồi thay hằng số bằng kết quả tính."
  }
]
```


## Đại diện

sample_004, sample_087, sample_003, sample_013

## sample_003 — train — đại diện

```c
#include <stdio.h>



int main() {
	int x;
	int horas;
	int min;
	int seg;
	
	scanf("%d", &x);
	while (x <= 0) {
		
		scanf("%d", &x);
	}
	horas = x / (60*60);
	x = x % (60*60);
	min = x / (60);
	x = x % (60);
	seg = x;
	printf("%02d:%02d:%02d\n", horas, min, seg);
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
  "source_sha256": "c019eeb56cb9e528eb68c6f4dc01f03eec2adf835ccf90c83df3fd4e0d2e8ef3",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "00:00:01\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "00:00:06\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "00:00:03\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_004 — train — đại diện

```c
#include <stdio.h>

int main() {

	int n1, n2, n3;

	printf("Insira 3 numeros:\n");
	scanf("%d %d %d", &n1, &n2, &n3);

	if ((n1 > n2) && (n1 > n3)) {
		printf("%d\n", n1);}

	else if ((n2 > n1) && (n2 > n3)) {
		printf("%d\n", n2);}

	else {
		printf("%d\n", n3);};

	return 0;
}

```

```json
{
  "sample_id": "sample_004",
  "partition": "train",
  "representative": true,
  "is_train_medoid": true,
  "raw_code_truncated": false,
  "source_sha256": "3e3ff0379183af5d0cf25167a4d09fd1abc8397f196fac2da1a60a8eae8522b2",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Insira 3 numeros:\n3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Insira 3 numeros:\n6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Insira 3 numeros:\n3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_013 — train — đại diện

```c
#include <stdio.h>

int main(){
    printf("Hello world!\n");
    return 0;
}
```

```json
{
  "sample_id": "sample_013",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "80bc84502a44e1ffab5a8c311de16cf178003936dd4ab5da6aba1e151d1fd66f",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Hello world!\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Hello world!\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Hello world!\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "0",
    "ast:c_update": "0",
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
    "is_hardcoded_output": true
  }
}
```


## sample_087 — validation — đại diện

```c


#include <stdio.h>

int main(){
    int x,y,z;

    scanf("%d%d%d",&x,&y,&z);

    if (x>=y && x>=z)
        printf("%d\n",x);

    else if (x>=z)
        printf("%d\n",y);
    
    else
        printf("%d\n",z);

    return 0;
}
```

```json
{
  "sample_id": "sample_087",
  "partition": "validation",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "ada988055bfcf98e936635c0e77bccd09c6142c7f15535b903f80ae352f26f13",
  "outcomes": {
    "ex01_0": "pass",
    "ex01_1": "pass",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "1\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "pass",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex01_0:relation": "__unknown__",
    "stdout:ex01_0:edit_band": "__unknown__",
    "stdout:ex01_1:relation": "__unknown__",
    "stdout:ex01_1:edit_band": "__unknown__",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "pass",
    "test:ex01_2": "fail",
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


## sample_001 — train

```c
#include <stdio.h>

int main()
{
    int a,b,c;
    printf("Introduza 3 números inteiros\n");
    scanf("%d%d%d",&a,&b,&c);
    if (a>=b && a >= c){
        printf("%d\n",a);
    }

    if ( b >= a && b >= c){
        printf("%d\n",b);
    }

    if (c >= b && c >= a){
        printf("%d\n",c);
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
  "source_sha256": "cf2d8b54dffe8b448bb0b83db48586232481593bd6b8d9c1a6b9a261af523ded",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza 3 números inteiros\n3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza 3 números inteiros\n6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza 3 números inteiros\n3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_002 — train

```c
#include <stdio.h>

#define INFERIOR 1
#define SUPERIOR 3
#define PASSO 1

int main()
{
	int maior;
	int input;
	int contador;

	for (contador = INFERIOR; contador <= SUPERIOR; contador += PASSO)
	{
		scanf("%d", &input);
		if (contador == 1 || maior < input) {
			maior = input;
		}
	}
	printf("Maior: %d\n", maior);
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
  "source_sha256": "a7068b535f57a0f00e433d0b3246e271158eaa474b49cc65f024088448562b10",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Maior: 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Maior: 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Maior: 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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

int main() {

	int n1, n2, n3;

	printf("Insira 3 numeros:\n");
	scanf("%d %d %d", &n1, &n2, &n3);

	if ((n1 > n2) & (n1 > n3)) {
		printf("%d\n", n1);}

	else if ((n2 > n1) & (n2 > n3)) {
		printf("%d\n", n2);}

	else {
		printf("%d\n", n3);};

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
  "source_sha256": "8455adc637940f3df57d58f22879963614d93364a3c21910af25cd55dbf65d0b",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Insira 3 numeros:\n3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Insira 3 numeros:\n6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Insira 3 numeros:\n3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_006 — train

```c
#include <stdio.h>

int main() {

int n1, n2, n3;

printf("Insira 3 numeros:\n");
scanf("%d %d %d", &n1, &n2, &n3);

if ((n1 > n2) & (n1 > n3)) {
	printf("%d\n", n1);}

else if ((n2 > n1) & (n2 > n3)) {
	printf("%d\n", n2);}

else {
	printf("%d\n", n3);};

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
  "source_sha256": "69bd0fe9b1dce6832df7eaf3025ff4fb2085aca4a23e5fd2d869deb22c7fa60f",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Insira 3 numeros:\n3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Insira 3 numeros:\n6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Insira 3 numeros:\n3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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

int main(){

 int a,b,c;
 printf("Introduza tres inteiros: ");
 scanf("%d %d %d", &a, &b, &c);

 if (a > b && a > c){
 	printf("%d\n", a);
 }

 if (b > a && b > c){
    printf("%d\n", b);
 }
 	

 if (c > a && c > b){
 	printf("%d\n", c );
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
  "source_sha256": "e0619c8a9b118111fdb9533796e0e8cbae8b423f0240e261fe699c59ecc22911",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza tres inteiros: 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza tres inteiros: 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza tres inteiros: 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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

int maior(int a, int b,int c){

	if (a > b && a > c){
 	return a;
 }

 if (b > a && b > c){
    return b;
 }
 	

 if (c > a && c > b){
 	return c;
 }
 return 0;
}

int main(){

 int a, b, c, m;
 printf("Introduza tres inteiros: ");
 scanf("%d %d %d", &a, &b, &c);
 m = maior(a, b, c);
 printf("%d\n", m);

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
  "source_sha256": "7fd170cba2e411cb3c956712b4e9413bd04ac480b91961aa0453fea77f3c4143",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza tres inteiros: 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza tres inteiros: 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza tres inteiros: 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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

int main(){

 int a,b,c;
 printf("Introduza tres inteiros: ");
 scanf("%d %d %d", &a, &b, &c);
 
 if (a > b && a > c){
 	printf("%d", a);
 }

 if (b > a && b > c){
    printf("%d", b);
 }
 	

 if (c > a && c > b){
 	printf("%d", c );
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
  "source_sha256": "50552977b3067892b163355498c977566b539f8ad743c8b0b614f1e900789295",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza tres inteiros: 3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza tres inteiros: 6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza tres inteiros: 3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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

 int a,b,c;
 printf("Introduza tres inteiros: ");
 scanf("%d", &a);
 scanf("%d", &b);
 scanf("%d", &c);

 if (a > b && a > c){
 	printf("%d", a);
 }

 if (b > a && b > c){
    printf("%d", b);
 }
 	

 if (c > a && c > b){
 	printf("%d", c );
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
  "source_sha256": "cdae0d9d701f85baa102edfb847bc06e014d6211711d3eca2ead2a77cd7ca8bf",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza tres inteiros: 3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza tres inteiros: 6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza tres inteiros: 3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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

int main(){

 int a,b,c;
 printf("Introduza tres inteiros: ");
 scanf("%d", &a);
 scanf("%d", &b);
 scanf("%d", &c);

 if (a > b && a > c){
 	printf("%d\n", a);
 }

 if (b > a && b > c){
    printf("%d\n", b);
 }
 	

 if (c > a && c > b){
 	printf("%d\n", c );
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
  "source_sha256": "b22908e50cf1d27d7a955741eb9387e76a801d53db7b5889da71c21bc1f8d8e8",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza tres inteiros: 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza tres inteiros: 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza tres inteiros: 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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

	int a, b, c;

	printf("Introduza tres numeros:\n");
	scanf("%d%d%d", &a, &b, &c);
	if (a > b && a > c){
		printf("%d\n", a);
	}
	if (b > a && b > c){
		printf("%d\n", b);
	}
	if (c > a && c > b){
		printf("%d\n", c );
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
  "source_sha256": "e72141450c52a87de883350157d45f55e291ac33ca2b7344b1f4e141731de69c",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza tres numeros:\n3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza tres numeros:\n6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza tres numeros:\n3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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

int main()
{
 int x,y,z,maior;
 printf("Insira 3 inteiros: \n");
 scanf (" %d%d%d",&x,&y,&z);
 maior = x;

 if (y > maior) {
  maior = y; }
 if (z > maior) {
  maior = z;
 }

 printf("O numero e: %d\n",maior);
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
  "source_sha256": "50ad1d0e286f5f4813565e3b9db1119fd333fddfa78d7747d44e99b391c17a51",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Insira 3 inteiros: \nO numero e: 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Insira 3 inteiros: \nO numero e: 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Insira 3 inteiros: \nO numero e: 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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
    int primeiro,segundo,terceiro,maior;

    printf("Insira três números ");
    scanf("%d%d%d", &primeiro,&segundo,&terceiro);

    {if (primeiro > segundo)    
        {
        if (primeiro > terceiro)
            {maior = primeiro;}
        }
    }

    {
    if (segundo > primeiro)    
        {   
        if (segundo > terceiro)
            {maior = segundo;}
        }   
    }

    {
    if (terceiro > primeiro)    
        {   
        if (terceiro > segundo)
            {maior = terceiro;}
        }   
    }
    printf("O maior número é %d\n",maior);
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
  "source_sha256": "c9afe7eb361388880096504ae91bc4eeab386a4b8b734ee6c86a21980b03e14a",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Insira três números O maior número é 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Insira três números O maior número é 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Insira três números O maior número é 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_016 — validation

```c
#include <stdio.h>



int main()
{
    int primeiro,segundo,terceiro,maior;

    printf("Insira três números ");
    scanf("%d%d%d", &primeiro,&segundo,&terceiro);

    {if (segundo > primeiro)
        maior = segundo;
     else
        if(terceiro > primeiro)
            maior = terceiro;
        else
            maior = primeiro;
    }

    printf("O maior número é %d \n",maior);

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
  "source_sha256": "faa133aca968aafcf201ad7dc71e3877af74996313b0e36a218d9bfe7a973d46",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Insira três números O maior número é 2 \n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Insira três números O maior número é 6 \n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Insira três números O maior número é 3 \n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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

    int primeiro,segundo,terceiro,maior;

    printf("Insira três números ");
    scanf("%d%d%d", &primeiro,&segundo,&terceiro);

    {if (primeiro > segundo)    
        {
        if (primeiro > terceiro)
            maior = primeiro;
        }
    }

    {
    if (segundo > primeiro)    
        {   
        if (segundo > terceiro)
            maior = segundo;
        }   
    }

    {
    if (terceiro > primeiro)    
        {   
        if (terceiro > segundo)
            maior = terceiro;
        }   
    }
    printf("O maior lido foi %d\n",maior);
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
  "source_sha256": "a11baeee3afb63cd30abf8696981a833c49e187dd6f70275c1698b64f71f5060",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Insira três números O maior lido foi 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Insira três números O maior lido foi 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Insira três números O maior lido foi 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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
    int num, max, i;
    printf("Introduza 3 numeros inteiros:\n");
    scanf("%d", &max);
    for(i = 0; i < 2; i = i + 1)
    {
        scanf("%d", &num);
        if (num > max)
        {
            max = num;
        }
    }
    printf("O maior numero e:\n");
    printf( "%d\n", max);
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
  "source_sha256": "d2fcefde322a917a1827cc1a44c3b26cda3857782b3f44241930f9efdab43492",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza 3 numeros inteiros:\nO maior numero e:\n3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza 3 numeros inteiros:\nO maior numero e:\n6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza 3 numeros inteiros:\nO maior numero e:\n3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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

int main() {
    int a, b, c;
    printf("Introduza 3 numeros inteiros: \n");
    scanf("%d%d%d", &a, &b, &c);
    if (a <= b) {
        if (b <= c) {
            printf("%d", c);
        }
        else{
            printf("%d", b);
        }
    } 
    else {
        if (a <= c) {
            printf("%d", c);
        }
        else {
            printf("%d", a);
        }
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
  "source_sha256": "43ba399a72c759eb6e61161c49acc6d7d2dcb3c07a02191e7a5e0105f923f9f8",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza 3 numeros inteiros: \n3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza 3 numeros inteiros: \n6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza 3 numeros inteiros: \n3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_020 — train

```c
#include <stdio.h>


int main()
{
int maior,cont,num;
scanf ("%d",&maior);
for(cont =0;cont <2; cont++)
  {
   scanf("%d",&num);
   if (num > maior)
     {
     maior = num;
     } 
  }
printf ("O maior e %d\n",maior);
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
  "source_sha256": "5ea7bbc16800b4318a9ac219aea7d54d0764f9a349b99af75bc286ac06d7e3da",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "O maior e 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "O maior e 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "O maior e 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
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


int main()
{
int maior,b,c;
scanf ("%d%d%d",&maior,&b,&c);
if (b >maior)
  {
   maior = b;
  }
if(c> maior)
  {
  maior = c;
  }
printf ("O maior e %d\n",maior);
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
  "source_sha256": "3f8bc2839fa9e5782636263abe69e55f04d043b0d5406418e29ee62826d493d9",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "O maior e 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "O maior e 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "O maior e 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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

int main(){
    int num, i, maior;
    maior = 0;
    for(i = 1; i <= 3; ++i){
        printf("Insira um número: ");
        scanf("%d", &num);
        if(num > maior){
            maior = num;
        }
    }
    printf("O maior número é: %d\n", maior);
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
  "source_sha256": "5848495d44851a083b92f7b3697c579e6c4112d39b0972b30075ced185e1f9ad",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Insira um número: Insira um número: Insira um número: O maior número é: 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Insira um número: Insira um número: Insira um número: O maior número é: 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Insira um número: Insira um número: Insira um número: O maior número é: 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
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


## sample_023 — train

```c
#include <stdio.h>

int main(){
    int num1, num2, num3;
    printf("Insira três inteiros: ");
    scanf("%d %d %d", &num1, &num2, &num3);
    if(num1 > num2 && num1 > num3){
        printf("%d\n", num1);
    } else if(num2 > num1 && num2 > num3){
        printf("%d\n", num2);
    } else{
        printf("%d\n", num3);
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
  "source_sha256": "55dc74c75ca8c9dc27646ca654492d5d95fef245be0743e398e9837b28d8a64a",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Insira três inteiros: 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Insira três inteiros: 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Insira três inteiros: 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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



int main () {
    int a;
    int b;
    int c;

    printf ("Introduza três numeros:\n");
    scanf("%d%d%d", &a, &b, &c);

    if (a > b) {
        if (a > c) {
            printf(" O numero maior é %d\n", a);
        }
        else {
            printf( " O maior numero é %d\n", c);
        }}
    else {
        if (b > c) {
            printf(" O maior numero é %d\n", b);
        }
        else {
            printf("O maior numero é %d\n", c);
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
  "source_sha256": "d9aa6b4e4b3b45261a33fe3f6eba85b00ec21d5942fc361ec7fe1707059fac34",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza três numeros:\nO maior numero é 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza três numeros:\n O numero maior é 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza três numeros:\n O maior numero é 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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

#define NUM_PEDIDO 3



int main() {
  int i, maior, cont=0;

  printf("Insira três números inteiros para ver qual é o maior:\n1º número -> ");
  scanf("%d", &i);
  maior = i;
  while (++cont < NUM_PEDIDO) {
    printf("%dº número -> ", cont+1);
    scanf("%d", &i);
    if (i > maior)
      maior = i;
  }

  printf("O maior número inserido pelo utilizardor é: %d\n", maior);

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
  "source_sha256": "3a6e98d5b1ee3d5fb91f3be787fb678982fa1046e9d0e633178273ef7d67154f",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Insira três números inteiros para ver qual é o maior:\n1º número -> 2º número -> 3º número -> O maior número inserido pelo utilizardor é: 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Insira três números inteiros para ver qual é o maior:\n1º número -> 2º número -> 3º número -> O maior número inserido pelo utilizardor é: 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Insira três números inteiros para ver qual é o maior:\n1º número -> 2º número -> 3º número -> O maior número inserido pelo utilizardor é: 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
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


## sample_026 — train

```c
#include <stdio.h>
int main() {
  int a, b, c;
  printf("Introduz o primeiro número: ");
  scanf("%d", &a);
  printf("Introduz o segundo número: ");
  scanf("%d", &b);
  printf("Introduz o terceiro número: ");
  scanf("%d", &c);
  if (a >= b) {
    if (c >= a) {
      printf("%d\n", c);
    } else {
      printf("%d\n", a);
    }
  } else {
    if (c >= b) {
      printf("%d\n", c);
    } else {
      printf("%d\n", b);
    }
  }
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
  "source_sha256": "d0a40193686f99c99befeae4263092b0e447098efa86abe9c60e56b65da67c1c",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduz o primeiro número: Introduz o segundo número: Introduz o terceiro número: 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduz o primeiro número: Introduz o segundo número: Introduz o terceiro número: 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduz o primeiro número: Introduz o segundo número: Introduz o terceiro número: 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_027 — validation

```c


#include <stdio.h>

int main()
{
    int a, b, c;
    scanf("%d%d%d", &a, &b, &c);

    if (a > b && a > c)
    {
        printf("The highest number is: %d\n", a);
    }
    else if (b > a && b > c)
    {
        printf("The highest value is: %d\n", b);
    }
    else
    {
        printf("The highest value is %d\n", c);
    }

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
  "source_sha256": "5427eff8d2550d2a48fc81f53dae6c8bd4e0bddc9f3c2faff6d55642658297d5",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "The highest value is 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "The highest number is: 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "The highest value is: 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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
    int n1, n2, n3, max;
    printf("Introduza tres numeros:\n");
    scanf("%d %d %d", &n1, &n2, &n3);
    max = n1;
    if (n2 > max) 
        max = n2;
    if (n3 > max) 
        max = n3;
    printf("o maximo é:%d\n", max);
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
  "source_sha256": "3beda59b0e210fab7b117857e35bfbadc81fbb307c3799941b3b3e60618fbd4b",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza tres numeros:\no maximo é:3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza tres numeros:\no maximo é:6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza tres numeros:\no maximo é:3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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



int main()
{
    int x, y, z, max;
    printf("Introduza tres inteiros:\n");
    scanf("%d%d%d", &x, &y, &z);
    max = x;
    if (y > max)
        max = y;
    if (z > max)
        max = z;
    printf("%d\n", max);
    
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
  "source_sha256": "c58b4a72b44a7196d9b0e7ad357880a071de46658206dc3c6f59f3f73544c42c",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza tres inteiros:\n3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza tres inteiros:\n6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza tres inteiros:\n3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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

int main(){
    int a;
    int b;
    int c;
    printf("? ");
    scanf("%d", &a);
    printf("? ");
    scanf("%d", &b);
    printf("? ");
    scanf("%d", &c);
    if(a < 1 || b < 1 || c < 1){
        printf("As dimensões dos lados dos triângulos devem ser todas positivas");
    }
    else{
        if(a + b <= c || a + c <= b || c + b <= a){
            printf("Não é triângulo");
        }
        else{
            if(a == b && b == c){
                printf("O triângulo é equilátero");
            }
            else{
                if(a == b || b == c || c == a){
                    printf("O triângulo é isósceles");
                }
                else{
                    printf("O triângulo é escaleno");
                }
            }
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
  "source_sha256": "d9f887acf892f13d888c0e8d6bd094fde2f5b9a31e2a327e601a60e6ae13aff1",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "? ? ? Não é triângulo"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "? ? ? Não é triângulo"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "? ? ? As dimensões dos lados dos triângulos devem ser todas positivas"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_031 — validation

```c
#include <stdio.h>

int main(){
    int a;
    int b;
    int c;
    printf("? ");
    scanf("%d", &a);
    printf("? ");
    scanf("%d", &b);
    printf("? ");
    scanf("%d", &c);
    if(a < 1 || b < 1 || c < 1){
        printf("As dimensões dos lados do triângulo devem ser todas positivas");
    }
    else{
        if(a + b <= c || a + c <= b || c + b <= a){
            printf("Não é triângulo");
        }
        else{
            if(a == b && b == c){
                printf("O triângulo é equilátero");
            }
            else{
                if(a == b || b == c || c == a){
                    printf("O triângulo é isósceles");
                }
                else{
                    printf("O triângulo é escaleno");
                }
            }
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
  "source_sha256": "690d915c9cdd3902713edfa2b7553cd372d99f2763d866ef4cadcc49f114b815",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "? ? ? Não é triângulo"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "? ? ? Não é triângulo"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "? ? ? As dimensões dos lados do triângulo devem ser todas positivas"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_032 — validation

```c
#include <stdio.h>

int main()
{
    int x, y, z;
    printf("Introduza três inteiros.\n");
    scanf("%d%d%d", &x, &y, &z);
    if(x > y && x > z)
        printf("%d\n", x);    
    else if(y > z)
        printf("%d\n", y);
    else
        printf("%d\n", z);
    return 0;
}
```

```json
{
  "sample_id": "sample_032",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "eb01a01e3273a6675808d3ebe33de5b7b592ef38997c8f3a715f2857d282d41b",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza três inteiros.\n3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza três inteiros.\n6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza três inteiros.\n3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_033 — validation

```c
#include <stdio.h>
int main()
{
    int x, y, z;
    printf("Introduza três inteiros.\n");
    scanf("%d %d %d", &x, &y, &z);
    if(x > y && x > z)
        printf("%d\n", x);    
    else if(y > z)
        printf("%d\n", y);
    else
        printf("%d\n", z);
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
  "source_sha256": "72279d6d2704a8c557a48d1532cd1ae07a102e0163d1e763c3e6b2b830e36534",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza três inteiros.\n3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza três inteiros.\n6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza três inteiros.\n3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_034 — validation

```c
#include <stdio.h>
int main()
{
    int x, y, z;
    printf("Introduza três inteiros.\n");
    scanf("%d%d%d", &x, &y, &z);
    if(x > y && x > z)
        printf("%d\n", x);    
    else if(y > z)
        printf("%d\n", y);
    else
        printf("%d\n", z);
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
  "source_sha256": "beaa31f9441e090d09764b5e1eba8019ed9f69322614f3665a1bb531fb1843c2",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza três inteiros.\n3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza três inteiros.\n6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza três inteiros.\n3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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

int main()
{
    int x, y, z;
    printf("Introduza três inteiros.\n");
    scanf("%d\n%d\n%d", &x, &y, &z);
    if(x > y && x > z)
        printf("O maior dos três números é: %d\n", x);    
    else if(y > z)
        printf("O maior dos três números é: %d\n", y);
    else
        printf("O maior dos três números é: %d\n", z);
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
  "source_sha256": "2317f969430e0cec68e4b0ac41a78ea7e9527e2cf96564f80c8b5528dd8f2e3f",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza três inteiros.\nO maior dos três números é: 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza três inteiros.\nO maior dos três números é: 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza três inteiros.\nO maior dos três números é: 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_036 — validation

```c
#include <stdio.h>

int main()
{
    int x, y, z;
    printf("Introduza três inteiros.\n");
    scanf("%d\n%d\n%d", &x, &y, &z);
    if(x > y && x > z)
        printf("%d", x);    
    else if(y > z)
        printf("%d", y);
    else
        printf("%d", z);
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
  "source_sha256": "500ba086cb3ca10a8a0c911828e02c3971ae81cc691009cd21e9af1be1310cae",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza três inteiros.\n3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza três inteiros.\n6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza três inteiros.\n3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_037 — train

```c
#include <stdio.h>

int main()
{
	int num1, cont=0, num, maior;
	printf("Escreva um numero inteiro:");
	scanf("%d", &num1);
	maior = num1;
	while (cont < 2)
	{
		printf("Escreva um numero inteiro:");
		scanf("%d", &num);
		if (num >= num1)
		{
			maior = num;
		}
		cont++;
	}
	printf("%d\n", maior);
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
  "source_sha256": "4f1d5f696a4f1e068b669dd9626fa00738cb1e2c82f58680a40ed4099895ab35",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Escreva um numero inteiro:Escreva um numero inteiro:Escreva um numero inteiro:3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Escreva um numero inteiro:Escreva um numero inteiro:Escreva um numero inteiro:6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Escreva um numero inteiro:Escreva um numero inteiro:Escreva um numero inteiro:1\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
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


## sample_038 — train

```c
#include <stdio.h>

int main()
{
  int a, b, c;

  printf("Escreva 3 números:\n");
  scanf("%d\n%d\n%d", &a, &b, &c);

  if (a > b && a > c)
    printf("%d é o maior número\n", a);
  else if (b > a && b > c)
    printf("%d é o maior número\n", b);   
   else
    printf("%d é o maior número\n", c); 
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
  "source_sha256": "e91426b14cd05bcc932d93d763c087f731417d74be6ef4841385809cb3041900",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Escreva 3 números:\n3 é o maior número\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Escreva 3 números:\n6 é o maior número\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Escreva 3 números:\n3 é o maior número\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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

int main()
{
  int a, b, c;

  scanf("%d%d%d", &a, &b, &c);

  if (a > b && a > c)
    printf("%d é o maior número\n", a);
  else if (b > a && b > c)
    printf("%d é o maior número\n", b);   
  else
    printf("%d é o maior número\n", c); 

    
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
  "source_sha256": "9e535713f0c3a7b3f44c893de30386a5d210757b8aad44375cf161e5eb15970a",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3 é o maior número\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6 é o maior número\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3 é o maior número\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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
  int N, M;

  scanf("%d%d", &N, &M);

  if(N > M)
    printf("\n%d\n%d\n", M, N);
  else
    printf("\n%d\n%d\n", N, M);

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
  "source_sha256": "6a5a9ca6682729dfa6e3bafc804779035ad088c873f3274cbcd7c7b635f2b47d",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "\n1\n2\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "\n2\n6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "\n-1\n3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_041 — validation

```c
#include <stdio.h>
int n_original, dig, numero_dig = 0, soma, n;

int main(){
    printf("Escreva um numero\n");
    scanf("%d", &n_original);

    n = n_original;
    while (n > 0)
    {
        dig = n % 10;
        soma = soma + dig;
        numero_dig++;
        n = n/10;
    }
    printf("%d\n%d", numero_dig, soma);
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
  "source_sha256": "d41937a2127b989f54dfc89cf4145e13a4695e3105406f37e719abd7dd1883fe",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Escreva um numero\n1\n1"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Escreva um numero\n1\n6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Escreva um numero\n0\n0"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
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


## sample_042 — train

```c
#include <stdio.h>

int main() {
    int n1, n2, n3, n4;
    printf("Insira tres numeros, separados por virgulas:");
    scanf("%d,%d,%d",&n1,&n2,&n3);
    if (n1>n2 && n1>n3)
        n4 = n1;
    else if(n2>n1 && n2>n3)
        n4 = n2;
    else n4 = n3;
    printf("O maior numero e': %d",n4);
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
  "source_sha256": "9a22c7d6633268c7ad961f7c20c56f51e206a416ef5e59c1c2210beaff39fddf",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Insira tres numeros, separados por virgulas:O maior numero e': 32767"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Insira tres numeros, separados por virgulas:O maior numero e': 817556320"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Insira tres numeros, separados por virgulas:O maior numero e': 607572544"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_043 — train

```c
#include <stdio.h>

int main() {
    int n1, n2, n3, n4;
    printf("Insira tres numeros, separados por virgulas:");
    scanf("%d %d    %d",&n1,&n2,&n3);
    if (n1>n2 && n1>n3)
        n4 = n1;
    else if(n2>n1 && n2>n3)
        n4 = n2;
    else n4 = n3;
    printf("%d",n4);
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
  "source_sha256": "ac97029b6ea0f09fd490815795aabd95d20a624e34fad988c4ea1cff451db2c7",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Insira tres numeros, separados por virgulas:3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Insira tres numeros, separados por virgulas:6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Insira tres numeros, separados por virgulas:3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_044 — train

```c
#include <stdio.h>

int main() {
    int n1, n2, n3, n4;
    printf("Insira tres numeros, separados por virgulas:");
    scanf("%d,%d,%d",&n1,&n2,&n3);
    if (n1>n2 && n1>n3)
        n4 = n1;
    else if(n2>n1 && n2>n3)
        n4 = n2;
    else n4 = n3;
    printf("%d",n4);
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
  "source_sha256": "803ff2e425220d6c65a526a9ac77a57bf0938ca6b7f055444aff64317f979b7b",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Insira tres numeros, separados por virgulas:128461856"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Insira tres numeros, separados por virgulas:32764"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Insira tres numeros, separados por virgulas:32766"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_045 — validation

```c


#include <stdio.h>

int main(){
    int i, n, maior = 0;
    for (i = 0; i < 3; i++){
        scanf("%d", &n);
        if (n > maior)
            maior = n;
    }
    printf("%d\n", n);
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
  "source_sha256": "c2bee6cc69f5a1192b9ab6c562d9c4382cc8abc4cac9043cbbc42d5f46c31828",
  "outcomes": {
    "ex01_0": "pass",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "1\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "1\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "__unknown__",
    "stdout:ex01_0:edit_band": "__unknown__",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex01_0": "pass",
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


## sample_046 — validation

```c


#include <stdio.h>

int main(){
    int i, n, maior = 0;
    for (i = 0; i < 3; i++){
        scanf("%d", &n);
        if (n > maior)
            maior = n;
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_046",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "4a26c8b005c03ed7e57b067ec4d8d7ad22356d0a2e51d72895a5aed485453d1f",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": ""
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": ""
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "empty",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "empty",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "empty",
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

int main() {
    int num1, num2, num3, maior;
    
    printf("Digite três números inteiros: ");
    scanf("%d %d %d", &num1, &num2, &num3);
    
    maior = num1;
    
    while (num2 > maior) {
        maior = num2;
    }
    
    while (num3 > maior) {
        maior = num3;
    }
    
    printf("O maior número é %d", maior);
    
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
  "source_sha256": "2ac19021862a02b7153388edfc1f45be2aaf6aa4245a0f06f19aee42baa8e28e",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Digite três números inteiros: O maior número é 3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Digite três números inteiros: O maior número é 6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Digite três números inteiros: O maior número é 3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_048 — train

```c

#include <stdio.h>
int main (){
    int num1,num2,num3;
    int contador;
    for(contador=0;contador<3;contador+=1){
        if (contador==0) 
            scanf( "%d",&num1);
        if (contador==1)
            scanf( "%d",&num2);
        if (contador==2)
            scanf( "%d",&num3);
    }
    if ((num1>=num2) && (num1>=num3)) 
        printf("n%d\n",num1);
    else if ((num2>=num1) && (num2>=num3)) 
        printf("n%d\n",num2);
    else if ((num3>=num2) && (num3>=num1)) 
        printf("n%d\n",num3); 
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
  "source_sha256": "fe7abc6930b9eec82f85e9aaba8a337fe970ced3a89a7c11805ba08d954c6ae6",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "n3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "n6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "n3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "medium",
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


## sample_049 — train

```c

#include <stdio.h>

int main() {
    int num1, num2, num3;
    scanf("%d", &num1);
    scanf("%d", &num2);
    scanf("%d", &num3);
    
    if (num1 > num2 && num1 > num3)
        printf("%d é o maior numero", num1);
    else if (num1 < num2 && num2 > num3)
        printf("%d é o maior numero", num2);
    else if (num3 > num1 && num3 > num2)
        printf("%d é o maior numero", num3);

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
  "source_sha256": "684b1dd1a7caf87f8dc811852b6d1ff91781f247bc26ea002d058bedd93ba3f1",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3 é o maior numero"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6 é o maior numero"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3 é o maior numero"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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
    int num1, num2, num3;
    scanf("%d", &num1);
    scanf("%d", &num2);
    scanf("%d", &num3);
    
    if (num1 > num2 && num1 > num3)
        printf("%d é o maior numero", num1);
    else if (num1 < num2 && num2 > num3)
        printf("%d\n é o maior numero", num2);
    else if (num3 > num1 && num3 > num2)
        printf("%d\n é o maior numero", num3);

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
  "source_sha256": "373f5217bdfb2798411cf0d076d8229f899ff48dd4835422cbc67350c23d2b42",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3\n é o maior numero"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6 é o maior numero"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3\n é o maior numero"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_051 — train

```c

#include<stdio.h>

int main (){

int a, b, c;

printf("Insira os 3 numeros pff\n");

scanf("%d%d%d", &a, &b, &c);

if (a>b && a>c){

    printf("O maior numero inserido é %d \n", a );
}

else if (b>a && b>c){

    printf("O maior numero inserido é%d \n", b );

}

else {

printf("O maior numero inserido é %d \n", c );

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
  "source_sha256": "662a032adedf799c576027d16b684d4d0b01f04d9fdcf4ef40c3bdfc8b22f073",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Insira os 3 numeros pff\nO maior numero inserido é 3 \n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Insira os 3 numeros pff\nO maior numero inserido é 6 \n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Insira os 3 numeros pff\nO maior numero inserido é3 \n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_052 — train

```c

#include <stdio.h>

int main()
{
    int min;
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    min = a;
    if (b < min)
        min = b;
    if (c < min)
        min = c;
    printf("%d", min);
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
  "source_sha256": "04778f8200e9fa137439ecbb5d36538416aef37cccb946b4e4529b358ecbc3ec",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "1"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "1"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "-1"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_053 — train

```c

#include <stdio.h>

int main(){
    int num1_ex1, num2_ex1, num3_ex1 = 0;   
    scanf("%d%d%d",&num1_ex1,&num2_ex1,&num3_ex1);
    if (num1_ex1 > num2_ex1){
        if (num1_ex1 > num3_ex1){
            printf("O maior numero e: %d", num1_ex1);
        }
        else{
            printf("O maior numero e: %d", num3_ex1);
        }
    }
    else if (num2_ex1 > num1_ex1){
        if (num2_ex1 > num3_ex1){
            printf("O maior numero e: %d", num2_ex1);
        }
        else{
            printf("O maior numero e: %d", num3_ex1);
        }
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
  "source_sha256": "f4438570b0140b7033d4dfa4f45a61209c6525516f549911fc7e4cac77de246d",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "O maior numero e: 3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "O maior numero e: 6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "O maior numero e: 3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_054 — validation

```c

#include <stdio.h>


int main()
{
    int num1;
    int num2;
    int num3;
    scanf("%d, %d, %d",&num1, &num2, &num3);
    if (num1>num2 && num1>num3)
    {
        printf("%d", num1);
    }
    if (num2>num1 && num2>num3)
    {
        printf("%d", num2);
    }
    if (num3>num2 && num1<num3)
    {
        printf("%d", num3);
    }
    return 0;
} 


```

```json
{
  "sample_id": "sample_054",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "0acfda9f71bf4c9c05aeba20113ca86ff3cd86a09f64d03002b65f515409b888",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "32766"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "32766"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "32766"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_055 — validation

```c

#include <stdio.h>


int main()
{
    int num1;
    int num2;
    int num3;
    scanf("%d, %d, %d",&num1, &num2, &num3);
    if (num1>num2 && num1>num3)
    {
        printf("%d", num1);
    }
    if (num2>num1 && num2>num3)
    {
        printf("%d", num2);
    }
    if (num3>num2 && num1<num3)
    {
        printf("%d", num3);
    }
    return 0;
} 

```

```json
{
  "sample_id": "sample_055",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "44b3eabfce22f0a0ae547453ed7a37da4e370c6f5014d46d93d7732a0bf66578",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "32764"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "32765"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "32764"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_056 — train

```c


#include <stdio.h>

int main()
{
    int x, y, z, vm;

    printf("Introduz 3 números inteiros: \n");
    scanf("%d%d%d", &x, &y, &z);
    if ((x > y) && (x > z))
    {
        vm = x;
    }
    if ((y > x) && (y > z))
    {
        vm = y;
    }
    if ((z > x) && (z > y))
    {
        vm = z;
    }
    printf("O valor maior é %d\n", vm);
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
  "source_sha256": "029be46622cf66dae0f96a53984583578b79afcfc41f4704c8a9086ef6d88988",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduz 3 números inteiros: \nO valor maior é 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduz 3 números inteiros: \nO valor maior é 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduz 3 números inteiros: \nO valor maior é 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_057 — train

```c


#include <stdio.h>

int main()
{
    int x, y, z, vm;

    printf("Introduz 3 números inteiros: \n");
    scanf("%d%d%d", &x, &y, &z);
    if ((x > y) && (x > z))
    {
        vm = x;
    }
    if ((y > x) && (y > z))
    {
        vm = y;
    }
    if ((z > x) && (z > y))
    {
        vm = z;
    }
    printf("O valor maior é %d\n", vm);
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
  "source_sha256": "029be46622cf66dae0f96a53984583578b79afcfc41f4704c8a9086ef6d88988",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduz 3 números inteiros: \nO valor maior é 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduz 3 números inteiros: \nO valor maior é 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduz 3 números inteiros: \nO valor maior é 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_058 — train

```c


#include <stdio.h>

int main()
{
    int x, y, z, vm;

    printf("Introduz 3 números inteiros: \n");
    scanf("%d%d%d", &x, &y, &z);
    if ((x > y) && (x > z))
    {
        vm = x;
    }
    if ((y > x) && (y > z))
    {
        vm = y;
    }
    if ((z > x) && (z > y))
    {
        vm = z;
    }
    printf("O valor maior é %d\n", vm);
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
  "source_sha256": "66e843706da7888cd8a97964437a19d78ad57ff37e326e6f809c22c77d1620dd",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduz 3 números inteiros: \nO valor maior é 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduz 3 números inteiros: \nO valor maior é 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduz 3 números inteiros: \nO valor maior é 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_059 — train

```c


#include <stdio.h>

int main()
{
    int x, y, z, vm;

    printf("Introduz 3 números inteiros: \n");
    scanf("%d%d%d", &x, &y, &z);
    if ((x > y) && (x > z))
    {
        vm = x;
    }
    if ((y > x) && (y > z))
    {
        vm = y;
    }
    if ((z > x) && (z > y))
    {
        vm = z;
    }
    printf("%d\n", vm);
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
  "source_sha256": "f193acd1406a5cb1cce64ef87806b3038031143aafc877c00e5ee550f486be51",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduz 3 números inteiros: \n3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduz 3 números inteiros: \n6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduz 3 números inteiros: \n3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_060 — train

```c


#include <stdio.h>

int main()
{
    int x, y, z, vm;

    printf("Introduz 3 números inteiros: \n");
    scanf("%d%d%d", &x, &y, &z);
    if ((x > y) && (x > z))
    {
        vm = x;
    }
    if ((y > x) && (y > z))
    {
        vm = y;
    }
    if ((z > x) && (z > y))
    {
        vm = z;
    }
    printf("O valor maior é %d\n", vm);
    return 0;
}
```

```json
{
  "sample_id": "sample_060",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "66e843706da7888cd8a97964437a19d78ad57ff37e326e6f809c22c77d1620dd",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduz 3 números inteiros: \nO valor maior é 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduz 3 números inteiros: \nO valor maior é 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduz 3 números inteiros: \nO valor maior é 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_061 — train

```c


#include <stdio.h>

int main()
{
    int input = 0;
    int output = 0;
    int i = 0;

    scanf("%d", &input);
    output = input;

    while(i<2){
        scanf("%d", &input);
        if(input < output)
            output = input;

        i++;
    }

    printf("%d", output);

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
  "source_sha256": "bc4a1c50864e3bf7acb1016a16d032bb3e1cb233be6502a6070f6f947eaad4e6",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "1"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "1"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "-1"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
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


## sample_062 — validation

```c

#include <stdio.h>

int main()
{
    int primeiro, segundo , terceiro;
    scanf("%d",&primeiro);
    scanf("%d",&segundo);
    scanf("%d",&terceiro);
    
    if (primeiro < segundo && primeiro < terceiro)
    {
        printf("%d",primeiro);
    }
    if (primeiro > segundo && segundo < terceiro)
    {
        printf("%d",segundo);
    }
    if (primeiro > terceiro && segundo > terceiro)
    {
        printf("%d",terceiro);
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_062",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "af185993df4db96da832e6186cf5d5b54f224f42e071cc863bfca7c2849188e2",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "1"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "1"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "-1"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_063 — train

```c


#include <stdio.h>


#define PASSO 1
#define INICIO 0
#define FIM 2

int main()
{
    int n_maior = INICIO, contador, lista[3];
    printf("Introduza três números inteiros:\n");
    for (contador = INICIO; contador <= FIM; contador = contador + PASSO)
        scanf("%d", &lista[contador]);
    for (contador = INICIO; contador <= FIM; contador = contador + PASSO)
    {
        if (lista[contador] > n_maior)
            n_maior = lista[contador];
    } 
    printf("%d\n", n_maior);
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
  "source_sha256": "2c5008aa33a593f571bfed7c4623b42996f5906533fdd5836be72097971559cb",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza três números inteiros:\n3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza três números inteiros:\n6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza três números inteiros:\n3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_064 — train

```c


#include <stdio.h>

#define PASSO 1
#define INICIO 0
#define FIM 2

int main()
{
    int n_maior = INICIO, contador, lista[3];
    printf("Introduza três números inteiros:\n");
    for (contador = INICIO; contador <= FIM; contador = contador + PASSO)
        scanf("%d", &lista[contador]);
    for (contador = INICIO; contador <= FIM; contador = contador + PASSO)
    {
        if (lista[contador] > n_maior)
            n_maior = lista[contador];
    } 
    printf("%d\n", n_maior);
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
  "source_sha256": "7a657f7eb1060d4f8a7498784360322221833a2f2824302b4afca246437d493c",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza três números inteiros:\n3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza três números inteiros:\n6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza três números inteiros:\n3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_065 — train

```c


#include <stdio.h>



#define PASSO 1
#define INICIO 0
#define FIM 2

int main()
{
    int n_maior = INICIO, contador, lista[3];
    printf("Introduza três números inteiros:\n");
    for (contador = INICIO; contador <= FIM; contador = contador + PASSO)
        scanf("%d", &lista[contador]);
    for (contador = INICIO; contador <= FIM; contador = contador + PASSO)
    {
        if (lista[contador] > n_maior)
            n_maior = lista[contador];
    } 
    printf("%d\n", n_maior);
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
  "source_sha256": "1cde0411c6b1d67469d99c383a7e54e1043a2ffc63d3be8f50914a01bf6abfb9",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza três números inteiros:\n3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza três números inteiros:\n6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza três números inteiros:\n3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_066 — train

```c

#include <stdio.h>
int main() {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    if (a>b && a>c) {
        printf("O maior numero: %d", a);
    }
    if (b>a && b>c){
        printf("o maior numero: %d", b);
    }
    if (c>a && c>b){
        printf("o maior numero: %d", c);
    }
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
  "source_sha256": "7a1a91bd0d474de8d266ab2bb8f4fc22ebc4ec9d2d6f1f33071902a1b881a18b",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "o maior numero: 3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "O maior numero: 6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "o maior numero: 3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_067 — train

```c

#include <stdio.h>

int biggest(int num1, int num2, int num3) {
    if ((num1 > num2) && (num1 > num3)) {
        return num1;
    }
    else if ((num2 > num1) && (num2 > num3)) {
        return num2;
    }
    else {
        return num3;
    }
}

int main() {
    int num1, num2, num3;
  
    printf("Num:");
    scanf("%d %d %d", &num1,&num2,&num3);

    printf("%d", biggest(num1, num2, num3));
  
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
  "source_sha256": "aa1116792acbce7b8b046b6b474f21968d8eb3b70082263fd138d5b1fd317c79",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Num:3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Num:6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Num:3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_068 — train

```c

#include <stdio.h>

int biggest(int num1, int num2, int num3) {
    if ((num1 > num2) && (num1 > num3)) {
        return num1;
    }
    else if ((num2 > num1) && (num2 > num3)) {
        return num2;
    }
    else {
        return num3;
    }
}

int main() {
    int num1, num2, num3;
  
    printf(" ");
    scanf("%d %d %d", &num1,&num2,&num3);

    printf("%d", biggest(num1, num2, num3));
  
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
  "source_sha256": "15dcd245c5db4b0a1b0ca47dbc84631d601fcb2548abdc88655c960c4c416109",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": " 3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": " 6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": " 3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_069 — train

```c

#include <stdio.h>

int biggest(int num1, int num2, int num3) {
    if ((num1 > num2) && (num1 > num3)) {
        return num1;
    }
    else if ((num2 > num1) && (num2 > num3)) {
        return num2;
    }
    else {
        return num3;
    }
}

int main() {
    int num1, num2, num3;
  
    printf("Numbers: ");
    scanf("%d,%d,%d", &num1,&num2,&num3);

    printf("%d", biggest(num1, num2, num3));
  
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
  "source_sha256": "3ebfaa0d496fc697e5c9f740f39ec5ddd15a7cf2cca6ff2f0c6ac8a6434ab7c5",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Numbers: 1"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Numbers: 6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Numbers: 0"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_070 — train

```c

#include <stdio.h>

int main()
{
    int n1, n2, n3;

    printf("Digite três números com o seguinte formato: n1 n2 n3\n");
    scanf("%d %d %d", &n1, &n2, &n3);

    if( n1 > n2 && n1 > n3)
    {
        printf("%d\n", n1);
    }
    else if( n2 > n3)
    {
        printf("%d\n", n2);
    }
    else
    {
        printf("%d\n",n3);
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
  "source_sha256": "960fc80e259f718d0a8f796eb1c5d66c036e316da6039d70ff2f9237d8421d11",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Digite três números com o seguinte formato: n1 n2 n3\n3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Digite três números com o seguinte formato: n1 n2 n3\n6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Digite três números com o seguinte formato: n1 n2 n3\n3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_071 — validation

```c

#include <stdio.h>

int main(){
    int x1, x2, x3;
    printf("Introduza 3 numeros inteiros:\n");
    scanf("%d%d%d", &x1, &x2, &x3);
    return printf("%d\n", x1>x2?(x1>x3?x1:x3):(x2>x3?x2:x3))==EOF;
}
```

```json
{
  "sample_id": "sample_071",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "4457216d99858a80c02c2a2c957728794a1463c08ada76881d6951986b09fc66",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza 3 numeros inteiros:\n3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza 3 numeros inteiros:\n6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza 3 numeros inteiros:\n3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_072 — validation

```c
#include <stdio.h>

int main() {
    
    int numUm, numDois, numTres;

    printf("Enter three numbers: ");
    scanf("%d", &numUm);
    scanf("%d", &numDois);
    scanf("%d", &numTres);

    if (numUm > numDois && numUm > numTres) {
        printf("Maximum number is: %d\n", numUm);
    } else if (numDois > numTres) {
        printf("Maximum number is: %d\n", numDois);
    } else {
        printf("Maximum number is: %d\n", numTres);
    }

    return 0;
}

```

```json
{
  "sample_id": "sample_072",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "acb68b03365dfbbc340adc743cda1d8aafa8a7928b305163f9a4cfebd233518f",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Enter three numbers: Maximum number is: 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Enter three numbers: Maximum number is: 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Enter three numbers: Maximum number is: 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_073 — validation

```c
#include <stdio.h>

int main() {
    
    int numUm, numDois, numTres;

    printf("Enter three numbers: ");
    scanf("%d", &numUm);
    scanf("%d", &numDois);
    scanf("%d", &numTres);

    if (numUm > numDois && numUm > numTres) {
        printf("%d", numUm);
    } else if (numDois > numTres) {
        printf("%d", numDois);
    } else {
        printf("%d", numTres);
    }

    return 0;
}

```

```json
{
  "sample_id": "sample_073",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "a3a525470a7152bfa1af9cdc4f6670e05d58a115d1b369a7013cbe0319cd65d4",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Enter three numbers: 3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Enter three numbers: 6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Enter three numbers: 3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_074 — validation

```c

#include <stdio.h>

int main() {
    int num1, num2, num3;

    printf("Insere tres numeros inteiros:");
    scanf("%d %d %d", &num1, &num2, &num3);

    if (num1 >= num2 && num1 >= num3)
        printf("%d\n", num1);
    else if (num2 >= num1 && num2 >= num3)
        printf("%d\n", num2);
    else
        printf("%d\n", num3);

    return 0;
}
```

```json
{
  "sample_id": "sample_074",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "4e6030af9a2817226a60ca342aa91ef9a4bc95fef716bf00ff1bef6dba0fc01a",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Insere tres numeros inteiros:3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Insere tres numeros inteiros:6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Insere tres numeros inteiros:3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_075 — validation

```c

#include <stdio.h>



int main()
{
    int num1, num2, num3;

    printf("Insert three diferent numbers.");
    scanf("%d", &num1);
    scanf("%d", &num2);
    scanf("%d", &num3);
    if (num1>num2)
    {
        if (num1>num3)
        {
            printf("%d is the biggest", num1);
        }
        else
        {
            printf("%d is the biggest", num3); 
        }
    }
    else
    {
        if (num2>num3)
        {
            printf("%d is the biggest", num2);
        }
        else
        {
            printf("%d is the biggest", num3); 
        }
    }

    return 0;
}
```

```json
{
  "sample_id": "sample_075",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "0c5d187dc2fa9266b45c0589eec46ca6453abee080d8050f0b023a3e00e4f46f",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Insert three diferent numbers.3 is the biggest"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Insert three diferent numbers.6 is the biggest"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Insert three diferent numbers.3 is the biggest"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_076 — validation

```c

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

int main(){
    int num1, num2, num3, max;
    printf("Introduza 3 numeros: ");
    scanf("%d %d %d", &num1, &num2, &num3);

    max = num1;
    if(num2 > max){
        max = num2;
    }
    if (num3 > max){
        max = num3;
    }
    printf("%d\n", max);
    return 0;
}
```

```json
{
  "sample_id": "sample_076",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "12a8f1b24f13baae9ac558f4f4b99d28f2d9b1916c040293aebbcd19f28da5d6",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza 3 numeros: 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza 3 numeros: 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza 3 numeros: 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_077 — train

```c

#include <stdio.h>

int main() {
    int n_1, n_2, n_3, foo;

    printf("Input: ");

    scanf("%d %d %d", &n_1, &n_2, &n_3);
    
    foo = n_1 > n_2 ? n_1 : n_2;
    foo = foo > n_3 ? foo : n_3;

    printf("%d\n", foo);

    return 0;

}    
```

```json
{
  "sample_id": "sample_077",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "f233e1f2fd5b0240d7227f61697c539b38003ecb45f9785d5e3852e8199532dc",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Input: 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Input: 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Input: 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_078 — train

```c

#include <stdio.h>

int num1, num2, num3, num_maior;

int main() { 
    scanf("%d%d%d", &num1, &num2, &num3);

    if (num1 >= num2) 
        num_maior = num1;
    
    else 
        num_maior = num2;
    
    if (num3 >= num_maior) 
        num_maior = num3;

    printf("%d.", num_maior);
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
  "source_sha256": "ca2f9b448009e10eab39195237c4b23533c87e68599e05cc59ad0304828634b4",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3."
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6."
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3."
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_079 — train

```c

#include <stdio.h>

int main()
{
    int n_1, n_2, n_3;

    scanf("%d %d %d", &n_1, &n_2, &n_3);

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
  "source_sha256": "864f559566f92fb46e8b0bfbe5ed4c9ed4c5e6844909e91bc1118660bf3820a8",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": ""
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": ""
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex01_0:relation": "empty",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "empty",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "empty",
    "stdout:ex01_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_080 — validation

```c


#include <stdio.h>

int main() {
    int x, y, z;
    printf("Hello\n");
    scanf("%d %d %d", &x, &y, &z);
    if (x > y && x > z) {
        printf("%d", x);
    }
    else if (y > x && y > z) {
        printf("%d", y);
    }
    else {
        printf("%d", z);
    }
    
    return 0;
}






```

```json
{
  "sample_id": "sample_080",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "dd233ad061464ef5fec3f303d2b296c4296c118c4f52be869a379e03f7327344",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Hello\n3"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Hello\n6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Hello\n3"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_081 — train

```c


#include <stdio.h>

int main() {
    int maior, numero, contador = 0;

    scanf("%d", &maior);

    while (contador < 2) {
        if (numero > maior)
            maior = numero;      
        ++contador;
        scanf("%d", &numero);
    }

    printf("O maior número é %d.\n", maior);
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
  "source_sha256": "6bb97b2aa4d427f488cfc0bad1bdd6ee23625ca85b5909fc68a0a4607c193e48",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "O maior número é 2.\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "O maior número é 6.\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "O maior número é 3.\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
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


## sample_082 — train

```c

#include <stdio.h>

int main()
{
    int a, b;
    scanf("%d%d", &a, &b);

    if (a > b) {
        printf("%d\n%d\n", b, a);
    }
    else {
        printf("%d\n%d\n", a, b);
    }
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
  "source_sha256": "d5a8bc3866d9748be998795f6b38772cacdf3d6525b8fd7daba8a9ef01967086",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "1\n2\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "2\n6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "-1\n3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
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


## sample_083 — train

```c

#include <stdio.h>

int main(){
    int maior,n1,n2,n3;
    scanf("%d,%d,%d",&n1,&n2,&n3);
    if (n2>n1){
        maior=n2;
    }
    if (n3>n2){
        maior=n3;
    }       
    printf("%d\n",maior);
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
  "source_sha256": "47c3bbe13a00ab0a5f83b84838abecc895e9ddd32e7aad1d57bd90930405467b",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "0\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "0\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "0\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_084 — train

```c

#include <stdio.h>

int main() {
    int a, b, c;
    scanf("%d%d%d/n", &a, &b, &c);
    if (a>b) {
        (c>=a) ? (printf("%d/n", c)) : printf("%d/n", a);
    } else {
        (c>=b) ? (printf("%d/n", c)) : printf("%d/n", b);
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
  "source_sha256": "cc31990fd564e80032bdbba62b9b9a91fc7af829845b31d18c77d4f3e3d1166f",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "3/n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6/n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "3/n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_085 — train

```c


#include <stdio.h>

int main() {
	int a, b, c;

	printf("Diga 3 numeros: ");
	scanf("%d %d %d",&a, &b, &c);

	if (a > b && a > c) {
		printf("O maior numero e:%d\n",a);
	} else if (b > a && b > c) {
		printf("O maior numero e:%d\n",b);
	} else {
		printf("O maior numero e:%d\n",c);
	}
	return 0;
}
```

```json
{
  "sample_id": "sample_085",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "b22aa72273b0520db5ffc4c40443a7a0bb45574edb33f66361936d7a20148e8f",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Diga 3 numeros: O maior numero e:3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Diga 3 numeros: O maior numero e:6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Diga 3 numeros: O maior numero e:3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_086 — validation

```c


#include <stdio.h>
int main() {
    int a, b, c;
    printf("Digite 3 números: ");
    if (scanf("%d %d %d", &a, &b, &c) != 3) return 1;
    printf("%d\n", (a > b && a > c) ? a : (b > c ? b : c));
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
  "source_sha256": "8cf8bc39a7171f144f45feb9359fc5de71bfa6de0ba5349a2d75c745bcafba87",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Digite 3 números: 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Digite 3 números: 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Digite 3 números: 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_088 — train

```c

#include <stdio.h>

#define QUANTIDADE 3

int main() {
    int value;
    int maior;
    int i;

    scanf("%d", &maior);

    i = 1;
    while (i < QUANTIDADE) {
        scanf("%d", &value);
        if (value > maior) {
            value = maior;
        }
        i++;
    } 

    printf("%d", maior);

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
  "source_sha256": "0f4f58792afa9baee2636808003f5b691206aee432d3d6c46658a7d6d31f2e45",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "1"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "6"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "-1"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "whitespace",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "different",
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


## sample_089 — train

```c

#include<stdio.h>

int a, b, c, maior;



int main () {
   
    scanf("%d %d %d", &a, &b, &c);

    if(a > b) b=a;
    if(b > c) c=b;
    if( a > c) c=a;

    printf("O maior número é: %d\n", c);
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
  "source_sha256": "3b03d389b52e0de85cbfbaf8f00a6c8dbdb0f7ff6440b8dd8c3f3e8bff377015",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "O maior número é: 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "O maior número é: 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "O maior número é: 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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


## sample_090 — train

```c

#include<stdio.h>

int a, b, c, maior;



int main () {
    printf("Introduza o primeiro número: ");
    scanf("%d", &a);        

    printf("Introduza o segundo número: ");
    scanf("%d", &b);

    printf("Introduza o terceiro número: ");
    scanf("%d", &c);

    maior = a;
    if (b > maior) {
        maior = b;
    }
    if (c > maior){
        maior = c;
    }

    printf("O maior número é: %d\n", maior);
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
  "source_sha256": "e6329d6de7751102f5fe70c89df8a1527bd4f51d8cb03d7a40f410972b946670",
  "outcomes": {
    "ex01_0": "fail",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_0",
      "input": "1 2 3",
      "expected": "3\n",
      "output": "Introduza o primeiro número: Introduza o segundo número: Introduza o terceiro número: O maior número é: 3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "6 2 1",
      "expected": "6\n",
      "output": "Introduza o primeiro número: Introduza o segundo número: Introduza o terceiro número: O maior número é: 6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "-1 3 1",
      "expected": "3\n",
      "output": "Introduza o primeiro número: Introduza o segundo número: Introduza o terceiro número: O maior número é: 3\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
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
  "members/sample_090/tests/ex01_2"
]
```
