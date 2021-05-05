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


|Name                 |Variable                                                          |Unit                                                                           |Assets on GEE                                                                                                    |
|:--------------------|:-----------------------------------------------------------------|:------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------|
|ORMC                 |Organic Matter Content                                            |%                                                                              |[ormc](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/ormc)            |
|STC                  |Soil Texture Class                                                |O (Organic), VF (Very Fine), F (Fine), MF (Medium Fine), C (Coarse), M (Medium)|[stc](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/stc)              |
|ALPHA                |Alpha parameter for Mualem Van Genuchten Equation                 |1/cm                                                                           |[alpha](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/alpha)          |
|N                    |N parameter for Mualem Van Genuchten Equation                     |-                                                                              |[N](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/N)                  |
|WCsat                |Saturated Water Content                                           |m 3 /m3                                                                        |[wcsat](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/wcsat)          |
|WCres                |Residual Water Content                                            |m 3 /m3                                                                        |[wcres](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/wcres)          |
|Ksat                 |Saturated Hydraulic Conductivity                                  |cm/d                                                                           |[ksat](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/ksat)            |
|WCpF2                |Water content at pF2 (field capacity)                             |m 3 /m3                                                                        |[wcpf2](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/wcpf2)          |
|WCpF3                |Water content at pF3 (wilting point)                              |m 3 /m3                                                                        |[wcpf3](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/wcpf3)          |
|WCpF4.2              |Water content at pF4.2 (permanent wilting point)                  |m 3 /m3                                                                        |[wcpf4-2](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/wcpf4-2)      |
|WCavail              |Available water content                                           |m 3 /m3                                                                        |[wcavail](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/wcavail)      |
|SAT-FIELD            |Water content between saturation point and field capacity (pF2)   |m 3 /m3                                                                        |[sat-field](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/sat-field)  |
|FIELD-WILT           |Water content between field capacity (pF2_ and wilting point (pF3)|m 3 /m3                                                                        |[field-wilt](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/field-crit)|
|WILT-PERM            |Water content between wilting point (pF3)                         |m 3 /m3                                                                        |[wilt-perm](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/crit-wilt)  |
|Hydrologic_Soil_Group|Hydrologic Soil Group                                             |A (low runoff potential when thoroughly wet) water transmitted freely<br>B (moderately low runoff when thoroughly wet) transmission unimpeded<br>C (moderately high Runoff when thoroughly wet) transmission somewhat restricted<br>D (High Runoff potential when thoroughly wet) water movement restricted<br>Dual hydrologic group soils with 60cm from surface (A/D, B/D and C/D )based on their saturated hydraulic conductivity & water table depth First letter drained condition, second undrained condition      |[hydrologic-soil-group](https://code.earthengine.google.com/?asset=projects/sat-io/open-datasets/HiHydroSoilv2_0/Hydrologic_Soil_Group_250m)                                                           |

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
var wilt_perm = ee.ImageCollection("projects/sat-io/open-datasets/HiHydroSoilv2_0/crit-wilt"),
var field_wilt = ee.ImageCollection("projects/sat-io/open-datasets/HiHydroSoilv2_0/field-crit");
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
