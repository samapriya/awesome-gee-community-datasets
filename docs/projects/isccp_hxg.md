# International Satellite Cloud Climatology Project: HXG Cloud Cover

The data consists of one variable 'cloud' from the  ISCCP HXG, dataset as retrieved from the  NCEI in September of 2021. Quoting from the ISCCP website (isccp.giss.nasa.gov) :

The International Satellite Cloud Climatology Project (ISCCP) was established in 1982 as part of the World Climate Research Program (WCRP) to collect weather satellite radiance measurements and to analyze them to infer the global distribution of clouds, their properties, and their diurnal, seasonal and interannual variations. The resulting datasets and analysis products are being used to study the role of clouds in climate, both their effects on radiative energy exchanges and their role in the global water cycle.

The "H" series of data products is a high spatial resolution (0.1 degree) version of the ISCCCP dataset which is documented at:
https://data.amerigeoss.org/es/dataset/97db2b39-9602-4501-a3de-421ab2375027

The ISCCP H-Series Climate Data Record consists of several parts

1. ISCCP H-Series dataset
2. ISCCP-Basic H-Series
3. Ancillary and input datasets.

ISCCP H Series data The full ISCCP dataset consists of netCDF files containing various derived cloud parameters. The H-Series data includes several products. These include: HXS (H-series pixel level single satellite - not in netcdf), HXG (H-series pixel level gridded), HGG (H-series Gridded Global), HGH (H-series gridded monthly by hour), and * HGM ( H-series Gridded Monthly). The netCDF files are not structured with CF-standard names. Data variables are unitless and rely on data tables that are needed to represent each geophysical variable. Keeping ISCCP H-Series in this native format ensures that existing "power users" will be able to continue using the data.ISCCP Basic H Series ISCCP Basic files contains a subset of the cloud variables and products available in the full ISCCP dataset. It consists of remapped, calibrated, and subsetted variables following CF-conventions. In addition, the netCDF files follow full netCDF CF and ACDD Conventions. These files are intended to be use by new and/or less advanced users that may want to use cloud data, but do not need the full ISCCP dataset. These were converted to Geotiff files for use from the netCDF files.

The values in the file are as follows: 0 (no cloud) 1 (cloud) and 255 (NoData)

#### Citation

```
Rossow, WB., RA Schiffer, 1999: Advances in understanding clouds from ISCCP. BULLETIN OF THE AMERICAN
METEOROLOGICAL SOCIETY, 80, 2261-2287.
```

![isccp_jan_dec](https://user-images.githubusercontent.com/6677629/136728573-d4368020-2b70-4e62-9f5e-992c9f9b1a66.gif)

#### Earth Engine Snippet: HiHydro Additional Layers

```js
var isccp = ee.ImageCollection('projects/sat-io/open-datasets/isccp/hxg');
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/HXG-CLOUD-COVER

#### License
Public Domain/No restrictions (CC0): Under the terms of this license you are free to use the material for any purpose without any restrictions.

Preprocessed by: Michael Lefsky

Curated by: Samapriya Roy & Michael Lefsky

Keywords: ISCCP, Clouds,  International Satellite Cloud Climatology Project, WCRP, World Climate Research Program
