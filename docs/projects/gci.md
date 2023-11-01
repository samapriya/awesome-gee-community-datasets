# Areas of global conservation value

A series of global priority layers are provided from the [NatureMap project](https://iiasa.ac.at/models-tools-data/areas-of-global-conservation-importance-for-biodiversity-carbon-and-water). These maps were created by jointly optimizing biodiversity and NCPs such as carbon and/or water. They describe on a continuous scale the amount of land area with the greatest upper potential value for expanding conservation efforts.

<div class="result" markdown>

???+ note

    **Conservation in this context should be interpreted as not prescriptive (e.g. specifically the establishment of protected areas), but rather means that a certain area harbour great biophysical potential for contributing to the conservation of biodiversity, carbon and water assets.**

</div>

#### Usage notes
The datasets cover roughly the period of 2015 to 2019 and with a spatial resolution of 10 km (50 km versions are available as well on the data repository). The datasets were copied over from the source paths to harmonize path and naming conventions within the community catalog and all dunder characters (double underscores __) were removed with a single underscore. Folder names were also split with a hyphen to separate the words like biodiversity-carbon rather than biodiversitycarbon.

* Maps are supplied at 10km resolution. Maps can either start from a blank state (ignoring existing conservation areas) or build on the global protected area network that was established in 2019.
* Different layers are available for obtaining either priorities for biodiversity only, or for biodiversity and carbon and/or water. A separate distinction is whether maps include stratifications by biome. For more details there please consult Jung et al. (2021).
* The ranks for each layer are area-specific and can be used to extract summary statistics by simple subsetting. For example: To obtain the top 30% of land area for biodiversity and carbon, one needs to create a mask of all areas lower than a value of 30 from the respective ranked layers.


| Filename Suffix       | Description                                                                                                         |
|-----------------------|---------------------------------------------------------------------------------------------------------------------|
| minshort_speciestargets | Problem formulation where targets were achieved by minimizing a shortfall                                         |
| repruns10              | The number of representatives that were used to create the ranked layer                                              |
| biome.id              | Species distribution was split by biome, creating separate targets for subpopulations                             |
| withPA                | Fractions of current protected areas (Date: WDPA 2019) were locked in as a baseline and starting budget. Approximately 15% of the globe. Note that not entire grid cells, but fractions were locked in and built upon! |
| carbon                | Carbon was included in the prioritization and jointly optimized together with the other assets by giving it equal weighting (see manuscript) |
| water                 | Water was included in the prioritization and jointly optimized together with the other assets by giving it equal weighting (see manuscript) |

The layers can be navigated openly through a dedicated Earth engine app ([conservation importance](https://uploads.users.earthengine.app/view/conservationimportance)).Coarser grained versions at 50km are also available [see Zenodo data repository](https://doi.org/10.5281/zenodo.5006332) but not uploaded to Google Earth Engine.

#### Citation

```
- Jung, M., Arnell, A., de Lamo, X. et al. Areas of global importance for conserving terrestrial biodiversity, carbon and water. Nat Ecol Evol 5, 1499–1509 (2021). https://doi.org/10.1038/s41559-021-01528-7

- Jung, M., Arnell, A., De Lamo, X., García-Rangelm, S., Lewis, M., Mark, J., Merow, C., Miles, L., Ondo, I., Pironon, S., Ravilious, C., Rivers, M., Schepashenko, D., Tallowin, O., van Soesbergen, A., Govaerts, R., Boyle, B. L., Enquist, B. J., Feng, X., … Visconti, P. (2021). Areas of global importance for conserving terrestrial biodiversity, carbon, and water (1.0) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.5006332
```

![areas_global_conservation_value_small](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/b990e8f6-4545-427f-84f1-5f52ec5fb329)

### Earth Engine Snippet

```js
// ------------------------ //
// Import the layers
// -- Biodiv --
var biodiv_biome = ee.Image("projects/sat-io/open-datasets/naturemap/biodiversity/minshort_speciestargets_biome_esh10km_repruns10_ranked");
var biodiv_pa_biome = ee.Image("projects/sat-io/open-datasets/naturemap/biodiversity/minshort_speciestargets_biome_withPA_esh10km_repruns10_ranked");
var biodiv = ee.Image("projects/sat-io/open-datasets/naturemap/biodiversity/minshort_speciestargets_esh10km_repruns10_ranked");
var biodiv_pa = ee.Image("projects/sat-io/open-datasets/naturemap/biodiversity/minshort_speciestargetswithPA_esh10km_repruns10_ranked");
// -- Biodiv Carbon--
var biodivcarbon_biome = ee.Image("projects/sat-io/open-datasets/naturemap/biodiversity-carbon/minshort_speciestargets_biome_carbon_esh10km_repruns10_ranked");
var biodivcarbon_pa_biome = ee.Image("projects/sat-io/open-datasets/naturemap/biodiversity-carbon/minshort_speciestargets_biome_withPA_carbon_esh10km_repruns10_ranked");
var biodivcarbon = ee.Image("projects/sat-io/open-datasets/naturemap/biodiversity-carbon/minshort_speciestargets_carbon_esh10km_repruns10_ranked");
var biodivcarbon_pa = ee.Image("projects/sat-io/open-datasets/naturemap/biodiversity-carbon/minshort_speciestargetswithPA_carbon_esh10km_repruns10_ranked");
// -- Biodiv water--
var biodivwater_biome = ee.Image("projects/sat-io/open-datasets/naturemap/biodiversity-water/minshort_speciestargets_biome_water_esh10km_repruns10_ranked");
var biodivwater_pa_biome = ee.Image("projects/sat-io/open-datasets/naturemap/biodiversity-water/minshort_speciestargets_biome_withPA_water_esh10km_repruns10_ranked");
var biodivwater = ee.Image("projects/sat-io/open-datasets/naturemap/biodiversity-water/minshort_speciestargets_water_esh10km_repruns10_ranked");
var biodivwater_pa = ee.Image("projects/sat-io/open-datasets/naturemap/biodiversity-water/minshort_speciestargetswithPA_water_esh10km_repruns10_ranked");
// -- Biodiv carbonwater--
var biodivcarbonwater_biome = ee.Image("projects/sat-io/open-datasets/naturemap/biodiversity-carbon-water/minshort_speciestargets_biome_carbon_water_esh10km_repruns10_ranked");
var biodivcarbonwater_pa_biome = ee.Image("projects/sat-io/open-datasets/naturemap/biodiversity-carbon-water/minshort_speciestargets_biome_withPA_carbon_water_esh10km_repruns10_ranked");
var biodivcarbonwater = ee.Image("projects/sat-io/open-datasets/naturemap/biodiversity-carbon-water/minshort_speciestargets_carbon_water_esh10km_repruns10_ranked");
var biodivcarbonwater_pa = ee.Image("projects/sat-io/open-datasets/naturemap/biodiversity-carbon-water/minshort_speciestargetswithPA_carbon_water_esh10km_repruns10_ranked");
// ------------------------ //

// Define SLD style of discrete intervals to apply to the image.
var default_colours = {min: 1, max: 100, palette: ['7a0403','c92903','f56918','fbb938','c9ef34','74fe5d','1be5b5','35abf8','4662d8','30123b']};

// Default entries
var what = "Biodiversity, carbon and water";

// Visualize
Map.addLayer(biodivcarbon, default_colours, "Biodiversity and Carbon", true);

// The layers are area-consistent, thus through subsetting it becomes possible to identify for example
// the 10% of land-areas with the greatest conservation value for biodiversity

var bio30x30 = biodiv.expression("b(0) <= 10");
Map.addLayer(bio30x30.mask(bio30x30.eq(1)), {'palette':['red']}, "Top 10% value for biodiversity only", false);
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:/biodiversity-ecosystems-habitat/GLOBAL-CONSERVATION-IMP-BIODIV-CARBON-WATER

#### Enter license information

The datasets are provided under a CC-BY-SA 4.0

#### Additional resources
You can explore the dataset layers [using this app](https://uploads.users.earthengine.app/view/conservationimportance)

Keywords: biodiversity, conservation importance, priorities, carbon, water

Provided by: IIASA

Curated in GEE by: IISA, Samapriya Roy

Last updated in GEE: 2023-10-31
