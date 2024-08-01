# Exploring the Global 30m Land Cover Change Dataset (1985-2022) GLC_FCS30D

<p style="text-align: right;">
by <a href="mailto:ujaval@spatialthoughts.com">Ujaval Gandhi</a> from <a href="https://spatialthoughts.com/">Spatial Thoughts</a>
</p>

A temporally consistent global multi-class time-series classification dataset is critical to understand and quantify long-term changes. Previously, options were limited to lower resolution datasets such as MODIS Landcover (2000-present) at 500m resolution or ESA CCI (1992-present) at 300m resolution. The new GLC_FCS30D dataset provides a high-resolution landcover time-series derived from the Landsat archive (1984-2022) at 30m resolution with 35 classes. This dataset is valuable for studying landscape dynamics at high resolution and is available in the public domain. It can be downloaded from Zenodo as GeoTIFF files or accessed directly in the Google Earth Engine (GEE) Community catalog. In this tutorial, we will:

- Access and preprocess the GLC_FCS30D dataset.
- Visualize and compare landcover changes between 1985-2022.
- Calculate landcover statistics and export a CSV with areas of each class for the entire time series over multiple regions.

### 1. Preprocessing the Data

The original dataset was produced in 5° x 5° tiles with each image having bands for each year of classification. This structure was uploaded to the Earth Engine Community Catalog, split into datasets for five-yearly classifications (1985-90, 1990-95, and 1995-2000) and yearly classifications (2000-2022). GEE workflows are structured around ImageCollections rather than multiband images, so we need to transform the original data into an ImageCollection.

#### Steps:

1. Merge the tiles into a global mosaic.
2. Convert the multi-band images into ImageCollections.
3. Merge the five-yearly and yearly images into a single ImageCollection.
4. Reclassify the pixels to sequential class values.

Here's the Earth Engine code for the preprocessing step and a [link to the code](https://code.earthengine.google.co.in/fa41d55186e6d708a4be367237353ff0)

```javascript
// Example script showing how to pre-process the GLC_FCS30D landcover dataset

// Yearly data from 2000-2022
var annual = ee.ImageCollection('projects/sat-io/open-datasets/GLC-FCS30D/annual');
// Five-Yearly data for 1985-90, 1990-95 and 1995-2000
var fiveyear = ee.ImageCollection('projects/sat-io/open-datasets/GLC-FCS30D/five-years-map');

// Classification scheme has 36 classes (35 landcover classes and 1 fill value)
var classValues = [10, 11, 12, 20, 51, 52, 61, 62, 71, 72, 81, 82, 91, 92, 120, 121, 122, 130, 140, 150, 152, 153, 181, 182, 183, 184, 185, 186, 187, 190, 200, 201, 202, 210, 220, 0];
var classNames = ['Rainfed_cropland', 'Herbaceous_cover_cropland', 'Tree_or_shrub_cover_cropland', 'Irrigated_cropland', 'Open_evergreen_broadleaved_forest', 'Closed_evergreen_broadleaved_forest', 'Open_deciduous_broadleaved_forest', 'Closed_deciduous_broadleaved_forest', 'Open_evergreen_needle_leaved_forest', 'Closed_evergreen_needle_leaved_forest', 'Open_deciduous_needle_leaved_forest', 'Closed_deciduous_needle_leaved_forest', 'Open_mixed_leaf_forest', 'Closed_mixed_leaf_forest', 'Shrubland', 'Evergreen_shrubland', 'Deciduous_shrubland', 'Grassland', 'Lichens_and_mosses', 'Sparse_vegetation', 'Sparse_shrubland', 'Sparse_herbaceous', 'Swamp', 'Marsh', 'Flooded_flat', 'Saline', 'Mangrove', 'Salt_marsh', 'Tidal_flat', 'Impervious_surfaces', 'Bare_areas', 'Consolidated_bare_areas', 'Unconsolidated_bare_areas', 'Water_body', 'Permanent_ice_and_snow', 'Filled_value'];
var classColors = ['#ffff64', '#ffff64', '#ffff00', '#aaf0f0', '#4c7300', '#006400', '#a8c800', '#00a000', '#005000', '#003c00', '#286400', '#285000', '#a0b432', '#788200', '#966400', '#964b00', '#966400', '#ffb432', '#ffdcd2', '#ffebaf', '#ffd278', '#ffebaf', '#00a884', '#73ffdf', '#9ebb3b', '#828282', '#f57ab6', '#66cdab', '#444f89', '#c31400', '#fff5d7', '#dcdcdc', '#fff5d7', '#0046c8', '#ffffff', '#ffffff'];

// Mosaic the data into a single image
var annualMosaic = annual.mosaic();
var fiveYearMosaic = fiveyear.mosaic();

// Rename bands from b1, b2, etc. to 2000, 2001, etc.
var fiveYearsList = ee.List.sequence(1985, 1995, 5).map(function(year) { return ee.Number(year).format('%04d'); });
var fiveyearMosaicRenamed = fiveYearMosaic.rename(fiveYearsList);
var yearsList = ee.List.sequence(2000, 2022).map(function(year) { return ee.Number(year).format('%04d'); });
var annualMosaicRenamed = annualMosaic.rename(yearsList);
var years = fiveYearsList.cat(yearsList);

// Convert the multiband image to an ImageCollection
var fiveYearlyMosaics = fiveYearsList.map(function(year) {
  var date = ee.Date.fromYMD(ee.Number.parse(year), 1, 1);
  return fiveyearMosaicRenamed.select([year]).set({'system:time_start': date.millis(), 'system:index': year, 'year': ee.Number.parse(year)});
});
var yearlyMosaics = yearsList.map(function(year) {
  var date = ee.Date.fromYMD(ee.Number.parse(year), 1, 1);
  return annualMosaicRenamed.select([year]).set({'system:time_start': date.millis(), 'system:index': year, 'year': ee.Number.parse(year)});
});
var allMosaics = fiveYearlyMosaics.cat(yearlyMosaics);
var mosaicsCol = ee.ImageCollection.fromImages(allMosaics);

// Recode the class values into sequential values
var newClassValues = ee.List.sequence(1, ee.List(classValues).length());
var renameClasses = function(image) {
  var reclassified = image.remap(classValues, newClassValues).rename('classification');
  return reclassified;
};
var landcoverCol = mosaicsCol.map(renameClasses);

print('Pre-processed Collection', landcoverCol);

// Visualize the data
var year = 2022;
var selectedLandcover = landcoverCol.filter(ee.Filter.eq('year', year)).first();
var palette = ['#ffff64', '#ffff64', '#ffff00', '#aaf0f0', '#4c7300', '#006400', '#a8c800', '#00a000', '#005000', '#003c00', '#286400', '#285000', '#a0b432', '#788200', '#966400', '#964b00', '#966400', '#ffb432', '#ffdcd2', '#ffebaf', '#ffd278', '#ffebaf', '#00a884', '#73ffdf', '#9ebb3b', '#828282', '#f57ab6', '#66cdab', '#444f89', '#c31400', '#fff5d7', '#dcdcdc', '#fff5d7', '#0046c8', '#ffffff', '#ffffff'];
var classVisParams = {min:1, max:36, palette: palette};
Map.addLayer(selectedLandcover, classVisParams, 'Landcover ' + year);
```

### 2. Visualizing Changes Using a Split-panel App

A useful way to visualize a landcover time-series is through a user interface that allows us to compare and contrast data for multiple years. Using a split-panel, we can load classifications for two different years and swipe to see changes between them. We will create a split panel interface with a dropdown selector allowing you to change the year and visualize the changes. To make the map interpretation easier, we will also construct a legend.

You can explore the app at [Global Landcover Change Explorer](https://spatialthoughts.projects.earthengine.app/view/global-landcover-change-explorer).

Here's the source code for the app:

```javascript
// Example script for an App to explore GLC_FCS30D landcover dataset using a split-panel

// Pre-process the Collection
var annual = ee.ImageCollection('projects/sat-io/open-datasets/GLC-FCS30D/annual');
var fiveyear = ee.ImageCollection('projects/sat-io/open-datasets/GLC-FCS30D/five-years-map');
var classValues = [10, 11, 12, 20, 51, 52, 61, 62, 71, 72, 81,

 82, 91, 92, 120, 121, 122, 130, 140, 150, 152, 153, 181, 182, 183, 184, 185, 186, 187, 190, 200, 201, 202, 210, 220, 0];
var newClassValues = ee.List.sequence(1, ee.List(classValues).length());
var allImages = annual.merge(fiveyear);
var renameClasses = function(image) {
  var reclassified = image.remap(classValues, newClassValues).rename('classification');
  return reclassified;
};
var landcoverCol = allImages.map(renameClasses);
var years = ee.List.sequence(1985, 2022).map(function(year) { return ee.Number(year).format('%04d'); });

var visParams = {min:1, max:36, palette: ['#ffff64', '#ffff64', '#ffff00', '#aaf0f0', '#4c7300', '#006400', '#a8c800', '#00a000', '#005000', '#003c00', '#286400', '#285000', '#a0b432', '#788200', '#966400', '#964b00', '#966400', '#ffb432', '#ffdcd2', '#ffebaf', '#ffd278', '#ffebaf', '#00a884', '#73ffdf', '#9ebb3b', '#828282', '#f57ab6', '#66cdab', '#444f89', '#c31400', '#fff5d7', '#dcdcdc', '#fff5d7', '#0046c8', '#ffffff', '#ffffff']};

// Create a Split-panel Map
var leftMap = ui.Map();
var rightMap = ui.Map();
var splitPanel = ui.SplitPanel({
  firstPanel: leftMap,
  secondPanel: rightMap,
  wipe: true,
  style: {stretch: 'both'}
});
ui.root.clear();
ui.root.add(splitPanel);

var createLegend = function() {
  var legend = ui.Panel({
    style: {
      position: 'bottom-left',
      padding: '8px 15px'
    }
  });
  var legendTitle = ui.Label({
    value: 'Landcover Legend',
    style: {fontWeight: 'bold', fontSize: '14px', margin: '0 0 4px 0', padding: '0'}
  });
  legend.add(legendTitle);

  var makeRow = function(color, name) {
    var colorBox = ui.Label({
      style: {
        backgroundColor: color,
        padding: '8px',
        margin: '0 0 4px 0'
      }
    });
    var description = ui.Label({
      value: name,
      style: {margin: '0 0 4px 6px'}
    });
    return ui.Panel({
      widgets: [colorBox, description],
      layout: ui.Panel.Layout.Flow('horizontal')
    });
  };

  for (var i = 0; i < classNames.length; i++) {
    legend.add(makeRow(classColors[i], classNames[i]));
  }
  return legend;
};

var legend = createLegend();
leftMap.add(legend);
var intro = ui.Panel([
  ui.Label('Global Landcover Change Explorer', {fontWeight: 'bold', fontSize: '20px'}),
  ui.Label('Explore landcover change over time by selecting different years and comparing side-by-side. Zoom in and out to explore regions of interest.')
]);
leftMap.add(intro);

var createDropdown = function(map, labelText, defaultValue) {
  var yearLabel = ui.Label(labelText);
  var yearSelect = ui.Select({
    items: years.getInfo(),
    value: defaultValue,
    onChange: function(year) {
      var selectedImage = landcoverCol.filter(ee.Filter.eq('year', parseInt(year))).first();
      map.layers().set(0, ui.Map.Layer(selectedImage, visParams, 'Landcover ' + year));
    }
  });
  var panel = ui.Panel([yearLabel, yearSelect]);
  map.add(panel);
  return yearSelect;
};

var leftYearSelect = createDropdown(leftMap, 'Select Left Year:', '1985');
var rightYearSelect = createDropdown(rightMap, 'Select Right Year:', '2022');

leftMap.centerObject(landcoverCol.first().geometry(), 3);
```

### 3. Calculating and Exporting Landcover Statistics

A crucial step for any analysis is to calculate the area covered by each landcover class over time and export the data for further analysis. Here, we will use the zonal statistics approach to compute the area of each class for the entire time series. We will create a table with landcover class and year-wise area statistics and export it as a CSV file.

Here's the Earth Engine code to achieve this. You can find the [full code here](https://code.earthengine.google.co.in/0cf53210dbad828ca49dc837d2c1d47e)

```javascript
// Function to calculate area of each class
var calculateArea = function(image) {
  var areaImage = ee.Image.pixelArea().divide(10000).addBands(image);
  var areas = areaImage.reduceRegion({
    reducer: ee.Reducer.sum().group({
      groupField: 1,
      groupName: 'class'
    }),
    geometry: geometry,
    scale: 30,
    maxPixels: 1e10
  });
  return ee.Feature(null, areas);
};

// Apply the function on the ImageCollection
var areasCol = landcoverCol.map(calculateArea);

// Flatten the collection to create a single FeatureCollection
var features = areasCol.map(function(feature) {
  var dict = ee.Dictionary(feature.get('groups')).map(function(key, value) {
    return ee.Number(value).get(0);
  });
  return ee.Feature(null, dict);
});

// Export the data
Export.table.toDrive({
  collection: features,
  description: 'LandcoverAreaStatistics',
  fileFormat: 'CSV'
});
```

### Conclusion

The GLC_FCS30D dataset opens up new avenues for detailed and high-resolution landcover analysis. This tutorial demonstrated how to preprocess, visualize, and analyze the dataset within Google Earth Engine, providing a robust starting point for further exploration and research.

Keywords: GLC_FCS30D, Preprocessing, Mosaicking, Reclassification, Visualization, Split-panel App, Interactive Map, Legend, Land Cover Statistics, Zonal Statistics, Area Calculation, CSV Export
