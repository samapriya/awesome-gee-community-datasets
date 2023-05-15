# Canada Landsat derived FAO forest identification (2019)

Landsat-based forest area consistent with FAO definitions for Canada's forested ecosystems. To conform with international reporting guidelines and programs, using Landsat data we map the forest area for Canada following the Food and Agricultural Organization of the United Nations (FAO) definition. The FAO definition incorporates land use, whereby trees removed by fire and harvesting for instance, remain forest as the trees will return. Annually representative maps were produced using over three decades of annual land cover data generated from Landsat derived time series land cover and change information (to generate a spatially explicit estimate of the forest area of Canada in 2019). We mapped the area of 'forest', as defined by the FAO, for Canada's 650 Mha of forested ecozones. The map includes the current forest cover in a given year (i.e. 2019), plus the satellite-based temporally informed forest area where tree cover had been temporarily lost due to fire or harvest. See [Wulder et al. (2020)](https://doi.org/10.1093/forestry/cpaa006) for an overview of the methods, data, image processing, as well as information on accuracy assessment using Canada’s National Inventory (NFI). You can [download the dataset here](https://opendata.nfis.org/downloads/forest_change/CA_FAO_forest_2019.zip)

Forest area codes for the dataset are

0: Non forest
1: Current forest area 2019
2: Temporally informed forest area 2019

#### Citation

```
Wulder, M.A., T. Hermosilla, G. Stinson, F.A. Gougeon, J.C. White, D.A. Hill, B.P. Smiley. (2020). Satellite-based time series land cover and change
information to map forest area consistent with national and international reporting requirements. Forestry 93(3), 331-343.
```

![ca_fao_mapped_small](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/ef0e63bf-3a55-4f57-bc71-91a93ff7dbfb)

#### Earth Engine Snippet

```js
var ca_fao = ee.Image("projects/sat-io/open-datasets/CA_FOREST/CA_FAO_forest_2019");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/CA-FAO-FOREST-IDENTIFICATION-2019

#### License
[Open Government Licence - Canada](http://open.canada.ca/en/open-government-licence-canada)

Created by: Wulder et al. (2020)

Curated by: Spencer Bronson and Samapriya Roy

Keywords: Forest area, temporally informed forest area, disturbance informed forest area, Forest inventory, Land cover, Landsat

Last updated: 2023-03-29

