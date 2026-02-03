# Global Surface Water Transitions (1984-2022)

This dataset provides the first global analysis of surface water transition timing at annual resolution, tracking when and where water bodies have advanced or receded from 1984 to 2022. Using Landsat satellite imagery and novel algorithms developed for Google Earth Engine, this dataset identifies persistent changes in surface water features by filtering out seasonal or shorter-term fluctuations. The dataset captures transitions across diverse water environments including rivers, lakes, reservoirs, flooded agriculture, and coastal regions.

Each 30m×30m pixel records whether water advance or recession occurred and specifies the year of transition. Unlike previous global surface water datasets that focus on net changes over multi-decade periods, this dataset emphasizes the timing of transitions, enabling clearer assessment of causation by linking surface water changes to their driving factors. The dataset reveals both natural processes (river meandering, delta dynamics, floodplain evolution) and anthropogenic interventions (dam construction, land reclamation, agricultural expansion), with human interventions typically driving rapid transitions while natural processes show more gradual patterns.

The dataset demonstrates high accuracy with a Mean Absolute Percentage Error (MAPE) of 14.9%, coefficient of determination (R²) of 0.80, and Critical Success Index (CSI) of 96.7%. Coastal regions and lakes show the highest accuracy (MAPE: 12.7-15.9%, CSI: 96-98.9%), while rivers also demonstrate strong performance (MAPE: 15.5%, CSI: 95.5%). Water advance events are detected with higher precision than recession events, with exact year matches in 26.5% of advance cases and 19.2% of recession cases, improving to 64.5% and 46.3% respectively within ±1 year tolerance.

You can read the [open access paper here](https://www.nature.com/articles/s41597-025-06013-5) and download the data and supplementary materials from [Figshare](https://springernature.figshare.com/articles/dataset/Surface_Water_Transitions_1984-2022_A_Global_Dataset_at_Annual_Resolution/28138643/1).

#### Dataset Structure

**Raster Bands:**
- **Band 1 (b1):** Year of water advance (1984-2022) - pixels that transitioned from dry to persistently wet
- **Band 2 (b2):** Year of water recession (1984-2022) - pixels that transitioned from wet to persistently dry

**Spatial Resolution:** 30m × 30m (Landsat resolution)

**Temporal Coverage:** 1984-2022 (38 years)

**Temporal Resolution:** Annual (year of transition)

#### Citation

```
Nagel, G.W., Darby, S.E. & Leyland, J. Surface Water Transitions 1984–2022: A Global Dataset at Annual Resolution.
Scientific Data 12, 1729 (2025). https://doi.org/10.1038/s41597-025-06013-5
```

![swt](../images/swt.png)

#### Earth Engine Snippet

```js
// Load the Surface Water Transitions ImageCollection and get median composite
var waterTransitions = ee.ImageCollection('projects/sat-io/open-datasets/SURFACE_WATER_TRANSITIONS').median();

// Extract individual bands
var waterAdvance = waterTransitions.select('b1');  // Year of water advance
var waterRecession = waterTransitions.select('b2'); // Year of water recession

// Load color palettes
var palettes = require('users/gena/packages:palettes');
var advancePalette = palettes.kovesi.linear_blue_5_95_c73[7];
var recessionPalette = palettes.kovesi.linear_kry_5_95_c72[7];

// Visualization parameters
var advanceViz = {
  min: 1984,
  max: 2022,
  palette: advancePalette
};

var recessionViz = {
  min: 1984,
  max: 2022,
  palette: recessionPalette
};

// Add layers to map
Map.addLayer(waterAdvance, advanceViz, 'Water Advanced (Year of Transition)', false);
Map.addLayer(waterRecession, recessionViz, 'Water Receded (Year of Transition)', false);

// Center on area of interest (example: Ganges Delta)
Map.setCenter(90.9074, 22.4508, 10);

// Print information about the dataset
print('Water Transitions Dataset:', waterTransitions);
print('Bands:', waterTransitions.bandNames());
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/GLOBAL-SURFACE-WATER-TRANSITIONS

Interactive App: https://ee-gustavoonagel.projects.earthengine.app/view/water-change-time-detection

#### License

This work is licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Curated by: Gustavo Willy Nagel, Stephen E. Darby, Julian Leyland (University of Southampton)

Curated in GEE by: Gustavo Willy Nagel and Samapriya Roy

Keywords: Surface water, Water dynamics, Rivers, Lakes, Reservoirs, Wetlands, Erosion, Sedimentation, Dams, Water resources, Hydrology, Coastal change, Climate change, Land use change, Remote sensing, Landsat, Time series analysis, Floodplains, Deltas, River meandering

Last updated: 2026-02-03
