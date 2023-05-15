# Global Forest Canopy Height from GEDI & Landsat

A new, 30-m spatial resolution global forest canopy height map was developed through the integration of the Global Ecosystem Dynamics Investigation (GEDI) lidar forest structure measurements and Landsat analysis-ready data time-series. The NASA GEDI is a spaceborne lidar instrument operating onboard the International Space Station since April 2019. It provides footprint-based measurements of vegetation structure, including forest canopy height between 52°N and 52°S globally. The Global Land Analysis and Discover team at the University of Maryland (UMD GLAD) integrated the GEDI data available to date (April-October 2019) with the year 2019 Landsat analysis-ready time-series data (Landsat ARD). The GEDI RH95 (relative height at 95%) metric was used to calibrate the model. The Landsat multi-temporal metrics that represent the surface phenology serve as the independent variables for global forest height modeling. The “moving window” locally calibrated and applied bagged regression tree ensemble model was implemented to ensure high quality of forest height prediction and global map consistency. The model was extrapolated in the boreal regions (beyond the GLAD data range) to create the global forest height prototype map.

The global forest height map is a prototype product that has known issues related to GEDI data quality and Landsat optical time-series data availability and feasibility of characterizing forest structure. GEDI data overestimate forest height on slopes within temperate and subtropical mountain grasslands, e.g. in New Zealand and Lesotho. Tree height over cities and suburbs may be confounded with building height, as GEDI data do not discriminate between the height of vegetation and man-made objects. The GEDI calibration uncertainties (specifically, geolocation precision and land surface height estimation) may be responsible for some of the map errors. The forest height model saturated above 30m and does not adequately represent the height of the tallest trees. The global product will be updated in the future to address most of the issues. The newly processed GEDI data will include refinements to land surface detection algorithms, an urban mask, and improved geolocation. Planned integration of higher spatial resolution Sentinel-2 data will allow the implementation of texture metrics. Application of advanced machine learning tools (namely, convolution neural networks) will be tested to improve forest height modeling accuracy.

Map data within the GEDI data range provided in the geographic coordinates using the WGS84 reference system. 8-bit unsigned LZW-compressed GeoTiff. Pixel size is 0.00025 x 0.00025 degree. Data aggregated into continental mosaics which can [be downloaded here](https://glad.umd.edu/dataset/gedi/). Pixel values:  0-60 Forest canopy height, meters, 101 Water, 102 Snow/ice ,103 No data

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Citation

```
P. Potapov, X. Li, A. Hernandez-Serna, A. Tyukavina, M.C. Hansen, A. Kommareddy, A. Pickens, S. Turubanova, H. Tang, C. E. Silva, J. Armston, R.
Dubayah, J. B. Blair, M. Hofton (2020). https://doi.org/10.1016/j.rse.2020.112165
```

![forest_canopy_ht_small](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/9d40f361-24c8-4e88-9601-1e568b987ed8)


#### Earth Engine snippet

```js
var gf = ee.ImageCollection("projects/sat-io/open-datasets/GLAD/GEDI_V27");
var gbf = ee.ImageCollection("projects/sat-io/open-datasets/GLAD/GEDI_V25_Boreal");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/GLOBAL-FOREST-CANOPY-HT-GEDI-LANDSAT

Earth Engine app: http://glad.earthengine.app/view/global-forest-canopy-height-2019

#### License
The global dataset is available online, with no charges for access and no restrictions on subsequent redistribution or use, as long as the proper citation is provided as specified by the Creative Commons Attribution License (CC BY)

Provided by : Potapov et al. 2020

Curated in GEE by : Potapov et al and Samapriya Roy

Keywords: GEDI, Canopy Height, Landsat, Tree

Last updated: 2020-07-25
