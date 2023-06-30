# Global maps of habitat types

We provide a global, spatially explicit characterization of terrestrial and marine habitat types, as defined in the International Union for Conservation of Nature (IUCN) habitat classification scheme, which is widely used in ecological analyses, including for quantifying species’ Area of Habitat. We produced this novel habitat map for the years 2015-2019 by creating a global decision tree that intersects the best currently available global data on elevation and bathymetry, land and ocean cover, climate and land use.

#### Citation

```
Jung, M., Dahal, P.R., Butchart, S.H.M. et al. A global map of terrestrial habitat types.
Sci Data 7, 256 (2020). https://doi.org/10.1038/s41597-020-00599-8
```

![Habitat map](https://raw.githubusercontent.com/Martin-Jung/Habitatmapping/master/screen_lvl2.png)

#### Earth Engine Snippet

```js
// Level 1 and level 2 for the year 2015
var lvl1 = ee.Image("projects/sat-io/open-datasets/IUCN_HABITAT/iucn_habitatclassification_composite_lvl1_ver004")
var lvl2 = ee.Image("projects/sat-io/open-datasets/IUCN_HABITAT/iucn_habitatclassification_composite_lvl2_ver004")

// Note: Colour code is random
Map.addLayer(lvl2.randomVisualizer(),{},'Habitat Classification Level 1')

// Changemask for later.
// Replace year in folder and mask to get a different year (for years 2016-2019)
//for example 2017 would be var change2017_lvl1 = ee.Image("projects/sat-io/open-datasets/IUCN_HABITAT/changemasks/iucn_habitatclassification_2017changemask_lvl1_ver004")
var change2019_lvl1 = ee.Image("projects/sat-io/open-datasets/IUCN_HABITAT/changemasks/iucn_habitatclassification_2019changemask_lvl1_ver004").select('comp2019').unmask(0)
var change2019_lvl2 = ee.Image("projects/sat-io/open-datasets/IUCN_HABITAT/changemasks/iucn_habitatclassification_2019changemask_lvl2_ver004").select('comp2019').unmask(0)
print(change2019_lvl1)

//Level 1 and level 2 for the year 2019
var lvl12019 = change2019_lvl1.firstNonZero(lvl1)
var lvl22019 = change2019_lvl2.firstNonZero(lvl2)

Map.addLayer(lvl12019.randomVisualizer(),{},'Level 1 2019')
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:geophysical-biological-biogeochemical/GLOBAL-HABITAT-TYPES

Extra Info:
Code to reproduce the maps can be found [here](https://github.com/Martin-Jung/Habitatmapping) and be visualized [here](https://uploads.users.earthengine.app/view/habitat-types-map). Default Maps are for the year 2015. Change maps are also available for later years (2016-2019) based on Copernicus only. Note that provided changemasks are cumulative (e.g. the year 2019 includes changes up to 2019). They can be used to `updateMask` the 2015 image.

#### Repository for download:
https://zenodo.org/record/4058819

#### Source Code for dataset
[https://github.com/Martin-Jung/Habitatmapping](https://github.com/Martin-Jung/Habitatmapping)

Created by : Jung, M., Dahal, P.R., Butchart, S.H.M. et al

Curated by: Martin Jung

Keywords: Global habitats, Ecosystems, Integrated map, IUCN, Biodiversity, Species

Last updated: 2020-09-01
