# Canadian Satellite-Based Forest Inventory (SBFI)

The Satellite-Based Forest Inventory (SBFI) provides information on Canada’s forested land cover, disturbance recovery, structure, species, and stand age in 2020, as well as stand-replacing disturbances from 1985-2020. The SBFI polygons represent homogeneous forest conditions similar to those of stands delineated in a strategic forest inventory. More than 25 million SBFI polygons were delineated using a multiresolution segmentation algorithm applied to the 2020 Landsat surface-reflectance BAP image composite (30-m spatial resolution), fire year, and harvest year layers derived from Landsat using the C2C approach. A minimum map unit of 0.45 ha (5 pixels) was used to define polygons. The entirety of Canada’s forest ecosystems were mapped using the same data, attributes, and temporal representation, resulting in a common vegetation inventory system of Canada’s ~650 Mha forested ecosystems. Given the large and diverse forest area of Canada, the strength of an SBFI lies in the use of a consistent data source and methodology across jurisdictional boundaries, and managed and unmanaged forest areas, enabling consistently generated synoptic, spatially explicit information outputs. The data included herein are based upon free and open satellite data and information products following established and communicated approaches.

Full descriptions of feature attributes are found within the attached data dictionary or within the [downloadable dataset found here](https://opendata.nfis.org/downloads/forest_change/CA_Forest_Satellite_Based_Inventory_2020.zip)

??? example "CA SBFI feature attributes"

    <center>

    | Group        | Field                              | Description                                                         | Units                |
    |--------------|------------------------------------|---------------------------------------------------------------------|----------------------|
    | ID           | ID                                 | Unique polygon identifier                                           |                      |
    |              | TILE                               | Tile identifier                                                     |                      |
    | Geometry     | AREA_HA                            | Area of the polygon                                                 | ha                   |
    |              | PERIMETER_M                        | Length of polygon’s boundary                                        | m                    |
    | Stratification | JURSDICTION                       | Most represented province/territory                                 |                      |
    |              | ECOZONE                            | Most represented terrestrial ecozone as defined by Ecological Stratification Working Group (1996) |                      |
    |              | ECOPROVINCE                        | Most represented ecoprovince as defined by Ecological Stratification Working Group (1996) |                      |
    |              | ECOREGION                          | Most represented ecoregion as defined by Ecological Stratification Working Group (1996) |                      |
    |              | MANAGEMENT                         | Most represented land status from the forest management classification from Stinson et al_ (2019) |                      |
    | Land cover   | LC_WATER                           | Area covered by water                                               | % of polygon area    |
    |              | LC_SNOW_ICE                        | Area covered by snow/ice                                            | % of polygon area    |
    |              | LC_ROCK_RUBBLE                     | Area covered by rock/rubble                                         | % of polygon area    |
    |              | LC_EXPOSED_BARREN                  | Area covered by exposed/barren land                                 | % of polygon area    |
    |              | LC_BRYOIDS                         | Area covered by bryoids                                             | % of polygon area    |
    |              | LC_SHRUBS                          | Area covered by shrubs                                              | % of polygon area    |
    |              | LC_WETLAND                         | Area covered by wetland                                             | % of polygon area    |
    |              | LC_WETLAND-TREED                   | Area covered by wetland-treed                                       | % of polygon area    |
    |              | LC_HERBS                           | Area covered by herbs                                               | % of polygon area    |
    |              | LC_CONIFEROUS                      | Area covered by coniferous                                          | % of polygon area    |
    |              | LC_BROADLEAF                       | Area covered by broadleaf                                           | % of polygon area    |
    |              | LC_MIXEDWOOD                       | Area covered by mixedwood                                           | % of polygon area    |
    |              | LC_TREED                           | Area covered by treed vegetation derived from combining the land cover classes | % of polygon area    |
    |              | LC_FAO_FOREST                      | Area covered by forest consistent with FAO definitions (Wulder et al_ 2020) | % of polygon area    |
    |              | LC_WETLAND_VEGETATION              | Area covered by wetlands derived from combining the land cover classes | % of polygon area    |
    | Disturbances | DISTURB_FIRE_PERC                 | Area impacted by fire disturbances                                  | % of polygon area    |
    |              | DISTURB_FIRE_YEAR                 | Modal year of fire disturbances                                     | years                |
    |              | DISTURB_FIRE_MAGNITUDE_MIN        | Minimum value of fire magnitude                                      | dNBR                 |
    |              | DISTURB_FIRE_MAGNITUDE_MAX        | Maximum value of fire magnitude                                      | dNBR                 |
    |              | DISTURB_FIRE_MAGNITUDE_AVG        | Average value of fire magnitude                                      | dNBR                 |
    |              | DISTURB_FIRE_MAGNITUDE_SD         | Standard deviation of fire magnitude                                | dNBR                 |
    |              | DISTURB_FIRE_MAGNITUDE_MED        | Median value of fire magnitude                                       | dNBR                 |
    |              | DISTURB_HARVEST_PERC              | Area impacted by harvesting disturbances                            | % of polygon area    |
    |              | DISTURB_HARVEST_YEAR              | Modal year of harvesting disturbances                                | years                |
    | Recovery     | RECOVERY_FIRE_MIN                 | Minimum value of spectral recovery for fire disturbances             | % of pre-disturbance |
    |              | RECOVERY_FIRE_MAX                 | Maximum value of spectral recovery for fire disturbances             | % of pre-disturbance |
    |              | RECOVERY_FIRE_AVG                 | Average value of spectral recovery for fire disturbances             | % of pre-disturbance |
    |              | RECOVERY_FIRE_SD                  | Standard deviation of spectral recovery for fire disturbances        | % of pre-disturbance |
    |              | RECOVERY_FIRE_MED                 | Median value of spectral recovery for fire disturbances              | % of pre-disturbance |
    |              | RECOVERY_HARVEST_MIN              | Minimum value of spectral recovery for harvesting disturbances      | % of pre-disturbance |
    |              | RECOVERY_HARVEST_MAX              | Maximum value of spectral recovery for harvesting disturbances      | % of pre-disturbance |
    |              | RECOVERY_HARVEST_AVG              | Average value of spectral recovery for harvesting disturbances      | % of pre-disturbance |
    |              | RECOVERY_HARVEST_SD               | Standard deviation of spectral recovery for harvesting disturbances | % of pre-disturbance |
    |              | RECOVERY_HARVEST_MED              | Median value of spectral recovery for harvesting disturbances       | % of pre-disturbance |
    | Age          | AGE_MIN                            | Minimum forest age                                                  | years                |
    |              | AGE_MAX                            | Maximum forest age                                                  | years                |
    |              | AGE_AVG                            | Average forest age                                                  | years                |
    |              | AGE_SD                             | Standard deviation of forest age                                    | years                |
    |              | AGE_MED                            | Median forest age                                                   | years                |
    |              | AGE_0_10, AGE_10_20, AGE_20_30, AGE_30_40, AGE_40_50, AGE_50_60, AGE_60_70, AGE_70_80, AGE_80_90, AGE_90_100, AGE_100_110, AGE_110_120, AGE_120_130, AGE_130_140, AGE_140_150, AGE_GT_150 | Ten-year age class frequency distribution | % of treed area in polygon |
    | Forest structure | STRUCTURE_CANOPY_HEIGHT_MIN     | Minimum canopy height                                               | m                    |
    |              | STRUCTURE_CANOPY_HEIGHT_MAX        | Maximum canopy height                                               | m                    |
    |              | STRUCTURE_CANOPY_HEIGHT_AVG        | Average canopy height                                               | m                    |
    |              | STRUCTURE_CANOPY_HEIGHT_SD         | Standard deviation of canopy height                                 | m                    |
    |              | STRUCTURE_CANOPY_HEIGHT_MED        | Median canopy height                                                | m                    |
    |              | STRUCTURE_CANOPY_COVER_MIN     | Minimum canopy cover                                               | %                    |
    |              | STRUCTURE_CANOPY_COVER_MAX        | Maximum canopy cover                                               | %                    |
    |              | STRUCTURE_CANOPY_COVER_AVG        | Average canopy cover                                               | %                    |
    |              | STRUCTURE_CANOPY_COVER_SD         | Standard deviation of canopy cover                                 | %                    |
    |              | STRUCTURE_CANOPY_COVER_MED        | Median canopy cover                                                | %                    |
    |              | STRUCTURE_LOREYS_HEIGHT_MIN        | Minimum Lorey’s height                                             | m                    |
    |              | STRUCTURE_LOREYS_HEIGHT_MAX        | Maximum Lorey’s height                                             | m                    |
    |              | STRUCTURE_LOREYS_HEIGHT_AVG        | Average Lorey’s height                                             | m                    |
    |              | STRUCTURE_LOREYS_HEIGHT_SD         | Standard deviation of Lorey’s height                               | m                    |
    |              | STRUCTURE_LOREYS_HEIGHT_MED        | Median Lorey’s height                                              | m                    |
    |              | STRUCTURE_BASAL_AREA_MIN           | Minimum basal area                                                 | m2 ha−1              |
    |              | STRUCTURE_BASAL_AREA_MAX           | Maximum basal area                                                 | m2 ha−1              |
    |              | STRUCTURE_BASAL_AREA_AVG           | Average basal area                                                 | m2 ha−1              |
    |              | STRUCTURE_BASAL_AREA_SD            | Standard deviation of basal area                                   | m2 ha−1              |
    |              | STRUCTURE_BASAL_AREA_MED           | Median basal area                                                  | m2 ha−1              |
    |              | STRUCTURE_BASAL_AREA_TOTAL         | Total basal area in polygon                                        | m2                   |
    |              | STRUCTURE_AGB_MIN                  | Minimum aboveground biomass                                        | t ha−1               |
    |              | STRUCTURE_AGB_MAX                  | Maximum aboveground biomass                                        | t ha−1               |
    |              | STRUCTURE_AGB_AVG                  | Average aboveground biomass                                        | t ha−1               |
    |              | STRUCTURE_AGB_SD                   | Standard deviation of aboveground biomass                          | t ha−1               |
    |              | STRUCTURE_AGB_MED                  | Median aboveground biomass                                         | t ha−1               |
    |              | STRUCTURE_AGB_TOTAL                | Total aboveground biomass in polygon                               | t                    |
    |              | STRUCTURE_VOLUME_MIN               | Minimum gross stem volume                                          | m3 ha−1              |
    |              | STRUCTURE_VOLUME_MAX               | Maximum gross stem volume                                          | m3 ha−1              |
    |              | STRUCTURE_VOLUME_AVG               | Average gross stem volume                                          | m3 ha−1              |
    |              | STRUCTURE_VOLUME_SD                | Standard deviation of gross stem volume                            | m3 ha−1              |
    |              | STRUCTURE_VOLUME_MED               | Median gross stem volume                                           | m3 ha−1              |
    |              | STRUCTURE_VOLUME_TOTAL             | Total gross stem volume in polygon                                 | m3                   |
    | Tree species | SPECIES_NUMBER                     |                                                                    |                      |
    |              | SPECIES_1                          | Name of the 1st most common leading tree species representing a percentage of treed area in polygon >2_5% |                      |
    |              | SPECIES_2                          | Name of the 2nd most common leading tree species representing a percentage of treed area in polygon >2_5% |                      |
    |              | SPECIES_3                          | Name of the 3rd most common leading tree species representing a percentage of treed area in polygon >2_5% |                      |
    |              | SPECIES_4                          | Name of the 4th most common leading tree species representing a percentage of treed area in polygon >2_5% |                      |
    |              | SPECIES_5                          | Name of the 5th most common leading tree species representing a percentage of treed area in polygon >2_5% |                      |
    |              | SPECIES_1_PERC                     | Area covered by the 1st most common leading tree species            | % of treed area in polygon |
    |              | SPECIES_2_PERC                     | Area covered by the 2nd most common leading tree species            | % of treed area in polygon |
    |              | SPECIES_3_PERC                     | Area covered by the 3rd most common leading tree species            | % of treed area in polygon |      | SPECIES_4_PERC                     | Area covered by the 4th most common leading tree species            | % of treed area in polygon |
    |              | SPECIES_5_PERC                     | Area covered by the 5th most common leading tree species            | % of treed area in polygon |
    |              | SPECIES_CONIFEROUS_PERC           | Area covered by coniferous tree species                             | % of treed area in polygon |
    |              | SPECIES_CML1                       | Name of the 1st most common tree species based on the class membership likelihood values |                      |
    |              | SPECIES_CML2                       | Name of the 2nd most common tree species based on the class membership likelihood values |                      |
    |              | SPECIES_CML3                       | Name of the 3rd most common tree species based on the class membership likelihood values |                      |
    |              | SPECIES_CML4                       | Name of the 4th most common tree species based on the class membership likelihood values |                      |
    |              | SPECIES_CML5                       | Name of the 5th most common tree species based on the class membership likelihood values |                      |
    |              | SPECIES_CML1_PERC                  | Distribution of the class membership likelihood values of the 1st most common tree species | % of class membership likelihood from treed pixels in polygon |
    |              | SPECIES_CML2_PERC                  | Distribution of the class membership likelihood values of the 2nd most common tree species | % of class membership likelihood from treed pixels in polygon |
    |              | SPECIES_CML3_PERC                  | Distribution of the class membership likelihood values of the 3rd most common tree species | % of class membership likelihood from treed pixels in polygon |
    |              | SPECIES_CML4_PERC                  | Distribution of the class membership likelihood values of the 4th most common tree species | % of class membership likelihood from treed pixels in polygon |
    |              | SPECIES_CML5_PERC                  | Distribution of the class membership likelihood values of the 5th most common tree species | % of class membership likelihood from treed pixels in polygon |
    |              | SPECIES_CML_CONIFEROUS_PERC       | Proportion of class membership likelihood values of coniferous tree species | % of class membership likelihood from treed pixels in polygon |
    |              | SPECIES_CML_ASSEMBLAGES           | Name of the tree species conforming an assemblage                   |                      |
    |              | SPECIES_CML_ASSEMBLAGES_PERC      | Proportion of class membership likelihood values conforming the assemblage | % of class membership likelihood from treed pixels in polygon |
    | Symbology    | SYMB_LAND_BASE_LEVEL              | Land base level classification based on the NFI land cover hierarchy (Wulder et al_ 2008) |                      |
    |              | SYMB_LAND_COVER_LEVEL             | Land cover level classification based on the NFI land cover hierarchy (Wulder et al_ 2008) |                      |
    |              | SYMB_VEGETATION_LEVEL             | Vegetation level classification based on the NFI land cover hierarchy (Wulder et al_ 2008) |                      |
    |              | SYMB_DISTURBANCE                  | Simplified coding for disturbance type and year                      |                      |
    |              | SYMB_RECOVERY                     | Simplified coding for spectral recovery                             |                      |
    |              | SYMB_AGE                          | Simplified coding for forest age                                    |                      |

    <center>

#### Dataset postprocessing

The tile datasets are merged into a single feature collection for ease of use. The grid file is kept as is for users to understand how the grids are created.

#### Citation

```
Wulder, Michael A., Txomin Hermosilla, Joanne C. White, Christopher W. Bater, Geordie Hobart, and Spencer C. Bronson. "Development and
implementation of a stand-level satellite-based forest inventory for Canada." Forestry: An International Journal of Forest Research (2024): cpad065.
```

#### Dataset Citation

```
Wulder, M.A., Hermosilla, T., White, J.C., Bater, C.W., Hobart, G., Bronson, S.C., 2024. Development and implementation of a stand-level
satellite-based forest inventory for Canada. Forestry: An International Journal of Forest Research. https://doi.org/10.1093/forestry/cpad065
```

![canada_sbif_random-small](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/a10443db-c554-4471-83b1-f0ffc0d0ab25)

#### Earth Engine Snippet

```js
var sbfi_merged = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/CA_SBFI/CA_SBFI_MERGED");
var grid_fe = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/CA_SBFI/GRID_forested_ecosystems");
var grid_labels = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/CA_SBFI/Grid_Labels");
```

Sample Code:  https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/CA-SBFI

#### License
This work is licensed under and freely available to the public under the [Open Government Licence - Canada](http://open.canada.ca/en/open-government-licence-canada).

Created by: Wulder et al. 2024

Curated in GEE by : Samapriya Roy

Keyworks: Landsat, land cover, change detection, forest structure, biomass; NFI

Last updated in GEE: 2024-08-29
