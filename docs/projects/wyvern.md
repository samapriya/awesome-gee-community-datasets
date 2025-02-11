# Wyvern Open Data

Wyvern's Open Data Program provides free medium resolution (5.30 m) hyperspectral satellite imagery captured from the Dragonette hyperspectral satellite constellation. The dataset features 23 spectral bands ranging from 503nm to 799nm, with a revisit rate of 2 times a day. The initial release contains 25 images covering various land cover features including forests, wildfire events, pivot and row crop fields, coastal bathymetry, open pit mines, solar farms and well sites from across the globe. Find additional information about the [program here](https://wyvern.space/open-data/)


#### Technical Specifications

<center>

| Parameter           | Value                        |
| ------------------- | ---------------------------- |
| Spatial Resolution  | 5.30 m                       |
| Spectral Bands      | 23 bands (503-799 nm)        |
| Processing Level    | Level 1B                     |
| Bit Depth           | 12-bit (delivered as 32-bit) |
| Revisit Rate        | Every 2 days                 |
| Swath Width         | 20 km                        |
| Geographic Coverage | Global                       |

</center>

#### Spectral Band Information

Band information is preserved in the ingested image and bands are named as Band_wavelength for example Band_669nm

??? example "Expand to show Band information for Wyvern Datasets"

    <center>

    | Band Number | Band Center (nm) | Wavelength Range (nm) | Spectral Region |
    | ----------- | ---------------- | --------------------- | --------------- |
    | 1           | 500              | 480-520               | Green           |
    | 2           | 510              | 490-530               | Green           |
    | 3           | 520              | 499-541               | Green           |
    | 4           | 540              | 514-566               | Green           |
    | 5           | 550              | 528-572               | Green           |
    | 6           | 570              | 547-593               | Green           |
    | 7           | 585              | 562-608               | Yellow          |
    | 8           | 608.5            | 576-641               | Yellow          |
    | 9           | 615              | 590-640               | Yellow          |
    | 10          | 635              | 610-660               | Red             |
    | 11          | 650              | 624-676               | Red             |
    | 12          | 660              | 634-686               | Red             |
    | 13          | 670              | 643-697               | Red             |
    | 14          | 680              | 653-707               | Red             |
    | 15          | 690              | 662-718               | Red             |
    | 16          | 700              | 672-728               | Red             |
    | 17          | 712              | 684-740               | Red Edge        |
    | 18          | 722              | 693-751               | Red Edge        |
    | 19          | 735              | 706-764               | Red Edge        |
    | 20          | 750              | 720-780               | Red Edge        |
    | 21          | 765              | 734-796               | Red Edge        |
    | 22          | 782              | 751-813               | Red Edge        |
    | 23          | 800              | 768-832               | Near-Infrared   |

#### Citation

Use the following copyright notice on or adjacent to the source image data products and any adaptations or modifications including 'Value-Added Product (VAP)' and 'Derived Product (DP)' derivatives as define in the Wyvern General Terms and Conditions:

"©[YEAR] Wyvern Incorporated. All Rights Reserved."

where [YEAR] must reflect the year any given imagery data product was collected by a Wyvern satellite as reflected in the dataset’s acquisition 'datetime' metadata field.

![wyvern_app](https://github.com/user-attachments/assets/ad0fdca5-43c7-4662-9cf5-1c02806c8857)

#### Code Snippet

```js
// Load the Wyvern collection
var wyvernCollection = ee.ImageCollection('projects/sat-io/open-datasets/disaster/wyvern-open-data')
.filter(ee.Filter.eq('system:index','wyvern_dragonette-001_20240823T172127_4ef5c7ec'));
var image = wyvernCollection.first()

// Visualization parameters
var visParams = {
  // Natural Color-like composite
  naturalColor: {
    bands: ['Band_635nm', 'Band_549nm', 'Band_503nm'],
    min: 35,
    max: 188,
    gamma: 1.2
  },
  // False Color Vegetation composite (NIR, Red, Green)
  falseColor: {
    bands: ['Band_799nm', 'Band_669nm', 'Band_549nm'],
    min: 34,
    max: 145,
    gamma: 1.2
  }
};

// Add the layers to the map
Map.addLayer(image, visParams.naturalColor, 'Natural Color');
Map.addLayer(image, visParams.falseColor, 'False Color Vegetation');

// Center map on the image
Map.centerObject(image, 10);
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-events-layers/WYVERN-OPEN-DATA

App Link: https://space-geographer.projects.earthengine.app/view/wyvern-open-data

#### License

This dataset is made available under Creative Commons Attribution 4.0 International License (CC BY 4.0).

Provided by: Wyvern

Curated in GEE by: Samapriya Roy

Keywords: Hyperspectral, Open data

Last updated: 2025-02-05
