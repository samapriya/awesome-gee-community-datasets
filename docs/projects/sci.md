# Social Connectedness Index (SCI)

The Social Connectedness Index measures the strength of connectedness between two geographic areas as represented by Facebook friendship ties. These connections can reveal important insights about economic opportunities, social mobility, trade and more. We use aggregated friendship connections on Facebook to measure social connectedness between geographies. Locations are assigned to users based on information they provide, connection information, and location services they have opted into (to learn more about how Facebook uses location data and how to control location privacy see Location Privacy Basics).   We use these friendships to estimate the probability a pair of users in these countries are Facebook friends (we rescale based on the population of two regions) and map this to an index score called the Social Connectedness Index (SCI). If the SCI is twice as large between two pairs of regions, it means the users in the first region-pair. are about twice as likely to be connected than the second region-pair. More details on the methodology can be found by clicking Learn More below, or in the paper [Social Connectedness: Measurement, Determinants, and Effects published in the Journal of Economic Perspectives](https://www.aeaweb.org/articles/pdf/doi/10.1257/jep.32.3.259).

## Features

Friendship Data
The Social Connectedness Index offers a new type of data to the research and non-profit community, measuring the frequency and density of friendship and social ties around the world, a type of data that has rarely been made available to those interested in understanding how relationships affect social outcomes.

Global Reach
With over 2.5 billion active users globally, the Social Connectedness Index from Facebook provides the first comprehensive measure of social networks at an international level.

Privacy
The index provides researchers with connectedness scores, but not the number of links between two places or any of the underlying data. The data set uses sampling, differential privacy noise, and normalization to protect privacy.

#### Extra processing
The datasets are provided as TSV files with lat long Relative Wealth Index (RWI) and error. The TSV files are then converted to spatial by joining with country boundary units and ingested as tables for each of the countries. For now only Country to Country SCIs are processed. Two datasets are created one using the User or First Location and the second using the FR_LOC or Second Location. You can [download the source data here to process it as needed](https://data.humdata.org/dataset/social-connectedness-index).

![sci](https://user-images.githubusercontent.com/6677629/115154756-170dd400-a042-11eb-8edf-a856d22d76b4.gif)

#### Citation

```
M. Bailey, R. Cao, T. Kuchler, J. Stroebel, and A. Wong. Social connectedness: Measurements,
determinants, and effects. Journal of Economic Perspectives, 32(3):259–80, 2018b.and the Facebook Data for Good Program, Social Connectedness Index (SCI). https://dataforgood.fb.com/, Accessed DAY MONTH YEAR."
```

Each dataset has three columns

|Column Name|Description    |
|-----------|---------------|
|user_loc   |First Location |
|fr_loc     |Second Location|
|scaled_sci |Scaled SCI     |


#### Earth Engine Snippet

```js
var sci_user_loc = ee.FeatureCollection("projects/sat-io/open-datasets/facebook/sci_user_loc");
var sci_fr_loc = ee.FeatureCollection("projects/sat-io/open-datasets/facebook/sci_fr_loc");
```

Sample Code: https://code.earthengine.google.com/4dadf30cb45f181e301fcd4f17dfdb2d

Interactive Map: http://beta.povertymaps.net/

#### License

Public Domain/No restrictions (CC0): Under the terms of this license you are free to use the material for any purpose without any restrictions.

Processed secondary/formatted & Curated by: Samapriya Roy

Keywords: : "Social Connectedness Index, SCI, Facebook, CIESIN, country,first location, second location"

Last updated: 2021-04-18
