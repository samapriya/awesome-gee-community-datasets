# Land Change Monitoring, Assessment, and Projection (LCMAP) v1.2

Land Change Monitoring, Assessment, and Projection (LCMAP) represents a new generation of land cover mapping and change monitoring from the U.S. Geological Survey’s Earth Resources Observation and Science (EROS) Center. LCMAP answers a need for higher quality results at greater frequency with additional land cover and change variables than previous efforts. LCMAP Collection 1.2 products were released in November 2021, including LCMAP products for 1985-2020.

LCMAP science product documentation contain details, descriptions and caveats for the products and it can be [downloaded here](https://www.usgs.gov/media/files/lcmap-collection-12-science-product-guide). Collection 1.0 for Hawaii was made available Jan 19 and [more information can be found here](https://www.usgs.gov/special-topics/lcmap/collection-1-hawaii-science-products)

<center>

|Additional Resources| Links |
|---------------------------|-------|
|LCMAP website|https://www.usgs.gov/core-science-systems/eros/lcmap|
|Algorithm description document|https://www.usgs.gov/media/files/lcmap-ccdc-add|
|RSS Feed|https://www.usgs.gov/core-science-systems/eros/lcmap/news|
|Validation (these are tables)|https://www.sciencebase.gov/catalog/item/5f86f28682cebef40f170771|
|Reference data (these are points)|https://www.sciencebase.gov/catalog/item/5e42e54be4b0edb47be84535|
|USGS LCMAP Publications|https://www.usgs.gov/core-science-systems/eros/lcmap/publications   |

</center>


#### LCMAP Products

LCMAP provides 10 science products based on the USGS implementation of CCDC. The science products provide annual products for the years 1985-2019 for each CONUS ARD tile and CONUS level downloads are available which is used for the GEE collection. Land surface change products, denoted by the “SC” prefix in the short name, are produced directly from CCDC time series models. Land cover products, denoted by the “LC” prefix in the short name, are produced by the classification of the time series models. Note to optimize size GeoTiff files were run through a lossless LZW compression.

|Product Name                   |Short Name|Product Description                                                                                            |
|-------------------------------|----------|---------------------------------------------------------------------------------------------------------------|
|Time of Spectral Change        |SCTIME    |Indicator of a spectral change in the current year and the specific timing (day-of-year - DOY) within the year.|
|Change Magnitude               |SCMAG     |Indicator of a spectral change in the current year and degree of change.                                       |
|Spectral Stability Period      |SCSTAB    |Time, in days, that the spectral time series has been in its current state.                                    |
|Time Since Last Change         |SCLAST    |Time, in days, since the last identified Spectral Change (SCTIME).                                             |
|Spectral Model Quality         |SCMQA     |Information regarding the type of time series model applied on July 1 of the current year.                     |
|Primary Land Cover             |LCPRI     |The most likely Level 1 land cover class on July 1 of the current year                                         |
|Primary Land Cover Confidence  |LCPCONF   |Measure of confidence that the Primary Land Cover label matches the training data.                             |
|Secondary Land Cover           |LCSEC     |The second most likely Level 1 land cover class on July 1 of the current year                                  |
|Secondary Land Cover Confidence|LCSCONF   |Measure of confidence that the Secondary Land Cover label matches the training data.                           |
|Annual Land Cover Change       |LCACHG    |Synthesis of Primary Land Cover of current and previous year identifying changes in land cover class.          |

#### Product Specifications

The product specifications allows for understanding categorical vs continious datasets and informed pyramid policy for ingest into Google Earth Engine.

|Short Name|Data Type|Units              |Range              |Valid Range         |Fill Value|
|----------|---------|-------------------|-------------------|--------------------|----------|
|SCTIME    |UINT16   |DOY                |0-65535            |0-366               |0         |
|SCMAG     |FLOAT32  |Unitless           |-3.4e+38 - +3.4e+38|0 to +3.4e+38       |0         |
|SCSTAB    |UINT16   |Days               |0-65535            |0-65535             |0         |
|SCLAST    |UINT16   |Days               |0-65535            |0-65535             |0         |
|SCMQA     |UINT8    |Discrete           |0-255              |0- 4,6,8,14,24,44,54|0         |
|LCPRI     |UINT8    |Discrete           |0-255              |0-8                 |0         |
|LCPCONF   |UINT8    |                   |0-255              |0-255               |0         |
|LCSEC     |UINT8    |Discrete           |0-255              |0-8                 |0         |
|LCSCONF   |UINT8    |                   |0-255              |0-255               |0         |
|LCACHG    |UINT8    |Discrete           |0-255              |0-87                |0         |


#### LCMAP Level 1 Land Cover Classes

For classification of thematic land cover, LCMAP implements a Level 1 classification schema similar to an Anderson Level 1 (Anderson et al., 1976) representing dominant land cover classes most relevant to remotely monitoring land change.

|Land Cover Class|Description                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Developed       |Areas of intensive use with much of the land covered with structures (e.g., high-density residential, commercial, industrial, mining, or transportation), or less intensive uses where the land cover matrix includes vegetation, bare ground, and structures (e.g., low-density residential, recreational facilities, cemeteries, transportation/utility corridors, etc.), including any land functionality related to the developed or built-up activity.|
|Cropland        |Land in either a vegetated or unvegetated state used in production of food, fiber, and fuels. This includes  cultivated and uncultivated croplands, hay lands, orchards, vineyards, and confined livestock operations. Forest plantations are considered as forests or woodlands (Tree Cover class) regardless of the use of the wood products.                                                                                                            |
|Grass/Shrub     |Land predominantly covered with shrubs and perennial or annual natural and domesticated grasses (e.g., pasture), forbs, or other forms of herbaceous vegetation. The grass and shrub cover must comprise at least 10% of the area and tree cover is less than 10% of the area.                                                                                                                                                                             |
|Tree Cover      |Tree-covered land where the tree cover density is greater than 10%. Cleared or harvested trees (i.e., clearcuts) will be mapped according to current cover (e.g., Barren, Grass/Shrub).                                                                                                                                                                                                                                                                    |
|Water           |Areas covered with water, such as streams, canals, lakes, reservoirs, bays, or oceans.                                                                                                                                                                                                                                                                                                                                                                     |
|Wetland         |Lands where water saturation is the determining factor in soil characteristics, vegetation types, and animal communities. Wetlands are composed of mosaics of water, bare soil, and herbaceous or wooded vegetated cover.                                                                                                                                                                                                                                  |
|Ice/Snow        |Land where accumulated snow and ice does not completely melt during the summer period (i.e., perennial ice/snow).                                                                                                                                                                                                                                                                                                                                          |
|Barren          |Land comprised of natural occurrences of soils, sand, or rocks where less than 10% of the area is vegetated.                                                                                                                                                                                                                                                                                                                                               |

#### Citation
There are no restrictions on the use of the LCMAP Reference Data Products. It is not a requirement of data use, but the following citation may be used in publication or presentation materials to acknowledge the USGS as a data source and to credit the original research.

LCMAP Reference Data products courtesy of the U.S. Geological Survey Earth Resources Observation and Science Center.

```
Brown, J.F., Tollerud, H.J., Barber, C.P., Zhou, Q., Dwyer, J.L., Vogelmann, J.E., Loveland, T.R., Woodcock, C.E., Stehman, S.V., Zhu, Z.,
Pengra, B.W., Smith, K., Horton, J.A., Xian, G., Auch, R.F., Sohl, T.L., Sayler, K.L., Gallant, A.L., Zelenak, D., Reker, R.R., and Rover, J.,
2020 Lessons learned implementing an operational continuous United States national land change monitoring capability—The Land Change Monitoring,
Assessment, and Projection (LCMAP) approach: Remote Sensing of Environment, v. 238, article 111356, at https://doi.org/10.1016/j.rse.2019.111356.

Zhu, Z., and Woodcock, C.E., 2014, Continuous change detection and classification of land cover using all available Landsat data: Remote Sensing
of Environment, v. 144, p. 152–171, at https://doi.org/10.1016/j.rse.2014.01.011.
```

![lcmap](https://user-images.githubusercontent.com/6677629/132149114-1fc74475-6991-4336-b2e6-1f7c3df4e5fc.gif)

#### Earth Engine Snippet

```js
var lcachg = ee.ImageCollection("projects/sat-io/open-datasets/LCMAP/LCACHG");
var lcpconf = ee.ImageCollection("projects/sat-io/open-datasets/LCMAP/LCPCONF");
var lcpri = ee.ImageCollection("projects/sat-io/open-datasets/LCMAP/LCPRI");
var lcsconf = ee.ImageCollection("projects/sat-io/open-datasets/LCMAP/LCSCONF");
var lcsec = ee.ImageCollection("projects/sat-io/open-datasets/LCMAP/LCSEC");
var sclast = ee.ImageCollection("projects/sat-io/open-datasets/LCMAP/SCLAST");
var scmag = ee.ImageCollection("projects/sat-io/open-datasets/LCMAP/SCMAG");
var scmqa = ee.ImageCollection("projects/sat-io/open-datasets/LCMAP/SCMQA");
var scstab = ee.ImageCollection("projects/sat-io/open-datasets/LCMAP/SCSTAB");
var sctime = ee.ImageCollection("projects/sat-io/open-datasets/LCMAP/SCTIME");
```

Sample code: https://code.earthengine.google.com/791aa894ce0abfe1a9eb1dc478bbc5d7

**I have also added the reference dataset to be used with the other 10 LCMAP products, which is about 25000 plot level datasets.**

```js
var reference = ee.FeatureCollection("projects/sat-io/open-datasets/LCMAP/LCMAP_CU_20200414_V01_REF");
```

Sample code: https://code.earthengine.google.com/729f0a1a2fa4e04f8c034b4228da164b

![reference_points](https://user-images.githubusercontent.com/6677629/132157362-a921f5bd-50b9-4cca-8746-7e8004eafb67.PNG)

#### Reference Publications: [Find additional publications here](https://www.usgs.gov/core-science-systems/eros/lcmap/publications)

* Brown, Jesslyn F., Heather J. Tollerud, Christopher P. Barber, Qiang Zhou, John L. Dwyer, James E. Vogelmann, Thomas R. Loveland et al. "Lessons learned implementing an operational continuous United States national land change monitoring capability: The Land Change Monitoring, Assessment, and Projection (LCMAP) approach." Remote Sensing of Environment 238 (2020): 111356.
* Zhu, Zhe, and Curtis E. Woodcock. "Continuous change detection and classification of land cover using all available Landsat data." Remote sensing of Environment 144 (2014): 152-171.
* Zhou, Qiang, Heather Tollerud, Christopher Barber, Kelcy Smith, and Daniel Zelenak. "Training data selection for annual land cover classification for the land change monitoring, assessment, and projection (LCMAP) initiative." Remote Sensing 12, no. 4 (2020): 699.
* Stehman, Stephen V., Bruce W. Pengra, Josephine A. Horton, and Danika F. Wellington. "Validation of the US Geological Survey's Land Change Monitoring, Assessment and Projection (LCMAP) Collection 1.0 annual land cover products 1985–2017." Remote Sensing of Environment 265 (2021): 112646.


#### License

LCMAP data are freely available to the public (similar to a CC0 license) and are generated by leveraging other national programs including the Landsat satellite program

Created by: U.S. Geological Survey Center for Earth Resources Observation and Science (EROS)

Curated by: Samapriya Roy

Keywords: Landsat, ARD, Land Cover, Spectral Change, USGS, EROS

Last updated: 2022-05-04

#### Changelog

USGS posted a notification for v1.2, so datasets were reprocessed and ingested

```
A processing issue was found in LCMAP Conterminous United States (CONUS) Collection 1.2 product mosaics in March 2022. The CONUS Collection 1.2 mosaics have been
reprocessed as of April 14, 2022, and users who downloaded CONUS Collection 1.2 mosaics before that date are encouraged to redownload the reprocessed data. CONUS
Collection 1.2 tiled data were unaffected and are available on EarthExplorer. LCMAP Conterminous United States (CONUS) Collection 1.2 products are available on
EarthExplorer, the LCMAP Web Viewer, and the LCMAP Mosaic Download website as of December 2021. CONUS Collection 1.2 includes LCMAP products for 1985-2020. Previous
LCMAP collections will remain available on EarthExplorer; however, user are encouraged to use the most recent release. LCMAP Hawaii (HI) Collection 1.0 products are also
available on EarthExplorer, the LCMAP Web Viewer, and the LCMAP Mosaic Download website as of January 2022. HI Collection 1.0 includes LCMAP products for 2000-2020.
```
