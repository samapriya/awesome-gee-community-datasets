# Global Database of Iron and Steel Production Assets

The Global Database of Iron and Steel Production Assets provides information on global iron and steel production plants that are operational today. The database contains 1,598 production plants with exact geolocation and provides information about ownership, production type, plant type, capacity and production start year where available.

Primary steel production processes (blast furnace, basic oxygen furnace or open-hearth furnaces), typically use coal as an energy source and take place in large integrated facilities. Whereas secondary steel production processes (electric arc furnaces) typically use electricity as an energy source and take place in so called ‘mini-mills’. The database captures a wide range of assets across the steel production process, including the procurement and processing of raw materials (in particular coking and pelletisation plants), the production of crude steel (integrated plants and mini-mills) and the production of finished steel products (downstream plants).

#### Citation

```
McCarten, M., Bayaraa, M., Caldecott, B., Christiaen, C., Foster, P., Hickey, C., Kampmann, D.,
Layman, C., Rossi, C., Scott, K., Tang, K., Tkachenko, N., and Yoken, D., 2021.
Global Database of Iron and Steel Production Assets. Spatial Finance Initiative
```

Additional Information about the [Spatial Finance Initiative can be found here](https://spatialfinanceinitiative.com/geoasset-project/)

![iron_steel_database](https://user-images.githubusercontent.com/6677629/126023801-04a02bf0-95ac-44a6-a068-5761a9644945.gif)


|SNo|Field                  |Field_Description                                                                                                                                                                  |GEE_Field      |
|---|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
|1  |uid                    |Unique identifier for the plant                                                                                                                                                    |uid            |
|2  |city                   |City in which the plant is located                                                                                                                                                 |city           |
|3  |state                  |State or province in which the plant is located                                                                                                                                    |state          |
|4  |country                |Country in which the plant is located                                                                                                                                              |country        |
|5  |iso3                   |Three-letter country code defined in ISO 3166-1 alpha 3                                                                                                                            |iso3           |
|6  |country_code           |Three-digit country code defined in ISO 3166-1 numeric                                                                                                                             |country_code   |
|7  |region                 |Region in which the plant is located                                                                                                                                               |region         |
|8  |sub_region             |Subregion in which the plant is located                                                                                                                                            |sub_region     |
|9  |latitude               |Latitude for the geolocation of the plant (based on WGS84 (EPSG:4326))                                                                                                             |latitude       |
|10 |longitude              |Longitude for the geolocation of the plant (based on WGS84 (EPSG:4326))                                                                                                            |longitude      |
|11 |accuracy               |The accuracy of the latitude and longitude                                                                                                                                         |accuracy       |
|12 |status                 |Current plant operating status                                                                                                                                                     |status         |
|13 |plant_type             |The type of iron and steel production facility. Plant types include: Integrated, Mini-Mill, DRI, Downstream, Coke, and Pelletisation plants.                                       |plant_type     |
|14 |primary_production_type|The primary production type used at the plant                                                                                                                                      |prprod_typ     |
|15 |primary_product        |The primary product that is produced at the plant. Product types include: Crude Steel, Finished Steel, Iron, Coke and Pellets.                                                     |primary_product|
|16 |capacity               |Total steel production capacity (millions of tons) of the primary product                                                                                                          |cap            |
|17 |capacity_source        |Source used to obtain capacity information                                                                                                                                         |cap_sr         |
|18 |year                   |Year the plant started production                                                                                                                                                  |year           |
|19 |owner_permid           |PermID of the primary owner of the plant*                                                                                                                                          |ow_pid         |
|20 |owner_name             |Name of the primary owner of the plant                                                                                                                                             |ow_name        |
|21 |owner_source           |Source reporting the ownership link between the plant and owner                                                                                                                    |ow_sr          |
|22 |parent_permid          |PermID of the ultimate parent of the owner of the plant*                                                                                                                           |pr_pid         |
|23 |parent_name            |Name of the ultimate parent of the owner of the plant                                                                                                                              |pr_name        |
|24 |ownership_stake        |The percentage ownership attributed to the parent company if the plant is a joint venture. If the plant is majority owned by a single parent company then this column will be blank|ow_stake       |
|25 |parent_lei             |Legal Entity Identifier (LEI) of the ultimate parent of the owner of the plant                                                                                                     |pr_lei         |
|26 |parent_holding_status  |The holding status of the ultimate parent (Private or Public)                                                                                                                      |pr_hstat       |
|27 |parent_ticker          |The primary ticker for the ultimate parent, if the company is publicly traded                                                                                                      |pr_tkr         |
|28 |parent_exchange        |The primary exchange for the ultimate parent, if the company is publicly traded                                                                                                    |pr_exc         |
|29 |parent_permid_2        |PermID of the 2nd ultimate parent of the owner of the plant*                                                                                                                       |pr_pid2        |
|30 |parent_name_2          |Name of the 2nd ultimate parent of the owner of the plant                                                                                                                          |pr_name2       |
|31 |ownership_stake_2      |The percentage ownership attributed to the 2nd parent company if the plant is a joint venture                                                                                      |ow_stake2      |
|32 |parent_lei_2           |Legal Entity Identifier (LEI) of the 2nd ultimate parent                                                                                                                           |pr_lei2        |
|33 |parent_holding_status_2|The holding status of the 2nd ultimate parent (Private or Public)                                                                                                                  |pr_hstat2      |
|34 |parent_ticker_2        |The primary ticker for the 2nd ultimate parent, if the company is publicly traded                                                                                                  |pr_tkr2        |
|35 |parent_exchange_2      |The primary exchange for the 2nd ultimate parent, if the company is publicly traded                                                                                                |pr_exc2        |

#### Earth Engine Snippet

```js
var global_steel = ee.FeatureCollection("projects/sat-io/open-datasets/SFI/global_steel_database_20210701")
```

Sample Code: https://code.earthengine.google.com/599f1159ef75427d407f4f464530c46b

#### Acknowledgements

Both databases have been developed by the Oxford Sustainable Finance Programme, Satellite Applications Catapult, and The Alan Turing Institute as part of the Spatial Finance Initiative ‘s GeoAsset Project. Project [FAQ's can be found here](https://spatialfinanceinitiative.com/geoasset-project/faqs/)

#### License
The Global Database of Iron and Steel Production Assets can be used by others and is available under a CC BY 4.0 license

Data download page: [Download Request Form](https://spatialfinanceinitiative.com/geoasset-project/data/)

Curated in GEE by: Samapriya Roy

Keywords: : GeoAsset Project, Oxford Sustainable Finance Programme, Satellite Applications Catapult, Alan Turing Institute, McCarten et al , Iron, Steel , Global database

Last updated: 2021-07-16
