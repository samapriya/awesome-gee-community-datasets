# Cyanobacteria Aggregated Manual Labels (CAML)

Continuous monitoring for cyanobacteria blooms in small, inland water bodies via in-situ sampling and analysis can be challenging not only due to the number and locations of
water bodies to cover, but also due to the dynamic nature of algal growth and toxin production. Detection targets vary with cyanobacteria strains as well as physical, chemical,
and biological factors. Ground monitoring also lacks consistency as sampling methods, frequency, and analytical techniques vary from region to region. However, remote sensing
allows systematic data collection over a large area to identify regions with potential harmful algal growth. We introduce the Cyanobacteria Aggregated Manual Labels (CAML), a
large dataset of in-situ cyanobacteria measurements for investigations of cyanobacteria detection and severity classification in inland water bodies across the United States.
Relevant satellite imagery from publicly available endpoints are applicable to use when applying the CAML dataset to models. 

The dataset labels ground measurements of cyanobacteria cell counts at 23,570 points in U.S. inland water bodies over 2013 - 2021. Algorithms trained on this data could be used to estimate cyanobacteria cell counts in water bodies for timely water quality and public health interventions and to gain an understanding of environmental and anthropogenic factors associated with cyanobacteria
incidence and proliferation. Data is provided in a comma-separated values (CSV) format. You can find the dataset [here](https://seabass.gsfc.nasa.gov/archive/NASA_HEADQUARTERS/SGupta/CAML/CAML_2013_2021)

Severity levels are based on World Health Organization (WHO) cyanobacteria density thresholds.

* Low: 0 - 20,000 cells/ml
* Moderate: 20,000 - 100,000 cells/ml
* High: > 100,000 cells/ml

However users should feel free to to use their own thresholds as makes sense for their needs.

![caml_field_data](https://github.com/user-attachments/assets/246b6359-e89c-4c16-ad3c-952267d061a8)

#### Dataset Citation

```
CAML Data (2013-2021). Investigators: Emily Gelbart (NASA), Ritwik Gupta (UC Berkeley), Katie Wetstone (DrivenData), Emily Dorne (DrivenData), Shobhana Gupta (NASA, ASRC
Federal). Retrieved from https://seabass.gsfc.nasa.gov/archive/NASA_HEADQUARTERS/SGupta/CAML/CAML_2013_2021
```

#### Earth Engine Snippet

```js
var caml = ee.FeatureCollection("projects/sat-io/open-datasets/HAB-DETECTION/CAML_cyanobacteria_abundance_20211229_R1");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:hydrology/CYANOBACTERIA-AGG-MANUAL-LABELS

#### License
Following the [NASA Earth Science Data and Information Policy](http://science.nasa.gov/earth-science/earth-science-data/data-information-policy/), all SeaBASS data are publicly available.

Provided by: NASA, UC Berkeley,DrivenData, ASRC Federal

Curated in GEE by: Samapriya Roy

Keywords: water quality, HAB, Cyanobacteria, Manual Labels, Ground data

Last updated: 2024-03-20
