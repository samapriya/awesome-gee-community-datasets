# Sensor-Independent LAI/FPAR CDR 2000 to 2022

<div class="result" markdown>

???+ note

    **This dataset is part of a paper in submission and as such does not have citation and DOI information. This will be updated as the paper progresses through review and publication cycles.**

</div>

This geospatial dataset encompasses crucial biophysical parameters, namely Leaf Area Index (LAI) and Fraction of Photosynthetically Active Radiation (FPAR), indispensable for characterizing terrestrial ecosystems. The dataset addresses the limitations observed in existing global LAI/FPAR products, including challenges related to spatial-temporal coherence and accuracy.

Drawing from a range of long-term global LAI/FPAR products, including MODIS&VIIRS, this dataset facilitates a comprehensive analysis of vegetation dynamics and their interplay with climate change. Developed as a Sensor-Independent (SI) LAI/FPAR Climate Data Record (CDR), this dataset is derived from Terra-MODIS, Aqua-MODIS, and VIIRS LAI/FPAR standard products.

Encompassing a substantial temporal scope spanning from 2000 to 2022, the SI LAI/FPAR CDR provides valuable insights at various spatial resolutions: 500 meters, 5 kilometers, and 0.05 degrees. Its temporal granularity includes 8-day intervals and bimonthly frequency. To facilitate diverse analyses and applications, this dataset is accessible in both sinusoidal and WGS1984 projections. It represents a comprehensive and refined resource for studying terrestrial ecosystems and their response to climate dynamics.

![lai_fpar](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/28942045-9429-41a9-8836-9f398bac50ec)

#### Earth Engine Snippet

```js
var wgs_500m_8d = ee.ImageCollection("projects/sat-io/open-datasets/BU_LAI_FPAR/wgs_500m_8d");
var wgs_5km_8d = ee.ImageCollection("projects/sat-io/open-datasets/BU_LAI_FPAR/wgs_5km_8d");
var wgs_005degree_8d = ee.ImageCollection("projects/sat-io/open-datasets/BU_LAI_FPAR/wgs_005degree_8d");
var wgs_500m_bimonthly = ee.ImageCollection("projects/sat-io/open-datasets/BU_LAI_FPAR/wgs_500m_bimonthly");
var wgs_5km_bimonthly = ee.ImageCollection("projects/sat-io/open-datasets/BU_LAI_FPAR/wgs_5km_bimonthly");
var wgs_005degree_bimonthly = ee.ImageCollection("projects/sat-io/open-datasets/BU_LAI_FPAR/wgs_005degree_bimonthly");
```

Sample Code: https://code.earthengine.google.com/d3b5bab6889b842e3dadea918fd525bd

#### License

The dataset is under a Creative Commons Attribution 4.0 International.

Provided by: Jiabin et al

Curated in GEE by : Samapriya Roy

keywords: Sensor-Independent, Leaf Area Index (LAI), Fraction of Photosynthetically Active Radiation (FPAR), Climate Dataset Record (CDR)

Last updated on GEE: 2023-06-09
