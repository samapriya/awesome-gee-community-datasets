# Relative Wealth Index (RWI)

The Relative Wealth Index predicts the relative standard of living within countries using de-identified connectivity data, satellite imagery and other nontraditional data sources. This index is built using nontraditional data sources, including satellite imagery and de-identified Facebook connectivity data. The index is validated using ground truth measurements from the Demographic and Health Surveys. The data is provided for 93 low and middle-income countries at 2.4km resolution.

#### Extra processing
The datasets are provided as CSV files with lat long Relative Wealth Index (RWI) and error. The CSV files are converted to Shapefiles and ingested as tables for each of the countries. A master feature collection is then created to combine all feature collections across low and middle-income countries (LMICs) countries. Currently only 92 countries are made available from Facebook. You can download the updated dataset from the [Humanitarian Data Exchange website](https://data.humdata.org/dataset/relative-wealth-index) or from [Facebook's data for Good website](https://dataforgood.fb.com/tools/relative-wealth-index/).

#### Steps

- Researchers at the University of California - Berkeley and Facebook developed micro-estimates of wealth and poverty that cover the populated surface of all 135 low and middle-income countries (LMICs) at 2.4km resolution.
- They leverage measurements of household wealth collected through face-to-face surveys conducted by the United States Agency for International Development  with 1,457,315 unique households living in 66,819 villages in 56 different LMICs around the world.
- They use spatial markers to link villages to non-traditional data sources, including satellite imagery, cellular network data, topographic maps, and de-identified connectivity data from Facebook.
- They process the non-traditional data using deep learning and other computational algorithms, which convert the raw data to a set of quantitative features for each village.
- They use these features to train a supervised machine learning model that predicts the relative wealth of each populated 2.4km2 grid cell on the planet, even in regions where no ground truth data exists.

![rwi](https://user-images.githubusercontent.com/6677629/115134793-efceec80-9fd8-11eb-8a6d-286528d985a1.gif)

#### Earth Engine Snippet

```js
var rwi = ee.FeatureCollection("projects/sat-io/open-datasets/facebook/relative_wealth_index");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/RELATIVE-WEALTH-INDEX(RWI)

Interactive Map: http://beta.povertymaps.net/

#### License

Public Domain/No restrictions (CC0): Under the terms of this license you are free to use the material for any purpose without any restrictions.

Processed secondary/formatted & Curated by: Samapriya Roy

Keywords: :"Relative Wealth Index, RWI, Facebook, CIESIN, gridded"

Last updated: 2021-04-18
