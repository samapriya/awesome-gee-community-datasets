# Global Mangrove Watch

This study has used L-band Synthetic Aperture Radar (SAR) global mosaic datasets from the Japan Aerospace Exploration Agency (JAXA) for 11 epochs from 1996 to 2020 to develop a long-term time-series of global mangrove extent and change. The study used a map-to-image approach to change detection where the baseline map (GMW v2.5) was updated using thresholding and a contextual mangrove change mask. This approach was applied between all image-date pairs producing 10 maps for each epoch, which were summarised to produce the global mangrove time-series. The resulting mangrove extent maps had an estimated accuracy of 87.4 % (95th conf. int.: 86.2 - 88.6 %), although the accuracies of the individual gain and loss change classes were lower at 58.1 % (52.4 - 63.9 %) and 60.6 % (56.1 - 64.8 %), respectively.

Sources of error included a mis-registration in the SAR mosaic datasets, which could only be partially corrected for, but also confusion in fragmented areas of mangroves, such as around aquaculture ponds. Overall, 152,604 km2 (133,996 - 176,910) of mangroves were identified for 1996, with this decreasing by -5,245 km2 (-13,587 - 3686) resulting in a total extent of 147,359 km2 (127,925 - 168,895) in 2020, and representing an estimated loss of 3.4 % over the 24-year time period. The Global Mangrove Watch Version 3.0 represents the most comprehensive record of global mangrove change achieved to date and is expected to support a wide range of activities, including the ongoing monitoring of the global coastal environment, defining and assessments of progress towards conservation targets, protected area planning and risk assessments of mangrove ecosystems worldwide.

You can [download the dataset here](https://zenodo.org/record/6894273#.YyMn4tXMKdw) and [read the paper here](https://www.mdpi.com/2072-4292/14/15/3657)

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Preprocessing

Raster tiles were mosaiced so that all extents and allied rasters can fit into single collections. Date ranges were added later to the raster and the vector layers.

#### Citation:

```
Bunting, P.; Rosenqvist, A.; Hilarides, L.; Lucas, R.M.; Thomas, T.; Tadono, T.; Worthington, T.A.; Spalding, M.; Murray, N.J.; Rebelo, L-M. Global
Mangrove Extent Change 1996 – 2020: Global Mangrove Watch Version 3.0. Remote Sensing. 2022
```

#### Dataset citation

```
Bunting, Pete, Rosenqvist, Ake, Hilarides, Lammert, Lucas, Richard, Thomas, Nathan, Tadono , Takeo, Worthington, Thomas, Spalding , Mark, Murray,
Nicholas, & Rebelo, Lisa-Maria. (2022). Global Mangrove Watch (1996 - 2020) Version 3.0 Dataset (3.0) [Data set]. Zenodo. https://doi.org/10.5281/
zenodo.6894273
```

![gmw_small](https://user-images.githubusercontent.com/6677629/190841060-d939cc7d-f3ce-499f-8411-623806936bc8.gif)

#### Earth Engine Snippet: Extent

```js
var extent_raster = ee.ImageCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/extent/GMW_V3");
var extent_1996 = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/extent/gmw_v3_1996_vec");
var extent_2007 = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/extent/gmw_v3_2007_vec");
var extent_2008 = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/extent/gmw_v3_2008_vec");
var extent_2009 = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/extent/gmw_v3_2009_vec");
var extent_2010 = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/extent/gmw_v3_2010_vec");
var extent_2015 = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/extent/gmw_v3_2015_vec");
var extent_2016 = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/extent/gmw_v3_2016_vec");
var extent_2017 = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/extent/gmw_v3_2017_vec");
var extent_2018 = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/extent/gmw_v3_2018_vec");
var extent_2019 = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/extent/gmw_v3_2019_vec");
var extent_2020 = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/extent/gmw_v3_2020_vec");
```

#### Earth Engine Snippet: Change from 1996

```js
var change_f1996_raster = ee.ImageCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/change/change_f1996");
var change_f1996_2007 = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/change/gmw_v3_f1996_t2007_vec");
var change_f1996_2008 = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/change/gmw_v3_f1996_t2008_vec");
var change_f1996_2009 = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/change/gmw_v3_f1996_t2009_vec");
var change_f1996_2010 = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/change/gmw_v3_f1996_t2010_vec");
var change_f1996_2015 = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/change/gmw_v3_f1996_t2015_vec");
var change_f1996_2016 = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/change/gmw_v3_f1996_t2016_vec");
var change_f1996_2017 = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/change/gmw_v3_f1996_t2017_vec");
var change_f1996_2018 = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/change/gmw_v3_f1996_t2018_vec");
var change_f1996_2019 = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/change/gmw_v3_f1996_t2019_vec");
var change_f1996_2020 = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/change/gmw_v3_f1996_t2020_vec");
```
#### Earth Engine Snippet: Union

Single layer of pixels which were mangroves at any date in the time series

```js
var gmw_union_raster = ee.Image("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/union/gmw_v3_mng_union");
var gmw_union_vector = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/union/gmw_v3_union_vec");
```

#### Earth Engine Snippet: Core

Single layer of pixels which were mangroves at all dates within the time series

```js
var gmw_core_raster = ee.Image("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/core/gmw_v3_mng_core");
var gmw_core_vector = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/core/gmw_v3_core_vec");
```

#### Earth Engine Snippet: Tiles
Vector layer with the 1x1 degree tiles used for the analysis

```js
var tiles = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GMW/gmw_v3_tiles");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/GLOBAL-MANGROVE-WATCH

Resolution: approx 30m

#### License & Usage
Attribution 4.0 International [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Curated in GEE by: Samapriya Roy

Keywords: Global, Mangrove, GMW, 1996, 2020

Last updated: 2022-09-16
