# High Resolution Tree Species Information for Canada

## Distance-to-second class for the leading tree species map

Distance-to-second class (D2SC) value used as indicator of attribution confidence for the leading tree species map produced from surface reflectance values in a spatially exhaustive, 30-m spatial resolution, Landsat image composite representing year 2019 conditions. Also included in the modeling of species are geographic and climate data, elevation derivatives, and remote sensing derived phenology following the framework described in Hermosilla et al. (2022). Regional classification models were generated based on Canada??s National Forest Inventory using a 150x150 km tiling system. D2SC is computed using the class membership probabilities derived from the first and second most voted classes from the Random Forests models.

## High Resolution Maps of tree species membership likelihood

Tree species maps indicate the class membership probability of all possible classes on a pixel level. The maps are generated using a 2019 Landsat image composite, geographic and climate data, elevation derivatives, and remote sensing derived phenology following the framework described in Hermosilla et al. (2022). Values represent the class membership probabilities derived from the Random Forests votes. Regional classification models were generated based on Canada??s National Forest Inventory (NFI) using a 150x150 km tiling system. The regional classification models utilize and aim to map only the trees species known to be present in a given tiling unit based on the information provided by the NFI.

## High Resolution Map of leading tree species distribution

Leading tree species map produced from a 2019 Landsat image composite, geographic and climate data, elevation derivatives, and remote sensing derived phenology following the framework described in Hermosilla et al. (xxxx). Regional classification models were generated based on Canada??s National Forest Inventory using a 150x150 km tiling system. The leading tree species are defined by representing the most voted tree species from the Random Forests classification models (i.e. the class with the highest class membership probability).

For an overview on the data, image processing, and methods applied, as well as information on independent accuracy assessment of the data, see Hermosilla et al. (2022) https://doi.org/10.1016/j.rse.2022.113276

#### Citation

```
Hermosilla, T., Bastyr, A., Coops, N.C., White, J.C., Wulder, M.A., 2022. Mapping the presence and distribution of tree species in Canada's forested ecosystems. Remote Sensing of Environment 282, 113276.
```

![ca-lead](https://user-images.githubusercontent.com/6677629/195024364-744e72f2-38ec-4cbe-aedf-9482da15e686.gif)

#### Earth Engine Snippet: Distance to Second Class

```js
var D2SC = ee.Image("projects/sat-io/open-datasets/CA_FOREST/DISTANCE2SECOND");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/CA-DISTANCE-2-SECOND-CLASS

#### Earth Engine Snippet: tree species membership likelihood

```js
var membership_likelihood_prob = ee.ImageCollection("projects/sat-io/open-datasets/CA_FOREST/SPECIES_CLASS_MEMBERSHIP_PROBABILITIES");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/CA-SPECIES-CLASS-MEM-PROBABILITIES

#### Earth Engine Snippet: leading tree species

```js
var lead_tree_species = ee.Image("projects/sat-io/open-datasets/CA_FOREST/LEAD_TREE_SPECIES");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/CA-LEAD-TREE-SPECIES

#### License

This work is licensed under and freely available to the [public Open Government Licence - Canada](http://open.canada.ca/en/open-government-licence-canada).

Created by: Hermosilla et al. 2022

Curated in GEE by : Samapriya Roy

keywords: Tree species, Forest inventory, Land cover, Landsat, Machine learning, Classification

Last updated on GEE: 2022-10-11

