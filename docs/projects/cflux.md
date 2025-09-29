# Global Forest Carbon Fluxes (2001-2024)

Net forest carbon flux represents the net exchange of carbon between forests and the atmosphere between 2001 and 2024, calculated as the balance between carbon emitted by forests and removed by (or sequestered by) forests during the model period (megagrams CO2 emissions/ha). Net carbon flux is calculated by subtracting average annual gross removals from average annual gross emissions in each modeled pixel; negative values are where forests were net sinks of carbon and positive values are where forests were net sources of carbon between 2001 and 2024. Net fluxes are calculated following IPCC Guidelines for national greenhouse gas inventories in each pixel where forests existed in 2000 or were established between 2000 and 2020 according to the Global Forest Change tree cover change data of Hansen et al. (2013) and Potapov et al. (2022). This layer reflects the cumulative net flux during the model period (2001-2024) and must be divided by 24 to obtain average annual net flux; net flux values cannot be assigned to individual years of the model.

Forest carbon removals from the atmosphere (sequestration) by forest sinks represent the cumulative carbon captured (megagrams CO2/ha) by the growth of established and newly regrowing forests during the model period between 2001-2024. Removals include accumulation of carbon in both aboveground and belowground live tree biomass. Following IPCC Tier 1 assumptions for forests remaining forests, removals by dead wood, litter, and soil carbon pools are assumed to be zero. In each pixel, carbon removals are calculated following IPCC Guidelines for national greenhouse gas inventories where forests existed in 2000 or were established between 2000 and 2020 according to the Global Forest Change tree cover loss data of Hansen et al. (2013) and tree cover gain data of Potapov et al. (2022). Carbon removed by each pixel is based on maps of forest type (e.g., mangrove, plantation), ecozone (e.g., humid Neotropics), forest age (e.g., primary, old secondary), and number of years of carbon removal. This layer reflects the cumulative removals during the model period (2001-2024) and must be divided by 24 to obtain an annual average during the model duration; removal rates cannot be assigned to individual years of the model.

Forest carbon emissions represent the greenhouse gas emissions arising from stand-replacing forest disturbances that occurred in each modeled year (megagrams CO2 emissions/ha, between 2001 and 2023). Emissions include all relevant ecosystem carbon pools (aboveground biomass, belowground biomass, dead wood, litter, soil) and greenhouse gases (CO2, CH4, N2O). Emissions estimates for each pixel are calculated following IPCC Guidelines for national greenhouse gas inventories where stand-replacing disturbance occurred, as mapped in the Global Forest Change annual tree cover loss data of Hansen et al. (2013). The carbon emitted from each pixel is based on carbon densities in 2000, with adjustment for carbon accumulated between 2000 and the year of disturbance. Emissions reflect a gross estimate, i.e., carbon removals from subsequent regrowth are not included. Instead, gross carbon removals resulting from subsequent regrowth after clearing are accounted for in the companion forest carbon removals layer. The fraction of carbon emitted from each pixel upon disturbance (emission factor) is affected by several factors, including the direct driver of disturbance, whether fire was observed in the year of or preceding the observed disturbance event, whether the disturbance occurred on peat, and more. All emissions are assumed to occur in the year of disturbance. Emissions can be assigned to a specific year using the Hansen tree cover loss data.

All three layers are part of the forest carbon flux model described in [Harris et al. (2021)](https://www.nature.com/articles/s41558-020-00976-6) and updated in Gibbs et al. (2025). This paper introduces a geospatial monitoring framework for estimating global forest carbon fluxes which can assist governments and non-government actors with tracking greenhouse gas fluxes from forests and decreasing emissions or increasing removals by forests. All input layers were resampled to a common resolution of 0.00025 x 0.00025 degrees each to match Hansen et al. (2013). Please also find the dataset on [Global Forest Watch](https://gfw.global/3jLklJ9).

Disclaimer: Parts or all of the dataset description is borrowed from existing description provided by authors.

#### Dataset updates

Each year, the tree cover loss, drivers of tree cover loss, and burned area are updated. Since 2023, multiple model input data sets and constants have been changed to improve accuracy and incorporate the latest scientific advances. Please refer to [this blog post](https://www.globalforestwatch.org/blog/data/whats-new-carbon-flux-monitoring) for detailed information on all updates.

#### Citation

```
Harris, N.L., Gibbs, D.A., Baccini, A. et al. Global maps of twenty-first century forest carbon fluxes. Nat. Clim. Chang. 11, 234–240 (2021).
https://doi.org/10.1038/s41558-020-00976-6
```

![flux_compressed](https://user-images.githubusercontent.com/6677629/167321603-e46c580c-9ba9-438e-a373-6d420ede7d54.gif)


```
var emissions = ee.Image("projects/sat-io/open-datasets/forest_carbon_fluxes/gross_emissions");
var removals = ee.Image("projects/sat-io/open-datasets/forest_carbon_fluxes/gross_removals");
var net_flux = ee.Image("projects/sat-io/open-datasets/forest_carbon_fluxes/net_flux");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/GLOBAL-FOREST-CARBON-FLUXES

#### License

The Global Forest Carbon Fluxes (2001-2024) products are provided free of charge, without restriction of use. For the full license information see the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/) publications, models and data products that make use of these datasets must include proper acknowledgement, including citing the datasets and the journal article as in the following citation.

Created by: Harris, N.L., Gibbs, D.A., Baccini, A. et al

Curated in GEE by: David Gibbs, Melissa Rose, Nancy Harris and Samapriya Roy

Keywords: Carbon emissions, forest change, climate, carbon, greenhouse gas, IPCC, removals, sequestration

Last updated on GEE: 2025-09-28

#### Changelog

### Version 1.4.2 (2025)
**Major updates discussed in the [GFW blog post](https://www.globalforestwatch.org/blog/data/whats-new-carbon-flux-monitoring/)**

**Model Updates:**
- Updated to year 2024 tree cover loss data
- **Fire emission combustion factors:** Updated from 2006 IPCC Guidelines to 2019 Refinement values for boreal and temperate forests. This significantly reduces combustion factors in temperate forests where fires are associated with natural disturbances or unknown drivers
- **Soil carbon emission factors:** Updated stock-change factors for mineral soil with revised IPCC values. Factors are now higher for tropical forests when forests are converted to permanent agriculture
- **Emissions from mineralization of soil nitrogen:** Added N₂O emissions from soil nitrogen mineralization following IPCC guidelines where driver of tree cover loss is permanent agriculture, shifting cultivation, hard commodity production, or settlement and infrastructure
- **Higher resolution drivers of tree cover loss:** Updated from 10-km Curtis et al. 2018 map to 1-km Sims et al. 2025 map, including additional drivers at smaller spatial scales (natural disturbances other than wildfires, hard commodities like mining)
