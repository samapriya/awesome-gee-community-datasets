# Global Soil bioclimatic variables

Research in global change ecology relies heavily on global climatic grids derived from estimates of air temperature in open areas at around 2 m above the ground. These climatic grids do not reflect conditions below vegetation canopies and near the ground surface, where critical ecosystem functions occur and most terrestrial species reside. Here, we provide global maps of soil temperature and bioclimatic variables at a 1-km2 resolution for 0–5 and 5–15 cm soil depth. These maps were created by calculating the difference (i.e. offset) between in situ soil temperature measurements, based on time series from over 1200 1-km2 pixels (summarized from 8519 unique temperature sensors) across all the world's major terrestrial biomes, and coarse-grained air temperature estimates from ERA5-Land (an atmospheric reanalysis by the European Centre for Medium-Range Weather Forecasts).

#### Citation

```
Lembrechts, Jonas J., Johan van den Hoogen, Juha Aalto, Michael B. Ashcroft, Pieter De Frenne, Julia Kemppinen, Martin Kopecký et al. "Global maps
of soil temperature." Global Change Biology 28, no. 9 (2022): 3110-3144.
```

![gcb16060-fig-0003-m](https://user-images.githubusercontent.com/37101570/217479710-77c0aecc-782b-45d8-91e8-430f42e4a2a1.png)

#### Earth Engine Snippet
```js
var SBIO_0_5cm = ee.Image("projects/crowtherlab/soil_bioclim/SBIO_v2_0_5cm")
var SBIO_5_15cm = ee.Image("projects/crowtherlab/soil_bioclim/SBIO_v2_5_15cm")
```

#### Code snippet

```js
// Load image
var SBIO_0_5cm = ee.Image('projects/crowtherlab/soil_bioclim/SBIO_v2_0_5cm')

// Print bandNames
print(SBIO_0_5cm.bandNames())

// Add to map
Map.addLayer(SBIO_0_5cm.select('SBIO1_Annual_Mean_Temperature'),
             {min: -10, max: 30, palette: ["2166AC", "4393C3", "92C5DE", "D1E5F0", "FDDBC7", "F4A582", "D6604D", "B2182B"]},
             'SBIO1_Annual_Mean_Temperature')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:soil-properties/SOIL-BIOCLIM

Extra Info: Each of the 11 soil bioclims is available for two soil depths: 0-5 cm and 5-15cm.

#### License
Creative Commons Attribution 4.0 International License

Curated by: Jonas Lembrechts & Johan van den Hoogen

Keywords: Bioclim, soil, soil temperature, climate

Last updated: 2022-10-02
