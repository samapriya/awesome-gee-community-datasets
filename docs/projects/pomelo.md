# POMELO Model Population Density Maps

POMELO is a deep learning model addressing the need for fine-grained population maps in urban planning, environmental monitoring, public health, and humanitarian operations. It uses coarse census data and open geospatial data to create high-resolution population maps with a 100-meter ground sampling distance. POMELO can estimate populations even in regions lacking census data, achieving accuracy in sub-Saharan Africa experiments. It evaluates performance in three scenarios: coarse supervision, fine supervision, and transfer tasks, highlighting the practicality of fine supervision. POMELO estimates building occupancy rates and computes populations by multiplying them with building counts. It relies on free sources like the Open Buildings dataset but acknowledges potential errors. Dependence on high-resolution images and data availability is a concern. Crowdsourced data is essential in data-scarce regions. POMELO uses various geospatial data layers, with nightlight and settlement layers being predictive. Future improvements may include additional covariates from open geospatial sources, but handling incomplete and biased data remains a challenge. This dataset presents a fine-grained population map of Tanzania, Mozambique, Uganda, Zambia, and Rwanda with a resolution of 100 meters for 2020, generated using the POMELO super-resolution technique that is based on deep learning. Please refer to our [Nature Scientific Reports publication](https://www.nature.com/articles/s41598-022-24495-w) for more details. Each pixel contains a floating point number specifying the number of inhabitants of the respective pixel (i.e. People/100m).

Traditionally, many countries, including those in sub-Saharan Africa, rely on aggregated census data over expansive spatial units, which are not always timely or accurate. The need for detailed population maps is paramount in several sectors, including urban development, environmental supervision, public health, and humanitarian initiatives. Addressing this gap, the POMELO methodology leverages coarse census data in conjunction with open geodata to produce high precision population maps.

#### Key Features
- Resolution: The map offers a granular view with a 100m ground sampling distance, providing intricate details about population distributions in Rwanda.
- Data Sources: Utilizing a combination of projected admisistrative census data (UN), and supplementing it with open geodata.
- Reliability: In comparative experiments conducted in sub-Saharan Africa, POMELO's ability to disaggregate coarse census counts achieved R2 values of 85-89%. Furthermore, its potential to predict population numbers without any census data reached accuracy levels of 48-69%.

#### Citation

```
Metzger, Nando, John E. Vargas-Muñoz, Rodrigo C. Daudt, Benjamin Kellenberger, Thao Ton-That Whelan, Ferda Ofli, Muhammad Imran, Konrad Schindler,
and Devis Tuia. "Fine-grained population mapping from coarse census counts and open geodata." Scientific Reports 12, no. 1 (2022): 20085.
```

![pomelo_small](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/41cc1651-327b-4aee-84f5-75f630cf5a00)

### Earth Engine Snippet

```js
// load the population density
var popDensity = ee.Image("projects/sat-io/open-datasets/POMELO/POMELOv1");

// Define the inferno color palette
var infernoPalette = [
  '#000004', '#1b0c41', '#4a0c6b', '#781c81', '#a52c7a', '#cf4446',
  '#ed721c', '#fb9b06', '#f7d03c', '#fcffa4'
];

// Define visualization parameters.
var visParams = {
  min: 0,
  max: 450,
  palette: infernoPalette,
  opacity: 0.7 // 70% transparent
};

// Add the population density layer to the map.
Map.addLayer(popDensity, visParams, 'Population Density');

// Center map
Map.setCenter(39.2026, -6.1659, 12);
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/POMELO-POP-DENSITY

#### License
Creative Commons Attribution 4.0 International (CC-BY-4.0)

Keywords: population mapping, developing countires, population density, humanitarian actions

Provided by: Metzger et al 2022

Curated in GEE by: Metzger et al 2022 and Samapriya Roy
