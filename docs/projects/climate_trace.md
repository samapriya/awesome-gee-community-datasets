# Climate Trace Global Emissions Data
Climate TRACE is a non-profit coalition that has unveiled an open emissions database containing more than 352 million assets. The database provides a comprehensive accounting of greenhouse gas (GHG) emissions based primarily on direct, independent observation. It includes every country and territory in the world and covers various emitting activities such as energy production, industrial processes, and land use. The data are derived from satellites, remote sensing, and other public and commercial sources, making it the most comprehensive and granular dataset of recent GHG emissions ever created. The inventory allows for transparent assessment of each country's progress toward emission reduction goals.

For more detailed information, you can visit the Climate TRACE website at [climatetrace.org](https://climatetrace.org).

#### Dataset preprocessing

The downloaded datasets were processed to get system:time_start and system:time_end in epoch time and these were added to the data column in GEE. Each sector and their associated emissions dataset sources were processed providing 38,731,650 total features. Not all sectors had emissions locations and some were provided only at a country level.

#### Citation

```
Climate TRACE - Tracking Realtime Atmospheric Carbon Emissions (2022), Climate TRACE Emissions Inventory,
https://climatetrace.org [Date Accessed].
```

For individual sectors refer to citation information from the downloads page.

#### Metadata Descriptors

??? example "Expand to show data attributes and definitions for the emissions database"

    <center>

    | Data-attribute            | Definition                                                                                                        |
    | ------------------------- | ----------------------------------------------------------------------------------------------------------------- |
    | source_id                 | The internal Climate TRACE identifier for each individual source of emissions.                                    |
    | source_name               | Name of the entity or source that produced the emissions.                                                         |
    | source_type               | Description of the emission source classification.                                                                |
    | iso3_country              | Corresponds to the ISO 3166-1 alpha-3 specification of the country where the entity is physically located.        |
    | original_inventory_sector | Intergovernmental Panel on Climate Change (IPCC) emissions sector to which the emissions source belongs.          |
    | start_time                | The time using Coordinated Universal Time (UTC) of emissions, either as an instance of start time of observation. |
    | end_time                  | The time using Coordinated Universal Time (UTC) of emissions, either as an instance of end time of observation.   |
    | lat                       | Approximate latitude location of the source.                                                                      |
    | lon                       | Approximate longitude location of the source.                                                                     |
    | geometry_ref              | Corresponds to the reference id to the geopackage file present in the downloads.                                  |
    | gas                       | Greenhouse gases for which emissions are reported in metric tonnes.                                               |
    | emissions_quantity        | Quantity of gas emitted in metric tonnes.                                                                         |
    | temporal_granularity      | Resolution of the data available.                                                                                 |
    | activity                  | Activity of the entity producing the emissions, not including units.                                              |
    | activity_units            | Units of reported "activity".                                                                                     |
    | emissions_factor          | Emissions factor of reported activity.                                                                            |
    | emissions_factor_units    | Units of reported "emissions factor" field.                                                                       |
    | capacity                  | Capacity of the entity producing emissions, not including units.                                                  |
    | capacity_units            | Units of reported "capacity" field.                                                                               |
    | capacity_factor           | Corresponds to the ratio of the actual source output (activity) to the source capacity.                           |
    | capacity_factor_units     | Units of repored "capacity_factor" field.                                                                         |
    | other1                    | Additional data field available for the sub-sector.                                                               |
    | other1_def                | Definition of reported data of Other1 field.                                                                      |
    | other2                    | Additional data field available for the sub-sector.                                                               |
    | other2_def                | Definition of reported data of Other2 field.                                                                      |
    | other3                    | Additional data field available for the sub-sector.                                                               |
    | other3_def                | Definition of reported data of Other3 field.                                                                      |
    | other4                    | Additional data field available for the sub-sector.                                                               |
    | other4_def                | Definition of reported data of Other4 field.                                                                      |
    | other5                    | Additional data field available for the sub-sector.                                                               |
    | other5_def                | Definition of reported data of Other5 field.                                                                      |
    | other6                    | Additional data field available for the sub-sector.                                                               |
    | other6_def                | Definition of reported data of Other6 field.                                                                      |
    | other7                    | Additional data field available for the sub-sector.                                                               |
    | other7_def                | Definition of reported data of Other7 field.                                                                      |
    | other8                    | Additional data field available for the sub-sector.                                                               |
    | other8_def                | Definition of reported data of Other8 field.                                                                      |
    | other9                    | Additional data field available for the sub-sector.                                                               |
    | other9_def                | Definition of reported data of Other9 field.                                                                      |
    | other10                   | Additional data field available for the sub-sector.                                                               |
    | other10_def               | Definition of reported data of Other10 field.                                                                     |
    | created_date              | Date emissions source was added to the Climate TRACE database.                                                    |
    | modified_date             | Last date on which any updates were made to the dataset for the specific source.                                  |

    </center>

![carbon_trace](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/a1adee01-d0a4-435a-8fcc-c923ae7e853c)


#### Earth Engine Snippet

```js
var aluminum = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/aluminum_emissions-sources");
var bauxiteMining = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/bauxite-mining_emissions-sources");
var cement = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/cement_emissions-sources");
var chemicals = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/chemicals_emissions-sources");
var coalMining = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/coal-mining_emissions-sources");
var copperMining = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/copper-mining_emissions-sources");
var croplandFires = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/cropland-fires_emissions-sources");
var domesticAviation = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/domestic-aviation_emissions-sources");
var domesticShipping = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/domestic-shipping_emissions-sources");
var electricityGeneration = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/electricity-generation_emissions-sources");
var entericFermentationCattleFeedlot = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/enteric-fermentation-cattle-feedlot_emissions-sources");
var entericFermentationCattlePasture = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/enteric-fermentation-cattle-pasture_emissions-sources");
var forestLandClearing = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/forest-land-clearing_emissions-sources");
var forestLandDegradation = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/forest-land-degradation_emissions-sources");
var forestLandFires = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/forest-land-fires_emissions-sources");
var internationalAviation = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/international-aviation_emissions-sources");
var internationalShipping = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/international-shipping_emissions-sources");
var ironMining = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/iron-mining_emissions-sources");
var manureLeftOnPastureCattle = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/manure-left-on-pasture-cattle_emissions-sources");
var manureManagementCattleFeedlot = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/manure-management-cattle-feedlot_emissions-sources");
var netForestLand = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/net-forest-land_emissions-sources");
var netShrubgrass = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/net-shrubgrass_emissions-sources");
var netWetland = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/net-wetland_emissions-sources");
var oilAndGasRefining = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/oil-and-gas-refining_emissions-sources");
var otherManufacturing = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/other-manufacturing_emissions-sources");
var petrochemicals = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/petrochemicals_emissions-sources");
var pulpAndPaper = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/pulp-and-paper_emissions-sources");
var removals = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/removals_emissions-sources");
var riceCultivation = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/rice-cultivation_emissions-sources");
var roadTransportation = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/road-transportation_emissions-sources");
var shrubgrassFires = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/shrubgrass-fires_emissions-sources");
var solidWasteDisposal = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/solid-waste-disposal_emissions-sources");
var steel = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/steel_emissions-sources");
var syntheticFertilizerApplication = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/synthetic-fertilizer-application_emissions-sources");
var wastewaterTreatmentAndDischarge = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/wastewater-treatment-and-discharge_emissions-sources");
var waterReservoirs = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/water-reservoirs_emissions-sources");
var wetlandFires = ee.FeatureCollection("projects/sat-io/open-datasets/CLIMATE-TRACE/EMISSIONS/wetland-fires_emissions-sources");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/CLIMATE-TRACE-EMISSIONS

#### License

All Climate TRACE data is freely available under the Creative Commons Attribution 4.0 International Public License, unless otherwise noted below

Created by: Climate Trace

Curated in GEE by: Samapriya Roy

Keywords: Climate Trace, Emissions, Sectors, Agriculture, Buildings, Fossil Fuel Operations, Forestry And Land Use, Manufacturing, Mineral Extraction, Power, Transportation, Waste

Last updated: 2024-01-17
