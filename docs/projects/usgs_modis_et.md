# USGS MODIS Evapotranspiration
The evapotranspiration (ET) dataset presented here is the result of remote sensing techniques, primarily harnessing MODIS-thermal imagery alongside global weather datasets. This dataset corresponds to version 5 of the global ET product employed by Climate Engine. It provides valuable insights into the spatiotemporal dynamics of ET, covering the period from 2003 to 2023'. The dataset's cornerstone is the operational Simplified Surface Energy Balance (SSEBop) model, meticulously detailed by Senay et al. (2013). Built upon the foundations of the Simplified Surface Energy Balance (SSEB) approach, initially proposed by Senay et al. in 2007 and further refined in subsequent publications (Senay et al., 2011), the SSEBop model features unique parameterization specifically tailored for operational applications, akin to principles associated with psychrometry. Its robustness is underscored by a comprehensive model evaluation conducted by Velpuri et al. in 2013.

The global ET estimates are meticulously derived by integrating MODIS-based land surface temperature data, acquired from the Aqua satellite, with maximum air temperature data sourced from WorldClim. Additionally, reference ET values are obtained through [global data assimilation systems (GDAS)](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-data-assimilation-system-gdas) for calibration and validation purposes, further enhancing the accuracy of this dataset. This comprehensive approach not only enriches our understanding of the intricate processes of evapotranspiration on a global scale but also offers invaluable temporal and spatial insights into these dynamics. Additional information regarding this [dataset can be found here](https://earlywarning.usgs.gov/fews/search/Global). You can find a link to this dataset [within climate engine org here](https://support.climateengine.org/article/110-usgs-modis-et)

#### Dataset details

<center>

| **Spatial extent**   | Global                                           |
|----------------------|-------------------------------------------------|
| **Spatial resolution**| 1-km grid (1/96-deg)                             |
| **Temporal resolution**| Dekadal, monthly, and yearly                     |
| **Time span**        | 2003 to Present                                 |
| **Update frequency** | Updated every 10-12 days                         |

</center>

**Variables**

<center>

| Variable                | Evapotranspiration (ETa) ('et')                  |
|------------------------|-------------------------------------------------|
| Units                  | Millimeters                                     |
| Scale factor           | 1.0                                             |

</center>

#### Citation

```
Senay, G.B., Kagone S., Velpuri N.M., 2020, Operational Global Actual Evapotranspiration using the SSEBop model: U.S. Geological Survey data release, [https://doi.org/10.5066/P9OUVUUI.](https://doi.org/10.5066/P9OUVUUI) Publication: https://www.mdpi.com/1424-8220/20/7/1915

Senay, G. B., Budde, M. E., & Verdin, J. P. (2011). Enhancing the Simplified Surface Energy Balance (SSEB) approach for estimating landscape ET: Validation with the METRIC model. Agricultural Water Management, 98(4), 606-618.

Senay, G. B., Budde, M., Verdin, J. P., & Melesse, A. M. (2007). A coupled remote sensing and simplified surface energy balance approach to estimate actual evapotranspiration from irrigated fields. Sensors, 7(6), 979-1000.

Velpuri, N. M., Senay, G. B., Singh, R. K., Bohms, S., and Verdin, J. P. (2013). A comprehensive evaluation of two MODIS evapotranspiration products over the conterminous United States: Using point and gridded FLUXNET and water balance ET, Remote Sensing of Environment, 139, 35-49, [(Abstract and Article)](http://dx.doi.org/10.1016/j.rse.2013.07.013)
```

![modis_et_img](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/7e799a2e-ab35-4657-b470-6712ca9e3a1b)

### Earth Engine Snippet

```js
// Read in dekadal, monthly, and annual Image Collections and get single image from each
var modis_et_d_ic = ee.ImageCollection('projects/earthengine-legacy/assets/projects/usgs-ssebop/modis_et_v5_dekadal')
var modis_et_d_i = modis_et_d_ic.first()
var modis_et_m_ic = ee.ImageCollection('projects/earthengine-legacy/assets/projects/usgs-ssebop/modis_et_v5_monthly')
var modis_et_m_i = modis_et_m_ic.first()
var modis_et_a_ic = ee.ImageCollection('projects/earthengine-legacy/assets/projects/usgs-ssebop/modis_et_v5_annual')
var modis_et_a_i = modis_et_a_ic.first()

// Print first image to see bands
print(modis_et_d_i)
print(modis_et_m_i)
print(modis_et_a_i)

// Visualize select bands from first image
var et_palette = ['#f5e4a9', '#fff4ad', '#c3e683', '#6bcc5c', '#3bb369', '#20998f', '#1c8691']
Map.addLayer(modis_et_d_i.select('et'), {min: 0, max: 10, palette: et_palette}, 'et, dekadal')
Map.addLayer(modis_et_m_i.select('et'), {min: 0, max: 30, palette: et_palette}, 'et, monthly')
Map.addLayer(modis_et_a_i.select('et'), {min: 0, max: 1000, palette: et_palette}, 'et, annual')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/USGS-MODIS-ET

#### License
USGS-authored or produced data and information are considered to be in the U.S. Public Domain.

Keywords: evapotranspiration, MODIS, ETa, SSEBop, global, near real-time, monthly, annual, dekadal

Created & provided by: USGS

Curated by: USGS & Climate Engine Org
