# Global Intra-Urban Land Use

This dataset provides land use maps for the year 2020 for all 4,000+ cities and metropolitan areas in the world with populations exceeding 100,000.
The resulting product is the first freely available, global intra-urban land use maps at 5-meter resolution. The data includes a 4-tier land use
taxonomy which at its root distinguishes open-space from built-up area. At the second tier, it subdivides the built-up category into nonresidential
and residential areas. The third tier distinguishes formal from informal residential land use, and the fourth tier further subdivides formal and
informal residential land uses into more detailed categories. Results of a separate road/street classification model based on the same methods are
also provided. You can read more [in the paper here](https://doi.org/10.1016/j.compenvurbsys.2022.101917)

#### Citation

```
Guzder-Williams, Brookie, Eric Mackres, Shlomo Angel, Alejandro M. Blei, and Patrick Lamson-Hall. "Intra-urban land use maps for a global sample of
cities from Sentinel-2 satellite imagery and computer vision." Computers, Environment and Urban Systems 100 (2023): 101917.
```

![intra_urban_small](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/8e1491c0-882b-4908-8a01-8f8609db3eac)

#### Earth Engine Snippet

```js
var ULU = ee.ImageCollection('projects/wri-datalab/cities/urban_land_use/V1')

// Define classes and set color parameters.
var CLASSES_7=[
  "open_space",
  "nonresidential",
  "atomistic",
  "informal_subdivision",
  "formal_subdivision",
  "housing_project",
  "road"]
var COLORS_7=[
  '33A02C',
  'E31A1C',
  'FB9A99',
  'FFFF99',
  '1F78B4',
  'A6CEE3',
  'bdbdbd']
var CLASSES=CLASSES_7
var colors=COLORS_7
var ULU7Params = {bands: ['lulc'], min: 0, max: 6, opacity: 1, palette: colors};

// Generate image of 6-class land use from the highest probability class at each pixel.
var ULUimage = ULU.select('lulc').reduce(ee.Reducer.firstNonNull()).rename('lulc')
ULUimage=ULUimage.mask(ULUimage.mask().gt(0))

// Generate image of road areas based on a pixels with greater than 50% probability of being road.
var roadsImage = ULU.select('road').reduce(ee.Reducer.firstNonNull()).rename('lulc')
var roadProb = 50
var roadsMask = roadsImage.updateMask(roadsImage.gt(roadProb)).where(roadsImage, 1)

// Composite 6-class land use and roads into as single image.
var ULUandRoads = ULUimage.where(roadsMask,6).select('lulc')

// Map both the 6-class land use and composite images.
Map.addLayer(ULUimage, ULU7Params, 'Intra-urban land use, 6-class (2020)');
Map.addLayer(ULUandRoads, ULU7Params, 'Intra-urban land use, 7-class (2020)');
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/GLOBAL-INTRA-URBAN-LANDUSE

#### License

The dataset is provided under a [Creative Commons BY-4.0 license](https://creativecommons.org/licenses/by/4.0/)

Keywords: Urban land use maps; Land use land cover; Sentinel-2; Neural networks; Computer vision; Supervised classification; Google Earth Engine; Informal settlements

Provided by: WRI

Curated in GEE by: WRI

Last updated in GEE: 2023-05-29
