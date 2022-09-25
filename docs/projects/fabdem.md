# FABDEM (Forest And Buildings removed Copernicus 30m DEM)

FABDEM (Forest And Buildings removed Copernicus DEM) removes building and tree height biases from the Copernicus GLO 30 Digital Elevation Model (DEM) (Airbus, 2020). The data is available at 1 arc second grid spacing (approximately 30m at the equator) for the globe. The authors use machine learning to
remove buildings and forests from the Copernicus Digital Elevation Model to produce, for the first time, a global map of elevation with buildings and forests removed at 1 arc second (∼30 m) grid spacing. You can [read the paper here](https://iopscience.iop.org/article/10.1088/1748-9326/ac4d4f/pdf) and the overall dataset can be [downloaded here](https://data.bris.ac.uk/data/dataset/25wfy0f9ukoge2gs7a5mqpq2j7)

Disclaimer: Parts or all of the dataset description is borrowed from existing description provided by authors.

#### Source Data structure
The data are in Geotiff format, with each file divided into 1x1 degree tiles. Files are divided into 10x10 degree zipped folders (detailed in Data structure section below). Files are labelled using the south-west corner of the tile. For example N51E005_FABDEM_V1-0.tif has an extent from 51-52 degrees N, 5-6 degrees E.

Zipped folders are labeled with the southwest corner to northeast corner. For example For example N10E010-N20E020_FABDEM_V1-0.zip has an extent from 10-20 degrees N, 10-20 degrees E.

#### Citation

```
Hawker, Laurence, Peter Uhe, Luntadila Paulo, Jeison Sosa, James Savage, Christopher Sampson, and Jeffrey Neal. "A 30m global map of elevation with
forests and buildings removed." Environmental Research Letters (2022).
```

![fabdem](https://user-images.githubusercontent.com/6677629/152706490-50cdf32a-df09-4c4c-a005-5c2668cfe96d.gif)

#### Earth Engine Snippet

```js
var fabdem = ee.ImageCollection("projects/sat-io/open-datasets/FABDEM");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:elevation-bathymetry/FABDEM

#### License

The FABDEM dataset is licensed under a [Creative Commons "CC BY-NC-SA 4.0" license](https://creativecommons.org/licenses/by-nc-sa/4.0/).

This is a non-commercial and ShareAlike license. In other words, FABDEM may not be used for commercial purposes, and if it is remixed, transformed or built upon you must redistribute your contributions under the same license.

When using the data, users must include the below statements, as per the requirement of the original license.

FABDEM is produced using Copernicus WorldDEM-30 © DLR e.V. 2010-2014 and © Airbus Defence and Space GmbH 2014-2018 provided under COPERNICUS by the European Union and ESA; all rights reserved. The organizations in charge of the Copernicus program by law or by delegation do not incur any liability for any use of the Copernicus WorldDEM-30

The original license can be found: https://docs.sentinel-hub.com/api/latest/static/files/data/dem/resources/license/License-COPDEM-30.pdf

Created by: Hawker, L., Uhe, P., Paulo, L., Sosa, J., Savage, J., Sampson, C., & Neal, J

Curated by: Samapriya Roy

Keywords: digital elevation model, bare-earth, terrain, remote sensing, machine learning
