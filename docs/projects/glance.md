# Global Land Cover Estimation (GLanCE)

The Global Land Cover Estimation (GLanCE) dataset provides high-quality, long-term records of annual land cover and land cover change from 2001 to 2019, using Landsat imagery at 30-meter spatial resolution. The dataset covers all global land areas except Antarctica, and includes 10 Science Data Sets (SDSs) that track land cover, land cover changes and greenness dynamics. The Continuous Change Detection and Classification (CCDC) algorithm is used to identify land cover and changes based on all available, clear Landsat observations.

The GLanCE SDSs are organized into three categories:

1. **Land Cover and Change**: Four SDSs provide information related to: (1) land cover class, (2) estimated quality associated with land cover class,  (3) previous land cover for those places where change occurred, and (4) the approximate day of year of change (DOY).
2. **Greenness Dynamics**: Four SDSs characterize annual greenness using the Enhanced Vegetation Index (EVI2), including (1) median, (2) amplitude, (3) rate of change (if present), and (4) magnitude of change in EVI2 median  for those pixels where change occurred.
3. **Leaf Type and Phenology**: Two SDSs identify leaf type and phenology for tree-covered pixels.

Version 1 data includes seven layers and their  corresponding band names. Note that these band names differ slightly from those listed in the user guide on the LP DAAC website.

This table shows the layer names and their corresponding band names from Version 1 data.

<center>

| **Layer Name**        | **Band Name**     |
|-----------------------|-------------------|
| Land Cover Class       | LC                |
| Previous Class         | prevClass         |
| Change Date            | changeDate        |
| EVI2 Median            | EVI2median        |
| EVI2 Amplitude         | EVI2amplitude     |
| EVI2 Rate              | EVI2rate          |
| Change EVI2 Median     | changeMag         |

</center>

The user manual with more detailed information about each data layer can be found [here.](https://lpdaac.usgs.gov/documents/1567/GLanCE_User_Guide_v1.pdf)

#### Notes
- The current dataset includes data for the Americas, Europe and Oceania. Africa and Asia will be released early in 2025.
- Land cover quality assurance layer will be provided in the next map release (e.g. v1.1)
- Tree leaf type and phenology datasets will be provided in future releases.
- The Google Earth Engine dataset uses a different tiling system designed for simplicity and efficiency in the platform, and is stored using the World Geodetic Coordinate System 1984 (EPSG:4326), matching the underlying CCDC dataset used to generate them. In contrast, the dataset stored in the LP-DAAC has been exported from GEE using using a custom tiling system based on continental grids (150 x 150 km tile size) and projections (continental Lambert Azimuthal Equal Area projections).

???+ note

    **The citation paper will be updated once we finalize the release of V1 data.**

#### Citation

```
Friedl, M.A., Woodcock, C.E., Olofsson, P., Zhu, Z., Loveland, T., Stanimirova, R., Arévalo, P., Bullock, E., Hu, K.-T., Zhang, Y., Turlej, K.,
Tarrio, K., McAvoy, K., Gorelick, N., Wang, J.A., Barber, C.P., Souza, C., 2022. Medium Spatial Resolution Mapping of Global Land Cover and Land
Cover Change Across Multiple Decades From Landsat. Frontiers in Remote Sensing 3. https://doi.org/10.3389/frsen.2022.894571
```

#### Dataset Dataset:

```
Arévalo, P., R. Stanimirova, E. Bullock, Y. Zhang, K. Tarrio, K. Turlej, K. Hu, K. McAvoy, V. Pasquarella, C. Woodcock, P. Olofsson, Z. Zhu, N.
Gorelick, T. Loveland, C. Barber, M. Friedl. Global Land Cover Mapping and Estimation Yearly 30 m V001. 2022, distributed by NASA EOSDIS Land
Processes Distributed Active Archive Center, https://doi.org/10.5067/MEaSUREs/GLanCE/GLanCE30.001. Accessed YYYY-MM-DD.
```

![glance](https://github.com/user-attachments/assets/df62637f-fb20-46e2-8cc6-5dfb048c7fdb)

#### Earth Engine Snippet

```js
var GLANCE = ee.ImageCollection("projects/GLANCE/DATASETS/V001")
```

Sample Code 1: [Load and visualize datasets](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/GLANCE-VISUALIZATION)

Sample Code 2: [Load year of change and EVI2 change data](https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/GLANCE-INDICES)

App: https://glance.earthengine.app/view/datasetviewer


#### License

This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Created and Curated by: Friedl et al 2022

Keywords: land cover, land cover change, greenness, EVI2, CCDC, global, Landsat, NASA MEaSUREs

Last updated in GEE: 2024-09-25
