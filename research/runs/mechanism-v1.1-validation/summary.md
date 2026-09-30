# Mechanism evaluation (validation partition)

## real (primary scope: partition, cohorts: 2)

| Representation | ARI K-means (oracle k) | ARI HAC (oracle k) | ARI K-means (silhouette k) | Ceiling |
|---|---:|---:|---:|---:|
| outcomes | 0.578 | 0.578 | 0.249 | 0.845 |
| outcomes_stdout | 1.000 | 1.000 | 0.249 | 1.000 |
| combined_stdout | 1.000 | 1.000 | 0.417 | 1.000 |
| structural | 0.643 | 0.643 | 0.221 | 0.917 |
| code_cues | 0.324 | 0.324 | 0.185 | 0.929 |
| deviation | 0.741 | 0.741 | 0.352 | 1.000 |
| evidence | 0.741 | 0.741 | 0.378 | 1.000 |
| embedding | 0.324 | 0.324 | 0.249 | - |

Exact test signature ARI: 0.5782828282828283

| Hypothesis | Mean | 95% CI | Wins/Losses | Holm p | Verdict |
|---|---:|---|---|---:|---|
| H1a | 0.845 | [0.833, 0.857] | 2/0 | - | supported |
| H1b | 0.104 | [0.084, 0.123] | 2/0 | 1.0000 | supported |
| H2_kmeans | 0.162 | [-0.130, 0.455] | 1/1 | 1.0000 | not_supported |
| H2_hac | 0.162 | [-0.130, 0.455] | 1/1 | 1.0000 | not_supported |
| H3_kmeans | -0.259 | [-0.519, 0.000] | 0/1 | 1.0000 | not_supported |
| H3_hac | -0.259 | [-0.519, 0.000] | 0/1 | 1.0000 | not_supported |

H4 (ILA-2 evidence minus outcome summary, macro-F1): {'mean': 0.11594661474634553, 'ci95': [0.002695372380560922, 0.2198419028415668]} -> supported

| Rule model | Macro-F1 | Coverage | Selective accuracy | Rules |
|---|---:|---:|---:|---:|
| seen_problems|evidence|ila | 0.250 | 0.552 | 0.892 | 12 |
| seen_problems|evidence|ila2 | 0.269 | 0.761 | 0.804 | 14 |
| seen_problems|evidence|cart | 0.194 | 1.000 | 0.493 | - |
| seen_problems|outcome_summary|ila | 0.000 | 0.000 | 0.000 | 1 |
| seen_problems|outcome_summary|ila2 | 0.126 | 0.881 | 0.644 | 3 |
| seen_problems|outcome_summary|cart | 0.124 | 1.000 | 0.567 | - |
| seen_problems|majority | 0.056 | 1.000 | 0.507 | - |
| unseen_problems|evidence|ila | 0.111 | 0.200 | 0.500 | 10 |
| unseen_problems|evidence|ila2 | 0.167 | 0.600 | 0.333 | 13 |
| unseen_problems|evidence|cart | 0.167 | 1.000 | 0.200 | - |
| unseen_problems|outcome_summary|ila | 0.000 | 0.000 | 0.000 | 1 |
| unseen_problems|outcome_summary|ila2 | 0.167 | 0.800 | 0.250 | 3 |
| unseen_problems|outcome_summary|cart | 0.167 | 1.000 | 0.200 | - |
| unseen_problems|majority | 0.000 | 1.000 | 0.000 | - |

## injected (primary scope: partition, cohorts: 22)

| Representation | ARI K-means (oracle k) | ARI HAC (oracle k) | ARI K-means (silhouette k) | Ceiling |
|---|---:|---:|---:|---:|
| outcomes | 0.080 | 0.097 | 0.078 | 0.492 |
| outcomes_stdout | 0.357 | 0.323 | 0.346 | 0.826 |
| combined_stdout | 0.348 | 0.328 | 0.307 | 0.897 |
| structural | -0.051 | -0.051 | -0.054 | 0.380 |
| code_cues | 0.071 | 0.010 | 0.066 | 0.727 |
| deviation | 0.366 | 0.331 | 0.354 | 0.871 |
| evidence | 0.358 | 0.328 | 0.275 | 0.951 |
| embedding | -0.074 | -0.063 | -0.102 | - |

Exact test signature ARI: 0.09061626625228951

| Hypothesis | Mean | 95% CI | Wins/Losses | Holm p | Verdict |
|---|---:|---|---|---:|---|
| H1a | 0.492 | [0.420, 0.567] | 22/0 | - | supported |
| H1b | 0.189 | [0.136, 0.244] | 19/1 | 0.0009 | supported |
| H2_kmeans | 0.286 | [0.203, 0.376] | 21/0 | 0.0006 | supported |
| H2_hac | 0.234 | [0.139, 0.335] | 19/1 | 0.0013 | supported |
| H3_kmeans | 0.010 | [-0.030, 0.050] | 10/7 | 1.0000 | not_supported |
| H3_hac | -0.001 | [-0.062, 0.053] | 12/7 | 1.0000 | not_supported |
| H5 | 0.749 | [0.595, 0.892] | 21/1 | 0.0000 | supported |

| Rule model | Macro-F1 | Coverage | Selective accuracy | Rules |
|---|---:|---:|---:|---:|
| seen_problems|evidence|ila | 0.440 | 0.315 | 0.960 | 35 |
| seen_problems|evidence|ila2 | 0.646 | 0.760 | 0.778 | 42 |
| seen_problems|evidence|cart | 0.451 | 1.000 | 0.587 | - |
| seen_problems|outcome_summary|ila | 0.000 | 0.000 | 0.000 | 0 |
| seen_problems|outcome_summary|ila2 | 0.023 | 0.024 | 0.800 | 1 |
| seen_problems|outcome_summary|cart | 0.077 | 1.000 | 0.226 | - |
| seen_problems|majority | 0.035 | 1.000 | 0.188 | - |
| unseen_problems|evidence|ila | 0.273 | 0.352 | 0.674 | 24 |
| unseen_problems|evidence|ila2 | 0.362 | 0.636 | 0.559 | 38 |
| unseen_problems|evidence|cart | 0.451 | 1.000 | 0.431 | - |
| unseen_problems|outcome_summary|ila | 0.000 | 0.000 | 0.000 | 0 |
| unseen_problems|outcome_summary|ila2 | 0.036 | 0.040 | 0.800 | 1 |
| unseen_problems|outcome_summary|cart | 0.096 | 1.000 | 0.162 | - |
| unseen_problems|majority | 0.027 | 1.000 | 0.123 | - |

