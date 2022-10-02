---
name: Suggest update to existing awesome-gee-community catalog dataset
about: This template can be issued to create an issue to update an existing dataset
  in the catalog
title: Add existing Dataset Title/Name
labels: update dataset
assignees: samapriya, valpasq, edtrochim

---

Follow the underlying template when creating an update request for an existing dataset in the awesome-gee-community-catalog.

Please edit the markdown text below as needed

### Dataset Name and Catalog Page
Dataset Name and provide a link to the current dataset page.

### Dataset update, version, and release date
Describe updates made to the dataset, including update date, release, and/or version number pertaining to it.

### Updated dataset link
Link to the updated dataset. If the dataset is already an Earth Engine image collection provide the snippet

```js
var updated_collection = ee.ImageCollection("path to your collection")

or

var updated_image = ee.Image("path to your image")

or

var updated_table = ee.FeatureCollection("path to your table/feature collection")
```

### Reason for update
If you own a particular dataset you should provide a reason for dataset update like reanalysis performed, a version was upgraded or if the data was temporarily removed for assessment, and so on.

### Updated License
If the license remains the same just mention N/A

### Relationship to Dataset
Owner/Maintainer/Curator or Reporter

Sample Code: Add a sample code maybe just adding your datasets in the code editor.

Last updated: Last date the dataset was updated if known
