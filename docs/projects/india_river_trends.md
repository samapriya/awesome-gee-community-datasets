# Temporal trends of Surface water across Indian Rivers & Basins

This dataset quantifies the extent and rate of annual change in surface water area (SWA) across India's rivers and basins
over 30 years from 1991 to 2020. It does so by season (annual dry, wet and permanent water, based on India's seasons) and at
two spatial scales: the river basin scale (1516 level-7 basins from HydroBASINS) and the finer river reach scale (68,367
reaches). This dataset is derived from the historical time series of monthly surface water occurrence by [JRC's Global
Surface Water Explorer](https://global-surface-water.appspot.com/). You can read additional [details about the dataset in
the paper](https://www.sciencedirect.com/science/article/pii/S2352340923010211) and access the [dataset here](https://zenodo.org/records/7803903).

The authors have also provided a dataset page and an earth engine app to [analyze the dataset further](https://sites.google.com/view/surface-water-trends-india/).

These are available as the following GEE assets

- Annual rate of change of surface water area, by season

    * Reaches: `projects/sat-io/open-datasets/indian_rivers/riverchanges/txsTrends`
    * Basins: `projects/sat-io/open-datasets/indian_rivers/riverchanges/basinsTrends`


??? example "Expand to show Attributes for Annual rate of change of surface water area feature collections"

    <center>

    | Attribute            | Description                                                                                                                                                                                                                                                                                                                                                                        |
    |---------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | HYBAS_ID or txId     | Feature's unique identifier. <ul><li>HYBAS_ID is for basins. It is the basin's identifier HYBAS_ID in the HydroBASINS dataset</li><li>txId is for transects. It is the '_' concatenated string derived from the longitude and latitude values, truncated to 4 decimals, of the transect's median point. Specifically, it is "_xx.xxxx_yy.yyyy_" where _xx.xxxx_ and _yy.yyyy_ are the median's longitude and latitude values truncated to 4 decimals.</li></ul> |
    | season               | Denotes the season, in "_sss_mmm_" format, where <ul><li>"_sss_" denotes the season: "_dry_" for dry, "_wet_" for wet and "_prm_" for permanent </li><li>"_mmm_" denotes the span of the season in calendar months: "_fma_" is for dry season of February-March-April, "_ond_" is for wet (post-monsoon) season of October-November-December and "_DnW_" is for permanent which is dry AND wet season. </li></ul>|
    | sl_perYr            | Regression slope of the surface water area vs. year Sen's slope regression analysis, and "_perYr_" denotes its units, per year. |
    | offset               | Regression offset of the surface water area vs. year Sen's slope regression analysis. |
    | tsPtCount            | Number of time-points included in the Sen's slope regression analysis. |
    | system:index         | GEE system-generated unique identifier. |



- Time series of annual surface water area, by season

    * Reaches: `projects/sat-io/open-datasets/indian_rivers/riverchanges/mainlandIndia_areasTs_txs`
    * Basins: `projects/sat-io/open-datasets/indian_rivers/riverchanges/mainlandIndia_areasTs_basinsL7`

??? example "Expand to show Attributes for Time series of annual surface water area feature collections"

    <center>

    | Attribute            | Description                                                                                                                                                                                                                                                                                                                                                                        |
    |---------------------:|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | HYBAS_ID or txId     | Feature's unique identifier. <br> - HYBAS_ID is for basins. It is the basin's identifier HYBAS_ID in the HydroBASINS dataset. <br> - txId is for transects. It is the '_' concatenated string derived from the longitude and latitude values, truncated to 4 decimals, of the transect's median point. Specifically, it is "_xx.xxxx_yy.yyyy_" where _xx.xxxx_ and _yy.yyyy_ are the median's longitude and latitude values truncated to 4 decimals. |
    | season               | Denotes the season, in "_sss_mmm_" format. <br> - "_sss_" denotes the season: "_dry_" for dry, "_wet_" for wet, and "_prm_" for permanent. <br> - "_mmm_" denotes the span of the season in calendar months: "_fma_" is for the dry season of February-March-April, "_ond_" is for the wet (post-monsoon) season of October-November-December, and "_DnW_" is for permanent which is dry AND wet season.               |
    | year               | Year.                                                                                                                                                                                                                                                                                                                                                                               |
    | water_ha            | Area of water pixels in the feature, in hectares.                                                                                                                                                                                                                                                                                                                                  |
    | notwater_ha        | Area of notwater pixels in the feature, in hectares.                                                                                                                                                                                                                                                                                                                               |
    | nodata_ha          | Area of nodata pixels in the feature, in hectares.                                                                                                                                                                                                                                                                                                                                 |
    | nodataFrac         | Proportion of the feature's area with nodata pixels.                                                                                                                                                                                                                                                                                                                               |
    | system:index      | GEE system-generated unique identifier.    |
                                                                                                                                                                                                                                                                                                                                             |
- Time series of annual surface water occurrence, by season: `projects/sat-io/open-datasets/indian_rivers/riverchanges/waterOccSeasComps`

??? example "Expand to show band information for Time series of annual surface water image collection"

    <center>

    | Bands             | Description                                                                                                       |
    |------------------:|:------------------------------------------------------------------------------------------------------------------|
    | drySeasCompos_fma | Each pixel in these bands have one of 3 integer values (following the convention in the JRC water dataset, Pekel et al. 2016) |
    |wetSeasCompos_ond  | * `2`: a pixel with valid data and containing water (denoting a "water" pixel)                                     |
    |prmSeasCompos_DnW  | * `1`: a pixel with valid data and not containing water (denoting a "notwater" pixel)                               |
    |                   | * `0`: a pixel with no valid data (denoting a "nodata" pixel)                                                       |


??? example "Expand to show attributes for Time series of annual surface water image collection"

    <center>

    | Properties | Description |
    |----------:|:------------|
    |year       | year of the image. |
    |monsoonYearStartMonth | Number (between 1-12) of the month when monsoon (or, hydrological) year starts. It is 6, indicating June, and is the same for all images. A year is taken to be June to May in this analysis. |
    |drySeasMonthsOffset | Number of months after `monsoonYearStartMonth` when dry season starts. It is 8, indicating February. |
    |drySeasMonthsTag    | Suffix tag, in names of image bands, table columns, etc., indicating the 3 months of the dry season. |
    |wetSeasMonthsOffset | Number of months after `monsoonYearStartMonth` when wet season starts. It is 4, indicating October. |
    |wetSeasMonthsTag    | Suffix tag, in names of image bands, table columns, etc., indicating the 3 months of the wet season. |

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

