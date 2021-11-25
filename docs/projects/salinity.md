# Global Surface water and groundwater salinity measurements (1980-2019)

This data contains a new global salinity database, compiled from electrical conductivity (EC) monitoring data of both surface water (rivers, lakes/reservoirs) and groundwater locations over the period 1980-2019. The database includes information from over 16.3 million samples, from 45,103 surface water locations and 208,550 groundwater locations around the world.

The database consists of three categories;
1. River Data
2. Lake/Reservoir Data
3. Groundwater Data

Each category have two associated data files in csv-format, one containing the full salinity data, and one summary file currently the full salinity datasets are ingested. You can [download the dataset here](https://doi.pangaea.de/10.1594/PANGAEA.913939?format=html#download). You can [read the article here](https://www.nature.com/articles/s41597-020-0562-z)

#### Data Citation

```
Thorslund, Josefin; van Vliet, Michelle T H (2020): A global salinity dataset of surface water
and groundwater measurements from 1980-2019. PANGAEA, https://doi.org/10.1594/PANGAEA.913939
```

#### Paper Citation

```
Thorslund, Josefin, and Michelle TH van Vliet. "a global dataset of surface water and groundwater
salinity measurements from 1980–2019." Scientific Data 7, no. 1 (2020): 1-11.
```

![salinity](https://user-images.githubusercontent.com/6677629/143496557-aa7e244e-c2a9-4854-8602-ec343c6e542b.gif)

#### Earth Engine Snippet

```js
var groundwater = ee.FeatureCollection("projects/sat-io/open-datasets/global_water_salinity/groundwaters_database");
var rivers = ee.FeatureCollection("projects/sat-io/open-datasets/global_water_salinity/rivers_database");
var lakes_reservoir = ee.FeatureCollection("projects/sat-io/open-datasets/global_water_salinity/lakes_reservoirs_database");
```

Sample Code: https://code.earthengine.google.com/e49f67214364657a53276752089a60a7

#### License

This work is licensed under the Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0). Users are free to use, copy, distribute, transmit, and adapt the work for commercial and non-commercial purposes, without restriction, as long as clear attribution of the source is provided.

Created by: Thorslund et al

Curated by: Samapriya Roy

Keywords: : electrical conductivity, groundwater monitoring, Salinity, surface water, lakes, reservoirs

Last updated: 2021-11-25
