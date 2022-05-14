# Gridded Global GDP and HDI (1990-2015)

Two global key indicators of development are Gross Domestic Product (GDP) and Human Development Index (HDI). While ‘GDP measures the monetary value of final goods and services—that is, those that are bought by the final user—produced in a [given area] in a given period of time, HDI is a composite index of ‘average achievement in key dimensions of human development:

* a long and healthy life,
* being knowledgeable and
* have a decent standard of living’30.

Gap-filled multiannual datasets in gridded form for Gross Domestic Product (GDP) and Human Development Index (HDI). To provide a consistent product over time and space, the sub-national data were only used indirectly, scaling the reported national value and thus, remaining representative of the official statistics. This resulted in annual gridded datasets for GDP per capita (PPP), total GDP (PPP), and HDI, for the whole world at 5 arc-min resolution for the 25-year period of 1990–2015. Additionally, total GDP (PPP) is provided with 30 arc-sec resolution for three time steps (1990, 2000, 2015).

Disclaimer: Whole or parts of the dataset description was provided by the author(s) or their works.

|Dataset             |Dimensions   |Note                                                                                                                                  |
|--------------------|-------------|--------------------------------------------------------------------------------------------------------------------------------------|
|GDP per capita (PPP)|Timesteps: 26|Gridded GDP per capita, derived from a combination of sub-national and national datasets                                              |
|GDP (PPP)-5 arc-min |Timesteps: 26|Total GDP (PPP) of each grid cell, derived from GDP per capita (PPP) which is multiplied by gridded population data HYDE 3.2          |
|GDP (PPP)-30 arc-sec|Timesteps: 3 |Total GDP (PPP) of each grid cell, derived from GDP per capita (PPP) which is multiplied by gridded population data GHS               |
|Pedigree of GDP data|Timesteps: 26|Reports the scale (national, sub-national) and type (reported, interpolated, extrapolated) of each year of data                       |
|HDI                 |Timesteps: 26|Gridded HDI, derived from a combination of sub-national and national datasets                                                         |
|Pedigree of HDI data|Timesteps: 26|Reports the level (national, sub-national) and type (reported, interpolated, extrapolated) of each year of data                       |
|Administrative units|Products: 2  |Represents the administrative units used for GDP per capita (PPP) and HDI. National admin units have id 1–999, sub-national ones 1001-|

#### Dataset notes

* Units for GDP is US dollar

* Pedigree GDP:  Pedigree index numbers, coded as follows: 1-regional reported; 2-regional interpolated; 3-regional extrapolated; 5-national reported; 6-national interpolated; 7-national extrapolated

* Pedigree HDI: Pedigree index numbers, coded as follows: 1-regional reported; 2-regional scaled; 4-national reported; 5-national interpolated; 6-national extrapolated; 7-no data, regional average used

#### Paper citation

```
Kummu, M., Taka, M. & Guillaume, J. Gridded global datasets for Gross Domestic Product and Human Development Index over 1990–2015. Sci Data 5, 180004 (2018).
https://doi.org/10.1038/sdata.2018.4
```


#### Dataset citation

```
Kummu, Matti; Taka, Maija; Guillaume, Joseph H. A. (2020), Data from: Gridded global datasets for Gross Domestic Product and Human Development Index over 1990-2015,
Dryad, Dataset, https://doi.org/10.5061/dryad.dk1j0
```

![gdp_hdi](https://user-images.githubusercontent.com/6677629/168412311-8e1de844-298e-4c4f-8ffc-2ce38963f70c.gif)


#### Earth Engine Snippet

```js
var gdp_ppp = ee.Image("projects/sat-io/open-datasets/GRIDDED_HDI_GDP/GDP_PPP_1990_2015_5arcmin_v2");
var gdp_ppp_30arc = ee.Image("projects/sat-io/open-datasets/GRIDDED_HDI_GDP/GDP_PPP_30arcsec_v3");
var gdp_per_capita = ee.Image("projects/sat-io/open-datasets/GRIDDED_HDI_GDP/GDP_per_capita_PPP_1990_2015_v2");
var hdi = ee.Image("projects/sat-io/open-datasets/GRIDDED_HDI_GDP/HDI_1990_2015_v2");
var admin_areas = ee.Image("projects/sat-io/open-datasets/GRIDDED_HDI_GDP/admin_areas_GDP_HDI");
var pedigree_gdp = ee.Image("projects/sat-io/open-datasets/GRIDDED_HDI_GDP/pedigree_GDP_per_capita_PPP_1990_2015_v2");
var pedigree_hdi = ee.Image("projects/sat-io/open-datasets/GRIDDED_HDI_GDP/pedigree_HDI_1990_2015_v2");
```

Sample Code: https://code.earthengine.google.com/75ab868ddbf11372285c4bc009655f1d


#### License
This work is licensed under a CC0 1.0 Universal (CC0 1.0) Public Domain Dedication license.

Produced by : Kummu, Matti; Taka, Maija; Guillaume, Joseph H. A.

Curated in GEE by : Samapriya Roy

Keywords: : Development indicator, global spatial data, gridded data, Gross Domestic Product (GDP), Human Development Index (HDI), Purchasing Power Parity (PPP)

Last updated on GEE: 2022-04-30
