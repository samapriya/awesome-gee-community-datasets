# awesome-gee-community-datasets
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
![GEE Community Datasets](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/samapriya/34bc0c1280d475d3a69e3b60a706226e/raw/community.json)

Read the [Medium Post article here](https://medium.com/geospatial-processing-at-scale/community-datasets-data-commons-in-google-earth-engine-8585d8baef1f)

Copy this badge as you contribute datasets: ![contributor](https://img.shields.io/badge/gee--awesome--datasets-data%20commons%20contributor-green)

Community Datasets added by users and made available for use at large

## [Submit your Dataset as Issue Now using Template Link](https://github.com/samapriya/awesome-gee-community-datasets/issues/new?assignees=samapriya&labels=&template=new-community-gee-dataset-template.md&title=Dataset+%26+Curator+Name)

![new_issue_datasets](https://user-images.githubusercontent.com/6677629/81495266-2eaedb00-927d-11ea-849f-af017ac7b32a.gif)


****

## Table of Contents
1. [High Resolution Settlement Layer](#high-resolution-settlement-layer)
2. [Global Shoreline Dataset](#global-shoreline-dataset)
3. [OSM Water Layer Surface Waters in OpenStreetMap](#osm-water-layer-surface-waters-in-openstreetmap)
4. [Mapbiomas Annual land cover and use maps](#mapbiomas-annual-land-cover-and-use-maps)
5. [EarthEnv Global 1-km Cloud Frequency Version 1](#earthenv-global-1-km-cloud-frequency-version-1)
6. [Global 30m Height Above the Nearest Drainage](#global-30m-height-above-the-nearest-drainage)
7. [Global Mangrove Watch](#global-mangrove-watch)
8. [SoilGrids250m_2.0](#soilgrids250m_20)
9. [Global Mining Areas and Validation Datasets](#global-mining-areas-and-validation-datasets)
10. [Predictive mapping of the global power system using open data](#predictive-mapping-of-the-global-power-system-using-open-data)
11. [Global Roads Inventory Project global roads database](#global-roads-inventory-project-global-roads-database)
12. [Geomorpho90m Geomorphometric Layers](#geomorpho90m-geomorphometric-layers)

### High Resolution Settlement Layer
In partnership with the Center for International Earth Science Information Network (CIESIN) at Columbia University, Facebook used state-of-the-art computer vision techniques to identify buildings from publicly accessible mapping services to create the world's most accurate population datasets. You can [read about their project here](https://dataforgood.fb.com/tools/population-density-maps/). These are the datasets available for download on the Humanitarian Data Exchange for nearly every country in the world:

* Overall population density
* Male
*Female
* Women of reproductive age (ages 15-49)
* Children (ages 0-5)
* Youth (ages 15-24)
* Elderly (ages 60+)


To reference this data, please use the following citation:

```
Facebook Connectivity Lab and Center for International Earth Science Information Network - CIESIN - Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery for HRSL Copyright 2016 DigitalGlobe. Accessed DAY MONTH YEAR. Data shared under: Creative Commons Attribution International.
```


You can get methodology here:

https://dataforgood.fb.com/docs/methodology-high-resolution-population-density-maps-demographic-estimates/

and step by step download here

https://dataforgood.fb.com/docs/high-resolution-population-density-maps-demographic-estimates-documentation/


![HRSL_pop](https://user-images.githubusercontent.com/6677629/110987570-e648c980-8334-11eb-8615-535114fde903.gif)

#### Earth Engine Snippet
```js
var HRSL = ee.ImageCollection("projects/sat-io/open-datasets/hrsl/hrslpop");
var HRSL_men = ee.ImageCollection("projects/sat-io/open-datasets/hrsl/hrsl_men");
var HRSL_women = ee.ImageCollection("projects/sat-io/open-datasets/hrsl/hrsl_women");
var HRSL_youth = ee.ImageCollection("projects/sat-io/open-datasets/hrsl/hrsl_youth");
var HRSL_children_under_five = ee.ImageCollection("projects/sat-io/open-datasets/hrsl/hrsl_children_under_five");
var HRSL_women_reproductive_age = ee.ImageCollection("projects/sat-io/open-datasets/hrsl/hrsl_women_reproductive_age");
var HRSL_elderly_over_sixty = ee.ImageCollection("projects/sat-io/open-datasets/hrsl/hrsl_elderly_over_sixty");
```

Sample Code: https://code.earthengine.google.com/5f8af7ee25d50d44a58c90bf0efc91bb

Extra Info: [Medium Article here](https://medium.com/@samapriyaroy/community-datasets-in-google-earth-engine-an-experiment-b72daa474819)

Download Tool/Code snippets if any: [hdxpop](https://github.com/samapriya/hdxpop)

Curated by: Samapriya Roy

Keywords: High Density Population, Population, Facebook

Last updated: 2021-03-12
****

### Global Shoreline Dataset

A new 30-m spatial resolution global shoreline vector (GSV) was developed from annual composites of 2014 Landsat satellite imagery. The semi-automated classification of the imagery was accomplished by manual selection of training points representing water and non-water classes along the entire global coastline. Polygon topology was applied to the GSV, resulting in a new characterisation of the number and size of global islands. Three size classes of islands were mapped: continental mainlands (5), islands greater than 1 km2 (21,818), and islands smaller than 1 km2 (318,868). The GSV represents the shore zone land and water interface boundary, and is a spatially explicit ecological domain separator between terrestrial and marine environments. The development and characteristics of the GSV are presented herein. An approach is also proposed for delineating standardised, high spatial resolution global ecological coastal units (ECUs). For this coastal ecosystem mapping effort, the GSV will be used to separate the nearshore coastal waters from the onshore coastal lands. The work to produce the GSV and the ECUs is commissioned by the Group on Earth Observations (GEO), and is associated with several GEO initiatives including GEO Ecosystems, GEO Marine Biodiversity Observation Network (MBON) and GEO Blue Planet.

Publication URL: https://pubs.er.usgs.gov/publication/70202401

Scale: 30m

Please use Citation:
```
Sayre, R., S. Noble, S. Hamann, R. Smith, D. Wright, S. Breyer, K. Butler, K. Van Graafeiland, C. Frye, D. Karagulle, D. Hopkins, D. Stephens, K. Kelly, Z. Basher, D. Burton, J. Cress, K. Atkins, D. Van Sistine, B. Friesen, R. Allee, T. Allen, P. Aniello, I. Asaad, M. Costello, K. Goodin, P. Harris, M. Kavanaugh, H. Lillis, E. Manca, F. Muller-Karger, B. Nyberg, R. Parsons, J. Saarinen, J. Steiner, and A. Reed. 2019. A new 30 meter resolution global shoreline vector and associated global islands database for the development of standardized ecological coastal units. Journal of Operational Oceanography, 12:sup2, S47-S56, DOI: 10.1080/1755876X.2018.1529714
```

Shared Under: Creative Commons Attribution-Share Alike 4.0 International License

![global_shorlines](https://user-images.githubusercontent.com/6677629/81495134-112d4180-927c-11ea-82db-face703c3238.gif)

#### Earth Engine Snippet
```js
var mainlands = ee.FeatureCollection('projects/sat-io/open-datasets/shoreline/mainlands');
var big_islands = ee.FeatureCollection('projects/sat-io/open-datasets/shoreline/big_islands');
var small_islands = ee.FeatureCollection('projects/sat-io/open-datasets/shoreline/small_islands');
```

Sample Code: https://code.earthengine.google.com/609a16955ed07b282fcd4bff4750f814

Extra Info: Over 100 Million+ vertices

Curated by: Samapriya Roy

Keywords: Global Shoreline, Shoreline, Oceans

Last updated: 2020-05-08
****

## OSM Water Layer Surface Waters in OpenStreetMap
OSM Water Layers is a global surface water data, generated by extracting surface water features from OpenStreetMap. The OSM water layer rasterized map is referenced to WGS84. The data is prepared as 5 degree x 5 degree tiles (6000 pixel x 6000 pixel). Filename represents the center of the lower left pixel of the data domain; e.g. the file "n30w120.tif" is for the domain N30-N35, W120-W115. (more accurately, N29.99958333-N34.99958333,W120.0004167-W115.0004167)

Scale: 90m

#### Raster Values

* 1: Ocean
* 2: Large Lake/River
* 3: Major River
* 4: Canal
* 5: Small Stream

Citation

```
Yamazaki, Dai, Daiki Ikeshima, Jeison Sosa, Paul D. Bates, George H. Allen, and Tamlin M. Pavelsky. "MERIT Hydro: a high‐resolution global hydrography map based on latest topography dataset." Water Resources Research 55, no. 6 (2019): 5053-5073.
```

License: Creative Commons Attribution 4.0 International (CC BY 4.0)

![osm_watermask](https://user-images.githubusercontent.com/6677629/82018670-c59bde80-9653-11ea-9136-882c720570db.gif)

#### Earth Engine Snippet
```js
var mainlands = ee.ImageCollection("projects/sat-io/open-datasets/OSM_waterLayer");
```

Sample Code: https://code.earthengine.google.com/cab4e587c9fa6d86e9d848432efe874b

Extra Info: [Go to the OSM Water Layer webpage](http://hydro.iis.u-tokyo.ac.jp/~yamadai/OSM_water/)

Curated by: Samapriya Roy and Erin Trochim

Keywords: Global water layer, Open Street Map, OSM

Last updated: 2020-04-28
****

### Mapbiomas Annual land cover and use maps

The Brazilian Annual Land Use and Land Cover Mapping Project is an initiative that involves a collaborative network of biomes, land use, remote sensing, GIS and computer science experts that rely on Google Earth Engine platform and its cloud processing and automated classifiers capabilities to generate Brazil’s annual land use and land cover time series. MapBiomas Project - is a multi-institutional initiative to generate annual land cover and use maps using automatic classification processes applied to satellite images. The complete description of the project can be [found here](http://mapbiomas.org).

Scale: 30 m,
Data Type: Multiple raster datasets and types

Please use Citation:
```
"Project MapBiomas - Collection [version] of Brazilian Land Cover & Use Map Series, accessed on [date] through the link: [LINK]"
```

Shared Under: Creative Commons Attribution-Share Alike 4.0 International License

![MapBiomas](https://user-images.githubusercontent.com/6677629/81698669-5300e800-9434-11ea-9c5f-e8bf9588e737.gif)

#### Earth Engine Snippet
```js
//From downloader v 1.1.4
assets: {
    integration: 'projects/mapbiomas-workspace/public/collection4_1/mapbiomas_collection41_integration_v1',
    transitions: 'projects/mapbiomas-workspace/public/collection4_1/mapbiomas_collection41_transitions_v1',
    vectors: [
        'projects/mapbiomas-workspace/AUXILIAR/areas-protegidas',
        'projects/mapbiomas-workspace/AUXILIAR/municipios-2016',
        'projects/mapbiomas-workspace/AUXILIAR/estados-2017',
        'projects/mapbiomas-workspace/AUXILIAR/biomas-2019',
        'projects/mapbiomas-workspace/AUXILIAR/bacias-nivel-1',
        'projects/mapbiomas-workspace/AUXILIAR/bacias-nivel-2',
    ]
},
```

Add repo link: https://code.earthengine.google.com/?accept_repo=users/mapbiomas/user-toolkit

Extra Info: [GitHub Tutorial](https://github.com/mapbiomas-brazil/user-toolkit)

Curated by: [MapBiomas](https://mapbiomas.org/)

Keywords: Mapbiomas, Land Use, Land Cover

Last updated: [Refer to webpage](https://mapbiomas.org/)
****

### EarthEnv Global 1-km Cloud Frequency Version 1

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
****

### Global 30m Height Above the Nearest Drainage

Read about the [methodology here](https://www.researchgate.net/publication/301559649_Global_30m_Height_Above_the_Nearest_Drainage)

![image](https://user-images.githubusercontent.com/169821/83188656-541e5e80-a130-11ea-8443-936e13aa8a62.png)

Or get it from https://gena.users.earthengine.app/view/global-hand

Use the following credit when these data are cited:

```
Donchyts, Gennadii, Hessel Winsemius, Jaap Schellekens, Tyler Erickson, Hongkai Gao, Hubert Savenije, and Nick van de Giesen. "Global 30m Height Above the Nearest Drainage (HAND)",
Geophysical Research Abstracts, Vol. 18, EGU2016-17445-3, 2016, EGU General Assembly (2016).
```

#### Earth Engine Snippet

```js
var hand30_100 = ee.ImageCollection("users/gena/global-hand/hand-100").mosaic()
var hand30_1000 = ee.Image("users/gena/GlobalHAND/30m/hand-1000")
var hand90_1000 = ee.Image("users/gena/GlobalHAND/90m-global/hand-1000")
```

#### Resolutions
30 and 90 - cell resolution, 100 and 1000 - number of river head threshold cells

Sample Code: https://code.earthengine.google.com/ed75ecef7fcf94897b74ac56bfbb3f43

Shared License:
This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Source and Curated by: Donchyts/Deltares

Keywords: Global Hand, Hydrology, drainage

Last updated: ~2017
****

### Global Mangrove Watch

From the Global Mangrove Dataset (1996 - 2016) website:

**The GMW has generated a global baseline map of mangroves for 2010 using ALOS PALSAR and Landsat (optical) data, and changes from this baseline for six epochs between 1996 and 2016 derived from JERS-1 SAR, ALOS PALSAR and ALOS-2 PALSAR-2. Annual maps are planned from 2018 and onwards.**

Updated dataset: https://www.globalmangrovewatch.org/datasets/

#### Citation:

```
Bunting P., Rosenqvist A., Lucas R., Rebelo L-M., Hilarides L., Thomas N., Hardy A., Itoh T., Shimada M. and Finlayson C.M. (2018). The Global Mangrove Watch – a New 2010 Global Baseline of Mangrove Extent. Remote Sensing 10(10): 1669. doi: 10.3390/rs1010669.


Thomas N, Lucas R, Bunting P, Hardy A, Rosenqvist A, Simard M. (2017). Distribution and drivers of global mangrove forest change, 1996-2010. PLOS ONE 12: e0179302. doi: 10.1371/journal.pone.0179302
```

![mangrove](https://user-images.githubusercontent.com/6677629/83225702-598aa180-a14e-11ea-9dce-65c46278531f.gif)

#### Earth Engine Snippet

```js
var gmw2007 = ee.FeatureCollection("projects/sat-io/open-datasets/GMW/GMW_2007_v2");
var gmw2008 = ee.FeatureCollection("projects/sat-io/open-datasets/GMW/GMW_2008_v2");
var gmw2009 = ee.FeatureCollection("projects/sat-io/open-datasets/GMW/GMW_2009_v2");
var gmw2010 = ee.FeatureCollection("projects/sat-io/open-datasets/GMW/GMW_2010_v2");
var gmw2015 = ee.FeatureCollection("projects/sat-io/open-datasets/GMW/GMW_2015_v2");
var gmw2016 = ee.FeatureCollection("projects/sat-io/open-datasets/GMW/GMW_2016_v2");
var gmw1996 = ee.FeatureCollection("projects/sat-io/open-datasets/GMW/GMW_1996_v2");
```

Sample Code: https://code.earthengine.google.com/ded574858c353cac4df6652e14f501b2

Resolution:
0.8 degee approx 30m

#### License & Usage
Attribution 4.0 International (CC BY 4.0)
https://creativecommons.org/licenses/by/4.0/.

You are free to:
Share — copy and redistribute the material in any medium or format
Adapt — remix, transform, and build upon the material for any purpose, even commercially.

Under the following terms:
Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

Website:  https://data.unep-wcmc.org/datasets/45

Curated by: Samapriya Roy

Keywords: Global, Mangrove, GMW

Last updated: 2019-06-14
****

### SoilGrids250m_2.0

SoilGrids is designed as a globally consistent, data-driven system that predicts soil properties and classes using global covariates and globally fitted models. If you are looking for soil information on national and/or local levels we advise to compare SoilGrids predictions with soil maps derived from national and local soil geographical databases. National soil maps are usually based on more detailed input soil information and therefore are often more accurate than SoilGrids (within the local coverage area). For an overview of national and regional soil databases, please refer to the Soil Geographic Databases compendium. The ‘mean’ and ‘median (0.5 quantile)’ may both be used as predictions of the soil property for a given cell. The mean represents the ‘expected value’ and provides an unbiased prediction of the soil property.


| Name | Description | Mapped units | Conversion factor | Conventional units |Assets on GEE |
|----------|------------------------------------------------------------------------------------|----------------|-------------------|--------------------|--------|
| bdod | Bulk density of the fine earth fraction | cg/cm³ | 100 | kg/dm³ |[bdod_mean](https://code.earthengine.google.com/?asset=projects/soilgrids-isric/bdod_mean)|
| cec | Cation Exchange Capacity of the soil | mmol(c)/kg | 10 | cmol(c)/kg |[cec_mean](https://code.earthengine.google.com/?asset=projects/soilgrids-isric/cec_mean) |
| cfvo | Volumetric fraction of coarse fragments (> 2 mm) | cm3/dm3 (vol‰) | 10 | cm3/100cm3 (vol%) |[cfvo_mean](https://code.earthengine.google.com/?asset=projects/soilgrids-isric/cfvo_mean) |
| clay | Proportion of clay particles (< 0.002 mm) in the fine earth fraction | g/kg | 10 | g/100g (%) |[clay_mean](https://code.earthengine.google.com/?asset=projects/soilgrids-isric/clay_mean) |
| nitrogen | Total nitrogen (N) | cg/kg | 100 | g/kg |[nitrogen_mean](https://code.earthengine.google.com/?asset=projects/soilgrids-isric/nitrogen_mean) |
| phh2o | Soil pH | pHx10 | 10 | pH |[phh2o_mean](https://code.earthengine.google.com/?asset=projects/soilgrids-isric/phh2o_mean) |
| sand | Proportion of sand particles (> 0.05 mm) in the fine earth fraction | g/kg | 10 | g/100g (%) |[sand_mean](https://code.earthengine.google.com/?asset=projects/soilgrids-isric/sand_mean) |
| silt | Proportion of silt particles (≥ 0.002 mm and ≤ 0.05 mm) in the fine earth fraction | g/kg | 10 | g/100g (%) |[silt_mean](https://code.earthengine.google.com/?asset=projects/soilgrids-isric/silt_mean) |
| soc | Soil organic carbon content in the fine earth fraction | dg/kg | 10 | g/kg |[soc_mean](https://code.earthengine.google.com/?asset=projects/soilgrids-isric/soc_mean) |
| ocd | Organic carbon density | hg/dm³ | 10 | kg/dm³ |[ocd_mean](https://code.earthengine.google.com/?asset=projects/soilgrids-isric/ocd_mean) |
| ocs | Organic carbon stocks | t/ha | 10 | kg/m² |[ocs_mean](https://code.earthengine.google.com/?asset=projects/soilgrids-isric/ocs_mean) |

#### Citation

```
de Sousa, L., Poggio, L., Batjes, N.H., Heuvelink, G.B.M., Kempen, B., Ribeiro, E., Rossiter, D. SoilGrids 2.0: producing quality-assessed soil information for the globe. Under submission to SOIL
```

![gee_isric_main](https://user-images.githubusercontent.com/6677629/96608670-44f6a380-12bf-11eb-9e0b-1419a891fa84.gif)

#### Earth Engine Snippet
```js
var isric_bdod_mean = ee.Image("projects/soilgrids-isric/bdod_mean"),
var isric_cec = ee.Image("projects/soilgrids-isric/cec_mean"),
var isric_cfvo = ee.Image("projects/soilgrids-isric/cfvo_mean"),
var isric_clay = ee.Image("projects/soilgrids-isric/clay_mean")
var isric_sand = ee.Image("projects/soilgrids-isric/sand_mean")
var isric_silt = ee.Image("projects/soilgrids-isric/silt_mean")
var isric_nitrogen = ee.Image("projects/soilgrids-isric/nitrogen_mean")
var isric_phh20 = ee.Image("projects/soilgrids-isric/phh20_mean")
var isric_soc = ee.Image("projects/soilgrids-isric/soc_mean"),
var isric_ocd = ee.Image("projects/soilgrids-isric/ocd_mean");
var isric_ocs = ee.Image("projects/soilgrids-isric/ocs_mean");
```

Sample Code: https://code.earthengine.google.com/6618d200de937bb5b0325235d52d690f

#### Data available from
www.soilgrids.org.

#### Publication date
2020-05-04

#### Period
Fri Mar 31 1905 19:00:00 GMT-0500 Mon Jul 04 2016 20:00:00 GMT-0400

#### Provided by :
International Soil Reference and Information Centre (ISRIC)

#### License
Attribution 4.0 International (CC BY 4.0)

#### DOI
https://doi.org/10.17027/isric-soilgrids.713396fa-1687-11ea-a7c0-a0481ca9e724

Created and Curated by: International Soil Reference and Information Centre (ISRIC)

Keywords: For example Global Soilgrid, Sandy Soil, ISRIC

Last updated: 2020-10-20
****

### Global Mining Areas and Validation Datasets

This data set provides spatially explicit estimates of the area directly used for surface mining on a global scale. It contains more than 21,000 polygons of activities related to mining, mainly of coal and metal ores. Several data sources were compiled to identify the approximate location of mines active at any time between the years 2000 to 2017. This data set does not cover all existing mining locations across the globe. The polygons were delineated by experts using Sentinel-2 cloudless (https://s2maps.eu by EOX IT Services GmbH (contains modified Copernicus Sentinel data 2017 & 2018)) and very high-resolution satellite images available from Google Satellite and Bing Imagery. The derived polygons cover the direct land used by mining activities, including open cuts, tailing dams, waste rock dumps, water ponds, and processing infrastructure.

The overall accuracy calculated from the control points was 88.4%

Read about the [methodology here](https://www.nature.com/articles/s41597-020-00624-w)

![mining](https://user-images.githubusercontent.com/6677629/113477655-fc840a00-9448-11eb-9216-b617e831568a.gif)

Use the following credit when these data are cited:

```
Maus, Victor; Giljum, Stefan; Gutschlhofer, Jakob; da Silva, Dieison M; Probst, Michael; Gass, Sidnei L B; Luckeneder, Sebastian; Lieber, Mirko; McCallum, Ian (2020): Global-scale mining polygons (Version 1). PANGAEA https://doi.org/10.1594/PANGAEA.910894
```

You can cite the original paper using:

```
Maus, Victor, Stefan Giljum, Jakob Gutschlhofer, Dieison M. da Silva, Michael Probst, Sidnei LB Gass, Sebastian Luckeneder, Mirko Lieber, and Ian McCallum. "A global-scale data set of mining areas." Scientific Data 7, no. 1 (2020): 1-13.
```

#### Earth Engine Snippet

```js
var mining = ee.FeatureCollection("projects/sat-io/open-datasets/global-mining/global_mining_polygons");
var validation = ee.FeatureCollection("projects/sat-io/open-datasets/global-mining/global_mining_validation");
```

#### Additional Info
21,000 main polygons and 1000 validation polygons

Sample Code: https://code.earthengine.google.com/21caa84d736a622b9de9c760c266e3d9

Shared License:
This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Curated by: Samapriya Roy

Keywords: Mining, High Resolution, Global, coal, land-use, metal ores, minerals, raw material extraction

Last updated: 2021
****
### Predictive mapping of the global power system using open data

Read about the [methodology here](https://www.nature.com/articles/s41597-019-0347-4)

![power](https://user-images.githubusercontent.com/6677629/113477651-f857ec80-9448-11eb-93b2-71c9cb96af4a.gif)

Download the dataset [here](https://zenodo.org/record/3628142#.YGOrmWhKhPY)

Use the following credit when these datasets are cited:

```
Arderne, Christopher, NIcolas, Claire, Zorn, Conrad, & Koks, Elco E. (2020). Data from: Predictive mapping of the global power system using open data (Version 1.1.1) [Data set]. Nature Scientific Data. Zenodo. http://doi.org/10.5281/zenodo.3628142
```

Cite the paper using

```
Arderne, Christopher, Conrad Zorn, Claire Nicolas, and E. E. Koks. "Predictive mapping of the global power system using open data." Scientific data 7, no. 1 (2020): 1-12.
```

Current version: v1.1.1 released 2020-01-16
You can access the app here: https://gridfinder.org/

#### Earth Engine Snippet

```js
var lv = ee.Image("projects/sat-io/open-datasets/predictive-global-power-system/lv");
var targets = ee.Image("projects/sat-io/open-datasets/predictive-global-power-system/targets");
var transmission = ee.FeatureCollection("projects/sat-io/open-datasets/predictive-global-power-system/distribution-transmission-lines");
```

#### Resolutions
lv is at 250m, targets at 463.83 m

Sample Code: https://code.earthengine.google.com/ed75ecef7fcf94897b74ac56bfbb3f43

Shared License:
This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Curated by: Samapriya Roy

Keywords: Global transmission lines, electricity, infrastructure, power

Last updated: 2021-04-03
****
### Global Roads Inventory Project global roads database

The Global Roads Inventory Project (GRIP) dataset was developed to provide a more recent and consistent global roads dataset for use in global environmental and biodiversity assessment models like GLOBIO.

The GRIP dataset consists of global and regional vector datasets in ESRI filegeodatabase and shapefile format, and global raster datasets of road density at a 5 arcminutes resolution (~8x8km).

The GRIP dataset is mainly aimed at providing a roads dataset that is easily usable for scientific global environmental and biodiversity modelling projects. The dataset is not suitable for navigation. GRIP4 is based on many different sources (including OpenStreetMap) and to the best of our ability we have verified their public availability, as a criteria in our research. The UNSDI-Transportation datamodel was applied for harmonization of the individual source datasets. GRIP4 is provided under a Creative Commons License (CC-BY 4.0) and is free to use. Read about the [methodology here](https://iopscience.iop.org/article/10.1088/1748-9326/aabd42)

![grip4](https://user-images.githubusercontent.com/6677629/113480809-e3d11f80-945b-11eb-8ac8-ccfd79de11be.gif)

Download the dataset [here](https://www.globio.info/download-grip-dataset)

Use the following credit when these datasets are cited:

```
Meijer, Johan R., Mark AJ Huijbregts, Kees CGJ Schotten, and Aafke M. Schipper. "Global patterns of current and future road infrastructure." Environmental Research Letters 13, no. 6 (2018): 064006.
```

#### Earth Engine Snippet

```js
var grip4_africa = ee.FeatureCollection("projects/sat-io/open-datasets/GRIP4/Africa");
var grip4_central_south_america = ee.FeatureCollection("projects/sat-io/open-datasets/GRIP4/Central-South-America");
var grip4_europe = ee.FeatureCollection("projects/sat-io/open-datasets/GRIP4/Europe");
var grip4_north_america = ee.FeatureCollection("projects/sat-io/open-datasets/GRIP4/North-America");
var grip4_oceania = ee.FeatureCollection("projects/sat-io/open-datasets/GRIP4/Oceania");
var grip4_south_east_asia = ee.FeatureCollection("projects/sat-io/open-datasets/GRIP4/South-East-Asia");
var grip4_middle_east_central_asia = ee.FeatureCollection("projects/sat-io/open-datasets/GRIP4/Middle-East-Central-Asia");
```

Sample Code: https://code.earthengine.google.com/2557707383c16bb212eeb7f358d753a8

Total features: 25,758,453

Shared License:
This work is licensed under a Creative Commons Attribution 4.0. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Curated by: Samapriya Roy

Keywords: global, road map, infrastructure, global roads inventory project (GRIP), SSP scenarios

Last updated: 2021-04-03
****
### Geomorpho90m Geomorphometric Layers

Topographical relief comprises the vertical and horizontal variations of the Earth’s terrain and drives processes in geomorphology, biogeography, climatology, hydrology and ecology. Its characterisation and assessment, through geomorphometry and feature extraction, is fundamental to numerous environmental modelling and simulation analyses. We, therefore, developed the Geomorpho90m global dataset comprising of different geomorphometric features derived from the MERIT-Digital Elevation Model (DEM) - the best global, high-resolution DEM available. The fully-standardised 26 geomorphometric variables consist of layers that describe the (i) rate of change across the elevation gradient, using first and second derivatives, (ii) ruggedness, and (iii) geomorphological forms. The Geomorpho90m variables are available at 3 (~90 m) and 7.5 arc-second (~250 m) resolutions under the WGS84 geodetic datum, and 100 m spatial resolution under the Equi7 projection. They are useful for modelling applications in fields such as geomorphology, geology, hydrology, ecology and biogeography.

Geomorpho90m is a set of geomorphometric variables derived from MERIT-DEM. The are available at 3 resolutions the ingested ones are the 3 arc-second (~90m) resolution.The layers can be downloaded from [OpenTopography](https://portal.opentopography.org/dataspace/dataset?opentopoID=OTDS.012020.4326.1) or from [Google Drive](https://drive.google.com/drive/folders/1D4YHUycBBhNFVVsz4ohaJI7QXV9BEh94).

Read about the [methodology here](https://www.nature.com/articles/s41597-020-0479-6)

![geomorph90](https://user-images.githubusercontent.com/6677629/113523325-deafc580-956c-11eb-8dfd-1bf69ee7e216.gif)

Use the following credit when these datasets are cited:

```
Amatulli, Giuseppe, Daniel McInerney, Tushar Sethi, Peter Strobl, and Sami Domisch. "Geomorpho90m, empirical evaluation and accuracy assessment of global high-resolution geomorphometric layers." Scientific Data 7, no. 1 (2020): 1-18.
```

#### Earth Engine Snippet

```js
var cti = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/cti");
var tri = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/tri");
var slope = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/slope");
```

Sample Code: https://code.earthengine.google.com/3efd5e8c5f2f02e637cdbfeedd1d968b

Shared License:
This work is licensed under a Creative Commons Attribution 4.0. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Curated by: Samapriya Roy

Keywords: Geomorpho90m, geomorphometric layers, MERIT DEM, topographic index, terrain ruggedness index, slope

Last updated: 2021-04-04
****
