# Mismanaged Plastic Waste Dataset in Rivers

This dataset shows the exposure of global rivers to mismanaged plastic waste (MPW) in 2015 and its projected impact in 2060 based on three scenarios. The different scenarios for 2060 are A: business as usual, B: improved plastic recycling, and C:improved plastic recycling and reduced plastic use projection.

Four global datasets are available that include

1. MPW in 2015 and for three scenarios in 2060,
2. the river type (e.g., meandering or braided)
3. migration of rivers over the past 36-years and
4. the human impact on rivers.

Datasets are described in further detailed in the [paper](https://www.sciencedirect.com/science/article/pii/S0048969723004369) published in Science of the Total Environment, at the Zenodo data [repository](https://zenodo.org/record/6894684) or using the interactive map available [here](https://bjornburrnyberg.users.earthengine.app/view/riverpi).


**Mismanaged Plastic Waste Dataset**

* Band 'MPW2015' = MPW input in 2015
* Band 'MPW2060A' = MPW input in 2060 based on a 'business as usual' projection.
* Band 'MPW2060B' = MPW input in 2060 based on an 'improved plastic recycling' scenario.
* Band 'MPW2060C' = MPW input in 2060 based on an 'improved plastic recycling and reduced plastic demand' scenario.
* Band 'FFPW2015' = Potential plastic accumulation in 2015.
* Band 'FFPW2060A' = Potential plastic accumulation in 2060 based on a 'business as usual' projection.
* Band 'FFPW2060B' = Potential plastic accumulation in 2060 based on an 'improved plastic recycling' scenario.
* Band 'FFPW2060C' = Potential plastic accumulation in 2060 based on an 'improved plastic recycling and reduced plastic demand' scenario.

_Values for MPW datasets_

* 1000 = Very High impact (> 10 t/yr/km2)
* 2000 = High impact (1 to 10 t/yr/km2)
* 3000 = Moderate Impact (0.1 to 1 t/yr/km2)
* 4000 = Low Impact (< 0.1 t/yr/km2)
* 5000 = None

_Values for FFPW datasets_

* 1000 = Very High impact (> 100 t/yr/km2)
* 2000 = High impact (10 to 100 t/yr/km2)
* 3000 = Moderate Impact (1 to 10 t/yr/km2)
* 4000 = Low Impact (< 1 t/yr/km2)
* 5000 = None


**River Type Dataset**

* Code 0 = No Data/Background
* Code 1 = Meandering/Single-threaded River
* Code 2 = Braided/Multi-threaded River
* Code 3 = Lacustrine/Wetland Environment

**River Migration Dataset**

* Code 0 = No Data/Background
* Code 20 =  Actively migrating river over 36-years of satellite observations
* Code 30 = Permanent river waterbody over 36-years of satellite observations

**River Impact Dataset**

* Code 0 - No Data/Background
* Code 100 - Free Flowing River
* Code 200 - Good Connectivity River
* Code 300 - Impacted River

#### Citation

```
Nyberg, Björn, Peter T. Harris, Ian Kane, and Thomas Maes. "Leaving a plastic legacy: Current and future scenarios for mismanaged plastic waste in
rivers." Science of the Total Environment 869 (2023): 161821.
```

#### Dataset citation

```
Nyberg, Bjorn. (2022). Legacy of MPW in Rivers (0.1) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.6894684
```

![mpw](https://user-images.githubusercontent.com/6677629/223344445-652196f1-43e9-456c-bdcc-5e21a434980d.gif)

#### Earth Engine Snippet

```js
var change = ee.Image('projects/sat-io/open-datasets/MPW/changeMap'); //River Change
var ffr = ee.Image('projects/sat-io/open-datasets/MPW/riverImpact'); //Free flowing rivers
var env = ee.Image('projects/sat-io/open-datasets/MPW/Plastics_Env'); //River Types
var mpw = ee.Image('projects/sat-io/open-datasets/MPW/MPW_data'); // Mismanaged plastic waste
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:oceans-shorelines/MISMANAGED-PLASTIC-WASTE

#### License
The dataset is made available under the terms of the [Creative Commons Attribution 4.0 International license](https://creativecommons.org/licenses/by/4.0/legalcode)

Curated by: Björn Nyberg

Keywords: Rivers, Plastic, Mismanaged plastic waste

Last updated: July 24th 2022
