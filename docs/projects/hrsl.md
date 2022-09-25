# High Resolution Settlement Layer
In partnership with the Center for International Earth Science Information Network (CIESIN) at Columbia University, Facebook used state-of-the-art computer vision techniques to identify buildings from publicly accessible mapping services to create the world's most accurate population datasets. You can [read about their project here](https://dataforgood.fb.com/tools/population-density-maps/). These are the datasets available for download on the Humanitarian Data Exchange for nearly every country in the world:

* Overall population density
* Male
* Female
* Women of reproductive age (ages 15-49)
* Children (ages 0-5)
* Youth (ages 15-24)
* Elderly (ages 60+)


To reference this data, please use the following citation:

```
Facebook Connectivity Lab and Center for International Earth Science Information Network - CIESIN - Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery for HRSL Copyright 2016 DigitalGlobe. Accessed DAY MONTH YEAR. Data shared under: Creative Commons Attribution International.
```


You can get methodology here:

https://dataforgood.fb.com/docs/methodology-high-resolution-population-density-maps-demographic-estimates/

and step by step download here

https://dataforgood.fb.com/docs/high-resolution-population-density-maps-demographic-estimates-documentation/

License: Creative Commons Attribution International

![HRSL_pop](https://user-images.githubusercontent.com/6677629/110987570-e648c980-8334-11eb-8615-535114fde903.gif)

#### Earth Engine Snippet
```js
var HRSL = ee.ImageCollection("projects/sat-io/open-datasets/hrsl/hrslpop");
var HRSL_men = ee.ImageCollection("projects/sat-io/open-datasets/hrsl/hrsl_men");
var HRSL_women = ee.ImageCollection("projects/sat-io/open-datasets/hrsl/hrsl_women");
var HRSL_youth = ee.ImageCollection("projects/sat-io/open-datasets/hrsl/hrsl_youth");
var HRSL_children_under_five = ee.ImageCollection("projects/sat-io/open-datasets/hrsl/hrsl_children_under_five");
var HRSL_women_reproductive_age = ee.ImageCollection("projects/sat-io/open-datasets/hrsl/hrsl_women_reproductive_age");
var HRSL_elderly_over_sixty = ee.ImageCollection("projects/sat-io/open-datasets/hrsl/hrsl_elderly_over_sixty");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/FACEBOOK-HRSL-30m

Extra Info: [Medium Article here](https://medium.com/@samapriyaroy/community-datasets-in-google-earth-engine-an-experiment-b72daa474819)

Download Tool/Code snippets if any: [hdxpop](https://github.com/samapriya/hdxpop)

Curated by: Samapriya Roy

Keywords: High Density Population, Population, Facebook

#### Changelog

* Automated version check & updated added
* Now includes data version as metadata & uses global COGs
* Now includes data from HRSL v1.5+

Last updated: 2022-08-27
