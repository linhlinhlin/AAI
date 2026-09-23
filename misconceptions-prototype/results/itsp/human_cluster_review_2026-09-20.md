# Human expert validation — cluster review

Status: **waiting_for_human_expert_annotation**. Completed human reviews: 0; adjudications: 0.

Scope: selected review samples only, not whole-cluster or whole-cohort estimates. Types are codebook categories, not confirmed mechanisms. Multiple observed types flag cases for human inspection; a single type does not establish a shared cause. Ties list all modal types; no automatic majority adjudication or outlier labels.

No/Unclear/pending/untyped Yes are excluded from type purity. AI annotations never supply these metrics. No student-level generalization.

| Problem | Arm | Cluster | Selected | Typed Yes | Coverage | Decisions | Type counts | Modal types | Multiple types |
|---|---|---|---|---|---|---|---|---|---|
| 2812 | A | 0 | 2 | 0 | 0.000 | {"pending": 2} | {} | null | null |
| 2812 | A | 1 | 1 | 0 | 0.000 | {"pending": 1} | {} | null | null |
| 2812 | A | 2 | 2 | 0 | 0.000 | {"pending": 2} | {} | null | null |
| 2812 | B | 0 | 5 | 0 | 0.000 | {"pending": 5} | {} | null | null |
| 2812 | C | 0 | 2 | 0 | 0.000 | {"pending": 2} | {} | null | null |
| 2812 | C | 1 | 1 | 0 | 0.000 | {"pending": 1} | {} | null | null |
| 2812 | C | 2 | 2 | 0 | 0.000 | {"pending": 2} | {} | null | null |
| 2825 | A | 0 | 2 | 0 | 0.000 | {"pending": 2} | {} | null | null |
| 2825 | A | 1 | 2 | 0 | 0.000 | {"pending": 2} | {} | null | null |
| 2825 | A | 2 | 2 | 0 | 0.000 | {"pending": 2} | {} | null | null |
| 2825 | B | 0 | 6 | 0 | 0.000 | {"pending": 6} | {} | null | null |
| 2825 | C | 0 | 2 | 0 | 0.000 | {"pending": 2} | {} | null | null |
| 2825 | C | 1 | 2 | 0 | 0.000 | {"pending": 2} | {} | null | null |
| 2825 | C | 2 | 2 | 0 | 0.000 | {"pending": 2} | {} | null | null |
| 2833 | A | 0 | 2 | 0 | 0.000 | {"pending": 2} | {} | null | null |
| 2833 | A | 1 | 2 | 0 | 0.000 | {"pending": 2} | {} | null | null |
| 2833 | A | 2 | 2 | 0 | 0.000 | {"pending": 2} | {} | null | null |
| 2833 | B | 0 | 5 | 0 | 0.000 | {"pending": 5} | {} | null | null |
| 2833 | B | 2 | 1 | 0 | 0.000 | {"pending": 1} | {} | null | null |
| 2833 | C | 0 | 2 | 0 | 0.000 | {"pending": 2} | {} | null | null |
| 2833 | C | 1 | 2 | 0 | 0.000 | {"pending": 2} | {} | null | null |
| 2833 | C | 2 | 2 | 0 | 0.000 | {"pending": 2} | {} | null | null |

## Purity by problem and arm

- 2812/A: purity=null; numerator=None; typed denominator=0/5 candidates.
- 2812/B: purity=null; numerator=None; typed denominator=0/5 candidates.
- 2812/C: purity=null; numerator=None; typed denominator=0/5 candidates.
- 2825/A: purity=null; numerator=None; typed denominator=0/6 candidates.
- 2825/B: purity=null; numerator=None; typed denominator=0/6 candidates.
- 2825/C: purity=null; numerator=None; typed denominator=0/6 candidates.
- 2833/A: purity=null; numerator=None; typed denominator=0/6 candidates.
- 2833/B: purity=null; numerator=None; typed denominator=0/6 candidates.
- 2833/C: purity=null; numerator=None; typed denominator=0/6 candidates.

## Agreement

```json
null
```

## Trace selected members

- 2812/A/0: itsp-2812-270285_buggy, itsp-2812-270293_buggy
- 2812/A/1: itsp-2812-270277_buggy
- 2812/A/2: itsp-2812-270276_buggy, itsp-2812-270283_buggy
- 2812/B/0: itsp-2812-270276_buggy, itsp-2812-270277_buggy, itsp-2812-270283_buggy, itsp-2812-270285_buggy, itsp-2812-270293_buggy
- 2812/C/0: itsp-2812-270285_buggy, itsp-2812-270293_buggy
- 2812/C/1: itsp-2812-270277_buggy
- 2812/C/2: itsp-2812-270276_buggy, itsp-2812-270283_buggy
- 2825/A/0: itsp-2825-271154_buggy, itsp-2825-271203_buggy
- 2825/A/1: itsp-2825-271173_buggy, itsp-2825-271188_buggy
- 2825/A/2: itsp-2825-271163_buggy, itsp-2825-271213_buggy
- 2825/B/0: itsp-2825-271154_buggy, itsp-2825-271163_buggy, itsp-2825-271173_buggy, itsp-2825-271188_buggy, itsp-2825-271203_buggy, itsp-2825-271213_buggy
- 2825/C/0: itsp-2825-271154_buggy, itsp-2825-271203_buggy
- 2825/C/1: itsp-2825-271173_buggy, itsp-2825-271188_buggy
- 2825/C/2: itsp-2825-271163_buggy, itsp-2825-271213_buggy
- 2833/A/0: itsp-2833-271912_buggy, itsp-2833-271920_buggy
- 2833/A/1: itsp-2833-271916_buggy, itsp-2833-271986_buggy
- 2833/A/2: itsp-2833-271965_buggy, itsp-2833-271975_buggy
- 2833/B/0: itsp-2833-271912_buggy, itsp-2833-271916_buggy, itsp-2833-271920_buggy, itsp-2833-271965_buggy, itsp-2833-271986_buggy
- 2833/B/2: itsp-2833-271975_buggy
- 2833/C/0: itsp-2833-271912_buggy, itsp-2833-271920_buggy
- 2833/C/1: itsp-2833-271916_buggy, itsp-2833-271986_buggy
- 2833/C/2: itsp-2833-271965_buggy, itsp-2833-271975_buggy

Annotation SHA-256: `f08a372235c9496cfde9ad587b7a8593db65071014e9b034eb9a3e7459f9e914`. Assignment SHA-256: `bffe0aa482f5a0f47beaa803dbee82b55ad70d320f00935d17314af6fe645c22`.
