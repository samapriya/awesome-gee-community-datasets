#  NOAA Evaporative Stress Index (ESI)

The Evaporative Stress Index (ESI) is produced by the NOAA Center for Satellite Applications and Research (STAR) and USDA-ARS Hydrology and Remote Sensing Laboratory. The Evaporative Stress Index (ESI) is a thermal indicator of anomalous ET conditions that can be used for drought monitoring. The Evaporative Stress Index (ESI) describes temporal anomalies in evapotranspiration (ET), highlighting areas with anomalously high or low rates of water use across the land surface. Here, ET is retrieved via energy balance using remotely sensed land-surface temperature (LST) time-change signals. LST is a fast- response variable, providing proxy information regarding rapidly evolving surface soil moisture and crop stress conditions at relatively high spatial resolution. The ESI also demonstrates capability for capturing early signals of “flash drought”, brought on by extended periods of hot, dry and windy conditions leading to rapid soil moisture depletion. You can get additional information on this [dataset here](https://www.drought.gov/data-maps-tools/evaporative-stress-index-esi) and [climate engine org data page here](https://support.climateengine.org/article/60-esi).

**Spatial Information**

| Parameter            | Value               |
|----------------------|---------------------|
| Spatial extent       | Global              |
| Spatial resolution   | 4-km (1/24-deg)     |
| Temporal resolution  | Weekly              |
| Time span            | 2001-01-01 to present |
| Update frequency     | Updated weekly with 1 week lag |

**Variables**

| Variable                         | Details                              |
|----------------------------------|--------------------------------------|
| 4-week Evaporative Stress Index (‘ESI_4wk’) | - Units: Unitless                     |
|                                  | - Scale factor: 1.0                    |
| 12-week Evaporative Stress Index (‘ESI_12wk’) | - Units: Unitless                     |
|                                  | - Scale factor: 1.0                    |


#### Citation

```
- Anderson, M. C., J. M. Norman, G. R. Diak, W. P. Kustas, and J. R. Mecikalski, 1997: A two-source time-integrated model for estimating surface
fluxes using thermal infrared remote sensing. Remote Sens. Environ., 60, 195-216.

- Anderson, M. C., J. M. Norman, J. R. Mecikalski, J. P. Otkin, and W. P. Kustas, 2007a: A climatological study of evapotranspiration and moisture
stress across the continental U.S. based on thermal remote sensing: I. Model formulation. J. Geophys. Res., 112, D10117, doi:10110.11029/
12006JD007506.

- Anderson, M. C., J. M. Norman, J. R. Mecikalski, J. P. Otkin, and W. P. Kustas, 2007b: A climatological study of evapotranspiration and moisture
stress across the continental U.S. based on thermal remote sensing: II. Surface moisture climatology. J. Geophys. Res., 112, D11112, doi:11110.11029/
12006JD007507.

- Anderson, M. C., C. R. Hain, B. Wardlow, J. R. Mecikalski, and W. P. Kustas (2011), Evaluation of a drought index based on thermal remote sensing
of evapotranspiration over the continental U.S., J. Climate, 24, 2025-2044.

- McKee, T. B., N. J. Doesken, and J. Kleist, 1993: The relationship of drought frequency and duration to time scales. AMS Eighth conf. on Applied
Climatology, Anaheim, CA, 179-184.

- McKee, T. B., N. J. Doesken, and J. Kleist, 1995: Drought monitoring with multiple time scales. AMS Ninth conf. on Applied Climatology, Dallas,
TX, 233-236.

- Norman, J. M., W. P. Kustas, and K. S. Humes, 1995: A two-source approach for estimating soil and vegetation energy fluxes from observations of
directional radiometric surface temperature. Agric. For. Met., 77, 263-293.

- Svoboda, M., and Coauthors, 2002: The Drought Monitor. Bull. Amer. Meteorol. Soc., 83, 1181-1190.
```

![esi](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/4c4d36bd-1eb6-4f15-a109-06b1d7dfb2ad)

#### Earth Engine Snippet

```js
// Read in Image Collection and get first image
var esi_4wk_ic = ee.ImageCollection('projects/climate-engine/esi/4wk')
var esi_4wk_i = esi_4wk_ic.filterDate('2020-08-01', '2020-08-10').first()
var esi_12wk_ic = ee.ImageCollection('projects/climate-engine/esi/12wk')
var esi_12wk_i = esi_12wk_ic.filterDate('2020-08-01', '2020-08-10').first()

// Print first image to see bands
print(esi_4wk_i)
print(esi_12wk_i)

// Visualize select bands from first image — additional bands are present in the Image Collection
var esi_palette = ["#0000aa", "#0000ff", "#00aaff", "#00ffff", "#aaff55", "#ffffff", "#ffff00", "#fcd37f", "#ffaa00", "#e60000", "#730000"]
Map.addLayer(esi_4wk_i.select('ESI'), {min: -2.5, max: 2.5, palette: esi_palette}, 'ESI_4wk')
Map.addLayer(esi_12wk_i.select('ESI'), {min: -2.5, max: 2.5, palette: esi_palette}, 'ESI_12wk')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/GLOBAL-ESI-10KM

#### License

NOAA data, information, and products, regardless of the method of delivery, are not subject to copyright and carry no restrictions on their subsequent use by the public. Once obtained, they may be put to any lawful use. The forgoing data is in the public domain and is being provided without restriction on use and distribution. For more information visit the NWS disclaimer site.

Keywords: Drought, vegetation, remote sensing, climate, USDA-ARS, NOAA, MODIS, LST, global, near real-time

Provided by NOAA,USDA-ARS

Curated in GEE by: Climate Engine Org
