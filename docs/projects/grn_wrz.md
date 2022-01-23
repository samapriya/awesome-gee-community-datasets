# Global river networks & Corresponding Water resources zones

River networks and water resources zones (WRZ) are critical for planning, utilization, development, conservation and management of water resources. Currently, the river network and WRZ of world are most obtained based on digital elevation model data automatically, which are not accurate enough, especially in plains. In addition, the WRZ code is inconsistent with the river network. The authors proposed a series of methods and generated a higher resolution and consistent high-precision global river network and corresponding WRZs at level 1 to 4. This dataset provides an important basis and support for reasonable use of water resources and sustainable social development in the world. You can read the [full paper here](https://www.nature.com/articles/s41597-019-0243-y)

Level Categorization for Global River Networks(GRN) and Water Resources Zone(WRZ)

* The river at level 1 (L1 river) refers to the river that flows into the sea or lake.

* The river at level 2 (L2 river) refers to the river that flows into the L1 river, and its confluence area is larger than one hundredth of the L1 river or 10,000 km2.

* The river at level 3 (L3 river) refers to the river that flows into the L2 river, and its confluence area is larger than one hundredth of the L2 river or 1000 km2.

* The river at level 4 (L4 river) refers to the river that flows into the L3 river, and its confluence area is large than one hundredth of the L3 river or 100 km2.

The tributaries that do not satisfy the above conditions were neglected.

The WRZ correspond to River Levels

#### Paper Citation

```
Yan, D., Wang, K., Qin, T. et al. A data set of global river networks and corresponding water resources zones divisions.
Sci Data 6, 219 (2019). https://doi.org/10.1038/s41597-019-0243-y
```

#### Data Citation

```
Yan, Denghua; Wang, Kun; Qin, Tianling; Weng, Baisha; wang, Hao; Bi, Wuxia; et al. (2019): A data set of global river networks and corresponding
water resources zones divisions. figshare. Dataset. https://doi.org/10.6084/m9.figshare.8044184.v6
```

#### Data preprocessing
The river networks are ingested for each continent and as provided by the author. The water resources zone on the other hands were available as level based subsets for each continent so a total of 24 files. To make this accessible as large feature collections Levels across multiple continents were merged into single feature collections.

<center>

|Global River Network          |Levels        |
|------------------------------|--------------|
|Asia                          |Level 1,2,3,4 |
|Africa                        |Level 1,2,3,4 |
|Australia                     |Level 1,2,3,4 |
|Europe                        |Level 1,2,3,4 |
|North America                 |Level 1,2,3,4 |
|South America                 |Level 1,2,3,4 |

|Water Resources Zone          |Levels        |
|------------------------------|--------------|
|Asia                          |Level 1,2,3,4 |
|Africa                        |Level 1,2,3,4 |
|Australia                     |Level 1,2,3,4 |
|Europe                        |Level 1,2,3,4 |
|North America                 |Level 1,2,3,4 |
|South America                 |Level 1,2,3,4 |

|Combined Water Resources Zones|Locations     |
|------------------------------|--------------|
|Level 1                       |All Continents|
|Level 2                       |All Continents|
|Level 3                       |All Continents|
|Level 4                       |All Continents|

</center>

![grn_comp](https://user-images.githubusercontent.com/6677629/150692409-84388d28-aa87-48cb-8603-f290c60677ca.gif)


#### Earth Engine Snippet

```js
var af_river = ee.FeatureCollection("projects/sat-io/open-datasets/GRN/af_river");
var as_river = ee.FeatureCollection("projects/sat-io/open-datasets/GRN/as_river");
var au_river = ee.FeatureCollection("projects/sat-io/open-datasets/GRN/au_river");
var eu_river = ee.FeatureCollection("projects/sat-io/open-datasets/GRN/eu_river");
var na_river = ee.FeatureCollection("projects/sat-io/open-datasets/GRN/na_river");
var sa_river = ee.FeatureCollection("projects/sat-io/open-datasets/GRN/sa_river");
var WRZ_L1 = ee.FeatureCollection("projects/sat-io/open-datasets/WRZ/WRZ_L1");
var WRZ_L2 = ee.FeatureCollection("projects/sat-io/open-datasets/WRZ/WRZ_L2");
var WRZ_L3 = ee.FeatureCollection("projects/sat-io/open-datasets/WRZ/WRZ_L3");
var WRZ_L4 = ee.FeatureCollection("projects/sat-io/open-datasets/WRZ/WRZ_L4");
```

Sample Code: https://code.earthengine.google.com/74a0d0f6991b7bbcf3e66de416b5a24d

#### Data subsets
The Water Resources Zones are also available as level based extracts for each countinent. Use the prefix and the level to get to each feature collection. The format is

**projects/sat-io/open-datasets/WRZ/(Level)/(Prefix)_(Level)**

Here are the prefix list and some examples

<center>

|Country                       |Prefix        |Path                                        |
|------------------------------|--------------|--------------------------------------------|
|Asia                          |as            |projects/sat-io/open-datasets/WRZ/L1/as_wrz1|
|Africa                        |af            |projects/sat-io/open-datasets/WRZ/L2/af_wrz2|
|Australia                     |au            |projects/sat-io/open-datasets/WRZ/L3/au_wrz3|
|Europe                        |eu            |projects/sat-io/open-datasets/WRZ/L4/eu_wrz4|
|North America                 |na            |projects/sat-io/open-datasets/WRZ/L1/na_wrz1|
|South America                 |sa            |projects/sat-io/open-datasets/WRZ/L3/sa_wrz3|

</center>


#### License
This work is distributed under the Creative Commons Attribution 4.0 International License

Created by: Yan, D., Wang, K., Qin, T. et al.

Curated by: Samapriya Roy

Keywords: River networks, Water Resources, Hydrology

Last updated: 2019-09-28
