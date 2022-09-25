# Global high-resolution floodplains (GFPLAIN250m)

The GFPLAIN250m includes raster data of Earth's floodplains identified using a geomorphic approach presented in Nardi et al. (2006, 2018). The 250m floodplain dataset is derived by processing the NASA SRTM Digital Elevation model gathered from http://srtm.csi.cgiar.org/, and in particular the 250-m SRTM version 4.1 DTM. The coding used for each continent and additional information are detailed in the metadata included in the GFPLAIN250m data repository. You can find the [dataset here](https://figshare.com/articles/dataset/GFPLAIN250m/6665165/1)

You can read the [full paper here](https://www.nature.com/articles/sdata2018309). The elevation data are processed by a fast geospatial tool for floodplain mapping available for download at https://github.com/fnardi/GFPLAIN. As per the paper, the GFPLAIN250m dataset can support many applications, including flood hazard mapping, habitat restoration, development studies, and the analysis of human-flood interactions.

Disclaimer: Whole or parts of the dataset description was provided by the author(s) or their works.

#### Paper Citation

```
Nardi, F. et al. GFPLAIN250m, a global high-resolution dataset of Earth’s floodplains.
Sci. Data. 6:180309 doi: 10.1038/sdata.2018.309 (2019).
```

#### Data Citation

```
Nardi, Fernando; Annis, Antonio (2018): GFPLAIN250m. figshare. Dataset.
https://doi.org/10.6084/m9.figshare.6665165.v1
```

![gfplain](https://user-images.githubusercontent.com/6677629/150666145-04db0d11-a35d-4a17-b0c9-59f1504f8b72.gif)

#### Earth Engine Snippet

```js

var gfplain250 =  ee.ImageCollection("projects/sat-io/open-datasets/GFPLAIN250")

```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/GLOBAL-HIGHRES-FLOODPLAINS

#### License
This work is distributed under the Creative Commons Attribution 4.0 International License

Created by: Nardi, F. et al

Curated by: Samapriya Roy

Keywords: Floodplain, Digital Elevation Model (DEM), Terrain analysis, river networks, landscape features

Last updated: 2018-11-11
