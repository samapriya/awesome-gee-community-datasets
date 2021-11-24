# World Settlement Footprint & Evolution

### World Settlement Footprint 2015

The World Settlement Footprint (WSF) 2015 is a 10m (0.32 arc sec) resolution binary mask outlining the 2015 global settlement extent derived by jointly exploiting multitemporal Sentinel-1 radar and Landsat-8 optical satellite imagery.

**The world settlement footprint 2015 is now available in the official GEE catalog and [you can find it here](https://developers.google.com/earth-engine/datasets/catalog/DLR_WSF_WSF2015_v1)**

The entire catalog consists of 306 GeoTIFF files (EPSG4326 projection, deflate compression) each one referring to a portion of 10x10 degree size (~1110x1110km) whose upper-left and lower-right corner coordinates are specified in the file name [e.g., the tile WSF2015_v1_EPSG4326_e010_n60_e020_n50.tif covers the area between (10E;60N) and (20E;50N)].

Settlements are associated with value 255; all other pixels are associated with value 0.


### World Settlement Footprint (WSF) 2019

The World Settlement Footprint (WSF 2019) is a 10m resolution binary mask outlining the extent of human settlements globally derived by means of 2019 multitemporal Sentinel-1 and Sentinel-2 imagery.

The dataset is organized in 5138 GeoTIFF files (EPSG4326 projection) each one referring to a portion of 2x2 degree size (~222x222km on the ground) with an extra buffer of 0.1 degree to avoid any discontinuity between neighbour tiles. Each tile is identified by the lower-left corner coordinates specified in the file name [e.g., the tile WSF2019_v1_12_18.tif covers the area between (12E;18N) and (14E;20N)]. You can [download the files here](https://download.geoservice.dlr.de/WSF2019/files/)

Settlements are associated with value 255; all other pixels are associated with value 0.

### World Settlement Footprint Evolution (1985-2015)

This repository contains the World Settlement Footprint (WSF) Evolution, a 30m resolution layer outlining the global settlement extent on a yearly basis from 1985 to 2015 derived by means of multitemporal Landsat-5 and Landsat-7 imagery.

The dataset is organized in 5138 GeoTIFF files (EPSG4326 projection) each one referring to a portion of 2x2 degree size (~222x222km on the ground) with an extra buffer of 0.1 degree to avoid any discontinuity between neighbour tiles. Each tile is identified by the lower-left corner coordinates specified in the file name [e.g., the tile WSFevolution_v1_12_18.tif covers the area between (12E;18N) and (14E;20N)]. You can [download the files here](https://download.geoservice.dlr.de/WSF_EVO/files/)

Values range between 1985 and 2015 corresponding to the estimated year of settlement detection, whereas 0 is no data.



#### Data Citation

```
Marconcini, Mattia; Metz-Marconcini, Annekatrin; Üreyen, Soner; Palacios-Lopez,
Daniela; Hanke, Wiebke; Bachofer, Felix; et al. (2020): World Settlement Footprint (WSF) 2015.
figshare. Dataset. https://doi.org/10.6084/m9.figshare.10048412.v1
```

You can read the [Outlining where humans live, the World Settlement Footprint 2015 here](https://www.nature.com/articles/s41597-020-00580-5) and [Understanding Current Trends
in Global Urbanisation – The World Settlement Footprint suite here](https://austriaca.at/0xc1aa5576_0x003c9b4c.pdf)

#### Paper Citation

```
Marconcini, Mattia, Annekatrin Metz-Marconcini, Soner Üreyen, Daniela Palacios-Lopez,
Wiebke Hanke, Felix Bachofer, Julian Zeidler et al. "Outlining where humans live,
the World Settlement Footprint 2015." Scientific Data 7, no. 1 (2020): 1-14.

Marconcini, M., Metz-Marconcini, A., Esch, T., Gorelick, N. (2021). Understanding Current Trends
in Global Urbanisation – The World Settlement Footprint suite. GI_Forum, 1, 33-38.
https://doi.org/10.1553/giscience2021_01_s33.
```

![wsf](https://user-images.githubusercontent.com/6677629/143169273-5acbf695-fd6e-44eb-af47-f5109bbbeab1.gif)


#### Earth Engine Snippet

The dataset is single value only with a value of 255 for WSF 2015 and 2019 and pixel values are 1985 to 2015 for the WSF evolution dataset.

```js
var wsf2015 = ee.ImageCollection("projects/sat-io/open-datasets/WSF/WSF_2015");
var wsf2019 = ee.ImageCollection("projects/sat-io/open-datasets/WSF/WSF_2019");
var wsf_evo = ee.ImageCollection("projects/sat-io/open-datasets/WSF/WSF_EVO");
```

Sample Code: https://code.earthengine.google.com/2f94935ff4d43327ae10677f5c08e268

#### License
The World Settlement Footprint 2015 is released under a CC0 1.0 Universal (CC0 1.0) Public Domain Dedication. You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.

The World Settlement Footprint 2019 is licensed under CC-BY-4.0.

The World Settlement Footprint evolution 1985-2015 is licensed under CC-BY-4.0.

Created by : Marconcini, et al

Curated in GEE by: Samapriya Roy

Keywords: World Settlement Footprint, Settlement Extent, Urbanization, Earth Observation, Remote Sensing, Sentinel-1, Landsat-8

Last updated : 2021-11-23
