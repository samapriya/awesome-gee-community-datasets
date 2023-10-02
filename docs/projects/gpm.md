# Global Precipitation Measurement (GPM)

Global Precipitation Measurement (GPM) is an international satellite mission to provide next-generation observations of rain and snow worldwide every three hours. NASA and the Japanese Aerospace Exploration Agency (JAXA) launched the GPM Core Observatory satellite on February 27th, 2014, carrying advanced instruments that set a new standard for precipitation measurements from space. The data they provide is used to unify precipitation measurements made by an international network of partner satellites to quantify when, where, and how much it rains or snows around the world. Note: Additional bands (‘HQprecipitation’, ‘IRprecipitation’, ‘precipitationUncal’, ‘randomError’) are provided with [documentation provided here](https://gpm.nasa.gov/sites/default/files/document_files/IMERG_ATBD_V06.pdf). You can find [additional information here](https://www.nasa.gov/mission_pages/GPM/overview/index.html) and [climate engine org dataset page here](https://support.climateengine.org/article/65-gpm-daily).

This dataset is derived from the Earth Engine asset, NASA/GPM_L3/IMERG_V06, using the processing steps:
1. The GPM Daily dataset hosted on Climate Engine is sourced from the 30-min data. These data are summed to daily based on 0 UTC time zone.
2. This collection contains provisional products that are regularly replaced with updated versions when the data become available. This transition typically occurs about 1-2 years out.

**Spatial Information**

| Parameter            | Value              |
|----------------------|--------------------|
| Spatial extent       | Global             |
| Spatial resolution   | 11-km (1/10-deg)   |
| Temporal resolution  | Daily              |
| Time span            | 2000-06-01 to present |
| Update frequency     | Updated daily with 2 day lag time |

**Variables**

| Variable                  | Details                              |
|---------------------------|--------------------------------------|
| Precipitation (Calibrated) - daily data is derived from 30-minute data ('precipitationCal') | - Units: Millimeters                    |
|                           | - Scale factor: 1.0                    |

#### Citation

```
Jackson, Gail & Berg, Wesley & Kidd, Chris & Kirschbaum, Dalia & Petersen, Walter & Huffman, George & Takayabu, Yukari. (2018). Global Precipitation Measurement (GPM): Unified Precipitation Estimation from Space. 10.1007/978-3-319-72583-3_7.
```

![GPM](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/a6822d72-6d68-499c-a7fd-b4f584172987)

#### Earth Engine Snippet

```js
// Read in Image Collections and get single image
var gpm_ic = ee.ImageCollection('projects/climate-engine-pro/assets/ce-gpm-imerg-daily')
var gpm_i = gpm_ic.first()

// Print single image to see bands
print(gpm_i)

// Visualize precipitation for single image
var prec_palette = ["#ffffcc", "#c7e9b4", "#7fcdbb", "#41b6c4", "#1d91c0", "#225ea8", "#0c2c84"]
Map.addLayer(gpm_i.select('precipitationCal'), {min: 0, max: 200, palette: prec_palette}, 'precipitationCal')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/GLOBAL-PRECIP-MEASUREMENT

#### License
NASA promotes the full and open sharing of all data with research and applications communities, private industry, academia, and the general public.

Keywords: precipitation, climate, NASA, JAXA, satellite, near real-time

Provided by: Climate Engine Org, NASA

Curated in GEE by: Climate Engine Org

