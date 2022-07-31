# HydroWASTE v1.0

HydroWASTE is a spatially explicit global database of 58,502 wastewater treatment plants (WWTPs) and their characteristics. This database was developed by combining national and regional datasets with auxiliary information to derive or complete missing characteristics, including the amount of people served, the flow rate of effluents, and the level of treatment of processed wastewater. The HydroSHEDS river network with streamflow estimates was used to geo-reference plant outfall locations and to assess the distribution of wastewaters at a global scale. All wastewater treatment plants are co-registered to the global river network of the HydroRIVERS database via their estimated outfall locations. You can find the [datsets page here](https://www.hydrosheds.org/products/hydrowaste)

For more information on HydroATLAS please refer to [hydrosheds page on hydroatlas](https://www.hydrosheds.org/hydroatlas) and technical information is [included in the paper](https://doi.org/10.5194/essd-14-559-2022)

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Citations

The development of BasinATLAS and RiverATLAS is fully described in Linke et al. (2019) and should be cited as:

```
Ehalt Macedo, H., Lehner, B., Nicell, J., Grill, G., Li, J., Limtong, A., Shakya, R. (2022). Distribution and characteristics of wastewater
treatment plants within the global river network. Earth System Science Data, 14(2): 559–577. https://doi.org/10.5194/essd-14-559-2022
```

![hydrowaste](https://user-images.githubusercontent.com/6677629/182042705-1f70fda1-9be4-49b9-89b9-ec04a16a56c2.gif)

#### Earth Engine Snippet

```js
var hydrowaste = ee.FeatureCollection("projects/sat-io/open-datasets/HydroWaste/HydroWASTE_v10");
```

Sample Code: https://code.earthengine.google.com/761bd1c4fc4ad6c91286b035ef4d1a0b


#### License
The data is licensed under a Creative Commons Attribution 4.0 International License (see section 4). By downloading and using the data the user agrees to the terms and conditions of this license.

Created by: Ehalt Macedo, H., Lehner, B., Nicell, J., Grill, G., Li, J., Limtong, A., Shakya, R.

Curated in GEE by: Samapriya Roy

Keywords: water,hydrology, rivers, discharge, depth, volume, area, hydrowaste, wastewater

Last updated: 2022-07-09
