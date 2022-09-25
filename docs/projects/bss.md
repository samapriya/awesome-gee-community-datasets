# Bare Earth’s Surface Spectra 1980-2019

This datasets provides global bare surface area and frequency for a 30 year time range using Landsat Imagery in Google Earth Engine.


From the paper we find

*Earth’s surface dynamics provide essential information for guiding environmental and agricultural policies. Uncovered and unprotected surfaces experience several undesirable effects, which can affect soil ecosystem functions. We developed a technique to identify global bare surface areas and their dynamics based on multitemporal remote sensing images to aid the spatiotemporal evaluation of anthropic and natural phenomena. Two additional products were obtained with a similar technique: a) Earth’s bare surface frequency, which represents where and how many times a single pixel was detected as bare surface, based on Landsat series, and b) Earth’s bare soil tendency, which represents the tendency of bare surface to increase or decrease. This technique enabled the retrieval of bare surfaces on 32% of Earth’s total land area and on 95% of land when considering only agricultural areas.*

Read [the paper here](https://www.nature.com/articles/s41598-020-61408-1)

![bss](https://user-images.githubusercontent.com/6677629/121795301-1a05ea80-cbd5-11eb-8505-8d275ca64953.gif)

Use the following credit when these datasets or paper is cited:

```
Demattê, José AM, et al. "Bare earth’s Surface Spectra as a proxy for Soil Resource Monitoring."
Scientific reports 10.1 (2020): 1-11.
```

#### Earth Engine Snippet

```js
var bare_surface = ee.Image('users/geocis/BareSurfaces/BS_1980_2019');
var bare_frequency = ee.Image('users/geocis/BareSurfaces/BF_1980_2019');
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:geophysical-biological-biogeochemical/BARE_EARTH_SPECTRA

App Website: [App link here](https://geocis.users.earthengine.app/view/bare-surfaces)

Source Code to App: https://code.earthengine.google.com/6b2935468ce30e08ce693a9cc95f943c

Shared License:
This work is licensed under a Creative Commons Attribution 4.0. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Created & Curated by: Demattê, José AM, et al

Keywords: Bare Earth Surface, Soil, Geomorphology, Landsat, Bare Surface Frequency

Last updated: 2021-06-12
