# Climate Hazards Group InfraRed Precipitation with Station Data-Prelim (CHIRPS-Prelim)

The Climate Hazards Center InfraRed Precipitation With Station Data-Prelim (CHIRPS-Prelim) is a blend of CHIRPS data with in situ precipitation data
to unbias the data and enhance its accuracy. The process of generating CHIRPS- Prelim is similar to the CHIRPS process, with the main difference
being its reliance on Global Telecommunication System (GTS) stations only, which are available in near-real time. Blending of CHIRP with GTS-only
stations allows for the latency of CHIRPS- Prelim to be <5 days. Note that, in general, the differences in CHIRPS-Prelim and CHIRPS are within
acceptable limits, as both data sets share the same climatological mean. You can find additional [information here](https://www.chc.ucsb.edu/data/chirps) and [on climate org dataset page here](https://support.climateengine.org/article/53-chirps).

This dataset is to be used in conjunction with CHIRPS Pentad/Daily collections, which are Earth Engine assets at:
- UCSB-CHG/CHIRPS/PENTAD

- UCSB-CHG/CHIRPS/DAILY

#### Dataset Description

**Spatial Information**

| Parameter            | Value                   |
|----------------------|-------------------------|
| Spatial extent       | Global                  |
| Spatial resolution   | 4.8-km grid (1/20 deg) |
| Temporal resolution  | 5-day (pentad)          |
| Time span            | 2015 to present         |
| Update frequency     | Updated weekly          |

**Variables**

| Variable                  | Details                              |
|---------------------------|--------------------------------------|
| Precipitation ('precipitation') | - Units: Millimeters                    |
|                           | - Scale factor: 1.0                    |

#### Citation

```
Funk, C.C., Peterson, P.J., Landsfeld, M.F., Pedreros, D.H., Verdin, J.P., Rowland, J.D., Romero, B.E., Husak, G.J., Michaelsen, J.C., and Verdin, A.
P., 2014, A quasi-global precipitation time series for drought monitoring: U.S. Geological Survey Data Series 832, 4 p.,
http://dx.doi.org/10.3133/ds832
```

![chirps-prelim](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/f75d7410-8eea-4a17-a916-04c0aef78a55)

#### Earth Engine Snippet

```js
// Read in Image Collections and get single image
var chirps_ic = ee.ImageCollection('projects/climate-engine-pro/assets/ce-chirps-prelim-pentad')
var chirps_i = chirps_ic.first()

// Print single image to see bands
print(chirps_i)

// Visualize precipitation for single image
var prec_palette = ["#ffffcc", "#c7e9b4", "#7fcdbb", "#41b6c4", "#1d91c0", "#225ea8", "#0c2c84"]
Map.addLayer(chirps_i.select('precipitation'), {min: 0, max: 200, palette: prec_palette}, 'precipitation')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:/weather-climate/CHIRPS-PRELIM

#### License

This datasets are in the public domain. To the extent possible under law, Pete Peterson has waived all copyright and related or neighboring rights to Climate Hazards Group Infrared Precipitation with Stations (CHIRPS).

Keywords: precipitation, near real-time, climate, CHIRPS

Provided by: Climate Hazards Group Infrared Precipitation with Stations (CHIRPS)

Curated in GEE by: Climate Engine org
