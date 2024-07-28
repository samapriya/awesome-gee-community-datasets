# Global 30 m Wetland Map with a Fine Classification System

**GWL_FCS30** is a global wetland map with a resolution of 30 meters, designed to provide detailed information on wetland ecosystems worldwide. This dataset spans from 2000 to 2022 and includes a fine classification system that distinguishes between eight specific wetland subcategories. These subcategories encompass both coastal tidal wetlands and inland wetlands, offering a comprehensive view of wetland types across the globe.

The coastal tidal wetlands in this dataset are categorized into mangroves, salt marshes, and tidal flats. For inland wetlands, the classification includes permanent water, swamps, marshes, flooded flats, and saline wetlands. This level of detail is crucial for understanding and managing different wetland types and their ecological functions.

The dataset was created using a novel approach that combines automatic sample extraction from various existing global wetland products with multi-temporal satellite imagery, including Landsat reflectance data and Sentinel-1 SAR imagery. This method allows for capturing the complex temporal dynamics and spectral variations of wetlands. Additionally, a stratified classification strategy was employed, utilizing local adaptive random forest models to ensure precise classification at a high spatial resolution.

The GWL_FCS30 dataset offers a spatial resolution of 30 meters and covers the entire globe. It provides valuable insights into wetland areas and their distribution over the past two decades, with the data presented in square kilometers. This dataset is an important resource for ecological studies, wetland management, and conservation efforts, providing essential information for understanding and preserving wetland ecosystems.

You can read the [paper here](https://doi.org/10.1038/s41597-024-03143-0), and find the complete [dataset here](https://doi.org/10.5281/zenodo.10068479)

#### Dataset Preprocessing
Yearly images are distributed as zipped files consisting of tiles for global regions which are merged into a single image per year. These are then ingested into a single image collection in GEE.

#### Citation

```
Zhang, X., Liu, L., Zhao, T., Chen, X., Lin, S., Wang, J., Mi, J., & Liu, W. (2023). GWL_FCS30: a global 30 m wetland map with a fine classification
system using multi-sourced and time-series remote sensing imagery in 2020. *Earth Syst. Sci. Data*, 15, 265–293.
https://doi.org/10.5194/essd-15-265-2023
```

#### Dataset Citation

```
Liangyun, L., & Xiao, Z. (2023). Time-series global 30 m wetland maps from 2000 to 2022 [Data set]. Zenodo. https://doi.org/10.5281/zenodo.10068479
```

<center>

| Class Code   | Wetland Subcategory   |
|--------------|-----------------------|
| 0            | Non-wetland           |
| 180          | Permanent Water       |
| 181          | Swamp                 |
| 182          | Marsh                 |
| 183          | Flooded Flat          |
| 184          | Saline                |
| 185          | Mangrove Forest       |
| 186          | Salt Marsh            |
| 187          | Tidal Flat            |

</center>

![global_wetland_map](https://github.com/user-attachments/assets/5902c902-9a33-497b-83ac-ec34b2ab7990)

#### Earth Engine Snippet

```js
var gwl_fcs30 = ee.ImageCollection("projects/sat-io/open-datasets/GWL_FCS30");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/GWL-FCS30-WETLANDS

#### License
These datasets are made available under the Creative Commons Attribution 4.0 International.

Provided by: Zhang et al 2023

Curated in GEE by: Samapriya Roy

Keywords: fine classification system, land cover, wetland, wetland ecosystem

Last updated: 2024-07-28


