# Global Fungi Database

Fungi are essential components of ecosystems, contributing to vital functions such as carbon cycling, decomposition, plant associations, and pathogenicity. However, our knowledge of fungal biogeography and the factors driving these patterns is limited. To address this gap, we compiled and validated data on soil fungal communities from terrestrial environments, including soil and plant-associated habitats. This valuable dataset, available through the user interface at https://globalfungi.com, encompasses over 600 million observations of fungal sequences derived from more than 17,000 samples, with precise geographic information and metadata from 178 original studies. The dataset, which includes millions of unique nucleotide sequences of the fungal internal transcribed spacers (ITS) 1 and 2, represents an extensive atlas of global fungal distribution. It is designed to facilitate the integration of third-party data, promoting further exploration and enhancing our understanding of fungal biogeography and its environmental drivers. You can read the [details in the paper here](https://www.nature.com/articles/s41597-020-0567-7) and you can get to the [database here](https://globalfungi.com/).

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Dataset preprocessing
Feature field were transformed to make sure it meets the limits for characters. The overall global extract was created from globalfungi.com and converted to a shapefile. Changes are

```
'year_of_sampling': 'sample_yr'
'ITS1_extracted': 'ITS1_extr',
'ITS3_extracted': 'ITS2_extr'
```

#### Citation

```
Větrovský, Tomáš, Daniel Morais, Petr Kohout, Clémentine Lepinay, Camelia Algora, Sandra Awokunle Hollá, Barbara Doreen Bahnmann et al.
"GlobalFungi, a global database of fungal occurrences from high-throughput-sequencing metabarcoding studies." Scientific Data 7, no. 1 (2020): 228.
```

#### Dataset details

```
GlobalFungi dataset release 4 (20.7.2021). Taxonomy based on UNITE version 8.2 (4.2.2020).
Actual number of samples in the database: 57184; actual number of studies included: 515.
Number of ITS sequence variants: 481 799 996; number of ITS1 sequences 791 513 743; number of ITS2 sequences 2 892 377 338.
```

![globa-fungi](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/b281e047-5fa0-4f45-9b6c-a42346e9d640)

#### Earth Engine snippet

```js
var table = ee.FeatureCollection("projects/sat-io/open-datasets/GLOBAL-FUNGI-DB/global-fungi-db-20230627");
```

Sample code : https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/GLOBAL-FUNGI-DATABASE

#### License
This database is available under a Creative Commons Attribution 4.0 International License

Curated by: Větrovský, Tomáš, et al. 2020

Keywords: Global Fungi database, Global dataset, carbon cycling

Last updated: June 27, 2023
