# Monitoring Trends in Burn Severity (MTBS) 1984-2019

Monitoring Trends in Burn Severity (MTBS) is an interagency program whose goal is to consistently map the burn severity and extent of large fires across all lands of the United States from 1984 to present. This includes all fires 1000 acres or greater in the western United States and 500 acres or greater in the eastern Unites States. The extent of coverage includes the continental U.S., Alaska, Hawaii and Puerto Rico.

The program is conducted by the U.S. Geological Survey Center for Earth Resources Observation and Science (EROS) and the USDA Forest Service Geospatial Technology and Applications Center (GTAC).

The two datasets included in this package include

* The fire occurrence location dataset is a vector point ESRI shapefile of the centroids of all currently completed MTBS fires occurring in the continental United States, Alaska, Hawaii and Puerto Rico.

* The burned area boundaries dataset is a vector polygon ESRI shapefile of the extent of the burned areas of all currently completed MTBS fires for the continental United States, Alaska, Hawaii and Puerto Rico.

You can read the MTBS overview [paper here](https://www.mtbs.gov/sites/default/files/inline-files/Eidenshink-final.pdf)

In the MTBS project (from the [FAQ page](https://www.mtbs.gov/faqs) ), "burn severity" refers specifically to fire effects on above-ground biomass. The definition is drawn from the reference: NWCG Glossary of Wildland Fire Terms and is based on the term Fire Severity, which is defined as: "Degree to which a site has been altered or disrupted by fire; loosely, a product of fire intensity and residence time."

The following additional statements further clarify the nature of the products developed by this project:

* Burn severity is a composite of first-order effects and second order effects that arise within one growing season.
* Burn severity relates principally to visible changes in living and non-living biomass, fire byproducts (scorch, char, ash), and soil exposure.
* Burn severity occurs on a gradient or ordinal scale.
* Burn severity is a mosaic of effects that occur within a fire perimeter.
* Longer term effects are controlled by variables that evolve after a fire and are beyond the scope of this program.
* Burn severity is mappable and remotely sensed data provide a measurement framework.

The area occurence layer is now part of [official GEE catalog offering, you can find it here](https://developers.google.com/earth-engine/datasets/catalog/USFS_GTAC_MTBS_burned_area_boundaries_v1)

### Paper citation

```
Eidenshink, Jeff, Brian Schwind, Ken Brewer, Zhi-Liang Zhu, Brad Quayle, and Stephen Howard. "
A project for monitoring trends in burn severity." Fire ecology 3, no. 1 (2007): 3-21.
```

#### MTBS Citation Target	Reference	Example

|Citation Target                              |Reference                                                                                   |Example                                                                                                                                                 |
|---------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
|General information from MTBS project website|Webpage Title. (revision date). MTBS Project Homepage. Available online: URL [Access Date]. |Monitoring Trends in Burn Severity. (2017, July - last revised). [MTBS Project Homepage, USDA Forest Service/U.S. Geological Survey]. Available online:http://mtbs.gov/[2017, July12] |                                                                                                                     |
|MTBS geospatial datasets                     |Webpage Title: Data product. (revision date). Agencies. Available online: URL [Access Date].|MTBS Data Access: Fire Level Geospatial Data. (2017, July - last revised). MTBS Project (USDA Forest Service/U.S. Geological Survey). Available online: http://mtbs.gov/direct-download [2017, July12] |                                                                                                     |
|MTBS project reports                         |Report compiler. Publication date. Report title. Available online: URL.                     |Schwind, B. (compiler). 2008. Monitoring Trends in Burn Severity: Report on the PNW & PSW Fires—1984 to 2005. Available online: http://mtbs.gov/.       |

![mtbs](https://user-images.githubusercontent.com/6677629/132140559-611df45d-4073-4ebe-a1cc-c490b8ca873b.gif)

#### Earth Engine Snippet

```js
var area_boundaries = ee.FeatureCollection("projects/sat-io/open-datasets/MTBS/burned_area_boundaries");
var fire_occurrence = ee.FeatureCollection("projects/sat-io/open-datasets/MTBS/fire_occurrence");
```

Sample code: https://code.earthengine.google.com/0f71c9417a141c674c8dbf55f60a6f65


#### License

MTBS data are freely available to the public (similar to a CC0 license) and are generated by leveraging other national programs including the Landsat satellite program, jointly developed and managed by the USGS and NASA. Landsat data are analyzed through a standardized and consistent methodology, generating products at a 30 meter resolution dating back to 1984.

Created by: U.S. Geological Survey Center for Earth Resources Observation and Science (EROS) and the USDA Forest Service Geospatial Technology and Applications Center (GTAC)

Curated by: Samapriya Roy

Keywords: burned area,fire occurrence, fire area, burn severity,MTBS, EROS, GTAC, USGS, USDA

Last updated: 2021-09-05
