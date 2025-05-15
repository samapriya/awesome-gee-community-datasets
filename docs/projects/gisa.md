# Global Impervious Surface Area (1972-2021)

The Global Impervious Surface Area (GISA) dataset provides comprehensive 30-meter resolution mapping of impervious surfaces worldwide. The latest version, GISA-new (1972-2021), addresses omission and commission errors in previous versions by implementing advanced algorithms including a multi-temporal Continuous Change Detection and Classification (NA-CCDC) method and a multi-scale iterative algorithm (MIA). With these improvements, GISA-new achieves the highest overall accuracy (93.12%), lowest omission errors (10.50%), and lowest commission errors (3.52%) among global ISA datasets.

GISA was originally developed using more than three million Landsat satellite images. The original version (1972-2019) provided global ISA maps with a time span from 1972–2019 and achieved high accuracy (F-score of 0.954). The new version extends coverage to 2021 and significantly improves accuracy in challenging areas including rural and arid regions.

!!! info

    **GISA-new Improvements:**

    - Reduced omission errors in low-density impervious surfaces (rural, suburban areas)
    - Removed commission errors from spectrally similar surfaces (bare soil, water bodies)
    - Improved accuracy in challenging regions (arid landscapes, rural settlements)
    - Expanded temporal coverage to 2021
    - Enhanced consistency across the time series

![gisa](https://user-images.githubusercontent.com/6677629/127800833-db1b8f0a-3d71-43fa-9337-0526187dd860.gif)

#### Dataset Details

| Characteristic  | Description                                                   |
|-----------------|---------------------------------------------------------------|
| Name            | GISA and GISA-new                                             |
| Provider        | Wuhan University                                              |
| Resolution      | 30 meters                                                     |
| Coverage        | Global                                                        |
| Temporal Range  | 1972-2019 (GISA), 1985-2021 (GISA-new)                        |
| Accuracy        | Overall accuracy: 93.12% (GISA-new)                           |
| Data Structure  | Pixel values indicate first year when ISA was detected        |
| No-data value   | 0                                                             |

For GISA (1972-2019), pixel values correspond to the first year of ISA detection according to this lookup table:

| Year | Pixel Value | Year | Pixel Value | Year | Pixel Value |
|------|-------------|------|-------------|------|-------------|
| 1972 | 1           | 1992 | 10          | 2008 | 26          |
| 1978 | 2           | 1993 | 11          | 2009 | 27          |
| 1985 | 3           | 1994 | 12          | 2010 | 28          |
| 1986 | 4           | 1995 | 13          | 2011 | 29          |
| 1987 | 5           | 1996 | 14          | 2012 | 30          |
| 1988 | 6           | 1997 | 15          | 2013 | 31          |
| 1989 | 7           | 1998 | 16          | 2014 | 32          |
| 1990 | 8           | 1999 | 17          | 2015 | 33          |
| 1991 | 9           | 2000 | 18          | 2016 | 34          |
|      |             | 2001 | 19          | 2017 | 35          |
|      |             | 2002 | 20          | 2018 | 36          |
|      |             | 2003 | 21          | 2019 | 37          |
|      |             | 2004 | 22          |      |             |
|      |             | 2005 | 23          |      |             |
|      |             | 2006 | 24          |      |             |
|      |             | 2007 | 25          |      |             |

#### Data Access
- [Download updated GISA (1972-2021)](https://zenodo.org/records/14848113)

#### Citation

```
Huang, X., Li, J., Yang, J. et al. 30 m global impervious surface area dynamics
and urban expansion pattern observed by Landsat satellites: From 1972 to 2019.
Sci. China Earth Sci. (2021). https://doi.org/10.1007/s11430-020-9797-9

Ren, H., Huang, X., Yang, J., & Zhou, G. (2025). Improving 30-meter global impervious
surface area (GISA) mapping: New method and dataset. ISPRS Journal of Photogrammetry
and Remote Sensing, 220, 354-376. https://doi.org/10.1016/j.isprsjprs.2024.12.023
```

#### Data Citation

```
Xin Huang, Jiayi Li, Jie Yang, Zhen Zhang, Dongrui Li, & Xiaoping Liu. (2021).
30 m global impervious surface area dynamics and urban expansion pattern observed
by Landsat satellites: from 1972 to 2019 (Version 1.0.0)
[Data set]. http://doi.org/10.1007/s11430-020-9797-9

Huiqun, R., Xin, H., Jie, Y., & Guoqing, Z. (2024). Improving 30-meter global impervious
surface area (GISA) mapping: New method and dataset [Data set].
Zenodo. https://doi.org/10.5281/zenodo.14848113
```

#### Earth Engine Snippet

```javascript
var gisa = ee.ImageCollection("projects/sat-io/open-datasets/GISA_1972_2021");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/GLOBAL-IMPERVIOUS-SURFACE-AREA

#### License

This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to
transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Created by: Xin Huang, Huiqun Ren, Jie Yang, Guoqing Zhou, and collaborators at Wuhan University

Curated in GEE by: Samapriya Roy

Keywords: Landsat, Urban, Google Earth Engine, Impervious surface, Urban expansion, Time series, Urbanization, Sustainable development

Last updated: 2025-05-15
