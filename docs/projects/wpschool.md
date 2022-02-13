# Gridded Sex-Disaggregated School-Age Population (2020)

Following the IIEP-UNESCO methodology for reconstructing georeferenced school-age populations (ISCED 1 to 3) by year and sex, these datasets were produced by WorldPop (University of Southampton) by applying the Sprague Multipliers to 30-arcsecond (approximately 1km at the equator) gridded datasets depicting the estimated spatial distribution of sex-disaggregated 5-year age groups. These datasets include the sex disaggregated school age population for countries and Dependent territories in Africa only.

#### Inputs

* Gagnon, A.A. and G. Vargas Mesa. 2021. Estimating School-Age Populations by Applying Sprague Multipliers to Raster Data. IIEP Technical Notes, 1. Paris: IIEP-UNESCO. Last accessed 17 Jan 2022 https://unesdoc.unesco.org/ark:/48223/pf0000379198
* UNESCO Institute for Statistics Education database. Last accessed 17 Jan 2022 from http://data.uis.unesco.org
* WorldPop (www.worldpop.org - School of Geography and Environmental Science, University of Southampton; Department of Geography and Geosciences, University of Louisville; Departement de Geographie, Universite de Namur) and Center for International Earth Science Information Network (CIESIN), Columbia University (2018). Global High Resolution Population Denominators Project - Funded by The Bill and Melinda Gates Foundation (OPP1134076). DOI:10.5258/SOTON/WP00646

####  Citation

```
Bondarenko, M., Sorichetta, A., Vargas Mesa, G., Gagnon, A.A., Tatem, A.J. (2022). Gridded Sex Disaggregated School-Age Population Datasets for Countries
and Dependent Territories in Africa in 2020, doi:10.5258/SOTON/WP00732
```

![school_gridded](https://user-images.githubusercontent.com/6677629/153728335-5b8f51cd-2123-4909-846a-03b4995caff6.gif)

#### Earth Engine Snippet

```js
var f_primary = ee.ImageCollection("projects/sat-io/open-datasets/worldpop/africa_F_PRIMARY");
var f_secondary = ee.ImageCollection("projects/sat-io/open-datasets/worldpop/africa_F_secondary");
var m_primary = ee.ImageCollection("projects/sat-io/open-datasets/worldpop/africa_M_PRIMARY");
var m_secondary = ee.ImageCollection("projects/sat-io/open-datasets/worldpop/africa_M_secondary");
var fm_primary = ee.ImageCollection("projects/sat-io/open-datasets/worldpop/africa_F_M_PRIMARY");
var fm_secondary = ee.ImageCollection("projects/sat-io/open-datasets/worldpop/africa_F_M_SECONDARY");
```

Sample Code: https://code.earthengine.google.com/fe362e62a7f6a39e502c11b64ae1c84e

#### License
WorldPop datasets are available under the Creative Commons Attribution 4.0 International License. This means that you are free to share (copy and redistribute the material in any medium or format) and adapt (remix, transform, and build upon the material) for any purpose, even commercially, provided attribution is included (appropriate credit and a link to the licence).

Created by: WorldPop (University of Southampton)

Curated in GEE by: Samapriya Roy

Keywords: gridded model, population data, school age, disaggregated, worldpop
