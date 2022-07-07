# C-CAP Medium-Resolution Land Cover - Beta

The NOAA Coastal Change Analysis Program (C-CAP) produces national standardized land cover and change products for the coastal regions of the U.S. C-CAP products inventory coastal intertidal areas, wetlands, and adjacent uplands with the goal of monitoring changes in these habitats. These maps are developed utilizing high resolution National Agriculture Imagery Program (NAIP) imagery, and can be used to track changes in the landscape through time. This trend information gives important feedback to managers on the success or failure of management policies and programs and aid in developing a scientific understanding of the Earth system and its response to natural and human-induced changes. This understanding allows for the prediction of impacts due to these changes and the assessment of their cumulative effects, helping coastal resource managers make more informed regional decisions. NOAA C-CAP is a contributing member to the Multi-Resolution Land Characteristics consortium and C-CAP products are included as the coastal expression of land cover within the National Land Cover Database.

**These data should be considered to be BETA-level or draft products. They are based on 1-meter land cover mapping that were entirely automated and the relationship of those data to existing wetlands data. As such, there may be issues that result from the different vintages of these products, as well as the errors included in each. While not perfect, the data should provide an example of what level of detail would be possible through such higher-resolution mapping. These data are not jurisdictional or intended for use in litigation. NOAA does not assume liability for any damages or misrepresentations caused by inaccuracies in the data, or as a result of the data used on a particular system. NOAA makes no warranty, expressed or implied, nor does the fact of distribution constitute such a warranty.**

These detailed products bring NOAA’s national land cover mapping framework to the local level and are developed for specific project-based geographies (not the entire coastal land cover mapping boundary). Data are often developed in partnership with state and local groups. Attributes for this product are as follows: 0 Background, 1 Unclassified (Cloud, Shadow, etc), 2 Impervious, 3 4 5 Developed Open Space, 6 Cultivated Land, 7 Pasture/Hay, 8 Grassland, 9 Deciduous Forest, 10 Evergreen Forest, 11 Mixed Forest, 12 Scrub/Shrub, 13 Palustrine Forested Wetland, 14 Palustrine Scrub/Shrub Wetland, 15 Palustrine Emergent Wetland, 16 Estuarine Forested Wetland, 17 Estuarine Scrub/Shrub Wetland, 18 Estuarine Emergent Wetland, 19 Unconsolidated Shore, 20 Bare Land, 21 Open Water, 22 Palustrine Aquatic Bed, 23 Estuarine Aquatic Bed, 24 Tundra, 25 Snow/Ice, Recommended Citation. NOAA Coastal Change Analysis Program (C-CAP) Regional Land Cover Database.

This dataset was created by NOAA's Ocean Service, Office for Coastal Management (OCM). Random Forest Classification: The initial 1m spatial resolution 6 class high resolution land cover product was developed using a Geographic Object-Based Image Analysis (GEOBIA) processing framework. This involves taking each image to be classified and grouping the pixels based on spectral and spatial properties into regions of homogeneity called objects. You can [read a sample metadata file here](https://coast.noaa.gov/htdata/raster1/landcover/bulkdownload/hires/ma/MA_2016_lc.xml)

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Citation

```
National Oceanic and Atmospheric Administration, Office for Coastal Management. “Name of Data Set.” Coastal Change Analysis Program (C-
CAP) 10m-Resolution Land Cover. Charleston, SC: NOAA Office for Coastal Management. Accessed [Month Year] at www.coast.noaa.gov/
htdata/raster1/landcover/bulkdownload/hires/.
```

```
National Oceanic and Atmospheric Administration, Office for Coastal Management. “Name of Data Set.” Coastal Change Analysis Program (C-
CAP) 30m-Resolution Land Cover. Charleston, SC: NOAA Office for Coastal Management. Accessed [Month Year] at www.coast.noaa.gov/
htdata/raster1/landcover/bulkdownload/hires/.
```

#### Preprocessing

The regional land cover dataset files were downloaded for each region. If the files were img then they were convert to GeoTIFF. Each region was converted into a collection and start and end dates were added based on available information and filenames.


![CCAP_beta](https://user-images.githubusercontent.com/6677629/177836823-e16c9a76-f360-439b-883e-5f7dbbc8a83c.gif)

#### Earth Engine Snippet

```js
var CCAP_LC10 = ee.ImageCollection("projects/sat-io/open-datasets/NOAA/ccap_10m");
var CCAP_LC30 = ee.ImageCollection("projects/sat-io/open-datasets/NOAA/ccap_30m");
```

Sample Code LC: https://code.earthengine.google.com/e7180cf756bdb8593c479f0da91e8118


![impervious_30m](https://user-images.githubusercontent.com/6677629/177843948-f47ce3d6-9dd7-43bc-a99e-f8f68d544925.gif)

```js
var CCAP_IMP30 = ee.ImageCollection("projects/sat-io/open-datasets/NOAA/ccap_30m_impervious");
```

Sample Code Impervious: https://code.earthengine.google.com/f8f1636a5ae3b0b03715c805ec436f67

#### License

The dataset is released under an assumed CC0 1.0 Universal (CC0 1.0) Public Domain Dedication.

Produced by: NOAA's Ocean Service, Office for Coastal Management (OCM)

Curated in GEE by: Samapriya Roy

Keywords: Land Use, Land Cover, Urban Watch, Remote Sensing, High Resolution, OBIA, NOAA

Last updated on GEE: 2022-06-12
