# Global Natural and Planted Forests

The **Global Natural and Planted Forests** dataset offers a high-resolution (30-meter) map distinguishing natural from planted forests worldwide as of 2021. Created using over 70 million training samples generated from 30-meter Landsat images (1985–2021), this dataset supports improved environmental monitoring and conservation efforts, carbon sequestration assessment, and biodiversity management. The data includes rich spectral, structural, textural, and topographic attributes, enabling users to identify forest types and quantify forest coverage across various spatial scales.

#### Data Generation and Classification
The dataset leverages a time-series change detection method applied to Landsat imagery, distinguishing planted forests from natural forests based on disturbance frequency. Using a locally adaptive random forest classifier (RF), this method achieved an overall accuracy of 85% when validated against independently interpreted reference data. This high precision makes the dataset an effective tool for global forest resource assessment.

#### Key Features
- **Resolution**: 30-meter spatial resolution
- **Temporal Range**: Training samples span 1985–2021; map output is for 2021.
- **Training Samples**: Over 70 million samples generated based on disturbance frequency, drawn from Landsat and auxiliary data.
- **Accuracy**: 85% when compared to independent visual reference data.
- **Data Representation**: RGB map where:
  - Green pixels represent natural forests,
  - Yellow pixels indicate planted (artificial) forests,
  - Other colors represent non-forest areas.

#### Access and Citation
The dataset is publicly available and can be accessed via:
- [Primary Data Source](https://doi.org/10.5281/zenodo.10701417)
- [Supplemented Tiles 300–400](https://doi.org/10.5281/zenodo.13759567)

#### Citation

```
Xiao, Yuelong, Qunming Wang, and Hankui K. Zhang. "Global Natural and Planted Forests Mapping at Fine Spatial Resolution of 30 m."
Journal of Remote Sensing 4 (2024): 0204.
```

#### Dataset Citation

```
Xiao, Y. (2024). Global Natural and Planted Forests Mapping at Fine Spatial Resolution of 30 m [Data set].
Zenodo. https://doi.org/10.5281/zenodo.10701417
```

![global_ftype](https://github.com/user-attachments/assets/f2668b0a-e4cb-4569-b81b-bc812518b1bf)

#### Earth Engine Snippet

```js
var global_forest_types = ee.ImageCollection("projects/sat-io/open-datasets/GLOBAL-NATURAL-PLANTED-FORESTS");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/GLOBAL-NATURAL-PLANTED-FORESTS

#### License

This dataset is licensed under a Creative Commons Attribution 4.0 International license.

Provided by: Xiao et al 2024

Curated in GEE by: Samapriya Roy

Keywords: Global Forest Mapping, Natural and Planted Forests, Carbon Sequestration, Forest Cover Classification,  Biodiversity Monitoring, Forest Disturbance, Random Forest Classifier

Last updated in GEE: 2024-10-27
