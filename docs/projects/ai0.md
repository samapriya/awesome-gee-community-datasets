# Global Aridity Index

The Global Aridity Index (Global-Aridity_ET0) and Global Reference Evapotranspiration (Global-ET0) Version 3 dataset provides high-resolution (30 arc-seconds) global raster climate data for the 1970-2000 period, related to evapotranspiration processes and rainfall deficit for potential vegetative growth, based upon the implementation of a Penman Monteith Evapotranspiration equation for reference crop. The dataset follows the development and is based upon the [WorldClim 2.1](https://www.worldclim.org/data/worldclim21.html) at 30 arc seconds or ~ 1km at the equator. You can read the [paper here](https://www.nature.com/articles/s41597-022-01493-1)

Aridity Index represent the ratio between precipitation and ET0, thus rainfall over vegetation water demand (aggregated on annual basis). Under this formulation, Aridity Index values increase for more humid conditions, and decrease with more arid conditions. The Aridity Index values reported within the Global Aridity Index_ET0 geodataset have been multiplied by a factor of 10,000 to derive and distribute the data as integers (with 4 decimal accuracy). This multiplier has been used to increase the precision of the variable values without using decimals.

#### Data citation

```
Zomer, Robert; Trabucco, Antonio (2019): Global Aridity Index and Potential Evapotranspiration (ET0) Database: Version 3.
figshare. Dataset. https://doi.org/10.6084/m9.figshare.7504448.v6
```

#### Paper citation

```
Zomer, R.J.; Xu, J.;  Trabuco, A. 2022. Version 3 of the Global Aridity Index and Potential Evapotranspiration Database.
Scientific Data 9, 409. https://www.nature.com/articles/s41597-022-01493-1
```

![aridity0](https://user-images.githubusercontent.com/6677629/117587582-5204a400-b0e4-11eb-8cd7-8223546da061.gif)

Global-AI grid layers are available as monthly averages (12 data layers, i.e. one layer for each month) or as an annual average (1 data layer) for the 1970-2000 period.

#### Earth Engine Snippet

```js
var aridity_index_yearly = ee.Image("projects/sat-io/open-datasets/global_ai/global_ai_yearly");
var aridity_index_monthly = ee.Image("projects/sat-io/open-datasets/global_ai/global_ai_monthly")
```

Sample Code: https://code.earthengine.google.com/c256ad3f90a656a2edccb6d7d2453c19

<center>

|Aridity Index Value|Climate Class|
|:------------------|:------------|
|<0.03              |Hyper Arid   |
|0.03-0.2           |Arid         |
|0.2-0.5            |Semi-Arid    |
|0.5-0.65           |Dry sub-humid|
|>0.65              |Humid        |

</center>

#### License

The Global-Aridity_ET0 and Global-ET0 datasets are provided for non-commercial use under the CC BY 4.0 Attribution 4.0 International license.

Data Website: You can download the [data and description here](https://figshare.com/articles/dataset/Global_Aridity_Index_and_Potential_Evapotranspiration_ET0_Climate_Database_v2/7504448/6)

Curated in GEE by: Samapriya Roy

Keywords: aridity index, evapotranspiration, geospatial modeling

Last updated: 2022-09-02
