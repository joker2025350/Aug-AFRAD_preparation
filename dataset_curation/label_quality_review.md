# Dataset Curation: Label Quality Review

Dataset: AFRAD (Wang et al., 2025)

Forty-seven images assigned to the normal class contain visible defects. These images were removed from the experimental dataset.

## Overview

| Item | Count |
| --- | --- |
| Mislabeled images | 47 |
| In `train/good` | 22 |
| In `test/good` | 25 |
| Filename ends with `_ng` | 46 |
| Filename ends with `_ok` | 1 |

Note: the `good` directories under each defect category (Base / broken / crack / folds / impurities / rough) contain the same set of images, so each file appears once in all six category folders.

## Image List

| # | Filename | Current location |
| --- | --- | --- |
| 1 | `050811-2622-389-7751-101_ng.jpg` | `<category>/train/good` |
| 2 | `050810-3851-794-5414-101_ng.jpg` | `<category>/test/good` |
| 3 | `050811-2625-910-7755-101_ng.jpg` | `<category>/test/good` |
| 4 | `050812-4351-608-5746-101_ng.jpg` | `<category>/test/good` |
| 5 | `050813-2425-175-3280-101_ng.jpg` | `<category>/train/good` |
| 6 | `050813-2627-676-3370-101_ng.jpg` | `<category>/train/good` |
| 7 | `042615-4558-397-3144-101_ng.jpg` | `<category>/train/good` |
| 8 | `050808-4117-829-69-101_ng.jpg` | `<category>/train/good` |
| 9 | `050809-0058-332-874-101_ng.jpg` | `<category>/train/good` |
| 10 | `050809-0240-401-971-101_ng.jpg` | `<category>/train/good` |
| 11 | `050809-2235-978-1918-101_ng.jpg` | `<category>/train/good` |
| 12 | `050809-2448-864-2037-101_ng.jpg` | `<category>/test/good` |
| 13 | `050809-4530-685-3079-101_ng.jpg` | `<category>/test/good` |
| 14 | `050810-4029-313-5494-101_ng.jpg` | `<category>/train/good` |
| 15 | `050810-4121-599-5534-101_ng.jpg` | `<category>/test/good` |
| 16 | `050811-2621-491-7750-101_ng.jpg` | `<category>/test/good` |
| 17 | `050812-1219-168-2014-101_ng.jpg` | `<category>/test/good` |
| 18 | `050812-3728-255-1485-101_ng.jpg` | `<category>/test/good` |
| 19 | `050814-2435-848-7719-101_ng.jpg` | `<category>/test/good` |
| 20 | `050814-2622-995-7887-101_ng.jpg` | `<category>/train/good` |
| 21 | `050814-2727-427-7990-101_ng.jpg` | `<category>/train/good` |
| 22 | `050814-3029-250-8257-101_ng.jpg` | `<category>/test/good` |
| 23 | `050814-3238-384-8455-101_ng.jpg` | `<category>/train/good` |
| 24 | `050815-0219-593-10969-101_ng.jpg` | `<category>/test/good` |
| 25 | `050815-1159-744-11843-101_ng.jpg` | `<category>/train/good` |
| 26 | `042615-1950-069-1754-101_ng.jpg` | `<category>/test/good` |
| 27 | `042615-3036-726-2380-101_ng.jpg` | `<category>/train/good` |
| 28 | `050809-2228-439-1908-101_ng.jpg` | `<category>/train/good` |
| 29 | `050809-2719-399-2167-101_ng.jpg` | `<category>/test/good` |
| 30 | `050809-2817-410-2206-101_ng.jpg` | `<category>/test/good` |
| 31 | `050810-1849-521-4568-101_ng.jpg` | `<category>/train/good` |
| 32 | `050812-0707-894-1403-101_ng.jpg` | `<category>/test/good` |
| 33 | `050812-0721-745-1438-101_ng.jpg` | `<category>/train/good` |
| 34 | `050812-2407-653-3306-101_ng.jpg` | `<category>/test/good` |
| 35 | `050812-4415-515-1846-101_ng.jpg` | `<category>/train/good` |
| 36 | `050814-2516-562-7784-101_ng.jpg` | `<category>/test/good` |
| 37 | `050814-2721-189-7981-101_ng.jpg` | `<category>/test/good` |
| 38 | `050814-2850-735-8108-101_ng.jpg` | `<category>/train/good` |
| 39 | `050814-3005-867-8212-101_ng.jpg` | `<category>/train/good` |
| 40 | `050814-3008-353-8214-101_ng.jpg` | `<category>/train/good` |
| 41 | `041610-1921-398-2692-101_ok.jpg` | `<category>/train/good` |
| 42 | `042616-1626-771-5075-101_ng.jpg` | `<category>/test/good` |
| 43 | `050809-4511-116-3063-101_ng.jpg` | `<category>/test/good` |
| 44 | `050810-0005-822-3735-101_ng.jpg` | `<category>/test/good` |
| 45 | `050811-1125-843-7111-101_ng.jpg` | `<category>/test/good` |
| 46 | `050814-3012-904-8222-101_ng.jpg` | `<category>/test/good` |
| 47 | `050815-0228-593-10976-101_ng.jpg` | `<category>/test/good` |

## Review Protocol

Five annotators reviewed the images independently. All annotators classified the 47 images as defective rather than normal.
