# West Africa Coastal Vulnerability Mapping

The West Africa Coastal Vulnerability Mapping: Social Vulnerability Indices data set includes three indices: Social Vulnerability, Population Exposure, and Poverty and Adaptive Capacity. The Social Vulnerability Index (SVI) was developed using six indicators: population density (2010), population growth (2000-2010), subnational poverty and extreme poverty (2005), maternal education levels circa 2008, market accessibility (travel time to markets) circa 2000, and conflict data for political violence (1997-2013). Because areas of high population density and growth (high vulnerability) are generally associated with urban areas that have lower levels of poverty and higher degrees of adaptive capacity (low vulnerability), to some degree, the population factors cancel out the poverty and adaptive capacity indicators. To account for this, the data set includes two sub-indices, a Population Exposure Index (PEI), which only includes population density and population growth; and a Poverty and Adaptive Capacity Index (PACI), composed of subnational poverty, maternal education levels, market accessibility, and conflict. These sub-indices are able to isolate the population indicators from the poverty and conflict metrics. The indices represent Social Vulnerability in the West Africa region within 200 kilometers of the coast.

Purpose:
To provide a measure of social vulnerability and "defenselessness" in the face of climate stressors in the coastal zone of West Africa.

The documentation for this dataset is [available here](https://sedac.ciesin.columbia.edu/data/set/wacvm-social-vulnerability-indices/docs)

Use the following citation

```
Center for International Earth Science Information Network - CIESIN - Columbia University. 2018. West Africa Coastal Vulnerability Mapping: Social Vulnerability Indices. Palisades, NY: NASA Socioeconomic Data and Applications Center (SEDAC). https://doi.org/10.7927/H4H41PCK. Accessed DAY MONTH YEAR.
```

![wacvm_svi](https://user-images.githubusercontent.com/6677629/114324581-7de63700-9af0-11eb-82ea-d70cf71c47ea.gif)

#### Earth Engine Snippet

```js
var wacvm_paci = ee.FeatureCollection("projects/sat-io/open-datasets/sedac/wacvm-social-vulnerability-indices-paci");
var wacvm_pei = ee.FeatureCollection("projects/sat-io/open-datasets/sedac/wacvm-social-vulnerability-indices-pei");
var wacvm_svi = ee.FeatureCollection("projects/sat-io/open-datasets/sedac/wacvm-social-vulnerability-indices-svi");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/WEST_AFRICA-COASTAL-VULN

Shared License:
This work is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0). Users are free to use, copy, distribute, transmit, and adapt the work for commercial and non-commercial purposes, without restriction, as long as clear attribution of the source is provided.

Curated by: Samapriya Roy

Keywords: census geography, GPWv4, gridded population, uniform distribution

Last updated: 2021-04-11
