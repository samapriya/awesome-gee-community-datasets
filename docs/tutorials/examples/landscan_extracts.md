# Comparing Global Population Trends with GeoBoundaries and Landscan

<p style="text-align: right;">
by <a href="mailto:ujaval@spatialthoughts.com">Ujaval Gandhi</a> from <a href="https://spatialthoughts.com/">Spatial Thoughts</a>
</p>

### Introduction

This tutorial demonstrates how to use GeoBoundaries and the Landscan Population Dataset to compare population data for different Admin1 regions using Earth Engine. You will learn how to load admin boundaries, filter a population dataset by date range, extract resolution information, and create a time-series chart comparing population data.

To view the complete code for this tutorial, click [here](https://code.earthengine.google.com/580fe304e023625748b4f3e0ef34b2cf).

### Section 1: Load Admin Boundaries (GeoBoundaries) and Select Regions

Use the `ee.FeatureCollection` method to load the admin boundaries dataset from GeoBoundaries.

```javascript
var admin0 = ee.FeatureCollection("projects/sat-io/open-datasets/geoboundaries/CGAZ_ADM0");
```

Select two Admin1 regions to compare: Japan and Mexico.

```javascript
var region1 = 'Japan';
var region2 = 'Mexico';
```

Use the `filter` method to select the desired regions from the admin boundaries dataset.

```javascript
var selectedRegions = admin0.filter(ee.Filter.inList('shapeName', [region1, region2]));
print('Filtered Admin1 collection', selectedRegions);
```

### Section 2: Load Landscan Population Dataset

Use the `ee.ImageCollection` method to load the Landscan population dataset.

```javascript
var landscan = ee.ImageCollection("projects/sat-io/open-datasets/ORNL/LANDSCAN_GLOBAL");
var band = 'b1';
```

Set the date range for the population data using `ee.Date.fromYMD`.

```javascript
var startYear = 2000;
var endYear = 2020;

var startDate = ee.Date.fromYMD(startYear, 1, 1);
var endDate = ee.Date.fromYMD(endYear + 1, 1, 1);
```

Use the `filter` method to filter the population dataset by date range.

```javascript
var populationFiltered = landscan.filter(ee.Filter.date(startDate, endDate)).select(band);
print('Filtered Population Collection', populationFiltered);
```
### Section 3: Extract Resolution of Landscan Dataset

Get the resolution of the population dataset using `projection.nominalScale`.

```javascript
var projection = populationFiltered.first().projection();
var resolution = projection.nominalScale();
print('Landscan Global Resolution', resolution);
```

### Section 4: Create Time-Series Chart Comparing Population

Create a time-series chart comparing the population data for the selected regions.

```javascript
var chartOptions = {
    title: 'Population Time Series',
    vAxis: {
        title: 'Population',
      },
      hAxis: {
        title: '',
        format: 'YYYY',
        gridlines: {color: 'transparent'}

      },
  }

var chart = ui.Chart.image.seriesByRegion({
  imageCollection: populationFiltered,
  regions: selectedRegions,
  reducer: ee.Reducer.sum(),
  scale: resolution,
  seriesProperty: 'shapeName'
}).setChartType('ColumnChart')
  .setOptions(chartOptions);
print(chart);
```

Keywords: GeoBoundaries, Landscan Population Dataset, Earth Engine, Admin1 regions, Population data
