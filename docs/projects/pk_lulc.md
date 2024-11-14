# High Res Land Cover Change & Carbon Storage Pakistan (1990-2020)

This dataset, generated from the study titled _[Urbanization-led land cover change impacts terrestrial carbon storage capacity: A high-resolution remote sensing-based nation-wide assessment in Pakistan (1990–2020)](https://doi.org/10.1016/j.eiar.2023.107396), provides high-resolution, national-scale **Land Use/Land Cover (LULC)** and **terrestrial carbon stock** maps for Pakistan across four time periods: 1990, 2000, 2010, and 2020. The **LULC dataset** includes nine distinct land cover classes (outlined in the table below). Classification was performed using a **hybrid random forest-based machine learning approach**, with model training and validation carried out using approximately **40,000 stratified random samples** to ensure robust accuracy.

The **carbon stock maps** were produced using the **InVEST model**, estimating carbon storage across four major carbon pools: above-ground biomass, below-ground biomass, soil organic carbon, and dead organic matter. The results highlight a substantial reduction in carbon storage capacity due to rapid urban expansion, particularly in major cities such as **Karachi** and **Lahore**, where large areas of forest and agricultural land were converted into urban landscapes. The study estimates that **Pakistan lost approximately 5% of its carbon storage capacity** during this period, while urban areas expanded by over **1040%**. For more details, you can read the full paper [here](https://doi.org/10.1016/j.eiar.2023.107396).

#### Citation

```
Waleed, M., Sajjad, M., & Shazil, M. S. (2024). Urbanization-led land cover change impacts terrestrial carbon storage capacity: A high-resolution remote sensing-based nation-wide assessment in Pakistan (1990–2020). Environmental Impact Assessment Review, 105, 107396. https://doi.org/10.1016/j.eiar.2023.107396
```

####  Dataset Citation

```
Mirza, W. (2024). Pakistan 30m land use land cover and carbon storage dataset (1990-2020) [Data set]. In Urbanization-led land cover change impacts terrestrial carbon storage
capacity: A high-resolution remote sensing-based nation-wide assessment in Pakistan (1990–2020). Elsevier. https://doi.org/10.1016/j.eiar.2023.107396
```

#### Dataset Preprocessing
The image files for both landcover and carbon stock were moved into single collections and date ranges were added for easily filtering across there.

## For more details, visit:

- [**Github Project Repository Link**](https://github.com/waleedgeo/lulc_pk)
- [**Paper DOI Link**](https://doi.org/10.1016/j.eiar.2023.107396)
- [**Paper PDF Link**](https://waleedgeo.com/papers/waleed2024_paklulc.pdf)
- [**Datasets Download Link**](https://zenodo.org/records/13982339)

#### LULC Classification Table

<center>

<table style="margin-left: auto; margin-right: auto; border-collapse: collapse;">
  <tr>
    <th>LULC Class</th>
    <th>Class Value</th>
    <th>Visual</th>
  </tr>
  <tr>
    <td>Forest Cover</td>
    <td>1</td>
    <td style="background-color:#54bb19; color:white;">#54bb19</td>
  </tr>
  <tr>
    <td>Agriculture/Cropland</td>
    <td>3</td>
    <td style="background-color:#affd08;">#affd08</td>
  </tr>
  <tr>
    <td>Rangeland</td>
    <td>4</td>
    <td style="background-color:#d1fbb9;">#d1fbb9</td>
  </tr>
  <tr>
    <td>Wetlands</td>
    <td>5</td>
    <td style="background-color:#652ff3; color:white;">#652ff3</td>
  </tr>
  <tr>
    <td>Barren Lands</td>
    <td>6</td>
    <td style="background-color:#fed483;">#fed483</td>
  </tr>
  <tr>
    <td>Water Bodies</td>
    <td>7</td>
    <td style="background-color:#005ce6; color:white;">#005ce6</td>
  </tr>
  <tr>
    <td>Built-up Areas</td>
    <td>8</td>
    <td style="background-color:#e50600; color:white;">#e50600</td>
  </tr>
  <tr>
    <td>Snow/Ice</td>
    <td>9</td>
    <td style="background-color:#fe4fcd;">#fe4fcd</td>
  </tr>
</table>

</center>

![LULC App Static Image](https://imgur.com/azb1v8H.gif)

#### Earth Engine Snippet

```js
var landcover = ee.ImageCollection("projects/sat-io/open-datasets/pk-lulc");
var carbon = ee.ImageCollection("projects/sat-io/open-datasets/pk-carbon-stock");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:regional-landuse-landcover/PK-LANCOVER-CARBON-STOCK


The dataset is also available as interactive **Google Earth Engine (GEE) applications**.

* **Link to GEE - LULC App for Pakistan:** [https://waleedgis.users.earthengine.app/view/pakistan-lulc-1990-2020](https://waleedgis.users.earthengine.app/view/pakistan-lulc-1990-2020)

* **Link to GEE - Carbon App for Pakistan:** [https://waleedgis.users.earthengine.app/view/pakistan-carbon-1990-2020](https://waleedgis.users.earthengine.app/view/pakistan-carbon-1990-2020)

#### Enter license information

This dataset is licensed under a Creative Commons Attribution 4.0 International license.

Provided by: Waleed et al 2024

Curated in GEE by: Samapriya Roy

Keywords: land use, land cover, pakistan, lulc, carbon, urban, InVEST model

Last updated in GEE: 2024-11-13
