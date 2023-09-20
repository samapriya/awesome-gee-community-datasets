# CEMS Fire Danger Indices

Fire danger indices from the ECMWF, calculated using weather forecasts from historical simulations provided by ECMWF ERA5 reanalysis.The CEMS Fire Danger Indices dataset provides a comprehensive set of indices designed to assess and quantify fire danger and wildfire risk at regional and global scales. You can get additional information on the [dataset here](https://cds.climate.copernicus.eu/cdsapp#!/dataset/cems-fire-historical-v1?tab=overview) and on the [climateengine.org dataset page here](https://support.climateengine.org/article/49-cems-fire)

- Build-up Index: The Build-Up Index is a weighted combination of the Duff moisture code and Drought code to indicate the total amount of fuel available for combustion by a moving flame front. The Duff moisture code has the most influence on the Build-up index value. For example, a Duff moisture code value of zero always results in a Build-up index value of zero regardless of what the Drought code value is. The Drought code has the strongest influence on the Build-up index when Duff moisture code values are high. The greatest effect that the Drought code can have is to make the Build-up index value equal to twice the Duff moisture code value. The Build-up index is often used for pre-suppression planning purposes.

- Burning Index: The Burning Index measures the difficulty of controlling a fire. It is derived from a combination of Spread component (how fast it will spread) and Energy release component (how much energy will be produced). In this way, it is related to flame length, which, in the Fire Behavior Prediction System, is based on rate of spread and heat per unit area. However, because of differences in the calculations for Burning index and flame length, they are not the same.

- Drought Code: The Drought code is an indicator of the moisture content in deep compact organic layers. This code represents a fuel layer at approximately 10-20 cm deep. The Drought code fuels have a very slow drying rate, with a time lag of 52 days. The Drought code scale is open-ended, although the maximum value is about 800.

- Drought Factor: The drought factor is a component representing fuel availability. It is is given as a number between 0 and 10 and represents the influence of recent temperatures and rainfall events on fuel availability (see Griffiths 1998 for details). The Drought Factor is partly based on the soil moisture deficit which is commonly calculated in Australia as the Keetch-Byram Drought Index (KBDI) (also available). The KBDI estimates the soil moisture below saturation up to a maximum

- Duff Moisture Code: The Duff moisture code is an indicatore of the moisture content in loosely-compacted organic layers of moderate depth. It is representative of the duff layer that is 5-10 cm deep. Duff moisture code fuels are affected by rain, temperature and relative humidity. Because these fuels are below the forest floor surface, wind speed does not affect the fuel moisture content. The Duff moisture code fuels have a slower drying rate than the Fine fuel moisture code fuels, with a timelag of 12 days. Although the Duff moisture code has an open-ended scale, the highest probable value is in the range of 150.

- Energy Release Component: The Energy release component is a number related to the available energy (British Thermal Unit) per unit area (square foot) within the flaming front at the head of a fire. Daily variations in Energy release component are due to changes in moisture content of the various fuels present, both live and dead. Since this number represents the potential "heat release" per unit area in the flaming zone, it can provide guidance to several important fire activities. It may also be considered a composite fuel moisture value as it reflects the contribution that all live and dead fuels have to potential fire intensity. The Energy release component is a cumulative or "build-up" type of index. As live fuels cure and dead fuels dry, the Energy release component values get higher thus providing a good reflection of drought conditions. The scale is open-ended or unlimited and, as with other National Forest Danger Rating System components, is relative.

- Fine Fuel Moisture Code: The Fine fuel moisture code is an indicatore of the moisture content in litter and other cured fine fuels (needles, mosses, twigs less than 1 cm in diameter). The Fine fuel moisture code is representative of the top litter layer less than 1-2 cm deep. Fine fuel moisture code values change rapidly because of a high surface area to volume ratio, and direct exposure to changing environmental conditions. The Fine fuel moisture code scale ranges from 0-99 and is the only component of the Fire weather index system which does not have an open-ended scale. Generally, fires begin to ignite at Fine fuel moisture code values near 70, and the maximum probable value that will ever be achieved is 96.

- Fire Daily Severity Rating: Numeric rating of the difficulty of controlling fires. It is an exponential transformation of the Fire weather index and more accurately reflects the expected efforts required for fire suppression as it increases exponentially as the Fire weather index is above a certain value.

- Fire Danger Index: The Fire danger index is a metric related to the chances of a fire starting, its rate of spread, its intensity, and its difficulty of suppression. It is open ended however a value of 50 and above is considered extreme in most vegetation

- Fire Weather Index:The Fire weather index is a combination of Initial spread index and Build-up index, and is a numerical rating of the potential frontal fire intensity. In effect, it indicates fire intensity by combining the rate of fire spread with the amount of fuel being consumed. Fire weather index values are not upper bounded however a value of 50 is considered as extreme in many places. The Fire weather index is used for general public information about fire danger conditions.

- Ignition Component: The Ignition component measures the probability a firebrand will require suppression action. Since it is expressed as a probability, it ranges on a scale of 0 to 100. An Ignition component of 100 means that every firebrand will cause a fire requiring action if it contacts a receptive fuel. Likewise an Ignition component of 0 would mean that no firebrand would cause a fire requiring suppression action under those conditions.

- Initial Fire Spread Index: The Initial spread index combines the Fine fuel moisture code and wind speed to indicate the expected rate of fire spread. Generally, a 13 km h-1 increase in wind speed will double the Initial spread index value. The Initial spread index is accepted as a good indicator of fire spread in open light fuel stands with wind speeds up to 40 km h-1.

- Keetch-Byram Drought Index: The Keetch-Byram drought index (KBDI) is a number representing the net effect of evapotranspiration and precipitation in producing cumulative moisture deficiency in deep duff and upper soil layers. It is a continuous index, relating to the flammability of organic material in the ground.The Keetch-Byram drought index attempts to measure the amount of precipitation necessary to return the soil to saturated conditions. It is a closed system ranging from 0 to 200 units and represents a moisture regime from 0 to 20 cm of water through the soil layer. At 20 cm of water, the Keetch-Byram drought index assumes saturation. Zero is the point of no moisture deficiency and 200 is the maximum drought that is possible. At any point along the scale, the index number indicates the amount of net rainfall that is required to reduce the index to zero, or saturation.

- Spread Component: The Spread component is a measure of the spead at which a headfire would spread. The spread component is numerically equal to the theoretical ideal rate of spread expressed in feet-per-minute however is considered as a dimensionless variable. The Spread component is expressed on an open-ended scale; thus it has no upper limit.

<center>

| **Spatial Extent**               | Global                                                  |
|----------------------------------|---------------------------------------------------------|
| **Spatial Resolution**           | ~25km (0.25 deg)                                        |
| **Temporal Resolution**          | Daily                                                   |
| **Time Span**                    | 1940-01-01 to Present                                   |
| **Update Frequency**             | Updated daily with one week lag                         |

</center>

<center>

| **Variables**                    |                                                           |
|----------------------------------|---------------------------------------------------------|
| Build-up Index ('build_up_index') | - Units: Dimensionless                                  |
|                                  | - Scale Factor: 1.0                                    |
| Burning Index ('burning_index')   | - Units: Dimensionless                                  |
|                                  | - Scale Factor: 1.0                                    |
| Drought Code ('drought_code')     | - Units: Dimensionless                                  |
|                                  | - Scale Factor: 1.0                                    |
| Drought Factor ('drought_factor') | - Units: Dimensionless                                  |
|                                  | - Scale Factor: 1.0                                    |
| Duff Moisture Code ('duff_moisture_code') | - Units: Dimensionless                       |
|                                  | - Scale Factor: 1.0                                    |
| Energy Release Component ('energy_release_component') | - Units: J/m2 |
|                                  | - Scale Factor: 1.0                                    |
| Fine Fuel Moisture Code ('fine_fuel_moisture_code') | - Units: Dimensionless |
|                                  | - Scale Factor: 1.0                                    |
| Fire Daily Severity Rating ('fire_daily_severity_rating') | - Units: Dimensionless |
|                                  | - Scale Factor: 1.0                                    |
| Fire Danger Index ('fire_danger_index') | - Units: Dimensionless                             |
|                                  | - Scale Factor: 1.0                                    |
| Fire Weather Index ('fire_weather_index') | - Units: Dimensionless                           |
|                                  | - Scale Factor: 1.0                                    |
| Ignition Component ('ignition_component') | - Units: %                                            |
|                                  | - Scale Factor: 1.0                                    |
| Initial Fire Spread Index ('initial_fire_spread_index') | - Units: Dimensionless                        |
|                                  | - Scale Factor: 1.0                                    |
| Keetch-Byram Drought Index ('keetch_byram_drought_index') | - Units: Dimensionless                    |
|                                  | - Scale Factor: 1.0                                    |
| Spread Component ('spread_component') | - Units: Dimensionless                                |
|                                  | - Scale Factor: 1.0                                    |

</center>

#### Citation

```
Vitolo, C., Di Giuseppe, F., Barnard, C., Coughlan, R., San-Miguel-Ayanz, J., Libertá, G., & Krzeminski, B. (2020). ERA5-based global
meteorological wildfire danger maps. Scientific data, 7(1), 1-11. 'Contains modified Copernicus Climate Change Service information [Year]'

Copernicus Climate Change Service, Climate Data Store, (2019): Fire danger indices historical data from the Copernicus Emergency Management
Service. Copernicus Climate Change Service (C3S) Climate Data Store (CDS). DOI: 10.24381/cds.0e89c522 (Accessed on DD-MMM-YYYY)
```

![cems_fire](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/09a7cc9a-fd05-48a5-b836-4841b1fb6770)

#### Earth Engine Snippet

```js
// Read in Image Collection and get most recent image
var cems_ic = ee.ImageCollection('projects/climate-engine-pro/assets/ce-cems-fire-daily-4-1')
var cems_i = cems_ic.filterDate('2023-01-01', ee.Date(Date.now())).sort('system:time_start', false).first()

// Print first image to see bands
print(cems_i)

// Visualize select bands from first image - additional variables are available in the Image Collection
var fire_palette = ["#b2182b", "#ef8a62", "#fddbc7", "#f7f7f7", "#d1e5f0", "#67a9cf", "#2166ac"].reverse()
Map.addLayer(cems_i.select('burning_index'), {min: 0, max: 50, palette: fire_palette}, 'burning_index')
Map.addLayer(cems_i.select('fire_weather_index'), {min: 0, max: 50, palette: fire_palette}, 'fire_weather_index')
Map.addLayer(cems_i.select('fire_danger_index'), {min: 0, max: 50, palette: fire_palette}, 'fire_danger_index')
Map.addLayer(cems_i.select('ignition_component'), {min: 0, max: 50, palette: fire_palette}, 'ignition_component')
Map.addLayer(cems_i.select('spread_component'), {min: 0, max: 10, palette: fire_palette}, 'spread_component')
Map.addLayer(cems_i.select('energy_release_component'), {min: 0, max: 50, palette: fire_palette}, 'energy_release_component')
Map.addLayer(cems_i.select('fire_daily_severity_rating'), {min: 0, max: 50, palette: fire_palette}, 'fire_daily_severity_rating')
```
Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:fire-monitoring-analysis/CEMS-FIRE-DAILY

#### License
The license for CEMS Fire Danger Indices data is the Copernicus Licence to Use Copernicus Products (the "Licence"). The Licence is a modified Creative Commons Attribution 4.0 International (CC BY 4.0) license, with the following additional terms:
* You must acknowledge the European Commission and the European Centre for Medium-Range Weather Forecasts (ECMWF) as the source of the data.
* You must not use the data for commercial purposes without prior permission from the European Commission.
* You must not modify the data in a way that could mislead the public about its source or accuracy.

Data are subject to the License to Use Copernicus Products [found here](https://cds.climate.copernicus.eu/api/v2/terms/static/licence-to-use-copernicus-products.pdf)

Keywords: ECMWF, Copernicus, wildfire, climate, reanalysis, ERA5, daily, near real-time

Provided by : Copernicus

Curated in GEE by: ClimateEngine Org
