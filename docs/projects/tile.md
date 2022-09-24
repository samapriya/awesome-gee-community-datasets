# Tile Drained Croplands (30m)

Tile drainage is one of the dominant agricultural management practices in the United States and has greatly expanded since the late 1990s. It has proven effects on land surface water balance and quantity and quality of streamflow at the local scale. The effect of tile drainage on crop production, hydrology, and the environment on a regional scale is elusive due to lack of high-resolution, spatially-explicit tile drainage area information for the Contiguous United States (CONUS). We developed a 30-m resolution tile drainage map of the most-likely tile-drained area of the CONUS (AgTile-US) from county-level tile drainage census using a geospatial model that uses soil drainage information and topographic slope as inputs. Validation of AgTile-US with 16000 ground truth points indicated 86.03% accuracy at the CONUS-scale. Over the heavily tile-drained midwestern regions of the U.S., the accuracy ranges from 82.7% to 93.6%. These data can be used to study and model the hydrologic and water quality responses of tile drainage and to enhance streamflow forecasting in tile drainage dominant regions. You can read the [full paper here](https://www.nature.com/articles/s41597-020-00596-x)

#### Paper Citation

```
Valayamkunnath, P., Barlage, M., Chen, F. et al. Mapping of 30-meter resolution tile-drained croplands using a
geospatial modeling approach. Sci Data 7, 257 (2020). https://doi.org/10.1038/s41597-020-00596-x
```

![tile_drain](https://user-images.githubusercontent.com/6677629/129658746-654d908d-c6a8-4254-a9c6-33d75e436df6.gif)

#### Earth Engine Snippet

```js
var tile30m = ee.Image("projects/sat-io/open-datasets/agtile/AgTile-US");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/US-TILE-DRAINED-CROPLANDS

#### License

This work is licensed under the Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0). Users are free to use, copy, distribute, transmit, and adapt the work for commercial and non-commercial purposes, without restriction, as long as clear attribution of the source is provided.

Created by: Valayamkunnath, P., Barlage, M., Chen, F. et al.

Curated by: Samapriya Roy

Keywords: Agriculture,Tile Drainage,Subsurface,USA,CONUS,GIS,30 meter,data,gridded,raster

Last updated: 2021-08-16
