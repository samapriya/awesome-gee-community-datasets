# Global Channel Belt (GCB)

The Global Channel Belt (GCB) datasets describes the global extent of river channel belts. A two-tier single-threaded (e.g., meandering) versus multi-threaded (e.g., braided) classification is provided showing the likely morphology of the associated active river channel. In addition, the GCB model provides a new global classification of riverine and lacustrine environments based on the mapped extent of the river channel belts.

To read more about the dataset check out the Nature Communications article [here](https://www.nature.com/articles/s41467-023-37852-8). The datasets are also publically available on the Zenodo data repository [here](https://zenodo.org/record/7680163#.ZD_QEnZBw2w).

#### Citation

```
Nyberg, B., Henstra, G., Gawthorpe, R.L. et al. Global scale analysis on the extent of river channel belts. Nat Commun 14, 2163 (2023).
```

#### GCB Datasets

* Band 'Meandering' - % confidence that a pixel is single-threaded (0 to 100%)
* Band 'Braided' - % confidence that a pixel is multi-threaded (0 to 100%)

The combined value of the 'Meandering' and 'Braided' bands yield the confidence of the channel belt extent. The remaining percentage out of a total 100, is the confidence that a pixel is classified as background (or non riverine).

#### Environments Dataset

* Code 1 - Background Value
* Code 2 - Channel Belt
* Code 3 - 36-year river migration
* Code 4 - Active River Channel in 2020
* Code 5 - Wetland/Lacustrine extent in 2020
* Code 6 - Smaller Rivers / Channel Belt Lakes extent in 2020

![GCB](https://user-images.githubusercontent.com/37108459/233066033-12c11409-5cf2-4666-ac69-3e2973a3d8c6.JPG)

#### Earth Engine Snippet

```js
var gcb = ee.Image('projects/sat-io/open-datasets/GCB/GRMM'); // Global Channel Belt Prediction 0 to 100% confidence
var env = ee.Image('projects/sat-io/open-datasets/GCB/Env'); // Global Depositional Environment Classifications
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/GLOBAL-CHANNEL-BELT

For use as a basemap in QGIS or another GIS software use the following XYZ layer links.

```
https://storage.googleapis.com/ge_rivermaps/GRMM/tiles/{z}/{x}/{y}               #GCB Map
https://storage.googleapis.com/ge_rivermaps/riverClasses/tile/{z}/{x}/{y}         #Environments Map
```

#### License
This dataset is available under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/legalcode)

Curated by: Björn Nyberg

Curated in GEE by: Björn Nyberg and Samapriya Roy

Keywords: Rivers, Hydrology, Morphology, Landforms, Ecosystems

Last updated: June 8, 2022
