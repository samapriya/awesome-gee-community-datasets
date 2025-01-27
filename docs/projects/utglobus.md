# GLObal Building heights for Urban Studies (UT-GLOBUS)

The University of Texas - GLObal Building heights for Urban Studies (UT-GLOBUS) dataset provides building heights and urban canopy parameters (UCPs) for more than 1200 cities worldwide. It combines open-source spaceborne altimetry (ICESat-2 and GEDI), and coarse-resolution urban canopy elevation data with a machine-learning model to estimate building-level information. The dataset includes individual building polygons with height attributes in meters above ground level, suitable for visualization using GIS platforms.  UCPs are provided in a binary file format compatible with the Weather Research and Forecasting (WRF) preprocessing system. The primary objective of UT-GLOBUS is to provide a dataset for modelling applications from city to street scales, particularly for deriving UCPs for the multi-layer UCM in the WRF-Urban model and for providing building heights for the SOlar and LongWave Environmental Irradiance Geometry (SOLWEIG) model.

**Key Features and Details**

*   **Building Heights:** Provided as vector files with individual building polygons and height attributes in meters.
*   **Urban Canopy Parameters (UCPs):** Available in a binary file format compatible with WRF preprocessing system. UCPs include plan area fraction (λp), building surface to plan area ratio (λb), and area-averaged building height (ha), along with the building height histogram with 5-meter bin size.
*   **Spatial Resolution:** Building heights are derived at a 30-meter spatial resolution. UCPs are calculated using a 300-meter sliding kernel with 1 km² area.
*   **Data Sources:** Combines data from spaceborne altimetry (ICESat-2 and GEDI), JAXA ALOS/PRISM near-global stereo DSM, the World Settlement Footprint (WSF) 3-D dataset, and OpenStreetMap (OSM), Google, and Microsoft for building footprints.
*   **Machine Learning:** A random forest model is used to predict building heights, trained on LiDAR data from six US cities.
*   **Validation:** Validation using LiDAR data from six U.S. cities showed that UT-GLOBUS derived building heights had a root mean squared error (RMSE) of 9.1 meters. Validation of mean building heights within 1-km2 grid cells, including data from Hamburg and Sydney, resulted in an RMSE of 7.8 meters.
*  **Data Access:** The dataset can be accessed on [Zenodo here](https://doi.org/10.5281/zenodo.11156602). The dataset includes building heights in vector file format, UCPs in WRF pre-processing system compatible binary file format, and a city coverage vector file.

#### Citation

```
Kamath, H.G., Singh, M., Malviya, N. et al. GLObal Building heights for Urban Studies (Ut-GLOBUS) for city- and street- scale urban simulations: Development and first
applications. *Sci Data* **11**, 617 (2024). https://doi.org/10.1038/s41597-024-03719-w
```

#### Dataset Citation

```
Kamath, H., Singh, M., Malviya, N., Martilli, A., He, L., Aliaga, D., He, C., Chen, F., Magruder, L., Yang, Z.-L., & Niyogi, D. (2024). GLObal Building heights for Urban Studies
(UT-GLOBUS) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.11156602
```

#### Dataset preprocessing
The datasets which are in gpkg format are converted into Earth Engine compatible formats. In some cases cities were divided into multiple parts and attempts were made to create a merged feature collection. Custom code was written to automate this process and to progressively remove duplicates and parts once merge had been completed. While the original collection has 1200 cities only 1088 could be ingested owing to ingestion failure at Earth Engine side. I wanted to create an app for users to select a city and click and get heigh information and that has been implemented and I have included the link.

![ut-globus](https://github.com/user-attachments/assets/f5d856a2-55ea-49ef-9fb0-3a29bf3d8fbe)

#### Code Snippet

```js
//Sample code for a city
var table = ee.FeatureCollection("projects/sat-io/open-datasets/UT-GLOBUS/peoria");

// Set the map center and zoom
Map.setCenter(-89.60, 40.73, 17);

// Get the current map bounds
var bounds = ee.Geometry.Rectangle(Map.getBounds());

// Filter the feature collection to the bounds
var filteredTable = table.filterBounds(bounds);

// Calculate minimum and maximum heights
var ht_min = filteredTable.aggregate_min('height');
var ht_max = filteredTable.aggregate_max('height');

// Define a color palette as an Earth Engine List
var palette = ee.List([
  '#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78',
  '#2ca02c', '#98df8a', '#d62728', '#ff9896',
  '#9467bd', '#c5b0d5'
]);

// Assign colors based on height
var colorFeatures = filteredTable.map(function(feature) {
  var height = feature.getNumber('height');
  var min = ee.Number(ht_min);
  var max = ee.Number(ht_max);

  // Normalize the height to [0, 1]
  var normalizedHeight = height.subtract(min).divide(max.subtract(min));

  // Map the normalized height to one of the palette indices
  var paletteIndex = normalizedHeight.multiply(palette.length().subtract(1)).floor();

  // Clamp the palette index to valid bounds
  var clampedIndex = paletteIndex.min(palette.length().subtract(1)).max(0);

  // Get the corresponding color from the Earth Engine List
  var color = palette.get(clampedIndex);

  return feature.set('style', {color: color, width: 2});
});

// Apply the styles and add to the map
var styledTable = colorFeatures.style({styleProperty: 'style'});

Map.addLayer(styledTable, {}, 'Palette Colored Table');
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/UT-GLOBUS

Earth Engine App: https://sat-io.earthengine.app/view/ut-globus

#### License
The article is licensed under a Creative Commons Attribution 4.0 International license.

Provided by: Kamath, H.G., Singh, M., Malviya, N. et al 2024

Curated in GEE by: Samapriya Roy

Keywords: Building cover, Building Height, City Morphology, Machine Learning

Last updated in GEE: 2025-01-25


