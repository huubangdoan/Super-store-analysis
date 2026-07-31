# 🔍 Findings — Super Store Data Exploration

Documenting the exploratory data analysis (EDA) process and insights derived from the Superstore dataset, which inform the design of the dashboard.

## 1. Data Overview

- Number of rows: `9,994` (raw) | Number of columns: `13`
- No date column (`Order Date`) in this dataset → trend-over-time analysis is not possible
- Missing values: **none** — all 13 columns have 0 nulls
- Duplicate rows: **17 fully identical rows found but not removed**
  - No unique Order ID / Customer ID exists in this dataset, so duplicates were identified by checking if *all* column values matched exactly
  - Inspected the duplicate pairs: `Profit` values match to 4 decimal places (e.g. `16.1838`, `19.8720`, `6.2208`) across both rows in each pair — the probability of two unrelated orders coincidentally matching to that precision is effectively zero, so these are treated as genuine duplicate entries (likely a data import issue) rather than coincidental separate orders

## 2. Key Variable Distributions

### Sales & Profit
- Sales ranges from `$0.44` to `$22,638.48`, average `$229,86`, median `$54.49` → **strongly right-skewed** (a small number of large orders pull the average well above the median)
- Profit ranges from `-$6,599.98` to `$8,399.98`, average `$28.66`
- **1,869 rows (18.7%)** have negative Profit → nearly 1 in 5 orders is sold at a loss
- Total Sales: **$2,297,200.00** | Total Profit: **$286,394.00**

### Discount
- Discount ranges from `0%` to `80%`, average `15.6%`, median `20%`
- Discount and Profit have a **clear inverse relationship** (see section 3)

## 3. Insights by Dimension

### By Region
| Region | Sales | Profit |
|---|---|---|
| West | $725,256 | $108,329 |
| East | $678,435 | $91,506 |
| Central | $500,783 | $39,654 |
| South | $391,721 | $46,749 |

Observation: **West** leads in both Sales and Profit. **Central** has similar Sales to South but notably lower Profit — worth investigating (higher discounting or costlier product mix in Central).

### By Sub-Category
- Highest Sales: `Chairs` ($327,778), `Phones` ($330,007), `Storage` ($223,844)
- **Sub-Categories running an overall loss**: `Tables` (-$17,725), `Bookcases` (-$3,473), `Supplies` (-$1,189)
- Most profitable: `Copiers` ($55,618), `Phones` ($44,514), `Accessories` ($41,936)

### By Segment
| Segment | Sales |
|---|---|
| Consumer | $1,160,832 |
| Corporate | $706,070 |
| Home Office | $429,293 |

Observation: **Consumer** is by far the largest segment, contributing more than the other two combined.

### Discount vs Profit
Average Profit by discount level:
| Discount range | Avg. Profit |
|---|---|
| 0% | $67.02 |
| 0–20% | $26.52 |
| 20–40% | -$78.01 |
| 40–60% | -$134.62 |
| 60–80% | -$98.48 |

Observation: profit turns **negative once discount exceeds ~20%**, and worsens sharply from there. This is one of the clearest patterns in the dataset.
Conclusion: discounting beyond ~20% is generally unprofitable in this dataset — worth a policy review, especially for `Tables` and `Bookcases` (already loss-making sub-categories).

### Top / Bottom States
- Highest Sales: **California** ($457,576), **New York** ($310,827), **Texas** ($170,125)
- Lowest Profit: **Texas** (-$25,751), **Ohio** (-$16,959), **Pennsylvania** (-$15,565)

Observation: **Texas** is the 3rd highest in Sales but the *worst* in Profit — a strong candidate for discount/pricing review.

## 4. Outliers (IQR method)

| Column | Outliers | % of data |
|---|---|---|
| Sales | 1,167 | 11.70% |
| Quantity | 170 | 1.70% |
| Discount | 855 | 8.57% |
| Profit | 1,881 | 18.85% |

**Decision: outliers were kept, not removed.** Reasoning:
- High-Sales outliers correspond to genuinely large orders (mostly Technology), and Profit scales up accordingly — these are real, valid transactions, not data errors
- High-discount outliers explain most of the negative-Profit outliers (consistent with the Discount vs Profit pattern above)
- Removing them would hide the very loss-making pattern the analysis is meant to surface

## 5. Conclusions & Recommendations

- **Review discount policy** above ~20%, where profit consistently turns negative — particularly for `Tables` and `Bookcases`
- **Investigate Furniture category** pricing/costs — Sales are strong but Profit lags far behind Technology and Office Supplies
- **Texas** deserves attention: high Sales but the largest overall loss among all states, likely driven by heavy discounting
- **West region** is the strongest performer and could be a benchmark for pricing/discount strategy in other regions

## 6. Limitations

- No date column → cannot analyze monthly/quarterly/seasonal trends
- No unique order/transaction ID → duplicate detection relies on full-row matching rather than a reliable key, so duplicate identification (see Section 1) is inferential, not guaranteed
- No cost/margin breakdown beyond Profit → can't separate the effect of discount from underlying product cost

---