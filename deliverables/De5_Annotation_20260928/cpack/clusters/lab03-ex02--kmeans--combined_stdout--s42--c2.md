# lab03-ex02--kmeans--combined_stdout--s42--c2

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 41; phân vùng: {'train': 36, 'validation': 5}.


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
    "n_cluster": 41,
    "n_observed": 41,
    "n_failed": 41,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 41
    }
  },
  {
    "test_id": "ex02_1",
    "n_cluster": 41,
    "n_observed": 41,
    "n_failed": 41,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 41
    }
  },
  {
    "test_id": "ex02_2",
    "n_cluster": 41,
    "n_observed": 41,
    "n_failed": 41,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 41
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex02_2:edit_band",
    "value": "medium",
    "n": 37,
    "n_cluster": 41,
    "rate": 0.9024390243902439,
    "cohort_rate": 0.3065326633165829,
    "difference_from_cohort": 0.595906361073661
  },
  {
    "feature": "stdout:ex02_1:edit_band",
    "value": "medium",
    "n": 39,
    "n_cluster": 41,
    "rate": 0.9512195121951219,
    "cohort_rate": 0.36180904522613067,
    "difference_from_cohort": 0.5894104669689912
  },
  {
    "feature": "stdout:ex02_0:edit_band",
    "value": "medium",
    "n": 39,
    "n_cluster": 41,
    "rate": 0.9512195121951219,
    "cohort_rate": 0.4120603015075377,
    "difference_from_cohort": 0.5391592106875842
  },
  {
    "feature": "stdout:ex02_1:relation",
    "value": "whitespace",
    "n": 41,
    "n_cluster": 41,
    "rate": 1.0,
    "cohort_rate": 0.6934673366834171,
    "difference_from_cohort": 0.3065326633165829
  },
  {
    "feature": "stdout:ex02_2:relation",
    "value": "whitespace",
    "n": 41,
    "n_cluster": 41,
    "rate": 1.0,
    "cohort_rate": 0.6934673366834171,
    "difference_from_cohort": 0.3065326633165829
  },
  {
    "feature": "stdout:ex02_0:relation",
    "value": "whitespace",
    "n": 41,
    "n_cluster": 41,
    "rate": 1.0,
    "cohort_rate": 0.7386934673366834,
    "difference_from_cohort": 0.2613065326633166
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 33,
    "n_cluster": 41,
    "rate": 0.8048780487804879,
    "cohort_rate": 0.6984924623115578,
    "difference_from_cohort": 0.10638558646893004
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 39,
    "n_cluster": 41,
    "rate": 0.9512195121951219,
    "cohort_rate": 0.8994974874371859,
    "difference_from_cohort": 0.05172202475793597
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 40,
    "n_cluster": 41,
    "rate": 0.975609756097561,
    "cohort_rate": 0.9246231155778895,
    "difference_from_cohort": 0.0509866405196715
  },
  {
    "feature": "ast:c_while",
    "value": "0",
    "n": 28,
    "n_cluster": 41,
    "rate": 0.6829268292682927,
    "cohort_rate": 0.6633165829145728,
    "difference_from_cohort": 0.019610246353719885
  },
  {
    "feature": "ast:c_for",
    "value": "0",
    "n": 7,
    "n_cluster": 41,
    "rate": 0.17073170731707318,
    "cohort_rate": 0.15577889447236182,
    "difference_from_cohort": 0.014952812844711366
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 41,
    "n_cluster": 41,
    "rate": 1.0,
    "cohort_rate": 0.9899497487437185,
    "difference_from_cohort": 0.01005025125628145
  },
  {
    "feature": "ast:c_update",
    "value": "0",
    "n": 1,
    "n_cluster": 41,
    "rate": 0.024390243902439025,
    "cohort_rate": 0.01507537688442211,
    "difference_from_cohort": 0.009314867018016915
  },
  {
    "feature": "test:ex02_0",
    "value": "fail",
    "n": 41,
    "n_cluster": 41,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "test:ex02_1",
    "value": "fail",
    "n": 41,
    "n_cluster": 41,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "test:ex02_2",
    "value": "fail",
    "n": 41,
    "n_cluster": 41,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 40,
    "n_cluster": 41,
    "rate": 0.975609756097561,
    "cohort_rate": 0.9849246231155779,
    "difference_from_cohort": -0.009314867018016981
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 34,
    "n_cluster": 41,
    "rate": 0.8292682926829268,
    "cohort_rate": 0.8442211055276382,
    "difference_from_cohort": -0.014952812844711394
  },
  {
    "feature": "ast:c_while",
    "value": "1",
    "n": 13,
    "n_cluster": 41,
    "rate": 0.3170731707317073,
    "cohort_rate": 0.33668341708542715,
    "difference_from_cohort": -0.01961024635371983
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "0",
    "n": 1,
    "n_cluster": 41,
    "rate": 0.024390243902439025,
    "cohort_rate": 0.07537688442211055,
    "difference_from_cohort": -0.05098664051967152
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 33,
    "n_cluster": 41,
    "rate": 0.8048780487804879,
    "cohort_rate": 0.6984924623115578,
    "difference_from_cohort": 0.10638558646893004
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 39,
    "n_cluster": 41,
    "rate": 0.9512195121951219,
    "cohort_rate": 0.8994974874371859,
    "difference_from_cohort": 0.05172202475793597
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 40,
    "n_cluster": 41,
    "rate": 0.975609756097561,
    "cohort_rate": 0.9246231155778895,
    "difference_from_cohort": 0.0509866405196715
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 41,
    "n_cluster": 41,
    "rate": 1.0,
    "cohort_rate": 0.9899497487437185,
    "difference_from_cohort": 0.01005025125628145
  },
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 41,
    "n_cluster": 41,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 40,
    "n_cluster": 41,
    "rate": 0.975609756097561,
    "cohort_rate": 0.9849246231155779,
    "difference_from_cohort": -0.009314867018016981
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 34,
    "n_cluster": 41,
    "rate": 0.8292682926829268,
    "cohort_rate": 0.8442211055276382,
    "difference_from_cohort": -0.014952812844711394
  }
]
```


## IF–THEN dự đoán cluster, không dự đoán gold

```json
[
  {
    "rule_id": 7,
    "if": [
      "stdout:ex02_1:relation=whitespace",
      "NOT (stdout:ex02_1:edit_band=small)"
    ],
    "then_cluster": 2,
    "train_support": 34,
    "train_precision": 1.0,
    "holdout_support": 5,
    "holdout_precision": 1.0
  },
  {
    "rule_id": 10,
    "if": [
      "stdout:ex02_1:relation=whitespace",
      "stdout:ex02_1:edit_band=small",
      "stdout:ex02_2:edit_band=medium"
    ],
    "then_cluster": 2,
    "train_support": 3,
    "train_precision": 0.6666666666666666,
    "holdout_support": 0,
    "holdout_precision": null
  }
]
```


## Candidate chưa xác thực

```json
{
  "source": "local_heuristic_not_gold",
  "misconception_name": "Chưa đủ bằng chứng để đặt tên lỗi",
  "misconception_type": null,
  "reasoning": "Có 41 bài trong cụm. Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
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

sample_009, sample_008, sample_019, sample_022

## sample_008 — train — đại diện

```c
# include <stdio.h>

void piramide(int N){
    int num=1,cont=1,num_espacos=N,N1=cont;
    while(cont<=N){
        while(num_espacos!=0){
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
  "sample_id": "sample_008",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "2fdb832fe14ed733efc1b327a412500a248eec72d02f952a803a873f236c03d4",
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
      "output": "      1\n    1 2 1 \n  1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "        1\n      1 2 1 \n    1 2 3 2 1 \n  1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "                1\n              1 2 1 \n            1 2 3 2 1 \n          1 2 3 4 3 2 1 \n        1 2 3 4 5 4 3 2 1 \n      1 2 3 4 5 6 5 4 3 2 1 \n    1 2 3 4 5 6 7 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
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
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
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


## sample_009 — train — đại diện

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
            if (j)
                putchar(' ');
            if (i + j - n - 1> 0) 
                printf("%d", i + j - n - 1);
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
  "sample_id": "sample_009",
  "partition": "train",
  "representative": true,
  "is_train_medoid": true,
  "raw_code_truncated": false,
  "source_sha256": "0a5601f9b9229a596286880fe7361a28fce891feeef7cb408cfe55dfcc222d26",
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
      "output": "     1   \n   1 2 1  \n 1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1    \n     1 2 1   \n   1 2 3 2 1  \n 1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1        \n             1 2 1       \n           1 2 3 2 1      \n         1 2 3 4 3 2 1     \n       1 2 3 4 5 4 3 2 1    \n     1 2 3 4 5 6 5 4 3 2 1   \n   1 2 3 4 5 6 7 6 5 4 3 2 1  \n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
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
    "stdout:ex02_1:edit_band": "medium",
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


## sample_019 — validation — đại diện

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
        for (j=1; j<=(2*(N-i)); j++)
            printf(" ");
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
  "sample_id": "sample_019",
  "partition": "validation",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "d7a007f12606216efb43c8fb819a455fc2f5c93d338084cb8809556da43f9df6",
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
      "output": "    1     \n  1 2 1   \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1       \n    1 2 1     \n  1 2 3 2 1   \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1               \n            1 2 1             \n          1 2 3 2 1           \n        1 2 3 4 3 2 1         \n      1 2 3 4 5 4 3 2 1       \n    1 2 3 4 5 6 5 4 3 2 1     \n  1 2 3 4 5 6 7 6 5 4 3 2 1   \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
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
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
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


## sample_022 — train — đại diện

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
        for (j = 1; j <= N-i; j++) {
            printf("  ");
        }
        printf("\n");
    }
}


```

```json
{
  "sample_id": "sample_022",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "8d3868ef85927a0a6ab3b23a8bb26c84e760bc247d637f7709c29d128a7a6045",
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
      "output": "    1     \n  1 2 1   \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1       \n    1 2 1     \n  1 2 3 2 1   \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1               \n            1 2 1             \n          1 2 3 2 1           \n        1 2 3 4 3 2 1         \n      1 2 3 4 5 4 3 2 1       \n    1 2 3 4 5 6 5 4 3 2 1     \n  1 2 3 4 5 6 7 6 5 4 3 2 1   \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
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
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "medium"
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


## sample_001 — train

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
		for (coluna = N-linha; coluna > 0; coluna--) {
			printf("  ");
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
  "sample_id": "sample_001",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "e1d92d9a5cc01b60c5a398dc90d688e8ce9afa7ca8b41dd8dac4fca2f4c24694",
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
      "output": "    1     \n  1 2 1   \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1       \n    1 2 1     \n  1 2 3 2 1   \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1               \n            1 2 1             \n          1 2 3 2 1           \n        1 2 3 4 3 2 1         \n      1 2 3 4 5 4 3 2 1       \n    1 2 3 4 5 6 5 4 3 2 1     \n  1 2 3 4 5 6 7 6 5 4 3 2 1   \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
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
    "stdout:ex02_1:edit_band": "medium",
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


## sample_002 — train

```c
#include <stdio.h>

void piramide(int n){
    int i = 1, j, k;
    while(i <= n){
        j = 1;
        while(j <= (2*n - 1)){
            if(j > n){
                k = n - (j - n);
            } else {
                k = j;
            }
            k = k - (n - i);
            if(k <= 0){
                printf("%c", ' ');
            } else {
                printf("%d", k);
            }
            
            printf("%c", ' ');
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
  "sample_id": "sample_002",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "aae2d283d4291af8bcedb6004f7c22ff421fd4ba8cea2fd09805930beb74a0e2",
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
      "output": "    1     \n  1 2 1   \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1       \n    1 2 1     \n  1 2 3 2 1   \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1               \n            1 2 1             \n          1 2 3 2 1           \n        1 2 3 4 3 2 1         \n      1 2 3 4 5 4 3 2 1       \n    1 2 3 4 5 6 5 4 3 2 1     \n  1 2 3 4 5 6 7 6 5 4 3 2 1   \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
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
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "medium"
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


## sample_003 — train

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
            if(k <= 0){
                printf("%c", ' ');
            } else {
                printf("%d", k);
            }
            if(j < 2*n){
                printf("%c", ' ');
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
  "sample_id": "sample_003",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "18d2fdd2ca06feb47b46544851d24ae25a9b28843cbbbea41686b3a90ccb141c",
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
      "output": "    1      \n  1 2 1    \n1 2 3 2 1  \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1        \n    1 2 1      \n  1 2 3 2 1    \n1 2 3 4 3 2 1  \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1                \n            1 2 1              \n          1 2 3 2 1            \n        1 2 3 4 3 2 1          \n      1 2 3 4 5 4 3 2 1        \n    1 2 3 4 5 6 5 4 3 2 1      \n  1 2 3 4 5 6 7 6 5 4 3 2 1    \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1  \n"
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
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "medium"
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


## sample_004 — train

```c
#include <stdio.h>

void piramide(int n){
    int i = 1, j, k;
    while(i <= n){
        j = 1;
        while(j <= (2*n - 1)){
            if(j > n){
                k = n - (j - n);
            } else {
                k = j;
            }
            k = k - (n - i);
            if(k <= 0){
                printf("%c", ' ');
            } else {
                printf("%d", k);
            }

            if(j < (2*n - 1)){
                printf("%c", ' ');
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
  "sample_id": "sample_004",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "741d050ed37527b04b6a32088ad943aa8ad582b19c3678161e7ad2f01a98b0c5",
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
      "output": "    1    \n  1 2 1  \n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1      \n    1 2 1    \n  1 2 3 2 1  \n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1              \n            1 2 1            \n          1 2 3 2 1          \n        1 2 3 4 3 2 1        \n      1 2 3 4 5 4 3 2 1      \n    1 2 3 4 5 6 5 4 3 2 1    \n  1 2 3 4 5 6 7 6 5 4 3 2 1  \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
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
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "medium"
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


## sample_005 — train

```c
#include <stdio.h>

void piramide(int n){
    int i = 1, j, k;
    while(i <= n){
        j = 1;
        while(j <= (2*n - 1)){
            if(j > n){
                k = n - (j - n);
            } else {
                k = j;
            }
            k = k - (n - i);
            if(k <= 0){
                printf("%c", ' ');
            } else {
                printf("%d", k);
            }
            if(j < 2*n){
                printf("%c", ' ');
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
  "sample_id": "sample_005",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "5a6a61103836e3686243a1bf81a09a770362d1f44915f818e42866124e4cd95b",
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
      "output": "    1     \n  1 2 1   \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1       \n    1 2 1     \n  1 2 3 2 1   \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1               \n            1 2 1             \n          1 2 3 2 1           \n        1 2 3 4 3 2 1         \n      1 2 3 4 5 4 3 2 1       \n    1 2 3 4 5 6 5 4 3 2 1     \n  1 2 3 4 5 6 7 6 5 4 3 2 1   \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
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
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "medium"
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


## sample_006 — train

```c
#include <stdio.h>

void piramide (int N)  {
 
 #define ESPACOS 8
 #define NUMEROS 1
 int i, espacos = ESPACOS, j, numeros = NUMEROS, k;

 for (i = 1; i <= N; i++) {

   for (j = 0; j < espacos; j++)  {

    printf(" "); }

  espacos -= 2;

  for (k=1 ; k<= numeros; k++)  {
 
   if ( (k <= i)&& i != 1) {
    printf ("%d ", k); }

   else  {

      if (i - ( k -i) == 1)

        printf ("%d", i - (k-i));

     else
    
        printf("%d ", i - (k-i));} }

  numeros += 2; 
  printf ("\n"); }
}


int main()  {

 int N;

 scanf ("%d", &N);
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
  "source_sha256": "5a6a89edeb3192aa8c16e47469ea944cf4038c9439a5a2c5633ba4602508b2bb",
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
      "output": "        1\n      1 2 1\n    1 2 3 2 1\n"
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
      "output": "        1\n      1 2 1\n    1 2 3 2 1\n  1 2 3 4 3 2 1\n1 2 3 4 5 4 3 2 1\n1 2 3 4 5 6 5 4 3 2 1\n1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
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


## sample_007 — train

```c
#include <stdio.h>

void piramide (int N)  {

 
 #define ESPACOS 8
 #define NUMEROS 1
 int i, espacos = ESPACOS, j, numeros = NUMEROS, k;

 for (i = 1; i <= N; i++) {

   for (j = 0; j < espacos; j++)  {

    printf(" "); }

  espacos -= 2;

  for (k=1 ; k<= numeros; k++)  {
 
   if ( (k <= i)&& i != 1) {
    printf ("%d ", k); }

   else  {

      if (i - ( k -i) == 1)

        printf ("%d", i - (k-i));

     else
    
        printf("%d ", i - (k-i));} }

  numeros += 2; 
  printf ("\n"); }
}


int main()  {

 int N;

 scanf ("%d", &N);
 piramide(N);
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
  "source_sha256": "11cfac8068e697390112683675e0057dd88abd68fbb55827c5ebe4782d2a43ef",
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
      "output": "        1\n      1 2 1\n    1 2 3 2 1\n"
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
      "output": "        1\n      1 2 1\n    1 2 3 2 1\n  1 2 3 4 3 2 1\n1 2 3 4 5 4 3 2 1\n1 2 3 4 5 6 5 4 3 2 1\n1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
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


## sample_010 — train

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
            if (j)
                putchar(' ');
            if (i + j - n - 1> 0) 
                printf("%d", i + j - n - 1);
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
  "sample_id": "sample_010",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "a8b8fa160ed27cb52116935c7f8c843f084d6e8cd376a03d788e11ef3529d2da",
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
      "output": "     1   \n   1 2 1  \n 1 2 3 2 1 "
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1    \n     1 2 1   \n   1 2 3 2 1  \n 1 2 3 4 3 2 1 "
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1        \n             1 2 1       \n           1 2 3 2 1      \n         1 2 3 4 3 2 1     \n       1 2 3 4 5 4 3 2 1    \n     1 2 3 4 5 6 5 4 3 2 1   \n   1 2 3 4 5 6 7 6 5 4 3 2 1  \n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 "
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
    "stdout:ex02_1:edit_band": "medium",
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


## sample_011 — train

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
            if (j)
                putchar(' ');
            if (i + j - n - 1> 0) 
                printf("%d", i + j - n - 1);
            else
                putchar(' ');
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
  "sample_id": "sample_011",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "72e8d05f1d9c02d385cf6bfb1c186f9d541a53ab31398790a1680abd22f95ca7",
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
      "output": "     1      \n   1 2 1    \n 1 2 3 2 1  \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1        \n     1 2 1      \n   1 2 3 2 1    \n 1 2 3 4 3 2 1  \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1                \n             1 2 1              \n           1 2 3 2 1            \n         1 2 3 4 3 2 1          \n       1 2 3 4 5 4 3 2 1        \n     1 2 3 4 5 6 5 4 3 2 1      \n   1 2 3 4 5 6 7 6 5 4 3 2 1    \n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1  \n"
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
    "stdout:ex02_1:edit_band": "medium",
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


## sample_012 — train

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
            if (j)
                putchar(' ');
            if (i + j - n - 1> 0) 
                printf("%d", i + j - n - 1);
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
  "sample_id": "sample_012",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "6cdfa065a55389d3c60fcf201e497b32345e70ddc707c11272fd5b53af3b49b0",
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
      "output": "     1   \n   1 2 1  \n 1 2 3 2 1 "
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1    \n     1 2 1   \n   1 2 3 2 1  \n 1 2 3 4 3 2 1 "
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1        \n             1 2 1       \n           1 2 3 2 1      \n         1 2 3 4 3 2 1     \n       1 2 3 4 5 4 3 2 1    \n     1 2 3 4 5 6 5 4 3 2 1   \n   1 2 3 4 5 6 7 6 5 4 3 2 1  \n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 "
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
    "stdout:ex02_1:edit_band": "medium",
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


## sample_013 — train

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
            if (j)
                putchar(' ');
            if (i + j - n - 1> 0) 
                printf("%d", i + j - n - 1);
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
  "sample_id": "sample_013",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "689b765008c6e75217558dbdfa4f93e9a7bd61dc3370cbaea31d249ae6d27c99",
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
      "output": "     1   \n   1 2 1  \n 1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1    \n     1 2 1   \n   1 2 3 2 1  \n 1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1        \n             1 2 1       \n           1 2 3 2 1      \n         1 2 3 4 3 2 1     \n       1 2 3 4 5 4 3 2 1    \n     1 2 3 4 5 6 5 4 3 2 1   \n   1 2 3 4 5 6 7 6 5 4 3 2 1  \n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
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
    "stdout:ex02_1:edit_band": "medium",
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


## sample_014 — train

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
            if (j)
                putchar(' ');
            if (i + j - n - 1> 0) 
                printf("%d", i + j - n - 1);
            else
                putchar(' ');
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
  "sample_id": "sample_014",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "3484cd2383a81d1265fa79165b7b0d6cde9738734138fcc91b86b655db1b4d58",
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
      "output": "     1      \n   1 2 1    \n 1 2 3 2 1  \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1        \n     1 2 1      \n   1 2 3 2 1    \n 1 2 3 4 3 2 1  \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1                \n             1 2 1              \n           1 2 3 2 1            \n         1 2 3 4 3 2 1          \n       1 2 3 4 5 4 3 2 1        \n     1 2 3 4 5 6 5 4 3 2 1      \n   1 2 3 4 5 6 7 6 5 4 3 2 1    \n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1  \n"
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
    "stdout:ex02_1:edit_band": "medium",
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


## sample_015 — train

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
            if (j)
                putchar(' ');
            if (i + j - n - 1> 0) 
                printf("%d", i + j - n - 1);
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
  "sample_id": "sample_015",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "b01a721f2a8ba08d7abeeaf3b825ea623fc642b8d0b41b80820c667fd8fcf47a",
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
      "output": "     1   \n   1 2 1  \n 1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1    \n     1 2 1   \n   1 2 3 2 1  \n 1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1        \n             1 2 1       \n           1 2 3 2 1      \n         1 2 3 4 3 2 1     \n       1 2 3 4 5 4 3 2 1    \n     1 2 3 4 5 6 5 4 3 2 1   \n   1 2 3 4 5 6 7 6 5 4 3 2 1  \n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
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
    "stdout:ex02_1:edit_band": "medium",
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


## sample_016 — train

```c

#include <stdio.h>

void piramide(int n)
{
    int i, j; 
    for(j = 1; j <= n; j++){
        for(i = j - n + 1; i <= j; i++){
            if (i < 1){
                printf("  ");  
            }
            else{
                printf("%d ", i);
           }     
        }
        for(i = j - 1; i >= j - n + 2; i--){
            if (i < 1){
                printf("  ");  
            }
            else{
                printf("%d ", i);
           }
        }
        if (j - n + 1 < 1){
                printf(" \n");  
            }
            else{
                printf("%d\n", i);
           }
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
  "sample_id": "sample_016",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "052cba17c03fc3fe0df87eb3ab5923238ee5a9a04e3e9292e6628cb09b7f87be",
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
      "output": "    1    \n  1 2 1  \n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1      \n    1 2 1    \n  1 2 3 2 1  \n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1              \n            1 2 1            \n          1 2 3 2 1          \n        1 2 3 4 3 2 1        \n      1 2 3 4 5 4 3 2 1      \n    1 2 3 4 5 6 5 4 3 2 1    \n  1 2 3 4 5 6 7 6 5 4 3 2 1  \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
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
    "stdout:ex02_1:edit_band": "medium",
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


## sample_017 — train

```c

#include <stdio.h>

void piramide(int N) {
    int i, j;
    for (i = 0; i < N; i++) {
        for (j = N - 1 - i; j > 0; j--) 
            printf("  ");
        for (j = 1; j <= 1 + i; j++) {
            printf("%d", j);
            printf(" ");
        }
        for (j -= 2; j > 0; j--) {
            printf("%d", j);
            printf(" ");
        }
        for (j = N - 2 - i; j > 0; j--) 
            printf("  ");
        printf("\n");
    }
    return;
}

int main() {
    int N;
    scanf("%d", &N);
    if (N < 2)
        return 1;
    piramide(N);
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
  "source_sha256": "628e8cf24f43d04b67f8178cfad33405b313b73f067f410b8eda51b6784ec672",
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
      "output": "    1   \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1     \n    1 2 1   \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1             \n            1 2 1           \n          1 2 3 2 1         \n        1 2 3 4 3 2 1       \n      1 2 3 4 5 4 3 2 1     \n    1 2 3 4 5 6 5 4 3 2 1   \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
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
    "stdout:ex02_1:edit_band": "medium",
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


## sample_018 — train

```c

#include <stdio.h>
 
void piramide(int N) {
    int i, j;
    for (i = 0; i < N; i++) {
        for (j = N - 1 - i; j > 0; j--) 
            printf("  ");
        for (j = 1; j <= 1 + i; j++) {
            printf("%d", j);
            printf(" ");
        }
        for (j -= 2; j > 0; j--) {
            printf("%d", j);
            printf(" ");
        }
        for (j = N - 2 - i; j > 0; j--) 
            printf("  ");
        printf("\n");
    }
    return;
}

int main() {
    int N;
    scanf("%d", &N);
    if (N < 2)
        return 1;
    piramide(N);
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
  "source_sha256": "5a3c4469faf066c81ac06160088af6b2f1374a2b7e2c729b094c376edf781a64",
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
      "output": "    1   \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1     \n    1 2 1   \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1             \n            1 2 1           \n          1 2 3 2 1         \n        1 2 3 4 3 2 1       \n      1 2 3 4 5 4 3 2 1     \n    1 2 3 4 5 6 5 4 3 2 1   \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
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
    "stdout:ex02_1:edit_band": "medium",
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


## sample_020 — validation

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
        for (j=1; j<=(2*(N-i)); j++)
            printf(" ");
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
  "sample_id": "sample_020",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "0c21cf276ccfa48158e875153c387f117b05e917f59835396548873d9c690870",
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
      "output": "    1     \n  1 2 1   \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1       \n    1 2 1     \n  1 2 3 2 1   \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1               \n            1 2 1             \n          1 2 3 2 1           \n        1 2 3 4 3 2 1         \n      1 2 3 4 5 4 3 2 1       \n    1 2 3 4 5 6 5 4 3 2 1     \n  1 2 3 4 5 6 7 6 5 4 3 2 1   \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
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
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
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


## sample_021 — train

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
            if (m==1)
            {
                printf("%d ",m);
            }
            else{
                printf("%d\n",m);
            }
        }
    }
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
  "source_sha256": "8e1bc26bf2abecd1521c2f66115c51fd2d625bc8dec65d1dfa6f9a66daac0749",
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
      "output": "    1   1 2 1 1 2 3 2\n1 "
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1     1 2 1   1 2 3 2\n1 1 2 3 4 3\n2\n1 "
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1             1 2 1           1 2 3 2\n1         1 2 3 4 3\n2\n1       1 2 3 4 5 4\n3\n2\n1     1 2 3 4 5 6 5\n4\n3\n2\n1   1 2 3 4 5 6 7 6\n5\n4\n3\n2\n1 1 2 3 4 5 6 7 8 7\n6\n5\n4\n3\n2\n1 "
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
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "medium"
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


## sample_023 — train

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

        for(j = 1; j <= i; j ++){
            printf("%d ", j);
        }

        for(k= i-1; k > 0; k--){
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
  "sample_id": "sample_023",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "b159f7263098c32d81beb4bc298ab05b0819e72840502cce4f46af99fb1092bf",
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
      "output": "  1 \n 1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "   1 \n  1 2 1 \n 1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "       1 \n      1 2 1 \n     1 2 3 2 1 \n    1 2 3 4 3 2 1 \n   1 2 3 4 5 4 3 2 1 \n  1 2 3 4 5 6 5 4 3 2 1 \n 1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
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
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "medium"
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


## sample_024 — train

```c


#include <stdio.h>

void piramide(int N) {

    int base, i, j, k;
    base = 2 * N - 1;

    for (i = 1; i <= N; i++) {
        for (j = 1; j <= N - i + 1; j++) 
            printf(" ");
        for (k = 1; k <= N * 2 - 1; k++)
            if (k > N - i && k <= base / 2 + 1)
                printf("%d ", k - (N - i));
            else if (k < N + i && k >= base / 2 + 1)
                printf("%d ", (k - (N + i)) * (-1));
            else 
                printf(" ");
        printf("\n");
    }
    printf("\n");
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
  "sample_id": "sample_024",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "ebf882634ab68140381d5f09ee3b69083f9759f2dc25ed8dfc29128aa74c6787",
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
      "output": "     1   \n   1 2 1  \n 1 2 3 2 1 \n\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1    \n     1 2 1   \n   1 2 3 2 1  \n 1 2 3 4 3 2 1 \n\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1        \n             1 2 1       \n           1 2 3 2 1      \n         1 2 3 4 3 2 1     \n       1 2 3 4 5 4 3 2 1    \n     1 2 3 4 5 6 5 4 3 2 1   \n   1 2 3 4 5 6 7 6 5 4 3 2 1  \n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n\n"
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
    "stdout:ex02_1:edit_band": "medium",
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


## sample_025 — train

```c


#include <stdio.h>

void piramide(int N) {

    int base, i, j, k;
    base = 2 * N - 1;

    for (i = 1; i <= N; i++) {
        for (j = 1; j <= N - i + 1; j++) 
            putchar(' ');
        for (k = 1; k <= N * 2 - 1; k++)
            if (k > N - i && k <= base / 2 + 1)
                printf(" %d", k - (N - i));
            else if (k < N + i && k >= base / 2 + 1)
                printf(" %d", (k - (N + i)) * (-1));
            else 
                putchar(' ');
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
  "sample_id": "sample_025",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "461e32dd58c942e1a15b8d71242d2f84190f0bfe9c8f7a6cc68beb09001655f8",
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
      "output": "      1  \n    1 2 1 \n  1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "        1   \n      1 2 1  \n    1 2 3 2 1 \n  1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "                1       \n              1 2 1      \n            1 2 3 2 1     \n          1 2 3 4 3 2 1    \n        1 2 3 4 5 4 3 2 1   \n      1 2 3 4 5 6 5 4 3 2 1  \n    1 2 3 4 5 6 7 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
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
    "stdout:ex02_1:edit_band": "medium",
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


## sample_026 — train

```c


#include <stdio.h>

void piramide(int N) {

    int base, i, j, k;
    base = 2 * N - 1;

    for (i = 1; i <= N; i++) {
        for (j = 1; j <= N - i + 1; j++) 
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
  "sample_id": "sample_026",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "fb9a271625d4efdd98521d77d1c8a60d91b62b67f91008966cb648469d4f1885",
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
      "output": "      1 \n    1 2 1 \n  1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "        1 \n      1 2 1 \n    1 2 3 2 1 \n  1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "                1 \n              1 2 1 \n            1 2 3 2 1 \n          1 2 3 4 3 2 1 \n        1 2 3 4 5 4 3 2 1 \n      1 2 3 4 5 6 5 4 3 2 1 \n    1 2 3 4 5 6 7 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
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
    "stdout:ex02_1:edit_band": "medium",
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

void piramide(int N) {

    int base, i, j, k;
    base = 2 * N - 1;

    for (i = 1; i <= N; i++) {
        for (j = 1; j <= N - i + 1; j++) 
            printf(" ");
        for (k = 1; k <= N * 2 - 1; k++)
            if (k > N - i && k <= base / 2 + 1)
                printf("%d ", k - (N - i));
            else if (k < N + i && k >= base / 2 + 1)
                printf("%d ", (k - (N + i)) * (-1));
            else 
                printf(" ");
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
  "sample_id": "sample_027",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "6c6201c53aeea01af7227485756e5eee3983c990e9e89d92133a04ebe8d3831d",
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
      "output": "     1   \n   1 2 1  \n 1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1    \n     1 2 1   \n   1 2 3 2 1  \n 1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1        \n             1 2 1       \n           1 2 3 2 1      \n         1 2 3 4 3 2 1     \n       1 2 3 4 5 4 3 2 1    \n     1 2 3 4 5 6 5 4 3 2 1   \n   1 2 3 4 5 6 7 6 5 4 3 2 1  \n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
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
    "stdout:ex02_1:edit_band": "medium",
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


## sample_028 — train

```c


#include <stdio.h>

void piramide(int N) {

    int base, i, j, k;
    base = 2 * N - 1;

    for (i = 1; i <= N; i++) {
        for (j = 1; j <= N - i + 1; j++) 
            printf(" ");
        for (k = 1; k <= N * 2 - 1; k++)
            if (k > N - i && k <= base / 2 + 1)
                printf("%d ", k - (N - i));
            else if (k < N + i && k >= base / 2 + 1)
                printf("%d ", (k - (N + i)) * (-1));
            else 
                printf(" ");
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
  "sample_id": "sample_028",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "6c6201c53aeea01af7227485756e5eee3983c990e9e89d92133a04ebe8d3831d",
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
      "output": "     1   \n   1 2 1  \n 1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1    \n     1 2 1   \n   1 2 3 2 1  \n 1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1        \n             1 2 1       \n           1 2 3 2 1      \n         1 2 3 4 3 2 1     \n       1 2 3 4 5 4 3 2 1    \n     1 2 3 4 5 6 5 4 3 2 1   \n   1 2 3 4 5 6 7 6 5 4 3 2 1  \n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
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
    "stdout:ex02_1:edit_band": "medium",
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


## sample_029 — train

```c


#include <stdio.h>

void piramide(int N) {

    int base, i, j, k;
    base = 2 * N - 1;

    for (i = 1; i <= N; i++) {
        for (j = 1; j <= N - i + 1; j++) 
            printf(" ");
        for (k = 1; k <= N * 2 - 1; k++)
            if (k > N - i && k <= base / 2 + 1)
                printf("%d ", k - (N - i));
            else if (k < N + i && k >= base / 2 + 1)
                printf("%d ", (k - (N + i)) * (-1));
            else 
                printf(" ");
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
  "sample_id": "sample_029",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "e4adbc00b31639ca6809ad4e31bbd7772c542a7932d8df0cd2fb1eda97ce43d1",
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
      "output": "     1      1 2 1   1 2 3 2 1 "
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1         1 2 1      1 2 3 2 1   1 2 3 4 3 2 1 "
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1                     1 2 1                  1 2 3 2 1               1 2 3 4 3 2 1            1 2 3 4 5 4 3 2 1         1 2 3 4 5 6 5 4 3 2 1      1 2 3 4 5 6 7 6 5 4 3 2 1   1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 "
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
    "stdout:ex02_1:edit_band": "medium",
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


## sample_030 — train

```c


#include <stdio.h>

void piramide(int N) {

    int base, i, j, k;
    base = 2 * N - 1;

    for (i = 1; i <= N; i++) {
        for (j = 1; j <= N - i + 1; j++) 
            printf(" ");
        for (k = 1; k <= N * 2 - 1; k++)
            if (k > N - i && k <= base / 2 + 1)
                printf(" %d", k - (N - i));
            else if (k < N + i && k >= base / 2 + 1)
                printf(" %d", (k - (N + i)) * (-1));
            else 
                printf(" ");
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
  "sample_id": "sample_030",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "c6cd8a393da626dc2d2de03f8e02ef988f6e868af7155cd1908a7b0e9a865460",
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
      "output": "      1  \n    1 2 1 \n  1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "        1   \n      1 2 1  \n    1 2 3 2 1 \n  1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "                1       \n              1 2 1      \n            1 2 3 2 1     \n          1 2 3 4 3 2 1    \n        1 2 3 4 5 4 3 2 1   \n      1 2 3 4 5 6 5 4 3 2 1  \n    1 2 3 4 5 6 7 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
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
    "stdout:ex02_1:edit_band": "medium",
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


## sample_031 — train

```c

#include <stdio.h>

void piramide(int n){
	int i = 0, u, meio;

	for (; i < n; i++){
		for (u = 0; u < n - i - 1; u++){
			printf("  ");
		}
		for (meio = 0; meio < i + 1; meio++ ){
			printf("%d ", meio + 1);
		}
		for (meio--; meio >= 1; meio--){
			printf("%d ", meio);

		}
		for (u = 0; u < n - i - 1; u++){
			printf("  ");
		}
		printf("\n");
	}	
}

int main(){
	int n = 0;

	while (n < 2){
		scanf("%d", &n);
	}
	piramide(n);
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
  "source_sha256": "43c82bc3ffd00e4e9b6d51bc468575093e6647a417862cef2cc6f1c088196c2c",
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
      "output": "    1     \n  1 2 1   \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1       \n    1 2 1     \n  1 2 3 2 1   \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1               \n            1 2 1             \n          1 2 3 2 1           \n        1 2 3 4 3 2 1         \n      1 2 3 4 5 4 3 2 1       \n    1 2 3 4 5 6 5 4 3 2 1     \n  1 2 3 4 5 6 7 6 5 4 3 2 1   \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
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
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "medium"
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


## sample_032 — train

```c

#include <stdio.h>

int main(){

    int N;
    void piramide();

    scanf("%d", &N);
    piramide(N);

    return 0;

}

void piramide(int N){

    int i, incial = 1;
    
    while (incial <= N)
    {
    
        for(i = 0; i < (N-incial)*2; i++)
            printf(" ");

        for(i = 1; i <= incial; i++)
            printf("%d ", i);
        
        for(i -= 2; i > 0; i--)
            printf("%d ", i);
    
        for(i = 0; i < (N-incial)*2; i++)
            printf(" ");
        printf("\n");
        incial++;
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
  "source_sha256": "e6dca25786dee8a0c8bf94aafe243897869c3af745e344f3659521a3e5f955a9",
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
      "output": "    1     \n  1 2 1   \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1       \n    1 2 1     \n  1 2 3 2 1   \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1               \n            1 2 1             \n          1 2 3 2 1           \n        1 2 3 4 3 2 1         \n      1 2 3 4 5 4 3 2 1       \n    1 2 3 4 5 6 5 4 3 2 1     \n  1 2 3 4 5 6 7 6 5 4 3 2 1   \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
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
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "medium"
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


## sample_033 — train

```c

#include <stdio.h>

int main(){

    int N;
    void piramide();

    scanf("%d", &N);
    piramide(N);

    return 0;

}

void piramide(int N){

    int i, incial = 1;
    
    while (incial <= N)
    {
    
        for(i = 0; i < (N-incial)*2; i++)
            printf(" ");

        for(i = 1; i <= incial; i++){
            printf("%d", i);
            if (incial != 1) 
                printf(" ");
        }
            
        
        for(i -= 2; i > 0; i--){
            printf("%d", i);
            if (i != 1)
                printf(" ");
        }
        
        for(i = 0; i < (N-incial)*2; i++)
            printf(" ");
        printf("\n");
        incial++;
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
  "source_sha256": "2d3088dbc329bafff7c222644d86aa146bbbf148745b140bab1925a0adec59a8",
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
      "output": "    1    \n  1 2 1  \n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1      \n    1 2 1    \n  1 2 3 2 1  \n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1              \n            1 2 1            \n          1 2 3 2 1          \n        1 2 3 4 3 2 1        \n      1 2 3 4 5 4 3 2 1      \n    1 2 3 4 5 6 5 4 3 2 1    \n  1 2 3 4 5 6 7 6 5 4 3 2 1  \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
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
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "medium"
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


## sample_034 — train

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
    spaces(n, p);
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
  "sample_id": "sample_034",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "9143e15a7ca4afdbfef6bef213ec8bc9cfd7feeb91a97d4af99d25ebc043ddaa",
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
      "output": "    1     \n  1 2 1  \n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1       \n    1 2 1    \n  1 2 3 2 1  \n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1               \n            1 2 1            \n          1 2 3 2 1          \n        1 2 3 4 3 2 1        \n      1 2 3 4 5 4 3 2 1      \n    1 2 3 4 5 6 5 4 3 2 1    \n  1 2 3 4 5 6 7 6 5 4 3 2 1  \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
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
    "stdout:ex02_1:edit_band": "medium",
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


## sample_035 — validation

```c


#include <stdio.h>

void piramide(int n) {
    int i, j, s;
    for (i = 0; i < n; i++) {
        for (s = 2*i; s < 2*(n-1); s++){
            putchar(' ');
        }
        for (j = (n+1); j > (n-i); j--) {
            printf("%d", (n+2-j));
            if ((j > (n-i+1)) | (i != 0)) 
                putchar(' ');
        }
        for (j = (n-i+1); j < (n+1); j++) {
            printf("%d", (n+1-j));
            if (j < (n))
                putchar(' ');
        }
        for (s = 2*i; s < 2*(n-1); s++){
            putchar(' ');
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
  "sample_id": "sample_035",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "566b88cd221b3318d44ea9adaa0aac0ffc30c3b8e28cc7bbd7e1c9170d78631f",
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
      "output": "    1    \n  1 2 1  \n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1      \n    1 2 1    \n  1 2 3 2 1  \n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1              \n            1 2 1            \n          1 2 3 2 1          \n        1 2 3 4 3 2 1        \n      1 2 3 4 5 4 3 2 1      \n    1 2 3 4 5 6 5 4 3 2 1    \n  1 2 3 4 5 6 7 6 5 4 3 2 1  \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
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
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
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

void piramide(int N){
    int i, j;

    for(i = 0; i <= N; i++){
        for(j = 1; j <= 2 * (N- i); j++){
            printf(" ");
        }

        for(j = 1; j <= i; j++){
            printf("%d ", j);
        }

        for(j = i -1; j >= 1; j--){
            printf("%d ", j);
        }
        printf("\n");
    }
}



int main(){

    int N;
    scanf("%d", &N);
    if(N < 2){
        printf("O número tem que ser superior a 2\n");
        scanf("%d", &N);
    }
    piramide(N);
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
  "source_sha256": "5411d1ce354e8da484c8c861bbdf59f14f01bca559ec914149af784733acb422",
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
      "output": "      \n    1 \n  1 2 1 \n1 2 3 2 1 \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "        \n      1 \n    1 2 1 \n  1 2 3 2 1 \n1 2 3 4 3 2 1 \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "                \n              1 \n            1 2 1 \n          1 2 3 2 1 \n        1 2 3 4 3 2 1 \n      1 2 3 4 5 4 3 2 1 \n    1 2 3 4 5 6 5 4 3 2 1 \n  1 2 3 4 5 6 7 6 5 4 3 2 1 \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 \n"
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
    "stdout:ex02_1:edit_band": "medium",
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


## sample_037 — validation

```c

#include <stdio.h>

void piramide(int N){
    int i, j;

    for(i = 0; i <= N; i++){
        for(j = 1; j <= 2 * (N- i); j++){
            printf(" ");
        }

        for(j = 1; j <= i; j++){
            printf("%d ", j);
        }

        for(j = i -1; j >= 1; j--){
            if(j == 1){
                printf("%d", j);
            }
            else{
                printf("%d ", j);
            }
        }
        printf("\n");
    }
}



int main(){

    int N;
    scanf("%d", &N);
    if(N < 2){
        printf("O número tem que ser superior a 2\n");
        scanf("%d", &N);
    }
    piramide(N);
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
  "source_sha256": "381d8afee000e70711fd71596ee1b45e496f12d59a810f60e11778b27b7d3d42",
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
      "output": "      \n    1 \n  1 2 1\n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "        \n      1 \n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "                \n              1 \n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
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
    "stdout:ex02_1:edit_band": "medium",
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


## sample_038 — train

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
            printf("  ");
            ++e;
        }
        while(N-i <= e && e <= N) {
            printf("%2d", num);
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
            (i == N-i) ? printf("%2d\n", num) : printf("%2d", num);
            ++e;
        }
        while(N+i < e && e < 2*N-1) {
            printf("  ");
            ++e;
        }
        if(e == 2*N-1)
            printf(" \n");
        e = 1;
        num = 1;
        ++i;
    }
}
```

```json
{
  "sample_id": "sample_038",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "96f6f67ee0002ad2cd9e02f0ede8c095cdf0bce417896b06eac386017f7230b7",
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
      "output": "     1   \n   1 2 1 \n 1 2 3 2 1"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1     \n     1 2 1   \n   1 2 3 2 1\n \n 1 2 3 4 3 2 1"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1             \n             1 2 1           \n           1 2 3 2 1         \n         1 2 3 4 3 2 1       \n       1 2 3 4 5 4 3 2 1\n     \n     1 2 3 4 5 6 5 4 3 2 1   \n   1 2 3 4 5 6 7 6 5 4 3 2 1 \n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1"
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
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "medium"
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


## sample_039 — train

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
            printf("  ");
            ++e;
        }
        while(N-i <= e && e <= N) {
            printf("%2d", num);
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
            (i == N-i) ? printf("%2d\n", num) : printf("%2d", num);
            ++e;
        }
        while(N+i < e && e < 2*N-1) {
            printf("  ");
            ++e;
        }
        if(e == 2*N-1)
            printf(" \n");
        e = 1;
        num = 1;
        ++i;
    }
}
```

```json
{
  "sample_id": "sample_039",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "96f6f67ee0002ad2cd9e02f0ede8c095cdf0bce417896b06eac386017f7230b7",
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
      "output": "     1   \n   1 2 1 \n 1 2 3 2 1"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "       1     \n     1 2 1   \n   1 2 3 2 1\n \n 1 2 3 4 3 2 1"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "               1             \n             1 2 1           \n           1 2 3 2 1         \n         1 2 3 4 3 2 1       \n       1 2 3 4 5 4 3 2 1\n     \n     1 2 3 4 5 6 5 4 3 2 1   \n   1 2 3 4 5 6 7 6 5 4 3 2 1 \n 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1"
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
    "stdout:ex02_0:edit_band": "medium",
    "stdout:ex02_1:relation": "whitespace",
    "stdout:ex02_1:edit_band": "medium",
    "stdout:ex02_2:relation": "whitespace",
    "stdout:ex02_2:edit_band": "medium"
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


## sample_040 — train

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
        for(j=n-i;j>=0;j--){
            printf("  ");
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
  "sample_id": "sample_040",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "8687b7034793910109cff46707e95544e83caf7e3e34d0d8590cfafca0a269c2",
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
      "output": "    1       \n  1 2 1     \n1 2 3 2 1   \n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1         \n    1 2 1       \n  1 2 3 2 1     \n1 2 3 4 3 2 1   \n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1                 \n            1 2 1               \n          1 2 3 2 1             \n        1 2 3 4 3 2 1           \n      1 2 3 4 5 4 3 2 1         \n    1 2 3 4 5 6 5 4 3 2 1       \n  1 2 3 4 5 6 7 6 5 4 3 2 1     \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1   \n"
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
    "stdout:ex02_1:edit_band": "medium",
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


## sample_041 — train

```c


#include <stdio.h>


void piramide(int N){

    int i, j;

    for (i = -N; i < 0; i++){

        for (j = 2; j <= N; j++){

            if (i + j > 0){
                printf("%d ", i + j);
            }
            else{
                printf("  ");
            }
        }

        for (j = j; j > 2; j--){

            if (i + j > 0){
                printf("%d ", i + j);
            }
            else{
                printf("  ");
            }
        }

        if (i + j > 0){
            printf("%d", i + j);
        }

        else{
            printf(" ");
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
  "sample_id": "sample_041",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "21a06fcf31e79bb5ec7244f635719292b5d7e07ff18ff22dc6afe5c3ff6b7e78",
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
      "output": "    1    \n  1 2 1  \n1 2 3 2 1\n"
    },
    {
      "test_id": "ex02_1",
      "input": "4",
      "expected": "      1\n    1 2 1\n  1 2 3 2 1\n1 2 3 4 3 2 1\n",
      "output": "      1      \n    1 2 1    \n  1 2 3 2 1  \n1 2 3 4 3 2 1\n"
    },
    {
      "test_id": "ex02_2",
      "input": "8",
      "expected": "              1\n            1 2 1\n          1 2 3 2 1\n        1 2 3 4 3 2 1\n      1 2 3 4 5 4 3 2 1\n    1 2 3 4 5 6 5 4 3 2 1\n  1 2 3 4 5 6 7 6 5 4 3 2 1\n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n",
      "output": "              1              \n            1 2 1            \n          1 2 3 2 1          \n        1 2 3 4 3 2 1        \n      1 2 3 4 5 4 3 2 1      \n    1 2 3 4 5 6 5 4 3 2 1    \n  1 2 3 4 5 6 7 6 5 4 3 2 1  \n1 2 3 4 5 6 7 8 7 6 5 4 3 2 1\n"
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
    "stdout:ex02_1:edit_band": "medium",
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
  "members/sample_041/tests/ex02_2"
]
```
