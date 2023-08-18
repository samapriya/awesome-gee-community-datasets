# DynQual Global Surface Water Quality Dataset

Maintaining optimal surface water quality is essential for preserving ecosystems and ensuring safe human water utilization. However, our understanding of surface water quality relies heavily on data from monitoring stations, which are spatially limited and temporally fragmented. Addressing these limitations, we introduce the dynamical surface water quality model (DynQual). This model offers simulations of water temperature (Tw), as well as concentrations of total dissolved solids (TDS), biological oxygen demand (BOD), and fecal coliform (FC). DynQual operates at a daily time step and boasts a spatial resolution of 5 arcmin (∼ 10 km).

This comprehensive global model allows us to evaluate its performance against real-world water quality observations. In addition, we present insights into spatial patterns and temporal trends of TDS, BOD, and FC concentrations spanning the years 1980 to 2019. Our analysis identifies dominant sectors contributing to surface water pollution. Remarkably, DynQual reveals widespread multi-pollutant hotspots, particularly in northern India and eastern China, though water quality issues extend across all regions worldwide. The most significant declines in water quality have occurred in developing regions, especially sub-Saharan Africa and South Asia. Researchers can access the open-source model code (Jones et al., 2023) as well as the global datasets encompassing simulated hydrology, Tw, TDS, BOD, and FC at 5 arcmin resolution on a monthly basis (Jones et al., 2022b). These datasets hold the potential to enhance diverse studies ranging from ecological research to human health and water scarcity assessments. Discover more at [DynQual Model Code](https://doi.org/10.5281/zenodo.7932317) and [Global Surface Water Quality Datasets](https://doi.org/10.5281/zenodo.7139222). You can read [the full paper here](https://gmd.copernicus.org/articles/16/4481/2023/)

**Please refer to the original paper on guidance on displaying the concentration maps, the authors recommend these are only plotted above a given discharge/channelStorage threshold**

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Datasets preprocessing
The datasets were downloaded and converted from NetCDF to Geotiff format for ingestion. Since this was a multi band monthly aggregated image and I wanted to allow the user to slice by time frame, the image bands were seperated as individual images and the overall results are image collections with date range information attached.

#### Citation

```
Jones, E. R., Bierkens, M. F. P., Wanders, N., Sutanudjaja, E. H., van Beek, L. P. H., and van Vliet, M. T. H.:
DynQual v1.0: a high-resolution global surface water quality model, Geosci. Model Dev., 16, 4481–4500, https://doi.
org/10.5194/gmd-16-4481-2023, 2023.
```

#### Dataset citation

```
Jones, E. R., Bierkens, M. F. P., Wanders, N., Sutanudjaja, E. H., van Beek, L. P. H., & van Vliet, M. T. H.
(2022). Global monthly hydrology and water quality datasets, derived from the dynamical surface water quality
model (DynQual) at 10 km spatial resolution [Data set]. In Geoscientific Model Development (Vol. 16, pp.
4481–4500). Zenodo. https://doi.org/10.5281/zenodo.7139222
```

![fc_constrained](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/62afe386-ec7b-4000-b758-4e7f655f0b4f)

#### Earth Engine Snippet

```js
var fc = ee.ImageCollection("projects/sat-io/open-datasets/DYNQUAL/fecal-coliform");
var discharge = ee.ImageCollection("projects/sat-io/open-datasets/DYNQUAL/discharge");
var tds = ee.ImageCollection("projects/sat-io/open-datasets/DYNQUAL/total-dissolved-solids");
var bod = ee.ImageCollection("projects/sat-io/open-datasets/DYNQUAL/biological-oxygen-demand");
var water_temp = ee.ImageCollection("projects/sat-io/open-datasets/DYNQUAL/water-temperature");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/DYNQUAL-EXAMPLE

#### License
Creative Commons Attribution 4.0 International Public License

Created by: Jones, E. R., Bierkens, M. F. P., Wanders, N., Sutanudjaja, E. H., van Beek, L. P. H., and van Vliet, M. T. H.

Curated in GEE by: Samapriya Roy

Keywords: water quality, discharge, water temperature, total dissolved solids, TDS, salinity, biological oxygen demand, BOD, fecal coliform, FC

