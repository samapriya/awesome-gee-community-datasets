# Using the Global Shoreline Dataset to Create Land and Ocean Masks with Google Earth Engine (GEE)

<p style="text-align: right;">
by <a href="mailto:ujaval@spatialthoughts.com">Ujaval Gandhi</a> from <a href="https://spatialthoughts.com/">Spatial Thoughts</a>
</p>

### Introduction

The Global Shoreline dataset, hosted on the [Gee-Community Catalog](https://gee-community-catalog.org/projects/shoreline/), is a valuable resource for creating land and ocean masks in Google Earth Engine (GEE). This tutorial provides an overview of how to use this dataset to generate these masks, which can be useful for various geospatial analyses and applications. The complete code [can be found here](https://code.earthengine.google.co.in/a5cbf2f9d14a545efef050b80e5182d9)

### Dataset Description

The Global Shoreline dataset comprises three sets of polygon features:

1. Mainland coastlines from continents around the world.
2. Large island chains (with an area greater than n5,000 square kilometers).
3. Smaller islands not included in either set.

### Getting Started with GEE and Shoreline Dataset


To begin working with this dataset on Google Earth Engine, first import the necessary collections:

```javascript
// Importing Global Shoreline Dataset Collections
var mainlands  ee.FeatureCollection('projects/sat-io/open-datasets/shoreline/mainlands');
var big_islands  ee.FeatureCollection('projects/sat-io/open-datasets/shoreline/big_islands');
var small_islands  ee.FeatureCollection('projects/sat-io/open-datasets/shoreline/small_islands');
```

### Merging Collections and Rasterizing Polygons


The next step is to merge the individual collections into a single collection, which can then be rasterized:

```javascript
// Merge all collections
var merged  mainlands.merge(big_islands).merge(small_islands);

// Rasterize polygons using 'ee.Reducer.count()' to get land pixel counts
var mask  merged.reduceToImage({
  reducer: ee.Reducer.count(),
});
```

### Visualizing Land and Ocean Areas


The rasterized image can now be visualized on the map using different color palettes - brown for land (with higher pixel counts) and blue for ocean:

```javascript
// Add mask as a layer to display land areas in brown
Map.addLayer(mask, {min: 0, max: 1}, 'Land Mask');

// Create an inverted version of the mask to visualize ocean areas in blue
var invertMask  mask.multiply(-1);
Map.addLayer(invertMask, {min: -1, max: 0}, 'Ocean Mask');
```

### Creating Land and Ocean Masks for Further Processing


The rasterized image can be used to create separate land and ocean masks for further processing within GEE:

```javascript
// Create an ocean mask using '.selfMask()' on the inverted version of 'mask'
var oceanMask  invertMask.updateMask(invertMask);

// Use 'image.updateMask(oceanMask)' to remove ocean pixels from another image

// Create a land mask by inverting 'oceanMask' and using '.selfMask()'
var landMask  oceanMask.not().updateMask(oceanMask);

// Use 'image.updateMask(landMask)' to remove land pixels from another image
```

### Conclusion

This tutorial demonstrates how to use the Global Shoreline dataset in Google Earth Engine to create rasterized masks representing land and ocean areas, which can be visualized
on a map or used for further processing. This approach provides a valuable resource for various geospatial analyses and applications.

Keywords: GEE, Global Shoreline Dataset, Land Mask, Ocean Mask, Rasterization, Shoreline,  Landcover,  Image Processing
