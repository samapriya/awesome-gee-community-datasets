# Snow Data Assimilation System (SNODAS)
The Snow Data Assimilation System (SNODAS) represents a comprehensive modeling and data assimilation system meticulously developed by the National Operational Hydrologic Remote Sensing Center (NOHRSC). Its primary objective is to provide highly accurate estimations of snow cover and associated parameters, serving as a crucial resource for hydrologic modeling and analysis. SNODAS achieves this by assimilating data from a diverse array of sources, including satellite observations, ground-based measurements, and numerical weather prediction models. These disparate data streams undergo thorough processing within a snow mass and energy balance model, ultimately yielding estimations of snow water equivalent (SWE), snow depth, snow cover extent, and snow albedo.

The SNODAS dataset boasts a spatial resolution of 1 km and a temporal resolution of 24 hours, ensuring precise and timely insights. Updated daily, the dataset encompasses the continental United States, Alaska, and Hawaii, offering comprehensive coverage for users across a spectrum of applications. SNODAS data caters to a wide-ranging audience, including water resource managers, emergency responders, and climate scientists. These invaluable data play a pivotal role in diverse applications, including estimating snowmelt runoff, forecasting snow avalanches, monitoring snowpack conditions for drought and flood management, and conducting studies on the influence of climate change on snow dynamics. SNODAS data is freely accessible through the National Snow and Ice Data Center (NSIDC), further enhancing its accessibility and utility for a broad user base.

This dataset description provides a comprehensive overview of SNODAS, emphasizing its significance in supporting hydrologic research and decision-making across various domains. You can find [additional information here](https://nsidc.org/data/g02158) and you can also find link to the dataset in [climate engine org here](https://support.climateengine.org/article/44-snodas)

#### Dataset details

<center>

| **Spatial extent**   | Conterminous US                             |
|----------------------|--------------------------------------------|
| **Spatial resolution**| 1000 m (1/120-deg)                        |
| **Temporal resolution**| Daily                                  |
| **Time span**        | 2003-10-01 to present                     |
| **Update frequency** | Updated daily with 1 day lag             |

</center>

**Variables**

<center>

| Variable                | Units          | Scale Factor  |
|------------------------|-----------------|---------------|
| Snow Water Equivalent   | Meters          | 1.0           |
| Snow Depth              | Meters          | 1.0           |

</center>

#### Citation

```
Barrett, Andrew. 2003. National Operational Hydrologic Remote Sensing Center Snow Data Assimilation System (SNODAS) Products at NSIDC. NSIDC Special
Report 11. Boulder, CO USA: National Snow and Ice Data Center. 19 pp.

Barrett, A. P., R. L. Armstrong, and J. L. Smith. 2001. The Snow Data Assimilation System (SNODAS): An overview.
Journal of Hydrometeorology 2(3):288-306.
```

![snodas_img](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/8fce65c6-84c0-44c6-bab1-749e8f0d4f33)

### Earth Engine Snippet

```js
// Read in Image Collection and get image
var snodas_ic = ee.ImageCollection('projects/earthengine-legacy/assets/projects/climate-engine/snodas/daily')
var snodas_i = snodas_ic.filterDate('2022-01-01', '2022-01-05').first()

// Print first image to see bands
print(snodas_i)

// Visualize select bands from first image
var prec_palette = ["#ffffcc", "#c7e9b4", "#7fcdbb", "#41b6c4", "#1d91c0", "#225ea8", "#0c2c84"]
Map.addLayer(snodas_i.select('Snow_Depth'), {min: 0, max: 1, palette: prec_palette}, 'Snow_Depth')
Map.addLayer(snodas_i.select('SWE'), {min: 0, max: 1, palette: prec_palette}, 'SWE')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/SNODAS-DAILY

### License

NOAA data, information, and products, regardless of the method of delivery, are not subject to copyright and carry no restrictions on their subsequent use by the public. Once obtained, they may be put to any lawful use. The forgoing data is in the public domain and is being provided without restriction on use and distribution. For more information visit the NWS disclaimer site.

Keywords: snow, climate, near real-time, CONUS, United States, NOAA, daily

Created & provided by: NOAA, NSIDC

Curated by: Climate Engine Org
