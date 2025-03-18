# S2 SR HARMONIZED SWITZERLAND

Sentinel-2 (ESA) optical satellite data provides complete coverage of Switzerland approximately every three days. The effectiveness of this data
relies significantly on meteorological factors like cloud cover, atmospheric correction, data registration, and delivery methods (projection). We've
enhanced existing processing procedures and incorporated additional post-processing techniques to produce analysis-ready surface reflectance data
specifically tailored for Switzerland. You can find additional information in [geocat.ch - the swiss geographic catalogue](https://www.geocat.ch)
and [metadata information can be found here](https://www.geocat.ch/geonetwork/srv/eng/catalog.search#/metadata/7ae5cd5b-e872-4719-92c0-dc2f86c4d471). Processing code can be found in the [SATROMO GitHub Repository](https://github.com/swisstopo/topo-satromo).

#### Processing
- The input dataset is the Level 2A (surface reflectance) data from Sentinel-2: [S2_SR_HARMONIZED](https://developers.google.com/earth-engine/datasets/catalog/COPERNICUS_S2_SR_HARMONIZED?hl=en).
- For cloud detection the [CloudScore+](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_CLOUD_SCORE_PLUS_V1_S2_HARMONIZED?hl=en) dataset is used with a 0.4 threshold for the cs_cdf band to identify clouds. Additionally, a stricter 0.2 threshold is applied in a projection corridor of the clouds derived from the solar and satellite geometries.
- Using the same geometries as above in addition to a digital elevation model (swissALTI3D) terrain shadows are detected and added as a mask.
- The tiles from each overpass are mosaiced.
- Lastly, the mosaics are co-registered by the displacement vectors in relation to the Sentinel Ground Reference Image to achieve sub-pixel location accuracy. All the mosaics are saved in epsg:2056 (CH1903+ / LV95) and the covered perimeter includes Switzerland and Liechtenstein.

#### Assets, bands & masks
Each overpass is mosaiced and there are two assets per overpass for the 10m and 20m spatial resolution, both can be filtered using a property called "pixel_size_meter" so for example you can filter using ```collection.filter(ee.Filter.eq('pixel_size_meter',10))``` for 10m bands

??? example "Expand to show asset resolution and band list"

    <center>

    | **Asset Resolution** | **Bands**                            |
    |------------------|----------------------------------|
    | 10m              | - B2 (Blue)                      |
    |                  | - B3 (Green)                     |
    |                  | - B4 (Red)                       |
    |                  | - B8 (NIR)                       |
    |                  | - terrainShadowMask (binary mask for terrain shadow) |
    |                  | - cloudAndCloudShadowMask (binary mask for clouds and cloud shadows) |
    |                  | - reg_dx (offset in x direction from the co-registration) |
    |                  | - reg_dy (offset in y direction from the co-registration) |
    |                  | - reg_confidence (displacement confidence from the co-registration) |
    |                  | - cloudProbability (percentage of cloud probability) |
    | 20m              | - B8A (NIR 2)                    |
    |                  | - B11 (SWIR 1)                   |
    |                  | - B5 (Red Edge 1)                |

![s2_h_sr-optimize](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/7f75b1c1-68bd-46e9-a789-ceab8c6763da)

### Earth Engine Snippet

```js
var s2_sr_harmonized_swiss = ee.ImageCollection("projects/satromo-prod/assets/col/S2_SR_HARMONIZED_SWISS");
```

Sample Script: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:analysis-ready-data/SWISSTOPO-S2-SR-HARMONIZED

#### License
The free geodata and geoservices of swisstopo may be used, distributed and made accessible. Furthermore, they may be enriched and processed and also
used commercially. [Terms of use for free geodata and geoservices(OGD) from swisstopo](https://www.swisstopo.admin.ch/en/terms-of-use-free-geodata-and-geoservices). Contains modified Copernicus Sentinel data.

1. Legal basis

The use of free geodata and geoservices from swisstopo is governed by the following legal bases

   - Federal Act on Geoinformation (Geoinformation Act, GeoIA 510.62) Art. 10 ff
   - Ordinance on Geoinformation (Geoinformation Ordinance, 510.620) Art. 20 ff
   - swisstopo ordinance on fees and charges

A reference to the source is mandatory. In the case of digital or analogue representations and publications, as well as in the case of dissemination, one of the following source references must be attached in any case:

- Bundesamt für Landestopografie swisstopo
- Office fédéral de topographie swisstopo
- Ufficio federale di topografia swisstopo
- Uffizi federal da topografia swisstopo
- Federal Office of Topography swisstopo
- ©swisstopo

Keywords: BGDI, optical satellite imagery, Sentinel-2, surface reflectance, Analysis ready data

Created and provided by: [Federal Office of Topography swisstopo](https://www.swisstopo.admin.ch/en)

Curated in GEE by: swisstopo and Samapriya Roy

Last updated: 2025-03-18
