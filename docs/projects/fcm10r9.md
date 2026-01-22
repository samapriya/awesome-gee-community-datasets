# Forest Communities Mapping with AlphaEarth Embeddings

!!! warning "Preprint Dataset"
    This dataset is based on a preprint research paper that has not yet been peer reviewed. The methodology, data products, and interpretations may be updated as the paper proceeds through the peer review process. Please cite appropriately and check for updates.

This dataset represents a novel application of deep learning-based geospatial embeddings for ecological mapping, demonstrating how the AlphaEarth Foundations (AEF) model can transform forest community mapping by synthesizing petabytes of multi-source Earth observations into information-rich, 64-dimensional feature spaces. By combining AEF embeddings—which harmonize Sentinel-1/2, Landsat, GEDI, SAR, climate, and numerous other data sources with 22,658 Forest Inventory and Analysis (FIA) plots, this dataset delivers comprehensive forest community maps at 10-meter resolution across the Northeastern and Midwestern United States (U.S. Forest Service Region 9).

The resulting products cover over 65 million hectares of forest across 20 states and include community-constrained species composition for over 50 tree species, plus forest structure metrics (aboveground carbon, total basal area, and stem density). Critically, the AEF embeddings eliminate the need for manual feature engineering that has constrained previous forest mapping approaches, providing globally consistent, highly generalizable predictors that enable both k-nearest neighbor (kNN) imputation for species composition and Random Forest regression for structural attributes. The aboveground carbon estimates outperform four existing national and regional products, demonstrating the transformative potential of geospatial embeddings for large-scale ecological monitoring. You can read the [preprint here](https://ssrn.com/abstract=5936862) for additional details.

#### Citation

```
Gao, X., Pasquarella, V.J., Laflower, D., and Thompson, J.R. (2025). Mapping Forest Communities, Including Species Composition, Structure, and Carbon,
at 10-m Resolution Using Geospatial Embeddings. Available at SSRN: https://ssrn.com/abstract=5936862
```

**Note:** This is a preprint and has not been peer reviewed. Please check for updated citation information as the paper proceeds through review.

#### Key Features and Details

**Spatial Resolution:** 10 meters

**Temporal Coverage:** 2021 (based on FIA measurements from 2018-2022 and 2021 AEF embeddings)

**Coverage:** U.S. Forest Service Region 9, including 20 states: Connecticut (CT), Delaware (DE), Iowa (IA), Illinois (IL), Indiana (IN), Massachusetts (MA), Maryland (MD), Maine (ME), Michigan (MI), Minnesota (MN), Missouri (MO), New Hampshire (NH), New Jersey (NJ), New York (NY), Ohio (OH), Pennsylvania (PA), Rhode Island (RI), Vermont (VT), Wisconsin (WI), and West Virginia (WV)

**Study Area:** > 65 million hectares of forest

**Data Products:**

1. **Species-Specific Basal Area (SPEC):** Over 50 tree species mapped individually with basal area (m² ha⁻¹) as the metric. Species composition maps preserve ecologically realistic assemblages through kNN imputation (k=1).

2. **Aboveground Carbon (AGC):** Plot-level aboveground carbon stocks (Mg C ha⁻¹) mapped using Random Forest regression. Cross-validation R² = 0.56, RMSE = 26.64 Mg C ha⁻¹. Outperforms existing products at county (R² = 0.47) and state (R² = 0.90) levels.

3. **Total Basal Area (BA):** Plot-level total basal area (m² ha⁻¹) across all species. Cross-validation R² = 0.52, RMSE = 7.96 m² ha⁻¹.

4. **Stem Density (SD):** Plot-level stem density (trees ha⁻¹). Cross-validation R² = 0.50, RMSE = 166 trees ha⁻¹.


#### Mapped Tree Species

??? example "Expand to show the list of species"

      | Code | Scientific Name | Common Name |
      |------|----------------|-------------|
      | ABBA | *Abies balsamea* | Balsam fir |
      | ACPE | *Acer pensylvanicum* | Striped maple |
      | ACRU | *Acer rubrum* | Red maple |
      | ACSA | *Acer saccharum* | Sugar maple |
      | BEAL | *Betula alleghaniensis* | Yellow birch |
      | BELE | *Betula lenta* | Sweet birch |
      | BEPA | *Betula papyrifera* | Paper birch |
      | BEPO | *Betula populifolia* | Gray birch |
      | CAAL | *Carya alba* | Mockernut hickory |
      | CACA | *Carpinus caroliniana* | American hornbeam |
      | CAGL | *Carya glabra* | Pignut hickory |
      | CAOV | *Carya ovata* | Shagbark hickory |
      | COFL | *Cornus florida* | Flowering dogwood |
      | FAGR | *Fagus grandifolia* | American beech |
      | FRAM | *Fraxinus americana* | White ash |
      | FRNI | *Fraxinus nigra* | Black ash |
      | FRPE | *Fraxinus pennsylvanica* | Green ash |
      | JUVI | *Juniperus virginiana* | Eastern redcedar |
      | LALA | *Larix laricina* | Tamarack |
      | LIST | *Liquidambar styraciflua* | Sweetgum |
      | LITU | *Liriodendron tulipifera* | Tulip poplar |
      | NYSY | *Nyssa sylvatica* | Black gum |
      | OSVI | *Ostrya virginiana* | Eastern hophornbeam |
      | OXAR | *Oxydendrum arboreum* | Sourwood |
      | PIAB | *Picea abies* | Norway spruce |
      | PIBA | *Picea mariana* | Black spruce |
      | PIEC | *Picea glauca* | White spruce |
      | PIGL | *Picea glauca* | White spruce |
      | PIMA | *Picea mariana* | Black spruce |
      | PIRE | *Picea rubens* | Red spruce |
      | PIRI | *Pinus rigida* | Pitch pine |
      | PIRU | *Picea rubens* | Red spruce |
      | PIST | *Pinus strobus* | Eastern white pine |
      | PITA | *Pinus taeda* | Loblolly pine |
      | PIVI | *Pinus virginiana* | Virginia pine |
      | POBA | *Populus balsamifera* | Balsam poplar |
      | POBA2 | *Populus balsamifera* | Balsam poplar |
      | POGR | *Populus grandidentata* | Bigtooth aspen |
      | POTR | *Populus tremuloides* | Quaking aspen |
      | PRPE2 | *Prunus pensylvanica* | Pin cherry |
      | PRSE | *Prunus serotina* | Black cherry |
      | QUAL | *Quercus alba* | White oak |
      | QUCO | *Quercus coccinea* | Scarlet oak |
      | QUFA | *Quercus falcata* | Southern red oak |
      | QUMA | *Quercus macrocarpa* | Bur oak |
      | QUNI | *Quercus nigra* | Water oak |
      | QUPR | *Quercus prinus* | Chestnut oak |
      | QURU | *Quercus rubra* | Northern red oak |
      | QUST | *Quercus stellata* | Post oak |
      | QUVE | *Quercus velutina* | Black oak |
      | ROPS | *Robinia pseudoacacia* | Black locust |
      | SAAL | *Salix alba* | White willow |
      | THOC | *Thuja occidentalis* | Northern white-cedar |
      | TIAM | *Tilia americana* | American basswood |
      | TSCA | *Tsuga canadensis* | Eastern hemlock |
      | ULAL | *Ulmus alata* | Winged elm |
      | ULAM | *Ulmus americana* | American elm |
      | ULRU | *Ulmus rubra* | Slippery elm |

#### Dataset Preprocessing for Earth Engine

The FCM10R9 dataset consists of four main image collections representing different forest attributes. All products were generated at 10-m resolution and masked to forested areas using ESA WorldCover 2021. Species-specific basal area maps were created through kNN imputation, while plot-level metrics were generated using Random Forest regression. The dataset is available through both Harvard Dataverse and Google Earth Engine. The datasets are provided per state and species and merged into collections for easy access and include metadata for easy filtering.

**Metadata Properties:**

All images include the following properties:

- `spatial_resolution`: 10
- `product`: "FCM10R9"
- `version`: "R9"
- `state`: Two-letter state code (e.g., "MA", "NY")
- `metric`: Metric type (e.g., "AGC", "BA", "SD")
- `unit`: Measurement unit (e.g., "Mg/Ha", "m2/Ha", "Trees/Ha")

Species images additionally include:

- `species_code`: Four-letter species code (e.g., "ACRU", "QURU")
- `species_scientific_name`: Scientific name (e.g., "*Acer rubrum*")
- `species_common_name`: Common name (e.g., "Red maple")

![fcm10r9](../images/fcm10r9.gif)

#### Earth Engine Snippet

```js
var agc = ee.ImageCollection("projects/sat-io/open-datasets/FCM10R9/AGC");
var ba = ee.ImageCollection("projects/sat-io/open-datasets/FCM10R9/BA");
var sd = ee.ImageCollection("projects/sat-io/open-datasets/FCM10R9/SD");
var species = ee.ImageCollection("projects/sat-io/open-datasets/FCM10R9/SPEC");

Map.setCenter(-84.787,41.238,5)

// Create mosaics
var agcMosaic = agc.mosaic();
var baMosaic = ba.mosaic();
var sdMosaic = sd.mosaic();

print(species.aggregate_histogram("species_code"))

// Aboveground Carbon Vis
var agcVis = {
  min: 0,
  max: 150,
  palette: ['fef0d9', 'fdd49e', 'fdbb84', 'fc8d59', 'e34a33', 'b30000', '7f0000']
};

// Basal Area Vis
var baVis = {
  min: 0,
  max: 40,
  palette: ['f7fbff', 'deebf7', 'c6dbef', '9ecae1', '6baed6', '4292c6', '2171b5', '08519c', '08306b']
};

// Stem Density Vis
var sdVis = {
  min: 0,
  max: 1000,
  palette: ['f7f4f9', 'e7e1ef', 'd4b9da', 'c994c7', 'df65b0', 'e7298a', 'ce1256', '980043', '67001f']
};

// Sugar Maple Vis
var sugarMaple = species.filter(ee.Filter.eq('species_code', 'ACSA')).mosaic();
var sugarMapleVis = {
  min: 0,
  max: 20,
  palette: ['ffffd4', 'fee391', 'fec44f', 'fe9929', 'ec7014', 'cc4c02', '993404', '662506']
};

// Eastern Hemlock Vis
var easternHemlock = species.filter(ee.Filter.eq('species_code', 'TSCA')).mosaic();
var easternHemlockVis = {
  min: 0,
  max: 20,
  palette: ['f7fcf5', 'e5f5e0', 'c7e9c0', 'a1d99b', '74c476', '41ab5d', '238b45', '006d2c', '00441b']
};


Map.addLayer(agcMosaic, agcVis, 'Aboveground Carbon (Mg C/ha)', true);
Map.addLayer(baMosaic, baVis, 'Basal Area (m²/ha)', false);
Map.addLayer(sdMosaic, sdVis, 'Stem Density (trees/ha)', false);
Map.addLayer(sugarMaple, sugarMapleVis, 'Sugar Maple - Autumn Gradient', false);
Map.addLayer(easternHemlock, easternHemlockVis, 'Eastern Hemlock - Forest Greens', false);

var snazzy = require("users/aazuspan/snazzy:styles");
snazzy.addStyle("https://snazzymaps.com/style/15/subtle-grayscale", "Subtle Gray");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/FCM10R9-FOREST-COMMUNITIES

#### License

This work is licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). You are free to share and adapt the material for any purpose, provided appropriate credit is given.

#### Acknowledgments

This work was funded by NSF-DEB-LTER Grant 18-32210 and NSF-DISES Grant 22-05705. The authors thank Christopher F. Brown at Google DeepMind for support with the AlphaEarth Foundations embeddings, and the U.S. Forest Service for access to precise FIA plot coordinates under Data Use Agreement #19-MU-11242305-016.

Provided by: Gao et al. (2025), Harvard Forest, Harvard University

Curated in GEE by: Samapriya Roy

Keywords: Forest Communities, Species Composition, Aboveground Carbon, Basal Area, Stem Density, Tree Species, Forest Structure, Remote Sensing, Deep Learning, Geospatial Embeddings, AlphaEarth Foundations, FIA, kNN Imputation, Random Forest, Northeastern US, Midwestern US

Last updated in GEE: 2026-01-19
