# Global Wind Atlas Datasets

The Global Wind Atlas is a free, web-based application developed to help policymakers, planners, and investors identify high-wind areas for wind power generation virtually anywhere in the world, and then perform preliminary calculations. The Global Wind Atlas facilitates online queries and provides freely downloadable datasets based on the latest input data and modeling methodologies. Users can additionally download high-resolution maps of the wind resource potential, for use in GIS tools, at the global, country, and first-administrative unit (State/Province/Etc.) levels. You can read more about the [methods used here](https://globalwindatlas.info/about/method)

The modeling process is made up of a WAsP calculation of local wind climates for every 250 m at five heights: 10 m; 50 m; 100 m; 150 m and; 200 m. On a 250 m grid, there is a local wind climate estimate for every node. Power density data takes into account geographical variations of air density. Includes variables in the Google Earth Engine collection include, wind speed, air density and power density. Surface roughness length is a property of the surface which can be used to determine the way the horizontal wind speed varies with height. The wind speed at a given height decreases with increasing surface roughness.

Most of the data are named as follows: gwa_{variable}_{height}.tif with GEE collections, where variable is one of and this [description below is obtained here](https://data.dtu.dk/articles/dataset/Global_Wind_Atlas_v3/9420803)

* wind-speed - The mean wind speed at the location for the 10 year period

* power-density - The mean power density of the wind, which is related to the cube of the wind speed, and can provide additional information about the strength of the wind not found in the mean wind speed alone.

* air-density - The air density is found by interpolating the air density from the CFSR reanalysis to the elevation used in the global wind atlas following the approach described in WAsP 12.

* RIX - The RIX (Ruggedness IndeX) is a measure of how complex the terrain is. It provides the percent of the area within 10 km of the position that have slopes over 30-degrees. A RIX value greater than 5 suggests that you should use caution when interpreting the results.

The files which do not follow the naming convention above are the capacity-factor layers. The capacity factor layers were calculated for 3 distinct wind turbines, with 100m hub height and rotor diameters of 112, 126, and 136m, which fall into three IEC Classes (IEC1, IEC2, and IEC3). Capacity factors can be used to calculate a preliminary estimate of the energy yield of a wind turbine (in the MW range), when placed at a location. This can be done by multiplying the rated power of the wind turbine by the capacity factor for the location (and the number of hours in a year):

AEP = P<sub>rated</sub> * CF * 8760 hr/year,

where AEP is annual energy production, Prated is rated power, and CF is capacity factor.

<center>

|Variable Name       |Version|Heights(in m)    |
|--------------------|-------|-----------------|
|Wind Speed          |3      |10,50,100,150,200|
|Power Density       |3      |10,50,100,150,200|
|Air Density         |3      |10,50,100,150,200|
|Capacity Factor IEC1|3      |NA               |
|Capacity Factor IEC2|3      |NA               |
|Capacity Factor IEC3|3      |NA               |
|Ruggedness Index    |3      |NA               |


</center>

#### Attribution and License
If you get the data or use the dataset within the GWA app attribution below, the Works (datasets) themselves are under are licensed under the Creative Commons Attribution 4.0 International license, CC BY 4.0, except where expressly stated that another license applies.

```
[Data/information/map obtained from the] “Global Wind Atlas 3.0, a free, web-based application developed,
owned and operated by the Technical University of Denmark (DTU). The Global Wind Atlas 3.0 is released in partnership
with the World Bank Group, utilizing data provided by Vortex, using funding provided by
the Energy Sector Management Assistance Program (ESMAP). For additional information: https://globalwindatlas.info”
```

You can also find the Global Wind Atlas [here](https://globalwindatlas.info/) and you can interact and download the datasets [here](https://globalwindatlas.info/download/gis-files)

![gwa](https://user-images.githubusercontent.com/6677629/125204763-7b58c200-e244-11eb-9932-79e7c9c0fb6c.gif)

#### Data Preprocessing for GEE
Capacity Factors were added onto a single collection and rotor diameter and hub height was added as metadata property for filtering. For variables that have height gradients, height was added as a metadata for filtering.

#### Earth Engine Datasets

```js
var air_density = ee.ImageCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/global_wind_atlas/air-density');
var capacity_factor = ee.ImageCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/global_wind_atlas/capacity-factor');
var power_density = ee.ImageCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/global_wind_atlas/power-density');
var rix= ee.Image('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/global_wind_atlas/ruggedness-index');
var wind_speed= ee.ImageCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/global_wind_atlas/wind-speed');
```

Sample Code: https://code.earthengine.google.com/8c3d27d67a2e7d9bda015c325d505409


Produced and maintained by the [Global Wind Atlas](https://globalwindatlas.info/), Department of Wind Energy at the Technical University of Denmark (DTU Wind Energy) and the World Bank Group (consisting of The World Bank and the International Finance Corporation, or IFC)

Processed secondary/formatted & Curated by: Samapriya Roy

Keywords: : Wind, energy, ruggedness index, capacity factor, wind speed, power density

Last updated: 2021-07-11
