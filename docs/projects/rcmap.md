# Rangeland Condition Monitoring Assessment and Projection (RCMAP)

The Rangeland Condition Monitoring Assessment and Projection (RCMAP) v8 dataset quantifies the percent cover of rangeland components across western North America using Landsat imagery from 1985-2025. The RCMAP product suite consists of ten fractional components: annual herbaceous, bare ground, herbaceous, litter, non-sagebrush shrub, perennial herbaceous, sagebrush, shrub, tree, and shrub height; in addition to the temporal trends of each component.

Several enhancements were made to the RCMAP process relative to prior generations:

1. The training database was expanded by incorporating new observations from the BLM Analysis
   Inventory and Monitoring (AIM) dataset, Global Biodiversity Information Facility (GBIF)
   observations of sagebrush and various invasive grass species, Uncrewed Aerial Vehicle (UAV)
   data for Western South Dakota (Johnston et al. 2025), and additional Landsat scale
   observations collected by RCMAP
2. 10 new high-resolution training sites were added in the Great Plains
3. Enhanced noise filtering post-processing using the Savitsky-Golay filter
4. Integration of Exotic Annual Grass products into the RCMAP hierarchy

RCMAP data are useful to natural resource decision making including understanding drought impact, invasive species, fire risk, and livestock management.

#### Available Datasets

The RCMAP v8 product suite includes both cover data and time-series trends analysis. The following table shows the current availability status:

| Dataset Type | Description | Status | Earth Engine Collection |
| --- | --- | --- | --- |
| **Cover** | Percent cover of each component (1985-2025) | ✅ Complete | `projects/sat-io/open-datasets/USGS/RCMAP/V8/TIME_SERIES/COVER` |
| **Break Point Presence** | Presence/absence of structural breaks each year | ✅ Complete | Individual collections per component |
| **Break Point Count** | Number of structural breaks in time-series | ✅ Complete | `projects/sat-io/open-datasets/USGS/RCMAP/V8/TIME_SERIES_TRENDS/BREAK_POINT_COUNT` |
| **Theil Slope** | Theil-Sen linear slope over full period (1985-2025) | ✅ Complete | `projects/sat-io/open-datasets/USGS/RCMAP/V8/TIME_SERIES_TRENDS/THEIL_SLOPE` |
| **Total Change Intensity Index** | Derivative index of total change across primary components | ✅ Complete | `projects/sat-io/open-datasets/USGS/RCMAP/V8/TIME_SERIES_TRENDS/TOTAL_CHANGE_INDEX` |

#### Dataset Details

??? example "The RCMAP v8 dataset details can be found here"

      | Characteristic | Description |
      | --- | --- |
      | Name | RCMAP v8 |
      | Provider | USGS Earth Resources Observation and Science (EROS) Center |
      | Resolution | 30 meters |
      | Coverage | Western North America |
      | Temporal Range | 1985-2025 |
      | Components | 10 fractional cover components |
      | Data Structure | Percent cover of each component per pixel |
      | Study Area | Expanded to include grasslands biome (+1,830,783 km²) |

#### Rangeland Components

??? example "The RCMAP v8 dataset includes the following fractional cover components"

      | Component | Band Name | Description |
      | --- | --- | --- |
      | Annual Herbaceous | annual_herbaceous | Annual grasses and forbs |
      | Bare Ground | bare_ground | Exposed soil and rock surfaces |
      | Herbaceous | herbaceous | Combined herbaceous vegetation |
      | Litter | litter | Dead plant material on ground |
      | Non-Sagebrush Shrub | non_sagebrush_shrub | Shrubs excluding sagebrush species |
      | Perennial Herbaceous | perennial_herbaceous | Perennial grasses and forbs |
      | Sagebrush | sagebrush | Sagebrush shrub species |
      | Shrub | shrub | All shrub vegetation |
      | Shrub Height | shrub_height | Height measurement of shrub cover (cm) |
      | Tree | tree | Tree canopy cover |

#### RCMAP Time-Series Trends Analysis

The RCMAP product suite assesses temporal patterns in each component using two approaches: 1. linear trends and 2. a breaks and stable states method with a temporal moving window based on structural change at the pixel level.

Linear trend products include Theil-Sen slope, which features improved estimation of trend given outliers compared to the least squares method. The slope represents the average percent cover change per year over the time-series.

The structural change method partitions the time-series into segments of similar slope values, with statistically significant break-points indicating perturbations to the prior trajectory. The break point trends analysis suite produces the following statistics:

1. **Break Point Presence/Absence** - Presence/absence of structural breaks in each component each year
2. **Break Point Count** - Number of structural breaks observed in the time-series
3. **Total Change Intensity Index** - Derivative index highlighting total change across primary components
4. **Slope of Linear Model** - Theil-Sen slope of linear trends model (% change/year × 100)

#### Data Access

Component products can be downloaded at the [MRLC website](https://www.mrlc.gov/data) and are available in an interactive viewer: [MRLC Rangeland Viewer](https://www.mrlc.gov/viewer/). Additionally, data are available as WMS/WCS services through the [MRLC Data Services Page](https://www.mrlc.gov/data-services-page). Prior versions of RCMAP remain archived at [ScienceBase](https://www.sciencebase.gov/catalog/item/636a6727d34ed907bf6a6859).

#### Citation

```
Rigge, M., Bunde, B., and Postma, K., 2026, Rangeland Condition Monitoring Assessment and Projection (RCMAP) Fractional Component Time-Series Across Western North America from 1985-2025: U.S. Geological Survey data release, https://doi.org/10.5066/P138CYEL.
```

![rcmap_cover](../images/rcmap_cover.gif)

#### Earth Engine Snippet

```javascript
var rcmap_cover = ee.ImageCollection("projects/sat-io/open-datasets/USGS/RCMAP/V8/TIME_SERIES/COVER");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:regional-landuse-landcover/RCMAP-COVER

##### Break Point Presence Data (1985-2025)

```javascript
var bp_annual_herbaceous = ee.ImageCollection("projects/sat-io/open-datasets/USGS/RCMAP/V8/TIME_SERIES_TRENDS/BREAKPOINT_PRESENCE_ANNUAL/ANNUAL_HERBACEOUS");
var bp_bare_ground = ee.ImageCollection("projects/sat-io/open-datasets/USGS/RCMAP/V8/TIME_SERIES_TRENDS/BREAKPOINT_PRESENCE_ANNUAL/BARE_GROUND");
var bp_herbaceous = ee.ImageCollection("projects/sat-io/open-datasets/USGS/RCMAP/V8/TIME_SERIES_TRENDS/BREAKPOINT_PRESENCE_ANNUAL/HERBACEOUS");
var bp_litter = ee.ImageCollection("projects/sat-io/open-datasets/USGS/RCMAP/V8/TIME_SERIES_TRENDS/BREAKPOINT_PRESENCE_ANNUAL/LITTER");
var bp_non_sagebrush_shrub = ee.ImageCollection("projects/sat-io/open-datasets/USGS/RCMAP/V8/TIME_SERIES_TRENDS/BREAKPOINT_PRESENCE_ANNUAL/NON_SAGEBRUSH_SHRUB");
var bp_perennial_herbaceous = ee.ImageCollection("projects/sat-io/open-datasets/USGS/RCMAP/V8/TIME_SERIES_TRENDS/BREAKPOINT_PRESENCE_ANNUAL/PERENNIAL_HERBACEOUS");
var bp_sagebrush = ee.ImageCollection("projects/sat-io/open-datasets/USGS/RCMAP/V8/TIME_SERIES_TRENDS/BREAKPOINT_PRESENCE_ANNUAL/SAGEBRUSH");
var bp_shrub = ee.ImageCollection("projects/sat-io/open-datasets/USGS/RCMAP/V8/TIME_SERIES_TRENDS/BREAKPOINT_PRESENCE_ANNUAL/SHRUB");
var bp_shrub_height = ee.ImageCollection("projects/sat-io/open-datasets/USGS/RCMAP/V8/TIME_SERIES_TRENDS/BREAKPOINT_PRESENCE_ANNUAL/SHRUB_HEIGHT");
var bp_tree = ee.ImageCollection("projects/sat-io/open-datasets/USGS/RCMAP/V8/TIME_SERIES_TRENDS/BREAKPOINT_PRESENCE_ANNUAL/TREE");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:regional-landuse-landcover/RCMAP-BREAK-POINT

##### Break Point Count Data

```javascript
var breakpoint_count = ee.Image("projects/sat-io/open-datasets/USGS/RCMAP/V8/TIME_SERIES_TRENDS/BREAK_POINT_COUNT");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:regional-landuse-landcover/RCMAP-BREAK-POINT-COUNT

##### Theil-Sen Slope

```javascript
var theil_slope = ee.Image("projects/sat-io/open-datasets/USGS/RCMAP/V8/TIME_SERIES_TRENDS/THEIL_SLOPE");
```

##### Total Change Intensity Index

```javascript
var total_change = ee.Image("projects/sat-io/open-datasets/USGS/RCMAP/V8/TIME_SERIES_TRENDS/TOTAL_CHANGE_INDEX");
```

#### License

This work is marked with CC0 1.0 Universal. You are free to copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.

Created by: Matthew B. Rigge, Brett Bunde, Kory Postma, and collaborators at USGS Earth Resources Observation and Science (EROS) Center

Curated in GEE by: Samapriya Roy

Keywords: Rangeland, USGS, Google Earth Engine, Landsat, Vegetation mapping, Fractional cover, Time series, Natural resources, Land management, Western North America

Last updated: 2026-06-09
