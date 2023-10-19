# Streamflow reconstruction for Indian sub-continental river basins 1951–2021

The Hydrological Model-Simulated Monthly Streamflow Dataset for Indian-Subcontinental (ISC) River Basins, spanning from 1951 to 2021, addresses a critical need for long-term streamflow observations in the ISC region. Given the essential role of streamflow data in water resources management, hydroclimatic analysis, and ecological assessments, this dataset provides a valuable resource for a wide range of applications. The dataset is constructed through a multi-faceted approach that combines meteorological data, sophisticated hydrological modeling, and a high-resolution vector-based routing model known as mizuRoute. By synthesizing these elements, the dataset yields monthly streamflow simulations for 9579 stream reaches within the ISC river basins.

Validation of the dataset against observed flows at gauge stations demonstrates its reliability, with a significant proportion of the gauge stations showing strong agreement, as evidenced by coefficient of determination (R²) and Nash-Sutcliffe efficiency (NSE) values exceeding 0.70. Such validation empowers the analysis of variability in low, average, and high flow within the stream networks. The dataset's significance extends to identifying long-term changes in streamflow patterns. Notably, it highlights a substantial decline in flow within the Ganga basin and an increase in semi-arid western India and the Indus basin, findings of great relevance for water management planning and climate change adaptation in the Indian subcontinent. Moreover, this resource alleviates the challenge posed by limited streamflow observations, especially in the case of the three major transboundary basins (Ganga, Indus, and Brahmaputra), where conventional monitoring falls short. You can [read the paper here for more details](https://www.nature.com/articles/s41597-023-02618-w)

#### Dataset processing

The datasets are available [for download on Zenodo here](https://zenodo.org/records/8004633) the stream shapefile consists of the streamlines and segment information whereas additional datasets were provided without any file extensions. These were converted to csv files and renamed as needed along with making sure that all NaN values were replaced with 9999 since Earth Engine does not support mixed variable types in a column. These were then joined to the stream shapefile and segment id/seg_id was used to then combine variables to the stream network asset. The following contains the dataset and description


| Variable Name | Description | Data Files and Arrangement |
| --- | --- | --- |
| **Mean_flow** | This folder contains the river segment-wise mean annual and mean monsoon streamflow. The segment ID can be obtained from the India_streams.shp shapefile in this directory. | - **annual_flow**: seg_id, mean_annual_flow (m³/s)<br>- **monsoon_flow**: seg_id, mean_monsoon_flow (m³/s) |
| **high&low_flow** | This folder contains the river segment-wise mean high and mean low streamflow. The segment ID can be obtained from the India_streams.shp shapefile in this directory. | - **high_flow**: seg_id, mean_high_flow (m³/s)<br>- **low_flow**: seg_id, mean_low_flow (m³/s) |
| **Coefficient_of_variability** | This folder contains the river segment-wise coefficient of variability in mean annual and mean monsoon streamflow. The segment ID can be obtained from the India_streams.shp shapefile in this directory. | - **CV_annual_flow**: seg_id, coefficient_of_variability<br>- **CV_monsoon_flow**: seg_id, coefficient_of_variability |
| **Trend_analysis** | This folder contains the list of stream reaches that exhibit a statistically significant trend in streamflow between 1951 and 2021. The segment ID can be obtained from the India_streams.shp shapefile in this directory. | - **streamflow_trend**: seg_id, hypothesis_test (h=1: significant), sen’s_slope |
| **SSI** | This folder contains the standardized streamflow index (SSI) for the top four dry and wet months during the 1951-2021 period. The top four driest and wettest months were calculated based on the Standardized Precipitation Index (SPI) from the monthly average rainfall data for the Indian Subcontinent. The segment ID can be obtained from the India_streams.shp shapefile in this directory. | - **dry_years** (Sub-folder):<br>  - **SSI_**month**_**year****: seg_id, SSI<br>- **wet_years** (Sub-folder):<br>  - **SSI_**month**_**year****: seg_id, SSI |

#### Citation

```
Chuphal, D.S., Mishra, V. Hydrological model-based streamflow reconstruction for Indian sub-continental river basins, 1951–2021. Sci Data 10, 717
(2023). https://doi.org/10.1038/s41597-023-02618-w
```

#### Dataset citation

```
Chuphal, D. S., & Mishra, V. (2023). Reconstructed streamflow for Indian sub-continental river basins, 1951-2021 [Data set].
Zenodo. https://doi.org/10.5281/zenodo.8004633
```

![streamflow_india](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/d336de90-7d9a-4c9d-ad61-05aab43cc7d4)

#### Earth Engine Snippet

```js
var cv_annual_flow = ee.FeatureCollection("projects/sat-io/open-datasets/indian-streams/CV/cv_annual_flow");
var cv_monsoon_flow = ee.FeatureCollection("projects/sat-io/open-datasets/indian-streams/CV/cv_monsoon_flow");
var high_flow = ee.FeatureCollection("projects/sat-io/open-datasets/indian-streams/HIGH-LOW-FLOW/high_flow");
var low_flow = ee.FeatureCollection("projects/sat-io/open-datasets/indian-streams/HIGH-LOW-FLOW/low_flow");
var mean_annual_flow = ee.FeatureCollection("projects/sat-io/open-datasets/indian-streams/MEAN-FLOW/mean_annual_flow");
var mean_monsoon_flow = ee.FeatureCollection("projects/sat-io/open-datasets/indian-streams/MEAN-FLOW/mean_monsoon_flow");
var ssi_dry_july_1972 = ee.FeatureCollection("projects/sat-io/open-datasets/indian-streams/SSI/ssi_dry_july_1972");
var ssi_dry_july_2002 = ee.FeatureCollection("projects/sat-io/open-datasets/indian-streams/SSI/ssi_dry_july_2002");
var ssi_dry_june_2009 = ee.FeatureCollection("projects/sat-io/open-datasets/indian-streams/SSI/ssi_dry_june_2009");
var ssi_dry_june_2014 = ee.FeatureCollection("projects/sat-io/open-datasets/indian-streams/SSI/ssi_dry_june_2014");
var ssi_wet_august_2020 = ee.FeatureCollection("projects/sat-io/open-datasets/indian-streams/SSI/ssi_wet_august_2020");
var ssi_wet_july_1988 = ee.FeatureCollection("projects/sat-io/open-datasets/indian-streams/SSI/ssi_wet_july_1988");
var ssi_wet_september_1983 = ee.FeatureCollection("projects/sat-io/open-datasets/indian-streams/SSI/ssi_wet_september_1983");
var ssi_wet_september_2019 = ee.FeatureCollection("projects/sat-io/open-datasets/indian-streams/SSI/ssi_wet_september_2019");
var streamflow_trend = ee.FeatureCollection("projects/sat-io/open-datasets/indian-streams/streamflow_trend");
var streams = ee.FeatureCollection("projects/sat-io/open-datasets/indian-streams/streams");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/STREAMFLOW-RECONSTRUCTION-INDIAN-SUBCONTINENT

#### License
These datasets are available under the Creative Commons Attribution 4.0 International license.

Provided by: Chuphal, D. S., & Mishra, V., Indian Institute of Technology (IIT) Gandhinagar

Curated in GEE by: Samapriya Roy

Keywords: H08, mizuRoute, Streamflow,India, Hydrology, Water Management, Climate change adaptation, Hydroclimatic extremes analysis

Last updated in GEE: 2023-10-18
