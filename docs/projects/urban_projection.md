# Global urban projections under SSPs (2020-2100)

These datasets include two separate global projections of future urban land under shared socioeconomic pathways (SSPs), one from Chen et al. (2020) and the other from Gao & O'Neill (2020). The Chen et al. dataset provides a binary classification of urban and non-urban land (pixel value of 2 for urban; 1 otherwise) at 1 km resolution for every 10th year from 2020 to 2100 (inclusive). On the other hand, the Gao & O'Neill (2020) dataset provides continuous values representing the probability of full urbanization of each 1/8 degree grid for the same years.

When using these future projections, it is important to recognize that they are based on different methodologies, different training data, and different assumptions about future scenarios. For instance, the Gao & O'Neill dataset considers broad urbanization patterns across 375 sub-regions, while the Chen et al. data uses 32 regions. While both of these datasets are trained using the Global Human Settlement Layer (GHSL), the Chen et al. data are further calibrated against the European Space Agency's Climate Change Initiative (ESA CCI) data for 2015.  There are many other differences and users should ideally go through the assumptions and methodology described in the respective papers before using the data.

As an example of these differences, below is a plot of projected urban percentage over time for Asia for different SSP scenarios from these datasets and the Li et al. (2021) urban extent data, which is also in the community catalog. Note that the Li et al. data are not based on GHSL, but on historical urban extent dataset from nighttime lights:

#### Dataset notes

* (Chen et al 2020): This dataset provides future estimates of urban expansion for all Shared Socioeconomic Pathways (SSPs) every 10 years from 2020 to 2100 (inclusive). The data are at 1 km resolution. Pixels have a value of 2 (for urban) or 1 (for non-urban). Each image corresponds to a date and there are separate bands for each SSP scenario.

* (Gao et al 2020): This dataset provides future estimates of urban expansion for all Shared Socioeconomic Pathways (SSPs) every 10 years from 2020 to 2100 (inclusive). The data are at 1/8 degree resolution. Probabilities of conversion of entire grid to urban is provided instead of a binary classification. Each image corresponds to a date and there are separate bands for each SSP scenario.

#### Citation

```
Chen, G., Li, X., Liu, X. et al. Global projections of future urban land expansion under shared socioeconomic pathways. Nat Commun 11, 537 (2020).
https://doi.org/10.1038/s41467-020-14386-x
```

```
Gao, J., O’Neill, B.C. Mapping global urban land for the 21st century with data-driven simulations and Shared Socioeconomic Pathways. Nat Commun 11,
2302 (2020). https://doi.org/10.1038/s41467-020-15788-7
```

![urban_scenarios](https://user-images.githubusercontent.com/6677629/197396105-9d87e4be-fb9b-4a31-8ff8-c0c4bb77c6bb.gif)


#### Earth Engine snippet

```js
var chenSSP = ee.ImageCollection("projects/sat-io/open-datasets/FUTURE-URBAN-LAND/CHEN_2020_2100");
var gaoSSP = ee.ImageCollection("projects/sat-io/open-datasets/FUTURE-URBAN-LAND/GAO_2020_2100");
```

https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/GLOBAL-URBAN-SCENARIO-PROJECTIONS

#### License

This work is licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/legalcode) for Gao et al 2022 and under [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-nc-sa/4.0/) for Chen et al 2020.

Created by: Gao, et al. 2022 and Chen, et al. 2022

Curated in GEE by : [TC Chakraborty](tc.chakraborty25@gmail.com) and Samapriya Roy

Keywords: urban, SSPs, urban projection, temporal models

Last updated on GEE: 2022-10-23
