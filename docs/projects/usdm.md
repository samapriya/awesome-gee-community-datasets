# United States Drought Monitor

The U.S. Drought Monitor is a map released every Thursday, showing parts of the U.S. that are in drought. The map uses five classifications: abnormally dry (D0), showing areas that may be going into or are coming out of drought, and four levels of drought: moderate (D1), severe (D2), extreme (D3) and exceptional (D4).

The Drought Monitor has been a team effort since its inception in 1999, produced jointly by the National Drought Mitigation Center (NDMC) at the University of Nebraska-Lincoln, the National Oceanic and Atmospheric Administration (NOAA), and the U.S. Department of Agriculture (USDA). The NDMC hosts the web site of the drought monitor and the associated data, and provides the map and data to NOAA, USDA and other agencies. It is freely available at droughtmonitor.unl.edu.

Unlike most of the weather maps people see in the news, the U.S. Drought Monitor is not a forecast. In fact, it looks backward. It’s a weekly assessment of drought conditions, based on how much precipitation did or didn’t fall, up to the Tuesday morning before the map comes out. That gives authors about two working days to review the latest data. If a lot of rain falls in a drought area on a Wednesday, the soonest drought would be removed from the map is the following week. Drought is a slow-moving hazard, so you can be certain that an area will still be in drought if it doesn’t get rain. But it also may take more than one good rainfall to end a drought, especially if an area has been in drought for a long time.

![drought_large](https://user-images.githubusercontent.com/6677629/115971804-31e3bb00-a510-11eb-80db-cab7cd0e77fb.gif)

#### Preprocessing
Drought Monitor GIS Data is [available as shapefiles](https://droughtmonitor.unl.edu/Data/GISData.aspx). To create a consistent data structure, the shapefiles are ingested for all years starting from 2000 and with a weekly cadence. These have 5 different drought classes/categories and are converted into a raster with the DM(Drought Monitor class/category values) as raster property. This makes using it as collection and analysis of the data much easier. Start and end dates are added with the release week date as the end date and a week ago as a start date. **For now the goal is to keep this collection updated so that this dataset is consistently synced with the source dataset.**

#### Earth Engine Snippet

```js
var usdm = ee.ImageCollection("projects/sat-io/open-datasets/us-drought-monitor");
```

#### Drought Categories

![drought_categories](https://user-images.githubusercontent.com/6677629/115967546-ccd09b00-a4f8-11eb-9ca9-e969f58f0085.png)

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/UNITED-STATES-DROUGHT-MONITOR

Earth Engine App: https://sat-io.earthengine.app/view/usdm-explorer

#### License
The work is licensed under an Open data license for use.

```
The U.S. Drought Monitor is jointly produced by the National Drought Mitigation Center
at the University of Nebraska-Lincoln, the United States Department of Agriculture
and the National Oceanic and Atmospheric Administration. Map courtesy of NDMC.
```

Produced by : National Drought Mitigation Center at the University of Nebraska-Lincoln, the United States Department of Agriculture, and the National Oceanic and Atmospheric Administration. Map courtesy of NDMC

Processed secondary/formatted & Curated by: Samapriya Roy

Keywords: :"National Drought Mitigation Center, NDMC, Drought, University of Nebraska-Lincoln, United States Department of Agriculture, USDA, National Oceanic and Atmospheric Administration, NOAA, USDM"

Last updated: 2021-04-24
