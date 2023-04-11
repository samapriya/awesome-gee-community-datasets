# GlobCover Global Land Cover

GlobCover is an ESA initiative which began in 2005 in partnership with JRC, EEA, FAO, UNEP, GOFC-GOLD and IGBP. The aim of the project was to develop a service capable of delivering global composites and land cover maps using as input observations from the 300m MERIS sensor on board the ENVISAT satellite mission. ESA makes available the land cover maps, which cover 2 periods: December 2004 - June 2006 and January - December 2009. You can download the datasets [here](http://due.esrin.esa.int/page_globcover.php).

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

![globcover_animation](https://user-images.githubusercontent.com/6677629/231052814-fd4ccaee-2bac-44e3-9a94-b7a26677718e.gif)

#### Earth Engine Snippet

```js
var globcoverv23 = ee.Image("projects/sat-io/open-datasets/ESA/GLOBCOVER_L4_200901_200912_V23");
var globcoverv22 = ee.Image("projects/sat-io/open-datasets/ESA/GLOBCOVER_200412_200606_V22_Global_CLA");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/ESA-GLOBCOVER

#### License

The GlobCover products have been processed by ESA and by the Université Catholique de Louvain. They are made available to the public by ESA. You may use the GlobCover land cover map for educational and/or scientific purposes, without any fee on the condition that you credit ESA and the Université Catholique de Louvain as the source of the GlobCover products:

```
© ESA 2010 and UCLouvain
Accompanied by a link to our ESA DUE GlobCover website: http://due.esrin.esa.int/page_globcover.php
```

Should you write any scientific publication on the results of research activities that use GlobCover products as input, you shall acknowledge the ESA GlobCover 2009 Project in the text of the publication and provide ESA with an electronic copy of the publication (due@esa.int).
If you wish to use the GlobCover 2009 products in advertising or in any commercial promotion, you shall acknowledge the ESA GlobCover 2009 Project and you must submit the layout to ESA for approval beforehand (due@esa.int).

Created by: ESA and by the Université Catholique de Louvain

Curated in GEE by : Samapriya Roy

keywords: Landcover, Global Landcover, ESA, JRC, EEA, FAO, UNEP, GOFC-GOLD and IGBP, ENVISAT product

Last updated on GEE: 2023-02-28
