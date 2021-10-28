# Global Photovoltaics Inventory (2016-2018)

Photovoltaic (PV) solar energy generating capacity has grown by 41 per cent per year since 2009. The authors point out that energy system projections that mitigate climate change and aid universal energy access show a nearly ten-fold increase in PV solar energy generating capacity by 2040. The authors further locate and verify 68,661 facilities, an increase of 432 per cent (in number of facilities) on previously available asset-level data. With the help of a hand-labelled test set, we estimate global installed generating capacity to be 423 gigawatts (−75/+77 gigawatts) at the end of 2018.

For installations over 10,000 m2 (approximately 600 kW), achieved precision was 98.6% relative to our test set, with a modest trade-off in recall which drops to 90% (Supplementary Fig. 6). The IoU of the final dataset for installations over 10,000 m2 is 90%—sufficient for the wide range of uses based on the user report. You can [read the paper here](https://www.nature.com/articles/s41586-021-03957-7)

#### Citation:

```
Kruitwagen, L., Story, K.T., Friedrich, J. et al. A global inventory of photovoltaic solar energy generating units.
Nature 598, 604–610 (2021). https://doi.org/10.1038/s41586-021-03957-7
```

#### Dataset Citation

```
Kruitwagen, Lucas, Story, Kyle, Friedrich, Johannes, Byers, Logan, Skillman, Sam, & Hepburn, Cameron. (2021). A global
inventory of solar photovoltaic generating units - dataset (1.0.0) [Data set].
Zenodo. https://doi.org/10.5281/zenodo.5005868
```

![pv](https://user-images.githubusercontent.com/6677629/139303370-15e7cb1d-51bd-456b-be0d-3fd13671c26f.gif)


#### Earth Engine Snippet
```js
var predicted_set = ee.FeatureCollection("projects/sat-io/open-datasets/global_photovoltaic/predicted_set");
var cv_polygons = ee.FeatureCollection("projects/sat-io/open-datasets/global_photovoltaic/cv_polygons");
var cv_tiles = ee.FeatureCollection("projects/sat-io/open-datasets/global_photovoltaic/cv_tiles");
var test_polygons = ee.FeatureCollection("projects/sat-io/open-datasets/global_photovoltaic/test_polygons");
var test_tiles = ee.FeatureCollection("projects/sat-io/open-datasets/global_photovoltaic/test_tiles");
var trn_tiles = ee.FeatureCollection("projects/sat-io/open-datasets/global_photovoltaic/trn_tiles");
var trn_polygons = ee.FeatureCollection("projects/sat-io/open-datasets/global_photovoltaic/trn_polygons");
```

Sample code: https://code.earthengine.google.com/0577d22ed1d7bacba8a27bc31e306f65

#### Layer name and description table

|File Name    |Description                                                                                                                                                                 |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|trn_tiles    |18,570 rectangular areas-of-interest used for sampling training patch data.                                                                                                 |
|trn_polygons |36,882 polygons obtained from OSM in 2017 used to label training patches                                                                                                    |
|cv_tiles     |560 rectangular areas-of-interest used for sampling cross-validation data seeded from WRI GPPDB                                                                             |
|cv_polygons  |6,281 polygons corresponding to all PV solar generating units present in cv_tiles at the end of 2018.                                                                       |
|test_tiles   |122 rectangular regions-of-interest used for building the test set.                                                                                                         |
|test_polygons|7,263 polygons corresponding to all utility-scale (>10kW) solar generating units present in test_tiles at the end of 2018.                                                  |
|predicted_set|68,661 polygons corresponding to predicted polygons in global deployment, capturing the status of deployed photovoltaic solar energy generating capacity at the end of 2018.|


#### License
Creative Commons Attribution 4.0 International License

Created by: Kruitwagen et al

Curated by: Samapriya Roy

Keywords: photovoltaic solar remote sensing geospatial data computer vision

Last updated: 2021-10-28
