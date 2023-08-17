# USDA Crop Sequence Boundaries 2015-2022

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
var csbal22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBAL1522");
var csbar22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBAR1522");
var csbaz22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBAZ1522");
var csbca22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBCA1522");
var csbco22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBCO1522");
var csbct22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBCT1522");
var csbde22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBDE1522");
var csbga22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBGA1522");
var csbfl22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBFL1522");
var csbia22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBIA1522");
var csbid22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBID1522");
var csbil22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBIL1522");
var csbin22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBIN1522");
var csbks22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBKS1522");
var csbky22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBKY1522");
var csbla22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBLA1522");
var csbma22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBMA1522");
var csbmd22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBMD1522");
var csbme22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBME1522");
var csbmi22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBMI1522");
var csbmn22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBMN1522");
var csbmo22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBMO1522");
var csbms22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBMS1522");
var csbmt22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBMT1522");
var csbne22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBNE1522");
var csbnh22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBNH1522");
var csbnj22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBNJ1522");
var csbnm22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBNM1522");
var csbnv22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBNV1522");
var csbny22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBNY1522");
var csbnc22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBNC1522");
var csbnd22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBND1522");
var csboh22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBOH1522");
var csbok22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBOK1522");
var csbor22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBOR1522");
var csbpa22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBPA1522");
var csbri22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBRI1522");
var csbsc22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBSC1522");
var csbsd22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBSD1522");
var csbtn22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBTN1522");
var csbtx22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBTX1522");
var csbut22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBUT1522");
var csbvt22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBVT1522");
var csbva22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBVA1522");
var csbwa22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBWA1522");
var csbwv22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBWV1522");
var csbwi22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBWI1522");
var csbwy22 = ee.FeatureCollection("projects/nass-csb/assets/csb1522/CSBWY1522");
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
