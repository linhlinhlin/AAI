# lab04-ex07--kmeans--combined_stdout--s42--c2

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 12; phân vùng: {'train': 9, 'validation': 3}.


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
    "test_id": "ex07_0",
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
    "test_id": "ex07_2",
    "n_cluster": 12,
    "n_observed": 12,
    "n_failed": 10,
    "n_not_run": 0,
    "failure_rate_observed": 0.8333333333333334,
    "failure_rate_cluster": 0.8333333333333334,
    "outcome_counts": {
      "fail": 10,
      "pass": 2
    }
  },
  {
    "test_id": "ex07_4",
    "n_cluster": 12,
    "n_observed": 12,
    "n_failed": 5,
    "n_not_run": 0,
    "failure_rate_observed": 0.4166666666666667,
    "failure_rate_cluster": 0.4166666666666667,
    "outcome_counts": {
      "pass": 7,
      "fail": 5
    }
  },
  {
    "test_id": "ex07_3",
    "n_cluster": 12,
    "n_observed": 12,
    "n_failed": 1,
    "n_not_run": 0,
    "failure_rate_observed": 0.08333333333333333,
    "failure_rate_cluster": 0.08333333333333333,
    "outcome_counts": {
      "pass": 11,
      "fail": 1
    }
  },
  {
    "test_id": "ex07_1",
    "n_cluster": 12,
    "n_observed": 12,
    "n_failed": 0,
    "n_not_run": 0,
    "failure_rate_observed": 0.0,
    "failure_rate_cluster": 0.0,
    "outcome_counts": {
      "pass": 12
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex07_3:edit_band",
    "value": "__unknown__",
    "n": 11,
    "n_cluster": 12,
    "rate": 0.9166666666666666,
    "cohort_rate": 0.1864406779661017,
    "difference_from_cohort": 0.7302259887005649
  },
  {
    "feature": "stdout:ex07_3:relation",
    "value": "__unknown__",
    "n": 11,
    "n_cluster": 12,
    "rate": 0.9166666666666666,
    "cohort_rate": 0.1864406779661017,
    "difference_from_cohort": 0.7302259887005649
  },
  {
    "feature": "test:ex07_3",
    "value": "pass",
    "n": 11,
    "n_cluster": 12,
    "rate": 0.9166666666666666,
    "cohort_rate": 0.1864406779661017,
    "difference_from_cohort": 0.7302259887005649
  },
  {
    "feature": "stdout:ex07_1:edit_band",
    "value": "__unknown__",
    "n": 12,
    "n_cluster": 12,
    "rate": 1.0,
    "cohort_rate": 0.2711864406779661,
    "difference_from_cohort": 0.728813559322034
  },
  {
    "feature": "stdout:ex07_1:relation",
    "value": "__unknown__",
    "n": 12,
    "n_cluster": 12,
    "rate": 1.0,
    "cohort_rate": 0.2711864406779661,
    "difference_from_cohort": 0.728813559322034
  },
  {
    "feature": "test:ex07_1",
    "value": "pass",
    "n": 12,
    "n_cluster": 12,
    "rate": 1.0,
    "cohort_rate": 0.2711864406779661,
    "difference_from_cohort": 0.728813559322034
  },
  {
    "feature": "stdout:ex07_0:relation",
    "value": "different",
    "n": 12,
    "n_cluster": 12,
    "rate": 1.0,
    "cohort_rate": 0.3050847457627119,
    "difference_from_cohort": 0.6949152542372881
  },
  {
    "feature": "stdout:ex07_2:relation",
    "value": "different",
    "n": 10,
    "n_cluster": 12,
    "rate": 0.8333333333333334,
    "cohort_rate": 0.1864406779661017,
    "difference_from_cohort": 0.6468926553672316
  },
  {
    "feature": "test:ex07_2",
    "value": "fail",
    "n": 10,
    "n_cluster": 12,
    "rate": 0.8333333333333334,
    "cohort_rate": 0.3559322033898305,
    "difference_from_cohort": 0.47740112994350287
  },
  {
    "feature": "stdout:ex07_4:edit_band",
    "value": "__unknown__",
    "n": 7,
    "n_cluster": 12,
    "rate": 0.5833333333333334,
    "cohort_rate": 0.11864406779661017,
    "difference_from_cohort": 0.4646892655367232
  },
  {
    "feature": "stdout:ex07_4:relation",
    "value": "__unknown__",
    "n": 7,
    "n_cluster": 12,
    "rate": 0.5833333333333334,
    "cohort_rate": 0.11864406779661017,
    "difference_from_cohort": 0.4646892655367232
  },
  {
    "feature": "test:ex07_4",
    "value": "pass",
    "n": 7,
    "n_cluster": 12,
    "rate": 0.5833333333333334,
    "cohort_rate": 0.11864406779661017,
    "difference_from_cohort": 0.4646892655367232
  },
  {
    "feature": "test:ex07_0",
    "value": "fail",
    "n": 12,
    "n_cluster": 12,
    "rate": 1.0,
    "cohort_rate": 0.576271186440678,
    "difference_from_cohort": 0.423728813559322
  },
  {
    "feature": "stdout:ex07_0:edit_band",
    "value": "large",
    "n": 6,
    "n_cluster": 12,
    "rate": 0.5,
    "cohort_rate": 0.1016949152542373,
    "difference_from_cohort": 0.3983050847457627
  },
  {
    "feature": "stdout:ex07_2:edit_band",
    "value": "large",
    "n": 5,
    "n_cluster": 12,
    "rate": 0.4166666666666667,
    "cohort_rate": 0.0847457627118644,
    "difference_from_cohort": 0.3319209039548023
  },
  {
    "feature": "stdout:ex07_2:edit_band",
    "value": "medium",
    "n": 4,
    "n_cluster": 12,
    "rate": 0.3333333333333333,
    "cohort_rate": 0.06779661016949153,
    "difference_from_cohort": 0.2655367231638418
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 8,
    "n_cluster": 12,
    "rate": 0.6666666666666666,
    "cohort_rate": 0.4745762711864407,
    "difference_from_cohort": 0.19209039548022594
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "0",
    "n": 9,
    "n_cluster": 12,
    "rate": 0.75,
    "cohort_rate": 0.559322033898305,
    "difference_from_cohort": 0.19067796610169496
  },
  {
    "feature": "ast:c_for",
    "value": "0",
    "n": 5,
    "n_cluster": 12,
    "rate": 0.4166666666666667,
    "cohort_rate": 0.3050847457627119,
    "difference_from_cohort": 0.1115819209039548
  },
  {
    "feature": "ast:c_zero_index",
    "value": "0",
    "n": 12,
    "n_cluster": 12,
    "rate": 1.0,
    "cohort_rate": 0.9322033898305084,
    "difference_from_cohort": 0.06779661016949157
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 8,
    "n_cluster": 12,
    "rate": 0.6666666666666666,
    "cohort_rate": 0.4745762711864407,
    "difference_from_cohort": 0.19209039548022594
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 12,
    "n_cluster": 12,
    "rate": 1.0,
    "cohort_rate": 0.9661016949152542,
    "difference_from_cohort": 0.03389830508474578
  },
  {
    "feature": "ast:c_array_parameter",
    "value": "1",
    "n": 12,
    "n_cluster": 12,
    "rate": 1.0,
    "cohort_rate": 0.9830508474576272,
    "difference_from_cohort": 0.016949152542372836
  },
  {
    "feature": "ast:c_while",
    "value": "1",
    "n": 7,
    "n_cluster": 12,
    "rate": 0.5833333333333334,
    "cohort_rate": 0.576271186440678,
    "difference_from_cohort": 0.007062146892655385
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
    "feature": "ast:c_subscript",
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
    "feature": "ast:c_for",
    "value": "1",
    "n": 7,
    "n_cluster": 12,
    "rate": 0.5833333333333334,
    "cohort_rate": 0.6949152542372882,
    "difference_from_cohort": -0.1115819209039548
  }
]
```


## IF–THEN dự đoán cluster, không dự đoán gold

```json
[
  {
    "rule_id": 2,
    "if": [
      "NOT (stdout:ex07_3:relation=different)",
      "NOT (stdout:ex07_4:relation=whitespace)"
    ],
    "then_cluster": 2,
    "train_support": 8,
    "train_precision": 1.0,
    "holdout_support": 3,
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

sample_007, sample_011, sample_004, sample_010

## sample_004 — train — đại diện

```c
#include <stdio.h>

#define MAX 80



int leLinha(char s[]) {
	int chars = 0;
	getchar(); 

	while ((s[chars] = getchar()) != EOF && s[chars] != '\n')
		chars++;
	s[chars] = '\0';

	return chars;
}

void apagaCaracter(char s[], char c) {
	int len = leLinha(s), j, i;

	for (i = len - 1; i >= 0; i--)
		if (s[i] == c)
			for (j = i; s[j] != '\0'; j++)
				s[j] = s[j + 1];
}

int main() {
	char s[MAX], c = getchar();
	apagaCaracter(s, c);
	printf("%s\n", s);

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
  "source_sha256": "207b2dcfb3a84265c6331762fa2ceba280c753a0186b6b6bff76aaf536a9c6b4",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "pass",
    "ex07_2": "fail",
    "ex07_3": "pass",
    "ex07_4": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "a adeus\n"
    },
    {
      "test_id": "ex07_2",
      "input": "abdddba\nh",
      "expected": "abdddba\n",
      "output": "dddb\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "test:ex07_4": "pass",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "0",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "__unknown__",
    "stdout:ex07_1:edit_band": "__unknown__",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "__unknown__",
    "stdout:ex07_3:edit_band": "__unknown__",
    "stdout:ex07_4:relation": "__unknown__",
    "stdout:ex07_4:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "test:ex07_4": "pass",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
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
#include <string.h>
#define MAX 100

void apagaCaracter(char s[], char c)
{
    int i, j;
    for (i=0, j=0; s[i]!='\0'; i++)
    {
        if (s[i]!=c)
        {
            s[j]=s[i];
            j++;
        }
    }
    s[j]='\0';
}

int main()
{
    char s[MAX], c;
    fgets(s, MAX, stdin);
    scanf("%s", &c);
    apagaCaracter(s,c);
    printf ("%s\n", s);
    return 0;
}
```

```json
{
  "sample_id": "sample_007",
  "partition": "train",
  "representative": true,
  "is_train_medoid": true,
  "raw_code_truncated": false,
  "source_sha256": "a8158a9e5d1ef5d259949a347dd2504439fbeeb89f9b443eb346abe310e8d88c",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "pass",
    "ex07_2": "fail",
    "ex07_3": "pass",
    "ex07_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "\n"
    },
    {
      "test_id": "ex07_2",
      "input": "abdddba\nh",
      "expected": "abdddba\n",
      "output": "\n"
    },
    {
      "test_id": "ex07_4",
      "input": "aaaaaxaaaaaaaaaaaa\na",
      "expected": "x\n",
      "output": "\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "test:ex07_4": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "__unknown__",
    "stdout:ex07_1:edit_band": "__unknown__",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "__unknown__",
    "stdout:ex07_3:edit_band": "__unknown__",
    "stdout:ex07_4:relation": "different",
    "stdout:ex07_4:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "test:ex07_4": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
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


## sample_010 — train — đại diện

```c

#include <stdio.h>
#define MAX 80

void apagaCaracter(char s[], char c);
int lelinha(char s[]);

int main() {
    char c, s[80];
    c = getchar();
    getchar(); 
    lelinha(s);
    apagaCaracter(s, c);
    printf("%s\n", s);

    return 0;
}


void apagaCaracter(char s[], char c) {
    int i, i2;
    for (i = 0; i < MAX; i++)
        if (s[i] == c){
            for (i2 = i; i2 < MAX-1; i2++) 
                s[i2] = s[i2+1]; 
        }
}



int lelinha(char s[]) {
    int contador = 0;
    do {
        s[contador] = getchar();
    } while (s[contador] != '\n' && s[contador++] != EOF);
    s[contador] = '\0';
    return contador;
}
```

```json
{
  "sample_id": "sample_010",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "1b85dfd15fa2da1193eeb71f3de45dd3189d0aaa687608a5120c1459c72988cf",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "pass",
    "ex07_2": "fail",
    "ex07_3": "fail",
    "ex07_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "a adeus\n"
    },
    {
      "test_id": "ex07_2",
      "input": "abdddba\nh",
      "expected": "abdddba\n",
      "output": "dddb\n"
    },
    {
      "test_id": "ex07_3",
      "input": "aaaaaaaaaaaaaaaaaa\na",
      "expected": "\n",
      "output": "aaaaaaaa\n"
    },
    {
      "test_id": "ex07_4",
      "input": "aaaaaxaaaaaaaaaaaa\na",
      "expected": "x\n",
      "output": "axaaaaaa\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "test:ex07_4": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "0",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "__unknown__",
    "stdout:ex07_1:edit_band": "__unknown__",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "different",
    "stdout:ex07_3:edit_band": "large",
    "stdout:ex07_4:relation": "different",
    "stdout:ex07_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "test:ex07_4": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_011 — train — đại diện

```c

#include <stdio.h>

void apagaCaracter(char s[], char c){
    int i=0, novapalavra=0;
    while (s[i]!='\0'){
        if (s[i]!=c){
            s[novapalavra]=s[i];
            novapalavra++;
        }
        i++;
    }
    s[novapalavra]='\0'; 
    
}

int main(){
    char s[80],c;
    scanf("%s %c",s,&c);
    apagaCaracter(s,c);
    printf("%s\n",s);
    return 0;
}
```

```json
{
  "sample_id": "sample_011",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "9b069a9c74f7b803ae9290ecca10d978f9e619f50eb1ef3be292fc89b52376af",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "pass",
    "ex07_2": "pass",
    "ex07_3": "pass",
    "ex07_4": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "ol\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "pass",
    "test:ex07_3": "pass",
    "test:ex07_4": "pass",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "__unknown__",
    "stdout:ex07_1:edit_band": "__unknown__",
    "stdout:ex07_2:relation": "__unknown__",
    "stdout:ex07_2:edit_band": "__unknown__",
    "stdout:ex07_3:relation": "__unknown__",
    "stdout:ex07_3:edit_band": "__unknown__",
    "stdout:ex07_4:relation": "__unknown__",
    "stdout:ex07_4:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "pass",
    "test:ex07_3": "pass",
    "test:ex07_4": "pass",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
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


## sample_001 — train

```c
#include <stdio.h>

#define MAX 80



int leLinha(char str[]);

void apagaCaracter(char str[], char c);

int main()
{
    char str[MAX], c;
    
    fgets(str, MAX, stdin);
    scanf("%c", &c);
    
    apagaCaracter(str, c);

    printf("%s", str);

    return 0;
}    


void apagaCaracter(char str[], char c)
{
    int i = 0, j = 0;
    char car;

    while(str[i++] != '\0')
    {
        car = str[i];
        if (car != c) 
            str[j++] = car;
    }
    str[j] = '\0';
}
```

```json
{
  "sample_id": "sample_001",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "be07320e61a6f8a91c04c7938391eab9e3e24ad75e96b8ff9a73fd564749731b",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "pass",
    "ex07_2": "fail",
    "ex07_3": "pass",
    "ex07_4": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "l deus\n"
    },
    {
      "test_id": "ex07_2",
      "input": "abdddba\nh",
      "expected": "abdddba\n",
      "output": "bdddba\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "test:ex07_4": "pass",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "small",
    "stdout:ex07_1:relation": "__unknown__",
    "stdout:ex07_1:edit_band": "__unknown__",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "__unknown__",
    "stdout:ex07_3:edit_band": "__unknown__",
    "stdout:ex07_4:relation": "__unknown__",
    "stdout:ex07_4:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "test:ex07_4": "pass",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
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


## sample_002 — validation

```c
#include <stdio.h>

#define MAX 80

void apagaCaracter(char s[], char c);


int main()
{
    char s[MAX];
    char c;
    
    fgets(s, MAX, stdin);
    c = getchar();
    apagaCaracter(s, c);

    printf("%s", s);
    return 0;
}



void apagaCaracter(char s[], char c) {
    
    int read_i, write_i;
    char c2;
    read_i = write_i = 0;
    
    while((c2 = s[read_i++]) != '\0') {
        if (c2 != c)
            s[write_i++] = c2;
    s[write_i] = '\0';
    }

}
```

```json
{
  "sample_id": "sample_002",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "016913d4ffb6a49c7d0d4dc1e01aae7a77f52f2342d641d2e24df4fea1c5bd18",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "pass",
    "ex07_2": "fail",
    "ex07_3": "pass",
    "ex07_4": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "o"
    },
    {
      "test_id": "ex07_2",
      "input": "abdddba\nh",
      "expected": "abdddba\n",
      "output": "a"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "test:ex07_4": "pass",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "0",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "__unknown__",
    "stdout:ex07_1:edit_band": "__unknown__",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "__unknown__",
    "stdout:ex07_3:edit_band": "__unknown__",
    "stdout:ex07_4:relation": "__unknown__",
    "stdout:ex07_4:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "test:ex07_4": "pass",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
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

#define MAX 80

int leLinha(char s[]){
	int i, c, cont = 0;

	for (i = 0; i < MAX-1 && (c = getchar()) != EOF && c != '\n'; i++){
		s[i] = c;
		cont++;
	}
	s[i] = '\0';

	return cont;
}

void apagaCaracter(char s[], char c){
	int i, i2 = 0;
	for(i = 0; s[i] != '\0'; i++){
		if(s[i] != c){
			s[i2] = s[i];
			i2++;
		}
	}
	s[i2] = '\0';
}

int main(){
	char c, s[MAX];
	scanf("%c\n", &c);
	leLinha(s);
	apagaCaracter(s, c);
	printf("%s\n", s);
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
  "source_sha256": "075138e9094c2f73470c5e63bfb0cf2ab561e1fa925744e308f2d80673282920",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "pass",
    "ex07_2": "fail",
    "ex07_3": "pass",
    "ex07_4": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "la adeus\n"
    },
    {
      "test_id": "ex07_2",
      "input": "abdddba\nh",
      "expected": "abdddba\n",
      "output": "bdddb\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "test:ex07_4": "pass",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "__unknown__",
    "stdout:ex07_1:edit_band": "__unknown__",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "__unknown__",
    "stdout:ex07_3:edit_band": "__unknown__",
    "stdout:ex07_4:relation": "__unknown__",
    "stdout:ex07_4:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "test:ex07_4": "pass",
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


## sample_005 — train

```c

#include <stdio.h>
#include <string.h>
#define DIM 100

void lelinha(char vec[]){
    char c;
    int i=0;
    while ((c=getchar())!= EOF && c!='\n')
    {
        vec[i]=c;
    }
    vec[i]='\n';
    vec[++i]='\0';
}

void vareraser(char vec[], char c){
    char vec2[DIM];
    int i,n,k;
    k=0;
    n=strlen(vec);
    for ( i = 0; i < n; i++)
    {
        if (vec[i]!=c)
        {
            vec2[k]=vec[i];
            k++;
        }
        
    }
    printf("%s",vec2);
}

int main(){
    char vec[DIM];
    char c;
    lelinha(vec);
    scanf("%c",&c);
    vareraser(vec,c);
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
  "source_sha256": "1001d6c42184b5d082c8a7084cef9f92401c03bde147751624dce97b55489675",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "pass",
    "ex07_2": "fail",
    "ex07_3": "pass",
    "ex07_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "\n"
    },
    {
      "test_id": "ex07_2",
      "input": "abdddba\nh",
      "expected": "abdddba\n",
      "output": "\n"
    },
    {
      "test_id": "ex07_4",
      "input": "aaaaaxaaaaaaaaaaaa\na",
      "expected": "x\n",
      "output": "\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "test:ex07_4": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "__unknown__",
    "stdout:ex07_1:edit_band": "__unknown__",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "__unknown__",
    "stdout:ex07_3:edit_band": "__unknown__",
    "stdout:ex07_4:relation": "different",
    "stdout:ex07_4:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "test:ex07_4": "fail",
    "ast:c_for": "1",
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


## sample_006 — validation

```c

#include <stdio.h>
#define MAX 50


void apagaCaracter(char s[], char n){
    int c, contador = 0;

    while((c = getchar()) != EOF && c != '\n'){
        if(c != n)
            s[contador++] = c;
    }
    s[contador] = '\0';
}

int main(){
    char n, str[MAX];

    scanf("%c", &n);
    apagaCaracter(str, n);

    printf("%s\n", str);

    return 0;
}
```

```json
{
  "sample_id": "sample_006",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "a7a10c8a6ef5e10a4977530e9b5cf370cc9027a4dc70f8b20a2ab16a06ad44eb",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "pass",
    "ex07_2": "fail",
    "ex07_3": "pass",
    "ex07_4": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "la adeus\n"
    },
    {
      "test_id": "ex07_2",
      "input": "abdddba\nh",
      "expected": "abdddba\n",
      "output": "bdddb\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "test:ex07_4": "pass",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "__unknown__",
    "stdout:ex07_1:edit_band": "__unknown__",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "medium",
    "stdout:ex07_3:relation": "__unknown__",
    "stdout:ex07_3:edit_band": "__unknown__",
    "stdout:ex07_4:relation": "__unknown__",
    "stdout:ex07_4:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "test:ex07_4": "pass",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
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


## sample_008 — train

```c


#include <stdio.h>
#include <string.h>
#define MAX 80

void apagaCaracter(char s[], char c)
{
    int i, j;
    for (i=0, j=0; s[i]!='\0'; i++)
    {
        if (s[i]!=c)
        {
            s[j]=s[i];
            j++;
        }
    }
    s[j]='\0';
}

int main()
{
    char s[MAX], c;
    fgets(s, MAX, stdin);
    scanf("%s", &c);
    apagaCaracter(s,c);
    printf ("%s\n", s);
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
  "source_sha256": "76993d5c4b940985269fe615ec31b466cfb10192bc1d8140fa991c40b7d328ba",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "pass",
    "ex07_2": "fail",
    "ex07_3": "pass",
    "ex07_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "\n"
    },
    {
      "test_id": "ex07_2",
      "input": "abdddba\nh",
      "expected": "abdddba\n",
      "output": "\n"
    },
    {
      "test_id": "ex07_4",
      "input": "aaaaaxaaaaaaaaaaaa\na",
      "expected": "x\n",
      "output": "\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "test:ex07_4": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "__unknown__",
    "stdout:ex07_1:edit_band": "__unknown__",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "__unknown__",
    "stdout:ex07_3:edit_band": "__unknown__",
    "stdout:ex07_4:relation": "different",
    "stdout:ex07_4:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "test:ex07_4": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
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


## sample_009 — validation

```c

#include <stdio.h>
#include <string.h>

#define DIM 80

#define BOA 1
#define MAU 0
#define NADA 2

void apagaCaracter(char s[DIM], char c) {

    int i;
    int current = NADA;

    for (i = 0; s[i] != '\0'; i++) {

            if (s[i] == c) {
            current = MAU;
        }

        if (s[i] != c && s[i] != ' ') {

            if (current == NADA) {
                putchar(s[i]);
            }
            if (current == MAU) {
                putchar(s[i]);
            }
            if (current == BOA) {
            putchar(s[i]);
            }

            current = BOA;
        }
        
        if (s[i] == ' ') {

            if (current == BOA) {
                putchar(s[i]);
            }
            current = NADA;
        }

    }

}

int main () {

    char s[DIM];
    char c;

    fgets(s, DIM, stdin);
    c = getchar();

    apagaCaracter(s, c);


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
  "source_sha256": "c8a3ae6b0be004560d3b13c9a8db40218df79901cce4b629aa37571c269ffc2f",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "pass",
    "ex07_2": "pass",
    "ex07_3": "pass",
    "ex07_4": "pass"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "oldeus\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "pass",
    "test:ex07_3": "pass",
    "test:ex07_4": "pass",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "0",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "small",
    "stdout:ex07_1:relation": "__unknown__",
    "stdout:ex07_1:edit_band": "__unknown__",
    "stdout:ex07_2:relation": "__unknown__",
    "stdout:ex07_2:edit_band": "__unknown__",
    "stdout:ex07_3:relation": "__unknown__",
    "stdout:ex07_3:edit_band": "__unknown__",
    "stdout:ex07_4:relation": "__unknown__",
    "stdout:ex07_4:edit_band": "__unknown__"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "pass",
    "test:ex07_3": "pass",
    "test:ex07_4": "pass",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
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

void apagaCaracter(char s[], char c){
    int i=0, j=0;
    while (s[i]!='\0'){
        if (s[i]!=c){
            s[j]=s[i];
            j++;
        }
        i++;
    }
    s[j]='\0'; 
   
}

int main(){
    char s[80],c;
    scanf("%c",&c);
    apagaCaracter(s,c);
    printf("%s\n",s);
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
  "source_sha256": "9d9a5e77e7f205357eaf87c8b26c7618bbca0f8a56b3690699834788508232d4",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "pass",
    "ex07_2": "fail",
    "ex07_3": "pass",
    "ex07_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "\n"
    },
    {
      "test_id": "ex07_2",
      "input": "abdddba\nh",
      "expected": "abdddba\n",
      "output": "\n"
    },
    {
      "test_id": "ex07_4",
      "input": "aaaaaxaaaaaaaaaaaa\na",
      "expected": "x\n",
      "output": "\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "test:ex07_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "large",
    "stdout:ex07_1:relation": "__unknown__",
    "stdout:ex07_1:edit_band": "__unknown__",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "large",
    "stdout:ex07_3:relation": "__unknown__",
    "stdout:ex07_3:edit_band": "__unknown__",
    "stdout:ex07_4:relation": "different",
    "stdout:ex07_4:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "pass",
    "test:ex07_2": "fail",
    "test:ex07_3": "pass",
    "test:ex07_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
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


## Evidence refs hợp lệ

```json
[
  "test_statistics",
  "feature_statistics",
  "learned_if_then_rules",
  "semantic_findings",
  "problem_statement",
  "members/sample_001/raw_code",
  "members/sample_001/tests/ex07_0",
  "members/sample_001/tests/ex07_2",
  "members/sample_002/raw_code",
  "members/sample_002/tests/ex07_0",
  "members/sample_002/tests/ex07_2",
  "members/sample_003/raw_code",
  "members/sample_003/tests/ex07_0",
  "members/sample_003/tests/ex07_2",
  "members/sample_004/raw_code",
  "members/sample_004/tests/ex07_0",
  "members/sample_004/tests/ex07_2",
  "members/sample_005/raw_code",
  "members/sample_005/tests/ex07_0",
  "members/sample_005/tests/ex07_2",
  "members/sample_005/tests/ex07_4",
  "members/sample_006/raw_code",
  "members/sample_006/tests/ex07_0",
  "members/sample_006/tests/ex07_2",
  "members/sample_007/raw_code",
  "members/sample_007/tests/ex07_0",
  "members/sample_007/tests/ex07_2",
  "members/sample_007/tests/ex07_4",
  "members/sample_008/raw_code",
  "members/sample_008/tests/ex07_0",
  "members/sample_008/tests/ex07_2",
  "members/sample_008/tests/ex07_4",
  "members/sample_009/raw_code",
  "members/sample_009/tests/ex07_0",
  "members/sample_010/raw_code",
  "members/sample_010/tests/ex07_0",
  "members/sample_010/tests/ex07_2",
  "members/sample_010/tests/ex07_3",
  "members/sample_010/tests/ex07_4",
  "members/sample_011/raw_code",
  "members/sample_011/tests/ex07_0",
  "members/sample_012/raw_code",
  "members/sample_012/tests/ex07_0",
  "members/sample_012/tests/ex07_2",
  "members/sample_012/tests/ex07_4"
]
```
