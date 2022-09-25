# Global Landslide Catalog :NASA Goddard (1970-2019)

The Global Landslide Catalog (GLC) was developed with the goal of identifying rainfall-triggered landslide events around the world, regardless of size, impacts or location. The GLC considers all types of mass movements triggered by rainfall, which have been reported in the media, disaster databases, scientific reports, or other sources. The GLC has been compiled since 2007 at NASA Goddard Space Flight Center. This is a unique data set with the ID tag “GLC” in the landslide editor.

You can find information about the [project here](https://gpm.nasa.gov/landslides/index.html) and find source information for the [dataset here](https://catalog.data.gov/dataset/global-landslide-catalog-export)

#### Citation
```
Kirschbaum, D. B., Adler, R., Hong, Y., Hill, S., & Lerner-Lam, A. (2010). A global landslide catalog
for hazard applications: method, results, and limitations. Natural Hazards, 52(3), 561–575.
doi:10.1007/s11069-009-9401-4.

Kirschbaum, D.B., T. Stanley, Y. Zhou (In press, 2015). Spatial and Temporal Analysis of a Global
Landslide Catalog. Geomorphology. doi:10.1016/j.geomorph.2015.03.016.
```

![glc](https://user-images.githubusercontent.com/6677629/116783374-fe46ea80-aa53-11eb-90c6-077a7c184994.gif)

#### Earth Engine Snippet

```js
var glc = ee.FeatureCollection("projects/sat-io/open-datasets/events/global_landslide_1970-2019");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-events-layers/GLOBAL-LANDSLIDE-CATALOG

#### License

This dataset is intended for public access and use.

Compiled by : NASA Goddard Space Flight Center

Curated by: Samapriya Roy

Keywords: :"landslide, rainfall, NASA, GLC"

Last updated: 2021-05-01
