# Applied Climate Information System (ACIS) NRCC NN

The ACIS Climate Maps are produced daily using data from the Applied Climate Information System (ACIS) at a 5-km (0.04-deg x 0.04-deg) spatial
resolution from 1951-present, updated every 1-2 weeks.You can find additiona [information here](https://www.rcc-acis.org/examples.html) and the [Climate Engine org dataset page](https://support.climateengine.org/article/47-acis-nrcc-nn). Station data in ACIS primarily come from the following networks:

- National Weather Service Cooperative Observer Program (NWS COOP)
- Weather-Bureau-Army-Navy/Automated Surface Observing System (WBAN/ASOS)
- Snow Telemetry (SNOTEL)
- Community Collaborative Rain, Hail, & Snow (CoCoRaHS) Network
- Remote Automatic Weather Stations (RAWS)

Note: All near-real-time data are considered preliminary and subject to change.

#### Dataset Description

**Spatial Information**

| Parameter            | Value                     |
|----------------------|---------------------------|
| Spatial extent       | Conterminous United States |
| Spatial resolution   | 5-km (0.04-deg x 0.04-deg)|
| Temporal resolution  | Daily                     |
| Time span            | 1951-01-01 to present     |
| Update frequency     | 1-2 weeks                 |

**Variables**

| Variable                  | Details                              |
|---------------------------|--------------------------------------|
| Minimum temperature, 2m ('tmax') | - Units: Degrees Fahrenheit            |
|                           | - Scale factor: 1.0                    |
| Maximum temperature, 2m ('tmin') | - Units: Degrees Fahrenheit            |
|                           | - Scale factor: 1.0                    |
| Precipitation ('precip')  | - Units: Inches                        |
|                           | - Scale factor: 1.0                    |

#### Earth Engine Snippet if dataset already in GEE

```js
// Read in Image Collection and get first image
var acis_nrcc_nn_ic = ee.ImageCollection('projects/climate-engine-pro/assets/noaa-nrcc-acis-nn/daily')
var acis_nrcc_nn_i = acis_nrcc_nn_ic.first()

// Print first image to see bands
print(acis_nrcc_nn_i)

// Visualize each band from first image
var prec_palette = ["#ffffcc", "#c7e9b4", "#7fcdbb", "#41b6c4", "#1d91c0", "#225ea8", "#0c2c84"]
var temp_palette = ["#b2182b", "#ef8a62", "#fddbc7", "#f7f7f7", "#d1e5f0", "#67a9cf", "#2166ac"].reverse()
Map.addLayer(acis_nrcc_nn_i.select('precip'), {min: 0, max: 0.5, palette: prec_palette}, 'precip')
Map.addLayer(acis_nrcc_nn_i.select('tmin'), {min: -10, max: 50, palette: temp_palette}, 'tmin')
Map.addLayer(acis_nrcc_nn_i.select('tmax'), {min: -10, max: 50, palette: temp_palette}, 'tmax')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/NOAA-NRCC-ACIS

#### License

NOAA data, information, and products, regardless of the method of delivery, are not subject to copyright and carry no restrictions on their subsequent use by the public. Once obtained, they may be put to any lawful use. The forgoing data is in the public domain and is being provided without restriction on use and distribution. For more information visit the NWS disclaimer site.

Keywords: climate, precipitation, temperature, NOAA, reanalysis, CONUS, daily, near real-time

Dataset provider: NOAA

Curated in GEE by: Climate Engine Org
