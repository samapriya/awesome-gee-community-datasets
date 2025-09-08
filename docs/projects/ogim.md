# Oil and Gas Infrastructure Mapping (OGIM) database

The Oil and Gas Infrastructure Mapping (OGIM) dataset, available in the Awesome Google Earth Engine (GEE) Community Catalog, is a comprehensive global repository of spatially explicit information on oil and gas infrastructure. Developed by the Environmental Defense Fund (EDF) (www.edf.org) and MethaneSAT, LLC (www.methanesat.org), a wholly owned subsidiary of EDF, the OGIM database is meticulously curated to facilitate the quantification and characterization of methane emissions from oil and gas sources.

This dataset is a result of extensive efforts at EDF and MethaneSAT, involving the acquisition, analysis, curation, integration, and quality assurance of public-domain datasets sourced from official government reports, industry publications, academic studies, and various non-government entities. The primary objective of the OGIM database is to provide valuable support for research and analysis related to oil and gas methane emissions. The dataset spans across the globe, offering a comprehensive view of oil and gas infrastructure. It provides detailed information on the locations and attributes of various oil and gas infrastructure types known to be significant sources of methane emissions. This includes data on oil and gas production wells, offshore production platforms, natural gas compressor stations, processing facilities, liquefied natural gas facilities, crude oil refineries, pipelines, and more.

OGIM v2.7 includes approximately 6.7 million features, including 4.5 million point locations of oil and gas wells and over 1.2 million kilometers of oil and gas pipelines. The database is based on public-domain datasets reported in February 2025 or prior. Each record in OGIM indicates a date (SRC_DATE) when the original source of the record was published or last updated. Some records may contain out-of-date information, for example, if a facility's status has changed since the last data source update. The database is updated on a regular cadence with new public domain datasets as they become available.

You can read more about [the OGIM dataset here](https://essd.copernicus.org/articles/15/3761/2023/essd-15-3761-2023.pdf) and you can find the [dataset here](https://zenodo.org/records/7922117).

#### Citation

```
Omara, Mark, Ritesh Gautam, Madeleine O'Brien, Anthony Himmelberger, Alex Franco, Kelsey Meisenhelder, Grace Hauser et al.
"Developing a spatially explicit global oil and gas infrastructure database for characterizing methane emission sources at
high resolution." Earth System Science Data Discussions 2023 (2023): 1-35.
```

#### Dataset citation

```
O'Brien, M., Omara, M., Himmelberger, A., & Gautam, R. (2025). Oil and Gas Infrastructure Mapping (OGIM) database (OGIM_v2.7) [Data set].
Zenodo. https://doi.org/10.5281/zenodo.15103476
```

#### OGIM Layer Descriptors

??? example "Expand to show OGIM geospatial layers"

    <center>

    | OGIM geospatial data layer                              | Additional information                                                                                                                       | Geometry type |
    |---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|---------------|
    | Oil and natural gas wells                               | Includes active, inactive, and plugged and abandoned oil and natural gas wells. Production data now integrated into this layer.            | POINT         |
    | Natural gas compressor stations                         | Facilities for natural gas compression in the gathering, transmission, and distribution sector.                                              | POINT         |
    | Gathering and processing facilities                     | Includes natural gas processing plants, natural gas dehydration and other treatment facilities, and oil gathering and processing facilities. | POINT         |
    | Tank battery                                            | Can be collocated with well sites; typical equipment includes oil and natural gas separation equipment and an arrangement of storage tanks.  | POINT         |
    | Offshore platforms                                      | Oil and natural gas drilling, production, and processing platforms in offshore areas.                                                        | POINT         |
    | LNG facilities                                          | Includes both liquefaction and regasification facilities.                                                                                    | POINT         |
    | Crude oil refineries                                    | -                                                                                                                                            | POINT         |
    | Petroleum terminals                                     | Includes tank farms and petroleum bulk storage tanks and terminals.                                                                          | POINT         |
    | Injection and disposal facilities                       | Underground injection, disposal, and storage facilities.                                                                                     | POINT         |
    | Stations - Other                                        | Includes metering and regulating stations and POL (petroleum, oil, and lubricants) pumping stations.                                         | POINT         |
    | Equipment and components                                | Includes point locations for dehydrators, separators, tanks, and valves.                                                                     | POINT         |
    | Natural gas flaring detections                          | Based on VIIRS natural gas flaring detections in 2021.                                                                                       | POINT         |
    | Oil and natural gas pipelines                           | Pipeline infrastructure for oil and natural gas transportation.                                                                               | LINESTRING    |
    | Oil and natural gas basins                              | Geological basins containing oil and natural gas resources.                                                                                   | POLYGON       |
    | Oil and natural gas fields                              | Defined oil and natural gas production fields.                                                                                               | POLYGON       |
    | Oil and natural gas license blocks                      | Licensed areas for oil and natural gas exploration and production.                                                                           | POLYGON       |

    <center>

![ogim_v11](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/11cbe7b9-ae51-413a-adfa-cd85c05d278e)

#### Earth Engine Snippet

```js
var crude_oil_refineries = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/crude_oil_refineries");
var equipment_and_components = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/equipment_and_components");
var gathering_and_processing = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/gathering_and_processing");
var injection_disposal_and_underground_storage = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/injection_and_disposal");
var lng_facilities = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/lng_facilities");
var natural_gas_compressor_stations = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/natural_gas_compressor_stations");
var natural_gas_flaring_detections = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/natural_gas_flaring_detections");
var offshore_platforms = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/offshore_platforms")
var oil_and_natural_gas_basins = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/oil_and_natural_gas_basins")
var oil_and_natural_gas_fields = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/oil_and_natural_gas_fields")
var oil_and_natural_gas_license_blocks = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/oil_and_natural_gas_license_blocks")
var oil_and_natural_gas_pipelines = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/oil_and_natural_gas_pipelines");
var oil_and_natural_gas_wells = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/oil_and_natural_gas_wells");
var petroleum_terminals = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/petroleum_terminals");
var stations_other = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/stations_other");
var tank_battery = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/tank_battery");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/OGIM

#### License

These datasets are provided under a Creative Commons Attribution 4.0 International Public License, unless otherwise noted.

Created by: Omara et al

Curated in GEE by: Samapriya Roy

Keywords: OGIM dataset, Methane emissions, Environmental Defense Fund (EDF), MethaneSAT, infrastructure types, oil and gas wells, offshore platforms, Compressor stations, Liquefied natural gas facilities, Crude oil refineries

Last updated: 2025-09-08

#### Version History

**v2.7 Changes:**
- Updated to approximately 6.7 million features (increased from ~6 million in v1)
- Expanded to 4.5 million point locations of oil and gas wells (increased from 2.6 million in v1)
- Increased pipeline coverage to over 1.2 million kilometers (expanded from 2.6×10⁶ km in v1)
- Added new feature collections: oil and natural gas basins, fields, and license blocks (polygon data)
- Renamed "injection_disposal_and_underground_storage" to "injection_and_disposal"
- Removed separate "oil_and_natural_gas_production" layer (production data now integrated into wells layer)
- Updated Earth Engine asset paths to OGIM_STAGING directory structure
- Based on public-domain datasets reported through February 2025
- Continues regular database updates with new public domain datasets as they become available


