# lab02-ex10--kmeans--combined_stdout--s42--c1

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 11; phân vùng: {'train': 10, 'validation': 1}.


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
    "test_id": "ex10_0",
    "n_cluster": 11,
    "n_observed": 11,
    "n_failed": 11,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 11
    }
  },
  {
    "test_id": "ex10_1",
    "n_cluster": 11,
    "n_observed": 11,
    "n_failed": 11,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 11
    }
  },
  {
    "test_id": "ex10_2",
    "n_cluster": 11,
    "n_observed": 11,
    "n_failed": 11,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 11
    }
  },
  {
    "test_id": "ex10_3",
    "n_cluster": 11,
    "n_observed": 11,
    "n_failed": 11,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 11
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex10_0:relation",
    "value": "whitespace",
    "n": 11,
    "n_cluster": 11,
    "rate": 1.0,
    "cohort_rate": 0.3333333333333333,
    "difference_from_cohort": 0.6666666666666667
  },
  {
    "feature": "stdout:ex10_1:relation",
    "value": "whitespace",
    "n": 11,
    "n_cluster": 11,
    "rate": 1.0,
    "cohort_rate": 0.3333333333333333,
    "difference_from_cohort": 0.6666666666666667
  },
  {
    "feature": "stdout:ex10_2:relation",
    "value": "whitespace",
    "n": 11,
    "n_cluster": 11,
    "rate": 1.0,
    "cohort_rate": 0.3333333333333333,
    "difference_from_cohort": 0.6666666666666667
  },
  {
    "feature": "stdout:ex10_3:relation",
    "value": "whitespace",
    "n": 10,
    "n_cluster": 11,
    "rate": 0.9090909090909091,
    "cohort_rate": 0.30303030303030304,
    "difference_from_cohort": 0.606060606060606
  },
  {
    "feature": "stdout:ex10_1:edit_band",
    "value": "medium",
    "n": 11,
    "n_cluster": 11,
    "rate": 1.0,
    "cohort_rate": 0.45454545454545453,
    "difference_from_cohort": 0.5454545454545454
  },
  {
    "feature": "stdout:ex10_2:edit_band",
    "value": "medium",
    "n": 10,
    "n_cluster": 11,
    "rate": 0.9090909090909091,
    "cohort_rate": 0.3939393939393939,
    "difference_from_cohort": 0.5151515151515151
  },
  {
    "feature": "stdout:ex10_0:edit_band",
    "value": "medium",
    "n": 11,
    "n_cluster": 11,
    "rate": 1.0,
    "cohort_rate": 0.5757575757575758,
    "difference_from_cohort": 0.4242424242424242
  },
  {
    "feature": "stdout:ex10_3:edit_band",
    "value": "medium",
    "n": 10,
    "n_cluster": 11,
    "rate": 0.9090909090909091,
    "cohort_rate": 0.5757575757575758,
    "difference_from_cohort": 0.33333333333333326
  },
  {
    "feature": "test:ex10_0",
    "value": "fail",
    "n": 11,
    "n_cluster": 11,
    "rate": 1.0,
    "cohort_rate": 0.7878787878787878,
    "difference_from_cohort": 0.21212121212121215
  },
  {
    "feature": "ast:c_while",
    "value": "1",
    "n": 11,
    "n_cluster": 11,
    "rate": 1.0,
    "cohort_rate": 0.8484848484848485,
    "difference_from_cohort": 0.1515151515151515
  },
  {
    "feature": "test:ex10_1",
    "value": "fail",
    "n": 11,
    "n_cluster": 11,
    "rate": 1.0,
    "cohort_rate": 0.8484848484848485,
    "difference_from_cohort": 0.1515151515151515
  },
  {
    "feature": "test:ex10_2",
    "value": "fail",
    "n": 11,
    "n_cluster": 11,
    "rate": 1.0,
    "cohort_rate": 0.8484848484848485,
    "difference_from_cohort": 0.1515151515151515
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "0",
    "n": 7,
    "n_cluster": 11,
    "rate": 0.6363636363636364,
    "cohort_rate": 0.48484848484848486,
    "difference_from_cohort": 0.1515151515151515
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 11,
    "n_cluster": 11,
    "rate": 1.0,
    "cohort_rate": 0.8787878787878788,
    "difference_from_cohort": 0.12121212121212122
  },
  {
    "feature": "test:ex10_3",
    "value": "fail",
    "n": 11,
    "n_cluster": 11,
    "rate": 1.0,
    "cohort_rate": 0.9090909090909091,
    "difference_from_cohort": 0.09090909090909094
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 10,
    "n_cluster": 11,
    "rate": 0.9090909090909091,
    "cohort_rate": 0.8181818181818182,
    "difference_from_cohort": 0.09090909090909083
  },
  {
    "feature": "ast:c_if",
    "value": "0",
    "n": 11,
    "n_cluster": 11,
    "rate": 1.0,
    "cohort_rate": 0.9393939393939394,
    "difference_from_cohort": 0.06060606060606055
  },
  {
    "feature": "stdout:ex10_2:edit_band",
    "value": "small",
    "n": 1,
    "n_cluster": 11,
    "rate": 0.09090909090909091,
    "cohort_rate": 0.06060606060606061,
    "difference_from_cohort": 0.030303030303030304
  },
  {
    "feature": "ast:c_do",
    "value": "0",
    "n": 11,
    "n_cluster": 11,
    "rate": 1.0,
    "cohort_rate": 0.9696969696969697,
    "difference_from_cohort": 0.030303030303030276
  },
  {
    "feature": "ast:c_for",
    "value": "0",
    "n": 11,
    "n_cluster": 11,
    "rate": 1.0,
    "cohort_rate": 0.9696969696969697,
    "difference_from_cohort": 0.030303030303030276
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_while",
    "value": "1",
    "n": 11,
    "n_cluster": 11,
    "rate": 1.0,
    "cohort_rate": 0.8484848484848485,
    "difference_from_cohort": 0.1515151515151515
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 11,
    "n_cluster": 11,
    "rate": 1.0,
    "cohort_rate": 0.8787878787878788,
    "difference_from_cohort": 0.12121212121212122
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 10,
    "n_cluster": 11,
    "rate": 0.9090909090909091,
    "cohort_rate": 0.8181818181818182,
    "difference_from_cohort": 0.09090909090909083
  },
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 11,
    "n_cluster": 11,
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
      "NOT (stdout:ex10_1:relation=different)",
      "test:ex10_1=fail"
    ],
    "then_cluster": 1,
    "train_support": 10,
    "train_precision": 1.0,
    "holdout_support": 3,
    "holdout_precision": 0.3333333333333333
  }
]
```


## Candidate chưa xác thực

```json
{
  "source": "local_heuristic_not_gold",
  "misconception_name": "Chưa đủ bằng chứng để đặt tên lỗi",
  "misconception_type": null,
  "reasoning": "Có 11 bài trong cụm. Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
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

sample_005, sample_001, sample_003, sample_002

## sample_001 — train — đại diện

```c
#include <stdio.h>

int N;
int dig, soma = 0, contador = 0;

int main(){

    scanf("%d", &N);
    while (N > 0 ){
        dig = N % 10;
        N = N / 10;
        contador += 1;
        soma = soma + dig;
    }   
    printf("%d\t%d\n", contador, soma);
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
  "source_sha256": "8088f5ffb46961d3c2f2384b62ea60e2dc06beff51b7315efdf0b7b4468e9b73",
  "outcomes": {
    "ex10_0": "fail",
    "ex10_1": "fail",
    "ex10_2": "fail",
    "ex10_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex10_0",
      "input": "12",
      "expected": "2\n3\n",
      "output": "2\t3\n"
    },
    {
      "test_id": "ex10_1",
      "input": "123",
      "expected": "3\n6\n",
      "output": "3\t6\n"
    },
    {
      "test_id": "ex10_2",
      "input": "12345",
      "expected": "5\n15\n",
      "output": "5\t15\n"
    },
    {
      "test_id": "ex10_3",
      "input": "10",
      "expected": "2\n1\n",
      "output": "2\t1\n"
    }
  ],
  "clustering_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "0",
    "stdout:ex10_0:relation": "whitespace",
    "stdout:ex10_0:edit_band": "medium",
    "stdout:ex10_1:relation": "whitespace",
    "stdout:ex10_1:edit_band": "medium",
    "stdout:ex10_2:relation": "whitespace",
    "stdout:ex10_2:edit_band": "medium",
    "stdout:ex10_3:relation": "whitespace",
    "stdout:ex10_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
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


## sample_002 — train — đại diện

```c

#include<stdio.h>

int main() {
    int N, digitos = 0, soma = 0;
    
    
    scanf("%d", &N);
    
    while (N != 0) {
        digitos++;
        soma += N % 10;
        N /= 10;
    }
    
    printf(" %d\n%d\n", digitos, soma);
    
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
  "source_sha256": "3be25fcd138c3fd07d16329ec696159dc1af86b28fc9bb4aa5b36493825098d2",
  "outcomes": {
    "ex10_0": "fail",
    "ex10_1": "fail",
    "ex10_2": "fail",
    "ex10_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex10_0",
      "input": "12",
      "expected": "2\n3\n",
      "output": " 2\n3\n"
    },
    {
      "test_id": "ex10_1",
      "input": "123",
      "expected": "3\n6\n",
      "output": " 3\n6\n"
    },
    {
      "test_id": "ex10_2",
      "input": "12345",
      "expected": "5\n15\n",
      "output": " 5\n15\n"
    },
    {
      "test_id": "ex10_3",
      "input": "10",
      "expected": "2\n1\n",
      "output": " 2\n1\n"
    }
  ],
  "clustering_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex10_0:relation": "whitespace",
    "stdout:ex10_0:edit_band": "medium",
    "stdout:ex10_1:relation": "whitespace",
    "stdout:ex10_1:edit_band": "medium",
    "stdout:ex10_2:relation": "whitespace",
    "stdout:ex10_2:edit_band": "small",
    "stdout:ex10_3:relation": "whitespace",
    "stdout:ex10_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_003 — validation — đại diện

```c

#include <stdio.h>

int main()
{
    int num, digito,soma=0, contador=0;
    scanf("%d", &num);
    while (num>0)
    {
        digito= num%10;
        num= num/10;
        soma += (digito);
        contador++;
    }
    printf("%d\n%d", contador, soma);
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
  "source_sha256": "f22b009895baeb2afec8ac19ee2d71ad353dc70a19d466cbf547fb3663f2c308",
  "outcomes": {
    "ex10_0": "fail",
    "ex10_1": "fail",
    "ex10_2": "fail",
    "ex10_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex10_0",
      "input": "12",
      "expected": "2\n3\n",
      "output": "2\n3"
    },
    {
      "test_id": "ex10_1",
      "input": "123",
      "expected": "3\n6\n",
      "output": "3\n6"
    },
    {
      "test_id": "ex10_2",
      "input": "12345",
      "expected": "5\n15\n",
      "output": "5\n15"
    },
    {
      "test_id": "ex10_3",
      "input": "10",
      "expected": "2\n1\n",
      "output": "2\n1"
    }
  ],
  "clustering_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex10_0:relation": "whitespace",
    "stdout:ex10_0:edit_band": "medium",
    "stdout:ex10_1:relation": "whitespace",
    "stdout:ex10_1:edit_band": "medium",
    "stdout:ex10_2:relation": "whitespace",
    "stdout:ex10_2:edit_band": "medium",
    "stdout:ex10_3:relation": "whitespace",
    "stdout:ex10_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
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


## sample_005 — train — đại diện

```c


#include <stdio.h>

int main() {

    int n, dig = 0, soma_dig = 0;

    scanf("%d", &n);

    while (n != 0) {
        dig++;
        soma_dig += n % 10;
        n /= 10;
    }

    printf("%d\n", dig);
    printf("%d", soma_dig);

    return 0;
}

```

```json
{
  "sample_id": "sample_005",
  "partition": "train",
  "representative": true,
  "is_train_medoid": true,
  "raw_code_truncated": false,
  "source_sha256": "478945aab8c57aab51719b9979a4b3e30c6b40053bb564873ba0102a713515a9",
  "outcomes": {
    "ex10_0": "fail",
    "ex10_1": "fail",
    "ex10_2": "fail",
    "ex10_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex10_0",
      "input": "12",
      "expected": "2\n3\n",
      "output": "2\n3"
    },
    {
      "test_id": "ex10_1",
      "input": "123",
      "expected": "3\n6\n",
      "output": "3\n6"
    },
    {
      "test_id": "ex10_2",
      "input": "12345",
      "expected": "5\n15\n",
      "output": "5\n15"
    },
    {
      "test_id": "ex10_3",
      "input": "10",
      "expected": "2\n1\n",
      "output": "2\n1"
    }
  ],
  "clustering_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex10_0:relation": "whitespace",
    "stdout:ex10_0:edit_band": "medium",
    "stdout:ex10_1:relation": "whitespace",
    "stdout:ex10_1:edit_band": "medium",
    "stdout:ex10_2:relation": "whitespace",
    "stdout:ex10_2:edit_band": "medium",
    "stdout:ex10_3:relation": "whitespace",
    "stdout:ex10_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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

int main (){

    int N, digito, contador_digitos=0, soma_digitos=0;
    scanf("%d", &N);

    while (N > 0){
        digito = N % 10;          
        soma_digitos += digito;
        contador_digitos ++;
        N = N/10;
    }    
    printf("%d \n %d", contador_digitos, soma_digitos);
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
  "source_sha256": "f2d087f02cba26bfe65bf40a29032109869ffd18558db9fc3097ff2a66d7dc34",
  "outcomes": {
    "ex10_0": "fail",
    "ex10_1": "fail",
    "ex10_2": "fail",
    "ex10_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex10_0",
      "input": "12",
      "expected": "2\n3\n",
      "output": "2 \n 3"
    },
    {
      "test_id": "ex10_1",
      "input": "123",
      "expected": "3\n6\n",
      "output": "3 \n 6"
    },
    {
      "test_id": "ex10_2",
      "input": "12345",
      "expected": "5\n15\n",
      "output": "5 \n 15"
    },
    {
      "test_id": "ex10_3",
      "input": "10",
      "expected": "2\n1\n",
      "output": "2 \n 1"
    }
  ],
  "clustering_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex10_0:relation": "whitespace",
    "stdout:ex10_0:edit_band": "medium",
    "stdout:ex10_1:relation": "whitespace",
    "stdout:ex10_1:edit_band": "medium",
    "stdout:ex10_2:relation": "whitespace",
    "stdout:ex10_2:edit_band": "medium",
    "stdout:ex10_3:relation": "whitespace",
    "stdout:ex10_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
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


## sample_006 — train

```c

#include <stdio.h>

int main()
{
    int N, digitos = 0, soma = 0;

    scanf("%d", &N);

    while (N)
    {
        soma = soma + (N % 10);
        digitos++;
        N = N / 10;
    }


    printf("%d\n%d", digitos, soma);
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
  "source_sha256": "43f2340082d31a9d65380d740ebf99e65f9058959aee907725a11c233e64db27",
  "outcomes": {
    "ex10_0": "fail",
    "ex10_1": "fail",
    "ex10_2": "fail",
    "ex10_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex10_0",
      "input": "12",
      "expected": "2\n3\n",
      "output": "2\n3"
    },
    {
      "test_id": "ex10_1",
      "input": "123",
      "expected": "3\n6\n",
      "output": "3\n6"
    },
    {
      "test_id": "ex10_2",
      "input": "12345",
      "expected": "5\n15\n",
      "output": "5\n15"
    },
    {
      "test_id": "ex10_3",
      "input": "10",
      "expected": "2\n1\n",
      "output": "2\n1"
    }
  ],
  "clustering_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex10_0:relation": "whitespace",
    "stdout:ex10_0:edit_band": "medium",
    "stdout:ex10_1:relation": "whitespace",
    "stdout:ex10_1:edit_band": "medium",
    "stdout:ex10_2:relation": "whitespace",
    "stdout:ex10_2:edit_band": "medium",
    "stdout:ex10_3:relation": "whitespace",
    "stdout:ex10_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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

int main()
{
    int N, digitos = 0, soma = 0;

    scanf("%d", &N);

    while (N)
    {
        soma = soma + (N % 10);
        digitos++;
        N = N / 10;
    }


    printf("%d\n\n%d", digitos, soma);
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
  "source_sha256": "a9c7b211047a771d82e01583c8e57a7a110aa5b94b4c20c1aac4e8ea937b6e31",
  "outcomes": {
    "ex10_0": "fail",
    "ex10_1": "fail",
    "ex10_2": "fail",
    "ex10_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex10_0",
      "input": "12",
      "expected": "2\n3\n",
      "output": "2\n\n3"
    },
    {
      "test_id": "ex10_1",
      "input": "123",
      "expected": "3\n6\n",
      "output": "3\n\n6"
    },
    {
      "test_id": "ex10_2",
      "input": "12345",
      "expected": "5\n15\n",
      "output": "5\n\n15"
    },
    {
      "test_id": "ex10_3",
      "input": "10",
      "expected": "2\n1\n",
      "output": "2\n\n1"
    }
  ],
  "clustering_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex10_0:relation": "whitespace",
    "stdout:ex10_0:edit_band": "medium",
    "stdout:ex10_1:relation": "whitespace",
    "stdout:ex10_1:edit_band": "medium",
    "stdout:ex10_2:relation": "whitespace",
    "stdout:ex10_2:edit_band": "medium",
    "stdout:ex10_3:relation": "whitespace",
    "stdout:ex10_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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

int main(){
    int N;
    int s;
    int temp;
    int counter = 0;
    scanf("%d", &N);

    while(N != 0){
        counter++;
        temp = N%10;
        s += temp; 
        N = N/10;
    }

    printf("%d\n%d", counter, s);
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
  "source_sha256": "812c890b8a48fc7c593baf53cc80ff021af89be303b68cc960514f7e0099af17",
  "outcomes": {
    "ex10_0": "fail",
    "ex10_1": "fail",
    "ex10_2": "fail",
    "ex10_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex10_0",
      "input": "12",
      "expected": "2\n3\n",
      "output": "2\n3"
    },
    {
      "test_id": "ex10_1",
      "input": "123",
      "expected": "3\n6\n",
      "output": "3\n6"
    },
    {
      "test_id": "ex10_2",
      "input": "12345",
      "expected": "5\n15\n",
      "output": "5\n15"
    },
    {
      "test_id": "ex10_3",
      "input": "10",
      "expected": "2\n1\n",
      "output": "2\n1"
    }
  ],
  "clustering_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex10_0:relation": "whitespace",
    "stdout:ex10_0:edit_band": "medium",
    "stdout:ex10_1:relation": "whitespace",
    "stdout:ex10_1:edit_band": "medium",
    "stdout:ex10_2:relation": "whitespace",
    "stdout:ex10_2:edit_band": "medium",
    "stdout:ex10_3:relation": "whitespace",
    "stdout:ex10_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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

int main(){

    int N, soma = 0, ndigitos = 0, digito;

    scanf("%d",&N);

    while(N != 0){ 
        digito = N % 10; 
        N = N / 10; 
        soma += digito; 
        ndigitos ++;
    }

    printf("%d\n%d", ndigitos, soma);
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
  "source_sha256": "3373f68b80ecd641e552835caa35f43c448fed6538958527fcadf18ebc4f0bc5",
  "outcomes": {
    "ex10_0": "fail",
    "ex10_1": "fail",
    "ex10_2": "fail",
    "ex10_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex10_0",
      "input": "12",
      "expected": "2\n3\n",
      "output": "2\n3"
    },
    {
      "test_id": "ex10_1",
      "input": "123",
      "expected": "3\n6\n",
      "output": "3\n6"
    },
    {
      "test_id": "ex10_2",
      "input": "12345",
      "expected": "5\n15\n",
      "output": "5\n15"
    },
    {
      "test_id": "ex10_3",
      "input": "10",
      "expected": "2\n1\n",
      "output": "2\n1"
    }
  ],
  "clustering_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex10_0:relation": "whitespace",
    "stdout:ex10_0:edit_band": "medium",
    "stdout:ex10_1:relation": "whitespace",
    "stdout:ex10_1:edit_band": "medium",
    "stdout:ex10_2:relation": "whitespace",
    "stdout:ex10_2:edit_band": "medium",
    "stdout:ex10_3:relation": "whitespace",
    "stdout:ex10_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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

int main(){
    int num, soma;
    int contador = 0, dig;

    scanf("%d",&num);
    dig = num % 10;
    num = num / 10;

    while (dig != 0){
        contador++;
        soma += dig;

        dig = num % 10;
        num = num / 10;
    } 
    printf("%d\n%d",contador,soma);

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
  "source_sha256": "37bb60d0f8cb070e851335981b40fe086e3fff9345c52526512023caebeda9d5",
  "outcomes": {
    "ex10_0": "fail",
    "ex10_1": "fail",
    "ex10_2": "fail",
    "ex10_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex10_0",
      "input": "12",
      "expected": "2\n3\n",
      "output": "2\n3"
    },
    {
      "test_id": "ex10_1",
      "input": "123",
      "expected": "3\n6\n",
      "output": "3\n6"
    },
    {
      "test_id": "ex10_2",
      "input": "12345",
      "expected": "5\n15\n",
      "output": "5\n15"
    },
    {
      "test_id": "ex10_3",
      "input": "10",
      "expected": "2\n1\n",
      "output": "0\n0"
    }
  ],
  "clustering_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex10_0:relation": "whitespace",
    "stdout:ex10_0:edit_band": "medium",
    "stdout:ex10_1:relation": "whitespace",
    "stdout:ex10_1:edit_band": "medium",
    "stdout:ex10_2:relation": "whitespace",
    "stdout:ex10_2:edit_band": "medium",
    "stdout:ex10_3:relation": "different",
    "stdout:ex10_3:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
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

int main(){
    int n, soma= 0, cont= 0;
    scanf("%d", &n);
    while (n > 0){
        soma += n % 10;
        cont++; 
        n = n/10;  
    }
    printf ("%d\n%d", cont, soma);
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
  "source_sha256": "3031fdb298f5620ff7b38a5d626661db00c1ff2e325eb508231d4572b5f10957",
  "outcomes": {
    "ex10_0": "fail",
    "ex10_1": "fail",
    "ex10_2": "fail",
    "ex10_3": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex10_0",
      "input": "12",
      "expected": "2\n3\n",
      "output": "2\n3"
    },
    {
      "test_id": "ex10_1",
      "input": "123",
      "expected": "3\n6\n",
      "output": "3\n6"
    },
    {
      "test_id": "ex10_2",
      "input": "12345",
      "expected": "5\n15\n",
      "output": "5\n15"
    },
    {
      "test_id": "ex10_3",
      "input": "10",
      "expected": "2\n1\n",
      "output": "2\n1"
    }
  ],
  "clustering_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex10_0:relation": "whitespace",
    "stdout:ex10_0:edit_band": "medium",
    "stdout:ex10_1:relation": "whitespace",
    "stdout:ex10_1:edit_band": "medium",
    "stdout:ex10_2:relation": "whitespace",
    "stdout:ex10_2:edit_band": "medium",
    "stdout:ex10_3:relation": "whitespace",
    "stdout:ex10_3:edit_band": "medium"
  },
  "diagnostic_oav": {
    "test:ex10_0": "fail",
    "test:ex10_1": "fail",
    "test:ex10_2": "fail",
    "test:ex10_3": "fail",
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


## Evidence refs hợp lệ

```json
[
  "test_statistics",
  "feature_statistics",
  "learned_if_then_rules",
  "semantic_findings",
  "problem_statement",
  "members/sample_001/raw_code",
  "members/sample_001/tests/ex10_0",
  "members/sample_001/tests/ex10_1",
  "members/sample_001/tests/ex10_2",
  "members/sample_001/tests/ex10_3",
  "members/sample_002/raw_code",
  "members/sample_002/tests/ex10_0",
  "members/sample_002/tests/ex10_1",
  "members/sample_002/tests/ex10_2",
  "members/sample_002/tests/ex10_3",
  "members/sample_003/raw_code",
  "members/sample_003/tests/ex10_0",
  "members/sample_003/tests/ex10_1",
  "members/sample_003/tests/ex10_2",
  "members/sample_003/tests/ex10_3",
  "members/sample_004/raw_code",
  "members/sample_004/tests/ex10_0",
  "members/sample_004/tests/ex10_1",
  "members/sample_004/tests/ex10_2",
  "members/sample_004/tests/ex10_3",
  "members/sample_005/raw_code",
  "members/sample_005/tests/ex10_0",
  "members/sample_005/tests/ex10_1",
  "members/sample_005/tests/ex10_2",
  "members/sample_005/tests/ex10_3",
  "members/sample_006/raw_code",
  "members/sample_006/tests/ex10_0",
  "members/sample_006/tests/ex10_1",
  "members/sample_006/tests/ex10_2",
  "members/sample_006/tests/ex10_3",
  "members/sample_007/raw_code",
  "members/sample_007/tests/ex10_0",
  "members/sample_007/tests/ex10_1",
  "members/sample_007/tests/ex10_2",
  "members/sample_007/tests/ex10_3",
  "members/sample_008/raw_code",
  "members/sample_008/tests/ex10_0",
  "members/sample_008/tests/ex10_1",
  "members/sample_008/tests/ex10_2",
  "members/sample_008/tests/ex10_3",
  "members/sample_009/raw_code",
  "members/sample_009/tests/ex10_0",
  "members/sample_009/tests/ex10_1",
  "members/sample_009/tests/ex10_2",
  "members/sample_009/tests/ex10_3",
  "members/sample_010/raw_code",
  "members/sample_010/tests/ex10_0",
  "members/sample_010/tests/ex10_1",
  "members/sample_010/tests/ex10_2",
  "members/sample_010/tests/ex10_3",
  "members/sample_011/raw_code",
  "members/sample_011/tests/ex10_0",
  "members/sample_011/tests/ex10_1",
  "members/sample_011/tests/ex10_2",
  "members/sample_011/tests/ex10_3"
]
```
