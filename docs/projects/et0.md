# Global Reference Evapotranspiration Layers

The Global Aridity Index (Global-Aridity_ET0) and Global Reference Evapotranspiration (Global-ET0) Version 3 dataset provides high-resolution (30 arc-seconds) global raster climate data for the 1970-2000 period, related to evapotranspiration processes and rainfall deficit for potential vegetative growth, based upon the implementation of a Penman Monteith Evapotranspiration equation for reference crop. The dataset follows the development and is based upon the [WorldClim 2.1](https://www.worldclim.org/data/worldclim21.html) at 30 arc seconds or ~ 1km at the equator. You can read the [paper here](https://www.nature.com/articles/s41597-022-01493-1).

Potential Evapo-Transpiration (PET) is a measure of the ability of the atmosphere to remove water through Evapo-Transpiration (ET) processes. Among several equations to estimate PET, a FAO application of the Penman-Monteith equation (Allen et al. 1998), here referred as FAOPM, is currently widely considered as a standard method (Walter et al. 2000). The FAO introduced the definition of PET as the ET of a reference crop (ET0) under optimal conditions, having the characteristics of well-watered grass with an assumed height of 12 centimeters, a fixed surface resistance of 70 seconds per meter and an albedo of 0.23 (Allen et al. 1998). The FAO-PM is a predominately physically based approach, which can be used globally because it does not require estimations of additional site-specific parameters. However, a major drawback of the FAO-PM method is its relatively high need for specific data for a variety of parameters
(i.e. windspeed, relative humidity, solar radiation, etc.).

#### Data citation

```
Zomer, Robert; Trabucco, Antonio (2019): Global Aridity Index and Potential Evapotranspiration (ET0) Database: Version 3.
figshare. Dataset. https://doi.org/10.6084/m9.figshare.7504448.v6
```

#### Paper citation

```
Zomer, R.J.; Xu, J.;  Trabuco, A. 2022. Version 3 of the Global Aridity Index and Potential Evapotranspiration Database.
Scientific Data 9, 409. https://www.nature.com/articles/s41597-022-01493-1
```

![et_v3](https://user-images.githubusercontent.com/6677629/188240636-221716c2-0dcc-4036-acd6-f336efa374a6.gif)


Global-ET0 grid layers are available as monthly averages (12 data layers, i.e. one layer for each month) or as an annual average (1 data layer)  as well as standard deviation for annual average for the 1970-2000 period.

#### Earth Engine Snippet

```js
var et_monthly = ee.ImageCollection("projects/sat-io/open-datasets/global_et0/global_et0_monthly");
var et_yearly = ee.Image("projects/sat-io/open-datasets/global_et0/global_et0_yearly");
var et_yearly_sd = ee.Image("projects/sat-io/open-datasets/global_et0/global_et0_yearly_sd");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/GLOBAL-ET0

#### License

The Global-Aridity_ET0 and Global-ET0 datasets are provided for non-commercial use under the CC BY 4.0 Attribution 4.0 International license.

Data Website: You can download the [data and description here](https://figshare.com/articles/dataset/Global_Aridity_Index_and_Potential_Evapotranspiration_ET0_Climate_Database_v2/7504448/6)

Curated in GEE by: Samapriya Roy

Keywords: aridity index, evapotranspiration, geospatial modeling

Last updated: 2022-09-02
