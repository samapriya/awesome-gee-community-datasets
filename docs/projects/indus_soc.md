# Mangrove Soil Organic Carbon Indus Delta, Pakistan

The Indus Delta in Pakistan is the world's largest arid mangrove forest system but lacks spatially explicit data on Soil Organic Carbon (SOC) despite its importance for conservation and carbon budgeting. This study establishes a baseline SOC map for 2020 at 10 m spatial resolution using Sentinel-1 (Synthetic Aperture Radar) and Sentinel-2 (MultiSpectral Instrument) satellite imagery, integrated with in-situ soil sampling. SOC predictions were made using a Classification and Regression Tree (CART) machine learning model within the Google Earth Engine platform, leveraging 40 predictor variables, including spectral bands and derived indices. The datasets are available for download at: https://zenodo.org/records/13824640

#### Dataset Description

A total of 53 topsoil (10 cm depth) samples were collected in February 2020 across the Indus Delta, and SOC was analyzed using the Walkley-Black method. The results showed an average SOC value of 67.59 ± 37.41 MgC ha⁻¹ (to 10 cm depth), and local values ranging from 15.07 to 138.04 MgC ha⁻¹, with a total of 0.91 PgC. The CART model demonstrated high accuracy, with an R² of 0.95 and an RMSE of 9.18 MgC ha⁻¹.

With the first high-resolution SOC map for the Indus Delta, this study provides valuable insights for ecosystem management, conservation planning, and carbon budgeting. The region faces challenges such as seawater intrusion and hypersalinity, which threaten its ability to sequester carbon. These findings have the potential to significantly influence initiatives like REDD+ and Blue Carbon projects.

#### Dataset Characteristics

<center>

| Parameter | Value |
|-----------|-------|
| Spatial Resolution | 10 meters |
| Coverage | Indus Delta, Pakistan (~8,000 km²) |
| Year | 2020 |
| SOC Range | 15.07 - 138.04 MgC ha⁻¹ |
| Mean SOC | 67.59 ± 37.41 MgC ha⁻¹ |
| Total Carbon Stock | 0.91 PgC |
| Model Accuracy | R² = 0.95, RMSE = 9.18 MgC ha⁻¹ |

</center>

#### Citation

```
Gilani, H., Shah, M., Ijaz, S. S., Asif, M., Nazir, A., & Hanan, N. P. (2025). Spatial distribution of mangrove soil organic carbon in Indus Delta, Pakistan:
A multi-sensor remote sensing and machine learning approach. Estuarine, Coastal and Shelf Science, 323, 109435.
https://doi.org/10.1016/j.ecss.2025.109435
```

#### Dataset Citation

```
Gilani, H., Shah, M., Sohail, S., Asif, M., & Nazir, A. (2024). Mapping Soil Organic Carbon in the World's Largest Arid Mangrove Forest
(Indus Delta, Pakistan): A Multi-Sensor Remote Sensing and Machine Learning Approach [Data set].
Zenodo. https://doi.org/10.5281/zenodo.13824640
```

![soc_layers](../images/indus_soc.gif)

#### Earth Engine Snippet

```javascript
// Load the Indus Delta Mangrove SOC datasets
var indus_delta_mangrove_soc = ee.Image('projects/sat-io/open-datasets/INDUS_DELTA_SOC/indusdelta_mangrove_soc2020');
var indus_delta_mangrove_soc_uncertainty = ee.Image('projects/sat-io/open-datasets/INDUS_DELTA_SOC/indusdelta_mangrove_soc_uncertainity2020');

// Center the map on the dataset
Map.centerObject(indus_delta_mangrove_soc, 8);

// Visualization parameters
var socVis = {
  min: 15,
  max: 138,
  palette: ['#d10019', '#ff8f51', '#fff6b6', '#a7d073', '#008134']
};

var uncertaintyVis = {
  min: 0,
  max: 100,
  palette: ['#FFFFFF', '#d10019']
};

// Add layers to map
Map.addLayer(indus_delta_mangrove_soc, socVis, 'Indus Delta Mangrove SOC (MgC ha⁻¹)');
Map.addLayer(indus_delta_mangrove_soc_uncertainty, uncertaintyVis, 'Indus Delta Mangrove SOC Uncertainty (%)', false);

// Print dataset information
print('SOC Dataset:', indus_delta_mangrove_soc);
print('Uncertainty Dataset:', indus_delta_mangrove_soc_uncertainty);

var snazzy = require("users/aazuspan/snazzy:styles");
snazzy.addStyle("https://snazzymaps.com/style/15/subtle-grayscale", "Greyscale");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:geophysical-biological-biogeochemical/INDUS-DELTA-MANGROVE-SOC

![indus_delta_soc](https://github.com/user-attachments/assets/soc-preview-image.png)

#### License

This dataset is available under Creative Commons Attribution (CC-BY) 4.0 International License.

Provided by: Gilani et al 2025

Keywords: Indus Delta, Mangrove, Soil Organic Carbon, SOC, Pakistan, Blue Carbon, Carbon Sequestration, Sentinel-1, Sentinel-2, Machine Learning, CART, Google Earth Engine

Curated in GEE by: Samapriya Roy

Last updated: 2025-08-05
