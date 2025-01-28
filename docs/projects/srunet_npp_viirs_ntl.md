# Global Annual Simulated NPP-VIIRS Nighttime Light Dataset (1992-2023)

The SVNL (Simulated VIIRS Nighttime Light) dataset provides a harmonized, continuous global annual NPP-VIIRS-like nighttime light data from 1992 to 2023. The longest available consistent NPP-VIIRS-like nighttime light dataset spanning over 32 years through cross-sensor calibration and deep learning methods.This dataset addresses critical gaps in existing nighttime light data by bridging DMSP-OLS (1992-2013) and NPP-VIIRS (2012-2023) through an innovative deep learning approach using a Nighttime Light U-Net super-resolution network (NTLSRU-Net).

The dataset features temporal coverage from 1992-2023 (32 years) with a spatial resolution of 15 arc-seconds (~500m). It provides global coverage from -180° to 180° longitude and 65°S to 75°N latitude. The data maintains consistent calibration across DMSP-OLS and VIIRS sensors while providing enhanced spatial detail comparable to NPP-VIIRS and reduced saturation and blooming effects compared to raw DMSP data. The dataset has been extensively validated against socioeconomic indicators and existing nighttime light datasets.

The dataset enables long-term analysis of urbanization monitoring, socioeconomic estimation, environmental assessment, human activity patterns, and regional and global development studies. This comprehensive temporal coverage makes it particularly valuable for studying long-term urban development, economic growth patterns, and environmental changes at both regional and global scales. You can read more in the [paper here](https://www.nature.com/articles/s41597-024-04228-6) and find the [dataset here](https://doi.org/10.6084/m9.figshare.22262545.v8)

#### Methods

The dataset was generated through:
1. Preprocessing of raw DMSP-OLS data to address interannual inconsistency
2. Cross-sensor calibration using NTLSRU-Net with Landsat NDVI assistance
3. Integration of simulated VIIRS data (1992-2011) with real VIIRS data (2012-2023)
4. Comprehensive validation across multiple scales and metrics

#### Dataset Preprocessing
Original data was not compression optimized , an LZW compression with tiling  was applied to convert these into COG for direct use as well as being ingested into Google Earth Engine. Nodata value was coded as 0 the same as the authors.

#### Citation

```
Chen, X., Wang, Z., Zhang, F., Shen, G., & Chen, Q. (2024). A global annual simulated VIIRS nighttime light dataset from 1992 to 2023. Scientific Data, 11(1380).
https://doi.org/10.1038/s41597-024-04228-6
```

#### Dataset Citation

```
Chen, Xiuxiu; Zhang, Feng; Wang, Zeyu (2023). A history reconstructed time series (1992-2011) of annual global NPP-VIIRS-like nighttime light data through a super-resolution
U-Net model. figshare. Dataset. https://doi.org/10.6084/m9.figshare.22262545.v8
```

![srunet_npp_viirs_ntl](https://github.com/user-attachments/assets/c4f1dffc-3db4-43f6-9408-f4932f80e330)

#### Earth Engine Snippet

```js
var viirs_ntl = ee.ImageCollection("projects/sat-io/open-datasets/srunet-npp-viirs-ntl");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/GLOBAL-SRUNET-NPP-VIIRS-LIKE-NTL

## License

This dataset is made available under Creative Commons 4.0 Internal Attribution License.

Created by: Chen, Xiuxiu et al.

Curated in GEE by: Samapriya Roy

Keywords: Nighttime light, VIIRS, NTL, NPP-VIIRS, Urban monitoring, super resolution, machine learning

Last updated: 2024-01-28
