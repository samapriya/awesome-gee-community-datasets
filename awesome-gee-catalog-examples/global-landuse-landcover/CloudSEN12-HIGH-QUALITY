var cs12_high = ee.ImageCollection("projects/sat-io/open-datasets/cloudsen12/high");

// viz
var border_style = {"style":{"color": "FF00FF",   "fillColor":"00000000"}}
var s2id = {"bands": ["B4", "B3", "B2"], "min":0 ,"max": 3000}
var gt = {"min":1, "max":3, "palette": ['FFFF00', '00FF00', 'FF0000']}

// random number generator
function getRandomArbitrary(min, max) {
    return Math.floor(Math.random() * (max - min) + min)
}
var ip_id = getRandomArbitrary(0, 10000)
print("Random Number: ", ip_id)

// display image patch (IP)
var img = ee.Image(cs12_high.toList(1, ip_id).get(0)) // Label
var borders = ee.FeatureCollection(ee.Feature(img.geometry(), border_style))
                .style({styleProperty: "style"}) // borders
var S2img = ee.Image(
  ee.String("COPERNICUS/S2/").cat(img.get("s2_id_gee")).getInfo()
)

// display properties
print(img.toDictionary())


Map.centerObject(img)
Map.addLayer(S2img, s2id, "Sentinel-2 L1C")
Map.addLayer(borders)
Map.addLayer(
  img.updateMask(img.neq(0)), gt,"cloudSEN12 human photointerpretation", true, 0.5
)