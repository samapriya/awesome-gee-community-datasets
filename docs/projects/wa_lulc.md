# West Africa Land Use Land Cover

Started in 1999, the West Africa Land Use Dynamics project represents an effort to map land use and land cover, characterize the trends in time and space, and understand their effects on the environment across West Africa. The outcome of the West Africa Land Use Dynamics project is the production of a three-time period (1975, 2000, and 2013) land use and land cover dataset for the Sub-Saharan region of West Africa, including the Cabo Verde archipelago. The West Africa Land Use Land Cover Time Series dataset offers a unique basis for characterizing and analyzing land changes across the region, systematically and at an unprecedented level of detail.


```
Tappan, G. G., Cushing, W.M., Cotillon, S.E., Mathis, M.L., Hutchinson, J.A., Herrmann, S.M., and
Dalsted, K.J., 2016, West Africa Land Use Land Cover Time Series:
U.S. Geological Survey data release, http://dx.doi.org/10.5066/F73N21JF
```

![wa_lc](https://user-images.githubusercontent.com/6677629/115177498-f7ec6200-a094-11eb-915d-5739ed5994fb.gif)

#### Earth Engine Snippet

```js
var wa1975 = ee.Image("projects/sat-io/open-datasets/wa-datasets/wa_lc_usgs_1975");
var wa2000 = ee.Image("projects/sat-io/open-datasets/wa-datasets/wa_lc_usgs_2000");
var wa2013 = ee.Image("projects/sat-io/open-datasets/wa-datasets/wa_lc_usgs_2013");
```

#### License

Creative Commons Attribution-Share Alike 4.0 International License


Curated by: Samapriya Roy

Keywords: United States Geological Survey, USGS, Land Use, Land Cover, West Africa

Last updated: 2021-04-17
