# Gridded Global GDP per capita (1990-2022)

Gross Domestic Product (GDP) measures the monetary value of final goods and services produced in a given area during a specific period. This dataset provides a comprehensive gridded GDP per capita dataset downscaled to multiple administrative levels covering 1990–2022, representing a substantial update to existing datasets which only used reported subnational data up to 2010.

The dataset employs novel methods for extrapolation and downscaling, including machine learning algorithms that showed high performance (R²=0.79 for cross-validation, R²=0.80 for test dataset) and accuracy against reported datasets (Pearson R=0.88). The dataset includes reported and downscaled annual data for three administrative levels and provides higher spatial resolution and wider temporal range than existing datasets.

#### Key Updates from Previous Version

- **Extended temporal coverage**: 1990-2022 (vs. previous 1990-2015)
- **More comprehensive subnational data**: Admin 1 level data for 89 countries (2,708 subnational units) vs. previous 83 countries (1,549 units)
- **Finer spatial resolution**: Now includes admin 2 level (municipality) data for 43,501 administrative units
- **Improved methodologies**: Novel extrapolation methods and machine learning-based downscaling
- **Enhanced validation**: Validated against OECD regional data with high accuracy (R=0.88)

#### Dataset Components

|Dataset|Administrative Level|Temporal Coverage|Resolution|Note|
|-------|-------------------|-----------------|----------|-----|
|GDP per capita (PPP) - Admin 0|National (237 countries)|1990-2022|5 arc-min|Reported national data from World Bank, IMF, CIA|
|GDP per capita (PPP) - Admin 1|Provincial (2,708 units, 89 countries)|1990-2022|5 arc-min|Reported subnational data from OECD, Eurostat, national censuses|
|GDP per capita (PPP) - Admin 2|Municipal (43,501 units)|1990-2022|5 arc-min, 30 arc-min|Downscaled using machine learning algorithms|
|Total GDP (PPP)|All levels|1990-2022|30 arc-sec, 5 arc-min, 30 arc-min|GDP per capita multiplied by gridded population data|

#### Methodology Highlights

- **Gap-filling**: Novel extrapolation method using linear regression with geographically closest countries with similar economic patterns
- **Downscaling**: Machine learning approach using ensemble trees with independent variables including urbanization level, travel time to cities, income inequality, and national GDP
- **Data harmonization**: Ratio-based approach ensuring consistency between administrative levels and alignment with national statistics
- **Validation**: Cross-validated against OECD subnational data and harmonized with national reported data

#### Dataset notes

* Units for GDP: US dollar (2017 international USD, PPP-adjusted)
* All administrative levels are gap-filled and harmonized with national statistics
* Machine learning downscaling achieved R²=0.80 on test dataset
* Data harmonization ensures subnational totals match national reported values

#### Band Structure
- Each administrative level dataset contains 33 bands (1990-2022)
- Band names follow format: "PPP_YYYY" where YYYY is the year
- Total GDP datasets have varying temporal coverage based on resolution:
  - 30 arc-sec: 1990-2020 (every 5 years)
  - 5 arc-min: 1990-2022 (annual)
  - 30 arc-min: 1990-2022 (annual)

#### Data Quality and Limitations
- Admin 2 level data are model predictions with validation R²=0.80
- Accuracy varies by region: highest in Europe/North America, lower in Central Asia/Latin America
- African continent has limited subnational data availability
- Small island states may have interpolated values where data unavailable

#### Paper citation

```
Kummu, M., Kosonen, M. & Masoumzadeh Sayyar, S. Downscaled gridded global dataset for gross domestic product (GDP) per capita PPP over 1990–2022.
Sci Data 12, 178 (2025). https://doi.org/10.1038/s41597-025-04487-x
```

#### Dataset citation

```
Kummu, M., Kosonen, M., & Masoumzadeh Sayyar, S. (2025). Data for: Downscaled gridded global dataset for Gross Domestic Product (GDP) per capita at purchasing power parity (PPP)
over 1990-2022 [Data set]. Zenodo. https://doi.org/10.5281/zenodo.16741980
```

![gdp_hdi](https://user-images.githubusercontent.com/6677629/168412311-8e1de844-298e-4c4f-8ffc-2ce38963f70c.gif)

#### Earth Engine Snippet

```js
// GDP per capita datasets by administrative level
var gdp_adm0 = ee.Image("projects/sat-io/open-datasets/GRIDDED_HDI_GDP/adm0_gdp_perCapita_1990_2022");
var gdp_adm1 = ee.Image("projects/sat-io/open-datasets/GRIDDED_HDI_GDP/adm1_gdp_perCapita_1990_2022");
var gdp_adm2 = ee.Image("projects/sat-io/open-datasets/GRIDDED_HDI_GDP/adm2_gdp_perCapita_1990_2022");
var gdp_adm2_30arcmin = ee.Image("projects/sat-io/open-datasets/GRIDDED_HDI_GDP/adm2_gdp_perCapita_1990_2022_30arcmin");

// Total GDP datasets by resolution
var gdp_total_30arcsec = ee.Image("projects/sat-io/open-datasets/GRIDDED_HDI_GDP/total_gdp_perCapita_1990_2020_30arcsec");
var gdp_total_5arcmin = ee.Image("projects/sat-io/open-datasets/GRIDDED_HDI_GDP/total_gdp_perCapita_1990_2022_5arcmin");
var gdp_total_30arcmin = ee.Image("projects/sat-io/open-datasets/GRIDDED_HDI_GDP/total_gdp_perCapita_1990_2022_30arcmin");

//Feature Collections
var gdp_adm0_poly = ee.FeatureCollection("projects/sat-io/open-datasets/GRIDDED_HDI_GDP/poly_adm0_gdp_perCapita_1990_2022");
var gdp_adm1_poly = ee.FeatureCollection("projects/sat-io/open-datasets/GRIDDED_HDI_GDP/poly_adm1_gdp_perCapita_1990_2022");
var gdp_adm2_poly = ee.FeatureCollection("projects/sat-io/open-datasets/GRIDDED_HDI_GDP/poly_adm2_gdp_perCapita_1990_2022");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/GLOBAL-GDP-HDI

#### License
This work is licensed under a Creative Commons Attribution 4.0 International License.

Created by: Kummu, M., Kosonen, M. & Masoumzadeh Sayyar, S

Curated in GEE by: Samapriya Roy

Keywords: Development indicator, global spatial data, gridded data, Gross Domestic Product (GDP), Purchasing Power Parity (PPP), machine learning downscaling, administrative boundaries

Last updated on GEE: 2025-09-07

### Changelog

#### Version 3.0 (2025)
- **NEW**: Extended temporal coverage from 1990-2022 (vs. previous 1990-2015)
- **NEW**: Added admin 2 level (municipal) GDP per capita data for 43,501 units
- **IMPROVED**: Enhanced subnational data coverage: 89 countries (2,708 units) vs. previous 83 countries (1,549 units)
- **NEW**: Machine learning-based downscaling methodology with validation R²=0.80
- **NEW**: Multiple resolution total GDP products (30 arc-sec, 5 arc-min, 30 arc-min)
- **IMPROVED**: Novel gap-filling methodology using geographic proximity and economic similarity
- **NEW**: Comprehensive validation against OECD regional data (Pearson R=0.88)
- **UPDATED**: License changed from CC0 to Creative Commons Attribution 4.0 International
- **UPDATED**: New Zenodo DOI and 2025 Scientific Data publication

#### Version 2.0 (2018)
- Original gridded GDP and HDI dataset (1990-2015)
- Admin 0 and Admin 1 level GDP per capita data
- Regional trend-based extrapolation methodology
- HDI dataset included
