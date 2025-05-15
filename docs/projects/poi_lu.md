# POI-based Large-Scale Land Use Modeling Framework

POI-based Land Use Modeling is a framework for characterizing land use patterns at different spatial scales and semantic granularities by leveraging Points of Interest (POI) data. This approach, developed by researchers at Oak Ridge National Laboratory, transforms Areas of Interest (AOIs) into high-dimensional embeddings using neural network language models. The framework integrates both spatial distribution and semantic attributes of POIs inside an AOI to capture its land use characteristics. By combining POIs with road network hierarchies and incorporating semantic representation based on OSM tags, this methodology provides a scalable solution for large-scale land use modeling across diverse geographic contexts.

#### Framework Components

- **POI Data Fusion**: Unifies heterogeneous POI data from multiple sources using OSM tags as semantic bridges
- **Spatially Explicit POI Corpus**: Organizes POIs hierarchically according to road network structure
- **Neural Network Embedding**: Transforms POIs into high-dimensional vectors capturing both spatial and semantic information
- **AOI Representation**: Calculates AOI embeddings as weighted averages of POI embeddings
- **Land Use Classification**: Predicts land use types at different semantic granularities (3-class or 13-class schemes)

#### Dataset Details

| Characteristic  | Description                                                           |
|-----------------|-----------------------------------------------------------------------|
| Name            | POI-based Land Use Modeling Framework                                 |
| Developers      | Oak Ridge National Laboratory (Junchuan Fan & Gautam Thakur)          |
| Data Sources    | Multiple POI providers (OSM, Facebook, Here, Google, TomTom, etc.)    |
| Spatial Coverage| Demonstrated across three continents (tested in South Africa, South Korea, England) |
| Resolution      | Multiple spatial scales (original land use boundaries or aggregated)  |
| Classification  | Two semantic granularities (3-class and 13-class land use schemes)    |
| License         | Open Access article under CC Attribution-NonCommercial License        |

#### Notes

- The framework integrates non-POI geographic features (roads, buildings) to enhance semantic representation
- Spatial scale analysis shows that original land use boundaries provided by volunteers yield better semantic coherence than aggregated boundaries
- The approach demonstrates effectiveness across different geographic regions with varying social, cultural and economic contexts
- Land use classification performance varies by region, reflecting unique geographical characteristics of each area
- The 3-class schema (residential, non-residential, open space) generally shows better performance than the 13-class detailed schema

#### Citation

```
Fan, J., & Thakur, G. (2023). Towards POI-based large-scale land use modeling: spatial scale, semantic granularity, and geographic context.
International Journal of Digital Earth, 16(1), 430-445. https://doi.org/10.1080/17538947.2023.2174607
```

#### Earth Engine Snippets

```js
// Access the POI-based land use modeling 3-class collection
var landUse_3class = ee.ImageCollection("projects/sat-io/open-datasets/ORNL/grid_3c");

// Visualization parameters for 3-class land use
var landUseVis = {
  bands: 'classification',
  min: 10,
  max: 30,
  palette: ['#3eca76', '#cf6aa6', '#e6e5d8']
  // Green (open space), Purple (residential), Light beige (non-residential)
};

// Initialize the map
Map.setOptions('HYBRID');
Map.setCenter(20, 10, 2); // Center on a global view

// Create a mosaic of the land use data
var landUseMosaic = landUse_3class.mosaic();

// Add land use layer
Map.addLayer(landUseMosaic, landUseVis, 'POI-based Land Use Classification');
```

Sample Script: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/POI-LANDUSE-FRAMEWORK

#### Use Cases

- Urban planning and zoning policy development
- Understanding urban form and function relationships
- Population distribution modeling
- Land use change detection and monitoring
- Transportation planning based on functional zones
- Rapid response for policy decision-making in regions with limited official data
- Cross-cultural land use pattern analysis

Keywords: Land Use, POI, Geospatial Semantics, Deep Learning, Neural Network, Word Embedding, Semantic Granularity, Spatial Scale, Geographic Context

Produced by: Oak Ridge National Laboratory

Curated in GEE by: Samapriya Roy

Last updated in GEE: 2025-05-15
