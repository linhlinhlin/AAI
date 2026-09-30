# lab03-ex02--kmeans--combined_stdout--s42--c1

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 99; phân vùng: {'train': 88, 'validation': 11}.


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
    "n_cluster": 99,
    "n_observed": 99,
    "n_failed": 99,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 99
    }
  },
  {
    "test_id": "ex02_1",
    "n_cluster": 99,
    "n_observed": 99,
    "n_failed": 99,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 99
    }
  },
  {
    "test_id": "ex02_2",
    "n_cluster": 99,
    "n_observed": 99,
    "n_failed": 99,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 99
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex02_1:edit_band",
    "value": "small",
    "n": 99,
    "n_cluster": 99,
    "rate": 1.0,
    "cohort_rate": 0.5527638190954773,
    "difference_from_cohort": 0.44723618090452266
  },
  {
    "feature": "stdout:ex02_2:edit_band",
    "value": "small",
    "n": 98,
    "n_cluster": 99,
    "rate": 0.98989898989899,
    "cohort_rate": 0.5527638190954773,
    "difference_from_cohort": 0.4371351708035126
  },
  {
    "feature": "stdout:ex02_0:edit_band",
    "value": "small",
    "n": 93,
    "n_cluster": 99,
    "rate": 0.9393939393939394,
    "cohort_rate": 0.5175879396984925,
    "difference_from_cohort": 0.42180599969544696
  },
  {
    "feature": "stdout:ex02_1:relation",
    "value": "whitespace",
    "n": 97,
    "n_cluster": 99,
    "rate": 0.9797979797979798,
    "cohort_rate": 0.6934673366834171,
    "difference_from_cohort": 0.2863306431145627
  },
  {
    "feature": "stdout:ex02_2:relation",
    "value": "whitespace",
    "n": 97,
    "n_cluster": 99,
    "rate": 0.9797979797979798,
    "cohort_rate": 0.6934673366834171,
    "difference_from_cohort": 0.2863306431145627
  },
  {
    "feature": "stdout:ex02_0:relation",
    "value": "whitespace",
    "n": 99,
    "n_cluster": 99,
    "rate": 1.0,
    "cohort_rate": 0.7386934673366834,
    "difference_from_cohort": 0.2613065326633166
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 92,
    "n_cluster": 99,
    "rate": 0.9292929292929293,
    "cohort_rate": 0.8442211055276382,
    "difference_from_cohort": 0.0850718237652911
  },
  {
    "feature": "ast:c_while",
    "value": "0",
    "n": 72,
    "n_cluster": 99,
    "rate": 0.7272727272727273,
    "cohort_rate": 0.6633165829145728,
    "difference_from_cohort": 0.06395614435815444
  },
  {
    "feature": "ast:c_if",
    "value": "0",
    "n": 34,
    "n_cluster": 99,
    "rate": 0.3434343434343434,
    "cohort_rate": 0.3015075376884422,
    "difference_from_cohort": 0.04192680574590124
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "0",
    "n": 12,
    "n_cluster": 99,
    "rate": 0.12121212121212122,
    "cohort_rate": 0.10050251256281408,
    "difference_from_cohort": 0.02070960864930714
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 93,
    "n_cluster": 99,
    "rate": 0.9393939393939394,
    "cohort_rate": 0.9246231155778895,
    "difference_from_cohort": 0.014770823816049994
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 99,
    "n_cluster": 99,
    "rate": 1.0,
    "cohort_rate": 0.9899497487437185,
    "difference_from_cohort": 0.01005025125628145
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 98,
    "n_cluster": 99,
    "rate": 0.98989898989899,
    "cohort_rate": 0.9849246231155779,
    "difference_from_cohort": 0.00497436678341201
  },
  {
    "feature": "test:ex02_0",
    "value": "fail",
    "n": 99,
    "n_cluster": 99,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "test:ex02_1",
    "value": "fail",
    "n": 99,
    "n_cluster": 99,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "test:ex02_2",
    "value": "fail",
    "n": 99,
    "n_cluster": 99,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_update",
    "value": "0",
    "n": 1,
    "n_cluster": 99,
    "rate": 0.010101010101010102,
    "cohort_rate": 0.01507537688442211,
    "difference_from_cohort": -0.004974366783412008
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "0",
    "n": 6,
    "n_cluster": 99,
    "rate": 0.06060606060606061,
    "cohort_rate": 0.07537688442211055,
    "difference_from_cohort": -0.014770823816049938
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 87,
    "n_cluster": 99,
    "rate": 0.8787878787878788,
    "cohort_rate": 0.8994974874371859,
    "difference_from_cohort": -0.020709608649307154
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 65,
    "n_cluster": 99,
    "rate": 0.6565656565656566,
    "cohort_rate": 0.6984924623115578,
    "difference_from_cohort": -0.04192680574590124
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 92,
    "n_cluster": 99,
    "rate": 0.9292929292929293,
    "cohort_rate": 0.8442211055276382,
    "difference_from_cohort": 0.0850718237652911
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 93,
    "n_cluster": 99,
    "rate": 0.9393939393939394,
    "cohort_rate": 0.9246231155778895,
    "difference_from_cohort": 0.014770823816049994
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 99,
    "n_cluster": 99,
    "rate": 1.0,
    "cohort_rate": 0.9899497487437185,
    "difference_from_cohort": 0.01005025125628145
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 98,
    "n_cluster": 99,
    "rate": 0.98989898989899,
    "cohort_rate": 0.9849246231155779,
    "difference_from_cohort": 0.00497436678341201
  },
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 99,
    "n_cluster": 99,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 87,
    "n_cluster": 99,
    "rate": 0.8787878787878788,
    "cohort_rate": 0.8994974874371859,
    "difference_from_cohort": -0.020709608649307154
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 65,
    "n_cluster": 99,
    "rate": 0.6565656565656566,
    "cohort_rate": 0.6984924623115578,
    "difference_from_cohort": -0.04192680574590124
  }
]
```


## IF–THEN dự đoán cluster, không dự đoán gold

```json
[
  {
    "rule_id": 5,
    "if": [
      "NOT (stdout:ex02_1:relation=whitespace)",
      "stdout:ex02_2:edit_band=small",
      "stdout:ex02_0:relation=whitespace"
    ],
    "then_cluster": 1,
    "train_support": 2,
    "train_precision": 1.0,
    "holdout_support": 0,
    "holdout_precision": null
  },
  {
    "rule_id": 9,
    "if": [
      "stdout:ex02_1:relation=whitespace",
      "stdout:ex02_1:edit_band=small",
      "NOT (stdout:ex02_2:edit_band=medium)"
    ],
    "then_cluster": 1,
    "train_support": 85,
    "train_precision": 1.0,
    "holdout_support": 11,
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
  "reasoning": "Có 99 bài trong cụm. Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
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

sample_009, sample_074, sample_019, sample_001

## sample_001 — train — đại diện

```c
#include <stdio.h>

void piramide(int N)
{
	int i, j;

	for(i = 0; i < N; i++)
	{
		for(j = 1; j < N-i; j++)
			printf("  ");
		for(j = 1; j < 1+i; j++)
			printf("%d ", j);
		for(j = 1+i; j > 0; j--)
			printf("%d ", j);
		printf("\n");
	}
}

int main()
{
	int in;
	scanf("%d", &in);

	piramide(in);

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
  "source_sha256": "f3aabe73d2e0b2727f63293025c13026dd3686d2551fea345563c5521b269d3c",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_009 — train — đại diện

```c
#include <stdio.h>




void piramide(int N)
{
    int i, j;
    for (i = 1; i<= N; i++)
    {
        for(j = 0; j < N - i; j++)
        {
            printf(" ");
            printf(" ");
        }
        
        for(j = 1; j <= i; j++)
        {
            printf("%d", j);
            printf(" ");
        }

        for(j = i - 1; j > 1; j--)
        {
            printf("%d", j);
            printf(" ");
        }
    if (i != 1)
        printf("1\n");
    else
        printf("\n");
    }
}


int main()
{
    int N;
    scanf("%d", &N);
    piramide(N);
    return 0;
}
```

```json
{
  "sample_id": "sample_009",
  "partition": "train",
  "representative": true,
  "is_train_medoid": true,
  "raw_code_truncated": false,
  "source_sha256": "01e1b5f199af5a10a8dddafef37c962503a1ec59f29dc03817f752a2a590bc8b",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_019 — train — đại diện

```c
# include <stdio.h>

void piramide(int N){
    int num=1,cont=1,num_espacos=N,N1=cont;
    while(cont<=N){
        while(num_espacos!=1){
            printf("  ");
            num_espacos-=1;
        }
        num_espacos=N-cont;
        if (cont==1){
            printf("%d",cont);
        }
        else{
            while(num<cont){
                printf("%d ",num);
                num+=1;
            }
            while(N1>=1){
                printf("%d ",N1);
                N1-=1;
            }
        }
        num=1;
        cont+=1;
        N1=cont;
        printf("\n");
    }
}
int main(){
    int N;
    scanf("%d",&N);
    piramide(N);
    return 0;
}
```

```json
{
  "sample_id": "sample_019",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "37cf12d45cd88353579182113a9c9073a54e2d57e7208427a9d3f743d1bed676",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1\n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1\n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1\n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_074 — train — đại diện

```c


#include <stdio.h>

void piramide(int n) {
    int vc = 1, espaco = n - 1, vg = 0, num = 1;
    while (vc - 1 != n) {
        while (vg < espaco) {
            printf("  ");
            vg++;
        }
        espaco--;
        vg = 0;
        while (num - 1 != vc) {
            printf("%d ", num);
            num++; 
        }
        num -= 1;
        while (num != 1) {
            num--;
            printf("%d ", num);
        }
        printf("\n");
        vc++;
    }
}

int main () {
    int n;
    scanf("%d", &n);
    piramide(n);
    return 0;
}
```

```json
{
  "sample_id": "sample_074",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "7835d3ce506d21d7db60adbe68a8a901d8356ab8e0fb220ceb38901dae178db7",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_002 — train

```c
#include <stdio.h>

#define LINHA_INICIAL 1
#define NUM_INICIAL 1
#define DIMINUI -1
#define AUMENTA 1
#define NUM_INICIAL_COLOCADOS 0

void piramide(int n)
{
	int linha;
	int num;
	int passo;

	int num_colocados;
	int max_colocados;
	int num_max;
	int espacos;
	int num_espacos;

	for (linha = LINHA_INICIAL; linha <= n; linha++) 
	{
		num = NUM_INICIAL;
		max_colocados = linha*2-1;
		num_max = linha;
		passo = AUMENTA;
		num_espacos = (n-linha+1)*2;
		
		for (espacos = 0; espacos < num_espacos; espacos++)
		{
			putchar(' ');
		}

		for (num_colocados = NUM_INICIAL_COLOCADOS; num_colocados < max_colocados-1; num_colocados++)
		{
			printf("%d ", num);
			if (num == num_max) {
				passo = DIMINUI;}
			num += passo;
		}
		printf("%d\n", num);
	}
}
int main()
{
	int n;
	scanf("%d", &n);
	piramide(n);
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
  "source_sha256": "25e0469b9950ed858598d4ece5de3aa633767a43dd7157d142d9761e8184bbc8",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "      1\n    1 2 1\n  1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "        1\n      1 2 1\n    1 2 3 2 1\n  1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "                1\n              1 2 1\n            1 2 3 2 1\n          1 2 3 4 3 2 1\n        1 2 3 4 5 4 3 2 1\n      1 2 3 4 5 6 5 4 3 2 1\n    1 2 3 4 5 6 7 6 5 4 3 2 1\n  1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_003 — validation

```c
#include <stdio.h>

void piramide(int N)
{ 
	
 	int i, n_linha, dig, n_espacos = 2*N;

 	for (n_linha = 1; n_linha <= N; ++n_linha)
 	{
 		n_espacos = n_espacos - 2;

 		for (i=0; i < n_espacos; ++i)
 			printf(" ");

 		
 		for (dig=1; dig < n_linha; ++dig)
 			printf("%d ", dig);

 		
 		for (; dig>=1; --dig)
 			printf("%d ", dig);

 		printf("\n");

 	}

}


int main()
{
	int n;

	scanf("%d", &n);
	piramide(n);
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
  "source_sha256": "73334189ccef5604d1e6b31e5de5cfc0414ce593f853b2e570f354ca8f363c74",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_004 — train

```c
#include <stdio.h>

void piramide(int N) {
	int coluna, linha;
	
	for (linha = 1; linha <= N; linha++) {
		for (coluna = 1; coluna <= N-linha; coluna++) {
			printf("  ");
		}
		for (coluna = 1; coluna <= linha; coluna++) {
			printf("%d ", coluna);
		}
		for (coluna = linha-1; coluna >= 1; coluna--) {
			printf("%d ", coluna);
		}
		printf("\n");
	}

	return;

}

int main() {
	int N;

	scanf("%d", &N);

	piramide(N);

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
  "source_sha256": "c8c93eb57bf6b4e5f6807fb30e7be4278874e35dfc8a585a36777e19daf30df9",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_005 — train

```c
#include <stdio.h>

void piramide(int N) {
    int x, pos, cn=N, col;
    for (col=1; col<=N; col++, --cn) {
        for (pos=1 ; pos<((2*cn)-1) ; ++pos) {
            printf(" ");
        }
        for (x=1;x<=col;++x) {
            printf("%d ", x);
        }
        for (x=x-2;x>=1;--x) {
            printf("%d ", x);
            
        }
        printf("\n");
    }
}

int main() {
	int N;
	scanf("%d", &N);
	while (N < 2) {
		scanf("%d", &N);
	}
	piramide(N);
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
  "source_sha256": "bc5024fd8e62693c0bf70386aacbe858a478e1c0109f1f049743dc3c17d17283",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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

void piramide(int N) {
    int x, pos, cn=N, col;
    for (col=1; col<=N; col++, --cn) {
        for (pos=1 ; pos<((2*cn)-1) ; ++pos) {
            printf(" ");
        }
        for (x=1;x<=col;++x) {
            printf("%d ", x);
        }
        for (x=x-2;x>=1;--x) {
            printf("%d", x);
            if (x != 1) {
                printf(" ");
            }
        }
        printf("\n");
    }
}

int main() {
	int N;
	scanf("%d", &N);
	while (N < 2) {
		scanf("%d", &N);
	}
	piramide(N);
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
  "source_sha256": "f0081bcff3802663cc358cac41a0bf8f398bb53b6695f4294e1e0d011100bfc7",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_007 — train

```c
#include <stdio.h>

void piramide(int n){
    int i = 1, j, k;
    while(i <= n){
        j = 1;
        while(j <= 2*n){
            if(j > n){
                k = n - (j - n);
            } else {
                k = j;
            }
            k = k - (n - i);
            if(j <= n || k >= 1){
                if(k <= 0){
                    printf("%c", ' ');
                } else {
                    printf("%d", k);
                }
                if(j < 2*n){
                    printf("%c", ' ');
                }
            }
            j++;
        }
        printf("\n");
        i++;
    }
}

int main(){
    int n;
    scanf("%d", &n);
    piramide(n);
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
  "source_sha256": "41cc41b755d636803ebc8b12f2105ba64e1f1cd23465f74dacc2d5c89f13d398",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_008 — train

```c
#include <stdio.h>




void piramide(int N)
{
    int i, j, k;
    for (i = 1; i<= N; i++)
    {
        for(j = 0; j < N - i; j++)
        {
            printf(" ");
            printf(" ");
        }
        
        for(j = 1; j <= i; j++)
        {
            printf("%d", j);
            printf(" ");
        }

        for(k = i - 1; k >= 1; --k)
        {
            printf("%d", k);
            printf(" ");
        }
    printf("\n");
    }
}


int main()
{
    int N;
    scanf("%d", &N);
    piramide(N);
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
  "source_sha256": "62b4fb3ad8a38c0771b4e968c65b51508de6e37c87334587ec199beb5ce9ae89",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_010 — train

```c
#include <stdio.h>

void piramide(int n)
{
 int linhas,coluna,col=0,espacos;
 for (linhas=1; linhas<=n; linhas++)
 {
  espacos = n-linhas;
  for (; espacos !=0; espacos--)
     printf("  ");
  col = linhas;
  for(coluna=1;coluna<=(linhas*2 -1); coluna++)
  {
   if (coluna<=linhas)
      printf ("%d ",coluna);
   else
      {
      col--;
      if (coluna==(linhas*2 -1))
          printf ("%d", col);
      else
          printf ("%d ",col);
      }
  }
  printf("\n");
 }
 return;
}


int main()
{
 int n;
 scanf("%d",&n);
 if (n>=2)
 {
  piramide(n);
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
  "source_sha256": "2225f426eb04755b964781fa06f605969d363d83f208ea37c5e76b311605548b",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_011 — train

```c
#include <stdio.h>

void piramide(int n)
{
 int linhas,coluna,col=0,espacos;
 for (linhas=1; linhas<=n; linhas++)
 {
  espacos = n-linhas;
  for (; espacos !=0; espacos--)
     printf("  ");
  col = linhas;
  for(coluna=1;coluna<=(linhas*2 -1); coluna++)
  {
   if (coluna<=linhas)
      printf ("%d ",coluna);
   else
      {
      col--;
     
          printf ("%d ",col);
      }
  }
  printf("\n");
 }
 return;
}


int main()
{
 int n;
 scanf("%d",&n);
 if (n>=2)
 {
  piramide(n);
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
  "source_sha256": "bd2bcbcd2c94eb2da045839cf55e0f4b585d02de05518a2ad4381fec02fda4cc",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_012 — train

```c
#include <stdio.h>

void piramide(int n)
{
	int i, j;
	for(i = 1; i <= n; i++){
		for(j = 0; j <= 2 * (n - i); j++){
			printf(" ");}
		for(j = 1; j <= i; j++){
			printf("%d ", j);}
		for(j = i - 1; j > 0; j--){
			printf("%d ", j);}
		printf("\n");
		}
}

int main()
{
	int n;
	scanf("%d", &n);
	piramide(n);
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
  "source_sha256": "03c75e4d2aedaa0d8d086da33b19d99c077a7b37cad7e2099c7d5964ae553cc8",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "     1 \n   1 2 1 \n 1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1 \n     1 2 1 \n   1 2 3 2 1 \n 1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1 \n             1 2 1 \n           1 2 3 2 1 \n         1 2 3 4 3 2 1 \n       1 2 3 4 5 4 3 2 1 \n     1 2 3 4 5 6 5 4 3 2 1 \n   1 2 3 4 5 6 7 6 5 4 3 2 1 \n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_013 — train

```c
#include <stdio.h>

void piramide(int n)
{
	int i, j;
	for(i = 1; i <= n; i++){
		for(j = 0; j <= 2 * (n - i); j++){
			printf(" ");}
		for(j = 1; j <= i; j++){
			printf("%d ", j);}
		for(j = i - 1; j > 0; j--){
			if (j == 1){
				printf("1");}
			else{
				printf("%d ", j);}}
		printf("\n");
		}
}

int main()
{
	int n;
	scanf("%d", &n);
	piramide(n);
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
  "source_sha256": "ba46b4c80eb50f48e1b76afd608d6c3da565e0faf381ac2413cbe688d606c337",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "     1 \n   1 2 1\n 1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1 \n     1 2 1\n   1 2 3 2 1\n 1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1 \n             1 2 1\n           1 2 3 2 1\n         1 2 3 4 3 2 1\n       1 2 3 4 5 4 3 2 1\n     1 2 3 4 5 6 5 4 3 2 1\n   1 2 3 4 5 6 7 6 5 4 3 2 1\n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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

void piramide(int n)
{
	int i, j;
	for(i = 1; i <= n; i++){
		for(j = 1; j <= 2 * (n - i); j++){
			printf(" ");}
		for(j = 1; j <= i; j++){
			printf("%d ", j);}
		for(j = i - 1; j > 0; j--){
			if (j == 1){
				printf("1");}
			else{
				printf("%d ", j);}}
		printf("\n");
		}
}

int main()
{
	int n;
	scanf("%d", &n);
	piramide(n);
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
  "source_sha256": "1fc6e9413e36f79c9bd087c3e2cb365035780ba7c75f82b988eb5173e2b9d76f",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_015 — train

```c
#include <stdio.h>

void piramide(int N)
{
    int cont, N1 = 1, i;
    for (cont = 1; cont <= N; cont++)
    {
        for (i = 1; i < (N + 1 - cont); i++)
            printf("  ");
        for (N1 = 1; N1 < cont; N1++)
            printf("%d ", N1);
        for (N1 = cont; N1 > 0; N1--)
            printf("%d ", N1);
        printf("\n");
    }
}
int main()
{
    int n;
    scanf("%d", &n);
    piramide(n);
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
  "source_sha256": "6cb24ea1b2da49185a75608e7296c5253f38a9da741aed904efad7844bb97257",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_016 — validation

```c
#include <stdio.h>

void piramide(int N);

int main()
{
    int N;
   
    scanf("%d", &N);
   
    piramide(N);
   
    return 0;
}

void piramide(int N)
{
    int i, j;
   
    for(i = 1; i <= N; i++)
    {
        for(j = 1; j <= 2 * (N - i); j++)
            putchar(' ');
       
        for(j = 1; j <= i; j++)
            printf("%d ", j);
       
        for(j = i - 1; j >= 1; j--)
            printf("%d ", j);
       
        printf("\n");
    }
}
```

```json
{
  "sample_id": "sample_016",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "92614ba772e1c1789314a60a3da0da87b9a95143ff8d0542c59b5f6fda685ab4",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_017 — validation

```c
#include <stdio.h>

void piramide(int N);

int main()
{
    int N;
   
    scanf("%d", &N);
   
    piramide(N);
   
    return 0;
}

void piramide(int N)
{
    int i, j;
   
    for(i = 1; i <= N; i++)
    {
        for(j = 1; j <= 2 * (N - i); j++)
            putchar(' ');
       
        for(j = 1; j <= i; j++)
        {
            if(i == 1)
                printf("%d", j);
            else
                printf("%d ", j);
        }
       
        for(j = i - 1; j >= 1; j--)
            printf("%d ", j);
        
        printf("\n");
    }
}
```

```json
{
  "sample_id": "sample_017",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "6280d59d9c1c71fbb344d88033b67c0d8304634f9f2b248e6f6fce6d6ed02756",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1\n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1\n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1\n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_018 — train

```c
#include <stdio.h>

void piramide(int n);

int main()
{
	int n;
	scanf("%d", &n);
	piramide(n);
	return 0;
}

void piramide(int n)
{
	int i, j;
	for(i = 1; i <= n; i++) {
		for(j = i - n + 1; j <= i; j++) {
			if(j > 0)
				printf("%d", j);
			else
				printf(" ");
			printf(" ");
		}
		for(j = i - 1; j > 0; j--) {
			printf("%d ", j);
		}
		printf("\n");
	}
}

```

```json
{
  "sample_id": "sample_018",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "06bbee79886edd1be7bd2f9fe2c53e07ae08fe5594cf864bf16137702319939f",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_020 — train

```c

#include <stdio.h>

void piramide(int n);

int main() {

    int N;
    scanf("%d", &N);
    piramide(N);
    return 0;
}

void piramide(int n) {

    int i, j;
    int s;

    for (s = 0; s <= n; s++) {
        putchar(' ');
    }

    printf("1\n");

    

    for (j = 2; j <= n; j++) {

        for (s = 0; s < n - j + 1; s++) {
            putchar(' ');
        }

        for (i = 1; i <= j; i++) {
            printf("%d ", i);
        } 
        for (i = j-1; i >= 1; i--) {
            if (i == 1) {
                printf("%d\n", i);
                break;
            } 
            printf("%d ", i);
        }

    }
}
```

```json
{
  "sample_id": "sample_020",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "59f0df162445523bba7d187102883790646e0b83ad44242ed87610f78f102729",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1\n  1 2 1\n 1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "     1\n   1 2 1\n  1 2 3 2 1\n 1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "         1\n       1 2 1\n      1 2 3 2 1\n     1 2 3 4 3 2 1\n    1 2 3 4 5 4 3 2 1\n   1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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

void piramide(int n) {
    int i, j;

    for (i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++) {
            if (j)
                putchar(' ');
            if (i + j - n > 0) 
                printf("%d", i + j - n);
            else
                putchar(' ');
        }
        for (j--; j > 0; j--) {  
            if (i + j - n - 1> 0) 
                printf(" %d", i + j - n - 1);
        }
        if (i > n)
            putchar('\n');
    }
}

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
    
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
  "source_sha256": "c088803f9b1c0bbf9fdb4d46735502fb2fd8936d6b55314f16b78d56b106bbae",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "     1   1 2 1 1 2 3 2 1"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1     1 2 1   1 2 3 2 1 1 2 3 4 3 2 1"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1             1 2 1           1 2 3 2 1         1 2 3 4 3 2 1       1 2 3 4 5 4 3 2 1     1 2 3 4 5 6 5 4 3 2 1   1 2 3 4 5 6 7 6 5 4 3 2 1 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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

void piramide(int n) {
    int i, j;

    for (i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++) {
            if (j)
                putchar(' ');
            if (i + j - n > 0) 
                printf("%d", i + j - n);
            else
                putchar(' ');
        }
        for (j--; j > 0; j--) {  
            if (i + j - n - 1> 0) 
                printf(" %d", i + j - n - 1);
        }
        putchar('\n');
    }
}

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
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
  "source_sha256": "ddf24a4f89d209eccb593ff24147fb1d329ecdc3bb1e2f3e4385be18a116dfe7",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "     1\n   1 2 1\n 1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1\n     1 2 1\n   1 2 3 2 1\n 1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1\n             1 2 1\n           1 2 3 2 1\n         1 2 3 4 3 2 1\n       1 2 3 4 5 4 3 2 1\n     1 2 3 4 5 6 5 4 3 2 1\n   1 2 3 4 5 6 7 6 5 4 3 2 1\n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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

void piramide(int n) {
    int i, j;

    for (i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++) {
            if (j)
                putchar(' ');
            if (i + j - n > 0) 
                printf("%d", i + j - n);
            else
                putchar(' ');
        }
        for (j--; j > 0; j--) {  
            if (i + j - n - 1> 0) 
                printf(" %d", i + j - n - 1);
        }
        if (i > n)
            putchar('\n');
    }
}

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
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
  "source_sha256": "695814a65e5cfefa880feb133595eaff775ca757ef037bd5f0380f28d39f25b6",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "     1   1 2 1 1 2 3 2 1"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1     1 2 1   1 2 3 2 1 1 2 3 4 3 2 1"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1             1 2 1           1 2 3 2 1         1 2 3 4 3 2 1       1 2 3 4 5 4 3 2 1     1 2 3 4 5 6 5 4 3 2 1   1 2 3 4 5 6 7 6 5 4 3 2 1 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_024 — train

```c


#include <stdio.h>

void piramide(int n) {
    int i, j;

    for (i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++) {
            if (j)
                putchar(' ');
            if (i + j - n > 0) 
                printf("%d", i + j - n);
            else
                putchar(' ');
        }
        for (j--; j > 0; j--) {  
            if (i + j - n - 1> 0) 
                printf(" %d", i + j - n - 1);
        }
        putchar('\n');
    }
}

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
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
  "source_sha256": "ddf24a4f89d209eccb593ff24147fb1d329ecdc3bb1e2f3e4385be18a116dfe7",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "     1\n   1 2 1\n 1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1\n     1 2 1\n   1 2 3 2 1\n 1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1\n             1 2 1\n           1 2 3 2 1\n         1 2 3 4 3 2 1\n       1 2 3 4 5 4 3 2 1\n     1 2 3 4 5 6 5 4 3 2 1\n   1 2 3 4 5 6 7 6 5 4 3 2 1\n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_025 — train

```c


#include <stdio.h>

void piramide(int n) {
    int i, j;

    for (i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++) {
            if (j)
                putchar(' ');
            if (i + j - n > 0) 
                printf("%d", i + j - n);
            else
                putchar(' ');
        }
        for (j--; j > 0; j--) {  
            if (i + j - n - 1> 0) 
                printf(" %d", i + j - n - 1);
        }
        if (i < n)
            putchar('\n');
    }
}

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
    
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
  "source_sha256": "a06816698175e7331e2a44df0e7d8dcf57575c2e52cb2439d29bf6abededcb9d",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "     1\n   1 2 1\n 1 2 3 2 1"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1\n     1 2 1\n   1 2 3 2 1\n 1 2 3 4 3 2 1"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1\n             1 2 1\n           1 2 3 2 1\n         1 2 3 4 3 2 1\n       1 2 3 4 5 4 3 2 1\n     1 2 3 4 5 6 5 4 3 2 1\n   1 2 3 4 5 6 7 6 5 4 3 2 1\n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_026 — train

```c


#include <stdio.h>

void piramide(int n) {
    int i, j;

    for (i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++) {
            if (j)
                putchar(' ');
            if (i + j - n > 0) 
                printf("%d", i + j - n);
            else
                putchar(' ');
        }
        for (j--; j > 0; j--) {  
            if (i + j - n - 1> 0) 
                printf(" %d", i + j - n - 1);
        }
        if (i < n)
            putchar('\n');
    }
}

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);

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
  "source_sha256": "f24c8ce2b8a69ee449b41910b4a8e39ad133ea80e5920a510ec61e972c1652a4",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "     1\n   1 2 1\n 1 2 3 2 1"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1\n     1 2 1\n   1 2 3 2 1\n 1 2 3 4 3 2 1"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1\n             1 2 1\n           1 2 3 2 1\n         1 2 3 4 3 2 1\n       1 2 3 4 5 4 3 2 1\n     1 2 3 4 5 6 5 4 3 2 1\n   1 2 3 4 5 6 7 6 5 4 3 2 1\n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_027 — train

```c


#include <stdio.h>

void piramide(int n) {
    int i, j;

    for (i = 1; i <= n; i++) {
        for (j = 1; j <= n; j++) {
            if (j)
                putchar(' ');
            if (i + j - n > 0) 
                printf("%d", i + j - n);
            else
                putchar(' ');
        }
        for (j--; j > 0; j--) {  
            if (i + j - n - 1> 0) 
                printf(" %d", i + j - n - 1);
        }
        putchar('\n');
    }
}

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);

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
  "source_sha256": "74d616b560947a370f28b6a03fb2037cb17694e8bce4fe0ac42bb5918f6a343f",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "     1\n   1 2 1\n 1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1\n     1 2 1\n   1 2 3 2 1\n 1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1\n             1 2 1\n           1 2 3 2 1\n         1 2 3 4 3 2 1\n       1 2 3 4 5 4 3 2 1\n     1 2 3 4 5 6 5 4 3 2 1\n   1 2 3 4 5 6 7 6 5 4 3 2 1\n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_028 — train

```c

#include <stdio.h>

void piramide(int N){
    int i, j;
    for (i=1; i<=N; i++){
        for (j=N - i; j>0; j--)
            printf("  "); 
        for (j=1; j<=i; j++)
            printf("%d ", j);
        for (j=i-1; j>=1; j--)
            printf("%d ", j);
        
        printf("\n");
              
    }

}


int main(){
    int N;
    scanf("%d", &N);
    while (N<2)
        scanf("%d", &N);
    piramide(N);
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
  "source_sha256": "48e4a281f1f2040eec122305c31a062da06a00d4dfd05a9438bcee3a45f54a84",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_029 — train

```c

#include <stdio.h>

void piramide(int N){
    int i, j;
    for (i=1; i<=N; i++){
        for (j=N - i; j>0; j--)
            printf("  "); 
        for (j=1; j<=i; j++)
            printf("%d ", j);
        for (j=i-1; j>1; j--)
            printf("%d ", j);
        if (j != 0)
            printf("%d\n", j);
        else 
            printf("\n");
              
    }

}


int main(){
    int N;
    scanf("%d", &N);
    while (N<2)
        scanf("%d", &N);
    piramide(N);
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
  "source_sha256": "f1e066ff19d28dcade32660d5a243f130e559b1f3bf92083f444062a544a193e",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_030 — train

```c

#include <stdio.h>

void piramide(int N){

    int contador, j;

    for (contador = 1; contador <= N; contador++){


        for (j = 1; j <= (N - contador); j++){
            printf("  ");
        }

        for (j = 1; j <= contador; j++){
            printf("%d ", j);
        }

        for (j = contador - 1; j >=1 ; j--){
            printf("%d ", j);
        }

        printf("\n");
    } 
    
}

int main(){

    int N;
    scanf("%d", &N);
    piramide(N);
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
  "source_sha256": "2db03c8300f82c6f6219173305f70ed823414a376694870aec5f594d7d5766ac",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_031 — train

```c


#include <stdio.h>

void piramide(int N);

int main(){
    int N;
    scanf("%d", &N);
    piramide(N);
    return 0;
}

void piramide(int N){
    int i,j,k,l = 1,m;
    for (i = N; i > 0; i--){
        
        for (j = 0; j < (i-1)*2; j++){
            putchar(' ');
        }
        for (k = 1; k <= l; k++){
            printf("%d ",k);
        }
        for (m = l-1; m > 0; m--){
            if (m == 1 && i == 1)
            printf("%d", m);
            else
            printf("%d ", m);
        }
        l++;
        if (i != 1)
        putchar('\n');
    }
}
```

```json
{
  "sample_id": "sample_031",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "09d264a037ed4eb94325a0459cdcf1daa7a7805fd875851e18ae43be271d2bbe",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_032 — train

```c


#include <stdio.h>

void piramide(int N);

int main(){
    int N;
    scanf("%d", &N);
    piramide(N);
    return 0;
}

void piramide(int N){
    int i,j,k,l = 1,m;
    for (i = N; i > 0; i--){
        
        for (j = 0; j < (i-1)*2; j++){
            putchar(' ');
        }
        for (k = 1; k <= l; k++){
            printf("%d ",k);
        }
        for (m = l-1; m > 0; m--){
            printf("%d ", m);
        }
        l++;
        putchar('\n');
    }
}
```

```json
{
  "sample_id": "sample_032",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "da5064271b3b7140ab413cf08e14b980138d6adbfa7366a950a25a1cbcc90435",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_033 — train

```c


#include <stdio.h>

void piramide(int N);

int main(){
    int N;
    scanf("%d", &N);
    piramide(N);
    return 0;
}

void piramide(int N){
    int i,j,k,l = 1,m;
    for (i = N; i > 0; i--){
        
        for (j = 0; j < (i-1)*2; j++){
            putchar(' ');
        }
        for (k = 1; k <= l; k++){
            printf("%d ",k);
        }
        for (m = l-1; m > 0; m--){
            if (m == 1 && i == 1)
            printf("%d", m);
            else
            printf("%d ", m);
        }
        l++;
        putchar('\n');
    }
}
```

```json
{
  "sample_id": "sample_033",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "dbee99e0ce710dd071c7f765f6e027a72949b7adbc347828dfe9011e53e12a29",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_034 — train

```c


#include <stdio.h>

void piramide(int N);

int main(){
    int N;
    scanf("%d", &N);
    piramide(N);
    return 0;
}

void piramide(int N){
    int i,j,k,l = 1,m;
    for (i = N; i > 0; i--){
        
        for (j = 0; j < (i-1)*2; j++){
            putchar(' ');
        }
        for (k = 1; k <= l; k++){
            printf(" %d",k);
        }
        for (m = l-1; m > 0; m--){
            printf(" %d", m);
        }
        l++;
        putchar('\n');
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
  "source_sha256": "21b16930a0909a5ead37aed8b69ba95fa219cb10de4192d08a13c0e6efe6b47e",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "     1\n   1 2 1\n 1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1\n     1 2 1\n   1 2 3 2 1\n 1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1\n             1 2 1\n           1 2 3 2 1\n         1 2 3 4 3 2 1\n       1 2 3 4 5 4 3 2 1\n     1 2 3 4 5 6 5 4 3 2 1\n   1 2 3 4 5 6 7 6 5 4 3 2 1\n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_035 — train

```c

#include <stdio.h>

void piramide(int N)
{
    int i, j;

    for (i = 1; i <= N; i++)
    {
        for (j = 1; j <= (N - i) * 2; j++)
        {
            printf(" ");
        }
        for (j = 1; j <= i; j++)
        {
            printf("%d ", j);
        }
        for (j = i - 1; j > 1; j--)
        {
            printf("%d ", j);
        }
        if (i != 1)
        {
            printf("1");
        }
        printf("\n");
    }
}

int main()
{
    int N = 0;

    while (N < 1)
    {
        scanf("%d", &N);
    }

    piramide(N);
    
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
  "source_sha256": "580b55c57f20dd43bfeeabe10ad9e2ccb6d3986a52026a7be326ec38b5a3e6fb",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_036 — train

```c

#include <stdio.h>

void piramide(int N)
{
    int i, j;

    for (i = 1; i <= N; i++)
    {
        for (j = 1; j <= (N - i) * 2; j++)
        {
            printf(" ");
        }
        for (j = 1; j <= i; j++)
        {
            printf("%d ", j);
        }
        for (j = i - 1; j > 1; j--)
        {
            printf("%d ", j);
        }
        if (i != 1)
        {
            printf("1");
        }
        printf("\n");
    }
}

int main()
{
    int N = 0;

    while (N < 1)
    {
        scanf("%d", &N);
    }

    piramide(N);
    
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
  "source_sha256": "580b55c57f20dd43bfeeabe10ad9e2ccb6d3986a52026a7be326ec38b5a3e6fb",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_037 — train

```c

#include <stdio.h>

void piramide(int N)
{
    int i, j;

    for (i = 1; i <= N; i++)
    {
        for (j = 1; j <= (N - i) * 2; j++)
        {
            printf(" ");
        }
        for (j = 1; j <= i; j++)
        {
            printf("%d ", j);
        }
        for (j = i - 1; j > 1; j--)
        {
            printf("%d ", j);
        }
        if (i != 1)
        {
            printf("%d", 1);
        }
        printf("\n");
    }
}

int main()
{
    int N = 0;

    while (N < 1)
    {
        scanf("%d", &N);
    }

    piramide(N);
    
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
  "source_sha256": "d247f4f7cdd5c78d85c23f754d93c60cdf3a09e24b7248f3c174c5d98276133e",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_038 — train

```c

#include <stdio.h>


void piramide(int n)
{
    int keep = n;
    int i, j, k;
    while (keep > 0)
    {
        for (i = 1; i <= (2*keep)-2; i++)
        {
            printf(" ");
        }
        for (j = 1; j <= n - keep + 1; j++)
        {
            printf("%d ", j);
        }
        for (k = n - keep; k >= 1; k--)
        {
            printf("%d ", k);
        }
        printf("\n");
        keep--;
    }
}

int main()
{
    int n;
    scanf("%d", &n);
    if (n < 2)
        return -1;
    piramide(n);
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
  "source_sha256": "c5caef4f8ba2827cbb59a1de9087518141f659fc7fbc16880ec5d0fcc46f60d4",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_039 — train

```c

#include <stdio.h>

void piramide(int n)
{
    int keep = n;
    int i, j, k;
    while (keep > 0)
    {
        for (i = 1; i <= (2*keep)-2; i++)
        {
            printf(" ");
        }
        for (j = 1; j <= n - keep + 1; j++)
        {
            printf("%d ", j);
        }
        for (k = n - keep; k >= 1; k--)
        {
            printf("%d ", k);
        }
        printf("\n");
        keep--;
    }
}

int main()
{
    int n;
    scanf("%d", &n);
    if (n < 2)
        return -1;
    piramide(n);
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
  "source_sha256": "374b562451a3985bfd9c088f9c8671cc8856baee7f8dcd7e834cdf08620c7c14",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_040 — train

```c

#include <stdio.h>


void piramide(int n)
{
    int keep = n;
    int i, j, k;
    while (keep > 0)
    {
        for (i = 1; i <= (2*keep)-2; i++)
        {
            printf(" ");
        }
        for (j = 1; j <= n - keep + 1; j++)
        {
            printf("%d ", j);

        }
        for (k = n - keep; k >= 1; k--)
        {
            if (k != 1)
                printf("%d ", k);
            else
                printf("%d", k);
        }
        printf("\n");
        keep--;
    }
}

int main()
{
    int n;
    scanf("%d", &n);
    if (n < 2)
        return -1;
    piramide(n);
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
  "source_sha256": "d2cffd244bb3f43b098969f25c893e361c4a2c2e13cfd3b3e6791720f09abb05",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_041 — validation

```c


#include <stdio.h>

void piramide(int N){
    int i, j;
    for (i=1; i<=N; i++){
        for (j=1; j<=(2*(N-i)); j++)
            printf(" ");
        for (j=1; j<=i; j++)
            printf("%d ", j);
        for (j=(i-1); j>=1; j--)
            printf("%d ", j);
            
        printf("\n");
    }
}

int main(){
    int N;

    scanf("%d", &N);
    piramide(N);

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
  "source_sha256": "962bc1a1a391de47da7248e0c8998d9df61a4b5e58f6169e63026199ebbb30a0",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_042 — validation

```c


#include <stdio.h>

void piramide(int N){
    int i, j;
    for (i=1; i<=N; i++){
        for (j=1; j<=(2*(N-i)); j++)
            printf(" ");
        for (j=1; j<=i; j++)
            printf("%d ", j);
        for (j=(i-1); j>=1; j--)
            printf("%d ", j);
        printf("\n");
    }
}

int main(){
    int N;

    scanf("%d", &N);
    piramide(N);

    return 0;
}

```

```json
{
  "sample_id": "sample_042",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "5de6b952057c6087d422b6c16bf23dfafdeafc11f6098a3f80f04375c4697202",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_043 — train

```c

#include <stdio.h>

int main(){
    int n,i,j,k,m;
    scanf("%d", &n);
    for ( j = 1; j<=n; j++)
    {
        k=1;
        m=j;
        for ( i = 1; i <=2*(n-j); i++)
        {
            printf(" ");
        }
        while (k<=j)
        {
            printf("%d ",k);
            k++;
        }
        while (m-->1)
        {
            printf("%d ",m);
        }
        printf("\n");
    }
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
  "source_sha256": "fa8284c54ba2fe74d7309c0d520095997f190d8f9324d0470d167c367bded187",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_044 — train

```c

#include <stdio.h>

int main(){
    int n,i,j,k,m;
    scanf("%d", &n);
    for ( j = 1; j<=n; j++)
    {
        k=1;
        m=j;
        for ( i = 1; i <=2*(n-j); i++)
        {
            printf(" ");
        }
        while (k<=j)
        {
            printf("%d ",k);
            k++;
        }
        while (m-->1)
        {
            printf("%d ",m);
        }
        printf("\n");
    }
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
  "source_sha256": "fa8284c54ba2fe74d7309c0d520095997f190d8f9324d0470d167c367bded187",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_045 — train

```c

#include <stdio.h>

int main(){
    int n,i,j,k,m;
    scanf("%d", &n);
    for ( j = 1; j<=n; j++)
    {
        k=1;
        m=j;
        for ( i = 1; i <=2*(n-j); i++)
        {
            printf(" ");
        }
        while (k<=j)
        {
            printf("%d ",k);
            k++;
        }
        while (m-->1)
        {
            printf("%d ",m);
        }
        printf("\n");
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
  "source_sha256": "fa8284c54ba2fe74d7309c0d520095997f190d8f9324d0470d167c367bded187",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_046 — train

```c

#include <stdio.h>

int main(){
    int n,i,j,k,m;
    scanf("%d", &n);
    for ( j = 1; j<=n; j++)
    {
        k=1;
        m=j;
        for ( i = 0; i <=2*(n-j); i++)
        {
            printf(" ");
        }
        while (k<=j)
        {
            printf("%d ",k);
            k++;
        }
        while (m-->1)
        {
            printf("%d ",m);
        }
        printf("\n");
    }
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
  "source_sha256": "e8aaed609912b7076a363c71dc4ec2b8c32a90e83ff29cf28fe3750354497810",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "     1 \n   1 2 1 \n 1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1 \n     1 2 1 \n   1 2 3 2 1 \n 1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1 \n             1 2 1 \n           1 2 3 2 1 \n         1 2 3 4 3 2 1 \n       1 2 3 4 5 4 3 2 1 \n     1 2 3 4 5 6 5 4 3 2 1 \n   1 2 3 4 5 6 7 6 5 4 3 2 1 \n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_047 — train

```c

#include <stdio.h>

int main(){
    int n,i,j,k,m;
    scanf("%d", &n);
    for ( j = 1; j<=n; j++)
    {
        k=1;
        m=j;
        for ( i = 1; i <=2*(n-j); i++)
        {
            printf(" ");
        }
        while (k<=j)
        {
            printf("%d ",k);
            k++;
        }
        while (m-->1)
        {
            printf("%d ",m);
        }
        printf("\n");
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
  "source_sha256": "fa8284c54ba2fe74d7309c0d520095997f190d8f9324d0470d167c367bded187",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_048 — train

```c

#include <stdio.h>

void piramide(int N);

int main() {
    int N;
    
    scanf("%d", &N);
    while(N < 2){
        scanf("%d", &N);    
    }
    piramide(N);
    return 0;
}

void piramide(int N) {
    int i, j, k;
    for (i = 1; i <= N; i++) {
        for (j = 1; j <= N-i; j++) {
            printf("  ");
        }
        for (k = 1; k <= i; k++) {
            printf("%d ", k);
        }
        for (k = i-1; k >= 1; k--) {
            printf("%d ", k);
        }
        printf("\n");
    }
}


```

```json
{
  "sample_id": "sample_048",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "f5ecd06e95bf82e3db86fb682e84a22d23af8c0694ef6b3b3cf067172a41d2d1",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_049 — validation

```c

#include <stdio.h>

void piramide(int N)
{
    int linhas, colunas, contador;

    for(linhas = 0; linhas < N; linhas++)
    {
        for(contador = 0; contador < N - linhas - 1; contador++)
            {
                printf("  ");
            }

        for(colunas = 0; colunas < linhas + 1; colunas++)
        {
            printf("%d ", colunas + 1);
        }
        for(colunas = 0; colunas < linhas; colunas++)
        {
            if(colunas == linhas - 1)
                printf("%d", linhas - colunas);
            else
                printf("%d ", linhas - colunas);
        }
        putchar('\n');     
    } 
}

int main()
{
    int N;
    scanf("%d", &N);

    piramide(N);
    return 0;
}
```

```json
{
  "sample_id": "sample_049",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "52711dce28e8753f37ed27aa1f5c382c5a23aa6d0fe4347d79e4ea295d8a4779",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_050 — validation

```c

#include <stdio.h>

void piramide(int N)
{
    int linhas, colunas, contador;

    for(linhas = 0; linhas < N; linhas++)
    {
        for(contador = 0; contador < N - linhas - 1; contador++)
            printf("  ");

        for(colunas = 0; colunas < linhas + 1; colunas++)
            printf("%d ", colunas + 1);
            
        for(colunas = 0; colunas < linhas; colunas++)
        {
            if(colunas == linhas - 1)
                printf("%d", linhas - colunas);
            else
                printf("%d ", linhas - colunas);
        }
        putchar('\n');     
    } 
}

int main()
{
    int N;
    scanf("%d", &N);

    piramide(N);
    return 0;
}
```

```json
{
  "sample_id": "sample_050",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "719d79fb921947a79c404acf45f5af1690b9fd4f299a42743076121c4c678c66",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_051 — train

```c


#include <stdio.h>

void piramide (int N){

    int i = 1, contador1 = 0;
    int j = 1, k=0;
    while (i<=N)
    {
        for(contador1 = 0; contador1 < N - i; contador1++){
            printf(" ");
        }

        for(j = 1; j < i; j ++){
            printf("%d ", j);
        }

        for(k = i; k > 0; k--){
            if(k==1)
                printf("%d", k);
            else
                printf("%d ", k);
        }

        printf("\n");
        i++;
    }
    
}

int main(){

    int N=0;

    scanf("%d", &N);

    piramide(N);

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
  "source_sha256": "80fce22c85d3d67e5f37c059fbed460aa7ffd37dd141ca549c7d8eda12e1b7bc",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "  1\n 1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "   1\n  1 2 1\n 1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "       1\n      1 2 1\n     1 2 3 2 1\n    1 2 3 4 3 2 1\n   1 2 3 4 5 4 3 2 1\n  1 2 3 4 5 6 5 4 3 2 1\n 1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_052 — train

```c


#include <stdio.h>

void piramide(int N) {

    int base, i, j, k;
    base = 2 * N - 1;

    for (i = 1; i <= N; i++) {
        for (j = 1; j < N - i + 1; j++) 
            printf("  ");
        for (k = 1; k <= N * 2 - 1; k++)
            if (k > N - i && k <= base / 2 + 1)
                printf("%d ", k - (N - i));
            else if (k < N + i && k >= base / 2 + 1)
                printf("%d ", (k - (N + i)) * (-1));
        printf("\n");
    }
}




int main(void) {
    int N;
    scanf("%d", &N);
    piramide(N);
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
  "source_sha256": "d9b622fcac1854d6793183a5940858c6efdcf6365c3d81ff950e8924594499c5",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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

void piramide(int N)
{
    int i, j;
    for(i=1; i<=N; i++)
    {
        for(j=1; j<=(N-i); j++)
        {
            putchar(' ');
            putchar(' ');
        }
        for(j=1; j<=i; j++)
        {
            printf("%d ", j);
        }
        for(j=i-1; j>0; j--)
        {
            printf("%d ", j);
        }
        putchar('\n');
    }
}

int main()
{
    int N;
    scanf("%d", &N);
    if(N>=2)
    {
        piramide(N);
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
  "source_sha256": "da52fdd21f29623794ef9efe0a3ca8b13b9d67cf4cbd6de3b36c5791a6e49541",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_054 — train

```c

#include <stdio.h>

void piramide(int DIM) {
    
    int linha, num, espacos;

    for (linha = 1; linha <= DIM; linha++) {
        espacos = DIM - linha;
        while (espacos-- > 0) {
            printf("  ");
        }
        for (num = 1; num <= linha; num++)
            printf("%d ", num);

        for (num = linha - 1; num >= 1; num--)
            printf("%d ", num);
        
        printf("\n");

    }
}

int main() {
    
    int dim;

    scanf("%d", &dim);

    piramide(dim);

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
  "source_sha256": "42e1b938a47026b33dbd41945bcb88979b13d53937d84fd8fbf4f82215114b87",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_055 — train

```c

#include <stdio.h>

void piramide(int DIM) {
    
    int linha, num, espacos;

    for (linha = 1; linha <= DIM; linha++) {
        espacos = DIM - linha;
        while (espacos-- > 0) {
            printf("  ");
        }
        for (num = 1; num <= linha; num++)
            printf("%d ", num);

        for (num = linha - 1; num >= 1; num--)
            printf("%d ", num);
        
        printf("\n");

    }
}

int main() {
    
    int dim;
    scanf("%d", &dim);

    piramide(dim);

    return 0;
}

```

```json
{
  "sample_id": "sample_055",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "1a0022e6fc08c14c9ac225dc284608ac96a8f1f96147ecfb0cfce5b0b10eda79",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_056 — train

```c


#include <stdio.h>


void piramide(int n);

int main () {
    int n;

    scanf("%d", &n);

    piramide(n);

    return 0;
}

void piramide(int n) {
    int i, j, k= 1;

    for (i = 1; i <= n; i++)
    {
        for ( j = 1; j <= 2*(n - i); j++)
        {
            printf(" ");
        }
        
        for (k = 1; k < i + 1; k++)
        {
            printf("%d ", k);
        }
        
        for ( k = i - 1; k >= 1  ; k--)
        {
            printf("%d ", k);
        }
        printf("\n");
    }
}
```

```json
{
  "sample_id": "sample_056",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "5a8dbf3776df933bb9eeac1800b2e1111d305613bbd63477e45f6b97f024c31b",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_057 — train

```c


#include <stdio.h>


void piramide(int n);

int main () {
    int n;

    scanf("%d", &n);

    piramide(n);

    return 0;
}

void piramide(int n) {
    int i, j, k= 1;

    for (i = 1; i <= n; i++)
    {
        for ( j = 1; j <= 2*(n - i); j++)
        {
            printf(" ");
        }
        
        for (k = 1; k < i + 1; k++)
        {
            printf("%d ", k);
        }
        
        for ( k = i - 1; k >= 1  ; k--)
        {
            if (k == 1)
            {
                printf("%d",k);
            }else
            
            printf("%d ", k);
        }
        
        printf("\n");
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
  "source_sha256": "bc08f32c104e4cb3036291c043f22277756337a0452df99f6d954bd8b6682a6d",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_058 — train

```c


#include <stdio.h>


void piramide(int n);

int main () {
    int n;

    scanf("%d", &n);

    piramide(n);

    return 0;
}

void piramide(int n) {
    int i, j, k= 1;

    for (i = 1; i <= n; i++)
    {
        for ( j = 1; j <= 2*(n - i); j++)
        {
            printf(" ");
        }
        
        for (k = 1; k < i + 1; k++)
        {
            printf("%d ", k);
        }
        
        for ( k = i - 1; k >= 1  ; k--)
        {
            printf("%d ", k);
        }
        
        printf("\n");
    }
}
```

```json
{
  "sample_id": "sample_058",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "df6f4e2618fe3ff75dc3a5a29e1e4b1bfb26bc7627c9008ca35c0df3252a78ec",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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

void piramide(int N) {
    int i, j;
    for (i = 1; i <= N; ++i) {
        for (j = N - i; j > 0; --j) 
            printf("  ");

        for (j = 1; j <= i; ++j) {
            if (j == 1) putchar(' ');
            printf(" %d", j);
        }

        for (j = 1; j < i; ++j) 
           printf(" %d", i - j);

        putchar('\n');
    }
}


int main() {
    int N;
    scanf("%d", &N);
    piramide(N);

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
  "source_sha256": "64018d57faa9c544a3e2dc8766a3e1a5b1525a5cc0104ba4533bda8ad5a67b72",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "      1\n    1 2 1\n  1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "        1\n      1 2 1\n    1 2 3 2 1\n  1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "                1\n              1 2 1\n            1 2 3 2 1\n          1 2 3 4 3 2 1\n        1 2 3 4 5 4 3 2 1\n      1 2 3 4 5 6 5 4 3 2 1\n    1 2 3 4 5 6 7 6 5 4 3 2 1\n  1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_060 — train

```c

#include <stdio.h>

void piramide(int N) {
    int i, j;
    for (i = 1; i <= N; ++i) {
        for (j = N - i; j > 0; --j) 
            printf("  ");

        for (j = 1; j <= i; ++j)
            printf(" %d", j);

        for (j = 1; j < i; ++j) 
            if (i != 1) printf(" %d", i - j);

        putchar('\n');
    }
}


int main() {
    int N;
    scanf("%d", &N);
    piramide(N);

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
  "source_sha256": "f048c030ff1b5b050c332e27387171a52c212caf649a3b9d4100cd7ed52fd278",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "     1\n   1 2 1\n 1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1\n     1 2 1\n   1 2 3 2 1\n 1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1\n             1 2 1\n           1 2 3 2 1\n         1 2 3 4 3 2 1\n       1 2 3 4 5 4 3 2 1\n     1 2 3 4 5 6 5 4 3 2 1\n   1 2 3 4 5 6 7 6 5 4 3 2 1\n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_061 — train

```c

#include <stdio.h>

void piramide(int N) {
    int i, j;
    for (i = 1; i <= N; ++i) {
        for (j = N - i; j > 0; --j) 
            printf("  ");

        for (j = 1; j <= i; ++j)
            printf(" %d", j);

        for (j = 1; j < i; ++j) 
            if (i == 1) putchar(' ');
            else printf(" %d", i - j);

        putchar('\n');
    }
}


int main() {
    int N;
    scanf("%d", &N);
    piramide(N);

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
  "source_sha256": "89eaef962ce0ba91199a05c7ecd362b83479569272e8a7760785bec933c5aebd",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "     1\n   1 2 1\n 1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1\n     1 2 1\n   1 2 3 2 1\n 1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1\n             1 2 1\n           1 2 3 2 1\n         1 2 3 4 3 2 1\n       1 2 3 4 5 4 3 2 1\n     1 2 3 4 5 6 5 4 3 2 1\n   1 2 3 4 5 6 7 6 5 4 3 2 1\n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_062 — train

```c


#include <stdio.h>

void piramide(int n) {

    int i, j;
    int num;

    for (i=1; i<=n; i++) {
        num = 1;
        for (j=1; j<=n-1; j++) {

            if (j > n-i) {
                printf("%d ",num);
                num++;
            }
            else {
                printf("  ");
            }
        }
        
        printf("%d",num);

        if (i == 1) {
            printf("\n");
            continue;
        }

        num--;
        printf(" ");
        
        for (++j; j<(2*n-1); j++) {

            if ((2*n-j) > n-i) {
                printf("%d ",num);
                num--;
            }
            else {
                printf("  ");
            }
        }

        if (i == n) {
            printf("%d\n",num);
        }
        else {
            printf(" \n");
        }

    }
}

int main() {

    int n;

    scanf("%d",&n);
    piramide(n);

    return 0;
}
```

```json
{
  "sample_id": "sample_062",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "b0606cd8a02839898eee4d42ae26abece57d0a1b15fe2bdcfddf25f5ada4d53d",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1\n  1 2 1  \n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1\n    1 2 1    \n  1 2 3 2 1  \n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1\n            1 2 1            \n          1 2 3 2 1          \n        1 2 3 4 3 2 1        \n      1 2 3 4 5 4 3 2 1      \n    1 2 3 4 5 6 5 4 3 2 1    \n  1 2 3 4 5 6 7 6 5 4 3 2 1  \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_063 — train

```c

#include <stdio.h>
void piramide(int numero)
{
    int i1, i2, i3, i4,espacos;
    for (i1 = 1; i1<= numero; i1++){
        espacos = (numero - i1)*2;
        for (i4=1; i4<=espacos; i4++){
            printf(" ");
        }
        for (i2 = 1; i2 <= i1; i2++){
            printf(" %d", i2);
        }
        if (i1>1){
            for(i3 = i2-2; i3>=1; i3--){
                printf(" %d", i3);
            }
        }
        printf("\n");
    }
}
int main()
{
    int numero;
    scanf("%d", &numero);
    piramide(numero);
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
  "source_sha256": "ebcf69333cbf90e24cbec7e0a2b804d14427b496870837b71d8453ab261364ec",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "     1\n   1 2 1\n 1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1\n     1 2 1\n   1 2 3 2 1\n 1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1\n             1 2 1\n           1 2 3 2 1\n         1 2 3 4 3 2 1\n       1 2 3 4 5 4 3 2 1\n     1 2 3 4 5 6 5 4 3 2 1\n   1 2 3 4 5 6 7 6 5 4 3 2 1\n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_064 — train

```c

#include <stdio.h>

void piramide (int N) {
    int linha, col, i;
    for (linha = 1; linha <= N; linha++) {
        i = 0;
        for (col = 1; col <= (N + linha - 1); col++) {
            if (col > (N - linha)){
                if (col <= N)
                    printf("%d", ++i);
                else
                    printf("%d", --i);
            }
            else {
                printf(" ");
            }
            printf(" ");
        }
        printf("\n");
    }
}

int main () {
    int N;
    scanf("%d", &N);
    piramide(N);

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
  "source_sha256": "d210c7155d7d5aeba5c48df9131ede93d8bb1578deadff8c9a24320a68536acb",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_065 — train

```c


#include <stdio.h>

void piramide(int N) {
    int i, j;
    for (i = 1; i <= N; i++) {
        
        for (j = 1; j <= N - i; j++) {
            printf("  ");
        }
        
        for (j = 1; j <= i; j++) {
            printf("%d ", j);
        }
        
        for (j = i - 1; j >= 1; j--) {
            printf("%d ", j);
        }
        printf("\n");
    }
}


int main() {
    int H;
    scanf("%d", &H);
    piramide(H);
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
  "source_sha256": "99cddd9c4588b573e0c569f8bd91360848620ef9cb87d5d27507b9e4d4525e48",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_066 — train

```c


#include <stdio.h>

void piramide(int N) {
    int i, j;
    for (i = 1; i <= N; i++) {
        
        for (j = 1; j <= N - i; j++) {
            printf("  ");
        }
        
        for (j = 1; j <= i; j++) {
            printf("%d ", j);
        }
        
        for (j = i - 1; j >= 1; j--) {
            printf("%d ", j);
        }
        printf("\n");
    }
}


int main() {
    int H;
    scanf("%d", &H);
    piramide(H);
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
  "source_sha256": "ded6fc175765db559d58618ff2a438c7c55e489201fcf33e720afdec01dcc1cb",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_067 — train

```c


#include <stdio.h>

void piramide(int N) {
    int i, j;
    for (i = 1; i <= N; i++) {
        
        for (j = 1; j <= N - i; j++) {
            printf("  ");
        }
        
        for (j = 1; j <= i; j++) {
            printf("%d ", j);
        }
        
        for (j = i - 1; j >= 1; j--) {
            if (j==1) {
                printf("%d",j);
            }else {
            printf("%d ", j);
            }
        }
        printf("\n");
    }
}


int main() {
    int H;
    scanf("%d", &H);
    piramide(H);
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
  "source_sha256": "0343277e7a0a09ae8cba9f7f0703ea047464f37e939034bddda2a9c8fbe3e008",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_068 — train

```c

#include <stdio.h>

void piramide(int N){
    int lin, col, colneg, espaco;

    for (lin = 1; lin <= N; lin++){
        for (espaco = 1; espaco <= (2*(N - lin)); espaco++)
                printf(" ");
        for (col = 1; col <= lin; col++)
            printf("%d ", col);
        for (colneg = lin - 1; colneg >= 1; colneg--){
            printf("%d", colneg);
            if (colneg > 1)
                putchar(' ');
        }
        printf("\n");
    }
}

int main(){
    int N;

    scanf("%d", &N);

    piramide(N);

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
  "source_sha256": "ae54cad462b0df4d503f4a4efd6521acbc5dbb6eba168f7f575befac1bee1ba5",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_069 — train

```c

#include <stdio.h>

void piramide(int N){
    int lin, col, colneg, espaco;

    for (lin = 1; lin <= N; lin++){
        for (espaco = 1; espaco <= (2*(N - lin)); espaco++)
                printf(" ");
        for (col = 1; col <= lin; col++)
            printf("%d ", col);
        for (colneg = lin - 1; colneg >= 1; colneg--)
            printf("%d ", colneg);
        printf("\n");
    }
}

int main(){
    int N;

    scanf("%d", &N);

    piramide(N);

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
  "source_sha256": "6b8061291f16a03e411fa1ae9962fcf91d189779615061ecf8c6423290689088",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_070 — train

```c

#include <stdio.h>

void piramide(int N){
    int lin, col, colneg, espaco;
    if (N < 2){
        printf("Digite um número maior que 2\n");
        return;
    }
    for (lin = 1; lin <= N; lin++){
        for (espaco = 1; espaco <= (2*(N - lin)); espaco++)
                printf(" ");
        for (col = 1; col <= lin; col++)
            printf("%d ", col);
        for (colneg = lin - 1; colneg >= 1; colneg--)
            printf("%d ", colneg);
        printf("\n");
    }
}

int main(){
    int N;

    scanf("%d", &N);

    piramide(N);

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
  "source_sha256": "6ae0a01e64f9e232635f5a5bdfb8f91788131a7a8ca97385db8068375654dc75",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_071 — train

```c

#include <stdio.h>

void piramide(int N);


int main()
{
    int N;

    scanf("%d", &N);

    piramide(N);

    return 0;
}

void piramide(int N)
{
    int l, c, number;

    for(l = 0; l < N ; l++)
    {
        number = 1;
        for(c = 1; c <= N + l; c++)
        {
            if(c >= N)
                printf("%d", number--);
            else if (c >= N - l)
                printf("%d", number++);
            else 
                printf(" ");
            putchar(' ');
        }
        printf("\n");
    }
}
```

```json
{
  "sample_id": "sample_071",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "cb1a9335093fb4e2c235942765ac7bfabaf40fc9c985dc3fa1902c68f7c9be00",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_072 — train

```c

#include <stdio.h>

void piramide(int N);


int main()
{
    int N;

    scanf("%d", &N);

    piramide(N);

    return 0;
}

void piramide(int N)
{
    int l, c, number;

    for(l = 0; l < N ; l++)
    {
        number = 1;
        for(c = 1; c <= N + l; c++)
        {
            if(c >= N)
                printf("%d ", number--);
            else if (c >= N - l)
                printf("%d ", number++);
            else 
                printf("  ");
        }
        printf("\n");
    }
}
```

```json
{
  "sample_id": "sample_072",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "a656b1a5f6f7e4d25abeb66d655c2071d8b0971c1e92a899bfd87ff943d91bc3",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_073 — train

```c

#include <stdio.h>

void piramide(int N) {
  int i, j;
  
  for(i = 1; i <= N; i++) {
    
    for(j = 0; j <((N-i)*2); j++) {
      printf(" ");
    }  
    
    for(j = 1; j <= i; j++) {
      printf("%d ", j);
    }
    
    for(j = i - 1; j > 0; j--) {
      printf("%d ", j);
    }  
    printf("\n");
  }

}
int main() {
  int N;

  scanf("%d", &N);
  piramide(N);
  
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
  "source_sha256": "49c1cf4ecdf31b84bbcaf494adfbf6d79c31706ae36e30810bc92fc460741cf2",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_075 — train

```c


#include <stdio.h>

void piramide(int n) {
    int vc = 1, espaco = n - 1, vg = 0, num = 1;
    while (vc - 1 != n) {
        while (vg < espaco) {
            printf("  ");
            vg++;
        }
        espaco--;
        vg = 0;
        while (num - 1 != vc) {
            printf("%d ", num);
            num++; 
        }
        num -= 1;
        while (num != 1) {
            num--;
            if (num == 1 && vc == n)
                printf("%d", num);
            else
                printf("%d ", num);
        }
        printf("\n");
        vc++;
    }
}


int main () {
    int n;
    scanf("%d", &n);
    piramide(n);
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
  "source_sha256": "e67c67d837b2ec2a6eacb4333cf1b7d0545dca664f4bdc05aef6cb89ad48b7b6",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_076 — train

```c


#include <stdio.h>

void piramide(int n) {
    int vc = 1, espaco = n - 1, vg = 0, num = 1;
    while (vc - 1 != n) {
        while (vg < espaco) {
            printf("  ");
            vg++;
        }
        espaco--;
        vg = 0;
        while (num - 1 != vc) {
            printf("%d ", num);
            num++; 
        }
        num -= 1;
        while (num != 1) {
            num--;
            printf("%d ", num);
        }
        printf("\n");
        vc++;
    }
}

int main () {
    int n;
    scanf("%d", &n);
    piramide(n);
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
  "source_sha256": "7835d3ce506d21d7db60adbe68a8a901d8356ab8e0fb220ceb38901dae178db7",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_077 — train

```c

#include <stdio.h>

void piramide(int N){
    int i,j;
    for(i=1;i<=N;i++){
        for(j=0;j<N-i;j++)
            printf("  ");
    
        for(j=1;j<=i;j++)
            printf("%d ",j);

        for(j=i-1;j>=1;j--)
            printf("%d ",j);
        printf("\n");
    }
}

int main(){
    int N;
    scanf("%d",&N);
    if (N<2)
        return 1;
    piramide(N);
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
  "source_sha256": "822fd356fb9fb5250fd91f7b4be16e94f52903405b31552c399303fa68c32533",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_078 — train

```c

#include <stdio.h>

#define SPC "  "

void spaces (int n, int p){
    for(;(n-p);p++){
        printf("%s", SPC);
    }
}

void linha (int n, int p){
    int step = 1;
    spaces(n, p);
    for (;(step<p);step++){
        printf("%d ",(step));
    }
    printf("%d ",p);
    for (step--;step;step--){
        if (step==1){
            printf("%d",step);
        }
        else {
            printf("%d ",step);
    
        }  
    } 
}

void piramide(int n){
    int p = 1;
    for (;p<=n;p++){
        linha(n, p);
        printf("\n");
    }
}

int main (){
    int n = 0;
    scanf("%d",&n);
    piramide(n);
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
  "source_sha256": "2840dece4d98cd6c8e23c3dcec55f761e978752dfd1f4ef4c8853b7d593c25e7",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_079 — train

```c

#include <stdio.h>

void piramide(int N){
    int num, tab, linhas = N - 1, max;

    while (linhas >= 0){
        
        for (tab = linhas; tab >= 1; tab--){
            printf("  "); 
        }

        
        for (num = 1; num <=  N - linhas; num++){
                printf("%d ", num);
                max = num;
        }

        
        for (num = max - 1; num > 1; num--){
            printf("%d ", num);
        }

        
        if (max != 1){printf("1\n");}

        
        else {printf("\n");}

        linhas--;
    }
}

int main(){
    int n;

    scanf("%d", &n);
    piramide(n);
    
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
  "source_sha256": "c5d4188c6a13beff94bf365ad847a73fee96e793831d606a3d435c778ad58037",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_080 — train

```c


#include <stdio.h>

void piramide(int N) {
    int n2, starter = 1, starter2 = 1, starter3 = 0, counter = 1;
    n2 = 2 * N;
    if (N >= 2) {
       for (;N > 0; N--) {
            for (;n2 > 2; n2--) {
                printf(" ");
            }
            for (;starter > 0; starter--) {
                printf("%d ", starter2);
                starter2++;
            }
            starter2 = starter2 - 2;
            for (;(starter3 > 0) & (starter2 > 0); starter3--) {
                if (starter3 == 1 ) 
                    printf("%d", starter2);
                else
                    printf("%d ", starter2);
                starter2--;
            }
        putchar('\n');
        starter2 = 1;
        counter++;
        starter3 = counter;
        starter = counter;
        n2 = 2*(N - 1);
        }
    }
}

int main() {
    int N;
    scanf("%d", &N);
    piramide(N);
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
  "source_sha256": "f2be22ee5fb61cf80db000226f5743eb6f7df87764880991664dadafe11a21c3",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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

void piramide(int N) {
    int n2, starter = 1, starter2 = 1, starter3 = 0, counter = 1;
    n2 = 2 * N;
    if (N >= 2) {
       for (;N > 0; N--) {
            for (;n2 > 2; n2--) {
                printf(" ");
            }
            for (;starter > 0; starter--) {
                printf("%d ", starter2);
                starter2++;
            }
            starter2 = starter2 - 2;
            for (;(starter3 > 0) & (starter2 > 0); starter3--) {
                if ((starter3 == 1) | (starter2 == 1)) 
                    printf("%d", starter2);
                else
                    printf("%d ", starter2);
                starter2--;
            }
        putchar('\n');
        starter2 = 1;
        counter++;
        starter3 = counter;
        starter = counter;
        n2 = 2*(N - 1);
        }
    }
}

int main() {
    int N;
    scanf("%d", &N);
    piramide(N);
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
  "source_sha256": "82d33ad7a1ac77c46fa84bcf9cae9d7e63d32c747d24cfda1d0c8d999cdc0687",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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
void piramide(int N){
    int i, j, n;
    if (N >= 2){
        for(i = 1; i <= N; i++){
            for(n = 0; n < N - i; n++) printf("  ");

            for(j = 1; j <= i; j++){
                printf("%d ", j);
            }

            for(j = i-1; j >= 1; j--){
                printf("%d ", j);
            }
            
            printf("\n");
        }
    }
}

int main(){
    int N;
    scanf("%d", &N);
    piramide(N);
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
  "source_sha256": "129f66aa58e0030b3a4ddae35f89d49402bb80ce2749aa448f2cefb889405a11",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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
void piramide(int N){
    int i, j, n;
    if (N >= 2){
        for(i = 1; i <= N; i++){
            for(n = 0; n < N - i; n++) printf(" ");

            for(j = 1; j <= i; j++){
                printf("%d", j);
                if (j < i) printf(" ");
            }

            for(j = i-1; j >= 1; j--){
                printf(" %d", j);
            }
            
            printf("\n");
        }
    }
}

int main(){
    int N;
    scanf("%d", &N);
    piramide(N);
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
  "source_sha256": "de609765e630d3440a9f2412c211e7889819ee48a1836ba87598805f46c24c3a",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "  1\n 1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "   1\n  1 2 1\n 1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "       1\n      1 2 1\n     1 2 3 2 1\n    1 2 3 4 3 2 1\n   1 2 3 4 5 4 3 2 1\n  1 2 3 4 5 6 5 4 3 2 1\n 1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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
void piramide(int N){
    int i, j, n;
    if (N >= 2){
        for(i = 1; i <= N; i++){
            for(n = 0; n < N - i; n++) printf("  ");

            for(j = 1; j <= i; j++){
                printf("%d ", j);
            }

            for(j = i-1; j >= 1; j--){
                printf("%d ", j);
            }
            
            printf("\n");
        }
    }
}

int main(){
    int N;
    scanf("%d", &N);
    piramide(N);
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
  "source_sha256": "129f66aa58e0030b3a4ddae35f89d49402bb80ce2749aa448f2cefb889405a11",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_085 — train

```c

#include <stdio.h>

void piramide(int N){
    int i, j, n;
    if (N >= 2){
        for(i = 1; i <= N; i++){
            for(n = 0; n < N - i; n++) printf("  ");

            for(j = 1; j <= i; j++){
                printf("%d ", j);
            }

            for(j = i-1; j >= 1; j--){
                printf("%d ", j);
            }
            
            printf("\n");
        }
    }
}

int main(){
    int N;
    scanf("%d", &N);
    piramide(N);
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
  "source_sha256": "36221bef7148d2db4e987c75508a6574baeaf002a803bf2794f065b86a0d0ece",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_086 — train

```c

#include <stdio.h>
void piramide(int N){
    int i, j, n;
    if (N >= 2){
        for(i = 1; i <= N; i++){
            for(n = 0; n < N - i; n++) printf("  ");

            for(j = 1; j <= i; j++){
                printf("%d ", j);
            }

            for(j = i-1; j >= 1; j--){
                printf("%d ", j);
            }
            
            printf("\n");
        }
    }
}
int main(){
    int N;
    scanf("%d", &N);
    piramide(N);
    return 0;
}
```

```json
{
  "sample_id": "sample_086",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "de4ed20333c4d3a72900271fdbfea3987725674c93528ae4acbbeb304ce4af41",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_087 — validation

```c


#include <stdio.h>

void piramide(int n) {
    int i, a, b, espacos;
    
    if (n <= 1) return;

    for (i = 1; i <= n; i++) {
        for (espacos = n*2 - 2*i; espacos > 0; espacos--){
            printf(" ");
        }
        for (a = 1; a <= i; a++) {
            if (a == i)
                printf("%d", a);
            else
                printf("%d ", a);
        }
        for (b = i -1; b >= 1; b--) {
            if (b == i - 1)
                printf(" %d ", b);
            else
                printf("%d ", b);
        }
        printf("\n");
    }
}

int main() {
    int n;

    scanf("%d", &n);
    piramide(n);
    return 0;
}
```

```json
{
  "sample_id": "sample_087",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "60ce1c7cfae4346bafd3666fc87653daa4f46e1c40298bb81c033f5d942cb61a",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1\n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1\n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1\n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_088 — train

```c

#include <stdio.h>

void piramide(int N);

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
    return 0;
}

void piramide(int N) {
    int i = 0, e = 1, num = 1;
    while(i < N) {
        while(e < N-i) {
            (e == 1) ? printf("%c", ' ') : printf("%2c", ' ');
            ++e;
        }
        while(N-i <= e && e <= N) {
            (e == 1) ? printf("%d", num) : printf("%2d", num);
            ++num;
            ++e;
        }
        num = num - 2;
        while(N < e && e < N+i) {
            printf("%2d", num);
            --num;
            ++e;
        }
        if(e == N+i) {
            (i == N-i) ? printf("%d\n", num) : printf("%2d", num);
            ++e;
        }
        while(N+i < e && e < 2*N-1) {
            ++e;
        }
        if(e == 2*N-1)
            printf("%2c\n", ' ');
        e = 1;
        num = 1;
        ++i;
    }
}
```

```json
{
  "sample_id": "sample_088",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "c83e241d2293fca629f12ff8d3b0d0bfce5d5cbcb6b158531108b3a090619546",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1  \n  1 2 1  \n1 2 3 2 1"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1  \n    1 2 1  \n  1 2 3 21\n  \n1 2 3 4 3 2 1"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1  \n            1 2 1  \n          1 2 3 2 1  \n        1 2 3 4 3 2 1  \n      1 2 3 4 5 4 3 21\n  \n    1 2 3 4 5 6 5 4 3 2 1  \n  1 2 3 4 5 6 7 6 5 4 3 2 1  \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_089 — train

```c

#include <stdio.h>

void piramide(int N);

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
    return 0;
}

void piramide(int N) {
    int i = 0, e = 1, num = 1;
    while(i < N) {
        while(e < N-i) {
            (e == 1) ? printf("%c", ' ') : printf("%2c", ' ');
            ++e;
        }
        while(N-i <= e && e <= N) {
            (e == 1) ? printf("%d", num) : printf("%2d", num);
            ++num;
            ++e;
        }
        num = num - 2;
        while(N < e && e < N+i) {
            printf("%2d", num);
            --num;
            ++e;
        }
        if(e == N+i) {
            (i == N-i) ? printf("%d\n", num) : printf("%2d", num);
            ++e;
        }
        while(N+i < e && e < 2*N-1) {
            ++e;
        }
        if(e == 2*N-1)
            printf("%c\n", ' ');
        e = 1;
        num = 1;
        ++i;
    }
}
```

```json
{
  "sample_id": "sample_089",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "ac3f5d476973d4736578ed5cd6a585b9cef8fe4a4dba1e6ff56afa6ddef8ed02",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 21\n \n1 2 3 4 3 2 1"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 21\n \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "different",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "different",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_090 — train

```c

#include <stdio.h>

void piramide(int n){
    int i , j;
    for(i=1;i<=n;i++){
        for(j=n-i;j>0;j--){
            printf("  ");
        }
        for(j=1;j<=i;j++){
            printf("%d ",j);
        }
        for(j=i;j>1;j--){
            printf("%d ",j-1);
        }
        printf("\n");
    }
}

int main(){
    int n;
    scanf("%d",&n);
    piramide(n);

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
  "source_sha256": "28198c0c0748ad1c0e2b2a8f54d76b7afcc8768674c6dc700758836a7a6729b2",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_091 — train

```c

#include <stdio.h>

void line(int l, int n) {
    int j;
    for(j = l; j < n; j++) {
        printf("  ");
    }
    for(j = 1; j <= l; j++) {
            printf("%d ", j);
    }
    for(j = l - 1; j >= 1; j--) {
        if(j== 1){
            printf("%d", j);
        }else{
        printf("%d ", j);
        } 
    }
    printf("\n");
}

int main() {
    int n, l;
    scanf("%d", &n);
    for(l = 1; l <= n; l++) {
        line(l, n);
    }
    return 0;
}
```

```json
{
  "sample_id": "sample_091",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "502131a02a91698d370d1b1ebda55f92228483c37ec00f70fa235bac1245b64b",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_092 — train

```c

#include <stdio.h>


void piramide(int N)
{
    int i, j, n;

    for(j = 0; j < N; j++)
    {
        n = 1;
        for(i = 1; i <= N + j; i++)
        {
            if (i == N)
            {
                printf("%d ", n--);
            }
            else if( i > N)
            {
                printf("%d ", n--);
            }
            else if(i >= N - j)
            {
                printf("%d ", n++);
            }
            else if(i == N + j)
            {

            }
            else
            {
                printf("  ");
            }
            
        }
        printf("\n");
    }
}


int main()
{
    int N;

    scanf("%d", &N);

    piramide(N);

    return 0;
}
```

```json
{
  "sample_id": "sample_092",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "113b66e32b4b575c6c48f76f1baabd50bfeab77d676c8bb273ae193b08c69884",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_093 — train

```c


#include <stdio.h>

void piramide(int N);

int main(){
    int N;
    scanf("%d",&N);
    piramide(N);
    return 0;
}

void piramide(int N){

    int linha,i,esp,j,k;


    for( linha=1; linha<=N; linha++){
        esp=2*(N-linha);
        for(j=1; j<=esp;j++) {printf(" ");}
        for (i=1;i<=linha;i++) {printf("%d ",i);}
        for (k=linha-1;k>0;k--) {printf("%d ",k);}
        printf("\n");
}

}
```

```json
{
  "sample_id": "sample_093",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "b24bf9f1ce139a064d379acff344672191bb3fc1cf376c752806be3e19e54762",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_094 — train

```c

#include <stdio.h>
void piramide(int N){
    int i,j,esp,v;
    for (i=1;i<=N;i++) {
        esp=2*(N-i);
        printf("%*s",esp,"");
        for (j=1;j>0;j++) {
            if (j<i) {
                printf("%d",j);
                printf("%*s",1," ");
            }
            else {
                printf("%d",j);
                printf("%*s",1," ");
                if (j!=1) {
                    for (v=j-1;v>0;v--) {
                        printf("%d",v);
                        printf("%*s",1," ");
                    }
                    j=-1;
                }
                else {
                    j=-1;
                }
                
            }
        }
        printf("\n");
    }
}

int main () {
    int N;
    scanf("%d",&N);
    piramide(N);
    return 0;
}
```

```json
{
  "sample_id": "sample_094",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "c47d2ba516177e1add12fafbb3cdf32546f6704c4f0cc2876770a3daef63b196",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_095 — train

```c

#include <stdio.h>
void piramide(int N){
    int i,j,esp,v;
    for (i=1;i<=N;i++) {
        esp=2*(N-i);
        printf("%*s",esp,"");
        for (j=1;j>0;j++) {
            if (j<i) {
                printf("%d",j);
                printf("%*s",1," ");
            }
            else {
                printf("%d",j);
                printf("%*s",1," ");
                if (j!=1) {
                    for (v=j-1;v>0;v--) {
                        printf("%d",v);
                        printf("%*s",1," ");
                    }
                    j=-1;
                }
                else {
                    j=-1;
                }
                
            }
        }
        printf("\n");
    }
}

int main () {
    int N;
    scanf("%d",&N);
    piramide(N);
    return 0;
}




```

```json
{
  "sample_id": "sample_095",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "86d386404a049ff4a18971ac2fb158fa276c44a8b90a1cf5ffea2c1e1516d3f4",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_096 — validation

```c


#include <stdio.h>

void piramide (int n)
{
    int i, j;

    if (n >= 2)
    {
        for (i = 1; i <= n; i++)
        {
            for (j = 1; j <= n - i; j++)
                printf("  ");

            for (j = 1; j < i; j++)
                printf("%d ", j);

            printf("%d ", i);

            for (j = i; j > 1; j--)
                printf("%d ", j - 1);

            printf("\n");
        }
    }
    return;
}

int main() 
{
    int num;

    scanf("%d", &num);
    piramide(num);
    
    return 0;
}
```

```json
{
  "sample_id": "sample_096",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "5dafcd7f0b53451ebd2a397590f6aafe1f257cbf973e7768da9c00b78f19626d",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_097 — validation

```c


#include <stdio.h>

void piramide (int n)
{
    int i, j;

    if (n >= 2)
    {
        for (i = 1; i <= n; i++)
        {
            for (j = 1; j <= n - i; j++)
                printf("  ");

            for (j = 1; j < i; j++)
                printf("%d ", j);

            printf("%d ", i);

            for (j = i; j > 1; j--)
            {
                printf("%d", j - 1);

                if (j != 2)
                    printf(" ");
            }
            
            printf("\n");
        }
    }
    return;
}

int main() 
{
    int num;

    scanf("%d", &num);
    piramide(num);
    
    return 0;
}
```

```json
{
  "sample_id": "sample_097",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "e11e3d4a85df64e433d10666f53cb0c50ef01f73712f73a825be8d8580b629b6",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_098 — train

```c

#include <stdio.h>

void piramide(int n){
    int i, j, s;
    for(i = 1; i <= n; i++){
        for(s = 0; s < n - i; s++){
            printf("  ");
        }
        for(j = 1; j <= i ; j++){
            printf("%d ", j);
        }
        for(j = i - 1; j >=1 ; j--){
            printf("%d ", j);
        }
        printf("\n");
    }
}

int main(){
    int n;
    scanf("%d", &n);
    piramide(n);
    return 0;
}
```

```json
{
  "sample_id": "sample_098",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "8a375d950c78fcf2f63955ff101aeeb9bfc6a58667a2ae6e2ebd86562904d834",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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


## sample_099 — validation

```c



#include <stdio.h>

void piramide(int n) {
    int i, j;
    for(i=1; i<=n; i++){
        for (j=1; j<=n-i; j++) {
            printf("  ");
        }

        for(j=1; j<=i; j++) {
            printf("%d ", j);
        }
        for(j=i-1; j>0; j--) {
            printf("%d ", j);
        }
        printf("\n");
    }
}

int main() {
    int n;
    scanf("%d", &n);
    piramide(n);
    return 0;
}
```

```json
{
  "sample_id": "sample_099",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "c88f3e3be128abf9af14a9c4eaa14564939c183dffff7819291c2fd01ecc4f19",
  "outcomes": {
    "ex02_0": "fail",
    "ex02_1": "fail",
    "ex02_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex02_0",
      "input": "3",
      "expected": "    1\n  1 2 1\n1 2 3 2 1\n",
      "output": "    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
    }
  ],
  "clustering_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex02_0:relation": "whitespace",
    "stdout:ex02_0:edit_band": "small",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "small",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex02_0": "fail",
    "test:ex02_1": "fail",
    "test:ex02_2": "fail",
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
  "members/sample_002/raw_code",
  "members/sample_002/tests/ex02_0",
  "members/sample_002/tests/ex02_1",
  "members/sample_002/tests/ex02_2",
  "members/sample_003/raw_code",
  "members/sample_003/tests/ex02_0",
  "members/sample_003/tests/ex02_1",
  "members/sample_003/tests/ex02_2",
  "members/sample_004/raw_code",
  "members/sample_004/tests/ex02_0",
  "members/sample_004/tests/ex02_1",
  "members/sample_004/tests/ex02_2",
  "members/sample_005/raw_code",
  "members/sample_005/tests/ex02_0",
  "members/sample_005/tests/ex02_1",
  "members/sample_005/tests/ex02_2",
  "members/sample_006/raw_code",
  "members/sample_006/tests/ex02_0",
  "members/sample_006/tests/ex02_1",
  "members/sample_006/tests/ex02_2",
  "members/sample_007/raw_code",
  "members/sample_007/tests/ex02_0",
  "members/sample_007/tests/ex02_1",
  "members/sample_007/tests/ex02_2",
  "members/sample_008/raw_code",
  "members/sample_008/tests/ex02_0",
  "members/sample_008/tests/ex02_1",
  "members/sample_008/tests/ex02_2",
  "members/sample_009/raw_code",
  "members/sample_009/tests/ex02_0",
  "members/sample_009/tests/ex02_1",
  "members/sample_009/tests/ex02_2",
  "members/sample_010/raw_code",
  "members/sample_010/tests/ex02_0",
  "members/sample_010/tests/ex02_1",
  "members/sample_010/tests/ex02_2",
  "members/sample_011/raw_code",
  "members/sample_011/tests/ex02_0",
  "members/sample_011/tests/ex02_1",
  "members/sample_011/tests/ex02_2",
  "members/sample_012/raw_code",
  "members/sample_012/tests/ex02_0",
  "members/sample_012/tests/ex02_1",
  "members/sample_012/tests/ex02_2",
  "members/sample_013/raw_code",
  "members/sample_013/tests/ex02_0",
  "members/sample_013/tests/ex02_1",
  "members/sample_013/tests/ex02_2",
  "members/sample_014/raw_code",
  "members/sample_014/tests/ex02_0",
  "members/sample_014/tests/ex02_1",
  "members/sample_014/tests/ex02_2",
  "members/sample_015/raw_code",
  "members/sample_015/tests/ex02_0",
  "members/sample_015/tests/ex02_1",
  "members/sample_015/tests/ex02_2",
  "members/sample_016/raw_code",
  "members/sample_016/tests/ex02_0",
  "members/sample_016/tests/ex02_1",
  "members/sample_016/tests/ex02_2",
  "members/sample_017/raw_code",
  "members/sample_017/tests/ex02_0",
  "members/sample_017/tests/ex02_1",
  "members/sample_017/tests/ex02_2",
  "members/sample_018/raw_code",
  "members/sample_018/tests/ex02_0",
  "members/sample_018/tests/ex02_1",
  "members/sample_018/tests/ex02_2",
  "members/sample_019/raw_code",
  "members/sample_019/tests/ex02_0",
  "members/sample_019/tests/ex02_1",
  "members/sample_019/tests/ex02_2",
  "members/sample_020/raw_code",
  "members/sample_020/tests/ex02_0",
  "members/sample_020/tests/ex02_1",
  "members/sample_020/tests/ex02_2",
  "members/sample_021/raw_code",
  "members/sample_021/tests/ex02_0",
  "members/sample_021/tests/ex02_1",
  "members/sample_021/tests/ex02_2",
  "members/sample_022/raw_code",
  "members/sample_022/tests/ex02_0",
  "members/sample_022/tests/ex02_1",
  "members/sample_022/tests/ex02_2",
  "members/sample_023/raw_code",
  "members/sample_023/tests/ex02_0",
  "members/sample_023/tests/ex02_1",
  "members/sample_023/tests/ex02_2",
  "members/sample_024/raw_code",
  "members/sample_024/tests/ex02_0",
  "members/sample_024/tests/ex02_1",
  "members/sample_024/tests/ex02_2",
  "members/sample_025/raw_code",
  "members/sample_025/tests/ex02_0",
  "members/sample_025/tests/ex02_1",
  "members/sample_025/tests/ex02_2",
  "members/sample_026/raw_code",
  "members/sample_026/tests/ex02_0",
  "members/sample_026/tests/ex02_1",
  "members/sample_026/tests/ex02_2",
  "members/sample_027/raw_code",
  "members/sample_027/tests/ex02_0",
  "members/sample_027/tests/ex02_1",
  "members/sample_027/tests/ex02_2",
  "members/sample_028/raw_code",
  "members/sample_028/tests/ex02_0",
  "members/sample_028/tests/ex02_1",
  "members/sample_028/tests/ex02_2",
  "members/sample_029/raw_code",
  "members/sample_029/tests/ex02_0",
  "members/sample_029/tests/ex02_1",
  "members/sample_029/tests/ex02_2",
  "members/sample_030/raw_code",
  "members/sample_030/tests/ex02_0",
  "members/sample_030/tests/ex02_1",
  "members/sample_030/tests/ex02_2",
  "members/sample_031/raw_code",
  "members/sample_031/tests/ex02_0",
  "members/sample_031/tests/ex02_1",
  "members/sample_031/tests/ex02_2",
  "members/sample_032/raw_code",
  "members/sample_032/tests/ex02_0",
  "members/sample_032/tests/ex02_1",
  "members/sample_032/tests/ex02_2",
  "members/sample_033/raw_code",
  "members/sample_033/tests/ex02_0",
  "members/sample_033/tests/ex02_1",
  "members/sample_033/tests/ex02_2",
  "members/sample_034/raw_code",
  "members/sample_034/tests/ex02_0",
  "members/sample_034/tests/ex02_1",
  "members/sample_034/tests/ex02_2",
  "members/sample_035/raw_code",
  "members/sample_035/tests/ex02_0",
  "members/sample_035/tests/ex02_1",
  "members/sample_035/tests/ex02_2",
  "members/sample_036/raw_code",
  "members/sample_036/tests/ex02_0",
  "members/sample_036/tests/ex02_1",
  "members/sample_036/tests/ex02_2",
  "members/sample_037/raw_code",
  "members/sample_037/tests/ex02_0",
  "members/sample_037/tests/ex02_1",
  "members/sample_037/tests/ex02_2",
  "members/sample_038/raw_code",
  "members/sample_038/tests/ex02_0",
  "members/sample_038/tests/ex02_1",
  "members/sample_038/tests/ex02_2",
  "members/sample_039/raw_code",
  "members/sample_039/tests/ex02_0",
  "members/sample_039/tests/ex02_1",
  "members/sample_039/tests/ex02_2",
  "members/sample_040/raw_code",
  "members/sample_040/tests/ex02_0",
  "members/sample_040/tests/ex02_1",
  "members/sample_040/tests/ex02_2",
  "members/sample_041/raw_code",
  "members/sample_041/tests/ex02_0",
  "members/sample_041/tests/ex02_1",
  "members/sample_041/tests/ex02_2",
  "members/sample_042/raw_code",
  "members/sample_042/tests/ex02_0",
  "members/sample_042/tests/ex02_1",
  "members/sample_042/tests/ex02_2",
  "members/sample_043/raw_code",
  "members/sample_043/tests/ex02_0",
  "members/sample_043/tests/ex02_1",
  "members/sample_043/tests/ex02_2",
  "members/sample_044/raw_code",
  "members/sample_044/tests/ex02_0",
  "members/sample_044/tests/ex02_1",
  "members/sample_044/tests/ex02_2",
  "members/sample_045/raw_code",
  "members/sample_045/tests/ex02_0",
  "members/sample_045/tests/ex02_1",
  "members/sample_045/tests/ex02_2",
  "members/sample_046/raw_code",
  "members/sample_046/tests/ex02_0",
  "members/sample_046/tests/ex02_1",
  "members/sample_046/tests/ex02_2",
  "members/sample_047/raw_code",
  "members/sample_047/tests/ex02_0",
  "members/sample_047/tests/ex02_1",
  "members/sample_047/tests/ex02_2",
  "members/sample_048/raw_code",
  "members/sample_048/tests/ex02_0",
  "members/sample_048/tests/ex02_1",
  "members/sample_048/tests/ex02_2",
  "members/sample_049/raw_code",
  "members/sample_049/tests/ex02_0",
  "members/sample_049/tests/ex02_1",
  "members/sample_049/tests/ex02_2",
  "members/sample_050/raw_code",
  "members/sample_050/tests/ex02_0",
  "members/sample_050/tests/ex02_1",
  "members/sample_050/tests/ex02_2",
  "members/sample_051/raw_code",
  "members/sample_051/tests/ex02_0",
  "members/sample_051/tests/ex02_1",
  "members/sample_051/tests/ex02_2",
  "members/sample_052/raw_code",
  "members/sample_052/tests/ex02_0",
  "members/sample_052/tests/ex02_1",
  "members/sample_052/tests/ex02_2",
  "members/sample_053/raw_code",
  "members/sample_053/tests/ex02_0",
  "members/sample_053/tests/ex02_1",
  "members/sample_053/tests/ex02_2",
  "members/sample_054/raw_code",
  "members/sample_054/tests/ex02_0",
  "members/sample_054/tests/ex02_1",
  "members/sample_054/tests/ex02_2",
  "members/sample_055/raw_code",
  "members/sample_055/tests/ex02_0",
  "members/sample_055/tests/ex02_1",
  "members/sample_055/tests/ex02_2",
  "members/sample_056/raw_code",
  "members/sample_056/tests/ex02_0",
  "members/sample_056/tests/ex02_1",
  "members/sample_056/tests/ex02_2",
  "members/sample_057/raw_code",
  "members/sample_057/tests/ex02_0",
  "members/sample_057/tests/ex02_1",
  "members/sample_057/tests/ex02_2",
  "members/sample_058/raw_code",
  "members/sample_058/tests/ex02_0",
  "members/sample_058/tests/ex02_1",
  "members/sample_058/tests/ex02_2",
  "members/sample_059/raw_code",
  "members/sample_059/tests/ex02_0",
  "members/sample_059/tests/ex02_1",
  "members/sample_059/tests/ex02_2",
  "members/sample_060/raw_code",
  "members/sample_060/tests/ex02_0",
  "members/sample_060/tests/ex02_1",
  "members/sample_060/tests/ex02_2",
  "members/sample_061/raw_code",
  "members/sample_061/tests/ex02_0",
  "members/sample_061/tests/ex02_1",
  "members/sample_061/tests/ex02_2",
  "members/sample_062/raw_code",
  "members/sample_062/tests/ex02_0",
  "members/sample_062/tests/ex02_1",
  "members/sample_062/tests/ex02_2",
  "members/sample_063/raw_code",
  "members/sample_063/tests/ex02_0",
  "members/sample_063/tests/ex02_1",
  "members/sample_063/tests/ex02_2",
  "members/sample_064/raw_code",
  "members/sample_064/tests/ex02_0",
  "members/sample_064/tests/ex02_1",
  "members/sample_064/tests/ex02_2",
  "members/sample_065/raw_code",
  "members/sample_065/tests/ex02_0",
  "members/sample_065/tests/ex02_1",
  "members/sample_065/tests/ex02_2",
  "members/sample_066/raw_code",
  "members/sample_066/tests/ex02_0",
  "members/sample_066/tests/ex02_1",
  "members/sample_066/tests/ex02_2",
  "members/sample_067/raw_code",
  "members/sample_067/tests/ex02_0",
  "members/sample_067/tests/ex02_1",
  "members/sample_067/tests/ex02_2",
  "members/sample_068/raw_code",
  "members/sample_068/tests/ex02_0",
  "members/sample_068/tests/ex02_1",
  "members/sample_068/tests/ex02_2",
  "members/sample_069/raw_code",
  "members/sample_069/tests/ex02_0",
  "members/sample_069/tests/ex02_1",
  "members/sample_069/tests/ex02_2",
  "members/sample_070/raw_code",
  "members/sample_070/tests/ex02_0",
  "members/sample_070/tests/ex02_1",
  "members/sample_070/tests/ex02_2",
  "members/sample_071/raw_code",
  "members/sample_071/tests/ex02_0",
  "members/sample_071/tests/ex02_1",
  "members/sample_071/tests/ex02_2",
  "members/sample_072/raw_code",
  "members/sample_072/tests/ex02_0",
  "members/sample_072/tests/ex02_1",
  "members/sample_072/tests/ex02_2",
  "members/sample_073/raw_code",
  "members/sample_073/tests/ex02_0",
  "members/sample_073/tests/ex02_1",
  "members/sample_073/tests/ex02_2",
  "members/sample_074/raw_code",
  "members/sample_074/tests/ex02_0",
  "members/sample_074/tests/ex02_1",
  "members/sample_074/tests/ex02_2",
  "members/sample_075/raw_code",
  "members/sample_075/tests/ex02_0",
  "members/sample_075/tests/ex02_1",
  "members/sample_075/tests/ex02_2",
  "members/sample_076/raw_code",
  "members/sample_076/tests/ex02_0",
  "members/sample_076/tests/ex02_1",
  "members/sample_076/tests/ex02_2",
  "members/sample_077/raw_code",
  "members/sample_077/tests/ex02_0",
  "members/sample_077/tests/ex02_1",
  "members/sample_077/tests/ex02_2",
  "members/sample_078/raw_code",
  "members/sample_078/tests/ex02_0",
  "members/sample_078/tests/ex02_1",
  "members/sample_078/tests/ex02_2",
  "members/sample_079/raw_code",
  "members/sample_079/tests/ex02_0",
  "members/sample_079/tests/ex02_1",
  "members/sample_079/tests/ex02_2",
  "members/sample_080/raw_code",
  "members/sample_080/tests/ex02_0",
  "members/sample_080/tests/ex02_1",
  "members/sample_080/tests/ex02_2",
  "members/sample_081/raw_code",
  "members/sample_081/tests/ex02_0",
  "members/sample_081/tests/ex02_1",
  "members/sample_081/tests/ex02_2",
  "members/sample_082/raw_code",
  "members/sample_082/tests/ex02_0",
  "members/sample_082/tests/ex02_1",
  "members/sample_082/tests/ex02_2",
  "members/sample_083/raw_code",
  "members/sample_083/tests/ex02_0",
  "members/sample_083/tests/ex02_1",
  "members/sample_083/tests/ex02_2",
  "members/sample_084/raw_code",
  "members/sample_084/tests/ex02_0",
  "members/sample_084/tests/ex02_1",
  "members/sample_084/tests/ex02_2",
  "members/sample_085/raw_code",
  "members/sample_085/tests/ex02_0",
  "members/sample_085/tests/ex02_1",
  "members/sample_085/tests/ex02_2",
  "members/sample_086/raw_code",
  "members/sample_086/tests/ex02_0",
  "members/sample_086/tests/ex02_1",
  "members/sample_086/tests/ex02_2",
  "members/sample_087/raw_code",
  "members/sample_087/tests/ex02_0",
  "members/sample_087/tests/ex02_1",
  "members/sample_087/tests/ex02_2",
  "members/sample_088/raw_code",
  "members/sample_088/tests/ex02_0",
  "members/sample_088/tests/ex02_1",
  "members/sample_088/tests/ex02_2",
  "members/sample_089/raw_code",
  "members/sample_089/tests/ex02_0",
  "members/sample_089/tests/ex02_1",
  "members/sample_089/tests/ex02_2",
  "members/sample_090/raw_code",
  "members/sample_090/tests/ex02_0",
  "members/sample_090/tests/ex02_1",
  "members/sample_090/tests/ex02_2",
  "members/sample_091/raw_code",
  "members/sample_091/tests/ex02_0",
  "members/sample_091/tests/ex02_1",
  "members/sample_091/tests/ex02_2",
  "members/sample_092/raw_code",
  "members/sample_092/tests/ex02_0",
  "members/sample_092/tests/ex02_1",
  "members/sample_092/tests/ex02_2",
  "members/sample_093/raw_code",
  "members/sample_093/tests/ex02_0",
  "members/sample_093/tests/ex02_1",
  "members/sample_093/tests/ex02_2",
  "members/sample_094/raw_code",
  "members/sample_094/tests/ex02_0",
  "members/sample_094/tests/ex02_1",
  "members/sample_094/tests/ex02_2",
  "members/sample_095/raw_code",
  "members/sample_095/tests/ex02_0",
  "members/sample_095/tests/ex02_1",
  "members/sample_095/tests/ex02_2",
  "members/sample_096/raw_code",
  "members/sample_096/tests/ex02_0",
  "members/sample_096/tests/ex02_1",
  "members/sample_096/tests/ex02_2",
  "members/sample_097/raw_code",
  "members/sample_097/tests/ex02_0",
  "members/sample_097/tests/ex02_1",
  "members/sample_097/tests/ex02_2",
  "members/sample_098/raw_code",
  "members/sample_098/tests/ex02_0",
  "members/sample_098/tests/ex02_1",
  "members/sample_098/tests/ex02_2",
  "members/sample_099/raw_code",
  "members/sample_099/tests/ex02_0",
  "members/sample_099/tests/ex02_1",
  "members/sample_099/tests/ex02_2"
]
```
