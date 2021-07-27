# Global georeferenced Database of Dams(GOODD)

GOODD, a global dataset of more than 38,000 georeferenced dams as well as their associated catchments. The source [paper](https://www.nature.com/articles/s41597-020-0362-5) presents the development of the global database through systematic digitisation of satellite imagery globally by a small team and highlights the various approaches to bias estimation and to validation of the data. The following datasets are provided (a) raw digitised coordinates for the location of dam walls (that may be useful for example in machine learning approaches to dam identification from imagery), (b) a global vector file of the watershed for each dam.

Read the paper for methodology and [further details here](https://www.nature.com/articles/s41597-020-0362-5)

You can [download the dataset here](https://springernature.figshare.com/articles/dataset/GOODD_global_dam_dataset/9747686?backTo=/collections/GOODD_a_global_dataset_of_more_than_38_000_georeferenced_dams/4648214)

#### Data Citation

```
van Soesbergen, Arnout; Mulligan, Mark; Sáenz, Leonardo (2020): GOODD global dam dataset
figshare. Dataset. https://doi.org/10.6084/m9.figshare.9747686.v1
```

#### Paper Citation

```
Mulligan, Mark, Arnout van Soesbergen, and Leonardo Sáenz.
"GOODD, a global dataset of more than 38,000 georeferenced dams."
Scientific Data 7, no. 1 (2020): 1-8.
```

![goodd](https://user-images.githubusercontent.com/6677629/126881520-3868ec5f-0da2-4292-9c2e-38e28cb0dd48.gif)

#### Earth Engine Snippet

```js
var catchments = ee.FeatureCollection("projects/sat-io/open-datasets/GOODD/GOOD2_catchments");
var dams = ee.FeatureCollection("projects/sat-io/open-datasets/GOODD/GOOD2_dams");
```

Sample Code: https://code.earthengine.google.com/a168dcd1f992cf60c16e64e03e1bc842

#### License
The dataset is released under a CC0 1.0 Universal (CC0 1.0) Public Domain Dedication. You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.

Created by : Mulligan, Mark, Arnout van Soesbergen, and Leonardo Sáenz

Curated in GEE by: Samapriya Roy

Keywords: Global dams, global catchments, vector, Hydrology

Last updated : 2021-07-24
