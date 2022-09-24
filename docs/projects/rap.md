# Rangeland Analysis Platform layers
Rangeland Analysis Platform data products are available as GEE assets and are made publicly available for analysis through the web application at [rangelands.app](https://rangelands.app)

**Vegetation Cover:** Vegetation Cover: Rangeland Analysis Platform (RAP) Vegetation Cover, version 3.0 consists of gridded fractional estimates of plant functional groups for rangelands in the continental United States. The estimates are produced at 30-meter spatial resolution for each year between 1984–present. The six plant functional groups are Annual Forbs and Grasses, Perennial Forbs and Grasses, Shrubs, Trees, Litter, and Bare Ground. Cover values are reported as percentages on a pixel-by-pixel basis. The estimates were produced using a temporal convolutional network using field measures of plant functional groups collected by the Natural Resources Conservation Service Natural Resources Inventory (NRI) program, the Bureau of Land Management Assessment, Inventory, and Monitoring (AIM) program, and the National Park Service Northern Colorado Plateau Network (NCPN) alongside spatially continuous earth observations from Landsat TM, ETM+, and OLI Collection 2.

**Rangeland Production:** : Rangeland Analysis Platform (RAP) Rangeland Production, version 3.0 consists of gridded estimates of herbaceous aboveground biomass, partitioned into vegetation types for annual forbs and grasses and perennial forbs and grasses. The estimates are produced at 30m spatial resolution from 1986-present. Estimates are provided annually and at 16-day intervals. Values are reported in terms of net primary productivity which can be converted to pounds per acre of new growth of aboveground biomass using the function in the Google Earth Engine script below– estimates do not reflect standing biomass from previous years. Estimates are calculated using a light use efficiency model (to estimate net primary production in terms of carbon) which is then allocated to aboveground and belowground pools (based on mean annual temperature) and further converted to biomass using a carbon-to-dry matter ratio.

Dataset was updated based on specifications provided in changelog below. Updated validation statistics provided here: https://rangelands.app/products/rapV3/

![RAP_v3](https://user-images.githubusercontent.com/33233973/148469528-e8e45e3b-bee6-4c00-907e-4f3b3dfb35c1.JPG)

#### Earth Engine Asset Snippets

```js
// Vegetation Cover
var RAP_veg = ee.ImageCollection("projects/rangeland-analysis-platform/vegetation-cover-v3")

// Net Primary Production (annual)
var RAP_npp = ee.ImageCollection("projects/rangeland-analysis-platform/npp-partitioned-v3")

```

Code Snippets: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/RANGELAND-ANALYSIS-PLATFORM-EXAMPLE

#### Citation

```
Jones, M.O., N.P. Robinson, D.E. Naugle, J.D. Maestas, M.C. Reeves, R.W.
Lankston, and B.W. Allred. 2020. Annual and 16-day rangeland production
estimates for the western United States. bioRxiv 2020.11.06.343038.
http://dx.doi.org/10.1101/2020.11.06.343038

Robinson, N. P., M. O. Jones, A. Moreno, T. A. Erickson, D. E. Naugle, and B. W.
Allred. 2019. Rangeland productivity partitioned to sub-pixel plant functional
types. Remote Sensing 11:1427. http://dx.doi.org/10.3390/rs11121427

Allred, B. W., B. T. Bestelmeyer, C. S. Boyd, C. Brown, K. W. Davies, L. M.
Ellsworth, T. A. Erickson, S. D. Fuhlendorf, T. V. Griffiths, V. Jansen, M. O.
Jones, J. Karl, J. D. Maestas, J. J. Maynard, S. E. McCord, D. E. Naugle, H. D.
Starns, D. Twidwell, and D. R. Uden. 2020. Improving Landsat predictions of
rangeland fractional cover with multitask learning and uncertainty.
bioRxiv:2020.06.10.142489. http://dx.doi.org/10.1101/2020.06.10.142489
```

Sample scripts are available on the [RAP Support Site](https://support.rangelands.app/article/61-processing-rap-data-in-google-earth-engine).

Extra Info: See any of the three herbaceous biomass scripts for the function to convert from net primary production to biomass.

Download Tool/Code snippets if any: Analysis can be performed on these datasets for your regions of interest through the GUI at [rangelands.app](https://rangelands.app)

#### License Information

Creative Commons Attribution-NonCommercial 4.0 International License

#### Curated by
Brady Allred and Matthew Jones, University of Montana, Data producers; Eric Jensen, University of Montana, Point of Contact

Keywords: rangelands, vegetation, time-series, machine learning, landsat

Last updated: 2022-01-06

#### Changelog

RAP v3 was released on 2022-01-01

Primary changes include:

* Use of Landsat Collection 2
* Addition of the National Park Service Northern Colorado Plateau Network (NCPN) monitoring data for cover training
* Identify agriculture, development, and water
* Addition of the eastern states
