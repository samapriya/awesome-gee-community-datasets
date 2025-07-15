# Modern-Era Retrospective analysis for Research and Applications, Version 2 (MERRA2)

NASAs Global Modeling and Assimilation Office (GMAO) produces the Modern-Era Retrospective analysis for Research and Applications, Version 2 (MERRA2) which is a 30+ year global climate reanalysis dataset.This dataset complements existing MERRA2 Earth Engine assets: https://developers.google.com/earth-engine/datasets/tags/merra. You can find additional information on this [dataset here](https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/) and read more about the dataset in the [climate org data page](https://support.climateengine.org/article/70-merra2)

#### Dataset Description

**Spatial Information**

| Parameter            | Value                                 |
|----------------------|---------------------------------------|
| Spatial extent       | Global                                |
| Spatial resolution   | ~50-km (0.5-deg x 0.625-deg)         |
| Temporal resolution  | Daily                                 |
| Time span            | 1980-04-02 to present                 |
| Update frequency     | Updated every 1-2 months              |

**Variables**

| Variable                                    | Details                                      |
|---------------------------------------------|----------------------------------------------|
| Minimum temperature, 2m ('T2MMIN')          | - Units: Degrees Kelvin                     |
|                                             | - Scale factor: 1.0                         |
| Maximum temperature, 2m ('T2MMAX')          | - Units: Degrees Kelvin                     |
|                                             | - Scale factor: 1.0                         |
| Precipitation ('PRECTOTCORR')              | - Units: Millimeters                        |
|                                             | - Scale factor: 1.0                         |
| Wind speed, 10m ('WIND2M')                 | - Units: Meters/second                      |
|                                             | - Scale factor: 1.0                         |
|                                             | - NOTE: Windspeed outputs are based on the  |
|                                             |   standard 10m measurement height, despite  |
|                                             |   the erroneous ‘2M’ suffix.               |
| ASCE Grass Reference Evapotranspiration     | - Units: Millimeters                        |
| ('ETo_ASCE')                                | - Scale factor: 1.0                         |
| ASCE Alfalfa Reference Evapotranspiration   | - Units: Millimeters                        |
| ('ETr_ASCE')                                | - Scale factor: 1.0                         |
| Specific humidity, 2m ('QV2M')              | - Units: kg kg-1                            |
|                                             | - Scale factor: 1.0                         |
| Surface pressure ('PS')                     | - Units: Pa                                 |
|                                             | - Scale factor: 1.0                         |
| Surface incoming shortwave flux ('SWGDN')    | - Units: W m-2                              |
|                                             | - Scale factor: 1.0                         |
| Surface incoming shortwave flux assuming    | - Units: W m-2                              |
| clear sky ('SWGDNCLR')                      | - Scale factor: 1.0                         |


#### Citation

```
MERRA-2 Overview: The Modern-Era Retrospective Analysis for Research and Applications, Version 2 (MERRA-2), Ronald Gelaro, et al., 2017, J. Clim.,
doi: 10.1175/JCLI-D-16-0758.1
```

![merra_v2](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/f407dfc8-ab4d-435c-adff-048cc9687c35)

#### Earth Engine Snippet

```js
// Read in Image Collection and get first image
var merra2_ic = ee.ImageCollection('projects/climate-engine-pro/assets/ce-merra2')
var merra2_i = merra2_ic.first()

// Print first image to see bands
print(merra2_i)

// Visualize select bands from first image — additional bands are present in the Image Collection
var prec_palette = ["#ffffcc", "#c7e9b4", "#7fcdbb", "#41b6c4", "#1d91c0", "#225ea8", "#0c2c84"]
var temp_palette = ["#b2182b", "#ef8a62", "#fddbc7", "#f7f7f7", "#d1e5f0", "#67a9cf", "#2166ac"].reverse()
var eto_palette = ["#ffffb2", "#fed976", "#feb24c", "#fd8d3c", "#fc4e2a", "#e31a1c", "#b10026"]
Map.addLayer(merra2_i.select('PRECTOTCORR'), {min: 0, max: 10, palette: prec_palette}, 'PRECTOTCORR')
Map.addLayer(merra2_i.select('T2MMAX').subtract(273.15), {min: -10, max: 30, palette: temp_palette}, 'T2MMAX')
Map.addLayer(merra2_i.select('T2MMIN').subtract(273.15), {min: -10, max: 30, palette: temp_palette}, 'T2MMIN')
Map.addLayer(merra2_i.select('ETo_ASCE'), {min: 0, max: 10, palette: eto_palette}, 'ETo_ASCE')
Map.addLayer(merra2_i.select('ETr_ASCE'), {min: 0, max: 10, palette: eto_palette}, 'ETr_ASCE')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:/weather-climate/MERRA-2

#### License

NASA promotes the full and open sharing of all data with research and applications communities, private industry, academia, and the general public.

Keywords: MERRA2, NASA, global, climate, reanalysis, temperature, precipitation, evapotranspiration, evaporative demand, wind

Datasets provided by: NASA

Dataset curated in GEE by: Climate Engine Org
