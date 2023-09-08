# South African National Land Cover (SANLC)

The South African National Land Cover (SANLC) datasets are a series of land cover classification datasets for South Africa. The datasets are based on the gazetted land-cover classification standard (SANS 19144-2) and have 73 classes of information. New updates includes the 2020 SANLC apart from the 2018 dataset included earlier.The South African National Land-Cover 2018 dataset has been generated from 20 meter multi-seasonal Sentinel 2 satellite imagery. The imagery used represents the full temporal range of available imagery acquired by Sentinel 2 during the period 01 January 2018 to 31 December 2018. The SANLC 2018 dataset is based primarily on the new gazetted land-cover classification standard (SANS 19144-2) with 73 classes of information and is comparable, with the previous 1990 and 2013-14 South African National Land-Cover (SANLC) datasets. The previous land cover classes are also included for comparisons.

The SANLC 2018 data was launched on the 1st October 2019 and is now available for download from the E-GIS website, download link: https://egis.environment.gov.za/gis_data_downloads.

![sa_nlc2018](https://user-images.githubusercontent.com/6677629/122017527-ab1cc300-cd87-11eb-95bd-aa66c9e4d53a.gif)

#### Earth Engine Snippet

```js
var sa_nlc2018 = ee.Image('projects/sat-io/open-datasets/landcover/SA_NLC_1990');
var sa_nlc2018 = ee.Image('projects/sat-io/open-datasets/landcover/SA_NLC_2018');
var sa_nlc2013_2014 = ee.Image('projects/sat-io/open-datasets/landcover/SA_NLC_2013_2014');
var sa_nlc_2020 = ee.Image('projects/sat-io/open-datasets/landcover/SA_NLC_2020');
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:regional-landuse-landcover/SOUTH-AFRICA-LULC


|No.|Legend Colour|2018 NLC Class Name                                              |
|---|-------------|-----------------------------------------------------------------|
|1  |#F2F2F2      |Contiguous (indigenous) Forest (combined very high, high, medium)|
|2  |#065106      |Contiguous Low Forest & Thicket (combined classes)               |
|3  |#005F00      |Dense Forest & Woodland (35 - 75% cc)                            |
|4  |#008500      |Open Woodland (10 - 35% cc)                                      |
|5  |#F74006      |Contiguous & Dense Planted Forest (combined classes)             |
|6  |#F9764D      |Open & Sparse Planted Forest                                     |
|7  |#F9906C      |Temporary Unplanted Forest                                       |
|8  |#B8ABD1      |Low Shrubland (other regions)                                    |
|9  |#8FAB39      |Low Shrubland (Fynbos)                                           |
|10 |#AC92C5      |Low Shrubland (Succulent Karoo)                                  |
|11 |#AC9CDA      |Low Shrubland (Nama Karoo)                                       |
|12 |#85D285      |Sparsely Wooded Grassland (5 - 10% cc)                           |
|13 |#D2B485      |Natural Grassland                                                |
|14 |#00009F      |Natural Rivers                                                   |
|15 |#041FA7      |Natural Estuaries & Lagoons                                      |
|16 |#0639AB      |Natural Ocean, Coastal                                           |
|17 |#0D50AC      |Natural Lakes                                                    |
|18 |#125FAC      |Natural Pans (flooded @ obsv time)                               |
|19 |#1373B4      |Artificial Dams (incl. canals)                                   |
|20 |#1D81B6      |Artificial Sewage Ponds                                          |
|21 |#1F8EB8      |Artificial Flooded Mine Pits                                     |
|22 |#06DEDC      |Herbaceous Wetlands (currently mapped)                           |
|23 |#06E0D0      |Herbaceous Wetlands (previous mapped extent)                     |
|24 |#9F1FEC      |Mangrove Wetlands                                                |
|25 |#ffffe0      |Natural Rock Surfaces                                            |
|26 |#DCDAC5      |Dry Pans                                                         |
|27 |#F9E0E0      |Eroded Lands                                                     |
|28 |#F9F9C5      |Sand Dunes (terrestrial)                                         |
|29 |#F9F9A7      |Coastal Sand Dunes & Beach Sand                                  |
|30 |#CDD2E0      |Bare Riverbed Material                                           |
|31 |#ffffe0      |Other Bare                                                       |
|32 |#A62C39      |Cultivated Commercial Permanent Orchards                         |
|33 |#B31F5C      |Cultivated Commercial Permanent Vines                            |
|34 |#DB0000      |Cultivated Commercial Sugarcane Pivot Irrigated                  |
|35 |#9F3978      |Commercial Permanent Pineapples                                  |
|36 |#FF0000      |Cultivated Commercial Sugarcane Non-Pivot (all other)            |
|37 |#F64D6C      |Cultivated Emerging Farmer Sugarcane Non-Pivot (all other)       |
|38 |#381A12      |Commercial Annuals Pivot Irrigated                               |
|39 |#521F1C      |Commercial Annuals Non-Pivot Irrigated                           |
|40 |#85402C      |Commercial Annuals Crops Rain-Fed / Dryland / Non-Irrigated      |
|41 |#C5735F      |Subsistence / Small-Scale Annual Crops                           |
|42 |#C1436C      |Fallow Land & Old Fields (Trees)                                 |
|43 |#C55E82      |Fallow Land & Old Fields (Bush)                                  |
|44 |#D27592      |Fallow Land & Old Fields (Grass)                                 |
|45 |#E0AAB8      |Fallow Land & Old Fields (Bare)                                  |
|46 |#DB90A9      |Fallow Land & Old Fields (Low Shrub)                             |
|47 |#ECDB0F      |Residential Formal (Tree)                                        |
|48 |#F6EC13      |Residential Formal (Bush)                                        |
|49 |#F9F81F      |Residential Formal (low veg / grass)                             |
|50 |#FFFF29      |Residential Formal (Bare)                                        |
|51 |#EC82EC      |Residential Informal (Tree)                                      |
|52 |#F691E0      |Residential Informal (Bush)                                      |
|53 |#F99FCF      |Residential Informal (low veg / grass)                           |
|54 |#FFC5CF      |Residential Informal (Bare)                                      |
|55 |#ECC500      |Village Scattered (bare only)                                    |
|56 |#FFD91F      |Village Dense (bare only)                                        |
|57 |#AC7879      |Smallholdings (Tree)                                             |
|58 |#B89192      |Smallholdings (Bush)                                             |
|59 |#C49C9E      |Smallholdings (low veg / grass)                                  |
|60 |#D2B8B8      |Smallholdings (Bare)                                             |
|61 |#BFFF00      |Urban Recreational Fields (Tree)                                 |
|62 |#33FF33      |Urban Recreational Fields (Bush)                                 |
|63 |#66FF66      |Urban Recreational Fields (Grass)                                |
|64 |#99FF99      |Urban Recreational Fields (Bare)                                 |
|65 |#C49F0D      |Commercial                                                       |
|66 |#8F8506      |Industrial                                                       |
|67 |#F9DD03      |Roads & Rail (Major Linear)                                      |
|68 |#FFFF00      |Mines: Surface Infrastructure                                    |
|69 |#B30606      |Mines: Extraction Sites: Open Cast & Quarries combined           |
|70 |#C50606      |Mines: Extraction Sites: Salt Mines                              |
|71 |#D21D1A      |Mines: Waste (Tailings) & Resource Dumps                         |
|72 |#F95479      |Land-fills                                                       |
|73 |#6CE7DC      |Fallow Land & Old Fields (wetlands)                              |


#### License

The South African National Land-Cover 2018 dataset is available on an open licence agreement.

Created by: Department of Forestry, Fisheries and the Environment, Republic of South Africa

Curated by: Geethen Singh & Samapriya Roy

Keywords: : land use, South Africa, land cover, Sentinel-2, copernicus, sentinel, satellite

Last updated: 2023-09-07
