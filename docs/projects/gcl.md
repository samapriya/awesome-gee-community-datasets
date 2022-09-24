# Global Consensus Landcover

The datasets integrate multiple global remote sensing-derived land-cover products and provide consensus information on the prevalence of 12 land-cover classes at 1-km resolution. For additional information about the integration approach and the evaluations of the datasets.

#### Paper citation

```
Tuanmu, M.-N. and W. Jetz. 2014. A global 1-km consensus land-cover product for biodiversity and ecosystem modeling.
Global Ecology and Biogeography 23(9): 1031-1045.
```

![gcl](https://user-images.githubusercontent.com/6677629/117578547-86606c00-b0b4-11eb-81c7-b6f6c9e25edd.gif)

#### Earth Engine Snippet

```js
var barren = ee.Image("projects/sat-io/open-datasets/global_consensus_landcover/barren");
var cultivated_and_managed_vegetation = ee.Image("projects/sat-io/open-datasets/global_consensus_landcover/cultivated_and_managed_vegetation");
var deciduous_broadleaf_trees = ee.Image("projects/sat-io/open-datasets/global_consensus_landcover/deciduous_broadleaf_trees");
var evergreen_deciduous_needleleaf_trees = ee.Image("projects/sat-io/open-datasets/global_consensus_landcover/evergreen-deciduous_needleleaf_trees");
var evergreen_broadleaf_trees = ee.Image("projects/sat-io/open-datasets/global_consensus_landcover/evergreen_broadleaf_trees");
var herbaceous_vegetation = ee.Image("projects/sat-io/open-datasets/global_consensus_landcover/herbaceous_vegetation");
var mixed_other_trees = ee.Image("projects/sat-io/open-datasets/global_consensus_landcover/mixed-other_trees");
var open_water = ee.Image("projects/sat-io/open-datasets/global_consensus_landcover/open_water");
var regularly_flooded_vegetation = ee.Image("projects/sat-io/open-datasets/global_consensus_landcover/regularly_flooded_vegetation");
var shrubs = ee.Image("projects/sat-io/open-datasets/global_consensus_landcover/shrubs");
var snow_ice = ee.Image("projects/sat-io/open-datasets/global_consensus_landcover/snow-ice");
var urban_built_up = ee.Image("projects/sat-io/open-datasets/global_consensus_landcover/urban-built-up");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:earthenv-bd-ecosystems-clim-layers/GLOBAL-CONSENSUS-LANDCOVER


#### License
EarthEnv Global 1-km Consensus Land Cover Version 1 by Tuanmu & Jetz is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License. Permissions beyond the scope of this license may be available at http://www.earthenv.org/landcover.html.

#### Dataset citation

```
Tuanmu, M.-N. and W. Jetz. 2014. A global 1-km consensus land-cover product for biodiversity and ecosystem modeling.
Global Ecology and Biogeography 23(9): 1031-1045. Data available on-line at http://www.earthenv.org/.
```

Project Website: http://www.earthenv.org/landcover

App Website: [App link here](https://earthenv-dot-map-of-life.appspot.com/5/81.826/25.542?collections=consensus&layers=Herbaceous_Vegetation)

Curated by: Samapriya Roy

Keywords: Earthenv, barren, cultivated and managed vegetation, deciduous broadleaf trees, evergreen broadleaf trees, mixed other trees, shrubs, urban built up, evergreen deciduous needleleaf trees, mixed other trees

Last updated: 2021-05-09
