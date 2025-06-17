# TransitionZero Solar Asset Mapper

TransitionZero's Solar Asset Mapper (TZ-SAM) is a global, satellite-derived dataset of utility-scale solar energy facilities (facilities with capacity exceeding 500kW), created through a combination of machine learning and human annotation. The Q4 2024 dataset contains the location and geometry of 94,099 assets, along with estimated nominal generating capacities. Construction dates are estimated for over 80% of these assets. The dataset contains 23,157 square kilometers of solar energy facilities across 183 countries, with a total estimated nominal generating capacity of 711 GW.

This dataset provides the most complete, asset-level view of solar installations globally, combining TransitionZero's novel detections with known solar farm geometries from other datasets. The data includes both an analysis-ready dataset with geometries, capacities and construction dates, as well as raw polygon data that exposes the underlying sources. The data can be [downloaded here](https://www.transitionzero.org/products/solar-asset-mapper/download)

#### Available Datasets

The TZ-SAM data is provided as four files:

- **Analysis Polygons (Full Geometry)**: The primary "analysis-ready" dataset containing complete geometries, capacity estimates, and construction date estimates.

- **Analysis Polygons (Centroid)**: A lightweight version of the analysis dataset containing central latitude and longitude coordinates instead of full geometries.

- **Raw Polygons (Full Geometry)**: Contains the original source geometries, their origins, and mapping to the clustered polygons in the analysis dataset.

- **Raw Polygons (Centroid)**: A centroid-only version of the raw polygons dataset, providing source information with simplified geometry representation.


#### Dataset Fields
The dataset includes the following key fields:

- cluster_id: Unique ID for the clustered asset
- capacity_mw: Estimated capacity of the asset in megawatts (MW)
- constructed_before: Upper bound for construction date (estimated date of image showing constructed state)
- constructed_after: Lower bound for construction date (estimated date showing start of construction)
- geometry: Polygon or MultiPolygon defining the asset
- latitude/longitude: Coordinates of the asset centroid
- country: Administrative country name

#### Methods
The dataset is developed through a combination of machine learning algorithms and satellite data to identify solar facilities and estimate their generating capacities. Construction dates for facilities built after 2017 are determined using quarterly time series predictions. Extensive training data, including OpenStreetMap annotations and validated detections, contribute to the accuracy of the dataset. To ensure data quality, manual validation is performed alongside automated processes. Additionally, capacity estimation models are employed to account for country-specific factors, refining the accuracy of the reported nominal generating capacities.

#### Citation

Please use one of these suggested citation formats:

```
"TransitionZero Solar Asset Mapper, TransitionZero,  2024 release." "TZ-SAM, TransitionZero, May 2024 release."
"TransitionZero (2024) Solar Asset Mapper."
```


![tz_solar](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/4075631c-9068-4d4c-bc8b-a288083d4d01)

#### Earth Engine Snippet

```js
var tzero_solar_analysis = ee.FeatureCollection("projects/sat-io/open-datasets/TZERO/TZ-SOLAR-2025Q1_ANALYSIS_POLYGONS");
var tzero_solar_analysis_centroid = ee.FeatureCollection("projects/sat-io/open-datasets/TZERO/TZ-SOLAR-2025Q1_ANALYSIS_POLYGONS_CENTROID");
var tzero_solar_raw = ee.FeatureCollection("projects/sat-io/open-datasets/TZERO/TZ-SOLAR-2025Q1_RAW_POLYGONS");
var tzero_solar_raw_centroid = ee.FeatureCollection("projects/sat-io/open-datasets/TZERO/TZ-SOLAR-2025Q1_RAW_POLYGONS_CENTROID");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/TZERO-GLOBAL-SOLAR-MAPPER

#### License
TZ-SAM is made available under a Creative Commons Attribution Non-Commercial 4.0 International License (CC-BY-NC-4.0). Attribution to TransitionZero is required. You must also clearly indicate if you have made any changes to the TZ-SAM dataset and what these are.

Keywords: solar energy, energy transition, open data

Provided by: Transition Zero

Curated in GEE by: Samapriya Roy

Last updated in GEE: 2025-02-04
