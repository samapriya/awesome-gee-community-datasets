# ESA CCI Global Forest Above Ground Biomass

This dataset updated to v5.01 provides estimates of forest above-ground biomass for the years 2010, 2015, 2016, 2017, 2018, 2019, 2020 and 2021. These estimates are derived from a combination of Earth observation data, depending on the year, obtained from the Copernicus Sentinel-1 mission, Envisat's ASAR instrument, and JAXA's Advanced Land Observing Satellite (ALOS-1 and ALOS-2), along with additional information from other Earth observation sources. The dataset has been generated as part of the European Space Agency's (ESA's) Climate Change Initiative (CCI) program by the Biomass CCI team.

The dataset includes multi-temporal observations at L-band for all biomes and for each year. The above-ground biomass (AGB) maps utilize revised allometries, which are now based on a more extensive collection of spaceborne LiDAR data from the GEDI and ICESat-2 missions. The retrieval algorithm now incorporates temporal information to capture and preserve biomass dynamics as expressed in the remote sensing data.

The data products consist of two (2) global layers that include estimates of:

1. Above ground biomass (AGB, unit: tons/ha i.e., Mg/ha) (raster dataset). This is defined as the mass, expressed as oven-dry weight of the woody parts (stem, bark, branches and twigs) of all living trees excluding stump and roots

2. Per-pixel estimates of above-ground biomass uncertainty expressed as the standard deviation in Mg/ha (raster dataset)

Also for this release I am including the change products which includes these two layers

1. Standard deviation of AGB change: Maps showing the uncertainty of AGB change for consecutive years (2015-2016) and the decade 2010-2020. Available for each time period (e.g., 2016-2017).

2. Quality flag of AGB change: Maps indicating the reliability of AGB change estimates for consecutive years (2015-2016) and the decade 2010-2020. Available for each time period (e.g., 2016-2017).

Note: AGB change values can be calculated by differencing the corresponding AGB maps.

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Dataset preprocessing for GEE
* Above ground biomass files were downloaded for each years as tiles and then merged into single year images rasters. Common metadata properties were preserved so as to be passed over to the collection
* The same approach for a yearly composite was applied to the Standard deviations tiles as well to make sure they can be mapped on top of each other.
* For ingestion a manifest file was created with Band 1 being AGB and Band 2 being SD so we could reduce the overall files for an image collection. The ingestion used a no data value of 0.
* For change product Band 1 was AGB_DIFF_SD and Band 2 was AGB_DIFF_QF and these were to represent standard deviation of AGB biomass change and quality flag of AGB biomass change.
* Metadata properties were copied over from AGB with some slight changes to fields and the dates were preproccessed and updated to v5.01.

#### Citation

```
Santoro, M.; Cartus, O. (2024): ESA Biomass Climate Change Initiative (Biomass_cci): Global datasets of forest above-ground biomass for the years 2010, 2015, 2016, 2017, 2018,
2019, 2020 and 2021, v5.01. NERC EDS Centre for Environmental Data Analysis, 22 August 2024. doi:10.5285/bf535053562141c6bb7ad831f5998d77.
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

Created: 2024-07-29

Last updated in GEE: 2025-01-27
