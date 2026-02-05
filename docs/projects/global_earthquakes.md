# USGS Global Earthquake dataset
The USGS Earthquake Hazards Program (EHP) offers a comprehensive earthquake dataset, serving as a valuable resource for monitoring, research, and earthquake preparedness worldwide. This dataset encompasses information about earthquakes from various sources, including seismic stations, satellite imagery, and ground-based observations. Continuously updated, it contains a staggering collection of millions of records of earthquakes from daily aggregates.

The USGS earthquake dataset serves a multitude of purposes, including earthquake hazard assessment, which aids in identifying earthquake-prone regions and evaluating potential impacts on communities. Additionally, it supports the development of earthquake early warning systems, enabling timely alerts to mitigate disaster. Furthermore, the dataset is instrumental in the creation of earthquake preparedness and response plans, enhancing community resilience. Lastly, it fuels earthquake research endeavors, facilitating investigations into earthquake hazards and mitigation strategies.

#### Dataset processing

Since exports were allowed in specific chunks I wrote a program to fetch these over periods starting from 1923-2026. This can be updated since the records extend all the way to 1900 and only earthquakes greater than 2.5 and those reviewed were selected.

#### Dataset Citation

```
U.S. Geological Survey (USGS). (YEAR). Earthquake Hazards Program (EHP). Retrieved from https://earthquake.usgs.gov/earthquakes
```

??? example "Expand to show yearly counts"

    <center>

    | Year | Earthquake Count |
    |------|-----------------|
    | 1923 | 129 |
    | 1924 | 132 |
    | 1925 | 166 |
    | 1926 | 275 |
    | 1927 | 310 |
    | 1928 | 310 |
    | 1929 | 314 |
    | 1930 | 296 |
    | 1931 | 304 |
    | 1932 | 512 |
    | 1933 | 877 |
    | 1934 | 609 |
    | 1935 | 691 |
    | 1936 | 580 |
    | 1937 | 510 |
    | 1938 | 565 |
    | 1939 | 485 |
    | 1940 | 523 |
    | 1941 | 453 |
    | 1942 | 455 |
    | 1943 | 394 |
    | 1944 | 348 |
    | 1945 | 285 |
    | 1946 | 526 |
    | 1947 | 672 |
    | 1948 | 580 |
    | 1949 | 594 |
    | 1950 | 604 |
    | 1951 | 506 |
    | 1952 | 861 |
    | 1953 | 797 |
    | 1954 | 842 |
    | 1955 | 575 |
    | 1956 | 689 |
    | 1957 | 637 |
    | 1958 | 595 |
    | 1959 | 734 |
    | 1960 | 1147 |
    | 1961 | 884 |
    | 1962 | 1028 |
    | 1963 | 1308 |
    | 1964 | 1174 |
    | 1965 | 1304 |
    | 1966 | 1163 |
    | 1967 | 1282 |
    | 1968 | 1677 |
    | 1969 | 1777 |
    | 1970 | 1549 |
    | 1971 | 2415 |
    | 1972 | 1836 |
    | 1973 | 5401 |
    | 1974 | 6729 |
    | 1975 | 8844 |
    | 1976 | 7636 |
    | 1977 | 6815 |
    | 1978 | 6931 |
    | 1979 | 8215 |
    | 1980 | 9680 |
    | 1981 | 7846 |
    | 1982 | 8519 |
    | 1983 | 10409 |
    | 1984 | 9374 |
    | 1985 | 10312 |
    | 1986 | 12342 |
    | 1987 | 10897 |
    | 1988 | 11112 |
    | 1989 | 12308 |
    | 1990 | 12215 |
    | 1991 | 12713 |
    | 1992 | 19893 |
    | 1993 | 16333 |
    | 1994 | 17042 |
    | 1995 | 18667 |
    | 1996 | 18669 |
    | 1997 | 17459 |
    | 1998 | 19308 |
    | 1999 | 19594 |
    | 2000 | 18373 |
    | 2001 | 20627 |
    | 2002 | 23650 |
    | 2003 | 24515 |
    | 2004 | 27467 |
    | 2005 | 31323 |
    | 2006 | 32478 |
    | 2007 | 30999 |
    | 2008 | 33041 |
    | 2009 | 15582 |
    | 2010 | 25040 |
    | 2011 | 23288 |
    | 2012 | 19960 |
    | 2013 | 20577 |
    | 2014 | 28581 |
    | 2015 | 27034 |
    | 2016 | 25250 |
    | 2017 | 22876 |
    | 2018 | 39948 |
    | 2019 | 26645 |
    | 2020 | 32232 |
    | 2021 | 28662 |
    | 2022 | 26892 |
    | 2023 | 27283 |
    | 2024 | 24798 |
    | 2025 | 28457 |
    | 2026 | 1151 |

    </center>


![usgs_eq](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/d5c9496c-1797-4466-bfd1-62edcef5053a)

#### Earth Engine Snippet

```js
var usgs_earthquakes = ee.FeatureCollection("projects/sat-io/open-datasets/USGS/usgs_earthquakes");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:/global-events-layers/USGS-EARTHQUAKES

#### License

These datasets are public domain data with no use restrictions, though if modifications or derivatives of the product(s) are created, then please add some descriptive modifier to the data set to avoid confusion

#### Changelog
- Updated earthquake datasets till 2026-02-05
- Updated earthquake datasets till 2025-06-06
- Updated earthquake datasets till 2024-07-28

Provided by: USGS

Curated in GEE by: Samapriya Roy

Last updated: 2026-02-05
