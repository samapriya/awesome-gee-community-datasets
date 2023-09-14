# Global 30m Impervious-Surface Dynamic Dataset (GISD30)

The Global 30 m Impervious-Surface Dynamic Dataset (GISD30) offers an invaluable resource for understanding the ever-changing landscape of impervious surfaces across the globe from 1985 to 2020. This dataset holds profound scientific significance and practical applications in the realms of urban sustainable development, anthropogenic carbon emissions assessment, and global ecological-environment modeling. The GISD30 was meticulously created through an innovative and automated methodology that capitalizes on the strengths of spectral-generalization and automatic-sample-extraction strategies. Leveraging time-series Landsat imagery on the Google Earth Engine cloud computing platform, the dataset provides comprehensive insights into impervious-surface dynamics.

In the dataset creation process, global training samples and corresponding reflectance spectra were automatically derived, enhancing accuracy and reliability. Spatiotemporal adaptive classification models were employed, taking into account the dynamic nature of impervious surfaces across different epochs and geographical tiles. Furthermore, a spatiotemporal-consistency correction method was introduced to enhance the reliability of impervious-surface dynamics. The GISD30 dynamic model exhibits remarkable accuracy, with an overall accuracy of 90.1% and a kappa coefficient of 0.865, validated using a substantial dataset of 23,322 global time-series samples. This dataset provides vital insights into the doubling of global impervious surface area over the past 35 years, from 1985 to 2020, with Asia experiencing the most substantial increase. The GISD30 dataset is freely accessible and serves as a crucial tool for monitoring urbanization at regional and global scales, offering invaluable support for diverse applications. Access the [dataset here](https://doi.org/10.5281/zenodo.5220816) (Liu et al., 2021b).

The global dynamic dataset was used to label the expansion information in a single band; specifically, the pervious surface and the impervious surface before 1985 were, respectively, labeled 0 and 1, and the expanded impervious surfaces in the periods 1985–1990, 1990–1995, 1995–2000, 2000–2005, 2005–2010, 2010–2015 and 2015–2020 were labeled 2, 3, 4, 5, 6, 7 and 8.

<center>

| Years           | Impervious Surface Labels |
|-----------------|---------------------------|
| Before 1985     | 1                         |
| 1985–1990       | 2                         |
| 1990–1995       | 3                         |
| 1995–2000       | 4                         |
| 2000–2005       | 5                         |
| 2005–2010       | 6                         |
| 2010–2015       | 7                         |
| 2015–2020       | 8                         |

</center>

#### Citation

```
Zhang, X., Liu, L., Zhao, T., Gao, Y., Chen, X., and Mi, J.: GISD30: global 30 m impervious-surface dynamic dataset from 1985 to 2020 using
time-series Landsat imagery on the Google Earth Engine platform, Earth Syst. Sci. Data, 14, 1831–1856,
https://doi.org/10.5194/essd-14-1831-2022, 2022
```

#### Dataset citation

```
Liangyun,Liu; Xiao,Zhang; Tingting,Zhao; Yuan,Gao; Xidong,Chen; Jun,Mi. (2021). GISD30: global 30-m impervious surface dynamic dataset from 1985 to
2020 using time-series Landsat imagery on the Google Earth Engine platform [Data set]. Zenodo. https://doi.org/10.5281/zenodo.5220816
```

![gisd_optimized_img](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/44e6bef1-3e60-4ca5-8380-f9654cefb329)

#### Earth Engine Snippet

```js
var gisd30 = ee.Image("projects/sat-io/open-datasets/GISD30_1985_2020");

//zoom to an urban center
Map.setCenter(31.16387, 30.97292,8)

var palette = ["#808080", "#006400", "#228B22", "#32CD32", "#ADFF2F", "#FFFF00", "#FFA500", "#FF0000"];

var snazzy = require("users/aazuspan/snazzy:styles");
snazzy.addStyle("https://snazzymaps.com/style/132/light-gray", "Grayscale");

Map.addLayer(gisd30,{min:1,max:8,palette:palette},'GISD 30')

```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:/global-landuse-landcover/GLOBAL-IMPERVIOUS-30-GISD

#### License

This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Created by : Zhang, X., Liu, L., Zhao, T., Gao, Y., Chen, X., and Mi, J.

Curated in GEE by: Samapriya Roy

Keywords: Landsat, Urban, Google Earth Engine, Impervious area, Urban expansion, global dataset

Last updated in GEE: 2023-09-12
