# Global Fertilizer Use by crop & country

Understanding how much inorganic fertilizer (referred to as fertilizer) is applied to different crops at national, regional and global levels is an essential component of fertilizer consumption analysis and demand projection. Good information on fertilizer use by crop (FUBC) is rarely available because it is difficult to collect and time-consuming to process and validate. To fill this gap, a first global FUBC report was published in 1992 for the 1990/1991 period, based on an expert survey conducted jointly by the Food and Agriculture Organization (FAO) of the UN, the International Fertilizer Development Center (IFDC) and the International Fertilizer Association (IFA). Since then, similar expert surveys have been carried out and published every two to four years in the main fertilizer-consuming countries. Since 2008 IFA has led these efforts and, to our knowledge, remains the only globally available data set on FUBC. This dataset includes data (in CSV format) from a survey carried out by IFA to represent the 2017–18 period as well as a collation of all historic FUBC data.

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Dataset Preprocessing
LSIB country boundaries were used to join tow table, since the primary table is not geospatial the country names were first refactored to match those of LSIB before creating an internal join. Since these are large geometries the join was converted to centroids for each feature and exported as a feature collection.

#### Paper Citation

```
Ludemann, C.I., Gruere, A., Heffer, P. et al. Global data on fertilizer use by crop and by country. Sci Data 9, 501 (2022).
https://doi.org/10.1038/s41597-022-01592-z
```

#### Data Citation

```
Ludemann, Cameron; Gruere, Armelle; Heffer, Patrick; Dobermann, Achim (2022), Global data on fertilizer use by crop and by country, Dryad,
Dataset, https://doi.org/10.5061/dryad.2rbnzs7qh
```

#### Earth Engine Snippet

```js
var global_fertilizer_use = ee.FeatureCollection("projects/sat-io/open-datasets/global_fertilizer_use_centroid");
```

Sample code: https://code.earthengine.google.com/e0869dccc3b869ecc365470afdc55c7a

#### License

This work is licensed under a CC0 1.0 Universal (CC0 1.0) Public Domain Dedication license.

Created by: Ludemann, Cameron; Gruere, Armelle; Heffer, Patrick; Dobermann, Achim

Curated in GEE by : Samapriya Roy

keywords: Global fertilizer use, agriculture, FAO, crop

Last modified: 2022-08-22

Last updated on GEE: 2022-09-05
