# HydroATLAS v1.0

HydroATLAS offers a global compendium of hydro-environmental characteristics for all sub-basins of HydroBASINS, all river reaches of HydroRIVERS, and all lake polygons of HydroLAKES. The HydroATLAS database is divided into three distinct sub-datasets: BasinATLAS, RiverATLAS, and LakeATLAS which represent sub-basin delineations (polygons), the river network (lines), and lake shorelines (polygons), respectively. In total, HydroATLAS contains 1.0 million sub-basins, 8.5 million river reaches, and 1.4 million lakes.

HydroATLAS has been created by compiling and re-formatting a wide range of hydro-environmental attributes derived from existing global datasets in a consistent and organized manner. The resulting data compendium offers attributes grouped in seven categories: hydrology; physiography; climate; land cover & use; soils & geology; and anthropogenic influences. For each of the three sub-datasets, HydroATLAS contains 56 hydro-environmental variables, partitioned into 281 individual attributes. You can download [the files here](https://www.hydrosheds.org/hydroatlas)

The HydroATLAS database is distributed in large file sizes due to the enriched attribute information. Users who only need geometric information and digital vector maps of sub-basin boundaries, river network lines, and lake shorelines may prefer to download the HydroBASINS, HydroRIVERS, or HydroLAKES products instead.

#### Technical Documentation
For more information on HydroATLAS please refer to [hydrosheds page on hydroatlas](https://www.hydrosheds.org/hydroatlas) and the [HydroATLAS Technical Documentation](https://data.hydrosheds.org/file/technical-documentation/HydroATLAS_TechDoc_v10_1.pdf).

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Citations

The development of BasinATLAS and RiverATLAS is fully described in Linke et al. (2019) and should be cited as:

```
Linke, S., Lehner, B., Ouellet Dallaire, C., Ariwi, J., Grill, G., Anand, M., Beames, P., Burchard-Levine, V.,
Maxwell, S., Moidu, H., Tan, F., Thieme, M. (2019). Global hydro-environmental sub-basin and river reach
characteristics at high spatial resolution. Scientific Data 6: 283. doi: https://doi.org/10.1038/s41597-019-0300-6
```
‍
The development of LakeATLAS is fully described in Lehner et al. (2022) and should be cited as:

```
Lehner, B., Messager, M.L., Korver, M.C., Linke, S. (2022). Global hydro-environmental lake characteristics at
high spatial resolution. Scientific Data 9: 351. doi: https://doi.org/10.1038/s41597-022-01425-z
```

#### License
The HydroATLAS database is licensed under a Creative Commons Attribution (CC-BY) 4.0 International License. Please also refer to the HydroATLAS Technical Documentation for more details on the license and requested citations. By downloading and using the data the user agrees to the terms and conditions of this license.


ou can read the paper here : https://www.nature.com/articles/ncomms13603?origin=ppub

![hydroatlas](https://user-images.githubusercontent.com/6677629/182036911-8391d91c-17b2-4446-b302-851cb5d562d9.gif)

#### Earth Engine Snippet

```js
var riveratlas = ee.FeatureCollection("projects/sat-io/open-datasets/HydroAtlas/RiverAtlas_v10");
var lakeatlas_pt = ee.FeatureCollection("projects/sat-io/open-datasets/HydroAtlas/LakeAtlas/LakeAtlas_v10_point");
var lakeatlas_poly = ee.FeatureCollection("projects/sat-io/open-datasets/HydroAtlas/LakeAtlas/LakeAtlas_v10_polygon");
var basin_l01 = ee.FeatureCollection("projects/sat-io/open-datasets/HydroAtlas/BasinAtlas/BasinATLAS_v10_lev01");
var basin_l02 = ee.FeatureCollection("projects/sat-io/open-datasets/HydroAtlas/BasinAtlas/BasinATLAS_v10_lev02");
var basin_l03 = ee.FeatureCollection("projects/sat-io/open-datasets/HydroAtlas/BasinAtlas/BasinATLAS_v10_lev03");
var basin_l04 = ee.FeatureCollection("projects/sat-io/open-datasets/HydroAtlas/BasinAtlas/BasinATLAS_v10_lev04");
var basin_l05 = ee.FeatureCollection("projects/sat-io/open-datasets/HydroAtlas/BasinAtlas/BasinATLAS_v10_lev05");
var basin_l06 = ee.FeatureCollection("projects/sat-io/open-datasets/HydroAtlas/BasinAtlas/BasinATLAS_v10_lev06");
var basin_l07 = ee.FeatureCollection("projects/sat-io/open-datasets/HydroAtlas/BasinAtlas/BasinATLAS_v10_lev07");
var basin_l08 = ee.FeatureCollection("projects/sat-io/open-datasets/HydroAtlas/BasinAtlas/BasinATLAS_v10_lev08");
var basin_l09 = ee.FeatureCollection("projects/sat-io/open-datasets/HydroAtlas/BasinAtlas/BasinATLAS_v10_lev09");
var basin_l10 = ee.FeatureCollection("projects/sat-io/open-datasets/HydroAtlas/BasinAtlas/BasinATLAS_v10_lev10");
var basin_l11 = ee.FeatureCollection("projects/sat-io/open-datasets/HydroAtlas/BasinAtlas/BasinATLAS_v10_lev11");
var basin_l12 = ee.FeatureCollection("projects/sat-io/open-datasets/HydroAtlas/BasinAtlas/BasinATLAS_v10_lev12");
```
Sample code: https://code.earthengine.google.com/9bc272d8183275bcbc6d2f89e3361485

Created by: Linke et al and Lehner et al

Curated by: Samapriya Roy

Keywords: water,hydrology, lakes, global lake surface, discharge, depth, volume, area, hydrolakes, hydrobasins, hydrorivers

Last updated: 2022-07-10
