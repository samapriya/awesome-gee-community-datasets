# Harmonized World Soil Database (HWSD) version 2.0

The Harmonized World Soil Database version 2.0 (HWSD v2.0) is a unique global soil inventory providing information on the morphological, chemical and physical properties of soils at approximately 1 km resolution. Its main objective is to serve as a basis for prospective studies on
agro-ecological zoning, food security and climate change.

This updated version (HWSD v2.0) is built on the previous versions of HWSD with several improvements on (i) the data source that now includes several national soil databases, (ii) an enhanced number of soil attributes available for seven soil depth layers, instead of two in HWSD v1.2, and (iii) a common soil reference for all soil units (FAO1990 and the World Reference Base for Soil Resources). This contributes to a further harmonization of the database.

You can download the files and tutorials [for the datasets here](https://data.isric.org/geonetwork/srv/all/catalog.search#/metadata/54aebf11-ec73-4ff8-bf6c-ecff4b0725ea)

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Dataset preprocessing

A multiband image containing all the attributes of the FAO Harmonized World Soil Database v2.0 Soil Mapping Units (SMUs). The dataset was processed
with special thanks to William Ouellette.

The band order is the following:

- `HWSD2_ID` (numeric)
- `WISE30s_ID` (string converted to numeric in ascending alphanumeric order)
- `COVERAGE` (numeric)
- `SHARE` (numeric) - unit: `%`
- `WRB4` (string converted to numeric in ascending alphanumeric order)
- `WRB_PHASES` (string converted to numeric in ascending alphanumeric order)
- `WRB2_CODE` (numeric) -- WRB2 is skipped, as it is redundant with WRB2_CODE
- `FAO90` (string converted to numeric in ascending alphanumeric order)
- `KOPPEN` (string converted to numeric in ascending alphanumeric order)
- `TEXTURE_USDA` (numeric)
- `REF_BULK_DENSITY` (numeric) - unit: `g/cm³`
- `BULK_DENSITY` (numeric) - unit: `g/cm³`
- `DRAINAGE` (numeric)
- `ROOT_DEPTH` (numeric)
- `AWC` (numeric) - unit: `mm/m`
- `PHASE1` (numeric)
- `PHASE2` (numeric)
- `ROOTS` (numeric)
- `IL` (numeric)
- `ADD_PROP` (numeric)

#### Citation

```
FAO & IIASA. 2023. Harmonized World Soil Database version 2.0. Rome and Laxenburg. https://doi.org/10.4060/cc3823en
```

![hwsd](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/2dfd67f3-f3f3-4c83-a2da-8597af9bfb54)

#### Earth Engine Snippet

```js
var hwsd2 = ee.Image("projects/sat-io/open-datasets/FAO/HWSD_V2_SMU");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:soil-properties/HWSD-V2-SMU

#### License
This dataset is made available under [Attribution-NonCommercial-ShareAlike 3.0 International (CC BY-NC-SA 3.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

Created by: FAO & IIASA

Curated in GEE by: William Ouellette & Samapriya Roy

Keywords: Soil, World Soil properties, Texture, USDA, FAO, IIASA

Last updated in GEE: 23/03/2023
