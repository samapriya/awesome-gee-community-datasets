# Global Soil Salinity Maps (1986-2016)

This dataset includes global soil salinity layers for the years 1986, 1992, 2000, 2002, 2005, 2009 and 2016. The maps were generated with a random forest classifier that was trained using seven soil properties maps, thermal infrared imagery and the ECe point data from the WoSIS database. The validation accuracy of the resulting maps was in the range of 67–70%. The total area of salt affected lands by our assessment is around 1 billion hectares, with a clear increasing trend. Further details are provided in a peer-reviewed journal article (https://doi.org/10.1016/j.rse.2019.111260). The main data page for this [dataset can be found here](https://data.isric.org/geonetwork/srv/eng/catalog.search;jsessionid=9251411A3E92851C12FAA0C06EB6745F#/metadata/c59d0162-a258-4210-af80-777d7929c512) along with links to the VRT and tiff files.


#### Paper Citation

```
Ivushkin, Konstantin, Harm Bartholomeus, Arnold K. Bregt, Alim Pulatov, Bas Kempen, and Luis De Sousa. "Global mapping of soil salinity change."
Remote sensing of environment 231 (2019): 111260.
```

![soil_salinity](https://user-images.githubusercontent.com/6677629/145707831-e5e9fbd3-c9e5-4581-a5f8-bd31395781c0.gif)

#### Earth Engine Snippet

```js
var soil_salinity = ee.ImageCollection("projects/sat-io/open-datasets/global_soil_salinity");
```

Sample Code: https://code.earthengine.google.com/eb155a39ed8a1ec45fe9f85534d5794c

#### License

This work is licensed under the Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0). Users are free to use, copy, distribute, transmit, and adapt the work for commercial and non-commercial purposes, without restriction, as long as clear attribution of the source is provided.

Created by: Ivushkin et al

Curated by: Samapriya Roy

Keywords: : salinity, digital soil mapping, electrical conductivity, global map, soilgrids, landsat, thermal, salinisation

Last updated: 2021-11-25
