# SWOT River Database (SWORD)

The Surface Water and Ocean Topography (SWOT) satellite mission, successfully launched in December 2022, has revolutionized our ability to observe rivers by providing vast datasets of river water surface elevation, width, and slope measurements. To maximize the utility and flexibility of this data, the SWOT mission delivers a variety of data products, including river vector data in shapefile format for each SWOT overpass. These vector products offer immense potential for multi-temporal analysis of river systems, allowing researchers to track changes in river characteristics over time.

To enable this type of analysis, it was crucial to define consistent river reaches and nodes before the launch of SWOT. This ensures that data from different overpasses can be accurately assigned and compared. The SWOT River Database (SWORD) fulfills this critical role by combining multiple global datasets related to rivers and satellite observations. SWORD provides a standardized framework of high-resolution river nodes (spaced every 200 meters along river centerlines) and reaches (river segments of approximately 10 kilometers) in both shapefile and netCDF formats. These nodes and reaches are accompanied by a range of relevant hydrologic variables such as water surface elevation, width, slope, and information on river obstructions, flow accumulation, and more. This comprehensive dataset, covering global rivers 30 meters wide and greater, empowers researchers to conduct in-depth analysis of river systems and utilize SWOT data to its full potential.

SWORD integrates data from several existing global hydrography datasets, including the Global River Widths from Landsat (GRWL), MERIT Hydro, HydroBASINS, and the Global River Obstruction Database (GROD). It provides a wealth of attributes for each node and reach, such as:

* Location: Latitude/longitude coordinates, reach boundaries.
* Physical characteristics: Water surface elevation, width, slope, flow accumulation, number of channels, obstruction type (dams, waterfalls, etc.).
* Hydrologic modeling: Parameters for various discharge estimation models (e.g., MetroMan, BAM, HiVDI) and associated uncertainties.
* SWOT observation information: Number of SWOT passes and specific orbit tracks intersecting each reach during the 21-day orbit cycle.
* Additional attributes: River names, ice cover flags, tributary flags, and quality flags indicating potential topological inconsistencies or data limitations.



??? example "Expand to show Node attribute descriptions"

    <center>

    | Attribute    | Description                                                                                                                       | Units                    |
    |--------------|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------|
    | x            | Longitude of each node ranging from 180°E to 180°W                                                                               | decimal degrees          |
    | y            | Latitude of each node, ranging from 90°S to 90°N                                                                                 | decimal degrees          |
    | node_id      | Unique identifier for each node, formatted as: CBBBBBRRRRNNNT (C: Continent, B: Pfafstetter basin codes, R: Reach ID, N: Node ID within reach, T: Type) | none                     |
    | node_length  | Length of the node measured along the high-resolution centerline points                                                          | meters                   |
    | reach_id     | ID of the reach associated with each node, formatted as: CBBBBBRRRRT (C: Continent, B: Pfafstetter basin codes, R: Reach ID, T: Type) | none                     |
    | wse          | Average water surface elevation of the node                                                                                      | meters                   |
    | wse_var      | Variance of water surface elevation along the high-resolution centerline points used to calculate the average water surface elevation for each node | meters^2                  |
    | width        | Average width of the node                                                                                                        | meters                   |
    | width_var    | Variance of width along the high-resolution centerline points used to calculate the average width for each node                  | meters^2                  |
    | n_chan_max   | Maximum number of channels observed within the node                                                                              | none                     |
    | n_chan_mod   | Mode (most frequent) number of channels observed within the node                                                                 | none                     |
    | obstr_type   | Type of obstruction at the node based on GROD and HydroFALLS databases: 0 - No Dam, 1 - Dam, 2 - Lock, 3 - Low Permeable Dam, 4 - Waterfall | none                     |
    | grod_id      | Unique GROD ID for nodes with obstr_type values 1-3                                                                              | none                     |
    | hfalls_id    | Unique HydroFALLS ID for nodes with obstr_type value 4                                                                          | none                     |
    | dist_out     | Distance from the river outlet to the node                                                                                        | meters                   |
    | type         | Node type identifier: 1 - River, 3 - Lake on river, 4 - Dam/waterfall, 5 - Unreliable topology, 6 - Ghost node                  | none                     |
    | facc         | Maximum flow accumulation value for the node                                                                                     | kilometers^2              |
    | lakeflag     | GRWL water body identifier: 0 - River, 1 - Lake/reservoir, 2 - Canal, 3 - Tidally influenced river                              | none                     |
    | max_width    | Maximum width across the channel for the node, including islands and bars                                                        | meters                   |
    | river_name   | All river names associated with the node (separated by semicolons if multiple)                                                    | none                     |
    | sinuosity    | Ratio of total reach length to the straight-line distance between reach endpoints, indicating the degree of meandering             | none                     |
    | meand_len    | Average length of meanders the node belongs to                                                                                    | meters                   |
    | manual_add   | Binary flag indicating if the node was manually added to GRWL centerlines (1) or not (0)                                          | none                     |
    | trib_flag    | Binary flag indicating if a large tributary not in SWORD enters the node (1) or not (0)                                           | none                     |

??? example "Expand to show Reach attribute descriptions"

    <center>

    | Attribute   | Description                                                                                                                         | Units             |
    |-------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------|
    | x           | Longitude of the reach center point (ranging from 180°E to 180°W)                                                                   | decimal degrees   |
    | y           | Latitude of the reach center point (ranging from 90°S to 90°N)                                                                     | decimal degrees   |
    | reach_id    | Unique identifier for each reach, formatted as: CBBBBBRRRRT (C: Continent, B: Pfafstetter basin codes, R: Reach ID, T: Type)     | none              |
    | reach_length | Length of the reach measured along the high-resolution centerline points                                                           | meters            |
    | wse         | Average water surface elevation of the reach                                                                                       | meters            |
    | wse_var     | Variance of water surface elevation along the high-resolution centerline points used to calculate the average water surface elevation for each reach | meters^2           |
    | width       | Average width of the reach                                                                                                         | meters            |
    | width_var   | Variance of width along the high-resolution centerline points used to calculate the average width for each reach                   | meters^2          |
    | n_nodes     | Number of nodes associated with the reach                                                                                          | none              |
    | n_chan_max  | Maximum number of channels observed within the reach                                                                               | none              |
    | n_chan_mod  | Mode (most frequent) number of channels observed within the reach                                                                  | none              |
    | obstr_type  | Type of obstruction within the reach based on GROD and HydroFALLS databases: 0 - No Dam, 1 - Dam, 2 - Lock, 3 - Low Permeable Dam, 4 - Waterfall | none              |
    | grod_id     | Unique GROD ID for reaches with obstr_type values 1-3                                                                              | none              |
    | hfalls_id   | Unique HydroFALLS ID for reaches with obstr_type value 4                                                                          | none              |
    | slope       | Average slope of the reach calculated along the high-resolution centerline points                                                  | m/km              |
    | dist_out    | Distance from the river outlet to the reach                                                                                         | meters            |
    | n_rch_up    | Number of upstream reaches connected to this reach                                                                                 | none              |
    | n_rch_down  | Number of downstream reaches connected to this reach                                                                               | none              |
    | rch_id_up   | IDs of the upstream reaches connected to this reach                                                                                 | none              |
    | rch_id_dn   | IDs of the downstream reaches connected to this reach                                                                               | none              |
    | lakeflag    | GRWL water body identifier: 0 - River, 1 - Lake/reservoir, 2 - Canal, 3 - Tidally influenced river                                 | none              |
    | max_width   | Maximum width across the channel for the reach, including islands and bars                                                         | meters            |
    | type        | Reach type identifier: 1 - River, 3 - Lake on river, 4 - Dam/waterfall, 5 - Unreliable topology, 6 - Ghost reach                 | none              |
    | facc        | Maximum flow accumulation value for the reach                                                                                      | kilometers^2      |
    | swot_obs    | Maximum number of SWOT passes intersecting the reach during the 21-day orbit cycle                                                 | none              |
    | swot_orbits | List of SWOT orbit track numbers that intersect the reach during the 21-day cycle                                                  | none              |
    | river_name  | All river names associated with the reach (separated by semicolons if multiple)                                                     | none              |
    | trib_flag   | Binary flag indicating if a large tributary not in SWORD enters the reach (1) or not (0)                                           | none              |

#### Dataset preprocessing
Reaches and nodes shapefile datasets were downloaded zipped and uploaded as individual component shapefiles. The folder assets were then merged to create a single nodes and reaches files. Attributes were preserved as is from the shapefiles.

#### Citation

```
Altenau et al., (2021) The Surface Water and Ocean Topography (SWOT) Mission River Database (SWORD): A Global River Network for Satellite Data
Products. Water Resources Research. https://doi.org/10.1029/2021WR030054
```

#### Dataset citation

```
Elizabeth H. Altenau, Tamlin M. Pavelsky, Michael T. Durand, Xiao Yang, Renato P. d. M. Frasson, & Liam Bendezu. (2023). SWOT River Database (SWORD)
(Version v16) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.10013982
```

![nodes_reaches](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/17e8c630-e84c-46db-95d3-c56d9e900412)

#### Earth Engine Snippet

```js
var nodes_merged = ee.FeatureCollection("projects/sat-io/open-datasets/SWORD/nodes_merged");
var reaches_merged = ee.FeatureCollection("projects/sat-io/open-datasets/SWORD/reaches_merged");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/SWORD-NODES-REACHES-MERGED

Individual nodes and reaches files were ingested for reference and can be access by the users by using

```js
var ee_nodes = ee.data.listAssets("projects/sat-io/open-datasets/SWORD/nodes");
var ee_reaches = ee.data.listAssets("projects/sat-io/open-datasets/SWORD/reaches");

print('Total of '+ee.List(ee_nodes.assets).size().getInfo()+ ' assets in nodes',ee_nodes.assets);
print('Total of '+ee.List(ee_reaches.assets).size().getInfo()+ ' reaches in nodes',ee_reaches.assets);
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/SWORD-NODES-REACHES

#### License

The datasets are provided under a Creative Commons 4.0 International License.

Provided by: Altenau et al., (2021)

Curated in GEE by: Samapriya Roy

Keywords: SWORD,SWOT,Rivers,Hydrology,Hydrography,River Networks,Global

Last updated in GEE: 2024-04-12

