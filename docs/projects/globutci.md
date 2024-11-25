# High-Resolution Global Monthly Universal Thermal Climate Index (2000–2022)

GloUTCI-M is a global monthly dataset of the Universal Thermal Climate Index (UTCI) with high spatial resolution (1 km). The dataset is expressed in degrees Celsius (°C) and is stored as an integer type (Int16). To utilize it appropriately, one must divide the values by 100. Spanning from March 2000 to October 2022, this dataset integrates advanced machine learning models and multiple meteorological covariates to provide accurate assessments of thermal and cold stress. GloUTCI-M enhances research on human thermal comfort, urban climate, and environmental health by offering precise, detailed, and global-scale UTCI data.

The Universal Thermal Climate Index (UTCI) is an advanced biometeorological index that evaluates human thermal comfort by incorporating multiple meteorological variables, including temperature, wind speed, humidity, and solar radiation. Despite its growing use, existing UTCI datasets often lack the spatial resolution and temporal coverage necessary for localized and global studies. GloUTCI-M addresses these limitations by offering a globally comprehensive, high-resolution (1 km), monthly UTCI dataset covering 2000–2022. This dataset was developed using the CatBoost machine learning model, which demonstrated superior accuracy in predicting UTCI (MAE: 0.747°C; RMSE: 0.943°C; R²: 0.994) compared to XGBoost and LightGBM. The dataset also includes detailed spatial and temporal analyses, highlighting trends in thermal and cold stress at urban, regional, and global scales.The dataset is publicly available for download at [https://doi.org/10.5281/zenodo.8310513](https://doi.org/10.5281/zenodo.8310513). For additional information, refer to the associated publication [Yang et al., 2023](https://essd.copernicus.org/articles/16/2407/2024/essd-16-2407-2024.html).

#### Key Features
1. Temporal Coverage: March 2000 – October 2022
2. Spatial Resolution: 1 km
3. Geographical Scope: Global
4. Variables Included: UTCI derived from temperature, wind speed, humidity, and solar radiation

#### Citation

```
Yang, Z., Peng, J., Liu, Y., Jiang, S., Cheng, X., Liu, X., ... & Yu, X. (2024). GloUTCI-M: a global monthly 1 km Universal Thermal Climate Index dataset from 2000 to 2022.
Earth System Science Data, 16(5), 2407-2424. doi: https://doi.org/10.5194/essd-16-2407-2024
```

#### Dataset Citation

```
Zhiwei Yang, Jian Peng, & Yanxu Liu. (2023). GloUTCI-M: A Global Monthly 1 km Universal Thermal Climate Index Dataset from 2000 to 2022 [Data set].
Zenodo. https://doi.org/10.5281/zenodo.8310513
```

#### Earth Engine Snippet

```js
var gloutci = ee.ImageCollection("projects/sat-io/open-datasets/gloutci-m");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/GLOUTCI-MONTHLY

#### License

This dataset is made available under the CC BY 4.0 Attribution 4.0 International license. This license allows users to distribute, remix, adapt,
and build upon the material in any medium or format, so long as attribution is given to the creator.

Created by: Zhiwei Yang, Jian Peng, & Yanxu Liu. (2023)

Curated in GEE by : Samapriya Roy

Keywords: Universal Thermal Climate Index, Heat Stress, GloUTCI-M

Last updated on GEE: 2024-11-23
