# Rangeland Analysis Platform layers
Rangeland Analysis Platform data products are available as GEE assets and are made publicly available for analysis through the web application at [rangelands.app](https://rangelands.app)

**Vegetation Cover 30m:** RAP Vegetation Cover, version 3.0 consists of gridded fractional estimates of plant functional groups for rangelands in the continental United States. The estimates are produced at 30-meter spatial resolution for each year between 1986–present. The six plant functional groups are Annual Forbs and Grasses, Perennial Forbs and Grasses, Shrubs, Trees, Litter, and Bare Ground. Cover values are reported as percentages on a pixel-by-pixel basis. The estimates were produced using a temporal convolutional network using field measures of plant functional groups collected by the Natural Resources Conservation Service Natural Resources Inventory (NRI) program, the Bureau of Land Management Assessment, Inventory, and Monitoring (AIM) program, and the National Park Service Northern Colorado Plateau Network (NCPN) alongside spatially continuous earth observations from Landsat TM, ETM+, and OLI Collection 2. 

**Vegetation Cover and Canopy Gap 10m:** : RAP Vegetation Cover and Canopy Gap 10m provides gridded annual estimates of plant functional group cover and canopy gap size classes across rangelands in the western United States. Estimates span 2018–present and are produced at a 10-meter spatial resolution using top-of-atmosphere Sentinel-2 reflectance and a one-dimensional convolutional neural network (1D CNN). The model was trained on 47,833 field plots collected via the Natural Resource Conservation Services’ Natural Resources Inventory (NRI), Bureau of Land Management’s Assessment, Inventory, and Monitoring (AIM) program, National Park Service, and other contributors. The dataset includes fractional cover for 10 plant functional groups and land cover types—Annual Forbs and Grasses, Perennial Forbs and Grasses, Shrubs, Trees, Litter, Bare Ground, Invasive Annual Grasses, Sagebrush, Pinyon-Juniper, and four Canopy Gap size classes (25–50 cm, 51–100 cm, 101-200 cm, >200 cm). Predictions were made using temporally segmented and log-normalized Sentinel-2 reflectance, spatial coordinates, and derived vegetation indices (NDVI, NBR2). The model demonstrated strong predictive performance and showed slight improvements when compared with 30-m Landsat-based vegetation cover estimates by capturing finer-scale spatiotemporal heterogeneity critical to modeling rangeland ecosystems. Output is provided as annual 10 m GeoTIFFs available and as Google Earth Engine assets. 

**Rangeland Production 30m :** : RAP Rangeland Production, version 3.0 consists of gridded estimates of herbaceous aboveground biomass, partitioned into vegetation types for annual forbs and grasses and perennial forbs and grasses. The estimates are produced at 30m spatial resolution from 1986-present. Estimates are provided annually and at 16-day intervals. Values are reported in terms of net primary productivity which can be converted to pounds per acre of new growth of aboveground biomass using the function in the Google Earth Engine script below– estimates do not reflect standing biomass from previous years. Estimates are calculated using a light use efficiency model (to estimate net primary production in terms of carbon) which is then allocated to aboveground and belowground pools (based on mean annual temperature) and further converted to biomass using a carbon-to-dry matter ratio.

Dataset was updated based on specifications provided in changelog below. Updated validation statistics for version 3.0 provided here: https://rangelands.app/products/rapV3/

![RAP_v3](https://user-images.githubusercontent.com/33233973/148469528-e8e45e3b-bee6-4c00-907e-4f3b3dfb35c1.JPG)

#### Citations

```
Allred, B. W., McCord, S. E., Assal, T. J., Bestelmeyer, B. T., Boyd, C. S., Brooks, A. C., Cady, S. M., Fuhlendorf, S. D., Green, S. A., Harrison, G. R., Jensen, E. R., Kachergis, E. J., Mattilio, C. M., Mealor, B. A., Naugle, D. E., O’Leary, D., Olsoy, P. J., Peirce, E. S., Reinhardt, J. R., Shriver, R. K., Smith, J. T., Tack, J. D., Tanner, A. M., Tanner, E. P., Twidwell, D., Webb, N. P., & Morford, S. L. (2025). Estimating rangeland fractional cover and canopy gap size class with Sentinel-2 imagery. bioRxiv. https://doi.org/10.1101/2025.03.13.643073 

Jones, M. O., Robinson, N. P., Naugle, D. E., Maestas, J. D., Reeves, M. C., Lankston, R. W., & Allred, B. W. (2021). Annual and 16-day rangeland production estimates for the western United States. Rangeland Ecology & Management, 77, 112-117.

Robinson, N. P., M. O. Jones, A. Moreno, T. A. Erickson, D. E. Naugle, and B. W.
Allred. 2019. Rangeland productivity partitioned to sub-pixel plant functional
types. Remote Sensing 11:1427. http://dx.doi.org/10.3390/rs11121427

Allred, B. W., Bestelmeyer, B. T., Boyd, C. S., Brown, C., Davies, K. W., Duniway, M. C., Ellsworth, L. M., Erickson, T. A., Fuhlendorf, S. D., Griffiths, T. V., Jansen, V., Jones, M. O., Karl, J., Knight, A., Maestas, J. D., Maynard, J. J., McCord, S. E., Naugle, D. E., Starns, H. D., Twidwell, D., & Uden, D. R. (2021). Improving Landsat predictions of rangeland fractional cover with multitask learning and uncertainty. Methods in Ecology and Evolution, 12(5), 841–849. https://doi.org/10.1111/2041-210X.13564
```

#### Earth Engine Asset Paths

```js
// Vegetation Cover 30m 
var RAP_veg_yearly_30m = ee.ImageCollection("projects/rap-data-365417/assets/vegetation-cover-v3") // Plant functional types

// Vegetation Cover and Canopy Gap 10m 
var RAP_veg_yearly_10m = ee.ImageCollection('projects/rap-data-365417/assets/vegetation-cover-10m') // Plant functional types
var RAP_iag_yearly_10m = ee.ImageCollection('projects/rap-data-365417/assets/invasive-annual-grass-cover-10m') // Invasive annual grasses
var RAP_sagebrush_yearly_10m = ee.ImageCollection('projects/rap-data-365417/assets/sagebrush-cover-10m') // Sagebrush (Artemisia spp.)
var RAP_pj_yearly_10m = ee.ImageCollection('projects/rap-data-365417/assets/pj-cover-10m') // Pinyon-juniper
var RAP_gap_yearly_10m = ee.ImageCollection('projects/rap-data-365417/assets/gap-cover-10m') // Canopy gaps

// Rangeland Production 30m
var RAP_npp_yearly = ee.ImageCollection("projects/rap-data-365417/assets/npp-partitioned-v3") // Net primary production (yearly)
var RAP_npp_16d = ee.ImageCollection("projects/rap-data-365417/assets/npp-partitioned-16day-v3") // Net primary production (16-day)
var RAP_npp_16d_prov = ee.ImageCollection("projects/rap-data-365417/assets/npp-partitioned-16day-v3-provisional") // Net primary production (16-day) provisional
```

#### Earth Engine Code Snippets

**Vegetation Cover 30m snippets:** 
[Sample scripts are available on the RAP Support Site.](https://rangelands.app/support/61-processing-rap-data-in-google-earth-engine))

**Vegetation Cover and Canopy Gap 10m :** 
https://code.earthengine.google.com/1d3f1a911ec21dcc8578955f65c193c5

**Rangeland Production 30m snippets :** 
[Sample scripts are available on the RAP Support Site.](https://rangelands.app/support/61-processing-rap-data-in-google-earth-engine))

Extra Info: See any of the three herbaceous biomass scripts for the function to convert from net primary production to biomass.

Download Tool/Code snippets if any: Analysis can be performed on these datasets for your regions of interest through the GUI at [rangelands.app](https://rangelands.app)

#### License Information

Public Domain-CC0

#### Curated by
Sarah McCord, Point of Contact, and Jeb Williamson, Agricultural Research Service, U.S. Department of Agriculture

Keywords: rangelands, vegetation, time-series, machine learning, landsat, sentinel-2

Last updated: 2025-05-20

#### Changelog

Vegetation Cover and Canopy Gap 10m was released on 2025-05-20 

Primary changes include:

* Use of Sentinel-2 
* Addition of new canopy gap layers and vegetation cover classes (pinyon juniper, sagebrush, invasive annual grasses) 

RAP Vegetation Cover and Rangeland Production 30m v3 was released on 2022-01-01

Primary changes include:

* Use of Landsat Collection 2
* Addition of the National Park Service Northern Colorado Plateau Network (NCPN) monitoring data for cover training
* Identify agriculture, development, and water
* Addition of the eastern states
