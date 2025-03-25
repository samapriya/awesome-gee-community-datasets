# Landfire Mosaics LF

LANDFIRE (LF), Landscape Fire and Resource Management Planning Tools, is a shared program between the wildland fire management programs of the U.S. Department of Agriculture's Forest Service, U.S. Department of the Interior's Geological Survey, and The Nature Conservancy.

LANDFIRE (LF) layers are created using predictive landscape models based on extensive field-referenced data, satellite imagery and biophysical gradient layers using classification and regression trees. You can read [about the Landfire 2023 updates here](https://landfire.gov/data/lf2023)

#### LANDFIRE 2023 Update

The LANDFIRE 2023 Update (LF 2023) represents the final step in the ongoing goal to move towards annual updates and reduced latency. Similar to the LF 2022 Update, in LF 2023, disturbances from the previous year are represented in current year products. This means the LANDFIRE team has improved production efficiencies and can turn around disturbances faster than ever, providing the newest data faster to users.

#### LF 2023 Products and Descriptions

??? example "Expand to show theme, product and abbreviations"

    <center>

    | Theme | Product Name | Abbreviation |
    |-------|-------------|--------------|
    | **Disturbance** | Limited Disturbance | LDIST |
    | | Preliminary Annual Disturbance | PDIST |
    | | 2023 Annual Disturbance | DIST |
    | | Historical Disturbance | HDIST |
    | | Fuel Disturbance | FDist |
    | **Historic Fire Regime** | Fire Regime Groups | FRG |
    | | Fire Return Interval | FRI |
    | | Percent Fire Severity | PFS |
    | **Fuel** | 13 Anderson Fire Behavior Fuel Models | FBFM13 |
    | | 40 Scott and Burgan Fire Behavior Fuel Models | FBFM40 |
    | | Forest Canopy Bulk Density | CBD |
    | | Forest Canopy Base Height | CBH |
    | | Forest Canopy Cover | CC |
    | | Forest Canopy Height | CH |
    | | Canadian Forest Fire Danger Rating System | CFFDRS |
    | | Operational Roads | Roads |
    | | Fuel Vegetation Cover | FVC |
    | | Fuel Vegetation Height | FVH |
    | | Fuel Vegetation Type | FVT |
    | | Fuel Rulesets Database | FRDB |
    | | Fuel Characteristic Classification System Fuelbeds | FCCS |
    | **Reference** | Public Events Geodatabase | EventsDB |
    | | Public Exotics Geodatabase | ExoticsDB |
    | | Public Model Ready Events Geodatabase | ModelReadyDB |
    | **Vegetation** | Biophysical Settings | BPS |
    | | Existing Vegetation Type | EVT |
    | | Existing Vegetation Cover | EVC |
    | | Existing Vegetation Height | EVH |
    | | Succession Classes | SClass |
    | | Vegetation Condition Class | VCC |
    | | Vegetation Departure Index | VDep |

#### Improvements Featured in the LF 2023 Update

??? example "Improvements were made to these layers and you can find the category and improvements information below."

    <center>

    | Category | Improvement |
    |----------|-------------|
    | Imagery | Use of 4 seasonal composites in disturbance mapping, doubling satellite imagery usage |
    | Coverage | Mapped disturbance events in the 90km buffer area surrounding CONUS |
    | Products | Two new types of Annual Disturbance products – Limited and Preliminary Annual Disturbance |
    | Calibration | New fuels calibration for the Southeast GeoArea, Colorado, and Oklahoma |
    | Infrastructure | Updated Operational Roads product for CONUS incorporating NLCD 2021 |
    | Fire Regime | Return of FRG, FRI, and PFS as standalone products |
    | Alaska Products | Updated BPS, FRG, FRI, and PFS products for AK |
    | Fuel Classification | Updated FCCS product for all extents |
    | Methodology | New approach for Existing Vegetation Cover (EVC), Height (EVH), and Type (EVT) within CONUS |

#### New Disturbance Products in LF 2023

To provide sooner delivery of LANDFIRE Annual Disturbance data and ensure a more complete record, LANDFIRE now distributes three Annual Disturbance Products, Limited, Preliminary and Final.

??? example "Expand to see Disturbance products in a single version"

    <center>

    | Product | Abbreviation | Description | Features |
    |---------|--------------|-------------|----------|
    | **Limited Annual Disturbance** | LDist | First cut of landscape change information | • Supports time-sensitive updates<br>• Does not include satellite change detection<br>• Does not provide image-based severity for contributed events<br>• Includes fire program perimeters and burn severity where available |
    | **Preliminary Annual Disturbance** | PDist | Second "draft" of landscape change information | • Released by geographic area<br>• Includes disturbance events from regional sources<br>• Includes LANDFIRE satellite change detection<br>• Includes image-based severity<br>• Used to update Vegetation and Fuel products |
    | **Annual Disturbance** | Dist | "Final" draft of Annual Disturbance data | • Includes additional fires and disturbance events<br>• Harvested from second "pull" of national online sources<br>• Included in the Public Events Geodatabase |

#### New Vegetation Modeling Approach

For LF 2023, LANDFIRE maps the lifeform, cover, and height of existing vegetation in areas that have been mapped as disturbed over the last twenty years using machine learning methods. This is a change from previous updates that relied on millions of rulesets developed from local and national experts.


![lf_others](https://user-images.githubusercontent.com/6677629/115133292-bc866080-9fcc-11eb-9cd1-286a46c67ad4.gif)

Currently included layers are

#### Earth Engine Snippet: Disturbance 2.4.0

```js
// LANDFIRE Disturbance Layers
var dist = ee.ImageCollection("projects/sat-io/open-datasets/landfire/DISTURBANCE/DIST");
var hdist = ee.ImageCollection("projects/sat-io/open-datasets/landfire/DISTURBANCE/HDIST");
var ldist = ee.ImageCollection("projects/sat-io/open-datasets/landfire/DISTURBANCE/LDIST");
var pdist = ee.ImageCollection("projects/sat-io/open-datasets/landfire/DISTURBANCE/PDIST");

```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/LANDFIRE-DISTURBANCE

#### Earth Engine Snippet FIRE REGIME:  v2.4.0

```js
// LANDFIRE Fire Regime Collections
var frg = ee.ImageCollection("projects/sat-io/open-datasets/landfire/FIRE-REGIME/FRG");
var fri = ee.ImageCollection("projects/sat-io/open-datasets/landfire/FIRE-REGIME/FRI");
var pfs = ee.ImageCollection("projects/sat-io/open-datasets/landfire/FIRE-REGIME/PFS");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/LANDFIRE-FIRE-REGIME


#### Earth Engine Snippet: Fuel 2.4.0

```js
// Landfire FUEL Layers
var cbd = ee.ImageCollection("projects/sat-io/open-datasets/landfire/FUEL/CBD");
var cbh = ee.ImageCollection("projects/sat-io/open-datasets/landfire/FUEL/CBH");
var cc = ee.ImageCollection("projects/sat-io/open-datasets/landfire/FUEL/CC");
var cffdrs = ee.ImageCollection("projects/sat-io/open-datasets/landfire/FUEL/CFFDRS");
var ch = ee.ImageCollection("projects/sat-io/open-datasets/landfire/FUEL/CH");
var fbfm13 = ee.ImageCollection("projects/sat-io/open-datasets/landfire/FUEL/FBFM13");
var fbfm40 = ee.ImageCollection("projects/sat-io/open-datasets/landfire/FUEL/FBFM40");
var fccs = ee.ImageCollection("projects/sat-io/open-datasets/landfire/FUEL/FCCS");
var fdist = ee.ImageCollection("projects/sat-io/open-datasets/landfire/FUEL/FDIST");
var fvc = ee.ImageCollection("projects/sat-io/open-datasets/landfire/FUEL/FVC");
var fvh = ee.ImageCollection("projects/sat-io/open-datasets/landfire/FUEL/FVH");
var fvt = ee.ImageCollection("projects/sat-io/open-datasets/landfire/FUEL/FVT");
var roads = ee.ImageCollection("projects/sat-io/open-datasets/landfire/FUEL/ROADS");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/LANDFIRE-FUEL

![lf_veg](https://user-images.githubusercontent.com/6677629/115133326-e3449700-9fcc-11eb-81bf-450c622ca166.gif)

#### Earth Engine Snippet: Vegetation 2.4.0

```js
// LANDFIRE Vegetation Collections
var bps = ee.ImageCollection("projects/sat-io/open-datasets/landfire/VEGETATION/BPS");
var evc = ee.ImageCollection("projects/sat-io/open-datasets/landfire/VEGETATION/EVC");
var evh = ee.ImageCollection("projects/sat-io/open-datasets/landfire/VEGETATION/EVH");
var evt = ee.ImageCollection("projects/sat-io/open-datasets/landfire/VEGETATION/EVT");
var sclass = ee.ImageCollection("projects/sat-io/open-datasets/landfire/VEGETATION/SCLASS");
var vcc = ee.ImageCollection("projects/sat-io/open-datasets/landfire/VEGETATION/VCC");
var vdep = ee.ImageCollection("projects/sat-io/open-datasets/landfire/VEGETATION/VDEP");
```


Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/LANDFIRE-VEGETATION

#### Earth Engine Snippet: Topography 2.3.0

```js
// LANDFIRE Vegetation Collections
var slpp = ee.ImageCollection("projects/sat-io/open-datasets/landfire/TOPOGRAPHY/SLPP");
var slpd = ee.ImageCollection("projects/sat-io/open-datasets/landfire/TOPOGRAPHY/SLPD");
var elev = ee.ImageCollection("projects/sat-io/open-datasets/landfire/TOPOGRAPHY/ELEV");
var asp = ee.ImageCollection("projects/sat-io/open-datasets/landfire/TOPOGRAPHY/ASP");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/LANDFIRE-VEGETATION


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

Last updated: 2025-03-16

#### Changelog

* 2025-03-16 Updated to v2.4.0 for available collections
* 2024-01-14 Updated to v2.2.3 for available collections
