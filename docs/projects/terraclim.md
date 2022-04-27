# Terraclimate Individual years for +2C and +4C climate futures

TerraClimate layers commensurate with global mean temperatures +2C and +4C above preindustrial levels. These data are available for pseudo years 1985-2015. Future climate projections were developed for two different climate futures: (1) when global mean temperatures are 2C warmer than pre-industrial, and (2) when global mean temperatures are 4C above preindustrial. We use a pattern scaling approach that makes use of monthly projections from 23 CMIP5 global climate models as described in Qin et al., 2020 and provide projections for monthly climate by imposing projected changes in means and variance from the modes scalable to the change in global temperature. You can find [more information here](https://www.climatologylab.org/terraclimate.html)

This data is at two links

* [+2C data](http://thredds.northwestknowledge.net:8080/thredds/catalog/TERRACLIMATE_ALL/data_plus2C/catalog.html)
* [+4C data](http://thredds.northwestknowledge.net:8080/thredds/catalog/TERRACLIMATE_ALL/data_plus4C/catalog.html)

#### Citation

```
Abatzoglou, J.T., S.Z. Dobrowski, S.A. Parks, K.C. Hegewisch, 2018, Terraclimate, a high-resolution global dataset of monthly climate and climatic water
balance from 1958-2015, Scientific Data
```

#### Data preprocessing
An automated script was created to fetch all datasets, which contains 31 annual NetCDF files with 12 bands each representing a month for each variable. The netcdf files for each variable was converted into Geotifs with global bounds and with lzw compressions. The collections were made available for both 2C and 4C scenarios and scale and offset were added as metadata for each collection to allow for processing in the appropriate units as mentioned in the variable list below.

#### Variable lists

Terraclimate variables and units can be found in the table below. As noted from their webpage these datasets have associated scales and offset value which has to be used to generate a correct representation of the variable data in the intended units. As part of data processing, the variable scale and offset values were included as metadata for each variable which can then be applied in computations directly.

<center>

|variable                                              |units    |
|------------------------------------------------------|---------|
|aet (Actual Evapotranspiration, monthly total)        | mm      |
|def (Climate Water Deficit, monthly total)            | mm      |
|pet (Potential evapotranspiration, monthly total)     | mm      |
|ppt (Precipitation, monthly total)                    | mm      |
|q (Runoff, monthly total)                             | mm      |
|soil (Soil Moisture, total column - at end of month)  | mm      |
|srad (Downward surface shortwave radiation)           | W/m2    |
|swe (Snow water equivalent - at end of month)         | mm      |
|tmax (Max Temperature, average for month)             | C       |
|tmin (Min Temperature, average for month)             | C       |
|vap (Vapor pressure, average for month)               | kPa     |
|ws (Wind speed, average for month)                    | m/s     |
|vpd (Vapor Pressure Deficit, average for month)       | kpa     |
|PDSI (Palmer Drought Severity Index, at end of month) | unitless|
|PDSI (Palmer Drought Severity Index, at end of month) |unitless |

</center>

![terraclimate](https://user-images.githubusercontent.com/6677629/165516012-0a573b1e-3cee-44f5-a515-1a02da419c6b.gif)


#### Earth Engine Snippet

```js
var aet_2c = ee.ImageCollection("projects/sat-io/open-datasets/TERRACLIMATE/2C/aet");
var def_2c = ee.ImageCollection("projects/sat-io/open-datasets/TERRACLIMATE/2C/def");
var pet_2c = ee.ImageCollection("projects/sat-io/open-datasets/TERRACLIMATE/2C/pet");
var ppt_2c = ee.ImageCollection("projects/sat-io/open-datasets/TERRACLIMATE/2C/ppt");
var soil_2c = ee.ImageCollection("projects/sat-io/open-datasets/TERRACLIMATE/2C/soil");
var srad_2c = ee.ImageCollection("projects/sat-io/open-datasets/TERRACLIMATE/2C/srad");
var swe_2c = ee.ImageCollection("projects/sat-io/open-datasets/TERRACLIMATE/2C/swe");
var tmax_2c = ee.ImageCollection("projects/sat-io/open-datasets/TERRACLIMATE/2C/tmax");
var tmin_2c = ee.ImageCollection("projects/sat-io/open-datasets/TERRACLIMATE/2C/tmin");
var vap_2c = ee.ImageCollection("projects/sat-io/open-datasets/TERRACLIMATE/2C/vap");
var vpd_2c = ee.ImageCollection("projects/sat-io/open-datasets/TERRACLIMATE/2C/vpd");
var aet_4c = ee.ImageCollection("projects/sat-io/open-datasets/TERRACLIMATE/4C/aet");
var def_4c = ee.ImageCollection("projects/sat-io/open-datasets/TERRACLIMATE/4C/def");
var pet_4c = ee.ImageCollection("projects/sat-io/open-datasets/TERRACLIMATE/4C/pet");
var ppt_4c = ee.ImageCollection("projects/sat-io/open-datasets/TERRACLIMATE/4C/ppt");
var soil_4c = ee.ImageCollection("projects/sat-io/open-datasets/TERRACLIMATE/4C/soil");
var swe_4c = ee.ImageCollection("projects/sat-io/open-datasets/TERRACLIMATE/4C/swe");
var tmax_4c = ee.ImageCollection("projects/sat-io/open-datasets/TERRACLIMATE/4C/tmax");
var tmin_4c = ee.ImageCollection("projects/sat-io/open-datasets/TERRACLIMATE/4C/tmin");
var vpd_4c = ee.ImageCollection("projects/sat-io/open-datasets/TERRACLIMATE/4C/vpd");
```

Sample code: https://code.earthengine.google.com/a229056c55d1fa89dfd01acbea0f6515


#### License
This work is licensed under a public domain license.

Created by: Abatzoglou, J.T., S.Z. Dobrowski, S.A. Parks, K.C. Hegewisch

Preprocessed and Curated in GEE by : Samapriya Roy

Keywords: Climate futures, +2C, +4C, TerraClimate

Last updated: 2021-04-15

Last updated on GEE: 2022-04-27
