# Exploring Dynamic Surface Water Extent (DSWE)

<p style="text-align: right;">
USGS contacts: <a href="mailto:csoulard@usgs.gov">Chris Soulard</a>,
<a href="mailto:jjwalker@usgs.gov">Jessica Walker</a> from
<a href="https://www.usgs.gov">US Geological Survey (USGS)</a>
</p>

Understanding surface water dynamics is crucial for effective water resource management, flood mapping, ecological research, and climate change analysis. The **Dynamic Surface Water Extent (DSWE)** dataset provides reliable, repeatable, and consistent maps of water presence derived from Landsat imagery. Originally introduced by Jones (2015), DSWE has been continuously improved and now leverages the power of Google Earth Engine (GEE) to deliver monthly surface water composites. Details on the code outputs can be found at the [USGS Official Source Code Archive](https://code.usgs.gov/place/dswe).

In this tutorial, we will:

- Access and preprocess Landsat imagery to generate DSWE layers.
- Understand DSWE categorization and confidence levels.
- Visualize monthly DSWE composites.
- Export the data for further analysis.

#### Citation

```
Walker JJ, Waller EK, Kreitler JR, Petrakis RE, Soulard CE. (2025). DSWE_GEE v2.0.0 Software release. U.S. Geological Survey. DOI: https://doi.org/10.5066/P14CF2B2.

Landsat DSWE Google Earth Engine code originally developed for this paper:

Walker, J.J., Soulard, C.E. and Petrakis, R.E., 2020. Integrating stream gage data and Landsat imagery to complete time-series of surface water extents in Central Valley, California. International Journal of Applied Earth Observation and Geoinformation, 84, p.101973.

MODIS DSWE Google Earth Engine code originally developed for this paper:

Soulard, C.E., Waller, E.K., Walker, J.J., Petrakis, R.E. and Smith, B.W., 2022. DSWEmod—The production of high‐frequency surface water map composites from daily MODIS images. JAWRA Journal of the American Water Resources Association, 58(2), pp.248-268.
```



## Tutorial Outline

#### 1. Accessing and Preparing Landsat Data

DSWE analysis uses Landsat satellite imagery collections, specifically Landsat 4 through Landsat 9, spanning from 1982 to the present. Before applying DSWE methods, imagery must be preprocessed for consistent reflectance and free from cloud contamination.

#### Steps:

- Define your area of interest (AOI) and date range.
- Load Landsat Collection 2 imagery.
- Apply scaling and cloud masking.
- Calculate terrain and solar geometry indices (e.g., hillshade).

Here's the Earth Engine JavaScript code snippet to access and preprocess data:

```javascript
// Define your date range (within Landsat availability)
var startdate = ee.Date('2000-08-01');
var enddate = ee.Date('2000-10-31');

// Define your AOI (user-defined polygon or drawn geometry)
var aoi = ee.Geometry.Polygon([
   [-113.285, 40.423],
   [-111.318, 40.423],
   [-111.318, 41.952],
   [-113.285, 41.952],
   [-113.285, 40.423]
]);

// Load and preprocess Landsat collections (example for Landsat 8)
var ls8 = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2')
            .filterBounds(aoi)
            .filterDate(startdate, enddate)
            .map(function(img) {
              var scaled = img.select('SR_B.*').multiply(0.0000275).add(-0.2);
              var qaMask = img.select('QA_PIXEL').bitwiseAnd(parseInt('111101', 2)).neq(0);
              return scaled.updateMask(qaMask);
            });

// Merge multiple collections (if using multiple Landsat sensors)
```

### 2. Generating the DSWE Layer

The DSWE algorithm categorizes surface water presence into classes based on multiple spectral indices and bitwise logical tests derived from Landsat bands. The output is a categorical layer indicating different confidence levels of surface water presence.

#### DSWE Categories:

- `0` - Not water
- `1` - High-confidence water
- `2` - Moderate-confidence water
- `3` - Partial surface water pixel
- `4` - Low-confidence water or wetland
- `9` - Cloud, cloud shadow, or snow

Here's how the categorization is performed in GEE:

```javascript
// DSWE indices calculation (e.g., MNDWI, NDVI, AWEsh)
var calculateIndices = function(img) {
    var ndvi = img.normalizedDifference(['SR_B5', 'SR_B4']).rename('ndvi');
    var mndwi = img.normalizedDifference(['SR_B3', 'SR_B6']).rename('mndwi');
    return img.addBands([ndvi, mndwi]);
};

var indexedCollection = ls8.map(calculateIndices);

// Apply DSWE decision logic (simplified example)
var dsweLayer = indexedCollection.map(function(img) {
  var water = img.select('mndwi').gt(0.124).rename('dswe');
  return water.set('system:time_start', img.get('system:time_start'));
});
```


#### 3. Creating Monthly DSWE Composites

Monthly composites are useful to provide stable and representative images of surface water extent over time. These composites handle multiple observations and prioritize higher-confidence water pixels.

Here's how you create monthly composites:

```javascript
// Generate monthly composites
var months = ee.List.sequence(0, enddate.difference(startdate, 'month').subtract(1));
var monthlyDSWE = ee.ImageCollection.fromImages(months.map(function(monthOffset) {
  var start = startdate.advance(monthOffset, 'month');
  var end = start.advance(1, 'month');
  var monthly = dsweLayer.filterDate(start, end).max(); // Example using max confidence
  return monthly.set('month', start.format('YYYY-MM'));
}));

print('Monthly DSWE Composites:', monthlyDSWE);
```

#### 4. Visualizing DSWE Layers

Visualizing DSWE layers effectively requires clear symbology to distinguish water confidence classes. Below is an example visualization:

```javascript
// DSWE visualization parameters
var dsweViz = {min:0, max:9, palette:['000000', '002ba1', '6287ec', '77b800', 'c1bdb6', 'ffffff']};

// Add the monthly composite layer to the map
Map.centerObject(aoi, 10);
var sampleMonth = monthlyDSWE.first();
Map.addLayer(sampleMonth, dsweViz, 'Monthly DSWE');
```

![image](https://picsur.spatialbytes.work/i/4947dbfe-3fdd-41dd-b838-366b74e96932.jpg)

#### 5. Exporting DSWE Data

DSWE layers can be exported for further GIS analysis or research applications:

```javascript
Export.image.toDrive({
  image: sampleMonth,
  description: 'DSWE_Monthly_Composite',
  folder: 'EarthEngineExports',
  scale: 30,
  region: aoi,
  crs: 'EPSG:5070',
  maxPixels: 1e13
});
```

Here's the Earth Engine code to achieve this. You can find the [full code here]()

#### Conclusion

The DSWE dataset provides an advanced, consistent, and high-resolution approach for analyzing water dynamics from space. This tutorial guides you through accessing, preprocessing, visualizing, and exporting DSWE data using Google Earth Engine, facilitating practical analysis for water resource management, flood detection, and ecological studies.

**Keywords:** Dynamic Surface Water Extent (DSWE), Landsat, Google Earth Engine, Monthly Composites, Surface Water Mapping, Flood Monitoring, Visualization, GIS, Remote Sensing.



#### License

This project is licensed under the Creative Commons Zero v1.0 Universal.
