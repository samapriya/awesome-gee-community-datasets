# Global Soil Organic Carbon Map (GSOCmap)

The Global Soil Organic Carbon Map (GSOCmap) is the first global soil organic carbon stock map created through a participatory, country-driven approach. Developed by the FAO's Global Soil Partnership, this dataset represents a collaborative effort to compile and harmonize national soil data, providing the best available estimate of Soil Organic Carbon (SOC) stocks at the country level for the top 30 cm of soil.

The GSOCmap v1.5 is a comprehensive global dataset estimating SOC stocks at a 30 arc-second resolution (~1 km). It was produced by compiling national SOC maps submitted by member countries, supplemented by joint mapping efforts and gap-filling for regions without data. The map is based on over one million sampling points and represents a significant step towards building a global soil information system. The total global SOC stock for the 0-30 cm depth is estimated to be 694 Petagrams. The dataset includes both the mean SOC stock prediction and an associated uncertainty layer represented by the standard deviation.

#### Dataset Characteristics

| Parameter | Value |
|-----------|-------|
| Spatial Resolution | ~1 km (30 arc-seconds) |
| Coverage | Global |
| Depth | 0-30 cm |
| Total SOC Stock | 694 Pg C |
| Units | tonnes/hectare (t/ha) |
| Validation Performance | Index of Agreement (IOA) = 0.50, Mean Gross Error = 35.07 t/ha |

#### Available Layers

The collection includes the mean SOC stock and the standard deviation as a measure of uncertainty.

| Asset Name           | Description                                         | Bands                                  | Units          |
| -------------------- | --------------------------------------------------- | -------------------------------------- | -------------- |
| `GSOCmap_T_PER_HA`       | Soil Organic Carbon (SOC) stock and associated uncertainty | `soc_mean` (SOC stock) | t/ha           |

**Note**: The map is a compilation of data from various national sources, which may lead to discontinuities at country borders.

#### Citation
FAO and ITPS. 2020. Global Soil Organic Carbon Map V1.5: Technical Report. Rome, FAO. https://doi.org/10.4060/ca7597en

#### Dataset Citation
Food and Agriculture Organization of the United Nations (FAO). 2020. Global Soil Organic Carbon Map (GSOCmap) v1.5.0.

![gsocmap](../images/gsoc.gif)


#### Earth Engine Snippet

```javascript
// Load the specific GSOCmap image asset you are using.
var gsoc = ee.Image("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/FAO/GSOCMAP1-5-0");

// Select the first band 'b1' and rename it for clarity.
var soc_mean = gsoc.select('b1').rename('soc_mean');

// Visualization parameters for SOC stock.
var socVis = {
  min: 0,
  max: 100,
  palette: ['#d7f3fe', '#83d4f6', '#34a0dc', '#24709a', '#0a425f', '#fef19c', '#fec978', '#fd9b57', '#f26838', '#d53521', '#a91b18']
};

// Center the map and add the SOC stock layer.
// The layer for uncertainty has been removed.
Map.setCenter(0, 20, 3);
Map.addLayer(soc_mean, socVis, 'Soil Organic Carbon Stock (t/ha)');

// --- Create and add a legend to the map ---

// Create a panel to hold the legend.
var legend = ui.Panel({
  style: {
    position: 'bottom-left',
    padding: '8px 15px'
  }
});

// Create the legend title.
var legendTitle = ui.Label({
  value: 'SOC Stock (t/ha)',
  style: {
    fontWeight: 'bold',
    fontSize: '18px',
    margin: '0 0 4px 0',
    padding: '0'
  }
});
legend.add(legendTitle);

// Function to create a legend row (color box + label).
var makeRow = function(color, name) {
  var colorBox = ui.Label({
    style: {
      backgroundColor: color,
      padding: '8px',
      margin: '0 0 4px 0',
      border: '1px solid black'
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

// Get the palette and labels for the legend.
var palette = socVis.palette;
var names = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80-90', '90-100', '>100'];

// Add each row to the legend.
for (var i = 0; i < 11; i++) {
  legend.add(makeRow(palette[i], names[i]));
}

// Add the legend to the map.
Map.add(legend);
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:geophysical-biological-biogeochemical/GSOC-MAP

#### License
This work is made available under the Creative Commons Attribution-NonCommercial ShareAlike licence.

Provided by: Food and Agriculture Organization of the United Nations (FAO), Global Soil Partnership (GSP)

Curated in GEE by: Samapriya Roy

Keywords: Soil Organic Carbon, SOC, Carbon Stock, Soil Mapping, FAO, Global Soil Partnership, Country-driven

Last updated: 2025-08-06
