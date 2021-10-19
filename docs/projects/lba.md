# Landsat Burned Area
The Landsat Burned Area product is designed to identify burned areas across all ecosystems (e.g. forests, shrublands, and grasslands) for Landsat 4-8 data. The Landsat Burned Area product contains two acquisition-based raster data products that represent burn classification and burn probability. Landsat Burned Area is generated from U.S. Landsat Analysis Ready Data (ARD) Surface Reflectance and Top of Atmosphere Brightness Temperature data.

The Landsat Burned Area product is processed to 30-meter spatial resolution in Albers Equal Area (AEA) projection using the World Geodetic System 1984 (WGS84) datum and gridded to a common tiling scheme.

Product Page URL: https://www.usgs.gov/core-science-systems/nli/landsat/landsat-burned-area
Product Guide URL: https://www.usgs.gov/media/files/landsat-burned-area-product-guide

Resolution: 30m

DOI: ​​​​​​​Landsat Level-3 Burned Area (BA) Science Product Digital Object Identifier (DOI) number: 10.5066/F77W6BDJ

#### Citation

```
Landsat Level 3 Burned Area  Science Product courtesy of the U.S. Geological Survey.

Hawbaker, T.J., Vanderhoof, M.K., Schmidt, G.L., Beal, Y.-J., Picotte, J.J., Takacs, J.D., Falgout, J.T., Dwyer, J.L., 2020. The Landsat Burned
Area algorithm and products for the United States. Remote Sensing of the Environment 244. https://doi.org/10.1016/j.rse.2020.111801

Hawbaker, T.J., Vanderhoof, M.K., Beal, Y.-J., Takacs, J.D., Schmidt, G.L., Falgout, J.T., Williams, B., Brunner, N.M., Caldwell, M.K., Picotte,
J.J., Howard, S.M., Stitt, S., Dwyer, J.L., 2017a. Landsat Burned Area Essential Climate Variable products for the conterminous United States
(1984 -2015). U.S. Geological Survey Data Release. https://doi.org/10.5066/F73B5X76

Hawbaker, T.J., Vanderhoof, M.K., Beal, Y.-J., Takacs, J.D., Schmidt, G.L., Falgout, J.T., Williams, B., Fairaux, N.M., Caldwell, M.K., Picotte,
J.J., Howard, S.M., Stitt, S., Dwyer, J.L., 2017b. Mapping burned areas using dense time-series of Landsat data. Remote Sensing of Environment
198, 504–522. https://doi.org/10.1016/j.rse.2017.06.027
```

<img width="922" alt="Screenshot 2021-10-19 at 12 59 12" src="https://user-images.githubusercontent.com/45358635/137981754-af14d472-f26c-41a8-88e1-7971fb2775b2.png">

#### Earth Engine Snippet

```js

var burn_probability = ee.Image("users/keikonomura/fire/LBA_CU_2019_20200415_C01_V01_BP_L8")

```

Sample Code: https://code.earthengine.google.com/34a2a4df430c5e7c8a6e5073cd66175c


#### Required
License Information: There are no restrictions on the use of Landsat Level-3 Science Products. It is not a requirement of data use, but the above citations may be used in publication or presentation materials to acknowledge the USGS as a data source and to credit the original research.

Curated by: Keiko Nomura

Keywords: Wildfire, Burned Area, Burn Probability, Burned Classification, Landsat

Last updated: 2021-10-19
