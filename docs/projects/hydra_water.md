# Tensor Flow Hydra Flood Models

This dataset is a surface water output image from the Hydrologic Remote Sensing Analysis for Floods (HYDRAFloods) system utilizing a Deep Learning TensorFlow approach. Specifically, this Joint Research Centre (JRC) Adjusted Learning Rate Binary Cross-Entropy (BCE) Dice model and methodology are discussed in detail in the recent [Deep learning approach for Sentinel-1 surface water mapping leveraging Google Earth Engine](https://www.sciencedirect.com/science/article/pii/S2667393221000053#!) publication.

#### Citation

```
Mayer, T., Poortinga, A., Bhandari, B., Nicolau, A.P., Markert, K., Thwal, N.S., Markert, A., Haag, A., Kilbride, J., Chishtie, F. and Wadhwa, A.,
2021. Deep Learning approach for Sentinel-1 Surface Water Mapping leveraging Google Earth Engine. ISPRS Open Journal of Photogrammetry and Remote
Sensing, p.100005.
```

For greater detail on the HYDRAFloods open-source Python application for downloading, processing, and delivering surface water maps derived from remote sensing data. Please see the [HYDRAFloods Documentation](https://servir-mekong.github.io/hydra-floods/).


![hydra](https://user-images.githubusercontent.com/6677629/138355409-60fb1d06-764f-419b-bd1b-871c529880e8.gif)


#### Earth Engine Snippet

```js

var HYDRAFloods = ee.Image("users/tjm0042/Hydrafloods_Outputs/TensorFlow_Surface_Water_Model_Mosaic")

```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/TENSORFLOW-HYDRA-FLOOD-MODELS

#### License
This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Curated by: Tim Mayer, Kel Markert, Biplov Bhandari, Ate Poortinga

Keywords: Surface Water Mapping, Floods, Deep Learning TensorFlow, SERVIR

Last updated: 2021-10-20
