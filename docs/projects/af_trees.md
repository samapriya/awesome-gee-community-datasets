# High resolution map of African tree cover

This dataset leverages high-resolution satellite imagery obtained from a nano-satellite constellation, accessible in the tropics through Norway's International Climate and Forest Initiative (NICFI) programme. The primary goal of this dataset is to comprehensively map both forest and non-forest trees on a continental scale across Africa, surpassing the precision of previous endeavors in mapping woody vegetation at large scales.

Utilizing a machine learning approach, we employ 3 m PlanetScope satellite imagery to segment tree canopy cover across Africa, reaching the level of individual scattered trees. The dataset provides a detailed quantification of the contribution of trees located outside traditional forested areas to the overall tree cover within each country. Notably, at the continental scale, our analysis reveals that 29% of the total tree cover exists outside regions classified as forests in a contemporary state-of-the-art map based on Sentinel-2 10 m imagery. You can read the [paper here](https://www.nature.com/articles/s41467-023-37880-4)

#### Citation

```
Reiner, F., Brandt, M., Tong, X. et al. More than one quarter of Africa’s tree cover is found outside areas previously
classified as forest. Nat Commun 14, 2258 (2023). https://doi.org/10.1038/s41467-023-37880-4
```

#### Dataset citation

```
Reiner, F., Brandt, M., Tong, X., Skole, D., Kariryaa, A., Ciais, P., Davies, A., Hiernaux, P., Chave, J., Mugabowindekwe, M.,
Igel, C., Oehmcke, S., Gieseke, F., Li, S., Liu, S., Saatchi, S., Boucher, P., Singh, J., Taugourdeau, S., … Fensholt, R.
(2023). Africa tree cover map [Data set]. Zenodo. https://doi.org/10.5281/zenodo.7764460
```

![af_treecover-small](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/211e34e9-d748-4c7e-ba88-35bc37ceb75c)

#### Earth Engine Snippet

```js
var tree_cover = ee.Image("projects/sat-io/open-datasets/PS_AFRICA_TREECOVER_2019_100m_V10")
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/PS-AFRICA-TREECOVER

#### License

This tree cover map is made freely available for non-commercial purposes. All usage of the data must be attributed and should be cited with the paper citation. Please see the NICFI license for full terms of usage, [available here](https://assets.planet.com/docs/Planet_ParticipantLicenseAgreement_NICFI.pdf)

Provided by: Reiner et al

Curated in GEE by: Samapriya Roy

Keywords: Africa, NICFI, Planet, Tree cover, Land cover

Last updated in GEE: 2024-01-18
