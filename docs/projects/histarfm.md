# HIghly Scalable Temporal Adaptive Reflectance Fusion Model (HISTARFM) database

The HISTARFM database is a high spatial resolution monthly reflectance temporal series corrected from cloud data gaps. The dataset was created at 30 meters resolution through the fusion of the Landsat and Moderate Resolution Imaging Spectroradiometer (MODIS) temporal series. The method involves using two estimators that work together to eliminate random noise and minimize the bias of Landsat spectral reflectances. The first estimator is an optimal interpolator that generates Landsat reflectance estimates using Landsat historical data and fused MODIS and Landsat reflectances from the nearest overpasses. The fusion process employs a linear regression model at a pixel level. The second estimator is a Kalman filter that corrects any bias in the reflectance produced by the first estimator. HISTARFM provides improved reflectance values and a unique and useful side product, the reflectance uncertainties, which is helpful for realistic error calculation (e.g., computing error bars of Vegetation Indexes or biophysical variables). For a more detailed explanation of the HISTARFM algorithm, please refer to the [Moreno-Martinez et al. 2020](https://www.sciencedirect.com/science/article/pii/S0034425720302716) manuscript.

<p align="center">
  <img width="600" height="550" src="https://user-images.githubusercontent.com/9036360/222484092-6b38bb57-ffc4-4d6d-a3ee-a002abaa9d8d.gif">
</p>
<p align="center">
Example of a mosaic ofHIghly Scalable Temporal Adaptive Reflectance Fusion Model (HISTARFM) database
 the HISTARFM data [right bottom], the red band uncertainty [left bottom], and the derivate leaf area index [top] over a large area in continental East Asia for a given year (2021).
</p>

#### Dataset Access
To access the HISTARFM dataset, you need to join the HISTARFM google group once you have access to the google group you can access the dataset using the code snippets and paths below. The method to find and add yourself to the group is fairly simple. Go to groups.google.com use the drop down to select all groups rather than my groups and search for keyword **HISTARFM collection** then click on join group and follow along. The steps are also captured below

![histarfrm_signup](https://user-images.githubusercontent.com/6677629/223832893-a00d1cfc-646f-4cab-a9c4-eca05b0cd3e7.gif)


#### Citation

```
Moreno-Martínez, Álvaro, Emma Izquierdo-Verdiguier, Marco P. Maneta, Gustau Camps-Valls, Nathaniel Robinson, Jordi Muñoz-Marí, Fernando Sedano,
Nicholas Clinton, and Steven W. Running. "Multispectral high resolution sensor fusion for smoothing and gap-filling in the cloud." Remote Sensing of
Environment 247 (2020): 111901.
```

#### Earth Engine Snippet

Different versions and study areas are already processes:

1. The CONUS database contains 154 images stored as assets. It corresponds with **version 2**, and temporal coverage ranges from January 2009 to October 2021. Each image in the ImageCollection covers the full CONUS, and each has the properties 'version', 'month', and 'year'. This information is also present in their file names. For example, the image called Gap_Filled_Landsat_CONUS_month_10_2009_v2 is an October 2009 image for the CONUS area. The CONUS database is available in [this asset](https://code.earthengine.google.com/?asset=projects/KalmanGFwork/GFLandsat_V1), and the images are loaded in Earth Engine as follows:

```js
var histarfm_conus = ee.ImageCollection("projects/KalmanGFwork/GFLandsat_V1")
```

1. The European, main part of east Asia and Somalia databases are currently being generated with **version 5** of the algorithm. Version 5 contains 26,916 images. Europe contains nine years from 2013 to 2021, east Asia contains three years from 2019 to 2021, and Somalia contains five years from 2010 to 2014. All the study areas are divided into tiles stored in the Google Cloud Plattform as Cloud Optimized Geotiffs. The name of the image includes the month, year, specific study area, and tile. As an example, the image called GF_2018_10_EUROPA_1 represents the image in October 2018 over the first tile in Europe. Version 5 of the database is available [here](https://code.earthengine.google.com/?asset=projects/ee-kalman-gap-filled/assets/histarfm_v5), and the images can be loaded in Earth Engine using the following code:

```js
var histarfm_ic = ee.ImageCollection("projects/ee-kalman-gap-filled/assets/histarfm_v5")
```

Sample code : https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples/HISTARFM-V5-EXAMPLE

For more information about how to work with HISTARFM and some examples of how to improve your research and applications with the HISTARFM database, visit the tutorial [here](https://developers.google.com/earth-engine/tutorials/community/histarfm-cloud-and-gap-free-landsat).

The HISTARFM database was used in the following papers:
- Martínez-Ferrer, L., et al. "Quantifying uncertainty in high resolution biophysical variable retrieval with machine learning." Remote Sensing of Environment 280 (2022): 113199.
- Salerno, L., et al. "Satellite Analyses Unravel the Multi-Decadal Impact of Dam Management on Tropical Floodplain Vegetation." Frontiers in Environmental Science (2022): 357.
- Kushal, K. C., and Sami Khanal. "Agricultural productivity and water quality tradeoffs of winter cover crops at a landscape scale through the lens of remote sensing." Journal of Environmental Management 330 (2023): 117212.

#### License
The HISTARFM model is licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the [License here](http://www.apache.org/licenses/LICENSE-2.0)

The dataset is licensed under a [Creative Commons Attribution NonCommercial 4.0 International](https://creativecommons.org/licenses/by-nc/4.0/) license.

Curated by: Álvaro Moreno-Martínez, Emma Izquierdo-Verdiguier, Jordi Muñoz-Marí and Nicolas Clinton.

Keywords: Land reflectance images, gap-filled temporal series, vegetation.

Last updated: 06-03-2023
