#  NAFD Forest Disturbance History 1986-2010

The North American Forest Dynamics (NAFD) products provided in this data set consist of 25 annual and two time-integrated forest disturbance maps for the conterminous United States (CONUS) derived from Landsat images for the period 1986-2010. Each annual map has classified pixels showing water, no forest cover, forest cover, no data available (data gaps) in present year, and forest disturbances that occurred in that year. The time-integrated maps are similarly classified, but over the entire 1986-2010 period with the first and last forest disturbance years identified and provided as separate maps.

Maps have a nominal spatial resolution of 30 m, with forest disturbances mapped at an annual time step . These products are referred to as the NAFD-NEX data set to acknowledge the collaboration with the supercomputing facilities at the NASA Ames Research Center provided by the NASA Earth Exchange (NEX: Nemani et al. 2011) to process the large volume of Landsat imagery used in this study. You can find details about the dataset [including the  Vegetation Change Tracker (VCT) algorithm here](https://daac.ornl.gov/NACP/guides/NAFD-NEX_Forest_Disturbance.html)

#### Data structure

The North American Forest Dynamics (NAFD) products provided in this data set consist of 25 annual and two time-integrated forest disturbance maps for the conterminous United States (CONUS) derived from Landsat images for the period 1986-2010. Each annual map has classified pixels showing water, no forest cover, forest cover, no data available (data gaps) in present year, and forest disturbances that occurred in that year. The time-integrated maps are similarly classified, but over the entire 1986-2010 period with the first and last forest disturbance years identified and provided as separate maps.

Maps have a nominal spatial resolution of 30 m, with forest disturbances mapped at an annual time step (Fig. 1). These products are referred to as the NAFD-NEX data set to acknowledge the collaboration with the supercomputing facilities at the NASA Ames Research Center provided by the NASA Earth Exchange (NEX: Nemani et al. 2011) to process the large volume of Landsat imagery used in this study.

#### Data File Naming

The annual forest disturbance map GeoTIFF files are named as follows:  VCT_Annual_30m_YYYY.tif

* VCT_ refers to the Vegetation Change Tracker, an automated forest change analysis algorithm (Huang et al. 2010) used to process the Landsat images.
* Annual_30m_ denotes annual disturbance maps at 30 m resolution.
* YYYY is the year Landsat images were analyzed for disturbances, beginning in 1986 through 2010. Twenty-five total files.
For example, VCT_Annual_30m_1986.tif

The two time-integrated forest disturbance GeoTIFF maps are named VCT_30m_first.tif and VCT_30m_last.tif.

* VCT_ refers to the Vegetation Change Tracker, an automated forest change analysis algorithm (Huang et al. 2010) used to process the Landsat images.
* 30m_ denotes the map has 30 m resolution.
* “first” and “last” indicate that one map shows the year when a first disturbance was detected for a pixel and the second map noting the last disturbance.

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Data Citation

```
Goward, S.N., C. Huang, F. Zhao, K. Schleeweis, K. Rishmawi, M. Lindsey, J.L. Dungan, and A. Michaelis. 2016. NACP NAFD Project:
Forest Disturbance History from Landsat, 1986-2010. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1290
```

![nafd_vct](https://user-images.githubusercontent.com/6677629/188573561-edf5191b-ed33-491e-b898-596cc2a01083.gif)

#### Earth Engine Snippet


```js
var nafd_annual = ee.ImageCollection("projects/sat-io/open-datasets/NAFD/vct_annual");
var nafd_first = ee.Image("projects/sat-io/open-datasets/NAFD/VCT_30m_first");
var nafd_last = ee.Image("projects/sat-io/open-datasets/NAFD/VCT_30m_last");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/NAFD-FOREST-DISTURBANCE

#### License

This work is licensed under a CC0 1.0 Universal (CC0 1.0) Public Domain Dedication license.

Created by: Goward, S.N., C. Huang, F. Zhao, K. Schleeweis, K. Rishmawi, M. Lindsey, J.L. Dungan, and A. Michaelis

Curated in GEE by : Samapriya Roy

keywords: NAFD, Forest Dynamics, NAFD-NEX, Landsat

Last modified: 2016-03-03

Last updated on GEE: 2022-09-05
