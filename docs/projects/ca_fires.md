# Canada 2023 Wildfires

Canada's 2023 wildfire season represented the largest area burned in a single fire season in Canada’s modern history. Using the Tracking Intra- and
Inter-year Change (TIIC) algorithm, wildfires occurring within Canada’s forested ecosystems during the 2023 fire season were detected at a 30-m
resolution. Time series data used to identify wildfires originated from Sentinel-2A and -2B, and Landsat-8 and -9. Fires have been grouped into two
classes based on detection period: summer fires and fall fires. Summer fires were detected between May 30 and September 17, and fall fires were
detected between September 17 and October 25. For summer fires, burned pixels were identified by TIIC as changed and typed as fire.

For the fall period, TIIC only detected changes within a 4-km buffer of NRCan fire perimeters (https://cwfis.cfs.nrcan.gc.ca/datamart). This
approach was used to limit commission errors that can occur due to known limitations of mapping with optical data in the fall due to phenology, snow
cover, or low sun angles. For the 2023 fire season, the TIIC algorithm detected 12.74 Mha of burned area in Canada’s forested ecozones, representing
1.8% of the total forest-dominated ecozone area. Of the 12.74 Mha, 11.57 Mha (90.9%) was burned by summer fires and 1.16 Mha (9.1%) by fall fires
(Pelletier et al., 2024). You can download the [dataset here](https://opendata.nfis.org/downloads/forest_change/CA_Forest_Fires_2023.zip)


#### Citation

```
Pelletier, F., Cardille, J.A., Wulder, M.A., White, J.C., Hermosilla, T., 2024. Revisiting the 2023 wildfire season in Canada. Science of Remote Sensing. 10, 100145. https://doi.org/10.1016/j.srs.2024.100145
```

![ca_forest23](https://github.com/user-attachments/assets/8856f1f0-752b-4718-8609-9495bbd66fb1)

### Earth Engine Snippet

```js
var image = ee.Image("projects/sat-io/open-datasets/CA_FOREST/CA_Forest_Wildfire_2023_Summer_Fall");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:fire-monitoring-analysis/CA-FOREST-FIRE-2023

#### License
This work is licensed under and freely available to the public Open Government Licence - Canada.

Created by: Pelletier et al. 2024

Curated in GEE by : Spencer Bronson and Samapriya Roy

keywords: Wildfire, Tracking Intra- Inter-year Change (TIIC), Landsat, Sentinel, Burned Area, Fire Occurrence, Canada

Last updated on GEE: 2024-08-29
