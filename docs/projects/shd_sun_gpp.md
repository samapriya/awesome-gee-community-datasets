# Global Sunlit and Shaded GPP for vegetation canopies (1992-2020)

Gross primary production (GPP) is a vital component of the terrestrial carbon budget and plays a prominent role in the global carbon cycle. Accurate estimation of terrestrial GPP is critical for understanding the interaction between the terrestrial biosphere and the atmosphere in the context of global climate change projecting future change, and informing climate policy decisions. GPP is closely related to vegetation types meteorological factors, soil moisture, and other factors. In particular, GPP is affected by vegetation canopy structures e.g., sunlit and shaded leaves. Sunlit leaves can absorb direct and diffuse radiation simultaneously, and light saturation is easy to occur when the radiation is high, while shaded leaves can only absorb diffuse radiation and the absorbed radiation intensity is generally between the light compensation point and the light saturation point.

Here we produce a global 0.05°, 8-day dataset for GPP, GPPshade and GPPsun over 1992–2020 using an updated two-leaf light use efficiency model (TL-LUE), which is driven by the GLOBMAP leaf area index, CRUJRA meteorology, and ESA-CCI land cover. Such products can support exploring the similarities and differences of sunlit and shaded leaves contributing to GPP or SIF (Sun induced chlorophyll fluorescence), to further excavate the interior ecological mechanism of different carbon cycle processes and advance carbon cycle modelling.

You can [download the dataset here](https://datadryad.org/stash/dataset/doi:10.5061/dryad.dfn2z352k) and [read the paper here](https://www.nature.com/articles/s41597-022-01309-2)

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### [Usage notes from Dataset page](https://datadryad.org/stash/dataset/doi:10.5061/dryad.dfn2z352k)

The units of three temporal resolutions (8-day, monthly, annual) are gC m-2 8day-1, gC m-2 month-1 and gC m-2 a-1, respectively. And the scale factor of the monthly data is 0.1, that of the 8-day data is 0.01. In the dataset, in order to ensure the authenticity, we did not delete or modify a small number of abnormally high values (caused by LAI). Therefore, when using this dataset, you can set thresholds to remove the anomalies.

#### Citation:

```
Bi, W., He, W., Zhou, Y. et al. A global 0.05° dataset for gross primary production of sunlit and shaded vegetation canopies from 1992 to 2020. Sci
Data 9, 213 (2022). https://doi.org/10.1038/s41597-022-01309-2
```

#### Dataset citation

```
Wenjun, Bi; Yanlian, Zhou (2022), A global 0.05° dataset for gross primary production of sunlit and shaded vegetation canopies (1992–2020), Dryad,
Dataset, https://doi.org/10.5061/dryad.dfn2z352k
```

![gpp_sunlit_shaded_small](https://user-images.githubusercontent.com/6677629/190882975-7f6e0358-f6bf-4417-8942-32fc24fcc03d.gif)

#### Earth Engine Snippet

```js
var gpp_annual = ee.Image("projects/sat-io/open-datasets/GPP_SUNLIT_SHADED/gpp_yearly/GPP_v21_2020");
var shaded_annual = ee.Image("projects/sat-io/open-datasets/GPP_SUNLIT_SHADED/shaded_yearly/Shade_GPP_v21_2020");
var sunlit_annual = ee.Image("projects/sat-io/open-datasets/GPP_SUNLIT_SHADED/sunlit_yearly/Sun_GPP_v21_2020");
var gpp_monthly = ee.ImageCollection("projects/sat-io/open-datasets/GPP_SUNLIT_SHADED/gpp_monthly");
var shaded_monthly = ee.ImageCollection("projects/sat-io/open-datasets/GPP_SUNLIT_SHADED/shaded_monthly");
var sunlit_monthly = ee.ImageCollection("projects/sat-io/open-datasets/GPP_SUNLIT_SHADED/sunlit_monthly");
var gpp_8day = ee.ImageCollection("projects/sat-io/open-datasets/GPP_SUNLIT_SHADED/gpp_8day");
var shaded_8day = ee.ImageCollection("projects/sat-io/open-datasets/GPP_SUNLIT_SHADED/shaded_8day");
var sunlit_8day = ee.ImageCollection("projects/sat-io/open-datasets/GPP_SUNLIT_SHADED/sunlit_8day");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/GLOBAL-SUNLIT-SHADED-GPP-VEG-CANOPIES

#### License & Usage

This work is licensed under a CC0 1.0 Universal (CC0 1.0) Public Domain Dedication license.

Curated in GEE by: Samapriya Roy

Keywords: carbon flux, global changes, long-time series, shaded GPP, sunlit GPP

Last updated: 2022-09-16
