# Global Leaf trait estimates for land modelling

At the organismal level, **plant traits**, which **are measurable morphological, anatomical, physiological, and phenological characteristics**, can
influence individuals' establishment, fitness, and survival. These measurable characteristics provide essential information to **explain long-term**
(e.g., annual) **patterns underlying carbon, water, energy fluxes, and biodiversity globally**. We provide the only global remotely sensed-based
maps of leaf traits at 1km spatial resolution. In particular, we present global maps of **specific leaf area (SLA), leaf dry matter content (LDMC),
leaf nitrogen content per dry mass (LNC), and leaf phosphorus content per dry mass (LPC)**. The methodology combines MODIS and Landsat data,
climatological data (Worldclim), the largest traits database (TRY), and machine learning algorithms.

The following figure shows a flowchart of the methodology for providing our traits estimates. The numbered boxes indicate the three main components
of the methods: (1) gap filling the traits database; (2) calculating the community weighted mean (CWM) trait values at the canopy level for [MODIS](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/modis) pixels with nearby trait observations; and (3) spatialization of CWMs to
global trait maps at 500 m resolution.

<img src="https://user-images.githubusercontent.com/49197052/206223378-5ff7624f-2ded-4211-9bb5-1c3c313a5c77.png " width="700">


The full information about the methodology can be found [here](https://doi.org/10.1016/j.rse.2018.09.006).
The users can also explore the dataset in GEE with the following [app](https://almoma153.users.earthengine.app/view/global-trait-maps-with-gee).

The data is also available at two spatial resolutions, 3km and 1km. It can be downloaded from these links [1](https://www.try-db.org/TryWeb/Data.
php#59), [2](https://www.try-db.org/TryWeb/Data.php#60).

#### Additional Information about v3
Version 3.0 of the processing chain prevents extrapolation and uses an updated categorical trait table. To prevent extrapolations, this updated
version of the processing chain uses the random forest algorithm (RF) with surrogates for the estimation of trait values. RF with surrogates allows
obtaining an ensemble of models inside the convex hull of the input data for the predictions. Additionally, the use of an updated and more extensive
categorical trait table allowed increasing the amount of training samples to produce the maps.

#### Citation

```
Moreno-Martínez, Á., Camps-Valls, G., Kattge, J., Robinson, N., Reichstein, M., Bodegom, P. V., Kramer, K., Cornelissen, J. H. C., Reich, P. B.,
Bahn, M., Niinemets, Ü., Peñuelas, J., Craine, J., Cerabolini, B., Minden, V., Laughlin, D. C., Sack, L., Allred, B., Baraloto, C., Byun, C.,
Soudzilovskaia, N. A., Running, S. W. (2018). A methodology to derive global maps of leaf traits using remote sensing and climate data.
Remote Sensing of Environment, 218, 69-88. [doi](https://doi.org/10.1016/j.rse.2018.09.006)
```

![image](https://user-images.githubusercontent.com/49197052/206224734-0aa2feb6-ca7f-4ec9-8ac5-71cfa557af29.png)

#### Earth Engine Snippet

```js
// SLA (mm2/g)
var SLA=ee.Image('projects/sat-io/open-datasets/GLOBAL-LEAF-TRAITS/SLA_1km_v3').select([0],['SLA']);
var SLA_SD = ee.Image('projects/sat-io/open-datasets/GLOBAL-LEAF-TRAITS/SLA_sd_1km_v3').select([0],['SLA_sd']);

// LNC (mg/g)
var LNC=ee.Image('projects/sat-io/open-datasets/GLOBAL-LEAF-TRAITS/LNC_1km_v3').select([0],['LNC']);
var LNC_SD = ee.Image('projects/sat-io/open-datasets/GLOBAL-LEAF-TRAITS/LNC_sd_1km_v3').select([0],['LNC_sd']);

// LPC (mg/g)
var LPC=ee.Image('projects/sat-io/open-datasets/GLOBAL-LEAF-TRAITS/LPC_1km_v3').select([0],['LPC']);
var LPC_SD=ee.Image('projects/sat-io/open-datasets/GLOBAL-LEAF-TRAITS/LPC_sd_1km_v3').select([0],['LPC_sd']);

// Leaf dry matter content LDMC (g/g)
var LDMC=ee.Image('projects/sat-io/open-datasets/GLOBAL-LEAF-TRAITS/LDMC_1km_v3').select([0],['LDMC']);
var LDMC_SD = ee.Image('projects/sat-io/open-datasets/GLOBAL-LEAF-TRAITS/LDMC_sd_1km_v3').select([0],['LDMC_sd']);

//let's mask unprocessed data (Positive values correspond with natural vegetated areas)
SLA = SLA.mask(SLA.gt(0));
LNC = LNC.mask(LNC.gt(0));
LPC = LPC.mask(LPC.gt(0));
LDMC = LDMC.mask(LDMC.gt(0));

var vis_vi = {min:7 , max: 22, palette: ["ffffd9", "edf8b1", "c7e9b4", "7fcdbb", "41b6c4", "1d91c0", "225ea8", "253494", "081d58"]};
Map.addLayer(SLA, vis_vi,  'SLA (mm2 / g)',true)
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/GLOBAL-LEAF-TRAITS

#### License
This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any
medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link
to the license, and indicate if changes were made.

#### Contact information
If you have any further questions or doubts, please don't hesitate to contact [us](mailto:alvaro.moreno@uv.es).

Curated by: Alvaro Moreno-Martínez, Gustau Camps-Valls, Jens Kattge, Nathaniel Robinson, Markus Reichstein, Peter van Bodegom, Josep Peñuelas, Brady Allred, Steve W. Running

Curated copy in GEE by: Samapriya Roy

Keywords: Plant traits, Machine learning, Remote sensing, Plant ecology, Climate, MODIS, Landsat

Last updated: Nov 2021

Last updated in GEE: 2022-12-18
