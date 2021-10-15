### Mississippi River Basin Floodplain Land Use Change (1941-2000)

A comprehensive dataset quantifying floodplain land use change along the 3.3 million km2 Mississippi River Basin (MRB) covering 60 years (1941–2000) at 250-m resolution.

#### Citation

```
Rajib, A., Zheng, Q., Golden, H.E, Wu, Q., Lane, C.R., Christensen, J.R., Morrison, R.R., Annis, A., & Nardi, F.  (2021). The changing face of
floodplains in the Mississippi River Basin detected by a 60-year land use change dataset. _Scientific Data_, 8, 271.
https://doi.org/10.1038/s41597-021-01048-w
```

![](https://i.imgur.com/xf26OdK.png)

#### Earth Engine Snippet

```js

var MRB_boundary = ee.FeatureCollection('users/giswqs/MRB/MRB_Boundary');
var floodplain = ee.Image('users/giswqs/MRB/USGS_Floodplain');
var img_1950 = ee.Image('users/giswqs/MRB/Major_Transitions_1941_1950');
var img_1960 = ee.Image('users/giswqs/MRB/Major_Transitions_1941_1960');
var img_1970 = ee.Image('users/giswqs/MRB/Major_Transitions_1941_1970');
var img_1980 = ee.Image('users/giswqs/MRB/Major_Transitions_1941_1980');
var img_1990 = ee.Image('users/giswqs/MRB/Major_Transitions_1941_1990');
var img_2000 = ee.Image('users/giswqs/MRB/Major_Transitions_1941_2000');

```

Sample Code: https://code.earthengine.google.com/e982f11b610438862eb908e22c2cc088

Earth Engine App: https://giswqs.users.earthengine.app/view/mrb-floodplain

#### License
This dataset is shared under a Creative Commons Attribution-Share Alike 4.0 International License

Provided by: Rajib et al 2021

Curated by: Qiusheng Wu

Keywords: land use, floodplain, Mississippi River Basin, hydrology, river basin, ecysostems

Last updated: October 2021
