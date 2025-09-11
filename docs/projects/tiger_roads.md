# TIGER Roads Time Series (2012-2025)

The TIGER (Topologically Integrated Geographic Encoding and Referencing) Roads time series dataset provides a comprehensive collection of United States road networks from 2012 to 2025, representing one of the most important foundational geospatial datasets in the digital mapping ecosystem. Developed and maintained by the U.S. Census Bureau, this dataset forms the backbone of countless mapping applications, navigation systems, and geospatial analyses across the United States.

TIGER Roads represents the most comprehensive, authoritative, and publicly available road network dataset for the United States. Each annual release contains millions of road segment features covering all 50 states, the District of Columbia, Puerto Rico, and U.S. Island Areas. The dataset's topological structure ensures that every road segment is properly connected to the broader network, enabling sophisticated routing and network analysis applications.

The time series reveals the ongoing evolution and refinement of this critical dataset. Rather than simple growth, the data shows a story of quality improvement and methodological enhancement, with feature counts declining from nearly 20 million in 2012 to approximately 16.4 million in 2025 as the Census Bureau consolidates redundant features and improves data topology.

#### Feature Count Evolution

| Year | Number of Road Features | Change from Previous Year |
|------|------------------------|---------------------------|
| 2012 | 19,889,811 | - |
| 2013 | 19,655,632 | -234,179 |
| 2014 | 19,609,146 | -46,486 |
| 2015 | 19,531,817 | -77,329 |
| 2016 | 19,401,722 | -130,095 |
| 2017 | 18,800,412 | -601,310 |
| 2018 | 18,315,773 | -484,639 |
| 2019 | 18,123,446 | -192,327 |
| 2020 | 18,009,370 | -114,076 |
| 2021 | 18,004,254 | -5,116 |
| 2022 | 17,979,848 | -24,406 |
| 2023 | 17,900,582 | -79,266 |
| 2024 | 17,813,006 | -87,576 |
| 2025 | 16,438,449 | -1,374,557 |

**Total Change (2012-2025): -3,451,362 features (-17.4%)**

The declining feature count reflects ongoing data quality improvements through conflation processes, where redundant or duplicate road segments are merged, topology is corrected, and the overall dataset structure is refined.

#### Technical Specifications

#### Feature Properties

Each road segment contains detailed attribute information that enables sophisticated address matching and routing operations:

| Property | Description | Example Value |
|----------|-------------|---------------|
| **FULLNAME** | Complete concatenated road name with all components | "I- 395" |
| **LINEARID** | Unique linear feature identifier used across TIGER products | "1104469410451" |
| **MTFCC** | MAF/TIGER Feature Class Code indicating road functional classification | "S1100" |
| **NAME** | Base street name or route number without directionals or types | "395" |
| **PREDIR** | Prefix directional (North, South, East, West) | null |
| **PREQUAL** | Prefix qualifier (Old, New, etc.) | null |
| **PRETYP** | Prefix type (State Route, County Road, etc.) | "344" |
| **RTTYP** | Route type classification for numbered highway systems | "I" |
| **SUFDIR** | Suffix directional (North, South, East, West) | null |
| **SUFQUAL** | Suffix qualifier | null |
| **SUFTYP** | Suffix type (Street, Avenue, Road, etc.) | null |

#### Route Type (RTTYP) Classifications

The route type code (RTTYP) describes the type of road for numbered highway systems:

| Code | Description |
|------|-------------|
| **C** | County Road |
| **I** | Interstate Highway |
| **M** | Common Name |
| **O** | Other |
| **S** | State Recognized Highway |
| **U** | U.S. Highway |

### MTFCC Road Classifications

| Code | Description | Typical Use |
|------|-------------|-------------|
| S1100 | Primary Road | Interstate highways, major arterials |
| S1200 | Secondary Road | State highways, major collectors |
| S1400 | Local Neighborhood Road | Residential streets, local roads |
| S1500 | Vehicular Trail | Unpaved roads, 4WD trails |

#### Earth Engine Assets

The complete time series is available in Google Earth Engine under the following asset structure:

```
projects/sat-io/open-datasets/TIGER/[YEAR]/Roads
```

Where [YEAR] ranges from 2012 to 2025.

![tigerroads](../images/tiger_roads.png)

#### Earth Engine Snippet

```javascript
// Load and visualize TIGER Roads for a specific year
var year = 2025;
var roads = ee.FeatureCollection("projects/sat-io/open-datasets/TIGER/" + year + "/Roads");

// Style roads with basic blue color
var styled = roads.style({color: '#4285F4', width: 1});

// Center map on New York City
Map.setCenter(-73.99172, 40.74101, 12);
Map.addLayer(styled, {}, 'TIGER/' + year + '/Roads');
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/TIGER-ROADS-MULTIYEAR

#### Citation

```
U.S. Census Bureau. TIGER/Line Shapefiles [Year]. Washington, DC: U.S. Census Bureau.
Available at: https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html
```

#### License

The U.S. Census Bureau offers some of its public data in machine-readable format via an Application Programming Interface (API). All of the content, documentation, code and related materials made available through the API are subject to [these terms and conditions](https://www.census.gov/data/developers/about/terms-of-service.html)

Keywords : TIGER, Roads, Transportation, Infrastructure, Time Series, U.S. Census Bureau, Network Analysis, Routing, Navigation, GIS, Temporal Analysis, National Mapping

Created by: U.S. Census Bureau

Curated for GEE by: Noah Weidig and Samapriya Roy

Last Updated :2025-09-11
