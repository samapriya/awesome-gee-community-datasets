# DeltaDTM Global coastal digital terrain model

DeltaDTM is a global coastal Digital Terrain Model (DTM) with a horizontal spatial resolution of 1 arcsecond (∼30 m) and a vertical mean absolute error (MAE) of 0.43 m overall. It improves upon the accuracy of existing global elevation datasets by correcting Copernicus DEM with spaceborne lidar data from the ICESat-2 and GEDI missions. This correction process involves bias correction, filtering of non-terrain cells (e.g., vegetation and buildings), and gap filling using interpolation. DeltaDTM specifically focuses on low-lying coastal areas (below 10 m above Mean Sea Level) that are particularly vulnerable to sea-level rise, subsidence, and extreme weather events.

DeltaDTM is a valuable resource for a wide range of applications, including coastal management, flood modeling, and adaptation planning. Its improved accuracy enables more precise assessments of coastal flood risks and supports the development of effective mitigation and adaptation strategies. The dataset is freely available in the public domain and can be easily accessed and utilized by researchers, policymakers, and coastal communities. You can read the [paper here](https://www.nature.com/articles/s41597-024-03091-9) and download the [dataset here](https://data.4tu.nl/datasets/1da2e70f-6c4d-4b03-86bd-b53e789cc629).

#### Citation

```
Pronk, M., Hooijer, A., Eilander, D. et al. DeltaDTM: A global coastal digital terrain model. Sci Data 11, 273 (2024).
https://doi.org/10.1038/s41597-024-03091-9
```

#### Dataset Citation

```
Pronk, Maarten (2024): DeltaDTM: A global coastal digital terrain model. Version 3. 4TU.ResearchData. dataset.
https://doi.org/10.4121/21997565.v3
```

![delta_dtm](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/e5d5b074-69cf-42fb-9853-f6b8df457280)

#### Earth Engine Snippet

```js
var delta_dtm = ee.Image("users/maartenpronk/deltadtm/v1-1");
var elevation = delta_dtm.select('b1');
elevation = elevation.updateMask(elevation.neq(30));

//Setup basemaps
var snazzy = require("users/aazuspan/snazzy:styles");
snazzy.addStyle("https://snazzymaps.com/style/132/light-gray", "Grayscale");

var elevationVis = {
  min: 0,
  max: 30.0,
  // cmocean deep
  palette: ["281a2c", "3f396c", "3e6495", "488e9e", "5dbaa4", "a5dfa7", "fdfecc"]
};

Map.setCenter(103, 0, 7);  // South East Asia
Map.addLayer(elevation, elevationVis, 'DeltaDTM');
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:elevation-bathymetry/DELTA-DTM

#### License
DeltaDTM is licensed as CC-BY 4.0. DeltaDTM is produced using Copernicus WorldDEM-30 © DLR e.V. 2010-2014 and © Airbus Defence and Space GmbH 2014-2018 provided under COPERNICUS by the European Union and ESA; all rights reserved.

Created by: Deltares, Pronk, M., Hooijer, A., Eilander, D. et al 2024

Curated in GEE by: Maarten Pronk and Samapriya Roy

Keywords: Altimetry, Digital Elevation Model (DEM), Digital terrain model (DTM), elevation, GEDI, ICESat-2, LiDAR

Last updated in GEE: 2024-11-18
