// 01 repo
var piscoeo_cl = ee.ImageCollection('users/lgutierrezlf/PISCOeo_pm/climatology');
var piscoeo_yr = ee.ImageCollection('users/lgutierrezlf/PISCOeo_pm/yearly');
var piscoeo_mn = ee.ImageCollection('users/lgutierrezlf/PISCOeo_pm/monthly');
var piscoeo_dy = ee.ImageCollection('users/lgutierrezlf/PISCOeo_pm/daily');
// 02 date filter
var vis = {min: 0, max: 2500, palette: '#ffffcc,#a1dab4,#41b6c4,#2c7fb8,#253494'};
var composite = piscoeo_cl.sum().visualize(vis);
var compositeLayer = ui.Map.Layer(composite).setName('Climatology');
var mapPanel = ui.Map();
var layers = mapPanel.layers();
layers.add(compositeLayer, 'Climatology');
// 02 Panel General
var inspectorPanel = ui.Panel({style: {width: '30%'}});
var intro = ui.Panel([
  ui.Label({
    value: 'PISCOeo_pm - Explorer',
    style: {fontSize: '20px', fontWeight: 'bold'}
  }),
  ui.Label('Click a location to see and download a reference evapotranspiration time series.')
]);
inspectorPanel.add(intro);
var lon = ui.Label();
var lat = ui.Label();
inspectorPanel.add(ui.Panel([lon, lat], ui.Panel.Layout.flow('horizontal')));
var date_start = ui.Textbox({
  value: '2011-01-01',
  onChange: function(value) {
    date_start.setValue(value);
    return(value);
  }
});
var date_end = ui.Textbox({
  value: '2017-01-01',
  onChange: function(value) {
    date_end.setValue(value);
    return(value);
  }
});
var start = ee.Date('2005-01-01')
var end = ee.Date('2017-01-01')
//inspectorPanel.add(ui.Panel([date_start, date_end], ui.Panel.Layout.flow('horizontal')));
// 03 Panel time series
var piscoeo_dy = piscoeo_dy.filterDate(start, end);
var generateChart = function (coords) {
  lon.setValue('lon: ' + coords.lon.toFixed(2));
  lat.setValue('lat: ' + coords.lat.toFixed(2));
  var point = ee.Geometry.Point(coords.lon, coords.lat);
  var dot = ui.Map.Layer(point, {color: '000000'}, 'point location');
  mapPanel.layers().set(1, dot);
  var peo_ts_cl = ui.Chart.image.series(piscoeo_cl, point, ee.Reducer.mean(), 500);
  var peo_ts_yr = ui.Chart.image.series(piscoeo_yr, point, ee.Reducer.mean(), 500);
  var peo_ts_mn = ui.Chart.image.series(piscoeo_mn, point, ee.Reducer.mean(), 500);
  var peo_ts_dy = ui.Chart.image.series(piscoeo_dy, point, ee.Reducer.mean(), 500);
  peo_ts_cl.setOptions({
    title: 'Climatology',
    vAxis: {title: 'Eo_pm (mm/month)'},
    hAxis: {title: 'Month', format: 'MM', gridlines: {count: 12}},
    series: {
      0: {
        color: 'steelblue',
        lineWidth: 0.7,
        pointsVisible: false,
        pointSize: 0,
      },
    },
    legend: {position: 'none'}
  });
  peo_ts_yr.setOptions({
    title: 'Yearly',
    vAxis: {title: 'Eo_pm (mm/year)'},
    hAxis: {title: 'Year', format: 'YYYY', gridlines: {count: 18}},
    series: {
      0: {
        color: 'steelblue',
        lineWidth: 0.7,
        pointsVisible: false,
        pointSize: 0,
      },
    },
    legend: {position: 'none'}
  });
  peo_ts_mn.setOptions({
    title: 'Monthly',
    vAxis: {title: 'Eo_pm (mm/month)'},
    hAxis: {title: 'Year', format: 'YYYY', gridlines: {count: 18}},
    series: {
      0: {
        color: 'steelblue',
        lineWidth: 0.7,
        pointsVisible: false,
        pointSize: 0,
      },
    },
    legend: {position: 'none'}
  });
  peo_ts_dy.setOptions({
    title: 'Daily',
    vAxis: {title: 'Eo_pm (mm/day)'},
    hAxis: {title: 'Year', format: 'YYYY', gridlines: {count: 18}},
    series: {
      0: {
        color: 'steelblue',
        lineWidth: 0.7,
        pointsVisible: false,
        pointSize: 0,
      },
    },
    legend: {position: 'none'}
  });
  inspectorPanel.widgets().set(3, peo_ts_cl);
  inspectorPanel.widgets().set(4, peo_ts_yr);
  inspectorPanel.widgets().set(5, peo_ts_mn);
  inspectorPanel.widgets().set(6, peo_ts_dy);
};
// 04 Panel Legend
function makeColorBarParams(palette) {
  return {
    bbox: [0, 0, 1, 0.1],
    dimensions: '100x10',
    format: 'png',
    min: 0,
    max: 1,
    palette: palette,
  };
}
var colorBar = ui.Thumbnail({
  image: ee.Image.pixelLonLat().select(0),
  params: makeColorBarParams(vis.palette),
  style: {stretch:'horizontal', margin:'0px 8px', maxHeight:'15px'},
});
var legendLabels = ui.Panel({
  widgets: [
    ui.Label(vis.min, {margin: '4px 8px'}),
    ui.Label((vis.max/4),{margin:'4px 8px', textAlign:'center', stretch:'horizontal'}),
    ui.Label((vis.max/2),{margin:'4px 8px', textAlign:'center', stretch:'horizontal'}),
    ui.Label((vis.max/4*3),{margin:'4px 8px', textAlign:'center', stretch:'horizontal'}),
    ui.Label(vis.max, {margin: '4px 8px'})
  ],
  layout: ui.Panel.Layout.flow('horizontal')
});
var legendTitle = ui.Label({
  value: 'Map Legend: Evapotranspiration mean (mm/year)',
  style: {fontWeight: 'bold'}
});
var legendPanel = ui.Panel([legendTitle, colorBar, legendLabels]);
inspectorPanel.widgets().set(2, legendPanel);
// 05 Map
mapPanel.onClick(generateChart);
mapPanel.style().set('cursor', 'crosshair');
var initialPoint = ee.Geometry.Point(-75.5, -10);
mapPanel.centerObject(initialPoint, 6);
ui.root.clear();
ui.root.add(ui.SplitPanel(inspectorPanel, mapPanel));
generateChart({
  lon: initialPoint.coordinates().get(0).getInfo(),
  lat: initialPoint.coordinates().get(1).getInfo()
});