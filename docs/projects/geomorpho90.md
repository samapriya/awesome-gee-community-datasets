# Geomorpho90m Geomorphometric Layers

Topographical relief comprises the vertical and horizontal variations of the Earth’s terrain and drives processes in geomorphology, biogeography, climatology, hydrology and ecology. Its characterisation and assessment, through geomorphometry and feature extraction, is fundamental to numerous environmental modelling and simulation analyses. We, therefore, developed the Geomorpho90m global dataset comprising of different geomorphometric features derived from the MERIT-Digital Elevation Model (DEM) - the best global, high-resolution DEM available. The fully-standardised 26 geomorphometric variables consist of layers that describe the (i) rate of change across the elevation gradient, using first and second derivatives, (ii) ruggedness, and (iii) geomorphological forms. The Geomorpho90m variables are available at 3 (~90 m) and 7.5 arc-second (~250 m) resolutions under the WGS84 geodetic datum, and 100 m spatial resolution under the Equi7 projection. They are useful for modelling applications in fields such as geomorphology, geology, hydrology, ecology and biogeography.

Geomorpho90m is a set of geomorphometric variables derived from MERIT-DEM. The are available at 3 resolutions the ingested ones are the 3 arc-second (~90m) resolution.The layers can be downloaded from [OpenTopography](https://portal.opentopography.org/dataspace/dataset?opentopoID=OTDS.012020.4326.1) or from [Google Drive](https://drive.google.com/drive/folders/1D4YHUycBBhNFVVsz4ohaJI7QXV9BEh94).

Read about the [methodology here](https://www.nature.com/articles/s41597-020-0479-6)

![geomorph90](https://user-images.githubusercontent.com/6677629/113523325-deafc580-956c-11eb-8dfd-1bf69ee7e216.gif)

Use the following credit when these datasets are cited:

```
Amatulli, Giuseppe, Daniel McInerney, Tushar Sethi, Peter Strobl, and Sami Domisch. "Geomorpho90m, empirical evaluation and accuracy assessment of global high-resolution geomorphometric layers." Scientific Data 7, no. 1 (2020): 1-18.
```

#### Earth Engine Snippet

#### Geomorphological forms

```js
var geom = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/geom");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:geophysical-biological-biogeochemical/GEOMORPHO90-GEOMORPHOLOGICAL-FORMS

#### First order derivatives

```js
var slope = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/slope");
var aspect = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/aspect");
var aspect_cosine = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/aspect-cosine");
var aspect_sine = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/aspect-sine");
var eastness = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/eastness");
var northness = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/northness");
var convergence = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/convergence");
var spi = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/spi");
var cti = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/cti");
var dx = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/dx");
var dy = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/dy");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:geophysical-biological-biogeochemical/GEOMORPHO90-FIRST-ORDER-DERIVATIVE

#### Second order derivatives

```js
var dxx = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/dxx");
var dxy = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/dxy");
var dyy = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/dyy");
var pcurv = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/pcurv");
var tcurv = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/tcurv");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:geophysical-biological-biogeochemical/GEOMORPHO90-SECOND-ORDER-DERIVATIVE


#### Ruggedeness

```js
var elev_stdev = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/elev-stdev")
var vrm = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/vrm");
var roughness = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/roughness");
var tri = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/tri");
var tpi = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/tpi");
var dev_magnitude = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/dev-magnitude");
var dev_scale = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/dev-scale");
var rough_magnitude = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/rough-magnitude");
var rough_scale = ee.ImageCollection("projects/sat-io/open-datasets/Geomorpho90m/rough-scale");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:geophysical-biological-biogeochemical/GEOMORPHO90-RUGGEDENESS


#### License

This work is licensed under a Creative Commons Attribution 4.0. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Curated by: Samapriya Roy

Keywords: Geomorpho90m, geomorphometric layers, MERIT DEM, topographic index, terrain ruggedness index, slope

Last updated: 2023-04-04
