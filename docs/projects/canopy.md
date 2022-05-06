# ETH Global Sentinel-2 10m Canopy Height (2020)

The worldwide variation in vegetation height is fundamental to the global carbon cycle and central to the functioning of ecosystems and their biodiversity. Geospatially explicit and, ideally, highly resolved information is required to manage terrestrial ecosystems, mitigate climate change, and prevent biodiversity loss. Here, we present the first global, wall-to-wall canopy height map at 10 m ground sampling distance for the year 2020. No single data source meets these requirements: dedicated space missions like GEDI deliver sparse height data, with unprecedented coverage, whereas optical satellite images like Sentinel-2 offer dense observations globally, but cannot directly measure vertical structures. By fusing GEDI with Sentinel-2, we have developed a probabilistic deep learning model to retrieve canopy height from Sentinel-2 images anywhere on Earth, and to quantify the uncertainty in these estimates.

The presented approach reduces the saturation effect commonly encountered when estimating canopy height from satellite images, allowing to resolve tall canopies with likely high carbon stocks. According to our map, only 5% of the global landmass is covered by trees taller than 30 m. Such data play an important role for conservation, e.g., we find that only 34% of these tall canopies are located within protected areas. Our model enables consistent, uncertainty-informed worldwide mapping and supports an ongoing monitoring to detect change and inform decision making. The approach can serve ongoing efforts in forest conservation, and has the potential to foster advances in climate, carbon, and biodiversity modelling. You can download the [cloud optimized geotiffs here](https://share.phys.ethz.ch/~pf/nlangdata/ETH_GlobalCanopyHeight_10m_2020_version1/)

Disclaimer: Parts or all of the dataset description is borrowed from existing description provided by authors.

#### Citation

```
Lang, Nico, Walter Jetz, Konrad Schindler, and Jan Dirk Wegner. "A high-resolution canopy height model of the Earth." arXiv preprint arXiv:2204.08322 (2022).
```

![canopy_10m_comp](https://user-images.githubusercontent.com/6677629/167065993-009e0736-5bda-4a85-9978-998dbb2ad00c.gif)


#### Earth Engine Snippet

```js
var canopy_height = ee.Image("users/nlang/ETH_GlobalCanopyHeight_2020_10m_v1");
var standard_deviation = ee.Image("users/nlang/ETH_GlobalCanopyHeightSD_2020_10m_v1");
```

Sample code: https://code.earthengine.google.com/126c172d63e7ce780596c8d26f06d384

GEE app link: https://nlang.users.earthengine.app/view/global-canopy-height-2020

GEE app source code link: https://code.earthengine.google.com/fefca6457efb90c0a3f8ae9806bee792

#### License

The ETH Global Canopy Height 2020 product is provided free of charge, without restriction of use. For the full license information see the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/) publications, models and data products that make use of these datasets must include proper acknowledgement, including citing the datasets and the journal article as in the following citation.

Created by: Lang, Nico, Walter Jetz, Konrad Schindler, and Jan Dirk Wegner

Curated by: Samapriya Roy

Keywords: Sentinel-2, Forest, Canopy Height, Machine Learning, CNN

Last updated on GEE: 2022-03-29
