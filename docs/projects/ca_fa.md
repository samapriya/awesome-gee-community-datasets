# Landsat-derived forest age for Canada's forested ecosystems (2019)

Landsat-derived forest age for Canada’s forested ecosystems 2019. Satellite-based forest age map for 2019 across Canada’s forested ecozones at a 30-m spatial resolution. Remotely sensed data from Landsat (disturbances, surface reflectance composites, forest structure) and MODIS (Gross Primary Production) are utilized to determine age. Age can be determined where disturbance can be identified directly (disturbance approach) or inferred using spectral information (recovery approach) or using inverted allometric equations to model age where there is no evidence of disturbance (allometric approach). The disturbance approach is based upon satellite data and mapped changes and is the most accurate. The recovery approach also avails upon satellite data plus logic regarding forest succession, with an accuracy that is greater than pure modeling. Given the lack of widespread recent disturbance over Canada’s forests, the allometric approach is required over the greatest area (86.6%). Using information regarding realized heights and growth and yield modeling, ages are estimated where none are otherwise possible. Trees of all ages are mapped, with trees >150 years old combined in an "old tree" category.

Forest area codes:

* No data: Non treed (Value = 255)
* 0-150: Forest age in years
* 151: Old class (forest age greater than 150 years)

#### Approach used to compute the Landsat-derived forest age for Canada (2019)

Map for displaying the approach followed to compute forest age for the treed areas in Canada’s forested ecosystems for a given year, in this case 2019.

1. The disturbance approach uses change detection protocols to detect disturbance from 1985 to 2019, with time since disturbance used as a proxy for forest age.
2. The recovery approach uses Landsat surface reflectance composites to identify pixels exhibiting evidence of recovery from a disturbance that occurred within the twenty years prior to 1985, allowing for the extension of forest age estimates to 1965. Finally,
3. The allometric approach couples inverted allometric equations with maps of forest structure and productivity metrics to model forest age for those pixels that show no evidence of disturbance or recovery to a maximum mapped age of 150 years.

Forest area codes:
0: Non treed
2: Disturbance approach
3: Recovery approach
4: Allometric approach

See Maltman et al. (2023) for an overview of the methods, data, image processing, as well as information on agreement assessment using Canada’s National Inventory (NFI). [Maltman et al. (2023)](https://doi.org/10.1016/j.rse.2023.113529)

#### Citation

```
Maltman, J.C., Hermosilla, T., Wulder, M.A., Coops, N.C., White, J.C., 2023. Estimating and mapping forest age across Canada’s forested ecosystems.
Remote Sensing of Environment 290, 113529.
```

![ca_forest_age_resized](https://user-images.githubusercontent.com/6677629/226199357-695d49a5-1f1c-4694-ad6a-b1f33ca0ae4b.gif)

#### Earth Engine Snippet: Landsat-derived forest age for Canada (2019)

```js
var age = ee.Image("projects/sat-io/open-datasets/CA_FOREST/CA_forest_age_2019");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/CA-FOREST-AGE-2019

#### Earth Engine Snippet: Approach used to compute the Landsat-derived forest age for Canada (2019)

```js
var age_appro = ee.Image("projects/sat-io/open-datasets/CA_FOREST/CA_forest_age_2019_approach");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/CA-FOREST-AGE-2019-APPROACH

Download Tool/Code snippets, if any: Download link
https://opendata.nfis.org/downloads/forest_change/CA_forest_age_2019.zip

#### Required
License Information: Open Government Licence - Canada (http://open.canada.ca/en/open-government-licence-canada)

Created by: Maltman et al. (2023)

Curated in GEE by: Spencer Bronson and Samapriya Roy

Keywords: Forest age, Forest inventory, Land cover, Landsat, Time since disturbance

Last updated: March 15th 2023

