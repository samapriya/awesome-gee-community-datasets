# Global River Classification (GloRiC)

The Global River Classification (GloRiC) provides river types and sub-classifications for all river reaches contained in the HydroRIVERS database. GloRiC has been developed by utilizing the river network delineation of HydroRIVERS combined with the hydro-enviromental characteristics from the HydroATLAS database and auxiliary information.

Version 1.0 of GloRiC provides a hydrologic, physio-climatic, and geomorphic sub-classification, as well as a combined river type for every river reach, resulting in a total of 127 river reach types. It also offers a k-means statistical clustering of the reaches into 30 groups. The dataset comprises 8.5 million river reaches with a total length of 35.9 million km.

You can find overall [technical documentation](https://data.hydrosheds.org/file/technical-documentation/GloRiC_TechDoc_v10.pdf) here and technical information for [GloRiC Canada here](https://data.hydrosheds.org/file/technical-documentation/GloRiC_Canada_TechDoc_v10.pdf)

#### Preprocessing

Besides the global version of GloRiC, there is also a regional version for Canada available, GloRiC-Canada, which follows the same classification principles but with Canada-specific adaptations. GloRiC-Canada categorizes all river reaches of Canada into 23 types.


Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Citation

```
Ouellet Dallaire, C., Lehner, B., Sayre, R., Thieme, M. (2019). A multidisciplinary framework to derive global river reach classifications at high
spatial resolution. Environmental Research Letters, 14(2): 024003. https://doi.org/10.1088/1748-9326/aad8e9

Ouellet Dallaire, C., Lehner, B., Creed, I. (2020): Multidisciplinary classification of Canadian river reaches to support the sustainable management
of freshwater systems. Canadian Journal of Fisheries and Aquatic Sciences, 77(2): 326–341. https://doi.org/10.1139/cjfas-2018-0284
```

![gloric_rivers](https://user-images.githubusercontent.com/6677629/182002515-97d08269-968b-487d-b6f5-9ecabfcd1f95.gif)

#### Earth Engine Snippet

```js
var gloric = ee.FeatureCollection("projects/sat-io/open-datasets/GloRiC/GloRiC_v10");
var gloric_canada = ee.FeatureCollection("projects/sat-io/open-datasets/GloRiC/GloRiC_Canada_v10");
```

|Column    |Description                                                                                                                                                                                                                                |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Reach_ID  |Unique identifier (ID) for every river reach Note: the first digit identifies the region/continent: 1: Africa; 2: Europe; 3: Siberia; 4: Asia; 5: Australia & Oceania; 6: South America; 7: North America; 8: American Arctic; 9: Greenland|
|Next_down |ID of next downstream river reach Note: the next downstream ID can be used to trace the river network by navigating from reach to reach. Values of 0 indicate reaches with no further downstream connection (pour points).                 |
|Length_km |Length of individual river reach [km]                                                                                                                                                                                                      |
|Log_Q_avg |Log-10 of long-term average discharge [m3 /sec]                                                                                                                                                                                            |
|Log_Q_var |Log-10 of flow regime variability                                                                                                                                                                                                          |
|Class_hydr|Classes of hydrologic sub-classification (15 classes)                                                                                                                                                                                      |
|Temp_min  |Long-term average of the minimum air temperature of the coldest month [degrees Celsius]                                                                                                                                                    |
|CMI_indx  |Climate Moisture Index                                                                                                                                                                                                                     |
|Log_elev  |Log-10 of average elevation of the reach [meters a.s.l.]                                                                                                                                                                                   |
|Class_phys|Classes of physio-climatic sub-classification (24 classes)                                                                                                                                                                                 |
|Lake_wet  |Lake or wetland influence [binary: 0 = no; 1 = yes]                                                                                                                                                                                        |
|Stream_pow|Total stream power [kW/m2 ]                                                                                                                                                                                                                |
|Class_geom|Classes of geomorphic sub-classification (127 classes)                                                                                                                                                                                     |
|Reach_type|Combined river reach type (4 classes)                                                                                                                                                                                                      |
|Kmeans_30 |Classes of k-means statistical clustering (30 classes)                                                                                                                                                                                     |

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/GLOBAL-RIVER-CLASSIFICATION(GLORIC)


#### License
The data is licensed under a Creative Commons Attribution 4.0 International License (see section 4). By downloading and using the data the user agrees to the terms and conditions of this license.

Created by: Ouellet Dallaire, C., Lehner, B., Sayre, R., Thieme, M. & Schmitt, O

Curated by: Samapriya Roy

Keywords: water,hydrology, rivers, discharge, depth, volume, area, gloric

Last updated: 2022-07-09
