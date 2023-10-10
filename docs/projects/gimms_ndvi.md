# GIMMS Normalized Difference Vegetation Index 1982-2022

The PKU GIMMS Normalized Difference Vegetation Index dataset (PKU GIMMS NDVI, version 1.2) offers consistent global NDVI data at half-month intervals and 1/12° resolution, spanning from 1982 to 2022. Its primary objective is to address key uncertainties prevalent in existing global long-term NDVI datasets, specifically mitigating the impact of NOAA satellite orbital drift and AVHRR sensor degradation.

This dataset was generated through the utilization of biome-specific Back-Propagation Neural Network (BPNN) models, leveraging the GIMMS NDVI3g product, and drawing from a pool of 3.6 million high-quality global NDVI samples. To extend its temporal coverage up to 2022, a pixel-wise Random Forests fusion method was employed, integrating data from the MODIS NDVI (MOD13C1).Notably, the PKU GIMMS NDVI dataset demonstrates impressive accuracy when assessed against Landsat NDVI samples. It effectively eliminates the adverse effects of satellite orbital drift and sensor degradation, showcasing robust temporal consistency with MODIS NDVI data concerning pixel values and global vegetation trends. Consequently, this dataset holds significant potential as a foundational resource for research in the realm of global change studies.

The dataset is available in two versions for download: one exclusively reliant on AVHRR data covering the period from 1982 to 2015, and the other consolidated with MODIS NDVI, encompassing data from 1982 to 2022. Users are strongly encouraged to utilize the quality control (QC) layer provided within the dataset to enhance data reliability. Additionally, it is recommended to apply a threshold (e.g., 0.1) for the removal of sparse vegetation during trend analysis, following established methodologies (Zhou et al., 2001; Liu et al., 2016).

#### Post Processing
The datasets were renames since periods are not allowed in earth engine filenames so v1.2 was renamed to v12 and dates were added as start dates to each image in the collection.

#### Dataset citation

```
Muyi Li, Sen Cao, Zaichun Zhu, Zhe Wang, Ranga B. Myneni, & Shilong Piao. (2023). Spatiotemporally consistent global dataset of the GIMMS Normalized
Difference Vegetation Index (PKU GIMMS NDVI) from 1982 to 2022 (V1.2) (V1.2) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.8253971
```

#### Citation

```
Li, Muyi, Sen Cao, Zaichun Zhu, Zhe Wang, Ranga B. Myneni, and Shilong Piao. "Spatiotemporally consistent global dataset of the GIMMS Normalized
Difference Vegetation Index (PKU GIMMS NDVI) from 1982 to 2022." Earth System Science Data 15, no. 9 (2023): 4181-4203.
```

![gimms_ndvi](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/e3029df9-3068-49b5-be77-81ff635658fa)


#### Earth Engine snippet

```js
var avhrr_modis_consolidated = ee.ImageCollection("projects/sat-io/open-datasets/PKU-GIMMS-NDVI/AVHRR_MODIS_CONSOLIDATED");
var avhrr_solely = ee.ImageCollection("projects/sat-io/open-datasets/PKU-GIMMS-NDVI/AVHRR_SOLELY");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/GIMMS-NDVI-1982-2022

#### License
This work is licensed under Creative Commons Attribution 4.0 International license.

Created by: Li, Muyi, Sen Cao, Zaichun Zhu, Zhe Wang, Ranga B. Myneni, and Shilong Piao

Curated in GEE by : Samapriya Roy

keywords: PKU GIMMS NDVI, Landsat, MODIS, Back Propagation Neural Network

Last updated on GEE: 2023-10-10
