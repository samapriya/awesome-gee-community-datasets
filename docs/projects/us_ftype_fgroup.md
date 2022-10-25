# US National Forest Type and Groups

## Forest Type
This dataset portrays 141 forest types across CONUS and Alaska. These data were derived from MODIS composite images from the 2002 and 2003 growing seasons in combination with nearly 100 other geospatial data layers, including elevation, slope, aspect, and ecoregions. The dataset was developed as a collaborative effort between the USFS Forest Inventory and Analysis and Forest Health Monitoring programs and the USFS Geospatial Technology and Applications Center. The purpose of this dataset is to portray broad distribution patterns of forest cover in the United States and provide input to national scale modeling projects.

## Forest Groups
This dataset portrays 28 forest type groups across the contiguous United States. These data were derived from MODIS composite images from the 2002 and 2003 growing seasons in combination with nearly 100 other geospatial data layers, including elevation, slope, aspect, ecoregions, and PRISM climate data. The dataset was developed as a collaborative effort between the USFS Forest Inventory and Analysis and Forest Health Monitoring programs and the USFS Geospatial Technology and Applications Center. Forest Type Groups are aggregations of forest types (Eyre 1980) into logical ecological groupings. There are 28 national forest type groups. Class accuracy was assessed using a randomly selected independent hold out of 6552 plots. Overall CONUS-wide accuracy for the forest type groups was 65%.

You can get detailed [sample forest group metadata here](https://data.fs.usda.gov/geodata/rastergateway/forest_type/conus_forest_type_group_metadata.php)


![forest_group_type](https://user-images.githubusercontent.com/6677629/197849054-51b4a41a-97c3-483a-8da8-929c0a2c7885.gif)


#### Earth Engine snippet: Forest Type

```js
var forest_type = ee.ImageCollection("projects/sat-io/open-datasets/USFS/national-forest-type");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/US-NATIONAL-FOREST-TYPE


#### Earth Engine snippet: Forest Group

```js
var forest_group = ee.ImageCollection("projects/sat-io/open-datasets/USFS/national-forest-group");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/US-NATIONAL-FOREST-GROUP

#### License

Although these data have been used by the USDA Forest Service, the USDA Forest Service shall not be held liable for improper or incorrect use of the data described and/or contained herein. These data are not legal documents and are not intended to be used as such.

Created by: USDA Forest Service-Forest Inventory and Analysis (FIA) Program & Geospatial Technology and Applications Center (GTAC)

Curated in GEE by : Samapriya Roy

Keywords: forest type, forest group, forest, remote sensing

Last updated on GEE: 2022-10-25
