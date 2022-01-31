# Long-term Gap-free High-resolution Air Pollutants (LGHAP)

A Long-term Gap-free High-resolution Air Pollutants concentration dataset (abbreviated as LGHAP) is of great significance for environmental management and earth system science analysis. In the current release of LGHAP aerosol dataset (LGHAP.v1), the 21-year-long (2000–2020) gap free AOD, PM2.5 and PM10 grids with a 1-km resolution covering the land area of China was provided. You can read the [accepted preprint here](https://essd.copernicus.org/preprints/essd-2021-404/essd-2021-404.pdf)

Specifically, data gaps in daily AOD imageries from MODIS aboard Terra were reconstructed based on a set of AOD data tensors acquired from satellites, numerical analysis, and in situ air quality data via integrative efforts of spatial pattern recognition for high dimensional gridded image analysis and knowledge transfer in statistical data mining.

#### Citation

```
Bai, K., Li, K., Ma, M., Li, K., Li, Z., Guo, J., Chang, N.-B., Tan, Z., and Han, D.: LGHAP: a Long-term Gap-free High-resolution Air Pollutants concentration dataset derived
via tensor flow based multimodal data fusion, Earth Syst. Sci. Data Discuss. [preprint], https://doi.org/10.5194/essd-2021-404, in review, 2021.
```

#### Data Citation

```
Kaixu Bai, Ke Li, Zhuo Tan, Di Han, & Jianping Guo. (2021). Daily 1-km gap-free AOD grids in China, v1 (2000–2020). [Data set].
Zenodo. https://doi.org/10.5281/zenodo.5652257

Kaixu Bai, Ke Li, Zhuo Tan, Di Han, & Jianping Guo. (2021). Daily 1-km gap-free PM2.5 grids in China, v1 (2000–2020). [Data set].
Zenodo. https://doi.org/10.5281/zenodo.5652265

Kaixu Bai, Ke Li, Zhuo Tan, Di Han, & Jianping Guo. (2021). Daily 1-km gap-free PM10 grids in China, v1 (2000–2020). [Data set].
Zenodo. https://doi.org/10.5281/zenodo.5652263

Kaixu Bai, Ke Li, Zhuo Tan, Di Han, & Jianping Guo. (2021). Monthly averaged 1-km gap-free AOD, PM2.5, and PM10 grids in China, v1 (2000–2020). [Data set].
Zenodo. https://doi.org/10.5281/zenodo.5655797

Kaixu Bai, Ke Li, Zhuo Tan, Di Han, & Jianping Guo. (2021). Annual mean 1-km gap-free AOD, PM2.5, and PM10 grids in China, v1 (2000–2020). [Data set].
Zenodo. https://doi.org/10.5281/zenodo.5655807
```

#### Data preprocessing
All datasets were provided as netCDF file formats and the authors did provide some code for conversation to geotiff. Their code was modified to support multithreaded batch processing along with the addition of LZW compression. Overall uncompressed size was approximately 4 TB which post ingestion across all assets was brought down to 246.65 GB. The code was also adjusted to handle tiling for optimizing output files. Additionally date were added to the GEE assets for quick filter and sorting.

<center>


|Collection Name |Collection Path                                     |
|----------------|----------------------------------------------------|
|AOD_daily       |projects/sat-io/open-datasets/LGHAP/AOD_daily       |
|AOD_monthly_avg |projects/sat-io/open-datasets/LGHAP/AOD_monthly_avg |
|AOD_yearly_avg  |projects/sat-io/open-datasets/LGHAP/AOD_yearly_avg  |
|PM10_daily      |projects/sat-io/open-datasets/LGHAP/PM10_daily      |
|PM10_monthly_avg|projects/sat-io/open-datasets/LGHAP/PM10_monthly_avg|
|PM10_yearly_avg |projects/sat-io/open-datasets/LGHAP/PM10_yearly_avg |
|PM25_daily      |projects/sat-io/open-datasets/LGHAP/PM25_daily      |
|PM25_monthly_avg|projects/sat-io/open-datasets/LGHAP/PM25_monthly_avg|
|PM25_yearly_avg |projects/sat-io/open-datasets/LGHAP/PM25_yearly_avg |


</center>

![lghap](https://user-images.githubusercontent.com/6677629/151752288-4c75daf9-4e4c-44e8-9d35-149d562fd687.gif)


#### Earth Engine Snippet

```js
var aod_daily = ee.ImageCollection("projects/sat-io/open-datasets/LGHAP/AOD_daily");
var aod_monthly_avg = ee.ImageCollection("projects/sat-io/open-datasets/LGHAP/AOD_monthly_avg");
var aod_yearly_avg = ee.ImageCollection("projects/sat-io/open-datasets/LGHAP/AOD_yearly_avg");
var pm10_daily = ee.ImageCollection("projects/sat-io/open-datasets/LGHAP/PM10_daily");
var pm10_monthly_avg = ee.ImageCollection("projects/sat-io/open-datasets/LGHAP/PM10_monthly_avg");
var pm10_yearly_avg = ee.ImageCollection("projects/sat-io/open-datasets/LGHAP/PM10_yearly_avg");
var pm25_daily = ee.ImageCollection("projects/sat-io/open-datasets/LGHAP/PM25_daily");
var pm25_monthly_avg = ee.ImageCollection("projects/sat-io/open-datasets/LGHAP/PM25_monthly_avg");
var pm25_yearly_avg = ee.ImageCollection("projects/sat-io/open-datasets/LGHAP/PM25_yearly_avg");
```

Sample Code: https://code.earthengine.google.com/dd31cd3ab59bf2a1333a596b0bf44884

#### License
This work is distributed under the Creative Commons Attribution 4.0 International License

Created by: Kaixu Bai; Ke Li; Zhuo Tan; Di Han; Jianping Guo

Curated by: Samapriya Roy

Keywords: AOD, PM2.5, PM10, Gap free
