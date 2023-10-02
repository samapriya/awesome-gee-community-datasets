# Forecast Reference Crop Evapotranspiration (FRET)

The National Weather Service is now producing Forecast Reference Crop Evapotranspiration (FRET), a forecast estimate of the amount of evapotranspiration for a well-watered reference crop (grass or alfalfa) under prescribed conditions for a 24 hour period. Weekly FRET forecast calculations and NLDAS derived reference crop ET Climatology and departure from normal are available as well. The Forecast Reference Evapotranspiration (FRET) are for a short canopy (or 12cm grasses). The short canopy ET values are calculated using the Penman-Monteith Reference Evapotranspiration Equations, adopted by the Environmental Water Resources Institute - American Society of Civil engineers (ASCE-EWRI, 2004), and the National Weather Service forecast of temperatures, relative humidity, wind, and cloud cover. This product will be issued daily by 8 am local time, year round. You can get additional information [about the dataset here](https://ams.confex.com/ams/93Annual/webprogram/Handout/Paper223261/FRET_AMS2013.pdf) and [here](https://www.weather.gov/cae/fretinfo.html). You can further find information about [this on the climate engine org data page](https://support.climateengine.org/article/62-fret).

#### Dataset Description

**Spatial Information**

| Parameter            | Value                          |
|----------------------|--------------------------------|
| Spatial extent       | Conterminous United States     |
| Spatial resolution   | 4000 m (1/24-deg)              |
| Temporal resolution  | Daily                          |
| Time span            | Next 1-7 days (updated every hour) |
| Update frequency     | Hourly                         |

**Variables**

| Variable                  | Details                              |
|---------------------------|--------------------------------------|
| ASCE Grass Reference Evapotranspiration (ETo) | - Units: Millimeters                |
|                           | - Scale factor: 1.0                  |

#### Citation

```
Palmer, C., Osborne, H., Krone-Davis, P., Melton, F., & Hobbins, M. National Weather Service–Forecast Reference Evapotranspiration (FRET).
```

![fret](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/6a52aa99-a363-4073-b36c-6eac75ac6978)

#### Earth Engine Snippet

```js
// Read in Image Collection and get single image
var fret_ic = ee.ImageCollection('projects/climate-engine/fret/forecast/eto')
var fret_i = fret_ic.first()

// Print image to see bands
print(fret_i)

// Visualize a single image
var fret_palette = ["#ffffb2", "#fed976", "#feb24c", "#fd8d3c", "#fc4e2a", "#e31a1c", "#b10026"]
Map.addLayer(fret_i, {min:0, max:10, palette: fret_palette}, 'fret_i')
```

Sample Code : https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/US-FRET

#### License

NOAA data, information, and products, regardless of the method of delivery, are not subject to copyright and carry no restrictions on their subsequent use by the public. Once obtained, they may be put to any lawful use. The forgoing data is in the public domain and is being provided without restriction on use and distribution. For more information visit the NWS disclaimer site.

Keywords: drought, aridity, evaporative demand, ASCE, evapotranspiration, climate, forecast, CONUS, United States

Provided by: NOAA

Curated in GEE by: Climate Engine Org
