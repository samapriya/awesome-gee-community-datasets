# Current and projected climate data for North America (CMIP6 scenarios)

Atmosphere-Ocean General Circulation Model (AOGCM) were developed to simulate climate variability on a wide range of time scales and are often tested in coupled simulations and data assimilation mode. You can [read more about AOGCMs and CMIP6 here](https://www.carbonbrief.org/cmip6-the-next-generation-of-climate-models-explained). The datasets on this page have been developed by AdaptWest, a project funded by the Wilburforce Foundation to develop information resources for climate adaptation planning. The data were generated using the ClimateNA software. ClimateNA uses data from PRISM and WorldClim for current climate, and downscales data from the Coupled Model Intercomparison Project phase 6 (CMIP6) database corresponding to the 6th IPCC Assessment Report for future projections.

Ensemble projections are average projections from 13 CMIP5 models (table below) that were chosen to represent all major clusters of similar AOGCMs. In addition to the ensemble projections, data are also provided from 9 individual AOGCMs (table below) that are representative of the larger ensemble. Nine individual models were selected to represent all major clusters of similar AOGCMs. A broader set of 13 AOGCMs were used to create the ensemble data. Ensemble projections are also provided here for a greater range of time periods and scenarios than are the projections from individual AOGCMs.

<center>

|AOGCM Ensemble Models|AOGCM Individual Models                   |
|---------------------|------------------------------------------|
|ACCESS-ESM1-5        |ACCESS-ESM1-5                             |
|BCC-CSM2-MR          |                                          |
|CNRM-ESM2-1          |CNRM-ESM2-1                               |
|CanESM5              |                                          |
|EC-Earth3            |EC-Earth3                                 |
|GFDL-ESM4            |GFDL-ESM4                                 |
|GISS-E2-1-G          |GISS-E2-1-G                               |
|INM-CM5-0            |                                          |
|IPSL-CM6A-LR         |                                          |
|MIROC6               |MIROC6                                    |
|MPI-ESM1-2-HR        |MPI-ESM1-2-HR                             |
|MRI-ESM2-0           |MRI-ESM2-0                                |
|UKESM1-0-LL          |UKESM1-0-LL                               |

</center>


#### Data citation

```
AdaptWest Project. 2021. Gridded current and projected climate data for North America at 1km resolution,
generated using the ClimateNA v7.01 software (T. Wang et al., 2021). Available at adaptwest.databasin.org.
```

### Paper citation

You can read the [paper here](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0156720) and cite as as below

```
Wang, T., A. Hamann, D. Spittlehouse, C. Carroll. 2016. Locally Downscaled and Spatially Customizable Climate Data
for Historical and Future Periods for North America. PLoS One 11(6): e0156720.
```

The current climatic variables included in the datasets for climate normals, AOGCM models and AOGCM ensemble model are listed below

<center>

|Monthly Variables|Description                               |
|-----------------|------------------------------------------|
|tmin             |minimum temperature for a given month (°C)|
|tmax             |maximum temperature for a given month (°C)|
|tave             |mean temperature for a given month (°C)   |
|ppt              |total precipitation for a given month (mm)|

</center>

![cimp6_scenario3-70](https://user-images.githubusercontent.com/6677629/122656133-8fb20f00-d11d-11eb-80eb-b21dc41106b4.gif)

#### Earth Engine Snippet

```
var climate_models_ppt = ee.ImageCollection("projects/sat-io/open-datasets/CMIP6-scenarios-NA/Climate-Models_ppt");
var climate_models_tave = ee.ImageCollection("projects/sat-io/open-datasets/CMIP6-scenarios-NA/Climate-Models_tave");
var climate_models_tmax = ee.ImageCollection("projects/sat-io/open-datasets/CMIP6-scenarios-NA/Climate-Models_tmax");
var climate_models_tmin = ee.ImageCollection("projects/sat-io/open-datasets/CMIP6-scenarios-NA/Climate-Models_tmin");
var climate_normals_ppt = ee.ImageCollection("projects/sat-io/open-datasets/CMIP6-scenarios-NA/Climate-Normals_ppt");
var climate_normals_tave = ee.ImageCollection("projects/sat-io/open-datasets/CMIP6-scenarios-NA/Climate-Normals_tave");
var climate_normals_tmax = ee.ImageCollection("projects/sat-io/open-datasets/CMIP6-scenarios-NA/Climate-Normals_tmax");
var climate_normals_tmin = ee.ImageCollection("projects/sat-io/open-datasets/CMIP6-scenarios-NA/Climate-Normals_tmin");
var aogcm_ensemble_ppt = ee.ImageCollection("projects/sat-io/open-datasets/CMIP6-scenarios-NA/AOGCM-ensemble_ppt");
var aogcm_ensemble_tave = ee.ImageCollection("projects/sat-io/open-datasets/CMIP6-scenarios-NA/AOGCM-ensemble_tave");
var aogcm_ensemble_tmax = ee.ImageCollection("projects/sat-io/open-datasets/CMIP6-scenarios-NA/AOGCM-ensemble_tmax");
var aogcm_ensemble_tmin = ee.ImageCollection("projects/sat-io/open-datasets/CMIP6-scenarios-NA/AOGCM-ensemble_tmin");
```

Sample Code: https://code.earthengine.google.com/f1a7a341371b4a9a6ea441f2f307f323

#### Post processing for Google Earth Engine
* All of the 9 individual AOGCM models are added to the collection pertaining to each climate variable and named Climate-Models_(Variable Name). The ensemble models are ingested as along with the climate normals.
* Both AOGCM ensemble and individual models have date range and emission scenario type **emission_scenario** and **start** and **end** dates are added as property.
* Since the Climate-Models-(Variable Name) collection consists of 9 individual models another metadata field is added to those collections namely **global_climate_model** to filter by model name.
* Since all Climate variables are monthly , an extra metadata called **month** is added to the climate normals, ensemble and the individual model collections for further slicing the data as needed.

#### Known issues:
1. Some discontinuity in precipitation values occurs along the US/Canada border due to edge-matching issues between the PRISM data for the two nations.

2. Mean annual solar radiation (MAR) data are provisional and are slated to be revised in an upcoming release of the ClimateNA software.

#### License
These datasets  are made available under the CC BY 4.0 Attribution 4.0 International license. This license allows users to distribute, remix, adapt, and build upon the material in any medium or format, so long as attribution is given to the creator.

Data Website: You can download the [data and description here](https://adaptwest.databasin.org/pages/adaptwest-climatena/)

Explore the data in [R-Shiny apps here](https://bcgov-env.shinyapps.io/cmip6-NA/)

Created by: AdaptWest Project, Wang, T., A. Hamann, D. Spittlehouse, C. Carroll

Curated in GEE by: Samapriya Roy

Keywords: climate change, global circulation models, gridded climate data, north america,emission scenarios,climate variables

Last updated: 2021-06-19
