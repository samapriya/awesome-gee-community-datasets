# Global River Width from Landsat (GRWL)

The Global River Width from Landsat (GRWL) layers are the major output from the GRWL paper and is extremely large with over 64 million features after joining all the subparts and this is a combination from the subpart files provided by the author. You can read the [paper here](https://science.sciencemag.org/content/361/6402/585)

The repository consists of 5 total files with each files having subparts

1) Simplified GRWL Vector Product: grwl_SummaryStats_v01_01

The shapefile contains the following attributes:

|Index|Attribute |Description |
|-----|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
|1 |    width_min | the minimum of river width measurements along the segment at mean discharge (meters) |
|2 |    width_med | the median of river width measurements along the segment at mean discharge (meters) |
|3 |    width_mean| the mean of river width measurements along the segment at mean discharge (meters) |
|4 |    width_max | the maximum of river width measurements along the segment at mean discharge (meters) |
|5 |    width_sd | the standard deviation of river width measurements along the segment at mean discharge (meters) |
|6 |    lakeflag | integer specifying if segment is located on a river (lakeflag=0), lake/reservoir (lakeflag=1), tidal river (lakeflag=2), or canal (lakeflag=3)|
|8 |    nSegPx | number of pixels within the segment (N pixels) |
|9 |    Shape_Leng| length of the segment (kilometers) |


2) GRWL Mask (raster): water_mask_v01_01

The file contains the following values:

|DN Value |Classification |
|---------|-------------------|
|DN = 256 | No Data |
|DN = 255 | River |
|DN = 180 | Lake/reservoir |
|DN = 126 | Tidal rivers/delta|
|DN = 86 | Canal |

3) GRWL Vector Product: water_vector_v01_01

The shapefile contains the following attributes:

|Index|Attribute |Description |
|-----|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
|1 |    utm_east | UTM Easting (UTM Zone is given in tile file name; meters) |
|2 |    utm_north | UTM Northing (UTM Zone is given in tile file name; meters) |
|3 |    width_m | wetted width of river (meters) [note: width_m == 1 indicates NA (no width data along the centerline) ] |
|4 |    nchannels | braiding index (-) |
|5 |    segmentID | unique ID of river segment in each tile |
|6 |    segmentInd| Index of each observation in each segment. Not sorted by upstream or downstream |
|7 |    lakeflag | integer specifying if observation is located on a river (lakeflag=0), lake/reservoir (lakeflag=1), tidal river (lakeflag=2), or canal (lakeflag=3). |
|8 |    lon | Longitude (decimal degrees) |
|9 |    lat | Latitude (decimal degrees) |
|10 |    elev | Elevation (meters) – sampled from the Hydro1k DEM |

and

4) Location map of the individual GRWL tiles: grwl_tiles

5) River and stream surface area totals by drainage basin (Fig. 4 in Allen & Pavelsky, 2018): rssa_basins

GRWL vector product has a feature Count: 64,572,998 features.

![grwl_layers](https://user-images.githubusercontent.com/6677629/115134104-06724500-9fd3-11eb-8ae2-2822d6f6705e.gif)

Currently included layers are

#### Earth Engine Snippet:

```js
var grwl_summary = ee.FeatureCollection("projects/sat-io/open-datasets/GRWL/grwl_SummaryStats_v01_01");
var water_mask = ee.ImageCollection("projects/sat-io/open-datasets/GRWL/water_mask_v01_01");
var grwl_water_vector = ee.FeatureCollection("projects/sat-io/open-datasets/GRWL/water_vector_v01_01");
var grwl_tiles = ee.FeatureCollection("projects/sat-io/open-datasets/GRWL/grwl_tiles");
var grwl_rssa_basins = ee.FeatureCollection("projects/sat-io/open-datasets/GRWL/rssa_basins");
```

Sample Code: https://code.earthengine.google.com/66543f94dcb97a8d27de1d6e128fe064

Resolution:
approx 30m

#### Cite the dataset using

```
Allen, George H., & Pavelsky, Tamlin M. (2018). Global River Widths from Landsat (GRWL) Database (Version V01.01) [Data set]. Zenodo. http://doi.org/10.5281/zenodo.1297434
```


#### Cite the paper using

```
Allen, George H., and Tamlin M. Pavelsky. "Global extent of rivers and streams."
Science 361, no. 6402 (2018): 585-588.
```

#### License
Shared License: This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.


Curated by: Samapriya Roy

Keywords: :"GRWL, Fluvial Geomorphology, Hydrology, Rivers, River Width, Landsat, MNDWI"

Last updated: 2021-04-17
