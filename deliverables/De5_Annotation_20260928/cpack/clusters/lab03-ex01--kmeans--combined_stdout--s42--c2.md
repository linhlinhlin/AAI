# lab03-ex01--kmeans--combined_stdout--s42--c2

Packet: `793b1b1e8bceeded702464b78ac2317269044d0d5080359747466c1029d5e0fb`


Trạng thái: **pending_annotation**. Chưa có gold hay xác nhận misconception.


Số bài: 37; phân vùng: {'train': 29, 'validation': 8}.


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
    "test_id": "ex01_1",
    "n_cluster": 37,
    "n_observed": 37,
    "n_failed": 37,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 37
    }
  },
  {
    "test_id": "ex01_2",
    "n_cluster": 37,
    "n_observed": 37,
    "n_failed": 37,
    "n_not_run": 0,
    "failure_rate_observed": 1.0,
    "failure_rate_cluster": 1.0,
    "outcome_counts": {
      "fail": 37
    }
  },
  {
    "test_id": "ex01_0",
    "n_cluster": 37,
    "n_observed": 37,
    "n_failed": 36,
    "n_not_run": 0,
    "failure_rate_observed": 0.972972972972973,
    "failure_rate_cluster": 0.972972972972973,
    "outcome_counts": {
      "fail": 36,
      "pass": 1
    }
  }
]
```


## OAV nổi bật

```json
[
  {
    "feature": "stdout:ex01_1:relation",
    "value": "different",
    "n": 33,
    "n_cluster": 37,
    "rate": 0.8918918918918919,
    "cohort_rate": 0.2426470588235294,
    "difference_from_cohort": 0.6492448330683624
  },
  {
    "feature": "stdout:ex01_2:relation",
    "value": "different",
    "n": 33,
    "n_cluster": 37,
    "rate": 0.8918918918918919,
    "cohort_rate": 0.2426470588235294,
    "difference_from_cohort": 0.6492448330683624
  },
  {
    "feature": "stdout:ex01_0:relation",
    "value": "different",
    "n": 31,
    "n_cluster": 37,
    "rate": 0.8378378378378378,
    "cohort_rate": 0.22794117647058823,
    "difference_from_cohort": 0.6098966613672496
  },
  {
    "feature": "stdout:ex01_0:edit_band",
    "value": "large",
    "n": 22,
    "n_cluster": 37,
    "rate": 0.5945945945945946,
    "cohort_rate": 0.16911764705882354,
    "difference_from_cohort": 0.4254769475357711
  },
  {
    "feature": "stdout:ex01_1:edit_band",
    "value": "medium",
    "n": 20,
    "n_cluster": 37,
    "rate": 0.5405405405405406,
    "cohort_rate": 0.19117647058823528,
    "difference_from_cohort": 0.3493640699523053
  },
  {
    "feature": "stdout:ex01_1:edit_band",
    "value": "large",
    "n": 16,
    "n_cluster": 37,
    "rate": 0.43243243243243246,
    "cohort_rate": 0.13970588235294118,
    "difference_from_cohort": 0.2927265500794913
  },
  {
    "feature": "stdout:ex01_2:edit_band",
    "value": "large",
    "n": 14,
    "n_cluster": 37,
    "rate": 0.3783783783783784,
    "cohort_rate": 0.11029411764705882,
    "difference_from_cohort": 0.2680842607313196
  },
  {
    "feature": "stdout:ex01_2:edit_band",
    "value": "medium",
    "n": 15,
    "n_cluster": 37,
    "rate": 0.40540540540540543,
    "cohort_rate": 0.16176470588235295,
    "difference_from_cohort": 0.24364069952305248
  },
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 25,
    "n_cluster": 37,
    "rate": 0.6756756756756757,
    "cohort_rate": 0.47794117647058826,
    "difference_from_cohort": 0.1977344992050874
  },
  {
    "feature": "stdout:ex01_0:edit_band",
    "value": "medium",
    "n": 13,
    "n_cluster": 37,
    "rate": 0.35135135135135137,
    "cohort_rate": 0.19852941176470587,
    "difference_from_cohort": 0.1528219395866455
  },
  {
    "feature": "ast:c_while",
    "value": "1",
    "n": 18,
    "n_cluster": 37,
    "rate": 0.4864864864864865,
    "cohort_rate": 0.3382352941176471,
    "difference_from_cohort": 0.14825119236883944
  },
  {
    "feature": "stdout:ex01_0:relation",
    "value": "empty",
    "n": 5,
    "n_cluster": 37,
    "rate": 0.13513513513513514,
    "cohort_rate": 0.03676470588235294,
    "difference_from_cohort": 0.0983704292527822
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "0",
    "n": 10,
    "n_cluster": 37,
    "rate": 0.2702702702702703,
    "cohort_rate": 0.17647058823529413,
    "difference_from_cohort": 0.09379968203497616
  },
  {
    "feature": "ast:c_for",
    "value": "0",
    "n": 7,
    "n_cluster": 37,
    "rate": 0.1891891891891892,
    "cohort_rate": 0.11029411764705882,
    "difference_from_cohort": 0.07889507154213038
  },
  {
    "feature": "ast:c_address_of",
    "value": "0",
    "n": 4,
    "n_cluster": 37,
    "rate": 0.10810810810810811,
    "cohort_rate": 0.029411764705882353,
    "difference_from_cohort": 0.07869634340222575
  },
  {
    "feature": "stdout:ex01_1:relation",
    "value": "empty",
    "n": 4,
    "n_cluster": 37,
    "rate": 0.10810810810810811,
    "cohort_rate": 0.029411764705882353,
    "difference_from_cohort": 0.07869634340222575
  },
  {
    "feature": "stdout:ex01_2:relation",
    "value": "empty",
    "n": 4,
    "n_cluster": 37,
    "rate": 0.10810810810810811,
    "cohort_rate": 0.029411764705882353,
    "difference_from_cohort": 0.07869634340222575
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "0",
    "n": 10,
    "n_cluster": 37,
    "rate": 0.2702702702702703,
    "cohort_rate": 0.21323529411764705,
    "difference_from_cohort": 0.057034976152623235
  },
  {
    "feature": "ast:c_update",
    "value": "0",
    "n": 3,
    "n_cluster": 37,
    "rate": 0.08108108108108109,
    "cohort_rate": 0.029411764705882353,
    "difference_from_cohort": 0.05166931637519873
  },
  {
    "feature": "stdout:ex01_0:edit_band",
    "value": "__unknown__",
    "n": 1,
    "n_cluster": 37,
    "rate": 0.02702702702702703,
    "cohort_rate": 0.007352941176470588,
    "difference_from_cohort": 0.01967408585055644
  }
]
```


## AST chung (chỉ là pattern cấu trúc)

```json
[
  {
    "feature": "ast:c_if",
    "value": "1",
    "n": 25,
    "n_cluster": 37,
    "rate": 0.6756756756756757,
    "cohort_rate": 0.47794117647058826,
    "difference_from_cohort": 0.1977344992050874
  },
  {
    "feature": "ast:c_return",
    "value": "1",
    "n": 37,
    "n_cluster": 37,
    "rate": 1.0,
    "cohort_rate": 1.0,
    "difference_from_cohort": 0.0
  },
  {
    "feature": "ast:c_update",
    "value": "1",
    "n": 34,
    "n_cluster": 37,
    "rate": 0.918918918918919,
    "cohort_rate": 0.9705882352941176,
    "difference_from_cohort": -0.05166931637519867
  },
  {
    "feature": "ast:c_strict_comparison",
    "value": "1",
    "n": 27,
    "n_cluster": 37,
    "rate": 0.7297297297297297,
    "cohort_rate": 0.7867647058823529,
    "difference_from_cohort": -0.05703497615262321
  },
  {
    "feature": "ast:c_address_of",
    "value": "1",
    "n": 33,
    "n_cluster": 37,
    "rate": 0.8918918918918919,
    "cohort_rate": 0.9705882352941176,
    "difference_from_cohort": -0.07869634340222575
  },
  {
    "feature": "ast:c_for",
    "value": "1",
    "n": 30,
    "n_cluster": 37,
    "rate": 0.8108108108108109,
    "cohort_rate": 0.8897058823529411,
    "difference_from_cohort": -0.07889507154213027
  },
  {
    "feature": "ast:c_inclusive_comparison",
    "value": "1",
    "n": 27,
    "n_cluster": 37,
    "rate": 0.7297297297297297,
    "cohort_rate": 0.8235294117647058,
    "difference_from_cohort": -0.09379968203497613
  }
]
```


## IF–THEN dự đoán cluster, không dự đoán gold

```json
[
  {
    "rule_id": 2,
    "if": [
      "NOT (stdout:ex01_1:edit_band=small)",
      "NOT (stdout:ex01_2:relation=whitespace)"
    ],
    "then_cluster": 2,
    "train_support": 28,
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
  "reasoning": "Có 37 bài trong cụm. Chưa xác định được cơ chế chung; cần đối chiếu từng bài.",
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

sample_031, sample_002, sample_017, sample_035

## sample_002 — train — đại diện

```c
#include <stdio.h>




int main ()
{
    char c;
    int state = 0;
    c = getchar();
    while (c != EOF)
    {
        if (c == ' ' || c == '\n')
        {
            if (state == 0)
                putchar('0');
            state = 0;
        }
        else if (state == 0)
        {
            if (c == '0')
                continue;
            state = 1;
        }
        putchar(c);
        c = getchar();
    }
    if (state == 0)
        putchar('0');
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
  "source_sha256": "8b7adcd66669376a5f3402906122501030a033fc875113ac838fdf0369140047",
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
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "4"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "8"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
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


## sample_017 — validation — đại diện

```c

#include <stdio.h>

int main()
{
    int numero;
    int colunas=0; 
    int linhas=0;
    int variavel;
    scanf("%d", &numero);

    while (linhas<numero)
    {
        while (colunas<numero)
        {
            printf("%d\t",variavel++);
            ++colunas;
        }
    ++linhas;
    ++variavel;
    printf("\n");
    }
    return 0;
}

```

```json
{
  "sample_id": "sample_017",
  "partition": "validation",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "7928842aef98a948df78edebfbc2ebd4fab4f9ce1ede1268d98ff424da7c27c9",
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
      "output": "32765\t32766\t32767\t\n\n\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "32767\t32768\t32769\t32770\t\n\n\n\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "32764\t32765\t32766\t32767\t32768\t32769\t32770\t32771\t\n\n\n\n\n\n\n\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
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


## sample_031 — train — đại diện

```c

#include <stdio.h>

void quadrado(int N){
    int linha, coluna;
    if (N < 2){
        printf("Digite um número maior que 2\n");
        return;
    }
    for (linha = 0; linha < N; linha++){
        for (coluna = linha + 1; coluna <= (N + linha); coluna++){
            printf("%d\t", coluna);
        }
        printf("\n");
    }
}

int main(){
    int N;

    printf("Digite um número maior que 2:\n");
    scanf("%d", &N);

    quadrado(N);

    return 0;
}
```

```json
{
  "sample_id": "sample_031",
  "partition": "train",
  "representative": true,
  "is_train_medoid": true,
  "raw_code_truncated": false,
  "source_sha256": "9d07962a54c4f59bab1d154a5d2bf627cb1131050d2185b8f7883955d2d6f146",
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
      "output": "Digite um número maior que 2:\n1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "Digite um número maior que 2:\n1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "Digite um número maior que 2:\n1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
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
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
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
    "ast:c_update": "1",
    "ast:c_return": "1",
    "ast:parse": "ok",
    "is_hardcoded_output": false
  }
}
```


## sample_035 — train — đại diện

```c


#include <stdio.h>

void quadrado(int N) {
    int n2, starter = 1, starter2 = 1, n3;
    n2 = N;
    n3 = N;
    if (N >= 2) {
        while (N > 0) {
            starter = starter2;
            while (n2-- > 0) {
                printf("%d\t", starter);
                starter ++;
                n2--;
            }
            printf("%d", starter);
            printf("\n");
            starter2 ++;
            N--;
            n2 = n3;
        }
    }

}

int main () {
    int N;
    scanf("%d", &N);
    quadrado(N);
    return 0;
}


```

```json
{
  "sample_id": "sample_035",
  "partition": "train",
  "representative": true,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "4ad2c7e41352d5e740d8b3e7fab9fa20b08c350036b6bfa5b11b0eed5bb3f1fe",
  "outcomes": {
    "ex01_0": "pass",
    "ex01_1": "fail",
    "ex01_2": "fail"
  },
  "logged_tests": [
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\n2\t3\t4\n3\t4\t5\n4\t5\t6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\n2\t3\t4\t5\t6\n3\t4\t5\t6\t7\n4\t5\t6\t7\t8\n5\t6\t7\t8\t9\n6\t7\t8\t9\t10\n7\t8\t9\t10\t11\n8\t9\t10\t11\t12\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "pass",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "__unknown__",
    "stdout:ex01_0:edit_band": "__unknown__",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "large"
  },
  "diagnostic_oav": {
    "test:ex01_0": "pass",
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


## sample_001 — train

```c
#include <stdio.h>

#define LINHA_INICIAL 1
#define COLUNA_INICIAL 1
#define NUM_INICIAL 1
#define PASSO_HORIZONTAL 1
#define PASSO_VERTICAL 1

void quadrado(int n)
{
	int linha, coluna;
	int num = NUM_INICIAL;

	for (linha = LINHA_INICIAL; linha < n; linha++) 
	{
		for (coluna = COLUNA_INICIAL; coluna < n; coluna++)
		{
			printf("%d\t", num);
			num += PASSO_HORIZONTAL;
		}
		printf("%d\n", num);
		num = NUM_INICIAL + PASSO_VERTICAL*linha;
	}
}

int main()
{
	int n;
	scanf("%d", &n);
	quadrado(n);
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
  "source_sha256": "1d2a60e4e5b6633b9723e64cf0db25b32ed9d8c879131d4e6a491a81b69960f7",
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
      "output": "1\t2\t3\n2\t3\t4\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n"
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
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "different",
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


## sample_003 — validation

```c
#include <stdio.h>

int main()
{
    char c, previous_char;
    int state = 0;
    c = getchar();
    while (c != EOF)
    {
        
        if (c == '\n' || c == ' ') {
            if (state == 0 && previous_char == '0') {
                putchar(previous_char);
            }
            putchar(c);
            state = 0;
        }
        else if (c != '0') {
            state = 1;
            putchar(c);
        }
        else if (c == '0' && state == 1){
            putchar(c);
        }
        previous_char = c;
        c = getchar();
    }
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
  "source_sha256": "7932b1b5e49d55047a075f935d0659d690c83d6be9be9af4b83cf091f9d171c7",
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
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "4"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "8"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
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


## sample_004 — validation

```c
#include <stdio.h>

int main()
{
    char c, previous_char;
    int state = 0;
    c = getchar();
    while (c != EOF)
    {
        
        if (c == '\n' || c == ' ') {
            if (state == 0 && previous_char == '0') {
                printf("yes");
                putchar(previous_char);
            }
            putchar(c);
            state = 0;
        }
        else if (c != '0') {
            state = 1;
            putchar(c);
        }
        else if (c == '0' && state == 1){
            putchar(c);
        }
        previous_char = c;
        c = getchar();
    }
    if (previous_char == '0' && state == 0) {
        putchar('0');
        
    }
    return 0; 
}
```

```json
{
  "sample_id": "sample_004",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "0a8a886674ae35ceacc0deceacce052ec2236518c63e255b8674fea5c11016c6",
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
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "4"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "8"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "0",
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


## sample_005 — train

```c
#include <stdio.h>
void quadrado(int N)
{
    int N1 = 1, cont;
    for (cont = 1; cont <= N; cont++)
    {
        for (N1 = cont; N1 <= (N - 1 + cont); N1++)
        {
            printf("%d\t", N1);
        }
        printf("\b\n");
    }
}
int main()
{
    int N;
    scanf("%d", &N);
    quadrado(N);
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
  "source_sha256": "29ae272c4317bffcfc9a82402178c3c25d8659a70f3d3e43d49dd7b09a11a160",
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
      "output": "1\t2\t3\t\b\n2\t3\t4\t\b\n3\t4\t5\t\b\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\b\n2\t3\t4\t5\t\b\n3\t4\t5\t6\t\b\n4\t5\t6\t7\t\b\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\b\n2\t3\t4\t5\t6\t7\t8\t9\t\b\n3\t4\t5\t6\t7\t8\t9\t10\t\b\n4\t5\t6\t7\t8\t9\t10\t11\t\b\n5\t6\t7\t8\t9\t10\t11\t12\t\b\n6\t7\t8\t9\t10\t11\t12\t13\t\b\n7\t8\t9\t10\t11\t12\t13\t14\t\b\n8\t9\t10\t11\t12\t13\t14\t15\t\b\n"
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
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "different",
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


## sample_006 — train

```c
#include <stdio.h>

void quadrado(int N) {
    int i, j;
    for (i = 1;i <= N;i++) {
        for (j = i; j < N + i;j++){
            if (j == i)
                printf ("%d",j);
            else
                printf("\t%d",j);
        }
        printf("\n");
    }   
}


int main(){
    int N = 0;
    while (N<2) {
        printf("qual é o tamanho do quadrado? (>= 2): ");
        scanf("%d",&N);
    }
    quadrado(N);
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
  "source_sha256": "677dfe5001f3e58e2dd7dfeb720f321c2861410ba777dcb095d788a977f74307",
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
      "output": "qual é o tamanho do quadrado? (>= 2): 1\t2\t3\n2\t3\t4\n3\t4\t5\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "qual é o tamanho do quadrado? (>= 2): 1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "qual é o tamanho do quadrado? (>= 2): 1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n"
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
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
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

void quadrado(int N) {
    int i, j;
    for (i = 1;i <= N;i++) {
        for (j = i; j < N + i - 1;j++){
            if (j == i)
                printf ("%d",j);
            else
                printf("\t%d",j);
        }
        printf("\n");
    }   
}


int main(){
    int N = 0;
    while (N<2) {
        printf("qual é o tamanho do quadrado? (>= 2): ");
        scanf("%d",&N);
    }
    quadrado(N);
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
  "source_sha256": "1b000f135c1032fb2d14bad7d266d61051f21866af5a1ec2f2fe279d98db717b",
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
      "output": "qual é o tamanho do quadrado? (>= 2): 1\t2\n2\t3\n3\t4\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "qual é o tamanho do quadrado? (>= 2): 1\t2\t3\n2\t3\t4\n3\t4\t5\n4\t5\t6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "qual é o tamanho do quadrado? (>= 2): 1\t2\t3\t4\t5\t6\t7\n2\t3\t4\t5\t6\t7\t8\n3\t4\t5\t6\t7\t8\t9\n4\t5\t6\t7\t8\t9\t10\n5\t6\t7\t8\t9\t10\t11\n6\t7\t8\t9\t10\t11\t12\n7\t8\t9\t10\t11\t12\t13\n8\t9\t10\t11\t12\t13\t14\n"
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
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "different",
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

void quadrado(int N) {
    int i, j;
    for (i = 1;i <= N;i++) {
        for (j = i; j < N + i - 1;j++) 
            printf ("%d\t",j);
        printf("%d\n",j++);
    }   
}


int main(){
    int N = 0;
    while (N<2) {
        printf("qual é o tamanho do quadrado? (>= 2): ");
        scanf("%d",&N);
    }
    quadrado(N);
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
  "source_sha256": "9c1ff308eb9511ba4ed3a129c6b225a65dda2c86a0f0237dee47cc9690d59cfb",
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
      "output": "qual é o tamanho do quadrado? (>= 2): 1\t2\t3\n2\t3\t4\n3\t4\t5\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "qual é o tamanho do quadrado? (>= 2): 1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "qual é o tamanho do quadrado? (>= 2): 1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n"
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
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
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


## sample_009 — train

```c
#include <stdio.h>

void quadrado(int N) {
    int i, j;
    for (i = 1;i <= N;i++) {
        for (j = i; j < N + i;j++) 
            printf ("%d\t",j);
        printf("\n");
    }   
}


int main(){
    int N = 0;
    while (N<2) {
        printf("qual é o tamanho do quadrado? (>= 2): ");
        scanf("%d",&N);
    }
    quadrado(N);
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
  "source_sha256": "2ac195394a187b7a30472631b1c817cfe0f4c52315e49b39df396c9efcaea748",
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
      "output": "qual é o tamanho do quadrado? (>= 2): 1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "qual é o tamanho do quadrado? (>= 2): 1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "qual é o tamanho do quadrado? (>= 2): 1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
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
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
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


## sample_010 — train

```c


#include <stdio.h>
# define FORA 0
# define NUMERO   1
# define ZERO  2

void quadrado(int N){
    
    int linha,coluna,soma;
    soma = 0;
    
    if (N>=2) {
    
        for (coluna=1; coluna<=N; coluna++) {
            for (linha=1; linha<=N; linha++) {
                printf("%d\t",linha+soma);
            }
            putchar('\n');
            soma++;
        }
    }
}

void piramide(int N){
    
    char espaco = ' ';
    int num_char,space_linha,andares,num_por_linha,cont,aux;
    
    num_char = N*4-3;
    
    for (andares=1; andares<=N; andares++) {
        
        num_por_linha= andares*2-1;
        space_linha = (num_char-num_por_linha-(andares*2-2))/2;
        cont = aux = 1;
        
        while (num_por_linha!=0 ) {
            
            
            if (space_linha!=0) {
                printf("%c",espaco);
                space_linha--;
            }
            else if (num_por_linha!=0){
                if (cont<=andares) {
                    printf("%d%c",cont,espaco);
                    num_por_linha--;
                    cont++;
                    aux = cont-1;
                }
                else{
                    aux--;
                    printf("%d%c",aux,espaco);
                    num_por_linha--;
                }
            }
        }
        printf("\n");
    }
}



int main(){
    int estado;
    int c;
    
    estado = FORA;
    while ((c=getchar())!=EOF) {
    
        if (estado==FORA && (c>'0'&& c<='9')) {
            putchar(c);
            estado=NUMERO;
        }
        else if (estado==NUMERO && (c==' '||c=='\n')){
            putchar(c);
            estado=FORA;
        }
        else if(estado==FORA && c=='0'){
            estado=ZERO;
        }
        else if (estado==ZERO && (c==' '|| c=='\n')){
            estado=FORA;
            printf("0%c",c);
        }
        else if (estado==ZERO && (c>'0'&& c<='9')){
            putchar(c);
            estado=NUMERO;
        }
        else if (estado==NUMERO || estado==FORA)
            putchar(c);
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
  "source_sha256": "49be348f0f5b51e3366be67ec746bea5f9f3952f71bf7e253e7efe8c12c37fa2",
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
      "output": "3"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "4"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "8"
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
    "ast:c_address_of": "0",
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
    "ast:c_address_of": "0",
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

void quadrado (int N) {
    int  i, z;
  
    if (N >= 2) {
  
        for (i = 1; i<=N; i++) {
            for (z = i; z < i+N; z++)
                printf("%d\t", z);
            printf("\n");
        }
    }
    return;
}


int main () {
    int N;
    printf("Hello\n");
    scanf("%d",&N);
   
    quadrado(N);
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
  "source_sha256": "497c3118afacd23c3795f05fe2c6089c6f7e7d7fe2effbb040fe8827435b20d9",
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
      "output": "Hello\n1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "Hello\n1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n4\t5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "Hello\n1\t2\t3\t4\t5\t6\t7\t8\t\n2\t3\t4\t5\t6\t7\t8\t9\t\n3\t4\t5\t6\t7\t8\t9\t10\t\n4\t5\t6\t7\t8\t9\t10\t11\t\n5\t6\t7\t8\t9\t10\t11\t12\t\n6\t7\t8\t9\t10\t11\t12\t13\t\n7\t8\t9\t10\t11\t12\t13\t14\t\n8\t9\t10\t11\t12\t13\t14\t15\t\n"
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
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "small"
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


## sample_012 — validation

```c


#include <stdio.h>

void quadrado(int n){
    int i, j, estado = 1;
    for (j = 0; n > j; j++){
        for (i = 0; n > i; i++){
            if (i)
                printf("%d", i + estado);
            printf("%d\t", i + estado);
        }
        estado ++;
        putchar('\n');
    }
}

int main(){
    int n;
    scanf("%d",&n);
    quadrado(n);
    return 0;
}
```

```json
{
  "sample_id": "sample_012",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "24b24b39e2169c0c7d042912ff991f637664c6c35cda6906f7e52e110e9e78db",
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
      "output": "1\t22\t33\t\n2\t33\t44\t\n3\t44\t55\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t22\t33\t44\t\n2\t33\t44\t55\t\n3\t44\t55\t66\t\n4\t55\t66\t77\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t22\t33\t44\t55\t66\t77\t88\t\n2\t33\t44\t55\t66\t77\t88\t99\t\n3\t44\t55\t66\t77\t88\t99\t1010\t\n4\t55\t66\t77\t88\t99\t1010\t1111\t\n5\t66\t77\t88\t99\t1010\t1111\t1212\t\n6\t77\t88\t99\t1010\t1111\t1212\t1313\t\n7\t88\t99\t1010\t1111\t1212\t1313\t1414\t\n8\t99\t1010\t1111\t1212\t1313\t1414\t1515\t\n"
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
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
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


## sample_013 — validation

```c


#include <stdio.h>

void quadrado(int n){
    int i, j, estado = 0;
    for (j = 1; n >= j; j++){
        for (i = 1; n >= i; i++){
            if (i == n)
                printf("%d", i + estado);
            printf("%d\t", i + estado);
        }
        estado ++;
        putchar('\n');
    }
}

int main(){
    int n;
    scanf("%d",&n);
    quadrado(n);
    return 0;
}
```

```json
{
  "sample_id": "sample_013",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "68d782cd5afbc4079e4df6f03cd9d0d3acbb922a855ef55c8772361773197900",
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
      "output": "1\t2\t33\t\n2\t3\t44\t\n3\t4\t55\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t44\t\n2\t3\t4\t55\t\n3\t4\t5\t66\t\n4\t5\t6\t77\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t88\t\n2\t3\t4\t5\t6\t7\t8\t99\t\n3\t4\t5\t6\t7\t8\t9\t1010\t\n4\t5\t6\t7\t8\t9\t10\t1111\t\n5\t6\t7\t8\t9\t10\t11\t1212\t\n6\t7\t8\t9\t10\t11\t12\t1313\t\n7\t8\t9\t10\t11\t12\t13\t1414\t\n8\t9\t10\t11\t12\t13\t14\t1515\t\n"
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
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "small"
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


## sample_014 — validation

```c


#include <stdio.h>

void quadrado(int n){
    int i, j, estado = 1;
    for (j = 0; n > j; j++){
        for (i = 0; n > i; i++){
            if (i)
                printf("\t%d", i + estado);
            printf("%d", i + estado);
        }
        estado ++;
        putchar('\n');
    }
}

int main(){
    int n;
    scanf("%d",&n);
    quadrado(n);
    return 0;
}
```

```json
{
  "sample_id": "sample_014",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "b4e2957574e8983b879d4034a7a617c3899f75640a1cabe4a3ea01c9fae72948",
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
      "output": "1\t22\t33\n2\t33\t44\n3\t44\t55\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t22\t33\t44\n2\t33\t44\t55\n3\t44\t55\t66\n4\t55\t66\t77\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t22\t33\t44\t55\t66\t77\t88\n2\t33\t44\t55\t66\t77\t88\t99\n3\t44\t55\t66\t77\t88\t99\t1010\n4\t55\t66\t77\t88\t99\t1010\t1111\n5\t66\t77\t88\t99\t1010\t1111\t1212\n6\t77\t88\t99\t1010\t1111\t1212\t1313\n7\t88\t99\t1010\t1111\t1212\t1313\t1414\n8\t99\t1010\t1111\t1212\t1313\t1414\t1515\n"
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
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
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


## sample_015 — train

```c

#include <stdio.h>

void quadrado(int N) {
    int i;
    scanf("%d",&N);
    while (N<2) {
        scanf("%d",&N);
    }
    for(;N>0;N--){
        for(i=1;i<=N;i++) {
            printf("%d\t",i);
        }
        printf("\n");
    } 
}
int main (){
    void quadrado(int N);
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
  "source_sha256": "0b4b4d6d2de6f4c428fe461a7aadb57b292ebfabb3b583da428d80a3e33d33fe",
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
      "output": ""
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": ""
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": ""
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


## sample_016 — train

```c

#include <stdio.h>

void quadrado(int N)
{
    int i, j;
    
    for (i = 1; i <= N; i++)
    {
        for (j = i; j < N; j++)
        {
            printf("%d\t", j);
        }
        printf("%d\n", N + i - 1);
    }
}

int main()
{
    int N;
    while (N < 1)
    {
        scanf("%d", &N);
    }

    quadrado(N);

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
  "source_sha256": "d4a8fc73ec4295116e13acb3b4f2c0b1810dce0db6489a34eaf764563fbb86d5",
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
      "output": "1\t2\t3\n2\t4\n5\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\n2\t3\t5\n3\t6\n7\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t9\n3\t4\t5\t6\t7\t10\n4\t5\t6\t7\t11\n5\t6\t7\t12\n6\t7\t13\n7\t14\n15\n"
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


## sample_018 — validation

```c

#include <stdio.h>

int main()
{
    int numero;
    int colunas=0; 
    int linhas=0;
    int variavel;
    scanf("%d", &numero);

    while (linhas<numero)
    {
        while (colunas<numero)
        {
            printf("%d\t",variavel++);
            ++colunas;
        }
    ++linhas;
    ++variavel;
    printf("\n");
    }
    return 0;
}





```

```json
{
  "sample_id": "sample_018",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "b647668662a0419c003526a3affe293da84748884619d2e5310d6f178446bc63",
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
      "output": "32766\t32767\t32768\t\n\n\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "32767\t32768\t32769\t32770\t\n\n\n\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "32767\t32768\t32769\t32770\t32771\t32772\t32773\t32774\t\n\n\n\n\n\n\n\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
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


## sample_019 — train

```c


#include <stdio.h>

void quadrado(int N) {

    int i, j, v = 1; 

    for (i = 0; i < N; i++) {
        for (j = 1; j < N; j++) {
            printf("%d\t", v);
            v++;
        }
        printf("%d", v);
        v -= 3;
        printf("\n");
    }
}

int main () {
    
    int N;

    do {
        scanf("%d", &N);
    } while (N < 2);

    quadrado(N);
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
  "source_sha256": "3d58f6c319ddceba8c6489da15efb612ac6015d3b22b618d2bb5ae988cf0a166",
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
      "output": "1\t2\t3\n0\t1\t2\n-1\t0\t1\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\n1\t2\t3\t4\n1\t2\t3\t4\n1\t2\t3\t4\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\n5\t6\t7\t8\t9\t10\t11\t12\n9\t10\t11\t12\t13\t14\t15\t16\n13\t14\t15\t16\t17\t18\t19\t20\n17\t18\t19\t20\t21\t22\t23\t24\n21\t22\t23\t24\t25\t26\t27\t28\n25\t26\t27\t28\t29\t30\t31\t32\n29\t30\t31\t32\t33\t34\t35\t36\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "1",
    "ast:c_if": "0",
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
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
    "ast:c_for": "1",
    "ast:c_while": "0",
    "ast:c_do": "1",
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


## sample_020 — train

```c

#include <stdio.h>
void quadrado (int N) {
    int l, c;
    for(l = 1; l < N; l++){
        for (c = 1; c < N; c++){
            printf("%d\t", (1+l+c));
        }
        printf("\n"); 
    }
}
int main (){
    int N;
    scanf("%d", &N);
    if (N>=2){
        quadrado (N);
    }    
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
  "source_sha256": "83c809d2558394749aee0ae704d4f8fbc9d3980dfc304b9ed8651a62ac267766",
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
      "output": "3\t4\t\n4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "3\t4\t5\t\n4\t5\t6\t\n5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "3\t4\t5\t6\t7\t8\t9\t\n4\t5\t6\t7\t8\t9\t10\t\n5\t6\t7\t8\t9\t10\t11\t\n6\t7\t8\t9\t10\t11\t12\t\n7\t8\t9\t10\t11\t12\t13\t\n8\t9\t10\t11\t12\t13\t14\t\n9\t10\t11\t12\t13\t14\t15\t\n"
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
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
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
void quadrado (int N) {
    int i, j;
    while (N <= 1){
        scanf("%d", &N);
    }
    for(i = 1; i < N; i++){
        for (j = 1; j < N; j++){
            printf("%d\t", (1+j+i));
        }
        printf("\n"); 
    }
}
int main (){
    int N;
    scanf("%d", &N);
    quadrado (N);
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
  "source_sha256": "1955b21beb8bfa11e6069af74f08eecfb04a1adbead12a40fdfbbe62d60e00bb",
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
      "output": "3\t4\t\n4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "3\t4\t5\t\n4\t5\t6\t\n5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "3\t4\t5\t6\t7\t8\t9\t\n4\t5\t6\t7\t8\t9\t10\t\n5\t6\t7\t8\t9\t10\t11\t\n6\t7\t8\t9\t10\t11\t12\t\n7\t8\t9\t10\t11\t12\t13\t\n8\t9\t10\t11\t12\t13\t14\t\n9\t10\t11\t12\t13\t14\t15\t\n"
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
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
    "stdout:ex01_2:relation": "different",
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


## sample_022 — train

```c


#include <stdio.h>

void quadrado(int N) {

    int i, j;

    for (i = 0; i < N; i++) {
        for (j = 1; j <= N; j++) {
            if (j == N)
                printf("%d\n", N);
            else
                printf("%d\t", j);
        }
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
  "sample_id": "sample_022",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "7acebda4cf9d51677af1efb2e6e9b98d4df2e68a85b8e90832fb868a36bce199",
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
      "output": "1\t2\t3\n1\t2\t3\n1\t2\t3\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\n1\t2\t3\t4\n1\t2\t3\t4\n1\t2\t3\t4\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\n1\t2\t3\t4\t5\t6\t7\t8\n1\t2\t3\t4\t5\t6\t7\t8\n1\t2\t3\t4\t5\t6\t7\t8\n1\t2\t3\t4\t5\t6\t7\t8\n1\t2\t3\t4\t5\t6\t7\t8\n1\t2\t3\t4\t5\t6\t7\t8\n1\t2\t3\t4\t5\t6\t7\t8\n"
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


void quadrado(int n);


int main() {
    int n, i;
    
    scanf("%d", &n);
    for ( i = 0; i < n; i++)
    {
        quadrado(n);
    }
    
    return 0;
}

void quadrado( int n) {
    int i;
    
    for ( i = 1; i <= n; i++)
    {
        printf("%d\t", i);
    }
    printf("\n");
    
}
```

```json
{
  "sample_id": "sample_023",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "2e5d82a08293762f8678f00380931b590a2eee0512189fd708b4cf9fd1777b50",
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
      "output": "1\t2\t3\t\n1\t2\t3\t\n1\t2\t3\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t\n1\t2\t3\t4\t\n1\t2\t3\t4\t\n1\t2\t3\t4\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t\n1\t2\t3\t4\t5\t6\t7\t8\t\n1\t2\t3\t4\t5\t6\t7\t8\t\n1\t2\t3\t4\t5\t6\t7\t8\t\n1\t2\t3\t4\t5\t6\t7\t8\t\n1\t2\t3\t4\t5\t6\t7\t8\t\n1\t2\t3\t4\t5\t6\t7\t8\t\n1\t2\t3\t4\t5\t6\t7\t8\t\n"
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
        for (j = i; j < n + i - 1; j++)
        {
            printf("%d\t", j);
        }
        printf("\n");
    }   
}
```

```json
{
  "sample_id": "sample_024",
  "partition": "train",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "03e13a684201ffbea115867bc033c49a42b5b3f65eeb325d1fd989c2ae0cedfd",
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
      "output": "1\t2\t\n2\t3\t\n3\t4\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t\n2\t3\t4\t\n3\t4\t5\t\n4\t5\t6\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t\n2\t3\t4\t5\t6\t7\t8\t\n3\t4\t5\t6\t7\t8\t9\t\n4\t5\t6\t7\t8\t9\t10\t\n5\t6\t7\t8\t9\t10\t11\t\n6\t7\t8\t9\t10\t11\t12\t\n7\t8\t9\t10\t11\t12\t13\t\n8\t9\t10\t11\t12\t13\t14\t\n"
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
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "small",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "small",
    "stdout:ex01_2:relation": "different",
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


## sample_025 — train

```c

#include <stdio.h>
void quadrado (int N){
    int l = 1,h,aux=0,buf = 0;
    for (h = 1; h <= N; ++h){
        for (l = 1 + buf; l <= (N + aux); ++l){
            if (l == N + aux)
                {printf("%d",l);}
            else
                {printf("%d\t",l);}
        }
        buf = l - N;
        aux += 1;
        printf("\n");
    }
}
int main(){
    int N;
    printf("Escreve numero: ");
    scanf("%d",&N);
    quadrado(N);
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
  "source_sha256": "e34cda6eb953e86e294463f7b575f22c2281caf160ca36ace2454b0f6cbcd6d4",
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
      "output": "Escreve numero: 1\t2\t3\n2\t3\t4\n3\t4\t5\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "Escreve numero: 1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "Escreve numero: 1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n"
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
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "small"
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


## sample_026 — train

```c

#include <stdio.h>

void quadrado(int N){

    int i, j;

    for(i = 1; i <= N; i++){
        for(j = 1; i <= N; j++){
            printf("%d", i + j - 1);
            if(j != N) putchar('\t');
        }
        putchar('\n');
    }

}

int main(){
    
    int N = 0;
    while(N >= 2){
        scanf("%d", &N);
    }

    quadrado(N);
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
  "source_sha256": "762474e77d36bc4c0ede8f6a32e37172d99dcd58f469e866d6465742014027d0",
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
      "output": ""
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": ""
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": ""
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
    "ast:c_strict_comparison": "0",
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


void quadrado(int N){

    int i, j;

    for(i = 1; i <= N; i++){
        for(j = 1; i <= N; j++){
            printf("%d", i + j - 1);
            if(j != N) putchar('\t');
        }
        putchar('\n');
    }
}

int main(){
    
    int N = 0;
    while(N >= 2){
        scanf("%d", &N);
    }

    quadrado(N);
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
  "source_sha256": "edf054e653f6231c3884f48ef80e4bdb18e9868d1da12b80ee100a35c1add808",
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
      "output": ""
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": ""
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": ""
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
    "ast:c_strict_comparison": "0",
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


void quadrado(int N){

    int i, j;

    for(i = 1; i <= N; i++){
        for(j = 1; i <= N; j++){
            printf("%d", i + j - 1);
            if(j != N) putchar('\t');
        }
        putchar('\n');
    }
}



int main(){
    
    int N = 0;
    while(N >= 2){
        scanf("%d", &N);
    }

    quadrado(N);
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
  "source_sha256": "291bb93b26cf5575b2d811a07e1bd7bda45940847aaef738447db8c41208cc27",
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
      "output": ""
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": ""
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": ""
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
    "ast:c_strict_comparison": "0",
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

void quadrado(int N){
    int elemento, linha;

    for (linha = 1; linha <= N; linha++){
        if (linha > 1)
            printf("\n");

        printf("%d",linha);
        
        for (elemento = 1 + linha; elemento <= (N + linha); elemento++){
            printf("\t%d",elemento);
        }
    }
    printf("\n");
}

int main(){
    int N;

    scanf("%d",&N);

    quadrado(N);

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
  "source_sha256": "be5a67a74098692cd9ded18b7600723410f68f58000582678adbb09cf9b88b85",
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
      "output": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t5\n2\t3\t4\t5\t6\n3\t4\t5\t6\t7\n4\t5\t6\t7\t8\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t9\n2\t3\t4\t5\t6\t7\t8\t9\t10\n3\t4\t5\t6\t7\t8\t9\t10\t11\n4\t5\t6\t7\t8\t9\t10\t11\t12\n5\t6\t7\t8\t9\t10\t11\t12\t13\n6\t7\t8\t9\t10\t11\t12\t13\t14\n7\t8\t9\t10\t11\t12\t13\t14\t15\n8\t9\t10\t11\t12\t13\t14\t15\t16\n"
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
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "small"
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


## sample_030 — validation

```c

#include <stdio.h>

void quadrado(int N);

int main () {
    int N;
    scanf("%d", &N);
    quadrado(N);
    return 0;
}

void quadrado(int N) {
    int i0, j0, j1;
    for (i0 = 1; i0 <= N; i0++) {
        j1 = i0;
        for (j0 = 0; j0 < N; j0++) {
            if (!(j0))
                printf("\t");
            printf("%d", j1);
            j1++;
        }
        printf("\n");
    }
    return;
}
```

```json
{
  "sample_id": "sample_030",
  "partition": "validation",
  "representative": false,
  "is_train_medoid": false,
  "raw_code_truncated": false,
  "source_sha256": "96fded4488790a4edabf61e8a382ad6de14480ba77f07f7f8247c01a0a86fe1f",
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
      "output": "\t123\n\t234\n\t345\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "\t1234\n\t2345\n\t3456\n\t4567\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "\t12345678\n\t23456789\n\t345678910\n\t4567891011\n\t56789101112\n\t678910111213\n\t7891011121314\n\t89101112131415\n"
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
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "large",
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

void quadrado(int N){
    int linha, coluna;
    for (linha = 0; linha < N; linha++){
        for (coluna = 1; coluna < N; coluna++){
            printf("%d", coluna + linha + 1);
            if (coluna != N)
                putchar('\t'); 
        }
        putchar('\n');
    }
}

int main(){
    int N;

    scanf("%d", &N);

    quadrado(N);

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
  "source_sha256": "c743edbbcb57c9c33f49db97883184e21ed2f426e7af12f2bb425a2ccb3c04a2",
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
      "output": "2\t3\t\n3\t4\t\n4\t5\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "2\t3\t4\t\n3\t4\t5\t\n4\t5\t6\t\n5\t6\t7\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "2\t3\t4\t5\t6\t7\t8\t\n3\t4\t5\t6\t7\t8\t9\t\n4\t5\t6\t7\t8\t9\t10\t\n5\t6\t7\t8\t9\t10\t11\t\n6\t7\t8\t9\t10\t11\t12\t\n7\t8\t9\t10\t11\t12\t13\t\n8\t9\t10\t11\t12\t13\t14\t\n9\t10\t11\t12\t13\t14\t15\t\n"
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
    "ast:c_inclusive_comparison": "0",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
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


## sample_033 — train

```c

#include <stdio.h>

void quadrado(int N)
{
    int linha, i;

    for (linha = 0; linha < N; linha++)
    {
        for (i = 1; i <= N; i++)
        {
            if (i == N) printf("%d\t", (i + linha));
            else printf("%d", (i + linha));
        } 
        printf("\n");
    }
}

int main()
{
    int n;

    scanf("%d", &n);
    quadrado(n);
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
  "source_sha256": "ec1f16fa9c6358932c6700e56d36245584494758c8c2cce8832933074b838fd1",
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
      "output": "123\t\n234\t\n345\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1234\t\n2345\t\n3456\t\n4567\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "12345678\t\n23456789\t\n345678910\t\n4567891011\t\n56789101112\t\n678910111213\t\n7891011121314\t\n89101112131415\t\n"
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


## sample_034 — train

```c


#include <stdio.h>

void quadrado(int N) {
    int n2, starter = 1, starter2 = 1, n3;
    n2 = N--;
    n3 = N--;
    if (N >= 2) {
        while (N > 0) {
            starter = starter2;
            while (n2 > 0) {
                printf("%d\t", starter);
                starter ++;
                n2--;
            }
            printf("%d", starter);
            printf("\n");
            starter2 ++;
            N--;
            n2 = n3;
        }
    }

}

int main () {
    int N;
    scanf("%d", &N);
    quadrado(N);
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
  "source_sha256": "dc185c6503ae7bfb6d861824fdd601eb630ed41bbe7e3ec4fe6c8a411c867e5d",
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
      "output": ""
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t5\n2\t3\t4\t5\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t9\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n"
    }
  ],
  "clustering_oav": {
    "test:ex01_0": "fail",
    "test:ex01_1": "fail",
    "test:ex01_2": "fail",
    "ast:c_for": "0",
    "ast:c_while": "1",
    "ast:c_do": "0",
    "ast:c_if": "1",
    "ast:c_inclusive_comparison": "1",
    "ast:c_strict_comparison": "1",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "empty",
    "stdout:ex01_0:edit_band": "large",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "medium"
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


## sample_036 — train

```c

#include <stdio.h>
void quadrado(int N) {
    int i, l;

    scanf("%d", &N);

    for(l = 1; l <= N; l++) {
        for(i = l; i <= N + l; i++) {
            printf("%d\t", i);
        }
        printf("\n");
    }
}

int main() {
    int N;
    
    scanf("%d", &N);
    
    if (N >= 2) {
        quadrado(N);
    }
    
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
  "source_sha256": "01c16b69388bd37183a010c8bdccaa7e96f40d26b5e56107d10c3d366de340a0",
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
      "output": "1\t2\t3\t4\t\n2\t3\t4\t5\t\n3\t4\t5\t6\t\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t2\t3\t4\t5\t\n2\t3\t4\t5\t6\t\n3\t4\t5\t6\t7\t\n4\t5\t6\t7\t8\t\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t2\t3\t4\t5\t6\t7\t8\t9\t\n2\t3\t4\t5\t6\t7\t8\t9\t10\t\n3\t4\t5\t6\t7\t8\t9\t10\t11\t\n4\t5\t6\t7\t8\t9\t10\t11\t12\t\n5\t6\t7\t8\t9\t10\t11\t12\t13\t\n6\t7\t8\t9\t10\t11\t12\t13\t14\t\n7\t8\t9\t10\t11\t12\t13\t14\t15\t\n8\t9\t10\t11\t12\t13\t14\t15\t16\t\n"
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
    "ast:c_strict_comparison": "0",
    "ast:c_address_of": "1",
    "ast:c_update": "1",
    "stdout:ex01_0:relation": "different",
    "stdout:ex01_0:edit_band": "medium",
    "stdout:ex01_1:relation": "different",
    "stdout:ex01_1:edit_band": "medium",
    "stdout:ex01_2:relation": "different",
    "stdout:ex01_2:edit_band": "small"
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


## sample_037 — train

```c

#include <stdio.h>

int main() {
    int n, i ,j;
    scanf("%d",&n);
    if (n<= 0)
        return 0;
    for (i = 0; i<n; i++) {
        for (j=1;j<n;j++){
            printf("%d\t",j+i);
        printf("%d\n",j+i);    
        }
    }
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
  "source_sha256": "92e498c9f91cb2e081b89c9f4554b5c7ce743791b2504e454d54fb1d26122df5",
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
      "output": "1\t1\n2\t2\n2\t2\n3\t3\n3\t3\n4\t4\n"
    },
    {
      "test_id": "ex01_1",
      "input": "4",
      "expected": "1\t2\t3\t4\n2\t3\t4\t5\n3\t4\t5\t6\n4\t5\t6\t7\n",
      "output": "1\t1\n2\t2\n3\t3\n2\t2\n3\t3\n4\t4\n3\t3\n4\t4\n5\t5\n4\t4\n5\t5\n6\t6\n"
    },
    {
      "test_id": "ex01_2",
      "input": "8",
      "expected": "1\t2\t3\t4\t5\t6\t7\t8\n2\t3\t4\t5\t6\t7\t8\t9\n3\t4\t5\t6\t7\t8\t9\t10\n4\t5\t6\t7\t8\t9\t10\t11\n5\t6\t7\t8\t9\t10\t11\t12\n6\t7\t8\t9\t10\t11\t12\t13\n7\t8\t9\t10\t11\t12\t13\t14\n8\t9\t10\t11\t12\t13\t14\t15\n",
      "output": "1\t1\n2\t2\n3\t3\n4\t4\n5\t5\n6\t6\n7\t7\n2\t2\n3\t3\n4\t4\n5\t5\n6\t6\n7\t7\n8\t8\n3\t3\n4\t4\n5\t5\n6\t6\n7\t7\n8\t8\n9\t9\n4\t4\n5\t5\n6\t6\n7\t7\n8\t8\n9\t9\n10\t10\n5\t5\n6\t6\n7\t7\n8\t8\n9\t9\n10\t10\n11\t11\n6\t6\n7\t7\n8\t8\n9\t9\n10\t10\n11\t11\n12\t12\n7\t7\n8\t8\n9\t9\n10\t10\n11\t11\n12\t12\n13\t13\n8\t8\n9\t9\n10\t10\n11\t11\n12\t12\n13\t13\n14\t14\n"
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
  "members/sample_035/tests/ex01_1",
  "members/sample_035/tests/ex01_2",
  "members/sample_036/raw_code",
  "members/sample_036/tests/ex01_0",
  "members/sample_036/tests/ex01_1",
  "members/sample_036/tests/ex01_2",
  "members/sample_037/raw_code",
  "members/sample_037/tests/ex01_0",
  "members/sample_037/tests/ex01_1",
  "members/sample_037/tests/ex01_2"
]
```
