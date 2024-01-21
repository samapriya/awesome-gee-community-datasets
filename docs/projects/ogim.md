# Oil and Gas Infrastructure Mapping (OGIM) database

The Oil and Gas Infrastructure Mapping (OGIM) dataset, available in the Awesome Google Earth Engine (GEE) Community Catalog, is a comprehensive global repository of spatially explicit information on oil and gas infrastructure. Developed by the Environmental Defense Fund (EDF) (www.edf.org), the OGIM database is meticulously curated to facilitate the quantification and characterization of methane emissions from oil and gas sources.

This dataset is a result of extensive efforts at EDF, involving the acquisition, analysis, curation, integration, and quality assurance of public-domain datasets sourced from official government reports, industry publications, academic studies, and various non-government entities. The primary objective of the OGIM database is to provide valuable support for research and analysis related to oil and gas methane emissions. The dataset spans across the globe, offering a comprehensive view of oil and gas infrastructure.It provides detailed information on the locations and attributes of various oil and gas infrastructure types known to be significant sources of methane emissions. This includes data on oil and gas production wells, offshore production platforms, natural gas compressor stations, processing facilities, liquefied natural gas facilities, crude oil refineries, pipelines, and more.

You can read more about [the OGIM dataset here](https://essd.copernicus.org/articles/15/3761/2023/essd-15-3761-2023.pdf) and you can find the [dataset here](https://zenodo.org/records/7922117).


#### Citation

```
Omara, Mark, Ritesh Gautam, Madeleine O'Brien, Anthony Himmelberger, Alex Franco, Kelsey Meisenhelder, Grace Hauser et al.
"Developing a spatially explicit global oil and gas infrastructure database for characterizing methane emission sources at
high resolution." Earth System Science Data Discussions 2023 (2023): 1-35.
```

#### Dataset citation

```
Ritesh Gautam. (2023). Oil and Gas Infrastructure Mapping (OGIM) database (OGIM_v1.1) [Data set]. Zenodo.
https://doi.org/10.5281/zenodo.7922117
```

#### OGIM Layer Descriptors

??? example "Expand to show OGIM geospatial layers"

    <center>

    | OGIM geospatial data layer                              | Additional information                                                                                                                       | Geometry type |
    |---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|---------------|
    | Oil and natural gas wells                               | Includes active, inactive, and plugged and abandoned oil and natural gas wells.                                                              | POINT         |
    | Natural gas compressor stations                         | Facilities for natural gas compression in the gathering, transmission, and distribution sector.                                              | POINT         |
    | Gathering and processing facilities                     | Includes natural gas processing plants, natural gas dehydration and other treatment facilities, and oil gathering and processing facilities. | POINT         |
    | Tank battery                                            | Can be collocated with well sites; typical equipment includes oil and natural gas separation equipment and an arrangement of storage tanks.  | POINT         |
    | Offshore platforms                                      | Oil and natural gas drilling, production, and processing platforms in offshore areas.                                                        | POINT         |
    | LNG facilities                                          | Includes both liquefaction and regasification facilities.                                                                                    | POINT         |
    | Crude oil refineries                                    | -                                                                                                                                            | POINT         |
    | Petroleum terminals                                     | Includes tank farms and petroleum bulk storage tanks and terminals.                                                                          | POINT         |
    | Injection, disposal, and underground storage facilities | -                                                                                                                                            | POINT         |
    | Stations - Other                                        | Includes metering and regulating stations and POL (petroleum, oil, and lubricants) pumping stations.                                         | POINT         |
    | Equipment and components                                | Includes point locations for dehydrators, separators, tanks, and valves.                                                                     | POINT         |
    | Oil and natural gas production                          | Includes reported well-level, facility-level, and field-level oil and natural gas production, as reported for 2021.                          | POINT         |
    | Natural gas flaring detections                          | Based on VIIRS natural gas flaring detections in 2021.                                                                                       | POINT         |

    <center>

![ogim_v11](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/11cbe7b9-ae51-413a-adfa-cd85c05d278e)


#### Earth Engine Snippet

```js
var crude_oil_refineries = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/crude_oil_refineries");
var equipment_and_components = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/equipment_and_components");
var gathering_and_processing = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/gathering_and_processing");
var injection_disposal_and_underground_storage = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/injection_disposal_and_underground_storage");
var lng_facilities = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/lng_facilities");
var natural_gas_compressor_stations = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/natural_gas_compressor_stations");
var natural_gas_flaring_detections = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/natural_gas_flaring_detections");
var offshore_platforms = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/offshore_platforms");
var oil_and_natural_gas_production = ee.FeatureCollection("projects/sat-io/open-datasets/OGIM/oil_and_natural_gas_production");
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

Keywords: OGIM dataset, Methane emissions, Environmental Defense Fund (EDF), infrastructure types, oil and gas wells, offshore platforms, Compressor stations, Liquefied natural gas facilities, Crude oil refineries

Last updated: 2024-01-19

