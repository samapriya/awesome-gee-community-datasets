# Vegetation Drought Response Index (VegDRI)

The Vegetation Drought Response Index (VegDRI) is a weekly geospatial model that depicts drought stress on vegetation within the conterminous United States. The development of the VegDRI drought-monitoring tool was a collaborative effort by scientists at the USGS EROS Center, the National Drought Mitigation Center (NDMC) at the University of Nebraska, and the High Plains Regional Climate Center (HPRCC).

VegDRI methodology integrates remote sensing data from NASA’s Moderate Resolution Imaging Spectroradiometer (MODIS) sensor on the Terra platform with climate and biophysical data to create a seamless product with a 1 km spatial resolution. The satellite components related to general vegetation conditions are Percent Annual Seasonal Greenness (PASG) and Start of Season Anomaly (SOSA) data. PASG is calculated weekly from eMODIS Normalized Difference Vegetation Index (NDVI) composites.

The climate-based drought data include the Palmer Drought Severity Index (PDSI) and weekly Standardized Precipitation Index (SPI) data from the HPRCC. Climate data identify areas that are experiencing dryness to help distinguish vegetation stress due to drought. The biophysical characteristics of the environment are derived from land use/land cover, soil available water capacity, ecological setting, irrigation status, and elevation data.  Environmental stressors such as land use change, soil conditions, pest infestations, disease, hail, flooding, or fire can also influence vegetation conditions.

This integrated approach considers climate and biophysical conditions to determine the cause of vegetation stress. This information is incorporated into the calculation of VegDRI to create an easy to interpret, color-coded map of drought stress on vegetation.  Drought-monitoring maps are produced every week using the latest information and are usually posted each Monday by 10:30 a.m. CT. You can get access to [Climate Engine ORG's website here](https://support.climateengine.org/article/141-vegdri). Additional information about DRI can be found [here](https://vegdri.unl.edu/Home.aspx) and from [USGS here](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-vegetation-monitoring-vegetation-drought-response-index)

#### Dataset Description

**Spatial Information**

| **Attribute**         | **Details**                                      |
|-----------------------|--------------------------------------------------|
| **Spatial extent**    | Conterminous United States                       |
| **Spatial resolution**| 1000m                                            |
| **Temporal resolution**| Weekly                                          |
| **Time span**         | 2009-04-22 to present                            |
| **Update frequency**  | Weekly on Monday by 10:30 a.m. CT                |

**Variables**

| **Variable**          | **Units** | **Offset** | **Scale factor** | **Description**                                                                                              |
|-----------------------|-----------|------------|------------------|--------------------------------------------------------------------------------------------------------------|
| **VegDRI (‘vegdri’)** | Unitless  | -128       | 0.0625           | Values provided as 8-bit integers that can be scaled to range consistent with Palmer Drought Severity Index. |
| **Water (‘water’)**   | Unitless  | N/A        | 1.0              | Binary mask of water.                                                                                        |
| **Out-of-Season (‘out_of_season’)**| Unitless  | N/A        | 1.0              | Binary mask of out-of-season (see documentation for more information).                                       |

#### Citation

```
Brown, J. F., Wardlow, B. D., Tadesse, T., Hayes, M. J., & Reed, B. C. (2008). The Vegetation Drought Response Index (VegDRI): A New Integrated
Approach for Monitoring Drought Stress in Vegetation. GIScience & Remote Sensing, 45(1), 16–46. https://doi.org/10.2747/1548-1603.45.1.16
```
![veg_dri](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/1342c902-777d-491c-aabd-9f6c737de573)

#### Earth Engine Snippet

```js
// Import VegDRI
var vegdri_ic = ee.ImageCollection('projects/climate-engine-pro/assets/ce-veg-dri')
var vegdri_i = vegdri_ic.first()
print(vegdri_i)

// Link to methods webpage: https://www.usgs.gov/special-topics/monitoring-vegetation-drought-stress/science/methods-vegdri
// Link to EROS page: https://www.usgs.gov/centers/eros/science/usgs-eros-archive-vegetation-monitoring-vegetation-drought-response-index

// VegDRI data are stored as 8-bit integer data and can be scaled into the values below
// Drought categories from EROS page
// Category           Bitmap      PDSI vals
// Extreme drought:   001-064     -7.9375 - -4.0000
// Severe drought:    065-080     -3.9375 - -3.0000
// Moderate drought:  081-096     -2.9375 - -2.0000
// Abnormally dry:    097-112     -1.9375 - -1.0000
// Near normal:       113-160     -0.9375 - 2.0000
// Abnormally wet:    161-176     2.0625 - 3.0000
// Moderately wet:    177-192     3.0625 - 4.0000
// Extremely wet:     193-255     4.0625 - 7.7500
// Water:                 253
// Out of season:         254
// Other landcover:       255

// Function to apply stretch to make consistent with values above
function scale_vegdri(img){

  // Select vegdri band and scale to PDSI range.
  var vegdri_scale = img.select('vegdri')
              .subtract(128) // convert to signed 8-bit integer
              .divide(16) // scale to PDSI range
              .rename('vegdri_scale') // rename image
  return img.addBands(vegdri_scale)
}
vegdri_ic = vegdri_ic.map(scale_vegdri)
print(vegdri_ic)

// VegDRI color palette
var vegdri_palette = ["#720206", "#cb3121", "#e36b09", "#fee301", "#ffffff", "#ffffff", "#ffffff", "#88f9c7", "#53c285", "#2b8032"]

// Select individual image and apply to map
var vegdri_i = vegdri_ic.first()
Map.addLayer(vegdri_i.select('vegdri_scale'), {min: -5, max: 5, palette: vegdri_palette}, 'VegDRI')
Map.addLayer(vegdri_i.select('out_of_season'), {min:254, max:254, palette: ['878787']}, 'VegDRI Out-of-Season')
Map.addLayer(vegdri_i.select('water'), {min:253, max:253, palette: ['0000FF']}, 'Water')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:/weather-climate/VEGETATION-DROUGHT-RESPONSE-INDEX

#### License
USGS-authored or produced data and information are considered to be in the U.S. Public Domain.

Dataset provider: USGS

Keywords : Drought, Climate, Remote sensing, MODIS, PDSI, CONUS, United States

Curated in GEE by: Climate Engine Org
