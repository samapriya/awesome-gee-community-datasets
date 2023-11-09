# Global Land subsidence mapping

This dataset centers on the creation of a global land subsidence dataset through the use of advanced geospatial and modeling techniques. The study investigates the relationships between groundwater stress, aquifer depletion, and land subsidence on a worldwide scale. Employing remote sensing data and model-based datasets, a machine learning model has been developed to predict land subsidence at a remarkably high spatial resolution of approximately 2 kilometers. The outcomes of this study include a comprehensive estimation of global land subsidence magnitude, a first-order assessment of aquifer storage loss due to consolidation, and the quantification of key factors driving subsidence. Notably, a significant portion of the observed subsidence is concentrated in cropland and urban areas, underscoring the urgency of adopting sustainable groundwater management practices in these regions. This dataset is invaluable for understanding the spatial distribution of subsidence in both known and previously unidentified groundwater-stressed areas worldwide.

The global land subsidence dataset is a pioneering effort in characterizing the complex interplay between groundwater dynamics, land subsidence, and aquifer storage loss. By leveraging machine learning and comprehensive datasets, this study contributes to a deeper understanding of the environmental challenges posed by excessive groundwater pumping and highlights the need for proactive measures to safeguard water resources and mitigate land subsidence impacts, particularly in regions facing water scarcity and population growth. You can read the [full paper here](https://www.nature.com/articles/s41467-023-41933-z). You can find additional information [in this GitHub repository](https://github.com/mdfahimhasan/Global-Subsidence-Groundwater).

#### Citation

```
Hasan, M.F., Smith, R., Vajedian, S. et al. Global land subsidence mapping reveals widespread loss of aquifer storage capacity.
Nat Commun 14, 6180 (2023). https://doi.org/10.1038/s41467-023-41933-z
```

#### Dataset citation

```
Hasan, M. F., R. Smith, S. Vajedian, R. Pommerenke, S. Majumdar (2023). Global Land Subsidence Mapping Reveals Widespread Loss of Aquifer Storage
Capacity Datasets, HydroShare, https://doi.org/10.4211/hs.dc7c5bfb3a86479b889d3b30ab0e4ef7
```

![land_subsidence_small](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/4c84a470-3acf-4866-9338-6ca0eec59f2f)

#### Earth Engine Snippet

```js
var subsidence_prediction_probability = ee.Image("projects/sat-io/open-datasets/global_subsidence/Final_subsidence_proba_greater_1cm_2013_2019_recoded");
var subsidence_prediction_recoded = ee.Image("projects/sat-io/open-datasets/global_subsidence/Final_subsidence_prediction_recoded");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:geophysical-biological-biogeochemical/GLOBAL-LAND-SUBSIDENCE

#### License

This resource is shared under the [Creative Commons Attribution CC BY](http://creativecommons.org/licenses/by/4.0/)

Created by: Hasan, M. F., R. Smith, S. Vajedian, R. Pommerenke, S. Majumdar

Curated in GEE by: Samapriya Roy

Keywords: machine learning,global groundwater,groundwater monitoring,land subsidence, InSAR

Last updated: 2023-11-08

