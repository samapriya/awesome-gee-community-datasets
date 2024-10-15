# Canada Long Term Tree Species (1984-2022)

In this dataset, we share maps of annual dominant tree species (also known as leading tree species) from 1984-2022 covering the entirety of Canada’s 650 Mha forested ecosystems using Landsat time-series imagery at a 30-m spatial resolution. Classifications are based on regionally representative Random Forests model using local training samples from Canada’s National Forest Inventory (Hermosilla et al., 2022). Descriptive metrics provide information on spectral, geographic, climatic, and topographic characteristics. Initial annual tree species classifications were subjected to a time series post-classification process using the forward-backward Hidden Markov Model to improve the temporal consistency of tree species transitions within the time series. Assessment of the annual species maps using independent validation data resulted in an overall accuracy of 86.1% ± 0.14% (95%-confidence interval). These data allow consistent comparison of trends and rates of change in tree species composition nationally and across regions using a common time frame, spatial resolution, and analytical approach.

<img width="959" alt="ca_species_aoi" src="https://github.com/user-attachments/assets/c6823fc9-1a27-407e-8707-cfd6ffd3c382">

#### Citation

```
Hermosilla, T., Wulder, M.A., White, J.C., Coops, N.C., Bater, C.W., Hobart, G.W., 2024. Characterizing long-term tree species dynamics in Canada's forested ecosystems using annual time series remote sensing data. Forest Ecology and Management 572, 122313. https://doi.org/10.1016/j.foreco.2024.122313 (Hermosilla et al. 2024)
```

You can download the [files here](https://opendata.nfis.org/mapserver/nfis-change_eng.html), found under the title: Annual Tree Species 1984-2022 and [Species_Names here](https://github.com/user-attachments/files/17334136/Species_Names.xlsx)

#### Dataset Post processing
The datasets were provided as an earth engine folder with images and have been converted to an imagecollection and start and end date have been added to each image in the image collection for filtering.

![ca_species](https://github.com/user-attachments/assets/13176b42-637a-40a0-9d05-4accaf5763d2)

#### Earth Engine Snippet

```js
var ca_species_ts = ee.ImageCollection("projects/sat-io/open-datasets/CA_FOREST/SPECIES-1984-2022");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/CA-SPECIES-TIME-SERIES

#### License
This work is licensed under and freely available to the [public Open Government License - Canada](http://open.canada.ca/en/open-government-licence-canada).

Created by: Hermosilla et al. 2024

Curated in GEE by : Spencer Bronson & Samapriya Roy

Keywords: Landsat, Time series analysis, Land cover, Land cover change, Forest succession, Dominant species

Last updated :2024-10-15
