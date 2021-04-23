# Rangeland Analysis Platform layers
Rangeland Analysis Platform data products are available as GEE assets and are made publicly available for analysis through the web application at [rangelands.app](https://rangelands.app)

**Vegetation Cover:** Rangeland Analysis Platform (RAP) Vegetation Cover, version 2.0 consists of gridded fractional estimates of plant functional groups for rangelands in the western United States. The estimates are produced at 30-meter spatial resolution for each year between 1984–present. The five plant functional groups are Annual Forbs and Grasses, Perennial Forbs and Grasses, Shrubs, Trees, and Bare Ground. Cover values are reported as percentages on a pixel-by-pixel basis. The estimates were produced using a temporal convolutional network using field measures of plant functional groups collected by the Natural Resources Conservation Service Natural Resources Inventory (NRI) program and the Bureau of Land Management Assessment, Inventory, and Monitoring (AIM) program alongside spatially continuous earth observations from Landsat TM, ETM, and OLI.

**Herbaceous Biomass:** Rangeland Analysis Platform (RAP) Herbaceous Biomass, version 1.0 consists of gridded estimates of herbaceous aboveground biomass, partitioned by annual forbs and grasses and perennial forbs and grasses. The estimates are produced at 30m spatial resolution from 1986-present. Estimates are provided annually and at 16-day intervals. Values are reported in pounds per acre and represent new growth of biomass – estimates do not reflect standing biomass from previous years. Estimates are calculated using a light use efficiency model (to estimate net primary production in terms of carbon) which is then allocated to above ground and below ground pools (based on mean annual temperature) and further converted to biomass using a carbon-to-dry matter ratio.

![Capture](https://user-images.githubusercontent.com/33233973/115937318-eddfb000-a454-11eb-8646-7d220ea19c6b.JPG)

#### Earth Engine Asset Snippets

```js
// Vegetation Cover
var RAP_veg = ee.ImageCollection("projects/rangeland-analysis-platform/vegetation-cover-v2")

// Net Primary Production (annual)
var RAP_npp = ee.ImageCollection("projects/rangeland-analysis-platform/npp-partitioned-v2")

// Net Primary Production (16-day)
var RAP_npp_16d = ee.ImageCollection("projects/rangeland-analysis-platform/npp-partitioned-16day-v2")
```

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

Last updated: 3/31/2021
