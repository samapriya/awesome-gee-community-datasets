# Ensemble Source Africa Cropland Mask 2016

In order to produce the most accurate cropland layer at 30 m spatial resolution for Africa, the cropland layers extracted from four remote sensing land cover datasets were integrated. The four datasets covered the period 2015 to 2017. Hence, the constructed cropland layer was produced for the nominal year 2016. To build the final layer, the cropland mapping accuracies of the four cropland layers were firstly investigated at the units of Agro-ecological zones. Then, the best cropland layers for all zones were spatially joined. The resulted cropland layer is a binary mask with higher overall accuracy than individual layers and more consistent with FAO official statistics. You can download [the datasets here](https://figshare.com/articles/dataset/A_30m_African_Cropland_Layer_for_2016_by_Integrating_Multiple_Remote_sensing_Crowdsource_and_Auxiliary_Datasets_/13520141). You can read [additional details from the paper here](https://www.tandfonline.com/doi/citedby/10.1080/20964471.2021.1914400)

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Citation

```
Nabil, Mohsen, Miao Zhang, Bingfang Wu, Jose Bofana, and Abdelrazek Elnashar. "Constructing a 30m African Cropland Layer for 2016 by Integrating
Multiple Remote sensing, crowdsourced, and Auxiliary Datasets." Big Earth Data 6, no. 1 (2022): 54-76.
```

#### Dataset Citation

```
Nabil, Mohsen; Zhang, Miao; Wu, Bingfang; Bofana, Jose; Elnashar, Abdelrazek (2021): A 30m African Cropland Layer for 2016 by Integrating Multiple
Remote sensing, Crowdsource, and Auxiliary Datasets.. figshare. Dataset. https://doi.org/10.6084/m9.figshare.13520141.v1
```

![cropland_mask_2016_af](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/fee77abf-89d6-4c34-83ba-32cee901adc7)

#### Earth Engine Snippet

```js
var af_cropmask_2016 = ee.Image("projects/sat-io/open-datasets/landcover/AF_Cropland_mask_30m_2016_v3");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/AF-CROPLAND-MASK-30M-2016

#### License
This dataset is made available under the CC BY Attribution 4.0 International License.

Created by: Nabil, Mohsen; Zhang, Miao; Wu, Bingfang; Bofana, Jose; Elnashar, Abdelrazek

Curated in GEE by: Samapriya Roy

Keywords: Agriculture, Africa, cropland, cropland maps, agriculture land use
