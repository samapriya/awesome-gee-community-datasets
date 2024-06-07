/**** Start of imports. If edited, may not auto-convert in the playground. ****/
var ca_lc = ee.ImageCollection("projects/sat-io/open-datasets/CA_FOREST_LC_VLCE2");
/***** End of imports. If edited, may not auto-convert in the playground. *****/
var ca_lc_last = ee.Image(ca_lc.sort('system:time_start',false).first());

var from = [0, 20, 31, 32, 33, 40, 50, 80, 81, 100, 210, 220, 230];
var to =   [0, 1,  2,  3,  4,  5,  6,  7,  8,  9,   10,  11,  12 ];
ca_lc_last = ca_lc_last.remap(from, to);

print("Reclassed values:");
print({"from": from, "to": to});

// Define a dictionary which will be used to make legend and visualize image on map
var dict = {
  "names": [
  "Unclassified",
  "Water",
  "Snow/Ice",
  "Rock/Rubble",
  "Exposed/Barren land",
  "Bryoids",
  "Shrubs",
  "Wetland",
  "Wetland-treed",
  "Herbs",
  "Coniferous",
  "Broadleaf",
  "Mixedwood"
  ],
  "colors": [
    "#686868",
    "#3333ff",
    "#ccffff",
    "#cccccc",
    "#996633",
    "#ffccff",
    "#ffff00",
    "#993399",
    "#9933cc",
    "#ccff33",
    "#006600",
    "#00cc00",
    "#cc9900"
  ]};

// Create a panel to hold the legend widget
var legend = ui.Panel({
  style: {
    position: 'bottom-left',
    padding: '8px 15px'
  }
});

// Function to generate the legend
function addCategoricalLegend(panel, dict, title) {

  // Create and add the legend title.
  var legendTitle = ui.Label({
    value: title,
    style: {
      fontWeight: 'bold',
      fontSize: '18px',
      margin: '0 0 4px 0',
      padding: '0'
    }
  });
  panel.add(legendTitle);

  var loading = ui.Label('Loading legend...', {margin: '2px 0 4px 0'});
  panel.add(loading);

  // Creates and styles 1 row of the legend.
  var makeRow = function(color, name) {
    // Create the label that is actually the colored box.
    var colorBox = ui.Label({
      style: {
        backgroundColor: color,
        // Use padding to give the box height and width.
        padding: '8px',
        margin: '0 0 4px 0'
      }
    });

    // Create the label filled with the description text.
    var description = ui.Label({
      value: name,
      style: {margin: '0 0 4px 6px'}
    });

    return ui.Panel({
      widgets: [colorBox, description],
      layout: ui.Panel.Layout.Flow('horizontal')
    });
  };

  // Get the list of palette colors and class names from the image.
  var palette = dict['colors'];
  var names = dict['names'];
  loading.style().set('shown', false);

  for (var i = 0; i < names.length; i++) {
    panel.add(makeRow(palette[i], names[i]));
  }

  Map.add(panel);

}


/*
  // Display map and legend ///////////////////////////////////////////////////////////////////////////////
*/

// Add the legend to the map
addCategoricalLegend(legend, dict, 'CA Annual forest LC map 2019');

Map.setCenter(-97.61655457157725,55.6280720462063,4)

// Add image to the map
Map.addLayer(ca_lc_last.mask(ca_lc_last.neq(0)), {min:0, max:12, palette:dict['colors']}, 'CA Annual forest LC map 2019')
