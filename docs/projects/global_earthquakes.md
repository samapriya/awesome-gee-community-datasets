# USGS Global Earthquake dataset
The USGS Earthquake Hazards Program (EHP) offers a comprehensive earthquake dataset, serving as a valuable resource for monitoring, research, and earthquake preparedness worldwide. This dataset encompasses information about earthquakes from various sources, including seismic stations, satellite imagery, and ground-based observations. Continuously updated, it contains a staggering collection of millions of records of earthquakes from daily aggregates.

The USGS earthquake dataset serves a multitude of purposes, including earthquake hazard assessment, which aids in identifying earthquake-prone regions and evaluating potential impacts on communities. Additionally, it supports the development of earthquake early warning systems, enabling timely alerts to mitigate disaster. Furthermore, the dataset is instrumental in the creation of earthquake preparedness and response plans, enhancing community resilience. Lastly, it fuels earthquake research endeavors, facilitating investigations into earthquake hazards and mitigation strategies.

#### Dataset processing

Since exports were allowed in specific chunks I wrote a program to fetch these over periods starting from 1923-2025. This can be updated since the records extend all the way to 1900 and only earthquakes greater than 2.5 and those reviewed were selected.

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
    | 1925 | 162 |
    | 1926 | 276 |
    | 1927 | 310 |
    | 1928 | 310 |
    | 1929 | 314 |
    | 1930 | 296 |
    | 1931 | 304 |
    | 1932 | 513 |
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
    | 1960 | 1,147 |
    | 1961 | 884 |
    | 1962 | 1,028 |
    | 1963 | 1,308 |
    | 1964 | 1,076 |
    | 1965 | 1,225 |
    | 1966 | 1,070 |
    | 1967 | 1,202 |
    | 1968 | 1,543 |
    | 1969 | 1,685 |
    | 1970 | 1,492 |
    | 1971 | 2,129 |
    | 1972 | 1,596 |
    | 1973 | 5,386 |
    | 1974 | 6,721 |
    | 1975 | 8,823 |
    | 1976 | 7,621 |
    | 1977 | 6,808 |
    | 1978 | 6,929 |
    | 1979 | 8,207 |
    | 1980 | 9,663 |
    | 1981 | 7,831 |
    | 1982 | 8,514 |
    | 1983 | 10,402 |
    | 1984 | 9,374 |
    | 1985 | 10,312 |
    | 1986 | 12,341 |
    | 1987 | 10,896 |
    | 1988 | 11,111 |
    | 1989 | 12,307 |
    | 1990 | 12,213 |
    | 1991 | 12,713 |
    | 1992 | 19,893 |
    | 1993 | 16,333 |
    | 1994 | 17,041 |
    | 1995 | 18,667 |
    | 1996 | 18,669 |
    | 1997 | 17,459 |
    | 1998 | 19,307 |
    | 1999 | 19,594 |
    | 2000 | 18,373 |
    | 2001 | 20,627 |
    | 2002 | 23,647 |
    | 2003 | 24,515 |
    | 2004 | 27,466 |
    | 2005 | 31,323 |
    | 2006 | 32,478 |
    | 2007 | 30,997 |
    | 2008 | 33,040 |
    | 2009 | 15,582 |
    | 2010 | 25,034 |
    | 2011 | 23,281 |
    | 2012 | 19,935 |
    | 2013 | 20,562 |
    | 2014 | 28,561 |
    | 2015 | 27,018 |
    | 2016 | 25,235 |
    | 2017 | 22,859 |
    | 2018 | 39,370 |
    | 2019 | 26,601 |
    | 2020 | 32,213 |
    | 2021 | 28,651 |
    | 2022 | 26,906 |
    | 2023 | 27,290 |
    | 2024 | 24,785 |
    | 2025 | 10,755 |

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
- Updated earthquake datasets till 2025-06-06
- Updated earthquake datasets till 2024-07-28

Provided by: USGS

Curated in GEE by: Samapriya Roy

Last updated: 2025-06-06
