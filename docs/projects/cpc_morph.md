# Climate Prediction Center (CPC) Morphing Technique (MORPH)

The Satellite Precipitation - CMORPH Climate Data Record (CDR) consists of satellite precipitation estimates that have been bias corrected and
reprocessed using the Climate Prediction Center (CPC) Morphing Technique (MORPH) to form a global, high resolution precipitation analysis at a 25-km
(1/2-deg x 1/2-deg) spatial resolution updated daily from 1980-present. Data is reprocessed on a global grid with daily temporal resolution. You can
get [additional information here](https://www.ncei.noaa.gov/products/climate-data-records/precipitation-cmorph) or on [climate engine org page here](https://support.climateengine.org/article/55-cpc-cmorph).

#### Dataset Description

**Spatial Information**

| Parameter            | Value                          |
|----------------------|--------------------------------|
| Spatial extent       | Global                         |
| Spatial resolution   | 25-km (1/2-deg x 1/2-deg)      |
| Temporal resolution  | Daily                          |
| Time span            | 1998-01-01 to present          |
| Update frequency     | Updated daily with 2-day lag   |

**Variables**

| Variable                  | Details                              |
|---------------------------|--------------------------------------|
| Precipitation ('precip') | - Units: Millimeters                |
|                           | - Scale factor: 1.0                  |

#### Citation

```
Xie, Pingping; Joyce, Robert; Wu, Shaorong; Yoo, S.-H.; Yarosh, Yelena; Sun, Fengying; Lin, Roger, NOAA CDR Program (2019): NOAA Climate Data Record
(CDR) of CPC Morphing Technique (CMORPH) High Resolution Global Precipitation Estimates, Version 1 [indicate subset].
NOAA National Centers for Environmental Information.
```

#### Earth Engine Snippet

```js
// Read in Image Collections and get single image
var cmorph_ic = ee.ImageCollection('projects/climate-engine-pro/assets/noaa-cpc-cmorph/daily')
var cmorph_i = cmorph_ic.first()

// Print single image to see bands
print(cmorph_i)

// Visualize precipitation for single image
var prec_palette = ["#ffffcc", "#c7e9b4", "#7fcdbb", "#41b6c4", "#1d91c0", "#225ea8", "#0c2c84"]
Map.addLayer(cmorph_i.select('precip'), {min: 0, max: 200, palette: prec_palette}, 'precip')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:/weather-climate/CPC-MORPH

#### License

NOAA data, information, and products, regardless of the method of delivery, are not subject to copyright and carry no restrictions on their subsequent use by the public. Once obtained, they may be put to any lawful use. The forgoing data is in the public domain and is being provided without restriction on use and distribution. For more information visit the NWS disclaimer site.

Keywords: NOAA, global, precipitation, climate, near real-time, NWS, CPC, MORPH, CMORPH

Dataset provided by: NOAA

Dataset curatd in GEE by: Climate Engine Org
