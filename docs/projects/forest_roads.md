# Congo Basin Forest Roads

This dataset provides high-detail mapping of road development in the tropical forests of the Congo Basin, created using Sentinel-1 and Sentinel-2 satellite imagery combined with a deep learning model. It delivers up-to-date road maps that are openly available and provide essential insights for forest conservation, sustainable management, and policy decisions.

Road construction in the Congo Basin forests, primarily driven by selective logging, poses significant ecological and climate risks. However, the full extent of these road networks, especially in remote areas, has been poorly understood. This dataset reveals all road networks established since 2019, providing a critical tool for studying the effects of logging, monitoring illegal forest activities, and assessing human impact on tropical forests at a large scale.

The road detection method integrates Sentinel-1 radar and Sentinel-2 optical imagery. Sentinel-2 provides high-resolution optical data in clear weather, while Sentinel-1's radar technology can penetrate clouds, offering consistent observation even during the rainy season. This combination ensures precise monthly updates on narrow and transient road segments. The map covers road development across the six Congo Basin countries: Cameroon, Central African Republic, Democratic Republic of the Congo, Equatorial Guinea, Gabon, and Republic of the Congo. You can read more in the [paper here](https://www.sciencedirect.com/science/article/pii/S0034425724004061).


| **Attribute** | **Description** |
|---------------|-----------------|
| NetworkID     | A unique ID for each connected road network. |
| SegLenM       | The length of the road segment (in meters). |
| NetLenM       | The length of the connected road network (in meters). |
| Month         | The road segment opening month. |
| Year          | The road segment opening year. |
| MonthNum      | The road segment opening month, depicted as a continuing count since the start of monitoring (e.g. 13 = January 2020). This attribute can be used for smooth and continuous temporal analyses or visualizations. |


#### Citation

```
Slagter, Bart, Kurt Fesenmyer, Matthew Hethcoat, Ethan Belair, Peter Ellis, Fritz Kleinschroth, Marielos Peña-Claros, Martin Herold, and Johannes Reiche. "Monitoring road
development in Congo Basin forests with multi-sensor satellite imagery and deep learning." Remote Sensing of Environment (2024): 114380.
```

#### Data Citation

```
Slagter, B., Fesenmyer, K., Hethcoat, M., Belair, E., Ellis, P., Kleinschroth, F., Peña-Claros, M., Herold, M., & Reiche, J. (2024). Forest roads (Congo Basin) [Data set]. In
Remote Sensing of Environment: Vol. xxx (1.02, Number xxx). Zenodo. https://doi.org/10.5281/zenodo.13739812
```

![forest_roads-ezgif com-optimize](https://github.com/user-attachments/assets/833ef019-504a-41a1-b934-0a2b1feb47fe)

#### Earth Engine Snippet

```js
var forest_roads = ee.FeatureCollection("projects/wurnrt-loggingroads/assets/distribution/forestroads_afr_2019-01_2024-12")
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/FOREST-ROADS

Earth Engine App: https://nrtwur.users.earthengine.app/view/forest-roads

#### License
These datasets are made available under the CC BY 4.0 Attribution 4.0 International license. This license allows users to distribute, remix, adapt, and build upon the material in any medium or format, so long as attribution is given to the creator.

Created by: Slagter et al. 2024

Curated in GEE by: Bart Slagter & Samapriya Roy

Keywords : Congo Basin, forest roads, road development, Sentinel-1, Sentinel-2, deep learning, selective logging, deforestation, illegal logging, forest conservation

Last updated in GEE: 2025-06-02

#### Changelog
- Annual updates to dataset to include 2024

