# Irrecoverable carbon in Earth’s ecosystems

These datasets provide global maps of carbon density (aboveground, belowground biomass carbon and soil organic carbon stocks) for the year 2010 and 2018 at ~300-m spatial resolution in Mg ha-1 (Coordinate System: WGS 1984, float format). Input maps were collected from published literature, and where necessary, updated to cover the focal time period. These updates were applied to the manageable carbon, vulnerable carbon and irrecoverable carbon maps. Manageable carbon is carbon in terrestrial and coastal ecosystems that could experience an anthropogenic land-use conversion event . Vulnerable carbon is the carbon that would be that would be released in a typical land-use conversion. Irrecoverable carbon is  the carbon that, if lost, would not recover by mid-century.  Datasets are disaggregated for carbon density in biomass or soils. To view these datasets, go to:  https://irrecoverable.resilienceatlas.org/map. You can read the [open sourced paper here](https://www.nature.com/articles/s41893-021-00803-6)

### Preprocessing
All datasets tif files were ingested in Google Earth Engine, Ecosystem layers were ingested after removing the no data value to avoid conflict with a -128 no data value. The ecosystem categorical layers were also ingested with a mode sampling as recommended by GEE.

#### Paper Citation

```
Noon, M.L., Goldstein, A., Ledezma, J.C. et al. Mapping the irrecoverable carbon in Earth’s ecosystems.
Nat Sustain (2021). https://doi.org/10.1038/s41893-021-00803-6
```

#### Data Citation

```
Noon, Monica, Goldstein, Allie, Ledezma, Juan Carlos, Roehrdanz, Patrick, Cook-Patton, Susan C., Spawn-Lee, Seth A., Wright, Timothy Maxwell,
Gonzalez-Roglich, Mariano, Hole, David G., Rockström, Johan, & Turner, Will R. (2021). Mapping the irrecoverable carbon in Earth's ecosystems
(1.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4091029
```


![irrecoverable_carbon](https://user-images.githubusercontent.com/6677629/146130595-b1aba7d4-e290-4595-9e88-ca7015ce0232.gif)


#### Earth Engine Snippet

```js
var irrecoverable_carbon_total = ee.ImageCollection("projects/sat-io/open-datasets/irrecoverable_carbon/carbon_total");
var irrecoverable_carbon_soil = ee.ImageCollection("projects/sat-io/open-datasets/irrecoverable_carbon/carbon_soil");
var irrecoverable_carbon_biomass = ee.ImageCollection("projects/sat-io/open-datasets/irrecoverable_carbon/carbon_biomass");
var vulnerable_carbon_total = ee.ImageCollection("projects/sat-io/open-datasets/vulnerable_carbon/carbon_total");
var vulnerable_carbon_soil = ee.ImageCollection("projects/sat-io/open-datasets/vulnerable_carbon/carbon_soil");
var vulnerable_carbon_biomass = ee.ImageCollection("projects/sat-io/open-datasets/vulnerable_carbon/carbon_biomass");
var manageable_carbon_total = ee.ImageCollection("projects/sat-io/open-datasets/manageable_carbon/carbon_total");
var manageable_carbon_soil = ee.ImageCollection("projects/sat-io/open-datasets/manageable_carbon/carbon_soil");
var manageable_carbon_biomass = ee.ImageCollection("projects/sat-io/open-datasets/manageable_carbon/carbon_biomass");
var ecosystem_extent = ee.ImageCollection("projects/sat-io/open-datasets/ecosystem_extent");
```

Sample Code: https://code.earthengine.google.com/e166302e9534c3ee55aec98d883221bd

#### License

This work is licensed under the Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0). Users are free to use, copy, distribute, transmit, and adapt the work for commercial and non-commercial purposes, without restriction, as long as clear attribution of the source is provided.

Created by: Noon et al

Curated by: Samapriya Roy

Keywords: : irrecoverable carbon, vulnerable carbon, manageable carbon, global map, ecosystem

Last updated: 2021-12-14
