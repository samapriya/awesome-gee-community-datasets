# Global Habitat Heterogeneity

The datasets contain 14 metrics quantifying spatial heterogeneity of global habitat at multiple resolutions based on the textural features of Enhanced Vegetation Index (EVI) imagery acquired by the Moderate Resolution Imaging Spectroradiometer (MODIS). For additional information about the metrics and the evaluations of their utility for biodiversity modeling. The dataset is generated at 1km, 5km and 25km resolution and only the 1km assets are listed here, simply replace _1km by _5km and _25km as needed.

#### Paper Citation

```
Tuanmu, M.-N. and W. Jetz. (2015) A global, remote sensing-based characterization of terrestrial habitat heterogeneity
for biodiversity and ecosystem modeling. Global Ecology and Biogeography. DOI: 10.1111/geb.12365.
```

![ghh](https://user-images.githubusercontent.com/6677629/117577332-fcfa6b00-b0ae-11eb-9fd3-1f235aebb114.gif)

#### Earth Engine Snippet

```js
var cov = ee.Image("projects/sat-io/open-datasets/global_habitat_heterogeneity/coefficient_of_variation_1km");
var contrast = ee.Image("projects/sat-io/open-datasets/global_habitat_heterogeneity/contrast_1km");
var corr = ee.Image("projects/sat-io/open-datasets/global_habitat_heterogeneity/correlation_1km");
var dissimilarity = ee.Image("projects/sat-io/open-datasets/global_habitat_heterogeneity/dissimilarity_1km");
var entropy = ee.Image("projects/sat-io/open-datasets/global_habitat_heterogeneity/entropy_1km");
var homogeneity = ee.Image("projects/sat-io/open-datasets/global_habitat_heterogeneity/homogeneity_1km");
var maximum = ee.Image("projects/sat-io/open-datasets/global_habitat_heterogeneity/maximum_1km");
var mean = ee.Image("projects/sat-io/open-datasets/global_habitat_heterogeneity/mean_1km");
var pielou = ee.Image("projects/sat-io/open-datasets/global_habitat_heterogeneity/pielou_1km");
var range = ee.Image("projects/sat-io/open-datasets/global_habitat_heterogeneity/range_1km");
var shannon = ee.Image("projects/sat-io/open-datasets/global_habitat_heterogeneity/shannon_1km");
var simpson = ee.Image("projects/sat-io/open-datasets/global_habitat_heterogeneity/simpson_1km");
var sd = ee.Image("projects/sat-io/open-datasets/global_habitat_heterogeneity/standard_deviation_1km");
var uniformity = ee.Image("projects/sat-io/open-datasets/global_habitat_heterogeneity/uniformity_1km");
var variance = ee.Image("projects/sat-io/open-datasets/global_habitat_heterogeneity/variance_1km");
```

Sample Script: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:earthenv-bd-ecosystems-clim-layers/GLOBAL-HABITAT-HETEROGENEITY


#### License
Global Habitat Heterogeneity Metrics Version 1 by Tuanmu & Jetz is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.
Permissions beyond the scope of this license may be available at http://www.earthenv.org/texture.html.

### Dataset Citation

```
Tuanmu, M.-N. and W. Jetz. (2015) A global, remote sensing-based characterization of terrestrial habitat heterogeneity
for biodiversity and ecosystem modeling. Global Ecology and Biogeography. DOI: 10.1111/geb.12365.
```

Project Website: http://www.earthenv.org/texture

App Website: [App link here](https://earthenv-dot-map-of-life.appspot.com/3/-36.607/39.842?collections=texture&layers=range1km)

Curated by: Samapriya Roy

Keywords: Earthenv, habitat heterogeneity, shannon, simpson, pielou, dissimilarity, homogeneity, variance, contrast

Last updated: 2021-05-09
