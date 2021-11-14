# High-resolution annual forest land cover maps for Canada's forested ecosystems (1984-2019)

The annual time series of forest land cover maps are national in scope (entire 650 million hectare forested ecosystem) and represent a wall-to-wall land cover characterization yearly from 1984 to 2019. These time-series land cover maps were produced from annual time-series of Landsat image composites, forest change information, and ancillary topographic and hydrologic data following the framework described in Hermosilla et al. (2022), which builds upon the approach introduced in Hermosilla et al. (2018). The methodological innovations included (i) a refined training pool derived from existing land cover products using airborne and spaceborne measures of forest structure; (ii) selection of training samples proportionally to the land cover distribution using a distance=weighted approach; and (iii) generation of regional classification models using a 150x150 km tiling system. Maps are post-processed using disturbance information to ensure logical class transitions over time using a Hidden Markov Model. Hidden Markov Models assess individual year class likelihoods to reduce variability and possible noise in year-on-year class assignments (for instances when class likelihoods are similar).

For an overview on the data, image processing, and time series change detection methods applied, as well as information on independent accuracy assessment of the data, see Hermosilla et al. (2022) No. 112780. DOI: https://doi.org/10.1016/j.rse.2021.112780 and Hermosilla et al. (2018) https://www.tandfonline.com/doi/full/10.1080/07038992.2018.1437719

The data represents annual forest land cover of Canada's forested ecosystems for 1984-2019. An image compositing window of August 1 -30 days was used to generate the best-available-pixel (BAP) image composites used as the source data for land cover classification. The science and methods developed to generate the information outcomes shown here, that track and characterize the history of Canada's forests, were led by Canadian Forest Service of Natural Resources Canada, partnered with the University of British Columbia, with support from the Canadian Space Agency, augmented by processing capacity from WestGrid of Compute Canada.


#### Citation
When using this data, please cite as:

```
Hermosilla, T., Wulder, M.A., White, J.C., Coops, N.C., 2022. Land cover classification in an era of big and open data: Optimizing localized
implementation and training data selection to improve mapping outcomes. Remote Sensing of Environment. No. 112780.
DOI: https://doi.org/10.1016/j.rse.2022.112780 [Open Access]
```

#### Class Schema

|Class Code                                        |Class                    |
|--------------------------------------------------|-------------------------|
|0                                                 | no change               |
|20                                                | water                   |
|31                                                | snow_ice                |
|32                                                | rock_rubble             |
|33                                                | exposed_barren_land     |
|40                                                | bryoids                 |
|50                                                | shrubs                  |
|80                                                | wetland                 |
|81                                                | wetland-treed           |
|100                                               | herbs                   |
|210                                               | coniferous              |
|220                                               | broadleaf               |
|230                                               | mixedwood               |

#### Earth Engine Snippet

```js
var forest_lc = ee.ImageCollection("projects/sat-io/open-datasets/CA_FOREST_LC_VLCE2");
```

Sample code: https://code.earthengine.google.com/c962180f9229986e9e19d141166479bb


#### License
This work is licensed under and freely available to the public Open Government Licence - Canada (http://open.canada.ca/en/open-government-licence-canada).

Created by: Sothe et al 2021

Curated in GEE by : Samapriya Roy

keywords: soil carbon density, soil carbon stock estimate, soil carbon storage, terrestrial ecosystem models, machine Learning Methods Enabled Predictive Modeling

Last updated on GEE: 2021-11-14
