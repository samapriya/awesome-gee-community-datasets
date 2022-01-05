# Global Storm Surge Reconstruction (GSSR) database

The Global Storm Surge Reconstruction (GSSR) database includes daily maximum surge values for the past at 882 tide gauges distributed along the global coastline. The data-driven models employed for the surge reconstruction were developed by Tadesse et al. (2020). The authors use five different atmospheric reanalysis products with different spatial and temporal resolution to produce surge information for the periods covered by the different reanalyses. The reanalysis that leads to the best validation results is marked with "best reconstruction" (note that in some locations data is not available for all reanalyses as there is no overlap in the periods covered by the tide gauges and the reanalysis). You can read the [full paper here](https://rdcu.be/cjV3v) The full surge reconstruction for each reanalysis (comprised of 882 compressed individual .csv files for the different tide gauges) can be downloaded from the following links:

* [20-CR Surge Reconstruction [1836 - 2015]](https://downgit.github.io/#/home?url=https://github.com/moinabyssinia/webmap/tree/gh-pages/20cr)
* [ERA-20C Surge Reconstruction [1900 - 2010]](https://downgit.github.io/#/home?url=https://github.com/moinabyssinia/webmap/tree/gh-pages/era20c)
* [ERA-Interim Surge Reconstruction [1979 - 2019]](https://downgit.github.io/#/home?url=https://github.com/moinabyssinia/webmap/tree/gh-pages/eraint)
* [MERAA-2 Reconstruction [1980 - 2019]](https://downgit.github.io/#/home?url=https://github.com/moinabyssinia/webmap/tree/gh-pages/merra)
* [ERA-Five Reconstruction [1979 - 2019]](https://downgit.github.io/#/home?url=https://github.com/moinabyssinia/webmap/tree/gh-pages/erafive)

#### Citation

```
Tadesse, M.G., Wahl, T. A database of global storm surge reconstructions. Sci Data 8, 125 (2021).
https://doi.org/10.1038/s41597-021-00906-x
```

#### Data preprocessing

The combined merged download daily maximum surge values for individual tide gauges and reanalysis products for different sites were merged into master feature collections while still maintaining different reanalyses products. Since site names included special characters like + or # or spaces which are not allowed in GEE naming convention we applied a consistent find and replace strategy to provide some level of consistency between locations. However in any case we hope the lat long provides a more accurate representation of a site. Another thing to note is that the CSVs seemed to have been exported with the index column which is not very useful and especially since it was missing a header, so the index column was removed from all CSVs before being renamed and ingested.

|Reanalysis Type                                |GEE Feature Collection name     |
|-----------------------------------------------|--------------------------------|
|20-CR Surge Reconstruction [1836 - 2015]       |20-CR_surge_reconstruction      |
|ERA-20C Surge Reconstruction [1900 - 2010]     |era-20C_surge_reconstruction    |
|ERA-Interim Surge Reconstruction [1979 - 2019] |era-Interim_surge_reconstruction|
|MERAA-2 Reconstruction [1980 - 2019]           |merra-2_surge_reconstruction    |
|ERA-Five Reconstruction [1979 - 2019]          |era-5_surge_reconstruction      |


![gssr](https://user-images.githubusercontent.com/6677629/148161951-b57628b4-f683-4c0c-9c57-1cb632131659.gif)


#### Earth Engine Snippet

```js
var surge_20_cr =  ee.FeatureCollection("projects/sat-io/open-datasets/open-ocean/global_storm_surge_reconstruction/20-CR_surge_reconstruction");
var surge_era_20c =  ee.FeatureCollection("projects/sat-io/open-datasets/open-ocean/global_storm_surge_reconstruction/era-20C_surge_reconstruction");
var surge_era_interim = ee.FeatureCollection("projects/sat-io/open-datasets/open-ocean/global_storm_surge_reconstruction/era-Interim_surge_reconstruction");
var surge_merra_2 =  ee.FeatureCollection("projects/sat-io/open-datasets/open-ocean/global_storm_surge_reconstruction/merra-2_surge_reconstruction");
var surge_era_5 =  ee.FeatureCollection("projects/sat-io/open-datasets/open-ocean/global_storm_surge_reconstruction/era-5_surge_reconstruction");
```

Sample Code: https://code.earthengine.google.com/95f76e127f7afec9858b8f5dd3f86066

#### License

This work is licensed under the Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0). Users are free to use, copy, distribute, transmit, and adapt the work for commercial and non-commercial purposes, without restriction, as long as clear attribution of the source is provided.

Created by: Tadesse, M.G., Wahl, T.

Curated by: Samapriya Roy

Keywords: : 20-CR, ERA-20C, ERA-Interim, MERAA-2, ERA-Five, reanalysis, storm-surge, surge-reconstruction, NCEP, extreme-sea-level

Last updated: 2022-01-04
