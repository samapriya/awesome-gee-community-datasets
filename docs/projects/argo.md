# Argo Float Data(Subset)

Argo is an international program that collects information from inside the ocean using a fleet of robotic instruments that drift with the ocean currents and move up and down between the surface and a mid-water level. Each instrument (float) spends almost all its life below the surface. The name Argo was chosen because the array of floats works in partnership with the Jason earth observing satellites that measure the shape of the ocean surface. (In Greek mythology Jason sailed on his ship the Argo in search of the golden fleece). To learn more about Argo, how it works, [its data and technology, and its scientific and environmental impact, click here](https://argo.ucsd.edu/).

![float_cycle_1](https://user-images.githubusercontent.com/6677629/127728607-85e6328f-0323-4ca2-a8da-4d3e8a79d141.png)

#### Citation

These data were collected and made freely available by the International Argo Program and the national programs that contribute to it.  (https://argo.ucsd.edu,  https://www.ocean-ops.org).  The Argo Program is part of the Global Ocean Observing System.

The general Argo DOI is below.

Argo (2000). Argo float data and metadata from Global Data Assembly Centre (Argo GDAC). SEANOE. https://doi.org/10.17882/42182

If you used data from a particular month, please add the month key to the end of the DOI url to make it reproducible.  The key is comprised of the hashtag symbol (#) and then numbers.  For example, the key for August 2020 is 76230. The citation would look like:

Argo (2020). Argo float data and metadata from Global Data Assembly Centre (Argo GDAC) – Snapshot of Argo GDAC of August 2020. SEANOE. https://doi.org/10.17882/42182#76230

#### ArgoVis citation
Argovis API was used to parse through and get to the datasets, you can cite argovis using the following

```
Tucker, T., D. Giglio, M. Scanderbeg, and S.S. Shen, 2020: Argovis: A Web Application for Fast Delivery,
Visualization, and Analysis of Argo Data. J. Atmos. Oceanic Technol., 37 (3), 401-416
https://doi.org/10.1175/JTECH-D-19-0041.1
```

#### Argo Float data tables

Argo float dataset has been parsed into a small subset of about 10,000 feature collections flattened into a single collection with over 6.5 million features with total distinct argo float count at 881. The argo float property variables and GEE property names are listed below

<center>

|Property         |GEE Property  |Property Type|
|-----------------|--------------|-------------|
|pid              |Platform ID   |integer      |
|Instrument Type  |inst_typ      |integer      |
|date             |date          |integer      |
|date added       |date_added    |integer      |
|profile number   |profile_number|string       |
|maximum pressure |max_pres      |float        |
|pres_max_for_TEMP|pmax_temp     |float        |
|pres_min_for_TEMP|pmin_temp     |float        |
|pres_max_for_PSAL|pmax_psal     |float        |
|pres_min_for_PSAL|pmin_psal     |float        |
|Temperature      |temp          |float        |
|Salinity         |psal          |float        |
|Pressure         |pres          |float        |


</center>

#### Earth Engine Snippet

```js
var argo = ee.FeatureCollection("projects/sat-io/open-datasets/argo-subset");
```

Sample Code: https://code.earthengine.google.com/f43b787ef6890302b01e7f87e40dd8e2

![argo_floats_10000](https://user-images.githubusercontent.com/6677629/127728608-08ed871a-bab4-46df-9cad-628760e6b335.png)

#### License
Argo data are freely available without restriction and are released in a model similar to a CC0 1.0 Universal (CC0 1.0) Public Domain Dedication.

Created by : International Argo Program, Global Data Assembly Centre

Curated in GEE by: Samapriya Roy

Keywords: float, Argo, global ocean observing system, ocean circulation, in-situ, ocean pressure, sea water salinity, sea water temperature, multi-year, weather climate and seasonal observation, global-ocean

Last updated : 2021-07-30
