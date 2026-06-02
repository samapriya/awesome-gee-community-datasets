# NAIP-CHM 0.6-meter Resolution Canopy Height Model for CONUS

!!! note "Preprint Notice"
    This dataset is associated with a **non-peer-reviewed preprint** submitted to bioRxiv (December 12, 2025; updated April 29, 2026). The methodology and results have not yet undergone formal peer review. Users are encouraged to review the [preprint](https://doi.org/10.64898/2025.12.12.694075) directly and exercise appropriate caution when citing or applying this dataset in research.

Above-ground vertical structure is a critical variable for ecosystem monitoring, carbon accounting, wildfire modeling, and land management. To address the high cost and limited coverage of airborne lidar, the [Numerical Terradynamic Simulation Group (NTSG)](https://www.ntsg.umt.edu) at the University of Montana developed **NAIP-CHM** — a 0.6-meter resolution canopy height and structure model (CHM) covering the **contiguous United States (CONUS)**. Functionally acting as a normalized Digital Surface Model (nDSM), the dataset characterizes the full vertical structure of the landscape — including vegetation, buildings, and infrastructure — rather than masking human-made features as forestry-specific products do. This design makes NAIP-CHM uniquely suited for applications in the wildland-urban interface, rangeland management, and open-canopy ecosystems where existing products have historically struggled.

The model was built from NAIP 4-band aerial imagery (2012–2023, with 96% acquired in 2022–2023) using a U-Net convolutional neural network enhanced with Convolutional Block Attention Modules (CBAM) and Feature-wise Linear Modulation (FiLM) conditioning. Training used a peer-reviewed, publicly available dataset of over 22.8 million co-registered NAIP and lidar-derived CHM pairs stratified by EPA Level III ecoregion and NLCD land cover class — with grassland and shrubland classes intentionally oversampled to improve performance in open-canopy environments. The model achieved an overall pixel-wise **RMSE of 2.28 m and r² of 0.87** on an independent test set of 2.27 million tiles. Read the [preprint here](https://doi.org/10.64898/2025.12.12.694075).

#### Data Scaling

Pixel values are stored as **scaled unsigned 16-bit integers (uint16)** to optimize storage. Divide raw values by **100** to obtain canopy height in meters. The valid range is 0–120 m; nodata is encoded as 65535.

| Stored Value | True Height |
|-------------|------------|
| 0 | 0.00 m |
| 100 | 1.00 m |
| 1500 | 15.00 m |
| 65535 | No data |

#### Dataset Coverage & Design

**Spatial coverage:** Contiguous United States (CONUS), excluding the Nevada Test and Training Range (southern Nevada) where NAIP imagery is restricted.

**Spatial resolution:** 0.6 m (nominal), matching the ground sampling distance of NAIP imagery. Each 432×432-pixel inference chip covers a 256×256 m physical footprint.

**Imagery source:** NAIP 4-band (R, G, B, NIR) orthoimagery acquired 2012–2023 (96% from 2022–2023). NAIP is collected during the growing season (leaf-on conditions) at a 1–3 year return interval per state.

**Total dataset size:** ~24.82 TB; 213,567 NAIP DOQQs processed covering approximately 7.7 million km².

Unlike many canopy height products that mask infrastructure to support carbon-only workflows, NAIP-CHM captures **all elevated features** — trees, shrubs, buildings, power lines, and other structures. Users requiring vegetation-only heights should apply an appropriate mask (e.g., NLCD land cover).

#### Citation

```
Morford, S. L., Allred, B. W., Coons, S. P., Marcozzi, A. A., McCord, S. E., Smith, J. T.,
& Naugle, D. E. (2025). A 0.6-meter resolution canopy height model for the contiguous
United States. bioRxiv. https://doi.org/10.64898/2025.12.12.694075
```

![naip_chm](../images/naip_chm_conus.png)

#### Earth Engine Snippet

```js
var chm = ee.ImageCollection("projects/naip-chm/assets/conus-structure-model");
var naip = ee.ImageCollection("USDA/NAIP/DOQQ");

chm = chm.map(function(img) {
  var rescaled = img.divide(100)
  return img.select([]).addBands(rescaled).rename(['chm_meters'])
})

naip = naip.filterDate('2012','2024').sort('system:time_start',true)
Map.addLayer(naip,{}, 'naip source', false)

var viridis = [
  '#440154', // deep purple
  '#482777',
  '#3f4a8a',
  '#31688e',
  '#26828e',
  '#1f9e89',
  '#35b779',
  '#6ece58',
  '#fde725'  // bright yellow
];

Map.addLayer(chm.mosaic(), {min:0, max: 15, palette: viridis}, 'chm_meters',true)
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/NAIP-CHM-CONUS

Interactive Explorer: https://naip-chm.projects.earthengine.app/view/naip-chm-a-conus-structure-model

#### License & Usage

This dataset is licensed under **Creative Commons Attribution 4.0 International (CC-BY 4.0)**. You are free to copy, redistribute, and build upon the material for any purpose, including commercially, provided you give appropriate credit, provide a link to the license, and indicate if changes were made.

Created by: Morford et al 2026

Curated in GEE by: Samapriya Roy

Keywords: Canopy Height, CHM, NAIP, CONUS, U-Net, Deep Learning, CBAM, FiLM, Lidar, Vegetation Structure, Wildfire, Rangeland, Open-Canopy, nDSM, Land Management

Last updated: 2026-06-02
