# Global tree allometry and crown architecture (Tallo) database

The Tallo database (v1.0.0) is a collection of 498,838 georeferenced and taxonomically standardized records of individual trees for which stem diameter, height and/or crown radius have been measured. Data were compiled from 61,856 globally distributed sites and include measurements for 5,163 tree species. Tallo includes nearly 500,000 georeferenced and taxonomically standardized records from more than 5000 tree species acquired at over 60,000 sites worldwide, including data from all major terrestrial biomes and some of the world's largest ever recorded trees. The majority of trees in the database are identified to species (88%), and collectively Tallo includes data for 5163 species distributed across 1453 genera and 187 plant families. The database is publicly archived under a CC-BY 4.0 licence

You can [read the paper here](https://onlinelibrary.wiley.com/doi/full/10.1111/gcb.16302) and [download the database from](https://zenodo.org/record/6637599)

#### Citation

```
Jucker, Tommaso, Fabian Jörg Fischer, Jérôme Chave, David A. Coomes, John Caspersen, Arshad Ali, Grace Jopaul Loubota Panzou et al. "Tallo: A global
tree allometry and crown architecture database." Global change biology 28, no. 17 (2022): 5254-5268.
```

#### Dataset citation

```
Jucker, Tommaso, Fischer, Fabian, Chave, Jérôme, Coomes, David, Caspersen, John, Ali, Arshad, Loubota Panzou, Grace Jopaul, Feldpausch, Ted,
Falster, Daniel, Usoltsev, Vladimir, Adu-Bredu, Stephen, Alves, Luciana, Aminpour, Mohammad, Angoboy, Ilondea, Anten, Niels, Antin, Cécile, Askari,
Yousef, Avilés, Rodrigo Muñoz, Ayyappan, Narayanan, … Zavala, Miguel. (2022). Tallo database (1.0.0) [Data set].
Zenodo. https://doi.org/10.5281/zenodo.6637599
```

![tallo_tree_canopy_heights](https://user-images.githubusercontent.com/6677629/197394198-9234b45a-84d0-47b9-9e84-da2b518aa966.gif)

#### Earth Engine Snippet: Distance to Second Class

```js
var tallo = ee.FeatureCollection("projects/sat-io/open-datasets/tallo_database");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/TREE-ALLOMETRY-CROWN-ARCH-DATABASE

#### License

This work is licensed under [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/legalcode).

Created by: Jucker, Tommaso, et al. 2022

Curated in GEE by : Samapriya Roy

Keywords: stem diameter, tree height, crown size, tree allometry, tree architecture, forest biomass, remote sensing

Last updated on GEE: 2022-10-21
