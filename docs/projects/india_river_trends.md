# Temporal trends of Surface water across Indian Rivers & Basins

This dataset quantifies the extent and rate of annual change in surface water area (SWA) across India's rivers and basins
over 30 years from 1991 to 2020. It does so by season (annual dry, wet and permanent water, based on India's seasons) and at
two spatial scales: the river basin scale (1516 level-7 basins from HydroBASINS) and the finer river reach scale (68,367
reaches). This dataset is derived from the historical time series of monthly surface water occurrence by [JRC's Global
Surface Water Explorer](https://global-surface-water.appspot.com/). You can read additional [details about the dataset in
the paper](https://www.sciencedirect.com/science/article/pii/S2352340923010211) and access the [dataset here](https://zenodo.org/records/7803903).

The authors have also provided a dataset page and an earth engine app to [analyze the dataset further](https://sites.google.com/view/surface-water-trends-india/).

These are available as the following GEE assets

* Annual rate of change of surface water area, by season
  
  * Reaches: `projects/sat-io/open-datasets/indian_rivers/riverchanges/txsTrends`
  * Basins: `projects/sat-io/open-datasets/indian_rivers/riverchanges/basinsTrends`
* Time series of annual surface water area, by season
  
  * Reaches: `projects/sat-io/open-datasets/indian_rivers/riverchanges/mainlandIndia_areasTs_txs`
  * Basins: `projects/sat-io/open-datasets/indian_rivers/riverchanges/mainlandIndia_areasTs_basinsL7`
    
* Time series of annual surface water occurrence, by season: `projects/sat-io/open-datasets/indian_rivers/riverchanges/waterOccSeasComps`

More details and resources:

| Published data repository (excluding the time series of annual surface water occurrence) | https://doi.org/10.5281/zenodo.7803903                    |
| ---------------------------------------------------------------------------------------: | :-------------------------------------------------------- |
|                                          Published Earth Engine code behind the analysis | https://doi.org/10.5281/zenodo.7839588                    |
|                                                               Published data description | https://doi.org/10.1016/j.dib.2023.109991                 |
|                                                      Interactive visualization, and more | https://sites.google.com/view/surface-water-trends-india/ |


#### Citation

```
Koulgi P, Jumani S. Dataset of temporal trends of surface water area across India's rivers and basins. Data Brief. 2023 Dec 19;52:109991.
doi: 10.1016/j.dib.2023.109991. PMID: 38235174; PMCID: PMC10792741.
```

![indian_basins](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/98ac274b-a30e-4c3f-b66c-0c31e7a54ceb)

#### Earth Engine Snippet if dataset already in GEE

```js
var reachTrends = ee.FeatureCollection('projects/sat-io/open-datasets/indian_rivers/riverchanges/txsTrends');
var reachAreaTimeseries = ee.FeatureCollection('projects/sat-io/open-datasets/indian_rivers/riverchanges/mainlandIndia_areasTs_txs');
var basTrends = ee.FeatureCollection('projects/sat-io/open-datasets/indian_rivers/riverchanges/basinsTrends');
var basAreaTimeseries = ee.FeatureCollection('projects/sat-io/open-datasets/indian_rivers/riverchanges/mainlandIndia_areasTs_basinsL7');
var annualWaterOccSeasComps = ee.ImageCollection('projects/sat-io/open-datasets/indian_rivers/riverchanges/waterOccSeasComps');

var brewer7ClPuOr = ['b35806', 'f1a340', 'fee0b6', 'f7f7f7', 'd8daeb', '998ec3', '542788'];
var empty = ee.Image().byte();

var reachTrendsDrySeason = reachTrends.filter(ee.Filter.eq('season', 'dry_fma'));
var fillsreach = empty.paint(reachTrendsDrySeason, 'sl_perYr');
Map.addLayer(fillsreach, {palette: brewer7ClPuOr, min: -0.02, max: 0.02}, 'dry_fma_reach');
Map.setCenter(79.49959, 16.63471, 14);

var basTrendDrySeason = basTrends.filter(ee.Filter.and(ee.Filter.eq('HYBAS_ID', 4071092530), ee.Filter.eq('season', 'dry_fma')));
var fillsBas = empty.paint(basTrendDrySeason, 'sl_perYr');
Map.addLayer(fillsBas, {palette: brewer7ClPuOr, min: -75, max: 75}, 'dry_fma_bas', false);
```

Sample code:  https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/TEMPORAL-TRENDS-INDIAN-RIVERS-BASINS

Earth Engine app: Access the [Earth Engine app here](https://pradeepkoulgi.users.earthengine.app/view/india-changing-rivers-and-basins) and the [data page here](https://sites.google.com/view/surface-water-trends-india/)

#### License

These datasets are provided under a CC-BY-4.0 license.

Provided by: Koulgi and Jumani 2023

Curated in GEE by: Pradeep Koulgi and Samapriya Roy

Keywords : surface water, river reaches, river basins, time series,india

Last updated on GEE: 2024-02-16

