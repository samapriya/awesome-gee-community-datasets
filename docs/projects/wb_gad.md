# World Bank Official Boundaries

The World Bank Official Boundaries project publishes high-resolution, regularly updated global administrative boundaries as open data, designed and endorsed by the World Bank for robust, cross-sectoral geospatial analysis. Developed through collaboration between the Development Data Group's Space2Stats program and the Cartography Unit from Global Corporate Solutions Interactive Media, this dataset delivers detailed boundaries at the national (Admin 0), provincial (Admin 1), and district (Admin 2) levels. It improves upon former datasets by offering higher resolution, standardized formats, and more frequent updates, promoting transparency and inclusion by making these foundational data resources openly available to researchers, development organizations, and partners worldwide.

The dataset addresses the previous lack of an updated, standardized source of World Bank boundary data and provides a consistent alternative to public datasets like GADM and GeoBoundaries, meeting WBG cartographic standards and following consistent update schedules. For detailed context, methodology, and case studies on how boundary data supports evidence-based development, see [Mapping progress: How the World Bank is improving access to global administrative boundaries](https://blogs.worldbank.org/en/opendata/mapping-progress--how-the-world-bank-is-improving-access-to-glob?cid=SHR_BlogSiteShare_EN_EXT) - World Bank Data Blog (October 28, 2025)

#### Data Sources

The World Bank Official Boundaries were compiled from multiple authoritative sources in order of priority:

1. **Second Administrative Level Boundaries (SALB)** geoportal - authoritative subnational boundary information managed by the UN Geographic Information Section
2. **Humanitarian Data Exchange (HDX)** platform - hosted by the Office for the Coordination of Humanitarian Affairs (OCHA)
3. **National Providers** - relevant national authorities identified through official channels
4. **World Bank GAD** - legacy World Bank Global Administrative Divisions dataset when no other sources were available

#### Citation

When referencing the World Bank Official Boundaries, follow these recommended citation practices:

**APA Style:**
```
The World Bank. (2025). World Bank Official Boundaries [Data set]. 
https://datacatalog.worldbank.org/search/dataset/0038272
```

**Chicago Style:**
```
The World Bank. 2025. "World Bank Official Boundaries." Washington, D.C.: 
World Bank. https://datacatalog.worldbank.org/search/dataset/0038272
```

#### Attributes

??? example "Expand to show ADM0 (Country Level) attributes"

    <center>

    | Field Name  | Description                                                      |
    |-------------|------------------------------------------------------------------|
    | ISO_A3      | ISO country-level 3 letter alpha code                           |
    | ISO_A2      | ISO country-level 2 letter alpha code                           |
    | WB_A3       | World Bank 3 letter country-level alpha code                    |
    | HASC_0      | HASC country-level 2 letter alpha code                          |
    | GAUL_0      | GAUL country-level numeric identifier code                      |
    | WB_REGION   | Official World Bank Region classification                        |
    | WB_STATUS   | Official World Bank legal status classification                  |
    | SOVEREIGN   | Sovereign countries of the entity (state or territory)          |
    | NAM_0       | Country name in long form (English)                             |

    </center>

    **Note**: ADM0_complete contains both ADM0 and NDLSA (Non-Determined Legal Status Area) polygons, while the standard ADM0 file excludes NDLSA polygons.

??? example "Expand to show ADM1 (Provincial Level) attributes"

    <center>

    | Field Name  | Description                                                      |
    |-------------|------------------------------------------------------------------|
    | ISO_A3      | ISO country-level 3 letter alpha code                           |
    | ISO_A2      | ISO country-level 2 letter alpha code                           |
    | WB_A3       | World Bank 3 letter country-level alpha code                    |
    | WB_REGION   | Official World Bank Region classification                        |
    | WB_STATUS   | Official World Bank legal status classification                  |
    | NAM_0       | Country name in long form (English)                             |
    | NAM_1       | Name (English) of the Administrative Level 1 unit               |
    | ADM1CD_c    | Complete list of Adm1 codes (primary key)                       |
    | GEOM_SRCE   | Source of geometry (SALB dataset or original WB GAD)            |

    </center>

??? example "Expand to show ADM1 additional attributes"

    <center>

    | Field Name    | Description                                                    |
    |---------------|----------------------------------------------------------------|
    | HASC_0        | HASC country-level 2 letter alpha code                        |
    | HASC_1        | HASC Adm1 alpha code                                          |
    | GAUL_0        | GAUL country-level numeric identifier code                    |
    | GAUL_1        | GAUL Adm1 numeric identifier code                             |
    | SOVEREIGN     | Sovereign countries of the entity (state or territory)        |
    | NAM_1_GAUL    | Admin 1 name in GAUL                                          |
    | NAM_1_STAT    | Admin 1 name as listed in the Statoids database               |
    | NAM_1_SRCE    | Admin 1 name from original data source (SALB, UN HDX, etc.)   |
    | NAM_1_NTVE    | Admin 1 name in the native language                           |
    | NAM_1_WIKI    | Admin 1 name used in Wikipedia articles                       |
    | P_CODE_1      | P-Code for ADM1 from UN HDX Global P-Code List                |
    | P_CODE_1_t    | Temporary P-Code (when official not available)                |
    | P_CODE_1_c    | Complete list of Adm1 P_Codes                                 |
    | P_NAME_1      | Name for ADM1 from UN HDX Global P-Code List                  |
    | ADM1CD        | ADM1 code from SALB dataset                                   |
    | ADM1CD_t      | Temporary ADM1 code based on SALB methodology                 |
    | ADM1NM        | Name for ADM1 from SALB dataset                               |
    | P_DATE        | "Valid from" date accompanying P-Code and name                |
    | SALB_DATE     | Temporal validity for codes/geometry from SALB dataset        |

    </center>

??? example "Expand to show ADM2 (District Level) attributes"

    <center>

    | Field Name  | Description                                                      |
    |-------------|------------------------------------------------------------------|
    | ISO_A3      | ISO country-level 3 letter alpha code                           |
    | ISO_A2      | ISO country-level 2 letter alpha code                           |
    | WB_A3       | World Bank 3 letter country-level alpha code                    |
    | WB_REGION   | Official World Bank Region classification                        |
    | WB_STATUS   | Official World Bank legal status classification                  |
    | NAM_0       | Country name in long form (English)                             |
    | NAM_1       | Name (English) of the Administrative Level 1 unit               |
    | ADM1CD_c    | Complete list of Adm1 codes based on SALB methodology          |
    | NAM_2       | Name (English) of the Administrative Level 2 unit               |
    | ADM2CD_c    | Complete list of Adm2 codes (primary key)                       |
    | GEOM_SRCE   | Source of geometry (SALB dataset or original WB GAD)            |

    </center>

??? example "Expand to show ADM2 additional attributes"

    <center>

    | Field Name    | Description                                                    |
    |---------------|----------------------------------------------------------------|
    | HASC_0        | HASC country-level 2 letter alpha code                        |
    | HASC_1        | HASC Adm1 alpha code                                          |
    | HASC_2        | HASC Adm2 alpha code                                          |
    | GAUL_0        | GAUL country-level numeric identifier code                    |
    | GAUL_1        | GAUL Adm1 numeric identifier code                             |
    | GAUL_2        | GAUL Adm2 numeric identifier code                             |
    | SOVEREIGN     | Sovereign countries of the entity (state or territory)        |
    | NAM_1_GAUL    | Admin 1 name in GAUL                                          |
    | NAM_1_STAT    | Admin 1 name as listed in the Statoids database               |
    | NAM_1_SRCE    | Admin 1 name from original data source (SALB, UN HDX, etc.)   |
    | NAM_1_NTVE    | Admin 1 name in the native language                           |
    | NAM_1_WIKI    | Admin 1 name used in Wikipedia articles                       |
    | NAM_2_GAUL    | Admin 2 name in GAUL                                          |
    | NAM_2_STAT    | Admin 2 name as listed in the Statoids database               |
    | NAM_2_SRCE    | Admin 2 name from original data source (SALB, UN HDX, etc.)   |
    | NAM_2_NTVE    | Admin 2 name in the native language                           |
    | NAM_2_WIKI    | Admin 2 name used in Wikipedia articles                       |
    | P_CODE_1      | P-Code for ADM1 from UN HDX Global P-Code List                |
    | P_CODE_1_t    | Temporary P-Code for ADM1 (when official not available)       |
    | P_CODE_1_c    | Complete list of Adm1 P_Codes                                 |
    | P_NAME_1      | Name for ADM1 from UN HDX Global P-Code List                  |
    | P_CODE_2      | P-Code for ADM2 from UN HDX Global P-Code List                |
    | P_CODE_2_t    | Temporary P-Code for ADM2 (when official not available)       |
    | P_CODE_2_c    | Complete list of Adm2 P_Codes                                 |
    | P_NAME_2      | Name for ADM2 from UN HDX Global P-Code List                  |
    | ADM1CD        | ADM1 code from SALB dataset                                   |
    | ADM1CD_t      | Temporary ADM1 code based on SALB methodology                 |
    | ADM1NM        | Name for ADM1 from SALB dataset                               |
    | ADM2CD        | ADM2 code from SALB dataset                                   |
    | ADM2CD_t      | Temporary ADM2 code based on SALB methodology                 |
    | ADM2NM        | Name for ADM2 from SALB dataset                               |
    | P_DATE        | "Valid from" date accompanying P-Code and name                |
    | SALB_DATE     | Temporal validity for codes/geometry from SALB dataset        |

    </center>

!!! note
    If ADM2CD_c is the same as ADM1CD_c (and P_CODE_1_c is the same as P_CODE_2_c), the country does not distinguish between administrative level 1 and 2, and the polygon geometries are identical.

#### Earth Engine Snippet

```js
var WB_Boundaries_ADM0 = ee.FeatureCollection("projects/sat-io/open-datasets/WORLD-BANK/WBGAD/WB_GAD_ADM0");
var WB_Boundaries_ADM1 = ee.FeatureCollection("projects/sat-io/open-datasets/WORLD-BANK/WBGAD/WB_GAD_ADM1");
var WB_Boundaries_ADM2 = ee.FeatureCollection("rojects/sat-io/open-datasets/WORLD-BANK/WBGAD/WB_GAD_ADM2");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/WB-GAD-2025

#### License

The World Bank Official Boundaries are available under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** license. Users are free to:

Produced and maintained by: World Bank Development Data Group

Curated in Earth Engine by: Samapriya Roy

Keywords: World Bank, Administrative boundaries, Geospatial data, Subnational boundaries, Space2Stats, Development indicators, SALB, P-Codes, GAUL, Official boundaries

Last updated on GEE: 2025-11-02
