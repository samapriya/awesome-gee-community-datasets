# Global Oil Palm Dataset 1990-2021

???+ note

    **This dataset is part of a paper in submission and citation and DOI information will be updated accordingly. This will be updated as the paper progresses through review and publication cycles.Please keep this into consideration while using this dataset**

The dataset provides a comprehensive global map of oil palm plantations, including both industrial and smallholder plots, at a 10-meter resolution using Sentinel-1 data from 2016 to 2021. Additionally, it includes planting year estimates from 1990 to 2021 at a 30-meter spatial resolution derived from Landsat-5, -7, and -8 imagery. This dataset aims to support environmental monitoring and policy discussions by offering detailed and up-to-date information on the extent and age of oil palm plantations worldwide. You can read [the preprint here](https://essd.copernicus.org/preprints/essd-2024-157/essd-2024-157.pdf).

This data repository can be [found here](https://zenodo.org/records/11034131) offers comprehensive data on global oil palm plantations, including a 10-meter resolution global oil palm extent layer for the year 2021 and a 30-meter resolution oil palm planting year layer spanning from 1990 to 2021. The extent layer was generated using a convolutional neural network applied to Sentinel-1 data, identifying both industrial and smallholder plantations. The planting year layer was developed to detect early oil palm growth stages using the Landsat time series.

The key findings of the dataset reveal a total mapped area of 23.98 million hectares (Mha) of oil palm plantations, comprising 16.66 ± 0.25 Mha of industrial and 7.59 ± 0.29 Mha of smallholder oil palm. The accuracy of the data is high, with producers' and users' accuracy for industrial plantations at 91.9 ± 3.4% and 91.8 ± 1.0%, respectively, and for smallholders at 72.7 ± 1.3% and 75.7 ± 2.5%, respectively. The average age of the plantations is 14.1 years, and 6.28 Mha are over 20 years old, indicating a significant need for replanting within the coming decade.

### Data Layers

#### 1. Grid_OilPalm2016-2021
- **Format:** Shapefile
- **Description:** Delineates the 609 grid cells of 100 x 100 km where oil palm was detected.
- **Use Case:** Provides a spatial reference for the distribution of oil palm plantations across the globe, essential for mapping and analysis tasks.

#### 2. GlobalOilPalm_OP-extent
- **Format:** Geotiff (Raster Tiles)
- **Description:** Contains 609 raster tiles (each 100x100 km) showing the results of the deep learning classification at a 10-meter spatial resolution.
- **Classes:**
  - [0] Other land covers that are not oil palm.
  - [1] Industrial oil palm plantations.
  - [2] Smallholder oil palm plantations.
- **Use Case:** Useful for detailed spatial analysis of oil palm distribution and for distinguishing between different types of plantations.

#### 3. GlobalOilPalm_YoP
- **Format:** Geotiff (Raster Tiles)
- **Description:** Comprises 609 raster tiles (each 100x100 km) depicting the year of oil palm plantation establishment at a 30-meter spatial resolution.
- **Use Case:** Enables temporal analysis of oil palm plantation expansion and monitoring of plantation ages over time.

#### 4. Validation_points_GlobalOP2016-2021
- **Format:** Shapefile
- **Description:** Contains 17,812 points used to validate the global oil palm extent and age layers. Each point includes:
  - ‘Class’: Assigned by visual interpretation (class values same as extent layer).
  - ‘OP2016-2021’ and ‘OP2019’: Mapped classes in this dataset and the 2019 global oil palm layer (Descals et al., 2021), respectively.
- **Classes:**
  - [0] Other land covers that are not oil palm.
  - [1] Industrial oil palm plantations.
  - [2] Smallholder oil palm plantations.
- **Use Case:** Critical for validation and accuracy assessment of the oil palm extent and age datasets.

### Visualization
The oil palm extent and planting year data can be explored through a web map available at: [Global Oil Palm Planting Year 1990-2021](https://ee-globaloilpalm.projects.earthengine.app/view/global-oil-palm-planting-year-1990-2021). This tool allows users to inspect the Landsat time series and view historical satellite images of oil palm plantations.

#### Citation

```
Descals, A., Gaveau, D. L. A., Wich, S., Szantoi, Z., and Meijaard, E.: Global mapping of oil palm planting year from 1990 to 2021
Earth Syst. Sci Data Discuss. [preprint], https://doi.org/10.5194/essd-2024-157, in review, 2024.
```

#### Dataset Citation

```
Descals, A. (2024). Global oil palm extent and planting year from 1990 to 2021 (v1.1) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.11034131
```

![globaloilpalm](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/94485bd0-b4f6-443f-bac0-3e315acf7982)

#### Earth Engine Snippet

```js
/*
GlobalOilPalm_YoP_2021: year of oil palm plantation establishment
grid_oilpalm: Delineates the 609 grid cells of 100 x 100 km where oil palm was detected
globaloilpalm_extent2021: Deep learning classification at a 10-meter spatial resolution
- **Classes:**
  - [0] Other land covers that are not oil palm.
  - [1] Industrial oil palm plantations.
  - [2] Smallholder oil palm plantations.
validation: Contains 17,812 points used to validate the global oil palm extent and age layers. Each point includes:
  - ‘Class’: Assigned by visual interpretation (class values same as extent layer).
  - ‘OP2016-2021’ and ‘OP2019’: Mapped classes in this dataset and the 2019 global oil palm layer (Descals et al., 2021), respectively.

  - **Classes:**
    - [0] Other land covers that are not oil palm.
    - [1] Industrial oil palm plantations.
    - [2] Smallholder oil palm plantations.

*/
var grid_oilpalm = ee.FeatureCollection('projects/sat-io/open-datasets/global-oil-palm/Grid_OilPalm_2021_v1-1');
var globaloilpalm_extent = ee.ImageCollection('projects/sat-io/open-datasets/global-oil-palm/GlobalOilPalm_extent_2021');
var globaloilpalm_yop_2021 = ee.ImageCollection("projects/sat-io/open-datasets/global-oil-palm/GlobalOilPalm_YoP_2021");
var validation = ee.FeatureCollection("projects/sat-io/open-datasets/global-oil-palm/Validation_points_GlobalOP2016-2021_v1-1")
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:/global-landuse-landcover/GLOBAL-OIL-PALM-1990-2021-APP

Earth Engine App: https://ee-globaloilpalm.projects.earthengine.app/view/global-oil-palm-planting-year-1990-2021

#### License
This product is licensed under a Creative Commons Attribution 4.0 International license.

Curated in GEE by: Descals et al 2024 and Samapriya Roy

Keywords: oil palm, planting year, global crop mapping, remote sensing, deep learning, Sentinel-1

Last updated in GEE: 2024-04-28
