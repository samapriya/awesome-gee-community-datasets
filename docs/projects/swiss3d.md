# swissSURFACE3D Raster (DSM)

<div class="result" markdown>

???+ note

    **This dataset is currently only available to those in the [insiders program](https://gee-community-catalog.org/insiders/)**

</div>

swissSURFACE3D Raster is a digital surface model (DSM) which represents the earth’s surface including visible and permanent landscape elements such as soil, natural cover, and all sorts of constructive work with the exception of power lines and masts. swissSURFACE3D Raster is derived from airborne LiDAR data of swissSURFACE3D. To model the surface, the following elements (classified LiDAR points) are used:

* soil (class 2)
* vegetation (class 3)
* buildings (class 6)
* bridges / footbridges / viaducts (class 17)
* water (class 9)

To improve the surface representation of large rivers and lakes, watercourse vectors of the topographic landscape model TLM are implemented.

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Data preprocessing
Datasets were preprocessed and distributed in multiple formats. The Cloud Optimized Geotiff files were made available and a program was written to go fetch all and current 31,321 tiles.

#### Citation

```
swissSURFACE3D Raster digital surface model (DSM). Last accessed **date** original data from https://www.swisstopo.admin.ch/en/geodata/height/
surface3d-raster.html
```

![swiss_3d](https://i.imgur.com/UiGzQvA.gif)

#### Code Snippet

```js
var swiss3d = ee.ImageCollection("projects/sat-io/open-datasets/swissSURFACE3D");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:elevation-bathymetry/swiss3D-RASTER

#### License & Terms of Use

The free geodata and geoservices of swisstopo may be used, distributed and made accessible. Furthermore, they may be enriched and processed and also used commercially. A reference to the source is mandatory. In the case of digital or analogue representations and publications, as well as in the case of dissemination, one of the following source references must be attached in any case:

* Bundesamt für Landestopografie swisstopo
* Office fédéral de topographie swisstopo
* Ufficio federale di topografia swisstopo
* Uffizi federal da topografia swisstopo
* Federal Office of Topography swisstopo
* ©swisstopo

Provided by: Federal Office of Topography swisstopo

Curated in GEE by : Samapriya Roy

keywords: LIDAR, Digital Surface Model, DSM, Topography

Last updated on GEE: 2023-01-28
