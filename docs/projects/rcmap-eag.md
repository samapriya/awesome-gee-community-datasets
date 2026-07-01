# RCMAP Weekly Herbaceous and Exotic Annual Grass (RCMAP-EAG)

The Rangeland Condition Monitoring Assessment and Projection (RCMAP) dataset quantifies the percent cover of rangeland components across western North America using Landsat imagery with annual products for 1985-2025.

Exotic Annual Grasses (EAGs) can disrupt ecosystems since they often possess competitive advantages over native species. Application of remote sensing to capture the extent of EAG invasion across years enables managers to evaluate treatment success and strategize for defending and growing core (uninvaded) habitats. At the same time, finer temporal scale (weekly) classification of EAG cover empowers decision making on fire management and grazing. Weekly maps of combined EAG cover were previously developed for a set of common species, along with individual maps for especially challenging species, using Harmonized Landsat Sentinel (HLS) imagery.

Major methodological improvements have been implemented relative to the previous mapping method:

1. Improved HLS composites
2. Additional training data and predictor variables
3. Expanded temporal mapping window
4. Training data association to a point in time instead of the seasonal curve
5. Enhanced post-processing
6. Improved product consistency
7. An additional component, total herbaceous, and nesting of EAG components within RCMAP components
8. Validation of the products with withheld Bureau of Land Management (BLM) Analysis Inventory and Monitoring (AIM) data

Weekly EAG releases are produced for weeks 10-38 (early March-late September) of 2016-present. Releases are available within a week of the most recent satellite image used in the product. Each weekly release contains eight fractional cover maps for the following components: total herbaceous, green herbaceous, senesced herbaceous, total EAG, cheatgrass, field brome, medusahead, and Sandberg's bluegrass; see component definitions in the section below.

In addition to weekly products, annual data are derived by obtaining the maximum cover value across weeks in a year by component. Weekly Herbaceous and EAG cover datasets were generated leveraging field observations from the BLM AIM database and RCMAP plots, weekly HLS composites, and other relevant environmental, vegetation, remotely sensed, and geophysical drivers, using artificial intelligence/machine learning techniques.

RCMAP-EAG data are useful to natural resource decision making including fire management, grazing strategy, invasive species treatment evaluation, and defending and growing core (uninvaded) habitats.

#### Available Datasets

The RCMAP-EAG product suite includes both weekly and annual cover data, delivered through a single Earth Engine collection. The following table shows the current availability status:

| Dataset Type | Description | Status | Earth Engine Collection |
| --- | --- | --- | --- |
| **Cover** | Percent cover of each component, weekly (weeks 10-38) and annual (max cover), 2016-present | ✅ Complete | `projects/sat-io/open-datasets/USGS/RCMAP/EAG/TIME_SERIES/COVER` |

#### Dataset Details

??? example "The RCMAP-EAG dataset details can be found here"

      | Characteristic | Description |
      | --- | --- |
      | Name | RCMAP-EAG |
      | Provider | USGS Earth Resources Observation and Science (EROS) Center |
      | Resolution | 30 meters |
      | Coverage | Western North America |
      | Temporal Range | Weeks 10-38 of 2016-present |
      | Components | 8 fractional cover components |
      | Data Structure | Percent cover of each component per pixel |
      | Study Area | Western and central CONUS and the sagebrush biome of Canada |

#### Rangeland Components

??? example "The RCMAP-EAG dataset includes the following fractional cover components"

      | Component | Band Name | Description |
      | --- | --- | --- |
      | Total Herbaceous* | total_herbaceous | Grasses, forbs and cacti which were photosynthetically active at any point in the year of mapping |
      | Green Herbaceous | green_herbaceous | Grasses, forbs and cacti which were photosynthetically active during the week of mapping |
      | Senesced Herbaceous | senesced_herbaceous | Grasses, forbs and cacti which were not photosynthetically active during the week of mapping |
      | Total EAG* | eag | Combined cover of field brome, rattlesnake brome, rescuegrass, bald brome, ripgut brome, soft brome, Japanese brome, compact brome, red brome, rye brome, cheatgrass, medusahead, and Ventenata |
      | Cheatgrass* | cheatgrass | *Bromus tectorum* |
      | Field Brome* | fieldbrome | Field brome (*Bromus arvensis*) and Japanese brome (*Bromus japonicus*) |
      | Medusahead* | medusahead | *Taeniatherum caput-medusae* |
      | Sandberg's Bluegrass* | sandbergs_bluegrass | *Poa secunda* |

      \* Indicates that weekly cover constitutes the total cover of relevant plant material that was photosynthetically active in the week of mapping or at any point year-to-date.

#### Data Access

Component products can be downloaded at the [MRLC website](https://www.mrlc.gov/data) and are available in an interactive viewer: [MRLC Rangeland Viewer](https://www.mrlc.gov/viewer/). Additionally, data are available as WMS/WCS services through [ArcGIS Online](https://usgs.maps.arcgis.com/home/group.html?id=50bfb9d0ff504d93a1431626b19c8c00).

#### Citation

```
Rigge, M., Postma, K., Dahal, D., Dornbierer, J., Megard, L., Benedict, T., and Bunde, B., 2026, Weekly Herbaceous and Exotic Annual Grass (EAG) Cover for western North America 2016 - 2026: U.S. Geological Survey database, https://doi.org/10.5066/P13QWBFH.
```

#### Earth Engine Snippet

```javascript
var rcmap_eag_cover = ee.ImageCollection("projects/sat-io/open-datasets/USGS/RCMAP/EAG/TIME_SERIES/COVER");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:regional-landuse-landcover/RCMAP-EAG-COVER

#### License

This work is marked with CC0 1.0 Universal. You are free to copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.

Created by: Matthew Rigge, Kory Postma, Devendra Dahal, Jordan Dornbierer, Logan Megard, Trenton Benedict, Brett Bunde, and collaborators at USGS Earth Resources Observation and Science (EROS) Center

Curated in GEE by: Samapriya Roy

Keywords: Rangeland, Exotic Annual Grass, Invasive Annual Grass, Cheatgrass, Medusahead, USGS, Google Earth Engine, Landsat, Vegetation mapping, Fractional cover, Time series, Natural resources, Land management, Western North America

Last updated: 2026-06-30
