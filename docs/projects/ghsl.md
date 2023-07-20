# Global Human Settlement Layer 2023

The Global Human Settlement Layer (GHSL) project is a comprehensive initiative that generates global spatial data and evidence-based analytics, offering insights into the distribution and characteristics of human presence on Earth. The project follows an open and unrestricted data and methods access policy. The knowledge derived from GHSL plays a crucial role in shaping European policies, fostering public discussions, and facilitating the implementation of international frameworks like the 2030 Development Agenda. This release offers enhanced built-up area information, including surface, volume, and height measurements, along with population data. Moreover, it introduces a new settlement model and a classification system for administrative and territorial units based on the "Degree of Urbanisation" framework. The GHSL Data Package 2023 consists of multitemporal products, that offers an insight into the human presence in the past (epochs from 1975 through 2020, 5 years interval) and the future (2025 and 2030). The datasets included can be found below along with descriptors and dataset citations. Methodological citations and additional details on the products themselves [can be found here](https://ghsl.jrc.ec.europa.eu/documents/GHSL_Data_Package_2023.pdf).

#### Dataset details

* GHS-BUILT-S R2023A - GHS built-up surface grid, derived from Sentinel-2 composite (2018) and Landsat, multitemporal (1975-2030, 5 years interval). These are available as reprocessed 10m resolution, The sub-pixel built-up fraction (BUFRAC) estimate at 10m resolution is produced from the 10m-resolution Sentinel-2 image composite, using as learning set a composite of data from GHS-BUILT-S2 R2020A, Facebook settlement delineation, Microsoft, and Open Street Map (OSM) building delineation. The inferential engine is a multiple-quantization-minimal-support (MQMS) generalization of the symbolic machine learning (SML) approach (Pesaresi, Syrris, et al., 2016) and 2030 at 100m resolution
* GHS-BUILT-H R2023A - GHS building height, derived from AW3D30, SRTM30, and Sentinel-2 composite (2018)
* GHS-BUILT-V R2023A - GHS built-up volume grids derived from joint assessment of Sentinel-2, Landsat, and global DEM data, multitemporal (1975-2030, 5 years interval)
* GHS-BUILT-C R2023A - GHS Settlement Characteristics, derived from Sentinel-2 composite (2018) and other GHS R2023A data
* GHS-POP R2023A - GHS population grid multitemporal (1975-2030, 5 years interval)
* GHS-SMOD R2023A - GHS settlement layers, application of the Degree of Urbanisation methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A, multitemporal (1975-2030, 5 years interval)

#### Dataset citations

```
Pesaresi, Martino; Politis, Panagiotis (2023): GHS-BUILT-S R2023A - GHS built-up surface grid, derived from
Sentinel2 composite and Landsat, multitemporal (1975-2030). European Commission, Joint Research Centre
(JRC) [Dataset] doi: 10.2905/9F06F36F-4B11-47EC-ABB0-4F8B7B1D72EA PID:
http://data.europa.eu/89h/9f06f36f-4b11-47ec-abb0-4f8b7b1d72ea

Pesaresi, Martino; Politis, Panagiotis (2023): GHS-BUILT-H R2023A - GHS building height, derived from AW3D30,
SRTM30, and Sentinel2 composite (2018). European Commission, Joint Research Centre (JRC) [Dataset] doi:
10.2905/85005901-3A49-48DD-9D19-6261354F56FE PID: http://data.europa.eu/89h/85005901-3a49-
48dd-9d19-6261354f56fe

Pesaresi, Martino; Politis, Panagiotis (2023): GHS-BUILT-V R2023A - GHS built-up volume grids derived from
joint assessment of Sentinel2, Landsat, and global DEM data, multitemporal (1975-2030). European
Commission, Joint Research Centre (JRC) [Dataset] doi: 10.2905/AB2F107A-03CD-47A3-85E5-139D8EC63283
PID: http://data.europa.eu/89h/ab2f107a-03cd-47a3-85e5-139d8ec63283

Pesaresi, Martino; Politis, Panagiotis (2023): GHS-BUILT-C R2023A - GHS Settlement Characteristics, derived
from Sentinel2 composite (2018) and other GHS R2023A data. European Commission, Joint Research Centre
(JRC) [Dataset] doi: 10.2905/3C60DDF6-0586-4190-854B-F6AA0EDC2A30 PID:
http://data.europa.eu/89h/3c60ddf6-0586-4190-854b-f6aa0edc2a30

Schiavina, Marcello; Freire, Sergio; Alessandra Carioli; MacManus, Kytt (2023): GHS-POP R2023A - GHS
population grid multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) [Dataset] doi:
10.2905/2FF68A52-5B5B-4A22-8F40-C41DA8332CFE PID: http://data.europa.eu/89h/2ff68a52-5b5b-4a22-
8f40-c41da8332cfe

Schiavina, Marcello; Melchiorri, Michele; Pesaresi, Martino (2023): GHS-SMOD R2023A - GHS settlement layers,
application of the Degree of Urbanisation methodology (stage I) to GHS-POP R2023A and GHS-BUILT-S R2023A,
multitemporal (1975-2030). European Commission, Joint Research Centre (JRC) [Dataset] doi:
10.2905/A0DF7A6F-49DE-46EA-9BDE-563437A6E2BA PID: http://data.europa.eu/89h/a0df7a6f-49de-46ea9bde-563437a6e2ba

```

![ghs-urban](https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/assets/6677629/ca86af79-2f62-4983-93aa-2de4a7d842c3)

#### Earth Engine Snippet

```js
var GHS_BUILT_S_2018 = ee.ImageCollection("projects/sat-io/open-datasets/GHS/GHS_BUILT_S_E2018_GLOBE_R2023A_54009_10_V1_0");
var GHS_BUILT_S_2030 = ee.Image("projects/sat-io/open-datasets/GHS/GHS_BUILT_S_E2030_GLOBE_R2023A_54009_100_V1_0");
var GHS_BUILT_H = ee.Image("projects/sat-io/open-datasets/GHS/GHS_BUILT_H_AGBH_E2018_GLOBE_R2023A_54009_100_V1_0");
var GHS_BUILT_V = ee.Image("projects/sat-io/open-datasets/GHS/GHS_BUILT_V_E2030_GLOBE_R2023A_54009_100_V1_0");
var GHS_BUILT_C = ee.ImageCollection("projects/sat-io/open-datasets/GHS/GHS_BUILT_C_MSZ_E2018_GLOBE_R2023A_54009_10_V1_0");
var GHS_POP = ee.Image("projects/sat-io/open-datasets/GHS/GHS_POP_E2030_GLOBE_R2023A_54009_100_V1_0");
var GHS_SMOD = ee.Image("projects/sat-io/open-datasets/GHS/GHS_SMOD_E2030_GLOBE_R2023A_54009_1000_V1_0");
```

Sample Script: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/JRC-GHSL-2023

#### License
The GHSL has been produced by the EC JRC as open and free data. Reuse is authorised, provided the source is acknowledged. For more information, please read the use conditions [European Commission Reuse and Copyright Notice](https://commission.europa.eu/legal-notice_en).

Created by: ESA & JRC

Curated in GEE by : Samapriya Roy

keywords: Global Population, Population count, Urban structure, Built up area, Built up volume, Building height

Last modified: 2022-01-20

Last updated on GEE: 2022-09-25
