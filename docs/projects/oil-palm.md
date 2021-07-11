# Oil Palm Plantation Layers

### 1) **Oil Palm Plantation (Indonesia, Malaysia, Thailand) 1984-2017**

This paper used a landsat time series approach coupled with other datasets to determine the year in which the oil palm plantations are first detected, at which point they are 2 to 3 years of age. From this, the approximate age of the oil palm plantation in 2017 was generated.

Read [the paper here](https://www.nature.com/articles/s41597-021-00867-1)

#### Data Records
The data set is publicly accessible for download from the permanent DARE repository housed by the International Institute for Applied Systems Analysis (IIASA) (http://dare.iiasa.ac.at/85/)33. It consists of a 16-bit GeoTIFF at a resolution of 30 m with a single attribute value, i.e., the year in which the oil palm plantation was first detected. At this point, the plantation is 2 to 3 years of age. The data values range from 0 to 37 where 0 is the No Data value. Values 1 to 3 are not present and a value of 4 corresponds to the year 1984, the first year oil palm was detected, and each consecutive number represents the next year, i.e., 5 is 1985, while the maximum value of 37 corresponds to 2017.

![oil_palm](https://user-images.githubusercontent.com/6677629/121999942-acdc8b80-cd73-11eb-84be-b1e6457803cb.gif)

Use the following credit when these datasets or paper is cited:

```
Danylo, O., Pirker, J., Lemoine, G. et al. A map of the extent and year of detection of oil palm plantations in Indonesia
Malaysia and Thailand. Sci Data 8, 96 (2021). https://doi.org/10.1038/s41597-021-00867-1
```

#### Earth Engine Snippet

Since the dataset was categorical the no data value was use for masking and a Mode pyramiding policy was applied for ingestion into Google Earth Engine.

```js
var oil_palm = ee.ImageCollection("projects/sat-io/open-datasets/landcover/oil-palm-plantation-1984_2017");
```

Sample Code: https://code.earthengine.google.com/28d034a4dbe01de5e8ca781ea2712b24

App Website: [App link here](https://olhadanylo.users.earthengine.app/view/oilpalmseasia)

Source Code to App: https://code.earthengine.google.com/b569003eec6dc5d60dd6a187a9213f06

#### Shared License
This work is licensed under a Creative Commons Attribution 3.0. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Created by : Olga Danylo, et al, International Institute for Applied Systems Analysis

Curated in GEE by: Samapriya Roy

Keywords: Oil palm plantations, Indonesia, Malaysia, Thailand, Landsat, Sentinel-1

Last updated: 2021-06-19


### 2) **High resolution global industrial and smallholder oil palm map for 2019**

The dataset contains 634 100x100 km tiles, covering areas where oil palm plantations were detected. The classified images (‘oil_palm_map’ folder, in geotiff format) are the output of the convolutional neural network based on Sentinel-1 and Sentinel-2 half-year composites. The images have a spatial resolution of 10 meters and contain three classes: [1] Industrial closed-canopy oil palm plantations, [2] Smallholder closed-canopy oil palm plantations, and [3] other land covers/uses that are not closed canopy oil palm.

You can find the [paper here](https://essd.copernicus.org/articles/13/1211/2021/essd-13-1211-2021.pdf) and download the [datasets here](https://zenodo.org/record/4473715)

Use the following credit when these datasets or paper is cited:

```
Descals, Adrià, Serge Wich, Erik Meijaard, David LA Gaveau, Stephen Peedell, and Zoltan Szantoi.
"High-resolution global map of smallholder and industrial closed-canopy oil palm plantations."
Earth System Science Data 13, no. 3 (2021): 1211-1231.
```

![oil_palm_2019](https://user-images.githubusercontent.com/6677629/125210739-51fd5d80-e267-11eb-9987-03db697959c0.gif)


Cite the Data using

```
Adrià, Descals, Serge, Wich, Erik, Meijaard, David, Gaveau, Stephen, Peedell, & Zoltan, Szantoi. (2021).
High resolution global industrial and smallholder oil palm map for 2019 (Version v1) [Data set].
Zenodo. http://doi.org/10.5281/zenodo.4473715
```

#### Earth Engine Snippet

Since the dataset was categorical the no data value was use for masking and a Mode pyramiding policy was applied for ingestion into Google Earth Engine.

```js
var oil_palm = ee.ImageCollection("projects/sat-io/open-datasets/landcover/oil_palm_industrial_smallholder_2019");
```

Sample Code: https://code.earthengine.google.com/a4f48493ef6cbbc1f1fc990f6d7e03ac

#### Shared License
This work is licensed under a Creative Commons Attribution 4.0 International. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Created by : Adrià Descals et al 2021

Curated in GEE by: Samapriya Roy

Keywords: industrial, smallholder, oil palm, deep learning, global, remote sensing, Sentinel-1, Sentinel-2, convolutional neural network

Last updated: 2021-06-19
