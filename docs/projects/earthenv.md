# EarthEnv Global 1-km Cloud Frequency Version 1

The Cloud Cover Frequency dataset v1.0 measures over 15 years of twice daily MODIS images to analyze and quantify cloud dynamics and cloud predictions over areas. This allows us to understand global cloud heterogeneity over a spatial and temporal scale. The study establises a baseline for temporal variability of cloud forest, dynamics and allows for users to determine temporal windows of imaging and cloud free snapshots. The complete description of the project can be [found here](http://www.earthenv.org/cloud).

Please use Citation:

```
Wilson AM, Jetz W (2016) Remotely Sensed High-Resolution Global Cloud Dynamics for Predicting Ecosystem and Biodiversity Distributions. PLoS Biol 14(3):
e1002415. doi:10.1371/journal. pbio.1002415
```

Shared Under: Creative Commons Attribution-Non Commercial 4.0 International License.

![global_cloud](https://user-images.githubusercontent.com/6677629/82632583-a9a1bb00-9bc6-11ea-831e-4c2af068583d.gif)

#### Earth Engine Snippet
```js
//EarthEnv Cloud Frequency v1.0
var cloud_forest_prediction = ee.Image("projects/sat-io/open-datasets/gcc/MODCF_CloudForestPrediction");
var interannual_sd = ee.Image("projects/sat-io/open-datasets/gcc/MODCF_interannualSD");
var intrannual_sd = ee.Image("projects/sat-io/open-datasets/gcc/MODCF_intraannualSD");
var mean_annual = ee.Image("projects/sat-io/open-datasets/gcc/MODCF_meanannual");
var monthly_mean = ee.ImageCollection("projects/sat-io/open-datasets/gcc/MODCF_monthlymean");
var seasonality_concentration = ee.Image("projects/sat-io/open-datasets/gcc/MODCF_seasonality_concentration");
var seasonality_rgb = ee.Image("projects/sat-io/open-datasets/gcc/MODCF_seasonality_rgb");
var seasonality_theta = ee.Image("projects/sat-io/open-datasets/gcc/MODCF_seasonality_theta");
var seasonality_visct = ee.Image("projects/sat-io/open-datasets/gcc/MODCF_seasonality_visct");
var spatial_sd_1deg = ee.Image("projects/sat-io/open-datasets/gcc/MODCF_spatialSD_1deg");
```

Project Website: http://www.earthenv.org/cloud

App Website: [App link here](https://earthenv-dot-map-of-life.appspot.com/4/20.650/15.675?collections=cloud&layers=Seasonality)

Metadata link: http://www.earthenv.org/metadata/Cloud_DataDescription.pdf

Curated by: Samapriya Roy

Created by: [Wilson AM, Jetz W 2016](http://www.earthenv.org/cloud)

Keywords: Earthenv, cloud concentration, seasonality, MODIS, Global Cloud

Last updated: [Refer to webpage](http://www.earthenv.org/cloud)
