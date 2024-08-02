# Overture Foundation Building Footprints

???+ note

    **This dataset will be updated in batches owing to the extent and size of the feature collections. These will be made available primarily in the insiders only dataset while they are ingested and tested. Once all areas have been ingested this will be made available to all users of the community catalog**

The Overture Foundation's building dataset is part of the 2024-07-22.0 data release and v1.0.0 of the schema, now available. The base, buildings, divisions, and places themes have reached General Availability (GA). The transportation theme remains in beta, and users can anticipate additional breaking changes to the transportation schema. Currently, the dataset only includes data extracted for the CONUS region.

#### Overview

The Overture Maps buildings theme describes human-made structures with roofs or interior spaces that are permanently or semi-permanently in one place (source: OSM building definition). The theme includes two feature types:

- **Building:** The most basic form of a building feature. The geometry is expected to be the most outer footprint—roofprint if traced from satellite/aerial imagery—of a building. Buildings have a boolean attribute `has_parts` that describes whether there are any associated building parts. (Currently only building layers are being added to the catalog)
- **Building Part:** A single part of a building. Building parts may share the same properties as buildings. A building part is associated with a parent building via a `building_id`.

#### Data Sources

The Overture buildings dataset is a combination of the following open building datasets:

| Source               | Type                        | Conflation Priority | Count        |
|----------------------|-----------------------------|----------------------|--------------|
| OpenStreetMap        | Community-contributed       | 1                    | ~600 Million |
| Esri Community Maps  | Community-contributed       | 2                    | ~14 Million  |
| Google Open Buildings| ML-derived roofprints (>90% precision) | 3 | ~400 Million |
| Microsoft            | ML-derived roofprints       | 4                    | ~600 Million |
| Google Open Buildings| ML-derived roofprints (<90% precision) | 5 | ~700 Million |

![overture_buildings](https://github.com/user-attachments/assets/14a18c64-b730-4158-8cd9-e44cb01c1df9)

#### Earth Engine Snippet

```js
var buildings = ee.FeatureCollection('projects/sat-io/open-datasets/OVERTURE/BUILDINGS/CONUS-EXTRACT');
Map.centerObject(buildings.first(),12)
Map.addLayer(buildings, {}, 'Buildings CONUS Extract');
```

Sample Code:  https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/OVERTURE-BUILDINGS-EXTRACT

#### License

The data from the Overture Foundation Building Dataset is available under the Open Data Commons Open Database License (ODbL).

Provided by: Overture Foundation

Curated in GEE by: Samapriya Roy

Keywords: Building Data, Overture Foundation, OpenStreetMap, Esri, Google, Microsoft

Dataset release date: 2024-07-22

Last updated in GEE: 2024-08-01


