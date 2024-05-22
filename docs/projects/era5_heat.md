# ERA5-HEAT Dataset

This dataset provides a complete historical reconstruction for a set of indices representing human thermal stress and discomfort in outdoor
conditions. This dataset, also known as ERA5-HEAT (Human thErmAl comforT) represents the current state-of-the-art for bioclimatology data record
production. The dataset is organized around two main variables: 1) the mean radiant temperature (MRT) and 2) the universal thermal climate index
(UTCI) These variables describe how the human body experiences atmospheric conditions, specifically air temperature, humidity, ventilation and
radiation.

The dataset is computed using the ERA5 reanalysis from the European Centre for Medium-Range Forecasts (ECMWF). ERA5 combines model data with
observations from across the world to provide a globally complete and consistent description of the Earth’s climate and its evolution in recent
decades. ERA5 is regarded as a good proxy for observed atmospheric conditions. Additional external information is available on this [product here](https://cds.climate.copernicus.eu/cdsapp#!/dataset/derived-utci-historical?tab=overview).

#### Dataset Description

**Spatial Information**

| **Attribute**           | **Details**                            |
|-------------------------|----------------------------------------|
| **Spatial extent**      | Global                                 |
| **Spatial resolution**  | 27.75km (.25 deg)                      |
| **Temporal resolution** | Daily                                  |
| **Time span**           | 1940-01-01 to present                  |
| **Update frequency**    | Updated daily with lag of 2 weeks      |

**Variables**

| **Variable**                                | **Units**        | **Scale factor** | **Description**                                                         |
|---------------------------------------------|------------------|------------------|-------------------------------------------------------------------------|
| **Mean Radiant Temperature (‘mrt_mean’, ‘mrt_max’, ‘mrt_min’, ‘mrt_median’)** | Degrees Kelvin  | 1.0              | Provided in four bands for daily mean, maximum, minimum, and median.    |
| **Universal Thermal Climate Index (‘utci_mean’, ‘utci_max’, ‘utci_min’, ‘utci_median’)** | Degrees Kelvin  | 1.0              | Provided in four bands for daily mean, maximum, minimum, and median.    |

#### Citation

```
Di Napoli C., Barnard C., Prudhomme C., Cloke HL and Pappenberger F. (2020): Thermal comfort indices derived from ERA5 reanalysis. Copernicus
Climate Change Service (C3S) Climate Data Store (CDS). DOI: 10.24381/cds.553b7518 (Accessed on DD-MMM-YYYY)
```

![era5_heat](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/11d5060c-085f-457d-ad8d-3c6dd0fe5bc7)

#### Earth Engine Snippet

```js
// Read in Image Collection and get first image
var era5_heat_ic = ee.ImageCollection('projects/climate-engine-pro/assets/ce-era5-heat')
var era5_heat_i = era5_heat_ic.first()

// Print first image to see bands
print(era5_heat_i)

// Visualize select bands from first image — additional bands are present in the Image Collection
var temp_palette = ["#b2182b", "#ef8a62", "#fddbc7", "#f7f7f7", "#d1e5f0", "#67a9cf", "#2166ac"].reverse()
Map.addLayer(era5_heat_i.select('mrt_mean').selfMask().subtract(273.15), {min: -10, max: 50, palette: temp_palette}, 'Mean Radiant Temperature, Daily Mean')
Map.addLayer(era5_heat_i.select('utci_mean').selfMask().subtract(273.15), {min: -10, max: 50, palette: temp_palette}, 'Universal Thermal Climate Index, Daily Mean')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:/weather-climate/ERA5-HEAT

#### License

ECMWF is available under an open license with terms of [agreement available here](https://cds.climate.copernicus.eu/api/v2/terms/static/licence-to-use-copernicus-products.pdf)

Keywords: heat exposure, climate, reanalysis, global, era5, thermal, public health, climate engine

Provided by: Copernicus

Curated in GEE by: Climate Engine Org
