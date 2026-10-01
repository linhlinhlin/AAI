# Exploratory per-category recovery (test run)

Share of items whose K-means cluster (oracle k, seed 42) has their category as majority.

## real (full scope)

| Category | n | exact_signature | outcomes | combined_stdout | deviation | evidence | embedding |
|---|---:|---:|---:|---:|---:|---:|---:|
| OUTPUT_TEXT | 177 | 0.98 | 0.98 | 0.92 | 0.95 | 0.94 | 0.92 |
| COMPUTATION | 28 | 0.54 | 0.54 | 0.64 | 0.57 | 0.61 | 0.32 |
| MISSING_STATEMENT | 27 | 0.37 | 0.37 | 0.67 | 0.56 | 0.63 | 0.70 |
| BRANCH_CONDITION | 17 | 0.29 | 0.24 | 0.65 | 0.59 | 0.59 | 0.18 |
| LOOP_BOUNDARY | 16 | 0.88 | 0.88 | 0.94 | 0.81 | 0.81 | 0.31 |
| OUTPUT_FORMAT | 13 | 0.00 | 0.00 | 0.69 | 0.69 | 0.69 | 0.77 |
| CONTROL_FLOW | 12 | 0.83 | 0.83 | 0.83 | 0.83 | 0.92 | 0.33 |
| EXTRA_STATEMENT | 8 | 0.12 | 0.12 | 0.38 | 0.50 | 0.50 | 0.62 |
| INITIALIZATION | 7 | 0.57 | 0.57 | 1.00 | 1.00 | 1.00 | 0.57 |
| INPUT | 6 | 0.50 | 0.50 | 0.50 | 0.50 | 0.50 | 0.50 |
| STATEMENT_PLACEMENT | 6 | 0.50 | 0.50 | 0.33 | 0.50 | 0.33 | 0.33 |
| NUMERIC_TYPE | 3 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.67 |

Pairs with identical test signatures: 2087; with different mechanisms: 740 (35.5%).

## injected (partition scope)

| Category | n | exact_signature | outcomes | combined_stdout | deviation | evidence | embedding |
|---|---:|---:|---:|---:|---:|---:|---:|
| MISSING_STATEMENT | 72 | 0.56 | 0.49 | 0.69 | 0.60 | 0.64 | 0.18 |
| EXTRA_STATEMENT | 65 | 0.49 | 0.46 | 0.68 | 0.82 | 0.82 | 0.57 |
| OUTPUT_TEXT | 60 | 0.62 | 0.62 | 0.90 | 0.97 | 0.95 | 0.18 |
| INITIALIZATION | 53 | 0.40 | 0.40 | 0.60 | 0.53 | 0.58 | 0.15 |
| LOOP_BOUNDARY | 50 | 0.62 | 0.56 | 0.68 | 0.62 | 0.62 | 0.20 |
| STATEMENT_PLACEMENT | 48 | 0.12 | 0.08 | 0.67 | 0.79 | 0.58 | 0.23 |
| COMPUTATION | 43 | 0.51 | 0.51 | 0.70 | 0.67 | 0.77 | 0.79 |
| BRANCH_CONDITION | 29 | 0.38 | 0.34 | 0.45 | 0.45 | 0.48 | 0.93 |
| OUTPUT_FORMAT | 9 | 1.00 | 1.00 | 1.00 | 1.00 | 0.89 | 0.00 |

Pairs with identical test signatures: 2901; with different mechanisms: 2367 (81.6%).

