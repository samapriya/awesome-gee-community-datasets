# USGS Historical Imagery Western US

This dataset contains an imagery base layer representing conditions from the mid-1950s across the western United States. We sourced the imagery from over 160,000 aerial images in the [USGS EROS Archive](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-aerial-photography-aerial-photo-single-frames) taken between 1940 and 1970, with the median acquisition date being 1954. The imagery provides complete coverage for 17 western U.S. states: Arizona, California, Colorado, Idaho, Kansas, Montana, North Dakota, Nebraska, New Mexico, Nevada, Oklahoma, Oregon, South Dakota, Texas, Utah, Washington, and Wyoming. Explore the dataset visually through our easy-to-use web map application at [LandscapeExplorer.org](https://LandscapeExplorer.org).

Find alternative methods of downloading and utilizing the imagery on our [data download](https://LandscapeExplorer.org/data) page.

We preprocessed the imagery in MATLAB to reduce image vignetting and improve image contrast. Orthorectification was performed in Metashape. The compiled imagery had varying Ground Sampling Distance values, ranging from 0.6 to 1.7 meters. The GEE dataset was written out at 1 meter GSD. Dive deeper into our data processing methods at our  [LandscapeExplorer.org development page](https://www.landscapeexplorer.org/about-landscape-explorer-faq/development-of-the-landscape-explorer-imagery/).

#### Additional Preprocessing
The feature collection had Dates in different formats everything from simply

<center>

| Format      |
|-------------|
| YYYY        |
| YYYY-MM/dd  |
| YYYYs       |
| YYYY-MM-dd  |

</center>

An approach was taken to convert and standardize these dates and add the corresponding dates as epoch system:time_start to features in the overall feature collection. This was then merged back into a feature collection with additional properties system:time_start, year, standardized_date. Based on the year metadata you can now get counts across multiple time periods I am summarizing a 5 year range distribution

<center>

| Year Range | Data Total |
|------------|------------|
| 1935-1939  | 2175       |
| 1940-1944  | 4380       |
| 1945-1949  | 31176      |
| 1950-1954  | 29966      |
| 1955-1959  | 25657      |
| 1960-1964  | 12347      |
| 1965-1969  | 12360      |
| 1970-1974  | 19623      |
| 1975-1979  | 14290      |
| 1980-1984  | 675        |
| 1985-1989  | 67         |

</center>

#### Citation

```
Morford, S.L., Allred, B.W., Jensen, E.R., Maestas, J.D., Mueller, K.R., Pacholski, C.L., Smith, J.T., Tack, J.D., Tackett, K.N. and Naugle, D.E.
(2023), Mapping tree cover expansion in Montana, U.S.A. rangelands using high-resolution historical aerial imagery. Remote Sens Ecol Conserv.
[https://doi.org/10.1002/rse2.357]( https://doi.org/10.1002/rse2.357)
```

![landscape_explorer](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/15743e82-4cce-440f-9a5a-d2b5f2fb5f35)

### Earth Engine Snippet

```js
var conusWest_imagery = ee.ImageCollection("projects/wlfw-um/assets/historical-imagery/conus-west");
var conusWest_metadata = ee.FeatureCollection("projects/wlfw-um/assets/historical-imagery/conus-west-seamlines");
var conusWest_metadata_with_date = ee.FeatureCollection("projects/sat-io/open-datasets/wlfm-um-extra/wlfm-um-seamlines");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:analysis-ready-data/USGS-HISTORICAL-AERIAL-IMAGERY

Sample app: https://sat-io.earthengine.app/view/landscape-explorer

#### License
These datasets are available under the [Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/)

Keywords: Aerial imagery, United States, Great Plains, Great Basin, Historical, photogrammetry

Provided by:  University of Montana, Lands for Wildlife, Montana NRCS and Intermountain West Joint Venture

Curated in GEE by: University of Montana, Lands for Wildlife, Montana NRCS and Intermountain West Joint Venture

Last updated: 2023-09-24
