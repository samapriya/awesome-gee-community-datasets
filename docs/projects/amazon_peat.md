# Amazonian Peatland Extent

Tropical peatlands represent some of the most carbon-dense terrestrial ecosystems on the planet, playing a significant role in the global carbon cycle. However, substantial uncertainty exists in estimating their global extent and carbon storage potential. This dataset provides the first field-data-driven model of peatland distribution across the Amazon basin, developed using 2,413 ground reference points and a random forest model applied to a combination of remote sensing products.

The model predicts an Amazonian peatland extent of approximately 251,015 km² (95th percentile confidence interval: 128,671–373,359 km²), which is larger than that of the Congo Basin but 30% smaller than other recent model-based estimates. The dataset addresses key spatial gaps in ground reference data, particularly in regions like Brazil and Bolivia, where uncertainty remains high. The model highlights peatland areas with varying degrees of confidence, such as northern Peru, the Rio Negro basin, and Bolivia, providing a critical resource for future research and field validation efforts. You can read the paper [here](https://iopscience.iop.org/article/10.1088/1748-9326/ad677b/pdf) and download the [datasets here](https://zenodo.org/records/13142590)

**Data Highlights**

* Model Type: Random forest-based prediction using field reference points and remote sensing data.
* Spatial Extent: Amazon basin, including northern Peru, Rio Negro basin, southwestern Orinoco basin, and Bolivia.
* Predicted Peatland Extent: 251,015 km² (95% CI: 128,671–373,359 km²).
* Model Performance: High confidence in certain areas like northern Peru; higher uncertainty in regions like Brazil, Bolivia, and the Rio Negro basin.
* Field Reference Points: 2,413 ground points in and around Amazonian peatlands.
* Predicted extent of Peat (organic soil of ≥ 30 cm thickness) across the study area (Amazon basin below 500 m and mean annual precipitation >1,390 mm) at 90 m resolution.

#### Citation

```
Hastie, A., Householder, J. E., Coronado, E. N. H., Pizango, C. G. H., Herrera, R., Lähteenoja, O., de Jong, J., Winton, R. S., Corredor, G. A. A., Reyna, J., Montoya,
E., Paukku, S., Mitchard, E. T. A., Åkesson, C. M., Baker, T. R., Cole, L. E. S., Oroche, C. J. C., Dávila, N., Águila, J. D., … Lawson, I. T. (2024). A new data-driven map
predicts substantial undocumented peatland areas in Amazonia. Environmental Research Letters, 19(9), 094019. https://doi.org/10.1088/1748-9326/ad677b
```

![amazon_peat](https://github.com/user-attachments/assets/9c3a9969-0c2e-4f7c-9215-a23d6ce8332c)

#### Earth Engine Snippet

```js
var Simple_AOI = ee.FeatureCollection("users/adamhastie50/Study_area_simplify");
var Amazon_peat_map = ee.Image("projects/sat-io/open-datasets/INT_Amazon_peat_map");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:regional-landuse-landcover/AMAZONIA-PEATMAP

#### License
The datasets are available under a Creative Commons Attribution 4.0 International license.

Created by: Hastie et al 2024

Curated in GEE by: Hastie et al 2024 and Samapriya Roy

Keywords: Peat, Tropical Peat, Amazon basin

Last updated in GEE: 2024-10-21
