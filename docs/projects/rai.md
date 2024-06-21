# Rural Access Index (RAI)

The Rural Access Index (RAI) is one of the most important global development indicators in the transport sector. It is currently the only indicator for the SDGs that directly measures rural accessibility, and it does so by assessing rural populations’ access to all-season roads. Following its adoption as Sustainable Development Goal (SDG) indicator 9.1.1 in 2015, the indicator received a new methodology taking advantage of geospatial techniques, published under the “Measuring rural access using new technologies” report in 2016 ([World Bank, 2016](https://www.frontiersin.org/articles/10.3389/frsen.2024.1375476/full#B19)). The World Bank has since endorsed an additional Research for Community Access Partnership (ReCAP) funded project led by the Transport Research Laboratory (TRL)—the RAI Supplemental Guidelines ([Workman and McPherson, 2019](https://www.frontiersin.org/articles/10.3389/frsen.2024.1375476/full#B15))—which provided detailed guidance for calculating the RAI, notably with an alternative approach to the all-season aspect of RAI, focusing on the changing accessibility profile of road networks rather than relying on road surface quality alone or scarce physical measurements for road conditions. Nevertheless, neither the 2016 nor the 2019 methodologies were implemented globally, with official implementations published by the World Bank being restricted to more in-depth studies for selected countries mostly in Africa and the Middle East ([World Bank, 2023a](https://www.frontiersin.org/articles/10.3389/frsen.2024.1375476/full#B17)) due to data source restrictions.

![image](https://github.com/samapriya/awesome-gee-community-datasets/assets/27212852/0bddad19-137b-4278-a012-5eb0cce5d35f)

Here the [SDG Transformation Center](https://sdgtransformationcenter.org/geospatial), part of the UN Sustainable Development Solutions Network (UN SDSN), seeks to fill in this gap by implementing the most up-to-date methodology endorsed by the World Bank’s ([World Bank’s 2016](https://www.frontiersin.org/articles/10.3389/frsen.2024.1375476/full#B19) methodology supplemented by TRL’s 2019 guidelines) at global scale with free remotely sensed datasets with global coverage. This dataset was produced by UN SDSN’s SDG Transformation Center and is, to date, the only publicly available application of this particular method at a global scale.

![image](https://github.com/samapriya/awesome-gee-community-datasets/assets/27212852/1184bdee-87d5-464a-92da-12768f35b4a9)


The complete methodology is available [here](https://www.frontiersin.org/articles/10.3389/frsen.2024.1375476/full#h1)

#### Citation

```
Iablonovski G, Drumm E, Fuller G and Lafortune G (2024) A global implementation of the rural access index.
Front. Remote Sens. 5:1375476. doi: 10.3389/frsen.2024.1375476
```

![rai](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/6041917f-98dc-43d3-9e82-a48fbf7cc6b2)

#### Earth Engine Snippet

```js
//Use the inaccessibility index to multiply your gridded rural population dataset to obtain the
//distribution of rural population with access to all-season roads
var inaccessibilityindex = ee.Image('projects/sat-io/open-datasets/RAI/raimultiplier');
Map.addLayer(inaccessibilityindex,{min:0, max:1, 'palette': ['EFC2B3','ECB176','E9BD3A','E6E600','63C600','00A600']}, 'Inaccessibility index');

//In order to get the Rural Access Index for any given set of boundaries, get zonal statistics
//for the total rural population and the rural population with access to all-season roads

var ruralpopulation = ee.Image('projects/sat-io/open-datasets/RAI/ruralpop');
Map.addLayer(ruralpopulation, {min:0, max:100,'palette': ['FFFFFF', 'ff0000']},'Rural Population');

var ruralpopulationwithaccess = ee.Image('projects/sat-io/open-datasets/RAI/ruralpopaccess');
Map.addLayer(ruralpopulationwithaccess,{min:0, max:100,'palette': ['00A600','63C600','E6E600','E9BD3A','ECB176','EFC2B3']},'Rural Pop w/ Access');

```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:population-socioeconomics/RURAL-ACCESS-INDEX

#### License

Creative Commons Attribution Noncommercial Share Alike license ([CC BY-NC-SA-4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode))
Most of our work is available in open source. Copyrights and licensing conditions for commercial reuse may vary across reports and studies. Should you have any questions on licensing and reuse of our work please reach out to: [privacy@unsdsn.org](mailto:privacy@unsdsn.org) .

Provided by: United Nations Sustainable Development Solutions Network

Curated in GEE by: UNSDSN and Samapriya Roy

Keywords: sdg, accessibility, rural

Last updated: 2024-06-15
