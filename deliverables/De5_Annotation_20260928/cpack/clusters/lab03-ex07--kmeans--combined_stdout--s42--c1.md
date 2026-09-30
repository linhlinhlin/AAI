# lab03-ex07--kmeans--combined_stdout--s42--c1

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 15; phân vùng: {'train': 13, 'validation': 2}.


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
    "n_cluster": 15,
    "n_observed": 15,
    "n_failed": 15,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 15
    }
  },
  {
    "test_id": "ex07_1",
    "n_cluster": 15,
    "n_observed": 15,
    "n_failed": 15,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 15
    }
  },
  {
    "test_id": "ex07_2",
    "n_cluster": 15,
    "n_observed": 15,
    "n_failed": 15,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 15
    }
  },
  {
    "test_id": "ex07_3",
    "n_cluster": 15,
    "n_observed": 15,
    "n_failed": 15,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 15
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex07_0:relation",
    "value": "whitespace",
    "n": 15,
    "n_cluster": 15,
    "rate": 1.0,
    "cohort_rate": 0.2830188679245283,
    "difference_from_cohort": 0.7169811320754718
  },
  {
    "feature": "stdout:ex07_1:relation",
    "value": "whitespace",
    "n": 15,
    "n_cluster": 15,
    "rate": 1.0,
    "cohort_rate": 0.2830188679245283,
    "difference_from_cohort": 0.7169811320754718
  },
  {
    "feature": "stdout:ex07_2:edit_band",
    "value": "small",
    "n": 15,
    "n_cluster": 15,
    "rate": 1.0,
    "cohort_rate": 0.2830188679245283,
    "difference_from_cohort": 0.7169811320754718
  },
  {
    "feature": "stdout:ex07_2:relation",
    "value": "whitespace",
    "n": 15,
    "n_cluster": 15,
    "rate": 1.0,
    "cohort_rate": 0.2830188679245283,
    "difference_from_cohort": 0.7169811320754718
  },
  {
    "feature": "stdout:ex07_3:relation",
    "value": "whitespace",
    "n": 15,
    "n_cluster": 15,
    "rate": 1.0,
    "cohort_rate": 0.2830188679245283,
    "difference_from_cohort": 0.7169811320754718
  },
  {
    "feature": "stdout:ex07_0:edit_band",
    "value": "medium",
    "n": 15,
    "n_cluster": 15,
    "rate": 1.0,
    "cohort_rate": 0.33962264150943394,
    "difference_from_cohort": 0.6603773584905661
  },
  {
    "feature": "stdout:ex07_1:edit_band",
    "value": "medium",
    "n": 15,
    "n_cluster": 15,
    "rate": 1.0,
    "cohort_rate": 0.33962264150943394,
    "difference_from_cohort": 0.6603773584905661
  },
  {
    "feature": "stdout:ex07_3:edit_band",
    "value": "medium",
    "n": 15,
    "n_cluster": 15,
    "rate": 1.0,
    "cohort_rate": 0.4339622641509434,
    "difference_from_cohort": 0.5660377358490566
  },
  {
    "feature": "test:ex07_0",
    "value": "fail",
    "n": 15,
    "n_cluster": 15,
    "rate": 1.0,
    "cohort_rate": 0.8113207547169812,
    "difference_from_cohort": 0.18867924528301883
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 11,
    "n_cluster": 15,
    "rate": 0.7333333333333333,
    "cohort_rate": 0.5660377358490566,
    "difference_from_cohort": 0.1672955974842767
  },
  {
    "feature": "test:ex07_1",
    "value": "fail",
    "n": 15,
    "n_cluster": 15,
    "rate": 1.0,
    "cohort_rate": 0.8490566037735849,
    "difference_from_cohort": 0.15094339622641506
  },
  {
    "feature": "ast:c_while",
    "value": "1",
    "n": 15,
    "n_cluster": 15,
    "rate": 1.0,
    "cohort_rate": 0.9245283018867925,
    "difference_from_cohort": 0.07547169811320753
  },
  {
    "feature": "ast:c_update",
    "value": "0",
    "n": 14,
    "n_cluster": 15,
    "rate": 0.9333333333333333,
    "cohort_rate": 0.8679245283018868,
    "difference_from_cohort": 0.06540880503144653
  },
  {
    "feature": "ast:c_address_of",
    "value": "0",
    "n": 15,
    "n_cluster": 15,
    "rate": 1.0,
    "cohort_rate": 0.9433962264150944,
    "difference_from_cohort": 0.05660377358490565
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "0",
    "n": 14,
    "n_cluster": 15,
    "rate": 0.9333333333333333,
    "cohort_rate": 0.8867924528301887,
    "difference_from_cohort": 0.046540880503144644
  },
  {
    "feature": "test:ex07_3",
    "value": "fail",
    "n": 15,
    "n_cluster": 15,
    "rate": 1.0,
    "cohort_rate": 0.9622641509433962,
    "difference_from_cohort": 0.037735849056603765
  },
  {
    "feature": "ast:c_zero_index",
    "value": "1",
    "n": 1,
    "n_cluster": 15,
    "rate": 0.06666666666666667,
    "cohort_rate": 0.03773584905660377,
    "difference_from_cohort": 0.028930817610062894
  },
  {
    "feature": "ast:c_for",
    "value": "0",
    "n": 14,
    "n_cluster": 15,
    "rate": 0.9333333333333333,
    "cohort_rate": 0.9056603773584906,
    "difference_from_cohort": 0.02767295597484276
  },
  {
    "feature": "ast:c_subscript",
    "value": "0",
    "n": 14,
    "n_cluster": 15,
    "rate": 0.9333333333333333,
    "cohort_rate": 0.9056603773584906,
    "difference_from_cohort": 0.02767295597484276
  },
  {
    "feature": "ast:c_dereference",
    "value": "0",
    "n": 15,
    "n_cluster": 15,
    "rate": 1.0,
    "cohort_rate": 0.9811320754716981,
    "difference_from_cohort": 0.018867924528301883
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 11,
    "n_cluster": 15,
    "rate": 0.7333333333333333,
    "cohort_rate": 0.5660377358490566,
    "difference_from_cohort": 0.1672955974842767
  },
  {
    "feature": "ast:c_while",
    "value": "1",
    "n": 15,
    "n_cluster": 15,
    "rate": 1.0,
    "cohort_rate": 0.9245283018867925,
    "difference_from_cohort": 0.07547169811320753
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 15,
    "n_cluster": 15,
    "rate": 1.0,
    "cohort_rate": 0.9811320754716981,
    "difference_from_cohort": 0.018867924528301883
  },
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 15,
    "n_cluster": 15,
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
    "rule_id": 3,
    "if": [
      "NOT (stdout:ex07_0:relation=different)",
      "stdout:ex07_2:relation=whitespace"
    ],
    "then_cluster": 1,
    "train_support": 13,
    "train_precision": 1.0,
    "holdout_support": 2,
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
  "reasoning": "Có 15 bài trong cụm. Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
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

sample_001, sample_006, sample_005, sample_004

## sample_001 — train — đại diện

```c
#include <stdio.h>

int main() {
    int c, eh_numero = 1, numero = 0, total = 0, eh_soma = 1;
    while((c = getchar()) != '\n') {

        if(c == ' ') {
            if(eh_numero) {
                if(eh_soma) total += numero;
                else total -= numero;
                numero = 0;
            }
            eh_numero = 0;
        } else if(c == '+' || c == '-') {
            if(c == '+') eh_soma = 1;
            else eh_soma = 0;
        } else if('0' <= c && c <= '9') {
            if(eh_numero) numero = numero * 10 + (c - '0');
            else numero = c - '0';
            eh_numero = 1;
        }
    }
    if(eh_soma) total += numero;
    else total -= numero;

    printf("%d", total);
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
  "source_sha256": "fb11b7215f2d58fbbcf00ede2eca33ce140087f81e67f2eb51a0d6c5642faa07",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8 + 1\n",
      "expected": "9\n",
      "output": "9"
    },
    {
      "test_id": "ex07_1",
      "input": "9 - 3 + 2 - 5\n",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex07_2",
      "input": "102 + 3456 + 45678 - 123 - 12\n",
      "expected": "49101\n",
      "output": "49101"
    },
    {
      "test_id": "ex07_3",
      "input": "1 + 10 + 100\n",
      "expected": "111\n",
      "output": "111"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_004 — validation — đại diện

```c


#include <stdio.h>

#define FALSE 0
#define TRUE 1

int charToDecimal(char c);
int strToInt();
char getOperator();
int evaluateExpressionTail(int currentEval, char operator);

int main() {
    int result = evaluateExpressionTail(0, '+');
    printf("\n%d\n", result);
    return 0;
}

int charToDecimal(char c) {
    return (9 - (57 % (int)c));
}

int strToInt() {
    char c;
    int num = 0;
    while((c = getchar()) != EOF && c != ' ' && c != '\\' && c != 'n' && c != '\n') {
        c = charToDecimal(c);
        num = num * 10 + c;
    }
    return num;
}

char getOperator() {
    char operator = getchar();
    getchar();
    return operator;
}

int evaluateExpressionTail(int currentEval, char operator) {
    int currentNum = strToInt();
    char nextOperator = getOperator();
    if (nextOperator == EOF || nextOperator == '\\' || nextOperator == 'n' || nextOperator == '\n') {
        if (operator == '+')
            return (currentEval + currentNum);
        return (currentEval - currentNum);
    }
    if (operator == '+')
        return evaluateExpressionTail((currentEval + currentNum), nextOperator);
    return evaluateExpressionTail((currentEval - currentNum), nextOperator);
}
```

```json
{
  "sample_id": "sample_004",
  "partition": "validation",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "05f6993b845d372e9f62e7eaed6aaefc8eaeef763864a275cccfab3181da107b",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8 + 1\n",
      "expected": "9\n",
      "output": "\n9\n"
    },
    {
      "test_id": "ex07_1",
      "input": "9 - 3 + 2 - 5\n",
      "expected": "3\n",
      "output": "\n3\n"
    },
    {
      "test_id": "ex07_2",
      "input": "102 + 3456 + 45678 - 123 - 12\n",
      "expected": "49101\n",
      "output": "\n49101\n"
    },
    {
      "test_id": "ex07_3",
      "input": "1 + 10 + 100\n",
      "expected": "111\n",
      "output": "\n111\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
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


## sample_005 — train — đại diện

```c


#include <stdio.h>

int main() {
    int c;
    int numero = 0;
    int conta = 0;
    int soma = 0;
    int sub = 0;

    while ((c = getchar()) != '\n'){
        if(c == ' ' && numero > 0){

            if(conta == 0){
                conta = numero;
                numero = 0;
            }
            if(soma){
                conta +=numero;
                numero = 0;
                soma = 0;
            }
            if(sub){
                conta -= numero;
                numero = 0;
                sub = 0;
            }
        }

        else if(c == '+')
            soma = 1;

        else if(c == '-')
            sub = 1;

        else if(c != ' '){
            numero = (10 * numero) + c - '0';
        }
            
    }
    if(soma){
        conta += numero;
    }
    if(sub){
        conta -= numero;
    }

    printf("%d \n", conta);

    return 0;
}

```

```json
{
  "sample_id": "sample_005",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "876163a3d626bd3d45e52afcd2d730b2b82094843dcc515132e0b9116e9afef6",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8 + 1\n",
      "expected": "9\n",
      "output": "9 \n"
    },
    {
      "test_id": "ex07_1",
      "input": "9 - 3 + 2 - 5\n",
      "expected": "3\n",
      "output": "3 \n"
    },
    {
      "test_id": "ex07_2",
      "input": "102 + 3456 + 45678 - 123 - 12\n",
      "expected": "49101\n",
      "output": "49101 \n"
    },
    {
      "test_id": "ex07_3",
      "input": "1 + 10 + 100\n",
      "expected": "111\n",
      "output": "111 \n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
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
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_006 — train — đại diện

```c


#include <stdio.h>

#define OUT 0
#define IN 1
#define SUM 10
#define SUBTRACT 11
#define ZERO_ASCII 48
#define NINE_ASCII 57
#define DIM 1000

int main() {

    int c, len, num = 0, soma = 0;
    int estado = OUT, estadoN = IN, estadoC = 0;
    int i = 0, j = 0;
    char tab[DIM][DIM];

    c = getchar();
    while (c != '\n' && c != EOF) {
        if (estado == OUT) {
            if (c >= ZERO_ASCII && c <= NINE_ASCII) {
                estado = IN;
                tab[i][j] = c;
                j++;
            }
            else if (c == '+' || c == '-') {
                tab[i][j] = c;
                j++;
                tab[i][j] = '\0';
                i++;
                j = 0;
            }
        }
        else if (estado == IN) {
            if (c == ' ') {
                estado = OUT;
                j++;
                tab[i][j] = '\0';
                j = 0;
                i++;
            }
            else {
                tab[i][j] = c;
                j++;
            }
        }
        c = getchar();
    }
    tab[i][j] = '\0';
    len = i;

    for (i = 0; i <= len; i++) {
        for (j = 0; tab[i][j] != '\0'; j++) {
            if (tab[i][j] >= ZERO_ASCII && tab[i][j] <= NINE_ASCII)
                estadoN = IN;
            else if (tab[i][0] == '+') {
                estadoC = SUM;
                estadoN = OUT;
            }
            else if (tab[i][0] == '-') {
                estadoC = SUBTRACT;
                estadoN = OUT;
            }
            if (estadoN == IN)
                num = num*10 + tab[i][j] - '0';
        }
        if (i == 0) {
            soma = num;
            num = 0;
        }
        if (estadoC == SUM) {
            soma += num;
            num = 0;
        }
        else if (estadoC == SUBTRACT) {
            soma -= num;
            num = 0;
        } 
    }

    printf("%d", soma);

    return 0;
}     
```

```json
{
  "sample_id": "sample_006",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "7d3463dbe667c4a1ea172e1ca287906b1c2924b3421e6fa51f4206ecc0df82ce",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8 + 1\n",
      "expected": "9\n",
      "output": "9"
    },
    {
      "test_id": "ex07_1",
      "input": "9 - 3 + 2 - 5\n",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex07_2",
      "input": "102 + 3456 + 45678 - 123 - 12\n",
      "expected": "49101\n",
      "output": "49101"
    },
    {
      "test_id": "ex07_3",
      "input": "1 + 10 + 100\n",
      "expected": "111\n",
      "output": "111"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "1",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "1",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "1",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "1",
    "ast:c_zero_index": "1",
    "ast:c_one_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_array_parameter": "0",
    "ast:c_address_of": "0",
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

#define SOMA 0
#define SUB 1
#define FOP 2

void calculadora(){
	int c, soma, num, op;
	num = 0;
	soma = 0;
	op = FOP;
	while ((c = getchar()) != '\n'){
		if (c >= '0' && c <= '9'){
			num = (num*10) + (c - '0');
		}
		if (c == '+'){
			op = SOMA;
			num = 0;
		}
		if  (c == '-'){
			op = SUB;
			num = 0;
		}
		if (c == ' '){
			if (op == SOMA){
				soma += num;
			} else if (op == SUB){
				soma -= num;
			} else if (op == FOP){
				soma =  num;
			}
		}
	}
	if (op == SOMA){
		soma += num;
	} else if (op == SUB){
		soma -= num;
	} else if (op == FOP){
		soma =  num;
	}
	printf("\n%d\n", soma);
}


int main(){
	calculadora();
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
  "source_sha256": "2244e0501aa298ec2298a6f69c6d860abb13a4cb9bafa6f15c0b69bb7f394132",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8 + 1\n",
      "expected": "9\n",
      "output": "\n9\n"
    },
    {
      "test_id": "ex07_1",
      "input": "9 - 3 + 2 - 5\n",
      "expected": "3\n",
      "output": "\n3\n"
    },
    {
      "test_id": "ex07_2",
      "input": "102 + 3456 + 45678 - 123 - 12\n",
      "expected": "49101\n",
      "output": "\n49101\n"
    },
    {
      "test_id": "ex07_3",
      "input": "1 + 10 + 100\n",
      "expected": "111\n",
      "output": "\n111\n"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_003 — validation

```c
#include <stdio.h>

#define MENOS 0
#define MAIS 1

int main()
{
    char c;
    int atual = 0, total = 0;
    int estado = MAIS;

    while((c = getchar()) != '\n')
    {
        if(0 <= c - '0' && c - '0' <= 9)
            atual = atual * 10 + c - '0';
        
        else if(c == ' ')
        {
            if(estado == MAIS)
                total += atual;
            else if(estado == MENOS)
                total -= atual;
            
            if((c = getchar()) == '+')
                estado = MAIS;
            else if(c == '-')
                estado = MENOS;
            
            c = getchar();
            atual = 0;
        }
    }

    if(estado == MAIS)
        total += atual;
    else if(estado == MENOS)
        total -= atual;
    
    printf("%d", total);
    
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
  "source_sha256": "d201222aa93ca77553bd065faf0df4c3d73ceedf52a20f9e28f646189a172941",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8 + 1\n",
      "expected": "9\n",
      "output": "9"
    },
    {
      "test_id": "ex07_1",
      "input": "9 - 3 + 2 - 5\n",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex07_2",
      "input": "102 + 3456 + 45678 - 123 - 12\n",
      "expected": "49101\n",
      "output": "49101"
    },
    {
      "test_id": "ex07_3",
      "input": "1 + 10 + 100\n",
      "expected": "111\n",
      "output": "111"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_address_of": "0",
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

#define ZERO '0'

int main()
{
    int c, dig, numero = 0, op = '+', op_total = 0, eh_numero = 0;

    while ((c = getchar()) != '\n') {
        if (c >= '0' && c <= '9') {
            dig = c - ZERO;
            if (eh_numero == 0) {
                numero += dig;
                eh_numero = 1;
            } else if (eh_numero == 1) {
                numero = numero * 10 + dig;
            }
        } else if (c == ' ') {
            if (op == '+')
                op_total += numero;
            else
                op_total -= numero;
            
            op = getchar();
            getchar(); 


            numero = 0;
            eh_numero = 0;
        }
    }

    if (op == '+')
        op_total += numero;
    else
        op_total -= numero;

    printf("%d", op_total);
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
  "source_sha256": "a38b3eba4570de15d6eb3aa12a6eb08d30f04f020f06f234df50fcaa2d738265",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8 + 1\n",
      "expected": "9\n",
      "output": "9"
    },
    {
      "test_id": "ex07_1",
      "input": "9 - 3 + 2 - 5\n",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex07_2",
      "input": "102 + 3456 + 45678 - 123 - 12\n",
      "expected": "49101\n",
      "output": "49101"
    },
    {
      "test_id": "ex07_3",
      "input": "1 + 10 + 100\n",
      "expected": "111\n",
      "output": "111"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_address_of": "0",
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

#define ZERO '0'

int main()
{
    int c, dig, op = '+';
    int numero = 0, op_total = 0, eh_numero = 0;

    while ((c = getchar()) != '\n') {
        if (c >= '0' && c <= '9') {
            dig = c - ZERO;
            if (eh_numero == 0) {
                numero += dig;
                eh_numero = 1;
            } else if (eh_numero == 1)
                numero = numero * 10 + dig;
            
        } else if (c == ' ') {
            if (op == '+')
                op_total += numero;
            else
                op_total -= numero;
            
            op = getchar();
            getchar(); 
            numero = 0;
            eh_numero = 0;
        }
    }

    if (op == '+')
        op_total += numero;
    else
        op_total -= numero;

    printf("%d", op_total);

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
  "source_sha256": "afa1ac33cf64e1f7815bc94b45822fd708bfa27aba8816cc52942cbdb9811822",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8 + 1\n",
      "expected": "9\n",
      "output": "9"
    },
    {
      "test_id": "ex07_1",
      "input": "9 - 3 + 2 - 5\n",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex07_2",
      "input": "102 + 3456 + 45678 - 123 - 12\n",
      "expected": "49101\n",
      "output": "49101"
    },
    {
      "test_id": "ex07_3",
      "input": "1 + 10 + 100\n",
      "expected": "111\n",
      "output": "111"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_address_of": "0",
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

#define ZERO '0'

int main()
{
    int c, dig, numero = 0, op = '+', op_total = 0, eh_numero = 0;

    while ((c = getchar()) != '\n') {
        if (c >= '0' && c <= '9') {
            dig = c - ZERO;
            if (eh_numero == 0) {
                numero += dig;
                eh_numero = 1;
            } else if (eh_numero == 1) {
                numero = numero * 10 + dig;
            }
        } else if (c == ' ') {
            if (op == '+')
                op_total += numero;
            else
                op_total -= numero;
            
            op = getchar();
            getchar(); 


            numero = 0;
            eh_numero = 0;
        }
    }

    if (op == '+')
        op_total += numero;
    else
        op_total -= numero;

    printf("%d", op_total);
    
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
  "source_sha256": "639a2e60700753e172caaf32dd01e0f2eb401880b63b645a308743e3d7e4c71f",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8 + 1\n",
      "expected": "9\n",
      "output": "9"
    },
    {
      "test_id": "ex07_1",
      "input": "9 - 3 + 2 - 5\n",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex07_2",
      "input": "102 + 3456 + 45678 - 123 - 12\n",
      "expected": "49101\n",
      "output": "49101"
    },
    {
      "test_id": "ex07_3",
      "input": "1 + 10 + 100\n",
      "expected": "111\n",
      "output": "111"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_address_of": "0",
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

#define ZERO '0'

int main()
{
    int c, dig, op = '+';
    int numero = 0, op_total = 0, eh_numero = 0;

    while ((c = getchar()) != '\n') {
        if (c >= '0' && c <= '9') {
            
            dig = c - ZERO;
            if (eh_numero == 0) {
                numero += dig;
                eh_numero = 1;
            } else if (eh_numero == 1)
                numero = numero * 10 + dig;
            
        } else if (c == ' ') {
            if (op == '+')
                op_total += numero;
            else
                op_total -= numero;
            
            op = getchar();
            getchar(); 
            numero = 0;
            eh_numero = 0;
        }
    }

    if (op == '+')
        op_total += numero;
    else
        op_total -= numero;

    printf("%d", op_total);

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
  "source_sha256": "3174ae15038c9d5791efaaa7ae855f26b618d7073c4f85252790b03686fab6a0",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8 + 1\n",
      "expected": "9\n",
      "output": "9"
    },
    {
      "test_id": "ex07_1",
      "input": "9 - 3 + 2 - 5\n",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex07_2",
      "input": "102 + 3456 + 45678 - 123 - 12\n",
      "expected": "49101\n",
      "output": "49101"
    },
    {
      "test_id": "ex07_3",
      "input": "1 + 10 + 100\n",
      "expected": "111\n",
      "output": "111"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_address_of": "0",
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

#define ZERO '0'

int main()
{
    int c, dig, op = '+';
    int numero = 0,op_total = 0, eh_numero = 0;

    while ((c = getchar()) != '\n') {
        if (c >= '0' && c <= '9') {
            dig = c - ZERO;
            if (eh_numero == 0) {
                numero += dig;
                eh_numero = 1;
            } else if (eh_numero == 1) {
                numero = numero * 10 + dig;
            }
        } else if (c == ' ') {
            if (op == '+')
                op_total += numero;
            else
                op_total -= numero;
            
            op = getchar();
            getchar(); 


            numero = 0;
            eh_numero = 0;
        }
    }

    if (op == '+')
        op_total += numero;
    else
        op_total -= numero;

    printf("%d", op_total);

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
  "source_sha256": "f86f071f98231c833475435f216f88ce5f20f0c4b8b3db675739c654925b89f8",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8 + 1\n",
      "expected": "9\n",
      "output": "9"
    },
    {
      "test_id": "ex07_1",
      "input": "9 - 3 + 2 - 5\n",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex07_2",
      "input": "102 + 3456 + 45678 - 123 - 12\n",
      "expected": "49101\n",
      "output": "49101"
    },
    {
      "test_id": "ex07_3",
      "input": "1 + 10 + 100\n",
      "expected": "111\n",
      "output": "111"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_address_of": "0",
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

#define ZERO '0'

int main()
{
    int c, dig, op = '+';
    int numero = 0, op_total = 0, eh_numero = 0;

    while ((c = getchar()) != '\n') {
        if (c >= '0' && c <= '9') {
            dig = c - ZERO;
            if (eh_numero == 0) {
                numero += dig;
                eh_numero = 1;
            } else if (eh_numero == 1)
                numero = numero * 10 + dig;
            
        } else if (c == ' ') {
            if (op == '+')
                op_total += numero;
            else
                op_total -= numero;
            
            op = getchar();
            getchar(); 


            numero = 0;
            eh_numero = 0;
        }
    }

    if (op == '+')
        op_total += numero;
    else
        op_total -= numero;

    printf("%d", op_total);

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
  "source_sha256": "c6f64f183bd684918ef29af67c2ad147b75cb8bc9dacfbf6e8e0a0bae28dbd94",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8 + 1\n",
      "expected": "9\n",
      "output": "9"
    },
    {
      "test_id": "ex07_1",
      "input": "9 - 3 + 2 - 5\n",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex07_2",
      "input": "102 + 3456 + 45678 - 123 - 12\n",
      "expected": "49101\n",
      "output": "49101"
    },
    {
      "test_id": "ex07_3",
      "input": "1 + 10 + 100\n",
      "expected": "111\n",
      "output": "111"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_address_of": "0",
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

enum estado {NUMERO, FORA, INICIO};
enum operacao {SOMA, SUBTRACAO};

int algarismo(char caracter)
{
    return '0' <= caracter && caracter <= '9';
}

int main()
{
    enum estado est = INICIO;
    enum operacao op;

    char atual;
    int total = 0, num;

    while((atual = getchar()) != EOF)
    {
        switch(est)
        {
            case INICIO:
                if(algarismo(atual))
                {
                    total *= 10;
                    total += atual - '0';
                }
                else
                    est = FORA;
                break;
            case FORA:
                if(algarismo(atual))
                {
                    num = atual - '0';
                    est = NUMERO;
                }
                else if(atual == '+')
                {
                    op = SOMA;
                }
                else if(atual == '-')
                {
                    op = SUBTRACAO;
                }
                break;
            case NUMERO:
                if(algarismo(atual))
                {
                    num *= 10;
                    num += atual - '0';
                }
                else
                {
                    if(op == SOMA)
                        total += num;
                    else if(op == SUBTRACAO)
                        total -= num;
                    est = FORA;
                }
                break;
        }
    }
    printf("%d", total);
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
  "source_sha256": "e30a69d3310a0c94a288d307b8cc0a14658e8aa47a7a630a885ea85f6795f455",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8 + 1\n",
      "expected": "9\n",
      "output": "9"
    },
    {
      "test_id": "ex07_1",
      "input": "9 - 3 + 2 - 5\n",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex07_2",
      "input": "102 + 3456 + 45678 - 123 - 12\n",
      "expected": "49101\n",
      "output": "49101"
    },
    {
      "test_id": "ex07_3",
      "input": "1 + 10 + 100\n",
      "expected": "111\n",
      "output": "111"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_address_of": "0",
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

int main(){
    char chara, operador;
    int numero_atual, res, primeiro_num;
    primeiro_num = 0;
    res = 0;
    chara = 0;
    numero_atual = 0;
    while(chara != '\n'){
        chara = getchar();
        if (chara == '1'){
            numero_atual = numero_atual*10 + 1;
        }
        else if (chara == '2'){
            numero_atual = numero_atual*10 + 2;
        }
        else if (chara == '3'){
            numero_atual = numero_atual*10 + 3;
        }
        else if (chara == '4'){
            numero_atual = numero_atual*10 + 4;
        }
        else if (chara == '5'){
            numero_atual = numero_atual*10 + 5;
        }
        else if (chara == '6'){
            numero_atual = numero_atual*10 + 6;
        }
        else if (chara == '7'){
            numero_atual = numero_atual*10 + 7;
        }
        else if (chara == '8'){
            numero_atual = numero_atual*10 + 8;
        }
        else if (chara == '9'){
            numero_atual = numero_atual*10 + 9;
        }
        else if (chara == '0'){
            numero_atual = numero_atual*10;
        }
        else if (chara == ' ' && primeiro_num == 0){
            res += numero_atual;
            primeiro_num = 1;
            numero_atual = 0;
            chara = getchar();
            operador = chara;
            chara = getchar();
        } 
        else if (chara == ' ' && primeiro_num == 1){
            if(operador == '+'){
                res += numero_atual;
                numero_atual = 0;
            }
            else if(operador == '-'){
                res -= numero_atual;
                numero_atual = 0;
            }
            chara = getchar();
            operador = chara;
            chara = getchar();
        }
    }
    if(operador == '+'){
        res += numero_atual;
        }
    else if(operador == '-'){
        res -= numero_atual;
    }
    printf("%d", res);
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
  "source_sha256": "070c33216a8cb297bec71b430d607799a5c9764c0a1b6680ce0dd0323a0d4e4f",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8 + 1\n",
      "expected": "9\n",
      "output": "9"
    },
    {
      "test_id": "ex07_1",
      "input": "9 - 3 + 2 - 5\n",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex07_2",
      "input": "102 + 3456 + 45678 - 123 - 12\n",
      "expected": "49101\n",
      "output": "49101"
    },
    {
      "test_id": "ex07_3",
      "input": "1 + 10 + 100\n",
      "expected": "111\n",
      "output": "111"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
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


## sample_015 — train

```c

#include <stdio.h>

int main(){
    char chara, operador;
    int numero_atual, res, primeiro_num;
    primeiro_num = 0;
    res = 0;
    chara = 0;
    numero_atual = 0;
    while(chara != '\n'){
        chara = getchar();
        if (chara == '1'){
            numero_atual = numero_atual*10 + 1;
        }
        else if (chara == '2'){
            numero_atual = numero_atual*10 + 2;
        }
        else if (chara == '3'){
            numero_atual = numero_atual*10 + 3;
        }
        else if (chara == '4'){
            numero_atual = numero_atual*10 + 4;
        }
        else if (chara == '5'){
            numero_atual = numero_atual*10 + 5;
        }
        else if (chara == '6'){
            numero_atual = numero_atual*10 + 6;
        }
        else if (chara == '7'){
            numero_atual = numero_atual*10 + 7;
        }
        else if (chara == '8'){
            numero_atual = numero_atual*10 + 8;
        }
        else if (chara == '9'){
            numero_atual = numero_atual*10 + 9;
        }
        else if (chara == '0'){
            numero_atual = numero_atual*10;
        }
        else if (chara == ' ' && primeiro_num == 0){
            res += numero_atual;
            primeiro_num = 1;
            numero_atual = 0;
            chara = getchar();
            operador = chara;
            chara = getchar();
        } 
        else if (chara == ' ' && primeiro_num == 1){
            if(operador == '+'){
                res += numero_atual;
                numero_atual = 0;
            }
            else if(operador == '-'){
                res -= numero_atual;
                numero_atual = 0;
            }
            chara = getchar();
            operador = chara;
            chara = getchar();
        }
    }
    if(operador == '+'){
        res += numero_atual;
        }
    else if(operador == '-'){
        res -= numero_atual;
    }
    printf("%d", res);
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
  "source_sha256": "f40352d85e1a4c2293f6f14b6de0be251f897540366a53ca042b73e3621e141d",
  "outcomes": {
    "ex07_0": "fail",
    "ex07_1": "fail",
    "ex07_2": "fail",
    "ex07_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex07_0",
      "input": "8 + 1\n",
      "expected": "9\n",
      "output": "9"
    },
    {
      "test_id": "ex07_1",
      "input": "9 - 3 + 2 - 5\n",
      "expected": "3\n",
      "output": "3"
    },
    {
      "test_id": "ex07_2",
      "input": "102 + 3456 + 45678 - 123 - 12\n",
      "expected": "49101\n",
      "output": "49101"
    },
    {
      "test_id": "ex07_3",
      "input": "1 + 10 + 100\n",
      "expected": "111\n",
      "output": "111"
    }
  ],
  "clustering_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_subscript": "0",
    "ast:c_zero_index": "0",
    "ast:c_pointer_declarator": "0",
    "ast:c_pointer_parameter": "0",
    "ast:c_address_of": "0",
    "ast:c_dereference": "0",
    "ast:c_update": "0",
    "stdout:ex07_0:relation": "whitespace",
    "stdout:ex07_0:edit_band": "medium",
    "stdout:ex07_1:relation": "whitespace",
    "stdout:ex07_1:edit_band": "medium",
    "stdout:ex07_2:relation": "whitespace",
    "stdout:ex07_2:edit_band": "small",
    "stdout:ex07_3:relation": "whitespace",
    "stdout:ex07_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex07_0": "fail",
    "test:ex07_1": "fail",
    "test:ex07_2": "fail",
    "test:ex07_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
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
  "members/sample_001/tests/ex07_2",
  "members/sample_001/tests/ex07_3",
  "members/sample_002/raw_code",
  "members/sample_002/tests/ex07_0",
  "members/sample_002/tests/ex07_1",
  "members/sample_002/tests/ex07_2",
  "members/sample_002/tests/ex07_3",
  "members/sample_003/raw_code",
  "members/sample_003/tests/ex07_0",
  "members/sample_003/tests/ex07_1",
  "members/sample_003/tests/ex07_2",
  "members/sample_003/tests/ex07_3",
  "members/sample_004/raw_code",
  "members/sample_004/tests/ex07_0",
  "members/sample_004/tests/ex07_1",
  "members/sample_004/tests/ex07_2",
  "members/sample_004/tests/ex07_3",
  "members/sample_005/raw_code",
  "members/sample_005/tests/ex07_0",
  "members/sample_005/tests/ex07_1",
  "members/sample_005/tests/ex07_2",
  "members/sample_005/tests/ex07_3",
  "members/sample_006/raw_code",
  "members/sample_006/tests/ex07_0",
  "members/sample_006/tests/ex07_1",
  "members/sample_006/tests/ex07_2",
  "members/sample_006/tests/ex07_3",
  "members/sample_007/raw_code",
  "members/sample_007/tests/ex07_0",
  "members/sample_007/tests/ex07_1",
  "members/sample_007/tests/ex07_2",
  "members/sample_007/tests/ex07_3",
  "members/sample_008/raw_code",
  "members/sample_008/tests/ex07_0",
  "members/sample_008/tests/ex07_1",
  "members/sample_008/tests/ex07_2",
  "members/sample_008/tests/ex07_3",
  "members/sample_009/raw_code",
  "members/sample_009/tests/ex07_0",
  "members/sample_009/tests/ex07_1",
  "members/sample_009/tests/ex07_2",
  "members/sample_009/tests/ex07_3",
  "members/sample_010/raw_code",
  "members/sample_010/tests/ex07_0",
  "members/sample_010/tests/ex07_1",
  "members/sample_010/tests/ex07_2",
  "members/sample_010/tests/ex07_3",
  "members/sample_011/raw_code",
  "members/sample_011/tests/ex07_0",
  "members/sample_011/tests/ex07_1",
  "members/sample_011/tests/ex07_2",
  "members/sample_011/tests/ex07_3",
  "members/sample_012/raw_code",
  "members/sample_012/tests/ex07_0",
  "members/sample_012/tests/ex07_1",
  "members/sample_012/tests/ex07_2",
  "members/sample_012/tests/ex07_3",
  "members/sample_013/raw_code",
  "members/sample_013/tests/ex07_0",
  "members/sample_013/tests/ex07_1",
  "members/sample_013/tests/ex07_2",
  "members/sample_013/tests/ex07_3",
  "members/sample_014/raw_code",
  "members/sample_014/tests/ex07_0",
  "members/sample_014/tests/ex07_1",
  "members/sample_014/tests/ex07_2",
  "members/sample_014/tests/ex07_3",
  "members/sample_015/raw_code",
  "members/sample_015/tests/ex07_0",
  "members/sample_015/tests/ex07_1",
  "members/sample_015/tests/ex07_2",
  "members/sample_015/tests/ex07_3"
]
```
