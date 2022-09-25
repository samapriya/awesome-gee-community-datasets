# Aqualink ocean surface and subsurface temperature subset

Aqualink is a philanthropically funded system to help people manage their local marine ecosystems in the face of increasing Ocean temperatures. The system consists of satellite-connected underwater temperature sensors and photographic surveys to allow for remote collaboration with scientists across the world. This export was created as a subset of datasets and sites available from aqualink.org as part of making ocean temperature readings in situ truly possible and globally accessible. The aqualink buoy is a collaboration of aqualink with sofarocean to deploy this buoy as sensors that capture ocean temperature both at surface and at varying depths. They are also capable of measuring things like wave height and wind conditions among other things. You can [read about aqualink buoys here](https://aqualink.org/buoy)

![aqualink_buoy](https://aqualink.org/static/media/fulldiag3_1.8c0851fb.svg)

The datasets were downloaded and processed using the [pyaqua tool I wrote earlier](https://samapriya.github.io/pyaqua/) and you can read about [aqualink and the pyaqua tool here](https://medium.com/p/open-ocean-data-with-aqualink-pyaqua-32fb4d99c837). These represent sea surface temperature as well as temperature at depth. These were generated only for deployed buoys and are exported CSVs are then imported into Google Earth Engine. The datasets have timestamp and value for said variable which can be used further to assess conditions over time.

**This is a one year subset only for 56 deployed sites from 2020-01-04 to 2021-01-04 and is a subset for users to test and the format and duration of data might change in the future as this project evolves**

#### Data Citation

Citation rules will vary by journal or need but a good example would be

```
aqualink.org (2021). Clerke Reef West side, Australia SST. Retrieved from https://aqualink.org/sites/1218
```

![aqualink_2021](https://user-images.githubusercontent.com/6677629/148172745-65cca8f0-a017-4059-8573-8b5326580f5f.gif)

#### Earth Engine Snippet

```js
var top_temp = ee.FeatureCollection("projects/sat-io/open-datasets/open-ocean/aqualink_top_temp_2020");
var bottom_temp = ee.FeatureCollection("projects/sat-io/open-datasets/open-ocean/aqualink_bottom_temp_2020");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:oceans-shorelines/AQUALINK-SUBSET-2020

#### License

All work and data under the aqualink project are under an MIT license and free and open to the community.

Created by: aqualink org

Curated by: Samapriya Roy

Keywords: : aqualink, buoy, temperature, sea surface temperature, sst, wave, oceans, bleaching, coral reefs, extreme-sea-level

Last updated: 2022-01-05
