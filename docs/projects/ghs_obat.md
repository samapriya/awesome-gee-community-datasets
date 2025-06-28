# Global Human Settlement - Open Buildings Attribute Table (GHS-OBAT)

The Global Human Settlement Layer (GHSL) Open Buildings Attribute Table (GHS-OBAT) represents a comprehensive data integration initiative that combines 2.3 billion building footprint geometries from the Overture Maps Foundation with thematic attributes derived from the Global Human Settlement Layer data suite. This dataset enhances building footprints with remotely sensed information including construction epochs, building heights, functional use classifications, and morphological characteristics, providing unprecedented global coverage for building-level analysis. You can read [the paper with additional information here](https://www.sciencedirect.com/science/article/pii/S2352340925004780)

The GHS-OBAT dataset bridges the gap between detailed vector building footprints and thematically rich gridded settlement data, enabling new research opportunities in building stock analysis, energy planning, disaster risk management, and urban morphology studies. Built upon the GHSL Data Package 2023, this dataset brings global settlement information to the individual building level through advanced vector-raster integration techniques.

#### Dataset Details

| Characteristic | Description |
|----------------|-------------|
| Name | GHS-OBAT - Global Human Settlement Open Buildings Attribute Table |
| Provider | European Commission Joint Research Centre (JRC) |
| Coverage | Global (2.3 billion building footprints) |
| Temporal Range | 2020 (reference year) |
| Resolution | Individual building footprints |
| Data Format | Feature Collections (by country) |
| Coordinate System | WGS84 (EPSG:4326) |
| Source Data | Overture Maps Foundation buildings + GHSL R2023/R2024 |

#### Citation

```
Florio, Pietro, Panagiotis Politis, Katarzyna Krasnodębska, Johannes H. Uhl, Michele Melchiorri,
Ana M. Martinez, Georgia Kakoulaki, Martino Pesaresi, and Thomas Kemper. "GHS-OBAT: Global,
Open Building Attribute data reporting age, function, height and compactness at footprint level."
Data in Brief (2025): 111751.

Florio, P., Politis, P., Krasnodębska, K., Uhl, J.H., Melchiorri, M., Martinez, A., Kakoulaki, G.,
Pesaresi, M., Kemper, T. (2025). GHS-OBAT: Global Human Settlement - Open Buildings Attribute Table.
European Commission, Joint Research Centre (JRC). doi: 10.2905/f41a22f1-5741-4c41-86eb-6384654f6927
```

#### Building Attributes

??? example "The GHS-OBAT dataset includes the following attributes for each building footprint"

      | Attribute | Type | Unit | Description |
      |-----------|------|------|-------------|
      | **id** | String | - | Unique GERS identifier linking to Overture buildings (32 HEX string) |
      | **lon** | Decimal | Degrees | Longitude of building footprint centroid (WGS84) |
      | **lat** | Decimal | Degrees | Latitude of building footprint centroid (WGS84) |
      | **country** | String | - | ISO 3166-1 alpha-3 country code (from GADM 4.1) |
      | **adm1** | String | - | First-level administrative division name |
      | **height** | Decimal | Meters | Mean building height from GHS-BUILT-H (minimum 2.5m) |
      | **shapefactor** | Decimal | m²/m³ | Building compactness ratio (surface/volume) |
      | **use** | Integer | 0-2 | Functional use: 0=outside domain, 1=residential, 2=non-residential |
      | **epoch** | Integer | 0-5 | Construction period: 0=outside domain, 1=before 1980, 2=1980-1990, 3=1990-2000, 4=2000-2010, 5=2010-2020 |
      | **area** | Decimal | m² | Building footprint area (computed in local UTM) |
      | **perimeter** | Decimal | Meters | Building footprint perimeter (computed in local UTM) |

#### Dataset Preprocessing

Certain countries sub parts have been merged to create a consistent single file representation which include, BRA, IND, IDN, MEX, USA, RUS, NGA and PAK. The multi part collections were ingested and then merged into a single feature collection in Earth Engine.

#### Coverage and Limitations

**Global Coverage**: The dataset covers all countries and territories with building footprints available in Overture Maps, totaling 2.28 billion attributed buildings worldwide.

!!! info "Known Limitations"

    - **Geographical Coverage**: Severe under representation in China and parts of Central Asia
    - **Height Accuracy**: Building height underestimation with Mean Absolute Error of 2.89m at feature level
    - **Functional Classification**: Reduced accuracy for small non-residential buildings
    - **Temporal Accuracy**: Construction epoch accuracy varies significantly - 40% for pre-1980 buildings, >65% for post-1980 construction

![ghs_obat_layers](../images/ghs_obat.gif)

#### Earth Engine Snippet

```javascript
// Load a specific country's building data (example: Trinidad and Tobago)
var ghs_obat_tto = ee.FeatureCollection("projects/sat-io/open-datasets/JRC/GHS-OBAT/GHS_OBAT_GPKG_TTO_E2020_R2024A_V1_0");

// Filter buildings by attributes (example: residential buildings constructed 2000-2010)
var residential_2000s = ghs_obat_tto.filter(ee.Filter.and(
  ee.Filter.eq('use', 1),  // Residential
  ee.Filter.eq('epoch', 4) // 2000-2010
));

// Visualize building height distribution
Map.addLayer(ghs_obat_tto, {color: 'height'}, 'Building Heights');
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/GHS-OBAT-OPEN-BUILDINGS

#### Data Access by Country

The dataset is organized by country using ISO 3166-1 alpha-3 codes. Each country's data is available as a separate Earth Engine FeatureCollection:

```javascript
// Examples of country-specific collections
var usa_buildings = ee.FeatureCollection("projects/sat-io/open-datasets/JRC/GHS-OBAT/GHS_OBAT_GPKG_USA_E2020_R2024A_V1_0");
var deu_buildings = ee.FeatureCollection("projects/sat-io/open-datasets/JRC/GHS-OBAT/GHS_OBAT_GPKG_DEU_E2020_R2024A_V1_0");
var jpn_buildings = ee.FeatureCollection("projects/sat-io/open-datasets/JRC/GHS-OBAT/GHS_OBAT_GPKG_JPN_E2020_R2024A_V1_0");
```

#### Validation and Accuracy

The dataset has been validated against authoritative building databases, particularly EUBUCCO for European countries:

- **Height Accuracy**: Generally underestimated with MAE of 2.89m (improves when weighted by building area)
- **Functional Use**: Small non-residential buildings may be misclassified as residential
- **Construction Epoch**: Higher accuracy for recent construction periods (post-1980)
- **Coverage Assessment**: Benchmarked against GHS-BUILT-S with identified gaps in specific regions

#### License

This dataset is made available under the Creative Commons Attribution 4.0 International (CC BY 4.0) license  type.

#### Keywords

Building Stock, Global Human Settlement, Urban Morphology, Construction Epoch, Building Height, Functional Use, Remote Sensing, Overture Maps, Energy Planning, Disaster Risk Management, Urban Planning, Climate Change

Created by: Pietro Florio et al 2025, European Commission Joint Research Centre

Curated in GEE by: Samapriya Roy

Last updated: 2025-06-28
