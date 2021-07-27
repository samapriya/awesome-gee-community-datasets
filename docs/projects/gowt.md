# Global offshore wind turbine dataset

This dataset including two contents including the validation datasets, only the location dataset has been ingested and the validation dataset can be downloaded. The location dataset consist of geocoded information on global offshore wind turbines (OWTs) derived from Sentinel-1 synthetic aperture radar (SAR) time-series images from 2015 to 2019. It identified 6,924 wind turbines comprising of more than 10 nations. Data is available at 10 m spatial resolution, providing an explicit dataset for planning, monitoring, and managing marine space. The global OWTs are stored in Shapefile (.shp) format. The attributes and metadata are organized with referenced to the WGS84 datum, and each record consists of seven attributes: centroid latitude (centr_lat), centroid longitude (centr_lon), continent, country, sea area (sea_area), appearance year (occ_year) and month (occ_month).

You can [download both location and validation datasets here](https://figshare.com/articles/dataset/Global_offshore_wind_farm_dataset/13280252/5)

You can read about the [methodology in the paper here](https://www.nature.com/articles/s41597-021-00982-z)

#### Citation

```
Zhang, T., Tian, B., Sengupta, D. et al. Global offshore wind turbine dataset.
Sci Data 8, 191 (2021). https://doi.org/10.1038/s41597-021-00982-z
```

#### Data Citation

```
Zhang, Ting; Tian, Bo; Sengupta, Dhritiraj; Zhang, Lei; Si, Yali (2020):
Global offshore wind turbine dataset. figshare. Dataset.
https://doi.org/10.6084/m9.figshare.13280252.v5
```

![gowt](https://user-images.githubusercontent.com/6677629/127196145-c23773b5-b7fd-4f71-92df-45a3e41b0aaf.gif)

#### Earth Engine Snippet

```js
var gowt = ee.FeatureCollection("projects/sat-io/open-datasets/global_offshore_wind_turbine_v1-3");
```

Sample Code: https://code.earthengine.google.com/d2a2479e7dd57a59f009d7eb19e40f1b

#### License
The dataset is released under a CC0 1.0 Universal (CC0 1.0) Public Domain Dedication. You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.

Created by : Zhang, T., Tian, B., Sengupta, D. et al

Curated in GEE by: Samapriya Roy

Keywords: Offshore energy systems, Coastal engineering, Google Earth Engine Platform, Ocean engineering, Marine planning, Coastal management, Sentinel-1

Last updated : 2021-07-27
