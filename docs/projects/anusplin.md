# ANUSPLIN Gridded Climate Dataset

The ANUSPLIN Gridded Climate Dataset for Canada is a station based interpolated dataset produced using the [Australian National University Spline (ANUSPLIN) model](https://support.climateengine.org/article/48-anusplin). It is produced by Agriculture and Agri-Food Canada and covers all of Canada. The dataset is available from 1950-2015 at daily and monthly timesteps for maximum temperature, minimum temperature, and total precipitation at 10km (0.1 degree) resolution. The ANUSPLIN Gridded Climate Dataset for Canada is a comprehensive and station-based interpolated dataset that has been meticulously produced using the [Australian National University Spline (ANUSPLIN) model](https://support.climateengine.org/article/48-anusplin). Created by Agriculture and Agri-Food Canada, this dataset encompasses the entire geographical expanse of Canada and offers a valuable resource for researchers and climate enthusiasts alike.

Researchers and users interested in accessing the dataset can find it through the following external links:
- **Daily Data:** [ANUSPLIN Gridded Climate Dataset for Canada (Daily)](https://cfs.nrcan.gc.ca/projects/3/4)
- **Monthly Data:** [ANUSPLIN Gridded Climate Dataset for Canada (Monthly)](https://cfs.nrcan.gc.ca/projects/3/3)

It provides a detailed view of climate conditions with data available from 1950 to 2015, offering insights into daily and monthly variations in maximum temperature, minimum temperature, and total precipitation. This dataset offers a valuable resource for climate research, environmental studies, and various applications that require historical climate data for Canada and parts of the United States. Researchers can explore climate trends, assess climate change impacts, and derive valuable insights into the region's climate patterns using this comprehensive dataset.

#### Dataset description

**Spatial Information**

| Parameter            | Value                         |
|----------------------|-------------------------------|
| Spatial extent       | United States and Canada       |
| Spatial resolution   | 10-km (~0.1-deg)              |
| Temporal resolution  | Daily and monthly             |
| Time span            | 1950-01-01 to 2015-12-31      |
| Update frequency     | Static                        |

**Variables**

| Variable                  | Details                              |
|---------------------------|--------------------------------------|
| Minimum temperature, 2m (‘maxt’) | - Units: Degrees Celsius             |
|                           | - Scale factor: 1.0                  |
| Maximum temperature, 2m (‘mint’) | - Units: Degrees Celsius             |
|                           | - Scale factor: 1.0                  |
| Precipitation ('pcp')    | - Units: Millimeters                 |
|                           | - Scale factor: 1.0                  |

#### Citation

```
- Hutchinson, M. F., McKenney, D.W., Lawrence, K., Pedlar, J.H., Hopkinson, R.F., Milewska, E., Papadopol, P. (2009).
"Development and testing of Canada-Wide Interpolated Spatial Models of Daily Minimum-Maximum Temperature and Precipitation for 1961-2003."
American Meteorological Society(April): 725-741.

- McKenney, D. W., Hutchinson, M.F., Papadopol, P., Lawrence, K., Pedlar, J., Campbell, K., Milewska, E., Hopkinson, R., Price, D., Owen, T. (2011).
"Customized spatial climate models for North America." Bulletin of American Meteorological Society-BAMS December: 1612-1622.
```

![anusplin_grid](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/ab19fbdd-9a26-4cb5-96ef-e3f2c2feacc8)

#### Earth Engine Snippet

```js
// Read in daily and monthly Image Collections and get single image from each collection
var anuspline_m_ic = ee.ImageCollection('projects/climate-engine-pro/assets/ce-anusplin-monthly')
var anuspline_m_i = anuspline_m_ic.first()
var anuspline_d_ic = ee.ImageCollection('projects/climate-engine-pro/assets/ce-anusplin-daily')
var anuspline_d_i = anuspline_d_ic.first()

// Print each single image to see bands
print(anuspline_m_i)
print(anuspline_d_i)

// Visualize each band from each single image
var prec_palette = ["#ffffcc", "#c7e9b4", "#7fcdbb", "#41b6c4", "#1d91c0", "#225ea8", "#0c2c84"]
var temp_palette = ["#b2182b", "#ef8a62", "#fddbc7", "#f7f7f7", "#d1e5f0", "#67a9cf", "#2166ac"].reverse()
Map.addLayer(anuspline_m_i.select('pcp'), {min: 0, max: 200, palette: prec_palette}, 'pcp, monthly')
Map.addLayer(anuspline_m_i.select('mint'), {min: -30, max: 30, palette: temp_palette}, 'mint, monthly')
Map.addLayer(anuspline_m_i.select('maxt'), {min: -30, max: 30, palette: temp_palette}, 'maxt, monthly')

Map.addLayer(anuspline_d_i.select('pcp'), {min: 0, max: 10, palette: prec_palette}, 'pcp, daily')
Map.addLayer(anuspline_d_i.select('mint'), {min: -30, max: 30, palette: temp_palette}, 'mint, daily')
Map.addLayer(anuspline_d_i.select('maxt'), {min: -30, max: 30, palette: temp_palette}, 'maxt, daily')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/ANUSPLIN-GRID

#### License

Data are subject to the Government of Canada Open Data Licence Agreement: https://open.canada.ca/en/open-government-licence-canada. The terms of this Agreement govern your use and reproduction of the data instead of the copyright reproduction statements found in Important Notices on the Agriculture and Agri-Food Canada website.

Keywords : climate, precipitation, temperature, AAFC, daily, monthly, reanalysis

Provider: Agriculture and Agri-Food Canada

Curator: ClimateEngine.org
