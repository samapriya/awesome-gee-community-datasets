# ESA WorldCover 10 m 2020 V100 InputQuality

The ESA WorldCover 10 m 2020 V100 product is delivered in 3x3 degree tiles as Cloud Optimized GeoTIFFs (COGs) in EPSG:4326 projection (geographic latitude/longitude CRS). There are 2651 tiles and more information on [accessing this dataset can be found here](https://esa-worldcover.org/en/data-access). The current collection focused on the Input Quality layers only, the Map layer is available in [Google Earth Engine as an image collection](https://developers.google.com/earth-engine/datasets/catalog/ESA_WorldCover_v100).

The input quality layer is a per pixel quality indicator showing the quality of the Earth Observation (EO) input data. The layer is a 3 band GeoTIFF with

• Band 1: Number of Sentinel-1 GAMMA0 observations used in the classification workflow

• Band 2: Number of Sentinel-2 L2A observations used in the classification workflow

• Band 3 Percentage (0-100) of invalid S2 observations discarded in the classification workflow
(after cloud and cloud shadow filtering).

Combining Band 2 and Band 3 yields the total absolute number of valid Sentinel-2 L2A observations
used in the classification workflow.

#### License

The ESA WorldCover product is provided free of charge, without restriction of use. For the full license information see the Creative Commons Attribution 4.0 International License.

Publications, models and data products that make use of these datasets must include proper acknowledgement, including citing the datasets and the journal article as in the following citation.

#### Citation

```
Zanaga, D., Van De Kerchove, R., De Keersmaecker, W., Souverijns, N., Brockmann, C., Quast, R., Wevers, J., Grosu, A.,
Paccini, A., Vergnaud, S., Cartus, O., Santoro, M., Fritz, S., Georgieva, I., Lesiv, M., Carter, S., Herold, M., Li,
Linlin, Tsendbazar, N.E., Ramoino, F., Arino, O., 2021. ESA WorldCover 10 m 2020 v100.
https://doi.org/10.5281/zenodo.5571936
```

![esa_iq](https://user-images.githubusercontent.com/6677629/139628031-9ce7c97a-c472-424f-8a41-3a70a177d2c5.gif)


#### Earth Engine Snippet

```js
var esa_iq = ee.ImageCollection("projects/sat-io/open-datasets/ESA_WorldCover_Input_Quality");
```
Sample Code: https://code.earthengine.google.com/47f7d56aa50aad4c991f677cefdf5f11

Data access page: [ESA_WorldCover_v100](https://esa-worldcover.org/en/data-access)

Provided by: Zanaga et al, ESA WorldCover consortium

Curated in GEE by: Samapriya Roy

Keywords: : land, cover, land use, land cover, lulc, 10m, global, world, sentinel-1, sentinel 2, ESA

Last updated: 2021-11-01
