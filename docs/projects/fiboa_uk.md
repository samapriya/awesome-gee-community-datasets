# Field Boundaries of Agriculture (FIBOA) UK Fields

???+ note

    **This dataset is part of project but is not part of a peer reviewed publication. This will be updated if and when this is converted into a paper and as it progresses through review and publication cycles.Please keep this into consideration while using this dataset**

fiboa is a collaborative initiative aimed at enhancing farm field boundary data interoperability and associated agricultural data. Introduced recently, fiboa is more than just a specification; it's a comprehensive system encompassing data adhering to the specification, ongoing discussions to refine the specs, and a vibrant community actively contributing to its development. This project focuses on fostering the creation of more data and open data concerning field boundaries and agriculture to facilitate informed decision-making processes. The emphasis lies on practical application and iterative refinement, rather than the pursuit of a perfect ontology in isolation. You can read about this [project here](https://cloudnativegeo.org/blog/2024/04/introducing-fiboa/).

## Datasets

#### UK Fields
The **ukfields** dataset is a publicly accessible Earth Engine asset comprising automatically delineated field boundaries across England, Wales,
Scotland, and Northern Ireland. This dataset provides comprehensive field boundary information for the United Kingdom, derived from harmonic
composites of Sentinel 2 imagery captured in 2021. The delineation process utilized the Segment Anything Model (SAM) developed by Meta, facilitating
efficient field segmentation at scale. Furthermore, the segmented fields have been accurately masked to a 2021 Dynamic World composite of cropland,
ensuring precise representation within the dataset.

![ukfields_os_compare_mask4](https://github.com/samapriya/awesome-gee-community-datasets/assets/3259632/dfd167a3-048b-4a7b-a46f-3ffae43f7dfe)

#### Dataset preprocessing
This dataset was further processed to drop empty geometries from the feature collection

#### Dataset Citation

```
Bancroft, S., & Wilkins, J. (2024). UKFields (1.0.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.11110206
```

![fiboa_uk-compressed](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/44e575bb-3318-41a6-bd0c-8e0a3961b31b)

#### Earth Engine Snippet

```js
var uk_fields = ee.FeatureCollection("projects/sat-io/open-datasets/UK-FIELDS");

Map.centerObject(uk_fields.first(),12)
var empty = ee.Image().byte();
var outline = empty.paint({
  featureCollection: uk_fields,
  color: 'random',
  width: 3
});

Map.addLayer(outline.randomVisualizer(), {opacity:0.8}, 'UK Fields')
Map.setOptions("SATELLITE")
```
Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/FIBOA-UK-FIELDS

#### License
This product is licensed under a Creative Commons Attribution 4.0 International license.

Curated in GEE by: Samapriya Roy and [Samuel Bancroft](https://github.com/Spiruel)

Keywords: fields, agriculture, UK, england, scotland, wales, northern-ireland

Last updated: 2024-05-11
