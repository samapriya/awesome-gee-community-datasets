# Canada High Resolution Digital Elevation Model (HRDEM)

<div class="result" markdown>

???+ note

    **This dataset is currently only available to those in the [insiders program](https://gee-community-catalog.org/insiders/)**

</div>

The High Resolution Digital Elevation Model (HRDEM) product is derived from airborne LiDAR data (mainly in the south) and satellite images in the north. The complete coverage of the Canadian territory is gradually being established. It includes a Digital Terrain Model (DTM), a Digital Surface Model (DSM) and other derived data. For DTM datasets, derived data available are slope, aspect, shaded relief, color relief and color shaded relief maps and for DSM datasets, derived data available are shaded relief, color relief and color shaded relief maps.

The HRDEM product is referenced to the Canadian Geodetic Vertical Datum of 2013 (CGVD2013), which is now the reference standard for heights across Canada. Source data for HRDEM datasets is acquired through multiple projects with different partners. Since data is being acquired by project, there is no integration or edgematching done between projects. The tiles are aligned within each project. The product High Resolution Digital Elevation Model (HRDEM) is part of the CanElevation Series created in support to the National Elevation Data Strategy implemented by NRCan. Collaboration is a key factor to the success of the National Elevation Data Strategy. You can find [more information here](https://open.canada.ca/data/en/dataset/957782bf-847c-4644-a757-e383c0057995)

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or providers of the dataset and their works.

#### Preprocessing

Most of the 2m resolution datasets are generated from ArcticDEM project and as such not ingested in this effort and only 1m resolution tiles were ingested. Since tile edges were not matched and datasets were from various sources and dates a simple approach was used for tiles with same names where the largest file size replaced any file of that name. This was a decision to help deconflict tiles with similar names and was done programatically.

#### Citation

```
openCanada.ca; High Resolution Digital Elevation Model (HRDEM) - CanElevation Series : Last accessed date
```

![hrdem_small](https://user-images.githubusercontent.com/6677629/211083890-c202c65c-049b-42c7-a376-f2a64539a220.gif)

#### Earth Engine Snippet : Sample

```js
var dsm = ee.ImageCollection("projects/sat-io/open-datasets/OPEN-CANADA/CAN_ELV/HRDEM_1M_DSM");
var dtm = ee.ImageCollection("projects/sat-io/open-datasets/OPEN-CANADA/CAN_ELV/HRDEM_1M_DTM");
var footprint = ee.FeatureCollection("projects/sat-io/open-datasets/OPEN-CANADA/CAN_ELV/dataset_footprints");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:elevation-bathymetry/OPEN-CANADA-HRDEM

#### License
This work is licensed under a Open Government Licence - Canada.

Created by: CanElevation Series, Gov of Canada

Curated in GEE by: Samapriya Roy

keywords: digital terrain model, digital surface model, bare-earth, terrain, remote sensing, lidar,dsm,dtm

Last updated in GEE: 2022-12-27
