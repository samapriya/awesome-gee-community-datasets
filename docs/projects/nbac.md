# Canada National Burned Area Composite (NBAC)

The National Burned Area Composite (NBAC) is a GIS database and system that calculates the area of forest burned on a national scale for each year since 1986. The data are used to help estimate carbon emissions in Canada. The burned area is determined by evaluating a number of available sources of data, which use different techniques to map any given fire. The system chooses the best available source of data for each burned area and builds a national composite picture.

The NBAC is part of the Fire Monitoring, Accounting and Reporting System (FireMARS), jointly developed by the Canada Centre for Mapping and Earth Observation (formerly the Canada Centre for Remote Sensing) of Natural Resources Canada and the Canadian Forest Service. Initially, FireMARS was developed with funding support from the Canadian Space Agency Government Related Initiatives Program through a collaboration of those in fire research, forest carbon accounting and remote sensing.

Data are provided for NBAC from:
• Natural Resources Canada, and
• Provincial, Territorial, and Parks Canada agencies.

The NBAC can be used for spatial and temporal analyses of landscape-scale fire impacts. You can download the [datasets here](https://cwfis.cfs.nrcan.gc.ca/downloads/nbac/)

#### Supplemental Information
NBAC is a national product compiled annually since 1986 by the FireMARS system which tracks forest fires for annual estimates of carbon emissions and to help identify National Forest Inventory plots that may have been disturbed by fire. See the FireMARS website at (http://www.nrcan.gc.ca/forests/fire/13159) and carbon accounting - disturbance monitoring website (http://www.nrcan.gc.ca/forests/climate-change/13109) for additional information.

When using these data for mapping activities and analysis, research, evaluation or display, please acknowledged the source using the following citation:

Canadian Forest Service. National Burned Area Composite (NBAC). Natural Resources Canada, Canadian Forest Service, Northern Forestry Centre, Edmonton, Alberta. https://cwfis.cfs.nrcan.gc.ca/.

#### Citation

```
Skakun, R.; Castilla, G.; Metsaranta, J.; Whitman, E.; Rodrigue, S.; Little, J.; Groenewegen, K.; Coyle, M. (2022). Extending the National Burned
Area Composite Time Series of Wildfires in Canada. Remote Sensing, 14, 3050. DOI: https://doi.org/10.3390/rs14133050

Skakun, R.S.; Whitman, E.; Little, J.M.; and Parisien, M.-A. (2021). Area burned adjustments to historical wildland fires in Canada. Environmental
Research Letters 16 064014. DOI: https://doi.org/10.1088/1748-9326/abfb2c

Hall, R.J.; Skakun, R.S.; Metsaranta, J.M.; Landry, R.; Fraser, R.H.; Raymond, D.A.; Gartrell, J.M.; Decker, V. and Little, J.M. (2020). Generating
annual estimates of forest fire disturbance in Canada: the National Burned Area Composite. International Journal of Wildland Fire. 10.1071/WF19201.
DOI: https://doi.org/10.1071/WF19201
```

![nbac](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/f8be9c35-e2f4-4892-841a-fca1612aab0c)

#### Earth Engine Snippet

```js
var nbac_raster7223 = ee.Image("projects/sat-io/open-datasets/CA_FOREST/NBAC/NBAC_MRB_1972_to_2023");
var nbac7223 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/nbac_1972_2023_20240530");
var nbac_1972_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1972_20240530");
var nbac_1973_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1973_20240530");
var nbac_1974_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1974_20240530");
var nbac_1975_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1975_20240530");
var nbac_1976_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1976_20240530");
var nbac_1977_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1977_20240530");
var nbac_1978_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1978_20240530");
var nbac_1979_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1979_20240530");
var nbac_1980_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1980_20240530");
var nbac_1981_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1981_20240530");
var nbac_1982_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1982_20240530");
var nbac_1983_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1983_20240530");
var nbac_1984_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1984_20240530");
var nbac_1985_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1985_20240530");
var nbac_1986_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1986_20240530");
var nbac_1987_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1987_20240530");
var nbac_1988_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1988_20240530");
var nbac_1989_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1989_20240530");
var nbac_1990_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1990_20240530");
var nbac_1991_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1991_20240530");
var nbac_1992_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1992_20240530");
var nbac_1993_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1993_20240530");
var nbac_1994_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1994_20240530");
var nbac_1995_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1995_20240530");
var nbac_1996_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1996_20240530");
var nbac_1997_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1997_20240530");
var nbac_1998_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1998_20240530");
var nbac_1999_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_1999_20240530");
var nbac_2000_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2000_20240530");
var nbac_2001_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2001_20240530");
var nbac_2002_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2002_20240530");
var nbac_2003_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2003_20240530");
var nbac_2004_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2004_20240530");
var nbac_2005_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2005_20240530");
var nbac_2006_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2006_20240530");
var nbac_2007_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2007_20240530");
var nbac_2008_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2008_20240530");
var nbac_2009_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2009_20240530");
var nbac_2010_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2010_20240530");
var nbac_2011_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2011_20240530");
var nbac_2012_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2012_20240530");
var nbac_2013_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2013_20240530");
var nbac_2014_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2014_20240530");
var nbac_2015_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2015_20240530");
var nbac_2016_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2016_20240530");
var nbac_2017_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2017_20240530");
var nbac_2018_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2018_20240530");
var nbac_2019_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2019_20240530");
var nbac_2020_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2020_20240530");
var nbac_2021_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2021_20240530");
var nbac_2022_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2022_20240530");
var nbac_2023_20240530 = ee.FeatureCollection("projects/sat-io/open-datasets/CA_FOREST/NBAC/YEARLY/nbac_2023_20240530");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:fire-monitoring-analysis/CA-NATIONAL-BURNED-AREA-COMPOSITE


#### License

Open Government Licence - Canada (http://open.canada.ca/en/open-government-licence-canada). When using these data for mapping activities and analysis, research, evaluation or display, please acknowledged the source using the following citation: Canadian Forest Service. National Burned Area Composite (NBAC). Natural Resources Canada, Canadian Forest Service, Northern Forestry Centre, Edmonton, Alberta. https://cwfis.cfs.nrcan.gc.ca/.

#### Changelog
- Updated to include datasets from 1972 to 2023
- Updated yearly and net changes

Created by: Natural Resources Canada,Canadian Wildland Fire Information System

Curated in GEE by : Samapriya Roy

Keywords: canada,burned area,forestry,forest fire,wildfire

Last updated in GEE: 2025-02-17
