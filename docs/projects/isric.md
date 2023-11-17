# Soil Grids 250m v2.0

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
Poggio, L., de Sousa, L. M., Batjes, N. H., Heuvelink, G. B. M., Kempen, B., Ribeiro, E., and Rossiter, D.: SoilGrids 2.0: producing soil information for the globe with quantified spatial uncertainty, SOIL, 7, 217–240, https://doi.org/10.5194/soil-7-217-2021, 2021.
```

![gee_isric_main](https://user-images.githubusercontent.com/6677629/96608670-44f6a380-12bf-11eb-9e0b-1419a891fa84.gif)

#### Earth Engine Snippet
```js
var isric_bdod_mean = ee.Image("projects/soilgrids-isric/bdod_mean");
var isric_cec = ee.Image("projects/soilgrids-isric/cec_mean");
var isric_cfvo = ee.Image("projects/soilgrids-isric/cfvo_mean");
var isric_clay = ee.Image("projects/soilgrids-isric/clay_mean");
var isric_sand = ee.Image("projects/soilgrids-isric/sand_mean");
var isric_silt = ee.Image("projects/soilgrids-isric/silt_mean");
var isric_nitrogen = ee.Image("projects/soilgrids-isric/nitrogen_mean");
var isric_phh20 = ee.Image("projects/soilgrids-isric/phh2o_mean");
var isric_soc = ee.Image("projects/soilgrids-isric/soc_mean");
var isric_ocd = ee.Image("projects/soilgrids-isric/ocd_mean");
var isric_ocs = ee.Image("projects/soilgrids-isric/ocs_mean");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:soil-properties/ISRIC-SOIL-GRID-250

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
