# Mechanism evaluation (test partition)

## real (primary scope: full, cohorts: 21)

| Representation | ARI K-means (oracle k) | ARI HAC (oracle k) | ARI K-means (silhouette k) | Ceiling |
|---|---:|---:|---:|---:|
| outcomes | 0.292 | 0.292 | 0.239 | 0.739 |
| outcomes_stdout | 0.363 | 0.367 | 0.313 | 0.907 |
| combined_stdout | 0.306 | 0.334 | 0.314 | 0.980 |
| structural | 0.064 | 0.029 | 0.080 | 0.772 |
| code_cues | 0.141 | 0.157 | 0.105 | 0.931 |
| deviation | 0.345 | 0.378 | 0.295 | 0.943 |
| evidence | 0.300 | 0.324 | 0.279 | 0.986 |
| embedding | 0.060 | 0.077 | 0.063 | - |

Exact test signature ARI: 0.2813448846368901

| Hypothesis | Mean | 95% CI | Wins/Losses | Holm p | Verdict |
|---|---:|---|---|---:|---|
| H1a | 0.739 | [0.696, 0.783] | 21/0 | - | supported |
| H1b | 0.080 | [0.052, 0.112] | 18/0 | 0.0018 | supported |
| H2_kmeans | 0.054 | [-0.081, 0.182] | 11/8 | 1.0000 | not_supported |
| H2_hac | 0.086 | [-0.025, 0.200] | 11/6 | 0.7440 | not_supported |
| H3_kmeans | -0.006 | [-0.097, 0.117] | 3/11 | 0.4416 | not_supported |
| H3_hac | -0.010 | [-0.111, 0.119] | 6/8 | 1.0000 | not_supported |

H4 (ILA-2 evidence minus outcome summary, macro-F1): {'mean': 0.09418468250431303, 'ci95': [-0.0111111111111111, 0.1714285714285714]} -> not_supported

| Rule model | Macro-F1 | Coverage | Selective accuracy | Rules |
|---|---:|---:|---:|---:|
| seen_problems|evidence|ila | 0.254 | 0.586 | 0.765 | 12 |
| seen_problems|evidence|ila2 | 0.256 | 0.690 | 0.700 | 14 |
| seen_problems|evidence|cart | 0.244 | 1.000 | 0.621 | - |
| seen_problems|outcome_summary|ila | 0.000 | 0.000 | 0.000 | 1 |
| seen_problems|outcome_summary|ila2 | 0.130 | 0.828 | 0.583 | 3 |
| seen_problems|outcome_summary|cart | 0.251 | 1.000 | 0.586 | - |
| seen_problems|majority | 0.109 | 1.000 | 0.483 | - |
| unseen_problems|evidence|ila | 0.354 | 1.000 | 0.500 | 10 |
| unseen_problems|evidence|ila2 | 0.354 | 1.000 | 0.500 | 13 |
| unseen_problems|evidence|cart | 0.381 | 1.000 | 0.500 | - |
| unseen_problems|outcome_summary|ila | 0.000 | 0.000 | 0.000 | 1 |
| unseen_problems|outcome_summary|ila2 | 0.214 | 0.750 | 0.500 | 3 |
| unseen_problems|outcome_summary|cart | 0.214 | 1.000 | 0.375 | - |
| unseen_problems|majority | 0.136 | 1.000 | 0.375 | - |

## injected (primary scope: partition, cohorts: 20)

| Representation | ARI K-means (oracle k) | ARI HAC (oracle k) | ARI K-means (silhouette k) | Ceiling |
|---|---:|---:|---:|---:|
| outcomes | 0.093 | 0.084 | 0.088 | 0.507 |
| outcomes_stdout | 0.338 | 0.299 | 0.332 | 0.839 |
| combined_stdout | 0.335 | 0.293 | 0.309 | 0.914 |
| structural | -0.066 | -0.068 | -0.052 | 0.353 |
| code_cues | 0.009 | -0.009 | -0.020 | 0.654 |
| deviation | 0.328 | 0.297 | 0.328 | 0.883 |
| evidence | 0.337 | 0.283 | 0.227 | 0.964 |
| embedding | -0.115 | -0.104 | -0.114 | - |

Exact test signature ARI: 0.09624282908556855

| Hypothesis | Mean | 95% CI | Wins/Losses | Holm p | Verdict |
|---|---:|---|---|---:|---|
| H1a | 0.507 | [0.429, 0.588] | 20/0 | - | supported |
| H1b | 0.172 | [0.121, 0.224] | 19/1 | 0.0000 | supported |
| H2_kmeans | 0.235 | [0.143, 0.331] | 16/4 | 0.0026 | supported |
| H2_hac | 0.214 | [0.117, 0.314] | 17/3 | 0.0028 | supported |
| H3_kmeans | 0.002 | [-0.055, 0.067] | 7/10 | 1.0000 | not_supported |
| H3_hac | -0.010 | [-0.060, 0.041] | 7/9 | 1.0000 | not_supported |
| H5 | 0.834 | [0.695, 0.958] | 19/1 | 0.0000 | supported |

| Rule model | Macro-F1 | Coverage | Selective accuracy | Rules |
|---|---:|---:|---:|---:|
| seen_problems|evidence|ila | 0.466 | 0.343 | 0.941 | 35 |
| seen_problems|evidence|ila2 | 0.649 | 0.807 | 0.742 | 42 |
| seen_problems|evidence|cart | 0.440 | 1.000 | 0.552 | - |
| seen_problems|outcome_summary|ila | 0.000 | 0.000 | 0.000 | 0 |
| seen_problems|outcome_summary|ila2 | 0.032 | 0.038 | 0.765 | 1 |
| seen_problems|outcome_summary|cart | 0.074 | 1.000 | 0.197 | - |
| seen_problems|majority | 0.031 | 1.000 | 0.159 | - |
| unseen_problems|evidence|ila | 0.261 | 0.427 | 0.623 | 24 |
| unseen_problems|evidence|ila2 | 0.350 | 0.720 | 0.524 | 38 |
| unseen_problems|evidence|cart | 0.402 | 1.000 | 0.441 | - |
| unseen_problems|outcome_summary|ila | 0.000 | 0.000 | 0.000 | 0 |
| unseen_problems|outcome_summary|ila2 | 0.039 | 0.042 | 0.833 | 1 |
| unseen_problems|outcome_summary|cart | 0.095 | 1.000 | 0.168 | - |
| unseen_problems|majority | 0.032 | 1.000 | 0.147 | - |

