# Global Freshwater Variables

The dataset consists of near-global, spatially continuous, and freshwater-specific environmental variables in a standardized 1km grid. We delineated the sub-catchment for each grid cell along the HydroSHEDS river network and summarized the upstream environment (climate, topography, land cover, surface geology and soil) to each grid cell using various metrics (average, minimum, maximum, range, sum, inverse distance-weighted average and sum). All variables were subsequently averaged across single lakes and reservoirs of the Global lakes and Wetlands Database that are connected to the river network. Monthly climate variables were summarized into 19 long-term climatic variables following the “bioclim” framework.

#### Paper citation

```
Domisch, S., Amatulli, G., and Jetz, W. (2015) Near-global freshwater-specific environmental variables for biodiversity analyses in 1 km resolution.
Scientific Data 2:150073 doi:10.1038/sdata.2015.73
```

![fresh_water_earthenv](https://user-images.githubusercontent.com/6677629/117553926-f0780300-b019-11eb-8139-d68cafbd1ff3.gif)



#### Earth Engine Snippet

```js
var annual_air_temperature_range_avg = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/annual_air_temperature_range_avg");
var annual_sum_of_precipitation_avg = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/annual_sum_of_precipitation_avg");
var barren_lands_sparse_vegetation_avg = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/barren_lands_sparse_vegetation_avg");
var catchment_size_sum = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/catchment_size_sum");
var cultivated_and_managed_vegetation_avg = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/cultivated_and_managed_vegetation_avg");
var deciduous_broadleaf_trees_avg = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/deciduous_broadleaf_trees_avg");
var elevation_avg = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/elevation_avg");
var elevation_range = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/elevation_range");
var evergreen_broadleaf_trees_avg = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/evergreen_broadleaf_trees_avg");
var evergreen_deciduous_needleleaf_trees_avg = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/evergreen_deciduous_needleleaf_trees_avg");
var herbaceous_vegetation_avg = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/herbaceous_vegetation_avg");
var mean_annual_air_temperature_avg = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/mean_annual_air_temperature_avg");
var mixed_other_trees_avg = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/mixed_other_trees_avg");
var open_water_avg = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/open_water_avg");
var precambrian_surface_lithology_wsum = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/precambrian_surface_lithology_wsum");
var precipitation_seasonality_avg = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/precipitation_seasonality_avg");
var quaternary_surface_lithology_wsum = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/quaternary_surface_lithology_wsum");
var regularly_flooded_shrub_herbaceous_vegetation_avg = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/regularly_flooded_shrub_herbaceous_vegetation_avg");
var shrubs_avg = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/shrubs_avg");
var slope_avg = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/slope_avg");
var slope_range = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/slope_range");
var snow_ice_avg = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/snow-ice_avg");
var stream_length_sum = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/stream_length_sum");
var urban_builtup_avg = ee.Image("projects/sat-io/open-datasets/global_freshwater_variables/urban_builtup_avg");
```

Sample Code: https://code.earthengine.google.com/9d8642769f76a2b79f192cd7df4a2183


#### License
EarthEnv Near-global environmental information for freshwater ecosystems in 1km resolution Version 1 by Domisch et al. is licensed under a “Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License”. Permissions beyond the scope of this license may be available at http://www.earthenv.org/.

#### Dataset citation

```
Domisch, S., Amatulli, G., and Jetz, W. (2015) Near-global freshwater-specific environmental variables for biodiversity analyses in 1 km resolution.
Scientific Data 2:150073 doi: 10.1038/sdata.2015.73. Data available online at http://www.earthenv.org/.
```


Project Website: http://www.earthenv.org/streams

App Website: [App link here](https://earthenv-dot-map-of-life.appspot.com/2/-24.961/-21.453?collections=streams&layers=Precipitation_seasonality_(avg))

Curated by: Samapriya Roy

Keywords: Earthenv, stream length, urban builtup, slope, shrubs, precambrian surface lithology, barren_lands, precipitation seasonality, herbaceous vegetation

Last updated: 2021-05-09
