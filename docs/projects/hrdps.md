# High Resolution Deterministic Prediction System (HRDPS)

The High Resolution Deterministic Prediction System (HRDPS) provides useful numerical simulations of temperature over large areas. Climate Engine is ingesting only the band containing temperature at 2m above ground level, but HRDPS also produces bands for precipitation, cloud cover, wind speed and direction, humidity, and others. These numerical simulations can be used for air quality modeling and forecasting, climate and wildfire modeling, and extreme weather forecasting. Users who will benefit most from using these new data are those for whom a detailed forecast of surface temperatures and winds is important. The 2.5 km forecasts could add much value especially during the change of seasons and in wintertime when rapid changes in temperature and winds cause phase transitions of precipitation (freezing rain to snow to rain for example). HRDPS is the high resolution counterpart to the RDPS dataset. You can additional [information here](https://weather.gc.ca/grib/grib2_HRDPS_HR_e.html) and on the [climate engine org dataset page](https://support.climateengine.org/article/68-hrdps).

#### Dataset Description

**Spatial Information**

| Parameter            | Value                     |
|----------------------|---------------------------|
| Spatial extent       | Canada                    |
| Spatial resolution   | 2.5 km grid (1/24 deg)   |
| Temporal resolution  | Daily                     |
| Time span            | 2015-04-23 to present     |
| Update frequency     | Updated daily with 1 day lag time |

**Variables**

| Variable                  | Details                              |
|---------------------------|--------------------------------------|
| Mean temperature ('Tavg') | - Units: Degrees Celsius                    |
|                           | - Scale factor: 1.0                    |

#### Citation

```
Milbrandt, J. A., Bélair, S., Faucher, M., Vallée, M., Carrera, M. L., & Glazer, A. (2016). The pan-Canadian high resolution (2.5 km) deterministic
prediction system. Weather and Forecasting, 31(6), 1791-1816.
```

![hrdps](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/c56f1612-fbcd-4ae6-a1b7-26f190c3b120)

#### Earth Engine Snippet

```js
// Read in Image Collection and get first image
var hrdps_ic = ee.ImageCollection('projects/climate-engine-pro/assets/ce-hrdps-daily')
var hrdps_i = hrdps_ic.first()

// Print first image to see bands
print(hrdps_i)

// Visualize temperature from first image
var temp_palette = ["#b2182b", "#ef8a62", "#fddbc7", "#f7f7f7", "#d1e5f0", "#67a9cf", "#2166ac"].reverse()
Map.addLayer(hrdps_i.select('Tavg'), {min: -10, max: 20, palette: temp_palette}, 'Tavg')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:/weather-climate/CE-HRDPS-DAILY


#### License

Data are subject to the Government of Canada Open Data Licence Agreement: https://open.canada.ca/en/open-government-licence-canada. The terms of this Agreement govern your use and reproduction of the data instead of the copyright reproduction statements found in Important Notices on the Agriculture and Agri-Food Canada website.

Keywords: climate, temperature, daily, Canada, near real-time

Dataset Provider: Environment and Climate Change Canada

Curated in GEE by: Climate Engine Org
