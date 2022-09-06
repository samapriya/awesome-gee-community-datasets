# Aboveground carbon accumulation in global monoculture plantation forests

Restoring forest cover is a key action for mitigating climate change. Although monoculture plantations dominate existing commitments to restore forest cover, we lack a synthetic view of how carbon accumulates in these systems. Here, we assemble a global database of 4756 field-plot measurements from monoculture plantations across all forested continents. With these data, we model carbon accumulation in aboveground live tree biomass and examine the biological, environmental, and human drivers that influence this growth.

This project systematically reviewed the literature for measurements of aboveground carbon stocks in monoculture plantation forests. The data compiled here are for monoculture (single-species) plantation forests, which are a subset of a broader review to identify empirical measurements of carbon stocks across all forest types. The database is structured similarly to that of the ForC (https://forc-db.github.io/) and GROA databases (https://github.com/forc-db/GROA). You can read [the paper here](https://www.nature.com/articles/s41467-022-31380-7)

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Dataset Preprocessing
To connect site id lat long to studies a code was written to iterate through all sites and studies and link with lat long. This was then ingested as a combined table.

#### Paper Citation

```
Bukoski, J.J., Cook-Patton, S.C., Melikov, C. et al. Rates and drivers of aboveground carbon accumulation in global monoculture plantation forests.
Nat Commun 13, 4206 (2022). https://doi.org/10.1038/s41467-022-31380-7
```

#### Data Citation

```
Bukoski, Jacob, Cook-Patton, Susan C., Melikov, Cyril, Ban, Hongyi, Chen, Jessica Liu, Goldman, Elizabeth D., Harris, Nancy L., & Potts, Matthew D.
(2022). Global Plantation Forest Carbon database (1.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.6555216
```

![monoculture](https://user-images.githubusercontent.com/6677629/188673963-c8d84d66-c1ff-4d25-9b12-63e3f6c1a4ab.gif)


#### Earth Engine Snippet

```js
var global_fertilizer_use = ee.FeatureCollection("projects/sat-io/open-datasets/global-monoculture-plantations");
```

Sample code: https://code.earthengine.google.com/243774c7f7cdbec21c3450c4fa8a64fb

#### License

This work is licensed under a Creative Commons Attribution 4.0 International license.

Created by: Bukoski, Jacob et al 2022

Curated in GEE by : Samapriya Roy

keywords: Forests, Aboveground carbon stocks, Climate change, Reforestation, Plantations, Aboveground biomass

Last modified: 2022-05-16

Last updated on GEE: 2022-09-05
