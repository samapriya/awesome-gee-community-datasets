# ASTER Global Digital Elevation Model (GDEM) v3

The first version of the ASTER GDEM, released in June 2009, was generated using stereo-pair images collected by the ASTER instrument onboard Terra. ASTER GDEM coverage spans from 83 degrees north latitude to 83 degrees south, encompassing 99 percent of Earth's landmass.

The improved GDEM V3 adds additional stereo-pairs, improving coverage and reducing the occurrence of artifacts. The refined production algorithm provides improved spatial resolution, increased horizontal and vertical accuracy. The ASTER GDEM V3 maintains the GeoTIFF format and the same gridding and tile structure as V1 and V2, with 30-meter postings and 1 x 1 degree tiles. You can read more about the product [in the user guide here](https://lpdaac.usgs.gov/documents/434/ASTGTM_User_Guide_V3.pdf)

Disclaimer: Parts or all of the dataset description is borrowed from existing description provided by authors.

#### Source Data structure
The data are in Geotiff format, with each file divided into 1x1 degree tiles. To allow for adding a single image instead of a collection output, the zip files were unzipped and a single composite tif file was generated.

#### Citation

```
NASA/METI/AIST/Japan Spacesystems, and U.S./Japan ASTER Science Team. ASTER Global
Digital Elevation Model V003. 2018, distributed by NASA EOSDIS Land Processes DAAC,
https://doi.org/10.5067/ASTER/ASTGTM.003
```

![gdem_global](https://user-images.githubusercontent.com/6677629/158051813-d20de8bb-f467-4024-be46-a225d6323a0c.gif)

#### Earth Engine Snippet

```js
var fabdem = ee.Image("projects/sat-io/open-datasets/ASTER/GDEM");
```

Sample Code: https://code.earthengine.google.com/7592ab36de453d718aab7291692abb88

#### License

All LP DAAC current data and products acquired through the LP DAAC have no restrictions on reuse, sale, or redistribution. This license can thus be treated similar to a public domain CC0 license. ASTER GDEM Version 3 (ASTGTM V003) was released on August, 5, 2019 and contains no redistribution requirements. The LP DAAC kindly requests that you properly cite the data in your research.

Created by:  NASA, METI, AIST, Japan Spacesystems and U.S./Japan ASTER Science Team

Curated in GEE by: Samapriya Roy

Keywords: ASTER, DEM, elevation, remote sensing
