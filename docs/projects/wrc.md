# Wildfire Risk to Communities (WRC)

The Wildfire Risk to Communities dataset was created by the USDA Forest Service to provide a nationwide view of wildfire risk potential. The dataset includes spatial data on the following components of wildfire risk: wildfire likelihood, wildfire intensity, susceptibility, and exposure. The data is available at a 270-meter resolution and covers the entire United States. It is based on a variety of sources, including vegetation data, fuel models, historical fire data, and population data.

The Wildfire Risk to Communities dataset can be used to assess wildfire risk at the community level and to develop wildfire mitigation plans. It can also be used to identify communities that are most in need of assistance. The Wildfire Risk to Communities dataset was created by USDA Forest Service to help assess risk to homes, businesses, and other valued resources. The dataset contains nationally-consistent information for the purpose of comparing relative wildfire risk among communities nationally or within a state or county. In situ risk (risk at the location where the adverse effects take place on the landscape) are modeled using the large fire simulation system (FSim) and LANDFIRE fuel loading datasets from 2014. The original data at 250m has been upsampled to 30m for this dataset on Climate Engine. You can find additional information about [the dataset here](https://www.fs.usda.gov/managing-land/fire/wildfirerisk) and read more [about this on climate engine org page here](https://support.climateengine.org/article/92-wrc). Here is a link to the [report documentation](https://www.fs.usda.gov/rds/archive/catalog/RDS-2020-0016)

<center>

| **Spatial Extent**                      | United States                                        |
|-----------------------------------------|------------------------------------------------------|
| **Spatial Resolution**                  | 30 m                                                 |
| **Temporal Resolution**                 | Single point in time                                |
| **Time Span**                           | 2014                                                 |
| **Update Frequency**                    | Static                                               |

</center>

<center>

| **Variables**                           |                                                      |
|-----------------------------------------|------------------------------------------------------|
| Burn probability ('BP')                 | - Units: Fractional probability                      |
|                                         | - Scale Factor: 1.0                                 |
| Conditional flame length ('CFL')        | - Units: Feet                                        |
|                                         | - Scale Factor: 1.0                                 |
| Conditional risk to potential structures ('CRPS') | - Units: Percentile                  |
|                                         | - Scale Factor: 1.0                                 |
| Exposure type ('Exposure')              | - Units: Exposure type                              |
|                                         | - Scale Factor: 1.0                                 |
| Flame length exceedance probability - 4 ft ('FLEP4') | - Units: Fractional probability       |
|                                         | - Scale Factor: 1.0                                 |
| Flame length exceedance probability - 8 ft ('FLEP8') | - Units: Fractional probability       |
|                                         | - Scale Factor: 1.0                                 |
| Risk to potential structures ('RPS')    | - Units: Percentiles                                |
|                                         | - Scale Factor: 1.0                                 |
| Wildfire hazard potential index ('WHP') | - Units: Unitless                                   |
|                                         | - Scale Factor: 1.0                                 |

</center>

#### Citation

```
Scott, Joe H.; Gilbertson-Day, Julie W.; Moran, Christopher; Dillon, Gregory K.; Short, Karen C.; Vogler, Kevin C. 2020. Wildfire Risk to
Communities: Spatial datasets of landscape-wide wildfire risk components for the United States. Fort Collins, CO: Forest Service Research Data
Archive. Updated 25 November 2020.
```

![wrc](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/c1509a48-ae97-48e4-ae6f-190eb1b0dd52)

### Earth Engine Snippet

```js
// Read in Image Collection and mosaic to single image
var wrc_i = ee.ImageCollection('projects/climate-engine-pro/assets/ce-wrc-static').mosaic()
// Print image to see bands
print(wrc_i)
// Visualize select bands from first image — additional bands are present in the Image Collection
var bp_palette = ["#d53e4f", "#fc8d59", "#fee08b", "#ffffbf", "#e6f598", "#99d594", "#3288bd"].reverse()
var exposure_palette = ["#f6eff7", "#d0d1e6", "#a6bddb", "#67a9cf", "#3690c0", "#02818a", "#016450"].reverse()
var crps_palette = ["#ffffd4", "#fee391", "#fec44f", "#fe9929", "#ec7014", "#cc4c02", "#8c2d04"]
var flep_palette = ["#8c510a", "#d8b365", "#f6e8c3", "#f5f5f5", "#c7eae5", "#5ab4ac", "#01665e"].reverse()
var rps_palette = ["#ffffb2", "#fed976", "#feb24c", "#fd8d3c", "#fc4e2a", "#e31a1c", "#b10026"]
var whp_palette = ["#d73027", "#fc8d59", "#fee08b", "#ffffbf", "#d9ef8b", "#91cf60", "#1a9850"].reverse()
Map.addLayer(wrc_i.select('BP'), {min: 0, max: 0.025, palette: bp_palette}, 'BP')
Map.addLayer(wrc_i.select('CFL').selfMask(), {min: 0, max: 15, palette: flep_palette}, 'CFL')
Map.addLayer(wrc_i.select('CRPS'), {min: 30, max: 80, palette: crps_palette}, 'CRPS')
Map.addLayer(wrc_i.select('Exposure'), {min: 0, max: 1, palette: exposure_palette}, 'Exposure')
Map.addLayer(wrc_i.select('FLEP4'), {min: 0.1, max: 0.9, palette: flep_palette}, 'FLEP4')
Map.addLayer(wrc_i.select('FLEP8'), {min: 0.1, max: 0.9, palette: flep_palette}, 'FLEP8')
Map.addLayer(wrc_i.select('RPS'), {min: 0, max: 1, palette: rps_palette}, 'RPS')
Map.addLayer(wrc_i.select('WHP'), {min: 0, max: 2000, palette: whp_palette}, 'WHP')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:fire-monitoring-analysis/WILDFIRE-RISK-COMMUNITIES

#### License
CC0 1.0 Universal (CC0 1.0) Public Domain Dedication

Keywords: Wildfire, CONUS, United States, USDA, Forest Service, LANDFIRE

Provided by: USDA Forest Service

Curated in GEE by: Climate Engine Org
