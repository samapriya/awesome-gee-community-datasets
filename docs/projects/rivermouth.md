# Global coastal rivers and environmental variables

A global dataset of 5399 coastal rivers and data on eight environmental variables. Of these rivers, 40 % (n=2174) have geomorphic deltas defined either by a protrusion from the regional shoreline, a distributary channel network, or both. Globally, coastlines average one delta for every ∼300 km of shoreline, but there are hotspots of delta formation, for example in Southeast Asia where there is one delta per 100 km of shoreline. Our analysis shows that the likelihood of a river to form a delta increases with increasing water discharge, sediment discharge, and drainage basin area. On the other hand, delta likelihood decreases with increasing wave height and tidal range. Delta likelihood has a non-monotonic relationship with receiving-basin slope: it decreases with steeper slopes, but for slopes >0.006 delta likelihood increases. This reflects different controls on delta formation on active versus passive margins.

![global_costal_rivers](https://user-images.githubusercontent.com/6677629/115134417-826d8c80-9fd5-11eb-8758-b2efadfab2b7.gif)


#### Earth Engine Snippet:

```js
var global_costal_rivers = ee.FeatureCollection("projects/sat-io/open-datasets/delta/global-costal-rivers-points");
```

Sample Code: https://code.earthengine.google.com/8dd904e9d95fe96fa058571b27f25f40


#### Citation

```
Caldwell, R. L., Edmonds, D. A., Baumgardner, S., Paola, C., Roy, S., and Nienhuis, J. H.: A global delta dataset and the environmental variables that predict delta formation on marine coastlines, Earth Surf. Dynam., 7, 773–787, https://doi.org/10.5194/esurf-7-773-2019, 2019.
```

Additional information


*Property Match from Supplement*

|Properties|Reference Property |
|----------|-----------------------------|
|ID |ID |
|DL_Binary |Delta Presence or Absence |
|Region |Region |
|Latitude |RM_Lat |
|Longitude |RM_Lon |
|MF_matches|M&F_matches |
|MF_IDs |M&F_ID(s) |
|WV_HT_Hw_m|Wave_Height_Hw (m) |
|WV_HT_m |Tidal_Range_Ht (m) |
|Bslope_RM |Bathymetric_Slope_from_RM_Sbr|
|SLC_mm |Sea_Level_Change (mm yr^-1) |


*Region Code and Description Tables*


|Region Code|Region Description |
|--------------------|----------------------------------|
|AFR |mainland Africa |
|AUS |Australia, New Zealand, New Guinea|
|BLS |Black Sea, Sea of Azov |
|CAM |Central America |
|EAS |East Asia |
|EUR |Europe |
|MAD |Madagascar |
|MED |Mediterranean |
|MID |Middle East |
|NAM |North America |
|RUS |Russia |
|SAM |South America |
|SAS |South Asia |
|SEA |Southeast Asia |


#### License
Shared License: This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.


Curated by: Samapriya Roy

Keywords: :"Fluvial Geomorphology, Hydrology, Rivers, Coastal Rivers, Tidal, River Mouth"

Last updated: 2021-04-17
