# Copernicus Digital Elevation Model (GLO-30 DEM)

The Copernicus DEM is a Digital Surface Model (DSM) which represents the surface of the Earth including buildings, infrastructure and vegetation. We provide two instances of Copernicus DEM named GLO-30 Public and GLO-90. GLO-90 provides worldwide coverage at 90 meters. GLO-30 Public provides limited worldwide coverage at 30 meters because a small subset of tiles covering specific countries are not yet released to the public by the Copernicus Program. Note that in both cases ocean areas do not have tiles, there one can assume height values equal to zero. Data is provided as Cloud Optimized GeoTIFFs and was downloaded from the [Amazon Open Registry](https://registry.opendata.aws/copernicus-dem/). You can read the [documentation here](https://copernicus-dem-30m.s3.amazonaws.com/readme.html)

#### Citation

```
Copernicus Digital Elevation Model (DEM) was accessed on DATE from
```

![glo30](https://user-images.githubusercontent.com/6677629/153137961-1f1879cf-3ca9-44ff-afed-0e40bcd1dba6.gif)

#### Earth Engine Snippet

```js
var glo30 = ee.ImageCollection("projects/sat-io/open-datasets/GLO-30");
```

Sample Code: https://code.earthengine.google.com/f6479dc43ab9c13dd1cc9bd527cf0c01

Earth Engine comparison app: https://samapriya.users.earthengine.app/view/glob-elevation

#### License
GLO-30 Public is available on a free basis for the general public under the terms and conditions of the [license found here.](https://docs.sentinel-hub.com/api/latest/static/files/data/dem/resources/license/License-COPDEM-30.pdf)

© DLR e.V. 2010-2014 and © Airbus Defence and Space GmbH 2014-2018 provided under COPERNICUS by the European Union and ESA; all rights reserved.

#### Disclaimer
The organisations in charge of the Copernicus programme by law or by delegation do not incur any liability for any use
of the Copernicus WorldDEM-30.See Article 6(c) in https://docs.sentinel-hub.com/api/latest/static/files/data/dem/resources/license/License-COPDEM-30.pdf


Created by: European Space Agency, COPERNICUS

Curated in GEE by: Samapriya Roy

Keywords: digital elevation model, terrain, remote sensing, esa, copernicus
