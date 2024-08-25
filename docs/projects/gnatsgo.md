# gNATSGO (gridded National Soil Survey Geographic Database)

???+ note

    **This dataset will be updated in batches owing to the extent and size of the image collections. These will be made available primarily in the insiders only dataset while they are ingested and tested. Once all raster collections have been ingested this will be made available to all users of the community catalog**

The gNATSGO (gridded National Soil Survey Geographic Database) database is a composite database that provides complete coverage of the best available soils information for all areas of the United States and Island Territories. This collection is sourced for the raster data only. Since the original format of the data is proprietary the source COGs are sourced from Planetary Computer STAC catalog.

The gNATSGO database was created by combining data from three sources: the Soil Survey Geographic Database (SSURGO), State Soil Geographic Database (STATSGO2), and Raster Soil Survey Databases (RSS). SSURGO is a USDA-NRCS Soil & Plant Science Division (SPSD) flagship soils database that has over 100 years of field-validated detailed soil mapping data. SSURGO contains soils information for more than 90 percent of the United States and island territories, but unmapped land remains.

STATSGO2 is a general soil map that has soils data for all of the United States and island territories, but the data is not as detailed as the SSURGO data. The Raster Soil Surveys (RSSs) are next-generation soil survey databases developed using advanced digital soil mapping methods. The gNATSGO database is composed primarily of SSURGO data, with STATSGO2 data used to fill in the gaps. The RSSs were merged into the gNATSGO after combining the SSURGO and STATSGO2 data. The extent of RSS is relatively limited at this time but is expected to increase in the coming years. To use the map unit values contained in the mukey raster asset, you will need to join to tables represented as Items in the gNATSGO Tables Collection. Many items have commonly used values encoded in additional raster assets.

??? example "Expand to show current asset collections"

    <center>

    | Titles       | STAC Key     | Roles | Description |
    |--------------|--------------|-------|-------------|
    | Aws0_5       | aws0_5       | Data  | Available water storage estimate (AWS) in a standard zone 1 (0-5 cm depth), expressed in mm. The volume of plant available water that the soil can store in this layer based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Aws0_20      | aws0_20      | Data  | Available water storage estimate (AWS) in standard zone 2 (0-20 cm depth), expressed in mm. The volume of plant available water that the soil can store in this zone based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Aws0_30      | aws0_30      | Data  | Available water storage estimate (AWS) in standard zone 3 (0-30 cm depth), expressed in mm. The volume of plant available water that the soil can store in this zone based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Aws0_100     | aws0_100     | Data  | Available water storage estimate (AWS) in standard zone 4 (0-100 cm depth), expressed in mm. The volume of plant available water that the soil can store in this zone based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Aws0_150     | aws0_150     | Data  | Available water storage estimate (AWS) in standard zone 5 (0-150 cm depth), expressed in mm. The volume of plant available water that the soil can store in this zone based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Aws0_999     | aws0_999     | Data  | Available water storage estimate (AWS) in total soil profile (0 cm to the reported depth of the soil profile), expressed in mm. The volume of plant available water that the soil can store in this layer based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Aws5_20      | aws5_20      | Data  | Available water storage estimate (AWS) in standard layer 2 (5-20 cm depth), expressed in mm. The volume of plant available water that the soil can store in this layer based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Aws20_50     | aws20_50     | Data  | Available water storage estimate (AWS) in standard layer 3 (20-50 cm depth), expressed in mm. The volume of plant available water that the soil can store in this layer based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Aws50_100    | aws50_100    | Data  | Available water storage estimate (AWS) in standard layer 4 (50-100 cm depth), expressed in mm. The volume of plant available water that the soil can store in this layer based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Aws100_150   | aws100_150   | Data  | Available water storage estimate (AWS) in standard layer 5 (100-150 cm depth), expressed in mm. The volume of plant available water that the soil can store in this layer based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Aws150_999   | aws150_999   | Data  | Available water storage estimate (AWS) in standard layer 6 (150 cm to the reported depth of the soil profile), expressed in mm. The volume of plant available water that the soil can store in this layer based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Soc0_5       | soc0_5       | Data  | Soil organic carbon stock estimate (SOC) in standard zone 1 (0-5 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter to a depth of 5 cm. NULL values are presented where data are incomplete or not available. |
    | Soc0_20      | soc0_20      | Data  | Soil organic carbon stock estimate (SOC) in standard zone 2 (0-20 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter to a depth of 20 cm. NULL values are presented where data are incomplete or not available. |
    | Soc0_30      | soc0_30      | Data  | Soil organic carbon stock estimate (SOC) in standard zone 3 (0-30 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter to a depth of 30 cm. NULL values are presented where data are incomplete or not available. |
    | Soc0_100     | soc0_100     | Data  | Soil organic carbon stock estimate (SOC) in a standard zone (0-100 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter to a depth of 100 cm. NULL values are presented where data are incomplete or not available. |
    | Soc0_150     | soc0_150     | Data  | Soil organic carbon stock estimate (SOC) in a standard zone (0-150 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter to a depth of 150 cm. NULL values are presented where data are incomplete or not available. |
    | Soc0_999     | soc0_999     | Data  | Soil organic carbon stock estimate (SOC) in a standard zone (0-999 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter to a depth of 999 cm. NULL values are presented where data are incomplete or not available. |
    | Soc100_150   | soc100_150   | Data  | Soil organic carbon stock estimate (SOC) in a standard zone (100-150 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter between 100 and 150 cm depth. NULL values are presented where data are incomplete or not available. |
    | Soc150_999   | soc150_999   | Data  | Soil organic carbon stock estimate (SOC) in a standard zone (150-999 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter between 150 and 999 cm depth. NULL values are presented where data are incomplete or not available. |
    | Soc20_50     | soc20_50     | Data  | Soil organic carbon stock estimate (SOC) in a standard zone (20-50 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter between 20 and 50 cm depth. NULL values are presented where data are incomplete or not available. |
    | Soc50_100    | soc50_100    | Data  | Soil organic carbon stock estimate (SOC) in a standard zone (50-100 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter between 50 and 100 cm depth. NULL values are presented where data are incomplete or not available. |
    | Soc5_20      | soc5_20      | Data  | Soil organic carbon stock estimate (SOC) in a standard zone (5-20 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter between 5 and 20 cm depth. NULL values are presented where data are incomplete or not available. |
    | Mukey        | mukey        | Data  | Map unit key is the unique identifier of a record in the Mapunit table. Use this column to join the Component table to the Map Unit table and the Valu1 table to the MapUnitRaster_10m raster map layer to map valu1 themes. |



    </center>

![gnatsgo](https://github.com/user-attachments/assets/ac9e4dc1-2b05-48cd-aaf7-914120a865ca)

#### Earth Engine Snippet

```js
var aws0_100 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/aws0_100');
var aws0_150 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/aws0_150');
var aws0_20 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/aws0_20');
var aws0_30 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/aws0_30');
var aws0_5 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/aws0_5');
var aws0_999 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/aws0_999');
var aws100_150 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/aws100_150');
var aws150_999 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/aws150_999');
var aws20_50 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/aws20_50');
var aws50_100 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/aws50_100');
var aws5_20 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/aws5_20');
var mukey = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/mukey');
var soc0_100 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/soc0_100');
var soc0_150 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/soc0_150');
var soc0_20 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/soc0_20');
var soc0_30 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/soc0_30');
var soc0_5 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/soc0_5');
var soc0_999 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/soc0_999');
var soc100_150 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/soc100_150');
var soc150_999 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/soc150_999');
var soc20_50 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/soc20_50');
var soc50_100 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/soc50_100');
var soc5_20 = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/soc5_20');
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:soil-properties/gNATSGO-DATABASE

#### License

The data from the Gridded National Soil Survey Geographic Database (gNATSGO) provided by the USDA Natural Resources Conservation Service (NRCS) is available under the Public Domain license (CC0 1.0 Universal Public Domain Dedication).

Provided by: United States Department of Agriculture, Natural Resources Conservation Service

Hosted by: Microsoft

Curated in GEE by: Samapriya Roy

Keywords: Soil Survey, USDA, NRCS, Raster Data, Gridded Data

Last updated: 2024-08-25

#### Changelog
- Added SOC Layers



