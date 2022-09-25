# Geocoded Disasters (GDIS) Dataset (1960 – 2018)

The Geocoded Disasters (GDIS) Dataset is a geocoded extension of a selection of natural disasters from the Centre for Research on the Epidemiology of Disasters' (CRED) Emergency Events Database (EM-DAT). The data set encompasses 39,953 locations for 9,924 disasters that occurred worldwide in the years 1960 to 2018. All floods, storms (typhoons, monsoons etc.), earthquakes, landslides, droughts, volcanic activity and extreme temperatures that were recorded in EM-DAT during these 58 years and could be geocoded are included in the data set. The highest spatial resolution in the data set corresponds to administrative level 3 (usually district/commune/village) in the Global Administrative Areas database (GADM, 2018). The vast majority of the locations are administrative level 1 (typically state/province/region). You can access the dataset from [NASA SEDAC](https://sedac.ciesin.columbia.edu/data/set/pend-gdis-1960-2018) and read the [full paper here](https://www.nature.com/articles/s41597-021-00846-6)

#### Data Citation

```
Rosvold, E., and H. Buhaug. 2021. Geocoded Disasters (GDIS) Dataset. Palisades, NY: NASA Socioeconomic Data and
Applications Center (SEDAC). https://doi.org/10.7927/zz3b-8y61. Accessed DAY MONTH YEAR.
```

#### Paper Citation

```
Rosvold, E.L., Buhaug, H. GDIS, a global dataset of geocoded disaster locations. Sci Data 8, 61 (2021).
https://doi.org/10.1038/s41597-021-00846-6
```

![gdis](https://user-images.githubusercontent.com/6677629/129650238-bdbc9768-b53d-4fda-9819-9a24a35641fa.PNG)

#### Earth Engine Snippet

```js
var gdis= ee.FeatureCollection("projects/sat-io/open-datasets/gdis_1960-2018");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-events-layers/GEOCODED-DISASTERS-DATASET

#### License

This work is licensed under the Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0). Users are free to use, copy, distribute, transmit, and adapt the work for commercial and non-commercial purposes, without restriction, as long as clear attribution of the source is provided.

Created by: NASA Socioeconomic Data and Applications Center (SEDAC)

Curated by: Samapriya Roy

Keywords: : droughts,earthquakes,floods,landslides,cyclones,volcanic eruptions

Last updated: 2021-08-16
