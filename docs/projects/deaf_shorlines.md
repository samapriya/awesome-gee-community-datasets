# Digital Earth Africa Coastlines

The Digital Earth Africa Coastlines is a continental dataset that includes annual shorelines and rates of coastal change along the entire African coastline. This is a provisional service that has been generated for 2000 to 2021 and we would like to improve and operationalize with users.

The product combines satellite data from the Digital Earth Africa program with tidal modelling to map the typical location of the coastline at mean sea level each year. The product enables trends of coastal erosion and growth to be examined annually at both a local and continental scale, and for patterns of coastal change to be mapped historically and updated regularly as data continues to be acquired. This allows current rates of coastal change to be compared with that observed in previous years or decades.

The ability to map shoreline positions for each year provides valuable insights into whether changes to the coastline are the result of particular events or actions, or a process of more gradual change over time. This information can enable scientists, managers, and policy makers to assess impact from the range of drivers impacting the coastlines and potentially assist planning and forecasting for future scenarios.  You can find [additional details here](https://docs.digitalearthafrica.org/en/latest/data_specs/Coastlines_specs.html) and you can [download the datasets here](https://docs.digitalearthafrica.org/en/latest/data_specs/Coastlines_specs.html#Data-Access)

#### Acknowledgment

The Coastlines algorithms incorporated in this product are the work of Robbi-Bishop Taylor, Rachel Nanson, Stephen Sagar, and Leo Lymburner, Geoscience Australia. Digital Earth Africa acknowledges the work done by the Centre de Suivi Ecologique (CSE), Dakar, in assessing the accuracy of the service with the participation of West African WACA stakeholders. Acknowledgements also go to the Regional Center for Mapping Resources for Development (RCMRD) for stakeholder engagement and feedback. Digital Earth Africa thanks the Digital Earth Africa Product Development task team for the co-design, the co-development and early feedback on the Service.

#### Citation

```
Bishop-Taylor, R., Nanson, R., Sagar, S., Lymburner, L. 2021. Digital Earth Australia
Coastlines. Geoscience Australia, Canberra. https://doi.org/10.26186/116268
```

![deaf_coastlines](https://user-images.githubusercontent.com/6677629/227800600-609a2359-3234-4633-8a9d-aae8c37faa5f.gif)

```js
var shoreline_annual = ee.FeatureCollection("projects/sat-io/open-datasets/DEAF/COASTLINES/coastlines_v040_shorelines_annual");
var hotspot_zoom_1 = ee.FeatureCollection("projects/sat-io/open-datasets/DEAF/COASTLINES/coastlines_v040_hotspots_zoom_1");
var hotspot_zoom_2 = ee.FeatureCollection("projects/sat-io/open-datasets/DEAF/COASTLINES/coastlines_v040_hotspots_zoom_2");
var hotspot_zoom_3 = ee.FeatureCollection("projects/sat-io/open-datasets/DEAF/COASTLINES/coastlines_v040_hotspots_zoom_3");
var rate_of_change = ee.FeatureCollection("projects/sat-io/open-datasets/DEAF/COASTLINES/coastlines_v040_rates_of_change");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:oceans-shorelines/DEAF-Shorlines-V040

#### License
These datasets are made available under the CC BY 4.0 Attribution 4.0 International license. This license allows users to distribute, remix, adapt, and build upon the material in any medium or format, so long as attribution is given to the creator.

Created by: Digital Earth Africa

Curated in GEE by : Samapriya Roy

Keywords : Sea, ocean and coast, marine and coastal, coast, erosion, waterline extraction, subpixel waterlines, coastal change, DEAF CoastLines, coastline data, coastal erosion

Last updated : 2023-03-26
