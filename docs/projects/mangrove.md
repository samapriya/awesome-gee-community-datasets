# Global Mangrove Watch

From the Global Mangrove Dataset (1996 - 2016) website:

**The GMW has generated a global baseline map of mangroves for 2010 using ALOS PALSAR and Landsat (optical) data, and changes from this baseline for six epochs between 1996 and 2016 derived from JERS-1 SAR, ALOS PALSAR and ALOS-2 PALSAR-2. Annual maps are planned from 2018 and onwards.**

Updated dataset: https://www.globalmangrovewatch.org/datasets/

#### Citation:

```
Bunting P., Rosenqvist A., Lucas R., Rebelo L-M., Hilarides L., Thomas N., Hardy A., Itoh T., Shimada M. and Finlayson C.M. (2018). The Global Mangrove Watch – a New 2010 Global Baseline of Mangrove Extent. Remote Sensing 10(10): 1669. doi: 10.3390/rs1010669.


Thomas N, Lucas R, Bunting P, Hardy A, Rosenqvist A, Simard M. (2017). Distribution and drivers of global mangrove forest change, 1996-2010. PLOS ONE 12: e0179302. doi: 10.1371/journal.pone.0179302
```

![mangrove](https://user-images.githubusercontent.com/6677629/83225702-598aa180-a14e-11ea-9dce-65c46278531f.gif)

#### Earth Engine Snippet

```js
var gmw2007 = ee.FeatureCollection("projects/sat-io/open-datasets/GMW/GMW_2007_v2");
var gmw2008 = ee.FeatureCollection("projects/sat-io/open-datasets/GMW/GMW_2008_v2");
var gmw2009 = ee.FeatureCollection("projects/sat-io/open-datasets/GMW/GMW_2009_v2");
var gmw2010 = ee.FeatureCollection("projects/sat-io/open-datasets/GMW/GMW_2010_v2");
var gmw2015 = ee.FeatureCollection("projects/sat-io/open-datasets/GMW/GMW_2015_v2");
var gmw2016 = ee.FeatureCollection("projects/sat-io/open-datasets/GMW/GMW_2016_v2");
var gmw1996 = ee.FeatureCollection("projects/sat-io/open-datasets/GMW/GMW_1996_v2");
```

Sample Code: https://code.earthengine.google.com/ded574858c353cac4df6652e14f501b2

Resolution:
0.8 degee approx 30m

#### License & Usage
Attribution 4.0 International (CC BY 4.0)
https://creativecommons.org/licenses/by/4.0/.

You are free to:
Share — copy and redistribute the material in any medium or format
Adapt — remix, transform, and build upon the material for any purpose, even commercially.

Under the following terms:
Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

Website:  https://data.unep-wcmc.org/datasets/45

Curated by: Samapriya Roy

Keywords: Global, Mangrove, GMW

Last updated: 2019-06-14

## Global Mangrove Watch 2010 Baseline (v2.5)

This study presents an updated global mangrove forest baseline for 2010: Global Mangrove Watch (GMW) v2.5. The previous GMW maps (v2.0) of the mangrove extent are currently considered the most comprehensive available global products, however areas were identified as missing or poorly mapped. Therefore, this study has updated the 2010 baseline map to increase the mapping quality and completeness of the mangrove extent. This revision resulted in an additional 2660 km2 of mangroves being mapped yielding a revised global mangrove extent for 2010 of some 140,260 km2. The overall map accuracy was estimated to be 95.1% with a 95th confidence interval of 93.8–96.5%, as assessed using 50,750 reference points located across 60 globally distributed sites. Of these 60 validation sites, 26 were located in areas that were remapped to produce the v2.5 map and the overall accuracy for these was found to have increased from 82.6% (95th confidence interval: 80.1–84.9) for the v2.0 map to 95.0% (95th confidence interval: 93.7–96.4) for the v2.5 map. Overall, the improved GMW v2.5 map provides a more robust product to support the conservation and sustainable use of mangroves globally. Read the full [paper here](https://www.mdpi.com/2072-4292/14/4/1034/htm?s=09)

Disclaimer: Whole or parts of the dataset description was provided by the author(s) or their works.

You can download the [datasets here](https://doi.org/10.5281/zenodo.5828339) and the [github page with code here](https://github.com/globalmangrovewatch/gmw_gap_fill_2020).

#### Citation:

```
Bunting P., Rosenqvist A., Lucas R., Rebelo L-M., Hilarides L., Thomas N., Hardy A., Itoh T., Shimada M. and Finlayson C.M. (2018). The Global Mangrove
Watch – a New 2010 Global Baseline of Mangrove Extent. Remote Sensing 10(10): 1669. doi: 10.3390/rs1010669.
```

![gmw25](https://user-images.githubusercontent.com/6677629/155864712-809e190f-4e58-4bc9-8ae9-66d9d6cd4716.gif)

#### Earth Engine Snippet

```js
var gmw_2010_v25 = ee.ImageCollection("projects/sat-io/open-datasets/GMW/GMW_2010_v25");
```

Sample Code: https://code.earthengine.google.com/713555a5cc2f2d0c8e9f305aeb9625ba

Resolution:
0.8 degee approx 30m

#### License & Usage
Attribution 4.0 International (CC BY 4.0)
https://creativecommons.org/licenses/by/4.0/.

You are free to:
Share — copy and redistribute the material in any medium or format
Adapt — remix, transform, and build upon the material for any purpose, even commercially.

Under the following terms:
Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

Curated by: Samapriya Roy

Keywords: Global, Mangrove, GMW

Last updated: 2022-01-07
