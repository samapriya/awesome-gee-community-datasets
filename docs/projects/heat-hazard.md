# Global Extreme Heat Hazard

Published by the World Bank (2017), this is a global data layer for extreme heat hazard, which is classified based on an existing and widely
accepted heat stress indicator, the Wet Bulb Globe Temperature (WBGT, in °C) – more specifically the daily maximum WGBT. The WBGT has an obvious
relevance for human health, but it is relevant in all kinds of projects and sectors, including infrastructure related, as heat stress affects
personnel and stakeholders, and therefore the design of buildings and infrastructure. Heat stress studies in the scientific literature that make use
of the WBGT apply thresholds of 28°C and 32°C to categorise heat stress risk. The damaging intensity thresholds are applied following this
definition of slight/low (<28°C), moderate/high (28-32°C) and severe/very high (>32°C) heat stress. This dataset is licensed under Creative Commons
Attribution 4.0. You can [download the report here](https://datacatalogfiles.worldbank.org/ddh-published/0040194/DR0087127/VITO%20-%20Extreme%20heat%20Final_report_v2.pdf?versionId=2022-06-24T15:35:23.0634409Z). Point of contact: sfraser@worldbank.org

Extra Info: There are three global GeoTIFF files in total, which can be combined into one single collection 5 year, 20 year and 100 year return period.

![gehh](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/30e5d77c-ee26-4252-80a0-74aee4dce3c3)

#### Earth Engine Snippet

```js
var global_extreme_heat_hazard = ee.ImageCollection('projects/sat-io/open-datasets/WORLD-BANK/global-ext-heat-hazard');
```

Sample code: : https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/GLOBAL-EXTREME-HEAT-HAZARD


#### License
This dataset is classified as Public under the Access to Information Classification Policy. Users inside and outside the Bank can access this dataset under a Creative Commons Attribution 4.0

Curated by: Koen De Ridder, Dirk Lauwaet, Hans Hooyberghs and Filip Lefebre from VITO (Author)

Keywords: Hazard Assessment, Extreme Heat, Climatology, Climate Change

Last updated: Mar 1, 2017

