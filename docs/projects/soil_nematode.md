# Soil nematode abundance & functional group composition

As the most abundant animals on earth, nematodes are a dominant component of the soil community. They play critical roles in regulating biogeochemical cycles and vegetation dynamics within and across landscapes and are an indicator of soil biological activity. Here, we present a comprehensive global dataset of soil nematode abundance and functional group composition. This dataset includes 6,825 georeferenced soil samples from all continents and biomes. For geospatial mapping purposes these samples are aggregated into 1,933 unique 1-km pixels, each of which is linked to 73 global environmental covariate data layers. This study uses direct measurements of soil nematode abundance from 6,825 georeferenced locations around the world, covering all continents and all terrestrial biomes. You can read the [paper here](https://www.nature.com/articles/s41597-020-0437-3)

#### Data Citation

```
Hoogen, Johan van den; Geisen, Stefan; Wall, Diana H.; Wardle, David A.; Traunspurger, Walter; Goede, Ron G. M. de;
et al. (2020): A global database of soil nematode abundance and functional group composition. figshare. Collection.
https://doi.org/10.6084/m9.figshare.c.4718003.v1
```

#### Paper Citation

```
van den Hoogen, J., Geisen, S., Wall, D.H. et al. A global database of soil nematode abundance and functional group
composition. Sci Data 7, 103 (2020). https://doi.org/10.1038/s41597-020-0437-3
```

![soil_nematode](https://user-images.githubusercontent.com/6677629/129513657-4ac209af-62d4-4fe3-bcff-c8143b7bb998.PNG)

#### Earth Engine Snippet

```js
var nematode= ee.FeatureCollection("projects/sat-io/open-datasets/global-nematode")
```

Sample Code: https://code.earthengine.google.com/dff3040051231efbb999ea8f2403add0

|Property Name  |GEE_Property    |Description                                        |Units                        |Source                              |
|---------------|----------------|---------------------------------------------------|-----------------------------|------------------------------------|
|Sample_ID      |﻿Sample_ID      |Unique sample ID                                   |                             |                                    |
|Bacterivores   |Bacterivores    |Number of bacterivorous nematodes                  |individuals per 100g dry soil|                                    |
|Fungivores     |Fungivores      |Number of fungivorous nematodes                    |individuals per 100g dry soil|                                    |
|Herbivores     |Herbivores      |Number of herbivorous nematodes                    |individuals per 100g dry soil|                                    |
|Omnivores      |Omnivores       |Number of omnivorous nematodes                     |individuals per 100g dry soil|                                    |
|Predators      |Predators       |Number of predatory nematodes                      |individuals per 100g dry soil|                                    |
|Unidentified   |Unidentified    |Number of unidentified nematodes                   |individuals per 100g dry soil|                                    |
|Total_Number   |Total_Number    |Total number of nematodes                          |individuals per 100g dry soil|                                    |
|Latitude       |Pixel_Lat       |Sample latitude                                    |Decimal degree in WGS84      |                                    |
|Longitude      |Pixel_Long      |Sample longitude                                   |Decimal degree in WGS84      |                                    |
|WWF_Biome      |WWF_Biome       |WWF Biome                                          |                             |https://www.worldwildlife.org/biomes|
|sampling method|sampling method:|Nematode extraction method                         |                             |                                    |
|sampling_ref   |sampling_ref    |Nematode extraction method, summarised             |                             |                                    |
|sampling depth |sampling depth  |Sampling Depth                                     |cm                           |                                    |
|DOI/URL        |DOI/URL         |Reference to original publication, where applicable|                             |                                    |
|Data_provider  |Data_provider   |Name of co-author(s) who supplied data             |                             |                                    |

#### License

Creative Commons Attribution-Share Alike 4.0 International License

Created by: Hoogen et al

Curated by: Samapriya Roy

Keywords: : nematode,soil ecology,biogeographic studies,soil biotic community

Last updated: 2021-08-16
