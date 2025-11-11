# Carbon Offset Project Boundaries

Nature-based climate solutions (NBS) have become an important component of  strategies aiming to reduce atmospheric CO2 and mitigate climate change impacts. Carbon offsets have emerged as one of the most widely implemented NBS strategies, however, these projects have also been criticized for exaggerating offsets. Verifying the efficacy of NBS-derived carbon offset is complicated by a lack of readily available geospatial boundary data. Herein, we detail methods and present a database of nature-based offset project boundaries. This database provides the locations of 575 NBS projects distributed across 55 countries. Geospatial boundaries were aggregated using a combination of scraping data from carbon project registries  (n=433, 75.3%) as well as manual georeferencing and digitization (n=127, 22.1%). Database entries include three varieties of carbon projects: avoided deforestation, afforestation, reforestation and re-vegetation, and improved forest management. An accuracy assessment of the georeferencing and digitizing process indicated a high degree of accuracy (intersection over union score of 0.98 +/- 0.015).

You can read the [dataset publication here](https://www.nature.com/articles/s41597-025-04868-2) and find the [dataset here](https://zenodo.org/records/11459391).

#### Database notes

- Users must carefully distinguish between overall project areas and project accounting areas based on their specific analysis requirements:
  * The **project area** is defined as the geographical area where the project participants implement activities to reduce deforestation.
  * The **project accounting area** is defined as the geographical area of the project that was used to calculate carbon credit issuance.

- This database does not represent a census of nature-based carbon projects and does not contain all varieties of nature-based carbon projects.

- Users should verify that any georeferencing inaccuracies will not significantly impact their analyses.

- The boundaries included in the database reflect the data available in the registries at the time of access, with some projects regularly updating their information.

- We note that we were unable to assess the accuracy of the boundaries constructed from linear features or from a developer provided protocol.

#### Dataset Description

| Attribute                     | Description                                                                                                                                                                  |
|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Project Name**              | The name of the carbon project as given in the documentation.                                                                                                               |
| **ProjectID**                 | A combination of the registry abbreviation and project number.                                                                                                               |
| **Registry Name**             | The name of the registry where project information is hosted. Possible values are: American Carbon Registry, BioCarbon Registry, Climate Action Reserve, EcoRegistry, Gold Standard, Verra. |
| **Methodology**               | The name of the methodology used for the project’s implementation.                                                                                                           |
| **Project Type**              | The type of forestry carbon offset program. One of the following: ARR, AD, IFM.                                                                                             |
| **Country**                   | The country where the project is located.                                                                                                                                      |
| **Project Developer Name**    | Name of the entity or individual organizing, proposing, or advocating a particular carbon offset project. In case of multiple entities/individuals, only the first name is recorded here. |
| **Project Start Date**        | Date of the start of the crediting period (mm/dd/yyyy).                                                                                                                       |
| **Project End Date**          | Date of the end of the crediting period (mm/dd/yyyy).                                                                                                                         |
| **Date of Entry**             | Date when the project information was added to the database (mm/dd/yyyy).                                                                                                     |
| **Processing Approach**       | One of four possible values: Official, Georeferenced, Linear, or Method. Official if the canonical boundary was obtained from a registry or the project developer. Georeferenced if the boundary data was obtained via georeferencing and digitizing maps obtained from the project documents. Linear if the boundary data were distributed as linear features that were processed into geometries. Method if a developer specified protocol was followed to obtain the boundary data. |
| **PD Declined to Provide**    | One of: Yes, No, N/A. Yes if the project developer was contacted for the project geometry but declined to provide the necessary information. No if the project developer provided the geometries or sufficient information to create the project geometry. N/A if the geometry was available from a registry and the developer was not contacted. |
| **Geometry Type**             | One of: Point or Polygon. Indicates if the geometry in the database is a point or a polygon.                                                                                  |
| **Project Area**              | The well-known text (WKT) representation of the geographical area where the project participants implement activities to reduce deforestation.                               |
| **Project Accounting Area**   | The WKT representation of the geographical area of the project which was used to calculate carbon credits. If the project area is the same as the project accounting area, then the project accounting area is not defined. |
| **Project Reference Region**  | The well-known text (WKT) representation of the geographical area of the project from where historical and current deforestation and forest degradation quantities and trends are obtained. This is not always defined. |
| **Comment**                   | Notes about how manual referencing was carried out or other relevant information.                                                                                             |

#### Citation

```
Karnik, Akshata, John Kilbride, Tristan Goodbody, Rachael Ross, and Elias Ayrey. "An open-access database of nature-based carbon offset project
boundarie." (2024).
```

#### Dataset Citation

```
Karnik, A., Kilbride, J., Goodbody, T., Rachel, R., & Ayrey, E. (2024). A global database of nature-based carbon offset project boundaries [Data set]. Zenodo. https://doi.org/10.5281/zenodo.11459391
```

![ca_projects](https://github.com/user-attachments/assets/1be47dc6-77f2-4adc-9f08-bd603eaf31b5)

#### Earth Engine Snippet

```js
var carbonoffsetscol = ee.FeatureCollection('projects/sat-io/open-datasets/CARBON-OFFSET-PROJECTS-GLOBAL');

var visParams = {
    palette: ['#9ab555'],
    min: 0.0,
    max: 1550000.0,
    opacity: 0.8,
};
var carbonoffsets = ee.Image().float().paint(carbonoffsetscol, 'REP_AREA');

Map.addLayer(carbonoffsets, visParams, 'Existing carbon projects area');
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/GLOBAL-CARBON-OFFSET-PROJECTS

#### License

This dataset is made available under Creative Commons Attribution 4.0 International license.

Keywords: carbon, carbon offsets, NBS, climate change, Nature-based climate solutions, Carbon offsets, Geospatial boundaries, Georeferencing,Forest carbon

Curated in GEE by: Filipe Silveiran and Samapriya Roy

Last updated : 2024-09-07
