# Coastal National Elevation Database (CoNED) Project -Topobathymetric digital elevation models (TBDEMs)

The Coastal National Elevation Database (CoNED) Project - topobathymetric digital elevation models (TBDEMs) are merged renderings of both topography (land elevation) and bathymetry (water depth) to provide seamless elevation products for select coastal regions in the United States (2011-present). This coastal elevation database integrates disparate light detection and ranging (lidar) and bathymetric data sources (such as sonar) into common databases aligned both vertically and horizontally to common reference systems.

This coastal elevation database integrates disparate light detection and ranging (lidar) and bathymetric data sources into common databases aligned both vertically and horizontally to common reference systems. CoNED Project - topobathymetric digital elevation models (TBDEMs) provide a required seamless elevation product for science application studies such as shoreline delineation, coastal inundation mapping, sediment-transport, sea-level rise, storm surge models, tsunami impact assessment, and analysis of the impact of various climate change scenarios on coastal regions.

Dataset description [can be found here](https://lta.cr.usgs.gov/coned_tbdem) and the [full datasets were downloaded from](https://topotools.cr.usgs.gov/topobathy_viewer/dwndata.htm)

Disclaimer: Whole or parts of the dataset description was provided by the author(s) or their works.

#### Citation

```
Coastal National Elevation Database (CoNED) Project - Topobathymetric Digital Elevation Model (TBDEM)
Digital Object Identifier (DOI) number: /10.5066/F7Z60MHJ
```

#### Dataset setup and preprocessing
The datasets were collected and made available with 3 meter, 2 meter, or 1 meter and different no data values. While GEE collections will allow for variable values for all of those, the nominal resolution and native CRS was left intact was no data value was reprocessed to -9999 by simply using gdalwarp. Some of the datasets were single mosaics with filesizes upward of 4GB to 200+GB, for efficiency and better handling of these gdal_retile tool was used to retile these into subparts while maintaining the file name for data tracing. I have added a function onto the example script which allows you to add the nominal scale as a property to the collection in case the user would like to split and apply different methods on top.


![tbdem](https://user-images.githubusercontent.com/6677629/155889584-6e32112b-faf5-493c-aee5-a69e5d14f99d.gif)

#### Earth Engine Snippet

```js
var tb_dem = ee.ImageCollection("projects/sat-io/open-datasets/NOAA/CoNED_TBDEM");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:elevation-bathymetry/NOAA-CoNED-TBDEM

#### License
The dataset is released under an assumed CC0 1.0 Universal (CC0 1.0) Public Domain Dedication. There are no restrictions on the use of data received from the U.S. Geological Survey's Earth Resources Observation and Science (EROS) Center or NASA's Land Processes Distributed Active Archive Center (LP DAAC), unless expressly identified prior to or at the time of receipt. Depending on the product source, we request that the following statements be used when citing, copying, or reprinting data: Data available from the U.S. Geological Survey.

Intended use:
Development, calibration and validation of coastal open-access EO-derived elevation/topography, vegetation and water quality products.

Provider:  USGS, CMGP, NGP, NOAA and NGDC

Curated by: Samapriya Roy

Keywords: Elevation, topography, topobathymetric, bathymetry

Last updated on GEE: 2022-02-27
