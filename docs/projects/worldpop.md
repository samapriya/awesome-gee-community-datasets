# WorldPop Global Population Data 2015-2030

WorldPop's Global 2015-2030 gridded demographic datasets provide high-resolution population estimates using a 'top-down' methodology that disaggregates administrative unit population counts to 100m grid cells. This dataset represents a significant improvement over previous global population datasets, incorporating the latest circa-2020 round of censuses, updated geospatial covariates, improved settlement mapping, and building footprints derived from satellite imagery using AI approaches. The dataset provides annual population estimates at 100m resolution for 242 countries globally, covering the period 2015-2030. The methodology employs a Random Forest (RF) dasymetric approach to spatially disaggregate population counts from administrative boundaries to grid cells, using machine learning models trained on comprehensive geospatial covariates including settlement data, environmental variables, and infrastructure features.

The population data were collected from the two most recent census rounds (circa 2010 and 2020), supplemented with UN Common Operational Datasets, US Census Bureau projections, and official estimates where census data were unavailable. Various demographic methods were applied to interpolate age and sex-disaggregated totals between years and project to 2030, with national totals aligned to the UN World Population Prospects 2024 estimates. You can download the datasets from [Humanitarian Data Exchange (HDX)](https://data.humdata.org/organization/worldpop)

#### Constrained vs Unconstrained Models

WorldPop employs two main modeling approaches but only the constrained datasets are added here:

**Constrained Models**: Population estimates are limited to areas identified as human settlements, using built settlement layers derived from satellite imagery. This approach assumes people only reside in areas with buildings or infrastructure, providing more realistic population distributions by excluding uninhabitable areas like water bodies, protected areas, or steep terrain.

**Unconstrained Models**: Population can be allocated to any land area within administrative boundaries, regardless of settlement presence. While this may result in population being assigned to uninhabitable areas, it can be useful for applications where the exact settlement boundaries are uncertain or where temporary populations might exist outside formal settlements.

#### Dataset Characteristics

<center>

| Parameter | Value |
|-----------|-------|
| Spatial Resolution | 100m × 100m |
| Temporal Coverage | 2015-2030 (annual) |
| Geographic Coverage | 242 countries globally |
| Coordinate System | Geographic (WGS84) |
| Data Format | GeoTIFF |
| Population Type | Residential population |
| Age Groups | 0-1, 5-year classes up to 90+ |
| Sex Disaggregation | Male, Female, Total |
| Methodology | Random Forest dasymetric mapping |

</center>

#### Available Data

The **WorldPop** collection provides population estimates at 100m resolution with the following characteristics:

**Total Population Dataset**

| Asset Name | Description | Band | Units |
|------------|-------------|------|--------|
| `pop` | Annual population estimates (2015-2030) | `population` | Number of people per grid cell |

**Age-Sex Disaggregated Dataset**


??? example "Expand to show the age-sex dataset provides population estimates broken down by gender and age groupings at 100m resolution"
        | Band Name | Description |
        |-----------|-------------|
        | `f_00`/`m_00` | Female/male population under 1 year old |
        | `f_01`/`m_01` | Female/male population aged 1-4 years |
        | `f_05`/`m_05` | Female/male population aged 5-9 years |
        | `f_10`/`m_10` | Female/male population aged 10-14 years |
        | `f_15`/`m_15` | Female/male population aged 15-19 years |
        | `f_20`/`m_20` | Female/male population aged 20-24 years |
        | `f_25`/`m_25` | Female/male population aged 25-29 years |
        | `f_30`/`m_30` | Female/male population aged 30-34 years |
        | `f_35`/`m_35` | Female/male population aged 35-39 years |
        | `f_40`/`m_40` | Female/male population aged 40-44 years |
        | `f_45`/`m_45` | Female/male population aged 45-49 years |
        | `f_50`/`m_50` | Female/male population aged 50-54 years |
        | `f_55`/`m_55` | Female/male population aged 55-59 years |
        | `f_60`/`m_60` | Female/male population aged 60-64 years |
        | `f_65`/`m_65` | Female/male population aged 65-69 years |
        | `f_70`/`m_70` | Female/male population aged 70-74 years |
        | `f_75`/`m_75` | Female/male population aged 75-79 years |
        | `f_80`/`m_80` | Female/male population aged 80-84 years |
        | `f_85`/`m_85` | Female/male population aged 85-89 years |
        | `f_90`/`m_90` | Female/male population aged 90 years and over |

#### Citation

```
WorldPop (www.worldpop.org - School of Geography and Environmental Science, University of Southampton; Department of Geography and Geosciences, University of Louisville; Departement de Geographie, Universite de Namur) and Center for International Earth Science Information Network (CIESIN), Columbia University (2018). Global High Resolution Population Denominators Project - Funded by The Bill and Melinda Gates Foundation (OPP1134076).
```

#### Dataset Citations

**Total Population Dataset:**
```
Bondarenko M., Priyatikanto R., Tejedor-Garavito N., Zhang W., McKeen T., Cunningham A., Woods T., Hilton J., Cihan D., Nosatiuk B., Brinkhoff T., Tatem A., Sorichetta A.. 2025 Constrained estimates of 2015- 2030 total number of people per grid square at a resolution of 3 arc (approximately 100m at the equator) R2024B version v1. Global Demographic Data Project - Funded by The Bill and Melinda Gates Foundation (INV-045237). WorldPop - School of Geography and Environmental Science, University of Southampton. DOI:10.5258/SOTON/WP00803
```

**Age-Sex Dataset:**
```
Bondarenko M., Priyatikanto R., Tejedor-Garavito N., Zhang W., McKeen T., Cunningham A., Woods T., Hilton J., Cihan D., Nosatiuk B., Brinkhoff T., Tatem A., Sorichetta A.. 2025. The spatial distribution of population broken down by gender and age groupings in 2015-2030 at a resolution of 3 arc (approximately 100m at the equator) R2025A version v1. Global Demographic Data Project - Funded by The Bill and Melinda Gates Foundation (INV-045237). WorldPop - School of Geography and Environmental Science, University of Southampton.
```

![worldpop](../images/worldpop.gif)

#### Earth Engine Snippet

**Total Population:**
```javascript
var worldpop = ee.ImageCollection("projects/sat-io/open-datasets/WORLDPOP/pop");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/WORLDPOP-2015_2030

**Age-Sex Dataset:**
```javascript
var ageSex = ee.ImageCollection("projects/sat-io/open-datasets/WORLDPOP/agesex");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/WORLDPOP-AGESEX

#### License

This work is licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0).

#### Changelog

**2026-02-03** Added Age-Sex 100m dataset to the WorldPop collections

Provided by: WorldPop, University of Southampton

Keywords: Population mapping, Demographics, Settlement patterns, Dasymetric mapping, Random Forest, Gridded population, Census data, Population projections, Human geography, Spatial analysis

Curated in GEE by: Samapriya Roy and Rhorom Priyatikanto

Last updated: 2026-02-02
