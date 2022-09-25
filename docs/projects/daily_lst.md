# MODIS Gap filled Long-term Land Surface Temperature Daily (2003-2020)

High spatiotemporal land surface temperature (LST) datasets are increasingly needed in a variety of fields such as ecology, hydrology, meteorology, epidemiology, and energy systems. In this study the authors developed a novel spatiotemporal gap-filling framework by implementing data preprocessing (filtering pixels with low data quality and gap-filling missing values at one overpass using values at one of the other three overpasses each day) and spatiotemporal fitting (filtering the long-term trend (overall mean) of observations in each pixel, and then spatiotemporally interpolating residuals between observations and overall mean values for each day, and finally adding the overall mean and interpolated residuals), to generate a seamless high spatiotemporal LST dataset using the four daily LST observations from the two MODIS instruments on Terra and Aqua satellites. The paper on the gap-filling method will be published in near future.

The method was implemented to create a global gap filled LST observation.. The cross-validation indicates that the average root mean squared error (RMSE) for mid-daytime (1:30pm) and mid-nighttime (1:30am) LST is 1.88K and 1.33K, respectively. The gap-filled LST in the unit of 0.1 Celsius temperature (0.1 degree C) .You can read the [abstract here](https://ui.adsabs.harvard.edu/abs/2020AGUFMGC127..01Z/abstract)

The datasets and entire collection is [available at Figshare](https://iastate.figshare.com/collections/A_global_seamless_1_km_resolution_daily_land_surface_temperature_dataset_2003_2020_/5078492).


#### Citation

**Paper Citation**

```
Li, Xiaoma, Yuyu Zhou, Ghassem R. Asrar, and Zhengyuan Zhu. "Creating a seamless 1 km resolution daily land surface
temperature dataset for urban and surrounding areas in the conterminous United States." Remote Sensing of
Environment 206 (2018): 84-97.
```

**Abstract Citation**

```
Zhang, Tao, Yuyu Zhou, and Zhengyuan Zhu. "A spatiotemporal gap-filling method for building a seamless MODIS land
surface temperature dataset." In AGU Fall Meeting Abstracts, vol. 2020, pp. GC127-01. 2020.
```

**Collection Citation**

```
Zhang, Tao; Zhou, Yuyu; Zhu, Zhengyuan; Li, Xiaoma; Asrar, Ghassem (2021): A global seamless 1 km resolution daily
land surface temperature dataset (2003 – 2020). Iowa State University. Collection. https://doi.org/10.25380/iastate.c.5078492.v1
```

![daytime_lst](https://user-images.githubusercontent.com/6677629/135794725-54341b20-f00e-4937-928c-c87fad3f08d8.gif)

#### Earth Engine Snippet Climate variables

```js
var gf_day_1km = ee.ImageCollection("projects/sat-io/open-datasets/gap-filled-lst/gf_day_1km");
var gf_night_1km = ee.ImageCollection("projects/sat-io/open-datasets/gap-filled-lst/gf_night_1km");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/MODIS-GAPFILLED-LST-DAILY

#### License
These datasets  are made available under the CC BY 4.0 Attribution 4.0 International license. This license allows users to distribute, remix, adapt, and build upon the material in any medium or format, so long as attribution is given to the creator.

Created by: Zhang, Tao; Zhou, Yuyu; Zhu, Zhengyuan; Li, Xiaoma; Asrar, Ghassem

Curated in GEE by: Samapriya Roy

Keywords: Land Surface Temperature, LST, MODIS, gapfilled

Last updated: 2021-10-03
