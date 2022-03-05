# Polaris 30m Probabilistic Soil Properties US
Probabilistic Remapping of SSURGO (POLARIS) soil properties—a database of 30-m probabilistic soil property maps over the contiguous United States (CONUS). The mapped variables over CONUS include soil texture, organic matter, pH, saturated hydraulic conductivity, Brooks-Corey and Van Genuchten water retention curve parameters, bulk density, and saturated water content.

|Variable|Description                                                                  |Units       |
|:-------|:----------------------------------------------------------------------------|:-----------|
|silt    |silt percentage                                                              |%           |
|sand    |sand percentage                                                              |%           |
|clay    |clay percentage                                                              |%           |
|bd      |bulk density                                                                 |g/cm3       |
|theta_s |saturated soil water content                                                 |m3/m3       |
|theta_r |residual soil water content                                                  |m3/m3       |
|ksat    |saturated hydraulic conductivity                                             |log10(cm/hr)|
|ph      |soil pH in H20                                                               |N/A         |
|om      |organic matter                                                               |log10(%)    |
|lambda  | pore size distribution index (brooks corey)                                 |N/A         |
|hb      | bubbling pressure (brooks corey)                                            |log10(kPa)  |
|n       | measure of the pore size distribution (van genuchten)                       |N/A         |
|alpha   | scale parameter inversely proportional to mean pore diameter (van genuchten)|log10(kPa-1)|

#### Citation & Related Publications

[Read the original paper here](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2018WR022797) and cite the work using

```
Chaney, Nathaniel W., Budiman Minasny, Jonathan D. Herman, Travis W. Nauman, Colby W. Brungard, Cristine LS Morgan
Alexander B. McBratney, Eric F. Wood, and Yohannes Yimam. "POLARIS soil properties: 30‐m probabilistic maps of soil properties
over the contiguous United States." Water Resources Research 55, no. 4 (2019): 2916-2938.
```

#### Data characteristics
POLARIS provides a spatially continuous, internally consistent, quantitative prediction of soil series. It offers potential solutions to the primary weaknesses in SSURGO: 1) unmapped areas are gap-filled using survey data from the surrounding regions, 2) the artificial discontinuities at political boundaries are removed, and 3) the use of high resolution environmental covariate data leads to a spatial disaggregation of the coarse polygons.

The dataset is available at varying depth from surface, while the statistics provided include mean, mode , median and percentile values, only median values have been included as part of the collection created.

<center>

|Depth from Surface|
|:----------------:|
|0-5 cm            |
|5-15 cm           |
|15-30 cm          |
|30-60 cm          |
|60-100 cm         |
|100-200 cm        |

</center>

Overall datasets include processing approximately 80,000 files which have been converted into individual images within a collection per property at varying depth. So for example collection bd_mean includes bd_0_5 and represents a single image for contiguous US with bd value at surface depth of 0-5 cm from surface.

#### Notes from Data providers
* 05/01/2019 - The variables hb, alpha, ksat, om are in log10 space.

* 05/01/2019 - Due to file size constraints, the 1 arcsec database is split into 1x1 degree tiffs. Each variable/layer/statistic has its own virtual raster that acts as the "glue" of all the smaller 1x1 degree chunks. For more information on virtual rasters see https://www.gdal.org/gdal_vrttut.html.

* 06/02/2019 - The variables hb and alpha were originally reported to have the units of log10(cm) and log10(cm-1) respectively. This was a typo. The correct units are log10(kPa) and log10(kPa-1) respectively.

#### Earth Engine Snippet: HiHydro Additional Layers

```js
var bd_mean = ee.ImageCollection('projects/sat-io/open-datasets/polaris/bd_mean');
var clay_mean = ee.ImageCollection('projects/sat-io/open-datasets/polaris/clay_mean');
var ksat_mean = ee.ImageCollection('projects/sat-io/open-datasets/polaris/ksat_mean');
var n_mean = ee.ImageCollection('projects/sat-io/open-datasets/polaris/n_mean');
var om_mean = ee.ImageCollection('projects/sat-io/open-datasets/polaris/om_mean');
var ph_mean = ee.ImageCollection('projects/sat-io/open-datasets/polaris/ph_mean');
var sand_mean = ee.ImageCollection('projects/sat-io/open-datasets/polaris/sand_mean');
var silt_mean = ee.ImageCollection('projects/sat-io/open-datasets/polaris/silt_mean');
var theta_r_mean = ee.ImageCollection('projects/sat-io/open-datasets/polaris/theta_r_mean');
var theta_s_mean = ee.ImageCollection('projects/sat-io/open-datasets/polaris/theta_s_mean');
var lambda_mean = ee.ImageCollection('projects/sat-io/open-datasets/polaris/lambda_mean');
var hb_mean = ee.ImageCollection('projects/sat-io/open-datasets/polaris/hb_mean');
var alpha_mean = ee.ImageCollection('projects/sat-io/open-datasets/polaris/alpha_mean');
```

![polaris_layers](https://user-images.githubusercontent.com/6677629/119921913-7231c100-bf34-11eb-9efc-fede2f162272.gif)

Sample Code: https://code.earthengine.google.com/8fe0fcfacbef1072b8cc7a2b68391616

You can download the datasets here: http://hydrology.cee.duke.edu/POLARIS/

#### License
POLARIS is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.

Curated by: Samapriya Roy

Keywords: Digital soil mapping, Soil, Environmental modeling, High performance computing

Last updated dataset: 2019-05-04

Last curated: 2022-03-05
