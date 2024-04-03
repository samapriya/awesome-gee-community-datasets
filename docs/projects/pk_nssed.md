# National-Scale Soil Erosion Dataset for Pakistan (2005 and 2015)

This dataset offers a comprehensive assessment of soil erosion dynamics in Pakistan from 2005 to 2015, utilizing the Revised Universal Soil Loss Equation (RUSLE) and considering six key influencing factors: rainfall erosivity (R), soil erodibility (K), slope-length (L), slope-steepness (S), cover management (C), and conservation practice (P). Soil erosion maps, categorized into four classes ranging from low to very high erosion rates, provide insights into the spatial distribution and changes in soil erosion patterns over the study period. Transition analyses among erosion classes reveal shifts in erosion intensity, while spatial patterns and dynamics are evaluated across seven administrative units of Pakistan. The dataset highlights a national-scale increase in soil erosion from 1.79 ± 11.52 ton ha⁻¹ yr⁻¹ in 2005 to 2.47 ± 18.14 ton ha⁻¹ yr⁻¹ in 2015, driven by land cover and land use changes induced by population growth, infrastructural development, and natural resource exploitation. Comprehensive assessment of soil erosion dynamics in Pakistan for 2005 and 2015 at 1 km² spatial resolution using the Revised Universal Soil Loss Equation (RUSLE) model and six influencing factors. Soil erosion maps are categorized into four classes: low, medium, high, and very high, revealing an increase from 1.79 to 2.47 ton ha⁻¹ yr⁻¹ on the national level. You can read [the full paper here](https://onlinelibrary.wiley.com/doi/epdf/10.1002/ldr.4138)

The national-scale soil erosion dataset for Pakistan (2005 and 2025) at 1km spatial resolution data is [available here](https://zenodo.org/records/10694225)

#### Citation

```
Gilani, H., Ahmad, A., Younes, I., & Abbas, S. (2021). Impact assessment of land cover and land use changes on soil erosion changes (2005–2015) in
Pakistan. Land Degradation & Development, 33(1):204–217. [doi.org/10.1002/ldr.4138](https://doi.org/10.1002/ldr.4138)
```

#### Dataset Citation

```
Gilani, Hammad, Ahmad, Adeel, Younes, Isma, & Abbas, Sawaid. (2021). National-scale soil erosion dataset for Pakistan (2005 and 2025) at 1km spatial resolution (1.0) [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.10694225
```

![pakistan_soilerosion](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/f14771d4-8143-4146-a141-2ad06fa2880e)

### Earth Engine Snippet

```js
var pk_soil_erosion_2005 = ee.Image('projects/sat-io/open-datasets/NSSED-PAKISTAN/Pakistan_soil_erosion_2005_1km');
var pk_soil_erosion_2015 = ee.Image('projects/sat-io/open-datasets/NSSED-PAKISTAN/Pakistan_soil_erosion_2015_1km');
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:soil-properties/NATIONAL-SOIL-ERODABILITY-DATASET-PK

#### License

The datasets are licensed under a Creative Commons Attribution (CC-BY) 4.0 International License.

Created by: Gilani et al. 2021

Curated in GEE by : Adeel Ahmad and Samapriya Roy

Keywords: soil erosion, soil conservation, RUSLE, Pakistan, temporal soil erosion

Last updated in GEE: 2024-02-20
