# United States Groundwater Well Database (USGWD)

Groundwater wells are critical infrastructure that enable the monitoring, extraction, and use of groundwater, which has important implications for
the environment, water security, and economic development. Despite the importance of wells, a unified database collecting and standardizing
information on the characteristics and locations of these wells across the United States has been lacking. To bridge this gap, we have created a
comprehensive database of groundwater well records collected from state and federal agencies, which we call the United States Groundwater Well
Database (USGWD). Presented in both tabular form and as vector points, USGWD comprises over 14.2 million well records with attributes, such as well
purpose, location, depth, and capacity, for wells constructed as far back as 1763 to 2023. Rigorous cross-verification steps have been applied to
ensure the accuracy of the data. The USGWD stands as a valuable tool for improving our understanding of how groundwater is accessed and managed
across various regions and sectors within the United States. You can read the [paper here](https://www.nature.com/articles/s41597-024-03186-3) and
download the [dataset here](https://www.hydroshare.org/resource/8b02895f02c14dd1a749bcc5584a5c55/).

#### Dataset preprocessing

The datasets were provided as state wide extracts and while the 50 state wide extracts were uploaded they were finally merged into a single feature collection for ease of use. While datasets were provided in both geospatial and tabular formats shapefiles are notorious for the property length truncation and size limit of 2GB, so tabular CSV datasets were selected which contained spatial information. However the tabular datasets themselves were has a lot of rows without location information which meant those rows had to be dropped and as such the files were reprocessed to allow us to select only those rows with location information for wells.

#### Citation

```
Lin, CY., Miller, A., Waqar, M. et al. A database of groundwater wells in the United States. Sci Data 11, 335 (2024).
https://doi.org/10.1038/s41597-024-03186-3
```

#### Dataset citation

```
Lin, C., A. Miller, M. Waqar, L. Marston (2024). A Database of Groundwater Wells in the United States, HydroShare,
https://doi.org/10.4211/hs.8b02895f02c14dd1a749bcc5584a5c55
```

![usgwd_features](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/86f8fc7c-5cd4-4a94-9fbf-c01cc7c9653f)

#### Earth Engine Snippet

```js
var usgwd = ee.FeatureCollection("projects/sat-io/open-datasets/USGWD-TABULAR-MERGED")
```

Individual states were also ingested for reference and can be access by the users by using

```js
var usgwd_states = ee.data.listAssets("projects/sat-io/open-datasets/USGWD-TABULAR");

print('Total of '+ee.List(usgwd_states.assets).size().getInfo()+ ' assets in nodes',usgwd_states.assets);
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/US-GROUNDWATER-WELL-DATABASE

#### License

The datasets are provided under a Creative Commons 4.0 International License.

Provided by: Lin, CY., Miller, A., Waqar, M. et al, (2024)

Curated in GEE by: Samapriya Roy

Keywords: USGWD, Groundwater well, Point of diversion, United States, Water infrastructure

Last updated in GEE: 2024-04-17
