# MAXAR Open Data Events: Multispectral

Pre and post event high-resolution satellite imagery in support of emergency planning, risk assessment, monitoring of staging areas and emergency response, damage assessment, and recovery. These images are generated using the Maxar ARD pipeline, tiled on an organized grid in analysis-ready cloud-optimized formats. New data is released in response to activations. Older data may be migrated to the ARD format as needed. You can find [additional details and datasets here](https://www.maxar.com/open-data)

#### Preprocessing

The metadata tags were parsed from the existing metadata json files and available properties were parsed to confirm to property names for GEE. The datetime property was added as system:time_start for easy filtering of datasets. Not all datasets have been added and this will be continuously updated to include additional datasets/disasters

#### Citation

```
Maxar Open Data Program was accessed on DATE from [url].
```

![maxar_opendata](https://user-images.githubusercontent.com/6677629/198897620-2714ab7d-89db-4885-95c2-0ede5602b3d5.gif)


#### Earth Engine Snippet

```js
var afghanistan_earthquake_2022 = ee.ImageCollection("projects/sat-io/open-datasets/MAXAR-OPENDATA/afghanistan_earthquake_2022");
var gambia_flooding_2022 = ee.ImageCollection("projects/sat-io/open-datasets/MAXAR-OPENDATA/gambia_flooding_2022");
var hurricane_fiona_2022 = ee.ImageCollection("projects/sat-io/open-datasets/MAXAR-OPENDATA/hurricane_fiona_2022");
var hurriance_ian_2022 = ee.ImageCollection("projects/sat-io/open-datasets/MAXAR-OPENDATA/hurricane_ian_2022");
var kentucky_flooding_2022  = ee.ImageCollection("projects/sat-io/open-datasets/MAXAR-OPENDATA/kentucky_flooding_2022");
var pakistan_flooding_2022 = ee.ImageCollection("projects/sat-io/open-datasets/MAXAR-OPENDATA/pakistan_flooding_2022");
var southafrica_flooding_2022 = ee.ImageCollection("projects/sat-io/open-datasets/MAXAR-OPENDATA/southafrica_flooding_2022");
var sudan_flooding_2022 = ee.ImageCollection("projects/sat-io/open-datasets/MAXAR-OPENDATA/sudan_flooding_2022");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-events-layers/MAXAR-OPENDATA-MS

#### License

This work is licensed under [Creative Commons Attribution Non Commercial 4.0](https://creativecommons.org/licenses/by-nc/4.0/).

Data provided by: MAXAR

Curated in GEE by : Samapriya Roy

Keywords: disaster, maxar, high resolution, flooding, hurriance, earthquake

Last updated on GEE: 2022-10-30
