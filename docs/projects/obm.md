# OpenBuildingMap Global Building Footprints with Semantic Information

OpenBuildingMap is a comprehensive global dataset containing 2.7 billion building footprints with semantic attributes including occupancy type, height, number of stories, and floorspace. This dataset addresses critical gaps in global building data by conflating AI-derived building footprints from Google Open Buildings and Microsoft Global ML Building Footprints with crowd-sourced OpenStreetMap data, creating the most detailed and extensive building dataset available.

The dataset provides structured building information using the Global Earthquake Model (GEM) Building Taxonomy, making it particularly valuable for disaster risk assessment, urban planning, energy efficiency analysis, and multi-hazard risk modeling. By combining multiple data sources with quality-based precedence, OpenBuildingMap balances the completeness bias in OpenStreetMap while maintaining high geometric accuracy.

#### Dataset Composition

**Global Statistics**:

- **Total Buildings**: 2.693 billion footprints
- **OpenStreetMap Source**: 613 million (23%)
- **Google Source**: 1.598 billion (59%)
- **Microsoft Source**: 483 million (18%)
- **With Height Data**: 2.026 billion (75.2%)
- **With Occupancy Type**: 1.051 billion (39.0%)
- **With Floorspace**: 32 million (from OpenStreetMap only)

!!! info "Data Conflation Methodology"

    Many building footprints are duplicated in two or three of the datasets. These duplicates usually do not have a perfect overlap. This is expected, as not only different methods are used to construct the datasets; it is likely that for each of the datasets, different satellite imagery has been used. Next to that, what may be considered ten separate buildings in the one of the datasets, could be identified as a single building in another dataset. Lastly, all building footprint sources differ in their geographical coverage and completeness. Considering the aforementioned differences in the datasets, we opted for a simple conflation method, where non-overlapping buildings are added based on a priority of the source dataset. The conflation follows a strict priority order: **OpenStreetMap → Google → Microsoft**.

??? example "Expand to show height and occupancy attributes"

    <center>

    | Category      | Code   | Description |
    |:---------------|:-------|:-------------|
    | **Height**     | **H**      | Exact number of stories (e.g., `H:1` for single-story) |
    |                | **HBET**   | Range of stories (e.g., `HBET:1-3`) |
    |                | **HAPP**   | Approximate number of stories |
    |                | **HHT**    | Height in meters (e.g., `HHT:10.0`) |
    |                | **HBEX**   | Basement stories |
    | **Occupancy**  | **RES**    | Residential (e.g., `RES2` for apartments) |
    |                | **COM**    | Commercial and public |
    |                | **MIX**    | Mixed use |
    |                | **IND**    | Industrial |
    |                | **AGR**    | Agricultural |
    |                | **ASS**    | Assembly |
    |                | **GOV**    | Government |
    |                | **EDU**    | Education |
    |                | **UNK**    | Unknown |
    |                | **OCO**    | Other occupancy |

    </center>

#### Citation

```
Oostwegel, L.J.N., Schorlemmer, D., & Guéguen, P. (2025). From Footprints to Functions: a Comprehensive Global and Semantic Building Footprint Dataset. Scientific Data, 12:1699.
https://doi.org/10.1038/s41597-025-06132-z
```

#### Dataset Citation

```
Oostwegel, L.J.N., Schorlemmer, D., Lingner, L., & Evaz Zadeh, T. (2025). OpenBuildingMap. GFZ Data Services. https://doi.org/10.5880/GFZ.LKUT.2025.002
```

!!! note "Data Availability in Earth Engine"

    The OpenBuildingMap dataset is available in Google Earth Engine as Feature Collections organized by Quadtree tiles. You can use the app to zoom into a specific tile.


![obm](../images/obm.png)

#### Earth Engine Snippet

```javascript
// Load the tile grid to explore coverage and metadata
var grid = ee.FeatureCollection('projects/sat-io/open-datasets/OPEN-BUILDING-MAPS/open_buildings_grid');

// Example: Load a specific tile (Berlin area - tile 120301)
var buildings = ee.FeatureCollection('projects/sat-io/open-datasets/OPEN-BUILDING-MAPS/tiles/building_311230');

// Print tile metadata from grid
var tile_info = grid.filter(ee.Filter.eq('quadkey', '311230')).first();
print('Tile Information:', tile_info);

// Filter buildings with known occupancy types
var buildings_with_occupancy = buildings.filter(ee.Filter.neq('occupancy', 'UNK'));
print('Buildings with occupancy:', buildings_with_occupancy.size());

// Filter buildings with height information
var buildings_with_height = buildings.filter(
  ee.Filter.and(
    ee.Filter.neq('height', ''),
    ee.Filter.neq('height', null)
  )
);
print('Buildings with height:', buildings_with_height.size());

// Visualize buildings by occupancy type
var occupancyColors = {
  'RES': '3498db',   // Residential - blue
  'RES1': '3498db',  // Single-family residential
  'RES2': '2980b9',  // Multi-family residential
  'COM': 'e74c3c',   // Commercial - red
  'MIX': '9b59b6',   // Mixed use - purple
  'IND': 'f39c12',   // Industrial - orange
  'AGR': '27ae60',   // Agricultural - green
  'ASS': '16a085',   // Assembly - teal
  'GOV': '34495e',   // Government - dark gray
  'EDU': 'e67e22',   // Education - orange
  'UNK': 'bdc3c7'    // Unknown - light gray
};

// Function to style buildings by occupancy type
function styleByOccupancy(occupancyType, color) {
  var filtered = buildings.filter(ee.Filter.stringStartsWith('occupancy', occupancyType));
  return filtered.style({
    color: color,
    fillColor: color + '80',  // Add transparency
    width: 1
  });
}

// Add layers for major occupancy types
Object.keys(occupancyColors).forEach(function(type) {
  var layer = styleByOccupancy(type, occupancyColors[type]);
  Map.addLayer(layer, {}, type + ' Buildings', false);
});

// Visualize buildings by data source
var osm_buildings = buildings.filter(ee.Filter.eq('source', 'OSM'));
var google_buildings = buildings.filter(ee.Filter.eq('source', 'Google'));
var microsoft_buildings = buildings.filter(ee.Filter.eq('source', 'Microsoft'));

Map.addLayer(osm_buildings.style({color: '2ecc71', width: 1}), {}, 'OpenStreetMap', false);
Map.addLayer(google_buildings.style({color: 'e74c3c', width: 1}), {}, 'Google', false);
Map.addLayer(microsoft_buildings.style({color: '3498db', width: 1}), {}, 'Microsoft', false);

// Example: Analyze residential buildings
var residential = buildings.filter(ee.Filter.stringStartsWith('occupancy', 'RES'));
Map.addLayer(residential.style({color: '3498db', fillColor: '3498db80', width: 1}),
             {}, 'Residential Buildings', true);

// Calculate statistics
print('Total buildings:', buildings.size());
print('Residential buildings:', residential.size());
print('OSM buildings:', osm_buildings.size());
print('Google buildings:', google_buildings.size());
print('Microsoft buildings:', microsoft_buildings.size());

// Create legend for occupancy types
var legend = ui.Panel({
  style: {
    position: 'bottom-left',
    padding: '8px 15px',
    backgroundColor: 'white'
  }
});

var legendTitle = ui.Label({
  value: 'Building Occupancy Types',
  style: {
    fontWeight: 'bold',
    fontSize: '16px',
    margin: '0 0 4px 0',
    padding: '0'
  }
});
legend.add(legendTitle);

// Add color entries to legend
Object.keys(occupancyColors).forEach(function(type) {
  var colorBox = ui.Label({
    style: {
      backgroundColor: '#' + occupancyColors[type],
      padding: '8px',
      margin: '0 8px 0 0'
    }
  });

  var description = ui.Label({
    value: type,
    style: {margin: '0 0 4px 0'}
  });

  var panel = ui.Panel({
    widgets: [colorBox, description],
    layout: ui.Panel.Layout.Flow('horizontal')
  });

  legend.add(panel);
});

Map.add(legend);

// Center on tile location (adjust coordinates for your tile)
Map.setCenter(buildings.first());
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/OPEN-BUILDING-MAP

Tile Grid Explorer App: https://sat-io.earthengine.app/view/obm

#### License

This dataset is available under the [Open Data Commons Open Database License (ODbL) v1.0](https://opendatacommons.org/licenses/odbl/1-0/).

Keywords: Building Footprint, Building Height, Building Occupancy, OpenStreetMap, Global Earthquake Model, GEM Taxonomy, Disaster Risk Assessment, Urban Planning, Semantic Building Data, AI-Derived Buildings, Building Classification, Global Coverage

#### Providers

Created by: Laurens J.N. Oostwegel, Danijel Schorlemmer, Philippe Guéguen (GFZ German Research Centre for Geosciences & ISTerre)

Curated in GEE by: Samapriya Roy

Last updated: 2025-11-10
