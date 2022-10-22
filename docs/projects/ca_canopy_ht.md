# Canopy height: forested ecosystems of Canada

This dataset contains two canopy height maps from forested ecosystems of Canada at 250m spatial resolution — one using information from the spaceborne LiDAR GEDI, and the other from ICESat-2. GEDI and ICESat-2 are particular in acquiring canopy height information in Canada — the former providing more accurate information of vegetation, yet not reaching full coverage in Canada, whilst the latter is not specifically designed to provide vegetation information but has a global coverage. We created wall-to-wall maps using ATL08 LiDAR product from the ICESat-2 satellite, and GEDI L2A from GEDI.

The data were download for the mid growing season (June and August 2020). Points were filtered regarding solar background noise and atmospheric scattering, totaling 208,554 points from ICESat-2, and 1,249,354 points for GEDI after filtering and point thinning. These points were associated with 14 ancillary variables primarily corresponding to structure information, such as seasonal Sentinel-1 VV and VH polarization, seasonal Sentinel-2 red and NIR bands, and annual PALSAR-2 HH and HV polarization. Afterwards, the random forest algorithm was used to extrapolate LiDAR observations and develop regression models with the abovementioned spatially continuous variables. GEDI had a better performance than ICESat-2 with a mean difference (MD) of 0.9 m and 2.9 m in relation to ALS data used for validation, and a root mean square error (RMSE) of 4.2 m and 5.2 m, respectively. However, as both GEDI and ALS have no coverage in most of the hemi-boreal forests, ICESat-2 captures the tall canopy heights expected for these forests better than GEDI.

You can read the [complete paper here](https://www.mdpi.com/2072-4292/14/20/5158) and download the [dataset at this link](https://data.4tu.nl/articles/dataset/Spatially_continuous_canopy_height_maps_of_forested_ecosystems_of_Canada/21363081/1)

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Citation

```
Sothe, Camile, Alemu Gonsamo, Ricardo B. Lourenço, Werner A. Kurz, and James Snider. "Spatially Continuous Mapping of Forest Canopy Height in Canada
by Combining GEDI and ICESat-2 with PALSAR and Sentinel." Remote Sensing 14, no. 20 (2022): 5158.
```

#### Data Citation

```
Sothe, Camile; Gonsamo, Alemu; Snider, James; Lourenço, Ricardo B.; Kurz, Werner A. (2022): Spatially continuous canopy height maps of forested
ecosystems of Canada. 4TU.ResearchData. Dataset. https://doi.org/10.4121/21363081.v1
```

![tree_canopy _small](https://user-images.githubusercontent.com/6677629/197342366-149bd4cf-feb3-4602-804f-2065468f3214.gif)


#### Earth Engine Snippet: Canopy Height GEDI

```js
var gedi_fc_ht = ee.Image("projects/sat-io/open-datasets/CA_FOREST/GEDI_forest_canopy_height_250m_v1");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/CA-TREE-CANOPY-HEIGHT-GEDI

#### Earth Engine Snippet: ICESat2

```js
var icesat_fc_ht = ee.Image("projects/sat-io/open-datasets/CA_FOREST/ICESat2_forest_canopy_height_250m_v1");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/CA-TREE-CANOPY-HEIGHT-ICESAT


#### License
This dataset is available under a Creative Commons BY-4.0 license

Created by: Sothe,Camile, et al. 2022

Curated in GEE by : Samapriya Roy

Keywords: LiDAR analysis, ICESat-2, GEDI, canopy height distribution, Carbon storage and distribution

Last updated on GEE: 2022-10-20
