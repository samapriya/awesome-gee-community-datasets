# Carbon Security Index

This dataset presents an index developed to assess carbon security across the sagebrush steppe in the Great Basin. The Carbon Security Index (CSI) incorporates data from three key sources: fractional plant cover from the [Rangeland Analysis Platform](https://rangelands.app/), a fire probability model specific to the Great Basin (Smith et al., 2023), and a resistance and resilience dataset for the sagebrush steppe (Chambers et al., 2014, 2017).

The CSI is calculated as follows:

**CSI = Preferred Rangeland Cover Index + Resistance & Resilience – P(Fire)**

The resulting index ranges from -2 to +2 and allows for spatial comparisons of carbon security across the region.

<div class="result" markdown>

???+ note

    **The associated paper for this dataset has been accepted as part of a special issue but does not yet have a DOI assigned. A preprint version was not made available. Please note that the listed citations do not refer to this paper.**

</div>

#### Supplemental Citation

```
[Smith, J.T., Allred, B.W., Boyd, C.S., Davies, K.W., Jones, M.O., Kleinhesselink, A.R., Maestas, J.D., Naugle, D.E. (2023). Where There's Smoke, There's Fuel: Dynamic Vegetation Data Improve Predictions of Wildfire Hazard in the Great Basin. Rangeland Ecol. Manage. 89:20-32. https://doi.org/10.1016/j.rama.2022.07.005](https://doi.org/10.1016/j.rama.2022.07.005)

[Chambers, J.C., Miller, R.F., Board, D.I., Pyke, D.A., Roundy, B.A., Grace, J.B., Schupp, E.W., Tausch, R.J. (2014). Resilience and Resistance of Sagebrush Ecosystems: Implications for State and Transition Models and Management Treatments. Rangeland Ecol. Manage. 67:440-454. https://doi.org/10.2111/REM-D-13-00074.1](https://doi.org/10.2111/REM-D-13-00074.1)

[Chambers, J.C., Maestas, J.D., Pyke, D.A., Boyd, C.S., Pellant, M., Wuenschel, A. (2017). Using Resilience and Resistance Concepts to Manage Persistent Threats to Sagebrush Ecosystems and Greater Sage-grouse. Rangeland Ecol. Manage. 70:149-164. https://doi.org/10.1016/j.rama.2016.08.005](https://doi.org/10.1016/j.rama.2016.08.005)
```

![csi](https://github.com/user-attachments/assets/e51d8c7e-4d64-4f23-bd02-9fe49f0586d3)

#### Earth Engine Snippet

```js
var carbonoffsetscol = ee.FeatureCollection('projects/sat-io/open-datasets/CARBON-OFFSET-PROJECTS-GLOBAL');

var visParams = {
    palette: ['#9ab555'],
    min: 0.0,
    max: 1550000.0,
    opacity: 0.8,
};
var carbonoffsets = ee.Image().float().paint(carbonoffsetscol, 'REP_AREA');

Map.setCenter(-52.692,-2.628,6)
Map.addLayer(carbonoffsets, visParams, 'Existing carbon projects area');

var snazzy = require("users/aazuspan/snazzy:styles");
snazzy.addStyle("https://snazzymaps.com/style/15/subtle-grayscale", "Greyscale");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/CARBON-SECURITY-INDEX

#### License
This dataset is made available under Creative Commons Attribution 4.0 International license.

Keywords: rangelands, sagebrush steppe, Great Basin, ecosystem function, environmental assessment and monitoring, environmental management

Curated in GEE by: Samapriya Roy

Last updated : 2024-07-24
