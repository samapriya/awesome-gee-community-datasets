# AgERA5 (ECMWF) dataset, version 2.0

Daily surface meteorological data for the period from 1979 to present as input for agriculture and agro-ecological studies. This dataset is based on
the hourly ECMWF ERA5 data at surface level and is referred to as AgERA5, version 2.0. Acquisition and pre-processing of the original ERA5 data is a complex and
specialized job. By providing the AgERA5 dataset, users are freed from this work and can directly start with meaningful input for their analyses and
modeling. To this end, the variables provided in this dataset match the input needs of most agriculture and agro-ecological models. Data were
aggregated to daily time steps at the local time zone and corrected towards a finer topography at a 0.1° spatial resolution. The correction to the 0.
1° grid was realized by applying grid and variable-specific regression equations to the ERA5 dataset interpolated at 0.1° grid. The equations were
trained on ECMWF's operational high-resolution atmospheric model (HRES) at a 0.1° resolution. This way the data are tuned to the finer topography,
finer land use pattern, and finer land-sea delineation of the ECMWF HRES model. You can find [additional information here](https://cds.climate.copernicus.eu/cdsapp#!/dataset/sis-agrometeorological-indicators?tab=overview) and [in the climate engine org dataset page here](https://support.climateengine.org/article/58-era5-ag)

#### Dataset Description

**Spatial Information**

| Parameter            | Value                     |
|----------------------|---------------------------|
| Spatial extent       | Global                    |
| Spatial resolution   | 9600 m (1/10-deg)         |
| Temporal resolution  | Daily                     |
| Time span            | 1979-01-01 to present     |
| Update frequency     | Updated daily with 7-day lag time |

**Variables**

| Variable                  | Details                              |
|---------------------------|--------------------------------------|
| Wind speed ('Wind_Speed_10m_Mean_24h') | - Units: Meters/second            |
|                           | - Scale factor: 1.0                |
| Minimum temperature, 2m ('Temperature_Air_2m_Min_24h') | - Units: Degrees Kelvin   |
|                           | - Scale factor: 1.0                |
| Maximum temperature, 2m ('Temperature_Air_2m_Max_24h') | - Units: Degrees Kelvin   |
|                           | - Scale factor: 1.0                |
| Mean temperature, 2m ('Temperature_Air_2m_Mean_24h') | - Units: Degrees Kelvin    |
|                           | - Scale factor: 1.0                |
| Max temperature, 2m, daytime ('Temperature_Air_2m_Max_Day_Time') | - Units: Degrees Kelvin |
|                           | - Scale factor: 1.0                |
| Mean temperature, 2m, daytime ('Temperature_Air_2m_Mean_Day_Time') | - Units: Degrees Kelvin |
|                           | - Scale factor: 1.0                |
| Min temperature, 2m, nighttime ('Temperature_Air_2m_Min_Night_Time') | - Units: Degrees Kelvin |
|                           | - Scale factor: 1.0                |
| Mean temperature, 2m, nighttime ('Temperature_Air_2m_Mean_Night_Time') | - Units: Degrees Kelvin |
|                           | - Scale factor: 1.0                |
| Dewpoint temperature, 2m ('Dew_Point_Temperature_2m_Mean_24h') | - Units: Degrees Kelvin |
|                           | - Scale factor: 1.0                |
| Precipitation ('Precipitation_Flux') | - Units: Millimeters           |
|                           | - Scale factor: 1.0                |
| Precipitation rain duration fraction ('Precipitation_Rain_Duration_Fraction') | - Units: Count |
|                           | - Scale factor: 1.0                |
| Precipitation solid duration fraction ('Precipitation_Solid_Duration_Fraction') | - Units: Count |
|                           | - Scale factor: 1.0                |
| FAO56 Reference ET ('ReferenceET_PenmanMonteith_FAO56') | - Units: Millimeters           |
|                           | - Scale factor: 1.0                |
| Snow depth ('Snow_Thickness_Mean_24h') | - Units: Centimeters           |
|                           | - Scale factor: 1.0                |
| Snow water equivalent ('Snow_Thickness_LWE_Mean_24h') | - Units: Centimeters        |
|                           | - Scale factor: 1.0                |
| Vapour pressure ('Vapour_Pressure_Mean_24h') | - Units: hPa                |
|                           | - Scale factor: 1.0                |
| Vapour pressure deficit ('VVapour_Pressure_Deficit_at_Maximum_Temperature') | - Units: hPa                |
|                           | - Scale factor: 1.0                |
| Downward solar radiation ('Solar_Radiation_Flux') | - Units: J m-2d-1         |
|                           | - Scale factor: 1.0                |
| Cloud cover ('Cloud_Cover_Mean_24h') | - Units: Fraction               |
|                           | - Scale factor: 1.0                |
| Relative humidity, 2m 06h ('Relative_Humidity_2m_06h') | - Units: Percent        |
|                           | - Scale factor: 1.0                |
| Relative humidity, 2m 15h ('Relative_Humidity_2m_15h') | - Units: Percent        |
|                           | - Scale factor: 1.0                |

#### Citation

```
Copernicus Climate Change Service (2020): Agrometeorological indicators from 1979 to present derived from reanalysis. Copernicus Climate Change Service (C3S) Climate Data Store (CDS). DOI: 10.24381/cds.6c68c9bb (Accessed on DD-MMM-YYYY)
```

![agera5](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/c93b3918-ff1e-4f0b-a3c3-18b12435f1e1)

#### Earth Engine Snippet

```js
// Read in Image Collection and get first image
var agera5_ic = ee.ImageCollection('projects/climate-engine-pro/assets/ce-ag-era5-v2/daily')
var agera5_i = agera5_ic.first()

// Print first image to see bands
print(agera5_i)

// Visualize select bands from first image — additional bands are present in the Image Collection
var prec_palette = ["#ffffcc", "#c7e9b4", "#7fcdbb", "#41b6c4", "#1d91c0", "#225ea8", "#0c2c84"]
var temp_palette = ["#b2182b", "#ef8a62", "#fddbc7", "#f7f7f7", "#d1e5f0", "#67a9cf", "#2166ac"].reverse()
var eto_palette = ["#b2182b", "#ef8a62", "#fddbc7", "#f7f7f7", "#d1e5f0", "#67a9cf", "#2166ac"].reverse()
Map.addLayer(agera5_i.select('Precipitation_Flux'), {min: 0, max: 1, palette: prec_palette}, 'Precipitation_Flux')
Map.addLayer(agera5_i.select('Temperature_Air_2m_Max_24h').selfMask().subtract(273.15), {min: -10, max: 50, palette: temp_palette}, 'Temperature_Air_2m_Max_24h')
Map.addLayer(agera5_i.select('Temperature_Air_2m_Min_24h').selfMask().subtract(273.15), {min: -10, max: 50, palette: temp_palette}, 'Temperature_Air_2m_Min_24h')
Map.addLayer(agera5_i.select('Temperature_Air_2m_Mean_24h').selfMask().subtract(273.15), {min: -10, max: 50, palette: temp_palette}, 'Temperature_Air_2m_Mean_24h')
Map.addLayer(agera5_i.select('Dew_Point_Temperature_2m_Mean_24h').selfMask().subtract(273.15), {min: -10, max: 50, palette: temp_palette}, 'Dew_Point_Temperature_2m_Mean')
Map.addLayer(agera5_i.select('Snow_Thickness_LWE_Mean_24h'), {min: 0, max: 20, palette: prec_palette}, 'Snow_Thickness_LWE_Mean')
Map.addLayer(agera5_ic.select('ReferenceET_PenmanMonteith_FAO56').filterDate('2023-10-01', '2024-09-30').sum(), {min: 0, max: 2000, palette: eto_palette}, 'ReferenceET_PenmanMonteith_FAO56')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:/weather-climate/AGERA5-DATASETS

#### License
Data are subject to the License to Use Copernicus Products:[ https://cds.climate.copernicus.eu/api/v2/terms/static/licence-to-use-copernicus-products.pdf](https://cds.climate.copernicus.eu/api/v2/terms/static/licence-to-use-copernicus-products.pdf)

Keywords: climate, reanalysis, near real-time, ECMWF, precipitation, temperature

Dataset provider: Copernicus

Dataset curated in GEE by: Climate Engine Org
