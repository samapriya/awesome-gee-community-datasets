# Brazilian Daily Weather Gridded Data(BR-DWGD) 1961-2020

The Comprehensive Brazilian Meteorological Gridded Dataset represents a significant advancement in meteorological research, addressing the growing demand for precise and extensive meteorological data. This dataset builds upon its predecessor by enhancing spatial resolution to 0.1° x 0.1° and expanding temporal coverage from January 1961 to July 2020. Incorporating elevation and temperature lapse rates, the dataset improves gridded interpolations for minimum and maximum temperatures, while also encompassing other crucial variables such as precipitation, solar radiation, wind speed, and relative humidity.

This dataset derives from a meticulous fusion of data from 11,473 rain gauges and 1,252 weather stations, enabling accurate interpolations. The selection of optimal interpolation methods, determined via ranked cross-validation statistics, underscores the dataset's commitment to precision. With two categories of gridded controls provided, researchers gain tools to assess interpolation accuracy against station data. As a comprehensive resource, the Comprehensive Brazilian Meteorological Gridded Dataset stands poised to catalyze advancements in climate, meteorology, and agricultural studies, offering nuanced insights for multifaceted scientific investigations.

These dataset presents the daily meteorological gridded data set from Brazil (BR-DWGD). The variables are Precipitation (pr, mm); maximum and minimum temperature (Tmax, tmin, °C); solar radiation (Rs, MJ/m2); relative humidity (RH, %); wind speed at 2 meters (u2, m/s) and evapotranspiration (ETo, mm). The temporal coverage is 1961/01/01-2020/07/31 (except precipitation: 1961/01/01-2022/12/31) and has the spatial resolution 0.1° x 0.1°, just for Brazil territory. You can find links to the dataset [here](https://sites.google.com/site/alexandrecandidoxavierufes/brazilian-daily-weather-gridded-data)

#### Dataset post processing
The datasets were provided as multiband netcdf files with each representing a single day since 1961 and then partitioned across 20 year intervals. There were then converted and split into single geotiff images and merged so they could be continious collections with about 21,762 images per collection except Precipitation which extends till 2022. The rain gauge and weather station location data was further added to the assets. The datasets must be scaled and offset should be applied to represent true values and they are included in the table below as well as the sample script.

|Variable|Variable name      |Units     |Offset|Scale      |
|--------|-------------------|----------|------|-----------|
|pr      |Precipitation      |mm        |255   |0.006866665|
|Eto     |evapotranspiration |mm        |0     |0.051181102|
|Tmax    |maximum temperature|C         |15    |0.001068148|
|Tmin    |minimum temperature|C         |15    |0.001068148|
|RH      |Relative humidity  |Percentage|0     |0.393700787|
|RS      |Solar radiation    |MJ/m2     |0     |0.157086614|
|U2      |Wind speed         |m/s       |0     |0.059055118|

#### Citation

```
Xavier, A. C., Scanlon, B. R., King, C. W., & Alves, A. I. (2022). New improved Brazilian daily weather gridded data (1961–2020).
International Journal of Climatology, 42( 16), 8390– 8404. https://doi.org/10.1002/joc.7731
```

![brazil_gridded_small](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/42738402-874c-47e5-bd6d-61af2ae6011e)

#### Earth Engine Snippet

```js
var ET = ee.ImageCollection("projects/sat-io/open-datasets/BR-DWGD/ET");
var PR = ee.ImageCollection("projects/sat-io/open-datasets/BR-DWGD/PR");
var RH = ee.ImageCollection("projects/sat-io/open-datasets/BR-DWGD/RH");
var RS = ee.ImageCollection("projects/sat-io/open-datasets/BR-DWGD/RS");
var TMAX = ee.ImageCollection("projects/sat-io/open-datasets/BR-DWGD/TMAX");
var TMIN = ee.ImageCollection("projects/sat-io/open-datasets/BR-DWGD/TMIN");
var U2 = ee.ImageCollection("projects/sat-io/open-datasets/BR-DWGD/U2");
var RAIN_GAUGES = ee.FeatureCollection("projects/sat-io/open-datasets/BR-DWGD/RAIN_GAUGES");
var WEATHER_STATIONS = ee.FeatureCollection("projects/sat-io/open-datasets/BR-DWGD/WEATHER_STATIONS");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/BR-DWDG-EXAMPLE


#### License
The datasets are provided under a Attribution 4.0 International (CC BY 4.0) license.

Provided by: Xavier, A. C. et al

Curated in GEE by : Samapriya Roy

Keywords: Brazil, maximum temperature, minimum temperature, precipitation, solar radiation, wind speed, relative humidity, evapotranspiration
