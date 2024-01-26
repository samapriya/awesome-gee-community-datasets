# Landfire Mosaics LF

LANDFIRE (LF), Landscape Fire and Resource Management Planning Tools, is a shared program between the wildland fire management programs of the U.S. Department of Agriculture's Forest Service, U.S. Department of the Interior's Geological Survey, and The Nature Conservancy.

LANDFIRE (LF) layers are created using predictive landscape models based on extensive field-referenced data, satellite imagery and biophysical gradient layers using classification and regression trees. You can read [about the Landfire 2022 updates v2.3.0 here](https://landfire.gov/lf_230.php)

The LANDFIRE (LF) 2022 Update represents another step in moving towards an annual update. This update is the first time in LANDFIRE history in which disturbances from the year before are represented in current year products. LF 2022 includes adjustments to vegetation and fuels in disturbed areas for disturbances recorded in 2021 and 2022. LF 2022 disturbance layers contain comprehensive polygon treatment data (disturbance events) obtained from national and local sources and fire program data including:

* Monitoring Trends in Burn Severity (MTBS)
* Burned Area Reflectance Classification (BARC)
* Rapid Assessment of Vegetation Condition after Wildfire (RAVG)

Disturbances are also identified with LF's remote sensing of landscape change (RSLC), which identifies spectral change in vegetation using automated algorithms and image analyst review of the entire country.

Both vegetation cover and height, as well as fuels, will be 2023 capable in disturbed areas. This means that in mapped disturbances, vegetation and fuels represent current year conditions. Transition rulesets for vegetation account for disturbances from 2017 to 2022 since they were designed to use LF 2016 Remap vegetation data as inputs. Fuel updates utilize 2013–2022 disturbances because fuels transition rules encompass ten years of disturbance and can use pre-disturbance fuel inputs.

Important changes featured in the LF 2022 update include:

* Existing Vegetation Type (EVT) Ecological Systems classifications will remain the same as LF 2020, except in areas where agriculture or urban areas have changed
* LF 2022 contains the first application of the "zero to one" Time Since Disturbance (TSD) rules for vegetation height and cover transition rules
    * New rules for the "zero to one" TSD category were developed for surface fuel transitions and are designed to represent the effects of disturbance on fuels for the growing season immediately following the disturbance
* The years represented in Historical Disturbance (HDist) and Fuel Disturbance (FDist) are now the same


![lf_others](https://user-images.githubusercontent.com/6677629/115133292-bc866080-9fcc-11eb-9cd1-286a46c67ad4.gif)

Currently included layers are

#### Earth Engine Snippet: Fire Regime v2.3.0

```js
var sclass = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fire-regime/sclass");
var vcc = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fire-regime/vcc");
var vdep = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fire-regime/vdep");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/LANDFIRE-FIRE-REGIME

#### Earth Engine Snippet: Disturbance 2.3.0

```js
var fdist = ee.ImageCollection("projects/sat-io/open-datasets/landfire/disturbance/FDIST");
var hdist = ee.ImageCollection("projects/sat-io/open-datasets/landfire/disturbance/HDIST");
var distyear = ee.ImageCollection("projects/sat-io/open-datasets/landfire/disturbance/DISTYEAR");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/LANDFIRE-DISTURBANCE

#### Earth Engine Snippet: Topographic 2.2.0

```js
var elevation = ee.ImageCollection("projects/sat-io/open-datasets/landfire/topographic/ELEV");
var aspect = ee.ImageCollection("projects/sat-io/open-datasets/landfire/topographic/ASP");
var slope_degrees = ee.ImageCollection("projects/sat-io/open-datasets/landfire/topographic/SLP");
var slope_perc_rise = ee.ImageCollection("projects/sat-io/open-datasets/landfire/topographic/SlpP");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/LANDFIRE-TOPOGRAPHIC

![topographic](https://user-images.githubusercontent.com/6677629/115172563-249b7c00-a08b-11eb-8fb5-c7603b9cb56f.gif)


#### Earth Engine Snippet: Fuel 2.3.0

```js
var cbd = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/CBD");
var cbh = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/CBH");
var cc = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/CC");
var cffdrs = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/CFFDRS");
var ch = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/CH");
var fbfm13 = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/FBFM13");
var fbfm40 = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/FBFM40");
var fvc = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/FVC");
var fvh = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/FVH");
var fvt = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/FVT");
```

#### Earth Engine Snippet: Fuel 2.2.0

```js
var fccs = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fuel/FCCS");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/LANDFIRE-FUEL

![lf_veg](https://user-images.githubusercontent.com/6677629/115133326-e3449700-9fcc-11eb-81bf-450c622ca166.gif)

#### Earth Engine Snippet: Vegetation 2.3.0

```js
var evc = ee.ImageCollection("projects/sat-io/open-datasets/landfire/vegetation/EVC");
var evh = ee.ImageCollection("projects/sat-io/open-datasets/landfire/vegetation/EVH");
var evt = ee.ImageCollection("projects/sat-io/open-datasets/landfire/vegetation/EVT");
```


Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/LANDFIRE-VEGETATION

#### Earth Engine Snippet: Transportation 2.2.0

```js
var roads = ee.ImageCollection("projects/sat-io/open-datasets/landfire/transportation/ROADS");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/LANDFIRE-TRANSPORTATION

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

Curated in GEE by: Samapriya Roy

Keywords: doi, fire, landfire, nature-conservancy, usda, usgs, vegetation, wildfire

Last updated: 2024-01-14

#### Changelog

* 2024-01-14 Updated to v2.2.3 for available collections
