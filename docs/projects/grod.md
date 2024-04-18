# Global River Obstruction Database (GROD)

GROD v1.1 (filename: GROD_v1.1.csv), or Global River Obstruction Database version 1.1, contains 30549 manually identified human-made structures that
obstructing river longitudinal flow. Obstructions have been identified on Google Earth Engine satellite map for all rivers mapped in the Global
River Widths from Landsat (GRWL) database. Each obstruction has assigned one of the six types—Dam, Lock, Low head dam, Channel dam, Partial dam 1,
Partial dam 2. Details of the mapping process and data quality can be [found in the publication](https://agupubs.onlinelibrary.wiley.com/doi/full/10.
1029/2021WR030386) and the dataset [can be accessed here](https://zenodo.org/record/5793918).

#### Citation

```
Yang, X., Pavelsky, T.M., Ross, M.R., Januchowski‐Hartley, S.R., Dolan, W., Altenau, E.H., Belanger, M., Byron, D., Durand, M., Van Dusen, I. and Galit, H., 2022. Mapping flow‐obstructing structures on global rivers. Water Resources Research, 58(1), p.e2021WR030386.
```

#### Dataset Citation

```
Yang, X., Pavelsky, T. M., Ross, M. R. V., Januchowski-Hartley, S. R., Dolan, W., Altenau, E. H., Belanger, M., Byron, D., Durand, M., Van Dusen,
I., Galit, H., Jorissen, M., Langhorst, T., Lawton, E., Lynch, R., Mcquillan, K. A., Pawar, S., & Whittemore, A. (2021). Global River Obstruction
Database v1.1 (v1.1) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.5793918
```

![grod_demo](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/4c5c1755-13f4-43d2-afc9-7ecc3c9abafe)

#### Earth Engine Snippet

```js
var grod = ee.FeatureCollection("projects/sat-io/open-datasets/GROD/GROD_V11");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/GLOBAL-RIVER-OBSTRUCTION-DATABASE

#### License

The datasets are provided under a Creative Commons 4.0 International License.

Provided by: Yang et al 2021

Curated in GEE by: Samapriya Roy

Keywords: river obstruction, dam, lock, low head dam, weir, partial dam, wing dam, dataset, fragmentation, SWOT

Last updated: 2024-04-15
