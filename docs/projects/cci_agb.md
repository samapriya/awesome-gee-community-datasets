# ESA CCI Global Forest Above Ground Biomass

This dataset updated to v6.0 provides estimates of forest above-ground biomass for the years 2007, 2010, 2015, 2016, 2017, 2018, 2019, 2020, 2021, and 2022. These estimates are derived from a combination of Earth observation data, depending on the year, obtained from the Copernicus Sentinel-1 mission, Envisat’s ASAR (Advanced Synthetic Aperture Radar) instrument, and JAXA's Advanced Land Observing Satellite (ALOS-1 and ALOS-2), along with additional information from other Earth observation sources. The dataset has been generated as part of the European Space Agency's (ESA's) Climate Change Initiative (CCI) program by the Biomass CCI team.

Compared to version 5, version 6 consists of updated AGB maps for the years 2010, 2015, 2016, 2017, 2018, 2019, 2020, 2021 and new AGB maps for 2007 and 2022. The dataset includes multi-temporal observations at L-band for all biomes and for each year. The above-ground biomass (AGB) maps utilize revised allometries, which are now based on a more extensive collection of spaceborne LiDAR data from the GEDI and ICESat-2 missions. The retrieval algorithm incorporates extended ICESat-2 observations to calibrate retrieval models and a refined cost function that preserves temporal features as expressed in the remote sensing data, limiting biases between the 2007-2010 and the 2015+ maps.

The data products consist of two (2) global layers that include estimates of:

1. Above ground biomass (AGB, unit: tons/ha i.e., Mg/ha) (raster dataset). This is defined as the mass, expressed as oven-dry weight of the woody parts (stem, bark, branches and twigs) of all living trees excluding stump and roots

2. Per-pixel estimates of above-ground biomass uncertainty expressed as the standard deviation in Mg/ha (raster dataset)

Additionally provided in this version release are aggregated data products. These aggregated products of the AGB and AGB change data layers are available at coarser resolutions (1, 10, 25 and 50km).

Also included are the change products which include these layers:

1. Standard deviation of AGB change: Maps showing the uncertainty of AGB change for consecutive years (e.g., 2016-2015, 2017-2016, 2018-2017, 2019-2018, 2020-2019, 2021-2020, 2022-2021), over a decade (2020-2010), and over the interval 2010-2007.

2. Quality flag of AGB change: Maps indicating the reliability of AGB change estimates for the same time periods mentioned above.

Note: AGB change values can be calculated by differencing the corresponding AGB maps. Data are provided in both netcdf and geotiff format.

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Dataset preprocessing for GEE
* Above ground biomass files were downloaded for each years as tiles and then merged into single year images rasters. Common metadata properties were preserved so as to be passed over to the collection
* The same approach for a yearly composite was applied to the Standard deviations tiles as well to make sure they can be mapped on top of each other.
* For ingestion a manifest file was created with Band 1 being AGB and Band 2 being SD so we could reduce the overall files for an image collection. The ingestion used a no data value of 0.
* For change product Band 1 was AGB_DIFF_SD and Band 2 was AGB_DIFF_QF and these were to represent standard deviation of AGB biomass change and quality flag of AGB biomass change.
* Metadata properties were copied over from AGB with some slight changes to fields and the dates were preprocessed and updated to v6.0.

#### Citation

```
Santoro, M.; Cartus, O. (2025): ESA Biomass Climate Change Initiative (Biomass_cci): Global datasets of forest above-ground biomass for the years 2007, 2010, 2015, 2016, 2017, 2018,
2019, 2020, 2021 and 2022, v6.0. NERC EDS Centre for Environmental Data Analysis, 17 April 2025. doi:10.5285/95913ffb6467447ca72c4e9d8cf30501.
```

![cci-biomass](https://github.com/aazuspan/snazzy/assets/6677629/f2269833-d283-4568-aba5-cadf928cb15c)

#### Earth Engine Snippet

```js
var agb = ee.ImageCollection("projects/sat-io/open-datasets/ESA/ESA_CCI_AGB");
```

Sample code:  https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/ESA-CCI-ABOVEGROUND-BIOMASS

```js
var agb_change = ee.ImageCollection("projects/sat-io/open-datasets/ESA/ESA_CCI_AGB_DIFF");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/ESA-CCI-ABOVEGROUND-BIOMASS-DIFFERENCE

#### License and Access
Use of these data is covered by the [license information found here](http://artefacts.ceda.ac.uk/licences/specific_licences/esacci_biomass_terms_and_conditions.pdf). The CCI BIOMASS datasets have been processed by the CCI BIOMASS consortium led by the University
of Aberystwyth (U.K.). They are made available to the public by ESA and the consortium. When using these data you must cite them correctly using the citation given on the catalogue record. The dataset is under a public access with access to these data available to both registered and non-registered users

Created by: CCI BIOMASS consortium led by the University of Aberystwyth (U.K.)

Curated in GEE by: Samapriya Roy

Keywords: satellite observation, forest, biomass

Created: 2025-04-17

Last updated in GEE: 2025-09-01

#### Changelog

**v6.0 (April 2025)**
- **Extended temporal coverage**: Added new AGB maps for 2007 and 2022
- **Updated existing maps**: Refreshed AGB estimates for 2010, 2015, 2016, 2017, 2018, 2019, 2020, and 2021
- **Enhanced calibration**: Extended ICESat-2 observations used for retrieval model calibration
- **Improved temporal consistency**: Refined cost function to limit biases between 2007-2010 and 2015+ maps
- **New aggregated products**: Added coarser resolution data products (1, 10, 25, and 50km)
- **Extended change products**: New AGB change maps for additional consecutive years (2022-2021) and 2010-2007 interval
- **Multiple formats**: Data now available in both netcdf and geotiff formats
- **Updated citation**: New DOI and publication details

**v5.01 (August 2024)**
- Initial release with AGB estimates for 2010, 2015, 2016, 2017, 2018, 2019, 2020, and 2021
- Utilized revised allometries based on GEDI and ICESat-2 spaceborne LiDAR data
- Incorporated temporal information to capture biomass dynamics
- Provided AGB change products for consecutive years and decade (2010-2020)
- Band 1: AGB, Band 2: Standard deviation for main collection
- Band 1: AGB_DIFF_SD, Band 2: AGB_DIFF_QF for change collection
