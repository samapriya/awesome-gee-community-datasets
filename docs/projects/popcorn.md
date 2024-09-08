# POPCORN Scalable Population Mapping with Sentinel-1 & Sentinel-2

Popcorn (POPulation from COaRrse census Numbers) is a population mapping method designed to address the challenges of generating accurate population maps, especially in data-scarce regions. By using only free, globally available satellite imagery from Sentinel-1 and Sentinel-2, along with a small number of aggregate census counts, Popcorn surpasses the accuracy of many traditional population mapping approaches that rely on high-resolution building footprints. For example, Popcorn produced 100m resolution population maps for Rwanda with fewer than 400 regional census counts, achieving an accuracy score of 66% in Kigali with an average error of just 10 inhabitants per hectare.

Popcorn's method retrieves explicit maps of built-up areas and local building occupancy rates, providing additional insights into the distribution of unpopulated built-up areas, such as industrial warehouses. This makes the method interpretable and practical for urban planning and humanitarian efforts. Popcorn aims to democratize access to high-resolution population maps, making them available to regions without the resources for extensive census campaigns. You can find the full [paper here](https://www.sciencedirect.com/science/article/pii/S0034425724004097) and find a lot more information about the model and files here on [Popcorn Population Mapping Project page](https://popcorn-population.github.io/)

#### Data Characteristics

| **Category**           | **Details**                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| **Data Inputs**         | - Satellite imagery from Sentinel-1 and Sentinel-2                           |
|                        | - Coarse regional population counts                                          |
| **Key Features**        | - 100m ground sampling distance (GSD)                                        |
|                        | - Built-up area and building occupancy rate maps                             |
|                        | - Scalable and timely mapping for urban planning and humanitarian use         |
| **Example Use Case**    | - Rwanda population mapping: 66% accuracy in Kigali with minimal census data |

#### Citation

```
Metzger, Nando, Rodrigo Caye Daudt, Devis Tuia, and Konrad Schindler. "High-resolution population maps derived from Sentinel-1 and Sentinel-2."
Remote Sensing of Environment 314 (2024): 114383.
```

![popcorn_popdensity](https://github.com/user-attachments/assets/9c33f411-8228-42f1-81c2-f26843779517)

#### Earth Engine Snippet

```js

var snazzy = require("users/aazuspan/snazzy:styles");
snazzy.addStyle("https://snazzymaps.com/style/15/subtle-grayscale", "Greyscale");


// load the population density
var popDensity = ee.Image("projects/sat-io/open-datasets/POPCORN/POPCORNv1");

// Define the inferno color palette
var infernoPalette = [
  '#000004', '#1b0c41', '#4a0c6b', '#781c81', '#a52c7a', '#cf4446',
  '#ed721c', '#fb9b06', '#f7d03c', '#fcffa4'
];

// Define visualization parameters.
var visParams = {
  min: 0,
  max: 4,
  palette: infernoPalette,
  opacity: 0.8 // 70% transparent
};


// Mask out the lowest values (e.g., less than a certain threshold)
var threshold = 0.08;
var maskedPopDensity = popDensity.updateMask(popDensity.gt(threshold));

// Add the masked population density layer to the map.
Map.addLayer(maskedPopDensity, visParams, 'Population Density');

// Create a legend
var legend = ui.Panel({
  style: {
    position: 'bottom-right',
    padding: '8px 15px',
  }
});

// Create legend title
var legendTitle1 = ui.Label({
  value: 'POPCORN',
  style: {
    fontWeight: 'bold',
    fontSize: '32px',
    margin: '0 0 4px 0',
    padding: '0'
    }
});

legend.add(legendTitle1);

// Create another legend title
var legendTitle2 = ui.Label({
  value: 'Population Density [People/ha]',
  style: {
    fontWeight: 'bold',
    fontSize: '18px',
    margin: '0 0 4px 0',
    padding: '0'
    }
});

legend.add(legendTitle2);

// Create a continuous color legend
var legendImage = ui.Thumbnail({
  image: ee.Image.pixelLonLat().select(0),
  params: {
    bbox: [0, 0, 1, 0.1],
    dimensions: '300x15',
    format: 'png',
    min: 0,
    max: 1,
    palette: infernoPalette,
  },
  style: { margin: '0 0 4px 0' },
});

legend.add(legendImage);

// Create labels for min and max values
var minLabel = ui.Label(visParams.min.toString(), { margin: '0 269px 4px 0' });
var maxLabel = ui.Label(visParams.max.toString(), { margin: '0 0 4px 0' });

// Add labels to the legend
var labelsPanel = ui.Panel([minLabel, maxLabel], ui.Panel.Layout.flow('horizontal'));
legend.add(labelsPanel);
Map.setControlVisibility({all: false});

// Add the legend to the map
Map.add(legend);

// Center map for the rwanda/DRC boarder scene
Map.setCenter(29.244453536522037, -1.6857641047022471, 13); // The third parameter is the zoom level.

```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/POPCORN-POPULATION-DENSITY

Earth Engine App: https://ee-nandometzger.projects.earthengine.app/view/popcornv1-rwa

#### License
Creative Commons Attribution 4.0 International (CC-BY-4.0)

Keywords: population mapping, developing countries, population density, humanitarian actions, machine learning models

Provided by: Metzger et al 2024

Curated in GEE by: Metzger et al 2024 and Samapriya Roy

Last updated: 2024-09-08
