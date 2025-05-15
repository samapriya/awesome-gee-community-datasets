# Catalog assets

![GEE Community Datasets](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/samapriya/34bc0c1280d475d3a69e3b60a706226e/raw/community.json)

It is feasible to sometimes use a machine readable list of catalog assets. While we are going to introduce a STAC catalog again at some point the assets are also available in two specific formats with the total running count above.

<center>

<div class="result" markdown>

[&nbsp; Download latest JSON version here:fontawesome-solid-download:][download-json]{ .md-button .md-button--primary}

</div>

</center>

[download-json]: https://raw.githubusercontent.com/samapriya/awesome-gee-community-datasets/master/community_datasets.json

## JSON format
This holds information about the datasets in this structure as a JSON list. If the license is custom for a dataset license text is included to clarify the details. The structure is the following

| **Field**         | **Description**                                                                                             |
|-------------------|-------------------------------------------------------------------------------------------------------------|
| **Title**         | The name of the dataset.                                                                                    |
| **Sample Code**   | A link to a sample script demonstrating how to use the dataset in Google Earth Engine.                     |
| **Type**          | The type of data (e.g., table).                                                                             |
| **ID**            | The unique identifier for the dataset in the Earth Engine catalog.                                          |
| **Provider**      | The organization or entity that provides the dataset.                                                       |
| **Tags**          | Keywords associated with the dataset to help with search and categorization.                                |
| **License**       | The licensing terms under which the dataset is provided.                                                    |
| **License Text**  | Additional text explaining the license (if applicable).                                                     |
| **Docs**          | A link to documentation or more information about the dataset.                                              |
| **Thematic Group**| The category or group under which the dataset falls (e.g., Oceans and Shorelines, Hydrology).               |


```json
[
    {
        "title": "Global Shoreline Dataset",
        "sample_code": "https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:oceans-shorelines/GLOBAL_SHORELINES",
        "type": "table",
        "id": "projects/sat-io/open-datasets/shoreline/mainlands",
        "provider": "United States Geological Survey, USGS",
        "tags": "Global Shoreline, Shoreline, mainlands, Oceans",
        "license": "Creative Commons Attribution Share Alike 4.0 International",
        "docs": "https://gee-community-catalog.org/projects/shoreline/",
        "thematic_group": "Oceans and Shorelines"
    },
    {
        "title": "NWI_CO_Riparian_Project_Metadata",
        "sample_code": "https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/NATIONAL-WETLANDS-INVENTORY",
        "type": "table",
        "id": "projects/sat-io/open-datasets/NWI/rpm/CO_Riparian_Project_Metadata",
        "provider": "U.S. Fish and Wildlife Service",
        "tags": "wetlands, conservation areas, habitats, fish, wildlife, drinking water, recreation, U.S. Fish and Wildlife Service,CO_Riparian_Project_Metadata",
        "license": "custom",
        "license_text": "The US FWS National Wetlands Inventory (NWI) is a publicly available resource that provides detailed information on the abundance, characteristics, and distribution of US",
        "docs": "https://gee-community-catalog.org/projects/nwi/",
        "thematic_group": "Hydrology"
    }
]
```

## CSV Format
The CSV file is created using a Github action within the repository and contains all fields in the JSON representation. Fields like license_text if empty for a specific license are left empty.

<center>

<div class="result" markdown>

[&nbsp; Download latest CSV version here:fontawesome-solid-download:][download-csv]{ .md-button .md-button--primary}

</div>

</center>

[download-csv]: https://raw.githubusercontent.com/samapriya/awesome-gee-community-datasets/master/community_datasets.csv


|id                                               |provider                             |title                   |type |tags                                          |sample_code                                                                                                                  |license                                                   |license_text|docs_page                                            |thematic_group       |
|-------------------------------------------------|-------------------------------------|------------------------|-----|----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|------------|-----------------------------------------------------|---------------------|
|projects/sat-io/open-datasets/shoreline/mainlands|United States Geological Survey, USGS|Global Shoreline Dataset|table|Global Shoreline, Shoreline, mainlands, Oceans|https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:oceans-shorelines/GLOBAL_SHORELINES|Creative Commons Attribution Share Alike 4.0 International|NA          |https://gee-community-catalog.org/projects/shoreline/|Oceans and Shorelines|
|projects/sat-io/open-datasets/NWI/rpm/CO_Riparian_Project_Metadata|U.S. Fish and Wildlife Service       |NWI_CO_Riparian_Project_Metadata|table|wetlands, conservation areas, habitats, fish, wildlife, drinking water, recreation, U.S. Fish and Wildlife Service,CO_Riparian_Project_Metadata|https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/NATIONAL-WETLANDS-INVENTORY|custom                                                    |The US FWS National Wetlands Inventory (NWI) is a publicly available resource that provides detailed information on the abundance, characteristics, and distribution of US|https://gee-community-catalog.org/projects/nwi/      |Hydrology            |
