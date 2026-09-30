# lab04-ex07--kmeans--combined_stdout--s42--c1

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 16; phân vùng: {'train': 15, 'validation': 1}.


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
    "n_cluster": 16,
    "n_observed": 16,
    "n_failed": 16,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 16
    }
  },
  {
    "test_id": "ex07_1",
    "n_cluster": 16,
    "n_observed": 16,
    "n_failed": 16,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 16
    }
  },
  {
    "test_id": "ex07_3",
    "n_cluster": 16,
    "n_observed": 16,
    "n_failed": 16,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 16
    }
  },
  {
    "test_id": "ex07_4",
    "n_cluster": 16,
    "n_observed": 16,
    "n_failed": 16,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 16
    }
  },
  {
    "test_id": "ex07_2",
    "n_cluster": 16,
    "n_observed": 16,
    "n_failed": 11,
    "n_not_run": 0,
    "failure_rate_observed": 0.6875,
    "failure_rate_cluster": 0.6875,
    "outcome_counts": {
      "pass": 5,
      "fail": 11
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex07_1:relation",
    "value": "whitespace",
    "n": 16,
    "n_cluster": 16,
    "rate": 1.0,
    "cohort_rate": 0.3050847457627119,
    "difference_from_cohort": 0.6949152542372881
  },
  {
    "feature": "stdout:ex07_3:relation",
    "value": "whitespace",
    "n": 16,
    "n_cluster": 16,
    "rate": 1.0,
    "cohort_rate": 0.3050847457627119,
    "difference_from_cohort": 0.6949152542372881
  },
  {
    "feature": "stdout:ex07_4:relation",
    "value": "whitespace",
    "n": 16,
    "n_cluster": 16,
    "rate": 1.0,
    "cohort_rate": 0.3050847457627119,
    "difference_from_cohort": 0.6949152542372881
  },
  {
    "feature": "stdout:ex07_0:relation",
    "value": "whitespace",
    "n": 15,
    "n_cluster": 16,
    "rate": 0.9375,
    "cohort_rate": 0.2711864406779661,
    "difference_from_cohort": 0.666313559322034
  },
  {
    "feature": "stdout:ex07_2:edit_band",
    "value": "small",
    "n": 11,
    "n_cluster": 16,
    "rate": 0.6875,
    "cohort_rate": 0.2033898305084746,
    "difference_from_cohort": 0.4841101694915254
  },
  {
    "feature": "stdout:ex07_2:relation",
    "value": "whitespace",
    "n": 10,
    "n_cluster": 16,
    "rate": 0.625,
    "cohort_rate": 0.1694915254237288,
    "difference_from_cohort": 0.4555084745762712
  },
  {
    "feature": "test:ex07_0",
    "value": "fail",
    "n": 16,
    "n_cluster": 16,
    "rate": 1.0,
    "cohort_rate": 0.576271186440678,
    "difference_from_cohort": 0.423728813559322
  },
  {
    "feature": "stdout:ex07_0:edit_band",
    "value": "small",
    "n": 10,
    "n_cluster": 16,
    "rate": 0.625,
    "cohort_rate": 0.2033898305084746,
    "difference_from_cohort": 0.4216101694915254
  },
  {
    "feature": "stdout:ex07_1:edit_band",
    "value": "large",
    "n": 10,
    "n_cluster": 16,
    "rate": 0.625,
    "cohort_rate": 0.2542372881355932,
    "difference_from_cohort": 0.3707627118644068
  },
  {
    "feature": "stdout:ex07_4:edit_band",
    "value": "medium",
    "n": 10,
    "n_cluster": 16,
    "rate": 0.625,
    "cohort_rate": 0.288135593220339,
    "difference_from_cohort": 0.336864406779661
  },
  {
    "feature": "test:ex07_2",
    "value": "fail",
    "n": 11,
    "n_cluster": 16,
    "rate": 0.6875,
    "cohort_rate": 0.3559322033898305,
    "difference_from_cohort": 0.3315677966101695
  },
  {
    "feature": "test:ex07_1",
    "value": "fail",
    "n": 16,
    "n_cluster": 16,
    "rate": 1.0,
    "cohort_rate": 0.7288135593220338,
    "difference_from_cohort": 0.27118644067796616
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 11,
    "n_cluster": 16,
    "rate": 0.6875,
    "cohort_rate": 0.4745762711864407,
    "difference_from_cohort": 0.2129237288135593
  },
  {
    "feature": "stdout:ex07_3:edit_band",
    "value": "medium",
    "n": 5,
    "n_cluster": 16,
    "rate": 0.3125,
    "cohort_rate": 0.1016949152542373,
    "difference_from_cohort": 0.2108050847457627
  },
  {
    "feature": "ast:c_while",
    "value": "0",
    "n": 10,
    "n_cluster": 16,
    "rate": 0.625,
    "cohort_rate": 0.423728813559322,
    "difference_from_cohort": 0.20127118644067798
  },
  {
    "feature": "test:ex07_3",
    "value": "fail",
    "n": 16,
    "n_cluster": 16,
    "rate": 1.0,
    "cohort_rate": 0.8135593220338984,
    "difference_from_cohort": 0.18644067796610164
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 9,
    "n_cluster": 16,
    "rate": 0.5625,
    "cohort_rate": 0.4406779661016949,
    "difference_from_cohort": 0.1218220338983051
  },
  {
    "feature": "test:ex07_4",
    "value": "fail",
    "n": 16,
    "n_cluster": 16,
    "rate": 1.0,
    "cohort_rate": 0.8813559322033898,
    "difference_from_cohort": 0.11864406779661019
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 13,
    "n_cluster": 16,
    "rate": 0.8125,
    "cohort_rate": 0.6949152542372882,
    "difference_from_cohort": 0.11758474576271183
  },
  {
    "feature": "stdout:ex07_0:edit_band",
    "value": "medium",
    "n": 6,
    "n_cluster": 16,
    "rate": 0.375,
    "cohort_rate": 0.2711864406779661,
    "difference_from_cohort": 0.1038135593220339
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 11,
    "n_cluster": 16,
    "rate": 0.6875,
    "cohort_rate": 0.4745762711864407,
    "difference_from_cohort": 0.2129237288135593
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 9,
    "n_cluster": 16,
    "rate": 0.5625,
    "cohort_rate": 0.4406779661016949,
    "difference_from_cohort": 0.1218220338983051
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 13,
    "n_cluster": 16,
    "rate": 0.8125,
    "cohort_rate": 0.6949152542372882,
    "difference_from_cohort": 0.11758474576271183
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 16,
    "n_cluster": 16,
    "rate": 1.0,
    "cohort_rate": 0.9661016949152542,
    "difference_from_cohort": 0.03389830508474578
  },
  {
    "feature": "ast:c_array_parameter",
    "value": "1",
    "n": 16,
    "n_cluster": 16,
    "rate": 1.0,
    "cohort_rate": 0.9830508474576272,
    "difference_from_cohort": 0.016949152542372836
  },
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 16,
    "n_cluster": 16,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_subscript",
    "value": "1",
    "n": 16,
    "n_cluster": 16,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 16,
    "n_cluster": 16,
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
      "NOT (stdout:ex07_3:relation=different)",
      "stdout:ex07_4:relation=whitespace",
      "stdout:ex07_0:relation=whitespace"
    ],
    "then_cluster": 1,
    "train_support": 14,
    "train_precision": 1.0,
    "holdout_support": 1,
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
  "reasoning": "Có 16 bài trong cụm. Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
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

sample_014, sample_003, sample_013, sample_002

## sample_002 — train — đại diện

```c
#include <stdio.h>
#define MAX 80

void lelinha(char s[])
{
    int i;
    char c;
    for(i=0;i<(MAX-1) && (c=getchar()) !='\n';i++)
    {
        s[i]=c;
    }
    s[i]= '\0';
}

void apagacaracter(char s[], char c)
{
    int i;
    for(i=0;s[i]!= '\0';i++)
    {
        if (s[i]==c)
        {
            s[i]=' ';
        }
    }
    printf("%s\n",s);
}
int main()
{
    char s[MAX],c;
    lelinha(s);
    scanf("%c",&c);
    apagacaracter(s,c);
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
  "source_sha256": "7200cc24ab57da4565f96e09a74141339fc61d994f460aa18f5f77e34c8aa48b",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "pass",
    "ex07_3": "fail",
    "ex07_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "ol   deus\n"
    },
    {
      "test_id": "ex07_1",
      "input": "ddd\nd",
      "expected": "\n",
      "output": "   \n"
    },
    {
      "test_id": "ex07_3",
      "input": "aaaaaaaaaaaaaaaaaa\na",
      "expected": "\n",
      "output": "                  \n"
    },
    {
      "test_id": "ex07_4",
      "input": "aaaaaxaaaaaaaaaaaa\na",
      "expected": "x\n",
      "output": "     x            \n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "pass",
    "test:ex07_3": "fail",
    "test:ex07_4": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "__unknown__",
    "stdout:ex07_2:edit_band": "__unknown__",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "large",
    "stdout:ex07_4:relation": "whitespace",
    "stdout:ex07_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "pass",
    "test:ex07_3": "fail",
    "test:ex07_4": "fail",
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


## sample_003 — train — đại diện

```c
#include <stdio.h>
#define MAX 80

void apagaCaracter(char s[],char c);

int main()
{
	char c, s[MAX];
	fgets(s, MAX, stdin);
	scanf("%c", &c);

	apagaCaracter(s,c);

	return 0;
}

void apagaCaracter(char s[], char c)
{
	int i = 0;

	while (s[i] != '\0'){
		if (s[i] == c){
			s[i] = ' ';}
		i++;}

	printf("%s", s);
}

```

```json
{
  "sample_id": "sample_003",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "8d255f514195111ade48520e20e4b7a920ae37b3c4c8e4f5ac98aaa6e825c28f",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "pass",
    "ex07_3": "fail",
    "ex07_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "ol   deus\n"
    },
    {
      "test_id": "ex07_1",
      "input": "ddd\nd",
      "expected": "\n",
      "output": "   \n"
    },
    {
      "test_id": "ex07_3",
      "input": "aaaaaaaaaaaaaaaaaa\na",
      "expected": "\n",
      "output": "                  \n"
    },
    {
      "test_id": "ex07_4",
      "input": "aaaaaxaaaaaaaaaaaa\na",
      "expected": "x\n",
      "output": "     x            \n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "pass",
    "test:ex07_3": "fail",
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "__unknown__",
    "stdout:ex07_2:edit_band": "__unknown__",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "large",
    "stdout:ex07_4:relation": "whitespace",
    "stdout:ex07_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "pass",
    "test:ex07_3": "fail",
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


## sample_013 — train — đại diện

```c


# include <stdio.h>

int leLinh(char s[]) {
    int i = 0;
    char c;
    while ((c = getchar()) != EOF && c != '\n') {
        s[i] = c;
        i++;
    }

    s[i] = '\0';

    return i;
}

void apagaCaracter(char s[], char c) {
    int i = 0 ,j = 0;

    while (s[i] != '\0') {
        if (s[i] != c) {
            s[j] = s[i];
            j++;
        }
        i++;
    }
    s[j] ='\0';
}

int main() {
    char s[100],c;
    int len,i = 0;

    len = leLinh(s);
    c = getchar();
    if (len > 0) {
        apagaCaracter(s,c);
    }
    while (s[i] != '\0') {
        putchar(s[i]);
        i++;
    }
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
  "source_sha256": "89d6b63be1448dd9439a58f71c5a12dd793c823913519cd98d05f68f488be13c",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail",
    "ex07_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "ol deus"
    },
    {
      "test_id": "ex07_1",
      "input": "ddd\nd",
      "expected": "\n",
      "output": ""
    },
    {
      "test_id": "ex07_2",
      "input": "abdddba\nh",
      "expected": "abdddba\n",
      "output": "abdddba"
    },
    {
      "test_id": "ex07_3",
      "input": "aaaaaaaaaaaaaaaaaa\na",
      "expected": "\n",
      "output": ""
    },
    {
      "test_id": "ex07_4",
      "input": "aaaaaxaaaaaaaaaaaa\na",
      "expected": "x\n",
      "output": "x"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "test:ex07_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "0",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "small",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "large",
    "stdout:ex07_4:relation": "whitespace",
    "stdout:ex07_4:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "test:ex07_4": "fail",
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


## sample_014 — train — đại diện

```c

#include <stdio.h>
#define MAX 80
void apagaCaracter(char s[], char c) {
    int i;
    for (i=0;s[i]!='\n' && s[i]!='\0';i++) {
        if (s[i]!=c) {
            printf("%c",s[i]);
        }
    }
}
int main() {
    char s[MAX];
    char c;
    fgets(s,MAX,stdin);
    scanf("%c",&c);
    apagaCaracter(s,c);
    return 0;
}
```

```json
{
  "sample_id": "sample_014",
  "partition": "train",
  "representative": true,
  "is_train_medoid": true,
  "raw_code_truncated": false,
  "source_sha256": "39a9826bcd02a4f749fe55f51d6651e8bc71e7ee5a94eebbd5bb73374000a5ee",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail",
    "ex07_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "ol deus"
    },
    {
      "test_id": "ex07_1",
      "input": "ddd\nd",
      "expected": "\n",
      "output": ""
    },
    {
      "test_id": "ex07_2",
      "input": "abdddba\nh",
      "expected": "abdddba\n",
      "output": "abdddba"
    },
    {
      "test_id": "ex07_3",
      "input": "aaaaaaaaaaaaaaaaaa\na",
      "expected": "\n",
      "output": ""
    },
    {
      "test_id": "ex07_4",
      "input": "aaaaaxaaaaaaaaaaaa\na",
      "expected": "x\n",
      "output": "x"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "small",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "large",
    "stdout:ex07_4:relation": "whitespace",
    "stdout:ex07_4:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
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


## sample_001 — train

```c
#include <stdio.h>

#define LEN_STR 100

int leLinha(char s[])
{
	int i = 0;
	char c;

	while((c = getchar()) != '\n' && c != EOF)
	{
		s[i] = c;
		i++;
	}

	return i;
}

void apagaCaracter(char s[], char c)
{
	int i;
	for(i = 0; s[i] != '\0'; i++)
	{
		if(s[i] == c)
		{
			s[i] = ' ';
		}
	}
}

int main()
{
	char c;
	char s[LEN_STR];
	leLinha(s);
	scanf("%c", &c);

	apagaCaracter(s, c);

	printf("%s\n", s);

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
  "source_sha256": "da3311803f9096960e791bdb013daf6f35677ed5ae3b611031277e79b7006a99",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "pass",
    "ex07_3": "fail",
    "ex07_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "ol   deus\n"
    },
    {
      "test_id": "ex07_1",
      "input": "ddd\nd",
      "expected": "\n",
      "output": "   \n"
    },
    {
      "test_id": "ex07_3",
      "input": "aaaaaaaaaaaaaaaaaa\na",
      "expected": "\n",
      "output": "                  \n"
    },
    {
      "test_id": "ex07_4",
      "input": "aaaaaxaaaaaaaaaaaa\na",
      "expected": "x\n",
      "output": "     x            \n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "pass",
    "test:ex07_3": "fail",
    "test:ex07_4": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "__unknown__",
    "stdout:ex07_2:edit_band": "__unknown__",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "large",
    "stdout:ex07_4:relation": "whitespace",
    "stdout:ex07_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "pass",
    "test:ex07_3": "fail",
    "test:ex07_4": "fail",
    "ast:c_for": "1",
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


## sample_004 — train

```c
#include <stdio.h>
#include <string.h>
#define DIM 80
#define NOVA 80

void apagaCaracter(char s[], char c){
    int i,j;
    
    
    for (i = 0; s[i] != '\0';i++){
        if (s[i] == c)
            s[i] = ' ';
            
        }
    
    for (i = 0; s[i] != '\0';i++){
        if (s[i+1] != ' ')
        s[i] = s[i+1];
        else
            {s[i] = s[i+2];
                
            for (j = i; s[j] != '\0';j++)
                s[j] = s[j+1];
                
        }
    }

        


    

            
    

            
         

    }
    





int main() {
	int i,c;
	char s[DIM];
    c = getchar();
    for (i = 0; i < DIM-1 && c != EOF && c != '\n'; i++) {
        s[i] = c;
        c = getchar();}
    s[i] = '\0';
    c  = getchar();
    apagaCaracter(s,c);
    printf("%s\n", s);
    
    

   

    
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
  "source_sha256": "754ac4599bc05b910927eae32220b28c4b7a5c01334739ce9220a6b4f79c1f55",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail",
    "ex07_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "l  eus\n"
    },
    {
      "test_id": "ex07_1",
      "input": "ddd\nd",
      "expected": "\n",
      "output": " \n"
    },
    {
      "test_id": "ex07_2",
      "input": "abdddba\nh",
      "expected": "abdddba\n",
      "output": "bdddba\n"
    },
    {
      "test_id": "ex07_3",
      "input": "aaaaaaaaaaaaaaaaaa\na",
      "expected": "\n",
      "output": "        \n"
    },
    {
      "test_id": "ex07_4",
      "input": "aaaaaxaaaaaaaaaaaa\na",
      "expected": "x\n",
      "output": "  x      \n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "test:ex07_4": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "0",
    "stdout:ex07_0:relation": "different",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "different",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "large",
    "stdout:ex07_4:relation": "whitespace",
    "stdout:ex07_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "test:ex07_4": "fail",
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
    "ast:c_address_of": "0",
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
#include <string.h>

#define MAX 100

void apagaCaracter(char s[], char c)
{
    int i, j;

    for (i = 0; s[i] != '\0';i++)
    {
        if (s[i] == c)
        {
            for (j = i; s[j] != '\0';j++)
                s[j] = s[j+1];
        i--;
        }
    }
}

int leLinha(char s[MAX])
{
    int i;
    
    for (i = 0; i < MAX; i++)
    {
        s[i] = getchar();
        if (s[i] == '\n' || s[i] == EOF)
            break;
    }
    s[i] = '\0';
    return 0;
}

int main()
{
    char s[MAX],c;
    leLinha(s);
    c = getchar();
    apagaCaracter(s,c);
    printf("%s",s);
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
  "source_sha256": "5abf1b12208a8064391aedd19c131690dfa507151e40015761585546be6c25b9",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail",
    "ex07_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "ol deus"
    },
    {
      "test_id": "ex07_1",
      "input": "ddd\nd",
      "expected": "\n",
      "output": ""
    },
    {
      "test_id": "ex07_2",
      "input": "abdddba\nh",
      "expected": "abdddba\n",
      "output": "abdddba"
    },
    {
      "test_id": "ex07_3",
      "input": "aaaaaaaaaaaaaaaaaa\na",
      "expected": "\n",
      "output": ""
    },
    {
      "test_id": "ex07_4",
      "input": "aaaaaxaaaaaaaaaaaa\na",
      "expected": "x\n",
      "output": "x"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "test:ex07_4": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "0",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "small",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "large",
    "stdout:ex07_4:relation": "whitespace",
    "stdout:ex07_4:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "test:ex07_4": "fail",
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
    "ast:c_address_of": "0",
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

#define MAX 80

int leLinha (char s[]) {

    int c, i;

    for (i = 0; i < MAX && (c = getchar()) != '\n' && c != EOF; i++) {
        s[i] = c;
    }

    s[i] = '\0';
    return i;
}

void apagaCaracter(char s[], char c) {

    int i, dif = 0;

    for (i = 0; s[i] != '\0'; i++) {
        if (s[i] != c)
            s[i - dif] = s[i];

        else
            dif++;
    }
    s[i - dif] = '\0';
}

int main () {

    char s[MAX], c;

    leLinha(s);
    c = getchar();
    apagaCaracter(s, c);
    printf("%s", s);

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
  "source_sha256": "3589ce592ad7dd62d59ff11d2cd64e4f0df9b332432ebeff8439f6bfe200a652",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail",
    "ex07_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "ol deus"
    },
    {
      "test_id": "ex07_1",
      "input": "ddd\nd",
      "expected": "\n",
      "output": ""
    },
    {
      "test_id": "ex07_2",
      "input": "abdddba\nh",
      "expected": "abdddba\n",
      "output": "abdddba"
    },
    {
      "test_id": "ex07_3",
      "input": "aaaaaaaaaaaaaaaaaa\na",
      "expected": "\n",
      "output": ""
    },
    {
      "test_id": "ex07_4",
      "input": "aaaaaxaaaaaaaaaaaa\na",
      "expected": "x\n",
      "output": "x"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "test:ex07_4": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "0",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "small",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "large",
    "stdout:ex07_4:relation": "whitespace",
    "stdout:ex07_4:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "test:ex07_4": "fail",
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
    "ast:c_address_of": "0",
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
    scanf("%c", &c);
    apagaCaracter(s,c);
    printf ("%s\n", s);
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
  "source_sha256": "cf156ffdeefa652b7ff7df11d14a077244b79fd1fd8a5c49583855aa8db00d89",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail",
    "ex07_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "ol deus\n\n"
    },
    {
      "test_id": "ex07_1",
      "input": "ddd\nd",
      "expected": "\n",
      "output": "\n\n"
    },
    {
      "test_id": "ex07_2",
      "input": "abdddba\nh",
      "expected": "abdddba\n",
      "output": "abdddba\n\n"
    },
    {
      "test_id": "ex07_3",
      "input": "aaaaaaaaaaaaaaaaaa\na",
      "expected": "\n",
      "output": "\n\n"
    },
    {
      "test_id": "ex07_4",
      "input": "aaaaaxaaaaaaaaaaaa\na",
      "expected": "x\n",
      "output": "x\n\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "small",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium",
    "stdout:ex07_4:relation": "whitespace",
    "stdout:ex07_4:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
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


## sample_008 — train

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
    scanf("%c", &c);
    getchar(); 
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
  "source_sha256": "39703a16db29810fbc1a95a482bdefa15bc0739e6aaa08017226409f1b9cf982",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail",
    "ex07_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "ol deus\n\n"
    },
    {
      "test_id": "ex07_1",
      "input": "ddd\nd",
      "expected": "\n",
      "output": "\n\n"
    },
    {
      "test_id": "ex07_2",
      "input": "abdddba\nh",
      "expected": "abdddba\n",
      "output": "abdddba\n\n"
    },
    {
      "test_id": "ex07_3",
      "input": "aaaaaaaaaaaaaaaaaa\na",
      "expected": "\n",
      "output": "\n\n"
    },
    {
      "test_id": "ex07_4",
      "input": "aaaaaxaaaaaaaaaaaa\na",
      "expected": "x\n",
      "output": "x\n\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "small",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium",
    "stdout:ex07_4:relation": "whitespace",
    "stdout:ex07_4:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
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


## sample_009 — train

```c

#include <stdio.h>
#include <string.h>


void apagaCaracter(char s[], char c) {
    int i, j;

    for (i = 0, j = 0; s[i] != '\0'; i++) {
        if (s[i] != c) {
            s[j++] = s[i];
        }
    }

    s[j] = '\0';
}

int main() {
    char linha[100];
    char caractere;

    
    fgets(linha, sizeof(linha), stdin);   

    
    scanf("%c", &caractere);

    
    apagaCaracter(linha, caractere);

    
    printf("%s\n", linha);

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
  "source_sha256": "5d1f7b19d030cf3d32437f21d6884671a2895ba28aa0d295c3266aa63fce45d6",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail",
    "ex07_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "ol deus\n\n"
    },
    {
      "test_id": "ex07_1",
      "input": "ddd\nd",
      "expected": "\n",
      "output": "\n\n"
    },
    {
      "test_id": "ex07_2",
      "input": "abdddba\nh",
      "expected": "abdddba\n",
      "output": "abdddba\n\n"
    },
    {
      "test_id": "ex07_3",
      "input": "aaaaaaaaaaaaaaaaaa\na",
      "expected": "\n",
      "output": "\n\n"
    },
    {
      "test_id": "ex07_4",
      "input": "aaaaaxaaaaaaaaaaaa\na",
      "expected": "x\n",
      "output": "x\n\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "small",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium",
    "stdout:ex07_4:relation": "whitespace",
    "stdout:ex07_4:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
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


## sample_010 — train

```c

#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX 80

void apagaCaracter(char s[], char c)
{
    char aux[MAX];
    int i, j = 0;
    aux[0] = '\0';
    fgets(s, MAX, stdin);
    scanf("%c", &c);
    for(i = 0; s[i] != '\n' && s[i] != '\0' && i < (int) strlen(s); i++){
        if(s[i] != c) {
            aux[j] = s[i];
            j++;
        }
    }
    for(i = 0; aux[i] != '\0' && i < (int) strlen(aux); i++){
        s[i] = aux[i];
    }
    s[i] = '\0';
}

int main()
{
    char c = '\0', s[MAX];
    apagaCaracter(s, c);
    printf("%s", s);
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
  "source_sha256": "1389b11485c12d9a5c71feeb863fa1998b0cde3446a609f95e8b34131e6d0c25",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail",
    "ex07_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "ol deus"
    },
    {
      "test_id": "ex07_1",
      "input": "ddd\nd",
      "expected": "\n",
      "output": ""
    },
    {
      "test_id": "ex07_2",
      "input": "abdddba\nh",
      "expected": "abdddba\n",
      "output": "abdddba"
    },
    {
      "test_id": "ex07_3",
      "input": "aaaaaaaaaaaaaaaaaa\na",
      "expected": "\n",
      "output": ""
    },
    {
      "test_id": "ex07_4",
      "input": "aaaaaxaaaaaaaaaaaa\na",
      "expected": "x\n",
      "output": "x"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "test:ex07_4": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_zero_index": "1",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "small",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "large",
    "stdout:ex07_4:relation": "whitespace",
    "stdout:ex07_4:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "test:ex07_4": "fail",
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


## sample_011 — train

```c

#include <stdio.h>
#include <string.h>
#define MAX 100
void apagaCaracter(char s[], char c)
{
    int quantidade = strlen(s), i;
    for (i = 0; i < quantidade; i++){
        if (s[i] != c){
            printf("%c", s[i]);
        }
    }
    printf("\n");
}
int main()
{
    char s[MAX], c;
    fgets(s, sizeof(s), stdin);
    scanf("%c", &c);
    apagaCaracter(s, c);
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
  "source_sha256": "965cc8e4d8eb077d4d0340ce649690c2275556e71e5f89991bdc67b53f0caee4",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail",
    "ex07_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "ol deus\n\n"
    },
    {
      "test_id": "ex07_1",
      "input": "ddd\nd",
      "expected": "\n",
      "output": "\n\n"
    },
    {
      "test_id": "ex07_2",
      "input": "abdddba\nh",
      "expected": "abdddba\n",
      "output": "abdddba\n\n"
    },
    {
      "test_id": "ex07_3",
      "input": "aaaaaaaaaaaaaaaaaa\na",
      "expected": "\n",
      "output": "\n\n"
    },
    {
      "test_id": "ex07_4",
      "input": "aaaaaxaaaaaaaaaaaa\na",
      "expected": "x\n",
      "output": "x\n\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "test:ex07_4": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "1",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "small",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium",
    "stdout:ex07_4:relation": "whitespace",
    "stdout:ex07_4:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "test:ex07_4": "fail",
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


## sample_012 — train

```c

#include <stdio.h>

void apagaCaracter(char s[], char c){
    int i = 0;
    while(s[i] != EOF && s[i] != '\0'){
        if (s[i] != c){
            putchar(s[i]);
        }
        i++;
    }
    putchar('\n');
}

int main(){
    char s[100], chara;
    fgets(s, sizeof(s), stdin);
    chara = getchar();
    apagaCaracter(s, chara);
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
  "source_sha256": "0d6b4ab35ff02a72f2124ff2fa1fc47edea5198a61a0b97041cb41a5a803d75d",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail",
    "ex07_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "ol deus\n\n"
    },
    {
      "test_id": "ex07_1",
      "input": "ddd\nd",
      "expected": "\n",
      "output": "\n\n"
    },
    {
      "test_id": "ex07_2",
      "input": "abdddba\nh",
      "expected": "abdddba\n",
      "output": "abdddba\n\n"
    },
    {
      "test_id": "ex07_3",
      "input": "aaaaaaaaaaaaaaaaaa\na",
      "expected": "\n",
      "output": "\n\n"
    },
    {
      "test_id": "ex07_4",
      "input": "aaaaaxaaaaaaaaaaaa\na",
      "expected": "x\n",
      "output": "x\n\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "test:ex07_4": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_zero_index": "0",
    "ast:c_one_index": "0",
    "ast:c_address_of": "0",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "small",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium",
    "stdout:ex07_4:relation": "whitespace",
    "stdout:ex07_4:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
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
    "ast:c_address_of": "0",
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

int leLinha(char s[]){
    int c, i = 0;
    while((c = getchar()) != '\n' && c != EOF){
        s[i++] = c;
    }
    s[i] = '\0';
    return c;
}

void apagaCaracter(char s[], char c){
    int i, n = 0;
    for(i = 0; s[i] != '\0'; i++){
        n +=1;
    }
    for(i = 0; i < n; i++){
        if(s[i] == c){
            s[i] = ' ';
        }
    }
}

int main(){
    char s[80] = "", c;
    leLinha(s);
    scanf(" %c", &c);
    apagaCaracter(s, c);
    printf("%s\n", s);
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
  "source_sha256": "0f896d711686a7e13d343ee34b5df8d89691303206e6e1a0a399e575fe195f4a",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "pass",
    "ex07_3": "fail",
    "ex07_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "ol   deus\n"
    },
    {
      "test_id": "ex07_1",
      "input": "ddd\nd",
      "expected": "\n",
      "output": "   \n"
    },
    {
      "test_id": "ex07_3",
      "input": "aaaaaaaaaaaaaaaaaa\na",
      "expected": "\n",
      "output": "                  \n"
    },
    {
      "test_id": "ex07_4",
      "input": "aaaaaxaaaaaaaaaaaa\na",
      "expected": "x\n",
      "output": "     x            \n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "pass",
    "test:ex07_3": "fail",
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "__unknown__",
    "stdout:ex07_2:edit_band": "__unknown__",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "large",
    "stdout:ex07_4:relation": "whitespace",
    "stdout:ex07_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "pass",
    "test:ex07_3": "fail",
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


## sample_016 — train

```c

#include <stdio.h>

int leLinha(char s[]){
    int c, i = 0;
    while((c = getchar()) != '\n' && c != EOF){
        s[i++] = c;
    }
    s[i] = '\0';
    return c;
}

void apagaCaracter(char s[], char c){
    int i, n = 0;
    for(i = 0; s[i] != '\0'; i++){
        n +=1;
    }
    for(i = 0; i < n; i++){
        if(s[i] == c){
            s[i] = ' ';
        }
    }
}

int main(){
    char s[80] = "", c;
    leLinha(s);
    scanf("%c", &c);
    apagaCaracter(s, c);
    printf("%s\n", s);
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
  "source_sha256": "6b0adfc5368bf41bfebad039e251f02eef71dd626df069aac4223df52cd3f6c7",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "pass",
    "ex07_3": "fail",
    "ex07_4": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "ola adeus\na",
      "expected": "ol deus\n",
      "output": "ol   deus\n"
    },
    {
      "test_id": "ex07_1",
      "input": "ddd\nd",
      "expected": "\n",
      "output": "   \n"
    },
    {
      "test_id": "ex07_3",
      "input": "aaaaaaaaaaaaaaaaaa\na",
      "expected": "\n",
      "output": "                  \n"
    },
    {
      "test_id": "ex07_4",
      "input": "aaaaaxaaaaaaaaaaaa\na",
      "expected": "x\n",
      "output": "     x            \n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "pass",
    "test:ex07_3": "fail",
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
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "large",
    "stdout:ex07_2:relation": "__unknown__",
    "stdout:ex07_2:edit_band": "__unknown__",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "large",
    "stdout:ex07_4:relation": "whitespace",
    "stdout:ex07_4:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "pass",
    "test:ex07_3": "fail",
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
  "members/sample_001/tests/ex07_1",
  "members/sample_001/tests/ex07_3",
  "members/sample_001/tests/ex07_4",
  "members/sample_002/raw_code",
  "members/sample_002/tests/ex07_0",
  "members/sample_002/tests/ex07_1",
  "members/sample_002/tests/ex07_3",
  "members/sample_002/tests/ex07_4",
  "members/sample_003/raw_code",
  "members/sample_003/tests/ex07_0",
  "members/sample_003/tests/ex07_1",
  "members/sample_003/tests/ex07_3",
  "members/sample_003/tests/ex07_4",
  "members/sample_004/raw_code",
  "members/sample_004/tests/ex07_0",
  "members/sample_004/tests/ex07_1",
  "members/sample_004/tests/ex07_2",
  "members/sample_004/tests/ex07_3",
  "members/sample_004/tests/ex07_4",
  "members/sample_005/raw_code",
  "members/sample_005/tests/ex07_0",
  "members/sample_005/tests/ex07_1",
  "members/sample_005/tests/ex07_2",
  "members/sample_005/tests/ex07_3",
  "members/sample_005/tests/ex07_4",
  "members/sample_006/raw_code",
  "members/sample_006/tests/ex07_0",
  "members/sample_006/tests/ex07_1",
  "members/sample_006/tests/ex07_2",
  "members/sample_006/tests/ex07_3",
  "members/sample_006/tests/ex07_4",
  "members/sample_007/raw_code",
  "members/sample_007/tests/ex07_0",
  "members/sample_007/tests/ex07_1",
  "members/sample_007/tests/ex07_2",
  "members/sample_007/tests/ex07_3",
  "members/sample_007/tests/ex07_4",
  "members/sample_008/raw_code",
  "members/sample_008/tests/ex07_0",
  "members/sample_008/tests/ex07_1",
  "members/sample_008/tests/ex07_2",
  "members/sample_008/tests/ex07_3",
  "members/sample_008/tests/ex07_4",
  "members/sample_009/raw_code",
  "members/sample_009/tests/ex07_0",
  "members/sample_009/tests/ex07_1",
  "members/sample_009/tests/ex07_2",
  "members/sample_009/tests/ex07_3",
  "members/sample_009/tests/ex07_4",
  "members/sample_010/raw_code",
  "members/sample_010/tests/ex07_0",
  "members/sample_010/tests/ex07_1",
  "members/sample_010/tests/ex07_2",
  "members/sample_010/tests/ex07_3",
  "members/sample_010/tests/ex07_4",
  "members/sample_011/raw_code",
  "members/sample_011/tests/ex07_0",
  "members/sample_011/tests/ex07_1",
  "members/sample_011/tests/ex07_2",
  "members/sample_011/tests/ex07_3",
  "members/sample_011/tests/ex07_4",
  "members/sample_012/raw_code",
  "members/sample_012/tests/ex07_0",
  "members/sample_012/tests/ex07_1",
  "members/sample_012/tests/ex07_2",
  "members/sample_012/tests/ex07_3",
  "members/sample_012/tests/ex07_4",
  "members/sample_013/raw_code",
  "members/sample_013/tests/ex07_0",
  "members/sample_013/tests/ex07_1",
  "members/sample_013/tests/ex07_2",
  "members/sample_013/tests/ex07_3",
  "members/sample_013/tests/ex07_4",
  "members/sample_014/raw_code",
  "members/sample_014/tests/ex07_0",
  "members/sample_014/tests/ex07_1",
  "members/sample_014/tests/ex07_2",
  "members/sample_014/tests/ex07_3",
  "members/sample_014/tests/ex07_4",
  "members/sample_015/raw_code",
  "members/sample_015/tests/ex07_0",
  "members/sample_015/tests/ex07_1",
  "members/sample_015/tests/ex07_3",
  "members/sample_015/tests/ex07_4",
  "members/sample_016/raw_code",
  "members/sample_016/tests/ex07_0",
  "members/sample_016/tests/ex07_1",
  "members/sample_016/tests/ex07_3",
  "members/sample_016/tests/ex07_4"
]
```
