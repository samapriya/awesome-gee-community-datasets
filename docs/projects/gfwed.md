# Global Fire WEather Database (GFWED)

The Global Fire WEather Database (GFWED) integrates different weather factors influencing the likelihood of a vegetation fire starting and spreading at daily temporal resolution and a ~50-km (0.5-deg x 0.625-deg) spatial resolution from 1980-present. It is based on the Fire Weather Index (FWI) System, the most widely used fire weather system in the world. The FWI System was developed in Canada, and is composed of three moisture codes and three fire behavior indices. The moisture codes capture the moisture content of three generalized fuel classes and the behavior indices reflect the spread rate, fuel consumption and intensity of a fire if it were to start. Details on the development and testing of GFWED can be found in Field et al. (2015) and the evaluation of GFWED products in Field (2020a). Applications of the FWI System can be found in Taylor and Alexander (2006) and technical descriptions are provided by van Wagner (1987) and Dowdy et al. (2009). Additional information about this dataset can [be found here](https://gmao.gsfc.nasa.gov/reanalysis/MERRA-2/) and [here](Global Fire WEather Database (GFWED)). You can also find this dataset [at the climate engine org page here](https://support.climateengine.org/article/71-merra2-fwi).

<center>

| **Spatial Extent**               | Global                                              |
|----------------------------------|-----------------------------------------------------|
| **Spatial Resolution**           | ~50-km (0.5-deg x 0.625-deg)                        |
| **Temporal Resolution**          | Daily                                               |
| **Time Span**                    | 1980-04-02 to present                               |
| **Update Frequency**             | Updated daily with 5-month lag time                 |

| **Variables**                    |                                                     |
|----------------------------------|-----------------------------------------------------|
| Fire Weather Index ('FWI')       | - Units: Unitless                                   |
|                                  | - Scale Factor: 1.0                                 |

</center>

#### Citation

```
Field, R.D., A.C. Spessa, N.A. Aziz, A. Camia, A. Cantin, R. Carr, W.J. de Groot, A.J. Dowdy, M.D. Flannigan, K. Manomaiphiboon, F. Pappenberger, V.
Tanpipat, and X. Wang, 2015: Development of a global fire weather database. Nat. Hazards Earth Syst. Sci., 15, 1407-1423, doi:10.5194/
nhess-15-1407-2015.

MERRA-2 Overview: The Modern-Era Retrospective Analysis for Research and Applications, Version 2 (MERRA-2), Ronald Gelaro, et al., 2017, J. Clim.,
doi: 10.1175/JCLI-D-16-0758.1
```

![gfwed](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/bb51e157-d453-4dd7-b63e-90f18bca3f47)

### Earth Engine Snippet

```js
// Read in Image Collection and get first image
var merra2_ic = ee.ImageCollection('projects/climate-engine-pro/assets/ce-merra2_fwi-daily')
var merra2_i = merra2_ic.filterDate('2020-08-01', '2020-08-05').first()

// Print first image to see bands
print(merra2_i)

// Visualize select bands from first image — additional bands are present in the Image Collection
var fwi_palette = ["#b2182b", "#ef8a62", "#fddbc7", "#f7f7f7", "#d1e5f0", "#67a9cf", "#2166ac"].reverse()
Map.addLayer(merra2_i.select('FWI'), {min: 0, max: 100, palette: fwi_palette}, 'FWI')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:fire-monitoring-analysis/GLOBAL-FIRE-WEATHER-DB

Sample Script:

#### License
NASA Earth science data are made freely available to the public to the fullest extent possible, consistent with applicable laws and regulations. NASA Earth science data are not subject to copyright.

Keywords: climate, fire, wildfire, NASA, MERRA2, daily, global, GFWED

Provided by : GFWED development is supported by the NASA Precipitation Measurement Missions Science Team and the NASA Group on Earth Observations Work Program

Curated in GEE by: Climate Engine Org



