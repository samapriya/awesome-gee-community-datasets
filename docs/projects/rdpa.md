# Regional Deterministic Precipitation Analysis (RDPA)

The Regional Deterministic Precipitation Analysis (RDPA) based on the Canadian Precipitation Analysis (CaPA) system is on a domain that corresponds
to that of the operational regional model, i.e. the Regional Deterministic Prediction System (RDPS-LAM3D) except for areas over the Pacific Ocean
where the western limit of the RDPA domain is slightly shifted eastward with respect to the regional model domain. The resolution of the RDPA
analysis is identical to the resolution of the operational regional system RDPS LAM3D. The fields in the RDPA GRIB2 dataset are on a
polar-stereographic (PS) grid covering North America and adjacent waters with a 10 km resolution at 60 degrees north, 2003-present. You can find
[additional information on the dataset here](https://open.canada.ca/data/en/dataset/fdd3446a-dc20-5bad-9755-0855e3ec9b19), and [also here](https://
weather.gc.ca/grib/grib2_RDPA_ps10km_e.html ) apart from the [climate engine org page](https://support.climateengine.org/article/82-rdpa).


| **Spatial extent**     | **Spatial resolution** | **Temporal resolution** | **Time span**            | **Update frequency**           |
|------------------------|------------------------|--------------------------|--------------------------|--------------------------------|
| United States and Canada | 10.0 km grid (1/11 deg) | Daily                   | 2003-01-01 to present    | Updated daily with 5 month lag time |

**Variables**

| **Variable**   | **Units**      | **Scale factor** |
|-----------------|----------------|------------------|
| Precipitation ('precip') | Millimeters | 1.0              |


#### Citation

```
[Canadian Precipitation Analysis (CaPA)](https://collaboration.cmc.ec.gc.ca/cmc/cmoi/product_guide/docs/lib/capa_information_leaflet_20141118_en.pdf) Methodology system

Fillion, Luc, Monique Tanguay, Ervig Lapalme, Bertrand Denis, Michel Desgagne, Vivian Lee, Nils Ek et al. "The Canadian regional data assimilation and forecasting system." Weather and Forecasting 25, no. 6 (2010): 1645-1669.

Environment and Climate Change Canada. (2023). Regional Deterministic Precipitation Analysis (RDPA) dataset [Version 2.0]. [Dataset]. Retrieved from https://open.canada.ca/data/en/dataset/fdd3446a-dc20-5bad-9755-0855e3ec9b19
```

![rdpa](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/15a00ae6-3fd6-45b4-866d-5821dfecd290)

### Earth Engine Snippet

```js
// Read in Image Collections and get single image
var rdpa_ic = ee.ImageCollection('projects/climate-engine-pro/assets/ce-rdpa-daily')
var rdpa_i = rdpa_ic.first()

// Print single image to see bands
print(rdpa_i)

// Visualize precipitation for single image
var prec_palette = ["#ffffcc", "#c7e9b4", "#7fcdbb", "#41b6c4", "#1d91c0", "#225ea8", "#0c2c84"]
Map.addLayer(rdpa_i.select('precip'), {min: 0, max: 200, palette: prec_palette}, 'precip')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:/weather-climate/CE-RDPA-DATASETS

#### License
Data are subject to the Government of Canada Open Data Licence Agreement: https://open.canada.ca/en/open-government-licence-canada. The terms of this Agreement govern your use and reproduction of the data instead of the copyright reproduction statements found in Important Notices on the Agriculture and Agri-Food Canada website.

Keywords: climate, precipitation, Canada, United States, daily

Provided by: Environment and Climate Change Canada

Curated in GEE by: Climate Engine Org
