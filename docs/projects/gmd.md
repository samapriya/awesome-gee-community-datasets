# Global Mangrove Distribution, Aboveground Biomass, and Canopy Height

This dataset characterizes the global distribution, biomass, and canopy height of mangrove-forested wetlands based on remotely sensed and in situ field measurement data. Estimates of (1) mangrove aboveground biomass (AGB), (2) maximum canopy height (height of the tallest tree), and (3) basal-area weighted height (individual tree heights weighted in proportion to their basal area) for the nominal year 2000 were derived across a 30-meter resolution global mangrove ecotype extent map using remotely-sensed canopy height measurements and region-specific allometric models. Also provided are (4) in situ field measurement data for selected sites across a wide variety of forest structures (e.g., scrub, fringe, riverine and basin) in mangrove ecotypes of the global equatorial region. Within designated plots, selected trees were identified to species and diameter at breast height (DBH) and tree height was measured using a laser rangefinder or clinometer. Tree density (the number of stems) can be estimated for each plot and expressed per unit area. These data were used to derive plot-level allometry among AGB, basal area weighted height (Hba), and maximum canopy height (Hmax) and to validate the remotely sensed estimates.

Spatially explicit maps of mangrove canopy height and AGB derived from space-borne remote sensing data and in situ measurements can be used to assess local-scale geophysical and environmental conditions that may regulate forest structure and carbon cycle dynamics. Maps revealed a wide range of canopy heights, including maximum values (> 62 m) that surpass maximum heights of other forest types.

There are 348 data files in GeoTIFF format (.tif) with this dataset representing three data products for each of 116 countries. The in situ tree measurements are provided in a single .csv file. You can [grab the dataset here](https://daac.ornl.gov/CMS/guides/CMS_Global_Map_Mangrove_Canopy.html)

#### Preprocessing
The tree measurements CSV has lat lon 2,3,4 removed and lat and lon1 were renamed to lat lon. The dataset table is as below. This and additional metadata can be [found here](https://daac.ornl.gov/CMS/guides/CMS_Global_Map_Mangrove_Canopy.html). The datasets divided into subsets of 116 datasets each were ingested into Google Earth Engine collections.

|Column name                              |Units/format                                                                                            |Type   |Description                                                                                                                                                                                                 |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|ID                                       |                                                                                                        |Character|A unique identifier for locating a specific observation. A combination of plot_name and tree number fields.                                                                                                 |
|region                                   |                                                                                                        |Character|Continent or subcontinent of observation                                                                                                                                                                    |
|subregion                                |                                                                                                        |Character|Country or state of observation                                                                                                                                                                             |
|biome                                    |                                                                                                        |Character|Biome type of observation - all mangrove                                                                                                                                                                    |
|date                                     |yyyy-mm-dd                                                                                              |Date   |Date of observation                                                                                                                                                                                         |
|plot_name                                |                                                                                                        |Character|Plot name                                                                                                                                                                                                   |
|tree_number                              |                                                                                                        |Character|Unique identifier for a tree in a specific plot. Trees characterized as “Severe inclined” were sometimes measured without assigning a number. These trees have been assigned M1, M2, M3, etc. within a plot.|
|genus                                    |                                                                                                        |Character|Genus                                                                                                                                                                                                       |
|species                                  |                                                                                                        |Character|Species                                                                                                                                                                                                     |
|dbh                                      |cm                                                                                                      |Numeric|Diameter at breast height (1.3 m), check tree_notes as some were estimated dbh                                                                                                                              |
|height                                   |meters                                                                                                  |Numeric|height of tree, check tree_notes as some were modeled height                                                                                                                                                |
|live                                     |                                                                                                        |Numeric|1 indicates tree is alive. 0 indicates tree is dead                                                                                                                                                         |
|tree_notes                               |                                                                                                        |Character|specific notes about a tree                                                                                                                                                                                 |
|use_for_allometry                        |                                                                                                        |Numeric|1 indicates tree was used for allometry, 0 indicates it was not.                                                                                                                                            |
|plot_type                                |                                                                                                        |Character|f = fixed plot size, v = variable plot size                                                                                                                                                                 |
|plot_shape                               |                                                                                                        |Character|shape of plot: s and square; r, circle, and circular. Missing when plot_type = v.                                                                                                                           |
|baf                                      |                                                                                                        |Numeric|basal area factor: with a value of 5 for plot_type = v, otherwise missing                                                                                                                                   |
|plot_area                                |m^2                                                                                                     |Numeric|plot area                                                                                                                                                                                                   |
|lat                                      |                                                                                                        |Numeric|latitude of plot location (center of circular and variable shape plots or a plot corner for square plots)                                                                                                   |
|lon                                      |                                                                                                        |Numeric|longitude of plot location (center of circular and variable shape plots or a plot corner for square plots)                                                                                                  |
|collected_by                             |                                                                                                        |Character|Collector of field observations                                                                                                                                                                             |
|digitized_by                             |                                                                                                        |Character|Performer of GIS activities                                                                                                                                                                                 |


#### Paper Citation

```
Simard, M., L. Fatpyinbo, C. Smetanka, V.H. Rivera-Monroy, E. Castaneda-Moya, N. Thomas, and T. Van der Stocken. 2019. Mangrove canopy height
globally related to precipitation, temperature and cyclone frequency. Nature Geoscience, 12: 40–45. https://doi.org/10.1038/s41561-018-0279-1
```

#### Data Citation

```
Simard, M., T. Fatoyinbo, C. Smetanka, V.H. Rivera-monroy, E. Castaneda, N. Thomas, and T. Van der stocken. 2019. Global Mangrove Distribution,
Aboveground Biomass, and Canopy Height. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1665
```

|File name                                |Variable/Description                                                                                    |Units  |
|-----------------------------------------|--------------------------------------------------------------------------------------------------------|-------|
|Mangrove_agb_country.tif                 |Aboveground mangrove biomass                                                                            |Mg ha-1|
|Mangrove_hba_country.tif                 |Mangrove basal-area weighted height (individual tree heights weighted in proportion to their basal area)|meters |
|Mangrove_hmax_country.tif                |Mangrove canopy maximum height (height of the tallest tree)                                             |meters |
|North_South_America_tree_measurements.csv|In situ mangrove tree measurements for locations on the coasts of North and South America.              |       |

#### Dataset revisions

* Version 1.3: The in situ tree measurement data file and documentation were added in April 2021. No changes to previously archived data.

* Version 1.2: Data files were updated in May 2019 because the height to biomass (AGB) conversion equations in the associated Nature Geoscience publication were correct but were implemented incorrectly when generating the publicly available data files. These have now been corrected. The Hba and Hmax data were updated so that they are now capped at the 95th percentile of the maximum value (55 m), as outlined in the publication. Countries without Hba and Hmax data have been omitted.

* Version 1.1: Science-quality data were released in March 2019. All preliminary data files were replaced with new files that incorporated some changes to the aboveground biomass estimation algorithm. In addition, several files with missing data were replaced.

* Version 1.0: Preliminary data were released in November 2018 to accompany the publication of the Simard et al, 2019 paper in Nature Geosciences.

![gmd](https://user-images.githubusercontent.com/6677629/146138883-76a5f7ce-07db-4727-8883-c0707745422e.gif)


#### Earth Engine Snippet

```js
var agb = ee.ImageCollection("projects/sat-io/open-datasets/global_mangrove_distribution/agb");
var hba95 = ee.ImageCollection("projects/sat-io/open-datasets/global_mangrove_distribution/hba95");
var hmax95 = ee.ImageCollection("projects/sat-io/open-datasets/global_mangrove_distribution/hmax95");
var americas_tree = ee.FeatureCollection("projects/sat-io/open-datasets/global_mangrove_distribution/americas_tree_measurements");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/GLOBAL-MANGROVE-BIOMASS-HEIGHT

#### License

Public Domain/No restrictions (CC0): Under the terms of this license you are free to use the material for any purpose without any restrictions.

Created by: Simard et al

Curated by: Samapriya Roy

Keywords: : global mangrove, above ground biomass, canopy height, basal-area weighted height, ecosystem, mangroves

Last updated: 2021-12-15
