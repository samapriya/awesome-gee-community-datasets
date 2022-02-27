# NOAA Sea-Level Rise Digital Elevation Models (DEMs)

The NOAA Coastal Services Center has developed high-resolution digital elevation models (DEMs) for use in the Center's Sea Level Rise and Coastal Flooding Impacts internet mapping application. These DEMs serve as source datasets used to derive data to visualize the impacts of inundation resulting from sea level rise along the coastal United States and its territories.

These data were created as part of the National Oceanic and Atmospheric Administration Coastal Services Center's efforts to create an online mapping viewer called the Sea Level Rise and Coastal Flooding Impacts Viewer. It depicts potential sea level rise and its associated impacts on the nation's coastal areas. The purpose of the mapping viewer is to provide coastal managers and scientists with a preliminary look at sea level rise (slr) and coastal flooding impacts. The viewer is a screening-level tool that uses nationally consistent data sets and analyses. Data and maps provided can be used at several scales to help gauge trends and prioritize actions for different scenarios. The [Sea Level Rise and Coastal Flooding Impacts Viewer may be accessed here](http://www.csc.noaa.gov/slr)

URL(s) of [dataset description can be found here](https://coast.noaa.gov/digitalcoast/tools/slr.html) and the dataset can be [downloaded here](https://coast.noaa.gov/slrdata/)

Disclaimer: Whole or parts of the dataset description was provided by the author(s) or their works.

#### Preprocessing
While the datasets were collected and made available from NOAA different collects do have varying nominal resolutions , different CRS and different no data values. While GEE collections will allow for variable values for all of those, the nominal resolution and native CRS was left intact was no data value was reprocessed to -9999 by simply using gdalwarp. I have added a function onto the example script which allows you to add the nominal scale as a property to the collection incase the user would like to split and apply different methods on top.

![slrdem](https://user-images.githubusercontent.com/6677629/155890474-b2fe6e10-58d7-4d67-b251-98e47100868b.gif)

#### Earth Engine Snippet

```js
var slrdem = ee.ImageCollection("projects/sat-io/open-datasets/NOAA/SLR_DEM");
```

Sample Code: https://code.earthengine.google.com/716e711368f4df16a5f61356691cb610

#### License
The dataset is released under an assumed CC0 1.0 Universal (CC0 1.0) Public Domain Dedication. There are no restrictions on the use of data received from the U.S. Geological Survey's Earth Resources Observation and Science (EROS) Center or NASA's Land Processes Distributed Active Archive Center (LP DAAC), unless expressly identified prior to or at the time of receipt. Depending on the product source, we request that the following statements be used when citing, copying, or reprinting data: Data available from the U.S. Geological Survey.

Provider:  NOAA

Curated by: Samapriya Roy

Keywords: Elevation, topography, topobathymetric, bathymetry, SLR, DEM, sea level rise

Last updated on GEE: 2022-02-27
