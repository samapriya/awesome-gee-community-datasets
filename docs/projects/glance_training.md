# GLANCE Global Landcover Training dataset

The GLanCE training dataset, available to the public, is designed for regional-to-global land cover and land cover change analyses. With a medium spatial resolution of 30 meters, it spans the years 1984 to 2020 and is geographically and spectrally representative of all global ecoregions. Offering up to 23 land cover characteristics per training unit, it provides a harmonized, standardized, and comprehensive database that includes information on abrupt and gradual land cover change processes, particularly spanning up to 36 years in select regions. The dataset's adaptability allows users to sub-sample and customize it based on their study region, classification algorithm, and desired classification legend, making it a versatile resource for in-depth land cover investigations. You can read about the dataset in the [paper here](https://www.nature.com/articles/s41597-023-02798-5)

| Column Name             | Description                                                                                                                                                                         |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Lat                     | Latitude                                                                                                                                                                             |
| Lon                     | Longitude                                                                                                                                                                            |
| Start_Year              | Start year of segment, ranging from 1984 to 2020 (integer)                                                                                                                          |
| End_Year                | End year of segment, ranging from 1984 to 2020 (integer)                                                                                                                            |
| Glance_Class_ID_level1  | Level 1 land cover value (integer): 1 (Water), 2 (Ice/snow), 3 (Developed), 4 (Barren/sparsely vegetated), 5 (Trees), 6 (Shrub), and 7 (Herbaceous)                             |
| Glance_Class_ID_level2  | Level 2 land cover value (integer): 1 (Water), 2 (Ice/snow), 3 (Developed), 4 (Soil), 5 (Rock), 6 (Beach/sand), 7 (Deciduous), 8 (Evergreen), 9 (Mixed), 10 (Shrub), 11 (Grassland), 12 (Agriculture), and 13 (Moss/lichen). NaN values present. |
| Leaf_Type               | Tree leaf type: broadleaf (1), needleleaf (2), and mixed (3). NaN values present.                                                                                                   |
| Impervious_Percent      | Impervious percent for developed samples: low 0%-30% (1), medium 30%-60% (2), and high 60%-100% (3). NaN values present.                                                             |
| Tree_Location           | Binary integer indicating whether trees are on the interior (0) or edge (1) of a forest. NaN values present.                                                                        |
| Veg_Density             | Vegetation density for trees and shrubs: sparse 0%-30% (1), open 30%-60% (2), and closed 60%-100% (3). NaN values present.                                                           |
| Veg_Modifier            | Vegetation modifiers, which can include one or more of the following: Cropland, Plantation, Wetland, Riparian/Flood, Mangrove, Greenhouse, and Trees/Shrub Present. NaN values present.                                                     |
| Segment_Type            | Indicates whether a segment is stable (0) or transitional (1). See Section 1 for a detailed description. Land cover for transitional segments is recorded at both the beginning and end of the time segment - typically the first and last three years. NaN values present. |
| Change                  | Indicates presence (1) or absence (0) of land cover change for Level 1 land cover labels. Includes both abrupt change and gradual change (transitional segments (1) from the Segment_Type attribute) if it happened at any time for that training unit. |
| LC_Confidence           | Interpreter confidence in the Level 1 land cover label from 1 (lowest) to 3 (highest). NaN values present.                                                                          |
| Level1_Ecoregion        | Ecoregion Level 1 number based on World Wildlife Fund definitions. For North America we used ecoregions based on the Environmental Protection Agency’s Ecoregions of North America product.                                                      |
| Level2_Ecoregion        | Ecoregion Level 2 number based on the Environmental Protection Agency’s Ecoregions of North America product. This field is available only for North America and is assigned a value of 0 for all other continents.                          |
| Continent_Code          | Assigned continent number: North America (1), South America (2), Africa (3), Europe (4), Asia (5), and Oceania (6).                                                                  |
| Dataset_Code            | Assigned dataset number: 1, 2, 3, 4, 5, 902, 999, 700, 701, 702, 703, 704, 705, 706, and 707. Numbers correspond to each Dataset as follows: STEP, CLUSTERING, LCMAP, ABoVE, MapBiomas, Feedback, Training_augment, MODIS_algo, GeoWiki, RadEarth, Collaborator_data, BU_team_collected, GLC30, LUCAS, ASB_crop. For details see Scientific Data publication. |
| Glance_ID               | Unique ID for each sample.                                                                                                                                                          |
| ID                      | ID for each unique combination of latitude and longitude. Change units have the same ID but different Glance_ID.                                                                    |

??? example "Expand to show Glance Training Level descriptors"

    <center>

    | Level 1                       | Level 2          | Description                                                                                                                                                                           |
    | ----------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Water (1)                     | Water (1)        | Areas covered with water throughout the year: streams, canals, lakes, reservoirs, oceans.                                                                                             |
    | Ice/snow (2)                  | Ice/snow (2)     | Land areas with snow and ice cover greater than 50% throughout the year.                                                                                                              |
    | Developed (3)                 | Developed (3)    | Areas of intensive use; land covered with structures, including any land functionally related to developed/built-up activity.                                                         |
    | Barren/sparsely vegetated (4) |                  | Land comprised of natural occurrences of soils, sand, or rocks where less than 10% of the area is vegetated.                                                                          |
    |                               | Soil (4)         | Land covered with less than 10% vegetation and dominated by soil.                                                                                                                     |
    |                               | Rock (5)         | Land covered with less than 10% vegetation and dominated by rocks.                                                                                                                    |
    |                               | Beach/sand (6)   | Land covered with less than 10% vegetation and dominated by beach/sand.                                                                                                               |
    | Trees (5)                     |                  | Land where tree cover is greater than 30%. Note that cleared trees (i.e., clear-cuts) are mapped according to current cover (e.g., barren/sparsely vegetated, shrubs, or herbaceous). |
    |                               | Deciduous (7)    | Land with tree cover greater than 30% and all trees present are deciduous.                                                                                                            |
    |                               | Evergreen (8)    | Land with tree cover greater than 30% and all trees present are evergreen.                                                                                                            |
    |                               | Mixed (9)        | Land with tree cover greater than 30% and neither deciduous nor evergreen trees dominate.                                                                                             |
    | Shrub (6)                     | Shrub (10)       | Land with less than 30% tree cover, where total vegetation cover exceeds 10% and shrub cover is greater than 10%.                                                                     |
    | Herbaceous (7)                |                  | Land covered by herbaceous plants. Total vegetation cover exceeds 10%, tree cover is less than 30%, and shrubs comprise less than 10% of the area.                                    |
    |                               | Grassland (11)   | Herbaceous land covered with grass.                                                                                                                                                   |
    |                               | Agriculture (12) | Herbaceous land covered with cultivated cropland.                                                                                                                                     |
    |                               | Moss/lichen (13) | Herbaceous land covered with lichen and/or moss.                                                                                                                                      |

    <center>

#### Citation

```
Stanimirova, R., Tarrio, K., Turlej, K., McAvoy K., Stonebrook S., Hu K-T., Arévalo P., Bullock E.L., Zhang Y., Woodcock C.E., Olofsson P., Zhu Z.,
Barber C.P., Souza C., Chen S., Wang J.A., Mensah F., Calderón-Loor M., Hadjikakou M., Bryan B.A., Graesser J., Beyene D.L., Mutasha B., Siame S.,
Siampale A., and M.A. Friedl (2023) A global land cover training dataset from 1984 to 2020. Sci Data 10, 879
https://doi.org/10.1038/s41597-023-02798-5
```

#### Dataset Citation

```
Stanimirova R., Tarrio K., Turlej K., McAvoy K., Stonebrook S., Hu K-T., Arévalo P., Bullock E.L., Zhang Y., Woodcock C.E., Olofsson P., Zhu Z.,
Barber C.P., Souza C., Chen S., Wang J.A., Mensah F., Calderón-Loor M., Hadjikakou M., Bryan B.A., Graesser J., Beyene D.L., Mutasha B., Siame S.,
Siampale A., and M.A. Friedl (2023) "A Global Land Cover Training Dataset from 1984 to 2020", Version 1.0, Radiant MLHub. [Date Accessed]
https://doi.org/10.34911/rdnt.x4xfh3
```

![glance_training](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/7fd24f73-9dce-4f93-a309-589ffd5c1f3b)

#### Earth Engine Snippet

```js
var glance_training = ee.FeatureCollection("projects/sat-io/open-datasets/GLANCE/GLANCE_TRAINING_DATA_V1")
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/GLANCE-TRAINING

#### License

The dataset is provided under a Creative Commons Attribution 4.0 International Public License, unless otherwise noted.

Created by: Stanimirova et al, Boston University

Curated in GEE by: Samapriya Roy

Keywords: Glance, LULC, training dataset, Medium resolution, global dataset, land use, land cover

Last updated in GEE: 2024-01-02
