# Global irrigation areas (2001 to 2015)

About 40% of global crop production takes place on irrigated land, which accounts for approximately 20% of the global farmland. The great majority of freshwater consumption by human societies is associated with irrigation, which contributes to a major modification of the global water cycle by enhancing evapotranspiration and reducing surface and groundwater runoff. In many regions of the world irrigation contributes to streamflow and groundwater depletion, soil salinization, cooler microclimate conditions, and altered land-atmosphere interactions. Despite the important role played by irrigation in food security, water cycle, soil productivity, and near-surface atmospheric conditions, its global extent remains poorly quantified. To date global maps of irrigated land are often based on estimates from circa year 2000. Here we apply artificial intelligence methods based on machine learning algorithms to satellite remote sensing and monthly climate data to map the spatial extent of irrigated areas between 2001 and 2015. We provide global annual maps of irrigated land at ≈9km resolution for the 2001-2015 and we make this dataset available online.

#### Citation:

```
Deepak Nagaraj, Eleanor Proust, Alberto Todeschini, Maria Cristina Rulli, Paolo D'Odorico,
A new dataset of global irrigation areas from 2001 to 2015, Advances in Water Resources,
Volume 152,2021,103910,ISSN 0309-1708,https://doi.org/10.1016/j.advwatres.2021.103910.
```

You can read the paper here : https://www.sciencedirect.com/science/article/pii/S0309170821000658

![Irrigation map](https://ndeepak.com/files/irr_extent.png)

#### Earth Engine Snippet
```js
var irrigation_maps = ee.ImageCollection("users/deepakna/global_irrigation_maps");
```

You can also get maps for individual years as TIF images:

```js
var highly_irrigated_areas_2001 = ee.Image("users/deepakna/global_irrigation_maps/2001")
  .expression("b(0) == 2 ? 1 : 0");
Map.addLayer(highly_irrigated_areas_2001.updateMask(highly_irrigated_areas_2001.neq(0))
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/GLOBAL-IRRIGATION-AREAS

#### Band Info: Irrigation classes are present in the band "classification"

|Band Value|Irrigation Class                                                      |
|:---------|:---------------------------------------------------------------------|
|0         |no or very little irrigation                                          |
|1         |low-to-medium irrigation (<= 2000 hectares in 86 sq km square of land)|
|2         |high irrigation (>2000 hectares in 86 sq km square of land)           |

#### License
Creative Commons Attribution 4.0 International License

Curated by: Deepak Nagaraj

Keywords: Global irrigation, agriculture, water sustainability, machine learning

Last updated: 2020-06-10
