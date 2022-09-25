# C-CAP Wetland Potential 30m
The probability rating which covers landcover mapping provides a continuum of wetness from dry to water. The layer is not a wetland classification but provides the wetland likelihood at a specific location. The rating was developed through a modelling process combining multiple GIS and remote sensing data sets including soil characteristics, elevation, existing wetland inventories, hydrographical extents and satellite imagery . Data can be [downloaded here](https://coast.noaa.gov/htdata/raster1/landcover/bulkdownload/wetlandpotential/). This classification is based on GIS and remote sensing data sets with variable ranges from the 1977 to 2010.

This dataset was created by NOAA's Ocean Service, Office for Coastal Management Initial Classification: 1m spatial resolution land cover data developed by the Chesapeake Bay Conservancy, University of Vermont Spatial Analysis Laboratory, and The Virginia Geographic Information Network (VGIN) was the starting point for this dataset. This product was developed using a Geographic Object-Based Image Analysis (GEOBIA) processing framework applied to NAIP imagery and Lidar data. This involves taking each image to be classified and grouping the pixels based on spectral and spatial properties into regions of homogeneity called objects. The resulting objects are the primary units for analysis. The original dataset can be downloaded here:https://chesapeakeconservancy.org/conservation-innovation-center/high-resolution-data/land-cover-data-project/.

The resulting 1-meter land cover was then resampled to a 10-meter raster. This was done using a 10x10 focal pixel window to compute the percent value associated with either the impervious or tree classes, for each land cover type in the 100 pixel neighborhood around each target pixel, and subsequently performing a nearest neighbor resampling of the resulting values. The output values were then coded to the appropriate percentage (between 0 and 100). This 10-meter raster was resampled a second time, using the average of values within a 3x3 focal pixel window in order to obtain the appropriate values over each 30-meter pixel area. Output values between 0 and 100 represent the appropriate percentage mapped within each pixel. Class 127 identifies areas not included in this mapping, or no data areas.

#### Class values

0: This is the value for nodata.
1: The value indicates there is an extremely low likelihood of wetness.
2-9: The value indicates a likelihood of wetness, where 1 is very unlikely and 9 is highly likely.
10: The value indicates open water.

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.


#### Citation

```
National Oceanic and Atmospheric Administration, Office for Coastal Management. “Name of Data Set.” Coastal Change Analysis Program (C-
CAP) Wetland Potential Layer: NOAA Office for Coastal Management. Accessed [Month Year] at https://coast.noaa.gov/htdata/raster1/landcover/bulkdownload/wetlandpotential/.
```

![CCAP-WETLAND-POTENTIAL](https://user-images.githubusercontent.com/6677629/177845289-596fa19e-d5eb-4ab2-b876-dbaf857d57f7.gif)

#### Earth Engine Snippet

```js
var ccap_wetland_potential = ee.Image("projects/sat-io/open-datasets/NOAA/conus_ccap_wetland_potential");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:regional-landuse-landcover/CCAP-WETLAND-POTENTIAL


#### License

The dataset is released under an assumed CC0 1.0 Universal (CC0 1.0) Public Domain Dedication.

Produced by: NOAA's Ocean Service, Office for Coastal Management (OCM)

Curated in GEE by: Samapriya Roy

Keywords: Wetland, Coastal data, NOAA, Remote Sensing

Last updated on GEE: 2022-05-17
