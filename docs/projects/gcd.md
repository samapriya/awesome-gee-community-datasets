# Global Database of Cement Production Assets

The Global Database of Cement Production Assets provides information on global cement production plants that are operational today. The database contains 3,117 cement plants with exact geolocation and provides information about ownership, production type, plant type, capacity and production start year where available.

The process consists of three steps: the mixing of limestone with other materials; the heating of the limestone mixture to produce clinker and the grinding of clinker with different ingredients to produce cement. The grinding process can happen in integrated facilities where the clinker is also produced or in independent grinding facilities closer to its end market. While the bulk of greenhouse gas emissions associated with cement production stem from clinker production and integrated facilities, the database covers both integrated as well as independent grinding facilities.

#### Citation

```
McCarten, M., Bayaraa, M., Caldecott, B., Christiaen, C., Foster, P., Hickey, C., Kampmann, D.,
Layman, C., Rossi, C., Scott, K., Tang, K., Tkachenko, N., and Yoken, D. 2021.
Global Database of Cement Production Assets. Spatial Finance Initiative
```

Additional Information about the [Spatial Finance Initiative can be found here](https://spatialfinanceinitiative.com/geoasset-project/)

![cement_database](https://user-images.githubusercontent.com/6677629/126024364-5d5e8299-3a48-445c-a480-345f8cb84a8f.gif)


|SNo|Field                  |Field_Description                                                                                                                                                                                              |GEE_Field   |
|---|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
|1  |accuracy               |The accuracy of the latitude and longitude                                                                                                                                                                     |accuracy    |
|2  |capacity               |Total cement production capacity (millions of tons)                                                                                                                                                            |cap         |
|3  |capacity_source        |Source used to obtain or estimate the capacity, either a link to reported capacity information or "Estimated." If "Estimated" then the capacity has been modelled based on annotated kiln and plant dimensions.|cap_sr      |
|4  |city                   |City in which the plant is located                                                                                                                                                                             |city        |
|5  |country                |Country in which the plant is located                                                                                                                                                                          |country     |
|6  |country_code           |Three-digit country code defined in ISO 3166-1 numeric                                                                                                                                                         |country_code|
|7  |iso3                   |Three-letter country code defined in ISO 3166-1 alpha 3                                                                                                                                                        |iso3        |
|8  |owner_name             |Name of the primary owner of the plant                                                                                                                                                                         |ow_name     |
|9  |owner_permid           |PermID of the primary owner of the plant*                                                                                                                                                                      |ow_pid      |
|10 |owner_source           |Source reporting the ownership link between the plant and owner                                                                                                                                                |ow_source   |
|11 |ownership_stake        |The percentage ownership attributed to the parent company if the plant is a joint venture. If the plant is majority owned by a single parent company then this column will be blank                            |ow_stake    |
|12 |ownership_stake_2      |The percentage ownership attributed to the 2nd parent company if the plant is a joint venture                                                                                                                  |ow_stake2   |
|13 |parent_exchange        |The primary exchange for the ultimate parent, if the company is publicly traded                                                                                                                                |pr_exc      |
|14 |parent_exchange_2      |The primary exchange for the 2nd ultimate parent, if the company is publicly traded                                                                                                                            |pr_exc2     |
|15 |parent_holding_status  |The holding status of the ultimate parent (Private or Public)                                                                                                                                                  |pr_hstat    |
|16 |parent_holding_status_2|The holding status of the 2nd ultimate parent (Private or Public)                                                                                                                                              |pr_hstat_2  |
|17 |parent_lei             |Legal Entity Identifier (LEI) of the ultimate parent of the owner of the plant                                                                                                                                 |pr_lei      |
|18 |parent_lei_2           |Legal Entity Identifier (LEI) of the 2nd ultimate parent                                                                                                                                                       |pr_lei2     |
|19 |parent_name            |Name of the ultimate parent of the owner of the plant                                                                                                                                                          |pr_name     |
|20 |parent_name_2          |Name of the 2nd ultimate parent of the owner of the plant                                                                                                                                                      |pr_name2    |
|21 |parent_permid          |PermID of the ultimate parent of the owner of the plant*                                                                                                                                                       |pr_pid      |
|22 |parent_permid_2        |PermID of the 2nd ultimate parent of the owner of the plant*                                                                                                                                                   |pr_pid2     |
|23 |parent_ticker          |The primary ticker for the ultimate parent, if the company is publicly traded                                                                                                                                  |pr_tkr      |
|24 |parent_ticker_2        |The primary ticker for the 2nd ultimate parent, if the company is publicly traded                                                                                                                              |pr_tkr2     |
|25 |plant_type             |The type of cement plant (Integrated or Grinding)                                                                                                                                                              |plant_type  |
|26 |production_type        |The production process used to produce the clinker at Integrated plants (Wet or Dry)                                                                                                                           |prod_type   |
|27 |region                 |Region in which the plant is located                                                                                                                                                                           |region      |
|28 |state                  |State or province in which the plant is located                                                                                                                                                                |state       |
|29 |status                 |Current plant operating status                                                                                                                                                                                 |status      |
|30 |sub_region             |Subregion in which the plant is located                                                                                                                                                                        |sub_region  |
|31 |uid                    |Unique identifier for the cement plant                                                                                                                                                                         |uid         |
|32 |year                   |Year the plant started production                                                                                                                                                                              |year        |

#### Earth Engine Snippet

```js
var global_cement = ee.FeatureCollection("projects/sat-io/open-datasets/SFI/global_cement_database_20210701")
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/GLOBAL-CEMENT-PRODUCTION-ASSETS

#### Acknowledgements

Both databases have been developed by the Oxford Sustainable Finance Programme, Satellite Applications Catapult, and The Alan Turing Institute as part of the Spatial Finance Initiative ‘s GeoAsset Project. Project [FAQ's can be found here](https://spatialfinanceinitiative.com/geoasset-project/faqs/)

#### License
The Global Database of Cement Production Assets can be used by others and is available under a CC BY 4.0 license

Data download page: [Download Request Form](https://www.cgfi.ac.uk/spatial-finance-initiative/geoasset-project/geoasset-databases/)

Curated in GEE by: Samapriya Roy

Keywords: : GeoAsset Project, Oxford Sustainable Finance Programme, Satellite Applications Catapult, Alan Turing Institute, McCarten et al , cement , Global database

Last updated: 2021-07-16
