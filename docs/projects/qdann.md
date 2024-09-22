# QDANN 30m Yield Map for Corn, Soy, and Winter Wheat in the U.S

This dataset presents a novel scale transfer framework for estimating crop yields at subfield levels using satellite remote sensing and machine learning techniques. The framework, known as **Quantile Loss Domain Adversarial Neural Networks (QDANN)**, utilizes knowledge from county-level datasets to accurately map yields at finer spatial resolutions, addressing the limitations posed by the scarcity of ground truth data for model training and evaluation.While broader scale yield mapping (e.g., state or county level) has become standard, finer-scale mapping has faced challenges due to the lack of subfield yield information. QDANN employs an unsupervised domain adaptation strategy, training on labeled county-level data while leveraging unlabeled subfield data, thus eliminating the need for yield information at the subfield level.

The dataset is based on Landsat imagery and Gridmet weather data, focusing on maize, soybean, and winter wheat fields across the United States. It is validated using yield monitor records from approximately one million field-year observations. QDANN's performance is benchmarked against various process-based and machine learning methods that utilize simulated yield records or county-level data.

Key results include:
- R² scores (RMSE) for maize, soybean, and winter wheat were 48% (2.29 t/ha), 32% (0.85 t/ha), and 39% (1.40 t/ha) respectively, demonstrating superior accuracy compared to benchmark methods.
- When yields were aggregated to the county level, QDANN's performance improved significantly, achieving R² scores (RMSE) of 78% (0.98 t/ha) for maize, 62% (0.37 t/ha) for soybean, and 53% (1.00 t/ha) for winter wheat.

This study illustrates the efficacy of the QDANN framework for reliable yield mapping at subfield levels, even in the absence of fine-scale yield data. The dataset includes publicly available 30-meter annual yield maps for major crop-producing states in the U.S., generated since 2008 with units kg/ha. You can find additional details in the [paper here](https://www.sciencedirect.com/science/article/pii/S003442572400453X?dgcid=author).

#### Dataset Preprocessing

The datasets were originally ingested by the authors as images into folders with State abbreviation and year to get to a specific image. These were now moved into two separate collections for corn-soybean and winter-wheat. State abbreviations were added as a property called "state_abbv" and dates are added to represent the time period. This allows for easy filtering of the collection by state and date.

<center>

| **Raster**       | **Band Info**        | **Unit** |
|------------------|----------------------|----------|
| Corn & Soybean   | b1: corn, b2: soybean| kg/ha    |
| Winter Wheat     | b1: winter wheat     | kg/ha    |

</center>

#### Citation

```
Ma, Yuchi, Sang-Zi Liang, D. Brenton Myers, Anu Swatantran, and David B. Lobell. "Subfield-level crop yield mapping without ground truth data:
A scale transfer framework." Remote Sensing of Environment 315 (2024): 114427.
```

![yield_map](https://github.com/user-attachments/assets/9d1ae2df-2e6b-474f-99f9-2d5a8f2c0854)

#### Earth Engine Snippet

```js
var corn_soybean = ee.ImageCollection("projects/sat-io/open-datasets/lobell-lab/VAE_QDANN_YIELD_MAP/CORN_SOY_MAP");
var winter_wheat = ee.ImageCollection("projects/sat-io/open-datasets/lobell-lab/VAE_QDANN_YIELD_MAP/WINTER_WHEAT_MAP")
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/QDANN-30M-YIELD-MAPS

#### License
QDANN Yield Maps follow [CC-BY-NC-SA 4.0](https://github.com/yuchima8/QDANN_Yield_Map/blob/main/CC-BY-NC-SA-4.0.txt). Thus, those compounds are freely available for academic purposes or individual research, but restricted for commercial use.

Created by: Ma,Yuchi et al. 2024, Lobell Lab

Curated in GEE by: Yuchi Ma & Samapriya Roy

Keywords : corn,soybean,winter wheat,yield

Last updated in GEE: 2024-09-22


