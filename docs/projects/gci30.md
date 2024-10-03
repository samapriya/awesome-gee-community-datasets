# Global Cropping Intensity Dataset 30m

The Global Cropping Intensity Dataset is the first high-resolution (30m) cropping intensity product covering the entire globe. This dataset is constructed using reconstructed time series data of the Normalized Difference Vegetation Index (NDVI) from multiple satellite sources, including Landsat-8, Sentinel-2, and MODIS. The dataset quantifies cropping intensity by enumerating the total number of valid cropping cycles, determined through a binary crop phenophase profile that distinguishes between growing and non-growing periods. To calculate average cropping intensity, the total number of valid cropping cycles is divided by three (representing three years from 2016 to 2018). The implementation of this algorithm leverages the capabilities of the Google Earth Engine (GEE) cloud computing platform to produce global cropping intensity products. You can find additional information [in the paper here](https://essd.copernicus.org/preprints/essd-2021-86/essd-2021-86-manuscript-version4.pdf)

#### Dataset Preprocessing
The dataset comprises 504 separate GeoTIFF files, each projected in GCS_WGS_1984. The spatial resolution is 0.00026949459 degrees, with each file covering an area of 10° × 10°. Files are named according to the format: `Cropping_Intensity_30m_2016_2018_$regions$.tif`, where "regions" designates the hemispherical and latitudinal/longitudinal coordinates of the top-left corner. Each file contains two layers:

The dataset includes two key layers for the average cropping intensity and the total number of crop cycles between 2016 and 2018. The Average Cropping Intensity layer classifies cropping patterns into three distinct values: '1' for single cropping, '2' for double cropping, and '3' for triple cropping. Areas with no data or masked regions are assigned a value of '-1'. The Total Number of Crop Cycles layer provides the original counts of crop cycles within the same period. Continuous cropping or instances of more than three crop cycles per year are indicated with a value of '127', while areas with no data or masked regions are also assigned '-1'. The images were ingested as a single image collection.

#### Citation

```
Zhang, Miao, Bingfang Wu, Hongwei Zeng, Guojin He, Chong Liu, Shiqi Tao, Qi Zhang et al. "GCI30: A global dataset of 30-m cropping intensity using
multisource remote sensing imagery." Earth System Science Data Discussions 2021 (2021): 1-22.
```

#### Dataset Citation

```
Zhang, Miao; Wu, Bingfang; Zeng, Hongwei; He, Guojin; Liu, Chong; Nabil, Mohsen; Tian, Fuyou; Bofana, José; Wang, Zhengdong; Yan, Nana, 2020,
"GCI30: Global Cropping Intensity at 30m resolution", https://doi.org/10.7910/DVN/86M4PO, Harvard Dataverse, V2
```

![gci30](https://github.com/user-attachments/assets/f7fe7556-34ba-4592-a76d-39574632734e)


#### Earth Engine Snippet

```js
var GCI30 = ee.ImageCollection("projects/sat-io/open-datasets/GCI30");

var snazzy = require("users/aazuspan/snazzy:styles");
snazzy.addStyle("https://snazzymaps.com/style/72543/assassins-creed-iv", "Greyscale");

// Average Cropping Intensity (Single/Double/Triple Cropping)
var average_cropping_intensity = GCI30.median().mask(GCI30.median().neq(-1));
var cropping_intensity_palette = ['#ffeda0', '#feb24c', '#f03b20', '#bd0026'];

Map.addLayer(average_cropping_intensity.select('b1'), {
  min: 1,
  max: 3,
  palette: cropping_intensity_palette
}, 'Average Crop Intensity Single/Double/Triple Cropping');

// Total Number of Crop Cycles
var total_crop_cycles = GCI30.median().mask(GCI30.median().neq(-1));

// Recode value 127 to 4 to make the palette continuous
var recoded_crop_cycles = total_crop_cycles.select('b2').remap([127], [4]);

var crop_cycles_palette = ['#762a83', '#af8dc3', '#e7d4e8', '#d9f0d3', '#7fbf7b', '#1b7837'];

Map.addLayer(total_crop_cycles.select('b2'), {
  min: 1,
  max: 4,
  palette: crop_cycles_palette
}, 'Total Number of Crop Cycles (Recode)');
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/GCI30

#### License
The Global Cropping Intensity Dataset is licensed under a CC0 1.0 Universal license.

Created by: Zhang et al 2021

Curated in GEE by: Samapriya Roy

Keywords : cropping intensity,crop cycle,average crop intensity

Last updated in GEE: 2024-10-02
