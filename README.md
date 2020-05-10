# awesome-gee-community-datasets
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

Community Datasets added by users and made available for use at large


### High Resolution Settlement Layer

To reference this data, please use the following citation:

```
Facebook Connectivity Lab and Center for International Earth Science Information Network - CIESIN - Columbia University. 2016. High Resolution Settlement Layer (HRSL). Source imagery for HRSL Copyright 2016 DigitalGlobe. Accessed DAY MONTH YEAR. Data shared under: Creative Commons Attribution International.
```


You can get methodology here:

https://dataforgood.fb.com/docs/methodology-high-resolution-population-density-maps-demographic-estimates/

and step by step download here

https://dataforgood.fb.com/docs/high-resolution-population-density-maps-demographic-estimates-documentation/


![HRSL_pop](https://user-images.githubusercontent.com/6677629/81494362-4e8ed080-9276-11ea-8feb-f286a2bcb8da.gif)

#### Earth Engine Snippet
```js
var HRSL = ee.ImageCollection("projects/sat-io/open-datasets/hrslpop")
```

Sample Code: https://code.earthengine.google.com/cc202df2d11ecd32960d414949996402

Extra Bit: [Medium Article here](https://medium.com/@samapriyaroy/community-datasets-in-google-earth-engine-an-experiment-b72daa474819)

Download Tool/Code snippets if any: [hdxpop](https://github.com/samapriya/hdxpop)

Curated by: Samapriya Roy

Last updated: 2020-03-31


