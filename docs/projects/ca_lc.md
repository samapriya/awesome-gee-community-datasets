# High-resolution annual forest land cover maps for Canada's forested ecosystems (1984-2019)

The annual time series of forest land cover maps are national in scope (entire 650 million hectare forested ecosystem) and represent a wall-to-wall land cover characterization yearly from 1984 to 2019. These time-series land cover maps were produced from annual time-series of Landsat image composites, forest change information, and ancillary topographic and hydrologic data following the framework described in Hermosilla et al. (2022), which builds upon the approach introduced in Hermosilla et al. (2018). The methodological innovations included (i) a refined training pool derived from existing land cover products using airborne and spaceborne measures of forest structure; (ii) selection of training samples proportionally to the land cover distribution using a distance=weighted approach; and (iii) generation of regional classification models using a 150x150 km tiling system. Maps are post-processed using disturbance information to ensure logical class transitions over time using a Hidden Markov Model. Hidden Markov Models assess individual year class likelihoods to reduce variability and possible noise in year-on-year class assignments (for instances when class likelihoods are similar).

For an overview on the data, image processing, and time series change detection methods applied, as well as information on independent accuracy assessment of the data, see Hermosilla et al. (2022) No. 112780. DOI: https://doi.org/10.1016/j.rse.2021.112780 and Hermosilla et al. (2018) https://www.tandfonline.com/doi/full/10.1080/07038992.2018.1437719

The data represents annual forest land cover of Canada's forested ecosystems for 1984-2019. An image compositing window of August 1 -30 days was used to generate the best-available-pixel (BAP) image composites used as the source data for land cover classification. The science and methods developed to generate the information outcomes shown here, that track and characterize the history of Canada's forests, were led by Canadian Forest Service of Natural Resources Canada, partnered with the University of British Columbia, with support from the Canadian Space Agency, augmented by processing capacity from WestGrid of Compute Canada.


#### Citation

Paper citation

```
Hermosilla, T., Wulder, M.A., White, J.C., Coops, N.C., 2022. Land cover classification in an era of big and open data: Optimizing localized
implementation and training data selection to improve mapping outcomes. Remote Sensing of Environment. No. 112780.
[Hermosilla et al. 2022](https://www.sciencedirect.com/science/article/pii/S0034425721005009)
```

When using this data, please cite as:

```
Hermosilla, T., Wulder, M.A., White, J.C., Coops, N.C., 2022. Land cover classification in an era of big and open data: Optimizing localized
implementation and training data selection to improve mapping outcomes. Remote Sensing of Environment. No. 112780.
DOI: https://doi.org/10.1016/j.rse.2022.112780 [Open Access]
```

#### Class Schema

<center>

<table width="500" border="1">
	<tr bgcolor="#686868">
		<td>#686868</td>
    <td>Class Code: 0</td>
    <td>Unclassified</td>
	</tr>

	<tr bgcolor="#3333ff">
    <td>#3333ff</td>
    <td>Class Code: 20</td>
		<td>Water</td>
	</tr>

  <tr bgcolor="#ccffff">
    <td>#ccffff</td>
    <td>Class Code: 31</td>
		<td>Snow/Ice</td>
	</tr>

	<tr bgcolor="#cccccc">
    <td>#cccccc</td>
    <td>Class Code: 32</td>
		<td>Rock/Rubble</td>
	</tr>
  <tr bgcolor="#996633">
    <td>#996633</td>
    <td>Class Code: 33</td>
		<td>Exposed/Barren Land</td>
	</tr>

	<tr bgcolor="#ffccff">
    <td>#ffccff</td>
    <td>Class Code: 40</td>
		<td>Bryoids</td>
	</tr>

  <tr bgcolor="#ffff00">
    <td>#ffff00</td>
    <td>Class Code: 50</td>
		<td>Shrubs</td>
	</tr>

	<tr bgcolor="#993399">
    <td>#993399</td>
    <td>Class Code: 80</td>
		<td>Wetland</td>
	</tr>

  <tr bgcolor="#9933cc">
    <td>#9933cc</td>
    <td>Class Code: 81</td>
		<td>Wetland Treed</td>
	</tr>

  <tr bgcolor="#ccff33">
    <td>#ccff33</td>
    <td>Class Code: 100</td>
		<td>Herbs</td>
	</tr>

  <tr bgcolor="#006600">
    <td>#006600</td>
    <td>Class Code: 210</td>
		<td>Coniferous</td>
	</tr>

  <tr bgcolor="#00cc00">
    <td>#00cc00</td>
    <td>Class Code: 220</td>
		<td>Broad Leaf</td>
	</tr>

  <tr bgcolor="#cc9900">
    <td>#cc9900</td>
    <td>Class Code: 230</td>
		<td>Mixedwood</td>
	</tr>


</table>

</center>


![ca_lc_map](https://user-images.githubusercontent.com/6677629/141745218-48410de0-0956-4da9-b90b-05d0c1bd485f.gif)


#### Earth Engine Snippet

```js
var forest_lc = ee.ImageCollection("projects/sat-io/open-datasets/CA_FOREST_LC_VLCE2");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:agriculture-vegetation-forestry/CA-FORESTED-ECOSYSTEM-LC

#### License
This work is licensed under and freely available to the public Open Government Licence - Canada (http://open.canada.ca/en/open-government-licence-canada).

Created by: Hermosilla et al. 2022

Curated in GEE by : Samapriya Roy

keywords: Land cover; Classification; Machine learning; Land cover change; Landsat; Lidar; ICESat-2

Last updated on GEE: 2021-11-14
