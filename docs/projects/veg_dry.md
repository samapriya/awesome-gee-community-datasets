# Vegetation dryness for western USA

This dataset shows how dry or wet the vegetation is in western US. The dataset is available at 15-day temporal resolution and 250 m spatial resolution. It spans April 2016 to present.

The variable contained in the maps is live fuel moisture content. It is defined as the mass of water per unit mass of live biomass (expressed as a percentage quantity). For e.g., if a pixel value = 150, it means that the vegetation in that pixel has 1.5 Kg of water for every 1 Kg of live biomass. Live fuel moisture content was estimated from a deep learning model trained using Sentinel-1 C-band backscatter, Landsat-8 optical reflectance, and various other land surface characteristics like canopy height, soil texture, etc.

#### Citation

```
Rao, K., Williams, A.P., Flefil, J.F. & Konings, A.G. (2020). SAR-enhanced mapping
of live fuel moisture content. Remote Sensing of Environment, 245, 111797.
DOI: 10.1016/j.rse.2020.111797
```

Read the [paper here](https://www.sciencedirect.com/science/article/pii/S003442572030167X)

<p align="center">
  <img width="360" src="https://github.com/kkraoj/lfmc_from_sar/blob/master/figures/lfmc_2_panels_projected_annotated.gif?raw=true" alt="Seasonal variation of live fuel moisture content estimated by our deep learning model.">
</p>

#### Earth Engine Snippet

**Asset Link**

```js
var asset_name = ee.ImageCollection("users/kkraoj/lfm-mapper/lfmc_col_25_may_2021")
```

**Sample Code**

This script imports and visualizes average vegetation dryness for 2019,
[go to script](https://code.earthengine.google.com/02f3f4401475dc5081ce707e37bdeac9)

```js
var start_date = '2019-01-01';
var end_date =  '2019-12-31';

// Import LFMC collection
var collection = ee.ImageCollection('users/kkraoj/lfm-mapper/lfmc_col_25_may_2021')
  .filterDate(start_date,end_date)

var image = collection.mean(); //calculate mean for the selected date range
var palette_lfmc = ['#703103','#945629','#ce7e45', '#df923d', '#f1b555', '#fcd163', '#99b718',
          '#74a901', '#66a000', '#529400', '#3e8601', '#207401', '#056201',
          '#004c00', '#023b01', '#012e01'
          , '#011d01', '#011301'];

Map.addLayer(image, {min: [50], max: [200], palette: palette_lfmc, opacity: 0.95}, 'LFMC mean');
Map.setCenter(-113.03, 38, 5);

```

**Earth Engine App** https://kkraoj.users.earthengine.app/view/live-fuel-moisture

**Earth Engine App Code** https://code.earthengine.google.com/e6b336fa58124f4f8cda2b3be76d156f

#### License Information

[CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) Under which you can copy and redistribute the material in any medium or format.

Created and Curated by: KrishnaRao, A. ParkWilliams, Jacqueline Fortin Flefil, Alexandra G.Konings

Keywords: vegetation, dryness, drought, wildfire, USA, live fuel moisture content

Last updated: 2021-06-29
