# Regional Deterministic Prediction System (RDPS)

The Regional Deterministic Prediction System (RDPS) carries out physics calculations to arrive at deterministic predictions of atmospheric elements
from the current day out to 48 hours into the future at a 10.0 km grid (1/11 deg) spatial resolution. The data for mean temperature covers North
America and is provided by the Meterological Service of Canada (MSC), a part of Environment and Climate Change Canada (ECCC). The MSC provides
weather forecasts and warnings 24 hours a day, 365 days a year. MSC also provides federal department, agencies and other levels of government with
information to support emergency preparedness and response to events such as storms, floods, wildfires and other weather-related emergencies. You can find [additional information here](https://eccc-msc.github.io/open-data/msc-data/nwp_rdps/readme_rdps-datamart_en) and also on the [climate org data page](https://support.climateengine.org/article/83-rdps).

#### Dataset Description

**Spatial Information**

| Parameter            | Value                           |
|----------------------|---------------------------------|
| Spatial extent       | United States and Canada        |
| Spatial resolution   | 10.0 km grid (1/11 deg)         |
| Temporal resolution  | Daily                           |
| Time span            | 2010-11-01 to present           |
| Update frequency     | Updated daily with 1 day lag time |

**Variables**

| Variable                  | Details                              |
|---------------------------|--------------------------------------|
| Mean temperature ('Tavg') | - Units: Degrees Celsius            |
|                           | - Scale factor: 1.0                  |

#### Citation

```
Fillion, L., Tanguay, M., Lapalme, E., Denis, B., Desgagne, M., Lee, V., ... & Pagé, C. (2010). The Canadian regional data assimilation and
forecasting system. Weather and Forecasting, 25(6), 1645-1669.
```

![rdps](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/7d1b3f1c-c0c6-4d7d-878d-91fdac9852ef)

#### Earth Engine Snippet

```js
// Read in Image Collection and get first image
var rdps_ic = ee.ImageCollection('projects/climate-engine-pro/assets/ce-rdps-daily')
var rdps_i = rdps_ic.first()

// Print first image to see bands
print(rdps_i)

// Visualize temperature from first image
var temp_palette = ["#b2182b", "#ef8a62", "#fddbc7", "#f7f7f7", "#d1e5f0", "#67a9cf", "#2166ac"].reverse()
Map.addLayer(rdps_i.select('Tavg'), {min: -10, max: 20, palette: temp_palette}, 'Tavg')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:/weather-climate/CE-RDPS-DAILY

#### License

Data are subject to the Government of Canada Open Data Licence Agreement: https://open.canada.ca/en/open-government-licence-canada. The terms of this Agreement govern your use and reproduction of the data instead of the copyright reproduction statements found in Important Notices on the Agriculture and Agri-Food Canada website.

Keywords: climate, daily, United States, Canada, daily, near real-time

Dataset provided by: Environment and Climate Change Canada

Dataset curated in GEE by: Climate Org
