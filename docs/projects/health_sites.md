# Global Healthsites Mapping Project

Healthsites.io and the Global Healthsites Mapping Project's mission is to help supply governments, NGOs, and the private sector with accurate and up-to-date health facility information. Health facility registers are the building blocks of a well-functioning health information system within a country. Accurate and up-to-date data provides the basic data that helps drive activities like service availability planning, monitoring and evaluation, and disaster risk preparedness.

The data is shared on both https://healthsites.io and expected a monthly updated on the [Humanitarian Data Exchange](https://data.humdata.org/organization/healthsites). Expected update Frequency for now is every month. Read the Healthsites concept note http://bit.ly/2ocL2KY

The healthsites.io datasets are served as nodes (defining points in space) and ways (defining linear features and area boundaries) based on open street map object relations.

![ghmp](https://user-images.githubusercontent.com/6677629/116788727-e3cf3a00-aa70-11eb-80f5-4430f8f28943.gif)

#### Earth Engine Snippet

```js
var node = ee.FeatureCollection("projects/sat-io/open-datasets/health-site-node");
var way = ee.FeatureCollection("projects/sat-io/open-datasets/health-site-way");
```

Sample code: https://code.earthengine.google.com/300ff48b6bc77713b051d33b3fae55b9


#### License

Open Database License (ODbL)

You are free to

* To Share: To copy, distribute and use the database.
* To Create: To produce works from the database.
* To Adapt: To modify, transform and build upon the database.

Conditions

* Attribute: You must attribute any public use of the database, or works produced from the database, in the manner specified in the ODbL. For any use or redistribution of the database, or works produced from it, you must make clear to others the license of the database and keep intact any notices on the original database.
* Share-Alike: If you publicly use any adapted version of this database, or works produced from an adapted database, you must also offer that adapted database under the ODbL.
* Keep open: If you redistribute the database, or an adapted version of it, then you may use technological measures that restrict the work (such as digital rights management) as long as you also redistribute a version without such measures.

Compiled by : Global Healthsites Mapping Project

Curated by: Samapriya Roy

Keywords: :"Global Healthsites Mapping Project, Healthsites, Health, GLC"

Last updated: 2022-08-27
