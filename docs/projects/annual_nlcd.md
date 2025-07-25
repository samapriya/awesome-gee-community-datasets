# Annual NLCD Land Cover Dataset

The USGS Land Cover program integrates methodologies from the National Land Cover Database (NLCD) and the Land Change Monitoring, Assessment, and Projection (LCMAP), along with advanced deep learning, to create Annual NLCD a dataset suite that includes six products, each representing various U.S. land cover and change characteristics. The U.S. Geological Survey’s (USGS) Annual NLCD Collection 1.0 leverages innovations from the National Land Cover Database (NLCD) and Land Change Monitoring, Assessment, and Projection (LCMAP) projects, incorporating modern deep learning techniques to deliver accurate, annual land cover and surface change data across the U.S.

Since 1985, Annual NLCD provides six products covering land cover, change, confidence, impervious surfaces, and spectral changes based on Landsat data, facilitating resource management and decision-making.These products leverage Landsat satellite data and are intended for applications in science, resource management, and decision-making, spanning from 1985 to 2024. This dataset supports various environmental analyses, such as urban growth studies, wetland monitoring, agricultural management, and climate impact assessments. Its annual updates and classification confidence features provide essential insights for long-term land use planning and change detection. You can acces [User Guide here](https://www.mrlc.gov/sites/default/files/docs/LSDS-2103%20Annual%20National%20Land%20Cover%20Database%20(NLCD)%20Collection%201%20Science%20Product%20User%20Guide%20-v1.0%202024_10_15.pdf)

#### Dataset Products and Descriptions

- **Land Cover**: A sixteen-class system based on the modified Anderson Level II classification, categorizing dominant surface types like water, forests, and urban areas per pixel. RGB values visually differentiate these categories, ensuring compatibility across federal systems.

- **Land Cover Change**: Tracks annual land cover shifts by comparing consecutive years, using concatenated codes (e.g., 9590 for wetland transitions) to identify changes. Areas without change retain their classification.

- **Land Cover Confidence**: Provides confidence scores based on deep learning probabilities, indicating the model’s certainty in class assignments. Scores are uncalibrated but gauge classification reliability.

- **Fractional Impervious Surface**: Measures the percentage of impermeable surfaces (0-100%) within a 30-meter pixel, informing developed area classifications like urban or suburban based on defined thresholds.

- **Impervious Descriptor**: Differentiates urban, non-urban, and road surfaces within developed areas, offering a clear map of roads distinct from other urban features for detailed analysis.

- **Spectral Change Day of Year**: Identifies the day significant spectral changes occur (values 1-366), pinpointing disturbances (e.g., fires) beyond seasonal variations, enabling temporal change tracking.


??? example "Expand to show Land Cover Classes"

    <center>

    | Class Value | Class Name                   | RGB Color |
    | ----------- | ---------------------------- | --------- |
    | 11          | Open Water                   | `#466b9f` |
    | 12          | Perennial Ice/Snow           | `#d1def8` |
    | 21          | Developed, Open Space        | `#dec5c5` |
    | 22          | Developed, Low Intensity     | `#d99282` |
    | 23          | Developed, Medium Intensity  | `#eb0000` |
    | 24          | Developed, High Intensity    | `#ab0000` |
    | 31          | Barren Land                  | `#b3ac9f` |
    | 41          | Deciduous Forest             | `#68ab5f` |
    | 42          | Evergreen Forest             | `#1c5f2c` |
    | 43          | Mixed Forest                 | `#b5c58f` |
    | 52          | Shrub/Scrub                  | `#ccb879` |
    | 71          | Grassland/Herbaceous         | `#dfdfc2` |
    | 81          | Pasture/Hay                  | `#dcd939` |
    | 82          | Cultivated Crops             | `#ab6c28` |
    | 90          | Woody Wetlands               | `#b8d9eb` |
    | 95          | Emergent Herbaceous Wetlands | `#6c9fb8` |

    </center>

#### Key Information

- **Data Type**: UINT8, UINT16 (product-dependent)
- **Spatial Resolution**: Based on the Landsat 30m grid
- **Temporal Coverage**: 1985–2024 (updated annually)
- **Access**: Products are accessible via multiple platforms, including MRLC Viewer and AWS S3.

<center>

| Layer Name                    | Class Values (Range)         | Min | Max | NoData Value |
|-------------------------------|------------------------------|-----|-----|--------------|
| Land Cover                     | Various land cover types (11, 12, ..., 95) | N/A | N/A | 250          |
| Land Cover Change              | Change class categories     | AABB  | AABB | 9999        |
| Land Cover Confidence          | Confidence levels           | 1   | 100 | 250         |
| Fractional Impervious Surface  | Imperviousness percentage   | 0   | 100 | 250         |
| Impervious Descriptor          | Impervious surface types (0: Non-Urban, 1: Roads, 2: Urban) | N/A | N/A | 250        |
| Spectral Change Day of Year    | Julian days of change       | 1   | 366 | 9999        |

</center>

#### Citation

```
U.S. Geological Survey (USGS), 2024, Annual NLCD Collection 1 Science Products: U.S. Geological Survey data release,
https://doi.org/10.5066/P94UXNTS.
```

![annual_nlcd](https://i.imgur.com/9DlcjOZ.gif)

#### Earth Engine Snippet

```js
var nlcd_landcover = ee.ImageCollection("projects/sat-io/open-datasets/USGS/ANNUAL_NLCD/LANDCOVER");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:regional-landuse-landcover/NLCD-ANNUAL-LANDCOVER

![annual_nlcd_layers-optimized](https://i.imgur.com/GVRiO60.gif)

```js
var nlcd_landcover_confidence = ee.ImageCollection("projects/sat-io/open-datasets/USGS/ANNUAL_NLCD/LANDCOVER_CONFIDENCE");
var nlcd_landcover_change = ee.ImageCollection("projects/sat-io/open-datasets/USGS/ANNUAL_NLCD/LANDCOVER_CHANGE");
var nlcd_fractional_impervious_surface = ee.ImageCollection("projects/sat-io/open-datasets/USGS/ANNUAL_NLCD/FRACTIONAL_IMPERVIOUS_SURFACE");
var nlcd_impervious_descriptor = ee.ImageCollection("projects/sat-io/open-datasets/USGS/ANNUAL_NLCD/IMPERVIOUS_DESCRIPTOR");
var nlcd_spectral_change_doy = ee.ImageCollection("projects/sat-io/open-datasets/USGS/ANNUAL_NLCD/SPECTRAL_CHANGE_DOY");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:regional-landuse-landcover/NLCD-ANNUAL-LANDCOVER-LAYERS

#### License

NLCD datasets are provided under a Creative Commons Zero v1.0 Universal license.

Provided by: USGS

Curated in GEE by: Samapriya Roy

Keywords: Land Cover, Land Change, Landsat, Deep Learning, Annual NLCD, USGS, Environmental Monitoring

#### Changelog
- Added 2024 Annual NLCD layers

Last updated in GEE: 2025-07-08
