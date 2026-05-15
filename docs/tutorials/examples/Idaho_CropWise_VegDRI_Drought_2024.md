# Crop-Wise Drought Sensitivity Mapping in Idaho Using the Vegetation Drought Response Index (VegDRI), 2024

## 1. What is VegDRI?

The **Vegetation Drought Response Index (VegDRI)** is a weekly drought-monitoring product for the United States that captures how vegetation actually responds to drought stress, rather than only describing climate dryness.

VegDRI was jointly developed by:
- USGS EROS Center  
- National Drought Mitigation Center (NDMC), University of Nebraska  
- High Plains Regional Climate Center (HPRCC)

VegDRI integrates three categories of information:
1. Satellite-based vegetation condition
2. Climate-based drought indicators
3. Biophysical and environmental controls

Satellite-based vegetation condition is derived from MODIS (Terra) NDVI data at 1 km spatial resolution using:
- **PASG** (Percent Annual Seasonal Greenness)
- **SOSA** (Start of Season Anomaly)

Climate-based drought indicators include:
- **PDSI** (Palmer Drought Severity Index)
- **SPI** (Standardized Precipitation Index)

Additional biophysical inputs include land use/land cover, soil available water capacity, elevation, irrigation status, and ecological region. Non-drought disturbances such as wildfire, pests, flooding, or land-use change can also influence VegDRI values.

## Why VegDRI is useful for agriculture

VegDRI reflects **actual crop stress** rather than potential drought conditions. For Idaho croplands such as alfalfa, potatoes, barley, and wheat, VegDRI enables:
- Crop-wise drought sensitivity assessment  
- Identification of spatial variability within the same crop  
- Comparison of drought response across crop types  
- Evaluation of drought response patterns for a single year (2024)

## Citation

Brown, J. F., Wardlow, B. D., Tadesse, T., Hayes, M. J., & Reed, B. C. (2008).  
**The Vegetation Drought Response Index (VegDRI): A New Integrated Approach for Monitoring Drought Stress in Vegetation.**  
*GIScience & Remote Sensing*, 45(1), 16–46.

## What you will learn

This workflow demonstrates how to:
- Load VegDRI data in Google Earth Engine (GEE)
- Extract VegDRI for Idaho croplands
- Generate crop-wise drought sensitivity maps
- Compare drought response among major crops in Idaho

GEE Code Link: https://code.earthengine.google.com/902d5e23281c379a6a3e4ba15173a650

---

## Idaho VegDRI 2024 Analysis — Complete Workflow with Explanation

```javascript
// ======================================================================
// STEP 1: DEFINE THE REGION OF INTEREST (IDAHO)
// ----------------------------------------------------------------------
// The TIGER/2018/States dataset is used to extract the boundary of Idaho.
// This limits all subsequent analysis and visualization to Idaho only.
// ======================================================================
var idaho = ee.FeatureCollection('TIGER/2018/States')
  .filter(ee.Filter.eq('NAME', 'Idaho'));

// Center the map view over Idaho for better visualization
Map.centerObject(idaho, 6);

// ======================================================================
// STEP 2: LOAD AND SCALE VEGDRI DATA FOR 2024
// ----------------------------------------------------------------------
// VegDRI values are stored as integer values.
// They must be converted to scaled VegDRI values using:
// VegDRI_scaled = (PixelValue - 128) / 16
// This rescales the data to approximately -4 (dry) to +4 (moist).
// ======================================================================
var vegdri_raw = ee.ImageCollection('projects/climate-engine-pro/assets/ce-veg-dri')
  .filterBounds(idaho)
  .filterDate('2024-01-01', '2025-01-01')
  .sort('system:time_start');

// Function to apply VegDRI scaling to each image
function scaleVeg(img){
  return img.addBands(
    img.select("vegdri")
      .subtract(128)
      .divide(16)
      .rename("vegdri_scale")
  );
}

// Apply scaling to all 2024 VegDRI images
var veg2024 = vegdri_raw.map(scaleVeg);

// ======================================================================
// STEP 3: DEFINE VEGDRI VISUALIZATION PALETTE
// ----------------------------------------------------------------------
// Red tones represent dry conditions.
// White represents near-normal vegetation conditions.
// Green tones represent moist conditions.
// ======================================================================
var vegPaletteSimple = [
  "#720206", "#cb3121", "#e36b09", "#fee301", // Dry
  "#ffffff",                                // Normal
  "#88f9c7", "#53c285", "#2b8032"           // Moist
];

// ======================================================================
// STEP 4: LOAD USDA CROPLAND DATA LAYER (CDL)
// ----------------------------------------------------------------------
// The Cropland Data Layer (CDL) is used to identify crop-specific pixels.
// Individual crops are selected using their CDL class codes.
// ======================================================================
var cdl = ee.ImageCollection("USDA/NASS/CDL")
  .filterBounds(idaho)
  .sort("system:time_start", false)
  .first()
  .select("cropland")
  .clip(idaho);

// List of major Idaho crops and their CDL codes
var crops = [
  {name: 'Corn', value: 1},
  {name: 'Barley', value: 21},
  {name: 'Spring Wheat', value: 23},
  {name: 'Winter Wheat', value: 24},
  {name: 'Alfalfa', value: 36},
  {name: 'Potatoes', value: 43},
  {name: 'Sugarbeets', value: 41}
];

// ======================================================================
// STEP 5: CREATE ANNUAL MEAN VEGDRI COMPOSITE
// ----------------------------------------------------------------------
// All weekly VegDRI images from 2024 are averaged to produce
// a single annual VegDRI map representing overall drought response.
// ======================================================================
var veg_annual = veg2024
  .select("vegdri_scale")
  .mean()
  .rename("veg_annual");

// Display the statewide annual VegDRI map
Map.addLayer(
  veg_annual.clip(idaho),
  {min:-5, max:5, palette: vegPaletteSimple},
  "VegDRI 2024 – Annual Mean"
);

// ======================================================================
// STEP 6: GENERATE CROP-SPECIFIC VEGDRI MAPS
// ----------------------------------------------------------------------
// For each crop, the CDL is used to mask VegDRI pixels belonging
// only to that crop, allowing crop-wise drought visualization.
// ======================================================================
function addCropAnnual(crop){
  var mask = cdl.eq(crop.value).selfMask();
  var layer = veg_annual.updateMask(mask);

  Map.addLayer(
    layer,
    {min:-5, max:5, palette: vegPaletteSimple},
    crop.name + " – VegDRI 2024",
    false
  );
}

// Apply the crop-specific mapping function
crops.forEach(addCropAnnual);

// ======================================================================
// STEP 7: CALCULATE CROP-WISE STATISTICS
// ----------------------------------------------------------------------
// Mean and standard deviation of VegDRI are calculated for each crop
// across the entire state of Idaho.
// ======================================================================
function cropStats(crop){
  var mask = cdl.eq(crop.value).selfMask();

  var stats = veg_annual.updateMask(mask)
    .reduceRegion({
      reducer: ee.Reducer.mean().combine({
        reducer2: ee.Reducer.stdDev(),
        sharedInputs: true
      }),
      geometry: idaho,
      scale: 500,
      maxPixels: 1e13
    });

  return ee.Feature(null, {
    crop: crop.name,
    mean: stats.get("veg_annual_mean"),
    std: stats.get("veg_annual_stdDev")
  });
}

// Convert statistics into a FeatureCollection
var stats_fc = ee.FeatureCollection(crops.map(cropStats));

// ======================================================================
// STEP 8: VISUALIZE CROP-WISE MEAN VEGDRI
// ----------------------------------------------------------------------
// A bar chart is created to compare annual mean VegDRI
// across different crop types.
// ======================================================================
var chart = ui.Chart.feature.byFeature(stats_fc, 'crop', ['mean'])
  .setChartType('ColumnChart')
  .setOptions({
    title: "VegDRI 2024 – Annual Mean by Crop",
    vAxis: {title: "VegDRI (scaled)"},
    hAxis: {title: "Crop"},
    legend: "none"
  });

// Display the chart in the console
print(chart);

// ======================================================================
// STEP 9: ADD VEGDRI LEGEND
// ----------------------------------------------------------------------
// A custom legend is added to explain drought and moisture classes.
// ======================================================================
var legend = ui.Panel({
  style: {position: 'bottom-left', padding: '8px'}
});

legend.add(ui.Label({
  value: 'VegDRI Drought Scale',
  style: {fontWeight:'bold', fontSize:'14px'}
}));

var labels = [
  "Severe","Moderate–Severe","Moderate","Mild Dry",
  "Normal","Mild Moist","Moist","Very Moist"
];

for (var i = 0; i < vegPaletteSimple.length; i++){
  var row = ui.Panel({layout: ui.Panel.Layout.Flow('horizontal')});

  row.add(ui.Label({
    style:{
      backgroundColor: vegPaletteSimple[i],
      padding:'8px',
      border:'1px solid black'
    }
  }));

  row.add(ui.Label(labels[i], {margin:'6px 0 0 6px'}));
  legend.add(row);
}

// Add the legend to the map
Map.add(legend);






