# Global Long-term Microwave Vegetation Optical Depth Dataset Archive VODCA v2

The Global Microwave Vegetation Optical Depth Climate Archive version 2 (VODCA v2) provides two new multi-satellite VOD datasets: VODCA CXKu, a
daily multi-frequency product spanning 1987-2021, and VODCA L, a 10-daily L-band product covering 2010-2021. Vegetation Optical Depth (VOD) is a
model-based indicator of the total water content stored in vegetation canopy derived from microwave Earth observations, related to vegetation
density, abundance, and above-ground biomass (AGB).

VODCA CXKu merges observations from multiple sensors in the C-, X- and Ku-band frequencies including SSM/I F08, F11, F13, F17, TRMM TMI, AMSR-E,
Windsat, AMSR2 and GPM GMI. The data is provided at daily temporal resolution and 0.25° spatial resolution. VODCA L combines VOD observations from
SMOS MIRAS and SMAP radiometer, provided at 10-day temporal resolution and 0.25° spatial resolution. Both products are masked for spurious
observations like frozen ground, snow, and radio-frequency interference.

The datasets were created using a novel weighted merging scheme based on first-order autocorrelation of input
datasets. VODCA CXKu exhibits lower random error levels and improved temporal sampling compared to
single-frequency products, while VODCA L shows strong spatial agreement with above-ground biomass maps and is more
sensitive to the entire canopy including branches and trunks. More importantly VODCA v2 incorporates several methodological improvements compared to
the first version and adds two new VOD datasets to the VODCA product suite. The VOD observations used in VODCA v2 are derived through the Land
Parameter Retrieval Model (LPRM; Owe et al. (2008); Van der Schalie et al. (2017)) You can read the [paper here](https://doi.org/10.5194/essd-16-4573-2024)

#### Dataset Preprocessing
The netCDF files were converted into cloud optimized geotiffs with LZW compression and overviews. The data is provided in two collections - one for
VODCA CXKu (daily) and one for VODCA L (10-daily), maintaining the original temporal and spatial resolutions.

#### Citation

```
Zotta, R.-M., Moesinger, L., van der Schalie, R., Vreugdenhil, M., Preimesberger, W., Frederikse, T., De Jeu, R., and Dorigo, W.: VODCA v2:
multi-sensor, multi-frequency vegetation optical depth data for long-term canopydynamics and biomass monitoring,
Earth Syst. Sci. Data, 16, 4573–4617, https://doi.org/10.5194/essd-16-4573-2024, 2024.
```
#### Dataset Citation

```
Zotta, R.-M., Moesinger, L., van der Schalie, R., Vreugdenhil, M., Preimesberger, W., Frederikse, T., De Jeu, R., & Dorigo, W. (2024). VODCA v2:
Multi-sensor, multi-frequency vegetation optical depth data for long-term canopy dynamics and biomass monitoring (1.0.0) [Data set].
TU Wien. https://doi.org/10.48436/t74ty-tcx62
```

![vodca2](https://github.com/user-attachments/assets/ce182850-2b77-4834-ba8f-418993ba3f1c)

#### Sample Earth Engine Script

```js
var ckxu_band = ee.ImageCollection("projects/sat-io/open-datasets/VODCA/CKXU_BAND_V2");
var l_band = ee.ImageCollection("projects/sat-io/open-datasets/VODCA/L_BAND_V2");

function getCollectionDateRange(collection) {
  // Get earliest date
  var startDate = ee.Date(collection.sort('system:time_start')
    .first()
    .get('system:time_start'))
    .format('YYYY-MM-dd');

  // Get latest date
  var endDate = ee.Date(collection.sort('system:time_start', false)
    .first()
    .get('system:time_start'))
    .format('YYYY-MM-dd');

  return {
    start: startDate,
    end: endDate
  };
}

var ckxuDates = getCollectionDateRange(ckxu_band);
var lDates = getCollectionDateRange(l_band);

print('CKXU dates:', ckxuDates.start, 'to', ckxuDates.end);
print('L-band dates:', lDates.start, 'to', lDates.end);

var vis = ['#a50026','#d73027','#f46d43','#fdae61','#fee08b','#ffffbf','#d9ef8b','#a6d96a','#66bd63','#1a9850','#006837']

Map.addLayer(ckxu_band.filterDate('2005-01-01','2005-12-31').median().select('VOD'),{palette:vis,min:0.1,max:1.5},'CKXU-Band 2005 subset')
Map.addLayer(l_band.filterDate('2010-01-01','2010-12-31').median().select('VOD'),{palette:vis,min:0.08,max:0.6},'L-Band 2010 subset')
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/VODCA_V2

#### License
This dataset is available under a Creative Commons Attribution 4.0 International license.

Created by: Zotta et al 2024

Curated in GEE by: Samapriya Roy

Keywords: VOD, Vegetation Optical Depth, Biomass, Vegetation water content, Microwave Remote Sensing, Biosphere, Time Series, Global vegetation monitoring, Plant water dynamics, Multi-frequency

Last updated: 2025-02-02
