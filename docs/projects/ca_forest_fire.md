# Canada Landsat Derived Wildfire disturbance & Magnitude 1985-2020

The annual forest change data included in this product is national in scope (entire forested ecosystem) and represents the wall-to-wall characterization of wildfire in Canada at a 30-m spatial resolution. The information outcomes represent 36 years of wildfire change over Canada’s forests, derived from a single, consistent, spatially explicit data source, derived in a fully automated manner. This demonstrated capacity to characterize forests at a resolution that captures human impacts is key to establishing a baseline for detailed monitoring of forested ecosystems from management and science perspectives. Time series of Landsat data were used to characterize national trends in stand replacing forest disturbances caused by wildfire and harvest for the period 1985–2020 for Canada's 650 Mha forested ecosystems.

Landsat data has a 30 m spatial resolution, so the change information is highly detailed and informative regarding both natural and human driven changes. These data represent annual stand replacing forest changes. The stand replacing disturbance types labeled are wildfire and harvest, with lower confidence wildfire and harvest, also shared. The distinction and sharing of lower class membership likelihoods is to indicate to users that some change events were more difficult to allocate to a change type, but are generally found to be in the correct category. For an overview on the data, image processing, and time series change detection methods applied, as well as information on independent accuracy assessment of the data, see ( Hermosilla et al. 2016). The data available is Change year for Wildfire Events. You can [download the dataset here](https://opendata.nfis.org/downloads/forest_change/CA_Forest_Fire_1985-2020.zip)

#### Canada Landsat-Derived Forest Wildfire Change Magnitude dNBR (1985-2020)
Wildfire change magnitude dNBR 1985-2020. Spectral change magnitude for wildfires that occurred from 1985 and 2020 expressed via differenced Normalized Burn Ratio (dNBR), computed as the variation between the spectral values before and after a given change event. This layer value has been transformed for data storage efficiency. The actual dNBR value can be calculated as follows dNBR = value / 100. Higher dNBR values are related to higher burn severity. You can [download the dataset here](https://opendata.nfis.org/downloads/forest_change/CA_Forest_Wildfire_dNBR_1985_2020.zip)


Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.


#### Dataset Citation

```
Hermosilla, T., Wulder, M.A., White, J.C., Coops, N.C., Hobart, G.W., Campbell, L.B., 2016. Mass data processing of time series Landsat imagery:
pixels to data products for forest monitoring. International Journal of Digital Earth 9(11), 1035-1054.
```

![ca_forest_harvest_small](https://user-images.githubusercontent.com/6677629/215292086-0b98bb65-e49a-479e-9fd4-4422d49e426e.gif)

#### Code Snippet

```js
var ca_forest_fire = ee.Image("projects/sat-io/open-datasets/CA_FOREST/CA_Forest_Fire_1985-2020");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/CA-FOREST-FIRE-1985-2020

```js
var ca_forest_fire_mag = ee.Image("projects/sat-io/open-datasets/CA_FOREST/CA_Forest_Wildfire_dNBR_1985_2020");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/CA-FOREST-FIRE-MAGNITUDE-1985-2020

#### License
This work is licensed under and freely available to the public Open Government Licence - Canada.

Created by: Hermosilla et al. 2016

Curated in GEE by : Spencer Bronson and Samapriya Roy

keywords: Forest Fire, Forest inventory, Land cover, Landsat, Machine learning

Last updated on GEE: 2023-07-02
