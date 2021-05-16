# Global Fire Atlas (2003-2016)

The Global Fire Atlas is a new freely available global dataset that tracks the daily dynamics of individual fires to determine the timing and location of ignitions, fire size and duration, and daily expansion, fire line length, speed, and direction of spread. Data are available in easily accessible GIS-layers and can also be explored online here and a detailed description of the underlying methodology is provided by Andela et al. (2019).

The data provide unique insights in the environmental conditions that give rise to the world's most extreme wildfires. The world's largest wildfires were found in sparsely populated arid and semiarid grasslands and shrublands of interior Australia, Africa, and Central Asia. Strikingly, fires of these proportions were nearly absent in similar ecosystems of North and South America, possibly due to higher landscape fragmentation and different management practices, including active fire suppression.

While the world's largest fires occurred in more arid ecosystems, the longest fires burned for over 2 months in seasonal regions of the humid tropics and high-latitude forests. In these sparsely populated high fuel-load systems fires can continuously burn as long as weather conditions are favorable. Abnormal weather conditions often synchronized the occurrence of multiple extreme wildfires across larger regions. Global patterns of fire velocity were reversely related to fuel loads, and the highest fire velocities typically occurred in areas of low fuel loads.


#### Citation

```
Andela, Niels, Douglas C. Morton, Louis Giglio, Ronan Paugam, Yang Chen, Stijn Hantson, Guido R. Werf, and James T. Randerson.
"The Global Fire Atlas of individual fire size, duration, speed and direction." Earth System Science Data 11, no. 2 (2019): 529-552.

```

![gfa](https://user-images.githubusercontent.com/6677629/118379283-ccc73680-b59e-11eb-91b6-a957a8691c91.gif)

#### Earth Engine Snippet

```js
var day_of_burn = ee.ImageCollection("projects/sat-io/open-datasets/global-fire-atlas/day_of_burn");
var fire_direction = ee.ImageCollection("projects/sat-io/open-datasets/global-fire-atlas/fire_direction");
var fire_line = ee.ImageCollection("projects/sat-io/open-datasets/global-fire-atlas/fire_line");
var fire_speed = ee.ImageCollection("projects/sat-io/open-datasets/global-fire-atlas/fire_speed");
```

Sample Code: https://code.earthengine.google.com/20d059ee5819d2fbb7e0de398f70eb90

|Data                       |Location                                                                  |
|:--------------------------|:-------------------------------------------------------------------------|
|Online Webpage             |https://www.globalfiredata.org/fireatlas.html                             |
|User Guide                 |https://glihtdata.gsfc.nasa.gov/files/fire_atlas/Fire_Atlas_user_guide.pdf|
|Overall data hosted by NASA|https://glihtdata.gsfc.nasa.gov/files/fire_atlas/                         |


The shapefiles of ignition locations (point) and fire perimeters (polygon) contain attribute tables with summary information for each individual fire

#### Global Fire Atlas: Earth Engine Snippet

```js
var ignitions_2003 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/ignitions/Global_fire_atlas_V1_ignitions_2003");
var ignitions_2004 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/ignitions/Global_fire_atlas_V1_ignitions_2004");
var ignitions_2005 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/ignitions/Global_fire_atlas_V1_ignitions_2005");
var ignitions_2006 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/ignitions/Global_fire_atlas_V1_ignitions_2006");
var ignitions_2007 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/ignitions/Global_fire_atlas_V1_ignitions_2007");
var ignitions_2008 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/ignitions/Global_fire_atlas_V1_ignitions_2008");
var ignitions_2009 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/ignitions/Global_fire_atlas_V1_ignitions_2009");
var ignitions_2010 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/ignitions/Global_fire_atlas_V1_ignitions_2010");
var ignitions_2011 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/ignitions/Global_fire_atlas_V1_ignitions_2011");
var ignitions_2012 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/ignitions/Global_fire_atlas_V1_ignitions_2012");
var ignitions_2013 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/ignitions/Global_fire_atlas_V1_ignitions_2013");
var ignitions_2014 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/ignitions/Global_fire_atlas_V1_ignitions_2014");
var ignitions_2015 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/ignitions/Global_fire_atlas_V1_ignitions_2015");
var ignitions_2016 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/ignitions/Global_fire_atlas_V1_ignitions_2016");
var perimeter_2003 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/perimeter/Global_fire_atlas_V1_perimeter_2003");
var perimeter_2004 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/perimeter/Global_fire_atlas_V1_perimeter_2004");
var perimeter_2005 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/perimeter/Global_fire_atlas_V1_perimeter_2005");
var perimeter_2006 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/perimeter/Global_fire_atlas_V1_perimeter_2006");
var perimeter_2007 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/perimeter/Global_fire_atlas_V1_perimeter_2007");
var perimeter_2008 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/perimeter/Global_fire_atlas_V1_perimeter_2008");
var perimeter_2009 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/perimeter/Global_fire_atlas_V1_perimeter_2009");
var perimeter_2010 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/perimeter/Global_fire_atlas_V1_perimeter_2010");
var perimeter_2011 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/perimeter/Global_fire_atlas_V1_perimeter_2011");
var perimeter_2012 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/perimeter/Global_fire_atlas_V1_perimeter_2012");
var perimeter_2013 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/perimeter/Global_fire_atlas_V1_perimeter_2013");
var perimeter_2014 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/perimeter/Global_fire_atlas_V1_perimeter_2014");
var perimeter_2015 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/perimeter/Global_fire_atlas_V1_perimeter_2015");
var perimeter_2016 = ee.FeatureCollection("projects/sat-io/open-datasets/global-fire-atlas/perimeter/Global_fire_atlas_V1_perimeter_2016");
```

Sample code: https://code.earthengine.google.com/bfc8e17388e4d003f3ae8fd5753e4f72


|GEE_Property_Name|Property_Name                   |Property_Example|
|:----------------|:-------------------------------|:---------------|
|end_DOY:         |End Day of Year                 |33              |
|end_date:        |End Date                        |2/2/2003        |
|expansion:       |Daily fire expansion (km2 day-1)|0.21            |
|fire_ID:         |Fire_ID                         |226089          |
|fire_line:       |Daily Fire Line                 |0.46            |
|lat:             |Latitude                        |39.8896         |
|lon:             |Longitude                       |-0.3178         |
|perimeter:       |Perimeter (km)                  |1.85            |
|size:            |Size(km2)                       |0.21            |
|speed:           |Speed (km day-1)                |0.46            |
|start_DOY:       |Start Day of Year               |33              |
|start_date:      |Start Date                      |2/2/2003        |
|tile_ID:         |Tile_ID                         |h17v05          |


#### License & Usage

This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Curated by: Samapriya Roy

Keywords: Human Dimensions, Natural Hazards, Wild Fires, Burned Area, Biosphere, Ecological Dynamics, Fire Ecology, Fire Dynamics, Fire Occurrence

Contact details & Created by: Niels Andela (niels.andela@nasa.gov)

Last updated: 2019-04-24
