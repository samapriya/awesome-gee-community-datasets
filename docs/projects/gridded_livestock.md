# Gridded Livestock Density Kazakhstan (2000-2019)

This dataset provides medium-resolution (1 km) gridded livestock density estimates for horses and small ruminants (sheep and goats) in Kazakhstan from 2000 to 2019. The database was developed using random forest regression modeling, incorporating vegetation proxies, climatic factors, socioeconomic variables, topographic data, and proximity forcing variables. Each file is saved with an acronym of 'sheep_goat' for small ruminants (Sheep & goat combined) and 'horse' for horses, followed by an underscore and a year. Missing data are represented by "No data."

For detailed methodology, validation results, and further insights, please refer to the associated publication: "Gridded livestock density database and spatial trends for Kazakhstan" you can read the [paper here](https://doi.org/10.1038/s41597-023-02736-5) and the dataset is [available here](https://doi.org/10.6084/m9.figshare.23528232).

#### Citation

```
Kolluru, V., John, R., Saraf, S. et al. Gridded livestock density database and spatial trends for Kazakhstan. Sci Data 10, 839 (2023).
https://doi.org/10.1038/s41597-023-02736-5
```

#### Dataset Citation

```
KOLLURU, VENKATESH; John, Ranjeet; Saraf, Sakshi; Chen, Jiquan; Hankerson, Brett; Robinson, Sarah; et al. (2023). Gridded livestock density database and spatial trends for
Kazakhstan. figshare. Dataset. https://doi.org/10.6084/m9.figshare.23528232.v3
```

![gridded_livestock](https://github.com/user-attachments/assets/3149707c-ebd8-4b7d-bd85-4431fedd43ed)

#### Earth Engine Snippet

```js
var sheep_goat_collection = ee.Image("projects/sat-io/open-datasets/GRIDDED-LIVESTOCK/KZ_SHEEP_GOAT_DENSITY_DB");
var horse_collection = ee.Image("projects/sat-io/open-datasets/GRIDDED-LIVESTOCK/KZ_HORSE_DENSITY_DB");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/KZ-GRIDDED-LIVESTOCK

#### License
The datasets are available under a Creative Commons Attribution 4.0 International license.

Created by: Kolluru et al 2023

Curated in GEE by: Kolluru et al 2023 and Samapriya Roy

Keywords: livestock, machine learning, random forest, population, small ruminant, grazing, vegetation, grasslands, kazakhstan

Last updated in GEE: 2024-10-21
