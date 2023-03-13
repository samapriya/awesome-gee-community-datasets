# Digital Earth Africa's cropland extent map Africa 2019

These maps shows the estimated location of croplands in the following countries for the period January to December 2019 where cropland is defined as a piece of land of minimum 0.01 ha (a single 10m x 10m pixel) that is sowed/planted and harvestable at least once within the 12 months after the sowing/planting date. It was also noted that "This definition will exclude non-planted grazing lands and perennial crops which can be difficult for satellite imagery to differentiate from natural vegetation." The provisional cropland extent maps have a resolution of 10 metres, and were built using Copernicus Sentinel-2 satellite images from 2019. The cropland extent maps were built seperately using extensive training data from Eastern, Western, Northern, and Sahel Africa, coupled with a Random Forest machine learning model. A detailed exploration of the methods used to produce the cropland extent map can be found in the [Jupyter Notebooks in DE Africa’s crop-mask](https://github.com/digitalearthafrica/crop-mask). Easiest place to download the datasets is from [AWS Open data registry](https://registry.opendata.aws/deafrica-crop-extent/)

* crop_mask: Entire African continent
* crop_mask_eastern: Tanzania, Kenya, Uganda, Ethiopia, Rwanda, and Burundi
* crop_mask_western: Nigeria, Benin, Togo, Ghana, Cote d’Ivoire, Liberia, Sierra Leone, Guinea, and Guinea-Bissau
* crop_mask_northern: Morocco, Algeria, Tunisia, Libya, and Egypt
* crop_mask_sahel: Mauritania, Senegal, Gambia, Mali, Burkina Faso, Niger, Chad, Sudan, South Sudan, Somalia, and Djibouti
* crop_mask_southern: South Africa, Namibia, Botswana, Lesotho, and Eswanti
* crop_mask_southeast: Zimbabwe, Zambia, Mozambique, and Malawi
* crop_mask_central: Angola, Democratic Republic of the Congo, Congo, Gabon, Cameroon, Equatorial Guinea, and Central African Republic
* crop_mask_indian_ocean: Madagascar, Mauritius, Reunion, and Comoros

The products contain three measurements:

* mask: This band displays cropped regions as a binary map. Values of 1 indicate the presence of crops, while a value of 0 indicates the absence of cropping. This band is a pixel-based cropland extent map, meaning the map displays the raw output of the pixel-based Random Forest classification.

* prob: This band displays the prediction probabilities for the ‘crop’ class. As this service uses a random forest classifier, the prediction probabilities refer to the percentage of trees that voted for the random forest classification. For example, if the model had 200 decision trees in the random forest, and 150 of the trees voted ‘crop’, the prediction probability is 150 / 200 x 100 = 75 %. Thresholding this band at > 50 % will produce a map identical to mask.

* filtered: This band displays cropped regions as a binary map. Values of 1 indicate the presence of crops, while a value of 0 indicates the absence of cropping. This band is an object-based cropland extent map where the mask band has been filtered using an image segmentation algorithm [see this paper for details on the algorithm used](https://www.mdpi.com/2072-4292/6/7/6111/htm). During this process, segments smaller than 1 Ha (100 10m x 10m pixels) are merged with neighbouring segments, resulting in a map where the smallest classified region is 1 Ha in size. The filtered dataset is provided as a complement to the mask band; small commission errors are removed by object-based filtering, and the ‘salt and pepper’ effect typical of classifying pixels is diminished.

|Band ID |Description               |Value range|Data type|NoData/Fill value|
|--------|--------------------------|-----------|---------|-----------------|
|mask    |crop extent (pixel)       |0 - 1      |uint8    |0                |
|prob    |crop probability (pixel)  |0 - 100    |uint8    |0                |
|filtered|crop extent (object-based)|0 - 1      |uint8    |0                |


You can details on the [method and more here](https://docs.digitalearthafrica.org/en/latest/data_specs/Cropland_extent_specs.html)

Disclaimer: Parts or all of the dataset description is borrowed from existing description provided by authors.

#### Preprocessing for GEE

All images were download and merged into single collections. The metadata tags including regions, versions were maintained from the STAC metadata JSON files provided for the regional downloads. Validation datasets for each region were downloaded ingested and merged into a single feature collection.

![dea_cropmask](https://user-images.githubusercontent.com/6677629/224822199-ec9c800f-e6be-489d-9e94-3a9d82c893f1.gif)

#### Earth Engine snippet

```js
var filtered = ee.ImageCollection("projects/sat-io/open-datasets/DEAF/CROPLAND-EXTENT/filtered")
var mask = ee.ImageCollection("projects/sat-io/open-datasets/DEAF/CROPLAND-EXTENT/mask");
var prob = ee.ImageCollection("projects/sat-io/open-datasets/DEAF/CROPLAND-EXTENT/prob");
var validation = ee.FeatureCollection("projects/sat-io/open-datasets/DEAF/CROPLAND-EXTENT/validation");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/DEA-CROPLAND-EXTENT

#### License

This dataset is made available under the CC BY Attribution 4.0 International License.

Created by: Digital Earth Africa

Curated by: Samapriya Roy

Keywords: agriculture, cog, deafrica, earth observation, food security, geospatial, satellite imagery, stac,sustainability

Last updated in GEE: 2023-03-13

