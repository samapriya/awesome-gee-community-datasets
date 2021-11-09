# Global urban extents from 1870 to 2100

Long term, global records of urban extent can help evaluate environmental impacts of anthropogenic activities. Remotely sensed observations can provide insights into historical urban dynamics, but only during the satellite era. Here, we develop a 1 km resolution global dataset of annual urban dynamics between 1870 and 2100 using an urban cellular automata model trained on satellite observations of urban extent between 1992 and 2013. Hindcast (1870–1990) and projected (2020–2100) urban dynamics under the five Shared Socioeconomic Pathways (SSPs) were modeled. We find that global urban growth under SSP5, the fossil-fuelled development scenario, was largest with a greater than 40-fold increase in urban extent since 1870. The high resolution dataset captures grid level urban sprawl over 200 years, which can provide insights into the urbanization life cycle of cities and help assess long-term environmental impacts of urbanization and human–environment interactions at a global scale. You can [read the paper here]()

The dataset includes hindcast urban extent from 1870 to 1990 with a 10-year interval, satellite observed urban extent from 1992 to 2013 at an annual interval, and projected urban extent from 2020 to 2100 under five SSP scenarios with a 10-year interval. The datasets and entire collection are [available at Figshare](https://figshare.com/articles/dataset/High_resolution_mapping_of_global_urban_extents_from_1870_to_2100_by_integrating_data_and_model_driven_approaches/9696218)

#### Citation

```
Li, Xuecao, Yuyu Zhou, Mohamad Hejazi, Marshall Wise, Chris Vernon, Gokul Iyer, and Wei Chen. "Global urban growth between 1870 and 2100 from
integrated high resolution mapped data and urban dynamic modeling." Communications Earth & Environment 2, no. 1 (2021): 1-10.
```

#### Data Citation

```
Li, Xuecao; Zhou, Yuyu (2020): High resolution mapping of global urban extents from 1870 to 2100 by integrating data and model driven approaches.
figshare. Dataset. https://doi.org/10.6084/m9.figshare.9696218
```

#### Data Preprocessing for GEE

Dates are added to the images and the start and end date are given one year periods to be consistent with a snapshot approach rather than a continuity approach. For the projected extent scenario is added as a metadata to the images for easy sort and use as needed.


![gue](https://user-images.githubusercontent.com/6677629/140876435-baf21d84-4879-43c9-8f7e-85f6dae8bf26.gif)

#### Earth Engine Snippet

```js
var hindcast_extent = ee.ImageCollection("projects/sat-io/open-datasets/global-urban-extents/hindcast_urban_extent");
var observed_extent = ee.ImageCollection("projects/sat-io/open-datasets/global-urban-extents/observed_urban_extent");
var projected_extent = ee.ImageCollection("projects/sat-io/open-datasets/global-urban-extents/project_urban_scenarios");
```

Sample code: https://code.earthengine.google.com/ca5b1a99dc41f3b3daf8661ea3d32291


#### License
This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Created by: Li, Xuecao, Yuyu Zhou, Mohamad Hejazi, Marshall Wise, Chris Vernon, Gokul Iyer, and Wei Chen

Curated in GEE by: Samapriya Roy

Keywords: Cellular Automata, Urban sprawl, temporal trend, Nighttime lights, hindcasts, Forecast

Last updated: 2021-11-09
