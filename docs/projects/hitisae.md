# High-spatial-resolution Thermal-stress Indices over South and East Asia (HiTiSAE)

This newly developed dataset is a high-spatial-resolution (0.1°×0.1°) gridded product that contains the daily values of the indoor, outdoor shaded and outdoor unshaded UTCI, the MRT and eight other widely adopted human thermal-stress indices (ESI, HI, Humidex, WBGT, WBT, WCT, AT, NET), derived from the newly available ECMWF ERA5-Land and ERA5 reanalysis products, over South and East Asia from Jan 3, 1981 to Dec 31, 2019. You can [read the complete article here](https://www.nature.com/articles/s41597-021-01010-w.pdf). This high-spatial-resolution database of human thermal stress indices over South and East Asia (HiTiSEA), which contains the daily mean, maximum, and minimum values of UTCI, MRT, and eight other widely adopted indices, is suitable for both indoor and outdoor applications and allows researchers and practitioners to investigate the spatial and temporal evolution of human thermal stress and its impacts on densely populated regions over South and East Asia at a fner scale. The dataset is available for download via a Figshare collection which [can be found here](https://springernature.figshare.com/collections/A_High-spatial-resolution_Dataset_of_Human_Thermal_Stress_Indices_over_South_and_East_Asia/5196296)


#### Paper Citation

```
Yan, Yechao, Yangyang Xu, and Shuping Yue. "A high-spatial-resolution dataset of human thermal stress indices over South and East Asia."
Scientific Data 8, no. 1 (2021): 1-14.
```

#### Dataset Citation

```
Yan, Yechao; Xu, Yangyang; Yue, Shuping (2021): A High-spatial-resolution Dataset of Human Thermal Stress Indices over South and East Asia.
figshare. Collection. https://doi.org/10.6084/m9.figshare.c.5196296
```

#### Data Preprocessing for GEE
The dataset contains 14242 daily NetCDF files which are archived by month and compressed into tar.gz files with a total volume of 450 GB. The netcdf files for each subvariable was converted into Geotifs with Minimum, Mean and Maximum value for each parameter. To reduce the overall index size, a band order was constructed with b1, b2,b3 for each variable coresponding to Min, Mean and Maximum value for the same parameter.

For example HiTiSea_1981-01-03_AT contains 3 bands with b1 with AT_min, b2 as AT_mean and b3 as AT_max

Included indices, names and GEE Variable are included in the table below

|Termal Indices       |Full Name of the Indices           |GEE Variable|Variable Stats|
|---------------------|-----------------------------------|------------|--------------|
|UTCI                 | universal thermal climate index   |UTCI        |Min,Mean, Max |
|indoor UTCI (UTCI2)  | UTCI for indoor environment       |UTCI2       |Min,Mean, Max |
|outdoor shaded(UTCI3)| UTCI UTCI for outdoor shaded space|UTCI3       |Min,Mean, Max |
|MRT                  | mean radiant temperature          |MRT         |Min,Mean, Max |
|ESI                  | environment stress index          |ESI         |Min,Mean, Max |
|HI                   | heat index                        |HI          |Min,Mean, Max |
|Humidex              | humidity index                    |Humidex     |Min,Mean, Max |
|WBGT                 | wet-bulb globe temperature        |WBGT        |Min,Mean, Max |
|WBT                  | wet bulb temperature              |WBT         |Min,Mean, Max |
|WCT                  | wind chill temperature            |WCT         |Min,Mean, Max |
|AT                   | apparent temperature              |AT          |Min,Mean, Max |
|NET                  | net efective temperature          |NET         |Min,Mean, Max |


![HiTiSAE](https://user-images.githubusercontent.com/6677629/140878970-6164d58d-1c60-4e81-b119-b88ed454dda0.gif)


#### Earth Engine Snippet

```js
var AT = ee.ImageCollection("projects/sat-io/open-datasets/HITISEA/AT");
var ESI = ee.ImageCollection("projects/sat-io/open-datasets/HITISEA/ESI");
var MRT = ee.ImageCollection("projects/sat-io/open-datasets/HITISEA/MRT");
var UTCI = ee.ImageCollection("projects/sat-io/open-datasets/HITISEA/UTCI");
var UTCI2 = ee.ImageCollection("projects/sat-io/open-datasets/HITISEA/UTCI2");
var UTCI3 = ee.ImageCollection("projects/sat-io/open-datasets/HITISEA/UTCI3");
var HI = ee.ImageCollection("projects/sat-io/open-datasets/HITISEA/HI");
var Humidex = ee.ImageCollection("projects/sat-io/open-datasets/HITISEA/Humidex");
var WBGT = ee.ImageCollection("projects/sat-io/open-datasets/HITISEA/WBGT");
var WBT = ee.ImageCollection("projects/sat-io/open-datasets/HITISEA/WBT");
var WCT = ee.ImageCollection("projects/sat-io/open-datasets/HITISEA/WCT");
var NET = ee.ImageCollection("projects/sat-io/open-datasets/HITISEA/NET");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/HIGHRES-THERMAL-STRESS-INDICES


#### License
This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Created by: Yechao Yan; Yangyang Xu; Shuping Yue

Preprocessed and Curated in GEE by : Samapriya Roy

Keywords: thermal-stress indices, south and southeast asia, heat index, humidity index, wind chill, apparent temperature

Last updated: 2021-05-20

Last updated on GEE: 2021-11-08
