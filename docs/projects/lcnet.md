# LandCoverNet Training Labels v1.0

LandCoverNet is a global annual land cover classification training dataset with labels for the multi-spectral satellite imagery from Sentinel-1, Sentinel-2 and Landsat-8 missions in 2018. Image chips of 256 x 256 pixels in LandCoverNet spanning across multiple tiles. Each image chip contains temporal observations from the following satellite products with an annual class label, all stored in raster format (GeoTIFF files):

* Sentinel-1 ground range distance (GRD) with radiometric calibration and orthorectification at 10m spatial resolution
* Sentinel-2 surface reflectance product (L2A) at 10m spatial resolution
* Landsat-8 surface reflectance product from Collection 2 Level-2

Radiant Earth Foundation designed and generated this dataset with a grant from [Schmidt Futures](https://schmidtfutures.com/) with additional support from [NASA ACCESS](https://earthdata.nasa.gov/esds/competitive-programs/access/radiant-mlhub), [Microsoft AI for Earth](https://www.microsoft.com/en-us/ai/ai-for-earth) and in kind technology support from [Sinergise](https://www.sinergise.com/).

One of the strongest feature of this dataset is Consensus labeling where each image chip was validated by three independent users. The accuracy of each user was assessed using chips that were separately labeled by experts from Radiant Earth’s team. To generate the consensus label for each pixel a Bayesian model averaging approach was implemented taking into account the accuracy of each user. The resulting labels are accompanied by a “consensus score” between 0 and 100 which indicates the degree of agreement among the three users. This forms b2 for the dataset while b1 is the class value.

You can read a [sample detailed methodology here](https://radiantearth.blob.core.windows.net/mlhub/landcovernet_af/Documentation.pdf) and you can go to the [sample dataset page here](https://mlhub.earth/data/ref_landcovernet_af_v1). You can read about the [approach in the paper here](https://arxiv.org/abs/2012.03111)

Tutorials on [this can be further accesed here](https://nbviewer.org/github/radiantearth/mlhub-tutorials/blob/main/notebooks/radiant-mlhub-landcovernet.ipynb)

**Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.**

#### Citation

```
Alemohammad, Hamed, and Kevin Booth. "LandCoverNet: A global benchmark land cover classification training dataset."
arXiv preprint arXiv:2012.03111 (2020).
```

#### Dataset Citation

```
Alemohammad S.H., Ballantyne A., Bromberg Gaber Y., Booth K., Nakanuku-Diggs L., & Miglarese A.H. (2020) "LandCoverNet Africa: A Geographically
Diverse Land Cover Classification Training Dataset", Version 1.0, Radiant MLHub. [Date Accessed] https://doi.org/10.34911/rdnt.d2ce8i
```

#### Data structure and preprocessing
The datasets are provided as raster chips with 256 x 256 pixel resolution meaning a total of 65,536 pixels. Overall dataset distribution per region is summarized below

|Abbreviation|Image Chip Count|Ref ID                       |Region       |Proportion Global|
|------------|----------------|-----------------------------|-------------|-----------------|
|AU          |600             |ref_landcovernet_au_v1_labels|Australia    |6.72             |
|AS          |2753            |ref_landcovernet_as_v1_labels|Asia         |30.81            |
|AF          |1980            |ref_landcovernet_af_v1_labels|Africa       |22.16            |
|EU          |840             |ref_landcovernet_eu_v1_labels|Europe       |9.4              |
|NA          |1561            |ref_landcovernet_na_v1_labels|North America|17.47            |
|SA          |1200            |ref_landcovernet_sa_v1_labels|South America|13.43            |

The datasets do consist of a STAC representation and while the command line tool is the way to access this data, I wrote some custom script for parsing the properties in STAC metadata as well as to download the raster objects and the source imagery CSVs for use as Google Earth Engine assset level property.

Retained metadata includes date which is used for both start and end date.

#### Additional Metadata fields
* Distinct Classes: There is a class count as part of the property of the STAC metadata for each tile, in this case a simple count was used to estimate how many distinct classes were available for chip and how that might effect your overall training.
* system:index/id_no was the name of the tile retained from the imagery as is and has not been modified
* source_imagery_start/end: Using the source imagery CSV files source imagery start and end dates were selected post sorting of the dates per chip and added to allow for creating a time filter.
* source_imagery_datelist: This is the complete source imagery date list you can use the list to identify and select specific days of S2 imagery from those days for analysis or comparison.

![lcnet](https://user-images.githubusercontent.com/6677629/179384144-1e5b996b-c1b4-40b6-9801-1e0c14c78cfa.gif)

#### Earth Engine Snippet

```js
var au = ee.ImageCollection("projects/sat-io/open-datasets/LandCoverNet/LABELS/ref_landcovernet_au_v1_labels");
var af = ee.ImageCollection("projects/sat-io/open-datasets/LandCoverNet/LABELS/ref_landcovernet_af_v1_labels");
var as = ee.ImageCollection("projects/sat-io/open-datasets/LandCoverNet/LABELS/ref_landcovernet_as_v1_labels");
var eu = ee.ImageCollection("projects/sat-io/open-datasets/LandCoverNet/LABELS/ref_landcovernet_eu_v1_labels");
var na = ee.ImageCollection("projects/sat-io/open-datasets/LandCoverNet/LABELS/ref_landcovernet_na_v1_labels");
var sa = ee.ImageCollection("projects/sat-io/open-datasets/LandCoverNet/LABELS/ref_landcovernet_sa_v1_labels");
```

Sample Code: https://code.earthengine.google.com/a042b202b2912c8e3abe0b4f42bceb2f


#### License

The dataset is released under (CC BY 4.0) license. You can find [license summary here](https://spdx.org/licenses/CC-BY-4.0.html)

Produced by: Radiant Earth Foundation

Curated in GEE by: Samapriya Roy

Keywords: Land Use, Land Cover, Remote Sensing, landsat-8, sentinel-1, sentinel-2, segmentation

Last updated on GEE: 2022-07-17
