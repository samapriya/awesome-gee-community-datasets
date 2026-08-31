# USDA Crop Sequence Boundaries 2018-2025

The **Crop Sequence Boundaries (CSB)**, developed in collaboration with the USDA's Economic Research Service, provides estimates of field boundaries, crop acreage, and crop rotations across the contiguous United States. This dataset utilizes satellite imagery along with other public data and is open source, enabling users to conduct area and statistical analysis of planted U.S. commodities. It offers valuable insights into farmer cropping decisions and practices.

NASS required a representative field dataset for predicting crop planting based on common rotations like corn-soy, while the Economic Research Service (ERS) employs the CSB to study changes in farm management practices such as tillage and cover cropping over time. The CSB dataset represents non-confidential single crop field boundaries within a specified timeframe. It does not include personal identifying information, ownership boundaries, or tax parcels. The data is sourced from satellite imagery and publicly available information, excluding contributions from producers or agencies like the Farm Service Agency. For access and further information, you can visit the [CSB website](https://www.nass.usda.gov/Research_and_Science/Crop-Sequence-Boundaries/index.php). Explore the [CSB GitHub repository](https://github.com/USDA-REE-NASS/crop-sequence-boundaries) for the codebase, and review the [metadata](https://www.nass.usda.gov/Research_and_Science/Crop-Sequence-Boundaries/metadata_Crop-Sequence-Boundaries-2025.htm) associated with the dataset.

Crop Sequence Boundaries (CSB) represent geospatial algorithm-generated field polygons, originating from the NASS Cropland Data Layer (CDL). These polygonal entities cater to the demands of applications reliant on gridded datasets, necessitating analytical units for streamlined data aggregation. The primary objective of CSBs is to furnish comprehensive coverage spanning the contiguous 48 United States, ensuring precision and replicability across multiple years. These structures are forged by amalgamating historical CDLs within a specified time frame, while also integrating road and rail networks to accurately depict crop sequences within these simulated fields. The most recent eight-year window covers the 2018 to 2025 growing seasons, and the full archive of eight-year windows runs from 2008-2015 onward.

#### Citations

```
Hunt, Kevin A., Jonathon Abernethy, Peter Beeson, Maria Bowman, Steven Wallander, and Ryan Williams. "Crop Sequence Boundaries (CSB): Delineated
Fields Using Remotely Sensed Crop Rotations."

Abernethy, Jonathon, Peter Beeson, Claire Boryan, Kevin Hunt, and Luca Sartore. "Preseason crop type prediction using crop sequence boundaries." Computers and Electronics in Agriculture 208 (2023): 107768.
```

#### Dataset structure and preprocessing
The datasets are made available as feature collections in Earth Engine for each state, where the 1825 in the collection name represents the 2018-2025 growing seasons. The state names are part of the feature collection name. While it may not be necessary it is possible to merge them into a single collection for those who would want to run some analysis on a combined feature collection.

Note that the state collections for this window carry crop history attributes for CDL years 2018 through 2025 (for example `CROP18` through `CROP25`), so scripts written against the 2016-2023 assets need their attribute names updated as well as their paths.

![csb_app_opt](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/ab8c00fa-b701-4c70-bc74-2fc77d2620cf)

#### Earth Engine Snippet: Source

```js
var csbal25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBAL1825");
var csbar25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBAR1825");
var csbaz25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBAZ1825");
var csbca25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBCA1825");
var csbco25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBCO1825");
var csbct25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBCT1825");
var csbde25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBDE1825");
var csbga25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBGA1825");
var csbfl25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBFL1825");
var csbia25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBIA1825");
var csbid25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBID1825");
var csbil25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBIL1825");
var csbin25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBIN1825");
var csbks25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBKS1825");
var csbky25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBKY1825");
var csbla25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBLA1825");
var csbma25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBMA1825");
var csbmd25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBMD1825");
var csbme25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBME1825");
var csbmi25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBMI1825");
var csbmn25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBMN1825");
var csbmo25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBMO1825");
var csbms25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBMS1825");
var csbmt25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBMT1825");
var csbne25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBNE1825");
var csbnh25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBNH1825");
var csbnj25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBNJ1825");
var csbnm25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBNM1825");
var csbnv25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBNV1825");
var csbny25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBNY1825");
var csbnc25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBNC1825");
var csbnd25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBND1825");
var csboh25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBOH1825");
var csbok25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBOK1825");
var csbor25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBOR1825");
var csbpa25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBPA1825");
var csbri25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBRI1825");
var csbsc25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBSC1825");
var csbsd25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBSD1825");
var csbtn25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBTN1825");
var csbtx25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBTX1825");
var csbut25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBUT1825");
var csbvt25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBVT1825");
var csbva25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBVA1825");
var csbwa25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBWA1825");
var csbwv25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBWV1825");
var csbwi25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBWI1825");
var csbwy25 = ee.FeatureCollection("projects/nass-csb/assets/CSB1825_rev23/CSBWY1825");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/USDA-CSB-APP

App code: [You can find the app here](https://www.nass.usda.gov/Research_and_Science/Crop-Sequence-Boundaries/Viewer/index.php)

#### License and Liability
The USDA NASS Crop Sequence Boundaries and the data offered at https://www.nass.usda.gov/Research_and_Science/Crop-Sequence-Boundaries are provided to the public as is and are considered public domain and free to redistribute. Users of the Crop Sequence Boundaries (CSB) are solely responsible for interpretations made from these products. The CSB are provided 'as is' and the USDA NASS does not warrant results you may obtain using the data. Contact our staff at (SM.NASS.RDD.GIB@usda.gov) if technical questions arise.

Created by: USDA NASS, USDA ERS

Curated in GEE by : USDA NASS, USDA ERS, Samapriya Roy

keywords: agricultural lands, USDA, crop layer, CDL, crop sequence boundary

Last updated in GEE: 2026-03-27

#### Changelog notes from Source

* The 2018-2025 CSB was released March 27, 2026, and is the window shown in the NASS interactive map. The current algorithm version is v2024.
* The 2017-2024 CSB was released in 2025, extending the archive by one eight-year window.
* The 2016-2023 CSB was released April 5, 2024. Concurrent with that release, all historic CSB data was re-released to reflect updates in methodology; that version is revision 2.3 (rev23), and the rev23 label still applies to the downloadable national archives.
* The current archive of these datasets spans 8-year time frames for all years from 2008 to current (2008-2015 through 2018-2025). Custom time frames can be created using the [Github code](https://github.com/USDA-REE-NASS/crop-sequence-boundaries).

#### Changelog for this page

* **2026-08-30** — Updated to the 2018-2025 window: state Earth Engine assets repointed to `projects/nass-csb/assets/CSB1825_rev23/CSBXX1825`, metadata link updated to the 2025 metadata page, release date added, and the retired 2016-2023 (`csb1623`) asset list and combined `CSB_1623` collection removed since those assets no longer resolve.
* **2024-05-25** — Original page documenting the 2016-2023 (`csb1623`) state assets and the combined `CSB_1623` collection.
