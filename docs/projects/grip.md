# Global Roads Inventory Project global roads database

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
