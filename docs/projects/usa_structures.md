# USA Structures

DHS, FIMA, FEMA’s Response Geospatial Office, Oak Ridge National Laboratory, and the U.S. Geological Survey collaborated to build and maintain the nation’s first comprehensive inventory of all structures larger than 450 square feet for use in Flood Insurance Mitigation, Emergency Preparedness and Response. To create the building outline inventory, FEMA, in conjunction with DHS Science and Technology, partnered with the Oak Ridge National Laboratory (ORNL) to extract the outlines via commercially available satellite imagery. You can download [the datasets here](https://gis-fema.hub.arcgis.com/pages/usa-structures) or explore them [using this link](https://fema.maps.arcgis.com/home/item.html?id=0ec8512ad21e4bb987d7e848d14e7e24#overview)

## Dataset Attributes

#### Building Occupancy Types
As of December 2021, the USA Structures dataset includes occupancy type (e.g., Residential, Commercial, Industrial) and primary occupancy type (e.g., Single Family Residential, Restaurant, Hospital) classifications for all structures. The team developed the data using a variety of sources including Census Housing Unit data, HIFLD, LightBox parcel data, and a modeled approach.

#### Universal Unique Identifier (UUID)
In addition to the occupancy type and geometry, each polygon includes an Universally Unique Identifier (UUID) which is a unique ID for each structure across the entire dataset. This allows for connections to individual structures to unique data sources. The data schema is flexible enough to add new data fields and attributes.

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or providers of the dataset and their works.

#### Citation

```
Oak Ridge National Laboratory (ORNL); Federal Emergency Management Agency (FEMA) Geospatial Response Office USA Structures : Last accessed date
```

![usa_str](https://user-images.githubusercontent.com/6677629/204973611-40616859-f006-4a61-9aca-4f1440360313.gif)

#### Earth Engine Snippet : Sample

All datasets are in the format

```js
var state  = ee.FeatureCollection('projects/sat-io/open-datasets/ORNL/USA-STRUCTURES/US_ST_{Two letter abbreviation for US state or territory}');
```

for a list of all US states and territories use this

```js
var ee_folder = ee.data.listAssets("projects/sat-io/open-datasets/ORNL/USA-STRUCTURES");
```

Here are some example setups for two states/territories

```js
var dc = ee.FeatureCollection('projects/sat-io/open-datasets/ORNL/USA-STRUCTURES/USA_ST_DC')
var arizona = ee.FeatureCollection('projects/sat-io/open-datasets/ORNL/USA-STRUCTURES/USA_ST_AZ')

```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/ORNL-US-STRUCTURES

#### License
This work is licensed under a Creative Commons by Attribution (CC BY 4.0) license.

Created by: DHS, FEMA, ORNL

Curated in GEE by: Samapriya Roy

keywords: homeland security, homeland defense, emergency response, structures, building outlines, USA structures, buildings, FEMA, Federal Emergency Management Agency, ORNL, Oak Ridge National Laboratory, federal, industrial, education, assembly, residential, commercial

Last updated in GEE: 2022-12-01
