# STaPL: Annual 30-m Tillage Maps for the U.S. Midwest (2001–2023)

Improved data on conservation practices in agriculture is critical for understanding their impacts on crop productivity, environmental outcomes, and climate resilience. Despite ongoing adoption of conservation tillage across the U.S. Midwest, public information has historically been limited to coarse estimates updated once or twice per decade. Here we present the STaPL (Scale Transfer with Pseudo-Labelling) tillage dataset annual 30-m resolution maps of tillage intensity (low-intensity and high-intensity) for corn and soybean cropland across twelve U.S. Midwestern states from 2001 to 2023. The STaPL framework combines Landsat earth observations, elevation data, and publicly available county-level tillage census statistics to generate pseudo-labels for field-level tillage classification without requiring any ground-truth field data. The dataset is the first of its kind to produce annual, field-scale tillage maps spanning more than two decades without reliance on proprietary ground records. Read the [paper and details here](https://doi.org/10.1016/j.rse.2026.115500).

#### Citation

```
Ma, Y., Shen, Y., Swatantran, A., Kelly, C., Lobell, D.B., 2026. STaPL: Scale Transfer with
Pseudo-Labelling for satellite-based mapping of agricultural practices. Remote Sensing of
Environment 343, 115500. https://doi.org/10.1016/j.rse.2026.115500
```

#### Data Coverage & Band Description

The annual STaPL tillage maps cover 12 states in the U.S. Midwest — Illinois (IL), Indiana (IN), Iowa (IA), Kansas (KS), Michigan (MI), Missouri (MO), Minnesota (MN), Nebraska (NE), North Dakota (ND), Ohio (OH), South Dakota (SD), and Wisconsin (WI) — at 30-m spatial resolution. Only corn and soybean pixels are mapped. Each annual image contains three bands:

| Band | Description |
|------|-------------|
| **Tillage** | Tillage type: `0` = high-intensity tillage (< 30% crop residue), `1` = low-intensity tillage (≥ 30% crop residue) |
| **Number** | Number of available cloud-free Landsat observations during April–June. Higher observation counts generally correspond to higher classification accuracy. |
| **Filled_Flag** | Gap-fill indicator: `1` if the pixel was missing and filled using the tillage value from an adjacent year (Year X–1 or Year X+1); `0` otherwise. |

Maps are named by year — e.g., `STAPL_2022` for the 2022 tillage map.

#### Technical Validation

Model performance was evaluated against the Corteva ground-based tillage dataset, which contains 25,536 field-year samples with verified tillage operation records collected across the twelve Midwestern states from 2016 to 2023. The STaPL Random Forest classifier achieved an overall accuracy of 75%, a weighted F1 of 74.81%, and a macro-F1 of 73.06% — comparable to field-supervised models trained on thousands of ground-truth records. Class-wise, STaPL performs better on detecting low-intensity tillage (F1 = 80.29%) than high-intensity tillage (F1 = 65.82%).

When aggregated to the county level, STaPL maps show strong agreement with official USDA and CTIC tillage statistics (r² = 0.65, RMSE = 0.19). Agreement improves substantially at the state level (r² = 0.83, RMSE = 0.12), confirming that STaPL captures both field-scale variability and broad spatial trends reliably.

Classification accuracy improves with greater Landsat data availability — reaching approximately 78% when more than 13 cloud-free observations are available during the April–June window — underscoring the importance of temporal observation density for tillage detection.

![stapl_tillage](../images/stapl_tillage.png)

#### Earth Engine Snippet

```js
var stapl_collection = ee.ImageCollection('projects/sat-io/open-datasets/lobell-lab/STAPL-TILLAGE');
var tillage_2023= stapl_collection.filterDate('2023-01-01','2023-12-31')

Map.setCenter(-93.5, 42.0, 6);
Map.addLayer(tillage_2023.select('Tillage'), {min: 0, max: 1, palette: ['#3b0764', '#fde047']}, 'Tillage 2023');

var snazzy = require("users/aazuspan/snazzy:styles");
snazzy.addStyle("https://snazzymaps.com/style/38/shades-of-grey", "Greyscale");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/STAPL-TILLAGE

#### License & Usage

The STaPL Tillage Maps are licensed under [CC-BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). They are freely available for academic purposes or individual research but restricted for commercial use. You must give appropriate credit, provide a link to the license, and indicate if changes were made. Any adaptations must be distributed under the same license.

GitHub Page: https://github.com/yuchima8/STaPL

Created by: Yuchi Ma, Yawen Shen, Anu Swatantran, Courtland Kelly, David B. Lobell (Stanford University & Corteva Agriscience)

Curated in GEE by: Samapriya Roy

Keywords: Tillage, Conservation Agriculture, Landsat, Crop Residue, Scale Transfer, Pseudo-Labelling, U.S. Midwest, Corn Belt, Random Forest

Last updated: 2026-06-01
