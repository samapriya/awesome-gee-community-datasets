# gNATSGO (gridded National Soil Survey Geographic Database)

The gNATSGO (gridded National Soil Survey Geographic Database) database is a composite database that provides complete coverage of the best available soils information for all areas of the United States and Island Territories. This collection is sourced for the raster data only. Since the original format of the data is proprietary the source COGs are sourced from Planetary Computer STAC catalog.

The gNATSGO database was created by combining data from three sources: the Soil Survey Geographic Database (SSURGO), State Soil Geographic Database (STATSGO2), and Raster Soil Survey Databases (RSS). SSURGO is a USDA-NRCS Soil & Plant Science Division (SPSD) flagship soils database that has over 100 years of field-validated detailed soil mapping data. SSURGO contains soils information for more than 90 percent of the United States and island territories, but unmapped land remains.

STATSGO2 is a general soil map that has soils data for all of the United States and island territories, but the data is not as detailed as the SSURGO data. The Raster Soil Surveys (RSSs) are next-generation soil survey databases developed using advanced digital soil mapping methods. The gNATSGO database is composed primarily of SSURGO data, with STATSGO2 data used to fill in the gaps. The RSSs were merged into the gNATSGO after combining the SSURGO and STATSGO2 data. The extent of RSS is relatively limited at this time but is expected to increase in the coming years. To use the map unit values contained in the mukey raster asset, you will need to join to tables represented as Items in the gNATSGO Tables Collection. Many items have commonly used values encoded in additional raster assets.

??? example "Expand to show current asset collections"

    <center>

    | Titles | STAC Key | Roles | Description |
    |---|---|---|---|
    | Aws0_5 | aws0_5 | Data | Available water storage estimate (AWS) in a standard zone 1 (0-5 cm depth), expressed in mm. The volume of plant available water that the soil can store in this layer based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Aws0_20 | aws0_20 | Data | Available water storage estimate (AWS) in standard zone 2 (0-20 cm depth), expressed in mm. The volume of plant available water that the soil can store in this zone based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Aws0_30 | aws0_30 | Data | Available water storage estimate (AWS) in standard zone 3 (0-30 cm depth), expressed in mm. The volume of plant available water that the soil can store in this zone based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Aws0_100 | aws0_100 | Data | Available water storage estimate (AWS) in standard zone 4 (0-100 cm depth), expressed in mm. The volume of plant available water that the soil can store in this zone based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Aws0_150 | aws0_150 | Data | Available water storage estimate (AWS) in standard zone 5 (0-150 cm depth), expressed in mm. The volume of plant available water that the soil can store in this zone based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Aws0_999 | aws0_999 | Data | Available water storage estimate (AWS) in total soil profile (0 cm to the reported depth of the soil profile), expressed in mm. The volume of plant available water that the soil can store in this layer based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Aws5_20 | aws5_20 | Data | Available water storage estimate (AWS) in standard layer 2 (5-20 cm depth), expressed in mm. The volume of plant available water that the soil can store in this layer based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Aws20_50 | aws20_50 | Data | Available water storage estimate (AWS) in standard layer 3 (20-50 cm depth), expressed in mm. The volume of plant available water that the soil can store in this layer based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Aws50_100 | aws50_100 | Data | Available water storage estimate (AWS) in standard layer 4 (50-100 cm depth), expressed in mm. The volume of plant available water that the soil can store in this layer based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Aws100_150 | aws100_150 | Data | Available water storage estimate (AWS) in standard layer 5 (100-150 cm depth), expressed in mm. The volume of plant available water that the soil can store in this layer based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Aws150_999 | aws150_999 | Data | Available water storage estimate (AWS) in standard layer 6 (150 cm to the reported depth of the soil profile), expressed in mm. The volume of plant available water that the soil can store in this layer based on all map unit components (weighted average). NULL values are presented where data are incomplete or not available. |
    | Soc0_5 | soc0_5 | Data | Soil organic carbon stock estimate (SOC) in standard zone 1 (0-5 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter to a depth of 5 cm. NULL values are presented where data are incomplete or not available. |
    | Soc0_20 | soc0_20 | Data | Soil organic carbon stock estimate (SOC) in standard zone 2 (0-20 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter to a depth of 20 cm. NULL values are presented where data are incomplete or not available. |
    | Soc0_30 | soc0_30 | Data | Soil organic carbon stock estimate (SOC) in standard zone 3 (0-30 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter to a depth of 30 cm. NULL values are presented where data are incomplete or not available. |
    | Soc0_100 | soc0_100 | Data | Soil organic carbon stock estimate (SOC) in a standard zone (0-100 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter to a depth of 100 cm. NULL values are presented where data are incomplete or not available. |
    | Soc0_150 | soc0_150 | Data | Soil organic carbon stock estimate (SOC) in a standard zone (0-150 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter to a depth of 150 cm. NULL values are presented where data are incomplete or not available. |
    | Soc0_999 | soc0_999 | Data | Soil organic carbon stock estimate (SOC) in a standard zone (0-999 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter to a depth of 999 cm. NULL values are presented where data are incomplete or not available. |
    | Soc100_150 | soc100_150 | Data | Soil organic carbon stock estimate (SOC) in a standard zone (100-150 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter between 100 and 150 cm depth. NULL values are presented where data are incomplete or not available. |
    | Soc150_999 | soc150_999 | Data | Soil organic carbon stock estimate (SOC) in a standard zone (150-999 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter between 150 and 999 cm depth. NULL values are presented where data are incomplete or not available. |
    | Soc20_50 | soc20_50 | Data | Soil organic carbon stock estimate (SOC) in a standard zone (20-50 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter between 20 and 50 cm depth. NULL values are presented where data are incomplete or not available. |
    | Soc50_100 | soc50_100 | Data | Soil organic carbon stock estimate (SOC) in a standard zone (50-100 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter between 50 and 100 cm depth. NULL values are presented where data are incomplete or not available. |
    | Soc5_20 | soc5_20 | Data | Soil organic carbon stock estimate (SOC) in a standard zone (5-20 cm depth). The concentration of organic carbon present in the soil expressed in grams C per square meter between 5 and 20 cm depth. NULL values are presented where data are incomplete or not available. |
    | Mukey | mukey | Data | Map unit key is the unique identifier of a record in the Mapunit table. Use this column to join the Component table to the Map Unit table and the Valu1 table to the MapUnitRaster_10m raster map layer to map valu1 themes. |
    | Droughty | droughty | Data | Zone for commodity crops that is less than or equal to 6 inches (152 mm) expressed as “1” for a drought vulnerable soil landscape map unit or “0” for a non-droughty soil landscape map unit or NULL for miscellaneous areas (includes water bodies) or where data were not available. |
    | Nccpi3sg | nccpi3sg | Data | National Commodity Crop Productivity Index for Small Grains (weighted average) for major earthy components. Values range from .01 (low productivity) to .99 (high productivity). NULL values are presented where data are incomplete or not available. |
    | Tk0_100a | tk0_100a | Data | Thickness of soil components used in standard zone 4 (0-100 cm) expressed in cm (weighted average) for the available water storage calculation. NULL values are presented where data are incomplete or not available. |
    | Tk0_100s | tk0_100s | Data | Thickness of soil components used in standard zone 4 (0-100 cm) expressed in cm (weighted average) for the Soil Organic Carbon calculation. NULL values are presented where data are incomplete or not available. |
    | Tk0_150a | tk0_150a | Data | Thickness of soil components used in standard zone 5 (0-150 cm) expressed in cm (weighted average) for the available water storage calculation. NULL values are presented where data are incomplete or not available. |
    | Tk0_150s | tk0_150s | Data | Thickness of soil components used in standard zone 5 (0-150 cm) expressed in cm (weighted average) for the Soil Organic Carbon calculation. NULL values are presented where data are incomplete or not available. |
    | Tk0_999a | tk0_999a | Data | Thickness of soil components used in total soil profile (0 cm to the reported depth of the soil profile) expressed in cm (weighted average) for the available water storage calculation. NULL values are presented where data are incomplete or not available. |
    | Tk0_999s | tk0_999s | Data | Thickness of soil components used in total soil profile (0 cm to the reported depth of the soil profile) expressed in cm (weighted average) for the Soil Organic Carbon calculation. NULL values are presented where data are incomplete or not available. |
    | Tk20_50a | tk20_50a | Data | Thickness of soil components used in standard layer 3 (20-50 cm) expressed in cm (weighted average) for the available water storage calculation. NULL values are presented where data are incomplete or not available. |
    | Tk20_50s | tk20_50s | Data | Thickness of soil components used in standard layer 3 (20-50 cm) expressed in cm (weighted average) for the Soil Organic Carbon calculation. NULL values are presented where data are incomplete or not available. |
    | Musumcpct | musumcpct | Data | The sum of the comppct_r (SSURGO component table) values for all listed components in the map unit. NULL values are presented where data are incomplete or not available. |
    | Nccpi3all | nccpi3all | Data | National Commodity Crop Productivity Index that has the highest value among Corn and Soybeans, Small Grains, or Cotton (weighted average) for major earthy components. NULL values are presented where data are incomplete or not available. |
    | Nccpi3cot | nccpi3cot | Data | National Commodity Crop Productivity Index for Cotton (weighted average) for major earthy components. NULL values are presented where data are incomplete or not available. |
    | Nccpi3soy | nccpi3soy | Data | National Commodity Crop Productivity Index for Soybeans (weighted average) for major earthy components. NULL values are presented where data are incomplete or not available. |
    | Pwsl1pomu | pwsl1pomu | Data | Potential Wetland Soil Landscapes (PWSL) is expressed as the percentage of the map unit that meets the PWSL criteria. NULL values are presented where data are incomplete or not available. |
    | Rootznaws | rootznaws | Data | Root zone available water storage estimate (RZAWS), expressed in mm, is the volume of plant available water that the soil can store within the root zone. NULL values are presented where data are incomplete or not available. |
    | Rootznemc | rootznemc | Data | Root zone depth is the depth within the soil profile that commodity crop roots can effectively extract water and nutrients for growth. NULL values are presented where data are incomplete or not available. |
    | Tk50_100a | tk50_100a | Data | Thickness of soil components used in standard layer 4 (50-100 cm) expressed in cm (weighted average) for the available water storage calculation. NULL values are presented where data are incomplete or not available. |
    | Tk50_100s | tk50_100s | Data | Thickness of soil components used in standard layer 4 (50-100 cm) expressed in cm (weighted average) for the Soil Organic Carbon calculation. NULL values are presented where data are incomplete or not available. |
    | Musumcpcta | musumcpcta | Data | The sum of the comppct_r (SSURGO component table) values used in the available water storage calculation for the map unit. NULL values are presented where data are incomplete or not available. |
    | Musumcpcts | musumcpcts | Data | The sum of the comppct_r (SSURGO component table) values used in the soil organic carbon calculation for the map unit. NULL values are presented where data are incomplete or not available. |
    | Nccpi3corn | nccpi3corn | Data | National Commodity Crop Productivity Index for Corn (weighted average) for major earthy components. NULL values are presented where data are incomplete or not available. |
    | Pctearthmc | pctearthmc | Data | The National Commodity Crop Productivity Index map unit percent earthy is the map unit summed comppct_r for major earthy components. NULL values are presented where data are incomplete or not available. |
    | Tk100_150a | tk100_150a | Data | Thickness of soil components used in standard layer 5 (100-150 cm) expressed in cm (weighted average) for the available water storage calculation. NULL values are presented where data are incomplete or not available. |
    | Tk100_150s | tk100_150s | Data | Thickness of soil components used in standard layer 5 (100-150 cm) expressed in cm (weighted average) for the Soil Organic Carbon calculation. NULL values are presented where data are incomplete or not available. |
    | Tk150_999a | tk150_999a | Data | Thickness of soil components used in standard layer 6 (150 cm to the reported depth of the soil profile) expressed in cm (weighted average) for the available water storage calculation. NULL values are presented where data are incomplete or not available. |
    | Tk150_999s | tk150_999s | Data | Thickness of soil components used in standard layer 6 (150 cm to the reported depth of the soil profile) expressed in cm (weighted average) for the Soil Organic Carbon calculation. NULL values are presented where data are incomplete or not available. |

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
var droughty = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/droughty');
var musumcpct = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/musumcpct');
var musumcpcta = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/musumcpcta');
var musumcpcts = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/musumcpcts');
var nccpi3all = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/nccpi3all');
var nccpi3corn = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/nccpi3corn');
var nccpi3cot = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/nccpi3cot');
var nccpi3sg = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/nccpi3sg');
var nccpi3soy = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/nccpi3soy');
var pctearthmc = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/pctearthmc');
var pwsl1pomu = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/pwsl1pomu');
var rootznaws = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/rootznaws');
var rootznemc = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/rootznemc');
var tk0_100a = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/tk0_100a');
var tk0_100s = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/tk0_100s');
var tk0_150a = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/tk0_150a');
var tk0_150s = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/tk0_150s');
var tk0_20a = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/tk0_20a');
var tk0_20s = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/tk0_20s');
var tk0_30a = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/tk0_30a');
var tk0_30s = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/tk0_30s');
var tk0_5a = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/tk0_5a');
var tk0_5s = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/tk0_5s');
var tk0_999a = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/tk0_999a');
var tk0_999s = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/tk0_999s');
var tk100_150a = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/tk100_150a');
var tk100_150s = ee.ImageCollection('projects/sat-io/open-datasets/gNATSGO/raster/tk100_150s');
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:soil-properties/gNATSGO-DATABASE

#### License

The data from the Gridded National Soil Survey Geographic Database (gNATSGO) provided by the USDA Natural Resources Conservation Service (NRCS) is available under the Public Domain license (CC0 1.0 Universal Public Domain Dedication).

Provided by: United States Department of Agriculture, Natural Resources Conservation Service

Hosted by: Microsoft

Curated in GEE by: Samapriya Roy

Keywords: Soil Survey, USDA, NRCS, Raster Data, Gridded Data

Last updated: 2024-10-22

#### Changelog

- All layers added and dataset is now generally available
- Added SOC Layers



