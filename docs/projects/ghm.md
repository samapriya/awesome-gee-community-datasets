# Global human modification v1.5

This updates v1 to v1.5, which provides additional datasets on 6 major stressors at 300 m resolution and two additional time steps (1995 and 2005), as well as reflecting minor data update and processing refinements. Users are advised to use these data instead of "CSP gHM: Global Human Modification" (https://developers.google.com/earth-engine/datasets/catalog/CSP_HM_GlobalHumanModification).
These data were updated June 17, 2023.

Data on the extent, patterns, and trends of human land use are critically important to support global and national priorities for conservation and sustainable development. To inform these issues, we created a series of detailed global datasets for 1990, 1995, 2000, 2005, 2010, 2015, and 2017 to evaluate temporal changes and spatial patterns of land use modification of terrestrial lands (excluding Antarctica). These data were calculated using the degree of human modification approach that combines the proportion of a pixel of a given stressor (i.e. footprint) times the intensity of that stressor (ranging from 0 to 1.0). Our novel datasets are detailed (0.09 km^2 resolution), temporally consistent (for 1990-2015, every 5 years), comprehensive (11 change stressors, 14 current), robust (using an established framework and incorporating classification errors and parameter uncertainty), and strongly validated. We also provide a dataset that represents ~2017 conditions and has 14 stressors for an even more comprehensive dataset, but the 2017 results should not be used to calculate change with the other datasets (1990-2015).You can read the [paper here](https://essd.copernicus.org/articles/12/1953/2020/essd-12-1953-2020.html). The v1.5 datasets [can also be accessed at](https://zenodo.org/record/7534895).

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Updates Changelog & reasoning
This updates v1 to v1.5, which provides additional datasets on 6 major stressors at 300 m resolution and two additional time steps (1995 and 2005), as well as reflecting minor data updates and processing refinements. Specifically:

1. Datasets are provided for each of the 6 stressor groups: built-up areas (BU), agricultural/timber harvest (AG), extractive energy and mining (EX), human intrusions (HI), natural system modifications (NS), and transportation & infrastructure (TI), available now at 300 m resolution for each of the time steps in the 1990-2015 time series.

2. It provides the addition datasets for the years 1995 and 2005, calculated using linear interpolation when stressor data do not provide data at the specific year.

3. The ESA 150 m water-mask dataset ([Lamarche et al. 2017](https://www.mdpi.com/2072-4292/9/1/36)) was used to provide better and more consistent alignment of datasets at the ocean-land-inland water interfaces.

4. The built-up stressor uses an updated version of the Global Human Settlement Layer (v2022A).

5. Values provided are 32-bit floating point values, with human modification values ranging from 0.0 to 1.0.

#### Citation

```
Theobald, David M., Christina Kennedy, Bin Chen, James Oakleaf, Sharon Baruch-Mordo, and Joe Kiesecker. "Earth transformed: detailed mapping of
global human modification from 1990 to 2017." Earth System Science Data 12, no. 3 (2020): 1953-1972.
```

#### Dataset citation

```
Theobald, David M., Kennedy, Christina, Chen, Bin, Oakleaf, James, Baruch-Mordo, Sharon, & Kiesecker, Joe. (2023). Data for detailed temporal
mapping of global human modification from 1990 to 2017 (v1.5) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.7534895
```

![ghm](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/9c7e404b-1c87-47b8-96c5-074d2e61acf1)

#### Earth Engine Snippet

```js
var waterMask = ee.Image("projects/sat-io/open-datasets/GHM/ESACCI-LC-L4-WB-Ocean-Land-Map-150m-P13Y-2000-v40");
var H2017static = ee.Image("projects/sat-io/open-datasets/GHM/ghm_v15_2017_300_60land")
var H2015change = ee.Image("projects/sat-io/open-datasets/GHM/ghm_v15_2015c_300_60land");
var H2010change = ee.Image("projects/sat-io/open-datasets/GHM/ghm_v15_2010c_300_60land");
var H2005change = ee.Image("projects/sat-io/open-datasets/GHM/ghm_v15_2005c_300_60land");
var H2000change = ee.Image("projects/sat-io/open-datasets/GHM/ghm_v15_2000c_300_60land");
var H1995change = ee.Image("projects/sat-io/open-datasets/GHM/ghm_v15_1995c_300_60land");
var H1990change = ee.Image("projects/sat-io/open-datasets/GHM/ghm_v15_1990c_300_60land");
var H2017_AG = ee.ImageCollection("projects/sat-io/open-datasets/GHM/SG-AG");
var H2017_BU = ee.ImageCollection("projects/sat-io/open-datasets/GHM/SG-BU");
var H2017_EX = ee.ImageCollection("projects/sat-io/open-datasets/GHM/SG-EX");
var H2017_HI = ee.ImageCollection("projects/sat-io/open-datasets/GHM/SG-HI");
var H2017_NS = ee.ImageCollection("projects/sat-io/open-datasets/GHM/SG-NS");
var H2017_TI = ee.ImageCollection("projects/sat-io/open-datasets/GHM/SG-TI");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/GLOBAL-HUMAN-MODIFICATION

Earth Engine App: https://davidtheobald8.users.earthengine.app/view/global-human-modification-change

#### License
This dataset is available under a CC-BY-SA-4.0.

Curated by: David M. Theobald & Samapriya Roy

Keywords: Global human modification, land use, human pressures, biodiversity

Last updated: June 17, 2023
