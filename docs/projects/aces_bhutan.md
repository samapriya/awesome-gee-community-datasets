# ACES-Enhanced Rice Crop Maps for Bhutan (2016-2022)

Annual crop type rice maps for 2016-2022 for enabling improved food security decision making has remained a challenge in Bhutan. These maps were developed in collaboration with the Bhutan Department of Agriculture and SERVIR. Through focusing on advancing Science, Technology, Engineering, and Mathematics (STEM) in Bhutan, an effort to co-develop a geospatial application known as the [Agricultural Classification and Estimation Service (ACES)](https://github.com/SERVIR/ag-classification-estimation/tree/main) was created. This dataset and paper focuses on the co-development of an Earth observation informed climate smart crop type framework which incorporates both modeling and training sample collection. The [ACES web application](https://servirglobalnet.users.earthengine.app/view/aces-bhutan) and subsequent ACES modeling software package enables stakeholders to more readily use Earth observation into their decision making process. Additionally, this data set and paper offers a transparent and replicable approach for addressing and combating remote sensing limitations due to topography and cloud cover, a common problem in Bhutan. Lastly, this approach resulted in a Random Forest "LTE 555" model, from a set of 3,600 possible models, with an overall test Accuracy of 85% and F-1 Score of .88 for 2020. The model was independently validated resulting in an independent accuracy of 83% and F-1 Score of .45 for 2020.

#### Citation

```
Mayer, Timothy, Biplov Bhandari, Filoteo Gómez Martínez, Kaitlin Walker, Stephanie A. Jiménez, Meryl Kruskopf, Micky Maganini et al. "Employing the
agricultural classification and estimation service (ACES) for mapping smallholder rice farms in Bhutan."
Frontiers in Environmental Science 11 (2023): 1137835.
```

![aces-rice-bhutan](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/8c6625d6-9ac1-4b0f-8543-a0f267dc4130)

#### Earth Engine Snippet

```js
var Bhutan_ACES_Rice_Maps = ee.ImageCollection("projects/servir-sco-assets/assets/Bhutan/Rice_Extent_Mapper/Predicted_Rice_Post_Processed_IC");
Map.setCenter(90.37, 27.51,8)
var palettes = require('users/gena/packages:palettes');

var snazzy = require("users/aazuspan/snazzy:styles");
snazzy.addStyle("https://snazzymaps.com/style/132/light-gray", "Grayscale");

Map.addLayer(Bhutan_ACES_Rice_Maps,{min: 0,max: 1, palette: ["fee6ce","fdae6b","e6550d"]},
"ACES Rice Maps 2016-2022 ")
```

Sample code:  https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/ACES-BHUTAN

#### License
This dataset is available under a Creative Commons BY-4.0 license

Keywords: agriculture, land use, land cover, Bhutan, rice

Created & provided by: Mayer et al 2023, NASA SERVIR

Curated by: Mayer et al 2023, NASA SERVIR
