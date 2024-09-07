# Global Peatland Database

The Global Peatland Map 2.0, launched by the **Global Peatlands Initiative** partners at the Global Peatland Pavilion during UNFCCC COP26, enhances our understanding of the location and extent of peatlands worldwide. This dataset integrates data on location, extent, and drainage status of peatlands and organic soils globally, covering 268 countries and regions. It combines external data with mapping contributions from the **Greifswald Mire Centre**, providing a composite map of global peatlands, organic soils, and proxy data. The dataset supports map production, statistics, and analysis for the **Global Peatland Assessment 2022**.

You can download [Global Peatland Map 2.0 here](https://nextcloud.uni-greifswald.de/index.php/s/s7Ln5QKxdQG5aaA) and additional information about [about Global Peatland Database can be found here](https://greifswaldmoor.de/global-peatland-database-en.html)

#### Dataset Characteristics

| **Property**        | **Value**                          |
|---------------------|------------------------------------|
| **Format**          | GeoTiff                            |
| **Projection**      | WGS 84                             |
| **Pixel Values**    | 1 = peat dominated, 2 = peat in soil mosaic |
| **Spatial Resolution** | 1x1 km                           |

#### Citation

```
Greifswald Mire Centre (2022). Global Peatland Map 2.0. Underlying dataset of the UNEP Global Peatland Assessment - The State of the World’s Peatlands: Evidence for action toward the conservation, restoration, and sustainable management of peatlands, Global Peatlands Initiative, United Nations Environment Programme, Nairobi.
```

![Global Peatland Map 2.0](https://github.com/samapriya/awesome-gee-community-datasets/assets/57500332/7f290701-c159-4bee-8d1c-4c856fefba54)

#### Earth Engine Snippet (Indonesia Example)
```js
// Load administrative boundaries for Indonesia
var admin1 = ee.FeatureCollection("projects/sat-io/open-datasets/geoboundaries/HPSCGS-ADM1");
var geometry = admin1.filter(ee.Filter.eq('shapeGroup', 'IDN'));

Map.centerObject(geometry, 4);
Map.setOptions("Hybrid");

var peat = ee.Image("projects/sat-io/open-datasets/GLOBAL-PEATLAND-DATABASE")
    .clip(geometry)
    .unmask();

// Display the results
Map.addLayer(peat.clip(geometry),
  {min: 0, max: 1, palette: ['#f7fcf5', '#c7e9c0', '#74c476', '#238b45', '#00441b']},
  'Peatland Distribution', true
  );
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/GLOBAL-PEATLAND-FRACTIONAL-COVER

#### License
This dataset is made available under a Creative Commons NonCommercial-ShareAlike 4.0 International.

#### Keywords
peatland, wetland, organic soil, soil carbon, ecosystem

Provided by: Greifswald Mire Centre (2022)

Curated in GEE by: Ka Hei and Samapriya Roy

Last updated in GEE: 2024-07-14
