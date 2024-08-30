# Global Groundwater-Dependent Ecosystems (GDEs)

Groundwater is the most widespread source of liquid freshwater, yet its critical role in supporting diverse ecosystems often goes unrecognized. The
location and extent of groundwater-dependent ecosystems (GDEs) remain largely unknown in many regions, leading to inadequate protection measures.
This dataset offers a high-resolution (approximately 30m) map of GDEs, revealing their presence on over one-third of the global drylands analyzed,
including key biodiversity hotspots. GDEs are found to be more extensive and contiguous in areas dominated by pastoralism with lower groundwater
depletion rates, indicating that many GDEs have likely already been lost due to unsustainable water and land use practices.

About 53% of the mapped GDEs are located in regions experiencing declining groundwater trends, underscoring the urgent need for protective measures.
Despite their importance, only 21% of GDEs are within protected areas or regions with sustainable groundwater management policies, highlighting a
significant gap in conservation efforts. Additionally, this dataset explores the connection between GDEs and cultural, socio-economic factors in the
Greater Sahel region, emphasizing their role in supporting biodiversity and rural livelihoods. The GDE map is a crucial tool for policymakers,
conservationists, and stakeholders to prioritize and develop strategies for safeguarding these vital ecosystems at local, regional, and
international levels. You can read the [paper here](https://doi.org/10.1038/s41586-024-07702-8) and individual tiles can be [downloaded here](https://zenodo.org/records/11062894).

#### Citation

```
Rohde, M.M., Albano, C.M., Huggins, X. et al. Groundwater-dependent ecosystem map exposes global dryland protection needs.
Nature 632, 101–107 (2024). https://doi.org/10.1038/s41586-024-07702-8
```

#### Dataset Citation

```
Rohde, M. M., Albano, C., Huggins, X., Klausmeyer, K., & Sharman, A. (2024). Data, code, and outputs for: groundwater-dependent ecosystem map
exposes global dryland protection needs [Data set]. Zenodo. https://doi.org/10.5281/zenodo.11062894
```

![global_gde](https://github.com/user-attachments/assets/fc271f7c-4b98-4347-b838-3d0281cee565)

#### Earth Engine Snippet

```js
var imageCollection = ee.ImageCollection("projects/sat-io/open-datasets/GlobalGDEMap_v6_TNC");
print(imageCollection)
```

Sample code:  https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:biodiversity-ecosystems-habitat/GROUNDWATER-DEP-ECOSYSTEMS

Earth Engine App: https://codefornature.projects.earthengine.app/view/global-gde

#### License

This work is licensed under the Creative Commons Attribution 4.0 International License (https://creativecommons.org/licenses/by/4.0). Users are free to use, copy, distribute, transmit, and adapt the work for commercial and non-commercial purposes, without restriction, as long as clear attribution of the source is provided.

Created by: TNC, Rohde, M.M., Albano, C.M., Huggins, X. et al

Curated by: TNC & Samapriya Roy

Keywords: : Global Groundwater-Dependent Ecosystems, GDE Mapping, Conflict Hotspots, Climate Change, Food Security

Last updated: 2024-08-28
