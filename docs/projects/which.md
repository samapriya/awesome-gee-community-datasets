# WHiCH (Western Himalaya Canopy Height) Map 2020, Pakistan

The western Himalayas region is a key biodiversity hotspot and a habitat for several species. This region needs an accurate spatial assessment of tree canopy height for improved estimates of aboveground biomass, carbon sequestration, and related forest ecosystem services. The WHiCH (Western Himalaya Canopy Height) Map provides a 10 m spatial resolution canopy height map of the study region for the year 2020.

The dataset was produced using a deep convolution neural networks model, U-Net, for estimating canopy heights by fusing Global Ecosystem Dynamics Investigation Mission (GEDI) data with multi-band Sentinel-2 datasets. Overall, the model achieved a Root Mean Square Error (RMSE) of 7.52 m and a Mean Absolute Error (MAE) of 5.71 m on the test set, outperforming existing global canopy height models in this topographically challenging region. You can [read the paper here](https://doi.org/10.1016/j.jag.2025.105030)

#### Key Features and Details

* **Spatial Resolution:** 10 meters
* **Temporal Coverage:** 2020
* **Coverage:** Western Himalayas, Pakistan
* **Accuracy:** RMSE of 7.52 m, MAE of 5.71 m
* **Data Format:** Earth Engine Image
* **Additional Relevant Metrics:** Produced using a U-Net CNN with stratified training.
* **Pixel values represent the estimated canopy height in meters.**

#### Citation

```
Adeel Ahmad, Subhashree Sastry, Aashis Dhakal, Shishir Khanal, Alexander Levering, Hammad Gilani, Nathan Jacobs "Canopy Height Mapping in the Western Himalayas, Pakistan: A Deep Learning Approach using GEDI and Sentinel-2 Fusion"
International Journal of Applied Earth Observation and Geoinformation, 2025
https://doi.org/10.1016/j.jag.2025.105030
```

#### Earth Engine Snippet

```js
var WhiCH_Map = ee.Image("projects/sat-io/open-datasets/WHICH_MAP");

Map.setCenter(73.5, 34.5, 8);
Map.addLayer(WhiCH_Map, {min: 0, max: 40, palette:['#ffffcc', '#c2e699', '#78c679', '#31a354', '#006837']}, 'WHiCH Canopy Height 2020');
```

Sample Code:  https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/WHICH-CANOPY-HT

#### License

This dataset is licensed under a Creative Commons Attribution 4.0 International (CC-BY-4.0) license.

Keywords: Western Himalayas, Canopy height, U-net CNN, GEDI, Sentinel-2, Stratified training, Pakistan, Forestry

Curated in GEE by: Adeel Ahmad & Samapriya Roy

Last updated in GEE: 2025-03-06
