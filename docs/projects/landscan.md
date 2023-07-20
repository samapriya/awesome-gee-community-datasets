# LandScan Population Data

The LandScan Program was initiated at Oak Ridge National Laboratory (ORNL) in 1997 to address the need for improved estimates of population for consequence assessment. For example, natural and manmade disasters across the globe place vast populations at risk, often with little or no advance warning. It was critical to develop highly resolved estimates so that they were useful to evaluate to events across multiple geographic scales. This has been an annual product since 1998.

Building on the modeling approach developed for LandScan Global, and taking advantage of higher quality data available for the U.S., we improved on both the spatial and the temporal resolution with our first version of LandScan USA in 2004. LandScan USA was created with the goal of capturing the diurnal variation of population that is critical for a variety of analyses and actions including emergency preparedness and response. In 2016, the original LandScan USA model was re-engineered to incoroporate advances in geospatial technology, machine learning approaches, and new input data sources. Since then, we have made annual improvements to the underlying model and released a new version of the dataset each year.

Around the time LandScan USA was first initiated, ORNL was also pioneering work in machine learning and computer vision, specifically to identify anthropogenic signals apparent in overhead imagery. This work ultimately enabled rapid, large-scale detection of human settlements from high resolution imagery and became the basis for early efforts to develop an improved resolution population distribution outside the U.S. known as Landscan HD. LandScan HD model employs a mixture of multi-modal data fusion, spatial data science, big data resources, and satellite imagery exploitation. The first country-scale LandScan HD dataset was created in 2014 and a continuous stream of new country-scale datasets have been developed ever since.

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Paper Citation

**LandScan Global 2021 for [other years find citation information here](https://landscan.ornl.gov/citations)**

```
Sims, K., Reith, A., Bright, E., McKee, J., & Rose, A. (2022). LandScan Global 2021 [Data set]. Oak Ridge National Laboratory. https://doi.org/10.
48690/1527702
```

**LandScan USA 2021 for [other years find citation information here](https://landscan.ornl.gov/citations)**

```
Weber, E., Moehl, J., Weston, S., Rose, A., Brelsford, C., & Hauser, T. (2022). LandScan USA 2021 [Data set]. Oak Ridge National Laboratory. https://
doi.org/10.48690/1527701
```

**LandScan HD 2021 for [find citation information for each country here](https://landscan.ornl.gov/citations)**


![landscan_global](https://user-images.githubusercontent.com/6677629/192157803-149b5efe-4aba-4e39-848b-de9fdf964f1b.gif)

#### Earth Engine Snippet: LANDSCAN GLOBAL

```js
var landscan_global = ee.ImageCollection("projects/sat-io/open-datasets/ORNL/LANDSCAN_GLOBAL");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/LANDSCAN-GLOBAL

#### Earth Engine Snippet: LANDSCAN USA

```js
var landscan_usa_night = ee.ImageCollection("projects/sat-io/open-datasets/ORNL/LANDSCAN_USA_NIGHT");
var landscan_usa_day = ee.ImageCollection("projects/sat-io/open-datasets/ORNL/LANDSCAN_USA_DAY");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/LANDSCAN-USA

#### Earth Engine Snippet: LANDSCAN HD

```js
var landscan_hd = ee.ImageCollection("projects/sat-io/open-datasets/ORNL/LANDSCAN_HD");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/LANDSCAN-HD

#### User Contributed Code

The code snippet shows how to use the Landscan Global population dataset to plot a time series chart comparing changes in the yearly population of two regions from 2000-2020.

Code link: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/LANDSCAN-POPULATION-COMPARE

Code Attribution Source: [Ujaval Gandhi](https://www.spatialthoughts.com/)

#### License

These datasets are offered under the Creative Commons Attribution 4.0 International License. Users are free to use, copy, distribute, transmit, and adapt the data for commercial and non-commercial purposes, without restriction, as long as clear attribution of the source is provided.

#### Changelog
* Landscan Global 2022 layer was released on 2023-07-05 and has now been added to existing global collection.

Created by: Oakridge National Laboratory

Curated in GEE by : Samapriya Roy

keywords: Global Population, Population count, Diurnal population, remote sensing, machine learning

Last modified: 2023-07-05

Last updated on GEE: 2023-07-20

