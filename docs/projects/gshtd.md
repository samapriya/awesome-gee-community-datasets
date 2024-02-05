# Global Seamless High-resolution Temperature Dataset (GSHTD)

The Global Seamless High-resolution Temperature Dataset (GSHTD) presented in this study offers a comprehensive and valuable resource for researchers across various fields. Covering the period from 2001 to 2020, this dataset focuses on land surface temperature (Ts) and near-surface air temperature (Ta). A unique feature of GSHTD is its incorporation of seven types of temperature data, including clear-sky daytime and nighttime Ts, all-sky daytime and nighttime Ts, and mean, maximum, and minimum Ta. Notably, the dataset achieves global coverage with an impressive 30 arcsecond or 1km spatial resolution.

The development of GSHTD involves the innovative Estimation of Temperature Difference (ETD) method, enabling the reconstruction of both clear- and cloudy-sky Ts. The dataset is seamless, eliminating missing values, and employs a Cubist machine learning algorithm to enhance accuracy in creating monthly averages of mean, maximum, and minimum Ta data. GSHTD exhibits high accuracy, outperforming existing methods with average mean absolute errors (MAEs) that are significantly lower. This dataset's accessibility at the Middle Yangtze River Geoscience Data Center provides a valuable tool for studies related to climate change, environmental science, ecology, epidemiology, and human health. You can find [additional information in the paper here](https://www.sciencedirect.com/science/article/abs/pii/S0034425722005284) including links to the dataset.

**These temperature datasets are not valid over open oceans.**

#### Citation

```
Yao, Rui, Lunche Wang, Xin Huang, Qian Cao, Jing Wei, Panxing He, Shaoqiang Wang, and Lizhe Wang. "Global seamless and high-resolution temperature
dataset (GSHTD), 2001–2020." Remote Sensing of Environment 286 (2023): 113422.
```

![gshtd](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/804cfa90-a684-420e-9a98-69370d942b84)

#### Earth Engine Snippet

```js
var all_sky_day = ee.ImageCollection("projects/sat-io/open-datasets/GSHTD/ALL_SKY_DAY");
var all_sky_night = ee.ImageCollection("projects/sat-io/open-datasets/GSHTD/ALL_SKY_NIGHT");
var clear_sky_day = ee.ImageCollection("projects/sat-io/open-datasets/GSHTD/CLEAR_SKY_DAY");
var clear_sky_night = ee.ImageCollection("projects/sat-io/open-datasets/GSHTD/CLEAR_SKY_NIGHT");
var tmax = ee.ImageCollection("projects/sat-io/open-datasets/GSHTD/TMAX");
var tmean = ee.ImageCollection("projects/sat-io/open-datasets/GSHTD/TMEAN");
var tmin = ee.ImageCollection("projects/sat-io/open-datasets/GSHTD/TMIN");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/GSHTD

#### License

The dataset is distributed under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) as requested by the authors.

Provided by: Yao et al 2023

Curated in GEE by: Samapriya Roy

Keywords: MODIS, High Resolution Temperature, Seamless, Gap filled, Global dataset

Last updated in GEE: 2024-02-04
