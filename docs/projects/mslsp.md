# Multi-Source Land Surface Phenology (MSLSP) North America 30m

The Multi-Source Land Surface Phenology (LSP) Yearly North America 30 meter (m) Version 1.1 product (MSLSP) provides Land Surface Phenology data for North America derived from Harmonized Landsat Sentinel-2 (HLS) data. The product combines data from Landsat 8 OLI and Sentinel-2A/B MSI to provide phenophase transition dates including greenup, maturity, senescence, and dormancy timing at 30 meter resolution.

These datasets support various applications including:
- Ecosystem and agro-ecosystem modeling
- Monitoring terrestrial ecosystem responses to climate variability and extreme events
- Crop-type discrimination
- Land cover, land use, and land cover change mapping

The MSLSP product includes layers for percent greenness, onset greenness dates, Enhanced Vegetative Index (EVI2) amplitude, maximum EVI2, and data quality information for up to two phenological cycles per year. Data gaps due to cloud cover or other factors are filled using good quality values from adjacent years. The data can be [accessed here](https://lpdaac.usgs.gov/products/mslsp30nav011/#tools)

#### Version Improvements

Version 1.1 includes:
- Modified spline fitting algorithm with 20+ day gap filling
- Updated Quality Assurance (QA) fields (values 1-6, 9, 10)
- New layers: Peak date and number of clear observations

#### Layers

??? example "Expand to show layer information"

    <center>

    | Layer Name | Description | Units | Data Type | Fill Value | Valid Range | Scale Factor |
    |------------|-------------|--------|------------|------------|--------------|--------------|
    | 50PCGD¹ | 50 Percent Greenness Decrease | Day | Int16 | 32767 | -181 to 548 | N/A |
    | 50PGCD_2¹ | Cycle 2 - 50 Percent Greenness Decrease | Day | Int16 | 32767 | -181 to 548 | N/A |
    | 50PCGI¹ | 50 Percent Greenness Increase | Day | Int16 | 32767 | -181 to 548 | N/A |
    | 50PCGI_2¹ | Cycle 2 - 50 Percent Greenness Increase | Day | Int16 | 32767 | -181 to 548 | N/A |
    | EVIamp | EVI2 Amplitude during vegetation cycle | N/A | Int16 | 32767 | 0 to 10000 | 0.0001 |
    | EVIamp_2 | Cycle 2 - EVI2 Amplitude | N/A | Int16 | 32767 | 0 to 10000 | 0.0001 |
    | EVIarea | Integrated EVI2 during vegetative cycle | N/A | Int16 | 32767 | 0 to 32766 | 0.01 |
    | EVIarea_2 | Cycle 2 - Integrated EVI2 | N/A | Int16 | 32767 | 0 to 32766 | 0.01 |
    | EVImax | Maximum EVI2 during vegetation cycle | N/A | Int16 | 32767 | 0 to 10000 | 0.0001 |
    | EVImax_2 | Cycle 2 - Maximum EVI2 | N/A | Int16 | 32767 | 0 to 10000 | 0.0001 |
    | NumCycles | Number of phenological cycles | Number | Int16 | 32767 | 0 to 6 | N/A |
    | OGD¹ | Onset Greenness Decrease (10%) | Day | Int16 | 32767 | -181 to 548 | N/A |
    | OGD_2¹ | Cycle 2 - Onset Greenness Decrease (10%) | Day | Int16 | 32767 | -181 to 548 | N/A |
    | OGI¹ | Onset Greenness Increase (15%) | Day | Int16 | 32767 | -181 to 548 | N/A |
    | OGI_2¹ | Cycle 2 - Onset Greenness Increase (15%) | Day | Int16 | 32767 | -181 to 548 | N/A |
    | OGMn¹ | Onset Greenness Minimum (85%) | Day | Int16 | 32767 | -181 to 548 | N/A |
    | OGMn_2¹ | Cycle 2 - Onset Greenness Minimum (85%) | Day | Int16 | 32767 | -181 to 548 | N/A |
    | OGMx¹ | Onset Greenness Maximum (90%) | Day | Int16 | 32767 | -181 to 548 | N/A |
    | OGMx_2¹ | Cycle 2 - Onset Greenness Maximum (90%) | Day | Int16 | 32767 | -181 to 548 | N/A |
    | Peak | Date of Cycle Peak | Day | Int16 | 32767 | 1 to 366 | N/A |
    | Peak_2 | Cycle 2 - Date of Cycle Peak | Day | Int16 | 32767 | 1 to 366 | N/A |
    | gdownQA | Quality Assurance for Greendown Segment | N/A | Int16 | 32767 | 1 to 7 | N/A |
    | gdownQA_2 | Cycle 2 - QA for Greendown Segment | N/A | Int16 | 32767 | 1 to 7 | N/A |
    | gupQA | Quality Assurance for Greenup Segment | N/A | Int16 | 32767 | 1 to 7 | N/A |
    | gupQA_2 | Cycle 2 - QA for Greenup Segment | N/A | Int16 | 32767 | 1 to 7 | N/A |

¹Some phenological cycles span multiple years therefore estimated phenometrics for a given year of interest can include dates that occur ~180 days prior to or beyond the year of interest. This is identified in the valid range from -181 to 548.

#### Quality Assurance Values

??? example "Expand to show Quality Assurance Band Values"

    <center>

    | QA Value | Description |
    |----------|-------------|
    | 1 | High Quality |
    | 2 | Moderate Quality |
    | 3 | Poor Quality with Successful Fill |
    | 4 | Poor Quality with Unsuccessful Fill |
    | 5 | No Cycle Detected |
    | 6 | Water, Algorithm Not Run |
    | 7 | Border Pixels Masked (2016) |

#### Known Issues

- Data sparsity in 2016-2017 due to limited Sentinel-2 coverage
- Disturbance events may cause premature senescence/dormancy detection
- Limited accuracy for areas with >2 growth cycles per year

#### Citation

```
Bolton, D. K., Gray, J.M, Melaas, E.K., Moon, M., Eklundh, L. and M.A. Friedl (2020). Continental-scale land surface phenology from harmonized Landsat 8 and Sentinel-2 imagery, Remote Sensing of Environment, 240, https://doi.org/10.1016/j.rse.2020.111685
```

#### Dataset Citation

```
Friedl, M.. MuSLI Multi-Source Land Surface Phenology Yearly North America 30 m V011. 2021, distributed by NASA EOSDIS Land Processes Distributed Active Archive Center, https://doi.org/10.5067/Community/MuSLI/MSLSP30NA.011. Accessed 2025-02-18.
```

#### Earth Engine Snippet

```js
var mslsp_2016 = ee.ImageCollection("projects/sat-io/open-datasets/MUSLI/MSLSP_2016");
var mslsp_2017 = ee.ImageCollection("projects/sat-io/open-datasets/MUSLI/MSLSP_2017");
var mslsp_2018 = ee.ImageCollection("projects/sat-io/open-datasets/MUSLI/MSLSP_2018");
var mslsp_2019 = ee.ImageCollection("projects/sat-io/open-datasets/MUSLI/MSLSP_2019");
```

Sample Script: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/MSLSP-YEARLY

#### License

Unless the content is marked with a use restriction or license, data provided from a NASA led mission are licensed as Creative Commons Zero (CC0).

Keywords : phenology, vegetation, landsat, sentinel, remote sensing, north america, EVI, NDVI, land surface

Created by: NASA, Friedl et al

Curated in GEE by: Samapriya Roy

Last updated: 2023-12-07

Last updated in GEE: 2025-12-31
