# Global Lakes and Wetlands Database (GLWD) Version 2

The Global Lakes and Wetlands Database (GLWD) Version 2 provides a harmonized global database of lakes, rivers, and wetlands at 15 arc-second resolution. This dataset combines and harmonizes multiple ground and satellite-based data products to create a comprehensive map of inland water extents, types, and their intrinsic temporal dynamics.

GLWD v2 represents 18.2 million km² of wetlands (13.4% of global land area excluding Antarctica) classified into 33 types. The classification system differentiates between natural and non-natural lakes, rivers of multiple sizes, and various wetland types incorporating information on:
- Seasonality (permanent vs. intermittent vs. ephemeral)
- Inundation vs. saturation
- Vegetation cover (forested vs. non-forested)
- Salinity
- Natural vs. non-natural origins
- Landscape position and water source (riverine, lacustrine, palustrine, coastal/marine)

#### Citation

```
Lehner, B., Anand, M., Fluet-Chouinard, E., Tan, F., Aires, F., Allen, G.H., Bousquet, P., Canadell, J.G., Davidson, N., Finlayson, C.M., Gumbricht, T., Hilarides, L., Hugelius, G., Jackson, R.B., Korver, M.C.,
McIntyre, P.B., Matthews, E., Nagy, S., Olefeldt, D., Pavelsky, T., Pekel, J.-F., Poulter, B., Prigent, C., Wang, J., Worthington, T.A., Yamazaki, D., Thieme, M. (in preparation). Mapping the world’s inland waters: an
update to the Global Lakes and Wetlands Database (GLWD v2).
```

#### Data Format and Limitations

The data is provided in both ESRI© Geodatabase and GeoTIFF formats at 15 arc-second resolution, covering an area from 180° West to 180° East and 56° South to 84° North (excluding Antarctica). The data uses the World Geodetic System 1984 (GCS_WGS_1984) coordinate system. The dataset has several known limitations:

* Data sparsity in certain regions
* Possible classification uncertainties in areas with complex wetland mosaics
* Limited accuracy for areas with rapid land use change

#### Dataset Components

The GLWD v2 dataset in Google Earth Engine consists of several components:

### Image Collections

- **DELTA_AREA_CLASS_PCT**: An image collection containing individual images for each of the 33 wetland classes (plus dryland), showing the extent of each wetland class per pixel as a percentage of pixel area. Values range from 0-100%.

### Individual Images
- **GLWD_V2_DELTA_AREA_HA_X10**: Shows the absolute area of all wetland classes combined in hectares, multiplied by 10 for precision (i.e., a value of 15 means 1.5 ha). This layer is useful for quantifying total wetland extent.

- **GLWD_V2_DELTA_AREA_PCT**: Represents the relative area of all wetland classes combined as a percentage of pixel area (0-100%). This layer helps visualize the density of wetland coverage.

- **GLWD_V2_DELTA_MAIN_CLASS**: Identifies the dominant wetland class within each pixel using class IDs 1-33 (0 indicates inland pixels without any wetland coverage). In cases where multiple classes have equal coverage, the lower class ID is chosen.

- **GLWD_V2_DELTA_MAIN_CLASS_50PCT**: Similar to MAIN_CLASS but only shows the dominant wetland class for pixels where total wetland extent exceeds 50%. Value 0 indicates inland pixels where dryland dominates.

- **GLWD_v2_delta_class_00_pct**: Shows the percentage of each pixel that is classified as dryland (non-wetland). Values range from 0-100%.

#### Wetland Classes

The dataset uses band values from 0 to 33 to classify different types of wetlands and water bodies

??? example "Expand to show Band Value and Corresponding Class information"

    <center>

    | Band Value | Class Name                                     | Description                                                     |
    | ---------- | ---------------------------------------------- | --------------------------------------------------------------- |
    | 0          | Dryland                                        | Non-wetland areas                                               |
    | 1          | Freshwater lake                                | Natural freshwater lakes                                        |
    | 2          | Saline lake                                    | Natural saline/salt lakes                                       |
    | 3          | Reservoir                                      | Artificial water bodies                                         |
    | 4          | Large river                                    | Major river channels                                            |
    | 5          | Large estuarine river                          | River sections influenced by tides                              |
    | 6          | Other permanent waterbody                      | Permanent water features not in other categories                |
    | 7          | Small streams                                  | Minor waterways and tributaries                                 |
    | 8          | Lacustrine, forested                           | Lake-associated forested wetlands                               |
    | 9          | Lacustrine, non-forested                       | Lake-associated non-forested wetlands                           |
    | 10         | Riverine, regularly flooded, forested          | River-associated forested wetlands with regular flooding        |
    | 11         | Riverine, regularly flooded, non-forested      | River-associated non-forested wetlands with regular flooding    |
    | 12         | Riverine, seasonally flooded, forested         | River-associated forested wetlands with seasonal flooding       |
    | 13         | Riverine, seasonally flooded, non-forested     | River-associated non-forested wetlands with seasonal flooding   |
    | 14         | Riverine, seasonally saturated, forested       | River-associated forested wetlands with seasonal saturation     |
    | 15         | Riverine, seasonally saturated, non-forested   | River-associated non-forested wetlands with seasonal saturation |
    | 16         | Palustrine, regularly flooded, forested        | Marsh-type forested wetlands with regular flooding              |
    | 17         | Palustrine, regularly flooded, non-forested    | Marsh-type non-forested wetlands with regular flooding          |
    | 18         | Palustrine, seasonally saturated, forested     | Marsh-type forested wetlands with seasonal saturation           |
    | 19         | Palustrine, seasonally saturated, non-forested | Marsh-type non-forested wetlands with seasonal saturation       |
    | 20         | Ephemeral, forested                            | Temporary forested wetlands                                     |
    | 21         | Ephemeral, non-forested                        | Temporary non-forested wetlands                                 |
    | 22         | Arctic/boreal peatland, forested               | Northern forested peat wetlands                                 |
    | 23         | Arctic/boreal peatland, non-forested           | Northern non-forested peat wetlands                             |
    | 24         | Temperate peatland, forested                   | Mid-latitude forested peat wetlands                             |
    | 25         | Temperate peatland, non-forested               | Mid-latitude non-forested peat wetlands                         |
    | 26         | Tropical peatland, forested                    | Tropical forested peat wetlands                                 |
    | 27         | Tropical peatland, non-forested                | Tropical non-forested peat wetlands                             |
    | 28         | Mangrove                                       | Coastal mangrove forests                                        |
    | 29         | Saltmarsh                                      | Coastal salt marshes                                            |
    | 30         | Delta                                          | River delta wetland complexes                                   |
    | 31         | Other coastal wetland                          | Other coastal wetland types                                     |
    | 32         | Salt pan, saline/brackish wetland              | Inland saline wetlands and salt flats                           |
    | 33         | Paddy rice                                     | Agricultural wetlands used for rice cultivation                 |


![glwd](https://github.com/user-attachments/assets/25529f5f-7fee-45b0-aded-2bc1fe02e379)

#### Earth Engine Snippet

```js
// Area by class in hectares (x10)
var glwdAreaHa = ee.Image('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GLWD/GLWD_V2_DELTA_AREA_HA_X10');

// Area as percentage
var glwdAreaPct = ee.Image('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GLWD/GLWD_V2_DELTA_AREA_PCT');

// Dominant wetland class
var glwdMainClass = ee.Image('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GLWD/GLWD_V2_DELTA_MAIN_CLASS');

// Dominant wetland class (>50% coverage)
var glwdMainClass50 = ee.Image('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GLWD/GLWD_V2_DELTA_MAIN_CLASS_50PCT');

// Dryland percentage
var glwdDrylandPct = ee.Image('projects/earthengine-legacy/assets/projects/sat-io/open-datasets/GLWD/GLWD_v2_delta_class_00_pct');

// Area by class percentage (ImageCollection)
var glwdClassPct = ee.ImageCollection('projects/sat-io/open-datasets/GLWD/DELTA_AREA_CLASS_PCT');
```

Sample Classes:  https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/GLWD-V2

#### License

GLWD v2 is licensed under a Creative Commons Attribution 4.0 International License. The data is available for [public download via hydrosheds](https://www.hydrosheds.org/products/glwd)

Keywords: wetlands, lakes, rivers, hydrology, water resources, ecosystem, conservation, global dataset

Created by: Lehner et al.

Curated in GEE by: Samapriya Roy

Last updated: 2025-02-19
