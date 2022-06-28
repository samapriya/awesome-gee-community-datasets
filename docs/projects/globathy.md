# GLOBathy (Global lakes bathymetry dataset)

We developed a novel GLObal Bathymetric (GLOBathy) dataset of 1.4+ million waterbodies to align with the well-established global dataset, HydroLAKES. GLOBathy uses a GIS-based framework to generate bathymetric maps based on the waterbody maximum depth estimates and HydroLAKES geometric/geophysical attributes of the waterbodies. The maximum depth estimates are validated at 1,503 waterbodies, making use of several observed data sources.

We also provide estimations for head-Area-Volume (h-A-V) relationships of the HydroLAKES waterbodies, driven from the bathymetric maps of the GLOBathy dataset. The h-A-V relationships provide essential information for water balance and hydrological studies of global waterbody systems. You can read the [full paper here](https://www.nature.com/articles/s41597-022-01132-9)

You can find the [datasets here](https://springernature.figshare.com/articles/dataset/GLOBathy_Bathymetry_Rasters/13404635)

Disclaimer: Parts or all of the dataset description is borrowed from existing description provided by authors.

#### Citation

```
Khazaei, B., Read, L.K., Casali, M. et al. GLOBathy, the global lakes bathymetry dataset. Sci Data 9, 36 (2022).
https://doi.org/10.1038/s41597-022-01132-9
```

#### Dataset citation

```
Khazaei, Bahram; Read, Laura K; Casali, Matthew; Sampson, Kevin M; Yates, David N (2022): GLOBathy Bathymetry Rasters. figshare.
Dataset. https://doi.org/10.6084/m9.figshare.13404635.v1
```

![globathy](https://user-images.githubusercontent.com/6677629/176226039-1b9fb8fa-4017-4f89-9347-d7cf268bb24d.gif)

#### Earth Engine Snippet

```js
var globathy = ee.Image("projects/sat-io/open-datasets/GLOBathy/GLOBathy_bathymetry");
var globathy_param = ee.FeatureCollection("projects/sat-io/open-datasets/GLOBathy/GLOBathy_basic_parameters");
```

Sample Code: https://code.earthengine.google.com/1b440cac2b9e8cd3ece21f9a021cd3a3


#### License

The dataset is released under an assumed CC0 1.0 Universal (CC0 1.0) Public Domain Dedication. The organizations responsible for generating and funding this dataset make no representations of any kind including, but not limited to the warranties of merchantability or fitness for a particular use, nor are any such warranties to be implied with respect to the data. Although every effort has been made to ensure the accuracy of information, errors may be reflected in data supplied. The user must be aware of data conditions and bear responsibility for the appropriate use of the information with respect to possible errors.

Produced by: Khazaei, B., Read, L.K., Casali, M. et al.

Curated in GEE by: Samapriya Roy

Keywords: bathymetry and depth, lake systems, reservoir management, Hydrological Modelling, Limnology, Geographic information systems (GIS), Geomorphology, topographic analysis

Last updated on GEE: 2022-01-26
