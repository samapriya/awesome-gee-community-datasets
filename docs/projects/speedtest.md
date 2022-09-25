# Global fixed broadband and mobile (cellular) network performance

Global fixed broadband and mobile (cellular) network performance, allocated to zoom level 16 web mercator tiles (approximately 610.8 meters by 610.8 meters at the equator). Data is provided in both Shapefile format as well as Apache Parquet with geometries represented in Well Known Text (WKT) projected in EPSG:4326. Download speed, upload speed, and latency are collected via the Speedtest by Ookla applications for Android and iOS and averaged for each tile. Measurements are filtered to results containing GPS-quality location accuracy.

Available years of datasets: 2019,2020,2021 and 2022

#### Citation

```
Speedtest® by Ookla® Global Fixed and Mobile Network Performance Maps.
Based on analysis by Ookla of Speedtest Intelligence® data for [DATA TIME PERIOD].
Provided by Ookla and accessed [DAY MONTH YEAR]. Ookla trademarks used under license
and reprinted with permission.
```

Find the GitHub project and datasets here: https://github.com/teamookla/ookla-open-data
You can also download the datasets from AWS Open data registry: https://registry.opendata.aws/speedtest-global-performance/

#### Tiles
Hundreds of millions of [Speedtests](https://www.speedtest.net/) are taken on the [Ookla](https://www.ookla.com/) platform each month. In order to create a manageable dataset, we aggregate raw data into tiles. The size of a data tile is defined as a function of "zoom level" (or "z"). At z=0, the size of a tile is the size of the whole world. At z=1, the tile is split in half vertically and horizontally, creating 4 tiles that cover the globe. This tile-splitting continues as zoom level increases, causing tiles to become exponentially smaller as we zoom into a given region. By this definition, tile sizes are actually some fraction of the width/height of Earth according to [Web Mercator projection](https://en.wikipedia.org/wiki/Web_Mercator_projection) (EPSG:3857). As such, tile size varies slightly depending on latitude, but tile sizes can be estimated in meters.

For the purposes of these layers, a zoom level of 16 (z=16) is used for the tiling. This equates to a tile that is approximately 610.8 meters by 610.8 meters at the equator (18 arcsecond blocks). The geometry of each tile is represented in [WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System) (EPSG:4326) in the `tile` field.


#### Tile Attributes
Each tile contains the following adjoining attributes:

| Field Name   | Type        | Description                                                                                        |
|--------------|-------------|----------------------------------------------------------------------------------------------------|
| avg_d_kbps | Integer     | The average download speed of all tests performed in the tile, represented in kilobits per second. |
| avg_u_kbps | Integer     | The average upload speed of all tests performed in the tile, represented in kilobits per second.   |
| avg_lat_ms | Integer     | The average latency of all tests performed in the tile, represented in milliseconds                |
| tests      | Integer     | The number of tests taken in the tile.                                                             |
| devices    | Integer     | The number of unique devices contributing tests in the tile.                                       |
| quadkey    | Text        | The quadkey representing the tile.                                                                 |


#### Quadkeys

[Quadkeys](https://docs.microsoft.com/en-us/bingmaps/articles/bing-maps-tile-system) can act as a unique identifier for the tile. This can be useful for joining data spatially from multiple periods (quarters), creating coarser spatial aggregations without using geospatial functions, spatial indexing, partitioning, and an alternative for storing and deriving the tile geometry.

#### Layers
Two layers are distributed as separate sets of files:

* `performance_mobile_tiles` - Tiles containing tests taken from mobile devices with GPS-quality location and a cellular connection type (e.g. 4G LTE, 5G NR).
* `performance_fixed_tiles` - Tiles containing tests taken from mobile devices with GPS-quality location and a non-cellular connection type (e.g. WiFi, ethernet).

#### Time Period and Update Frequency

Layers are generated based on a quarter year of data (three months) and files will be updated and added on a quarterly basis. A `/year=2020/quarter=1/` period, the first quarter of the year 2020, would include all data generated on or after `2020-01-01` and before `2020-04-01`.

Data is subject to be reaggregated regularly in order to honor Data Subject Access Requests (DSAR) as is applicable in certain jurisdictions under laws including but not limited to General Data Protection Regulation (GDPR), California Consumer Privacy Act (CCPA), and Lei Geral de Proteção de Dados (LGPD). Therefore, data accessed at different times may result in variation in the total number of tests, tiles, and resulting performance metrics.

![network_tiles](https://user-images.githubusercontent.com/6677629/126053848-fca2bde6-d922-47e3-a429-293b1a3e1890.gif)

#### Earth Engine Snippet

```js
var mobile_20210101 = ee.FeatureCollection("projects/sat-io/open-datasets/network/mobile_tiles/2022-01-01_performance_mobile_tiles");
var fixed_20210101 = ee.FeatureCollection("projects/sat-io/open-datasets/network/fixed_tiles/2022-01-01_performance_fixed_tiles");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/GLOBAL-FIXED-MOBILE-NETWORK-PERFORMANCE

Earth Engine files for mobile and fixed tiles across different quarters are arranged in the format, since quarters are 3 month intervals replace month variable by 01,04,07,10 which represents 3 month intervals

```js
* ee.FeatureCollection("projects/sat-io/open-datasets/network/mobile_tiles/Year-month-01_performance_mobile_tiles")
* ee.FeatureCollection("projects/sat-io/open-datasets/network/fixed_tiles/Year-month-01_performance_mobile_tiles")
```

#### Raster Datasets
As part of processing this datasets I further converted these datasets into 32 bit float rasters , these are produced at 610m resolution and feature property such as avg_d_kbps,avg_u_kbps,avg_lat_ms,devices,tests are converted in Bands for these images. The start and end date for each quarter are further added to the images however the quad information is not retained from vector to raster conversion. The result are two image collections for fixed and mobile datasets.

![network_rasters](https://user-images.githubusercontent.com/6677629/126076187-cdab105f-2ebc-4639-91ba-b0ffa6d6b76c.gif)

#### Earth Engine Snippet

```js
var fixed = ee.ImageCollection("projects/sat-io/open-datasets/network/raster_tiles/performance_fixed_tiles");
var mobile = ee.ImageCollection("projects/sat-io/open-datasets/network/raster_tiles/performance_mobile_tiles");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/GLOBAL-FIXED-MOBILE-NETWORK-PERF-RASTER

#### License
These datasets are made available under a Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)

Provided by: Ookla

Curated in GEE by: Samapriya Roy

Keywords: : analytics,broadband,cities,civic,infrastructure,internet,network traffic, telecommunications,tiles

Last updated: 2022-06-11
