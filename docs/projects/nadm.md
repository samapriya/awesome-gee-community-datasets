# North American Drought Monitor (NADM)
The North American Drought Monitor (NADM) raster dataset is produced by the National Centers for Environmental Information (NCEI) and the National Oceanic and Atmospheric Administration's (NOAA) National Integrated Drought Information System (NIDIS). This dataset is a gridded version of the North American Drought Monitor (NADM) produced by Canadian, Mexican and US authors where for each 2.5-km gridcell, the value is given by the current NADM drought classification for that region is:

Drought categories are coded as the following values in the images:

* NoData Value = -1 = no drought or wet
* 0 = abnormal dry
* 1 = moderate drought
* 2 = severe drought
* 3 = extreme drought
* 4 = exceptional drought

Additional [details can be found here](https://www.ncdc.noaa.gov/temp-and-precip/drought/nadm/) and information about this dataset is also available at [climate engine org](https://support.climateengine.org/article/73-nadm).


#### Dataset details

<center>

| **Spatial extent**   | North America                             |
|----------------------|-------------------------------------------|
| **Spatial resolution**| 2.5-km (0.025 deg)                        |
| **Temporal resolution**| Monthly                                  |
| **Time span**        | 2001-11-01 to present                     |
| **Update frequency** | Updated Monthly                           |

</center>

**Variables**

<center>

| Variable                | Drought category ('nadm')                   |
|------------------------|--------------------------------------------|
| Units                  | Drought classification                      |
| Scale factor           | 1.0                                        |

</center>


#### Citation

```
Heim, Jr., R. R., 2002. A review of Twentieth-Century drought indices used in the United States. Bulletin of the American Meteorological Society, 83, 1149-1165.

Lawrimore, J., et al., 2002. Beginning a new era of drought monitoring across North America. Bulletin of the American Meteorological Society, 83, 1191-1192.

Lott, N., and T. Ross, 2000. NCDC Technical Report 2000-02, A Climatology of Recent Extreme Weather and Climate Events. [Asheville, N.C.]: National Climatic Data Center.

Svoboda, M., et al., 2002. The Drought Monitor. Bulletin of the American Meteorological Society, 83, 1181-1190.
```

![nadm_img](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/bf161494-350b-49da-a724-b55b768c6a50)

#### Earth Engine Snippet

```js
// Read in Image Collection and mosaic to single image
var nadm_ic = ee.ImageCollection('projects/climate-engine/nadm/monthly')
var nadm_i = nadm_ic.first()

// Print image to see bands
print(nadm_i)

// Visualize a single image
var nadm_palette = ["#ffffff", "#ffff00", "#fcd37f", "#ffaa00", "#e60000", "#730000"]
Map.addLayer(nadm_i, {min:-1, max:4, palette: nadm_palette}, 'nadm_i')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/NADM-MONTHLY

#### License

NOAA data, information, and products, regardless of the method of delivery, are not subject to copyright and carry no restrictions on their subsequent use by the public. Once obtained, they may be put to any lawful use. The forgoing data is in the public domain and is being provided without restriction on use and distribution. For more information visit the NWS disclaimer site.

Keywords: drought, NADM, North America, United States, Canada, Mexico

Created & provided by: NOAA, NIDIS, NCEI

Curated by: Climate Engine Org
