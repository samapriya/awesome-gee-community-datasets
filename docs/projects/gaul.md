# Global Administrative Unit Layers (GAUL) 2024

The Global Administrative Unit Layers (GAUL) dataset is developed and owned by the Food and Agriculture Organization of the United Nations (FAO). It provides a comprehensive spatial dataset of sub-national administrative units for all countries in the world, consistent with the United Nations (UN) delineation of international boundaries.

GAUL 2024 includes two datasets: GAUL 2024 Subnational Level 1 (GAUL_2024_L1) and GAUL 2024 Subnational Level 2 (GAUL_2024_L2). The dataset was developed by consolidating national-level data from relevant sources, which involved editing geometries, standardizing attributes into a unified table structure, and preparing metadata for each country. You can find [the technical documentation here](https://openknowledge.fao.org/server/api/core/bitstreams/a400ec42-9ca7-46a3-a0ce-256de7d5ca94/content)

#### Data Sources

GAUL 2024 was compiled from multiple sources in order of priority:

1. Second Administrative Level Boundaries (SALB) geoportal - authoritative subnational boundary information managed by the UN Geographic Information Section
2. Humanitarian Data Exchange (HDX) platform - hosted by the Office for the Coordination of Humanitarian Affairs (OCHA)
3. National Providers - relevant national authorities identified through online research or FAO national representations
4. GAUL 2015 - used when no other data sources were available

#### Technical Details

- Coordinate System: WGS84 (EPSG:4326)
- Data structure: Seamless and topologically corrected geometries
- Coding system: Unique numeric codes within and across administrative levels
  - Country (level 0): 100-999
  - Level 1 unit: 1,000-99,999
  - Level 2 unit: 100,000-899,999
  - Waterbody: 900,000-999,000

#### Citation

```

Franceschini, G., Khan, A., Moretti, L., Nyabuti, K., Asif, M., Bezuidenhoudt, E. and Morteo, K. 2025. The Global Administrative Unit Layers (GAUL) 2024. Technical guidelines. Rome, FAO. https://doi.org/10.4060/cd4262en
```

#### Attributes

??? example "Expand to show attribute information for geometries"

    <center>

    | Field name   | Description                                          | Data type | Length |
    |--------------|------------------------------------------------------|-----------|--------|
    | iso3_code    | ISO3 code                                            | Text      | 3      |
    | map_code     | Map code – used for joining statistics               | Text      | 3      |
    | gaul0_code   | GAUL 2024 code at country level                      | Long      |        |
    | gaul0_name   | Name of administrative unit at country level         | Text      | 100    |
    | gaul1_code   | GAUL 2024 code at first level                        | Long      |        |
    | gaul1_name   | Name of administrative unit at first level           | Text      | 100    |
    | gaul2_code   | GAUL 2024 code at second level                       | Long      |        |
    | gaul2_name   | Name of administrative unit at second level          | Text      | 100    |
    | continent    | Name of the continent                                | Text      | 12     |
    | disp_en      | Display label in English                             | Text      | 255    |


![GAUL](https://github.com/user-attachments/assets/e7bff9fa-289c-41ed-9685-9d0161a0499a)

#### Earth Engine Snippet

```js
var GAUL_2024_L1 = ee.FeatureCollection("projects/sat-io/open-datasets/FAO/GAUL/GAUL_2024_L1");
var GAUL_2024_L2 = ee.FeatureCollection("projects/sat-io/open-datasets/FAO/GAUL/GAUL_2024_L2");
```

Sample Code:  https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/GAUL-2024

#### License

GAUL is available under the Creative Commons Attribution-4.0 International licence (CC BY 4.0). When using GAUL data, proper attribution must be given as follows: Some third-party data included in GAUL may have different terms of use. Users are responsible for checking and complying with any additional restrictions.


!!! note
    - GAUL 2024 should not be considered an authoritative or official representation of subnational boundaries. Its primary objective is to facilitate the representation of subnational statistics and attributes.
    - Country names in GAUL 2024 follow the Names of Countries and Territories (NOCS) database.
    - The dataset adopts the Latin alphabet to represent place names in their native languages, preserving accents and diacritics where applicable.
    - Some administrative units may be labeled as "Administrative unit not available" when the data is not available.
    - Waterbodies are included with unique code IDs greater than 900,000.

Produced and maintained by: Food and Agriculture Organization (FAO) of the United Nations

Curated in Earth Engine by: Samapriya Roy

Keywords: Administrative boundaries, Geospatial data, Subnational boundaries, FAO, Administrative units, International boundaries, Humanitarian data, SALB

Last updated: 2025-04-02
