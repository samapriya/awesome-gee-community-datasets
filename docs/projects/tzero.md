# TransitionZero Solar Asset Mapper

TransitionZero's Solar Asset Mapper is a global, satellite-derived dataset of utility-scale solar farms, created through a combination of machine
learning and human annotation. The Q1 2024 dataset includes the location and shape of 63,616 assets, along with their estimated capacities.
Construction dates are estimated for over 80% of these assets. This dataset covers over 19,100 square kilometers of solar farms across 183
countries, with a total estimated capacity of 711 GW.

This dataset represents the most comprehensive view of global asset-level solar installations, combining TransitionZero's detections with known solar farm geometries from other datasets. By integrating data from various sources, it provides a detailed and reliable picture of the current state of utility-scale solar farms worldwide.The data can be [downloaded here](https://zenodo.org/records/11368204)

#### Dataset Preprocessing
The dataset fields constructed_before and constructed_after was converted to system:time_start and system:time_end for easy filtering. Nulls are kept as nulls for both of those columns.

* cluster_id: ID of the corresponding item in the analysis-level dataset
* capacity_mw: estimated capacity of the asset in megawatts
* constructed_before: upper bound for construction date (estimated date of the image in which the solar plant was first seen in a constructed state)
* constructed_after: lower bound for construction date (estimated date of the image in which construction began for the solar plant)

#### Citation

Please refer to the suggested citation formats

```
"TransitionZero Solar Asset Mapper, TransitionZero, May 2024 release."
"TZ-SAM, TransitionZero, May 2024 release."
"TransitionZero (2024) Solar Asset Mapper."
```

#### Dataset Citation

```
Phillpott, M., O'Connor, J., Ferreira, A., Max, S., Kruitwagen, L., & Guzzardi, M. (2024). Solar Asset Mapper: A continuously-updated global
inventory of solar energy facilities built with satellite data and machine learning (1.0) [Data set].
Zenodo. https://doi.org/10.5281/zenodo.11368204
```

![tz_solar](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/4075631c-9068-4d4c-bc8b-a288083d4d01)

#### Earth Engine Snippet

```
var tzero_solar = ee.FeatureCollection("projects/sat-io/open-datasets/TZERO/TZ-SOLAR-2024Q1");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/TZERO-GLOBAL-SOLAR-MAPPER

#### License
TZ-SAM is made available under a Creative Commons Attribution Non-Commercial 4.0 International License (CC-BY-NC-4.0). Attribution to TransitionZero is required. You must also clearly indicate if you have made any changes to the TZ-SAM dataset and what these are.

Keywords: solar energy, energy transition, open data

Provided by; Transition Zero

Curated in GEE by: Samapriya Roy

Last updated in GEE: 2024-06-01
