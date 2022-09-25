# Reference ET gridded database based on FAO Penman-Monteith for Peru (PISCOeo_pm)

PISCOeo_pm has been developed for the 1981–2016 period at ~1 km (0.01°) spatial resolution for the entire continental Peruvian territory. The framework for the development of PISCOeo_pm is based on previously generated gridded data of meteorological subvariables such as air temperature (maximum and minimum), sunshine duration, dew point temperature, and wind speed.

Different steps, i.e., (i) quality control, (ii) gap-filling, (iii) homogenization, and (iv) spatial interpolation, were applied to the subvariables. PISCOeo_pm is useful for better understanding the terrestrial water and energy balances in Peru as well as for its application in fields such as climatology, hydrology, and agronomy, among others. Read [the full paper here](https://www.nature.com/articles/s41597-022-01373-8)

#### Citation

```
Huerta, A., Bonnesoeur, V., Cuadros-Adriazola, J., Gutierrez, L. F., Ochoa-Tocachi, B. F., Román-Dañobeytia, F., & Lavado-Casimiro, W.. (2022). PISCOeo_pm, a
reference evapotranspiration gridded database based on FAO Penman-Monteith in Peru. Nature Scientific Data. https://doi.org/10.1038/s41597-022-01373-8
```

#### Data Citation

```
Huerta, A., Bonnesoeur, V., Cuadros-Adriazola, J., Gutierrez, L. F., Ochoa-Tocachi, B. F., Román-Dañobeytia, F., & Lavado-Casimiro, W.. (2022). Reference
evapotranspiration gridded database based on FAO Penman-Monteith for Peru (PISCOeo_pm) V.1.0. SENAMHI-Perú. https://doi.org/10.6084/m9.figshare.c.5633182.v3
```

<center>
<img src="https://github.com/lgutierrezl/PISCOeo_pm_graphics/raw/main/eo_clim.gif" width=50%>
</center>

Currently included layers are:

#### Earth Engine Snippet: Yearly mean data

```js
var PISCOeo_pm_yearly = ee.ImageCollection('users/lgutierrezlf/PISCOeo_pm/yearly')
```

#### Earth Engine Snippet: Monthly climatology data

```js
var PISCOeo_pm_climatology = ee.ImageCollection('users/lgutierrezlf/PISCOeo_pm/climatology')
```

#### Earth Engine Snippet: Monthly data

```js
var PISCOeo_pm_monthly = ee.ImageCollection('users/lgutierrezlf/PISCOeo_pm/monthly')
```

#### Earth Engine Snippet: Daily data

```js
var PISCOeo_pm_daily = ee.ImageCollection('users/lgutierrezlf/PISCOeo_pm/daily')
```

#### Web Application PISCOeo_pm in GEE

https://lgutierrezlf.users.earthengine.app/view/piscoeopmts

**Resolution: 0.01° (or roughly 1km x 1km)**

app code : https://code.earthehttps://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/REFERENCE-ET-GRIDDED-PERU

#### License:
This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Curated by: Gutierrez Leonardo & Samapriya Roy

Keywords: reference evapotranspiration, FAO Penman Monteith, Peru, hydrology, satellite data, Earth observation, GIS.

Last updated: 27/06/2022
