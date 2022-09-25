# Harmonised global datasets of wind and solar farm locations and power

Energy systems need decarbonisation in order to limit global warming to within safe limits. While global land planners are promising more of the planet’s limited space to wind and solar photovoltaic, there is little information on where current infrastructure is located. The majority of recent studies use land suitability for wind and solar, coupled with technical and socioeconomic constraints, as a proxy for actual location data. Here, we address this shortcoming. Using readily accessible OpenStreetMap data we present, to our knowledge, the first global, open-access, harmonised spatial datasets of wind and solar installations. We also include user friendly code to enable users to easily create newer versions of the dataset. Finally, we include first order estimates of power capacities of installations. We anticipate these data will be of widespread interest within global studies of the future potential and trade-offs associated with the global decarbonisation of energy systems.

Data is available for download from [figshare here](https://figshare.com/articles/dataset/Harmonised_global_datasets_of_wind_and_solar_farm_locations_and_power/11310269)


#### Data Citation

```
Dunnett, S. Harmonised global datasets of wind and solar farm locations and power. figshare. Dataset. https://doi.org/10.6084/m9.figshare.11310269 (2020)
```

#### Paper Citation

```
Dunnett, S., Sorichetta, A., Taylor, G. et al. Harmonised global datasets of wind and solar farm locations and power. Sci Data 7, 130 (2020). https://doi.org/10.1038/s41597-020-0469-8
```

![solar_wind](https://user-images.githubusercontent.com/25802584/131460423-f5acebf1-d53b-48e7-a97a-9abab4ca8207.gif)

#### Earth Engine Snippet

```js
var wind_farms = ee.FeatureCollection("projects/sat-io/open-datasets/global_wind_farms_2020");
var solar_farms = ee.FeatureCollection("projects/sat-io/open-datasets/global_solar_farms_2020");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/HARMONIZED-WIND-SOLAR-FARMS

#### Property Mapping

|Name              |Detail          |
|------------------|----------------|
|X                 |X coordinate (.csv only)|
|Y                 |Y coordinate (.csv only)|
|x_id              |unique identifier for data record|
|GID_0             |ISO3 country code|
|panels            |number of panels|
|turbines          |number of turbines|
|panel.area        |total panel area in km2 (p_area for .gdb files)|
|landscape.area    |landscape area in km2 (l_area for .gdb files)|
|water             |binary response indicating whether data record is classified as water|
|urban             |binary response indicating whether data record is classified as urban centre|
|power             |estimated power capacity in MW|


#### License
Data adapted or built on OpenStreetMap data are required to be distributed under the same licence. These data are therefore made available under the Open Data Commons Open Database License (ODbL). Personal figshare accounts cannot currently present data under this licence so the data are currently (incorrectly) presented under a CC0 licence as a stopgap until this changes.

Created by: Dunnett et al.

Curated by: Samapriya Roy

Keywords:  solar, wind, energy, renewable

Last updated: 2021-08-31
