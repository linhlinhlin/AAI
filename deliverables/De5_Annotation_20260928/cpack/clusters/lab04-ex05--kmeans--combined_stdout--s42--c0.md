# lab04-ex05--kmeans--combined_stdout--s42--c0

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 29; phân vùng: {'train': 21, 'validation': 8}.


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
    "test_id": "ex05_0",
    "n_cluster": 29,
    "n_observed": 29,
    "n_failed": 29,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 29
    }
  },
  {
    "test_id": "ex05_1",
    "n_cluster": 29,
    "n_observed": 29,
    "n_failed": 29,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 29
    }
  },
  {
    "test_id": "ex05_3",
    "n_cluster": 29,
    "n_observed": 29,
    "n_failed": 29,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 29
    }
  },
  {
    "test_id": "ex05_2",
    "n_cluster": 29,
    "n_observed": 29,
    "n_failed": 24,
    "n_not_run": 0,
    "failure_rate_observed": 0.8275862068965517,
    "failure_rate_cluster": 0.8275862068965517,
    "outcome_counts": {
      "fail": 24,
      "pass": 5
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex05_1:relation",
    "value": "different",
    "n": 26,
    "n_cluster": 29,
    "rate": 0.896551724137931,
    "cohort_rate": 0.37142857142857144,
    "difference_from_cohort": 0.5251231527093596
  },
  {
    "feature": "stdout:ex05_3:relation",
    "value": "different",
    "n": 26,
    "n_cluster": 29,
    "rate": 0.896551724137931,
    "cohort_rate": 0.37142857142857144,
    "difference_from_cohort": 0.5251231527093596
  },
  {
    "feature": "stdout:ex05_0:relation",
    "value": "different",
    "n": 27,
    "n_cluster": 29,
    "rate": 0.9310344827586207,
    "cohort_rate": 0.4142857142857143,
    "difference_from_cohort": 0.5167487684729064
  },
  {
    "feature": "stdout:ex05_2:relation",
    "value": "different",
    "n": 21,
    "n_cluster": 29,
    "rate": 0.7241379310344828,
    "cohort_rate": 0.32857142857142857,
    "difference_from_cohort": 0.3955665024630542
  },
  {
    "feature": "stdout:ex05_0:edit_band",
    "value": "large",
    "n": 20,
    "n_cluster": 29,
    "rate": 0.6896551724137931,
    "cohort_rate": 0.3,
    "difference_from_cohort": 0.38965517241379316
  },
  {
    "feature": "stdout:ex05_1:edit_band",
    "value": "large",
    "n": 19,
    "n_cluster": 29,
    "rate": 0.6551724137931034,
    "cohort_rate": 0.2714285714285714,
    "difference_from_cohort": 0.383743842364532
  },
  {
    "feature": "stdout:ex05_3:edit_band",
    "value": "large",
    "n": 19,
    "n_cluster": 29,
    "rate": 0.6551724137931034,
    "cohort_rate": 0.2714285714285714,
    "difference_from_cohort": 0.383743842364532
  },
  {
    "feature": "stdout:ex05_2:edit_band",
    "value": "large",
    "n": 14,
    "n_cluster": 29,
    "rate": 0.4827586206896552,
    "cohort_rate": 0.2,
    "difference_from_cohort": 0.2827586206896552
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 22,
    "n_cluster": 29,
    "rate": 0.7586206896551724,
    "cohort_rate": 0.5,
    "difference_from_cohort": 0.2586206896551724
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 20,
    "n_cluster": 29,
    "rate": 0.6896551724137931,
    "cohort_rate": 0.45714285714285713,
    "difference_from_cohort": 0.23251231527093602
  },
  {
    "feature": "test:ex05_2",
    "value": "fail",
    "n": 24,
    "n_cluster": 29,
    "rate": 0.8275862068965517,
    "cohort_rate": 0.6571428571428571,
    "difference_from_cohort": 0.17044334975369457
  },
  {
    "feature": "stdout:ex05_1:edit_band",
    "value": "medium",
    "n": 8,
    "n_cluster": 29,
    "rate": 0.27586206896551724,
    "cohort_rate": 0.11428571428571428,
    "difference_from_cohort": 0.16157635467980297
  },
  {
    "feature": "stdout:ex05_3:edit_band",
    "value": "medium",
    "n": 8,
    "n_cluster": 29,
    "rate": 0.27586206896551724,
    "cohort_rate": 0.11428571428571428,
    "difference_from_cohort": 0.16157635467980297
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 28,
    "n_cluster": 29,
    "rate": 0.9655172413793104,
    "cohort_rate": 0.8142857142857143,
    "difference_from_cohort": 0.1512315270935961
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 8,
    "n_cluster": 29,
    "rate": 0.27586206896551724,
    "cohort_rate": 0.12857142857142856,
    "difference_from_cohort": 0.14729064039408868
  },
  {
    "feature": "ast:c_subscript",
    "value": "1",
    "n": 28,
    "n_cluster": 29,
    "rate": 0.9655172413793104,
    "cohort_rate": 0.8285714285714286,
    "difference_from_cohort": 0.13694581280788176
  },
  {
    "feature": "stdout:ex05_2:edit_band",
    "value": "medium",
    "n": 7,
    "n_cluster": 29,
    "rate": 0.2413793103448276,
    "cohort_rate": 0.12857142857142856,
    "difference_from_cohort": 0.11280788177339904
  },
  {
    "feature": "test:ex05_1",
    "value": "fail",
    "n": 29,
    "n_cluster": 29,
    "rate": 1.0,
    "cohort_rate": 0.9142857142857143,
    "difference_from_cohort": 0.08571428571428574
  },
  {
    "feature": "test:ex05_3",
    "value": "fail",
    "n": 29,
    "n_cluster": 29,
    "rate": 1.0,
    "cohort_rate": 0.9142857142857143,
    "difference_from_cohort": 0.08571428571428574
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 3,
    "n_cluster": 29,
    "rate": 0.10344827586206896,
    "cohort_rate": 0.04285714285714286,
    "difference_from_cohort": 0.06059113300492611
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 22,
    "n_cluster": 29,
    "rate": 0.7586206896551724,
    "cohort_rate": 0.5,
    "difference_from_cohort": 0.2586206896551724
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 20,
    "n_cluster": 29,
    "rate": 0.6896551724137931,
    "cohort_rate": 0.45714285714285713,
    "difference_from_cohort": 0.23251231527093602
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 28,
    "n_cluster": 29,
    "rate": 0.9655172413793104,
    "cohort_rate": 0.8142857142857143,
    "difference_from_cohort": 0.1512315270935961
  },
  {
    "feature": "ast:c_subscript",
    "value": "1",
    "n": 28,
    "n_cluster": 29,
    "rate": 0.9655172413793104,
    "cohort_rate": 0.8285714285714286,
    "difference_from_cohort": 0.13694581280788176
  },
  {
    "feature": "ast:c_array_parameter",
    "value": "1",
    "n": 27,
    "n_cluster": 29,
    "rate": 0.9310344827586207,
    "cohort_rate": 0.9,
    "difference_from_cohort": 0.03103448275862064
  },
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 29,
    "n_cluster": 29,
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
    "rule_id": 2,
    "if": [
      "NOT (stdout:ex05_0:relation=whitespace)",
      "NOT (stdout:ex05_3:edit_band=__unknown__)"
    ],
    "then_cluster": 0,
    "train_support": 21,
    "train_precision": 1.0,
    "holdout_support": 8,
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
  "reasoning": "Có 29 bài trong cụm. Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
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

sample_012, sample_002, sample_029, sample_011

## sample_002 — train — đại diện

```c
#include <stdio.h>
#include <string.h>

#define MAX 80

int leLinha(char s[]){
    char c;
    int num_char = 0;

    scanf("%c", &c);
    while ((c != '\n') && (c != EOF)){
        s[num_char] = c;
        num_char++;

        scanf("%c", &c);
        if (num_char >= 80) {
            break;
        }
    }

    s[num_char] = '\0';

    return num_char;
}

int main(){
    char s[MAX];
    int num_char, contador;

    num_char = leLinha(s);
    
    for (contador = 0; contador < num_char; contador++) {
        printf("%c", s[contador]);
    }
    printf("\n");

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
  "source_sha256": "a58071b5c812bc0bc456c65577df964aa50fa676e1984f5eef40ad04c96c1cc3",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "pass",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "ola adeussssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss\n"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "abccbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "abdddbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "pass",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "large",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "large",
    "stdout:ex05_2:relation": "__unknown__",
    "stdout:ex05_2:edit_band": "__unknown__",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "pass",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
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


## sample_011 — train — đại diện

```c

#include <stdio.h>
#include <string.h>

#define BUFFER 100

int leLinha(char s[BUFFER]);

int main() {

    char string[BUFFER];
    int n = leLinha(string);
    int i;
    for (i = 0; i <= n; i++) {
        printf("%c", string[i]);
    }

    return 0;

}

int leLinha(char s[BUFFER]) {

    char c;
    int j = 0;

    while ((c = getchar()) != EOF) {

        if (c == '\n') {
            s[j] = c;
            j++;
            break;
        }
        s[j] = c;
        j++; 
    }

    return j;
}
```

```json
{
  "sample_id": "sample_011",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "e02db4ab4b0af9bdf0afc5d518f6632321592fff8f99fc584424bf286787a0c3",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "ola adeus\u0000"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "abccba\u0000"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "Hello world!\n\u0000"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "abdddba\u0000"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "small",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "medium",
    "stdout:ex05_2:relation": "different",
    "stdout:ex05_2:edit_band": "small",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
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


## sample_012 — train — đại diện

```c

#include <stdio.h>
#include <string.h>
#define MAX_C 100

int leLinha(char s[]){
    int c, ind;
    c = getchar();
    for (ind = 0;ind < MAX_C && (c != EOF && c != '\n'); ind++)
        s[ind] = c;
    s[ind] = '\0';
    return ind;
}

void copiar(char s[],char s_destino[]){
    int i;
    for(i= 0;s[i] != '\0';i++){
        s_destino[i] = s[i];
    }
    s_destino[i] = '\0';
}

int main(){
    char s[MAX_C],s_destino[MAX_C];
    leLinha(s);
    copiar(s,s_destino);
    printf("%s\n",s_destino);
    return 0;
}
```

```json
{
  "sample_id": "sample_012",
  "partition": "train",
  "representative": true,
  "is_train_medoid": true,
  "raw_code_truncated": false,
  "source_sha256": "58d95499e1d0add9932891e77ba83bb1a0b5f6b7efa8a242f411a8c5a13b6336",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\n"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "large",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "large",
    "stdout:ex05_2:relation": "different",
    "stdout:ex05_2:edit_band": "large",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_029 — train — đại diện

```c

#include <stdio.h>

int main() {

    return 0;
}
```

```json
{
  "sample_id": "sample_029",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "a394a64700d59d01c4cd4546d63a88bbf7e268632b1649e6b84780a7d19b18f6",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": ""
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": ""
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": ""
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "0",
    "ast:c_update": "0",
    "stdout:ex05_0:relation": "empty",
    "stdout:ex05_0:edit_band": "large",
    "stdout:ex05_1:relation": "empty",
    "stdout:ex05_1:edit_band": "large",
    "stdout:ex05_2:relation": "empty",
    "stdout:ex05_2:edit_band": "large",
    "stdout:ex05_3:relation": "empty",
    "stdout:ex05_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
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


## sample_001 — train

```c
#include <stdio.h>
#include <string.h>

#define MAX 80

int leLinha(char s[]){
    char c;
    int num_char = 0;

    scanf("%c", &c);
    while ((c != '\n') && (c != EOF)){
        s[num_char] = c;
        num_char++;

        scanf("%c", &c);
        if (num_char >= 80) {
            break;
        }
    }

    s[num_char] = '\0';

    return num_char;
}

int main(){
    char s[MAX];
    int num_char, contador;

    num_char = leLinha(s);
    
    for (contador = 0; contador < num_char; contador++) {
        printf("%c", s[contador]);
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
  "source_sha256": "f4212d56b6b21e192ad2a1a10d149fd031d0229a17da8a5bee1f748b09fae2a5",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "ola adeussssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "abccbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "Hello world!"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "abdddbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "large",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "large",
    "stdout:ex05_2:relation": "whitespace",
    "stdout:ex05_2:edit_band": "small",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
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


## sample_003 — train

```c
#include <stdio.h>
#define MAX 80

int lelinha(char s[])
{
    int i,tam;
    char c;
    for(i=0;i<(MAX-1) && (c=getchar())!= EOF && c !='\n';i++)
    {
        tam++;
        s[i]=c;
    }
    return tam;
}

int main()
{
    int tam;
    char s[MAX];
    tam = lelinha(s);
    printf("%s\n",s);
    printf("%d\n",tam);
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
  "source_sha256": "f7890000271f19fed2af1e4255c85d1301a13c2145c8c4903885bb1d7901a565",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "ola adeus\n9\n"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "abccba\n6\n"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "Hello world!\n12\n"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "abdddba\n7\n"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "small",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "medium",
    "stdout:ex05_2:relation": "different",
    "stdout:ex05_2:edit_band": "medium",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_004 — validation

```c
#include <stdio.h>
#include <string.h>
#define MAX 80

int leLinha(char s[]);

int main()
{
    char s[MAX];
    int i, size;

    size = leLinha(s);

    for (i = 0; i < size; ++i)
        putchar(s[i]);

    putchar('\n');
    
    return 0;
}

int leLinha(char s[])
{
    int i = 0;
    char c;
    while ((c = getchar()) != EOF && c != '\n' && i < MAX - 1)
    {
        printf("%d, %s", i, &c);
        s[i++] = c;
        s[i] = '\0';
    }
    return i;
}
```

```json
{
  "sample_id": "sample_004",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "5a8108942c11f9cd20b091717660d7ded3e2c166c764b47fc46fd295792b4ed9",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "0, o1, l\u00012, a\u00023,  \u00034, a\u00045, d\u00056, e\u00067, u\u00078, s\bola adeus\n"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "0, a1, b\u00012, c\u00023, c\u00034, b\u00045, a\u0005abccba\n"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "0, H1, e\u00012, l\u00023, l\u00034, o\u00045,  \u00056, w\u00067, o\u00078, r\b9, l\t10, d\n11, !\u000bHello world!\n"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "0, a1, b\u00012, d\u00023, d\u00034, d\u00045, b\u00056, a\u0006abdddba\n"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "large",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "large",
    "stdout:ex05_2:relation": "different",
    "stdout:ex05_2:edit_band": "large",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
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

#define VECMAX 100

void grafico_h(int dim){
	int i, i2, item;
	int tab[VECMAX];

	for(i = 0; i < dim; i++){
		scanf("%d", &item);
		tab[i] = item;
	}

	for(i = 0; i < dim; i++){
		for (i2 = 0; i2 < tab[i]; i2++){
			printf("*");
		}
		printf("\n");
	}
}


int main(){
	int n;
	scanf("%d", &n);
	grafico_h(n);
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
  "source_sha256": "466d2c212ced31320858f785ee5ead7b07801f20a1e8c62da6951429840912eb",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": ""
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": ""
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": ""
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": ""
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "empty",
    "stdout:ex05_0:edit_band": "large",
    "stdout:ex05_1:relation": "empty",
    "stdout:ex05_1:edit_band": "large",
    "stdout:ex05_2:relation": "empty",
    "stdout:ex05_2:edit_band": "large",
    "stdout:ex05_3:relation": "empty",
    "stdout:ex05_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
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


## sample_006 — train

```c
#include <stdio.h>
#include <string.h>
#define DIM 80
#define NOVA 80

int lelinha(char s[]);



int main(){
	int i,c,contador;
	char s[DIM];
    c = getchar();
    for (i = 0; i < DIM-1 && c != EOF && c != '\n'; i++) {
        s[i] = c;
        c = getchar();}
    s[i] = '\0';
    printf("%s\n", s);
    contador = lelinha(s);
    printf("%d",contador);

    

   

    
    return 0;
}

int lelinha(char palavra[]){
int i,cont;

for (i=0;palavra[i]!= '\0';++i)
    cont = cont + 1;
return cont;
}

```

```json
{
  "sample_id": "sample_006",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "4e4867b730ac357842a64ff7efd5add3fa85381cb2c6ecdb8e2aa3a3386026d7",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "ola adeus\n9"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "abccba\n6"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "Hello world!\n12"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "abdddba\n7"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "small",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "small",
    "stdout:ex05_2:relation": "different",
    "stdout:ex05_2:edit_band": "small",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_007 — validation

```c
#include <stdio.h>

#define MAX 80

int leLinha(char s[]){

	int i = 0;
	char c;

	while((c = getchar()) != '\n' && c != EOF){

		s[i] = c;

		i++;
	}

	s[i] = '\0';

	return i;
}

int main(){

	char s[MAX];

	printf("%d\n%s\n", leLinha(s), s);

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
  "source_sha256": "1a4ebeed63e31972050d4894a21334ff81e8da4db15c09b972033f91de9a0ea0",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "9\nola adeus\n"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "6\nabccba\n"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "12\nHello world!\n"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "7\nabdddba\n"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "small",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "medium",
    "stdout:ex05_2:relation": "different",
    "stdout:ex05_2:edit_band": "medium",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_008 — validation

```c
#include <stdio.h>

#define MAX 80

int leLinha(char s[MAX]){
    int i = 0;
    while(s[i] != '\0')
        i++;
    return i;
}


int main(){
    int c, i;
    char s[MAX];

    for(i = 0; i < MAX - 1 && (c = getchar()) != EOF && c != '\n'; i++)
        s[i] = c;
    s[i] = '\0';
    printf("%s\n", s);
    printf("%d\n", leLinha(s));
    return 0;
}
```

```json
{
  "sample_id": "sample_008",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "ac91b962545beb92e2a8f0dc32261f6efee61b02b41561363a581686d6bee831",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "ola adeus\n9\n"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "abccba\n6\n"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "Hello world!\n12\n"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "abdddba\n7\n"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "small",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "medium",
    "stdout:ex05_2:relation": "different",
    "stdout:ex05_2:edit_band": "medium",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_009 — train

```c
#include <stdio.h>

#define MAX 80

int leLinha(char s[])
{
  int i, c;

  for (i = 0; i < MAX - 1 && (c = getchar()) != EOF && c != '\n'; i++)
  {
    s[i] = c;
  }

  s[i] = '\0';

  return i;
}

int main()
{
  int characters;
  char word[MAX];

  characters = leLinha(word);

  printf("%s\n", word);
  printf("%d\n", characters);

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
  "source_sha256": "b43fdb8e06797374f23543c75f7d4f49b0c9f96f6d0f0bf9c00e709bdea5bac5",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "ola adeus\n9\n"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "abccba\n6\n"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "Hello world!\n12\n"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "abdddba\n7\n"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "small",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "medium",
    "stdout:ex05_2:relation": "different",
    "stdout:ex05_2:edit_band": "medium",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_010 — validation

```c
#include <stdio.h>
 
int leLinha(char s[]);

#define DIM 80

int main() {

    char s[DIM];

    printf("%d\n", leLinha(s));
    printf("%s\n", s);

    return 0;
    }

int leLinha(char s[]) {

    int i = 0;
    char c;

    while ((c = getchar()) != '\n' && (c != EOF)) {
        s[i] = c;
        i++;
    }
    s[i] = '\0';
    return i;
}
```

```json
{
  "sample_id": "sample_010",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "141009b946a3ff3c67c53f216e85142145e99633d491e8d2767cf82df3cee911",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "9\nola adeus\n"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "6\nabccba\n"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "12\nHello world!\n"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "7\nabdddba\n"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "small",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "medium",
    "stdout:ex05_2:relation": "different",
    "stdout:ex05_2:edit_band": "medium",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_013 — train

```c

#include <stdio.h>
#include <string.h>
#define MAX_C 100

int leLinha(char s[]){
    int c, ind;
    c = getchar();
    for (ind = 0;ind < MAX_C && (c != EOF || c != '\n'); ind++)
        s[ind] = c;
    s[ind] = '\0';
    return ind;
}

int main(){
    char s[MAX_C];
    leLinha(s);
    printf("%s\n",s);
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
  "source_sha256": "0e8060efc45b853359c10872ca1f7d3453b023a0872dad20d7cba481e240bdb1",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\n"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "large",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "large",
    "stdout:ex05_2:relation": "different",
    "stdout:ex05_2:edit_band": "large",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_014 — train

```c

#include <stdio.h>
#include <string.h>
#define MAX_C 100

int leLinha(char s[]){
    int c, ind;
    c = getchar();
    for (ind = 0;ind < MAX_C && (c != EOF && c != '\n'); ind++)
        s[ind] = c;
    s[ind] = '\0';
    return ind;
}

int main(){
    int i;
    char s[MAX_C];
    char s_destino[MAX_C];
    leLinha(s);
    for(i = 0; s[i] != '\0';i++){
        s_destino[i] = s[i];
    }
    s_destino[i] = '\0';
    printf("%s\n",s_destino);
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
  "source_sha256": "b620163329df63d5bbf91df18cccd1c73d203b75584f1ff9d368386398194068",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\n"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "large",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "large",
    "stdout:ex05_2:relation": "different",
    "stdout:ex05_2:edit_band": "large",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_015 — train

```c

#include <stdio.h>
#include <string.h>
#define MAX_C 100


int leLinha(char s[]){
    int c, ind;
    c = getchar();
    for (ind = 0;ind < MAX_C && (c != EOF && c != '\n'); ind++)
        s[ind] = c;
    s[ind] = '\0';
    return ind;
}

int main(){
    char s[MAX_C],s_destino[MAX_C];
    int comprimento,i;
    comprimento = leLinha(s);
    for(i = 0; i < comprimento; i++){
        s_destino[i] = s[i];
    }
    s_destino[i] = '\0';
    printf("%s\n",s_destino);
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
  "source_sha256": "663c8b91870dc6cf6b6770fe21cb825cf1e69c1da627276a268dcf3584524360",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\n"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "large",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "large",
    "stdout:ex05_2:relation": "different",
    "stdout:ex05_2:edit_band": "large",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_016 — train

```c

#include <stdio.h>
#include <string.h>
#define MAX_C 100

int leLinha(char s[]){
    int c, ind;
    c = getchar();
    for (ind = 0;ind < MAX_C && (c != EOF && c != '\n'); ind++)
        s[ind] = c;
    s[ind] = '\0';
    return ind;
}

int main(){
    char s[MAX_C];
    leLinha(s);
    printf("%s\n",s);
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
  "source_sha256": "551fb6fa767273853a7b78588352175bb9c53ef08e92d7b8049e8455f0c45a90",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\n"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "large",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "large",
    "stdout:ex05_2:relation": "different",
    "stdout:ex05_2:edit_band": "large",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_017 — train

```c

#include <stdio.h>
#include <string.h>
#define MAX_C 100

int leLinha(char s[]){
    int c, ind;
    c = getchar();
    for (ind = 0;ind < MAX_C && (c != EOF && c != '\n'); ind++)
        s[ind] = c;
    s[ind] = '\0';
    return ind;
}

int main(){
    char s[MAX_C];
    leLinha(s);
    printf("%s\n",s);
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
  "source_sha256": "551fb6fa767273853a7b78588352175bb9c53ef08e92d7b8049e8455f0c45a90",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\n"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "large",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "large",
    "stdout:ex05_2:relation": "different",
    "stdout:ex05_2:edit_band": "large",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_018 — train

```c

#include <stdio.h>
#include <string.h>
#define MAX_C 100

int leLinha(char s[]){
    int c, ind;
    c = getchar();
    for (ind = 0;ind < MAX_C && (c != EOF && c != '\n'); ind++)
        s[ind] = c;
    s[ind] = '\0';
    return ind;
}

int main(){
    char s[MAX_C],s_destino[MAX_C];
    int comprimento,i;
    comprimento = leLinha(s);
    for(i = 0; i < comprimento; i++){
        s_destino[i] = s[i];
    }
    s_destino[i] = '\0';
    printf("%s\n",s_destino);
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
  "source_sha256": "afb76b3dc07c7122d86f8afdabc7e17b064e31149ef4a46b33b598ae175ce013",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo\n"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH\n"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\n"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "large",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "large",
    "stdout:ex05_2:relation": "different",
    "stdout:ex05_2:edit_band": "large",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_019 — train

```c


#include <stdio.h>

#define MAX 80

int leLinha (char s[]) {

    int c, i = 0;

    while ((c = getchar() != EOF && c != '\n')) {
        s[i] = c;
        i++;
    }

    s[i] = '\0';
    return i;
}

int main () {

    char s[MAX];
    int i, j;

    i = leLinha(s);

    for (j = 0; j < i; j++)
        putchar(s[j]);
    
    s[j] = '\0';
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
  "source_sha256": "64246925d925f4afd7cea9e6413cbc12cb1b9869b4d23d5ee7def00881bba0a1",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "\u0001\u0001\u0001\u0001\u0001\u0001"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "\u0001\u0001\u0001\u0001\u0001\u0001\u0001"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "large",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "large",
    "stdout:ex05_2:relation": "different",
    "stdout:ex05_2:edit_band": "large",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_020 — train

```c

#include<stdio.h>

#define MAX 100

int leLinha(char s[])
{
    int i=0, c;

    for(c = getchar(); c != '\n' && c != EOF; c = getchar())
        s[i++] = c;

    s[i] = '\0';
    return i;    
}

int main()
{
    char linha[MAX];
    int tamanho = leLinha(linha);

    printf("%s\n", linha);
    printf("%d\n", tamanho);

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
  "source_sha256": "dd971a02941afcaa056f99c67a1be663e5b262a6243cec4d895882ef08485e8e",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "ola adeus\n9\n"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "abccba\n6\n"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "Hello world!\n12\n"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "abdddba\n7\n"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "small",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "medium",
    "stdout:ex05_2:relation": "different",
    "stdout:ex05_2:edit_band": "medium",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_021 — train

```c

#include <stdio.h>
#include <string.h>

#define MAX 80

int leLinha(char s[]) {
  int charLido = 0;

  while((s[charLido] = getchar()) != EOF && s[charLido] != '\n' && s[charLido] != ' ') {charLido++;}
  
  s[charLido] = '\0';
  return charLido + 1;
}

int main() {
  char s[MAX];

  leLinha(s);

  printf("%s", s);

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
  "source_sha256": "4e9aaffca9296c8d8c385c7856ada977e4d5fb1c70ac0d2b906aeb51c6d9e825",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "ola"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "abccba"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "Hello"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "abdddba"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "large",
    "stdout:ex05_1:relation": "whitespace",
    "stdout:ex05_1:edit_band": "small",
    "stdout:ex05_2:relation": "different",
    "stdout:ex05_2:edit_band": "large",
    "stdout:ex05_3:relation": "whitespace",
    "stdout:ex05_3:edit_band": "small"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_022 — train

```c

#include <stdio.h>
#define MAX 80

int leLinha(char seq[MAX]) {
    int i = 0, caracteres = 0;
    char c;

    while ((c = getchar()) != '\n' && c != EOF && i < MAX - 1) {
        seq[i++] = c;
        caracteres++;
    }
    seq[i] = '\0';

    return caracteres;
}

int main() {
    char seq[MAX];
    int numCaracteres;

    numCaracteres = leLinha(seq);

    printf("%s\n", seq);
    printf("%d\n", numCaracteres);
    
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
  "source_sha256": "5d91488f9a217f0d5c384160a6a092e2f8ce73e7a2c51a0138a14f0b8e34e099",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "ola adeus\n9\n"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "abccba\n6\n"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "Hello world!\n12\n"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "abdddba\n7\n"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "small",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "medium",
    "stdout:ex05_2:relation": "different",
    "stdout:ex05_2:edit_band": "medium",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_023 — train

```c


#include <stdio.h>
#include <string.h>
#define MAX 80

int leLinha(char s[]){
    int DIM=strlen(s);
    int c, i;
    c = getchar();
    for (i = 0; i < DIM-1 && c != EOF && c != '\n'; i++) {
        s[i] = c;
        c = getchar();
    }

    s[i] = '\0';
    printf("%s\n", s);
    
    return 0;        
}

int main(){
    char s[MAX];
    leLinha(s);
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
  "source_sha256": "ed4dbb558b80c6835eef9ca7b5391351d13211e42c74d0db3781cd16226d94b2",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "\n"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "\n"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "\n"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "\n"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "large",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "large",
    "stdout:ex05_2:relation": "different",
    "stdout:ex05_2:edit_band": "large",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_024 — validation

```c

#include <stdio.h>
#define STRMAX 80
int leLinha(char s[]){
    char letra;
    int cont = 1;
    scanf("%c",&letra);
    s[0] = letra;
    while (letra != '\n' && letra != EOF && cont<STRMAX-1){
        scanf("%c",&letra);
        s[cont]= letra;
        cont++;
    }
    return cont;
}
int main(){
    char s[STRMAX];
    leLinha(s);
    printf("%s",s);
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
  "source_sha256": "234c1056fa0b28c56db0ede706ff99ff6322ea0a392b2018f90c0e5cfd1f6271",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "pass",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "ola adeusssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "abccbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "abdddbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "pass",
    "test:ex05_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "large",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "large",
    "stdout:ex05_2:relation": "__unknown__",
    "stdout:ex05_2:edit_band": "__unknown__",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "pass",
    "test:ex05_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_025 — validation

```c

#include <stdio.h>
#define STRMAX 80
int leLinha(char s[]){
    char letra;
    int cont = 1;
    scanf("%c",&letra);
    s[0] = letra;
    while (letra != '\n' && letra != EOF && cont<STRMAX-1){
        scanf("%c",&letra);
        s[cont]= letra;
        cont++;
    }
    return cont;
}
int main(){
    char s[STRMAX];
    leLinha(s);
    printf("%s",s);
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
  "source_sha256": "96f98b06a33210c6dc98f1546d76feb1fd8ee52395a740bf26e03c455956f3d1",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "pass",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "ola adeusssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "abccbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "abdddbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "pass",
    "test:ex05_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "large",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "large",
    "stdout:ex05_2:relation": "__unknown__",
    "stdout:ex05_2:edit_band": "__unknown__",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "pass",
    "test:ex05_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_026 — validation

```c

#include <stdio.h>
#define STRMAX 80
int leLinha(char s[]){
    char letra;
    int cont = 1;
    scanf("%c",&letra);
    s[0] = letra;
    while (letra != '\n' && letra != EOF && cont<STRMAX-1){
        scanf("%c",&letra);
        s[cont]= letra;
        cont++;
    }
    return cont+1;
}
int main(){
    char s[STRMAX];
    leLinha(s);
    printf("%s",s);
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
  "source_sha256": "ae91894f65a8713b5323ff703f886c7ea8610139cd9a073a40bb2a950768eac9",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "pass",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "ola adeusssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "abccbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "abdddbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "pass",
    "test:ex05_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "large",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "large",
    "stdout:ex05_2:relation": "__unknown__",
    "stdout:ex05_2:edit_band": "__unknown__",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "pass",
    "test:ex05_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_027 — validation

```c

#include <stdio.h>
#define STRMAX 80
int leLinha(char s[]){
    char letra;
    int cont = 1;
    scanf("%c",&letra);
    s[0] = letra;
    while (letra != '\n' && letra != EOF && cont<STRMAX-1){
        scanf("%c",&letra);
        s[cont]= letra;
        cont++;
    }
    return cont;
}
int main(){
    char s[STRMAX];
    leLinha(s);
    printf("%s",s);
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
  "source_sha256": "413af6f7572c3eb12bf4cedaf0fdaac27f4d813409839df09046316f0e906bf0",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "pass",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "ola adeusssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "abccbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "abdddbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "pass",
    "test:ex05_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "large",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "large",
    "stdout:ex05_2:relation": "__unknown__",
    "stdout:ex05_2:edit_band": "__unknown__",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "pass",
    "test:ex05_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
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


## sample_028 — train

```c

#include <stdio.h>
#define MAX 80
void leLinha(char s[]) {
    int i,soma=0;
    for (i=0;s[i]!='\n' && s[i]!='\0';i++) {
        if (s[i]!= ' ') {
            soma++;
            } 
        }
    printf("%d",soma);
}
int main() {
    char s[MAX];
    fgets(s,MAX,stdin);
    leLinha(s);
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
  "source_sha256": "6c6956d53d59c89e3010107160e67a54044fec00d618d1797cc185722b21e9f4",
  "outcomes": {
    "ex05_0": "fail",
    "ex05_1": "fail",
    "ex05_2": "fail",
    "ex05_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex05_0",
      "input": "ola adeus",
      "expected": "ola adeus\n",
      "output": "8"
    },
    {
      "test_id": "ex05_1",
      "input": "abccba",
      "expected": "abccba\n",
      "output": "6"
    },
    {
      "test_id": "ex05_2",
      "input": "Hello world!\n",
      "expected": "Hello world!\n",
      "output": "11"
    },
    {
      "test_id": "ex05_3",
      "input": "abdddba",
      "expected": "abdddba\n",
      "output": "7"
    }
  ],
  "clustering_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_array_parameter": "1",
    "ast:c_address_of": "0",
    "ast:c_update": "1",
    "stdout:ex05_0:relation": "different",
    "stdout:ex05_0:edit_band": "large",
    "stdout:ex05_1:relation": "different",
    "stdout:ex05_1:edit_band": "large",
    "stdout:ex05_2:relation": "different",
    "stdout:ex05_2:edit_band": "large",
    "stdout:ex05_3:relation": "different",
    "stdout:ex05_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex05_0": "fail",
    "test:ex05_1": "fail",
    "test:ex05_2": "fail",
    "test:ex05_3": "fail",
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


## Evidence refs hợp lệ

```json
[
  "test_statistics",
  "feature_statistics",
  "learned_if_then_rules",
  "semantic_findings",
  "problem_statement",
  "members/sample_001/raw_code",
  "members/sample_001/tests/ex05_0",
  "members/sample_001/tests/ex05_1",
  "members/sample_001/tests/ex05_2",
  "members/sample_001/tests/ex05_3",
  "members/sample_002/raw_code",
  "members/sample_002/tests/ex05_0",
  "members/sample_002/tests/ex05_1",
  "members/sample_002/tests/ex05_3",
  "members/sample_003/raw_code",
  "members/sample_003/tests/ex05_0",
  "members/sample_003/tests/ex05_1",
  "members/sample_003/tests/ex05_2",
  "members/sample_003/tests/ex05_3",
  "members/sample_004/raw_code",
  "members/sample_004/tests/ex05_0",
  "members/sample_004/tests/ex05_1",
  "members/sample_004/tests/ex05_2",
  "members/sample_004/tests/ex05_3",
  "members/sample_005/raw_code",
  "members/sample_005/tests/ex05_0",
  "members/sample_005/tests/ex05_1",
  "members/sample_005/tests/ex05_2",
  "members/sample_005/tests/ex05_3",
  "members/sample_006/raw_code",
  "members/sample_006/tests/ex05_0",
  "members/sample_006/tests/ex05_1",
  "members/sample_006/tests/ex05_2",
  "members/sample_006/tests/ex05_3",
  "members/sample_007/raw_code",
  "members/sample_007/tests/ex05_0",
  "members/sample_007/tests/ex05_1",
  "members/sample_007/tests/ex05_2",
  "members/sample_007/tests/ex05_3",
  "members/sample_008/raw_code",
  "members/sample_008/tests/ex05_0",
  "members/sample_008/tests/ex05_1",
  "members/sample_008/tests/ex05_2",
  "members/sample_008/tests/ex05_3",
  "members/sample_009/raw_code",
  "members/sample_009/tests/ex05_0",
  "members/sample_009/tests/ex05_1",
  "members/sample_009/tests/ex05_2",
  "members/sample_009/tests/ex05_3",
  "members/sample_010/raw_code",
  "members/sample_010/tests/ex05_0",
  "members/sample_010/tests/ex05_1",
  "members/sample_010/tests/ex05_2",
  "members/sample_010/tests/ex05_3",
  "members/sample_011/raw_code",
  "members/sample_011/tests/ex05_0",
  "members/sample_011/tests/ex05_1",
  "members/sample_011/tests/ex05_2",
  "members/sample_011/tests/ex05_3",
  "members/sample_012/raw_code",
  "members/sample_012/tests/ex05_0",
  "members/sample_012/tests/ex05_1",
  "members/sample_012/tests/ex05_2",
  "members/sample_012/tests/ex05_3",
  "members/sample_013/raw_code",
  "members/sample_013/tests/ex05_0",
  "members/sample_013/tests/ex05_1",
  "members/sample_013/tests/ex05_2",
  "members/sample_013/tests/ex05_3",
  "members/sample_014/raw_code",
  "members/sample_014/tests/ex05_0",
  "members/sample_014/tests/ex05_1",
  "members/sample_014/tests/ex05_2",
  "members/sample_014/tests/ex05_3",
  "members/sample_015/raw_code",
  "members/sample_015/tests/ex05_0",
  "members/sample_015/tests/ex05_1",
  "members/sample_015/tests/ex05_2",
  "members/sample_015/tests/ex05_3",
  "members/sample_016/raw_code",
  "members/sample_016/tests/ex05_0",
  "members/sample_016/tests/ex05_1",
  "members/sample_016/tests/ex05_2",
  "members/sample_016/tests/ex05_3",
  "members/sample_017/raw_code",
  "members/sample_017/tests/ex05_0",
  "members/sample_017/tests/ex05_1",
  "members/sample_017/tests/ex05_2",
  "members/sample_017/tests/ex05_3",
  "members/sample_018/raw_code",
  "members/sample_018/tests/ex05_0",
  "members/sample_018/tests/ex05_1",
  "members/sample_018/tests/ex05_2",
  "members/sample_018/tests/ex05_3",
  "members/sample_019/raw_code",
  "members/sample_019/tests/ex05_0",
  "members/sample_019/tests/ex05_1",
  "members/sample_019/tests/ex05_2",
  "members/sample_019/tests/ex05_3",
  "members/sample_020/raw_code",
  "members/sample_020/tests/ex05_0",
  "members/sample_020/tests/ex05_1",
  "members/sample_020/tests/ex05_2",
  "members/sample_020/tests/ex05_3",
  "members/sample_021/raw_code",
  "members/sample_021/tests/ex05_0",
  "members/sample_021/tests/ex05_1",
  "members/sample_021/tests/ex05_2",
  "members/sample_021/tests/ex05_3",
  "members/sample_022/raw_code",
  "members/sample_022/tests/ex05_0",
  "members/sample_022/tests/ex05_1",
  "members/sample_022/tests/ex05_2",
  "members/sample_022/tests/ex05_3",
  "members/sample_023/raw_code",
  "members/sample_023/tests/ex05_0",
  "members/sample_023/tests/ex05_1",
  "members/sample_023/tests/ex05_2",
  "members/sample_023/tests/ex05_3",
  "members/sample_024/raw_code",
  "members/sample_024/tests/ex05_0",
  "members/sample_024/tests/ex05_1",
  "members/sample_024/tests/ex05_3",
  "members/sample_025/raw_code",
  "members/sample_025/tests/ex05_0",
  "members/sample_025/tests/ex05_1",
  "members/sample_025/tests/ex05_3",
  "members/sample_026/raw_code",
  "members/sample_026/tests/ex05_0",
  "members/sample_026/tests/ex05_1",
  "members/sample_026/tests/ex05_3",
  "members/sample_027/raw_code",
  "members/sample_027/tests/ex05_0",
  "members/sample_027/tests/ex05_1",
  "members/sample_027/tests/ex05_3",
  "members/sample_028/raw_code",
  "members/sample_028/tests/ex05_0",
  "members/sample_028/tests/ex05_1",
  "members/sample_028/tests/ex05_2",
  "members/sample_028/tests/ex05_3",
  "members/sample_029/raw_code",
  "members/sample_029/tests/ex05_0",
  "members/sample_029/tests/ex05_1",
  "members/sample_029/tests/ex05_2",
  "members/sample_029/tests/ex05_3"
]
```
