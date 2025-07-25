# ESRI 10m Annual Land Cover (2017-2024)

Time series of annual global maps of land use and land cover (LULC) was updated to v3 with global 10m land cover from 2017-2024. The maps are derived from ESA Sentinel-2 imagery at 10m resolution. Each map is a composite of LULC predictions for 9 classes throughout the year in order to generate a representative snapshot of each year. This dataset was generated by Impact Observatory, who used billions of human-labeled pixels (curated by the National Geographic Society) to train a deep learning model for land classification. The global map was produced by applying this model to the Sentinel-2 annual scene collections on the Planetary Computer. Each of the maps has an assessed average accuracy of over 75%. These datasets produced by Impact Observatory and licensed by Esri were fetched from [Impact Observatory](https://api.impactobservatory.com/stac-aws/collections/io-10m-annual-lulc/items)

This map uses an updated model from the 10-class model and combines Grass(formerly class 3) and Scrub (formerly class 6) into a single Rangeland class (class 11). The original Esri 2020 Land Cover collection uses 10 classes (Grass and Scrub separate) and an older version of the underlying deep learning model. The [Esri 2020 Land Cover map was also produced by Impact Observatory and you can find it in GEE here](https://samapriya.github.io/awesome-gee-community-datasets/projects/esrilc2020/). The map remains available for use in existing applications. New applications should use the updated version of 2020 once it is available in this collection, especially when using data from multiple years of this time series, to ensure consistent classification.

You can find more information starting with the first release here
Kontgis, C. (2021, June 24). [Mapping the world in unprecedented detail](https://caitlin-kontgis.medium.com/mapping-the-world-in-unprecedented-detail-7c0513205b90)


#### Citation

```
Karra, Kontgis, et al. “Global land use/land cover with Sentinel-2 and deep learning.”
IGARSS 2021-2021 IEEE International Geoscience and Remote Sensing Symposium. IEEE, 2021.
```

![10m_lulc_ts](https://user-images.githubusercontent.com/6677629/187349140-d571fe8e-e979-48cf-a1a1-2f3c06b957a0.gif)


#### Class definitions
1. Water
Areas where water was predominantly present throughout the year; may not cover areas with sporadic or ephemeral water; contains little to no sparse vegetation, no rock outcrop nor built up features like docks; examples: rivers, ponds, lakes, oceans, flooded salt plains.

2. Trees
Any significant clustering of tall (~15 feet or higher) dense vegetation, typically with a closed or dense canopy; examples: wooded vegetation,  clusters of dense tall vegetation within savannas, plantations, swamp or mangroves (dense/tall vegetation with ephemeral water or canopy too thick to detect water underneath).

4. Flooded vegetation
Areas of any type of vegetation with obvious intermixing of water throughout a majority of the year; seasonally flooded area that is a mix of grass/shrub/trees/bare ground; examples: flooded mangroves, emergent vegetation, rice paddies and other heavily irrigated and inundated agriculture.

5. Crops
Human planted/plotted cereals, grasses, and crops not at tree height; examples: corn, wheat, soy, fallow plots of structured land.

7. Built Area
Human made structures; major road and rail networks; large homogeneous impervious surfaces including parking structures, office buildings and residential housing; examples: houses, dense villages / towns / cities, paved roads, asphalt.

8. Bare ground
Areas of rock or soil with very sparse to no vegetation for the entire year; large areas of sand and deserts with no to little vegetation; examples: exposed rock or soil, desert and sand dunes, dry salt flats/pans, dried lake beds, mines.

9. Snow/Ice
Large homogeneous areas of permanent snow or ice, typically only in mountain areas or highest latitudes; examples: glaciers, permanent snowpack, snow fields.

10. Clouds
No land cover information due to persistent cloud cover.

11. Rangeland
Open areas covered in homogeneous grasses with little to no taller vegetation; wild cereals and grasses with no obvious human plotting (i.e., not a plotted field); examples: natural meadows and fields with sparse to no tree cover, open savanna with few to no trees, parks/golf courses/lawns, pastures. Mix of small clusters of plants or single plants dispersed on a landscape that shows exposed soil or rock; scrub-filled clearings within dense forests that are clearly not taller than trees; examples: moderate to sparse cover of bushes, shrubs and tufts of grass, savannas with very sparse grasses, trees or other plants.

For Accuracy Assessment information visit the [ESRI release page](https://www.arcgis.com/home/item.html?id=cfcb7609de5f478eb7666240902d4d3d)

<center>

|Class Value|Remapped Value|Land Cover Class  |Hex Code|
|-----------|--------------|------------------|--------|
|1          |1             |Water             |#1A5BAB |
|2          |2             |Trees             |#358221 |
|4          |3             |Flooded Vegetation|#87D19E |
|5          |4             |Crops             |#FFDB5C |
|7          |5             |Built Area        |#ED022A |
|8          |6             |Bare Ground       |#EDE9E4 |
|9          |7             |Snow/Ice          |#F2FAFF |
|10         |8             |Clouds            |#C8C8C8 |
|11         |9             |Rangeland         |#C6AD8D |

</center>


#### Earth Engine Snippet

```js
var esri_lulc_ts= ee.ImageCollection("projects/sat-io/open-datasets/landcover/ESRI_Global-LULC_10m_TS");
```
Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/ESRI-10M-LANDCOVER

#### Credits, Attributions and License

This dataset was produced by Impact Observatory for Esri. © 2021 Esri. This dataset is available under a Creative Commons BY-4.0 license and any copy of or work based on this dataset requires the following attribution:


#### Changelog

- 2025-07-08 Added LULC 2024 to collection

- 2024-06-07 Added LULC 2023 to collection
- Example path was changed

- 2023-04-10 Added LULC 2022 to collection

Curated in GEE by: Samapriya Roy

Keywords: : landcover, landuse, lulc, 10m, global, world, sentinel, sentinel 2, impact observatory

Last updated: 2025-07-08
