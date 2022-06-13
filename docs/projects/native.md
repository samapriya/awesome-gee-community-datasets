# Native Land (Indigenous Land Maps)

Land acknowledgements are a way that people insert an awareness of Indigenous presence and land rights in everyday life. This is often done at the beginning of ceremonies, lectures, or, in this case, education guides. It can be an explicit yet limited way to recognize the history of colonialism and first nations as well as a need for change in settler-colonial societies. In this context, we’re looking to acknowledge the existence of Indigenous bodies in geography and how they occupy land. You can visit the actual map here https://native-land.ca/

Native-Land.ca offers an online platform where users can interact with maps of Indigenous territories, treaties, and languages, and locate themselves and their favorite places on the map. Fundamentally, the maps aim to visualize the complexity and diversity of Indigenous peoples, nations, and cultures across the Americas, Australia, and increasingly the world, so that nonIndigenous and Indigenous people alike can increase their understanding and knowledge of the breadth and depth of Indigenous history in these places. Some of the studies in the systematic review describe Indigenous populations within administrative boundaries (i.e. states and countries), for which data is relatively easy to obtain as it is often available through government sources. Other studies described Indigenous groups, lands and territories, for which data isn’t readily available for various reasons (colonial legacies and land tenure and governance, with factors such as changing boundaries and non-digitized records).


#### Native Land Disclaimer
This map does not represent or intend to represent official or legal boundaries of any Indigenous nations. To learn about definitive boundaries, contact the nations in question. Also, this map is not perfect -- it is a work in progress with tons of contributions from the community. Please send us fixes if you find errors. If you would like to read more about the ideas behind Native Land or where we are going, check out the blog. You can also see the roadmap. Also something to keep in mind

* Native Land is not meant to be vetted at the level of an academic resource
* Native Land is aimed at settlers to engage them with Indigenous history in a fun, interactive, and subtle way
* The datasets are always in flux and the latest datasets can be downloaded [using their API](https://native-land.ca/resources/api-docs/)


#### Suggested Citation

(dataset) Native Land Territories map. (2021). Native Land CA. https://native-land.ca/. Accessed 2021-09-19.

![native](https://user-images.githubusercontent.com/6677629/133938352-7c4d09a1-99b2-490f-acdd-14627c1e53bb.gif)


#### Earth Engine Snippet

```js
var territories = ee.FeatureCollection("projects/sat-io/open-datasets/native-land/indigenousTerritories");
var languages = ee.FeatureCollection("projects/sat-io/open-datasets/native-land/indigenousLanguages");
var treaties = ee.FeatureCollection("projects/sat-io/open-datasets/native-land/indigenousTreaties");
```

Sample code: https://code.earthengine.google.com/0c664cc64c35a964de7e36ffe54b41d4


#### License

The Native Land Maps are under a Creative Commons International Attribution License and the datasets are publicly available resource.

Created by: Native Land CA

Curated by: Samapriya Roy

Keywords: native lands, indigenousTreaties, indigenousLanguages, indigenousTerritories, Indigenous, land rights

Last updated: 2022-06-12
