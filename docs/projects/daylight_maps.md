# Daylight Map Distribution map data

Daylight is a complete distribution of global, open map data that’s freely available with support from community and professional mapmakers. We combine the work of global contributors to projects like OpenStreetMap with quality and consistency checks from Daylight mapping partners to create a free, stable, and easy-to-use street-scale global map. Daylight Map Distribution will include a new dataset consisting of vectorized landcover features derived from the European Space Agency’s 2020 World Cover (10m) rasters. This dataset provides global coverage and is suitable for use in maps up to 1:1 million (zoom level 8).

#### Dataset structure
Dataset releases are created by the team periodically and will be ingested accordingly into the GEE collection.

#### Attribution

```
* © OpenStreetMap contributors available under the Open Database License (www.openstreetmap.org/copyright)
* Building data © OpenStreetMap contributors, Microsoft, Esri Community Maps contributors
* Australia Building Footprints (github.com/microsoft/AustraliaBuildingFootprints)
* Canadian Building Footprints (github.com/microsoft/CanadianBuildingFootprints)
* Uganda/Tanzania Building Footprints (github.com/microsoft/Uganda-Tanzania-Building-Footprints)
* US Building Footprints (github.com/microsoft/USBuildingFootprints)
```

![daylight_small](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/41a023c4-e104-41b2-aced-8e0f65e96883)

#### Earth Engine snippet

```js
var water_polygons = ee.FeatureCollection("projects/sat-io/open-datasets/DAYLIGHTMAP/water_polygons");
var land_polygons = ee.FeatureCollection("projects/sat-io/open-datasets/DAYLIGHTMAP/land_polygons");
```
Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/DAYLIGHT-LAND-WATER-POLY

Landcover layer: ESA 2020

```js
var landcover = ee.FeatureCollection("projects/sat-io/open-datasets/DAYLIGHTMAP/LANDCOVER_ESA_2020");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/DAYLIGHT-LANDCOVER

#### License

Daylight Map Distribution is open data, licensed under the Open Data Commons Open Database License (ODbL). Daylight is built from upstream sources, primarily from OpenStreetMap contributors with optional additions from Esri Community Maps Contributors and Microsoft Corporation.

Provided by: Daylight Map Distribution

Curated in GEE by: Samapriya Roy

Keywords: Daylight Map Distribution, landcover, land polygons, water polygons, OSM, OpenStreetMap

Last updated in GEE: 2023-10-20
