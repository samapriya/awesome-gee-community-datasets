# USDA Crop Sequence Boundaries 2016-2023

The **Crop Sequence Boundaries (CSB)**, developed in collaboration with the USDA's Economic Research Service, provides estimates of field boundaries, crop acreage, and crop rotations across the contiguous United States. This dataset utilizes satellite imagery along with other public data and is open source, enabling users to conduct area and statistical analysis of planted U.S. commodities. It offers valuable insights into farmer cropping decisions and practices.

NASS required a representative field dataset for predicting crop planting based on common rotations like corn-soy, while the Economic Research Service (ERS) employs the CSB to study changes in farm management practices such as tillage and cover cropping over time. The CSB dataset represents non-confidential single crop field boundaries within a specified timeframe. It does not include personal identifying information, ownership boundaries, or tax parcels. The data is sourced from satellite imagery and publicly available information, excluding contributions from producers or agencies like the Farm Service Agency. For access and further information, you can visit the [CSB website](https://www.nass.usda.gov/Research_and_Science/Crop-Sequence-Boundaries/index.php).Explore the [CSB GitHub repository](https://github.com/USDA-REE-NASS/crop-sequence-boundaries/tree/main/csb-project) for the codebase, and review the [metadata](https://www.nass.usda.gov/Research_and_Science/Crop-Sequence-Boundaries/metadata_Crop-Sequence-Boundaries-2022.htm) associated with the dataset.

Crop Sequence Boundaries (CSB) represent geospatial algorithm-generated field polygons, originating from the NASS Cropland Data Layer (CDL). These polygonal entities cater to the demands of applications reliant on gridded datasets, necessitating analytical units for streamlined data aggregation. The primary objective of CSBs is to furnish comprehensive coverage spanning the contiguous 48 United States, ensuring precision and replicability across multiple years. These structures are forged by amalgamating historical CDLs within a specified time frame, while also integrating road and rail networks to accurately depict crop sequences within these simulated fields. The dataset is available for 2015 to 2022 growing seasons.

#### Citations

```
Hunt, Kevin A., Jonathon Abernethy, Peter Beeson, Maria Bowman, Steven Wallander, and Ryan Williams. "Crop Sequence Boundaries (CSB): Delineated
Fields Using Remotely Sensed Crop Rotations."

Abernethy, Jonathon, Peter Beeson, Claire Boryan, Kevin Hunt, and Luca Sartore. "Preseason crop type prediction using crop sequence boundaries." Computers and Electronics in Agriculture 208 (2023): 107768.
```

#### Dataset strucutre and preprocessing
The datasets are made available as feature collections in Earth Engine for each state the 1522 reprents the year 2015-2022 growing season. The state names are part of the feature collection name. While it may not be necessary it is possible to merge them into a single collection and I created that for those would want to run some analysis on a combined feature collection.

![csb_app_opt](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/ab8c00fa-b701-4c70-bc74-2fc77d2620cf)

#### Earth Engine Snippet: Source

```js
var csbal23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBAL1623");
var csbar23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBAR1623");
var csbaz23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBAZ1623");
var csbca23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBCA1623");
var csbco23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBCO1623");
var csbct23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBCT1623");
var csbde23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBDE1623");
var csbga23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBGA1623");
var csbfl23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBFL1623");
var csbia23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBIA1623");
var csbid23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBID1623");
var csbil23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBIL1623");
var csbin23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBIN1623");
var csbks23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBKS1623");
var csbky23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBKY1623");
var csbla23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBLA1623");
var csbma23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBMA1623");
var csbmd23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBMD1623");
var csbme23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBME1623");
var csbmi23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBMI1623");
var csbmn23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBMN1623");
var csbmo23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBMO1623");
var csbms23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBMS1623");
var csbmt23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBMT1623");
var csbne23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBNE1623");
var csbnh23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBNH1623");
var csbnj23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBNJ1623");
var csbnm23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBNM1623");
var csbnv23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBNV1623");
var csbny23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBNY1623");
var csbnc23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBNC1623");
var csbnd23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBND1623");
var csboh23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBOH1623");
var csbok23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBOK1623");
var csbor23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBOR1623");
var csbpa23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBPA1623");
var csbri23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBRI1623");
var csbsc23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBSC1623");
var csbsd23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBSD1623");
var csbtn23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBTN1623");
var csbtx23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBTX1623");
var csbut23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBUT1623");
var csbvt23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBVT1623");
var csbva23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBVA1623");
var csbwa23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBWA1623");
var csbwv23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBWV1623");
var csbwi23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBWI1623");
var csbwy23 = ee.FeatureCollection("projects/nass-csb/assets/csb1623/CSBWY1623");
```

#### Earth Engine Snippet Combined

```js
var combined_csb= ee.FeatureCollection('projects/sat-io/open-datasets/USDA/CSB_1522');
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/USDA-CSB-APP

App code: [You can find the app here](https://www.nass.usda.gov/Research_and_Science/Crop-Sequence-Boundaries/Viewer/index.php)

#### License and Liability
The USDA NASS Crop Sequence Boundaries and the data offered at https://www.nass.usda.gov/Research_and_Science/Crop-Sequence-Boundaries are provided to the public as is and are considered public domain and free to redistribute. Users of the Crop Sequence Boundaries (CSB) are solely responsible for interpretations made from these products. The CSB are provided 'as is' and the USDA NASS does not warrant results you may obtain using the data. Contact our staff at (SM.NASS.RDD.GIB@usda.gov) if technical questions arise.

Created by: USDA NASS, USDA ERS

Curated in GEE by : USDA NASS, USDA ERS, Samapriya Roy

keywords: agricultural lands, USDA, crop layer, CDL, crop sequence boundary

Last updated in GEE: 2024-05-25

#### Changelog notes from Source

* The 2016-2023 CSB was released April 5, 2024.
* Concurrent with the 2023 release, all historic CSB data was re-released to reflect updates in methodology. The new version is revision 2.3 (rev23).
* The current archive of these datasets span 8-year time frames for all years from 2008 to current. Custom time frames can be created using the [Github code](https://github.com/USDA-REE-NASS/crop-sequence-boundaries/tree/main/csb-project).
