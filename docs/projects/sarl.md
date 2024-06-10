# Surface Area of Rivers and Lakes (SARL)

The Surface Area of Rivers and Lakes (SARL) dataset, developed by Nyberg et al. (2024), provides a comprehensive analysis of water surface area changes in rivers and lakes over a 38-year period (1984-2022). This global dataset, at a 30-meter resolution, offers valuable insights into the dynamics of surface water, particularly highlighting the increasing role of seasonality.

The SARL dataset categorizes water bodies into seven classes:
- 0: Background Value: Represents areas without water.
- 1: Permanent River: Areas with continuous water presence throughout the year.
- 2: Permanent Lake: Areas with continuous water presence throughout the year.
- 3: Seasonal River: Areas with water present for at least one month during the year.
- 4: Seasonal Lake: Areas with water present for at least one month during the year.
- 5: No Data Lakes: Areas with missing data for lakes.
- 6: No Data Rivers: Areas with missing data for rivers.

The study, reveals that while the total permanent surface area of both rivers and lakes has remained relatively constant, the areas experiencing intermittent seasonal coverage have significantly increased. Specifically, seasonal river coverage has risen by 12%, and seasonal lake coverage has increased by 27%. These trends are statistically significant across over 84% of global water catchments. The open access article published in Hydrology and Earth System Sciences can be found [here](https://hess.copernicus.org/articles/28/1653/2024/). In addition, the datasets are archived in a Zenodo repository available at this [url](https://zenodo.org/records/6895820).

#### Citation

```
Nyberg, B., Sayre, R., and Luijendijk, E.: Increasing seasonal variation in the extent of rivers and lakes from 1984 to 2022,
Hydrol. Earth Syst. Sci., 28, 1653–1663, 2024.
```

#### Dataset Citation

```
Nyberg, B. (2023). Surface Area of River and Lakes (SARL) (1.0) [Data set]. Zenodo.
https://doi.org/10.5281/zenodo.6895820
```

![sarl](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/3ee40c25-7399-409f-b5ee-278bb2b0b656)


#### Earth Engine Snippet

```js
var sarl = ee.Image("projects/sat-io/open-datasets/SARL");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/SURFACE-AREA-RIVER-LAKES

Earth Engine App: https://bjornburrnyberg.users.earthengine.app/view/waterchange

App Source Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/SARL-APP

#### License
Creative Commons Attribution 4.0 International

Created by: Nyberg et al 2024

Curated in GEE by: Nyberg and Samapriya Roy

Keywords: water, water change, rivers, lakes

