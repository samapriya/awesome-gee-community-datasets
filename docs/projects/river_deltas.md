# Global River Deltas and vulnerability

Global river delta dataset combines 2174 delta locations with polygons that define delta area. We define delta area as the extent of geomorphic activity created by deltaic channel movement, and delta progradation. We focus on channel network activity because it defines the most flood-prone zone and creates the resources and natural infrastructures that make deltas attractive sites for habitation. We define deltaic polygons with five points that encompass deltaic activity. These five points mark visible traces of deltaic activity with two points capturing the lateral extent of deposition along the shoreline, and with three points enclosing the up and downstream extent of deposition. The convex hull around these five points defines a delta polygon. You can read the [open source paper here](https://www.nature.com/articles/s41467-020-18531-4?mc_cid=b1c1d848c0&mc_eid=1370129849) and you can download the data used to create the feature collection from the [supplementary material here](https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-020-18531-4/MediaObjects/41467_2020_18531_MOESM3_ESM.xlsx).

![delta_hull_bounds](https://user-images.githubusercontent.com/6677629/116001641-023dbd00-a5bb-11eb-8afc-5d16ba19afdb.gif)

#### Earth Engine Snippet

```js
var convex_hull = ee.FeatureCollection("projects/sat-io/open-datasets/delta/delta-convex-hull");
var convex_hull_bound = ee.FeatureCollection("projects/sat-io/open-datasets/delta/delta-convex-bounds");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/GLOBAL-RIVER-DELTAS-VULNERABILITY


#### Citation

```
Edmonds, Douglas A., Rebecca L. Caldwell, Eduardo S. Brondizio, and Sacha MO Siani.
"Coastal flooding will disproportionately impact people on river deltas."
Nature communications 11, no. 1 (2020): 1-8.
```

#### License

This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Curated by: Samapriya Roy

Keywords: : Fluvial Geomorphology, Hydrology, Rivers, Coastal Rivers, Tidal, River Mouth, Vulnerability, Poverty

Last updated: 2021-04-24
