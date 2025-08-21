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

| Asset Name | Description | Band | Units |
|------------|-------------|------|--------|
| `pop` | Annual population estimates (2015-2030) | `population` | Number of people per grid cell |

The dataset includes:
- **Total Population**: Overall population counts per grid cell

#### Citation

```
WorldPop (www.worldpop.org - School of Geography and Environmental Science, University of Southampton; Department of Geography and Geosciences, University of Louisville; Departement de Geographie, Universite de Namur) and Center for International Earth Science Information Network (CIESIN), Columbia University (2018). Global High Resolution Population Denominators Project - Funded by The Bill and Melinda Gates Foundation (OPP1134076).
```

#### Dataset Citation

```
Bondarenko M., Priyatikanto R., Tejedor-Garavito N., Zhang W., McKeen T., Cunningham A., Woods T., Hilton J., Cihan D., Nosatiuk B., Brinkhoff T., Tatem A., Sorichetta A.. 2025 Constrained estimates of 2015-2030 total number of people per grid square at a resolution of 3 arc (approximately 100m at the equator) R2024B version v1. Global Demographic Data Project - Funded by The Bill and Melinda Gates Foundation (INV-045237). WorldPop - School of Geography and Environmental Science, University of Southampton. DOI:10.5258/SOTON/WP00803
```

![worldpop](../images/worldpop.png)

#### Earth Engine Snippet

```javascript
var worldpop = ee.ImageCollection("projects/sat-io/open-datasets/WORLDPOP/pop");
```

Sample Code:  https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/WORLDPOP-2015_2030

#### License

This work is licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0).

Provided by: WorldPop, University of Southampton

Keywords: Population mapping, Demographics, Settlement patterns, Dasymetric mapping, Random Forest, Gridded population, Census data, Population projections, Human geography, Spatial analysis

Curated in GEE by: Samapriya Roy

Last updated: 2025-08-20
