# USGS Global Earthquake dataset
The USGS Earthquake Hazards Program (EHP) offers a comprehensive earthquake dataset, serving as a valuable resource for monitoring, research, and earthquake preparedness worldwide. This dataset encompasses information about earthquakes from various sources, including seismic stations, satellite imagery, and ground-based observations. Continuously updated, it contains a staggering collection of millions of records of earthquakes from daily aggregates.

The USGS earthquake dataset serves a multitude of purposes, including earthquake hazard assessment, which aids in identifying earthquake-prone regions and evaluating potential impacts on communities. Additionally, it supports the development of earthquake early warning systems, enabling timely alerts to mitigate disaster. Furthermore, the dataset is instrumental in the creation of earthquake preparedness and response plans, enhancing community resilience. Lastly, it fuels earthquake research endeavors, facilitating investigations into earthquake hazards and mitigation strategies.

#### Dataset processing

Since exports were allowed in specific chunks I wrote a program to fetch these over periods starting from 1923-2024. This can be updated since the records extend all the way to 1900 and only earthquakes greater than 2.5 and those reviewed were selected.

#### Dataset Citation

```
U.S. Geological Survey (USGS). (YEAR). Earthquake Hazards Program (EHP). Retrieved from https://earthquake.usgs.gov/earthquakes
```

??? example "Expand to show yearly counts"

    <center>

    | Year | Value |
    |------|-------|
    | 1923 | 129   |
    | 1924 | 132   |
    | 1925 | 162   |
    | 1926 | 276   |
    | 1927 | 310   |
    | 1928 | 310   |
    | 1929 | 314   |
    | 1930 | 296   |
    | 1931 | 304   |
    | 1932 | 513   |
    | 1933 | 877   |
    | 1934 | 609   |
    | 1935 | 691   |
    | 1936 | 580   |
    | 1937 | 510   |
    | 1938 | 565   |
    | 1939 | 485   |
    | 1940 | 523   |
    | 1941 | 453   |
    | 1942 | 455   |
    | 1943 | 394   |
    | 1944 | 348   |
    | 1945 | 285   |
    | 1946 | 526   |
    | 1947 | 672   |
    | 1948 | 580   |
    | 1949 | 594   |
    | 1950 | 604   |
    | 1951 | 506   |
    | 1952 | 861   |
    | 1953 | 797   |
    | 1954 | 842   |
    | 1955 | 575   |
    | 1956 | 688   |
    | 1957 | 637   |
    | 1958 | 595   |
    | 1959 | 734   |
    | 1960 | 1147  |
    | 1961 | 884   |
    | 1962 | 1028  |
    | 1963 | 1308  |
    | 1964 | 1076  |
    | 1965 | 1225  |
    | 1966 | 1070  |
    | 1967 | 1202  |
    | 1968 | 1543  |
    | 1969 | 1685  |
    | 1970 | 1492  |
    | 1971 | 2129  |
    | 1972 | 1596  |
    | 1973 | 5386  |
    | 1974 | 6721  |
    | 1975 | 8823  |
    | 1976 | 7621  |
    | 1977 | 6808  |
    | 1978 | 6929  |
    | 1979 | 8207  |
    | 1980 | 9663  |
    | 1981 | 7831  |
    | 1982 | 8514  |
    | 1983 | 10402 |
    | 1984 | 9374  |
    | 1985 | 10312 |
    | 1986 | 12341 |
    | 1987 | 10896 |
    | 1988 | 11111 |
    | 1989 | 12307 |
    | 1990 | 12213 |
    | 1991 | 12713 |
    | 1992 | 19893 |
    | 1993 | 16333 |
    | 1994 | 17041 |
    | 1995 | 18667 |
    | 1996 | 18669 |
    | 1997 | 17459 |
    | 1998 | 19307 |
    | 1999 | 19594 |
    | 2000 | 18373 |
    | 2001 | 20627 |
    | 2002 | 23647 |
    | 2003 | 24515 |
    | 2004 | 27466 |
    | 2005 | 31323 |
    | 2006 | 32478 |
    | 2007 | 30997 |
    | 2008 | 33039 |
    | 2009 | 15618 |
    | 2010 | 25037 |
    | 2011 | 23285 |
    | 2012 | 19939 |
    | 2013 | 20559 |
    | 2014 | 28577 |
    | 2015 | 27015 |
    | 2016 | 25233 |
    | 2017 | 22860 |
    | 2018 | 37558 |
    | 2019 | 26600 |
    | 2020 | 32212 |
    | 2021 | 28650 |
    | 2022 | 26916 |
    | 2023 | 27291 |
    | 2024 | 13528 |

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
- Updated earthquake datasets till 2024-07-28

Provided by: USGS

Curated in GEE by: Samapriya Roy

Last updated: 2024-07-28
