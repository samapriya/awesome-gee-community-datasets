# National Structures Inventory

???+ note

    **These will be made available primarily in the insiders only dataset before being made generally available to all users of the community catalog**

The National Structure Inventory (NSI) is a system of databases containing structure inventories of varying quality and spatial coverage. The purpose of the NSI databases is to facilitate storage and sharing of point-based structure inventories used in the assessment and analysis of natural hazards. Flood risk is the primary usage, but sufficient data exists on each structure to compute damages and life safety risk due to other hazard types. This document describes the NSI data structure and the processes utilized to produce the 2022 NSI base data.

The National Structure Inventory Base layer was created and is maintained by the U.S. Army Corps of Engineers (USACE). The USACE base data layer was created to simplify the GIS pre-processing workflow for the USACE Modeling Mapping and Consequence center, but the data has gone on to see use in a variety of USACE, FEMA, and other agency applications. The NSI is a repository of point structure inventories with a structured RESTful API service, and the inventory contains a series of required attributes or fields that describe each point in the inventory.

#### Table of Public Fields

??? example "The NSI attributes available to the general public are"

    <center>

    | Field Name    | Description                                                                                       | Attribute Type | Limits              |
    |---------------|---------------------------------------------------------------------------------------------------|----------------|---------------------|
    | fd_id       | A number that should be unique for all structures.                                                | Integer         |                     |
    | bid         | A building ID, represented as the centroid (in grid reference system format) and four cardinal extents. | String          |                     |
    | x           | X coordinate of each structure in the Geographic Coordinate System (GCS) WGS84.                   | Double          |                     |
    | y           | Y coordinate of each structure in GCS WGS84.                                                       | Double          |                     |
    | cbfips      | Census Block that contains the structure. Currently, the NSI refers to 2010 census blocks.          | String          | 15 Characters       |
    | st_damcat   | Damage category of the structure. Aggregated categories include Residential, Commercial, Industrial, or Public. | String          |                     |
    | occtype     | Damage Function or Occupancy Type of the structure, related to depth-damage relationships.           | String          |                     |
    | bldgtype    | Building type of the structure (e.g., Masonry, Wood, Manufactured, Steel).                          | String          |                     |
    | source      | The source of the initial iteration of the structure (e.g., Parcel, ESRI, HIFLD).                    | String          |                     |
    | sqft        | Estimated square footage of the structure.                                                            | Double          |                     |
    | ftprntid    | Identifier of the building footprint record used for estimating fields such as sqft and num_story.   | String          |                     |
    | ftprntsrc   | The source of the utilized footprint (e.g., Bing, Oak Ridge National Labs, NGA).                     | String          |                     |
    | found_type  | Type of foundation (e.g., Crawl, Basement, Slab, Pier).                                             | String          |                     |
    | found_ht    | Foundation height of the structure in feet from the ground elevation.                               | Double          |                     |
    | num_story   | The number of stories of the structure.                                                              | Double          |                     |
    | val_struct  | Value in dollars of the structure. The base NSI estimates depreciated replacement value.             | Double          |                     |
    | val_cont    | Value in dollars of the contents of the structure.                                                   | Double          |                     |
    | val_vehic   | Value in dollars of the cars at the structure.                                                       | Double          |                     |
    | med_yr_blt  | Median year built of structures within the Census Block.                                             | Integer         |                     |
    | pop2amu65   | Population at night for people under the age of 65.                                                  | Integer         |                     |
    | pop2amo65   | Population at night for people over the age of 65.                                                   | Integer         |                     |
    | pop2pmu65   | Population during the day for people under the age of 65.                                           | Integer         |                     |
    | pop2pmo65   | Population during the day for people over the age of 65.                                            | Integer         |                     |
    | students    | Number of students attending the school as estimated by NCES data.                                  | Integer         |                     |
    | o65disable  | Percent of the county population over the age of 65 with an ambulatory disability.                  | Double          |                     |
    | u65siable   | Percent of the county population under the age of 65 with an ambulatory disability.                 | Double          |                     |
    | firmzone    | Estimated 2021 flood zone for the structure.                                                         | String          |                     |
    | grnd_elv_m  | Ground elevation (in meters, NAVD88) at the structure.                                              | Double          |                     |
    | ground_elv  | Ground elevation (in feet, NAVD88) at the structure.                                                | Double          |                     |

    </center>

#### Structure Processing and Valuation
The National Structure Inventory (NSI) involves several key processes for managing and analyzing structures:

* Structure Placement and Aggregation: Initially, structure locations are based on source data such as parcel centroids or business addresses. The NSI Generator refines these locations by aligning structures with building footprints within the same parcel. Commercial structures outside their original parcel are relocated based on distance and use code similarity. Structures are placed in unpaired footprints until all footprints are matched. Stacked structures are partially or completely merged based on their occupancy type, with residential units combined as multi-family structures if stacked. Commercial structures are merged only if they share the same occupancy type and similar characteristics, like number of stories and construction material.

* Population Distribution: The NSI-2022 estimates population levels for 2020 using data from 2010 block information and 2020 county data. This population is distributed to structures according to housing units and block-level estimates. For commercial structures, worker population estimates are derived from the U.S. Census Bureau’s LEHD database.

* Structure Valuation: Depreciated replacement values for structures are estimated based on a dollar per square foot metric, with depreciation at 1% per year for the first 20 years. Content values are calculated using specific ratios tied to occupancy types.

#### Occupancy Type

Occupancy types help determine structure valuation and damage criteria. They are based on FEMA definitions with further classification.

??? example "The table below shows occupancy types and their content-to-structure value ratios"

    <center>

    | Damage Category | Occupancy Type Name | Description                                      | Content to Structure Value Ratio |
    |-----------------|----------------------|--------------------------------------------------|---------------------------------|
    | Residential      | RES1-1SNB            | Single Family Residential, 1 story, no basement | 0.5                             |
    | Residential      | RES1-1SWB            | Single Family Residential, 1 story, with basement | 0.5                             |
    | Residential      | RES1-2SNB            | Single Family Residential, 2 story, no basement | 0.5                             |
    | Residential      | RES1-2SWB            | Single Family Residential, 2 story, with basement | 0.5                             |
    | Residential      | RES1-3SNB            | Single Family Residential, 3 story, no basement | 0.5                             |
    | Residential      | RES1-3SWB            | Single Family Residential, 3 story, with basement | 0.5                             |
    | Residential      | RES1-SLNB            | Single Family Residential, split-level, no basement | 0.5                             |
    | Residential      | RES1-SLWB            | Single Family Residential, split-level, with basement | 0.5                             |
    | Residential      | RES2                 | Manufactured Home                                | 0.5                             |
    | Residential      | RES3A                | Multi-Family housing 2 units                     | 0.5                             |
    | Residential      | RES3B                | Multi-Family housing 3-4 units                   | 0.5                             |
    | Residential      | RES3C                | Multi-Family housing 5-10 units                  | 0.5                             |
    | Residential      | RES3D                | Multi-Family housing 10-19 units                 | 0.5                             |
    | Residential      | RES3E                | Multi-Family housing 20-50 units                 | 0.5                             |
    | Residential      | RES3F                | Multi-Family housing 50 plus units               | 0.5                             |
    | Commercial       | COM1                 | Light Commercial, Office, Retail                 | 1.0                             |
    | Commercial       | COM2                 | General Commercial                               | 1.0                             |
    | Commercial       | COM3                 | Heavy Commercial, Manufacturing                  | 1.0                             |
    | Commercial       | COM4                 | Industrial                                      | 1.0                             |
    | Public           | PUB1                 | Institutional                                    | 1.0                             |
    | Public           | PUB2                 | Education                                       | 1.0                             |
    | Public           | PUB3                 | Healthcare                                      | 1.0                             |
    | Public           | PUB4                 | Government                                       | 1.0                             |

    </center>

#### Main Data Sources

??? example "The table contains main data sources of data"

    <center>

    | **Source** | **Database**                 | **Dataset**               | **Description**                                                                                           |
    |------------|------------------------------|---------------------------|-----------------------------------------------------------------------------------------------------------|
    | HAZUS      | Bndrygbs.mdb                 | hzCensusBlock             | Provides the structure building schemes and block type.                                                   |
    |            |                              | flSchemeCoastal, flSchemeRiverine, flSchemeGLakes | Provides information on foundation type and height.                                                       |
    |            | MSH.mdb                      | flGenBldgScheme           | Provides the construction type distributions and NFIP entry year for structures.                           |
    | USACE      | NSI 2015                     | Base layer                | Used in any Census Block that lacks ESRI or CoreLogic data.                                               |
    | Homeland Infrastructure Foundation-Level Data | Lightbox | County Level Data | Parcel polygons and associated data tables; used for initial spatial location and occupancy type, and may influence structure attributes (square feet, foundation type, etc) of single-family structures. |
    |            |                              | Nursing Home              | Point data indicating the presence of a nursing home and its number of beds.                               |
    |            |                              | Hospital                  | Point data indicating the presence of a hospital and its number of beds.                                  |
    |            |                              | Mobile Home               | Point data indicating the presence of a mobile home park and the number of units associated with the park (either exact units, or a range). |
    |            |                              | Map Building Layer        | Nationwide building footprint parcel. Largely restricted to central business districts. Often indicating the height of the building to the nearest meter. Used to improve structure locations, square foot estimates and number of stories estimates. |
    | Esri       | Business Layer               | InfoGroup                 | Provides initial structure location; NAICS code informs occupancy type and the number of employee field influences population weighting and square footage estimates. |
    | Microsoft  | Building Footprints          | State level polygons      | Paired with parcel polygons to improve structure location and to inform structure aggregation and square footage estimates. |
    | FEMA Geospatial Resource Center | USA Structures | State level polygons | Includes both ORNL and NGA generated footprint polygons. Paired with parcel polygons to improve structure location and to inform structure aggregation and square footage estimates. NGA based footprints include heights in meters and help inform number of stories estimates. |
    | U.S. Census Bureau | American Community Survey | Population, Demographics | Informs population growth estimates, disability rates, and age distribution.                                |
    |            | Characteristics of New Housing | Annual, Various           | Provides structure characteristic data such as number of stories and square feet.                         |
    |            | Longitudinal Employer-Household Dynamic Database | Population Data | Contains worker counts by origin and destination census blocks. Used to decrease residential populations (primarily in the day) and to create a population pool for commercial workers. |
    | NCES       | Schools Database             | School Data               | Contains the locations of schools, number of teachers and students per school.                            |
    | U.S. Geological Survey | National Elevation Dataset | 10 Meter Dataset        | Provides raster ground elevation data.                                                                    |

    </center>

#### Citation

```
U.S. Army Corps of Engineers (Year). National Structure Inventory (NSI) Base Data. U.S. Army Corps of Engineers. URL or DOI.
```

![nsi](https://github.com/user-attachments/assets/7b3bf4f0-27e5-48e7-a181-78a76315ca86)

#### Earth Engine Snippet

The datasets are available by state using the two alphabet state abbreviation for example, for WYOMING (WY)

```js
var nsi_wy = ee.FeatureCollection('projects/sat-io/open-datasets/NSI/nsi_2022_WY');
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/NSI

#### License

The National Structure Inventory (NSI) from the U.S. Army Corps of Engineers (USACE) has a licensing structure that allows for public access to its primary fields, as these fields are curated to have less restrictive license agreements.

Provided by: USACE

Curated in GEE by: Samapriya Roy

Keywords: Buildings, Structures Inventory, US

Last updated: 2024-08-07
