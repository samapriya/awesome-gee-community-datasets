# Global Long-term Microwave Vegetation Optical Depth Climate Archive (VODCA)

Vegetation optical depth (VOD) describes the attenuation of radiation by plants. VOD a function of frequency as well as vegetation water content, and by extension biomass. VOD has many possible applications in studies of the biosphere, such as biomass monitoring, drought monitoring, phenology analyzes or fire risk management. We merged VOD observations from various spaceborne sensors (SSM/I, TMI, AMSR-E, AMSR2, WindSat) to create global long-term vod time series. Prior to aggregation the data has been rescaled to AMSR-E, removing systematic differences between them.

There is a product for C-band (~6.9 GHz, 2002 - 2018), X-band (10.7 GHz, 1997 - 2018) and Ku-band (~19 GHz, 1987 - 2017). The data is global sampled on a regular 0.25 degrees grid.

Variables of data in VODCA files:

* **VOD**: Unitless, Vegetation Optical Depth of the respective band
* **sensor_flag**: Bit-flag indicating which sensors contributed to each observation.
    * Values:
        * 1 = AMSR-E
        * 2 = AMSR2
        * 3 = SSM/I F8
        * 4 = SSM/I F11
        * 5 = SSM/I F13
        * 6 = TMI
        * 7 = WindSat
* **processing_flag**: Bit-flag indicating irregularities during processing affecting the quality of the observations
    * Values:
        * 0 = Everything is fine
        * 10 = AMSR-2 7.3 GHz band is used instead of 6.9 GHz
        * 11 = Sensor is scaled to matched TMI instead of AMSR-E
        * 12 = Sensor scaled without temporally overlapping observations

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.


#### Dataset preprocessing

The dataset were provided as zipped NetCDF files with subdatasets for VOD, Sensor flags and processing flags. The datasets including the subdatasets were exported as individual tif files and then stacked with the band order VOD, Sensor Flag and Processing Flag.

<center>

|Bands|Band Name      |Unit                         |
|-----|---------------|-----------------------------|
|b1   |VOD            |Unitless                     |
|b2   |Sensor Flag    |Refer to variable description|
|b3   |Processing Flag|Refer to variable description|

</center>


#### Dataset citation

```
Moesinger, Leander, Dorigo, Wouter, De Jeu, Richard, Van der Schalie, Robin, Scanlon, Tracy, Teubner, Irene, & Forkel, Matthias. (2019).
The Global Long-term Microwave Vegetation Optical Depth Climate Archive VODCA (1.0) [Data set].
Zenodo. https://doi.org/10.5281/zenodo.2575599
```

#### Paper Citation

```
Moesinger, Leander, Wouter Dorigo, Richard de Jeu, Robin van der Schalie, Tracy Scanlon, Irene Teubner, and Matthias Forkel.
"The global long-term microwave vegetation optical depth climate archive (VODCA)." Earth System Science Data 12, no. 1 (2020): 177-196.
```

![cband](https://user-images.githubusercontent.com/6677629/213619830-98c8f2f5-892e-4115-afe0-6fc02c217e8c.gif)


#### Earth Engine Snippet

```js
var cband = ee.ImageCollection("projects/sat-io/open-datasets/VODCA/C-BAND");
var kband = ee.ImageCollection("projects/sat-io/open-datasets/VODCA/K-BAND");
var xband = ee.ImageCollection("projects/sat-io/open-datasets/VODCA/X-BAND");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/VODCA

#### License
This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy and redistribute the material in any medium or format, and to transform and build upon the material for any purpose, even commercially. You must give appropriate credit, provide a link to the license, and indicate if changes were made.

Created by : Moesinger, Leander, Wouter Dorigo, Richard de Jeu, Robin van der Schalie, Tracy Scanlon, Irene Teubner, and Matthias Forkel

Curated in GEE by: Samapriya Roy

Keywords: VOD, Vegetation Optical Depth, Biomass, Vegetation water content, Microwave Remote Sensing, Biosphere, Time Series, global, vegetation

Last updated : 2023-01-19
