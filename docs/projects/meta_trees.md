# High Resolution 1m Global Canopy Height Maps

The Global Canopy Height Maps dataset offers comprehensive insights into tree canopy heights worldwide, facilitating precise monitoring of forest ecosystems, carbon sequestration, and climate change mitigation efforts. Developed through collaboration between Meta and the World Resources Institute, this dataset stands as a cornerstone for understanding forest structure and dynamics. This dataset achieves an unparalleled level of detail through the fusion of state-of-the-art satellite imagery and advanced artificial intelligence techniques. By analyzing satellite imagery spanning from 2009 to 2020, with a focus on data from 2018 to 2020, it provides extensive temporal coverage for tracking changes in canopy height over time across the entire landmass of the planet. Using AI models such as DiNOv2, the dataset enables precise prediction of canopy height with a mean absolute error of 2.8 meters, empowering accurate assessment of carbon stocks and the effectiveness of mitigation strategies.

Moreover, its integration into conservation initiatives, carbon credit monitoring, and climate agreements underscores its significance in guiding sustainable forest management practices, afforestation, reforestation efforts, and biodiversity conservation. Complemented by the accessibility of the AI model used to generate the data on GitHub, this dataset catalyzes further research and development in forest monitoring and carbon sequestration, contributing to global efforts to combat climate change. You can read the [blogpost from meta here](https://sustainability.fb.com/blog/2024/04/22/using-artificial-intelligence-to-map-the-earths-forests/) and the [associated paper here](https://www.sciencedirect.com/science/article/pii/S003442572300439X).

#### Citation

```
Tolan, J., Yang, H.I., Nosarzewski, B., Couairon, G., Vo, H.V., Brandt, J., Spore, J., Majumdar, S., Haziza, D., Vamaraju, J. and Moutakanni, T.,
2024. Very high resolution canopy height maps from RGB imagery using self-supervised vision transformer and convolutional decoder trained on aerial
lidar. Remote Sensing of Environment, 300, p.113888.
```

#### Dataset citation

```
High Resolution Canopy Height Maps by WRI and Meta was accessed on DATE from Google Earth Engine. Meta and World Resources Institude (WRI) - 2023.
High Resolution Canopy Height Maps (CHM). Source imagery for CHM © 2016 Maxar. Accessed DAY MONTH YEAR.
```

![canopy_ht_1m](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/171b3e30-49c0-448c-86cb-57c5464504e6)

#### Earth Engine Snippet

```js
var canopy_ht = ee.ImageCollection("projects/meta-forest-monitoring-okw37/assets/CanopyHeight")
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/GLOBAL-1m-CANOPY-HEIGHT

GEE app link: https://meta-forest-monitoring-okw37.projects.earthengine.app/view/canopyheight

#### License
This dataset is made available under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/)

Dataset provider: Meta and WRI, Tolan et al 2023

Curated in GEE by: Meta & WRI

Keywords: DiNOv2, Maxar, Self Supervised Learning (SSL), Canopy height, Global dataset, Meta, WRI

Last updated on GEE: 2024-04-13
