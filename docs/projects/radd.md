# RADD Forest Disturbance Alert

RADD - RAdar for Detecting Deforestation - Near real-time disturbances in humid tropical forest based on Sentinel-1 at 10m spatial scale. Primary humid tropical forest of South America (13 countries), Central America (6 countries), Africa (25 countries), insular Southeast Asia (5 countries) and Pacific (1 country). You can find [more information here at University of Wageningen](https://www.wur.nl/en/research-results/chair-groups/environmental-sciences/laboratory-of-geo-information-science-and-remote-sensing/research/sensing-measuring/radd-forest-disturbance-alert.htm)

The RADD (RAdar for Detecting Deforestation) alerts contribute to the World Resources Institute’s Global Forest Watch initiative in providing timely and accurate information to support a wide range of stakeholders in sustainable forest management and law enforcement activities against illegal deforestation. The RADD alerts are implemented in Google Earth Engine. This dataset is also available on Global Forest Watch - [Open Data Portal](https://data.globalforestwatch.org/datasets/gfw::deforestation-alerts-radd/about), [Sepal.io](https://sepal.io/) and [EarthMap](https://earthmap.org/)

#### Dataset Citation

```
Reiche J, Mullissa A, Slagter B, Gou Y, Tsendbazar N, Odongo-Braun C, Vollrath A, Weisse M, Stolle F, Pickens A, Donchyts G, Clinton N, Gorelick N &
Herold M, (2021), Forest disturbance alerts for the Congo Basin using Sentinel-1, Environmental Research Letters
https://doi.org/10.1088/1748-9326/abd0a8
```

#### Earth Engine Snippet

```js
var radd = ee.ImageCollection('projects/radar-wur/raddalert/v1');
var geography = 'sa';

// forest baseline mask
var forest_baseline = ee.Image(radd.filterMetadata('layer','contains','forest_baseline')
                            .filterMetadata('geography','equals',geography).first())

Map.addLayer(forest_baseline, {palette:['black'], opacity: 0.3},'Forest baseline')

var latest_radd_alert =  ee.Image(radd.filterMetadata('layer','contains','alert')
                            .filterMetadata('geography','equals',geography)
                            .sort('system:time_end', false).first());

Map.addLayer(latest_radd_alert.select('Alert'), {min:2,max:3,palette:['blue','coral']}, 'RADD alert')
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-events-layers/RADD-FOREST-ALERT

[Sample code to download RADD Alerts as GeoTIFF to Google Drive](https://code.earthengine.google.com/6be36b448b13aeed914b4aff7d1510dd)

#### License
The data is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/) and may be used by anyone, anywhere, anytime without permission or royalty payment.

Curated by: J Reiche, J Balling, M Herold, B Slagter, NE Tsendbazar

Keywords: Forest, Deforestation, Alerts, NBS, Sentinel-1, Radar

Last updated: 2023-01-08 (updates with S1)
