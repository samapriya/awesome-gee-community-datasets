# Global Renewables Watch Temporal Dataset of Solar and Wind Energy

A comprehensive global temporal dataset of commercial solar photovoltaic (PV) farms and onshore wind turbines, derived from high-resolution satellite imagery analyzed quarterly from the fourth quarter of 2017 to the second quarter of 2024. This dataset was created by training deep learning-based segmentation models to identify renewable energy installations from satellite imagery, deployed across over 13 trillion pixels covering the world. For each detected feature, the dataset includes estimated construction dates and preceding land use types.

The final spatial dataset includes 375,197 individual wind turbines and 86,410 solar PV installations, offering crucial insights into progress toward sustainable development goals. Country-level capacity estimates show strong correlation with IRENA's 2023 estimates, with R² values of 0.96 for solar PV and 0.93 for onshore wind.

Data is available for download from [GitHub releases](https://github.com/microsoft/global-renewables-watch/releases/tag/v1.0)

#### Methodology

Dataset created using deep learning on PlanetScope imagery (4.7m/px) from 2017 Q4 to 2024 Q2. Solar detection uses U-Net segmentation, wind uses FCN with localization-based counting. Training data sourced from OpenStreetMap with iterative cleaning. Validated against IRENA 2023 data (Solar r²=0.96, Wind r²=0.93).

#### Properties

|Property          |Solar (Polygons) |Wind (Points)    |
|------------------|-----------------|-----------------|
|geometry          |Installation area|Turbine centroid |
|area_m2           |✓                |—                |
|construction_date |Quarter estimate (e.g., "2020 Q3")|Quarter estimate |
|land_cover_2018   |ESA CCI class    |ESA CCI class    |
|country_code      |ISO3             |ISO3             |

#### Paper Citation

```
Robinson, C., Ortiz, A., Kim, A., Dodhia, R., Zolli, A., Nagaraju, S.K., Oakleaf, J.,
Kiesecker, J. and Ferres, J.M.L. Global Renewables Watch: A Temporal Dataset of Solar
and Wind Energy Derived from Satellite Imagery. arXiv preprint arXiv:2503.14860 (2025).
https://arxiv.org/abs/2503.14860
```

![grw](../images/grw.gif)

#### Earth Engine Snippet

```js
var wind = ee.FeatureCollection("projects/sat-io/open-datasets/GRW/WIND_V1");
var solar = ee.FeatureCollection("projects/sat-io/open-datasets/GRW/SOLAR_V1");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/GLOBAL-RENEWABLES-WATCH

#### License

This dataset is made available under the MIT License. Pre-trained models and inference code are available in the [GitHub repository](https://github.com/microsoft/global-renewables-watch).

Provided by: Robinson et al 2025, Microsoft AI for Good Research Lab & The Nature Conservancy

Curatedin GEE by: Samapriya Roy

Keywords: renewable energy, solar photovoltaic, wind turbines, satellite imagery, deep learning, temporal analysis, land use change, climate, sustainability

Last updated in GEE: 2025-12-03
