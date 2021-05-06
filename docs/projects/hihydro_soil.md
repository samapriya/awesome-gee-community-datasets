#  HiHydroSoil v2.0 layers

**In May 2020, ISRIC has released the latest version (v2.0) of its Soilgrids250m product. This release has made it possible for [FutureWater](https://www.futurewater.eu) to update its HiHydroSoil v1.2 database with newer, more precise and with a higher resolution soil data, which resulted in the development and release of HiHydroSoil v2.0.**

Soil information is the basis for all environmental studies. Since local soil maps of good quality are often not available, global soil maps with a low resolution are used. Furthermore, soil maps do not include information about soil hydraulic properties, which are of importance in, for example, hydrological modeling, erosion assessment and crop yield modelling. HiHydroSoil v2.0 can fill this data gap. HiHydroSoil v2.0 includes the following data and additional information along with links to download the data can be [found here](https://www.futurewater.eu/projects/hihydrosoil/)

* Organic Matter Content
* Soil Texture Class
* Saturated Hydraulic Conductivity
* Mualem van Genuchten parameters Alpha and N
* Saturated Water Content
* Residual Water Content
* Water content at pF2, pF3 and pF4.2
* Hydrologic Soil Group (USDA)

The Hydrologic Soil Group (HSG) determines the Runoff Curve Number which is often used in hydrological modelling to estimate the direct runoff from rainfall. Four hydrologic soil groups and three dual hydrologic soil groups. The data layers originally consisting of float data type were multiplied by a factor of 10,000 and subsequently converted to integer type. It is therefore required to translate the data to the proper units by multiplying with 0.0001.

#### Citation & Related Publications

```
Simons, G.W.H., R. Koster, P. Droogers. 2020. HiHydroSoil v2.0 - A high resolution soil map of global hydraulic properties.
FutureWater Report 213.
```

You can [download the report here](https://www.futurewater.nl/wp-content/uploads/2020/10/HiHydroSoil-v2.0-High-Resolution-Soil-Maps-of-Global-Hydraulic-Properties.pdf)


|Variable                                                                                  |Unit                                                                                                                                         |Description                                                                                                                                                                                                                                                                                                                                   |Range                 |Assets on GEE                                                                                                                                |
|:-----------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
|Organic Matter Content (ORMC)                                                             |%                                                                                                                                            |Soil organic matter (SOM) is the organic matter component of soil, consisting of plant and animal detritus at various stages of decomposition, cells and tissues of soil microbes, and substances that soil microbes synthesize.                                                                                                              |0 - 50                |[ormc](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/ormc)                                        |
|Soil Texture Class (STC)                                                                  |O (Organic), VF (Very Fine), F (Fine), MF (Medium Fine), C (Coarse), M (Medium)                                                              |Soil texture is a classification instrument used both in the field and laboratory to determine soil classes based on their physical texture.                                                                                                                                                                                                  |1- 6 (see column Unit)|[stc](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/stc)                                          |
|Alpha parameter for Mualem Van Genuchten Equation (ALPHA)                                 |1/cm                                                                                                                                         |The shape of water retention curves can be characterized by several models, one of them known as the van Genuchten model. The Alpha parameter in this model is related to the inverse of the air entry suction.                                                                                                                               |0 - 0.2               |[alpha](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/alpha)                                      |
|N parameter for Mualem Van Genuchten Equation (N)                                         |-                                                                                                                                            |The shape of water retention curves can be characterized by several models, one of them known as the van Genuchten model. The N parameter in this model is a measure of the pore-size distribution.                                                                                                                                           |1 - 2.3               |[N](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/N)                                              |
|Saturated Water Content (Wcsat)                                                           |m3/m3                                                                                                                                        |Saturated water content is the maximum amount of water a soil can store and which is equivalent to the porosity of the soil.                                                                                                                                                                                                                  |0.25 - 0.85           |[wcsat](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/wcsat)                                      |
|Residual Water Content (Wcres)                                                            |m3/m3                                                                                                                                        |The residual volumetric water content  represents the volumetric water content of a soil where a further increase in negative pore-water pressure does not produce significant changes in water content.                                                                                                                                      |0 - 0.02              |[wcres](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/wcres)                                      |
|Saturated Hydraulic Conductivity (Ksat)                                                   |cm/d                                                                                                                                         |Saturated hydraulic conductivity is a quantitative measure of a saturated soil's ability to transmit water when subjected to a hydraulic gradient. It can be thought of as the ease with which pores of a saturated soil permit water movement.                                                                                               |0 - 1500              |[ksat](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/ksat)                                        |
|Water content at pF2 (field capacity) (WCpF2)                                             |m3/m3                                                                                                                                        |Field Capacity is the amount of soil moisture or water content held in the soil after excess water has drained away and the rate of downward movement has decreased. It's the upper limit of the rapidly available water for plants at a matric potential of -100 cm or pF2.                                                                  |0 - 0.8               |[wcpf2](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/wcpf2)                                      |
|Water content at pF3 (critical point)  (WCpF3)                                            |m3/m3                                                                                                                                        |Critical point: lower limit of rapidly available water for plants. Upper limit of slowly available water for plants. This is at a matric potential of -1000 cm or pF3.                                                                                                                                                                        |0 - 0.7               |[wcpf3](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/wcpf3)                                      |
|Water content at pF4.2 (permanent wilting point)  (WCpF4.2)                               |m3/m3                                                                                                                                        |Plants can - on average - produce a suction till 16 x atmospheric pressure before a plants starts to permanently wilt. This atmosperic pressures is similar to a matrix potentential of -16000 cm, or pF 4.2.                                                                                                                                 |0 - 0.7               |[wcpf4-2](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/wcpf4-2)                                  |
|Available water content (Wcavail)                                                         |m3/m3                                                                                                                                        |The amount of water between field capacity (pF2) and permanent wilting point (pF4.2). This value should be used with caution. First, plants will start wilting with subsequent yield losses well before the permanent wilting point. Secondly, plant available soil water is replenished by capillary rise, rainfall and irrigation water.    |0 - 0.6               |[wcavail](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/wcavail)                                  |
|Water content between saturation point and field capacity (pF2) (SAT_FIELD)               |m3/m3                                                                                                                                        |Water content between saturation point and field capacity (pF2)                                                                                                                                                                                                                                                                               |…                     |[sat-field](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/sat-field)                              |
|Water content between field capacity (pF2) and critical point (pF3) (FIELD-CRIT)          |m3/m3                                                                                                                                        |Water content between field capacity (pF2) and critical point (pF3)                                                                                                                                                                                                                                                                           |0 - 0.4               |[field-crit](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/field-crit)                            |
|Water content between critical point (pF3) and permanent wilting point (pF4.2) (CRIT-WILT)|m3/m3                                                                                                                                        |Water content between critical point (pF3) and permanent wilting point (pF4.2)                                                                                                                                                                                                                                                                |0 - 0.25              |[crit-wilt](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/crit-wilt)                              |
|Hydrologic Soil Group                                                                     |A (low runoff potential), A/D, B (moderately low runoff potential), B/D, C (moderately high runoff potential), C/D, D (high runoff potential)|Along with land use, land management practices and soil hydrologic conditions the Hydrologic Soil Group (HSG) determines the Runoff Curve Number which is often used in hydrological modelling to estimate the direct runoff from rainfall. Four hydrologic soil groups and three dual hydrologic soil groups are described by the USDA (2009)|                      |[hydrologic-soil-group](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/Hydrologic_Soil_Group_250m) |


#### Earth Engine Snippet: HiHydro Layers (Hydrologic_Soil_Group_250m)

```js
var hydrologic_soil_group = ee.Image('projects/sat-io/open-datasets/HiHydroSoilv2_0/Hydrologic_Soil_Group_250m');
```

![soil_hydro_group](https://user-images.githubusercontent.com/6677629/117184621-87d12200-ad9e-11eb-9cdc-fb371b810d93.gif)

#### Raster Value Map

|ClassValue|Hydrologic Soil Group                                                                                              |
|:---------|:------------------------------------------------------------------------------------------------------------------|
|1         | A (low runoff potential when thoroughly wet) water transmitted freely                                             |
|2         | B (moderately low runoff when thoroughly wet) transmission unimpeded                                              |
|3         | C (moderately high Runoff when thoroughly wet) transmission somewhat restricted                                   |
|4         | D (High Runoff potential when thoroughly wet) water movement restricted                                           |
|14        | A/D Dual hydrologic group soils with 60cm from surface. First letter drained condition, second undrained condition|
|24        | B/D Dual hydrologic group soils with 60cm from surface. First letter drained condition, second undrained condition|
|34        | C/D Dual hydrologic group soils with 60cm from surface. First letter drained condition, second undrained condition|


Sample Code: https://code.earthengine.google.com/4da512c4c0785ef2767f159028579fc6


#### Earth Engine Snippet: HiHydro Additional Layers

```js
var ksat = ee.ImageCollection("projects/sat-io/open-datasets/HiHydroSoilv2_0/ksat");
var satfield = ee.ImageCollection("projects/sat-io/open-datasets/HiHydroSoilv2_0/sat-field");
var N = ee.ImageCollection("projects/sat-io/open-datasets/HiHydroSoilv2_0/N");
var alpha = ee.ImageCollection("projects/sat-io/open-datasets/HiHydroSoilv2_0/alpha");
var crit_wilt = ee.ImageCollection("projects/sat-io/open-datasets/HiHydroSoilv2_0/crit-wilt"),
var field_cirt = ee.ImageCollection("projects/sat-io/open-datasets/HiHydroSoilv2_0/field-crit");
var ormc = ee.ImageCollection("projects/sat-io/open-datasets/HiHydroSoilv2_0/ormc");
var stc = ee.ImageCollection("projects/sat-io/open-datasets/HiHydroSoilv2_0/stc");
var wcavail = ee.ImageCollection("projects/sat-io/open-datasets/HiHydroSoilv2_0/wcavail");
var wcpf2 = ee.ImageCollection("projects/sat-io/open-datasets/HiHydroSoilv2_0/wcpf2");
var wcpf3 = ee.ImageCollection("projects/sat-io/open-datasets/HiHydroSoilv2_0/wcpf3");
var wcpf4_2 = ee.ImageCollection("projects/sat-io/open-datasets/HiHydroSoilv2_0/wcpf4-2");
var wcres = ee.ImageCollection("projects/sat-io/open-datasets/HiHydroSoilv2_0/wcres");
var wcsat = ee.ImageCollection("projects/sat-io/open-datasets/HiHydroSoilv2_0/wcsat");
```

![hihydro_layers](https://user-images.githubusercontent.com/6677629/117179637-ef846e80-ad98-11eb-967f-e169fe7d84ba.gif)

Sample Code: https://code.earthengine.google.com/2b6f1aaf0b2acbf74a06144ed26ad606

#### License Information
HiHydroSoil v2.0 can be used freely and redistributed with attribution. No additional information made available by authors.

Curated by: William Ouellette and Samapriya Roy

Keywords: Global Hydrologic Soil Group, Hydrology, Hydrological, Soil, Hydraulic, Conductivity, Runoff, Run-off, Water, Water Cycle

Last updated dataset: October 2020
Last curated: 2021-05-05
