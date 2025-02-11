# Urban Sky Open Data

Urban Sky recently provided open and freely available high-resolution aerial and thermal imagery captured from stratospheric Microballoons over the LA fires. The dataset includes both RGB imagery at 10cm resolution and Long-Wave Infrared (LWIR) thermal imagery at 3m resolution, with coverage focused on wildfire events and urban areas. The Microballoon platform operates at altitudes of 15-21km, providing a unique vantage point that avoids interference with firefighting aircraft while maintaining high-resolution imaging capabilities.

## Technical Specifications of Images Shared

#### RGB Imagery Specifications

<center>

| Parameter | Value |
|-----------|--------|
| Spatial Resolution | 10.0 cm |
| Flight Altitude | 15-21 km |
| Sensor Bands | Red, Green, Blue (RGB) |
| Sensor Color Sampling | RGGB color filter array |
| Sensor Dynamic Range | 12 bits per sample |
| Product Dynamic Range | 8 bits per sample |
| Single Path Swath Width | 10.5-15.0 km (altitude dependent) |
| Off-nadir Look Angle | 20° ± 3° |
| Geolocation Accuracy (CE90) | 3 meters |
| File Format | Cloud-optimized GeoTiffs |
| Processing | Non-uniformity correction, Edge preserving noise reduction, Adaptive tonal curves |
| Compression | High-quality YCbCr JPEG |

</center>

### LWIR Thermal Imagery Specifications

<center>

| Parameter | Value |
|-----------|--------|
| Spatial Resolution | 3.0 m |
| Flight Altitude | 15-21 km |
| Spectral Band | 8μm - 14μm |
| Swath Width | 10-18 km (altitude dependent) |
| Coverage Rate | 50-1,500 km² per hour (1000 km²/hr typical) |
| Scene Dynamic Range | High Gain: Up to 140°C, Low Gain: Up to 500°C |
| Pixel Pitch | 12 μm |
| Thermal Sensitivity | 60 mK |
| Compatible Wind Speeds | 5-90 km/hr |

</center>

Note: STAC metadata was provided with the two images but there href links to the data were missing.

#### Dataset Preprocessing
The STAC metadata was parsed to create properties for the image band names were captures as red, green, blue or thermal to represent LWIR band.

#### Citation

Use the following copyright notice for any data products or derivatives:

"©[YEAR] Urban Sky. All Rights Reserved."

where [YEAR] reflects the year of image acquisition.

![urbansky](https://github.com/user-attachments/assets/6c7c54d7-abca-42f2-81f5-3edb0bc7c06c)

#### Code Snippet

```js
var HIGHRES_RGB = ee.Image("projects/sat-io/open-datasets/URBAN_SKY/USKY01_D00236_010_11S_20250119_20250125200840_A0_000_000_01");
var LWIR_THERMAL = ee.Image("projects/sat-io/open-datasets/URBAN_SKY/USKY02_D00235_400_11S_20250119_20250121015227_A2_000_000_01");

Map.centerObject(LWIR_THERMAL,10)
Map.addLayer(HIGHRES_RGB.mask(HIGHRES_RGB.gt(0)),{},'High Res RGB 10cm')
Map.addLayer(LWIR_THERMAL, {min: 3, max: 215, palette: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#fee090', '#fdae61', '#f46d43', '#d73027']}, 'LWIR Thermal 3m')

var snazzy = require("users/aazuspan/snazzy:styles");
snazzy.addStyle("https://snazzymaps.com/style/15/subtle-grayscale", "Greyscale");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-events-layers/URBAN-SKY-OPENDATA

#### License

This dataset is made available under Creative Commons Attribution 4.0 International License (CC BY 4.0).

#### Contact

For questions about the data or collaboration opportunities, contact Urban Sky at info@urbansky.com

Provided by: Urban Sky

Curated in GEE by: Samapriya Roy

Keywords: aerial imagery, thermal imaging, wildfire monitoring, high-resolution imagery, microballoon, stratospheric imaging, LWIR, RGB imagery

Last updated: 2025-02-11
