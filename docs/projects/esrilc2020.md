# ESRI 2020 Global Land Use Land Cover from Sentinel-2

This layer displays a global map of land use/land cover (LULC). The map is derived from ESA Sentinel-2 imagery at 10m resolution. It is a composite of LULC predictions for 10 classes throughout the year in order to generate a representative snapshot of 2020. This map was produced by a deep learning model trained using over 5 billion hand-labeled Sentinel-2 pixels, sampled from over 20,000 sites distributed across all major biomes of the world.

The underlying deep learning model uses 6 bands of Sentinel-2 surface reflectance data: visible blue, green, red, near infrared, and two shortwave infrared bands. To create the final map, the model is run on multiple dates of imagery throughout the year, and the outputs are composited into a final representative map of 2020.

Processing platform
Sentinel-2 L2A/B data was accessed via Microsoft’s Planetary Computer and scaled using Microsoft Azure Batch.

You can find more information here
Kontgis, C. (2021, June 24). [Mapping the world in unprecedented detail](https://caitlin-kontgis.medium.com/mapping-the-world-in-unprecedented-detail-7c0513205b90)


#### Citation

```
Karra, Kontgis, et al. “Global land use/land cover with Sentinel-2 and deep learning.”
IGARSS 2021-2021 IEEE International Geoscience and Remote Sensing Symposium. IEEE, 2021.
```

![esri_lulc](https://user-images.githubusercontent.com/6677629/123455559-77237800-d5a7-11eb-8c05-5bea30d1a092.gif)


#### Class definitions
1. Water
Areas where water was predominantly present throughout the year; may not cover areas with sporadic or ephemeral water; contains little to no sparse vegetation, no rock outcrop nor built up features like docks; examples: rivers, ponds, lakes, oceans, flooded salt plains.

2. Trees
Any significant clustering of tall (~15-m or higher) dense vegetation, typically with a closed or dense canopy; examples: wooded vegetation,  clusters of dense tall vegetation within savannas, plantations, swamp or mangroves (dense/tall vegetation with ephemeral water or canopy too thick to detect water underneath).

3. Grass
Open areas covered in homogenous grasses with little to no taller vegetation; wild cereals and grasses with no obvious human plotting (i.e., not a plotted field); examples: natural meadows and fields with sparse to no tree cover, open savanna with few to no trees, parks/golf courses/lawns, pastures.

4. Flooded vegetation
Areas of any type of vegetation with obvious intermixing of water throughout a majority of the year; seasonally flooded area that is a mix of grass/shrub/trees/bare ground; examples: flooded mangroves, emergent vegetation, rice paddies and other heavily irrigated and inundated agriculture.

5. Crops
Human planted/plotted cereals, grasses, and crops not at tree height; examples: corn, wheat, soy, fallow plots of structured land.

6. Scrub/shrub
Mix of small clusters of plants or single plants dispersed on a landscape that shows exposed soil or rock; scrub-filled clearings within dense forests that are clearly not taller than trees; examples: moderate to sparse cover of bushes, shrubs and tufts of grass, savannas with very sparse grasses, trees or other plants

7. Built Area
Human made structures; major road and rail networks; large homogenous impervious surfaces including parking structures, office buildings and residential housing; examples: houses, dense villages / towns / cities, paved roads, asphalt.

8. Bare ground
Areas of rock or soil with very sparse to no vegetation for the entire year; large areas of sand and deserts with no to little vegetation; examples: exposed rock or soil, desert and sand dunes, dry salt flats/pans, dried lake beds, mines.

9. Snow/Ice
Large homogenous areas of permanent snow or ice, typically only in mountain areas or highest latitudes; examples: glaciers, permanent snowpack, snow fields.

10. Clouds
No land cover information due to persistent cloud cover.

For Accuracy Assesment information visit the [ESRI release page](https://www.arcgis.com/home/item.html?id=d6642f8a4f6d4685a24ae2dc0c73d4ac)

<center>

|Category|Land Cover Class  |Hex Code|
|:------:|:----------------:|:------:|
|1       |No Data           |#FFFFFF |
|2       |Water             |#1A5BAB |
|3       |Trees             |#358221 |
|4       |Grass             |#A7D282 |
|5       |Flooded Vegetation|#87D19E |
|6       |Crops             |#FFDB5C |
|7       |Scrub/Shrub       |#EECFA8 |
|8       |Built Area        |#ED022A |
|9       |Bare Ground       |#EDE9E4 |
|10      |Snow/Ice          |#F2FAFF |
|11      |Clouds            |#C8C8C8 |

</center>


#### Earth Engine Snippet

```js
var esri_lulc2020= ee.ImageCollection("projects/sat-io/open-datasets/landcover/ESRI_Global-LULC_10m")
```
Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/ESRI-LULC-2020

#### Acknowledgements

Training data for this project makes use of the National Geographic Society Dynamic World training dataset, produced for the Dynamic World Project by National Geographic Society in partnership with Google and the World Resources Institute.

#### Credits, Attributions and License

This dataset was produced by Impact Observatory for Esri. © 2021 Esri. This dataset is available under a Creative Commons BY-4.0 license and any copy of or work based on this dataset requires the following attribution:

```
This dataset is based on the dataset produced for the Dynamic World Project
by National Geographic Society in partnership with Google and the World Resources Institute.
```

Data download page: [Esri 2020 Land Cover Downloader](https://www.arcgis.com/home/item.html?id=fc92d38533d440078f17678ebc20e8e2)

Curated in GEE by: Samapriya Roy

Keywords: : land, cover, land use, land cover, lulc, 10m, global, world, sentinel, sentinel-2, sentinel 2, impact observatory, impact, 2020, deep learning

Last updated: 2021-06-25
