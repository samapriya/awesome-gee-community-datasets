# GLC_FCS30D Global 30-meter Land Cover Change Dataset (1985-2022)

???+ note

    **This dataset is part of a paper in submission and as such does not have citation and DOI information. This will be updated as the paper progresses through review and publication cycles.Please keep this into consideration while using this dataset**

The GLC_FCS30D dataset represents a pioneering advancement in global land-cover monitoring, offering comprehensive insights into land cover dynamics at a 30-meter resolution spanning the period from 1985 to 2022. Developed using continuous change detection methods and leveraging the extensive Landsat imagery archives within the Google Earth Engine platform, GLC_FCS30D comprises 35 land-cover subcategories with 26 time steps, updated every five years prior to 2000 and annually thereafter. Through a rigorous refinement process, including spatiotemporal classification and temporal-consistency optimization, the dataset achieves high-confidence accuracy, validated with over 84,000 global samples and achieving an overall accuracy of 80.88%. Notably, GLC_FCS30D elucidates significant trends, revealing forest and cropland variations as dominant drivers of global land cover change over the past 37 years, with a net loss of approximately 2.5 million km² of forests and a net gain of around 1.3 million km² in cropland area. With its diverse classification system, high spatial resolution, and extensive temporal coverage, GLC_FCS30D serves as a valuable resource for climate change research and sustainable development analysis. Access the [dataset here](https://doi.org/10.5281/zenodo.8239305).

??? example "Expand to show Land Cover classes, RGB values and hex codes"

    <center>

    <table width="500" border="1">
        <tr>
            <th>LC Id</th>
            <th>Classification System</th>
            <th>RGB value</th>
            <th>Color</th>
        </tr>
        <tr>
            <td>10</td>
            <td>Rainfed cropland</td>
            <td>(255,255,100)</td>
            <td bgcolor="#ffff64"></td>
        </tr>
        <tr>
            <td>11</td>
            <td>Herbaceous cover cropland</td>
            <td>(255,255,100)</td>
            <td bgcolor="#ffff64"></td>
        </tr>
        <tr>
            <td>12</td>
            <td>Tree or shrub cover (Orchard) cropland</td>
            <td>(255,255,0)</td>
            <td bgcolor="#ffff00"></td>
        </tr>
        <tr>
            <td>20</td>
            <td>Irrigated cropland</td>
            <td>(170,240,240)</td>
            <td bgcolor="#aaf0f0"></td>
        </tr>
        <tr>
            <td>51</td>
            <td>Open evergreen broadleaved forest</td>
            <td>(76,115,0)</td>
            <td bgcolor="#4c7300"></td>
        </tr>
        <tr>
            <td>52</td>
            <td>Closed evergreen broadleaved forest</td>
            <td>(0,100,0)</td>
            <td bgcolor="#006400"></td>
        </tr>
        <tr>
            <td>61</td>
            <td>Open deciduous broadleaved forest (0.15&lt;fc&lt;0.4)</td>
            <td>(170,200,0)</td>
            <td bgcolor="#a8c800"></td>
        </tr>
        <tr>
            <td>62</td>
            <td>Closed deciduous broadleaved forest (fc&gt;0.4)</td>
            <td>(0,160,0)</td>
            <td bgcolor="#00a000"></td>
        </tr>
        <tr>
            <td>71</td>
            <td>Open evergreen needle-leaved forest (0.15&lt; fc &lt;0.4)</td>
            <td>(0,80,0)</td>
            <td bgcolor="#005000"></td>
        </tr>
        <tr>
            <td>72</td>
            <td>Closed evergreen needle-leaved forest (fc &gt;0.4)</td>
            <td>(0,60,0)</td>
            <td bgcolor="#003c00"></td>
        </tr>
        <tr>
            <td>81</td>
            <td>Open deciduous needle-leaved forest (0.15&lt; fc &lt;0.4)</td>
            <td>(40,100,0)</td>
            <td bgcolor="#286400"></td>
        </tr>
        <tr>
            <td>82</td>
            <td>Closed deciduous needle-leaved forest (fc &gt;0.4)</td>
            <td>(40,80,0)</td>
            <td bgcolor="#285000"></td>
        </tr>
        <tr>
            <td>91</td>
            <td>Open mixed leaf forest (broadleaved and needle-leaved)</td>
            <td>(160,180,50)</td>
            <td bgcolor="#a0b432"></td>
        </tr>
        <tr>
            <td>92</td>
            <td>Closed mixed leaf forest (broadleaved and needle-leaved)</td>
            <td>(120,130,0)</td>
            <td bgcolor="#788200"></td>
        </tr>
        <tr>
            <td>120</td>
            <td>Shrubland</td>
            <td>(150,100,0)</td>
            <td bgcolor="#966400"></td>
        </tr>
        <tr>
            <td>121</td>
            <td>Evergreen shrubland</td>
            <td>(150,75,0)</td>
            <td bgcolor="#964b00"></td>
        </tr>
        <tr>
            <td>122</td>
            <td>Deciduous shrubland</td>
            <td>(150,100,0)</td>
            <td bgcolor="#966400"></td>
        </tr>
        <tr>
            <td>130</td>
            <td>Grassland</td>
            <td>(255,180,50)</td>
            <td bgcolor="#ffb432"></td>
        </tr>
        <tr>
            <td>140</td>
            <td>Lichens and mosses</td>
            <td>(255,220,210)</td>
            <td bgcolor="#ffdcd2"></td>
        </tr>
        <tr>
            <td>150</td>
            <td>Sparse vegetation (fc&lt;0.15)</td>
            <td>(255,235,175)</td>
            <td bgcolor="#ffebaf"></td>
        </tr>
        <tr>
            <td>152</td>
            <td>Sparse shrubland (fc&lt;0.15)</td>
            <td>(255,210,120)</td>
            <td bgcolor="#ffd278"></td>
        </tr>
        <tr>
            <td>153</td>
            <td>Sparse herbaceous (fc&lt;0.15)</td>
            <td>(255,235,175)</td>
            <td bgcolor="#ffebaf"></td>
        </tr>
        <tr>
            <td>181</td>
            <td>Swamp</td>
            <td>(0,168,132)</td>
            <td bgcolor="#00a884"></td>
        </tr>
        <tr>
            <td>182</td>
            <td>Marsh</td>
            <td>(115,255,223)</td>
            <td bgcolor="#73ffdf"></td>
        </tr>
        <tr>
            <td>183</td>
            <td>Flooded flat</td>
            <td>(158,187,215)</td>
            <td bgcolor="#9ebb3b"></td>
        </tr>
        <tr>
            <td>184</td>
            <td>Saline</td>
            <td>(130,130,130)</td>
            <td bgcolor="#828282"></td>
        </tr>
        <tr>
            <td>185</td>
            <td>Mangrove</td>
            <td>(245,122,182)</td>
            <td bgcolor="#f57ab6"></td>
        </tr>
        <tr>
            <td>186</td>
            <td>Salt marsh</td>
            <td>(102,205,171)</td>
            <td bgcolor="#66cdab"></td>
        </tr>
        <tr>
            <td>187</td>
            <td>Tidal flat</td>
            <td>(68,79,137)</td>
            <td bgcolor="#444f89"></td>
        </tr>
        <tr>
            <td>190</td>
            <td>Impervious surfaces</td>
            <td>(195,20,0)</td>
            <td bgcolor="#c31400"></td>
        </tr>
        <tr>
            <td>200</td>
            <td>Bare areas</td>
            <td>(255,245,215)</td>
            <td bgcolor="#fff5d7"></td>
        </tr>
        <tr>
            <td>201</td>
            <td>Consolidated bare areas</td>
            <td>(220,220,220)</td>
            <td bgcolor="#dcdcdc"></td>
        </tr>
        <tr>
            <td>202</td>
            <td>Unconsolidated bare areas</td>
            <td>(255,245,215)</td>
            <td bgcolor="#fff5d7"></td>
        </tr>
        <tr>
            <td>210</td>
            <td>Water body</td>
            <td>(0,70,200)</td>
            <td bgcolor="#0046c8"></td>
        </tr>
        <tr>
            <td>220</td>
            <td>Permanent ice and snow</td>
            <td>(255,255,255)</td>
            <td bgcolor="#ffffff"></td>
        </tr>
        <tr>
            <td>0, 250</td>
            <td>Filled value</td>
            <td>(255,255,255)</td>
            <td bgcolor="#ffffff"></td>
        </tr>
    </table>

    <center>

#### Dataset postprocessing

The datasets consist of about 961 tiles with the annual layers consisting of about 23 years worth of imagery with each band representing a year from 2000 and the 5 year ones start from 1985 with 3 band representing a gap of 5 year so 1985-1990 is b1, 1990-1995 is b2 and 1990-2000 is b3.

#### Citation

```
Zhang, X., Zhao, T., Xu, H., Liu, W., Wang, J., Chen, X., and Liu, L.: GLC_FCS30D: The first global 30-m land-cover dynamic monitoring product with
a fine classification system from 1985 to 2022 using dense time-series Landsat imagery and continuous change-detection method, Earth Syst. Sci. Data
Discuss. [preprint], https://doi.org/10.5194/essd-2023-320, in review, 2023.
```

#### Dataset Citation

```
Liangyun Liu, Xiao Zhang, & Tingting Zhao. (2023). GLC_FCS30D: the first global 30-m land-cover dynamic monitoring product with fine classification
system from 1985 to 2022 [Data set]. Zenodo. https://doi.org/10.5281/zenodo.8239305
```

![glc_fcs30_multiyear_small](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/6499819b-93e2-47aa-92b7-73f9ebaa4b6f)

#### Earth Engine Snippet

```js
var annual = ee.ImageCollection("projects/sat-io/open-datasets/GLC-FCS30D/annual");
var five_year = ee.ImageCollection("projects/sat-io/open-datasets/GLC-FCS30D/five-years-map");
```

Sample code:  https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-landuse-landcover/GLC-FCS30D

#### License
This work is licensed under and freely available to the public under Creative Commons Attribution 4.0 International license.

Created by: Zhang et al. 2023

Curated in GEE by : Samapriya Roy

Keywords: GLC_FCS30D, 1985-2022, Land-cover change, Landsat, change detection, Google Earth Engine

Last updated in GEE: 2024-02-20
