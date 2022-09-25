# Soil carbon storage in terrestrial ecosystems of Canada

This collection contains datasets with the spatial distribution of carbon stock in soil and plants of Canada and canopy heights. It is being made public to act as supplementary data for the publication 'Large soil carbon storage in terrestrial ecosystems of Canada', currently under review.
The maps were produced in the Remote Sensing Lab, McMaster University, between January and December 2020. This research project was made possible by a grant from the World Wildlife Fund (WWF)- Canada. This project aimed to produce the first wall-to-wall estimate of carbon stocks in plants and soils of Canada at 250 m spatial resolution using multisource satellite, climate and topographic data and a machine-learning algorithm.

You can read the [paper here](https://doi.org/10.1029/2021GB007213) and download the datasets:

- Spatial distribution of maximum canopy height and heights percentiles (https://doi.org/10.4121/14573079.v1)
- Forest carbon stock and uncertainty maps (https://data.4tu.nl/articles/dataset/Carbon_map_and_uncertainty_in_forested_areas_of_Canada_250m_spatial_resolution/14572929/2)
- Soil carbon stock and uncertainty maps (https://doi.org/10.4121/16686154.v3)


#### Dataset descriptors

**Canopy Height Map**
The canopy height maps were built to be included as covariates in the model to predict AGB (and carbon stock) in forest areas of Canada. We created wall-to-wall height metrics using ATL08 LiDAR products from the ICESat-2 satellite. The data was download for one-year period (October 2018 to October 2019). Points were filtered regarding solar background noise and atmospheric scattering, totaling 49,959 points distributed over the entire Canada. These points were associated with 10 ancillary variables primarily corresponding to structure information, such as seasonal Sentinel-1 VV and VH polarization, annual PALSAR-2 HH and HV polarization, annual clumping index, and also the MODIS NDVI summer season. Afterwards, the random forest algorithm was used to extrapolate ATL08 parameters and develop regression models with the abovementioned spatially continuous variables.

**Soil Carbon Concentration**
To generate the soil carbon concentration maps, we used 6,533 ground soil samples, long-term climate data, multisource remote sensing data, topografic information, soil type, depth, and a 3D random forest regression model.

**Forest Carbon**
This dataset contains the map with total carbon stored in plants of forested areas in Canada (AGB, BGB and dead plants) and carbon stock uncertainty. To estimate the carbon stored in plants of forest areas, we used 47,967 ground measurements of AGB and 58 covariates mainly composed of optical data, terrain parameters, structural parameters (e.g., SAR data, clump index, canopy heights – generated from satellite LiDAR- included in the other dataset), soil type map and radiation flux data. We used a random forest model for spatial prediction of AGB in forest areas while 1st and 3rd quantiles of RF quantile regression were used to build the uncertainty map. After generating the AGB map, the root biomass of forest areas was computed by its relationship to AGB according to forest type. The dead plant materials were computed by a linear regression between live and dead AGB defined with ground measurements. Ultimately, the AGB as well as dead plant materials and BGB were multiplied by 0.5 to provide the carbon maps. *includes carbon stored in above and belowground biomass and dead plant materials*

**Soil Carbon Stock Map**
To generate the soil carbon stock map, we used 6,490 ground samples of soil organic carbon concentration (g/kg) and 2,973 ground samples of bulk density (kg/dm3), long-term climate data, multisource remote sensing data, topografic information, soil type, depth, and a 3D random forest regression model. The uncertainty map was generated using the random forest quantile regression approach difference between 95th and 5th quantiles (90% confidence interval) of soil organic carbon and bulk density predictions. Water and ice/snow areas were masked based on the [2015 Land Cover of Canada](https://open.canada.ca/data/en/dataset/4e615eae-b90c-420b-adee-2ca35896caf6) and SOC stock in permafrost areas was discounted according to ice abundance using the ['Ground ice map of Canada' (O'Neill et al., 2020)](https://doi.org/10.4095/326885).

|GEE asset                                         |Variable name            |
|--------------------------------------------------|-------------------------|
|projects/sat-io/open-datasets/carbon_stocks_ca/ch |Canopy Height            |
|projects/sat-io/open-datasets/carbon_stocks_ca/fc |Forest Carbon            |
|projects/sat-io/open-datasets/carbon_stocks_ca/sc |Soil Carbon Stock        |
|projects/sat-io/open-datasets/carbon_stocks_ca/scc|Soil Carbon Concentration|


#### Data Citation

```
Sothe, C., Gonsamo, A., Arabian, J., Kurz, W. A., Finkelstein, S. A., & Snider, J. (2022). Large soil carbon storage in terrestrial ecosystems of Canada. Global Biogeochemical Cycles, 36, e2021GB007213. https://doi.org/10.1029/2021GB007213
```

![ca_carbon](https://user-images.githubusercontent.com/6677629/141673532-bfd657f7-941a-4687-948e-fab97102908b.gif)


#### Earth Engine Snippet

```js
var ch = ee.ImageCollection("projects/sat-io/open-datasets/carbon_stocks_ca/ch");
var fc = ee.ImageCollection("projects/sat-io/open-datasets/carbon_stocks_ca/fc");
var sc = ee.ImageCollection("projects/sat-io/open-datasets/carbon_stocks_ca/sc");
var scc = ee.ImageCollection("projects/sat-io/open-datasets/carbon_stocks_ca/scc");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:geophysical-biological-biogeochemical/SOIL-CARBON-STOCKS-CANADA


#### License
This work is licensed under and freely available to the public (similar to a CC0 license).

Created by: Sothe et al 2022

Curated in GEE by : Samapriya Roy

keywords: soil carbon density, soil carbon stock estimate, soil carbon storage, terrestrial ecosystem models, machine Learning Methods Enabled Predictive Modeling

Last updated on GEE: 2021-11-14
