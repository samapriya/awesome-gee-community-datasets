# Wildland-Urban Interface (WUI) CONUS

The Wildland-Urban Interface (WUI) is the area where housing meets or intermingles with undeveloped wildland vegetation, making it a focal area for human-environment conflicts such as wildland fires, habitat fragmentation, invasive species, and biodiversity decline. Using geographic information systems (GIS), U.S. Census housing density data were integrated with USGS National Land Cover Data (NLCD) to map the Federal Register definition of WUI (Federal Register 66:751, 2001) across four time steps — 1990, 2000, 2010, and 2020 — for the conterminous United States.

This 4th edition dataset uses an improved public land adjustment (PLA) housing density process relative to prior editions, correcting topological errors and removing erroneous sliver polygons generated during the PLA process. Data are provided as block-level polygons and include housing and population densities for 1990, 2000, 2010, and 2020; wildland vegetation percentages for 1992, 2001, 2011, and 2019; and WUI classification for 1990, 2000, 2010, and 2020.

WUI data are useful for wildland fire research, policy, and management, as well as for evaluating the effects of housing growth on the environment at national, state, and local levels.

#### Available Datasets

| Dataset Type | Description | Status | Earth Engine Collection |
| --- | --- | --- | --- |
| **WUI Block Polygons** | Block-level housing density, wildland vegetation %, and WUI classification (1990-2020) | Complete | `projects/sat-io/open-datasets/CONUS_WUI` |

#### Dataset Details

??? example "The WUI dataset details can be found here"

      | Characteristic | Description |
      | --- | --- |
      | Name | Wildland-Urban Interface (WUI), 4th Edition |
      | Provider | SILVIS Lab (University of Wisconsin-Madison) and USDA Forest Service, Northern Research Station |
      | Data Type | Vector (polygon) |
      | Coverage | Conterminous United States (lower 48 states and District of Columbia) |
      | Temporal Range | 1990, 2000, 2010, 2020 |
      | Coordinate System | NAD 1983 Albers Equal Area Conic |
      | Data Structure | Census block-derived polygons attributed with housing density, wildland vegetation %, and WUI class per decade |

#### Key Attributes

??? example "The WUI dataset includes the following key attributes"

      | Attribute | Description |
      | --- | --- |
      | BLK20 | Unique Census block identifier (State + County + Tract + Block + Water, from TIGER) |
      | STATE | 2-letter state abbreviation |
      | FIPS | County Federal Information Processing Standards code |
      | POP2020 / HU2020 | 2020 population / total housing units |
      | POPDEN2020 / HUDEN2020 | 2020 population density / housing density (units per km²) |
      | HU1990, HU2000, HU2010 | Allocated total housing units for 1990, 2000, 2010 |
      | HUDEN1990, HUDEN2000, HUDEN2010 | Housing density (units per km²) for 1990, 2000, 2010 |
      | VEG1992PC, VEG2001PC, VEG2011PC, VEG2019PC | Wildland vegetation % (forests + grasslands + wetlands) for each decade |
      | WUIFLAG1990/2000/2010/2020 | WUI flag per decade (1 = intermix, 2 = interface, 0 = non-WUI) |
      | WUICLASS1990/2000/2010/2020 | WUI class per decade (see WUI Classes table below) |
      | PUBFLAG | Flag for protected/public land (1 = public land) |
      | BUFVEG | Flag for polygons within potential interface buffers (2.414 km around ≥75% wildland vegetation areas >500 ha in 2020) |
      | WATER20 / AWATER20PC | Water body flag and % of block area that is water |

#### WUI Classes

??? example "The WUICLASS attributes use the following enumerated classes"

      | Class | Definition |
      | --- | --- |
      | Water | Open water |
      | Uninhabited_Veg | Housing density = 0 and wildland vegetation > 50% |
      | Uninhabited_NoVeg | Housing density = 0 and wildland vegetation ≤ 50% |
      | Very_Low_Dens_Veg | Housing density < 6.18 units/km² and wildland vegetation > 50% |
      | Very_Low_Dens_NoVeg | Housing density < 6.18 units/km² and wildland vegetation ≤ 50% |
      | Low_Dens_Intermix | Housing density 6.18-49.42 units/km² and wildland vegetation > 50% |
      | Low_Dens_Interface | Housing density 6.18-49.42 units/km² and wildland vegetation ≤ 50%, within 2.414 km of ≥75% wildland vegetation area |
      | Low_Dens_NoVeg | Housing density 6.18-49.42 units/km² and wildland vegetation ≤ 50% (not within interface buffer) |
      | Med_Dens_Intermix | Housing density 49.42-741.32 units/km² and wildland vegetation > 50% |
      | Med_Dens_Interface | Housing density 49.42-741.32 units/km² and wildland vegetation ≤ 50%, within 2.414 km of ≥75% wildland vegetation area |
      | Med_Dens_NoVeg | Housing density 49.42-741.32 units/km² and wildland vegetation ≤ 50% (not within interface buffer) |
      | High_Dens_Intermix | Housing density ≥ 741.32 units/km² and wildland vegetation > 50% |
      | High_Dens_Interface | Housing density ≥ 741.32 units/km² and wildland vegetation ≤ 50%, within 2.414 km of ≥75% wildland vegetation area |
      | High_Dens_NoVeg | Housing density ≥ 741.32 units/km² and wildland vegetation ≤ 50% (not within interface buffer) |

      Intermix areas have wildland vegetation intermingled directly with housing; interface areas are non-vegetated but sit adjacent to dense wildland vegetation.

#### Data Access

The complete geodatabase (`CONUS_WUI_block_1990-2020_change_v4.gdb`) and metadata are available at the [Forest Service Research Data Archive](https://doi.org/10.2737/RDS-2015-0012-4). An interactive viewer is also available: [WUI Wildfire GEE App](https://ee-weidignc.projects.earthengine.app/view/wui-wildfire).

#### Citation

```
Radeloff, Volker C.; Helmers, David P.; Mockrin, Miranda H.; Carlson, Amanda R.; Hawbaker, Todd J.; Martinuzzi, Sebastián. 2023. The 1990-2020 wildland-urban interface of the conterminous United States - geospatial data. 4th Edition. Fort Collins, CO: Forest Service Research Data Archive. https://doi.org/10.2737/RDS-2015-0012-4
```

**Related publications:**

* Martinuzzi, S.; Stewart, S.I.; Helmers, D.P.; Mockrin, M.H.; Hammer, R.B.; Radeloff, V.C. 2015. The 2010 wildland-urban interface of the conterminous United States - geospatial data. https://doi.org/10.2737/RDS-2015-0012
* Radeloff, V.C.; Helmers, D.P.; Kramer, H.A.; Mockrin, M.H.; Alexandre, P.M.; Bar Massada, A.; Butsic, V.; Hawbaker, T.J.; Martinuzzi, S.; Syphard, A.D.; Stewart, S.I. 2017. The 1990-2010 wildland-urban interface of the conterminous United States - geospatial data. 2nd Edition. https://doi.org/10.2737/RDS-2015-0012-2
* Radeloff, V.C.; Helmers, D.P.; Mockrin, M.H.; Carlson, A.R.; Hawbaker, T.J.; Martinuzzi, S. 2022. The 1990-2020 wildland-urban interface of the conterminous United States - geospatial data. 3rd Edition. https://doi.org/10.2737/RDS-2015-0012-3
* Radeloff, V.C.; Helmers, D.P.; Kramer, H.A.; Mockrin, M.H.; Alexandre, P.M.; Bar Massada, A.; Butsic, V.; Hawbaker, T.J.; Martinuzzi, S.; Syphard, A.D.; Stewart, S.I. 2018. Rapid growth of the US wildland-urban interface raises wildfire risk. Proceedings of the National Academy of Sciences 115(3): 3314-3319. https://doi.org/10.1073/pnas.1718850115

![conus_wui](../images/wui.gif)

#### Earth Engine Snippet

```javascript
var conusWui = ee.FeatureCollection("projects/sat-io/open-datasets/CONUS_WUI");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/CONUS_WUI

Earth Engine App: https://ee-weidignc.projects.earthengine.app/view/wui-wildfire

#### License

These data were collected using funding from the U.S. Government and can be used without additional permissions or fees. If you use these data in a publication, presentation, or other research product please cite the data appropriately.

This work is marked with CC0 1.0 Universal (Public Domain).

Created by: Volker C. Radeloff, David P. Helmers, Miranda H. Mockrin, Amanda R. Carlson, Todd J. Hawbaker, and Sebastián Martinuzzi — SILVIS Lab (University of Wisconsin-Madison), USDA Forest Service Northern Research Station, and U.S. Geological Survey

Curated in GEE by: Noah Weidig, Victoria Donovan and Samapriya Roy

Keywords: WUI, Wildland-Urban Interface, Wildfire Risk, Fragmentation, Housing Growth, Wildland Fire, Sprawl

Last updated: 2026-06-30
