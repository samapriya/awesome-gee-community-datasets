# General Bathymetric Chart of the Oceans (GEBCO)

The GEBCO_2021 Grid is the latest global bathymetric product released by the General Bathymetric Chart of the Oceans (GEBCO) and has been developed through the Nippon Foundation-GEBCO Seabed 2030 Project.

The GEBCO_2021 Grid provides global coverage of elevation data in meters on a 15 arc-second grid of 43200 rows x 86400 columns, giving 3,732,480,000 data points. The GEBCO_2021 Grid is a continuous, global terrain model for ocean and land with a spatial resolution of 15 arc seconds. The grid uses as a ‘base’ Version 2 of the SRTM15+ data set (Tozer et al, 2019). This data set is a fusion of land topography with measured and estimated seafloor topography. It is augmented with the gridded bathymetric data sets developed by the four Seabed 2030 Regional Centers. The Regional Centers have compiled gridded bathymetric data sets, largely based on multibeam data, for their areas of responsibility. These regional grids were then provided to the Global Center.

For areas outside of the polar regions (primarily south of 60°N and north of 50°S), these data sets are in the form of 'sparse grids', i.e. only grid cells that contain data were populated. For the polar regions, complete grids were provided due to the complexities of incorporating data held in polar coordinates.

The compilation of the GEBCO_2021 Grid from these regional data grids was carried out at the Global Center, with the aim of producing a seamless global terrain model. The GEBCO_2021 Grid includes data sets from a number of international and national data repositories and regional mapping initiatives. For information on the data sets included in the GEBCO_2021 Grid, please see the [list of contributions included in this release of the grid.](https://www.gebco.net/data_and_products/gridded_bathymetry_data/gebco_2021/)

#### Data Citation & Attribution

```
GEBCO Compilation Group (2021) GEBCO 2021 Grid (doi:10.5285/c6612cbe-50b3-0cff-e053-6c86abc09f8f)
```

![gebco_grids](https://user-images.githubusercontent.com/6677629/115973752-0c10e300-a51d-11eb-8858-16f51762a948.gif)

#### Earth Engine Snippet

```js
var gebco_grid = ee.ImageCollection("projects/sat-io/open-datasets/gebco/gebco_grid");
var gebco_sub_ice_topo = ee.ImageCollection("projects/sat-io/open-datasets/gebco/gebco_sub-ice-topo");
var gebco_tid_grid = ee.ImageCollection("projects/sat-io/open-datasets/gebco/gebco_tid_grid");
```

Sample Code: https://code.earthengine.google.com/c1ddba42c1a75fd43fe0d6a38046e0a4

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

Last updated: 2021-09-29
