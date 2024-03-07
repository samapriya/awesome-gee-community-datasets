# GLOBGM v1.0 global-scale groundwater model

The GLOBGM v1.0 dataset marks a significant milestone in global groundwater modeling, offering a parallel implementation of a 30 arcsec PCR-GLOBWB-MODFLOW model. Developed by Jarno Verkaik et al., this dataset presents a comprehensive understanding of global groundwater dynamics at a spatial resolution of approximately 1 km at the Equator. Leveraging two model layers and the MODFLOW 6 framework, the dataset utilizes available 30′′ PCR-GLOBWB data to drive simulations, enabling researchers to explore groundwater flow dynamics on a global scale. The computational implementation is parallelized using the message-passing interface, facilitating efficient processing on distributed memory parallel clusters.

Covering the globe, excluding Greenland and Antarctica, the GLOBGM v1.0 dataset offers insights into various aspects of groundwater behavior. Despite its uncalibrated nature, the dataset undergoes limited evaluation using USGS National Water Information System (NWIS) head observations for the contiguous United States (CONUS). You can read the [paper here to understand the methodology better](https://gmd.copernicus.org/articles/17/275/2024/gmd-17-275-2024-discussion.html).

#### Data strucutre

This table provides a structured overview of the model raster outputs for the GLOBGM dataset, including file paths and descriptions of each file.

| File Path                                            | Description                                  |
|------------------------------------------------------|----------------------------------------------|
| /steady-state/globgm-heads-lower-layer-ss.tif        | Computed steady-state groundwater head [m] for the lower model layer |
| /steady-state/globgm-heads-lower-layer-ss.tif        | Computed steady-state groundwater head [m] for the upper model layer |
| /steady-state/globgm-wtd-ss.tif                     | Computed water table depth [m] (sampled from upper to lower layer) |
| /transient_1958-2015/globgm-wtd-<date>.tif          | Computed water table depth [m] (sampled from upper to lower layer) |
| /transient_1958-2015/globgm-wtd-bot-<date>*.tif     | Computed water table depth [m] (lower layer only) |

#### Citation

```
Verkaik, Jarno, Edwin H. Sutanudjaja, Gualbert HP Oude Essink, Hai Xiang Lin, and Marc FP Bierkens. "GLOBGM v1. 0: a parallel implementation of a 30
arcsec PCR-GLOBWB-MODFLOW global-scale groundwater model." Geoscientific Model Development 17, no. 1 (2024): 275-300.
```

#### Data Citation

```
Verkaik, J., Hughes J.D., Langevin, C.D., (2021). Parallel MODFLOW 6.2.1 prototype release 0.1 (6.2.1_0.1). Zenodo.
```

![globgm](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/b53a35a3-6a0b-4225-ba7c-ac995c1161bd)

#### Earth Engine Snippet

```js
var wtd = ee.ImageCollection("projects/sat-io/open-datasets/GLOBGM/TRANSIENT/WTD");
var wtd_bt = ee.ImageCollection("projects/sat-io/open-datasets/GLOBGM/TRANSIENT/WTD-BOTTOM");
var globgm_wtd_ss = ee.Image("projects/sat-io/open-datasets/GLOBGM/STEADY-STATE/globgm-wtd-ss");
var globgm_heads_lower_layer_ss = ee.Image("projects/sat-io/open-datasets/GLOBGM/STEADY-STATE/globgm-heads-lower-layer-ss");
var globgm_heads_upper_layer_ss = ee.Image("projects/sat-io/open-datasets/GLOBGM/STEADY-STATE/globgm-heads-upper-layer-ss");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/GLOBGM-GROUNDWATER-MODEL

#### License
GLOBGM v1.0 is open source and distributed under the terms of GNU General Public License v3.0, or any later version, as published by the Free
Software Foundation.

Created by: Verkaik et al. 2024

Curated in GEE by : Samapriya Roy

Keywords: GLOBGM,groundwater,global-scale modeling,PCR-GLOBWB,MODFLOW,high performance computing

Last updated in GEE: 2024-02-04
