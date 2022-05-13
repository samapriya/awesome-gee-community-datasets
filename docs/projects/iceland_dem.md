# ÍslandsDEM v1.0 10m

Since 2015, elevation data from the Arctic (north of 60°N, including Iceland) started to be openly available through the ArcticDEM project, led by the Polar Geospatial Center, University of Minnesota (https://www.pgc.umn.edu/data/arcticdem/).

This data consists of a large amount of Digital Elevation Models (DEMs) repeatedly acquired (multitemporal), typically from 2012-present, and the oldest data reaching back to 2008. The DEMs are derived from satellite sub-meter stereo imagery, particularly from WorldView 1-3 and GeoEye-1. The processing of the DEMs was done using SETSM, an open-source digital photogrammetric software, in the Bluewaters supercomputer (University of Ilinois). Each DEM has 2x2m resolution and a footprint of ~18x100km.

In a collaborative effort between the National Land Survey of Iceland, the Icelandic Meteorological Office and the Polar Geospatial Center, we developed methods to handle and process a large amount of data available for Iceland. The methods developed consisted of

* Spatial adjustment of all the available DEMs, for homogeneity and consistency in the location of each individual DEM.

* Robust mosaicking into one single DEM of Iceland, by taking advantage of the multi-temporal coverage of DEMs. Each pixel of the mosaic corresponds to a median elevation value from the possible elevations available from the ArcticDEM. More details on the dataset [available here](https://gatt.lmi.is/geonetwork/srv/eng/catalog.search#/metadata/e6712430-a63c-4ae5-9158-c89d16da6361). This DEM is resampled for 10x10m resolution.


![iceland_dem](https://user-images.githubusercontent.com/6677629/168207259-0ecfd923-91be-43ae-8747-7064e48b09d0.gif)


#### Earth Engine Snippet

```js
var DEM_10m_isn93 = ee.Image("projects/ee-landmaelingar/assets/IslandsDEMv1_10m_isn93")
```

Projection used: EPSG 3057 (ISN93/Lambert 1993)

Sample Code: https://code.earthengine.google.com/34517ab5c05be78e5f7d9227a4ca7b7e


#### License
The datasets are distributed under a Attribution 4.0 International (CC BY 4.0) license.

Produced by : National Land Survey of Iceland & PGC

Curated in GEE by : National Land Survey of Iceland

Keywords: : Elevation, DEM, ArticDEM, Iceland, Geophysical

Last updated on GEE: 2022-03-29
