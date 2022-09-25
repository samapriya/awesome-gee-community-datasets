# geoBoundaries Global Database of Political Administrative Boundaries

Produced and maintained by the William & Mary [geoLab](http://geolab.wm.edu/) since 2017, the geoBoundaries Global Database of Political Administrative Boundaries Database is an online, open license resource of boundaries (i.e., state, county) for every country in the world. We currently track 199 total entities, including all 195 UN member states, Greenland, Taiwan, Niue, and Kosovo. All boundaries are available to view or download in common file formats, including shapefiles; the only requirement for use is [acknowledgement](https://www.geoboundaries.org/index.html#citation). The most up-to-date information about geoBoundaries can be found at www.geoboundaries.org.

All boundary types have been ingested and are include the following with Admin level varying from 0-4 which have been ingested.

_HPSCU_  - High Precision Single Country Unstandardized. The premier geoBoundaries release, representing the highest precision files available for every country in the world. No standardization is performed on these files, so (for example) two countries may overlap in the case of contested boundaries.

_HPSCGS_  - High Precision Single Country Globally Standardized. A version of geoBoundaries high precision data that has been clipped to the U.S. Department of State boundary file, ensuring no contested boundaries or overlap in the dataset. This globally standardized product may have gaps between countries. If you need a product with no gaps, we recommend our simplified global product.

_SSCU_  - Simplified Single Country Unstandardized. A simplified version of every file available for every country in the world. No standardization is performed on these files, so (for example) two countries may overlap in the case of contested boundaries.

_SSCGS_  - Simplified Single Country Globally Standardized. A version of geoBoundaries simplified data that has been clipped to the U.S. Department of State boundary file, ensuring no contested boundaries or overlap in the dataset. This globally standardized product may have gaps between countries.

_CGAZ_  - Comprehensive Global Administrative Zones. A global composite of the SSCGS ADM0, ADM1 and ADM2, with gaps filled between borders.  Also available at higher levels of simplification.

<center>

|Feature Collection|Admin Levels|
|------------------|------------|
|HPSCU             |ADM0,ADM1,ADM2,ADM3,ADM4|
|HPSCGS            |ADM0,ADM1,ADM2,ADM3,ADM4|
|SSCU              |ADM0,ADM1,ADM2,ADM3,ADM4|
|SSCGS             |ADM0,ADM1,ADM2,ADM3,ADM4|
|CGAZ              |ADM0,ADM1,ADM2|


</center>

#### Citation
You can [read the paper here](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0231866) and cite using citation below

```
Runfola D, Anderson A, Baier H, Crittenden M, Dowker E, Fuhrig S, et al. (2020)
geoBoundaries: A global database of political administrative boundaries. PLoS ONE 15(4):
e0231866. https://doi.org/10.1371/journal.pone.0231866
```

You can also find more information on the [webpage](https://www.geoboundaries.org/) along with the [github project page](https://github.com/wmgeolab/geoBoundaries)

#### Data Preprocessing for GEE
To make the datasets more amenable they were downloaded using the API and all features in a folder were then merged into single collections pertaining to varying boundary type and admin levels. There might be some missing pieces owing to issues with downloads and or upload to GEE but care has been taken to minimize those efforts.

![level2_comparison](https://user-images.githubusercontent.com/6677629/125176833-6cb6d000-e19c-11eb-8b25-dcc87a9b1469.gif)

#### Earth Engine Datasets

```js
var CGAZ_ADM0 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/CGAZ_ADM0');
var CGAZ_ADM1 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/CGAZ_ADM1');
var CGAZ_ADM2 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/CGAZ_ADM2');
var HPSCGS_ADM0 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/HPSCGS-ADM0');
var HPSCGS_ADM1 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/HPSCGS-ADM1');
var HPSCGS_ADM2 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/HPSCGS-ADM2');
var HPSCGS_ADM3 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/HPSCGS-ADM3');
var HPSCGS_ADM4 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/HPSCGS-ADM4');
var HPSCU_ADM0 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/HPSCU-ADM0');
var HPSCU_ADM1 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/HPSCU-ADM1');
var HPSCU_ADM2 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/HPSCU-ADM2');
var HPSCU_ADM3 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/HPSCU-ADM3');
var HPSCU_ADM4 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/HPSCU-ADM4');
var SSCGS_ADM0 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/SSCGS-ADM0');
var SSCGS_ADM1 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/SSCGS-ADM1');
var SSCGS_ADM2 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/SSCGS-ADM2');
var SSCGS_ADM3 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/SSCGS-ADM3');
var SSCGS_ADM4 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/SSCGS-ADM4');
var SSCU_ADM0 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/SSCU-ADM0');
var SSCU_ADM1 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/SSCU-ADM1');
var SSCU_ADM2 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/SSCU-ADM2');
var SSCU_ADM3 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/SSCU-ADM3');
var SSCU_ADM4 = ee.FeatureCollection('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/geoboundaries/SSCU-ADM4');
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/GEOBOUNDARIES


#### License

Individual data files in the geoBoundaries database are governed by the license or licenses identified within the metadata for each respective boundary and are all variants of partially or completely open licenses.  All [referenced licenses can be read in their entirety here](https://github.com/wmgeolab/geoBoundaryBot/tree/main/dta/licenseText). Computer code and derivative works generated by the geoBoundaries project are released under the Attribution 4.0 International (CC BY 4.0) license.


Produced and maintained by the [William & Mary geoLab](http://geolab.wm.edu/) since 2017

Processed secondary/formatted & Curated by: Samapriya Roy

Keywords: : Metadata, Political Geography, Open Data, Built Structures, Physical Mapping

Last updated: 2021-07-10
