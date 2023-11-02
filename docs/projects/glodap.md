# Global Ocean Data Analysis Project (GLODAP) v2.2023

The **Global Ocean Data Analysis Project (GLODAP) v2.2023** represents a significant advancement in the synthesis of ocean biogeochemical bottle data. With a primary focus on seawater inorganic carbon chemistry, this update builds upon GLODAPv2.2022, incorporating several key enhancements. Notably, 43 new cruises have been added to expand the dataset's coverage until 2020. The data quality control process involved the removal of entries with missing temperatures. Moreover, the inclusion of digital object identifiers (DOIs) for each cruise enhances data traceability. GLODAPv2.2022 also includes minor corrections for improved data accuracy.

This dataset encompasses more than 1.4 million water samples from 1108 cruises across the global oceans, covering 12 essential variables such as salinity, oxygen, nitrate, silicate, phosphate, dissolved inorganic carbon, total alkalinity, pH, CFC-11, CFC-12, CFC-113, and CCl4. The data are available in two formats: the raw data format, updated to WOCE exchange format, and a merged data product with bias-minimizing adjustments. Rigorous quality control procedures were applied, and adjustments were made by comparing new cruise data with the quality-controlled data from GLODAPv2.2020. The dataset is believed to provide accurate measurements within specific limits for each variable.

To access this valuable resource and its documentation, including DOIs, visit the Ocean Carbon Data System of NOAA NCEI at [this link](https://www.ncei.noaa.gov/access/ocean-carbon-data-system/oceans/GLODAPv2_2023/). Additionally, the merged data product is available, offering a single global file and regional files for the Arctic, Atlantic, Indian, and Pacific oceans. These files contain ancillary and approximated data, derived from interpolation or calculation. For comprehensive information and data access, please visit [GLODAP's official website](https://www.glodap.info). Researchers can benefit from this living dataset by following the provided resources and documentation.

#### Data Quality and Accuracy
The dataset has undergone extensive quality control with a focus on systematic evaluation of bias. The adjustments made aim to remove potential biases stemming from errors related to measurement, calibration, and data handling practices, while preserving known or likely time trends or variations in the evaluated variables.

The compiled and adjusted data product is believed to have a high level of accuracy, with consistent measurements:

Salinity: Better than 0.005
Oxygen: 1%
Nitrate: 2%
Silicate: 2%
Phosphate: 2%
Dissolved Inorganic Carbon: 4 μmolkg⁻¹
Total Alkalinity: 4 μmolkg⁻¹
pH: 0.01–0.02 (varies by region)
Halogenated Transient Tracers: 5%
Other variables in the compilation, such as isotopic tracers and discrete CO2 fugacity (fCO2), have not undergone bias comparison or adjustments.

#### Variable key

| Variable / Parameter                               | Abbreviation | Unit           | Observation Type          | Sampling Instrument    | Quality Flag Convention                   | Researcher Name    |
|---------------------------------------------------|-------------|----------------|--------------------------|------------------------|------------------------------------------|--------------------|
| Temperature                                        | temperature | °C             | measured, data synthesis  | CDT, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| Potential temperature                              | theta       | °C             | calculated               |                        |                                          | GLODAP Group       |
| Salinity                                           | salinity    |               | measured, data synthesis  | CDT, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| Potential density                                  | sigma0      | kg m−3         | calculated               |                        |                                          | GLODAP Group       |
| Potential density, ref 1000 dbar                   | sigma1      | kg m−3         | calculated               |                        |                                          | GLODAP Group       |
| Potential density, ref 2000 dbar                   | sigma2      | kg m−3         | calculated               |                        |                                          | GLODAP Group       |
| Potential density, ref 3000 dbar                   | sigma3      | kg m−3         | calculated               |                        |                                          | GLODAP Group       |
| Potential density, ref 4000 dbar                   | sigma4      | kg m−3         | calculated               |                        |                                          | GLODAP Group       |
| Neutral density                                    | gamma       | kg m−3         | calculated               |                        |                                          | GLODAP Group       |
| Oxygen                                             | oxygen      | μmol kg−1      | measured, data synthesis  | CTD, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| Apparent oxygen utilization                        | aou         | μmol kg−1      | calculated               |                        |                                          | GLODAP Group       |
| Nitrate                                            | nitrate     | μmol kg−1      | measured, data synthesis  | CTD, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| Nitrite                                            | nitrite     | μmol kg−1      | measured, data synthesis  | CTD, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| Silicate                                           | silicate    | μmol kg−1      | measured, data synthesis  | CDT, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| Phosphate                                          | phosphate   | μmol kg−1      | measured, data synthesis  | CDT, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| TCO2                                               | tco2        | μmol kg−1      | measured, calculated, data synthesis  | CTD, Niskin Bottles   | Simplified WOCE quality control flags are used | GLODAP Group       |
| TAlk                                               | talk        | μmol kg−1      | measured, calculated, data synthesis  | CTD, Niskin Bottles   | Simplified WOCE quality control flags are used | GLODAP Group       |
| fCO2                                               | fco2        | microatmospheres | measured, calculated, data synthesis  | CTD, Niskin Bottles   | Simplified WOCE quality control flags are used | GLODAP Group       |
| pH at total scale, 25 °C and zero dbar of pressure | phts25p0    |               | measured, calculated, data synthesis  | CTD, Niskin Bottles   | Simplified WOCE quality control flags are used | GLODAP Group       |
| pH at total scale, in situ temperature and pressure | phtsinsitutp |               | measured, calculated, data synthesis  | CTD, Niskin Bottles   | Simplified WOCE quality control flags are used | GLODAP Group       |
| CFC-11                                            | cfc11       | pmol kg−1      | measured, data synthesis  | CTD, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| pCFC-11                                           | pcfc11      | ppt            | measured, data synthesis  | CTD, Niskin Bottles   |                                          | GLODAP Group       |
| CFC-12                                            | cfc12       | pmol kg−1      | measured, data synthesis  | CTD, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| pCFC-12                                           | pcfc12      | ppt            | measured, data synthesis  | CTD, Niskin Bottles   |                                          | GLODAP Group       |
| CFC-113                                           | cfc113      | pmol kg−1      | measured, data synthesis  | CTD, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| CCl4                                              | ccl4        | pmol kg−1      | measured, data synthesis  | CTD, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| pCCl4                                             | pccl4       | ppt            | calculated               |                        |                                          | GLODAP Group       |
| SF6                                               | sf6         | fmol kg−1      | measured, data synthesis  | CTD, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| pSF6                                              | psf6        | ppt            | calculated               |                        |                                          | GLODAP Group       |
| δ13C                                              | c13         | %              | measured, data synthesis  | CTD, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| ∆14C                                              | c14         | %              | measured, data synthesis  | CTD, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| ∆14C counting error                               | c14err      | %              | calculated               |                        |                                          | GLODAP Group       |
| 3H                                                | h3          | TU             | measured, data synthesis  | CTD, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| 3H counting error                                 | h3err       | TU             | calculated               |                        |                                          | GLODAP Group       |
| δ3He                                              | δ3He       | %

              | measured, data synthesis  | CTD, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| 3He counting error                                | he3err      | %              | calculated               |                        |                                          | GLODAP Group       |
| He                                                | He          | nmol kg−1      | measured, data synthesis  | CTD, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| He counting error                                  | heerr       | %              | calculated               |                        |                                          | GLODAP Group       |
| Neon                                              | neon        | nmol kg−1      | measured, data synthesis  | CTD, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| Neon counting error                                | neonerr     | nmol kg−1      | calculated               |                        |                                          | GLODAP Group       |
| δ18O                                              | o18         | %              | measured, data synthesis  | CTD, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| Total organic carbon                              | toc         | μmol L-1       | measured, data synthesis  | CTD, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| Dissolved organic carbon                           | doc         | μmol L-1       | measured, data synthesis  | CTD, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| Dissolved organic nitrogen                         | don         | μmol L-1       | measured, data synthesis  | CTD, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| Total dissolved nitrogen                           | tdn         | μmol L-1       | measured, data synthesis  | CTD, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |
| Chlorophyll a                                     | chla        | ug L-1         | measured, data synthesis  | CTD, Niskin Bottles   | WOCE quality control flags are used        | GLODAP Group       |

#### Citation

Whenever GLODAPv2 is used, the following citations must be included:

* For data and data product: Olsen et al., 2016 and Key et al., 2015
* For mapped product: Lauvset et al., 2016 and Key et al., 2015

```
Olsen, A., R. M. Key, S. van Heuven, S. K. Lauvset, A. Velo, X. Lin, C. Schirnick, A. Kozyr, T. Tanhua, M. Hoppema, S. Jutterström, R. Steinfeldt,
E. Jeansson, M. Ishii, F. F. Pérez and T. Suzuki. The Global Ocean Data Analysis Project version 2 (GLODAPv2) – an internally consistent data
product for the world ocean, Earth Syst. Sci. Data, 8, 297–323, 2016, doi:10.5194/essd-8-297-2016

Lauvset, S. K, R. M. Key, A. Olsen, S. van Heuven, A. Velo, X. Lin, C. Schirnick, A. Kozyr, T. Tanhua, M. Hoppema, S. Jutterström, R. Steinfeldt, E.
Jeansson, M. Ishii, F. F. Pérez, T. Suzuki and S. Watelet. A new global interior ocean mapped climatology: the 1°x1° GLODAP version 2, Earth Syst.
Sci. Data, 8, 325–340, 2016, doi:10.5194/essd-8-325-2016

Key, R.M., A. Olsen, S. van Heuven, S. K. Lauvset, A. Velo, X. Lin, C. Schirnick, A. Kozyr, T. Tanhua, M. Hoppema, S. Jutterström, R. Steinfeldt, E.
Jeansson, M. Ishii, F. F. Perez, and T. Suzuki. 2015. Global Ocean Data Analysis Project, Version 2 (GLODAPv2), ORNL/CDIAC-162, NDP-093. Carbon
Dioxide Information Analysis Center, Oak Ridge National Laboratory, US Department of Energy, Oak Ridge, Tennessee. doi:10.3334/CDIAC/OTG.
NDP093_GLODAPv2
```

#### Dataset preprocessing
The matlab derived products add a G2 infront of all column names and they are left in place as is,with an additional column called system:time_start and datetime added to reflect epoch time and UTC datetime derived from the existing columns. Adding the system:time_start and datetime allow for easily filtering across the earth engine collection. While the merged collection is provided individual feature collections are still maintained to provide the user with the flexibility of loading a smaller subset of features for operations.

![glodap](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/50f618ad-af4a-4866-b262-eca50d5f463e)

#### Earth Engine Snippet

```js
var merged = ee.FeatureCollection("projects/sat-io/open-datasets/GLODAP_V2/GLODAPv2_2023_Merged_Master_File_formatted");
var arctic_ocean = ee.FeatureCollection("projects/sat-io/open-datasets/GLODAP_V2/GLODAPv2_2023_Arctic_Ocean_formatted");
var atlantic_ocean = ee.FeatureCollection("projects/sat-io/open-datasets/GLODAP_V2/GLODAPv2_2023_Atlantic_Ocean_formatted");
var indian_ocean = ee.FeatureCollection("projects/sat-io/open-datasets/GLODAP_V2/GLODAPv2_2023_Indian_Ocean_formatted");
var pacific_ocean = ee.FeatureCollection("projects/sat-io/open-datasets/GLODAP_V2/GLODAPv2_2023_Pacific_Ocean_formatted");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:oceans-shorelines/GLODAP-V2_2023_MERGED

#### License

The dataset is distributed under a public licese. Distribution liability: NOAA and NCEI make no warranty, expressed or implied, regarding these data, nor does the fact of distribution constitute such a warranty. NOAA and NCEI cannot assume liability for any damages caused by any errors or omissions in these data. If appropriate, NCEI can only certify that the data it distributes are an authentic copy of the records that were accepted for inclusion in the NCEI archives.

Provided by: NCEI, NOAA, Olsen et al

Curated in GEE by: Samapriya Roy

Last updated in GEE: 2023-10-25
