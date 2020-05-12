# awesome-gee-community-datasets
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

Community Datasets added by users and made available for use at large

## [Submit your Dataset as Issue Now using Template Link](https://github.com/samapriya/awesome-gee-community-datasets/issues/new?assignees=samapriya&labels=&template=new-community-gee-dataset-template.md&title=Dataset+%26+Curator+Name)

![new_issue_datasets](https://user-images.githubusercontent.com/6677629/81495266-2eaedb00-927d-11ea-849f-af017ac7b32a.gif)

****

## Table of Contents
* [High Resolution Settlement Layer](#high-resolution-settlement-layer)
* [Global Shoreline Dataset](#global-shoreline-dataset)
* [Mapbiomas Annual land cover and use maps](#mapbiomas-annual-land-cover-and-use-maps)
* [Planet Open CA Subset](#planet-open-ca-subset)
* [Planet Open CA UDM2 Subset](#planet-open-ca-udm2-subset)


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

Extra Info: [Medium Article here](https://medium.com/@samapriyaroy/community-datasets-in-google-earth-engine-an-experiment-b72daa474819)

Download Tool/Code snippets if any: [hdxpop](https://github.com/samapriya/hdxpop)

Curated by: Samapriya Roy

Last updated: 2020-03-31
****

### Global Shoreline Dataset

A new 30-m spatial resolution global shoreline vector (GSV) was developed from annual composites of 2014 Landsat satellite imagery. The semi-automated classification of the imagery was accomplished by manual selection of training points representing water and non-water classes along the entire global coastline. Polygon topology was applied to the GSV, resulting in a new characterisation of the number and size of global islands. Three size classes of islands were mapped: continental mainlands (5), islands greater than 1 km2 (21,818), and islands smaller than 1 km2 (318,868). The GSV represents the shore zone land and water interface boundary, and is a spatially explicit ecological domain separator between terrestrial and marine environments. The development and characteristics of the GSV are presented herein. An approach is also proposed for delineating standardised, high spatial resolution global ecological coastal units (ECUs). For this coastal ecosystem mapping effort, the GSV will be used to separate the nearshore coastal waters from the onshore coastal lands. The work to produce the GSV and the ECUs is commissioned by the Group on Earth Observations (GEO), and is associated with several GEO initiatives including GEO Ecosystems, GEO Marine Biodiversity Observation Network (MBON) and GEO Blue Planet.

Publication URL: https://pubs.er.usgs.gov/publication/70202401

Scale: 30m

Please use Citation:
```
Sayre, R., S. Noble, S. Hamann, R. Smith, D. Wright, S. Breyer, K. Butler, K. Van Graafeiland, C. Frye, D. Karagulle, D. Hopkins, D. Stephens, K. Kelly, Z. Basher, D. Burton, J. Cress, K. Atkins, D. Van Sistine, B. Friesen, R. Allee, T. Allen, P. Aniello, I. Asaad, M. Costello, K. Goodin, P. Harris, M. Kavanaugh, H. Lillis, E. Manca, F. Muller-Karger, B. Nyberg, R. Parsons, J. Saarinen, J. Steiner, and A. Reed. 2019. A new 30 meter resolution global shoreline vector and associated global islands database for the development of standardized ecological coastal units. Journal of Operational Oceanography, 12:sup2, S47-S56, DOI: 10.1080/1755876X.2018.1529714
```

Shared Under: Creative Commons Attribution-Share Alike 4.0 International License

![global_shorlines](https://user-images.githubusercontent.com/6677629/81495134-112d4180-927c-11ea-82db-face703c3238.gif)

#### Earth Engine Snippet
```js
var mainlands = ee.FeatureCollection('projects/sat-io/open-datasets/shoreline/mainlands');
var big_islands = ee.FeatureCollection('projects/sat-io/open-datasets/shoreline/big_islands');
var small_islands = ee.FeatureCollection('projects/sat-io/open-datasets/shoreline/small_islands');
```

Sample Code: https://code.earthengine.google.com/609a16955ed07b282fcd4bff4750f814

Extra Info: Over 100 Million+ vertices

Curated by: Samapriya Roy

Last updated: 2020-05-08
****

### Mapbiomas Annual land cover and use maps

The Brazilian Annual Land Use and Land Cover Mapping Project is an initiative that involves a collaborative network of biomes, land use, remote sensing, GIS and computer science experts that rely on Google Earth Engine platform and its cloud processing and automated classifiers capabilities to generate Brazil’s annual land use and land cover time series. MapBiomas Project - is a multi-institutional initiative to generate annual land cover and use maps using automatic classification processes applied to satellite images. The complete description of the project can be [found here](http://mapbiomas.org).

Scale: 30 m,
Data Type: Multiple raster datasets and types

Please use Citation:
```
"Project MapBiomas - Collection [version] of Brazilian Land Cover & Use Map Series, accessed on [date] through the link: [LINK]"
```

Shared Under: Creative Commons Attribution-Share Alike 4.0 International License

![MapBiomas](https://user-images.githubusercontent.com/6677629/81698669-5300e800-9434-11ea-9c5f-e8bf9588e737.gif)

#### Earth Engine Snippet
```js
//From downloader v 1.1.4
assets: {
    integration: 'projects/mapbiomas-workspace/public/collection4_1/mapbiomas_collection41_integration_v1',
    transitions: 'projects/mapbiomas-workspace/public/collection4_1/mapbiomas_collection41_transitions_v1',
    vectors: [
        'projects/mapbiomas-workspace/AUXILIAR/areas-protegidas',
        'projects/mapbiomas-workspace/AUXILIAR/municipios-2016',
        'projects/mapbiomas-workspace/AUXILIAR/estados-2017',
        'projects/mapbiomas-workspace/AUXILIAR/biomas-2019',
        'projects/mapbiomas-workspace/AUXILIAR/bacias-nivel-1',
        'projects/mapbiomas-workspace/AUXILIAR/bacias-nivel-2',
    ]
},
```

Add repo link: https://code.earthengine.google.com/?accept_repo=users/mapbiomas/user-toolkit

Extra Info: [GitHub Tutorial](https://github.com/mapbiomas-brazil/user-toolkit)

Curated by: [MapBiomas](https://mapbiomas.org/)

Last updated: [Refer to webpage](https://mapbiomas.org/)
****


### Planet Open CA Subset

A sample dataset from Planet's open california project for 2018. Includes PlanetScope 4 Band Surface Reflectance data.

Scale: 3 m

Please use Citation:
```
Planet Team (2017). Planet Application Program Interface: In Space for Life on Earth. San Francisco, CA. https://api.planet.com.
```

Shared Under: Creative Commons Attribution-Share Alike 4.0 International License

![dark_openca](https://user-images.githubusercontent.com/6677629/81646337-0e0b9000-93f9-11ea-92b2-242058cbab07.gif)

#### Earth Engine Snippet
```js
var ps4bsr = ee.ImageCollection("projects/sat-io/open-ca/ps4bsr");
```

Sample Code: https://code.earthengine.google.com/47b1ba27d7de0e467164bde18bee56a5

Curated by: Samapriya Roy

Last updated: 2019-02-01
****

### Planet Open CA UDM2 Subset

A sample dataset from Planet's open california project for 2018. Includes UDM2 dataset for PlanetScope 4 Band data.

Scale: 3 m,
Data Type: 8 band and 8 bit data

Please use Citation:
```
Planet Team (2017). Planet Application Program Interface: In Space for Life on Earth. San Francisco, CA. https://api.planet.com.
```

Shared Under: Creative Commons Attribution-Share Alike 4.0 International License

![dyanmic_cloud_export](https://user-images.githubusercontent.com/6677629/81249836-a535a980-8fed-11ea-97c8-757e71bb6a64.gif)

#### Earth Engine Snippet
```js
var udm2 = ee.ImageCollection("projects/sat-io/open-datasets/udm2-tests/ps4bsr_udm2");
```

Sample Code: https://code.earthengine.google.com/10420481bb8cc8b4d7d258eb55e3ef67

Extra Info: [Medium Article](https://medium.com/@samapriyaroy/cloud-filter-the-cloud-native-way-planet-udm2-in-google-earth-engine-208502a99483)

Curated by: Samapriya Roy

Last updated: 2020-05-01
****
