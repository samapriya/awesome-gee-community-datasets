# Global Forest Carbon Fluxes (2001-2021)

Net forest carbon flux represents the net exchange of carbon between forests and the atmosphere between 2001 and 2021, calculated as the balance between carbon emitted by forests and removed by (or sequestered by) forests during the model period (megagrams CO2 emissions/ha). Net carbon flux is calculated by subtracting average annual gross removals from average annual gross emissions in each modeled pixel; negative values are where forests were net sinks of carbon and positive values are where forests were net sources of carbon between 2001 and 2021. Net fluxes are calculated following IPCC Guidelines for national greenhouse gas inventories in each pixel where forests existed in 2000 or were established between 2000 and 2012 according to the Global Forest Change tree cover change data of Hansen et al. (2013). This layer reflects the cumulative net flux during the model period (2001-2021) and must be divided by 20 to obtain average annual net flux; net flux values cannot be assigned to individual years of the model.

Forest carbon removals from the atmosphere (sequestration) by forest sinks represent the cumulative carbon captured (megagrams CO2/ha) by the growth of established and newly regrowing forests during the model period between 2001-2021. Removals include accumulation of carbon in both aboveground and belowground live tree biomass. Following IPCC Tier 1 assumptions for forests remaining forests, removals by dead wood, litter, and soil carbon pools are assumed to be zero. In each pixel, carbon removals are calculated following IPCC Guidelines for national greenhouse gas inventories where forests existed in 2000 or were established between 2000 and 2012 according to the Global Forest Change tree cover loss data of Hansen et al. (2013). Carbon removed by each pixel is based on maps of forest type (e.g., mangrove, plantation), ecozone (e.g., humid Neotropics), forest age (e.g., primary, old secondary), and number of years of carbon removal. This layer reflects the cumulative removals during the model period (2001-2021) and must be divided by 20 to obtain an annual average during the model duration; removal rates cannot be assigned to individual years of the model.

Forest carbon emissions represent the greenhouse gas emissions arising from stand-replacing forest disturbances that occurred in each modeled year (megagrams CO2 emissions/ha, between 2001 and 2021). Emissions include all relevant ecosystem carbon pools (aboveground biomass, belowground biomass, dead wood, litter, soil) and greenhouse gases (CO2, CH4, N2O). Emissions estimates for each pixel are calculated following IPCC Guidelines for national greenhouse gas inventories where stand-replacing disturbance occurred, as mapped in the Global Forest Change annual tree cover loss data of Hansen et al. (2013). The carbon emitted from each pixel is based on carbon densities in 2000, with adjustment for carbon accumulated between 2000 and the year of disturbance. Emissions reflect a gross estimate, i.e., carbon removals from subsequent regrowth are not included. Instead, gross carbon removals resulting from subsequent regrowth after clearing are accounted for in the companion forest carbon removals layer. The fraction of carbon emitted from each pixel upon disturbance (emission factor) is affected by several factors, including the direct driver of disturbance, whether fire was observed in the year of or preceding the observed disturbance event,  whether the disturbance occurred on peat, and more. All emissions are assumed to occur in the year of disturbance. Emissions can be assigned to a specific year using the Hansen tree cover loss data.

All three layers are part of the forest carbon flux model described in [Harris et al. (2021)](https://www.nature.com/articles/s41558-020-00976-6). This paper introduces a geospatial monitoring framework for estimating global forest carbon fluxes which can assist governments and non-government actors with tracking greenhouse gas fluxes from forests and decreasing emissions or increasing removals by forests. All input layers were resampled to a common resolution of 0.00025 x 0.00025 degrees each to match Hansen et al. (2013).

Disclaimer: Parts or all of the dataset description is borrowed from existing description provided by authors.

#### Dataset preprocessing
The tiled imagery for the three layers emissions, removals and net flux were combined into individual GEE image objects using GDAL before ingested. LZW compression and tiling was applied during mosaic operation.

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

Sample code: https://code.earthengine.google.com/d6d6390f0a9eafdaeb9766022b64065e

#### License

The Global Forest Carbon Fluxes (2001-2019) products are provided free of charge, without restriction of use. For the full license information see the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/) publications, models and data products that make use of these datasets must include proper acknowledgement, including citing the datasets and the journal article as in the following citation.

Created by: Harris, N.L., Gibbs, D.A., Baccini, A. et al

Curated in GEE by: Samapriya Roy

Keywords: Carbon emissions, forest change, climate, carbon

Last updated on GEE: 2022-04-27
