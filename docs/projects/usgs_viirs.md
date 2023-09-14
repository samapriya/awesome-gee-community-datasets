# USGS VIIRS Evapotranspiration
The VIIRS Evapotranspiration (ET) dataset, based on Version 6 of the global ET product, is derived from remote sensing utilizing VIIRS thermal imagery and global weather datasets. It employs the SSEBop (Simplified Surface Energy Balance operational version) methodology, initially proposed by Senay et al. in 2007, with specialized parameterization tailored for operational applications using satellite psychrometry principles, as introduced by Senay in 2018. In SSEBop Version 6, the novel Forcing And Normalizing Operation (FANO) algorithm, as outlined by Senay et al. in 2023, is employed to establish the wet-bulb boundary condition, enabling robust modeling of spatiotemporal dynamics of ETa (actual evapotranspiration) across various landscapes and seasons, irrespective of vegetation cover density.

Notably, recent assessments of the global ETa product indicate its promising performance for drought monitoring through ETa Anomaly analysis. However, for studies involving water budget analysis necessitating absolute magnitudes, a local or region-specific bias correction procedure, as detailed by Senay et al. in 2020, may be required. The dataset's creation involves the integration of VIIRS-based land surface temperature, maximum air temperature from WorldClim, and reference ET obtained from gridded weather datasets such as TerraClimate by Abatzoglou et al. (2018) for global coverage and Chiew et al. (2002) for Australia.

#### Dataset details

<center>

| **Spatial extent**   | Global                                           |
|----------------------|-------------------------------------------------|
| **Spatial resolution**| 1-km grid (1/96-deg)                             |
| **Temporal resolution**| Dekadal, monthly, and yearly                     |
| **Time span**        | 2012 to Present                                 |
| **Update frequency** | Updated every 10-12 days                         |

</center>

**Variables**

<center>

| Variable                | Evapotranspiration (ETa) ('et')                  |
|------------------------|-------------------------------------------------|
| Units                  | Millimeters                                     |
| Scale factor           | 1.0                                             |

</center>

### Additional information
You can find additional information on these datasets in the links below
- https://earlywarning.usgs.gov/fews/search/Global
- https://earlywarning.usgs.gov/fews/product/461
- https://earlywarning.usgs.gov/fews/product/460
- https://earlywarning.usgs.gov/fews/product/458

#### Citation

```
Senay, G.B., Parrish, G.E., Schauer, M., Friedrichs, M., Khand, K., Boiko, O., Kagone, S., Dittmeier, R., Arab, S. and Ji, L., 2023. Improving the Operational Simplified Surface Energy Balance Evapotranspiration Model Using the Forcing and Normalizing Operation. Remote Sensing,15(1), p.260. https://doi.org/10.3390/rs15010260

Senay, G.B., Kagone S., Velpuri N.M., 2020, Operational Global Actual Evapotranspiration using the SSEBop model: U.S. Geological Survey data release, [https://doi.org/10.5066/P9OUVUUI.](https://doi.org/10.5066/P9OUVUUI) Publication: https://www.mdpi.com/1424-8220/20/7/1915

Abatzoglou, J., Dobrowski, S., Parks, S. et al. TerraClimate, a high-resolution global dataset of monthly climate and climatic water balance from 1958–2015. Sci Data 5, 170191 (2018). https://doi.org/10.1038/sdata.2017.191

Senay, G. B. (2018). Satellite psychrometric formulation of the Operational Simplified Surface Energy Balance (SSEBop) model for quantifying and mapping evapotranspiration. Applied Engineering in Agriculture, 34(3), 555-566. https://doi.org/10.13031/aea.12614

Velpuri, N. M., Senay, G. B., Singh, R. K., Bohms, S., and Verdin, J. P. (2013). A comprehensive evaluation of two MODIS evapotranspiration products over the conterminous United States: Using point and gridded FLUXNET and water balance ET, Remote Sensing of Environment, 139, 35-49, [(Abstract and Article)](http://dx.doi.org/10.1016/j.rse.2013.07.013)

Senay, G. B., Budde, M., Verdin, J. P., & Melesse, A. M. (2007). A coupled remote sensing and simplified surface energy balance approach to estimate actual evapotranspiration from irrigated fields. Sensors, 7(6), 979-1000.

Chiew, F, Q.J. Wang, F. McConachy, R. James, W. Wright, and G. deHoedt, (2002). Evapotranspiration maps for Australia. Hydrology and Water Resources Symposium, Melbourne, 20-23, 2002, Institution of Engineers, Australia.
```

![viirs_et_img](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/7e799a2e-ab35-4657-b470-6712ca9e3a1b)

#### Earth Engine Snippet

```js
// Read in dekadal, monthly, and annual Image Collections and get single image from each
var viirs_et_d_ic = ee.ImageCollection('projects/usgs-ssebop/viirs_et_v6_dekadal')
var viirs_et_d_i = viirs_et_d_ic.first()
var viirs_et_m_ic = ee.ImageCollection('projects/usgs-ssebop/viirs_et_v6_monthly')
var viirs_et_m_i = viirs_et_m_ic.first()
var viirs_et_a_ic = ee.ImageCollection('projects/usgs-ssebop/viirs_et_v6_annual')
var viirs_et_a_i = viirs_et_a_ic.first()

// Print first image to see bands
print(viirs_et_d_i)
print(viirs_et_m_i)
print(viirs_et_a_i)

// Visualize select bands from first image
var et_palette = ['#f5e4a9', '#fff4ad', '#c3e683', '#6bcc5c', '#3bb369', '#20998f', '#1c8691']
Map.addLayer(viirs_et_d_i.select('et'), {min: 0, max: 10, palette: et_palette}, 'et, dekadal')
Map.addLayer(viirs_et_m_i.select('et'), {min: 0, max: 30, palette: et_palette}, 'et, monthly')
Map.addLayer(viirs_et_a_i.select('et'), {min: 0, max: 1000, palette: et_palette}, 'et, annual')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/USGS-VIIRS-ET

#### License
USGS-authored or produced data and information are considered to be in the U.S. Public Domain.

#### Keywords
VIIRS, remote sensing, satellite, evapotranspiration, monthly, yearly, dekadal, USGS, global

Created & provided by: USGS

Curated by: USGS & Climate Engine Org
