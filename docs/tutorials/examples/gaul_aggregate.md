# Creating Country-Level Boundaries from GAUL Dataset in Google Earth Engine

<p style="text-align: right;">
by <a href="#">Rambaud Pierrick</a>
</p>

### Introduction

This tutorial demonstrates how to create country-level boundaries (Level 0) from sub-national administrative units (Level 1) using the Global Administrative Unit Layers (GAUL) dataset in Google Earth Engine (GEE). You will learn how to aggregate Level 1 administrative boundaries to create country-level boundaries, handle GEE limitations, and implement alternative solutions using Python.

### Section 1: Understanding the GAUL Dataset

The Global Administrative Unit Layers (GAUL) dataset is developed and owned by the Food and Agriculture Organization of the United Nations (FAO). It provides a comprehensive spatial dataset of sub-national administrative units for all countries in the world, consistent with the United Nations (UN) delineation of international boundaries.

The GAUL dataset is available at different administrative levels:
- Level 0: Country boundaries
- Level 1: First-level administrative units (e.g., states, provinces)
- Level 2: Second-level administrative units (e.g., districts, counties)

While Level 1 boundaries are readily available in Google Earth Engine, Level 0 boundaries need to be created by dissolving Level 1 features by country.

```javascript
// Load the GAUL Level 1 dataset
var level1 = ee.FeatureCollection("projects/sat-io/open-datasets/FAO/GAUL/GAUL_2024_L1");
print('GAUL Level 1 collection', level1);
```

### Section 2: Creating Level 0 Boundaries in Google Earth Engine

You can create Level 0 boundaries by dissolving Level 1 features that belong to the same country. First, we need to get a list of unique country codes:

```javascript
// Get unique country codes from the Level 1 dataset
var level0_codes = level1.aggregate_array("gaul0_code").distinct();
print('Unique country codes', level0_codes);
```

Then, we can iterate through each country code, filter the Level 1 features for that country, and dissolve them to create a single country boundary:

```javascript
// Create a function to dissolve Level 1 features by country
var feature_list = level0_codes.map(function(code){
  var features = level1.filter(ee.Filter.eq("gaul0_code", code));
  return ee.Feature(
    ee.Feature(features.geometry().dissolve())
    .copyProperties({
      source: features.first(),
      exclude: ["gaul1_code", "gaul1_name"]
    })
  );
});

// Create a FeatureCollection of Level 0 boundaries
var level0 = ee.FeatureCollection(feature_list);
print('GAUL Level 0 collection', level0);

// Visualize the Level 0 boundaries
Map.addLayer(level0, {color: 'blue'}, 'GAUL Level 0');

// Export the Level 0 boundaries to an Earth Engine asset
Export.table.toAsset({
  collection: level0,
  description: 'GAUL_2024_L0',
  assetId: 'GAUL_2024_L0',
});
```

### Section 3: Handling GEE Limitations

The approach above may encounter limitations in Google Earth Engine due to the complexity of dissolving large geometries. GEE has a known issue (https://issuetracker.google.com/issues/417134421) that can cause errors when dissolving certain complex geometries.

If you encounter errors with the GEE approach, you can use an alternative method by exporting the Level 1 boundaries and processing them locally using Python and GeoPandas.

```javascript
// Export the Level 1 boundaries to a GeoJSON file for local processing
Export.table.toDrive({
  collection: level1,
  description: 'GAUL_2024_L1_for_local_processing',
  fileFormat: 'GeoJSON',
  fileNamePrefix: 'GAUL_2024_L1'
});
```

### Section 4: Creating Level 0 Boundaries Using Python

After exporting the Level 1 boundaries to a GeoJSON file, you can use Python and GeoPandas to dissolve the features by country:

```python
import geopandas as gpd

# Read the GeoJSON file exported from GEE
gdf = gpd.read_file("GAUL_2024_L1.geojson")

# Dissolve the features by country code
gdf0 = gdf.dissolve(by="gaul0_code").drop(columns=["gaul1_code", "gaul1_name"])

# Export the result to a Shapefile
gdf0.to_file("GAUL_2024_L0.shp")
```

This Python approach is more reliable for complex geometries and large datasets. After creating the Level 0 boundaries locally, you can upload them back to Google Earth Engine as an asset.

### Section 5: Using the Created Level 0 Boundaries

Once you have created the Level 0 boundaries, you can use them for various applications in Google Earth Engine:

```javascript
// Load the created Level 0 boundaries
var gaul0 = ee.FeatureCollection("users/YOUR_USERNAME/GAUL_2024_L0");

// Select specific countries by their GAUL codes
var france = gaul0.filter(ee.Filter.eq('gaul0_code', 85));
var germany = gaul0.filter(ee.Filter.eq('gaul0_code', 93));

// Visualize selected countries
Map.addLayer(france, {color: 'blue'}, 'France');
Map.addLayer(germany, {color: 'red'}, 'Germany');

// Center the map on Europe
Map.setCenter(10, 51, 4);
```

### Conclusion

This tutorial demonstrated how to create country-level boundaries (Level 0) from sub-national administrative units (Level 1) using the GAUL dataset in Google Earth Engine. You learned how to aggregate Level 1 boundaries by country, handle GEE limitations, and implement alternative solutions using Python and GeoPandas.

The created Level 0 boundaries can be used for various applications, such as country-level analysis, visualization, and as input for other Earth Engine algorithms.

Keywords: GAUL, Global Administrative Unit Layers, Earth Engine, Administrative Boundaries, GeoPandas, Dissolve, Level 0, Level 1
