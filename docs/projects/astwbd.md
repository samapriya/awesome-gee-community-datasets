# ASTER Global Water Bodies Database (ASTWBD) Version 1

The Terra Advanced Spaceborne Thermal Emission and Reflection Radiometer (ASTER) Global Water Bodies Database (ASTWBD) Version 1 data product provides global coverage of water bodies larger than 0.2 square kilometers at a spatial resolution of 1 arc second (approximately 30 meters) at the equator, along with associated elevation information.

The ASTWBD data product was created in conjunction with the ASTER Global Digital Elevation Model (ASTER GDEM) Version 3 data product by the Sensor Information Laboratory Corporation (SILC) in Tokyo. The ASTER GDEM Version 3 data product was generated using ASTER Level 1A scenes acquired between March 1, 2000, and November 30, 2013. The ASTWBD data product was then generated to correct elevation values of water body surfaces.

To generate the ASTWBD data product, water bodies were separated from land areas and then classified into three categories: ocean, river, or lake. Oceans and lakes have a flattened, constant elevation value. The effects of sea ice were manually removed from areas classified as oceans to better delineate ocean shorelines in high latitude areas. For lake water bodies, the elevation for each lake was calculated from the perimeter elevation data using the mosaic image that covers the entire area of the lake. Rivers presented a unique challenge given that their elevations gradually step down from upstream to downstream; therefore, visual inspection and other manual detection methods were required. You can find above mentioned detail along with [description here](https://lpdaac.usgs.gov/products/astwbdv001/)

Disclaimer: Parts or all of the dataset description is borrowed from existing description provided by authors.

#### Source Data structure
The data are in Geotiff format, with each file divided into 1x1 degree tiles. To allow for adding a single image instead of a collection output, the zip files were unzipped and a single composite tif file was generated.

#### Citation

```
NASA/METI/AIST/Japan Spacesystems, and U.S./Japan ASTER Science Team. ASTER Global
Digital Elevation Model V003. 2018, distributed by NASA EOSDIS Land Processes DAAC,
https://doi.org/10.5067/ASTER/ASTGTM.003
```

![astwbd](https://user-images.githubusercontent.com/6677629/158250993-cf99f11d-d1bd-4661-b152-81546a42827c.gif)

#### Earth Engine Snippet

```js
var fabdem = ee.Image("projects/sat-io/open-datasets/ASTER/ASTWBD_ATT");
```

Sample Code: https://code.earthengine.google.com/52693ef5d22167a7283fb4e9da60f11f

#### License

All LP DAAC current data and products acquired through the LP DAAC have no restrictions on reuse, sale, or redistribution. This license can thus be treated similar to a public domain CC0 license. ASTER GDEM Version 3 (ASTGTM V003) was released on August, 5, 2019 and contains no redistribution requirements. The LP DAAC kindly requests that you properly cite the data in your research.

Created by:  NASA, METI, AIST, Japan Spacesystems and U.S./Japan ASTER Science Team

Curated in GEE by: Samapriya Roy

Keywords: ASTER, DEM, elevation, remote sensing, Water Bodies Database
