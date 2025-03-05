# US EPA Total Deposition Layers (TDEP Layers)

The Total Deposition Science Committee (TDep) provides estimates of total nitrogen and sulfur deposition fluxes across the United States for use in critical loads and other ecological assessments, particularly where loading results in the acidification and eutrophication of ecosystems. Total deposition flux estimates are derived from summing contributions from wet and dry deposition.

Members of the TDep committee developed and maintain a **measurement-model fusion approach (TDep MMF)** to map total deposition that combines measured and modeled values. This provides a product that utilizes both the accuracy of the measurements and the spatial continuity of modeled estimates. In the TDep MMF, measured values are given more weight at the monitor locations, while modeled data are used to fill in spatial gaps and provide information on chemical species that are not measured by routine monitoring networks.

One of the main advantages to this approach is that it provides continuous spatial and temporal coverage of total deposition estimates in the U.S. (beginning in 2000). This allows the analysis of trends over time for any location. The data is provided at a 4km resolution

## Dataset Description

The TDep MMF products are evaluated and updated annually as both model simulations and measurements become available and as the methodology evolves. TDep MMF map images and gridded data are available as GeoTIFF files on an annual average basis for years 2000-2022 and as 3-year averages for all components of total sulfur and nitrogen deposition.

### Methodology

The TDep MMF combines multiple data sources:

- **Wet deposition values** are obtained from combining NADP/National Trends Network (NADP/NTN) measured values of precipitation chemistry with precipitation estimates from the Parameter-elevation Regression on Independent Slopes Model (PRISM).

- **Dry deposition flux values** are obtained by combining measured air concentration data from the Clean Air Status and Trends Network (CASTNET) with modeled deposition velocities estimated from EPA's Air QUAlity TimE Series Project (EQUATES) using Community Multiscale Air Quality (CMAQ) model 5.3.2.

- **Unmeasured species** (PAN, N2O5, NO, NO2, HONO and organic nitrate) are estimated with the EQUATES dataset.

- **Final total deposition estimates** are produced by combining dry deposition values with wet deposition values.

#### Variables Available

??? example "Expand to show Variable information. The following variables are available in the TDEP dataset"

    <center>

    | Variable   | Description                                                                  | Units    |
    | ---------- | ---------------------------------------------------------------------------- | -------- |
    | bc_dw      | Dry equivalent deposition of all base cations                                | keq/ha   |
    | bc_dwpct   | Dry deposition of base cations as percent of total (wet + dry) deposition    | Percent  |
    | bc_tw      | Total equivalent deposition of all base cations                              | keq/ha   |
    | ca_dw      | Dry deposition of calcium                                                    | kg-Ca/ha |
    | ca_tw      | Total deposition of calcium                                                  | kg-Ca/ha |
    | ca_ww      | Wet deposition of calcium                                                    | kg-Ca/ha |
    | cl_dw      | Dry deposition of chlorine                                                   | kg-Cl/ha |
    | cl_tw      | Total deposition of chlorine                                                 | kg-Cl/ha |
    | cl_ww      | Wet deposition of chlorine                                                   | kg-Cl/ha |
    | hno3_dw    | Total deposition of nitric acid                                              | kg-N/ha  |
    | k_dw       | Dry deposition of potassium                                                  | kg-K/ha  |
    | k_tw       | Total deposition of potassium                                                | kg-K/ha  |
    | k_ww       | Wet deposition of potassium                                                  | kg-K/ha  |
    | mg_dw      | Dry deposition of magnesium                                                  | kg-Mg/ha |
    | mg_tw      | Total deposition of magnesium                                                | kg-Mg/ha |
    | mg_ww      | Wet deposition of magnesium                                                  | kg-Mg/ha |
    | n_dw       | Dry deposition of nitrogen                                                   | kg-N/ha  |
    | n_dwpct    | Dry deposition of nitrogen as percent of total (wet + dry) deposition        | Percent  |
    | n_tw       | Total (wet + dry) nitrogen deposition                                        | kg-N/ha  |
    | n_ww       | Wet deposition of nitrogen                                                   | kg-N/ha  |
    | n_wwpct    | Wet deposition of nitrogen as percent of total (wet + dry) deposition        | Percent  |
    | na_dw      | Dry deposition of sodium                                                     | kg-Na/ha |
    | na_tw      | Total deposition of sodium                                                   | kg-Na/ha |
    | na_ww      | Wet deposition of sodium                                                     | kg-Na/ha |
    | nh3_dw     | Dry deposition of ammonia                                                    | kg-N/ha  |
    | nh4_dw     | Dry deposition of particulate ammonium                                       | kg-N/ha  |
    | nh4_ww     | Wet deposition of particulate ammonium                                       | kg-N/ha  |
    | no3_dw     | Dry deposition of particulate nitrate                                        | kg-N/ha  |
    | no3_ww     | Wet deposition of particulate nitrate                                        | kg-N/ha  |
    | nom_dw     | Dry deposition of unmeasured nitrogen species*                               | kg-N/ha  |
    | nom_dwpct  | Dry deposition of unmeasured nitrogen species as percent of total deposition | Percent  |
    | noxi_dw    | Dry deposition of oxidized nitrogen                                          | kg-N/ha  |
    | noxi_dwpct | Dry deposition of oxidized nitrogen as percent of total deposition           | Percent  |
    | noxi_tw    | Total (wet + dry) deposition of oxidized nitrogen                            | kg-N/ha  |
    | noxi_twpct | Total deposition of oxidized nitrogen as percent of total deposition         | Percent  |
    | nred_dw    | Dry deposition of reduced nitrogen                                           | kg-N/ha  |
    | nred_dwpct | Dry deposition of reduced nitrogen as percent of total deposition            | Percent  |
    | nred_tw    | Total (wet + dry) deposition of reduced nitrogen                             | kg-N/ha  |
    | nred_twpct | Total deposition of reduced nitrogen as percent of total deposition          | Percent  |
    | ns_tw      | Total equivalent nitrogen + sulfur deposition                                | keq/ha   |
    | precip_ww  | Annual precipitation                                                         | cm       |
    | s_dw       | Dry deposition of sulfur                                                     | kg-S/ha  |
    | s_dwpct    | Dry deposition of sulfur as percent of total deposition                      | Percent  |
    | s_tw       | Total (wet + dry) sulfur deposition                                          | kg-S/ha  |
    | s_ww       | Wet deposition of sulfur                                                     | kg-S/ha  |
    | s_wwpct    | Wet deposition of sulfur as percent of total deposition                      | Percent  |
    | so2_dw     | Dry deposition of sulfur dioxide                                             | kg-S/ha  |
    | so4_dw     | Dry deposition of particulate sulfate                                        | kg-S/ha  |
    | tno3_dw    | Dry deposition of nitric acid + particulate nitrate                          | kg-N/ha  |

*Unmeasured nitrogen species include nitrous acid (HONO), nitrogen pentoxide (N2O5), nitric oxide (NO), nitrogen dioxide (NO2), organic nitrate (NTR), peroxyacyl nitrate (PAN), aromatic PANs (OPAN), and C3 and higher PANs (PANX)

#### Known Limitations and Caveats

- There is likely an incomplete characterization of the wet and dry organic N components, resulting in an underestimate of total nitrogen deposition.
- Since the measurement sites used in the method are located in primarily rural areas, deposition in urban areas may not be well represented.
- Interpolation techniques inherently minimize extreme values, so more variability would be expected if more spatially resolved observations were available.
- The use of monitoring data is limited to sites and times that meet network completion criteria, which may cause discontinuities in temporal and spatial trends at specific locations.
- Data sparsity in certain regions may affect accuracy.
- Possible classification uncertainties exist in areas with complex deposition patterns.
- Limited accuracy in areas with rapid land use change.

#### References

```
Schwede, D.B. and G.G. Lear, 2014. A novel hybrid approach for estimating total deposition in the United States, Atmospheric Environment, 92, 207-220. 10-15. 10.1016/j.atmosenv.2014.04.008.

National Atmospheric Deposition Program, 2024. Total Deposition Maps README. Total Deposition Estimates Using the Measurement Model Fusion (TDep MMF version 2023.01) Approach with Modeled and Monitoring.
https://nadp.slh.wisc.edu/committees/tdep/ . [4/17/24].
```

#### Citation

Suggested citation for data or maps from this project:

```
National Atmospheric Deposition Program, 2023. Total Deposition Maps, version 2023.01.
https://nadp.slh.wisc.edu/committees/tdep/ . [date accessed].
```

![Image](https://github.com/user-attachments/assets/291a7a10-c03a-4b3e-b599-7f81640dc8ad)

#### Earth Engine Snippet

```js
// Base cations collections
var bc_dw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/BC_DW');
var bc_dwpct = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/BC_DWPCT');
var bc_tw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/BC_TW');

// Calcium collections
var ca_dw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/CA_DW');
var ca_tw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/CA_TW');
var ca_ww = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/CA_WW');

// Chlorine collections
var cl_dw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/CL_DW');
var cl_tw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/CL_TW');
var cl_ww = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/CL_WW');

// Nitrogen compounds
var hno3_dw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/HNO3_DW');
var nh3_dw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/NH3_DW');
var nh4_dw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/NH4_DW');
var nh4_ww = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/NH4_WW');
var no3_dw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/NO3_DW');
var no3_ww = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/NO3_WW');
var tno3_dw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/TNO3_DW');

// Potassium collections
var k_dw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/K_DW');
var k_tw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/K_TW');
var k_ww = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/K_WW');

// Magnesium collections
var mg_dw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/MG_DW');
var mg_tw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/MG_TW');
var mg_ww = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/MG_WW');

// Sodium collections
var na_dw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/NA_DW');
var na_tw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/NA_TW');
var na_ww = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/NA_WW');

// Total nitrogen collections
var n_dw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/N_DW');
var n_dwpct = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/N_DWPCT');
var n_tw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/N_TW');
var n_ww = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/N_WW');
var n_wwpct = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/N_WWPCT');

// Unmeasured nitrogen species
var nom_dw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/NOM_DW');
var nom_dwpct = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/NOM_DWPCT');

// Oxidized nitrogen
var noxi_dw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/NOXI_DW');
var noxi_dwpct = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/NOXI_DWPCT');
var noxi_tw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/NOXI_TW');
var noxi_twpct = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/NOXI_TWPCT');

// Reduced nitrogen
var nred_dw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/NRED_DW');
var nred_dwpct = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/NRED_DWPCT');
var nred_tw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/NRED_TW');
var nred_twpct = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/NRED_TWPCT');

// Nitrogen + sulfur
var ns_tw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/NS_TW');

// Precipitation
var precip_ww = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/PRECIP_WW');

// Sulfur collections
var s_dw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/S_DW');
var s_dwpct = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/S_DWPCT');
var s_tw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/S_TW');
var s_ww = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/S_WW');
var s_wwpct = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/S_WWPCT');
var so2_dw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/SO2_DW');
var so4_dw = ee.ImageCollection('projects/sat-io/open-datasets/TDEP/tdep-annual/SO4_DW');
```

Sample Script: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/US-EPA-TDEP

Sample App: https://space-geographer.projects.earthengine.app/view/tdep

#### License

The TDEP data layers are distributed under a license similar to Public domain license and distributed by United States Environmental Protection Agency (EPA).

Keywords: atmospheric deposition, nitrogen, sulfur, air quality, precipitation, wet deposition, dry deposition, NADP, CMAQ, atmospheric modeling

Created by: United States Environmental Protection Agency (EPA) and the National Atmospheric Deposition Program (NADP)

Curated in GEE by: Samapriya Roy

Last updated: 2023-11-28

Last updated in GEE: 2025-03-05
