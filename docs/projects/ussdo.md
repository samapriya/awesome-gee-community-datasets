# United States Seasonal Drought Outlook

The United States Drought Outlook raster dataset is produced by the National Weather Service Climate Prediction Center. It is released on the last day of each month and provides information on the drought outlook for the following month. The "US Seasonal Drought Outlook" dataset is released on a monthly basis, specifically on the third Thursday of each month. This dataset provides a qualitative assessment of the likelihood of drought conditions across different regions of the United States. The assessment is conducted using a four-category scale to characterize the anticipated drought conditions:

1. **Normal:** Drought conditions are not expected, indicating a situation of normalcy regarding water availability.
2. **Abnormally dry:** This category suggests that drought conditions are possible but not yet widespread, signifying a degree of caution.
3. **Moderately dry:** Drought conditions in this category are likely and have the potential to cause some economic or environmental impacts.
4. **Severely dry:** This category indicates a high likelihood of drought conditions, which could result in significant economic or environmental consequences.

You can find [additional information here](https://www.cpc.ncep.noaa.gov/products/expert_assessment/sdo_summary.php) and on the [climate engine org website](https://support.climateengine.org/article/90-us-drought). You can download the [datesets here](https://ftp.cpc.ncep.noaa.gov/GIS/droughtlook/)

**Categorical Values**

| Value    | Interpretation         |
|----------|------------------------|
| -9999    | NoData Value           |
| 0        | No drought            |
| 1        | Drought removal likely |
| 2        | Drought remains but improves |
| 3        | Drought development likely |
| 4        | Drought persists       |

**Spatial Information**

| Parameter            | Value                 |
|----------------------|-----------------------|
| Spatial extent       | United States         |
| Spatial resolution   | 500 m (1/48-deg)      |
| Temporal resolution  | Monthly               |
| Time span            | 2013-08-01 to present |
| Update frequency     | Updated last day of each month |

**Variables**

| Variable                | Details                          |
|-------------------------|----------------------------------|
| Drought category ('drought_outlook_class') | - Units: Drought outlook classification |
|                         | - Scale factor: 1.0                |

![ussdo](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/cd354bfc-6e79-4ebe-a887-b068f1483b1e)

#### Earth Engine Snippet

```js
// Read in Image Collection and get single image
var usdo_ic = ee.ImageCollection('projects/climate-engine-pro/assets/ce-cpc-usdo-monthly')
var usdo_i = usdo_ic.first()

// Print image to see bands
print(usdo_i)

// Visualize a single image

var usdo_palette = ["#ffffff", "#ABA362", "#DACBB5", "#FFD861", "#935743"]
Map.addLayer(usdo_i, {min:0, max:4, palette: usdo_palette}, 'usdo_i')
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:weather-climate/weather-climate/US-DROUGHT-OUTLOOK

#### License
NOAA data, information, and products, regardless of the method of delivery, are not subject to copyright and carry no restrictions on their
subsequent use by the public. Once obtained, they may be put to any lawful use. The forgoing data is in the public domain and is being provided
without restriction on use and distribution. For more information visit the NWS disclaimer site.

Keywords: drought, United Stated, outlook, forecast, NOAA, NWS, CPC, monthly

Provided by: NOAA

Curated in GEE by: Climate Engine Org
