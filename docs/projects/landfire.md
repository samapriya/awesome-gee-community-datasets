# Landfire Mosaics LF v2.0.0

LANDFIRE (LF), Landscape Fire and Resource Management Planning Tools, is a shared program between the wildland fire management programs of the U.S. Department of Agriculture's Forest Service, U.S. Department of the Interior's Geological Survey, and The Nature Conservancy.

LANDFIRE (LF) layers are created using predictive landscape models based on extensive field-referenced data, satellite imagery and biophysical gradient layers using classification and regression trees.

LF Remap is a comprehensive mapping effort that uses recent data to create a new base map product suite that better represents contemporary conditions. LF Remap represents circa 2016 ground conditions and is designed to produce vegetation, disturbance, and fuels products that inform wildland fire and ecological decision systems. LF Remap has improved past methodologies and processes to incorporate current satellite imagery, contemporary data sources, and the latest software and hardware technologies. Final LF Remap products offer significant improvements to all previous LF versions (read more about versions here https://www.landfire.gov/lf_schedule.php). LF Remap products are designed to facilitate national and regional level strategic fire and resource management planning and reporting of management activities. The principal purposes of the products include providing, 1) national level, landscape scale geospatial products to support fire and fuels management planning, and 2) consistent fuels products to support fire planning, analysis, and budgeting to evaluate fire management alternatives. Products are created at a 30 meter raster; however, the applicability of products varies by location and specific use. LF products were designed to support 1) national (all states) strategic planning, 2) regional (single large states or groups of smaller states), and 3) strategic/tactical planning for large sub regional landscapes and Fire Management Units (FMUs) (such as significant portions of states or multiple federal administrative entities). The applicability of LF products to support fire and land management planning on smaller areas will vary by product, location, and specific use. Managers and planners must evaluate LF products according to the scale and requirements specific to their needs.

![lf_others](https://user-images.githubusercontent.com/6677629/115133292-bc866080-9fcc-11eb-9cd1-286a46c67ad4.gif)

Currently included layers are

#### Earth Engine Snippet: Fire Regime

```js
var sclass = ee.ImageCollection("projects/sat-io/open-datasets/landfire/sclass");
var vcc = ee.ImageCollection("projects/sat-io/open-datasets/landfire/vcc");
var vdep = ee.ImageCollection("projects/sat-io/open-datasets/landfire/vdep");
```

#### Earth Engine Snippet: Disturbance

```js
var fdist = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fdist");
```

#### Earth Engine Snippet: Fuel

```js
var ch = ee.ImageCollection("projects/sat-io/open-datasets/landfire/ch");
var cc = ee.ImageCollection("projects/sat-io/open-datasets/landfire/cc");
var cbh = ee.ImageCollection("projects/sat-io/open-datasets/landfire/cbh");
var cbd = ee.ImageCollection("projects/sat-io/open-datasets/landfire/cbd");
var fvc = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fvc");
var fvh = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fvh");
var fvt = ee.ImageCollection("projects/sat-io/open-datasets/landfire/fvt");
```
Sample Code: https://code.earthengine.google.com/76c6cbf1f4c837f48ae6d080b15e1666

![lf_veg](https://user-images.githubusercontent.com/6677629/115133326-e3449700-9fcc-11eb-81bf-450c622ca166.gif)

### Earth Engine Snippet: Vegetation

```js
var bps = ee.ImageCollection("projects/sat-io/open-datasets/landfire/vegetation/bps_v2_0_0");
var evc = ee.ImageCollection("projects/sat-io/open-datasets/landfire/vegetation/evc_v2_0_0");
var evh = ee.ImageCollection("projects/sat-io/open-datasets/landfire/vegetation/evh_v2_0_0");
var evt = ee.ImageCollection("projects/sat-io/open-datasets/landfire/vegetation/evt_v2_0_0");
var nvc = ee.ImageCollection("projects/sat-io/open-datasets/landfire/vegetation/nvc_v2_0_0");
```


Sample Code: https://code.earthengine.google.com/76c6cbf1f4c837f48ae6d080b15e1666

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

Last updated: 2021-04-17
