# Urban Heat Island Intensity (UHII)

The Urban Heat Island (UHI) effect, characterized by localized warming over urban areas, is a critical consequence of urbanization on climate.
Traditional methods of estimating UHI intensity (UHII) have been constrained by limitations, such as focusing solely on clear-sky surface UHII and
neglecting all-sky surface and canopy (air temperature) UHII. These approaches often overlook anthropogenic disturbances, leading to uncertainties in the estimates. To overcome these challenges, this study introduces a new dynamic equal-area (DEA) method designed to reduce the impact of confounding factors through a dynamic cyclic process. By applying the DEA method and integrating gridded temperature data, a comprehensive global-scale UHII dataset has been developed, covering over 10,000 cities and spanning more than 20 years with monthly temporal resolution. This dataset offers multi-faceted UHII estimates, including clear-sky surface, all-sky surface, and canopy UHII, providing a robust foundation for analyzing UHI trends in urban environments.

The dataset reveals that UHII is greater than zero in more than 80% of the studied cities, with global annual average magnitudes around 1.0°C (day) and 0.8°C (night) for surface UHII, and approximately 0.5°C for canopy UHII. Moreover, an interannual upward trend in UHII is observed in over 60% of cities, with global average trends exceeding 0.1°C per decade (day) and 0.06°C per decade (night) for surface UHII, and slightly over 0.03°C per decade for canopy UHII. A positive correlation is also identified between the magnitude and trend of UHII, indicating that cities with stronger UHII tend to experience faster growth in UHII over time. The dataset further highlights discrepancies in UHII estimates based on differences in data types (surface or air temperature), data acquisition times (Terra or Aqua), weather conditions (clear-sky or all-sky), and processing methodologies. This comprehensive dataset and the accompanying analysis offer valuable insights for future urban climate studies and are publicly accessible at [https://doi.org/10.6084/m9.figshare.24821538](https://doi.org/10.6084/m9.figshare.24821538). A global dataset of urban heat island using multiple methods and including estimates for both air temperature and land surface temperature. It is available monthly from 2003 to 2020 (from 2001 for the dataset from MODIS Terra satellite). You can read more information [in the paper here](https://www.sciencedirect.com/science/article/pii/S0034425724003614?dgcid=coauthor)

<div class="result" markdown>

???+ note

    **The "Diurnal" field can be either "Day" or "Nig", signifying daytime and nighttime UHII, respectively. "Year” denotes the UHII year, and "Month” indicates the specific       month. It’s important to note that, besides monthly UHII results, we also provide quarterly and annual averages. When “Month” takes values from 1 to 12, it signifies         the monthly average. If “Month” is between 21 and 24, it indicates the quarterly average (21 for March-May, 22 for June-August, 23 for September-November, and 24 for         December-February). When “Month” is 30, it denotes the annual average. The UHII value can be converted to degrees Celsius by multiplying a scaling factor of 0.01.**

</div>




#### Dataset Details

| Indicator                                         | Data Source                             | Period     | Description                                                                                                                                                       |
|---------------------------------------------------|-----------------------------------------|------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Surface UHI intensity estimated by the clear-sky LST data | IMod1 (MOD11A1)                         | 2001-2021  | Clear-sky surface UHI from the MODIS Terra daily LST (A1) and 8-day LST (A2) products; both corresponding to an equatorial overpass time of 10:30 am local time during daytime and 10:30 pm at night |
| IMod2 (MOD11A2)                                   |                                         |            |                                                                                                                                                                   |
| IMyd1 (MYD11A1)                                   | 2003-2021                               | Clear-sky surface UHI from the MODIS Aqua daily LST (A1) and 8-day LST (A2) products; both corresponding to an equatorial overpass time of 1:30 pm local time during daytime and 1:30 am at night |
| IMyd2 (MYD11A2)                                   |                                         |            |                                                                                                                                                                   |
| Surface UHI intensity estimated by the seamless clear-sky LST data | ISMod2 (Seamless MOD11A2)                | 2001-2020  | Clear-sky surface UHI based on the seamless LST product [DOI](https://doi.org/10.1016/j.rse.2022.113422)                                                          |
| ISMyd1 (Seamless MYD11A1)                         | 2003-2020                               | Clear-sky surface UHI based on a second seamless LST product [DOI](https://doi.org/10.5194/essd-14-651-2022)                                                      |
| Surface UHI intensity estimated by the seamless all-sky LST data | IAMod2 (All-sky MOD11A2)                  | 2001-2020  | All-sky surface UHI based on the seamless all-sky LST product [DOI](https://doi.org/10.1016/j.rse.2022.113422)                                                    |
| Canopy UHI intensity estimated by the surface air temperature data | ISAT (Surface air temperature)            | 2001-2020  | Air temperature or canopy UHI based on the global surface air temperature product [DOI](https://doi.org/10.1016/j.rse.2022.113422)                                |

#### Citation

```
Yang, Qiquan, Yi Xu, T. C. Chakraborty, Meng Du, Ting Hu, Ling Zhang, Yue Liu et al. "A global urban heat island intensity dataset: Generation,
comparison, and analysis." Remote Sensing of Environment 312 (2024): 114343.
```

#### Dataset Citation

```
Qiquan Yang.Global Urban Heat Island Intensity Dataset. Figshare. https://doi.org/10.6084/m9.figshare.24821538, 2024.
```

![uhii_animation](https://github.com/user-attachments/assets/901ce1e8-7e6a-445b-8d07-ad3248eae773)

#### Earth Engine Snippet

```js
var AMOD2 = ee.ImageCollection('projects/sat-io/open-datasets/UHII/AMOD2');
var MOD1 = ee.ImageCollection('projects/sat-io/open-datasets/UHII/MOD1');
var MOD2 = ee.ImageCollection('projects/sat-io/open-datasets/UHII/MOD2');
var MYD1 = ee.ImageCollection('projects/sat-io/open-datasets/UHII/MYD1');
var MYD2 = ee.ImageCollection('projects/sat-io/open-datasets/UHII/MYD2');
var SAT = ee.ImageCollection('projects/sat-io/open-datasets/UHII/SAT');
var SMOD2 = ee.ImageCollection('projects/sat-io/open-datasets/UHII/SMOD2');
var SMYD1 = ee.ImageCollection('projects/sat-io/open-datasets/UHII/SMYD1');
```
Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:/weather-climate/URBAN-HEAT-ISLAND-INTENSITY

#### License
The datasets are provided under a Attribution 4.0 International (CC BY 4.0) license.

Provided by: Yang et al 2024

Curated in GEE by : Samapriya Roy

Keywords: urban, heat, climate, city

Last updated: 2024-09-06

#### Changelog
- Added extra properties for filtering and sorting
- Updated collections to include missing data
