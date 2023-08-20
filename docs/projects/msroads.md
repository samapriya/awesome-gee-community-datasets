# Microsoft Bing Global Mined Roads

<div class="result" markdown>

???+ note

    **This dataset is currently only available to those in the [insiders program](https://gee-community-catalog.org/insiders/)**

</div>

Bing Maps is releasing mined roads around the world. We have detected 47.8M km of all roads and 1165K km of roads missing from OSM. Mining is performed with Bing Maps imagery between 2020 and 2022 including Maxar and Airbus. Datasets were provided in tsv formats and additional steps were used to convert them into GEE ready formatting.

#### Data generation details
The road extraction is done in four stages (full drop went through two stages and OSM missing set went through all four)

+ Semantic Segmentation – Recognizing road pixels on the aerial image using Convolutional Neural Network (CNN).
+ Geometry Generation - A series of algorithms and processes transforming output of semantic segmentation into roads in geometry format.
    1. Image postprocessing
    2. Thinning
    3. Connectivity improvement
    4. Graph construction
    5. Finalizing road shapes and network quality
    6. Stiching road geojsons between neighboring images where needed
+ Conflation & Cutting - Excluding roads and parts of roads that already exist in the road network (OSM).
+ Classification - A classifier to filter out low-confidence roads and predict a road type.

You can find [additional information here](https://github.com/microsoft/RoadDetections).

Disclaimer: Whole or parts of the dataset description was provided by the author(s) or their works.

#### Data preprocessing
To get the datasets ready the TSV files were converted to GeoJSON format and then to shapefile splitting up large GeoJSON that would exceed the 4 GB limit for shapefiles. To allow for consistency checks checks were performed to exclude the point datasets that were part of the US data extract but encoded as line strings.The larger datasets like Europe and US were then merged back, flattened and exported into a single GEE asset for ease of use.

#### Citation

```
Microsoft Road Detection - Mined Roads : Last accessed date
```

![msroads_small](https://user-images.githubusercontent.com/6677629/211210802-76ccff90-3b0e-4ed1-bbde-e6a035d752a9.gif)

#### Earth Engine Snippet : Sample

```js
var africa_center = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/MSRoads/Africa/AfricaCenter");
var africa_east = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/MSRoads/Africa/AfricaEast");
var africa_north = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/MSRoads/Africa/AfricaNorth");
var africa_south = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/MSRoads/Africa/AfricaSouth");
var africa_west = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/MSRoads/Africa/AfricaWest");
var america_center = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/MSRoads/AmericaCenter");
var asia_center = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/MSRoads/Asia/AsiaCenter");
var asia_north = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/MSRoads/Asia/AsiaNorth");
var asia_south = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/MSRoads/Asia/AsiaSouth");
var asia_southeast = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/MSRoads/Asia/AsiaSouthEast");
var canada = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/MSRoads/Canada");
var caribbean_islands = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/MSRoads/CaribbeanIslands");
var eu = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/MSRoads/EU");
var middle_east = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/MSRoads/MiddleEast");
var oceania = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/MSRoads/Oceania");
var south_america = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/MSRoads/SouthAmerica");
var united_states = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/MSRoads/US");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/MS-GLOBAL-ROADS


#### License

The datasets are released under the [Open Data Commons Open Database License](https://spdx.org/licenses/ODbL-1.0.html).

Created by: Microsoft

Curated in GEE by: Samapriya Roy

Keywords: Mined Roads, Machine Learning, Classification, linestring, Global roads, OSM

Last updated in GEE: 2022-12-30
