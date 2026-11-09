# Dataset Curation: Multi-Defect Sample Review

Dataset: AFRAD (Wang et al., 2025)

Twenty-eight images contain two or more defect types and were excluded from the single-label classification dataset.

## Defect Categories

Samples are labelled with one of five categories: `broken`, `crack`, `folds`, `impurities`, `rough`.

## Overview

| Item | Count |
| --- | --- |
| Multi-defect images | 28 |
| With 2 defect types | 27 |
| With 3 defect types | 1 |

### Defect Combinations

| Combination | Count |
| --- | --- |
| broken + crack | 14 |
| broken + impurities | 6 |
| broken + rough | 3 |
| crack + impurities | 2 |
| impurities + rough | 2 |
| broken + crack + impurities | 1 |

## Image List

| # | Filename | Defect types | Categories |
| --- | --- | --- | --- |
| 1 | `041610-1957-514-2731-101_ok.jpg` | 2 | broken, impurities |
| 2 | `041916-3154-429-1982-101_ok.jpg` | 2 | broken, crack |
| 3 | `041916-3616-561-2177-101_ok.jpg` | 2 | broken, crack |
| 4 | `042014-5058-956-502-101_ok.jpg` | 2 | broken, impurities |
| 5 | `050718-3703-553-17-101_ng.jpg` | 2 | broken, impurities |
| 6 | `050718-3808-691-37-101_ng.jpg` | 2 | broken, impurities |
| 7 | `050809-2829-855-2217-101_ng.jpg` | 2 | broken, crack |
| 8 | `050809-5124-414-3304-101_ng.jpg` | 2 | broken, crack |
| 9 | `050809-5321-701-3422-101_ng.jpg` | 2 | broken, crack |
| 10 | `050809-5427-656-3475-101_ng.jpg` | 3 | broken, crack, impurities |
| 11 | `050809-5957-429-3724-101_ng.jpg` | 2 | broken, crack |
| 12 | `050810-2733-358-4962-101_ng.jpg` | 2 | broken, crack |
| 13 | `050810-5153-164-6112-101_ng.jpg` | 2 | broken, crack |
| 14 | `050812-2436-686-906-101_ng.jpg` | 2 | crack, impurities |
| 15 | `050812-4349-668-1827-101_ng.jpg` | 2 | broken, impurities |
| 16 | `050812-4834-128-2034-101_ng.jpg` | 2 | broken, crack |
| 17 | `050812-5537-506-2382-101_ng.jpg` | 2 | broken, crack |
| 18 | `050813-5402-740-5166-101_ng.jpg` | 2 | broken, crack |
| 19 | `050813-5831-332-5544-101_ng.jpg` | 2 | crack, impurities |
| 20 | `050814-1302-945-6708-101_ng.jpg` | 2 | broken, crack |
| 21 | `050814-4157-591-9179-101_ng.jpg` | 2 | broken, crack |
| 22 | `050814-4539-497-9523-101_ng.jpg` | 2 | broken, crack |
| 23 | `050814-5408-708-10201-101_ng.jpg` | 2 | broken, impurities |
| 24 | `110217-0728-156-467-101_ng.jpg` | 2 | impurities, rough |
| 25 | `110217-0958-122-541-101_ng.jpg` | 2 | broken, rough |
| 26 | `110217-1440-163-667-101_ng.jpg` | 2 | broken, rough |
| 27 | `110217-1522-524-690-101_ng.jpg` | 2 | impurities, rough |
| 28 | `110217-2004-842-791-101_ok.jpg` | 2 | broken, rough |

## Identification Criterion

A sample was classified as multi-defect when its filename occurred in the test/bad directory of at least two defect categories. No folds sample overlapped with another category.
