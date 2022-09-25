# Rasterized building footprint dataset for the US

The Bing Maps team at Microsoft released a U.S.-wide vector building dataset in 2018, which includes over 125 million building footprints for all 50 states in GeoJSON format. This dataset is extracted from aerial images using deep learning object classification methods. Large-extent modelling (e.g., urban morphological analysis or ecosystem assessment models) or accuracy assessment with vector layers is highly challenging in practice. Although vector layers provide accurate geometries, their use in large-extent geospatial analysis comes at a high computational cost.

High Performance Computing (HPC) were used by the authors to develop an algorithm that calculates six summary values for each cell in a raster representation of each U.S. state
1. total footprint coverage
2. number of unique buildings intersecting each cell
3. number of building centroids falling inside each cell, and
4. Minimum area of the buildings that intersect each cell
5. Maximum area of the buildings that intersect each cell
6. Average area of the buildings that intersect each cell

These values are represented as raster layers with 30m cell size covering the 48 conterminous states, to better support incorporation of building footprint data into large-extent modelling.

This Project is funded by NASA’s Biological Diversity and Ecological Forecasting program

**Award : 80NSSC18k0341**

You can [download the datasets here](https://www.sciencebase.gov/catalog/item/5d27a8dfe4b0941bde650fc7)

#### Data Citation

```
Heris, M.P., Foks, N., Bagstad, K., and Troy, A., 2020, A national dataset of rasterized building
footprints for the U.S.: U.S. Geological Survey data release, https://doi.org/10.5066/P9J2Y1WG.
```

#### Paper Citation

```
Heris, M.P., Foks, N.L., Bagstad, K.J. et al. A rasterized building footprint dataset for the
United States. Sci Data 7, 207 (2020). https://doi.org/10.1038/s41597-020-0542-3
```

![urban_raster](https://user-images.githubusercontent.com/6677629/143531807-17b3ed14-a4bc-415e-b0f0-f0a8599018b2.gif)


#### Earth Engine Snippet

```js
var avg_area = ee.Image("projects/sat-io/open-datasets/us_building_raster/building_avg_area");
var max_area = ee.Image("projects/sat-io/open-datasets/us_building_raster/building_max_area");
var min_area = ee.Image("projects/sat-io/open-datasets/us_building_raster/building_min_area");
var total_area = ee.Image("projects/sat-io/open-datasets/us_building_raster/building_total_area");
var building_count = ee.Image("projects/sat-io/open-datasets/us_building_raster/building_count");
var centroid_count = ee.Image("projects/sat-io/open-datasets/us_building_raster/building_centroid_count");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:regional-landuse-landcover/RASTERIZED-BUILDING-FOOTPRINT-US

#### License

Datasets are freely available to the public under the Creative Commons Public Domain Dedication waiver http://creativecommons.org/publicdomain/zero/1.0/.

Created by: Heris et al, NASA, USGS

Curated by: Samapriya Roy

Keywords: : Building Footprint, Built Environment Density, Land cover, Land use

Last updated: 2021-11-26
