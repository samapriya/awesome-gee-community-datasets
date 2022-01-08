# Plastic Inputs from Rivers into Oceans

This dataset shows a global estimate of plastic inputs from rivers into the oceans for 2010, expressed in kilograms per year. The authors used data on waste management, population density, and hydrological information to create this model. The dataset includes information on 40,760 watersheds and 182 different countries. The data is presented in a vector format.

Plastic pollution in our oceans and on our coastlines have become a major threat to ocean health worldwide. A better understanding and quantification of marine plastic sources can help in implementing mitigation strategies to alleviate the issue. The dataset can help in identifying places that require higher attention in terms of plastic waste monitoring and mitigation plans. This data can also be used as a baseline measurement for ocean plastic mass balance exercises.

This data was developed by researchers funded by The Ocean Cleanup Foundation.

#### Methodology
The amount of plastic inputs from rivers into the oceans was estimated by using data on mismanaged plastic waste production (MPW) per country, population density, topographic elevation, and location of artificial barriers (weirs and dams).

For each catchment area mismanaged plastic waste production (MPW) rates per day were calculated by combining data on waste generation by inhabitant per day and population density for the area. This data was combined with water flow per river catchment area to provide a final value for the mass of plastic released at the river’s mouth. This data was extrapolated using seasonal variations in water flow to create a year dataset. Data on population density was derived from the dataset Global 15 x 15 Minute Grids of the Downscaled Population by the Socioeconomic Data and Applications Center (SEDAC) for 182 countries. Data used to calculate MPW rates were collected from seven peer reviewed studies. Topographic information was taken from Global Land Data Assimilation System (GLDAS) hydrological model for surface/subsurface runoff and location of artificial barriers was taken from AquaStat and Global Reservoir and Dam Database (GRanD).

In total the dataset includes information for 40,760 watersheds worldwide. For the full documentation, please see the [source methodology](https://www.nature.com/articles/ncomms15611#Sec6).

#### Citation

```
lebreton, laurent; Reisser, Julia (2018): Supplementary data for 'River plastic emissions to the world's oceans'. figshare. Dataset. https://doi.org/10.6084/m9.figshare.4725541
```

#### Earth Engine Snippet

```js
var plastic = ee.FeatureCollection("projects/sat-io/open-datasets/open-ocean/river_plastic_emissions");
```

Sample Code: https://code.earthengine.google.com/b1a97a8988c176ff7fa4df5ee6509c5d

#### License

This work is licensed under the Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0). Users are free to use, copy, distribute, transmit, and adapt the work for commercial and non-commercial purposes, without restriction, as long as clear attribution of the source is provided.

Created by: Ocean Cleanup Foundation

Curated by: Samapriya Roy

Keywords: : Pollution, Society, Coral Reefs, SDG 14, Life below Water, Cities, Reefs Water, Oceans Waste, hydrology, waste management, marine plastic

Last updated: 2022-01-05
