# Vermont High Resolution Land Cover 2016

High resolution land cover dataset for Vermont. The primary sources used to derive this land cover layer were 2013-2017 LiDAR data and 2016 NAIP imagery. Ancillary data sources included GIS data provided by the State of Vermont or created by the UVM Spatial Analysis Laboratory. Object-based image analysis techniques (OBIA) were employed to extract land cover information using the best available remotely sensed and vector GIS datasets. OBIA systems work by grouping pixels into meaningful objects based on their spectral and spatial properties, while taking into account boundaries imposed by existing vector datasets. Within the OBIA environment a rule-based expert system was designed to effectively mimic the process of manual image analysis by incorporating the elements of image interpretation (color/tone, texture, pattern, location, size, and shape) into the classification process. A series of morphological procedures were employed to insure that the end product is both accurate and cartographically pleasing. Following the automated OBIA mapping a detailed manual review of the dataset was carried out at a scale of 1:3000 and all observable errors were corrected.


This dataset was developed as part of the Vermont High-Resolution Land Cover. As such, it represents a 'top down' mapping perspective in which tree canopy over hanging other features is assigned to the tree canopy class. At the time of its creation this dataset represents the most detailed and accurate land cover dataset for the area. Eight land cover classes were mapped:

* tree canopy
* grass/shrub
* bare earth
* water
* buildings
* roads
* other paved surfaces
* railroads.

#### Supplemental Information

This assessment and development of methods necessary for its conduct were completed by the University of Vermont's Spatial Analysis Laboratory with funding from the State of Vermont Clean Water Fund, Vermont Agency of Natural Resources, Vermont Agency of Transportation, Lake Champlain Basin Program, and the Vermont Center for Geographic Information (VCGI). Tree canopy assessments have been conducted for numerous communities throughout the U.S. where the results have been instrumental in helping to establishing tree canopy goals.

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

```
University of Vermont Spatial Analysis Laboratory and VT Center for Geographic Information. Vermont High Resolution Land Cover. Accessed [Month
Year] at https://geodata.vermont.gov/pages/land-cover
```

![VT-LC](https://user-images.githubusercontent.com/6677629/173284265-eacfa233-16d6-4256-a90b-c06e6d87a58c.gif)

#### Earth Engine Snippet

```js
var VT_baseLC2016 = ee.Image("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/HRLC/VT_BaseLC_2016");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:regional-landuse-landcover/VT-BASE-LC-2016

#### License

The dataset is released under an assumed CC0 1.0 Universal (CC0 1.0) Public Domain Dedication. VCGI and the State of Vermont make no representations of any kind, including but not limited to the warranties of merchantability or fitness for a particular use, nor are any such warranties to be implied with respect to the data.

Produced by: University of Vermont Spatial Analysis Laboratory, VT Center for Geographic Information

Curated in GEE by: Samapriya Roy

Keywords: Land Use, Land Cover, Urban Watch, Remote Sensing, High Resolution, OBIA

Last updated on GEE: 2022-06-12
