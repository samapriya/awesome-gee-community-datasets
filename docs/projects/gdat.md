# Global Dam Tracker (GDAT) Database

The Global Dam Tracker (GDAT) is one of the most comprehensive geo-referenced global dam databases, encompassing over 35,000 dams worldwide. It includes accurate geo-coordinates, satellite-derived catchment areas, and detailed attribute information such as completion year, dam height, length, purpose, and installed capacity. GDAT is built upon existing global datasets and enriched with regional data from governments, non-profits, and academic sources, especially in the Global South, which often lacks detailed coverage. The dataset is designed for inter-temporal analysis, allowing users to assess the environmental and socioeconomic impacts of dam construction over the past three decades, particularly focusing on changes in global surface water coverage. You can find the [paper here](https://www.nature.com/articles/s41597-023-02008-2) and the dataset repository on [Zenodo](https://doi.org/10.5281/zenodo.6784716).

#### Citation

```
Zhang, Alice Tianbo, and Vincent Xinyi Gu. "Global Dam Tracker: A database of more than 35,000 dams with location, catchment, and attribute information."
Scientific data 10, no. 1 (2023): 111.
```

#### Dataset Citation

```
Zhang, A. T., & Gu, V. X. (2023). Global Dam Tracker: A database of more than 35,000 dams with location, catchment, and attribute information [Data set].
In Scientific Data (Version v1, Vol. 10, Number 1, p. 111). Zenodo. https://doi.org/10.5281/zenodo.7616852
```

![gdat](https://github.com/user-attachments/assets/8faa4c66-6ba3-4b9f-ae95-f265ff120dfc)

#### Earth Engine Snippet

```js
var gdat_catchments = ee.FeatureCollection("projects/sat-io/open-datasets/GDAT/GDAT_V1_CATCHMENTS");
var gdat_dams = ee.FeatureCollection("projects/sat-io/open-datasets/GDAT/GDAT_V1_DAMS");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:/hydrology/GLOBAL-DAM-TRACKER

#### License Information
The dataset is available under a Creative Commons 4.0 International License.

Provided by: Zhang et al. 2023

Curated in GEE by: Samapriya Roy

Keywords: River Barriers, Reservoirs, Hydropower Dams, Water Storage, Flood Control, Aquatic Ecosystems

Last updated: 2024-10-27
