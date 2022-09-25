# Global 30m Height Above the Nearest Drainage

Read about the [methodology here](https://www.researchgate.net/publication/301559649_Global_30m_Height_Above_the_Nearest_Drainage)

![image](https://user-images.githubusercontent.com/169821/83188656-541e5e80-a130-11ea-8443-936e13aa8a62.png)

Or get it from https://gena.users.earthengine.app/view/global-hand

Use the following credit when these data are cited:

```
Donchyts, Gennadii, Hessel Winsemius, Jaap Schellekens, Tyler Erickson, Hongkai Gao, Hubert Savenije, and Nick van de Giesen. "Global 30m Height Above the Nearest Drainage (HAND)",
Geophysical Research Abstracts, Vol. 18, EGU2016-17445-3, 2016, EGU General Assembly (2016).
```

#### Earth Engine Snippet

```js
var hand30_100 = ee.ImageCollection("users/gena/global-hand/hand-100").mosaic()
var hand30_1000 = ee.Image("users/gena/GlobalHAND/30m/hand-1000")
var hand90_1000 = ee.Image("users/gena/GlobalHAND/90m-global/hand-1000")
```

#### Resolutions
30 and 90 - cell resolution, 100 and 1000 - number of river head threshold cells

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/GLOBAL-HEIGHT-ABV-NEAREST-DRAINAGE

Shared License:
This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Source and Curated by: Donchyts/Deltares

Keywords: Global Hand, Hydrology, drainage

Last updated: ~2017
