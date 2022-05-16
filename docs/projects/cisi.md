# Harmonized Global Critical infrastructure & Index (CISI)

Critical infrastructure (CI) is fundamental for the functioning of a society and forms the backbone for socio-economic development. Natural and human-made threats, however, pose a major risk to CI. Therefore, geospatial data on the location of CI are fundamental for in-depth risk analyses, which are required to inform policy decisions aiming to reduce risk. We present a first-of-its-kind globally harmonized spatial dataset for the representation of CI.

In this study the users generated: (1) a harmonized detailed geospatial data of the world’s main CI systems into a single geospatial database; and (2) a Critical Infrastructure Spatial Index (CISI) to express the global spatial intensity of CI. The datasets are generated from Open Streetmap extract from 8th January 2021 using https://planet.openstreetmap.org/. You can read the [full paper here](https://www.nature.com/articles/s41597-022-01218-4). You can download the spatial extracts for both the feature type and the Critical Infrastructure Spatial Index (CISI) [here](https://zenodo.org/record/4957647#.Yl5lhFzMJct)

Disclaimer: Whole or parts of the dataset description was provided by the author(s) or their works.

#### Paper citation

```
Nirandjan, S., Koks, E.E., Ward, P.J. et al. A spatially-explicit harmonized global dataset of critical infrastructure. Sci Data 9, 150 (2022).
https://doi.org/10.1038/s41597-022-01218-4
```


#### Dataset citation

```
Nirandjan, Sadhana, Koks, Elco E., Ward, Philip J., & Aerts, Jeroen C.J.H. (2021). A spatially-explicit harmonized global dataset of critical infrastructure (v1.0.0.)
[Data set]. Zenodo. https://doi.org/10.5281/zenodo.4957647
```

![cisi](https://user-images.githubusercontent.com/6677629/168509625-651d2582-0518-41bf-897e-e1468af52c95.gif)


#### Earth Engine Snippet

```js
var global_CISI = ee.Image("projects/sat-io/open-datasets/CISI/global_CISI"),
var infrastructure = ee.ImageCollection("projects/sat-io/open-datasets/CISI/amount_infrastructure");
```

Sample Code: https://code.earthengine.google.com/b4dbaceee9c3f46599a6f2f921042b13


#### License
This work is licensed under a Creative Commons Attribution 4.0 International license.

Produced by : Nirandjan, S., Koks, E.E., Ward, P.J. et al

Curated in GEE by : Samapriya Roy

Keywords: : Development indicator, global spatial data, gridded data, critical infrastructure, spatial index

Last updated on GEE: 2022-05-12
