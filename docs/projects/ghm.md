# Global human modification v1

Data on the extent, patterns, and trends of human land use are critically important to support global and national priorities for conservation and sustainable development. To inform these issues, we created a series of detailed global datasets for 1990, 2000, 2010, and 2015 to evaluate temporal and spatial trends of land use modification of terrestrial lands (excluding Antarctica). We found that the expansion of and increase in human modification between 1990 and 2015 resulted in 1.6 M km2 of natural land lost. The percent change between 1990 and 2015 was 15.2 % or 0.6 % annually – about 178 km2 daily or over 12 ha min−1. Worrisomely, we found that the global rate of loss has increased over the past 25 years. You can read the [paper here](https://essd.copernicus.org/articles/12/1953/2020/essd-12-1953-2020.html) and access the [datasets from zenodo](https://zenodo.org/record/5338803)

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Citation

```
Theobald, David M., Christina Kennedy, Bin Chen, James Oakleaf, Sharon Baruch-Mordo, and Joe Kiesecker. "Earth transformed: detailed mapping of
global human modification from 1990 to 2017." Earth System Science Data 12, no. 3 (2020): 1953-1972.
```

#### Dataset citation

```
Theobald, David M., Kennedy, Christina, Chen, Bin, Oakleaf, James, Baruch-Mordo, Sharon, & Kiesecker, Joe. (2021). Data for detailed temporal
mapping of global human modification from 1990 to 2017 (v1.4) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.5338803
```

![Screen Shot 2023-03-20 at 12 44 50 PM](https://user-images.githubusercontent.com/94803611/226436874-bb4c868a-b55c-4710-8f3a-665b3e258241.jpg)

#### Earth Engine Snippet

```js
var waterMask = ee.Image("projects/sat-io/open-datasets/GHM/landLakeResOcean300m");
var H2017static = ee.Image("projects/sat-io/open-datasets/GHM/gHMv1_2015_300_60s");
var H2015change = ee.Image("projects/sat-io/open-datasets/GHM/gHMv1_4_2015_300_60cland");
var H2010change = ee.Image("projects/sat-io/open-datasets/GHM/gHMv1_4_2010_300_60cland");
var H2000change = ee.Image("projects/sat-io/open-datasets/GHM/gHMv1_4_2000_300_60cland");
var H1990change = ee.Image("projects/sat-io/open-datasets/GHM/gHMv1_4_1990_300_60cland");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/GLOBAL-HUMAN-MODIFICATION

Earth Engine App: https://davidtheobald8.users.earthengine.app/view/global-human-modification-change

#### Required
License Information: CC-BY-SA-4.0.

Curated by: David M. Theobald & Samapriya Roy

Keywords: Global human modification, land use, human pressures, biodiversity

Last updated: Sept 21, 2021
