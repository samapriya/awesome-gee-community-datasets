# Global database of cement production assets and upstream suppliers

The Global Cement Production Dynamics dataset provides a comprehensive asset-level view of the cement industry, addressing the growing climate and
sustainability concerns faced by cement producers and investors. It integrates greenhouse gas emissions disclosure, sourcing patterns of raw
materials, and the age of production plants as key variables. Leveraging innovative techniques, including geospatial computer vision and Large
Language Modelling, the dataset offers a holistic understanding of global cement production dynamics. It serves various applications, such as
environmental impact assessment, investment decision-making, industry research, and policy development, contributing to more informed and
responsible decision-making within the sector.

The dataset contains spatial information for 3,117 cement production assets, offering near-approximate location data within a 10-kilometer radius.
This data, available for download in Excel format from the Dryad Repository, includes precise coordinates (WGS84), city, state, country, ISO codes,
sub-region, and region, obtained through reverse geocoding. Plant-specific details encompass plant type (integrated or grinding), production process
(wet or dry), capacity, and the year of production commencement, with corresponding sources for capacity data. Ownership information is also
comprehensive, encompassing direct or subsidiary owner names, ultimate parent details, PermID where available, Legal Entity Identifier (LEI),
holding status (public or private), ticker, and exchange for ultimate parents. In cases of joint ventures, information for both ultimate parents is
provided, alongside source links for ownership data. You can [read the paper here](https://www.nature.com/articles/s41597-023-02599-w).

#### Dataset structure
The datasets were renamed to end with the date of [dataset upload to Dryad Repository](https://datadryad.org/stash/dataset/doi:10.5061/dryad.6t1g1jx4f) and the primary layer consisting of the assets database includes the following fields. You can expand this section to get all field names or use the example code

??? example "Expand to show field names and description for primary asset database"

    <center>

    | Field              | Description                                                      |
    |--------------------|------------------------------------------------------------------|
    | uid                | Unique identifier for the cement plant                           |
    | city               | City in which the plant is located                                |
    | state              | State or province in which the plant is located                  |
    | country            | Country in which the plant is located                             |
    | iso3               | Three-letter country code defined in ISO 3166-1 alpha 3          |
    | country_code       | Three-digit country code defined in ISO 3166-1 numeric            |
    | region             | Region in which the plant is located                              |
    | sub_region         | Subregion in which the plant is located                           |
    | latitude           | Latitude for the geolocation of the plant (based on WGS84)        |
    | longitude          | Longitude for the geolocation of the plant (based on WGS84)       |
    | accuracy           | The accuracy of the latitude and longitude                        |
    | status             | Current plant operating status                                     |
    | plant_type         | The type of cement plant (Integrated or Grinding)                |
    | production_type    | The production process used to produce the clinker at Integrated plants (Wet or Dry) |
    | confdnc            | Accuracy of production capacity (in cases where numerous values are reported) |
    | capacity           | Total cement production capacity (millions of tons)               |
    | capacity_source    | Source used to obtain the capacity estimate (news media, company website, or company disclosure reports) |
    | year               | Year the plant started production                                 |
    | owner_permid       | PermID of the primary owner of the plant*                         |
    | owner_name         | Name of the primary owner of the plant                            |
    | owner_source       | Source reporting the ownership link between the plant and owner  |
    | parent_permid      | PermID of the ultimate parent of the owner of the plant*          |
    | parent_name        | Name of the ultimate parent of the owner of the plant             |
    | ownership_stake    | The percentage ownership attributed to the parent company if the plant is a joint venture. If the plant is majority owned by a single parent company, then this column will be blank ('n/a') |
    | parent_lei         | Legal Entity Identifier (LEI) of the ultimate parent of the owner of the plant |
    | parent_holding_status | The holding status of the ultimate parent (Private or Public)   |
    | parent_ticker      | The primary ticker for the ultimate parent, if the company is publicly traded |
    | parent_exchange    | The primary exchange for the ultimate parent, if the company is publicly traded |
    | parent_permid_2    | PermID of the 2nd ultimate parent of the owner of the plant*      |
    | parent_name_2      | Name of the 2nd ultimate parent of the owner of the plant         |
    | ownership_stake_2  | The percentage ownership attributed to the 2nd parent company if the plant is a joint venture |
    | parent_lei_2       | Legal Entity Identifier (LEI) of the 2nd ultimate parent          |
    | parent_holding_status_2 | The holding status of the 2nd ultimate parent (Private or Public) |
    | parent_ticker_2    | The primary ticker for the 2nd ultimate parent, if the company is publicly traded |
    | parent_exchange_2  | The primary exchange for the 2nd ultimate parent, if the company is publicly traded |
    | sourcing           | Locally sourced, imported, or hybrid supply of input production materials |
    | raw_mtrl           | Typology of raw input materials (limestone, clay, gypsum, sand, coal) |
    | clinker            | Whether clinker was used as an input material                      |

    </center>

The second dataset provides facility and supplier information

??? example "Expand to show field names and description for facility and supplier information"

    <center>

    | Field                | Description                                                        |
    |----------------------|--------------------------------------------------------------------|
    | uid                  | Unique identifier for the cement plant                              |
    | facility.country     | Country in which the plant is located                               |
    | supplier.country     | Country in which facility-supplier (mine) is located                |
    | supplier.latitude    | Latitude for the geolocation of the facility-supplier (based on WGS84 (EPSG:4326)) |
    | supplier.longitude   | Longitude for the geolocation of the facility-supplier (based on WGS84 (EPSG:4326)) |

    </center>

#### Citation

```
Tkachenko, N., Tang, K., McCarten, M. et al. Global database of cement production assets and upstream suppliers. Sci Data 10, 696 (2023).
https://doi.org/10.1038/s41597-023-02599-w
```

#### Dataset citation

```
Tkachenko, Nataliya et al. (2023). Global database of cement production assets and upstream suppliers [Dataset]. Dryad.
https://doi.org/10.5061/dryad.6t1g1jx4f
```

![global_cement_database](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/a8be3ae1-189a-4d63-848a-d1b6313fe203)

#### Earth Engine Snippet

```js
var assets_db = ee.FeatureCollection("projects/sat-io/open-datasets/SFI/global_cement_db_assets_20231004");
var suppliers_producers_db = ee.FeatureCollection("projects/sat-io/open-datasets/SFI/global_cement_db_suppliers_20231004");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/GLOBAL-CEMENT-SUPP-PROD-DB

#### License
This work is licensed under a CC0 1.0 Universal (CC0 1.0) Public Domain Dedication license

Data download page: [Dryad data download page](https://datadryad.org/stash/dataset/doi:10.5061/dryad.6t1g1jx4f)

Provided by: Tkachenko, N., Tang, K., McCarten, M. et al

Curated in GEE by: Samapriya Roy

Keywords: : Computer vision, Remote sensing, Computer and information sciences, asset-level data, Decarbonisation, LLMs, spatial finance, supply chains, sustainable finance, cement

Last updated: 2023-10-18
