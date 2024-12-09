# Global NPP-VIIRS-like nighttime light (2000-2023)

The nighttime light (NTL) satellite data have been widely used to investigate the urbanization process. The Defense Meteorological Satellite Program Operational Linescan System (DMSP-OLS) stable nighttime light data and Suomi National Polar-orbiting Partnership Visible Infrared Imaging Radiometer Suite (NPP-VIIRS) nighttime light data are two widely used NTL datasets. However, the difference in their spatial resolutions and sensor design requires a cross-sensor calibration of these two datasets for analyzing a long-term urbanization process.

The extended data NPP-VIIRS-like NTL data (2000–2024) have an excellent spatial pattern and temporal consistency which are similar to the composited NPP-VIIRS NTL data. In addition, the resulting product could be easily updated and provide a useful proxy to monitor the dynamics of demographic and socioeconomic activities for a longer time period compared to existing products.

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.


#### Citation

```
Chen, Z., Yu, B., Yang, C., Zhou, Y., Yao, S., Qian, X., Wang, C., Wu, B., and Wu, J.: An extended time series (2000–2018) of global NPP-VIIRS-like nighttime
light data from a cross-sensor calibration, Earth Syst. Sci. Data, 13, 889–906, https://doi.org/10.5194/essd-13-889-2021, 2021.
```

![ntl_viirs](https://user-images.githubusercontent.com/6677629/185727107-e76dcc00-4194-4f30-92f3-9aa851f671ae.gif)

#### Earth Engine Snippet

```js
var viirs_ntl = ee.ImageCollection("projects/sat-io/open-datasets/npp-viirs-ntl");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/GLOBAL-NPP-VIIRS-LIKE-NTL

#### License

These datasets are made available under the CC0 1.0 Universal (CC0 1.0) Public Domain Dedication. You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission. See Other Information below.

Created by: Chen, Zuoqi et al

Curated in GEE by : Samapriya Roy

keywords: Nighttime light, VIIRS, NTL, NPP-VIIRS

#### Changelog
* Year 2023 was added to the collection.

Last updated on GEE: 2024-12-08
