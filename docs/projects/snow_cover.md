# Global MODIS-based snow cover monthly values (2000-2020)

The Global monthly snow cover repository contains multiple products (based on the MODIS/Terra MOD10A2), the description along with the [datasets can be found here](https://zenodo.org/record/5774954)

* Global snow cover monthly long-term (2000–2012) P90 and standard deviation derived from the ESA CCI snow cover weekly product;
* Global snow cover monthly values P05, P50 and P95 for the period 2000–2020 derived using ESA snow cover fraction daily 1-km values;
* Min and max geometric temperatures for the mid-month;

Quantiles (probability either 0.05, 0.5, 0.9 and/or 0.95) have been derived by matching dates in the filenames (daily or weekly values). After deriving quantiles, gaps were filled using temporal neighbors (e.g. missing values for year 2002 were filled using average of values between year 2001 and 2003). The gaps were especially large for months of November, December, January and February, northern Hemisphere. Important note: maps still contain some artifacts due to high reflections of white-sands e.g. Salar de Uyuni desert in Bolivia and similar. Processing steps are available here. Antarctica is not included.

To access and visualize global datasets use: https://openlandmap.org

If you discover a bug, artifact or inconsistency in the maps, or if you have a question please use some of the following channels:

Technical issues and questions about the code: https://gitlab.com/openlandmap/global-layers/issues
All files provided as Cloud-Optimized GeoTIFFs / internally compressed using "COMPRESS=DEFLATE" creation option in GDAL. File naming convention:

* clm = theme: climate,
* snow.cover = variable: snow cover fractions,
* esa.modis = data source ESA snow product,
* p.90 = upper 90% quantile,
* 1km = spatial resolution / block support: 1 km,
* s0..0cm = vertical reference: land surface,
* 2000_2012 = time reference aggregated: from 2000 to 2012

#### Data citation

```
Hengl, T. (2021). Global MODIS-based snow cover monthly long-term (2000-2012) at 500 m, and aggregated monthly values (2000-2020)
at 1 km (v1.0) [Data set].
Zenodo. https://doi.org/10.5281/zenodo.5774954
```

![modis_lt_snow](https://user-images.githubusercontent.com/6677629/146651916-0fb69540-63c9-436c-8fa2-5aa365114fe9.gif)


#### Earth Engine Snippet

```js
var lt_p90 = ee.ImageCollection("projects/sat-io/open-datasets/MODIS_LT_SNOW/monthly_lt_p90");
var lt_sd = ee.ImageCollection("projects/sat-io/open-datasets/MODIS_LT_SNOW/monthly_lt_sd");
var lt_snow_quantile = ee.ImageCollection("projects/sat-io/open-datasets/MODIS_LT_SNOW/monthly_snow_quantile");
var tmax_geom = ee.ImageCollection("projects/sat-io/open-datasets/MODIS_LT_SNOW/midmonth_geom_tmax");
var tmin_geom = ee.ImageCollection("projects/sat-io/open-datasets/MODIS_LT_SNOW/midmonth_geom_tmin");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:geophysical-biological-biogeochemical/GLOBAL-MODIS-SNOWCOVER

#### License

This work is licensed under the Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0). Users are free to use, copy, distribute, transmit, and adapt the work for commercial and non-commercial purposes, without restriction, as long as clear attribution of the source is provided.

Created by: Hengl 2021

Curated by: Samapriya Roy

Keywords: : snow cover, global, openlandmap

Last updated: 2021-12-18
