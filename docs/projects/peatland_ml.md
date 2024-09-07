# Global Peatland Fractional Coverage

Peatlands, as waterlogged terrestrial wetland ecosystems, store vast amounts of soil carbon and freshwater, playing a crucial role in the global carbon and hydrologic cycles. The **Peat-ML** dataset is a spatially continuous **global map of peatland fractional coverage** generated using machine learning models trained with climate, geomorphological, soil data, and **remotely-sensed vegetation indices**. Available peatland coverage maps from 14 regions, along with non-peatland ecoregions, were used to develop a statistical model with an average **r-squared of 0.73** and errors of **9.11%** (root mean square) and **-0.36%** (bias). The dataset is available in **NetCDF format** and published in **2021**. For more information, you can access the associated research paper [here](https://gmd.copernicus.org/articles/15/4709/2022/).

The original datasets are available as NetCDF with a model accuracy with R² = 0.73, RMSE = 9.11%, MBE = -0.36%. You can download [the Peat-ML Dataset (2021) here](https://zenodo.org/records/7352284). Additional details are available in the paper [Melton et al., 2022](https://gmd.copernicus.org/articles/15/4709/2022/)

<center>

![Workflow for Peat-ML](https://github.com/samapriya/awesome-gee-community-datasets/assets/57500332/f2733723-c8ac-44bf-afc7-ad689017e9cb)

*Workflow for dataset generation (Joe R. Melton et al., 2022)*

</center>

<center>

![Peatland Distribution Indonesia](https://github.com/samapriya/awesome-gee-community-datasets/assets/57500332/b5245da1-b232-4158-a455-3b475b13f52a)
*Example data visualization of peatland distribution in Indonesia*

</center>

#### Citation

```
Melton, J. R., Chan, E., Millard, K., Fortier, M., Winton, R. S., Martín-López, J. M., Cadillo-Quiroz, H., Kidd, D., and Verchot, L. V.: A map of
global peatland extent created using machine learning (Peat-ML), Geosci. Model Dev., 15, 4709–4738, https://doi.org/10.5194/gmd-15-4709-2022, 2022.
```

#### Dataset Citation

```
Melton, J. R., Chan, E., Millard, K., Fortier, M., Winton, R. S., Martín-López, J. M., Cadillo-Quiroz, H., Kidd, D., & Verchot, L. V. (2021). A map
of global peatland extent created using machine learning (Peat-ML) [Data set]. In Geoscientific Model Development (1.0).
Zenodo. https://doi.org/10.5281/zenodo.7352284
```

#### Earth Engine Snippet

```js
// Load administrative boundaries for Indonesia
var admin1 = ee.FeatureCollection("projects/sat-io/open-datasets/geoboundaries/HPSCGS-ADM1");
var geometry = admin1.filter(ee.Filter.eq('shapeGroup', 'IDN'));

Map.centerObject(geometry, 4);
Map.setOptions("Hybrid");

var peat = ee.Image("projects/sat-io/open-datasets/ML-GLOBAL-PEATLAND-EXTENT")
    .clip(geometry)
    .unmask();

// Display the results
Map.addLayer(peat.clip(geometry),
  {min: 0, max: 100, palette: ['#f7fcf5', '#c7e9c0', '#74c476', '#238b45', '#00441b']},
  'Peatland Distribution', true
  );
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/GLOBAL-PEATLAND-FRACTIONAL-COVER

#### License
These datasets are provided under a Creative Commons Attribution 4.0.

#### Keywords
peatland, soil carbon, wetland, ecosystem

Provided by: Melton et al 2022

Curated in GEE by: Samapriya Roy

Last updated in GEE: 2024-07-14
