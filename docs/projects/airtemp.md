# Global Daily near-surface air temperature

Near-surface air temperature (Ta) is a key variable in global climate studies. A global gridded dataset of daily maximum and minimum Ta (Tmax and Tmin) is particularly valuable and critically needed in the scientific and policy communities. Zhang et al. (2022) developed a global dataset of daily Tmax and Tmin at 1-km resolution over land (50° S–79° N) through the combined use of station-based ground Ta measurements and satellite observations (i.e., digital elevation model, and land surface temperature) via a state-of-the-art statistical method named Spatially Varying Coefficient Models with Sign Preservation (SVCM-SP). The published dataset covered 2003–2020 and has since been extended, so the collection now spans **2003 to 2024**.

This gridded 1 km resolution global (50° S ~ 79° N) daily maximum and minimum near-surface air temperature dataset (2003–2024) was generated using a seamless 1 km resolution land surface temperature dataset, a 30-arc second (~1 km) resolution digital elevation model (DEM) data, and air temperature observations at weather stations and a spatially varying coefficient model with sign preservation (SVCM-SP) algorithm. The gridded air temperature dataset is of great use in global studies of urban, climate, and hydrology.

Reported accuracies from the 10-fold cross-validation in the source publication give root mean square errors ranging from 1.20 to 2.44 °C for Tmax and 1.69 to 2.39 °C for Tmin, with accuracy affected primarily by land cover type, elevation range, and climate background.

You can read the [published paper here](https://doi.org/10.5194/essd-14-5637-2022) and [download the datasets here](https://iastate.figshare.com/collections/A_global_1_km_resolution_daily_near-surface_air_temperature_dataset_2003_2020_/6005185)

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Data preprocessing

The datasets were generated regionally and for tmax and tmin. The tmax and tmin were combined into a single collection for the regions generated. Additional metadata called "prop_type" was added to allow for filtering along with other metadata like the day of year and the actual date information for date based filtering. The source data are distributed as GeoTIFFs in the MODIS ellipse sinusoidal projection at 1 km, with temperature stored in units of 0.1 °C; the datasets were projected to EPSG 4326 before being ingested to Google Earth Engine.

#### Citation

```
Zhang, T., Zhou, Y., Zhao, K., Zhu, Z., Chen, G., Hu, J., and Wang, L.: A global dataset of daily maximum and minimum
near-surface air temperature at 1 km resolution over land (2003-2020), Earth Syst. Sci. Data, 14, 5637-5649,
https://doi.org/10.5194/essd-14-5637-2022, 2022.
```

#### Dataset Citation

```
Zhang, Tao; Zhou, Yuyu (2022): A global 1 km resolution daily near-surface air temperature dataset (2003-2020).
Iowa State University. Collection. https://doi.org/10.25380/iastate.c.6005185.v1
```

![airtemp_daily](https://user-images.githubusercontent.com/6677629/183010148-ca435956-a295-47c7-8a84-f4e00fb9b9a2.gif)

#### Earth Engine Snippet

```js
var africa = ee.ImageCollection("projects/sat-io/open-datasets/global-daily-air-temp/africa");
var australia = ee.ImageCollection("projects/sat-io/open-datasets/global-daily-air-temp/australia");
var eurasia = ee.ImageCollection("projects/sat-io/open-datasets/global-daily-air-temp/europe_asia");
var latin_america = ee.ImageCollection("projects/sat-io/open-datasets/global-daily-air-temp/latin_america");
var north_america = ee.ImageCollection("projects/sat-io/open-datasets/global-daily-air-temp/north_america");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/GLOBAL-DAILY-NEAR-SURFACE-AIR-TEMP

#### License

These datasets are made available under the CC BY 4.0 Attribution 4.0 International license. This license allows users to distribute, remix, adapt,
and build upon the material in any medium or format, so long as attribution is given to the creator.

Created by: Zhang, T., Zhou, Y., Zhao, K., Zhu, Z., Chen, G., Hu, J., and Wang, L.

Curated in GEE by : Samapriya Roy

keywords: Air Temperature, land surface temperature (LST), SVCM-SP, MODIS, Global

Last updated on GEE: 2026-08-02
