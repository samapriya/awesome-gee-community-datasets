# Global 30m Landsat Tree Canopy Cover v4

The Global 30m Landsat Tree Canopy Version 4 (TCC) product is a 30-meter resolution dataset that shows tree canopy coverage per pixel between 0% and
100%. The TCC product was announced in May 2019 and was processed from the Landsat image archive. It replaces the previous version of global tree
canopy cover estimates for 2000, 2005, 2010, and 2015. It also includes annual tree cover estimates from 2010 to 2015 for North and South America.
The TCC datasets are based on Landsat and Sentinel-2 imagery. The most recent TCC version 2021.4 product suite released in 2023 includes several
components, including an annual Science product with maps and data for years 2008-2021. You can find [additional information here]() and download the [datasets here](https://e4ftl01.cr.usgs.gov/MEASURES/GFCC30TC.003/)

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Citation

```
Sexton, J. O., Song, X.-P., Feng, M., Noojipady, P., Anand, A., Huang, C., Kim, D.-H., Collins, K.M., Channan, S., DiMiceli, C., Townshend, J.R.G. (2013). Global, 30-m resolution continuous fields of tree cover: Landsat-based rescaling of MODIS Vegetation Continuous Fields with lidar-based estimates of error.
International Journal of Digital Earth, 130321031236007. doi:10.1080/17538947.2013.786146.
```

![gfcc30](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/f414d80e-e9e6-46ec-8c4b-0e42b1e6c7c5)

#### Earth Engine Snippet

```js
var GFCC30TC=  ee.ImageCollection("projects/sat-io/open-datasets/GFCC30TC");
```

Sample Script:  https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/GFCC30TC-TREE-CANOPY-COVER

#### License
This data is open to the public and browse images are freely available without restriction.

Created by: Sexton, J. O et al

Curated in GEE by : Samapriya Roy

keywords: Global Tree Canopy, Forestry, Time series, Landsat

Last updated on GEE: 2023-07-05
