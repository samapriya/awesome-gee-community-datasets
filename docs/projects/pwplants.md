# Global Power Plant Database

#### release version: 1.3, release date: 2021-06-02

The Global Power Plant Database is an open-source open-access dataset of grid-scale (1 MW and greater) electricity generating facilities operating across the world.

The Database currently contains nearly 35000 power plants in 167 countries, representing about 72% of the world's capacity. Entries are at the facility level only, generally defined as a single transmission grid connection point.
Generation unit-level information is not currently available.

* The methodology for the dataset creation is given in the World Resources Institute publication ["A Global Database of Power Plants"](www.wri.org/publication/global-power-plant-database).
* Associated code for the creation of the dataset can be [found on GitHub](https://github.com/wri/global-power-plant-database).
* See also the technical note published in early 2020 on an improved methodology to [estimate annual generation](https://www.wri.org/publication/estimating-power-plant-generation-global-power-plant-database).

You can find the dataset and related details at https://datasets.wri.org/dataset/globalpowerplantdatabase

#### Citation

```
Global Energy Observatory, Google, KTH Royal Institute of Technology in Stockholm, Enipedia,
World Resources Institute. 2019. Global Power Plant Database.
Published on Resource Watch and Google Earth Engine. http://resourcewatch.org/ https://earthengine.google.com/  
```

![power_plant](https://user-images.githubusercontent.com/6677629/126026014-ea9b2332-6b0b-4be6-b781-a02faea490b5.gif)


|SNo|Property Key                  |GEE Property Key|Field Description                                                                                         |
|---|------------------------------|----------------|----------------------------------------------------------------------------------------------------------|
|1  |country                       |country         | 3 character country code corresponding to the ISO 3166-1 alpha-3 specification                           |
|2  |country_long                  |country_long    | longer form of the country designation                                                                   |
|3  |name                          |name            | name or title of the power plant, generally in Romanized form                                            |
|4  |gppd_idnr                     |gppd_idnr       | 10 or 12 character identifier for the power plant                                                        |
|5  |capacity_mw                   |capacity_mw     | electrical generating capacity in megawatts                                                              |
|6  |primary_fuel                  |primary_fuel    | energy source used in primary electricity generation or export                                           |
|7  |other_fuel1                   |other_fuel1     | energy source used in electricity generation or export                                                   |
|8  |other_fuel2                   |other_fuel2     | energy source used in electricity generation or export                                                   |
|9  |other_fuel3                   |other_fuel3     | energy source used in electricity generation or export                                                   |
|10 |commissioning_year            |cm_yr           | year of plant operation, weighted by unit-capacity when data is available                                |
|11 |owner                         |owner           | majority shareholder of the power plant, generally in Romanized form                                     |
|12 |source                        |source          | entity reporting the data; could be an organization, report, or document, generally in Romanized form    |
|13 |url                           |url             | web document corresponding to the `source` field                                                         |
|14 |geolocation_source            |geo_source      | attribution for geolocation information                                                                  |
|15 |wepp_id                       |wepp_id         | a reference to a unique plant identifier in the widely-used PLATTS-WEPP database.                        |
|16 |year_of_capacity_data         |yr_capacity     | year the capacity information was reported                                                               |
|17 |generation_gwh_2013           |gen_gwh2013     | electricity generation in gigawatt-hours reported for the year 2013                                      |
|18 |generation_gwh_2014           |gen_gwh2014     | electricity generation in gigawatt-hours reported for the year 2014                                      |
|19 |generation_gwh_2015           |gen_gwh2015     | electricity generation in gigawatt-hours reported for the year 2015                                      |
|20 |generation_gwh_2016           |gen_gwh2016     | electricity generation in gigawatt-hours reported for the year 2016                                      |
|21 |generation_gwh_2017           |gen_gwh2017     | electricity generation in gigawatt-hours reported for the year 2017                                      |
|22 |generation_gwh_2018           |gen_gwh2018     | electricity generation in gigawatt-hours reported for the year 2018                                      |
|23 |generation_gwh_2019           |gen_gwh2019     | electricity generation in gigawatt-hours reported for the year 2019                                      |
|24 |generation_data_source        |gen_dat_src     | attribution for the reported generation information                                                      |
|25 |estimated_generation_gwh_2013 |est_gen_gwh2013 | estimated electricity generation in gigawatt-hours for the year 2013 (see [2])                           |
|26 |estimated_generation_gwh_2014 |est_gen_gwh2014 | estimated electricity generation in gigawatt-hours for the year 2014 (see [2])                           |
|27 |estimated_generation_gwh_2015 |est_gen_gwh2015 | estimated electricity generation in gigawatt-hours for the year 2015 (see [2])                           |
|28 |estimated_generation_gwh_2016 |est_gen_gwh2016 | estimated electricity generation in gigawatt-hours for the year 2016 (see [2])                           |
|29 |estimated_generation_gwh_2017 |est_gen_gwh2017 | estimated electricity generation in gigawatt-hours for the year 2017 (see [2])                           |
|30 |estimated_generation_note_2013|est_gen_nt2013  | label of the model/method used to estimate generation for the year 2013 (see section on this field below)|
|31 |estimated_generation_note_2014|est_gen_nt2014  | label of the model/method used to estimate generation for the year 2014 (see section on this field below)|
|32 |estimated_generation_note_2015|est_gen_nt2015  | label of the model/method used to estimate generation for the year 2015 (see section on this field below)|
|33 |estimated_generation_note_2016|est_gen_nt2016  | label of the model/method used to estimate generation for the year 2016 (see section on this field below)|
|34 |estimated_generation_note_2017|est_gen_nt2017  | label of the model/method used to estimate generation for the year 2017 (see section on this field below)|

#### Earth Engine Snippet

```js
var global_power_plants = ee.FeatureCollection("projects/sat-io/open-datasets/global_power_plant_DB_1-3")
```

Sample Code: https://code.earthengine.google.com/1ee7aca214940accbabf7f968770f481

#### License
The Global Power Planet Database is available under a CC BY 4.0 license

Data download page: [Download v1.3 from here](https://datasets.wri.org/dataset/globalpowerplantdatabase)

Dataset created by: World Resources Institute

Curated in GEE by: Samapriya Roy

Keywords: : infrastructure, energy, climate, power, power-plants, wri

Last updated: 2021-07-16

**Note: Older version of this dataset is [available in GEE](https://developers.google.com/earth-engine/datasets/catalog/WRI_GPPD_power_plants) and might be updated to reflect in the public catalog**
