# Hydrography 90m Layers

The Hydrography 90 layers uses the MERIT Hydro digital elevation model at 3 arcsec (∼ 90 m at the Equator) to derive a globally seamless, standardised hydrographic network, the "Hydrography90m", with corresponding stream topographic and topological information. A central feature of
the network is the minimal upstream contributing area, i.e. flow accumulation, of 0.05 km2 (or 5 ha) to initiate a stream channel, which allowed us to extract headwater stream channels in great detail.

The data validation procedures confirmed Hydrography90m as a more accurate representation of stream networks compared to HydroRIVERS, GRWL, and MERIT
Hydro–Vector. Improved accuracy was achieved principally by employing a higher resolution DEM, the MD8 flow routing algorithm, and a markedly smaller flow accumulation threshold to initiate stream channels. With these characteristics, Hydrography90m provides a valuable basis for supporting a variety of freshwater-related research disciplines. Find additional details [in the paper here](https://essd.copernicus.org/articles/14/4525/2022/essd-14-4525-2022.pdf). The datasets can [be downloaded here](https://hydrography.org/hydrography90m/hydrography90m_layers/). This is one of the highest resolution global hydrography datasets and has multiple applications.

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Dataset Preprocessing
The hydrography datasets can (downloaded here](https://hydrography.org/hydrography90m/hydrography90m_layers/). The folders were renamed based on the descriptions of the papers and are included in the tables below. The parameter name were kept consistent and additional information is provided as need along with units for said parameters.

#### Paper Citation

```
Amatulli, Giuseppe, Jaime Garcia Marquez, Tushar Sethi, Jens Kiesel, Afroditi Grigoropoulou, Maria M. Üblacker, Longzhu Q. Shen, and Sami Domisch.
"Hydrography90m: A new high-resolution global hydrographic dataset." Earth System Science Data 14, no. 10 (2022): 4525-4550.
```

#### Data structure: basin-network-layers
Base and network layers of Hydrography90m: flow accumulation, flow direction, drainage basins, outlets, stream segments, subcatchments,
regional units, and depression

|Output map description    |Unit                                                            |GEE Collection Name|
|--------------------------|----------------------------------------------------------------|-------------------|
|Flow accumulation (raster)|km2 accumulation=acc                                            |flow_accumulation  |
|Flow direction (raster)   |NE–N–NW–W–SW–S–SE–E  correspond to 1–2–3–4–5–6–7–8              |flow__direction    |
|Drainage basin (raster)   |IDs from 1 to 1 676 628                                         |drainage_basin     |
|Outlets (raster)          |ID=1 stream_vector=stream threshold=0.05; v.to.rast input=stream|outlet             |
|Depression (raster)       |ID = 1                                                          |depression         |
|Stream segment (raster)   |IDs from 1 to 726 723 221                                       |segment            |
|Sub-catchment (raster)    |IDs from basins=sub_catchment                                   |sub_catchment      |
|Regional unit (raster)    |IDs from 1 to 116 IDs from 150 to 200                           |regional_unit      |

![basin-network](https://user-images.githubusercontent.com/6677629/202756025-7aa160d1-0b9d-45aa-8b81-2ab754d9c7f6.gif)

#### Earth Engine snippet: basin-network-layers

```js
var flow_accumulation = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/base-network-layers/flow_accumulation");
var flow_direction = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/base-network-layers/flow_direction");
var depression = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/base-network-layers/depression");
var drainage_basin = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/base-network-layers/drainage_basin");
var outlet = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/base-network-layers/outlet");
var regional_unit = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/base-network-layers/regional_unit");
var segment = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/base-network-layers/segment");
var sub_catchment = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/base-network-layers/sub_catchment");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/HYDROGRAPHY90-BASE-NETWORK

#### Data structure: stream-slope
Curvature, gradient (elevation difference divided by distance), and elevation difference raster maps.

|Output raster map description                                                   |Unit                         |GEE Collection Name  |
|--------------------------------------------------------------------------------|-----------------------------|---------------------|
|Maximum curvature between highest upstream cell, focal cell, and downstream cell|m^-1 (scale factor 10^6)     |slope_curv_max_dw_cel|
|Minimum curvature between highest upstream cell, focal cell, and downstream cell|m^-1 (scale factor 10^6)     |slope_curv_min_dw_cel|
|Elevation difference between focal cell and downstream cell                     |m                            |slope_elv_dw_cel     |
|Focal cell gradient                                                             |Unitless (scale factor 10^6) |slope_grad_dw_cel    |

![stream-slope](https://user-images.githubusercontent.com/6677629/202982368-7947a026-103d-462d-b0f0-9e5e36dd18f9.gif)

#### Earth Engine Snippet: stream-slope

```js
var slope_curv_max_dw_cel = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-slope/slope_curv_max_dw_cel");
var slope_curv_min_dw_cel = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-slope/slope_curv_min_dw_cel");
var slope_elv_dw_cel = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-slope/slope_elv_dw_cel");
var slope_grad_dw_cel = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-slope/slope_grad_dw_cel");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/HYDROGRAPHY90-STREAM-SLOPE

#### Data structure: stream-outlet-distance
Stream or outlet distance and elevation difference raster maps.

|Output raster map description                                                                      |Unit|GEE collection name  |
|---------------------------------------------------------------------------------------------------|----|---------------------|
|Shortest upstream distance between focal grid cell and the nearest sub-catchment drainage divide   |m   |stream_dist_up_near  |
|Longest upstream distance between focal grid cell and the nearest sub-catchment drainage divide    |m   |stream_dist_up_farth |
|Distance between focal grid cell and its nearest downstream stream grid cell                       |m   |stream_dist_dw_near  |
|Distance between focal grid cell and the outlet grid cell in the network                           |m   |outlet_dist_dw_basin |
|Distance between focal grid cell and the downstream stream node grid cell                          |m   |outlet_dist_dw_scatch|
|Euclidean distance between focal grid cell and the stream network                                  |m   |stream_dist_proximity|
|Elevation difference of the shortest path from focal grid cell to the sub-catchment drainage divide|m   |stream_diff_up_near  |
|Elevation difference of the longest path from focal grid cell to the sub-catchment drainage divide |m   |stream_diff_up_farth |
|Elevation difference between focal grid cell and its nearest downstream stream pixel               |m   |stream_diff_dw_near  |
|Elevation difference between focal grid cell and the outlet grid cell in the network               |m   |outlet_diff_dw_basin |
|Elevation difference between focal grid cell and the downstream stream node grid cell              |m   |outlet_diff_dw_scatch|

![stream-distance](https://user-images.githubusercontent.com/6677629/202753611-beb69c1c-5c98-4971-b4c6-3d8a92e1daf2.gif)

#### Earth Engine snippet: stream-outlet-distance

```js
var outlet_diff_dw_basin = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-outlet-distance/outlet_diff_dw_basin");
var outlet_diff_dw_scatch = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-outlet-distance/outlet_diff_dw_scatch");
var outlet_dist_dw_basin = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-outlet-distance/outlet_dist_dw_basin");
var outlet_dist_dw_scatch = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-outlet-distance/outlet_dist_dw_scatch");
var stream_diff_dw_near = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-outlet-distance/stream_diff_dw_near");
var stream_diff_dw_far = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-outlet-distance/stream_diff_up_farth");
var stream_diff_up_near = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-outlet-distance/stream_diff_up_near");
var stream_dist_dw_near = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-outlet-distance/stream_dist_dw_near");
var stream_dist_proximity = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-outlet-distance/stream_dist_proximity");
var stream_dist_up_farth = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-outlet-distance/stream_dist_up_farth");
var stream_dist_up_near = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-outlet-distance/stream_dist_up_near");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/HYDROGRAPHY90-STREAM-OUTLET-DIST

#### Data structure: flow-index

The compound topographic index (cti), stream power index (spi), and stream transportation index (sti) derived from flow accumu- lation (α) and terrain slope (β)

|Output raster map description    |Unit                        |GEE collection name|
|---------------------------------|----------------------------|-------------------|
|Stream power index (spi)         |Unitless (scale factor 10^3)|spi                |
|Stream transportation index (sti)|Unitless (scale factor 10^3)|sti                |
|Compound topographic index (cti) |Unitless (scale factor 10^8)|cti                |

![flow_index](https://user-images.githubusercontent.com/6677629/202753614-ac4b62d7-4b7a-482b-a093-e6ea4a17d473.gif)

#### Earth Engine Snippet: flow-index

```js
var cti = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/flow_index/cti");
var spi = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/flow_index/spi");
var sti = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/flow_index/sti");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/HYDROGRAPHY90-FLOW-INDEX

#### Data structure:stream-order
Stream order rasters

|Output map description                   |GEE collection name|
|-----------------------------------------|-------------------|
|Strahler’s stream order (raster)         |order_strahler     |
|Shreve’s stream magnitude (raster)       |order_shreve       |
|Horton’s stream order (raster)           |order_horton       |
|Hack’s stream order (raster)             |order_hack         |
|Topological dimension of streams (raster)|order_topo         |

![stream-order](https://user-images.githubusercontent.com/6677629/202855983-9caad20c-0a20-4c83-89ae-404bf755f08a.gif)

#### Earth Engine snippet: stream-order

```js
var order_hack = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-order/order_hack");
var order_horton = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-order/order_horton");
var order_shreve = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-order/order_shreve");
var order_strahler = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-order/order_strahler");
var order_topo = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-order/order_topo");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/HYDROGRAPHY90-STREAM-ORDER


#### Data structure:curvature-gradient

Curvature, gradient (elevation difference divided by distance), and elevation change raster maps.

|Output raster map description                                                    |Unit                          |GEE collection name|
|---------------------------------------------------------------------------------|------------------------------|-------------------|
|Segment downstream mean gradient between focal cell and the node or outlet       |Unitless (scale factor 10^6)  |channel_grad_dw_seg|
|Segment upstream mean gradient between focal cell and the init or node           |Unitless (scale factor 10^6)  |channel_grad_up_seg|
|Upstream gradient between focal cell and the next cell                           |Unitless (scale factor 10^6)  |channel_grad_up_cel|
|Cell stream course curvature of the focal cell                                   |m^-1 (scale factor 10^6)      |channel_curv_cel   |
|Segment downstream elevation difference between focal cell and the node or outlet|m                             |channel_elv_dw_seg |
|Segment upstream elevation difference between focal cell and the init or node    |m                             |channel_elv_up_seg |
|Upstream elevation difference between focal cell and the next cell               |m (outlet cell value = 99 999)|channel_elv_up_cel |
|Downstream elevation difference between focal cell and the next cell             |m                             |channel_elv_dw_cel |
|Segment downstream distance between focal cell and the node or outlet            |m                             |channel_dist_dw_seg|
|Segment upstream distance between focal cell and the init or node                |m                             |channel_dist_up_seg|
|Upstream distance between focal cell and next cell                               |m                             |channel_dist_up_cel|

![stream-channel-small](https://user-images.githubusercontent.com/6677629/203386778-fe5f48bf-fda1-4eac-ae60-77b6390426cc.gif)

#### Earth Engine Snippet: curvature-gradient

```js
var channel_curv_cel = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-channel/channel_curv_cel");
var channel_dist_dw_seg = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-channel/channel_dist_dw_seg");
var channel_dist_up_cel = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-channel/channel_dist_up_cel");
var channel_dist_up_seg = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-channel/channel_dist_up_seg");
var channel_elv_dw_cel = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-channel/channel_elv_dw_cel");
var channel_elv_dw_seg = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-channel/channel_elv_dw_seg");
var channel_elv_up_cel = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-channel/channel_elv_up_cel");
var channel_elv_up_seg = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-channel/channel_elv_up_seg");
var channel_grad_dw_seg = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-channel/channel_grad_dw_seg");
var channel_grad_up_cel = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-channel/channel_grad_up_cel");
var channel_grad_up_seg = ee.ImageCollection("projects/sat-io/open-datasets/HYDROGRAPHY90/stream-channel/channel_grad_up_seg");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/HYDROGRAPHY90-STREAM-CHANNEL


### License

The dataset is licensed under a [Creative Commons "CC BY-NC 4.0" license](https://creativecommons.org/licenses/by-nc/4.0/).

Created by: Amatulli, Giuseppe, Jaime Garcia Marquez, Tushar Sethi, Jens Kiesel, Afroditi Grigoropoulou, Maria M. Üblacker, Longzhu Q. Shen, and Sami Domisch

Curated by: Samapriya Roy

Keywords: Hydrology, Hydrography, Slope, Channel, Stream, Runoff, Flow accumulation, Flow direction

Last updated in GEE: 2022-11-14
