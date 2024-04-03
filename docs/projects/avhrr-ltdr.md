# ESA Fire Disturbance Climate Change Initiative (CCI)

The ESA Fire Disturbance Climate Change Initiative (CCI) project has produced maps of global burned area derived from satellite observations. The AVHRR - LTDR Pixel v1.1 product described here contains gridded data of global burned area derived from spectral information from the AVHRR (Advanced Very High Resolution Radiometer) Land Long Term Data Record (LTDR) v5 dataset produced by NASA.

The dataset provides monthly information on global burned area at 0.05-degree spatial resolution (the resolution of the AVHRR-LTDR input data) from 1982 to 2018. The year 1994 is omitted as there was not enough input data for this year. The dataset is distributed in monthly GeoTIFF files, packed in annual tar.gz files, and it includes 5 files: date of BA detection (labelled JD), confidence label (CL), burned area in each pixel (BA), number of observations in the month (OB) and a metadata file. For further information on the product and its format see the Product User Guide. You can download the datasets [from this link](https://catalogue.ceda.ac.uk/uuid/b1bd715112ca43ab948226d11d72b85e)

The Spatial resolution of this BA product is 0.05 degrees, which is the resolution of the AVHRR-LTDR input data.

The Coordinate Reference System (CRS) used is a geographic coordinate system (GCS) based on the World Geodetic System 84 (WGS84) reference ellipsoid and using a Plate CarrÃ©e projection with geographical coordinates of equal pixel size.This product is distributed in global monthly files, grouped by year.

Details of the Pixel product
---------------------------
The pixel product is composed of 5 files:

* JD.tif: Day of first detection (Julian Day) of the burned area
* CL.tif: Confidence level of burned area detection
* BA.tif: Burned area corresponding to the proporcion of the pixel that is calculated as burned.
* OB.tif: Number of observations, i.e. times that the pixel has been observed in the month.
* xml: Metadata of the product

#### Pixel Attribute Summary

| Attribute | Units | Data Type | Notes |
|---|---|---|---|
| Date of the first detection (JD) | Day of the year (1-366) | Float |  - 0: Not burned - 1-366: Day of first detection for burned pixel  - -1: Not observed in month  - -2: Not burnable (water, bare land, urban, snow/ice) |
| Confidence level (CL) | 0-100 | Float | - 0: Low burn probability  - 1-100: Increasing burn probability confidence  - -1: Not observed in month  - -2: Not burnable (water, bare land, urban, snow/ice) |
| Burned Area (BA) | Square meters | Float | - 0-N: Burned area within pixel cell  - -1: Not observed in month  - -2: Not burnable (water, bare land, urban, snow/ice) |
| Number of observations (OB) | 0-31 | Int16 | - 0-31: No-cloud observations in pixel  - 0: Not observed  - -2: Not burnable (water, bare land, urban, snow/ice) |



#### Citation

```
Chuvieco, E.; Pettinari, M.L.; Otón, G. (2020): ESA Fire Climate Change Initiative (Fire_cci): AVHRR-LTDR Burned Area Pixel product, version 1.1.Centre for Environmental Data Analysis, 21 December 2020. doi:10.5285/b1bd715112ca43ab948226d11d72b85e.
https://dx.doi.org/10.5285/b1bd715112ca43ab948226d11d72b85e
```

![ee_cci](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/7b9e9e10-bf76-48e2-bd0f-3bf6e52d2507)

#### Earth Engine Snippet

```js
var BA = ee.ImageCollection("projects/sat-io/open-datasets/ESA/AVHRR-LTDR/BA");
var CL = ee.ImageCollection("projects/sat-io/open-datasets/ESA/AVHRR-LTDR/CL");
var JD = ee.ImageCollection("projects/sat-io/open-datasets/ESA/AVHRR-LTDR/JD");
var OB = ee.ImageCollection("projects/sat-io/open-datasets/ESA/AVHRR-LTDR/OB");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:fire-monitoring-analysis/ESA-FIRE-DISTURBANCE-CCI

#### License

You can find license information [here](http://licences.ceda.ac.uk/image/data_access_condition/esacci_fire_terms_and_conditions.pdf)

Created by: Chuvieco, E.; Pettinari, M.L.; Otón, G, ESA

Curated in GEE by : Samapriya Roy

keywords: ESA, CCI, Pixel, Burned Area, Fire Disturbance, Climate Change, GCOS Essential Climate Variable

Last modified: 2020-12-21

Last updated on GEE: 2024-04-01
