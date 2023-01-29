# EOG Annual VIIRS Night Time Light

**This dataset is currently only available to those in the [insiders program](https://gee-community-catalog.org/insiders/)**

A new consistently processed time series of annual global VIIRS nighttime lights has been produced from monthly cloud-free average radiance grids spanning 2012 to 2021 is processed by the Earth Observation Group(EOG). The new methodology (version 2.1) is a modification of the original VNL V1 that is available in the Earth Engine catalogue. Compared to VNL V1, this improved VNL V2.1 version removes ephemeral lights and background noise.

In both methods there is an initial filtering to remove sunlit, moonlit and cloudy pixels, leading to rough composites that contains lights, fires, aurora and background. In the original method, the rough annual composites are made from a full year of nightly DNB data. In the new method, the rough composites are made on monthly increments and then combined to form rough annual composites. Both methods employ outlier removal to discard biomass burning pixels and isolate the background.

In the original method the outlier removal is performed on scattergrams generated for each 15 arc second grid cell, with outliers clipped off from both the high and low radiance sides of the scattergram. The discard of outlier pixels proceeds until the scattergram’s standard deviation stabilizes. The new method uses the twelve-month median radiance to discard high and low radiance outliers, filtering out most fires and isolating the background. Background areas are zeroed out in both methods using the data range (DR) calculated from 3x3 grid cells. In both methods, the DR threshold for background is indexed to cloud-cover levels, with higher DR thresholds in areas having low numbers of cloud-free coverages. In the new method, particular attention is given to setting a single DR threshold for distinguishing lit grid cells from background for each 15 arc second grid cell. This is achieved by setting the DR threshold from a multiyear maximum median and a corresponding multiyear percent cloud-cover grids. The multiyear approach makes it possible to detect lighting present in each 15 arc second grid cell with a single DR threshold across all the years in the series. You can get [additional information here](https://eogdata.mines.edu/products/vnl/#annual_v2) and [download v2.1 here](https://eogdata.mines.edu/nighttime_light/annual/v21/)

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Data preprocessing
Datasets were preprocessed and metadata was added to each image in collection. The year 2012 had two datasets for a varying period and as such was excluded from the collection for now and maybe added later.

#### Citation

```
Elvidge, C.D, Zhizhin, M., Ghosh T., Hsu FC, Taneja J. Annual time series of global VIIRS nighttime lights derived from monthly averages:2012 to
2019. Remote Sensing 2021, 13(5), p.922, https://doi.org/10.3390/rs13050922
```

![eog_viirs](https://user-images.githubusercontent.com/6677629/215304379-2cbf6e19-1c66-4dd5-b974-5db99ba719f6.gif)

#### Code Snippet

```js
var average = ee.ImageCollection("projects/sat-io/open-datasets/EOG_VNL_V21/average");
var maximum = ee.ImageCollection("projects/sat-io/open-datasets/EOG_VNL_V21/maximum");
var median = ee.ImageCollection("projects/sat-io/open-datasets/EOG_VNL_V21/median");
var minimum = ee.ImageCollection("projects/sat-io/open-datasets/EOG_VNL_V21/minimum");
var average_masked = ee.ImageCollection("projects/sat-io/open-datasets/EOG_VNL_V21/average_masked");
var median_masked = ee.ImageCollection("projects/sat-io/open-datasets/EOG_VNL_V21/median_masked");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/EOG-VNL-V21

#### License
Public domain license with properitary license language.

```
Colorado School of Mines data, information, and products, regardless of the method of delivery, are not subject to copyright and carry no
restrictions on their subsequent use by the public. Once obtained, they may be put to any lawful use. The forgoing data is in the public domain and
is being provided without restriction on use and distribution.
```

Provided by: Colorado School of Mines, Elvidge et al. 2019

Curated in GEE by : Samapriya Roy

keywords: Nighttime lights, VIIRS, Annual time series, Earth Observation Group , EOG, Colorado School of Mines

Last updated on GEE: 2023-01-28
