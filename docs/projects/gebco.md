# General Bathymetric Chart of the Oceans (GEBCO)

The GEBCO_2023 Grid is a global terrain model for ocean and land, providing elevation data in meters on a 15 arc-second interval grid. This means that the grid has a spatial resolution of about 1 kilometer at the equator. The data values are pixel-center registered, meaning that they refer to the elevation at the center of each grid cell.

The grid is accompanied by a Type Identifier (TID) Grid, which provides information on the types of source data that the GEBCO_2023 Grid is based on. The primary GEBCO_2023 grid contains land and ice surface elevation information. A version is also made available with under-ice topography/bathymetry information for Greenland and Antarctica.

The GEBCO_2023 Grid was published in April 2023 and is the fifth GEBCO grid developed through the Nippon Foundation-GEBCO Seabed 2030 Project. This is a collaborative project between the Nippon Foundation of Japan and GEBCO, which aims to bring together all available bathymetric data to produce the definitive map of the world ocean floor and make it available to all. The GEBCO_2023 Grid is a valuable resource for a variety of applications, including oceanography, geology, marine biology, climate change research, and disaster management.For information on the data sets included in the GEBCO_2021 Grid, please see the [list of contributions included in this release of the grid.](https://www.gebco.net/data_and_products/gridded_bathymetry_data/)

#### Data Citation & Attribution

```
GEBCO Compilation Group (2023) GEBCO 2023 Grid (doi:10.5285/f98b053b-0cbc-6c23-e053-6c86abc0af7b)
```

![gebco_grids](https://user-images.githubusercontent.com/6677629/115973752-0c10e300-a51d-11eb-8858-16f51762a948.gif)

#### Earth Engine Snippet

```js
var gebco_grid = ee.ImageCollection("projects/sat-io/open-datasets/gebco/gebco_grid");
var gebco_sub_ice_topo = ee.ImageCollection("projects/sat-io/open-datasets/gebco/gebco_sub-ice-topo");
var gebco_tid_grid = ee.ImageCollection("projects/sat-io/open-datasets/gebco/gebco_tid_grid");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:elevation-bathymetry/GEBCO

#### GEBCO Type Identifier (TID) grid coding

|TID                  |Definition                                                                                                                                                                                                     |
|:-------------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
|0                    |Land                                                                                                                                                                                                           |
|**Direct measurements**  |                                                                                                                                                                                                               |
|10                   |Singlebeam - depth value collected by a single beam echo-sounder                                                                                                                                               |
|11                   |Multibeam - depth value collected by a multibeam echo-sounder                                                                                                                                                  |
|12                   |Seismic - depth value collected by seismic methods                                                                                                                                                             |
|13                   |Isolated sounding - depth value that is not part of a regular survey or trackline                                                                                                                              |
|14                   |ENC sounding - depth value extracted from an Electronic Navigation Chart (ENC)                                                                                                                                 |
|15                   |Lidar - depth derived from a bathymetric lidar sensor                                                                                                                                                          |
|16                   |Depth measured by optical light sensor                                                                                                                                                                         |
|17                   |Combination of direct measurement methods                                                                                                                                                                      |
|**Indirect measurements**|                                                                                                                                                                                                               |
|40                   |Predicted based on satellite-derived gravity data - depth value is an interpolated value guided by satellite-derived gravity data                                                                              |
|41                   |Interpolated based on a computer algorithm - depth value is an interpolated value based on a computer algorithm (e.g. Generic Mapping Tools)                                                                   |
|42                   |Digital bathymetric contours from charts - depth value taken from a bathymetric contour data set                                                                                                               |
|43                   |Digital bathymetric contours from ENCs - depth value taken from bathymetric contours from an Electronic Navigation Chart (ENC)                                                                                 |
|44                   |Bathymetric sounding - depth value at this location is constrained by bathymetric sounding(s) within a gridded data set where interpolation between sounding points is guided by satellite-derived gravity data|
|45                   |Predicted based on helicopter/flight-derived gravity data                                                                                                                                                      |
|**Unknown**              |                                                                                                                                                                                                               |
|70                   |Pre-generated grid - depth value is taken from a pre-generated grid that is based on mixed source data types, e.g. single beam, multibeam, interpolation etc.                                                  |
|71                   |Unknown source - depth value from an unknown source                                                                                                                                                            |
|72                   |Steering points - depth value used to constrain the grid in areas of poor data coverage                                                                                                                        |

#### License
The GEBCO Grid is placed in the public domain and may be used free of charge. Use of the GEBCO Grid indicates that the user accepts the conditions of use and disclaimer information given below. Users are free to: Copy, publish, distribute and transmit The GEBCO Grid. Adapt The GEBCO Grid. Commercially exploit The GEBCO Grid, by, for example, combining it with other information, or by including it in their own product or application.

Produced by : General Bathymetric Chart of the Oceans (GEBCO), Nippon Foundation-GEBCO Seabed 2030 Project

Curated by: Samapriya Roy

Keywords: :"Nippon Foundation-GEBCO Seabed 2030 Project, GEBCO, General Bathymetric Chart of the Oceans, Bathymetry , Elevation"

Last updated: 2023-08-28
