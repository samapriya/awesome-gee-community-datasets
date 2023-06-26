# Global Highres Mining Footprints

Mining is of major economic, environmental and societal consequence, yet  knowledge and understanding of its global footprint is still limited.
Here, we produce a global mining land use dataset via remote sensing analysis of high-resolution, publicly available satellite imagery. The
dataset comprises 74,548 polygons, covering ~66,000 km2 of features like waste rock dumps, pits, water ponds, tailings dams, heap leach pads and
processing/milling infrastructure. Our polygons finely contour the edges of mine features and do not include the space between them. This
distinguishes our dataset from others that employ broader definitions of mining lands. Hence, despite our database being the largest to date by
number of polygons, comparisons show relatively lower global land use. Our database is made freely available to support future studies of global
mining impacts. A series of spatial analyses are also presented that highlight global mine distribution patterns and broader environmental risks.

#### Citation

```
Tang, Liang, and Tim T. Werner. "Global mining footprint mapped from high-resolution satellite imagery."
Communications Earth & Environment 4, no. 1 (2023): 134.
```

#### Data citation

```
Tang, Liang, & Werner, Tim T. (2023). Global mining footprint mapped from high-resolution satellite imagery.
Communications earth & environment, 4(134). https://doi.org/10.5281/zenodo.7894216
```

![mining_resized](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/dd6c7c34-14db-496d-a353-1ea58e2d4bec)

#### Earth Engine snippet

```js
var mining_footprints = ee.FeatureCollection("projects/sat-io/open-datasets/global-mining/global_mining_footprints");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/GLOBAL-MINING-FOOTPRINTS

#### License
This dataset is available under a Creative Commons BY-4.0 license

Curated by: Tang, Liang, & Werner, Tim T.

Keywords: Mining, High Resolution, Global, coal, land-use, metal ores, minerals, raw material extraction

Last updated: April 26, 2023
