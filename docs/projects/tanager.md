# Planet Tanager Open Data

Planet's Tanager Open Data Program provides free hyperspectral satellite imagery captured from the Tanager constellation. The dataset features approximately 426 spectral bands ranging from 380nm to 2500nm with ~5 nm spectral resolution, collected at 30m ground sample distance. The initial release contains over 50 basic radiance scenes covering various land cover features including agricultural areas, energy and mining sites, snow and ice regions, urban areas, natural lands, and coastal zones from across the globe. Find additional information about the [program here](https://www.planet.com/pulse/unleash-the-power-of-hyperspectral-over-50-tanager-radiance-datasets-now-available-on-planet-s/). You can access the [STAC Catalog here](https://www.planet.com/data/stac/browser/tanager-core-imagery/catalog.json?.language=en) and [Tanager Scence docs can be found here](https://docs.planet.com/data/imagery/tanager/item-types/tanagerscene/) & [product specifications here](https://planet.widen.net/s/wq9dsgzvv6/planet-userdocumentation-tanager).

#### Technical Specifications

<center>

| Parameter | Value |
|-----------|-------|
| Spatial Resolution | 30 m (Ground Sample Distance) |
| Spectral Bands | ~426 bands (380-2500 nm) |
| Spectral Resolution | ~5 nm |
| Processing Level | Basic Radiance (TOA) |
| Bit Depth | 32-bit floating point |
| Revisit Rate | 4-5 days (mid-latitude) |
| Swath Width | 18 km |
| Geographic Coverage | Global |
| Radiometric Units | W/(m²·sr·μm) |

</center>

#### Product Description

The Tanager Basic Radiance product (`basic_radiance_hdf5`) provides unorthorectified, top-of-atmosphere radiance calibrated imagery. This product is **georeferenced but not projected to a cartographic projection**, preserving the native sensor geometry. The hyperspectral data covers the full visible to shortwave infrared (VSWIR) spectral range with exceptional spectral fidelity, built on scientific heritage shared with NASA-JPL's EMIT instrument.

#### Spectral Coverage

The Tanager sensor provides comprehensive spectral coverage across multiple regions:

- **Visible (VIS)**: 380-700 nm - Traditional RGB plus extended visible range
- **Near-Infrared (NIR)**: 700-1400 nm - Vegetation health and biomass assessment
- **Shortwave Infrared (SWIR)**: 1400-2500 nm - Mineral identification and moisture content

Band information is preserved in the ingested image property with spectral calibration metadata including center wavelengths and full-width half-maximum (FWHM) for each band.

![tanager_layers](../images/tanager.gif)

#### Code Snippet

```js
var tanager_collection = ee.ImageCollection('projects/sat-io/open-datasets/PLANET/TANAGER_HYPERSPECTRAL');
var vis = {"opacity":1,"bands":["B100","B060","B040"],"min":14.014482498168945,"max":147.4988250732422,"gamma":1};

Map.setCenter(-63.66,-22.19,12)

Map.setOptions('SATELLITE')
Map.addLayer(tanager,vis,'Tanager Sample')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:/global-events-layers/TANAGER-SAMPLE

App Link: https://sat-io.earthengine.app/view/tanager

#### Data Access

**Current Availability**: Only 52 basic radiance scenes available through Planet's Open Data STAC catalog

#### Attribution

Use the following attribution notice for any use of the data:

"Tanager STAC Data, available at www.planet.com/data/stac © [YEAR] Planet Labs PBC. All Rights Reserved."

where [YEAR] must reflect the year the data was captured by the Tanager satellite as indicated in the acquisition metadata.

#### License

This dataset is made available under Creative Commons Attribution 4.0 International License (CC BY 4.0).

Provided by: Planet Labs PBC

Curated in GEE by: Samapriya Roy

Keywords: Hyperspectral, Open data, Tanager, Planet, VSWIR, Radiance, Environmental monitoring

Last updated: 2025-07-23
