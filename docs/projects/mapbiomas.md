# Mapbiomas Annual land cover and use maps

The Brazilian Annual Land Use and Land Cover Mapping Project is an initiative that involves a collaborative network of biomes, land use, remote sensing, GIS and computer science experts that rely on Google Earth Engine platform and its cloud processing and automated classifiers capabilities to generate Brazil’s annual land use and land cover time series. MapBiomas Project - is a multi-institutional initiative to generate annual land cover and use maps using automatic classification processes applied to satellite images. The complete description of the project can be [found here](http://mapbiomas.org).

Scale: 30 m,
Data Type: Multiple raster datasets and types

Please use Citation:
```
"Project MapBiomas - Collection [version] of Brazilian Land Cover & Use Map Series, accessed on [date] through the link: [LINK]"
```

Shared Under: Creative Commons Attribution-Share Alike 4.0 International License

![MapBiomas](https://user-images.githubusercontent.com/6677629/81698669-5300e800-9434-11ea-9c5f-e8bf9588e737.gif)

#### Earth Engine Snippet
```js
//From collection 6
assets: {
    integration: 'projects/mapbiomas-workspace/public/collection6/mapbiomas_collection60_integration_v1',
    transitions: 'projects/mapbiomas-workspace/public/collection6/mapbiomas_collection60_transitions_v1',
    vectors: [
        'projects/mapbiomas-workspace/AUXILIAR/areas-protegidas',
        'projects/mapbiomas-workspace/AUXILIAR/municipios-2016',
        'projects/mapbiomas-workspace/AUXILIAR/estados-2017',
        'projects/mapbiomas-workspace/AUXILIAR/biomas-2019',
        'projects/mapbiomas-workspace/AUXILIAR/bacias-nivel-1',
        'projects/mapbiomas-workspace/AUXILIAR/bacias-nivel-2',
    ]
},
```

Add repo link: https://code.earthengine.google.com/?accept_repo=users/mapbiomas/user-toolkit

Extra Info: [GitHub Tutorial](https://github.com/mapbiomas-brazil/user-toolkit)

Curated by: [MapBiomas](https://mapbiomas.org/)

Keywords: Mapbiomas, Land Use, Land Cover

Last updated: [Refer to webpage](https://mapbiomas.org/)

Last updated on GEE community datasets: 2022-05-10


#### Changelog

* Catalog links updated to v6 additional dataset links were added.
