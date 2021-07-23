---
name: Update Community GEE Dataset Template
about: This template can be issued to create an issue to update an existing dataset
title: Dataset Name
labels: ''
assignees: samapriya

---

Follow the underlying template when creating an update dataset request

### Dataset Name and Catalog Page
Dataset Name and provide a link to the current dataset page.

### Dataset update , version and release date
Describe updates made to the dataset, including update date, release and/or version number pertaining to it.

### Updated dataset link
Link to the update dataset , if the dataset is already an Earth Engine image collection provide the snippet

```js
var updated_dataset = ee.Image('path to updated dataset')
```

### Reason for update
If you own a particular dataset you should provide a reason for dataset update like reanalysis performed, temporarily removed for assessment and so on

### Updated License
If the license remains the same just mention N/A

### Relationship to Dataset
Owner/Maintainer/Curator or any other

Sample Code: Add a sample code maybe just adding your datasets in code editor and visualizing or summarizing with the updated dataset

Last updated: Last date you updated the dataset
