# Finer Resolution Observation and Monitoring of Global Land Cover 10m (FROM-GLC10)

This work and the paper was designed with an aim to classify 10-m resolution images acquired in 2017 with a sensor on board a different satellite. We examined through the 10-m resolution map, FROM-GLC10, and compared it with our 2017 30-m global land cover map, FROM-GLC30. We found while the results are comparable the 10-m map did provide more spatial details. Although an overall accuracy comparable to the 30-m resolution data was achieved, the actual accuracy of the 10-m resolution map can only be properly assessed with test samples collected from the 10-m resolution data. You can [read the paper here](https://www.sciencedirect.com/science/article/abs/pii/S2095927319301380)

#### About FROM-GLC
Global land cover data are key sources of information for understanding the complex interactions between human activities and global change. FROM-GLC (Finer Resolution Observation and Monitoring of Global Land Cover) is the first 30 m resolution global land cover maps produced using Landsat Thematic Mapper (TM) and Enhanced Thematic Mapper Plus (ETM+) data.

You can [download the dataset here](http://data.ess.tsinghua.edu.cn/fromglc10_2017v01.html) the links are directly to a geotiff file and you can use a downloader like Uget to get to the files.

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Data preprocessing
The datasets were downloaded and a MODE pyramiding scheme was applied owing to the fact that these are classified datasets. The RGB values were provided by the authors and these were converted to hex code for creating a palette. The sample script also takes into consideration remapping the values to provide a more continuous mix max distribution.

#### Data Citation

```
Chen, B., B. Xu, Z. Zhu, C. Yuan, H. Ping Suen, J. Guo, N. Xu, W. Li, Y. Zhao, and J. J. S. B. Yang. "Stable classification with limited sample: Transferring a
30-m resolution sample set collected in 2015 to mapping 10-m resolution global land cover in 2017." Sci. Bull 64 (2019): 370-373.
```

![glc10_LC](https://user-images.githubusercontent.com/6677629/189573190-7e0fa889-47d8-448e-80e1-db71eae8e5aa.gif)


<center>

|Class     |Value|Remapped|Hex code   |
|----------|-----|--------|-----------|
|Background|0    |0       |    #000000|
|Cropland  |10   |1       |    #a3ff73|
|Forest    |20   |2       |    #267300|
|Grass     |30   |3       |    #4ce600|
|Shrub     |40   |4       |    #70a800|
|Water     |60   |5       |    #005cff|
|Impervious|80   |6       |    #c500ff|
|Bareland  |90   |7       |    #ffaa00|
|Snow/Ice  |100  |8       |    #00ffc5|
|Cloud     |120  |9       |    #ffffff|


</center>


#### Earth Engine Snippet

```js
var GLC10 = ee.ImageCollection("projects/sat-io/open-datasets/FROM-GLC10");
```
Sample Code: https://code.earthengine.google.com/69a783764fa5b37b23b275ba1eabe006

#### Credits, Attributions and License

This dataset is available under a Creative Commons BY-4.0 license.

Curated in GEE by: Samapriya Roy

Keywords: : landcover, landuse, lulc, 10m, global, world, sentinel 2, FROM-GLC

Last updated on GEE: 2022-09-10
