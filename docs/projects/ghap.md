# Global High Air Pollutants(GHAP) PM2.5 Concentrations (2017-2022)

This dataset is the first big data-derived gapless (100% spatial coverage) daily, monthly, and annual PM2.5 concentration product at 1km resolution (D1K, M1K, and Y1K) for global land areas from 2017 to 2022 and part of Global High Air Pollutants Dataset (GHAP). Leveraging machine learning and big data techniques, the dataset provides unprecedented insights into the spatiotemporal variability of PM2.5 pollution.  **In particular, it reveals extensive exposure to unhealthy air globally, identifies disparities in exposure between developed/developing countries, urban/rural areas, and within cities, captures the impact of events like COVID-19 lockdowns on air quality, and provides insights into nature-induced pollution episodes (e.g., biomass burning).** The dataset boasts high quality, with a cross-validation coefficient of determination (CV-R2) of 0.91 and a root-mean-square error (RMSE) of 9.20 µg m-3 on the daily basis.

| **Data Coverage:**     | **Variables:**             | **Scaling factor** |
|------------------------|----------------------------|-------------------|
| *Temporal:* Daily data from 2017 to 2022 | *PM2.5 concentration (μg/m³)* | *0.1* |
| *Spatial:* Global coverage (land areas) | | |

#### Citation

```
Wei, J., Li, Z., Lyapustin, A., Wang, J., Dubovik, O., Schwartz, J., Sun, L., Li, C., Liu, S., and Zhu, T. First close insight into global daily gapless 1 km PM2.5 pollution, variability, and health impact. Nature Communications, 2023, 14, 8349. https://doi.org/10.1038/s41467-023-43862-3
```

#### Dataset Citation

**Dataset citations are available based on the year and how the releases were packaged. You can find [them all here](https://zenodo.org/communities/ghap/records) and find an example below**

```
Wei, J., & Li, Z. (2024). GlobalHighPM2.5 (2022) (Version 1) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.10795662
```

![ghap_monthly](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/0ff89c06-75d5-4c67-a1ec-b865fffca2be)

#### Earth Engine Snippet

```js
var GHAP_DAILY = ee.ImageCollection("projects/sat-io/open-datasets/GHAP/GHAP_D1K_PM25");
var GHAP_MONTHLY = ee.ImageCollection("projects/sat-io/open-datasets/GHAP/GHAP_M1K_PM25");
var GHAP_YEARLY = ee.ImageCollection("projects/sat-io/open-datasets/GHAP/GHAP_Y1K_PM25");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/GHAP-DATASETS

#### License
These datasets are licensed under a Creative Commons Attribution 4.0 International license.

Provided by: Wei et al

Curated in GEE by: Samapriya Roy

Keywords: PM2.5, Pollutants, Air Quality, Air Pollutants, GHAP

Last updated in GEE: 2024-06-09
