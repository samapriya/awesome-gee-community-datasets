# High Res Extended Spring Indices database

The Extended Spring Indices (SI-x) provide a comprehensive dataset for studying the timing of spring onset and its relationship to climate change.
These models, derived from daily minimum and maximum temperatures, track the first leaf and first bloom events for key plant species. By
transforming temperature data into consistent indices, the SI-x enable the calculation of the frost damage index. This dataset offers a
multi-decadal, high-resolution (1 km) analysis of spring phenology across North America (1980-2022) and Europe (1950-2020).

At the present, the 1 km SI-x products are available over two study areas

* North and Central America (located between 14°02'31.3"N and 55°37'04.1"N latitude and 56°05'50.7"W 126°22'06.1"W longitude). [Daymet version 4](https://daymet.ornl.gov/) from 1980 to 2022, was used to generate this dataset. The daily maximunim and minimum temperature and daylength are available in GEE. These SI-x products are an updated version of those presented in [Izquierdo-Verdiguier et al](https://www.sciencedirect.com/science/article/pii/S0168192318302193?via%3Dihub).

* Europe (located between 35°55'48.7"N and 73°32'47.1"N latitude and  10°36'29.5"W and 44°50'29.5"E longitude). The daily maximum and minimum temperature come from the [Downscaled version of European Observations (E-OBS)](https://rmets.onlinelibrary.wiley.com/doi/10.1002/joc.4436) version 3 from 1950 to 2020, which is available for download [here](ftp://palantir.boku.ac.at/Public/ClimateData). The daylength is calculated (modelled) once the data are ingested in GEE (ingested because this data is not directly available in GEE).

#### Citation

```
Izquierdo-Verdiguier, Emma, Raúl Zurita-Milla, Toby R. Ault, and Mark D. Schwartz. "Development and analysis of spring plant phenology products: 36
years of 1-km grids over the conterminous US." Agricultural and forest meteorology 262 (2018): 34-41.
```

| First Leaf Index over Contiguous US | First Leaf Index over Europe |
|:-----------------------------------:|:-----------------------------:|
| ![America](https://github.com/user-attachments/assets/44dcc525-b815-4a64-a210-7b0bbcc11d67) | ![Europe](https://github.com/user-attachments/assets/bfb851d6-9737-4262-9117-1d1aa91e5e4c) |

#### Earth Engine Snippet

```js
// Define Image Collections
var bloomDaymet = 'projects/sat-io/open-datasets/SIx_products/BloomDaymetv4';
var bloomEurope = 'projects/sat-io/open-datasets/SIx_products/BloomEuropev3';
var diDaymet = 'projects/sat-io/open-datasets/SIx_products/DI_Daymetv4';
var diEurope = 'projects/sat-io/open-datasets/SIx_products/DI_Europev3';
var leafDaymet = 'projects/sat-io/open-datasets/SIx_products/LeafDaymetv4';
var leafEurope = 'projects/sat-io/open-datasets/SIx_products/LeafEuropev3';
```

Sample Script:  https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:analysis-ready-data/EXTENDED-SPRING-INDICES

Earth Engine App: https://emma.users.earthengine.app/view/spring-onset

#### License
This work is licensed under a CC BY-NC 4.0 license.

Created by: Izquierdo-Verdiguier. 2024

Curated in GEE by : Samapriya Roy

Keyworks: spring onset, phenology, climate change

Last updated in GEE: 2024-08-29
