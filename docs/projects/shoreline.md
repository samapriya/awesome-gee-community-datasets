# Global Shoreline Dataset

A new 30-m spatial resolution global shoreline vector (GSV) was developed from annual composites of 2014 Landsat satellite imagery. The semi-automated classification of the imagery was accomplished by manual selection of training points representing water and non-water classes along the entire global coastline. Polygon topology was applied to the GSV, resulting in a new characterisation of the number and size of global islands. Three size classes of islands were mapped: continental mainlands (5), islands greater than 1 km2 (21,818), and islands smaller than 1 km2 (318,868). The GSV represents the shore zone land and water interface boundary, and is a spatially explicit ecological domain separator between terrestrial and marine environments. The development and characteristics of the GSV are presented herein. An approach is also proposed for delineating standardised, high spatial resolution global ecological coastal units (ECUs). For this coastal ecosystem mapping effort, the GSV will be used to separate the nearshore coastal waters from the onshore coastal lands. The work to produce the GSV and the ECUs is commissioned by the Group on Earth Observations (GEO), and is associated with several GEO initiatives including GEO Ecosystems, GEO Marine Biodiversity Observation Network (MBON) and GEO Blue Planet.

Publication URL: https://pubs.er.usgs.gov/publication/70202401

Scale: 30m

Please use Citation:
```
Sayre, R., S. Noble, S. Hamann, R. Smith, D. Wright, S. Breyer, K. Butler, K. Van Graafeiland, C. Frye, D. Karagulle, D. Hopkins, D. Stephens, K. Kelly, Z. Basher, D. Burton, J. Cress, K. Atkins, D. Van Sistine, B. Friesen, R. Allee, T. Allen, P. Aniello, I. Asaad, M. Costello, K. Goodin, P. Harris, M. Kavanaugh, H. Lillis, E. Manca, F. Muller-Karger, B. Nyberg, R. Parsons, J. Saarinen, J. Steiner, and A. Reed. 2019. A new 30 meter resolution global shoreline vector and associated global islands database for the development of standardized ecological coastal units. Journal of Operational Oceanography, 12:sup2, S47-S56, DOI: 10.1080/1755876X.2018.1529714
```

Shared Under: Creative Commons Attribution-Share Alike 4.0 International License

![global_shorlines](https://user-images.githubusercontent.com/6677629/81495134-112d4180-927c-11ea-82db-face703c3238.gif)

#### Earth Engine Snippet
```js
var mainlands = ee.FeatureCollection('projects/sat-io/open-datasets/shoreline/mainlands');
var big_islands = ee.FeatureCollection('projects/sat-io/open-datasets/shoreline/big_islands');
var small_islands = ee.FeatureCollection('projects/sat-io/open-datasets/shoreline/small_islands');
```

Sample Code: https://code.earthengine.google.com/609a16955ed07b282fcd4bff4750f814

Extra Info: Over 100 Million+ vertices

Curated by: Samapriya Roy

Keywords: Global Shoreline, Shoreline, Oceans

Last updated: 2020-05-08
