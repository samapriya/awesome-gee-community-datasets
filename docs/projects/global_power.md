# Predictive mapping of the global power system using open data

Read about the [methodology here](https://www.nature.com/articles/s41597-019-0347-4)

![power](https://user-images.githubusercontent.com/6677629/113477651-f857ec80-9448-11eb-93b2-71c9cb96af4a.gif)

Download the dataset [here](https://zenodo.org/record/3628142#.YGOrmWhKhPY)

Use the following credit when these datasets are cited:

```
Arderne, Christopher, NIcolas, Claire, Zorn, Conrad, & Koks, Elco E. (2020). Data from: Predictive mapping of the global power system using open data (Version 1.1.1) [Data set]. Nature Scientific Data. Zenodo. http://doi.org/10.5281/zenodo.3628142
```

Cite the paper using

```
Arderne, Christopher, Conrad Zorn, Claire Nicolas, and E. E. Koks. "Predictive mapping of the global power system using open data." Scientific data 7, no. 1 (2020): 1-12.
```

Current version: v1.1.1 released 2020-01-16
You can access the app here: https://gridfinder.org/

#### Earth Engine Snippet

```js
var lv = ee.Image("projects/sat-io/open-datasets/predictive-global-power-system/lv");
var targets = ee.Image("projects/sat-io/open-datasets/predictive-global-power-system/targets");
var transmission = ee.FeatureCollection("projects/sat-io/open-datasets/predictive-global-power-system/distribution-transmission-lines");
```

#### Resolutions
lv is at 250m, targets at 463.83 m

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/PREDICTED-GLOBAL-POWER-SYSTEMS

Shared License:
This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Curated by: Samapriya Roy

Keywords: Global transmission lines, electricity, infrastructure, power

Last updated: 2021-04-03
