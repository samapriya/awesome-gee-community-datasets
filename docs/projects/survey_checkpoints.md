# USGS Consolidated Survey-Grade Checkpoints 3DEP 2010 to 2017

The **USGS Consolidated Standardized Survey-Grade Checkpoints 3DEP** dataset contains 41,958 survey-grade checkpoints collected between 2010 and 2017, covering 205 lidar and Interferometric Synthetic Aperture Radar (ifSAR) projects. These checkpoints were collected in the United States as part of the 3D Elevation Program (3DEP). The geospatial data is available in both Esri File-Geodatabase (GDB) and Open Geospatial Consortium’s (OGC) GeoPackage (GPKG) formats. The dataset includes horizontal and vertical coordinates based on the North American Datum of 1983 (2011) in decimal degrees (EPSG:6318) and North American Vertical Datum of 1988 (2011) in meters (EPSG:5703). Updates to vertical datums for the contiguous United States (CONUS) used GEOID18, while updates for Hawaii and Alaska used GEOID12B via NOAA’s VDatum tool.

This dataset is a valuable resource for validating and assessing the accuracy of lidar data collected for the 3DEP program and can be used in geospatial applications that require high-accuracy elevation data. Each checkpoint is characterized by attributes such as its unique identifier, survey type (NVA, VVA, or Unknown), geoid used, collection date, and more.

#### Citation

```
Miller, B.Y., and Cannici, C., 2024, Consolidated Standardized Survey-Grade Checkpoints 3DEP 2010 to 2017: U.S. Geological Survey data release,
https://doi.org/10.5066/P13NOW9E.
```

![survey_checkpoints](https://github.com/user-attachments/assets/5ab8e528-7143-4196-ac48-a88fd25ad316)

#### Earth Engine Snippet

```js
var survey_checkpoints = ee.FeatureCollection("projects/sat-io/open-datasets/USGS/SURVEY_CHECKPOINTS_3DEP_2010_2017");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:analysis-ready-data/USGS-3DEP-CONSOLIDATED-SURVEY-CHECKPOINTS

#### License
This dataset is provided under the Creative Commons Zero v1.0 Universal license (CC0 1.0).

Provided by: U.S. Geological Survey (USGS)

Curated in GEE by: Samapriya Roy

Keywords: 3DEP, Lidar, Survey-Grade Checkpoints, GEOID18, GEOID12B, Elevation, Accuracy, Survey Data, USGS, Vertical Datum, Horizontal Datum

Last updated in GEE: 2024-10-24

