# RealSAT Global Dataset of Reservoir and Lake Surface Area

RealSAT presents a new global dataset that contains the location and surface area variations of 681,137 lakes and reservoirs larger than 0.1 square kilometers (and south of 50 degree N) from 1984 to 2015, to enable the study of the impact of human actions and climate change on freshwater availability. Within its scope for size and region covered, this dataset is far more comprehensive than existing datasets such as HydroLakes. The static subset of the dataset was ingested rather than timeseries since there was transformation issues however the [dataset can be downloaded here.](https://zenodo.org/record/6468209). A reattempt might be made in the future to ingest the timeseries files.

You can read the paper here : https://www.nature.com/articles/s41597-022-01449-5 and a [viewer is made available to look at an online copy of the data](http://umnlcc.cs.umn.edu/realsat/)

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Citations

```
Khandelwal, A., Karpatne, A., Ravirathinam, P. et al. ReaLSAT, a global dataset of reservoir and lake surface area variations. Sci Data 9, 356
(2022). https://doi.org/10.1038/s41597-022-01449-5
```
‍
![realsat](https://user-images.githubusercontent.com/6677629/182044378-2fc1fa28-71bb-4748-a1a6-d5bd63e41024.gif)

#### Earth Engine Snippet

```js
var realsat = ee.FeatureCollection("projects/sat-io/open-datasets/ReaLSAT/ReaLSAT-1_4");
```
Sample code: https://code.earthengine.google.com/726c44a5b0252c26082064d14844bd01

#### License
The database is licensed under a Creative Commons Attribution (CC-BY) 4.0 International License.

Created by: Khandelwal, A., Karpatne, A., Ravirathinam, P. et al.

Curated in GEE by: Samapriya Roy

Keywords: water,hydrology, lakes, global lake surface, ReaLSAT, Surface water monitoring, Lakes and reservoirs, Hydrology, Landsat

Last updated: 2022-07-10
