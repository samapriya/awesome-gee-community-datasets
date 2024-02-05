# 30m Global Annual Burned Area Maps (GABAM)

Heretofore, global Burned Area (BA) products have only been available at coarse spatial resolution, since most of the current global BA products are produced with the help of active fire detection or dense time-series change analysis, which requires very high temporal resolution. In this study, however, we focus on an automated global burned area mapping approach based on Landsat images. By utilizing the huge catalog of satellite imagery, as well as the high-performance computing capacity of Google Earth Engine, we propose an automated pipeline for generating 30-m resolution global-scale annual burned area maps from time-series of Landsat images, and a novel 30-m resolution Global annual Burned Area Map of 2015 (GABAM 2015) was released.

30 m resolution global annual burned area maps (GABAM) of 1990-2021 are released for free download. The annual burned area map is defined as spatial extent of fires that occurs within a whole year and not of fires that occurred in previous years. GABAM was generated via an automated pipeline based on Google Earth Engine (GEE), using all the available Landsat images on GEE platform. The product was projected in a Geographic (Lat/Long) projection at 0.00025 degree​​ (approximately 30 meters) resolution, with the WGS84 horizontal datum and the EGM96 vertical datum, consisting of 10 degree × 10 degree tiles spanning the range 180W–180E and 80N–60S.

You can get links to [download the data here](https://vapd.gitlab.io/post/gabam/)

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.


#### Paper Citation

```
Long, Tengfei, Zhaoming Zhang, Guojin He, Weili Jiao, Chao Tang, Bingfang Wu, Xiaomei Zhang, Guizhou Wang, and Ranyu Yin. 2019. "30 m Resolution Global Annual
Burned Area Mapping Based on Landsat Images and Google Earth Engine" Remote Sensing 11, no. 5: 489. https://doi.org/10.3390/rs11050489
```
#### Data Citation

```
Long Tengfei; Zhang Zhaoming; He Guojin, 2021, "30 m Resolution Global Annual Burned Area Product", https://doi.org/10.7910/DVN/3CTMKP, Harvard Dataverse, V1
```

#### Data preprocessing

Tile names were modified to attach _year to allow for name based sorting as well as start and end year dates were added to each image in the collection.

Note: **The user did notice that some 8 years of datasets were missing or not provided by the author such as 1986,1988,1990,1991,1993,1994,1997,1999**


![gabam_small](https://user-images.githubusercontent.com/6677629/185780108-5a610321-54d4-4c1f-afaf-a81ffb4b6583.gif)

#### Earth Engine Snippet

```js
var gabam = ee.ImageCollection("projects/sat-io/open-datasets/GABAM");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:fire-monitoring-analysis/GLOBAL-ANNUAL-BURNED-AREA-MAPS

#### License

These datasets are made available under the CC0 1.0 Universal (CC0 1.0) Public Domain Dedication. You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission. See Other [Information here](https://doi.org/10.7910/DVN/3CTMKP).


#### Changelog
* Added 2020 and 2021 to the collection and collection has been updated.

Created by: Long Tengfei; Zhang Zhaoming; He Guojin

Curated in GEE by : Samapriya Roy

keywords: Global Fire, burned area, GABAM, remote sensing, Earth Engine

Last modified: 2022-07-14

Last updated on GEE: 2024-02-04
