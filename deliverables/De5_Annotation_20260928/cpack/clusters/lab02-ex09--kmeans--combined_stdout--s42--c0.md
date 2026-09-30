# lab02-ex09--kmeans--combined_stdout--s42--c0

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 57; phân vùng: {'train': 43, 'validation': 14}.


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
    "test_id": "ex09_0",
    "n_cluster": 57,
    "n_observed": 57,
    "n_failed": 57,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 57
    }
  },
  {
    "test_id": "ex09_3",
    "n_cluster": 57,
    "n_observed": 57,
    "n_failed": 57,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 57
    }
  },
  {
    "test_id": "ex09_1",
    "n_cluster": 57,
    "n_observed": 57,
    "n_failed": 55,
    "n_not_run": 0,
    "failure_rate_observed": 0.9649122807017544,
    "failure_rate_cluster": 0.9649122807017544,
    "outcome_counts": {
      "fail": 55,
      "pass": 2
    }
  },
  {
    "test_id": "ex09_2",
    "n_cluster": 57,
    "n_observed": 57,
    "n_failed": 54,
    "n_not_run": 0,
    "failure_rate_observed": 0.9473684210526315,
    "failure_rate_cluster": 0.9473684210526315,
    "outcome_counts": {
      "fail": 54,
      "pass": 3
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex09_0:relation",
    "value": "different",
    "n": 54,
    "n_cluster": 57,
    "rate": 0.9473684210526315,
    "cohort_rate": 0.5544554455445545,
    "difference_from_cohort": 0.392912975508077
  },
  {
    "feature": "stdout:ex09_1:relation",
    "value": "different",
    "n": 51,
    "n_cluster": 57,
    "rate": 0.8947368421052632,
    "cohort_rate": 0.5247524752475248,
    "difference_from_cohort": 0.3699843668577384
  },
  {
    "feature": "stdout:ex09_0:edit_band",
    "value": "medium",
    "n": 41,
    "n_cluster": 57,
    "rate": 0.7192982456140351,
    "cohort_rate": 0.40594059405940597,
    "difference_from_cohort": 0.31335765155462914
  },
  {
    "feature": "stdout:ex09_1:edit_band",
    "value": "medium",
    "n": 39,
    "n_cluster": 57,
    "rate": 0.6842105263157895,
    "cohort_rate": 0.38613861386138615,
    "difference_from_cohort": 0.29807191245440334
  },
  {
    "feature": "stdout:ex09_2:relation",
    "value": "different",
    "n": 50,
    "n_cluster": 57,
    "rate": 0.8771929824561403,
    "cohort_rate": 0.6039603960396039,
    "difference_from_cohort": 0.27323258641653636
  },
  {
    "feature": "stdout:ex09_3:relation",
    "value": "different",
    "n": 53,
    "n_cluster": 57,
    "rate": 0.9298245614035088,
    "cohort_rate": 0.7029702970297029,
    "difference_from_cohort": 0.22685426437380585
  },
  {
    "feature": "stdout:ex09_2:edit_band",
    "value": "medium",
    "n": 35,
    "n_cluster": 57,
    "rate": 0.6140350877192983,
    "cohort_rate": 0.43564356435643564,
    "difference_from_cohort": 0.17839152336286263
  },
  {
    "feature": "test:ex09_0",
    "value": "fail",
    "n": 57,
    "n_cluster": 57,
    "rate": 1.0,
    "cohort_rate": 0.8415841584158416,
    "difference_from_cohort": 0.15841584158415845
  },
  {
    "feature": "test:ex09_1",
    "value": "fail",
    "n": 55,
    "n_cluster": 57,
    "rate": 0.9649122807017544,
    "cohort_rate": 0.8217821782178217,
    "difference_from_cohort": 0.14313010248393265
  },
  {
    "feature": "stdout:ex09_3:edit_band",
    "value": "medium",
    "n": 38,
    "n_cluster": 57,
    "rate": 0.6666666666666666,
    "cohort_rate": 0.5346534653465347,
    "difference_from_cohort": 0.13201320132013195
  },
  {
    "feature": "stdout:ex09_2:edit_band",
    "value": "large",
    "n": 17,
    "n_cluster": 57,
    "rate": 0.2982456140350877,
    "cohort_rate": 0.16831683168316833,
    "difference_from_cohort": 0.12992878235191938
  },
  {
    "feature": "stdout:ex09_3:edit_band",
    "value": "large",
    "n": 17,
    "n_cluster": 57,
    "rate": 0.2982456140350877,
    "cohort_rate": 0.16831683168316833,
    "difference_from_cohort": 0.12992878235191938
  },
  {
    "feature": "ast:c_if",
    "value": "0",
    "n": 48,
    "n_cluster": 57,
    "rate": 0.8421052631578947,
    "cohort_rate": 0.7326732673267327,
    "difference_from_cohort": 0.10943199583116203
  },
  {
    "feature": "stdout:ex09_0:edit_band",
    "value": "large",
    "n": 14,
    "n_cluster": 57,
    "rate": 0.24561403508771928,
    "cohort_rate": 0.13861386138613863,
    "difference_from_cohort": 0.10700017370158066
  },
  {
    "feature": "stdout:ex09_1:edit_band",
    "value": "large",
    "n": 13,
    "n_cluster": 57,
    "rate": 0.22807017543859648,
    "cohort_rate": 0.12871287128712872,
    "difference_from_cohort": 0.09935730415146776
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "0",
    "n": 54,
    "n_cluster": 57,
    "rate": 0.9473684210526315,
    "cohort_rate": 0.8811881188118812,
    "difference_from_cohort": 0.06618030224075033
  },
  {
    "feature": "test:ex09_2",
    "value": "fail",
    "n": 54,
    "n_cluster": 57,
    "rate": 0.9473684210526315,
    "cohort_rate": 0.8910891089108911,
    "difference_from_cohort": 0.05627931214174042
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "0",
    "n": 48,
    "n_cluster": 57,
    "rate": 0.8421052631578947,
    "cohort_rate": 0.801980198019802,
    "difference_from_cohort": 0.040125065138092664
  },
  {
    "feature": "stdout:ex09_2:relation",
    "value": "empty",
    "n": 4,
    "n_cluster": 57,
    "rate": 0.07017543859649122,
    "cohort_rate": 0.039603960396039604,
    "difference_from_cohort": 0.03057147820045162
  },
  {
    "feature": "stdout:ex09_3:relation",
    "value": "empty",
    "n": 4,
    "n_cluster": 57,
    "rate": 0.07017543859649122,
    "cohort_rate": 0.039603960396039604,
    "difference_from_cohort": 0.03057147820045162
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 57,
    "n_cluster": 57,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 54,
    "n_cluster": 57,
    "rate": 0.9473684210526315,
    "cohort_rate": 0.9702970297029703,
    "difference_from_cohort": -0.022928608650338744
  }
]
```


## IF–THEN dự đoán cluster, không dự đoán gold

```json
[
  {
    "rule_id": 3,
    "if": [
      "NOT (stdout:ex09_0:edit_band=small)",
      "test:ex09_0=fail"
    ],
    "then_cluster": 0,
    "train_support": 42,
    "train_precision": 1.0,
    "holdout_support": 13,
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
  "reasoning": "Có 57 bài trong cụm. Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
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

sample_001, sample_056, sample_029, sample_004

## sample_001 — train — đại diện

```c
#include <stdio.h>

int main()
{
	int n, h, m, s;

	scanf("%d", &n);

	h = (n / 60 / 60) % 60;
	m = (n / 60) % 60;
	s = n % 60;

	printf("%d:%d:%d\n", h, m, s);

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
  "source_sha256": "21b2f228762dcd76f81809920dc0a79456a2762f9eaccf5d2525da6b8a76cd21",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:0:0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_004 — train — đại diện

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
	printf("%2d::%2d::%2d\n", horas, min, seg);
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
  "source_sha256": "9d3f2c77610601cbdf66f5ef0bd9c7cbb225192963013c8eee7eb4e93eb56e15",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": " 0:: 1:: 0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": " 0:: 2:: 0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": " 1:: 0:: 0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": " 1:: 6::40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_029 — validation — đại diện

```c

#include <stdio.h>

int main()
{
    int X, valor1, valor2,valor3;
    float seg = 0 , min = 0 , hora = 0 ;
    scanf("%d", &X);

    if (X < 60)
    {
        seg = X ;
        min = 0;
        hora = 0;
    }
    if (X >= 60)
    {
        valor1 = X % 60;
        valor2 = X / 60;
        if (valor1 == 0 && valor2 < 60)
        {
            seg = 0;
            min = valor2;
            hora = 0;
        }
        if (valor1 != 0)
        {
            seg = valor1;
        }
        if (valor2 >= 60)
        {
            valor3 = valor2 / 60;
            valor2 %= 60;
            if (valor2 == 0)
            {
                seg = 0;
                min = 0;
                hora = valor3;
            }
            if (valor2 != 0)
            {
                min = valor2;
                hora = -valor3 + valor2;
            }
        }
    }
    printf("%2.0f:%2.0f:%2.0f\n",hora,min,seg);
    return 0;
}
```

```json
{
  "sample_id": "sample_029",
  "partition": "validation",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "eb0bb423e0fcea7731f114959fa5c1224a9664cfb2218701337ed9dd614d1c3f",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": " 0: 1: 0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": " 0: 2: 0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": " 1: 0: 0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": " 5: 6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_056 — train — đại diện

```c

#include <stdio.h>
int main() {
    int N, min, seg, hor;
    scanf("%d",&N);
    if (N<60) {
        printf("00:00:%d\n",N);
        return 0;
    }
    else if (N>60 && N<3600) {
        min=N/60;
        seg=N-min*60;
        printf("00:0%d:0%d\n",min,seg);
        return 0;
    }
    else {
        hor=N/3600;
        min= N-hor*60;
        seg= N-min*60;
        printf("%d:%d:%d\n",hor,min,seg);
        return 0;
    }
}


   
```

```json
{
  "sample_id": "sample_056",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "2a4e4879bb3fac4f33f41b19020e4efd5063449ae8662731f858c24599d878bb",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "pass",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:60:-3540\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:3540:-208800\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:3940:-232400\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "pass",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "__unknown__",
    "stdout:ex09_1:edit_band": "__unknown__",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "large",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "pass",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_002 — train

```c
#include <stdio.h>

#define HORAEMSEG 3600
#define MINUTOEMSEG 60

int main()
{
	int n, s, h, m;
	scanf("%d", &n);
	h = n/HORAEMSEG;
	n %= HORAEMSEG;
	m = n/MINUTOEMSEG;
	s = n%MINUTOEMSEG;
	printf("%2d:%2d:%2d", h, m, s);
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
  "source_sha256": "675453ebcabd4a60645b9addb053021f7ad8838de806b307a912680db31e32d0",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": " 0: 1: 0"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": " 0: 2: 0"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": " 1: 0: 0"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": " 1: 6:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "large",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "large",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "large",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_003 — train

```c
#include <stdio.h>

int main() {
	int N, hrs, min;

	scanf("%d", &N);

	hrs = N / 360;
	N = N % 360;
	min = N / 60;
	N = N % 60;

	printf("%d:%d:%d\n", hrs, min, N);

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
  "source_sha256": "116fb058dc85dacbe1347c2f858928dc87d7b07a263317c5265fb6619bc0e192",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "10:0:0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "11:0:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_005 — train

```c
#include <stdio.h>

int main(){
	int n,horas,minutos,segundos;
	scanf("%d",&n);
	horas=n/3600;
	minutos=n/60 - horas*60;
	segundos=n%60;
	printf("%d:%d:%d\n",horas,minutos,segundos);
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
  "source_sha256": "42dff5c0210cc3a20fb9d29b8bd229769c0eb92dfeca22e3a4b6ff8c61bb994d",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:0:0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_006 — train

```c
#include <stdio.h>

int main(){
	
	int n, dias, horas, minutos;
	scanf("%d", &n);

	dias = n / (3600 * 24);
	n = n - dias * 3600 * 24;

	horas = n / 3600;
	n = n - horas * 3600;

	minutos = n / 60;
	n = n - minutos * 60;

	printf("%d %d %d\n", dias, horas, minutos );

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
  "source_sha256": "24bcda5ffd6459de2fd79704ed4bba72e5ceafe42c693773c321d3bb66609681",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0 0 1\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0 0 2\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "0 1 0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "0 1 6\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "large",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "large",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "large",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_007 — train

```c
#include <stdio.h>

int main(){
    int n, h, m, s;
    scanf("%d", &n);


    h = n / (60 * 60);
    n = n - h*(60 * 60);

    m = n / 60;
    n = n - m*60;

    s = n;
    
    printf("%d:%d:%d", h, m ,s);

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
  "source_sha256": "13791e442d10f98261ad45c8e1e1114254f6c222b2294097a910d0bc928a8232",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:0:0"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:6:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_008 — train

```c
#include <stdio.h>



#define segundos_hora 3600
#define segundos_minuto 60

int main() {

    int tempo, horas, minutos, segundos;

    scanf("%d", &tempo);
    horas = tempo / segundos_hora;
    tempo = tempo % segundos_hora;
    minutos = tempo / segundos_minuto;
    segundos = tempo % segundos_minuto;
    printf("%2d:%2d:%2d\n", horas, minutos, segundos);
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
  "source_sha256": "a54b460d4a4318c98f11544b38fb85e894c6c20dcb9c240eb0ff07ad80cbc983",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": " 0: 1: 0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": " 0: 2: 0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": " 1: 0: 0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": " 1: 6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_009 — train

```c
#include <stdio.h>

#define UMA_HORA_EM_SEG 3600
#define UMA_HORA_EM_MIN 60

int main()
{
  int N;
  int horas, minutos, segundos;
  float h1, h2, m1, m2, s1, s2;

  scanf("%d", &N);

  horas = (N / UMA_HORA_EM_SEG);
  minutos = ((N % UMA_HORA_EM_SEG) / UMA_HORA_EM_MIN);
  segundos = ((N % UMA_HORA_EM_SEG) % UMA_HORA_EM_MIN);

  h1 = (horas - (horas % 10)) / 10;
  h2 = horas % 10;
  m1 = (minutos - (minutos % 10)) / 10;
  m2 = minutos % 10;
  s1 = (segundos - (segundos % 10)) / 10;
  s2 = segundos % 10;

    printf("'%1.0f%1.0f:%1.0f%1.0f:%1.0f%1.0f'\n", h1, h2, m1, m2, s1, s2);
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
  "source_sha256": "9f1026292e4d2fc43bb47d8676ec2f5ea779a289963546cb9cebfb4de736e298",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "'00:01:00'\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "'00:02:00'\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "'01:00:00'\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "'01:06:40'\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_010 — train

```c
#include <stdio.h>

int main() {
    int n,h,m,s;
    scanf("%d", &n);
    h = n / 3600;
    n = n % 3600;
    m = n / 60;
    s = n % 60;
    printf("%d:%d:%d\n", h,m,s);
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
  "source_sha256": "924096d080ba0f6dc1dba8287d4a23d6b1d3cfa4da5086bc33386098ad1b8cbf",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:0:0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_011 — train

```c
#include <stdio.h>

int main ()
{
 int N,h,m,s;
 scanf ("%d",&N);
 h = N/1440;
 N = N - h*1440;
 m = N/60;
 N = N - m*60;
 s = N;
 
 printf ("%d:%d:%d\n",h,m,s);
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
  "source_sha256": "3b5f8bd1aa3406b20204fcb4bfbf6f4c91a4cc9db4d0819cc86868b82cb1bc44",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "2:12:0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "2:18:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "large",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_012 — train

```c
#include <stdio.h>

int main()
{	int t, h, m, s;
	scanf("%d\n", &t);
	s = t % 60;
	t = (t - s) / 60;
	m = t % 60;
	t = (t - m) / 60;
	h = t % 60;
	printf("%2d:%2d:%2d\n",h,m,s);
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
  "source_sha256": "bc57274ec89196d106f2d404c454897b0f8eb7b0c54201e8cf41b29023515a28",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": " 0: 1: 0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": " 0: 2: 0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": " 1: 0: 0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": " 1: 6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_013 — train

```c
#include <stdio.h>

int main(){
    int n, horas, mins, segs;
    scanf("%d", &n);
    horas = n / 3600;
    n %= 3600;
    mins = n /60;
    segs = n % 60;
    printf("%d:%d:%d\n", horas, mins, segs);
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
  "source_sha256": "078e09c1cf7e4f8086962c45a680b1b556dd221f438f7ae24f7ffdf060b1c880",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:0:0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_014 — train

```c
#include <stdio.h>

int N, horas, minutos, segundos;
int resto_h, resto_m;

int main(){

    scanf("%d", &N);

    horas = N / 3600;
    resto_h = N % 3600;
    minutos = resto_h / 60;
    resto_m = resto_h % 60;
    segundos = resto_m;

    printf("%d:%d:%d\n", horas, minutos, segundos);

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
  "source_sha256": "67279a1f36a985b54850a39f0f0c28354892fb9973bab8aa9ad9a8fccbea9efe",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:0:0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_015 — train

```c
#include <stdio.h>

#define SECSINHOUR 3600
#define SECSINMIN 60



int main() {
  int time, hours, minutes, seconds;

  scanf("%d", &time);

  hours = time / SECSINHOUR;
  time %= SECSINHOUR;
  minutes = time / SECSINMIN;
  seconds = time % SECSINMIN;

  printf("%d:%d:%d\n", hours, minutes, seconds);

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
  "source_sha256": "01e9d12ac063d0f77bc4fda540e8d031784f6909c40fe1ab11b68e327e672b6e",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:0:0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_016 — train

```c
#include <stdio.h>

int main() {
    
    int tempo, segundos, minutos, horas;

    printf("Insira tempo em segundos: ");
    

    scanf("%d", &tempo);

    horas = tempo / 3600;
    minutos = tempo % 3600 / 60;
    segundos = tempo % 3600 % 60;

    printf("%02d:%02d:%02d\n", horas, minutos, segundos);

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
  "source_sha256": "42afb66fa634a25d279a32db8c343f1da25ee7e8cc57dd5ddd71dc74ed19c2e3",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "Insira tempo em segundos: 00:01:00\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "Insira tempo em segundos: 00:02:00\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "Insira tempo em segundos: 01:00:00\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "Insira tempo em segundos: 01:06:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "large",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "large",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "large",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_017 — train

```c

#include<stdio.h>
int main(){
    int n, segundos, minutos, horas;
    scanf("%d",&n);
     
    
    horas = n/3600;
    minutos = (n-horas*3600)/60;
    segundos = (n-horas*3600-minutos*60);

    printf("%d:%d:%d\n", horas, minutos, segundos);
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
  "source_sha256": "937ff9086812b9aa860c4b4317fdf5912ae445ab491ed11feb4abe0a837da759",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:0:0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_018 — train

```c

#include<stdio.h>
int main(){
    int n, segundos, minutos, horas;
    scanf("%d",&n);
    horas = n/3600;
    minutos = (n%3600)/60;
    segundos = n%60;

    printf("%d:%d:%d\n", horas, minutos, segundos);
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
  "source_sha256": "d24bb8b2943625d6b586d9e98581413c0f08649c15d84ca29c658b6977a803ca",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:0:0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_019 — train

```c

#include <stdio.h>

int main () {
    int N;
    int HH = 0,MM = 0,SS = 0;
    scanf("%d",&N);
    SS = N;
    if (N < 60){
    printf("%d:%d:%d\n",HH,MM,SS);
    }
    else{
        MM = SS / 60;
        SS = SS % 60;
        if (MM < 60){
            printf("%d:%d:%d\n",HH,MM,SS);
        }
        else{
            HH = MM / 60;
            MM = MM % 60;
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
  "source_sha256": "deddb0fceab6ff39f53997400863442537f8cecab0ee2874997f00d4616039cd",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": ""
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "empty",
    "stdout:ex09_2:edit_band": "large",
    "stdout:ex09_3:relation": "empty",
    "stdout:ex09_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_020 — validation

```c


#include <stdio.h>

int main() {
	int s, m, h;
	scanf("%d", &s);
	if (s < 0) return 1;
	h =  s / 3600;
	s %= 3600;
	m = s / 60;
	s %= 60;
	printf("%02d : %02d : %02d\n", h, m, s);
	return 0;
}
```

```json
{
  "sample_id": "sample_020",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "e16ef16d1c80d8602e72b5bcbcda3c464d26b70e3ebe597f02c86e0255a2d77a",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00 : 01 : 00\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00 : 02 : 00\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01 : 00 : 00\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01 : 06 : 40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_021 — validation

```c



#include <stdio.h>

int main() {
	int s, m, h;
	scanf("%d", &s);
	if (s < 0) return 1;
	h =  s / 3600;
	s %= 3600;
	m = s / 60;
	s %= 60;
	printf("%02d : %02d : %02d\n", h, m, s);
	return 0;
}
```

```json
{
  "sample_id": "sample_021",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "d463d1f2187fe322a36aa54bf21a7e4909ce132de9d18ea2b3a5fb3861e94a18",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00 : 01 : 00\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00 : 02 : 00\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01 : 00 : 00\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01 : 06 : 40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_022 — validation

```c


#include <stdio.h>

int main(){
    int N, horas, minutos, segundos;

    scanf("%d", &N);
    horas = N/3600;
    N -= (horas*3600);
    minutos = N/60;
    N -= (minutos*60);
    segundos = N;
    printf("%d:%d:%d\n", horas, minutos, segundos);
    return 0;
}
```

```json
{
  "sample_id": "sample_022",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "c31d0eab22adb4fbb463e165ded002ffbe93b92f4c291f1e74e0f0c217caff85",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:0:0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_023 — validation

```c


#include <stdio.h>

int main(){
    int N, horas, minutos, segundos;

    scanf("%d", &N);
    horas = N/3600;
    N -= (horas*3600);
    minutos = N/60;
    N -= (minutos*60);
    segundos = N;
    printf("%d:%d:%d\n", horas, minutos, segundos);
    
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
  "source_sha256": "21ea84b89828f43a8518477ae586c99bfee37196e9d0847b2fe2ff13733c7959",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:0:0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_024 — validation

```c


#include <stdio.h>

int main(){
    int N, horas, minutos, segundos;

    scanf("%d", &N);
    horas = N/3600;
    N -= (horas*3600);
    minutos = N/60;
    N -= (minutos*60);
    segundos = N;
    printf("%d:%d:%d\n", horas, minutos, segundos);
    
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
  "source_sha256": "21ea84b89828f43a8518477ae586c99bfee37196e9d0847b2fe2ff13733c7959",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:0:0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_025 — validation

```c


#include <stdio.h>

int main(){
    int N, horas, minutos, segundos;

    scanf("%d", &N);
    horas = N/3600;
    N -= (horas*3600);
    minutos = N/60;
    N -= (minutos*60);
    segundos = N;
    printf("%d:%d:%d\n", horas, minutos, segundos);
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
  "source_sha256": "c31d0eab22adb4fbb463e165ded002ffbe93b92f4c291f1e74e0f0c217caff85",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:0:0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_026 — train

```c


#include <stdio.h>

#define HORASEMSEG 3600
#define MINEMSEG 60

int main()
{
int sintro, h, m, s;

scanf("%d", &sintro);
    h = (sintro/HORASEMSEG);
    m = ((sintro%HORASEMSEG)/MINEMSEG);
    s = (sintro%MINEMSEG);
printf("%2d:%2d:%2d\n", h, m, s);
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
  "source_sha256": "ae22349e7f0050ab5e31975d1b46c25e2efe5f8c2e8b4f61c8aba0fdda6434bf",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": " 0: 1: 0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": " 0: 2: 0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": " 1: 0: 0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": " 1: 6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_027 — train

```c


#include <stdio.h>

#define HORASEMSEG 3600
#define MINEMSEG 60

int main()
{
int sintro, h, m, s;

scanf("%d", &sintro);
    h = (sintro/HORASEMSEG);
    m = ((sintro%HORASEMSEG)/MINEMSEG);
    s = (sintro%MINEMSEG);
    printf("%2d:%2d:%2d\n", h, m, s);
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
  "source_sha256": "732c4d470588b5e42023c4db3f04ef81f520dff8bbd2fb80a64acb27f52aee95",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": " 0: 1: 0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": " 0: 2: 0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": " 1: 0: 0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": " 1: 6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_028 — validation

```c

#include <stdio.h>

int main()
{
    int X, valor1, valor2,valor3;
    float seg = 0 , min = 0 , hora = 0 ;
    scanf("%d", &X);

    if (X % 60 != 0)
    {
        seg = X % 60;
    }
    valor1 = (X - seg);
    if (valor1 %60 != 0)
    {
        min = valor1 % 60;
    }
    else if (valor1 %60 == 0)
    {   
        valor3 = valor1;
        valor3 /= 60;
        if (valor3 < 60)
        {
            min = valor3;
        }
        else
        {
            min = valor3 -60;
        }
    }
    valor2 = valor1 % 3600;
    if (valor2 == 0)
    {
        hora = valor1 / 3600;
    }

    printf("%2.0f:%2.0f:%2.0f\n",hora,min,seg);
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
  "source_sha256": "a3c05f21a2393e02cda3fca4d9c837df1b03e9e464ba8760c888561867290f49",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": " 0: 1: 0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": " 0: 2: 0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": " 1: 0: 0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": " 0: 6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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

int main(){

    int n, remainder;
    int hh = 0;
    int mm = 0;
    int ss = 0;

    scanf("%d", &n);

    if((n / 3600) > 1){
        hh = n / 3600;
        remainder = n % 3600;
    }
    else
        remainder = n;
    if((remainder / 60) > 1){
        mm = remainder / 60;
        remainder %= 60;
    }
    else
        ss = remainder / 60;
    
    printf("%02d:%02d:%02d", hh, mm, ss);

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
  "source_sha256": "ef5b70b7045f0b06888a36d1d6bf055b513ca50ac3fa7919f6518622c1a3fb4c",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:00:01"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "00:60:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "00:66:00"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "large",
    "stdout:ex09_1:relation": "whitespace",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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

int main () {

    int v;
    int horas, min, seg, resto;

    scanf("%d", &v);

    horas = v / 3600;
    resto = v % 3600;
    min = resto / 60;
    seg = resto % 60;
    
    printf("%2d:%2d:%2d\n", horas, min, seg);
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
  "source_sha256": "9bbc0cd21ef5f10b2678dbcd1a79df39d6b30dc84eefc291892a8ddf4f11fb44",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": " 0: 1: 0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": " 0: 2: 0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": " 1: 0: 0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": " 1: 6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_032 — train

```c

#include <stdio.h>
#define MIN 60;
#define HORA 3600;
int main(){
    int N, s, h=0, m=0, resto_m;
    printf("Indroduza tempo em segundos:  ");
    scanf("%d", &N);
    if (N >= 3600){
        h = N/HORA;
        resto_m = N%HORA;
        m = resto_m/MIN;
        s = resto_m%MIN;
    }
    if (N<3600 && N>=60){ 
        h = 0;
        m = N/MIN;
        s = N%MIN;   
    }
    if (N < 60){
        h = m = 0;
        s = N;
    }
    if (h <= 9){
        if (m <= 9){
            if (s <= 9){
                printf("0%d:0%d:0%d", h, m, s);}
            else
                printf("0%d:0%d:%d", h, m, s);
        }
        else {
            if (s <= 9){
                printf("0%d:%d:0%d", h, m, s);}
            else
                printf("0%d:%d:%d", h, m, s);
        }    
    }
    else {
        if (m <= 9){
            if (s <= 9){
                printf("%d:0%d:0%d", h, m, s);}
            else
                printf("%d:0%d:%d", h, m, s);
        }
        else {
            if (s <= 9){
                printf("%d:%d:0%d", h, m, s);}
            else
                printf("%d:%d:%d", h, m, s);
        }
    }
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
  "source_sha256": "8ae3e0ea154033dc4d64bb47d3a97d3f311cb642850c9aa574f7e213a426b5b7",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "Indroduza tempo em segundos:  00:01:00"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "Indroduza tempo em segundos:  00:02:00"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "Indroduza tempo em segundos:  01:00:00"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "Indroduza tempo em segundos:  01:06:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "large",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "large",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "large",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_033 — train

```c


#include <stdio.h>

int main(){
    
    int N, H, M, S;
    scanf("%d", &N);

    H = N/3600;
    M = (N % 3600)/60;
    S = N % 60;
    
    printf("%d:%d:%d\n", H, M, S);
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
  "source_sha256": "570b0596fbe0059ee7d6db8e43bad2d8b0d4e284f36fcbab2ad91a168e6e1adb",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:0:0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_034 — train

```c


#include <stdio.h>

int main(){
    int n,h,m,s;
    scanf("%d", &n);
    h = (n-n%3600)/3600;
    m = (n%3600-((n%3600)%60))/60;
    s = ((n%3600)%60);
    printf("%d:%d:%d",h,m,s);
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
  "source_sha256": "afd5c5d2b8ab5187d55278d1162746408ff577cd76ab08dc50a2f87a90e9ba80",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:0:0"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:6:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_035 — validation

```c

#include <stdio.h>

int main(){
    int N, horas, minutos, segundos;

    printf("Introduza o numero de segundos:\n");
    scanf("%d", &N);

    horas = N/3600;
    minutos = (N%3600)/60;
    segundos = (N%3600)%60;

    printf("%d:%d:%d\n", horas, minutos, segundos);
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
  "source_sha256": "d2eda8a9cb1a2193554a8eca7c225d44d7dc3acc07167eb4deb331092ecddac7",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "Introduza o numero de segundos:\n0:1:0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "Introduza o numero de segundos:\n0:2:0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "Introduza o numero de segundos:\n1:0:0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "Introduza o numero de segundos:\n1:6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "large",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "large",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "large",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_036 — validation

```c

#include <stdio.h>

int main(){
    int N, horas, minutos, segundos;

    scanf("%d", &N);
    horas = N/3600;
    minutos = (N%3600)/60;
    segundos = (N%3600)%60;

    printf("%d:%d:%d\n", horas, minutos, segundos);
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
  "source_sha256": "c507ec9cd7d3c15f1e665cfaf7e0d089797403296915314f255ff695e1ab2189",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:0:0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_037 — validation

```c

#include <stdio.h>

int main(){
    int N, horas, minutos, segundos;

    scanf("%d", &N);
    
    horas = N/3600;
    minutos = (N%3600)/60;
    segundos = (N%3600)%60;

    printf("%d:%d:%d\n", horas, minutos, segundos);
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
  "source_sha256": "1f8e6b2ecee1599c6b0500aa4f82d9e6dc77d1b473eba4df331ac4e80184da8c",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:0:0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_038 — train

```c

#include <stdio.h>

int main() {
    int segundos, horas, minutos, resto;

    
    printf("Digite um valor em segundos: ");
    scanf("%d", &segundos);

    
    horas = segundos / 3600;   
    resto = segundos % 3600;
    minutos = resto / 60;      
    segundos = resto % 60;

    
    printf("%02d:%02d:%02d\n", horas, minutos, segundos);

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
  "source_sha256": "cbca8c20f36a54c127f16fe567b5ee50cd72e57d7caa74fd0524ba213e46e79e",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "Digite um valor em segundos: 00:01:00\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "Digite um valor em segundos: 00:02:00\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "Digite um valor em segundos: 01:00:00\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "Digite um valor em segundos: 01:06:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "large",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "large",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "large",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_039 — validation

```c

#include <stdio.h>

int main() {
    int seconds;
    float test;
    float s;

    scanf("%d", &seconds);
    test = seconds / 60.0;  
    s = (test - (int)test) * 10;  
    printf("%f\n%f", test, s);

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
  "source_sha256": "b6d1014340cfa737ee3e7bc8a539970202a22a8d89b073f64640bdf7b538f50e",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "1.000000\n0.000000"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "2.000000\n0.000000"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "60.000000\n0.000000"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "66.666664\n6.666641"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "large",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "large",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "large",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_040 — validation

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
  "sample_id": "sample_040",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "f49c4fb585cc7b8c0a22f0fec550b668029b4e2884e7826195fe790fde87361c",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": ""
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": ""
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": ""
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "0",
    "stdout:ex09_0:relation": "empty",
    "stdout:ex09_0:edit_band": "large",
    "stdout:ex09_1:relation": "empty",
    "stdout:ex09_1:edit_band": "large",
    "stdout:ex09_2:relation": "empty",
    "stdout:ex09_2:edit_band": "large",
    "stdout:ex09_3:relation": "empty",
    "stdout:ex09_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_041 — train

```c

#include <stdio.h>


int main(){
    int N;
    int h;
    int m;
    int s;
    scanf("%d", &N);
    h = N/3600;
    m = (N - h*3600)/60;
    s = m%60;
    printf("%.2d:%.2d:%.2d\n", h, m, s);
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
  "source_sha256": "b726e41ef36c0ec4070aa29c561c82a5aa6a1c80416cbe488cc3c3ca30320a69",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "pass",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:01\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:02\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:06\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "pass",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "__unknown__",
    "stdout:ex09_2:edit_band": "__unknown__",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "pass",
    "test:ex09_3": "fail",
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


## sample_042 — train

```c

#include <stdio.h>


int main(){
    int N;
    int h;
    int m;
    int s;
    scanf("%d", &N);
    h = N/3600;
    m = (N % 3600)*60;
    s = m % 60;
    printf("%.2d:%.2d:%.2d\n", h, m, s);
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
  "source_sha256": "fc977f3a006b203f383e0aa663a23186c30249798a07152ec984a3a607528c3d",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "pass",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:3600:00\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:7200:00\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:24000:00\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "pass",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "__unknown__",
    "stdout:ex09_2:edit_band": "__unknown__",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "pass",
    "test:ex09_3": "fail",
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


## sample_043 — train

```c

#include <stdio.h>


int main(){
    int N;
    int h;
    int m;
    int s;
    scanf("%d", &N);
    h = N/3600;
    m = (N - h*3600)/60;
    s = m/60 + m%60;
    printf("%.2d:%.2d:%.2d\n", h, m, s);
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
  "source_sha256": "5a4e28fa5017903b325add07e6dd4ea7dafbf9e074e131f976d1ed8723cd449a",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "pass",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00:01:01\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00:02:02\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01:06:06\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "pass",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "__unknown__",
    "stdout:ex09_2:edit_band": "__unknown__",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "pass",
    "test:ex09_3": "fail",
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


## sample_044 — train

```c

#include <stdio.h>

int main() {


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
  "source_sha256": "a6ea5c087cfaad5e24511e662c0f9a09dc60076ab1f0b19686e9a52d7daa7527",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": ""
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": ""
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": ""
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "0",
    "stdout:ex09_0:relation": "empty",
    "stdout:ex09_0:edit_band": "large",
    "stdout:ex09_1:relation": "empty",
    "stdout:ex09_1:edit_band": "large",
    "stdout:ex09_2:relation": "empty",
    "stdout:ex09_2:edit_band": "large",
    "stdout:ex09_3:relation": "empty",
    "stdout:ex09_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_045 — train

```c

#include <stdio.h>

int main() {
    int segundos,horas,minutos;

    scanf("%d", &segundos);
    horas=segundos/3600;
    segundos-=horas*3600;
    minutos=segundos/60;
    segundos-=minutos*60;
    
    printf("%d:%d:%d\n",horas,minutos,segundos);
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
  "source_sha256": "e9f07f9e701ced6e938a4ef61b9429ab6c95840cc0de991945c90b9f9bbff402",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:0:0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_046 — train

```c


#include <stdio.h>

int main()
{
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
  "source_sha256": "1d9361f34946f91432aa4edf81c1371ae946c5ee3278f7145fbeb8c759b4abcd",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": ""
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": ""
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": ""
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "0",
    "stdout:ex09_0:relation": "empty",
    "stdout:ex09_0:edit_band": "large",
    "stdout:ex09_1:relation": "empty",
    "stdout:ex09_1:edit_band": "large",
    "stdout:ex09_2:relation": "empty",
    "stdout:ex09_2:edit_band": "large",
    "stdout:ex09_3:relation": "empty",
    "stdout:ex09_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_047 — train

```c

#include <stdio.h>

#define HORA_SEGUNDOS 3600
#define MINUTO_SEGUNDOS 60

int main() {
  int horas, minutos, segundos;
  int tempo;

  scanf("%d", &tempo);

  horas = tempo / HORA_SEGUNDOS;
  tempo %= HORA_SEGUNDOS;
  minutos = tempo / MINUTO_SEGUNDOS;
  segundos = tempo % MINUTO_SEGUNDOS;

  printf("%02d-%02d-%02d\n", horas, minutos, segundos);
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
  "source_sha256": "4267e478d57d4701e45f1fc6ac80ddb58d569ad14a11065cae521beaec4144fc",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "00-01-00\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "00-02-00\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "01-00-00\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "01-06-40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_048 — train

```c

#include <stdio.h>

int main(){
    int N, hora, minuto, segundo;
    scanf("%d", &N);
    minuto= N/60;
    hora = minuto/60;
    minuto -= hora*60;
    segundo = N - (minuto*60) - (hora*3600);
    printf("%d:%d:%d\n", hora, minuto, segundo);
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
  "source_sha256": "5bdf2bde76ad5965149f63ae2116e27f30e1e60d6f798a819ed73aab262b3dc5",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:0:0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_049 — train

```c

#include <stdio.h>

int main() {
    int segundos, horas, minutos, resto;
    scanf("%d", &resto);
    horas = resto / 3600;
    resto = resto % 3600;
    minutos = resto / 60;
    segundos = resto % 60;
    printf("%d:%d:%d", horas, minutos, segundos);
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
  "source_sha256": "2b9588b31906e75016809d7d13f6db35b6acc4c05fb8dff3814c19b7c241de29",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:1:0"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:2:0"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:0:0"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:6:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_050 — train

```c

#include <stdio.h>
int main(){
    int N, segundo, minuto, hora;
    scanf("%d", &N);
    hora = N / 3600;
    minuto = (N % 3600) / 60;
    segundo = (N % 3600) % 60;
    printf("%2d:%2d:%2d\n", hora, minuto, segundo);
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
  "source_sha256": "642e014a161056a4dc6895c17d02d443caf48c49b3eab0a62871111cc0ce2d71",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": " 0: 1: 0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": " 0: 2: 0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": " 1: 0: 0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": " 1: 6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_051 — train

```c

#include <stdio.h>
#define MINUTO 60
#define HORA 3600

int main() {
    int n;
    char horas, minutos, segundos;
    scanf("%d", &n );
    horas = n/HORA;
    n = n%HORA;
    minutos = n/MINUTO;
    n = n%MINUTO;
    segundos = n;
    printf("%2c:%2c:%2c\n", horas, minutos, segundos);
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
  "source_sha256": "40dc2c0adb7e07f3ee8387d3481727161988d41d883b77c8da03a16ec33effab",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": " \u0000: \u0001: \u0000\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": " \u0000: \u0002: \u0000\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": " \u0001: \u0000: \u0000\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": " \u0001: \u0006: (\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "large",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "large",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "large",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_052 — train

```c

#include <stdio.h>
#define MINUTO 60
#define HORA 3600

int main() {
    int n, horas, minutos, segundos;
    scanf("%d", &n );
    horas = n/HORA;
    n = n%HORA;
    minutos = n/MINUTO;
    n = n%MINUTO;
    segundos = n;
    printf("%2d:%2d:%2d", horas, minutos, segundos);
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
  "source_sha256": "f2a048e227cdd949df89000af6623544492b14e5a136860a03df66658a6a79c9",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": " 0: 1: 0"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": " 0: 2: 0"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": " 1: 0: 0"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": " 1: 6:40"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "large",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "large",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "large",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_053 — train

```c

#include <stdio.h>
#define MINUTO 60
#define HORA 3600

int main() {
    int n, horas, minutos, segundos;
    scanf("%d", &n );
    horas = n/HORA;
    n = n%HORA;
    minutos = n/MINUTO;
    n = n%MINUTO;
    segundos = n;
    printf("%2d:%2d:%2d\n", horas, minutos, segundos);
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
  "source_sha256": "b1b50a714c96bfeaf91ab32d265d783f879e6e92a0838ad87de50ea7ba764547",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": " 0: 1: 0\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": " 0: 2: 0\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": " 1: 0: 0\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": " 1: 6:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "medium",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "medium",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_054 — train

```c

#include <stdio.h>
#define MINUTO 60
#define HORA 3600

int main() {
    int n, horas, minutos, segundos;
    scanf("%d", &n );
    horas = n/HORA;
    n = n%HORA;
    minutos = n/MINUTO;
    n = n%MINUTO;
    segundos = n;
    printf("%2c:%2c:%2c\n", horas, minutos, segundos);
    return 0;
}
```

```json
{
  "sample_id": "sample_054",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "df8c2131d429ee93434a913273e07fad3c6dd75adcd5bce0ba3eb9d6e14ffbe6",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": " \u0000: \u0001: \u0000\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": " \u0000: \u0002: \u0000\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": " \u0001: \u0000: \u0000\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": " \u0001: \u0006: (\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "large",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "large",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "large",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_055 — validation

```c

#include <stdio.h>
#define UNIT 60

int main(){

    int seg;

    scanf("%d",&seg);

    printf("%d:%2.2d:%2.2d\n",seg/(UNIT*UNIT),(seg/UNIT)%UNIT,seg%UNIT);

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
  "source_sha256": "f0afe40bffc1616d70295fa2154846752eebb3bad951fe31f5c6c4ec1df3bf7a",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "fail",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:01:00\n"
    },
    {
      "test_id": "ex09_1",
      "input": "120",
      "expected": "00:02:00\n",
      "output": "0:02:00\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:00:00\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:06:40\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "small",
    "stdout:ex09_1:relation": "different",
    "stdout:ex09_1:edit_band": "small",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "small",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "fail",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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


## sample_057 — train

```c

#include <stdio.h>
int main() {
    int N, min, seg, hor;
    scanf("%d",&N);
    if (N<60) {
        printf("00:00:%d\n",N);
        return 0;
    }
    else if (N>60 && N<3600) {
        min=N/60;
        seg=N-min*60;
        printf("00:0%d:0%d\n",min,seg);
        return 0;
    }
    else {
        hor=N/3600;
        min= N-hor*60;
        seg= N-min*60;
        printf("%d:%d:%d\n",hor,min,seg);
        return 0;
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
  "source_sha256": "f4d7855395ee69cc330867b4c36118daed5629495900d6cb1838a700b3163ede",
  "outcomes": {
    "ex09_0": "fail",
    "ex09_1": "pass",
    "ex09_2": "fail",
    "ex09_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex09_0",
      "input": "60",
      "expected": "00:01:00\n",
      "output": "0:60:-3540\n"
    },
    {
      "test_id": "ex09_2",
      "input": "3600",
      "expected": "01:00:00\n",
      "output": "1:3540:-208800\n"
    },
    {
      "test_id": "ex09_3",
      "input": "4000",
      "expected": "01:06:40\n",
      "output": "1:3940:-232400\n"
    }
  ],
  "clustering_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "pass",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "stdout:ex09_0:relation": "different",
    "stdout:ex09_0:edit_band": "medium",
    "stdout:ex09_1:relation": "__unknown__",
    "stdout:ex09_1:edit_band": "__unknown__",
    "stdout:ex09_2:relation": "different",
    "stdout:ex09_2:edit_band": "large",
    "stdout:ex09_3:relation": "different",
    "stdout:ex09_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex09_0": "fail",
    "test:ex09_1": "pass",
    "test:ex09_2": "fail",
    "test:ex09_3": "fail",
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
  "members/sample_001/tests/ex09_0",
  "members/sample_001/tests/ex09_1",
  "members/sample_001/tests/ex09_2",
  "members/sample_001/tests/ex09_3",
  "members/sample_002/raw_code",
  "members/sample_002/tests/ex09_0",
  "members/sample_002/tests/ex09_1",
  "members/sample_002/tests/ex09_2",
  "members/sample_002/tests/ex09_3",
  "members/sample_003/raw_code",
  "members/sample_003/tests/ex09_0",
  "members/sample_003/tests/ex09_1",
  "members/sample_003/tests/ex09_2",
  "members/sample_003/tests/ex09_3",
  "members/sample_004/raw_code",
  "members/sample_004/tests/ex09_0",
  "members/sample_004/tests/ex09_1",
  "members/sample_004/tests/ex09_2",
  "members/sample_004/tests/ex09_3",
  "members/sample_005/raw_code",
  "members/sample_005/tests/ex09_0",
  "members/sample_005/tests/ex09_1",
  "members/sample_005/tests/ex09_2",
  "members/sample_005/tests/ex09_3",
  "members/sample_006/raw_code",
  "members/sample_006/tests/ex09_0",
  "members/sample_006/tests/ex09_1",
  "members/sample_006/tests/ex09_2",
  "members/sample_006/tests/ex09_3",
  "members/sample_007/raw_code",
  "members/sample_007/tests/ex09_0",
  "members/sample_007/tests/ex09_1",
  "members/sample_007/tests/ex09_2",
  "members/sample_007/tests/ex09_3",
  "members/sample_008/raw_code",
  "members/sample_008/tests/ex09_0",
  "members/sample_008/tests/ex09_1",
  "members/sample_008/tests/ex09_2",
  "members/sample_008/tests/ex09_3",
  "members/sample_009/raw_code",
  "members/sample_009/tests/ex09_0",
  "members/sample_009/tests/ex09_1",
  "members/sample_009/tests/ex09_2",
  "members/sample_009/tests/ex09_3",
  "members/sample_010/raw_code",
  "members/sample_010/tests/ex09_0",
  "members/sample_010/tests/ex09_1",
  "members/sample_010/tests/ex09_2",
  "members/sample_010/tests/ex09_3",
  "members/sample_011/raw_code",
  "members/sample_011/tests/ex09_0",
  "members/sample_011/tests/ex09_1",
  "members/sample_011/tests/ex09_2",
  "members/sample_011/tests/ex09_3",
  "members/sample_012/raw_code",
  "members/sample_012/tests/ex09_0",
  "members/sample_012/tests/ex09_1",
  "members/sample_012/tests/ex09_2",
  "members/sample_012/tests/ex09_3",
  "members/sample_013/raw_code",
  "members/sample_013/tests/ex09_0",
  "members/sample_013/tests/ex09_1",
  "members/sample_013/tests/ex09_2",
  "members/sample_013/tests/ex09_3",
  "members/sample_014/raw_code",
  "members/sample_014/tests/ex09_0",
  "members/sample_014/tests/ex09_1",
  "members/sample_014/tests/ex09_2",
  "members/sample_014/tests/ex09_3",
  "members/sample_015/raw_code",
  "members/sample_015/tests/ex09_0",
  "members/sample_015/tests/ex09_1",
  "members/sample_015/tests/ex09_2",
  "members/sample_015/tests/ex09_3",
  "members/sample_016/raw_code",
  "members/sample_016/tests/ex09_0",
  "members/sample_016/tests/ex09_1",
  "members/sample_016/tests/ex09_2",
  "members/sample_016/tests/ex09_3",
  "members/sample_017/raw_code",
  "members/sample_017/tests/ex09_0",
  "members/sample_017/tests/ex09_1",
  "members/sample_017/tests/ex09_2",
  "members/sample_017/tests/ex09_3",
  "members/sample_018/raw_code",
  "members/sample_018/tests/ex09_0",
  "members/sample_018/tests/ex09_1",
  "members/sample_018/tests/ex09_2",
  "members/sample_018/tests/ex09_3",
  "members/sample_019/raw_code",
  "members/sample_019/tests/ex09_0",
  "members/sample_019/tests/ex09_1",
  "members/sample_019/tests/ex09_2",
  "members/sample_019/tests/ex09_3",
  "members/sample_020/raw_code",
  "members/sample_020/tests/ex09_0",
  "members/sample_020/tests/ex09_1",
  "members/sample_020/tests/ex09_2",
  "members/sample_020/tests/ex09_3",
  "members/sample_021/raw_code",
  "members/sample_021/tests/ex09_0",
  "members/sample_021/tests/ex09_1",
  "members/sample_021/tests/ex09_2",
  "members/sample_021/tests/ex09_3",
  "members/sample_022/raw_code",
  "members/sample_022/tests/ex09_0",
  "members/sample_022/tests/ex09_1",
  "members/sample_022/tests/ex09_2",
  "members/sample_022/tests/ex09_3",
  "members/sample_023/raw_code",
  "members/sample_023/tests/ex09_0",
  "members/sample_023/tests/ex09_1",
  "members/sample_023/tests/ex09_2",
  "members/sample_023/tests/ex09_3",
  "members/sample_024/raw_code",
  "members/sample_024/tests/ex09_0",
  "members/sample_024/tests/ex09_1",
  "members/sample_024/tests/ex09_2",
  "members/sample_024/tests/ex09_3",
  "members/sample_025/raw_code",
  "members/sample_025/tests/ex09_0",
  "members/sample_025/tests/ex09_1",
  "members/sample_025/tests/ex09_2",
  "members/sample_025/tests/ex09_3",
  "members/sample_026/raw_code",
  "members/sample_026/tests/ex09_0",
  "members/sample_026/tests/ex09_1",
  "members/sample_026/tests/ex09_2",
  "members/sample_026/tests/ex09_3",
  "members/sample_027/raw_code",
  "members/sample_027/tests/ex09_0",
  "members/sample_027/tests/ex09_1",
  "members/sample_027/tests/ex09_2",
  "members/sample_027/tests/ex09_3",
  "members/sample_028/raw_code",
  "members/sample_028/tests/ex09_0",
  "members/sample_028/tests/ex09_1",
  "members/sample_028/tests/ex09_2",
  "members/sample_028/tests/ex09_3",
  "members/sample_029/raw_code",
  "members/sample_029/tests/ex09_0",
  "members/sample_029/tests/ex09_1",
  "members/sample_029/tests/ex09_2",
  "members/sample_029/tests/ex09_3",
  "members/sample_030/raw_code",
  "members/sample_030/tests/ex09_0",
  "members/sample_030/tests/ex09_1",
  "members/sample_030/tests/ex09_2",
  "members/sample_030/tests/ex09_3",
  "members/sample_031/raw_code",
  "members/sample_031/tests/ex09_0",
  "members/sample_031/tests/ex09_1",
  "members/sample_031/tests/ex09_2",
  "members/sample_031/tests/ex09_3",
  "members/sample_032/raw_code",
  "members/sample_032/tests/ex09_0",
  "members/sample_032/tests/ex09_1",
  "members/sample_032/tests/ex09_2",
  "members/sample_032/tests/ex09_3",
  "members/sample_033/raw_code",
  "members/sample_033/tests/ex09_0",
  "members/sample_033/tests/ex09_1",
  "members/sample_033/tests/ex09_2",
  "members/sample_033/tests/ex09_3",
  "members/sample_034/raw_code",
  "members/sample_034/tests/ex09_0",
  "members/sample_034/tests/ex09_1",
  "members/sample_034/tests/ex09_2",
  "members/sample_034/tests/ex09_3",
  "members/sample_035/raw_code",
  "members/sample_035/tests/ex09_0",
  "members/sample_035/tests/ex09_1",
  "members/sample_035/tests/ex09_2",
  "members/sample_035/tests/ex09_3",
  "members/sample_036/raw_code",
  "members/sample_036/tests/ex09_0",
  "members/sample_036/tests/ex09_1",
  "members/sample_036/tests/ex09_2",
  "members/sample_036/tests/ex09_3",
  "members/sample_037/raw_code",
  "members/sample_037/tests/ex09_0",
  "members/sample_037/tests/ex09_1",
  "members/sample_037/tests/ex09_2",
  "members/sample_037/tests/ex09_3",
  "members/sample_038/raw_code",
  "members/sample_038/tests/ex09_0",
  "members/sample_038/tests/ex09_1",
  "members/sample_038/tests/ex09_2",
  "members/sample_038/tests/ex09_3",
  "members/sample_039/raw_code",
  "members/sample_039/tests/ex09_0",
  "members/sample_039/tests/ex09_1",
  "members/sample_039/tests/ex09_2",
  "members/sample_039/tests/ex09_3",
  "members/sample_040/raw_code",
  "members/sample_040/tests/ex09_0",
  "members/sample_040/tests/ex09_1",
  "members/sample_040/tests/ex09_2",
  "members/sample_040/tests/ex09_3",
  "members/sample_041/raw_code",
  "members/sample_041/tests/ex09_0",
  "members/sample_041/tests/ex09_1",
  "members/sample_041/tests/ex09_3",
  "members/sample_042/raw_code",
  "members/sample_042/tests/ex09_0",
  "members/sample_042/tests/ex09_1",
  "members/sample_042/tests/ex09_3",
  "members/sample_043/raw_code",
  "members/sample_043/tests/ex09_0",
  "members/sample_043/tests/ex09_1",
  "members/sample_043/tests/ex09_3",
  "members/sample_044/raw_code",
  "members/sample_044/tests/ex09_0",
  "members/sample_044/tests/ex09_1",
  "members/sample_044/tests/ex09_2",
  "members/sample_044/tests/ex09_3",
  "members/sample_045/raw_code",
  "members/sample_045/tests/ex09_0",
  "members/sample_045/tests/ex09_1",
  "members/sample_045/tests/ex09_2",
  "members/sample_045/tests/ex09_3",
  "members/sample_046/raw_code",
  "members/sample_046/tests/ex09_0",
  "members/sample_046/tests/ex09_1",
  "members/sample_046/tests/ex09_2",
  "members/sample_046/tests/ex09_3",
  "members/sample_047/raw_code",
  "members/sample_047/tests/ex09_0",
  "members/sample_047/tests/ex09_1",
  "members/sample_047/tests/ex09_2",
  "members/sample_047/tests/ex09_3",
  "members/sample_048/raw_code",
  "members/sample_048/tests/ex09_0",
  "members/sample_048/tests/ex09_1",
  "members/sample_048/tests/ex09_2",
  "members/sample_048/tests/ex09_3",
  "members/sample_049/raw_code",
  "members/sample_049/tests/ex09_0",
  "members/sample_049/tests/ex09_1",
  "members/sample_049/tests/ex09_2",
  "members/sample_049/tests/ex09_3",
  "members/sample_050/raw_code",
  "members/sample_050/tests/ex09_0",
  "members/sample_050/tests/ex09_1",
  "members/sample_050/tests/ex09_2",
  "members/sample_050/tests/ex09_3",
  "members/sample_051/raw_code",
  "members/sample_051/tests/ex09_0",
  "members/sample_051/tests/ex09_1",
  "members/sample_051/tests/ex09_2",
  "members/sample_051/tests/ex09_3",
  "members/sample_052/raw_code",
  "members/sample_052/tests/ex09_0",
  "members/sample_052/tests/ex09_1",
  "members/sample_052/tests/ex09_2",
  "members/sample_052/tests/ex09_3",
  "members/sample_053/raw_code",
  "members/sample_053/tests/ex09_0",
  "members/sample_053/tests/ex09_1",
  "members/sample_053/tests/ex09_2",
  "members/sample_053/tests/ex09_3",
  "members/sample_054/raw_code",
  "members/sample_054/tests/ex09_0",
  "members/sample_054/tests/ex09_1",
  "members/sample_054/tests/ex09_2",
  "members/sample_054/tests/ex09_3",
  "members/sample_055/raw_code",
  "members/sample_055/tests/ex09_0",
  "members/sample_055/tests/ex09_1",
  "members/sample_055/tests/ex09_2",
  "members/sample_055/tests/ex09_3",
  "members/sample_056/raw_code",
  "members/sample_056/tests/ex09_0",
  "members/sample_056/tests/ex09_2",
  "members/sample_056/tests/ex09_3",
  "members/sample_057/raw_code",
  "members/sample_057/tests/ex09_0",
  "members/sample_057/tests/ex09_2",
  "members/sample_057/tests/ex09_3"
]
```
