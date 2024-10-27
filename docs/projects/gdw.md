# Global Dam Watch (GDW) Database

The Global Dam Watch (GDW) database provides a comprehensive, geo-referenced global repository of river barriers and reservoirs for large-scale analysis. Version 1.0 includes 41,145 river barriers and 35,295 associated reservoir polygons, detailing barrier attributes like height, purpose, year, volume, and discharge. The database is harmonized with global river networks (HydroSHEDS and RiverATLAS) to facilitate hydrological analysis and evaluate upstream/downstream effects. It integrates multiple sources, including satellite-derived data and machine learning techniques, to achieve consistent global coverage and supports various applications such as environmental impact assessments and freshwater system management. You can read more about the database in [their paper](https://www.nature.com/articles/s41597-024-03752-9)

The GDW v1.0 database consists of two GIS layers: a point layer containing representative barrier locations with attributes, and a polygon layer of corresponding reservoir outlines with attributes. Each barrier point lies within its reservoir polygon, allowing spatial joining based on location. Both attribute tables share the same unique identification number for each barrier-reservoir pair. Version 1.0 includes 41,145 barrier points and 35,295 reservoir polygons, meaning 5,850 barrier locations have no polygon. These include navigation locks, diversion barrages, flood-event storage check dams, weirs, other instream control barriers, or dams under construction without filled reservoirs. The dataset and its accompanying resources are accessible through the Global Dam Watch platform [https://www.globaldamwatch.org](https://www.globaldamwatch.org) and the Figshare repository [https://doi.org/10.6084/m9.figshare.25988293](https://doi.org/10.6084/m9.figshare.25988293).

#### Citation

```
Lehner, Bernhard, Penny Beames, Mark Mulligan, Christiane Zarfl, Luca De Felice, Arnout van Soesbergen, Michele Thieme et al. "The Global Dam Watch database of river barrier and reservoir information for large-scale applications." Scientific Data 11, no. 1 (2024): 1069.
```

#### Dataset Citation

```
Lehner, Bernhard; Beames, Penny; Mulligan, Mark; Zarfl, Christiane; De Felice, Luca; van Soesbergen, Arnout; et al. (2024). Global Dam Watch database version 1.0.
figshare. Dataset. https://doi.org/10.6084/m9.figshare.25988293.v1
```

![gdw](https://github.com/user-attachments/assets/d513f55c-78f9-4c93-8af3-4fc1d26010e5)

#### Earth Engine Snippet

```js
var gdw_barriers = ee.FeatureCollection("projects/sat-io/open-datasets/GDW/GDW_BARRIERS_V1_0");
var gdw_reservoirs = ee.FeatureCollection("projects/sat-io/open-datasets/GDW/GDW_RESERVOIRS_V1_0");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:/hydrology/GLOBAL-DAM-WATCH-DATABASE


### License Information
The GDW database is distributed under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.

Provided by: Lehner et al 2024, Global Dam Watch

Curated in GEE by: Samapriya Roy

Keywords: River Barriers, Reservoirs, Hydropower Dams, Water Storage, Flood Control, Aquatic Ecosystems

Last updated: 2024-10-27
