# Sensor-Independent MODIS & VIIRS LAI/FPAR CDR 2000 to 2024

This geospatial dataset encompasses crucial biophysical parameters, namely Leaf Area Index (LAI) and Fraction of Photosynthetically Active Radiation (FPAR), indispensable for characterizing terrestrial ecosystems. The dataset addresses the limitations observed in existing global LAI/FPAR products, including challenges related to spatial-temporal coherence and accuracy.

Drawing from a range of long-term global LAI/FPAR products, including MODIS&VIIRS, this dataset facilitates a comprehensive analysis of vegetation dynamics and their interplay with climate change. Developed as a Sensor-Independent (SI) LAI/FPAR Climate Data Record (CDR), this dataset is derived from Terra-MODIS, Aqua-MODIS, and VIIRS LAI/FPAR standard products.

Encompassing a substantial temporal scope spanning from 2000 to 2024, the SI LAI/FPAR CDR provides valuable insights at various spatial resolutions: 500 meters, 5 kilometers, and 0.05 degrees. Its temporal granularity includes 8-day intervals and bimonthly frequency. To facilitate diverse analyses and applications, this dataset is accessible in both sinusoidal and WGS1984 projections. It represents a comprehensive and refined resource for studying terrestrial ecosystems and their response to climate dynamics. You can read the [paper here](https://essd.copernicus.org/articles/16/15/2024/)

#### Citation

```
Pu, J., Yan, K., Roy, S., Zhu, Z., Rautiainen, M., Knyazikhin, Y., and Myneni, R. B.: Sensor-independent LAI/FPAR CDR:
reconstructing a global sensor-independent climate data record of MODIS and VIIRS LAI/FPAR from 2000 to 2022, Earth Syst. Sci.
Data, 16, 15–34, https://doi.org/10.5194/essd-16-15-2024, 2024
```

#### Dataset citation

```
Pu, J., Roy, S., Knyazikhin, Y., & Myneni, R. (2023). Sensor-Independent LAI/FPAR CDR [Data set]. In Sensor-independent LAI/
FPAR CDR: reconstructing a global sensor-independent climate data record of MODIS and VIIRS LAI/FPAR from 2000 to 2022 (Vol.
16, Number 1, pp. 15–34). Zenodo. https://doi.org/10.5281/zenodo.8076540
```

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

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/LAI-FPAR-2000-2022

#### License

The dataset is under a Creative Commons Attribution 4.0 International.

Provided by: Jiabin et al

Curated in GEE by : Samapriya Roy

keywords: Sensor-Independent, Leaf Area Index (LAI), Fraction of Photosynthetically Active Radiation (FPAR), Climate Dataset Record (CDR)

Last updated on GEE: 2025-12-03

#### Changelog
- added 2023 and 2024 datasets
