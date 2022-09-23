# Landfire Mosaics LF v2.2.0

LANDFIRE (LF), Landscape Fire and Resource Management Planning Tools, is a shared program between the wildland fire management programs of the U.S. Department of Agriculture's Forest Service, U.S. Department of the Interior's Geological Survey, and The Nature Conservancy.

LANDFIRE (LF) layers are created using predictive landscape models based on extensive field-referenced data, satellite imagery and biophysical gradient layers using classification and regression trees. You can read [about the Landfire 2020 updates v2.2.0 here](https://landfire.gov/lf_220.php)

The LF 2020 Update represents the second step in moving towards an annual update in which the disturbances from the year before are represented in current year products. LANDFIRE (LF) 2019L (Limited) was the first step towards this goal but contained limited disturbance information (events and fire program data only) for the years 2017-2019. LF 2020 includes adjustments to vegetation and fuels in disturbed areas for disturbances recorded in 2017-2020. LF 2020 disturbance layers contain events, fire program data (Monitoring Trends in Burn Severity (MTBS), Burned Area Reflectance Classification (BARC), Rapid Assessment of Vegetation Condition after Wildfire (RAVG)) and LF's remote sensing of landscape change (RSLC), which identifies spectral change in vegetation using automated algorithms and image analyst review. See the disturbance source information table.

LF 2020 replaces LF 2019L in terms of disturbances accounted for in vegetation and fuels product layers as it includes all disturbances in LF 2019L plus additional disturbances from 2017-2019 identified by LF's RSLC process and an additional year of full disturbance mapping (2020). Both vegetation cover and height, as well as fuels, will be 2022 capable in disturbed areas. This means that in mapped disturbances, vegetation and fuels are "grown" to current (delivery) year conditions. Transition rulesets for vegetation account for disturbances from 2017-2020 (using LF 2016 Remap vegetation as an input), meaning that no vegetation disturbed prior to LF 2016 Remap will be transitioned from what was mapped at the time. Fuel updates utilize 2012–2020 disturbances because fuels transition rules are based on pre-disturbance fuel inputs, which could pre-date LF 2016 Remap.

There are important changes to ancillary data and classes in the LF 2020 Update, including:

* A complete recalculation of topography based on the most recent 3D Elevation Program (3DEP) data and corrections to aspect that are crucial to fire behavior modeling
* Use of the latest National Land Cover Dataset (NLCD) 2019 data for roads and urban classes and a new separate product layer for roads designed for operational use
* Removal of the developed ruderal classes and the designation of new burnable developed classes based on the Microsoft Building Footprint data and the Wildfire Risk to Communities value added layer
* Removal of the recently disturbed classes, replaced with modeled vegetation
* Adjustment of agricultural classes using the new 2020 cropland data layer (CDL) and transitioning federal agricultural lands to burnable fuels in non-irrigated areas

![lf_others](https://user-images.githubusercontent.com/6677629/115133292-bc866080-9fcc-11eb-9cd1-286a46c67ad4.gif)

Currently included layers are

#### Earth Engine Snippet: Fire Regime v2.0.0

```js
var sclass = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fire-regime/sclass");
var vcc = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fire-regime/vcc");
var vdep = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fire-regime/vdep");
```

Sample Code: https://code.earthengine.google.com/769befc4e306957b0824e3668fbba709

#### Earth Engine Snippet: Disturbance 2.2.0

```js
var fdist = ee.ImageCollection("projects/sat-io/open-datasets/landfire/disturbance/FDIST");
var hdist = ee.ImageCollection("projects/sat-io/open-datasets/landfire/disturbance/HDIST");
var distyear = ee.ImageCollection("projects/sat-io/open-datasets/landfire/disturbance/DISTYEAR");
```

Sample Code: https://code.earthengine.google.com/63b6e1b40d7996cea4efadc371efa573

#### Earth Engine Snippet: Topographic 2.2.0

```js
var elevation = ee.ImageCollection("projects/sat-io/open-datasets/landfire/topographic/ELEV");
var aspect = ee.ImageCollection("projects/sat-io/open-datasets/landfire/topographic/ASP");
var slope_degrees = ee.ImageCollection("projects/sat-io/open-datasets/landfire/topographic/SLP");
var slope_perc_rise = ee.ImageCollection("projects/sat-io/open-datasets/landfire/topographic/SlpP");
```

Sample Code: https://code.earthengine.google.com/3f30203a14f746ba9cbd288affe6e9c0

![topographic](https://user-images.githubusercontent.com/6677629/115172563-249b7c00-a08b-11eb-8fb5-c7603b9cb56f.gif)


#### Earth Engine Snippet: Fuel 2.2.0

```js
var cbd = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/CBD");
var cbh = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/CBH");
var cc = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/CC");
var cffdrs = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/CFFDRS");
var ch = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/CH");
var fbfm13 = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/FBFM13");
var fbfm40 = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/FBFM40");
var fccs = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/FCCS");
var fvc = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/FVC");
var fvh = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/FVH");
var fvt = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/FVT");
```
Sample Code: https://code.earthengine.google.com/79ed0fdc4b116189a01488f666680aa7

![lf_veg](https://user-images.githubusercontent.com/6677629/115133326-e3449700-9fcc-11eb-81bf-450c622ca166.gif)

#### Earth Engine Snippet: Vegetation 2.2.0

```js
var evc = ee.ImageCollection("projects/sat-io/open-datasets/landfire/vegetation/EVC");
var evh = ee.ImageCollection("projects/sat-io/open-datasets/landfire/vegetation/EVH");
var evt = ee.ImageCollection("projects/sat-io/open-datasets/landfire/vegetation/EVT");
```


Sample Code: https://code.earthengine.google.com/ec41730e00de3dc9e50223cbdc886bd3

#### Earth Engine Snippet: Transportation 2.2.0

```js
var roads = ee.ImageCollection("projects/sat-io/open-datasets/landfire/transportation/ROADS");
```

Sample Code: https://code.earthengine.google.com/b378e2ec07797174980fdb8d7a197fc5

Resolution:
approx 30m

#### Citation
LANDFIRE spatial data products

Homepage title: Data product.(Last update). Agency. [Online].Available: URL [Access date].

```
LANDFIRE: LANDFIRE Existing Vegetation Type layer.(2013, June - last update). U.S. Department of Interior, Geological Survey.[Online]. Available: http://landfire.cr.usgs.gov/viewer/ [2013,May 8].
```

#### License
LANDFIRE data are public domain data with no use restrictions, though if modifications or derivatives of the product(s) are created, then please add some descriptive modifier to the data set to avoid confusion.


Curated by: Samapriya Roy

Keywords: doi, fire, landfire, nature-conservancy, usda, usgs, vegetation, wildfire

Last updated: 2022-08-16
