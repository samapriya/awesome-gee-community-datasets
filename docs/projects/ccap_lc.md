# C-CAP High-Resolution Land Cover

The NOAA Coastal Change Analysis Program (C-CAP) produces national standardized land cover and change products for the coastal regions of the U.S. C-CAP products inventory coastal intertidal areas, wetlands, and adjacent uplands with the goal of monitoring changes in these habitats. The timeframe for this metadata is summer 2016. These maps are developed utilizing high resolution National Agriculture Imagery Program (NAIP) imagery, and can be used to track changes in the landscape through time. This trend information gives important feedback to managers on the success or failure of management policies and programs and aid in developing a scientific understanding of the Earth system and its response to natural and human-induced changes. This understanding allows for the prediction of impacts due to these changes and the assessment of their cumulative effects, helping coastal resource managers make more informed regional decisions. NOAA C-CAP is a contributing member to the Multi-Resolution Land Characteristics consortium and C-CAP products are included as the coastal expression of land cover within the National Land Cover Database.

These detailed products bring NOAA’s national land cover mapping framework to the local level and are developed for specific project-based geographies (not the entire coastal land cover mapping boundary). Data are often developed in partnership with state and local groups. Attributes for this product are as follows: 0 Background, 1 Unclassified (Cloud, Shadow, etc), 2 Impervious, 3 4 5 Developed Open Space, 6 Cultivated Land, 7 Pasture/Hay, 8 Grassland, 9 Deciduous Forest, 10 Evergreen Forest, 11 Mixed Forest, 12 Scrub/Shrub, 13 Palustrine Forested Wetland, 14 Palustrine Scrub/Shrub Wetland, 15 Palustrine Emergent Wetland, 16 Estuarine Forested Wetland, 17 Estuarine Scrub/Shrub Wetland, 18 Estuarine Emergent Wetland, 19 Unconsolidated Shore, 20 Bare Land, 21 Open Water, 22 Palustrine Aquatic Bed, 23 Estuarine Aquatic Bed, 24 Tundra, 25 Snow/Ice, Recommended Citation. NOAA Coastal Change Analysis Program (C-CAP) Regional Land Cover Database.

This dataset was created by NOAA's Ocean Service, Office for Coastal Management (OCM). Random Forest Classification: The initial 1m spatial resolution 6 class high resolution land cover product was developed using a Geographic Object-Based Image Analysis (GEOBIA) processing framework. This involves taking each image to be classified and grouping the pixels based on spectral and spatial properties into regions of homogeneity called objects. You can [read a sample metadata file here](https://coast.noaa.gov/htdata/raster1/landcover/bulkdownload/hires/ma/MA_2016_lc.xml)

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Citation

```
National Oceanic and Atmospheric Administration, Office for Coastal Management. “Name of Data Set.” Coastal Change Analysis Program (C-
CAP) High-Resolution Land Cover. Charleston, SC: NOAA Office for Coastal Management. Accessed [Month Year] at www.coast.noaa.gov/
htdata/raster1/landcover/bulkdownload/hires/.
```

#### Preprocessing

The regional land cover dataset files were downloaded for each region. If the files were img then they were convert to GeoTIFF. Each region was converted into a collection and start and end dates were added based on available information and filenames.


![CCAP_LC_small](https://user-images.githubusercontent.com/6677629/173275567-d9b8a15a-d592-4227-ba8f-9b81081f53bf.gif)

#### Earth Engine Snippet

```js
var CCAP_AS_LC = ee.ImageCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/HRLC/CCAP_AS_LC");
var CCAP_CA_LC = ee.ImageCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/HRLC/CCAP_CA_LC");
var CCAP_CT_LC = ee.ImageCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/HRLC/CCAP_CT_LC");
var CCAP_GU_LC = ee.ImageCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/HRLC/CCAP_GU_LC");
var CCAP_HI_LC = ee.ImageCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/HRLC/CCAP_HI_LC");
var CCAP_LA_LC = ee.ImageCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/HRLC/CCAP_LA_LC");
var CCAP_MA_LC = ee.ImageCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/HRLC/CCAP_MA_LC");
var CCAP_ME_LC = ee.ImageCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/HRLC/CCAP_ME_LC");
var CCAP_MP_LC = ee.ImageCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/HRLC/CCAP_MP_LC");
var CCAP_OH_LC = ee.ImageCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/HRLC/CCAP_OH_LC");
var CCAP_OR_LC = ee.ImageCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/HRLC/CCAP_OR_LC");
var CCAP_PR_LC = ee.ImageCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/HRLC/CCAP_PR_LC");
var CCAP_RI_LC = ee.ImageCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/HRLC/CCAP_RI_LC");
var CCAP_VI_LC = ee.ImageCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/HRLC/CCAP_VI_LC");
var CCAP_WA_LC = ee.ImageCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/HRLC/CCAP_WA_LC");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:regional-landuse-landcover/CCAP-HRLC-HI


#### License

The dataset is released under an assumed CC0 1.0 Universal (CC0 1.0) Public Domain Dedication.

Produced by: NOAA's Ocean Service, Office for Coastal Management (OCM)

Curated in GEE by: Samapriya Roy

Keywords: Land Use, Land Cover, Urban Watch, Remote Sensing, High Resolution, OBIA, NOAA

Last updated on GEE: 2022-06-12
