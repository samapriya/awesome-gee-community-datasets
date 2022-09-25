# High-resolution gridded precipitation dataset for Peruvian and Ecuadorian watersheds (1981-2015)

RAIN4PE is a novel daily gridded precipitation dataset obtained by merging multi-source precipitation data (satellite-based Climate Hazards Group InfraRed Precipitation, CHIRP (Funk et al. 2015), reanalysis ERA5 (Hersbach et al. 2020), and ground-based precipitation) with terrain elevation using the random forest regression method. Furthermore, RAIN4PE is hydrologically corrected using streamflow data in catchments with precipitation underestimation through reverse hydrology. Hence, RAIN4PE is the only gridded precipitation product for Peru and Ecuador, which benefits from maximum available in-situ observations, multiple precipitation sources, elevation data, and is supplemented by streamflow data to correct the precipitation underestimation over páramos and montane catchments.

<center>
<img src="https://user-images.githubusercontent.com/16768318/147897036-960ea777-6bac-436c-9c2f-dbcc773b143e.gif" width=50%>
</center>


Currently included layers are:


#### Earth Engine Snippet: Annual mean

```js
var rain4pe_clim = ee.ImageCollection('users/csaybar/rainpe/annual_mean')
```
Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/RAIN4PE-GRIDDED-PRECIP-YEARLY

#### Earth Engine Snippet: Monthly climatology

```js
var rain4pe_clim = ee.ImageCollection('users/csaybar/rainpe/monthly_clim')
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/RAIN4PE-GRIDDED-PRECIP-MONTHLY-CLIM

#### Earth Engine Snippet: Monthly data

```js
var rain4pe_clim = ee.ImageCollection('users/csaybar/rainpe/monthly')
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/RAIN4PE-GRIDDED-PRECIP-MONTHLY

#### Earth Engine Snippet: Daily data

```js
var rain4pe_daily = ee.ImageCollection('projects/sat-io/open-datasets/rainpe/daily')
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/RAIN4PE-GRIDDED-PRECIP-DAILY


#### Resolution: 0.1° (or roughly 10km x 10km)

#### citation

**When using the data please cite:**

```
Fernandez-Palomino, C. A.; Hattermann, F. F.; Krysanova, V.; Lobanova, A.; Vega-Jácome, F.; Lavado, W.;
Santini, W.; Aybar, C.; Bronstert, A. (2021). Rain for Peru and Ecuador (RAIN4PE). V. 1.0. GFZ Data
Services. https://doi.org/10.5880/pik.2020.010
```

**The data are supplementary material to:**

```
Fernandez-Palomino, C. A.; Hattermann, F. F.; Krysanova, V.; Lobanova, A.; Vega-Jácome, F.; Lavado, W.;
Santini, W.; Aybar, C.; Bronstert, A. (2021). A novel high-resolution gridded precipitation dataset for
Peruvian and Ecuadorian watersheds – development and hydrological evaluation. Journal of
Hydrometeorology. https://doi.org/10.1175/jhm-d-20-0285.1
```

#### License

This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Curated by: Cesar Aybar & Samapriya Roy

Keywords: precipitation, streamflow, Peru, Ecuador, random forest, SWAT, reverse hydrology, satellite data, Earth observation, GIS.
