# Global Mining Areas and Validation Datasets

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
21,000 main polygons and 1000 validation points

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/GLOBAL-MINING-AND-VALIDATION

Shared License:
This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Curated by: Samapriya Roy

Keywords: Mining, High Resolution, Global, coal, land-use, metal ores, minerals, raw material extraction

Last updated: 2021
