# Open Aerial Map Subset

[OpenAerialMap (OAM) was created as a set of tools and portal](https://openaerialmap.org/) for searching, sharing, and using openly licensed satellite and unmanned aerial vehicle (UAV) imagery. Built on top of the Open Imagery Network (OIN), OAM is an open service that provides search and access to this imagery. While Open Aerial Map is excellent and with plug and play capability coming in the future this will only evolve as a resouce for most users the goal of bringing a subset in Google Earth Engine was to explore current capabilities of the platform with ultra high resolution datasets and to allow for labeling classification and potential use of the collection as teaching and training tool via plugins like Collect Earth online and other providers who might be interested in leveraging this further including applications like Machine learning models.

While a lot of preprocessing steps were applied the datasets are initially housed withing the analysis ready datasets snippets to reflect these images are often post processed by providers and are effectively ready to use to some extent.

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.

#### Data preprocessing

For creating a collection subset a automated script was created to fetch all images with a valid link and those that are not related to the platform satellite. This was to keep the overall platforms limited to other forms of platforms. The datasets were upload into a GCS bucket before ingest and while the uncompressed size for the overall collection was only 1.9 TB , GEE uncompressed quota usage exceed over 7+ TB. I am hoping to do more event specific updates in the future to allow for exploration across different use cases. Since a lot of the no data values for 8 bit imagery were coded incorrectly 0 and 255 were chosen and default nodata values list but results will vary depending on the individual images.

<img width="960" alt="oam_heatmap" src="https://user-images.githubusercontent.com/6677629/233264323-c6aa5de6-f471-4e17-ab9b-b5188a5bd397.PNG">

#### Earth Engine Snippet

```js
var oam_subset = ee.ImageCollection("projects/sat-io/open-datasets/open-aerial-map");
```

Sample Script: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:analysis-ready-data/OPEN-AERIAL-MAP

#### License
All imagery is publicly licensed and made available through the Humanitarian OpenStreetMap Team's Open Imagery Network (OIN) Node. All imagery contained in OIN is licensed CC-BY 4.0, with attribution as contributors of Open Imagery Network. Each imagery has their own license type and it is included in the image metadata.

Provided by: Open Aerial Map Community providers

Curated in GEE by : Samapriya Roy

keywords: Open Aerial Map, OAM, HOTOSM, Drones, UAV, High resolution

Last updated on GEE: 2023-04-20

