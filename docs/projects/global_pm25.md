# Global Monthly Satellite-derived PM2.5

This dataset provides annual and monthly estimates of ground-level fine particulate matter (PM2.5) from 2000 to 2019. The data are derived by integrating Aerosol Optical Depth (AOD) retrievals from multiple NASA instruments—MODIS, MISR, SeaWIFS, and VIIRS—with the GEOS-Chem chemical transport model. The initial PM2.5 estimates are then calibrated using a residual Convolutional Neural Network (CNN) against global ground-based observations.

#### Key Features

* Time Span: 2000-2019 (V6.GL.01), extended through 2022 (V6.GL.02)
* AOD Data Sources: MODIS, MISR, SeaWIFS, and VIIRS
* Calibration: GEOS-Chem model and residual CNN using global ground-based observations
* Updates in V6.GL.02:

    - Updated ground-based observations for the entire time series
    - Inclusion of SNPP VIIRS retrievals
    - Extended temporal coverage through 2022

Annual and monthly datasets are provided in NetCDF (.nc) format, with gridded files using the WGS84 projection. These estimates are primarily intended to aid in large-scale studies. Annual and coarse-resolution averages correspond to a simple mean of within-grid values. Gridded datasets are provided to allow users to agglomerate data as best meets their particular needs. High-resolution (0.01° × 0.01°) datasets are gridded at the finest resolution of the information sources that were incorporated but are unlikely to fully resolve PM2.5 gradients at the gridded resolution due to influence by information sources at coarser resolution. You can read the paper [here](https://pubs.acs.org/doi/full/10.1021/acsestair.3c00054) and download the [dataset here](https://sites.wustl.edu/acag/datasets/surface-pm2-5/#V6.GL.02)

#### Citation

```
Shen, S. Li, C. van Donkelaar, A. Jacobs, N. Wang, C. Martin, R. V.: Enhancing Global Estimation of Fine Particulate Matter Concentrations by
Including Geophysical a Priori Information in Deep Learning. (2024) ACS ES&T Air. DOI: 10.1021/acsestair.3c00054
```

![pm25_monthly](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/1874cb04-953f-4c34-9749-669b82a26c37)

#### Earth Engine Snippet

```js
var pm25_monthly = ee.ImageCollection("projects/sat-io/open-datasets/GLOBAL-SATELLITE-PM25/MONTHLY")
var pm25_yearly = ee.ImageCollection("projects/sat-io/open-datasets/GLOBAL-SATELLITE-PM25/ANNUAL")
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/GLOBAL-SATELLITE-PM25


#### License
The datasets are made available under the Creative Commons Attribution 4.0 International license.

Keywords: PM2.5, Remote Sensing, MODIS, SeaWIFS, VIIRS, MISR, AOD

Provided by: [Atmospheric Composition Analysis Group](https://sites.wustl.edu/acag/) at Washington University in St Louis

Curated in GEE by: Samapriya Roy

Last updated : 2024-06-19
