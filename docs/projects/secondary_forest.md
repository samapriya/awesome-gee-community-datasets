# Benchmark maps of 39 years of secondary forest age for Brazil v8.1 (1986-2024)

The restoration and reforestation of 12 million hectares of forests by 2030 are amongst the leading mitigation strategies for reducing carbon emissions within the Brazilian Nationally Determined Contribution targets assumed under the Paris Agreement. Understanding the dynamics of forest cover, which steeply decreased between 1985 and 2024 throughout Brazil, is essential for estimating the global carbon balance and quantifying the provision of ecosystem services. To know the long-term increment, extent, and age of secondary forests is crucial; however, these variables are yet poorly quantified. Here we developed a 30-m spatial resolution dataset of the annual increment, extent, and age of secondary forests for Brazil over the 1986–2024 period. Land-use and land-cover maps from MapBiomas Project (Collection 10.1) were used as input data for our algorithm, implemented in the Google Earth Engine platform. This dataset provides critical spatially explicit information for supporting carbon emissions reduction, biodiversity, and restoration policies, enabling environmental science applications, territorial planning, and subsidizing environmental law enforcement. Read the [dataset paper and details here](https://www.nature.com/articles/s41597-020-00600-4)

#### Citation:

```
Silva Junior, C.H.L., Heinrich, V.H.A., Freire, A.T.G., Broggio, I.S., Rosan, T.M., Doblas, J.,
Anderson, L.O., Rousseau, G.X., Shimabukuro, Y.E., Silva, C.A., House, J.I., Aragão, L.E.O.C.
Benchmark maps of 33 years of secondary forest age for Brazil. Scientific Data (2020).
https://doi.org/10.1038/s41597-020-00600-4
```

#### Dataset Citation

```
Celso H. L. Silva Junior, Viola H. A. Heinrich, Ana T. G. Freire, Igor S. Broggio, Thais M. Rosan, Juan Doblas,
Luiz E. O. C. Aragão. (2020). Benchmark maps of 33 years of secondary forest age for Brazil (Version v8.1)
[Data set]. Scientific Data. Zenodo. http://doi.org/10.5281/zenodo.3928660
```

![secondary_forest](https://user-images.githubusercontent.com/6677629/118372534-c07bb300-b577-11eb-87cb-5e3d807a5396.gif)

#### Earth Engine Snippet

```js
var age       = ee.Image('users/ybyrabr/public/secondary_forest_age_collection10_1_v8_1');
var extent    = ee.Image('users/ybyrabr/public/secondary_forest_extent_collection10_1_v8_1');
var increment = ee.Image('users/ybyrabr/public/secondary_forest_increment_collection10_1_v8_1');
var loss      = ee.Image('users/ybyrabr/public/secondary_forest_loss_collection10_1_v8_1');
print(age, extent, increment, loss);
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/BRAZIL-SECONDARY-FOREST-AGE

#### Technical Validation
This dataset is based on Collection 10.1 of the MapBiomas Project (Annual Land-Use and Land-Cover Maps of Brazil); thus, the accuracy of the secondary forest increment, extent, and age maps presented here is anchored to the accuracy of the MapBiomas land-use and land-cover dataset. The MapBiomas analyses of accuracy were performed using the Pontius Jr and Millones (2011) method. The accuracy assessment for the Brazilian biomes can be found in the MapBiomas accuracy statistics web page (https://mapbiomas.org/en/accuracy-analysis).

#### License & Usage
This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Github Page: https://github.com/celsohlsj/gee_brazil_sv

Export Page for App: https://code.earthengine.google.com/13bfcedb77ac7bac9ea1fb962b587a54?hideCode=true

Zenodo Data download page: [https://zenodo.org/record/8190133](https://zenodo.org/records/8190133)

Created and Curated by: Celso H. L. Silva Junior

Keywords: Deforestation, MapBiomas, Climate Change, Forest Restoration, Carbon Sequestration

Last updated: 2026-05-01

#### Summary of updates (v8.1)
- Updated processing based on MapBiomas Collection 10.1
- Time series extended to cover 1986–2024 (39 years)
- Improved temporal consistency across the full time series
- Harmonized methodology across all products (age, extent, increment, and loss)
- Refinements in the detection of secondary forest dynamics
- Improved spatial consistency and reduction of classification artifacts
- New asset paths under `users/ybyrabr/public/` namespace
