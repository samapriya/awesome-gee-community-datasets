# Randolph Glacier Inventory

The Randolph Glacier Inventory [RGI](https://www.glims.org/RGI) is a globally complete inventory of glacier outlines (excluding the ice sheets in Greenland and Antarctica). It is a subset of the database compiled by the Global Land Ice Measurements from Space [GLIMS](https://www.glims.org/) initiative. While GLIMS is a multi-temporal database with an extensive set of attributes, the RGI is intended to be a snapshot of the world’s glaciers at a specific target date, which in RGI 7.0 and all previous versions has been set as close as possible to the year 2000 (although in fact its range of dates can still be substantial in some regions). The RGI includes outlines of all glaciers larger than 0.01 km², which is the recommended minimum of the World Glacier Inventory. You can read more about the dataset in the [user guide here](https://www.glims.org/rgi_user_guide/welcome.html)

#### Dataset citation

```
RGI Consortium, . (2023). Randolph Glacier Inventory - A Dataset of Global Glacier Outlines, Version 7 [Data Set]. Boulder,
Colorado USA. National Snow and Ice Data Center. https://doi.org/10.5067/F6JMOVY5NAVZ. Date Accessed 01-04-2024.
```

#### Earth Engine Snippet

```js
var glacier_ft = ee.FeatureCollection("projects/sat-io/open-datasets/RGI/RGI_VECTOR_MERGED");
Map.centerObject(glacier_ft.first())

// print a feature
print('first glacier feature', glacier_ft.first());

// Make a raster image out of the land area attribute.
var glacier_img = glacier_ft.reduceToImage({
properties: ['area_km2'],
reducer: ee.Reducer.first()
});

// Make a binary mask
var glacier_binary = glacier_img.gt(0).unmask();

//Add layers
Map.addLayer(glacier_binary, {min:0, max:1}, 'Glacier raster mask',false);
Map.addLayer(glacier_ft,{color:'#368BC1'},'Glacier Features')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/RANDOLPH-GLACIER-INVENTORY


#### License
The RGI is licensed for distribution under a CC-BY-4.0 license.

Curated in GEE by: Hendrik Wulf and Samapriya Roy

Keywords: glacier outlines, RGI, GLIMS

Last updated: 2024-01-04
