# NOAA Evaporative Stress Index (ESI): Description, Methodology, and Google Earth Engine Implementation

The **Evaporative Stress Index (ESI)** is a satellite-based, unitless drought indicator developed by the **NOAA Center for Satellite Applications and Research (STAR)** in collaboration with the **USDA Agricultural Research Service (ARS)**. ESI quantifies **standardized anomalies in evapotranspiration (ET)** and is designed to detect vegetation and soil moisture stress independent of precipitation measurements (Anderson et al., 2011).

Unlike traditional drought indices (e.g., SPI or SPEI), which rely on precipitation and water balance assumptions, ESI is derived using a **thermal remote sensing–based energy balance approach**. Actual ET is estimated using **land surface temperature (LST) time-change signals**, which respond rapidly to changes in soil moisture and plant stress (Norman et al., 1995; Anderson et al., 1997). Because LST is a fast-response variable, ESI is particularly effective in identifying **rapid-onset or “flash” droughts** driven by hot, dry, and windy conditions (Otkin et al., 2013; Anderson et al., 2011).

ESI values represent standardized departures from a long-term ET climatology:
- **Positive ESI values** indicate wetter-than-normal or unstressed conditions  
- **Negative ESI values** indicate moisture stress and drought  

The dataset has **global coverage**, approximately **4 km spatial resolution (1/24°)**, **weekly temporal resolution**, spans **2001 to present**, and is updated weekly with approximately a **one-week latency**. Two commonly used time scales are:
- **4-week ESI**: short-term moisture stress and early drought signals  
- **12-week ESI**: seasonal-scale drought evolution  

---

## Google Earth Engine Code: Idaho ESI Analysis for 2024

The following Google Earth Engine (GEE) script loads NOAA ESI data from Climate Engine, clips it to Idaho, computes annual mean composites for 2024, visualizes spatial drought patterns, adds a simplified interpretive legend, and generates state-average weekly time series.

```js
// ======================================================================
// 1. LOAD IDAHO STATE BOUNDARY
// TIGER/2018 U.S. Census state boundaries are used for spatial masking
// ======================================================================
var idaho = ee.FeatureCollection('TIGER/2018/States')
  .filter(ee.Filter.eq('NAME', 'Idaho'));

Map.centerObject(idaho, 6);

// ======================================================================
// 2. LOAD NOAA ESI IMAGE COLLECTIONS (CLIMATE ENGINE)
// 4-week ESI captures short-term ET anomalies
// 12-week ESI captures seasonal moisture stress
// ======================================================================
var esi4 = ee.ImageCollection('projects/climate-engine/esi/4wk');
var esi12 = ee.ImageCollection('projects/climate-engine/esi/12wk');

// ======================================================================
// 3. FILTER FOR IDAHO AND CALENDAR YEAR 2024
// Spatial filtering ensures analysis is limited to Idaho
// Temporal filtering selects weekly data from 2024
// ======================================================================
var esi4_2024 = esi4
  .filterBounds(idaho)
  .filterDate('2024-01-01', '2025-01-01')
  .select('ESI');

var esi12_2024 = esi12
  .filterBounds(idaho)
  .filterDate('2024-01-01', '2025-01-01')
  .select('ESI');

print('4-week ESI image count (2024):', esi4_2024.size());
print('12-week ESI image count (2024):', esi12_2024.size());

// ======================================================================
// 4. COMPUTE ANNUAL MEAN ESI COMPOSITES
// Mean aggregation summarizes average moisture stress for the year
// ======================================================================
var esi4_mean = esi4_2024.mean().clip(idaho);
var esi12_mean = esi12_2024.mean().clip(idaho);

// ======================================================================
// 5. DEFINE ESI COLOR PALETTE
// Blue shades represent wet conditions, red shades indicate drought
// ======================================================================
var esi_palette = [
  "#0000aa", "#0000ff", "#00aaff", "#00ffff", "#aaff55",
  "#ffffff", "#ffff00", "#fcd37f", "#ffaa00", "#e60000", "#730000"
];

// ======================================================================
// 6. ADD ANNUAL MEAN ESI MAP LAYERS
// Visualization range follows standardized anomaly convention (±2.5)
// ======================================================================
Map.addLayer(
  esi4_mean,
  {min: -2.5, max: 2.5, palette: esi_palette},
  'ESI 4-week Mean (2024)'
);

Map.addLayer(
  esi12_mean,
  {min: -2.5, max: 2.5, palette: esi_palette},
  'ESI 12-week Mean (2024)'
);

// ======================================================================
// 7. ADD SIMPLIFIED INTERPRETIVE DROUGHT LEGEND
// Reduces full anomaly scale to six qualitative drought classes
// ======================================================================
var legend = ui.Panel({
  style: {position: 'bottom-left', padding: '8px'}
});

legend.add(ui.Label('ESI Drought Scale (NOAA)', {
  fontWeight: 'bold',
  fontSize: '14px'
}));

var simple_palette = [
  "#0000ff",  // Wet
  "#00ffff",  // Slightly Wet
  "#ffffff",  // Normal
  "#ffff00",  // Slightly Dry
  "#ffaa00",  // Dry
  "#e60000"   // Very Dry
];

var simple_labels = [
  'Wet',
  'Slightly Wet',
  'Normal',
  'Slightly Dry',
  'Dry',
  'Very Dry'
];

for (var i = 0; i < simple_palette.length; i++) {
  legend.add(
    ui.Panel({
      layout: ui.Panel.Layout.Flow('horizontal'),
      widgets: [
        ui.Label({
          style: {
            backgroundColor: simple_palette[i],
            padding: '10px',
            margin: '0 4px 0 0'
          }
        }),
        ui.Label(simple_labels[i], {margin: '6px 0 0 4px'})
      ]
    })
  );
}

Map.add(legend);

// ======================================================================
// 8. TIME SERIES: STATE-AVERAGED 4-WEEK ESI (2024)
// Highlights short-term drought dynamics across Idaho
// ======================================================================
var chart4 = ui.Chart.image.series({
  imageCollection: esi4_2024,
  region: idaho.geometry(),
  reducer: ee.Reducer.mean(),
  scale: 5000
}).setOptions({
  title: 'NOAA ESI 4-Week Time Series (Idaho, 2024)',
  vAxis: {title: 'ESI (unitless)', viewWindow: {min: -3, max: 3}},
  hAxis: {title: 'Date'},
  legend: {position: 'none'},
  colors: ['#0066ff']
});

print(chart4);

// ======================================================================
// 9. TIME SERIES: STATE-AVERAGED 12-WEEK ESI (2024)
// Represents seasonal drought evolution
// ======================================================================
var chart12 = ui.Chart.image.series({
  imageCollection: esi12_2024,
  region: idaho.geometry(),
  reducer: ee.Reducer.mean(),
  scale: 5000
}).setOptions({
  title: 'NOAA ESI 12-Week Time Series (Idaho, 2024)',
  vAxis: {title: 'ESI (unitless)', viewWindow: {min: -3, max: 3}},
  hAxis: {title: 'Date'},
  legend: {position: 'none'},
  colors: ['#ff6600']
});

print(chart12);
