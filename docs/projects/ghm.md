# Global Human Modification v3

The Global Human Modification v3 dataset provides a comprehensive, temporally consistent measure of cumulative human pressures on terrestrial ecosystems (excluding Antarctica) from 1990 to 2022. It builds on earlier versions (v1, v1.5, v2) by incorporating new time steps, higher-resolution data, and refined threat‐group layers. Users can leverage these data to quantify the extent and intensity of human modification for conservation planning, policy, and research.

The Global Human Modification v3 dataset offers a detailed, temporally consistent quantification of cumulative human pressures on global terrestrial ecosystems (excluding Antarctica) from 1990 through 2022. Building on earlier versions (v1, v1.5, v2), v3 introduces new five‑year time steps (2020) in the change‐consistent series and a comprehensive static snapshot for 2022 at both 300 m and 90 m resolutions. Each annual layer (1990, 1995, 2000, 2005, 2010, 2015, 2020 in the “c” series; 2022 in the “s” series) is computed per pixel and is provided for eight IUCN‑aligned threat categories—agriculture (AG), built‑up (BU), energy/mining (EX), biological resource use (FR), human accessibility (HI), natural systems modification (NS), pollution (PO), and transportation/service corridors (TI)—plus a combined overall layer (AA). Values are stored as 32‑bit floats in the \[0.0, 1.0] range, where 0.0 indicates no detectable human modification and 1.0 indicates maximum modeled modification. The 1990–2020 “c” series uses consistent input data every five years to enable valid change analysis; the 2022 “s” series incorporates updated satellite and land‑cover inputs and is not directly comparable to earlier years for quantitative change metrics.

v3 underwent rigorous technical validation using a spatially balanced sample (circa 2015–2017) from the Global Land Use Emergent Dataset (GLUED), yielding a 
root‑mean‑squared error (RMSE) of 0.180 at 300 m and 0.178 at 90 m—an improvement over v2 (RMSE = 0.213). Sensitivity analyses (e.g., Monte Carlo simulations for 
agricultural footprint uncertainty) demonstrated biome‐level mean differences of less than 0.004 under spatially random error assumptions. For full details, see 
Theobald et al. (2025) in *Scientific Data* [https://doi.org/10.1038/s41597-025-04892-2](https://doi.org/10.1038/s41597-025-04892-2). The 1990–2020 v3 “change” 
series is archived at Zenodo [https://doi.org/10.5281/zenodo.14449495](https://doi.org/10.5281/zenodo.14449495) and the 2022 “static” series at 
[https://doi.org/10.5281/zenodo.14502573](https://doi.org/10.5281/zenodo.14502573).


#### Key features of v3:

* **Temporal extent & granularity:** 1990, 1995, 2000, 2005, 2010, 2015, 2020 at 300 m resolution (`_c_` series), plus a 2022 static snapshot at both 300 m and 90 m resolutions (`_s_` series).

* **Dual resolutions for 2022:** 300 m (approx. 10 arc‐seconds) and 90 m (approx. 3 arc‐seconds).

* **Threat categories:** Eight IUCN-aligned threat codes (AG, BU, EX, FR, HI, NS, PO, TI) plus an overall combined index (AA) per year.

* **Data type:** Floating‐point values in \[0.0, 1.0], where each pixel’s modification score is:

  ${\text{modification}} = {\text{footprint proportion}} \times {\text{stressor intensity}}$

* **Naming conventions:** Asset IDs include suffixes `_YEARc_` for the 1990–2020 change‐consistent series, and `_2022s_` for the 2022 static snapshot. The `c` series is designed for temporal change analysis; the `s` series is a stand‐alone 2022 snapshot and is not recommended for direct quantitative comparisons with the `c` series.

#### Updates Changelog & reasoning
1. Bumped version to v3, extending the time‐series to include 2020 and introducing a static 2022 snapshot.
2. Added dual resolution for 2022 (`300 m` and `90 m`) to support higher‐resolution analyses.
3. Incorporated eight individual threat‐category layers (AG, BU, EX, FR, HI, NS, PO, TI) alongside the overall (AA) index for each year.
4. Updated dataset values to floating‐point format [0.0, 1.0] for improved precision over previous integer‐scaled data.
5. Refined threat‐group aggregation and metadata to align with Theobald *et al.* (2025) methodology.
6. Revised Earth Engine snippet to load hosted v3 collections (`HM_OVERALL`, `HM_THREAT_GROUP`, `HM_300M`, `HM_90M`) directly instead of assembling from individual assets.


#### Threat Code Legend

<center>

|  Code  | Description                                          |
| :----: | :--------------------------------------------------- |
| **AA** | All threats combined (overall modification)          |
| **AG** | Agriculture (croplands, forestry)                    |
| **BU** | Built-Up (residential, commercial, recreation areas) |
| **EX** | Energy production and mining                         |
| **FR** | Biological resource use                              |
| **HI** | Human accessibility (roads, trails, etc.)            |
| **NS** | Natural system modification (e.g., dams, reservoirs) |
| **PO** | Pollution                                            |
| **TI** | Transportation and service corridors                 |

</center>

#### Bands / Layers Metadata

Each `ee.Image` within the collections contains a single band named after its `threat_code`. Units are unitless floats in \[0.0, 1.0].

<center>

| Band / Threat Code | Description                                                | Data Type | Value Range |
| :----------------: | :--------------------------------------------------------- | :-------: | :---------: |
|       **AA**       | All threats combined (overall modification)                |  Float32  | \[0.0, 1.0] |
|       **AG**       | Agriculture (croplands, forestry)                          |  Float32  | \[0.0, 1.0] |
|       **BU**       | Built-Up (residential, commercial, recreation areas)       |  Float32  | \[0.0, 1.0] |
|       **EX**       | Energy production and mining                               |  Float32  | \[0.0, 1.0] |
|       **FR**       | Biological resource use                                    |  Float32  | \[0.0, 1.0] |
|       **HI**       | Human accessibility (roads, trails, infrastructure)        |  Float32  | \[0.0, 1.0] |
|       **NS**       | Natural system modification (e.g., dams, water regulation) |  Float32  | \[0.0, 1.0] |
|       **PO**       | Pollution                                                  |  Float32  | \[0.0, 1.0] |
|       **TI**       | Transportation and service corridors                       |  Float32  | \[0.0, 1.0] |

</center>


#### Citation

```
Theobald, D.M., Oakleaf, J.R., Moncrieff, G., Voigt, M., Kiesecker, J. & Kennedy, C.M. (2025). Global extent and change in human modification of terrestrial ecosystems from
1990 to 2022. *Scientific Data* **12**, 489. [doi:10.1038/s41597-025-04892-2](https://doi.org/10.1038/s41597-025-04892-2)
```

#### Dataset citations

```
Theobald, D.M., Oakleaf, J., Moncrieff, G., & Kennedy, C.M. (2024). Global human modification datasets of terrestrial ecosystems from 1990 to 2020 (v1.0.0) \[Data set]. Zenodo. [doi:10.5281/zenodo.14449495](https://doi.org/10.5281/zenodo.14449495)

Theobald, D.M., Oakleaf, J., Moncrieff, G., & Kennedy, C.M. (2024). Global human modification datasets of terrestrial ecosystems for 2022 (v1.0.0) \[Data set]. Zenodo. [doi:10.5281/zenodo.14502573](https://doi.org/10.5281/zenodo.14502573)
```

![ghm](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/9c7e404b-1c87-47b8-96c5-074d2e61acf1)

#### Earth Engine Snippet

```javascript
// Load the v3 collections
var HM_OVERALL = ee.ImageCollection("projects/sat-io/open-datasets/GHM/HM_1990_2020_OVERALL_300M");
var HM_THREAT_GROUP = ee.ImageCollection("projects/sat-io/open-datasets/GHM/HM_1990_2020_THREAT_GROUPS_300M");
var HM_300M = ee.ImageCollection("projects/sat-io/open-datasets/GHM/HM_2022_300M");
var HM_90M = ee.ImageCollection("projects/sat-io/open-datasets/GHM/HM_2022_90M");

// Define visualization palette (provided by authors)
var paletteHM = ['4c6100','adda25','e2ff9b','ffff73','ffe629','ffd37f','ffaa00','e69808','e60000','a80000','730000'];
var visParams = {min: 0.0, max: 1.0, palette: paletteHM};
var changeVis = {min: -0.5, max: 0.5, palette: ['blue','white','red']};

// --- Example usage & visualization ---
Map.setCenter(0, 0, 2); // Global view

// Overall modification for 2020 (300 m)
var overall2020 = HM_OVERALL.filter(ee.Filter.eq('year', 2020)).first();
Map.addLayer(overall2020, visParams, 'GHM-v3 2020 Overall (300m)');

// Change in overall modification: 1990 → 2020 (from HM_OVERALL)
var overall1990 = HM_OVERALL.filter(ee.Filter.eq('year', 1990)).first();
var change90_20 = overall2020.subtract(overall1990);
Map.addLayer(change90_20, changeVis, 'Change GHM Overall 1990–2020 (300m)', false);

// 2022 agriculture modification at 90 m
var ag2022_90 = HM_90M.filter(ee.Filter.eq('threat_code', 'AG')).first();
Map.addLayer(ag2022_90, visParams, 'GHM-v3 2022 Agriculture (90m)', false);

// Print collection summaries
print('HM_OVERALL (1990–2020 300m):', HM_OVERALL);
print('HM_THREAT_GROUP (1990–2020 per threat 300m):', HM_THREAT_GROUP);
print('HM_300M (2022 300m static):', HM_300M);
print('HM_90M (2022 90m static):', HM_90M);
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/GLOBAL-HUMAN-MODIFICATION

Earth Engine App: https://hm-30x30.projects.earthengine.app/view/hm-v3

#### License
This dataset is provided under a [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.

Provided by: David M. Theobald, James R. Oakleaf, Glenn Moncrieff, Maria Voigt, Joe Kiesecker, Christina M. Kennedy

Curated in GEE by: Samapriya Roy

Keywords: human modification, land use, biodiversity, global pressure, 30x30, Global Biodiversity Framework (GBF), conservation, anthropogenic impact, ecosystem change, human footprint

Last updated : 2025-06-03
