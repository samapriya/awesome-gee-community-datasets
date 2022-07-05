# UrbanWatch 1m Land Cover & Land Use

Very-high-resolution (VHR) land cover and land use (LCLU) is an essential baseline data for understanding fine-scale interactions between humans and the heterogeneous landscapes of urban environments. In this study, we developed a **Fine-resolution, Large-area Urban Thematic information Extraction (FLUTE)** framework to address multiple challenges facing large-area, high-resolution urban mapping, including the view angle effect, high intraclass and low interclass variation, and multiscale land cover types. FLUTE builds upon a teacher-student deep learning architecture and includes two new feature extraction modules – Scale-aware Parsing Module
(SPM) and View-aware Embedding Module (VEM).

Our model was trained with a new benchmark database containing 52.43 million labeled pixels (from 2014 to 2017 NAIP airborne Imagery) to capture diverse LCLU types and spatial patterns. We assessed the credibility of FLUTE by producing a 1-meter resolution database named UrbanWatch for 22 major cities across the conterminous United States. UrbanWatch contains nine LCLU classes – building, road, parking lot, tree canopy, grass/shrub, water, agriculture, barren, and others, with an overall accuracy of 91.52%. You can read the entire paper [UrbanWatch: A 1-meter resolution land cover and land use database for 22 major cities in the United States here](https://www.sciencedirect.com/science/article/abs/pii/S0034425722002206)

Disclaimer: Whole or parts of the dataset description were provided by the author(s) or their works.


#### Citation

```
Zhang, Yindan, Gang Chen, Soe W. Myint, Yuyu Zhou, Geoffrey J. Hay, Jelena Vukomanovic, and Ross K. Meentemeyer. "UrbanWatch: A 1-
meter resolution land cover and land use database for 22 major cities in the United States."
Remote Sensing of Environment 278 (2022): 113106.
```

#### Preprocessing

I added additional metadata to the images, including city names and abbreviations. While the uncompressed size for these datasets is 211 GB as per the paper, the total GEE collection size is only 4.54 GB. The city list is included in the sample code for easy filtering between the 23 cities.

**A nine-class urban classification scheme with diverse geographic patches**

<center>

<table width="500" border="1">
	<tr bgcolor="#FF0000">
    <td>Building</td>
    <td>A human-made structure with a roof (various sizes, shapes, colors, and materials) and walls across commercial, industrial, institutional, and residential areas,such as office buildings, stores, single family houses, townhouses, and condos.</td>
	</tr>

	<tr bgcolor="#858585">
		<td>Road</td>
    <td>A long, narrow stretch with a leveled or paved surface that has specific orientation, length, and width. It differs from building and parking lot with its unique feature of connectivity, such as highway, bridge, sidewalk, driveway, railway, rural pathway, and airport runway.</td>
	</tr>

  <tr bgcolor="#FF00C0">
		<td>Parking Lot</td>
    <td>A cleared area intended for parking vehicles such as an on-the-ground or a surface parking lot. It differs from building and road with its unique feature of vehicle presence and/or surface markings.</td>
	</tr>

	<tr bgcolor="#228B22">
    <td>Tree Canopy</td>
		<td>Individual trees or tree patches representing woody vegetation typically taller than 2 m, such as trees in yards, along streets and utility corridors, and in parks and nature reserves.</td>
	</tr>
  <tr bgcolor="#80EC68">
    <td>Grass/Shrub</td>
		<td>Small-sized perennial woody plants or herbaceous plants with height lower than 2 m, such as bushes, lawns, roadway medians, and grasslands.</td>
	</tr>

	<tr bgcolor="#FFC125">
    <td>Agriculture</td>
		<td>Land for cultivating crops, such as corn, wheat, and soy, as well as fallow plots.</td>
	</tr>

  <tr bgcolor="#0000FF">
    <td>Water</td>
		<td>Areas where water is predominantly present throughout the year, such as rivers, ponds, lakes, oceans, flooded plains, canals, streams, bays, estuaries, and swimming pools.</td>
	</tr>

	<tr bgcolor="#800000">
		<td>Barren</td>
    <td>Areas of rock, sand or soil with very sparse to no vegetation all year round, such as exposed rock or soil, desert, dunes, dry salt flats, dried lake beds, clay, mud, quarries, golf course sand traps, mine lands, and construction site, etc.</td>
	</tr>

  <tr bgcolor="#FFFFFF">
    <td>Others</td>
		<td>All other land cover/use not assigned to the above eight classes, such as outdoor tennis/basketball courts with artificial turf or acrylic surface, transmission towers, and areas covered by disturbed soils/sands without uniformed structures.</td>
	</tr>

</table>

</center>

![urban_watch](https://user-images.githubusercontent.com/6677629/173255159-ef2fbdee-e8b6-4421-b331-4106ee801faf.gif)

#### Earth Engine Snippet

```js
var urban_watch = ee.ImageCollection("projects/sat-io/open-datasets/HRLC/urban-watch-cities");
```

Sample Code: https://code.earthengine.google.com/2661b87b5fb16598cfdb4b1ba510617d


#### License

As per the authors, the urban watch data is freely accessible to support urban-related research, urban planning and management, and community outreach efforts. Therefore, the 1-m maps can be freely used for noncommercial purposes and cited; the assumed license is CC-BY-NC-4.0.

Produced by: Laboratory for Remote Sensing and Environmental Change (LRSEC) at the University of North Carolina

Curated in GEE by: Samapriya Roy

Keywords: Land Use, Land Cover, Urban Watch, Remote Sensing, High Resolution, FLUTE

Last updated on GEE: 2022-06-12
