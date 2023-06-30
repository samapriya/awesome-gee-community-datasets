# HySpecNet-11K Hyperspectral Benchmark dataset

The HySpecNet-11k dataset is a large-scale hyperspectral benchmark dataset constructed by the Remote Sensing Image Analysis (RSiM) group at TU Berlin and the Big Data Analytics in Earth Observation group at the Berlin Institute for the Foundations of Learning and Data (BIFOLD). It consists of 11,483 nonoverlapping image patches acquired by the EnMAP satellite, with each patch being a portion of 128 × 128 pixels and containing 224 spectral bands. These patches have a ground sample distance of 30 m. The dataset was constructed using a total of 250 EnMAP tiles acquired between 2 November 2022 and 9 November 2022, during the routine operation phase. Only tiles with less than 10% cloud and snow cover were considered. These tiles underwent radiometric, geometric, and atmospheric corrections to generate the L2A water & land product. Subsequently, the tiles were divided into nonoverlapping image patches, eliminating the cropped patches at the tile borders. This process resulted in more than 45 patches per tile, totaling 11,483 patches for the complete HySpecNet-11k dataset. You can read details [in the paper here](https://arxiv.org/abs/2306.00385) and find [information on the dataset and more here](https://hyspecnet.rsim.berlin/).

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Dataset preprocessing
The datset was split into multiple patch files including the Spectral images and the quality files. Single band quality files were selected and added as bands to the original spectral file with 224 bands. As suggested by the authors 22 bands were invalid and an example cope is included to remove the invalid bands. The single bands QL files and their values are included below. A custom manifest was used to achieve the band names of choice and to make sure the pyramiding schema for QL and spectral bands were Mode and Mean accordingly.

| Quality Layer             | 0       | 1             | 2        | 3      |
|---------------------------|---------|---------------|----------|--------|
| QL_QUALITY_CIRRUS.TIF     | None    | Thin          | Medium   | Thick  |
| QL_QUALITY_CLASSES.TIF    | None    | Land          | Water    | Background |
| QL_QUALITY_CLOUD.TIF      | None    | Cloud         |          |        |
| QL_QUALITY_CLOUDSHADOW.TIF| None    | Cloud Shadow  |          |        |
| QL_QUALITY_HAZE.TIF       | None    | Haze          |          |        |
| QL_QUALITY_SNOW.TIF       | None    | Snow          |          |        |

#### Citation

```
Fuchs, Martin Hermann Paul, and Begüm Demir. "HySpecNet-11k: A Large-Scale Hyperspectral Dataset for Benchmarking Learning-Based Hyperspectral Image
Compression Methods." arXiv preprint arXiv:2306.00385 (2023).
```

![hyspecnet](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/f8002b53-7018-4019-8c93-3b4d791526dc)


#### Earth Engine Snippet

```js
var hyspecnet = ee.ImageCollection("projects/sat-io/open-datasets/HySpecNet/HYSPECNET-11K");
print(hyspecnet.size())

//Remove invalid bands
var invalid_bands = ['B126', 'B127', 'B128', 'B129', 'B130', 'B131', 'B132', 'B133', 'B134', 'B135', 'B136', 'B137', 'B138', 'B139', 'B140', 'B160', 'B161', 'B162', 'B163', 'B164', 'B165', 'B166']

//Select an image
var image = hyspecnet.sort('system:time_start',false).first()
image = image.select(image.bandNames().removeAll(invalid_bands))
print('Resolution',image.select(['B1']).projection().nominalScale())
print('Band Names',image.bandNames())

//Add image as layer
Map.centerObject(image,12)
Map.addLayer(image,{"opacity":1,"bands":["B3","B2","B1"],"min":-154,"max":934,"gamma":1},'Sample HYSPECNET Image Chip')
```

Sample code : https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:analysis-ready-data/HYSPECNET-11K

#### License
This dataset is available under a [CC0 1.0 Universal (CC0 1.0) Public Domain Dedication](https://creativecommons.org/publicdomain/zero/1.0/)

Curated by: Fuchs, Martin Hermann Paul, and Begüm Demir

Keywords: Hyperspectral, Enmap, Benchmark, Tile

Last updated: June 29, 2023
