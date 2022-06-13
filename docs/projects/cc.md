# Chesapeake Bay High Resolution Land Cover Dataset (2013-2014)

This raster dataset was developed as part of the Land Cover Project, a cooperative agreement between the Chesapeake Conservancy and the National Park Service funded through an interagency agreement with the Environmental Protection Agency. Virginia Geographic Information Network (VGIN) coordinated with Worldview Solutions the creation of a separate VA statewide high-resolution land cover dataset, which has unique class names and descriptions. For the purposes of a matching bay-wide dataset, this VA dataset was reclassified and some classes were edited to better match the Chesapeake Bay Dataset class definitions below.

High Resolution mapping was used to develop consistent and extremely accurate land cover dataset for all the counties that comprise the Chesapeake Bay watershed. This land cover was created based on 2014 National Agriculture Imagery Program (NAIP) aerial imagery.

Dataset created and developed by the Conservation Innovation Center at the Chesapeake Conservancy. The creation of this dataset was made possible as a result of a cooperative agreement between the Chesapeake Conservancy and the National Park Service being funded through an interagency agreement with the Environmental Protection Agency. This dataset will enhance the ability to guide the most efficient use of resources in the Bay as well as aid the identification of priorities for conservation and restoration. Created based on 2013/2014 National Agriculture Imagery Program (NAIP) aerial imagery. You can find [additional information here](https://www.chesapeakeconservancy.org/conservation-innovation-center/high-resolution-data/land-cover-data-project/)

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Citation

```
Conservation Innovation Center at the Chesapeake Conservancy. Chesapeake Bay High Resolution Land Cover Dataset (2013-2014). Accessed [Month
Year] at https://www.chesapeakeconservancy.org/conservation-innovation-center/high-resolution-data/land-cover-data-project/
```

![CC_small](https://user-images.githubusercontent.com/6677629/173283180-ffd12d6d-e6b5-4118-a60e-4b1d51507ff5.gif)

#### Earth Engine Snippet

```js
var chesapeake = ee.Image("projects/earthengine-legacy/assets/projects/sat-io/open-datasets/HRLC/Baywide_13Class_20132014");
```

Sample Code: https://code.earthengine.google.com/5d6ecc3a93350f9670f063b7f3c0fe6c


#### License

The dataset is released under an assumed CC0 1.0 Universal (CC0 1.0) Public Domain Dedication. The organizations responsible for generating and funding this dataset make no representations of any kind including, but not limited to the warranties of merchantability or fitness for a particular use, nor are any such warranties to be implied with respect to the data. Although every effort has been made to ensure the accuracy of information, errors may be reflected in data supplied. The user must be aware of data conditions and bear responsibility for the appropriate use of the information with respect to possible errors.

Produced by: Conservation Innovation Center at the Chesapeake Conservancy

Curated in GEE by: Samapriya Roy

Keywords: Land Use, Land Cover, Urban Watch, Remote Sensing, High Resolution, Chesapeake Bay

Last updated on GEE: 2022-06-12
