# Global Mangrove Canopy Height Maps Derived from TanDEM-X

???+ note

    **This paper is currently in review with Nature Scientific Data and the citation will be updated once the paper has been published. Please keep this into consideration while using this dataset**

This dataset provides global mangrove canopy height maps for 2015 at a 12-meter resolution. Canopy height estimates were derived from the TanDEM-X digital surface models, calibrated and validated with GEDI Lidar data. The dataset covers a circum-equatorial band from 34 degrees north to 39 degrees south latitude, encompassing the majority of mangrove ecosystems globally. The dataset includes 1443 GeoTIFF files containing global mangrove canopy height maps organized into 1° by 1° tiles. Each GeoTIFF file represents a single tile and is named as follows: `TDM1_DEM__10_Y##X###_DEM_EGM08_GMW314_2015_WM_hcap_cal.tif`, where `Y##X###` represents the latitude (Y = "N" or "S") and longitude (X = "W" or "E") coordinates of the tile's southwest corner.

These canopy height maps are useful for assessing local-scale geophysical and environmental conditions that regulate forest structure and carbon cycle dynamics in mangrove ecosystems. These canopy height maps are instrumental for assessing local-scale geophysical and environmental conditions that regulate forest structure and carbon cycle dynamics in mangrove ecosystems. You can find the dataset on [ORNAL DAAC here](https://daac.ornl.gov/cgi-bin/dsviewer.pl?ds_id=2251)

#### Data acquisition and materials
For data acquisition and materials, the sources included Digital Elevation Model (DEM) data from the German Aerospace Agency (DLR) TanDEM-X mission, as reported by Rizzoli et al. in 2017. The Global Mangrove Watch (GMW) map provided a global mangrove extent map, as detailed by Bunting et al. in 2022. Additionally, Global Ecosystems Dynamics Investigation (GEDI) L2A data was used, as documented by Dubayah et al. in 2020.

#### Citation

```
Simard, M., L. Fatoyinbo, N.M. Thomas, A.E. Stovall, A. Parra, A. Barenblitt, P. Bunting, and I. Hajnsek. 2024. A new global mangrove height map with a 12-meter spatial resolution. In review 2024, Nature Scientific Data.
```

#### Dataset Citation

```
Simard, M., L. Fatoyinbo, N. Thomas, A. Stovall, A. Parra, M.W. Denbina, D. Lagomasino, and I. Hajnsek. 2024. CMS: Global Mangrove Canopy Height
Maps Derived from TanDEM-X, 2015. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/2251
```

#### Data Characteristics

| Characteristic | Description |
|---|---|
| Spatial Coverage | Circum-equatorial band from 34° N to 39° S |
| Spatial Resolution | 12 m |
| Temporal Coverage | Mangrove height maps: 2015; GEDI L2A mangrove heights: 2019-04-18 to 2022-05-22 |
| Temporal Resolution | One-time estimates for nominal year 2015 of maximum canopy height. GEDI data were collected between April 2019 and May 2022. |
| Data File Formats | Cloud optimized GeoTIFF (.tif) and CSV (*.csv) |
| Number of Files | 1443 GeoTIFF files and 1 CSV file |

#### GeoTIFF Characteristics

* Coordinate system: geographic coordinates using WGS 1984 datum with elevation (EPSG: 4979)
* Pixel resolution: 0.000111 degrees (~12 m)
* Number of bands: one
* Pixel values: maximum canopy height in meters
* No data value: All pixels are valid, but pixels without mangroves have a value of zero.

The `GEDI_MANGROVE_HT`, layer contains mangrove heights for individual GEDI L2A tiles used to generate the GeoTIFF files.

??? example "Expand to show Properties for Data Dictionary for GEDI_MANGROVE_HT feature collections"

    <center>

    | Variable | GEDI L2A variable name | Units | Description |
    |---|---|---|---|
    | GEDI_file_name | - | - | Name of the GEDI file |
    | beam | Beam ID | - | Beam number (0-11) |
    | delta_time | delta_time | YYYY-MM-DD HH:MM:SS.SSSSSS+00:00 | Transmit time of the shot |
    | shot_number | shot_number | 1 | Unique shot ID |
    | lat_lowestmode | lat_lowestmode | degrees | Latitude of center of lowest mode |
    | lon_lowestmode | lon_lowestmode | degrees | Longitude of center of lowest mode |
    | channel | channel | 1 | Channel number (0-7) |
    | degrade_flag | degrade_flag | flag | Non-zero values indicate the shot occurred during a degraded period |
    | digital_elevation_model | digital_elevation_model | m | Digital elevation model height above the WGS84 ellipsoid. Interpolated at latitude_bin0 and longitude_bin0 from the TandemX 90m product. |
    | digital_elevation_model_srtm | digital_elevation_model_srtm | m | Shuttle Radar Topography Mission (SRTM) elevation at GEDI footprint location |
    | elev_highestreturn | elev_highestreturn | m | Elevation of highest detected return relative to reference ellipsoid |
    | elev_lowestmode | elev_lowestmode | m | Elevation of lowest mode |
    | elevation_bias_flag | elevation_bias_flag | flag | Elevations potentially affected by 4bin (~60 cm) ranging error |
    | energy_total | energy_total | 1 | Integrated counts in the return waveform relative to the mean nise level |
    | landsat_treecover | landsat_treecover | percent | Tree cover in the year 2010, defined as canopy closure for all L2A vegetation taller than 5 m in height (Hansen et al., 2013). Encoded as a percentage per output grid cell. |
    | landsat_water_persistence | landsat_water_persistence | percent | The percent UMD GLAD Landsat observations with classified Derived surface water between 2018 and 2019. Values >80 usually represent permanent water, while values <10 represent permanent land. |
    | urban_proportion | urban_proportion | percent | The percentage proportion of land area within a focal area surrounding each shot that is urban land cover. Urban land cover is derived from the DLR 12 m resolution TanDEM-X Global Urban Footprint Product. |
    | mean_sea_surface | mean_sea_surface | m | Mean sea surface height above the WGS84 ellipsoid, includes the geoid. Interpolated at latitude_bin0 and longitude_bin0 from DTU15. |
    | num_detectedmodes | num_detectedmodes | 1 | Number of detected modes in rxwaveform |
    | quality_flag | quality_flag | flag | Flag simplifying selection of most useful data |
    | rh | rh | m | Relative height metrics at 98% interval |
    | rx_energy | rx_energy | 1 | total energy f rxwaveform, mean noise removed |
    | selected_algorithm | selected_algorithm | - | ID of algorithm selected as identifying the lowest non-noise mode |
    | sensitivity | sensitivity | degrees | Maximum canopy cover that can be penetrated considering th NR of the waveform |
    | solar_elevation | solar_elevation | degrees | The elevation of the sun position vector from the laser bounce point position in the local ENU frame. The angle is measured from the East-North plane and is positive Up. |
    | surface_flag | surface_flag | flag | Indicates elev_lowestmode is within 300 m of DEM or MSS |
    | egm_08 |  | m | Elevation over the EGM 2008 geoid |
    | tdx_max |  | m | Maximum TanDEM-X DEM value from the pixels overlapping the GEDI footprint |
    | tdx_std |  | m | Standard deviation of TanDEM-X DEM values from the pixels overlapping the GEDI footprint |
    | tdx_mean |  | m | Mean TanDEM-X DEM value from the pixels overlapping the GEDI footprint |
    | tdx_min |  | m | Minimum TanDEM-X DEM value from the pixels overlapping the GEDI footprint |
    | pixel_count |  | 1 | Number of TanDEM-X pixels overlapping the GEDI footprint |

    </center>

![mangrove_tandemx](https://github.com/user-attachments/assets/36fcc005-0a4f-4dac-88eb-3194977281f0)

#### Earth Engine Snippet

```js
var mangrove_tandemx_12 = ee.ImageCollection("projects/sat-io/open-datasets/GLOBAL_MANGROVE_HT_TANDEMX");
var mangrove_gedi = ee.FeatureCollection("projects/space-geographer/assets/GEDI_MANGROVE_HT");
```

Sample Code:  https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/GLOBAL-MANGROVE-CANOPY-HT-TANDEMX

#### License

Data hosted by the ORNL DAAC is openly shared, without restriction, in accordance with NASA's Earth Science program Data and Information Policy

Provided by: Simard et al 2024

Curated in GEE by: Samapriya Roy

Keywords: Mangrove, Tandem-X, Canopy Height, GEDI

Last updated : 2024-07-26
