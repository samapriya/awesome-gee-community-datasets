# Global gridded sea surface temperature (SSTG)

Sea surface temperature (SST) is an important geophysical parameter that is essential for studying global climate change. Although sea surface temperature can currently be obtained through a variety of sensors (MODIS, AVHRR, AMSR-E, AMSR2, WindSat, in situ sensors), the temperature values obtained by different sensors come from different ocean depths and different observation times, so different temperature products lack consistency.

The SSTG dataset is a global sea surface temperature data during the period of 2002-2019, in Celsius, in monthly temporal and 0.041° spatial resolution. It is produced by combing daily in situ SST data and daily satellite SST retrieval data from two infrared (MODIS and AVHRR) and three passive microwave (AMSR-E, AMSR2, Windsat) radiometers after calibration by using a temperature depth and observation time correction model. The accuracy assessments indicate that the reconstructed dataset exhibits significant improvements and can be used for mesoscale ocean phenomenon analyses.

#### Paper Citation

```
Cao, M., Mao, K., Yan, Y., Shi, J., Wang, H., Xu, T., Fang, S., and Yuan, Z.: A new global gridded sea surface temperature data product based on
multisource data, Earth Syst. Sci. Data, 13, 2111–2134, https://doi.org/10.5194/essd-13-2111-2021, 2021.
```

#### Data Citation

```
Mengmeng cao, Kebiao Mao, Yibo Yan, Jiancheng Shi, Han Wang, Tongren Xu, Shu Fang, & Zijin Yuan. (2021). A New Global Gridded Sea Surface
Temperature Data Product Based on Multisource Data (1.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.4762067
```

![sstg](https://user-images.githubusercontent.com/6677629/150665559-ac581093-f568-4b7a-b22f-d30d292dbe4e.png)


#### Earth Engine Snippet

```js

var sstg =  ee.ImageCollection("projects/sat-io/open-datasets/sstg")

```

Sample Code: https://code.earthengine.google.com/8a984f0e27a35fae4418aef1b9ceb4df

#### License
This work is distributed under the Creative Commons Attribution 4.0 International License

Created by: Mengmeng cao, Kebiao Mao, Yibo Yan, Jiancheng Shi, Han Wang, Tongren Xu, Shu Fang, & Zijin Yuan

Curated by:Samapriya Roy

Keywords: Sea Surface Temperature, SST, Gridded

Last updated: 2021-01-05
