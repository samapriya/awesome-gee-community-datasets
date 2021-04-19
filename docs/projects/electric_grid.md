# Facebook Electrical Distribution Grid Maps

Facebook has produced a model to help map global medium voltage (MV) grid infrastructure, i.e. the distribution lines which connect high-voltage transmission infrastructure to consumer-serving low-voltage distribution. The data found here are model outputs for six select African countries: Malawi, Nigeria, Uganda, DRC, Cote D’Ivoire, and Zambia. The grid maps are produced using a new methodology that employs various publicly-available datasets (night time satellite imagery, roads, political boundaries, etc) to predict the location of existing MV grid infrastructure. The model documentation and code are also available , so data scientists and planners globally can replicate the model to expand model coverage to other countries where this data is not already available.

Building Electrical Grid Maps begins by taking monthly images from the VIIRS satellite, and creating a composite. We then apply a custom image processing filter to remove background and reflected light, and identify locations that consistently demonstrate night-time lighting. These then serve as a proxy for the existence of grid electricity. Using known electrical grids as templates based on data available from energydata.info, we employ a custom algorithm to connect the communities and infer grid paths based on their likelihood to follow roads, avoid water, and follow the shortest paths possible. You can find the model code and documentation here: https://github.com/facebookresearch/many-to-many-dijkstra

![fb_grid](https://user-images.githubusercontent.com/6677629/115174385-ca041f00-a08e-11eb-9aa2-5db7a652d156.gif)

Note: current model accuracy is approximately 70% when compared to existing ground-truthed data. Accuracy can be further improved by integrating other locally-relevant information into the model and running it again.

#### Earth Engine Snippet

```js
var gmv_raster = ee.ImageCollection("projects/sat-io/open-datasets/facebook/global_medium_voltage_grid")
var gmv_vector = ee.FeatureCollection("projects/sat-io/open-datasets/facebook/gmv_grid");
```

Sample Code: https://code.earthengine.google.com/679d2b03fb371331f1823d7b0a51f9fd

#### Resolution:
geotiff is provided at Bing Tile Level 20

#### Location
Côte d'Ivoire,  Democratic Republic of the Congo,  Malawi,  Nigeria,  Uganda,  Zambia

#### License

This work is distributed under the Creative Commons Attribution 4.0 License.

Curated by: Samapriya Roy

Keywords: Electrical Distribution Grid, Facebook, Ivory Coast, Democratic Republic of the Congo,  Malawi,  Nigeria,  Uganda,  Zambia

Last updated: 2021-04-17
