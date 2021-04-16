# Gridded Population of the World Version 4 Administrative Unit Center Points with Population Estimates

The Gridded Population of the World, Version 4 (GPWv4): Administrative Unit Center Points with Population Estimates, Revision 11 consists of UN WPP-adjusted population estimates and densities for the years 2000, 2005, 2010, 2015 and 2020, as well as the basic demographic characteristics (age and sex) for the year 2010. The data set also includes administrative name, land and water area, and data context by administrative unit center point (centroid) location. The center points are based on approximately 13.5 million input administrative units used in GPWv4, therefore, these files require hardware and software that can read large amounts of data into memory.

Purpose:
To provide a vector (point) version of the input administrative units used in GPWv4 with population estimates, densities, 2010 basic demographic characteristics, and administrative name, area, and data context for use in data integration.

The documentation for this data set is available [here](http://sedac.ciesin.columbia.edu/data/set/gpw-v4-admin-unit-center-points-population-estimates-rev11/docs)

Use the following citation

```
Doxsey-Whitfield, Erin, Kytt MacManus, Susana B. Adamo, Linda Pistolesi, John Squires, Olena Borkovska, and Sandra R. Baptista. "Taking advantage of the improved availability of census data: a first look at the gridded population of the world, version 4." Papers in Applied Geography 1, no. 3 (2015): 226-234.
```

![gpw](https://user-images.githubusercontent.com/6677629/113961052-1330b500-97eb-11eb-927e-00737e522592.gif)

#### Earth Engine Snippet

```js
var gpw = ee.FeatureCollection("projects/sat-io/open-datasets/sedac/gpw-v4-admin-unit-center-points-population-estimates-rev11");
```

Sample Code: https://code.earthengine.google.com/00a4d124364828026daa89aa40fdd0cf

Shared License:
This work is licensed under a Creative Commons Attribution 4.0. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Curated by: Samapriya Roy

Keywords: census geography, GPWv4, gridded population, uniform distribution

Last updated: 2021-04-07
