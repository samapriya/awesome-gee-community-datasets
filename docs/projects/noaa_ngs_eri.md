# NOAA NGS Emergency Response Imagery

The NOAA National Geodetic Survey (NGS) Remote Sensing Division operates the Emergency Response Imagery (ERI) Program to rapidly acquire airborne imagery following natural disasters. Missions are prioritized to collect time-sensitive data over impacted coastal zones to support response, recovery, and situational awareness. Imagery is collected as soon as weather and flight conditions permit and released publicly as quickly as possible.

This aerial imagery was acquired by the NOAA Remote Sensing Division to support NOAA national security and emergency response requirements. The aerial imagery primarily supports NOAA interests including safety of navigation, HAZMAT and marine debris impacts, and coastal zone management activities. The data are not intended for mapping, charting, or navigation and are not suitable for litigation. The imagery is also used for research and development of airborne digital imagery standards.

#### Hurricane Melissa (2025)

Aerial imagery was acquired following Hurricane Melissa in targeted areas in Jamaica. The aerial photography missions were conducted by the NOAA Remote Sensing Division. The images were acquired using a Digital Sensor System (DSS) version 6.


#### Sample Dataset Details (Hurricane Melissa)

<center>

| **Parameter**                | **Details**                                      |
|------------------------------|--------------------------------------------------|
| **Sensor**                   | Digital Sensor System (DSS) Version 6            |
| **Platform**                 | Airplane                                         |
| **Spectral Information**     | Natural color (RGB)                              |
| **Ground Sample Distance**   | Approximately 15–30 cm                           |
| **Image Format**             | 8-bit RGB                                        |
| **Image Tile Size**          | Approximately 2.5 km by 2.5 km                   |
| **Horizontal Accuracy**      | Estimated 3–5 meters (minimal topographic relief)|
| **Temporal Coverage**        | 31 October 2025 - 6 November 2025                |

</center>

#### Citation

```
National Geodetic Survey, 2025: 2025 NOAA NGS Emergency Response Imagery: Hurricane Melissa.
https://www.fisheries.noaa.gov/inport/item/78480
```

#### Use Constraints

Users should be aware that temporal changes may have occurred since data collection. The dataset may not represent current ground conditions and should not be used for critical applications or litigation.

![IS2CHM](../images/noaa_ngs_eri.gif)

#### Earth Engine Snippet

```js
// Load the image collection
var dataset = ee.ImageCollection('projects/sat-io/open-datasets/NOAA_EVENTS/2025_HURRICANE_MELISSA');

// Select RGB bands (ignore b4 alpha band)
var collection = dataset.select(['b1', 'b2', 'b3']);

print('Total Images:', collection.size());

// RGB visualization parameters
var rgbVis = {
  min: 0,
  max: 255,
  bands: ['b1', 'b2', 'b3']
};

// Center on the collection
Map.setCenter(-77.357, 18.1256, 9);

// Function to add date property
function addDateProperty(image) {
  var date = ee.Date(image.get('system:time_start'));
  var dateString = date.format('YYYY-MM-dd');
  return image.set('date', dateString);
}

var collectionWithDates = collection.map(addDateProperty);

// Get unique dates
var dates = collectionWithDates.aggregate_array('date').distinct().sort();

print('Acquisition Dates:', dates);

// Add one layer for each date
dates.evaluate(function(dateList) {
  dateList.forEach(function(date) {
    var dailyImages = collectionWithDates.filter(ee.Filter.eq('date', date));
    var mosaic = dailyImages.mosaic();

    dailyImages.size().evaluate(function(count) {
      Map.addLayer(mosaic, rgbVis, date + ' (' + count + ' images)');
    });
  });
});
```

Sample Code:  https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-events-layers/NOAA-NGS-ERI-IMAGERY

#### Additional Event Imagery

More emergency response imagery from other events will be continuously added to the NOAA_EVENTS folder. To discover all available event collections, you can list the assets programmatically

```js
// List all available event imagery collections
var collections = ee.data.listAssets("projects/sat-io/open-datasets/NOAA_EVENTS");
print(collections['assets']);
```

This will return all hurricane and disaster event imagery datasets currently available in the collection.

#### License

These data were produced by NOAA and are not subject to copyright protection in the United States. NOAA waives any potential copyright and related rights worldwide under the Creative Commons Zero 1.0 Universal Public Domain Dedication (CC0-1.0).

Keywords: Emergency Response, Hurricane, Aerial Imagery, Natural Disasters, NOAA, NGS, Coastal Zones, Jamaica, Caribbean

Provided by: NOAA National Geodetic Survey

Curated in GEE by: Samapriya Roy

Last updated: 2025-12-15
