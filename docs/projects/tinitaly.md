# TINITALY: High-Resolution Digital Elevation Model of Italy

TINITALY is a high-resolution Digital Elevation Model (DEM) covering the entire Italian territory with a native grid resolution of 10 meters. Developed by the Istituto Nazionale di Geofisica e Vulcanologia (INGV), the DEM is derived from a Triangular Irregular Network (TIN) constructed using heterogeneous elevation data sources, including regional  topographic maps, GPS points, and radar altimetry data. The TIN structure is enhanced using the DEST algorithm, which improves input data by evaluating inferred break-lines,  resulting in a seamless and accurate representation of Italy's terrain. TINITALY is particularly valuable for applications in geomorphology, geology, environmental studies, and  hazard assessment. Additional information can be [found here](https://tinitaly.pi.ingv.it/)

#### Dataset Details

- **Name**: TINITALY
- **Provider**: Istituto Nazionale di Geofisica e Vulcanologia (INGV)
- **Resolution**: 10 meters
- **Coverage**: Entire Italian territory
- **Vertical Accuracy (RMSE)**: <3.5 meters
- **No Data Value**: -9999
- **License**: Creative Commons Attribution 4.0 International (CC BY 4.0)

#### Notes

- TINITALY provides a seamless and high-resolution representation of Italy's terrain, making it suitable for various geospatial analyses.
- The dataset is generated using the DEST algorithm, which enhances the TIN structure by evaluating inferred break-lines, resulting in improved accuracy.
- TINITALY has been compared to global DEMs such as SRTM and ASTER, demonstrating superior resolution and lower error margins.

#### Citation

```
Tarquini, S., Isola, I., Favalli, M., Battistini, A., Dotta, G. (2023). TINITALY, a digital elevation model of Italy with a 10 meters cell size (Version 1.1) [Data set].
Istituto Nazionale di Geofisica e Vulcanologia (INGV). https://doi.org/10.13127/tinitaly/1.1

Tarquini S., I. Isola, M. Favalli, F. Mazzarini, M. Bisson, M.T. Pareschi, E. Boschi (2007). TINITALY/01: a new triangular irregular network of Italy. Annals of Geophysics. https://doi.org/10.4401/ag-4424
```

![tinitaly](https://github.com/user-attachments/assets/8eb18873-085a-47e8-b231-72ffe2acafa8)

#### Earth Engine Snippet

```javascript
var Tinitaly_DTM = ee.ImageCollection("projects/sat-io/open-datasets/Tinitaly_DTM");
print(Tinitaly_DTM);
```

Sample Script: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:elevation-bathymetry/TINITALY-DTM-10m

Keywords: Italy, Digital Elevation Model, DEM, Topography, Geomorphology, Hazard Assessment

#### License
The datasets are distributed under a Attribution 4.0 International (CC BY 4.0) license.

Produced by : Istituto Nazionale di Geofisica e Vulcanologia

Curated in GEE by : Istituto Nazionale di Geofisica e Vulcanologia & Samapriya Roy

Last updated on GEE: 2025-04-12
