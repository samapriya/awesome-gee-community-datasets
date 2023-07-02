# geeSEBAL-MODIS Continental scale ET for South America

The geeSEBAL-MODIS Version 0-02 Evapotranspiration (ET) product is an 8-day product produced at 500 meter pixel resolution. The algorithm for ET calculation is based on the SEBAL model and the FAO Penman-Monteith equation, which includes inputs of daily meteorological reanalysis data along with MODIS remotely sensed data products such as vegetation property dynamics, albedo, land cover and land surface temperature (LST).

The pixel values for the layers are the average of all eight days within the period, multiplied by 1000. Images must be multiplied by 0.001 for the actual values. Note that the last 8-day period of each year is a 5 or 6-day composite period, depending on the year. The dataset is available from 2002-07-01 to 2022-12-31. Band information is the following

|Name       |Description                                                                                                                         |Min     |Max    |Units   |Scale|Offset|
|-----------|------------------------------------------------------------------------------------------------------------------------------------|--------|-------|--------|-----|------|
|ET_24h     |Daily actual evapotranspiration                                                                                                     |0       |6601   |mm day-1|0.001|0     |
|FE         |Evaporative fraction                                                                                                                |0       |1017   |[-]     |0.001|0     |
|ETr        |Reference evapotranspiration                                                                                                        |-220    |7543   |mm day-1|0.001|0     |
|Rn24h_G    |Daily average net radiation                                                                                                         |-84478  |198081 |w m-2   |0.001|0     |
|LE         |Instantaneous latent heat flux                                                                                                      |0       |2478572|w m-2   |0.001|0     |
|H          |Instantaneous sensible heat flux                                                                                                    |-829456 |964618 |w m-2   |0.001|0     |
|Rn         |Instantaneous net radiation                                                                                                         |-5435   |753836 |w m-2   |0.001|0     |
|G          |Instantaneous soil heat flux                                                                                                        |-2039206|102284 |w m-2   |0.001|0     |
|End_Members|Cold and hot endmember candidates. Pixels with -1.0 values are cold candidates and pixels equal to 1.0 are hot endmember candidates.|-121    |172    |[-]     |0.001|0     |
|LST_lat    |Land surface temperature, corrected by the adiabatic lapse rate and normalized by the solar zenith angle.                           |272879  |330413 |K       |0.001|0     |
|LST_dem    |Land surface temperature, corrected by the adiabatic lapse rate                                                                     |254456  |331505 |K       |0.001|0     |

#### Citation Preprint

```
Comini, Bruno & Ruhoff, Anderson & Laipelt, Leonardo & Fleischmann, Ayan & Huntington, Justin & Morton, Charles & Melton, Forrest & Erickson,
Tyler & Roberti, Débora & Souza, Vanessa & Biudes, Marcelo & Machado, Nadja & Santos, Carlos & Cosio, Eric. (2023). geeSEBAL-MODIS: Continental
scale evapotranspiration based on the surface energy balance for South America. 10.13140/RG.2.2.17579.11041.
```

![gee-sebal](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/51baa12f-fcf8-4f95-ad6b-d616e20e3ec4)

#### Code Snippet
```js
var geesebal = ee.ImageCollection("projects/et-brasil/assets/geesebal/myd11a2/sa/v0-02")
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/GEESEBAL-ET-SOUTH-AMERICA

#### License
The datset is made available under a CC-BY-4.0 license.

Curated by: Bruno Comini de Andrade, Anderson Ruhoff, Leonardo Laipelt

Keywords: evapotranspiration, South America, water resources

Last updated: 2023-03-26
https://code.earthengine.google.com/ba815cfffab1b2f60ef92446693b9170
