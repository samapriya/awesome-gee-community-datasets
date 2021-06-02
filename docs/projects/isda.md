# iSDAsoil Predicted Soil Properties for Africa 30m

iSDA Soil layers are 30 m resolution Soil Information System of the African continent using, to date, the most comprehensive compilation of soil samples (N≈150,000) and Earth Observation data. We produced predictions for soil pH, organic carbon (C) and total nitrogen (N), total carbon, effective Cation Exchange Capacity (eCEC), extractable—phosphorus (P), potassium (K), calcium (Ca), magnesium (Mg), sulfur (S), sodium (Na), iron (Fe), zinc (Zn)—silt, clay and sand, stone content, bulk density and depth to bedrock, at three depths (0, 20 and 50 cm) and using 2-scale 3D Ensemble Machine Learning framework implemented in the mlr (Machine Learning in R) package.

You can [read the paper here](https://www.nature.com/articles/s41598-021-85639-y)

#### Citation

```
Hengl, Tomislav, Matthew AE Miller, Josip Križan, Keith D. Shepherd, Andrew Sila, Milan Kilibarda, Ognjen Antonijević
et al. "African soil properties and nutrients mapped at 30 m spatial resolution using two-scale ensemble machine
learning." Scientific Reports 11, no. 1 (2021): 1-18.
```

![isda_layers](https://user-images.githubusercontent.com/6677629/120118704-80acf200-c159-11eb-9728-d31a7db7b15c.gif)


|Property                                |Unit      |Available Depths (cm)|Model Accuracy (R-square)|RMSE  |
|----------------------------------------|----------|---------------------|-------------------------|------|
|Fertility Capability Classification(fcc)|None      |0-50                 |N/A                      |N/A   |
|USDA Texture Class(texture)             |None      |0-20, 20-50          |N/A                      |N/A   |
|Clay content(clay_content)              |%         |0-20, 20-50          |0.746                    |9.6   |
|Bulk density, <2mm fraction(bd)         |g/cc      |0-20, 20-50          |0.819                    |126   |
|Carbon, total (carbon total)            |g/kg      |0-20, 20-50          |0.794*                   |0.291*|
|Effective Cation Exchange Capacity      |cmol(+)/kg|0-20, 20-50          |0.754*                   |0.417*|
|Nitrogen, total                         |g/kg      |0-20, 20-50          |0.732*                   |0.197*|
|Carbon organic                          |g/kg      |0-20, 20-50          |0.791*                   |0.369*|
|pH                                      |–         |0-20, 20-50          |0.818                    |0.459 |
|Sand content                            |%         |0-20, 20-50          |0.736                    |13.7  |
|Silt content                            |%         |0-20, 20-50          |0.64                     |8.92  |
|Stone content                           |%         |0-20, 20-50          |0.709*                   |0.803*|
|Depth to Bedrock                        |cm        |0-200                |0.429                    |41.3  |


#### Earth Engine Snippet

```js
var bedrock_depth = ee.Image("projects/sat-io/open-datasets/iSDAsoil_Africa_30m/bedrock_depth");
var bulk_density = ee.Image("projects/sat-io/open-datasets/iSDAsoil_Africa_30m/bulk_density");
var carbon_organic = ee.Image("projects/sat-io/open-datasets/iSDAsoil_Africa_30m/carbon_organic");
var carbon_total = ee.Image("projects/sat-io/open-datasets/iSDAsoil_Africa_30m/carbon_total");
var cation_exchange_capacity = ee.Image("projects/sat-io/open-datasets/iSDAsoil_Africa_30m/cation_exchange_capacity");
var clay_content = ee.Image("projects/sat-io/open-datasets/iSDAsoil_Africa_30m/clay_content");
var fertility_capability_classification = ee.Image("projects/sat-io/open-datasets/iSDAsoil_Africa_30m/fcc");
var nitrogen_total = ee.Image("projects/sat-io/open-datasets/iSDAsoil_Africa_30m/nitrogen_total");
var ph = ee.Image("projects/sat-io/open-datasets/iSDAsoil_Africa_30m/ph");
var sand_content = ee.Image("projects/sat-io/open-datasets/iSDAsoil_Africa_30m/sand_content");
var silt_content = ee.Image("projects/sat-io/open-datasets/iSDAsoil_Africa_30m/silt_content");
var stone_content = ee.Image("projects/sat-io/open-datasets/iSDAsoil_Africa_30m/stone_content");
var texture_class = ee.Image("projects/sat-io/open-datasets/iSDAsoil_Africa_30m/texture_class");
```

Sample Code: https://code.earthengine.google.com/9e34fbee9d350b1371f6a8deedcf601b

#### Data available from
https://www.isda-africa.com/isdasoil/

#### License
The data associated with iSDAsoil is available under a Creative Commons CC-BY 4.0 licence

#### Provided by :
iSDAsoil

Created and Curated by: Innovative Solutions for Decision Agriculture (iSDAsoil)

Keywords: soil, Africa, iSDA

Last updated: 2021-05-30
