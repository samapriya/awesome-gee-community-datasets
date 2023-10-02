# Canadian Drought Outlook

The Canadian Drought Outlook raster dataset is produced by the Agriculture and Agri-Food Canada (AAFC). The Canadian Drought Outlook predicts whether drought across Canada will emerge, stay the same or get better over the target month. In calculating the outlook, consideration is given to Agroclimate indices, such as the Standard Precipitation Index (SPI), the Standard Precipitation Evaporation Index (SPEI), and the Palmer Drought Severity Index (PDSI). The drought outlook is issued on the first Thursday of each calendar month and is valid for 32 days from that date. You can get additional information about [this dataset here](https://open.canada.ca/data/en/dataset/2c82daab-f6d9-4b19-96b5-238249e09fb9) and on the [climate engine org dataset page here](https://support.climateengine.org/article/91-can-drought).

#### Dataset Description

**Categorical Values**

| Value    | Interpretation         |
|----------|------------------------|
| -9999    | NoData Value           |
| 0        | No data                |
| 1        | Drought removal        |
| 2        | Drought improves       |
| 3        | Drought develops       |
| 4        | Drought persists       |
| 5        | Drought worsens        |

**Spatial Information**

| Parameter            | Value                 |
|----------------------|-----------------------|
| Spatial extent       | Canada                |
| Spatial resolution   | ~0.8-km (1/100-deg)   |
| Temporal resolution  | Monthly               |
| Time span            | 2021-06-01 to present |
| Update frequency     | Updated first week of each month |

**Variables**

| Variable                | Details                          |
|-------------------------|----------------------------------|
| Drought category ('drought_outlook_class') | - Units: Drought outlook classification |
|                         | - Scale factor: 1.0                |


#### Citation

```
Agriculture and Agri-Food Canada, 2021, "Canadian Drought Outlook", Agroclimate, Geomatics and Earth Observation Division, Science and Technology
Branch.
```

![canadian_drght_outlook](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/d3d1d2db-2955-4e4f-801a-789ce3167062)

#### Earth Engine Snippet

```js
// Read in Image Collection and get single image
var cdo_ic = ee.ImageCollection('projects/climate-engine-pro/assets/ce-aafc-cdo-monthly')
var cdo_i = cdo_ic.first()

// Print image to see bands
print(cdo_i)

// Visualize a single image
var cdo_palette = ["#ffffff", "#4a7733", "#dfb73d", "#b6a083", "#775412", "#c24d1b"]
Map.addLayer(cdo_i, {min:0, max:4, palette: cdo_palette}, 'cdo_i')
```

Sample code:  https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/CANADA-DROUGHT-OUTLOOK

#### License

Data are subject to the Government of Canada Open Data Licence Agreement: https://open.canada.ca/en/open-government-licence-canada. The terms of this Agreement govern your use and reproduction of the data instead of the copyright reproduction statements found in Important Notices on the Agriculture and Agri-Food Canada website.

Keywords: drought, Canada, forecast, AAFC

Provided by: Agriculture and Agri-Food Canada (AAFC)

Curated in GEE by: Climate Engine Org
