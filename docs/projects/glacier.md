# Global Glacier Elevation change products (2000-2019)

This dataset provides a comprehensive and globally consistent record of glacier elevation and mass changes between 2000 and 2019. It utilizes
extensive satellite imagery, primarily from NASA's Advanced Spaceborne Thermal Emission and Reflection Radiometer (ASTER), and advanced processing
techniques to offer a high-resolution view of glacier fluctuations worldwide. The full dataset, including global, regional, tile, and per-glacier
data, is [publicly available here](https://doi.org/10.6096/13) and you can read the [full paper here](https://www.nature.com/articles/s41586-021-03436-z).

While there are additional datasets provided by the publication only the elevation products are currently ingested.

#### Dataset Features:
* Global Coverage: The dataset encompasses nearly 99.9% of inventoried glacier areas, including peripheral glaciers around Greenland and Antarctica.
* High Resolution: Elevation change data is available at a 100m spatial resolution and monthly temporal resolution, providing detailed insights into
  glacier dynamics.

The dataset includes elevation change maps at a 100 m resolution, covering glaciers and their surrounding areas, for various time periods: 5-year intervals from 2000 to 2019, 10-year intervals (2000-2009 and 2010-2019), and the entire 20-year period. These maps, provided as GeoTIFF files, are organized by RGI region and split into 1° x 1° tiles for easier handling. Both the elevation change rates (meters per year) and their associated 1-sigma uncertainties are included, allowing for a comprehensive understanding of glacier elevation changes and their associated confidence levels. The file naming convention clearly identifies the location of each tile using its southwest corner coordinates.

To facilitate regional analysis, the dataset aggregates glacier change data for 19 major glacier regions around the world as defined by the Randolph Glacier Inventory 6.0. Recognizing the inherent uncertainties in such measurements, the dataset provides thorough uncertainty estimates for both elevation and mass changes. These estimates consider factors like observational coverage, spatial correlations due to instrument resolution and uncorrected noise, and the interpolation of the elevation time series. This ensures the reliability and transparency of the data. Further bolstering confidence in the data, the dataset has undergone extensive validation against independent, high-precision measurements from ICESat and Operation IceBridge campaigns, confirming its accuracy and suitability for a wide range of applications.

#### Citation:

```
Hugonnet, R., McNabb, R., Berthier, E. et al. Accelerated global glacier mass loss in the early twenty-first century. Nature 592, 726–731 (2021). https://doi.org/10.1038/s41586-021-03436-z
```

![glacial_elevation-optimize](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/8bd64e04-37c3-4302-9748-1174cd99a669)

#### Earth Engine Snippet

```js
var elevation_change = ee.ImageCollection("projects/sat-io/open-datasets/GLOBAL-GLACIER-MASS-LOSS/elevation-change");
var error = ee.ImageCollection("projects/sat-io/open-datasets/GLOBAL-GLACIER-MASS-LOSS/elevation-change-error");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:elevation-bathymetry/GLACIER-ELEVATION

#### License
This dataset is made available under the Creative Commons Attribution 4.0 International License.

Created by: Hugonnet, R., McNabb, R., Berthier, E. et al. 2021

Curated in GEE by: Samapriya Roy

Keywords: Altimetry, Digital Elevation Model (DEM), ICESat-2, Glaciers, Elevation change, ASTER, ICESat, Operation IceBridge, Randolph Glacier Inventory

Last updated in GEE: 2024-03-04
