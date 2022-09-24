# Global crop production tillage practices

No tillage (NT) is often presented as a means to grow crops with positive environmental externalities, such as enhanced carbon sequestration, improved soil quality, reduced soil erosion, and increased biodiversity. However, whether NT systems are as productive as those relying on conventional tillage (CT) is a controversial issue, fraught by a high variability over time and space. Here, we expand existing datasets to include the results of the most recent field experiments, and we produce a global dataset comparing the crop yields obtained under CT and NT systems. In addition to crop yield, our dataset also reports information on crop growing season, management practices, soil characteristics and key climate parameters throughout the experimental year. The final dataset contains 4403 paired yield observations between 1980 and 2017 for eight major staple crops in 50 countries. This dataset can help to gain insight into the main drivers explaining the variability of the productivity of NT and the consequence of its adoption on crop yields.


#### Data Citation

```
Su, Y., Gabrielle, B. & Makowski, D. A global dataset for crop production under conventional tillage and no tillage systems. figshare https://doi.org/10.6084/m9.figshare.12155553 (2020). v14
```

#### Paper Citation

```
Su, Y., Gabrielle, B. & Makowski, D. A global dataset for crop production under conventional tillage and no tillage systems. Scientific Data 8, 33 (2021).
```

![tillage](https://user-images.githubusercontent.com/6677629/131391652-b7319de6-ab6c-4a2b-851b-0bc23c3af547.gif)

#### Earth Engine Snippet

```js
var tillage = ee.FeatureCollection("projects/sat-io/open-datasets/global_tillage_production");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/GLOBAL-CROP-PRODUCTION-TILLAGE-PRACTICES

#### Property Mapping

|Property                                                             |GEE property    |
|---------------------------------------------------------------------|----------------|
|Author                                                               |author          |
|Journal                                                              |journal         |
|Year                                                                 |year            |
|Site country                                                         |site_country    |
|Location                                                             |location        |
|Latitude                                                             |latitude        |
|Longitude                                                            |longitude       |
|Soil information recorded in the paper                               |soil_from_paper |
|pH (surface layer)                                                   |pH_surface_layer|
|Replications in experiment                                           |replications_exp|
|Crop                                                                 |crop            |
|Initial year of NT practice ( or first year of experiment if missing)|init_yr_nt      |
|Sowing year                                                          |sowing_year     |
|Harvest year                                                         |harvest_year    |
|Years since NT started (yrs)                                         |yrs_from_nt     |
|Crop growing season recorded in the paper                            |cgsp            |
|Crop rotation with at least 3 crops involved in CT                   |crit            |
|Crop rotation with at least 3 crops involved in NT                   |crint           |
|Crop sequence (details)                                              |c_seq           |
|Cover crop before sowing                                             |cc_bf_sowing    |
|Soil cover in CT                                                     |soil_cover_ct   |
|Soil cover in NT                                                     |soil_cover_nt   |
|Residue management of previous crop in CT  (details)                 |rm_ct           |
|Residue management of previous crop in NT (details)                  |rm_nt           |
|Weed and pest control CT                                             |wp_ct           |
|Weed and pest control NT                                             |wp_nt           |
|Weed and pest control CT (details)                                   |wpc_ct          |
|Weed and pest control NT  (details)                                  |wpc_nt          |
|Fertilization CT                                                     |ft_ct           |
|Fertilization NT                                                     |ft_nt           |
|N input                                                              |n_inp           |
|N input rates with the unit kg N ha-1 (details)                      |n_inp_unit      |
|Field fertilization (details)                                        |fft             |
|Irrigation CT                                                        |i_ct            |
|Irrigation NT                                                        |i_nt            |
|Water applied in CT                                                  |w_ct            |
|Water applied in NT                                                  |w_nt            |
|Other information                                                    |other           |
|Yield of CT                                                          |yield_ct        |
|Yield of NT                                                          |yield_nt        |
|Relative yield change                                                |rel_yl_chg      |
|Yield increase with NT                                               |yl_inc_nt       |
|Outlier of CT                                                        |outlier_ct      |
|Outlier of NT                                                        |outlier_nt      |
|Sowing month                                                         |sw_month        |
|Harvesting month                                                     |hv_month        |
|P                                                                    |P               |
|E                                                                    |E               |
|PB                                                                   |PB              |
|Tave                                                                 |Tave            |
|Tmax                                                                 |Tmax            |
|Tmin                                                                 |Tmin            |
|ST                                                                   |ST              |

#### License

This work is licensed under the Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0). Users are free to use, copy, distribute, transmit, and adapt the work for commercial and non-commercial purposes, without restriction, as long as clear attribution of the source is provided.

Created by: Yang Su et al.

Curated by: Samapriya Roy

Keywords:  Conservation agriculture, Conventional tillage, crop yield, No tillage, No-till

Last updated: 2021-08-30
