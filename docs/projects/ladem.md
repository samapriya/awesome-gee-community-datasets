# Los Angeles Fires 2025 Lidar Collections and Change Analysis

This collection includes both emergency response lidar data and subsequent topographic change analysis for the January 2025 Palisades and Eaton fires in Los Angeles County, California. The dataset combines preliminary post-fire Digital Elevation Models (DEMs) created for immediate disaster response with detailed topographic differencing analysis comparing pre-fire (2016) and post-fire (2025) conditions.

#### Dataset Overview

The collection consists of three main components:

1. Palisades Fire Emergency Response Collection
   - Coverage: 266.77 km²
   - Collection Date: January 21, 2025
   - DOI: https://doi.org/10.5069/G9DR2SPG

2. Eaton Fire Emergency Response Collection
   - Coverage: 152.8 km²
   - Collection Date: January 21-22, 2025
   - DOI: https://doi.org/10.5069/G9JH3JD6

3. Topographic Differencing Analysis
   - Coverage: 378.18 km²
   - Time Span: 2016-2025
   - DOI: https://doi.org/10.5069/G95B00PW

**Important Note**: The emergency response DEMs are preliminary and have not been manually reviewed. NV5 Inc, UCSD, and USGS make no guarantee or warranty as to the data's completeness and accuracy. Users should consider this data provisional.

#### Technical Specifications

<center>

| Parameter | Emergency Response Collections | Differencing Analysis |
|-----------|------------------------------|---------------------|
| Spatial Resolution | 0.5 meter (DTM/DSM) | 1.0 meter |
| Nominal Pulse Spacing | 0.25 meters | N/A |
| Data Format | GeoTIFF | GeoTIFF |
| Collection Period | January 21-22, 2025 | 2016 (pre-fire), Jan 2025 (post-fire) |
| Pre-fire Source | N/A | USGS 3DEP Program |
| Post-fire Source | NV5/AlertCalifornia | NV5/AlertCalifornia |
| Horizontal CRS | NAD83 (2011) / UTM Zone 11N [EPSG: 6340] | WGS 84 / UTM zone 11N [EPSG: 32611] |
| Vertical Datum | NAVD88 (GEOID 18) [EPSG: 5703] | NAVD88 (GEOID 18) [EPSG: 5703] |

</center>

#### Data Products

Emergency Response Collections (per fire area):
- Digital Terrain Model (DTM) - 0.5m resolution
- Digital Surface Model (DSM) - 0.5m resolution

Differencing Analysis:
- Pre-fire DTM and DSM (2016)
- Post-fire DTM and DSM (2025, co-registered)
- Elevation difference products
- Change detection analysis

#### Citations

For complete differencing analysis:
```
Brigham, C., Scott, C., Crosby, C., Beckley, M. (2025). Topographic differencing spanning the 2025 Palisades and Eaton Fires, LA. Distributed by OpenTopography. https://doi.org/10.5069/G95B00PW
```

For Palisades Fire emergency response data:
```
NV5, University of California-San Diego, United States Geological Survey (2025). Preliminary Digital Elevation Models for Palisades Fire, CA 2025. Collected by NV5. Distributed by OpenTopography. https://doi.org/10.5069/G9DR2SPG
```

For Eaton Fire emergency response data:
```
NV5, University of California-San Diego, United States Geological Survey (2025). Preliminary Digital Elevation Models for Eaton Fire, CA 2025. Collected by NV5. Distributed by OpenTopography. https://doi.org/10.5069/G9JH3JD6
```

#### Data Providers and Roles

Emergency Response Collections:
- Funders: University of California San Diego, NV5
- Partners: United States Geological Survey
- Data Collection: NV5

Differencing Analysis:
- Arizona State University
- EarthScope Consortium
- Funding Support:
  - NSF Awards: 2410799, 2410800, 2410801
  - USGS Powell Center: G23AC00336

![Iadem](https://github.com/user-attachments/assets/501e8fb2-5e53-44e1-bac2-163c6436428d)

#### Earth Engine Snippet

```js
// Post-fire Digital Elevation Models (DEM)
var eatonPostfireDEM = ee.Image('projects/sat-io/open-datasets/disaster/EATON_POSTFIRE_DEM_LA25');
var palisadesPostfireDEM = ee.Image('projects/sat-io/open-datasets/disaster/PALISADES_POSTFIRE_DEM_LA25');

// Post-fire Digital Surface Models (DSM)
var eatonPostfireDSM = ee.Image('projects/sat-io/open-datasets/disaster/EATON_POSTFIRE_DSM_LA25');
var palisadesPostfireDSM = ee.Image('projects/sat-io/open-datasets/disaster/PALISADES_POSTFIRE_DSM_LA25');

// DSM Difference Layers (2025-2016)
var eatonDSMDifference = ee.Image('projects/sat-io/open-datasets/disaster/difference_dsm_eaton_2025_2016_aligned_1m');
var palisadesDSMDifference = ee.Image('projects/sat-io/open-datasets/disaster/difference_dsm_palisades_2025_2016_aligned_1m');

// DTM Difference Layers (2025-2016)
var eatonDTMDifference = ee.Image('projects/sat-io/open-datasets/disaster/difference_dtm_eaton_2025_2016_aligned_1m');
var palisadesDTMDifference = ee.Image('projects/sat-io/open-datasets/disaster/difference_dtm_palisades_2025_2016_aligned_1m');
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-events-layers/LA-POSTEVENT-LIDAR

Earth Engine App: https://space-geographer.projects.earthengine.app/view/la-fire-lidar

#### License

All datasets are made available under Creative Commons CC0 1.0 Universal Public Domain Dedication.

#### Access and Download

The datasets can be accessed through OpenTopography:
- Palisades Fire Collection: https://doi.org/10.5069/G9DR2SPG
- Eaton Fire Collection: https://doi.org/10.5069/G9JH3JD6
- Complete Differencing Analysis: https://doi.org/10.5069/G95B00PW

Keywords: lidar, emergency response, disaster response, California wildfires, Palisades Fire, Eaton Fire, DTM, DSM, preliminary data, topographic change, difference analysis

Last updated: 2025-02-14
