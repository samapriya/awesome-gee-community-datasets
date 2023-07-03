# MOD10A2061 Snow Cover 8-Day L3 Global 500m

MOD10A2 is a snow cover data set from the Moderate Resolution Imaging Spectroradiometer (MODIS) on the Terra satellite. The data set consists of 1200 km by 1200 km tiles of 500 m resolution data gridded in a sinusoidal map projection. The data set reports the maximum snow cover extent during an eight-day period. The snow cover algorithm identifies snow-covered land and snow-covered ice on inland water. The algorithm uses a Normalized Difference Snow Index (NDSI) and other criteria tests. The eight-day compositing period was chosen because that is the exact ground track repeat period of the Terra and Aqua platforms.

| Parameter              | Description                                     | Values                       |
|------------------------|-------------------------------------------------|------------------------------|
| Maximum_Snow_Extent    | Maximum snow extent observed over an eight-day period. | 0: missing data<br>1: no decision<br>11: night<br>25: no snow<br>37: lake<br>39: ocean<br>50: cloud<br>100: lake ice<br>200: snow<br>254: detector saturated<br>255: fill |

#### Dataset details

Title: MODIS/Terra Snow Cover 8-Day L3 Global 500m SIN Grid
Author: Hall, D. K. and G. A. Riggs.
Publisher: NASA NSIDC DAAC: NASA National Snow and Ice Data Center Distributed Active Archive Center
Publication date: 2021-03-30T12:00:00Z
Publication place: Boulder, Colorado USA
Series: MOD10A2
Edition: 61
DOI: 10.5067/MODIS/MOD10A2.061
URL: https://doi.org/10.5067/MODIS/MOD10A2.061

#### Citation

```
Hall, D. K., V. V. Salomonson, and G. A. Riggs. "MODIS/Terra snow cover 8-day l3 global 500m grid, version 5." Tile h12v12]. Boulder, Colorado USA:
National Snow and Ice Data Center (2006).
```

#### Dataset Citation

```
Hall, D. K. and G. A. Riggs. 2021. MODIS/Terra Snow Cover 8-Day L3 Global 500m SIN Grid, Version 61. [Indicate subset used]. Boulder, Colorado USA.
NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MOD10A2.061. [Date Accessed]
```

![moda261_small](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/9efda5d3-dc7d-49cb-a698-14645491f969)

#### Earth Engine Snippet

```js
var MOD10A261 = ee.ImageCollection("projects/sat-io/open-datasets/MODIS/MOD10A261");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/GLOBAL-MOD10A261-Snow-Cover-8-Day

#### License

You may download and use photographs, imagery, or text from the NSIDC web site, unless limitations for its use are specifically stated. For more
information on usage and citing NSIDC datasets, please visit the NSIDC [Use and Copyright page](https://nsidc.org/about/data-use-and-copyright).

Curated in GEE by: Michael Lefsky and Samapriya Roy

Keywords: albedo, eight-day, 8-day, geophysical, global, modis, nasa, nsidc, snow, terra, mod10a2

Last updated: Last date the dataset was updated (if known)
