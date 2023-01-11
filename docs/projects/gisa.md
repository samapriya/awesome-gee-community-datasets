# Global Impervious Surface Area (1972-2019)

Using more than three million Landsat satellite images, this research developed the first global impervious surface area (GISA) dataset from 1972 to 2019. Based on 120,777 independent and random reference sites from 270 cities all over the world, the omission error, commission error, and F-score of GISA are 5.16%, 0.82%, and 0.954, respectively. Compared to the existing global datasets, the merits of GISA include: (1) it provided the global ISA maps before the year of1985, and showed the longest time span (1972–2019), and the highest accuracy (in terms of a large number of randomly selected and third-party validation sample sets); (2) it presented a new global ISA mapping method, including a semi-automatic global sample collection, a locally adaptive classification strategy, and a spatio-temporal post-processing procedure; and (3) it extracted ISA from the whole global land area (not from an urban mask) and hence reduced the underestimation. The GISA can contribute to further understanding on the human's utilization and reformation to nature during the past half century.

Pixel values in each map indicate the first year when ISA was detected. No-data was labeled as 0. A look-up table for the detected year and pixel value is provided as follow:

year of first ISA:[1972, 1978, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

pixel value[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37]


You can [download the dataset here](https://zenodo.org/record/5136330)

You can read about the [methodology in the paper here](https://doi.org/10.1007/s11430-020-9797-9)

#### Citation

```
Huang, X., Li, J., Yang, J. et al. 30 m global impervious surface area dynamics
and urban expansion pattern observed by Landsat satellites: From 1972 to 2019.
Sci. China Earth Sci. (2021). https://doi.org/10.1007/s11430-020-9797-9
```

#### Data Citation

```
Xin Huang, Jiayi Li, Jie Yang, Zhen Zhang, Dongrui Li, & Xiaoping Liu. (2021).
30 m global impervious surface area dynamics and urban expansion pattern observed
by Landsat satellites: from 1972 to 2019 (Version 1.0.0)
[Data set]. http://doi.org/10.1007/s11430-020-9797-9
```

![gisa](https://user-images.githubusercontent.com/6677629/127800833-db1b8f0a-3d71-43fa-9337-0526187dd860.gif)

#### Earth Engine Snippet

```js
var gisa = ee.ImageCollection("projects/sat-io/open-datasets/GISA_1972_2019");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/GLOBAL-IMPERVIOUS-SURFACE-AREA

#### License
This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Created by : Xin Huang, Jiayi Li, Jie Yang, Zhen Zhang, Dongrui Li, & Xiaoping Liu

Curated in GEE by: Samapriya Roy

Keywords: Landsat, Urban, Google Earth Engine, Impervious area, Urban expansion

Last updated : 2021-08-01
