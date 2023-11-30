# Global Google-Microsoft Open Buildings Dataset

This dataset consolidates Google's V3 Open Buildings and Microsoft's most recent Building Footprints, comprising a staggering 2,534,595,270 footprints. As of September 2023, it stands out as the most comprehensive openly accessible dataset. Encompassing 92% of Level 0 administrative boundaries, the dataset is organized into 182 partitions. Each footprint is explicitly labeled with its origin, denoting whether it is from Google or Microsoft. Accessible in cloud-native geospatial formats such as GeoParquet, FlatGeobuf, and PMTiles, this dataset provides a robust resource for various applications. Further details, including the dataset's comprehensive information and methodology, can be explored [here](https://beta.source.coop/repositories/vida/google-microsoft-open-buildings/description/) and [here](https://cloudnativegeo.org/blog/2023/09/introducing-the-ultimate-cloud-native-building-footprints-dataset/), respectively.


#### Dataset Schema
Country level datasets were inegsted while each row in the dataset provides information on a specific building footprint with associated information on individual columns

* boundary_id (INTEGER): A unique ID linking the CGAZ level 0 boundary ISO to an integer, created for partitioning the datasets within BigQuery.
* confidence (FLOAT): A metric denoting the model's confidence about the accuracy of the building footprint. Microsoft-sourced footprints set this column to null since the original dataset doesn't feature this attribute.
* bf_source (STRING): Indicates the footprint's origin - Google or Microsoft.
* area_in_meters (FLOAT): Represents the polygon's area in square meters.

#### Dataset Citation

Please cite the original citations from source dataset including date of access of the combined dataset for citation here is a sample citation

```
Google-Microsoft Open Buildings - combined by VIDA, https://beta.source.coop/repositories/vida/google-microsoft-open-buildings. Date Accessed: [Insert the date you accessed the webpage in the format YYYY-MM-DD]
```

![combined_building_sample](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/7f1a0278-c3f6-4f26-a945-fabc530b7e66)

#### Earth Engine Snippet

The datasets were collected from the country level geoparquet files and only a subset of these are mentioned below while an earthengine ls should provide more information on all countries ingested. All feature collections are in the format

projects/sat-io/open-datasets/VIDA_COMBINED/"3 letter country ISO code"

for example India would be

```js
var ind = ee.FeatureCollection("projects/sat-io/open-datasets/VIDA_COMBINED/IND")
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/GLOBAL-COMBINED-BUILDING-FOOTPRINTS-VIDA

Earth Engine App: https://sat-io.earthengine.app/view/global-buildings

#### License

The data is shared under the Creative Commons Attribution (CC BY-4.0) license and the Open Data Commons Open Database License (ODbL) v1.0 license. As the user, you can pick which of the two licenses you prefer and use the data under the terms of that license.

Contact information: VIDA has provided contact information and if you'd like more information about the dataset or the processing steps, feel free to write an email to darell@vida.place.

Provided by: [VIDA](https://vida.place), Google, Microsoft

Curated in GEE by: Samapriya Roy

Last updated in GEE: 2023-11-28
