# NOAA Monthly U.S. Climate Gridded Dataset (NClimGrid)

The NOAA Monthly U.S. Climate Gridded Dataset (NClimGrid) dataset is available as either a daily (NClimGrid-d) or a monthly (NClimGrid-m) dataset.
The datasets contain gridded fields and area averages of maximum, minimum, and mean temperature and precipitation amounts for the contiguous United
States. NClimGrid consists of gridded fields covering the land area between approximately 24°N and 49°N and between 67°W and 125°W at a resolution
of 1/24 of a degree (0.041667°). The primary purpose of these products is to support applications such as drought monitoring that require time
series of spatially and/or temporally aggregated gridpoint values. Reliance on single-day values and individual points is discouraged due to the
significant uncertainty that is inherent in such a product, as a result of the spatial distribution of the underlying observations, differences in
observation time between neighboring stations, and interpolation errors. Spatial and temporal averaging tends to reduce the effect of these
uncertainties, and time series of such aggregated values can be shown to be suitable for climatological applications. You can find addtional information[about the dataset here](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00332) and [climate engine org page here](https://support.climateengine.org/article/75-nclim).

#### Dataset description

**Spatial Information**

| Parameter            | Value                         |
|----------------------|-------------------------------|
| Spatial extent       | Conterminous United States    |
| Spatial resolution   | 4.6-km (1/24-deg x 1/24-deg)  |
| Temporal resolution  | Daily and monthly             |
| Time span            | 1951-01-01 to present (daily data); 1895-01-01 to present (monthly data) |
| Update frequency     | Updated daily with 3 day lag (daily data); Updated monthly with 1 month lag (monthly data) |

**Variables**

| Variable                  | Details                              |
|---------------------------|--------------------------------------|
| Minimum temperature, 2m   | - Units: Degrees Celsius             |
|                           | - Scale factor: 1.0                  |
| Maximum temperature, 2m   | - Units: Degrees Celsius             |
| ('tmin')                  | - Scale factor: 1.0                  |
| Mean temperature ('tavg') | - Units: Degrees Celsius             |
|                           | - Scale factor: 1.0                  |
| Precipitation ('precip')  | - Units: Millimeters                 |
|                           | - Scale factor: 1.0                  |

#### Citation

```
Vose, Russell S., Applequist, Scott, Squires, Mike, Durre, Imke, Menne, Matthew J., Williams, Claude N. Jr., Fenimore, Chris, Gleason, Karin, and
Arndt, Derek (2014): NOAA Monthly U.S. Climate Gridded Dataset (NClimGrid), Version 1. [indicate subset used]. NOAA National Centers for
Environmental Information. DOI:10.7289/V5SX6B56 [access date].
```

![clim_grid](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/c40c521a-bf2b-40f8-8eb8-e82802dad700)

#### Earth Engine Snippet

```js

// Read in daily and monthly Image Collections and get single image from each collection
var nclimgrid_m_ic = ee.ImageCollection('projects/climate-engine-pro/assets/noaa-ncei-nclimgrid/monthly')
var nclimgrid_m_i = nclimgrid_m_ic.first()
var nclimgrid_d_ic = ee.ImageCollection('projects/climate-engine-pro/assets/noaa-ncei-nclimgrid/daily')
var nclimgrid_d_i = nclimgrid_d_ic.first()

// Print each single image to see bands
print(nclimgrid_m_i)
print(nclimgrid_d_i)

// Visualize each band from each single image
var prec_palette = ["#ffffcc", "#c7e9b4", "#7fcdbb", "#41b6c4", "#1d91c0", "#225ea8", "#0c2c84"]
var temp_palette = ["#b2182b", "#ef8a62", "#fddbc7", "#f7f7f7", "#d1e5f0", "#67a9cf", "#2166ac"].reverse()
Map.addLayer(nclimgrid_m_i.select('precip'), {min: 0, max: 200, palette: prec_palette}, 'precip, monthly')
Map.addLayer(nclimgrid_m_i.select('tmin'), {min: -20, max: 20, palette: temp_palette}, 'tmin, monthly')
Map.addLayer(nclimgrid_m_i.select('tmax'), {min: -20, max: 20, palette: temp_palette}, 'tmax, monthly')
Map.addLayer(nclimgrid_m_i.select('tavg'), {min: -20, max: 20, palette: temp_palette}, 'tavg, monthly')
Map.addLayer(nclimgrid_d_i.select('precip'), {min: 0, max: 10, palette: prec_palette}, 'precip, daily')
Map.addLayer(nclimgrid_d_i.select('tmin'), {min: -20, max: 20, palette: temp_palette}, 'tmin, daily')
Map.addLayer(nclimgrid_d_i.select('tmax'), {min: -20, max: 20, palette: temp_palette}, 'tmax, daily')
Map.addLayer(nclimgrid_d_i.select('tavg'), {min: -20, max: 20, palette: temp_palette}, 'tavg, daily')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/NOAA-NCLIM-GRID

#### License

NOAA data, information, and products, regardless of the method of delivery, are not subject to copyright and carry no restrictions on their subsequent use by the public. Once obtained, they may be put to any lawful use. The forgoing data is in the public domain and is being provided without restriction on use and distribution. For more information visit the NWS disclaimer site. NClimGrid Data Use And Access Constraints: https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.ncdc:C00332#Constraints

Keywords: NOAA, nclim, CONUS, United Stated, daily, near real-time, temperature, precipitation

Provider: NOAA

Curated in Earth Engine by: Climate Engine Org
