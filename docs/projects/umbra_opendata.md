# Umbra SAR Open Data

Umbra satellites generate the highest resolution SAR imagery ever offered commercially from space (better than 25 cm / 10 inches). SAR satellites can capture images at night, through cloud cover, smoke and rain. SAR is unique in its abilities to monitor changes. The Open Data Program (ODP) monitors ten diverse locations around the world. Updated frequently with new images. ODP enables users to analyze the time-series data to detect changes in each location.

#### Ciation

```
Umbra Synthetic Aperture Radar (SAR) Open Data was accessed on DATE from https://registry.opendata.aws/umbra-open-data.
```

#### Data subset
Only GEC data was selected from the available collections since they were already encoded as geotiffs. SAR GEC data is a geocoded product flattened to a single elevation to reduce visual distortions. It is analysis-ready, though it also contains layover and foreshortening.SAR GEC data is often taken as a post product processed from slant or ground range radar images. It contains amplitude information only.

![umbra_sample](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/9024368d-96db-40d2-ba2c-93771601276a)

#### Earth Engine Snippet

```js
var umbra_open = ee.ImageCollection('projects/sat-io/open-datasets/UMBRA/open-data');
var notoPeninsula = ee.ImageCollection('projects/sat-io/open-datasets/disaster/japan-earthquake-2024_UMBRA')
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-events-layers/UMBRA-OPENDATA

#### License

All Umbra data is provided to customers under a modified version of the Creative Commons Attribution 4.0 International (CC BY 4.0) license. Creative Commons, the nonprofit that created and maintains CC BY 4.0. While Umbra will always remain the underlying copyright holder for data provided to customers, our licensing strategy allows customers to i) Freely publish the data, with attribution, under the CC BY 4.0 license ii) Resell our data, at a profit, without paying a royalty to Umbra iii) Create derivative works, like analytics, and sell them at a profit (again, without paying a royalty to Umbra)

Provided by: Umbra

Curated in GEE by: Samapriya Roy

Keywords: UMBRA, SAR, GED, Open data

Last updated in GEE: 23/03/2023
