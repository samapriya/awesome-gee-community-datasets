# Enhanced National-Scale Urban Tree Canopy Cover (CONUS)

The Enhanced National-Scale Urban Tree Canopy Cover Dataset provides an improved 30-meter resolution representation of tree canopy cover across all U.S. Census urban areas. This dataset applies random forest models to combine high-resolution land cover data with moderate-resolution National Land Cover Database (NLCD) Tree Canopy Cover and additional explanatory variables to create a more accurate representation of urban forest coverage.

The dataset represents tree canopy cover for all Census urban areas in the conterminous United States at 30-meter resolution, covering approximately 273,844 km² (about 3.6% of the conterminous U.S.). The model significantly improves upon the native NLCD Tree Canopy Cover product by addressing consistent underestimations in urban areas, adding an average of 13.4% more tree canopy cover across the sampled urban areas. The dataset values represent percentage tree canopy cover (0-100%) for Census urban areas. You can read [more details in the paper here](https://www.nature.com/articles/s41597-025-04816-0)

#### Key Features

- 30-meter resolution raster dataset of tree canopy cover percentage (0-100%)
- Coverage of all Census 2020 Urban Areas in the conterminous United States
- Base year 2011 (aligned with NLCD 2011 products)
- Improved accuracy compared to original NLCD tree canopy products
- Overall coefficient of determination (R²) of 0.747

#### Validation

The model demonstrated robust performance across multiple validation approaches:
- 1,000-fold cross validation: median R² of 0.752
- Urban area leave-one-out cross validation: median R² of 0.675
- Cross validation by Census block group median year built: median R² of 0.743

The enhanced dataset reduced RMSE by 32% and MAE by 31% on average compared to the native NLCD tree canopy cover product.

#### Citation

```
Corro, L.M., Bagstad, K.J., Heris, M.P., Ibsen, P.C., Schleeweis, K.G., Diffendorfer, J.E., Troy, A., Megown, K., and O'Neil-Dunne, J., 2025, An enhanced national-scale urban tree canopy cover dataset for the United States Data Release (2025): U.S. Geological Survey data release, https://doi.org/10.5066/P13LECKC.
```

#### Paper Citation

```
Corro, L.M., Bagstad, K.J., Heris, M.P. et al. An enhanced national-scale urban tree canopy cover dataset for the United States. Sci Data 12, 490 (2025). https://doi.org/10.1038/s41597-025-04816-0
```

#### Earth Engine Snippet

```js
// Enhanced Urban Tree Canopy Cover 2011
var enhancedTCC = ee.Image('projects/sat-op/open-datasets/USGS/EnhancedTCC2011');
```

Sample Code:  https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/USGS-US-TCC

#### License

This work is made available under Creative Commons Zero v1.0 Universal (https://creativecommons.org/publicdomain/zero/1.0/).

Keywords: urban forests, tree canopy, ecosystem services, land cover, urban planning, census urban areas, random forest models, spatial data

Created by: Corro et al. 2025

Curated in GEE by: Samapriya Roy

Last updated: 2025-03-24
