# Edge-matched Global, Subnational and operational Boundaries

## Global Edge-matched Subnational Boundaries: Humanitarian Edge Matched
Uses OCHA Common Operational Datasets (COD) when available, falling back to geoBoundaries for regions without coverage. Represents the latest available data for humanitarian operational use. Uses the OpenStreetMap International ADM0 worldview for edge-matching. You can find dataset links in [different formats here](https://data.fieldmaps.io/edge-matched.json)

#### License

The humanitaring edge matched datasets are under a Open Data Commons Open Database License (ODbL) license.

#### Attribution
FieldMaps, OCHA, geoBoundaries, U.S. Department of State, OpenStreetMap

![edge_matched_open](https://user-images.githubusercontent.com/6677629/199188503-e5703654-41d3-48c2-8fde-cfd2cc21132f.gif)


#### Earth Engine Snippet

```js
var adm1 = ee.FeatureCollection("projects/sat-io/open-datasets/field-maps/edge-matched-humanitarian/adm1_polygons");
var adm2 = ee.FeatureCollection("projects/sat-io/open-datasets/field-maps/edge-matched-humanitarian/adm2_polygons");
var adm3 = ee.FeatureCollection("projects/sat-io/open-datasets/field-maps/edge-matched-humanitarian/adm3_polygons");
var adm4 = ee.FeatureCollection("projects/sat-io/open-datasets/field-maps/edge-matched-humanitarian/adm4_polygons");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/HUMANITARIAN-EDGEMATCHED

## Global Edge-matched Subnational Boundaries: Open Edge Matched

Uses geoBoundaries exclusively to ensure all data comes from sources with clearly defined licenses. Suitable for academic or commercial use. Uses the U.S. Geological Survey International ADM0 worldview for edge-matching. You can find dataset links in [different formats here](https://data.fieldmaps.io/edge-matched.json)

#### License

The open datasets are under a Creative Commons Attribution 4.0 International (CC BY 4.0) and any derived work must include attribution.

#### Attribution
FieldMaps, geoBoundaries, U.S. Department of State, U.S. Geological Survey

#### Earth Engine Snippet

```js
var adm1 = ee.FeatureCollection("projects/sat-io/open-datasets/field-maps/edge-matched-open/adm1_polygons");
var adm2 = ee.FeatureCollection("projects/sat-io/open-datasets/field-maps/edge-matched-open/adm2_polygons");
var adm3 = ee.FeatureCollection("projects/sat-io/open-datasets/field-maps/edge-matched-open/adm3_polygons");
var adm4 = ee.FeatureCollection("projects/sat-io/open-datasets/field-maps/edge-matched-open/adm4_polygons");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/OPEN-EDGEMATCHED


#### International ADM0 boundaries

International boundaries are built using either OpenStreetMap or U.S. Geological Survey coastlines. Within each set, ADM0 layers comes in several versions to represent different world views of disputed areas. Starting with the "All" version, areas are dissolved together based on varying international recognition. Only international boundaries were ingested, where the default version, uses OpenStreetMap (download) for coastlines so that it aligns with web maps using OSM for basemaps or other data. Specialty version, uses U.S. Geological Survey (download) for coastlines so that intellectual property and related rights in this dataset are absent.

#### License

The OSM edge matched datasets are under a Open Data Commons Open Database License (ODbL) license while the USGS datasets are under a CC0 or public domain license.

#### Attribution
The OSM datasets have attribution keywords defined such as
FieldMaps, U.S. Department of State, OpenStreetMap

![edge_matched_adm0](https://user-images.githubusercontent.com/6677629/199191574-a0955228-cd30-4ab5-9f23-2e9c2dd0087f.gif)

#### Earth Engine Snippet

```js
var adm0_osm = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/field-maps/OSM_adm0_polygons");
var adm0_usgs = ee.FeatureCollection("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/field-maps/USGS_adm0_polygons");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/AMD0-EDGEMATCHED

## Common Operation dataset Edge Matched

The COD layers are obtained from the Humanitarian Data Exchange at the source URLs below before processed for edge matching. Extended layers can be downloaded and clipped to any ADM0. You can download the dataset in [different formats here](https://data.fieldmaps.io/geoboundaries.json). Datasets were merged to create singular representation at each hierarchy so all ADM1 for example and ADM2 for example. Each component of the dataset retains the original license provided.

#### Earth Engine Snippet

```js
var adm1 = ee.FeatureCollection("projects/sat-io/open-datasets/field-maps/edge-matched-cod/adm1_cod");
var adm2 = ee.FeatureCollection("projects/sat-io/open-datasets/field-maps/edge-matched-cod/adm2_cod");
var adm3 = ee.FeatureCollection("projects/sat-io/open-datasets/field-maps/edge-matched-cod/adm3_cod");
var adm4 = ee.FeatureCollection("projects/sat-io/open-datasets/field-maps/edge-matched-cod/adm4_cod");
```
Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/COD-EDGEMATCHED

## GeoBoundaries Edge matched

The Humanitarian Data Exchange at the source URLs below before processed for edge matching. Extended layers can be downloaded and clipped to any ADM0. You can download the dataset and find license information here[different formats here](https://data.fieldmaps.io/geoboundaries.json). Datasets were merged to create singular representation at each hierarchy so all ADM1 for example and ADM2 for example. Each component of the dataset retains the original license provided.

```js
var adm = ee.FeatureCollection("projects/sat-io/open-datasets/field-maps/edge-matched-geoboundaries/adm1_geoboundaries");
var adm = ee.FeatureCollection("projects/sat-io/open-datasets/field-maps/edge-matched-geoboundaries/adm2_geoboundaries");
var adm = ee.FeatureCollection("projects/sat-io/open-datasets/field-maps/edge-matched-geoboundaries/adm3_geoboundaries");
var adm = ee.FeatureCollection("projects/sat-io/open-datasets/field-maps/edge-matched-geoboundaries/adm4_geoboundaries");
```

sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/GEOBOUNDARIES-EDGEMATCHED

Curated in GEE by : Samapriya Roy

Keywords: FieldMaps, U.S. Department of State, OpenStreetMap,U.S. Geological Survey, geoboundaries

Last updated on GEE: 2022-10-30
