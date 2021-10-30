# Global Solar Atlas Datasets

The current version of Global Solar Atlas is v 2.6 released in July 2021. The Global Solar Atlas version 2.0 is an enhancement of the online platform, originally published in 2016 in version 1.0, that offers access to data needed for preliminary assessment of solar energy projects and sites through use of GIS data layers and maps in Download section. This Technical report summarizes delivery of the GSA 2.0 version and compares version 2.0 with previous version 1.0 in terms of enhancement in methodology, data layers and Solargis approach to PV electricity simulation. GSA 2.0 provides an access to long-term averaged yearly (for selected parameters monthly) solar, air temperature, PV power potential data and map products for almost any site on Earth.

The atlas provides an access to long-term averaged yearly (for selected parameters monthly) solar, air temperature,
PV power potential data and map products for almost any site on Earth.

#### Attribution and License
If you get the data or use the dataset within the GSA app attribution below, the Works (datasets) themselves are under are licensed under the Creative Commons Attribution 4.0 International license, CC BY 4.0, except where expressly stated that another license applies.

```
[Data/information/map] obtained from the “Global Solar Atlas 2.0, a free, web-based application is developed and
operated by the company Solargis s.r.o. on behalf of the World Bank Group, utilizing Solargis data, with funding
provided by the Energy Sector Management Assistance Program (ESMAP).
For additional information: https://globalsolaratlas.info
```

You can find the Global Solar Atlas [here](https://globalsolaratlas.info/) and you can interact and download the datasets [here](https://globalsolaratlas.info/download)


#### Data Structure

Delivered GIS data include eight parameters in the form of a raster data layers, providing the information on solar
resource, photovoltaic power potential, air temperature and terrain elevation on global scale

Data layers are provided in Geographical coordinate system (EPSG:4326) and calculated in 30 arc-sec (nominally 1
km) resolution. On top of this, for more detailed analysis solar resource data (GHI, DIF, GTI and DNI) is also provided
in 9 arc-sec (nominally 250 m) resolution. Finally, auxiliary data layer of Optimum angle features with 2 arcmin
(nominally 4 km)resolution.

|Atlas Variable|Atlas GEE Variable       |Short Name                                     |Description                                                                              |
|--------------|-------------------------|-----------------------------------------------|-----------------------------------------------------------------------------------------|
|DIF           |dif_LTAy_AvgDailyTotals  |Diffuse horizontal irradiation                 |Longterm average of diffuse horizontal irradiation                                       |
|DNI           |dni_LTAy_AvgDailyTotals  |Direct normal irradiation                      |Longterm average of direct normal irradiation                                            |
|ELE           |ele_asl                  |Terrain elevation above sea level              |Terrain elevation                                                                        |
|GHI           |ghi_LTAy_AvgDailyTotals  |Global horizontal irradiation                  |Longterm average of global horizontal irradiation                                        |
|GTI           |gti_LTAy_AvgDailyTotals  |Global irradiation for optimally tilted surface|Longterm average of global irradiation at optimum tilt                                   |
|OPTA          |opta_LTAy_AvgDailyTotals |Optimum tilt to maximize yearly yield          |Optimum tilt of photovoltaic modules                                                     |
|PVOUT_LTAm    |pvout_LTAm_AvgDailyTotals|Photovoltaic power potential Average Monthly   |Longterm monthly average of daily totals of potential photovoltaic electricity production|
|PVOUT_LTAy    |pvout_LTAy_AvgDailyTotals|Photovoltaic power potential Average daily     |Longterm yearly average of daily totals of potential photovoltaic electricity production |
|TEMP          |temp_2m_agl              |Temperature at 2m above ground                 |Longterm yearly average of air temperature (1994-2018)                                   |


![gsa](https://user-images.githubusercontent.com/6677629/139536012-3a177130-3051-4113-b0fe-08f51240a280.gif)


#### Earth Engine Datasets

```js
var dif = ee.Image('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/global_solar_atlas/dif_LTAy_AvgDailyTotals');
var dni = ee.Image('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/global_solar_atlas/dni_LTAy_AvgDailyTotals');
var elevation_asl = ee.Image('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/global_solar_atlas/ele_asl');
var ghi = ee.Image('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/global_solar_atlas/ghi_LTAy_AvgDailyTotals');
var gti = ee.Image('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/global_solar_atlas/gti_LTAy_AvgDailyTotals');
var opta = ee.Image('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/global_solar_atlas/opta_LTAy_AvgDailyTotals');
var pvout_ltam = ee.ImageCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/global_solar_atlas/pvout_LTAm_AvgDailyTotals');
var pvout_ltay = ee.Image('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/global_solar_atlas/pvout_LTAy_AvgDailyTotals');
var temp_agl = ee.Image('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/global_solar_atlas/temp_2m_agl');
```

Sample Code: https://code.earthengine.google.com/d8964dead482e8dbbe5d9c97b41d68e3

Produced and maintained by the [Global Solar Atlas](https://globalsolaratlas.info), ESMAP, Solargis and the World Bank Group (consisting of The World Bank and the International Finance Corporation, or IFC)

Processed secondary/formatted & Curated by: Samapriya Roy

Keywords: : Solar, energy, photovoltaic capacity, irradiation, optimally tilted surface, Photovoltaic power potential

Last updated: 2021-10-30
