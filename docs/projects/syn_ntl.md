# GAN based Synthetic VIIRS (NTL) India

This study utilizes nighttime light (NTL) data from two primary sources: the Defense Meteorological Satellite Program (DMSP) and the Visible and Infrared Imaging Suite (VIIRS) onboard the Suomi National Polar Partnership (SNPP) satellite.  DMSP-OLS data provide monthly NTL observations from April 1992 to December 2013 at a 30-arc second spatial resolution, while VIIRS-DNB data offer monthly observations from April 2012 onwards at a finer 15-arc second resolution. Both datasets have been extensively used in research to monitor human activities and natural phenomena, but their different resolutions and temporal coverage present challenges for long-term analysis.

To address these limitations, this study uses preprocessed DMSP data to generate synthetic VIIRS-like imagery for the period 1992-2013. The model was trained using overlapping monthly NTL data for the years 2012 and 2013, and the generated imagery was validated against other VIIRS-like datasets and socio-economic indicators such as GDP and population.

The original DMSP monthly product (from which the current product is derived) have been captured by a series of satellites (F10-F18 ), and have been [made available by EOG](https://eogdata.mines.edu/products/dmsp/#monthly) between 1992 and 2014. The different colours in the image below show its availability over Indian landmass; [image source](https://doi.org/10.1080/01431161.2022.2152758)). The green ticks show the 216 monthly images that were used [in our paper](https://doi.org/10.1016/j.rsase.2024.101263), for the generation of the improved VIIRS-like product. The red crosses display the files that are available on EOG, however, due to clouds over the Indian region, the products had large spatial gaps, and could not be used for creation of this improved product. The blue cells indicate months for which data was absent on the EOG portal, at the time of creation of this improved product.

![image](https://github.com/samapriya/awesome-gee-community-datasets/assets/7839690/600d7d68-e779-42e2-8882-0546ff81e8a4)

Hence there are can be multiple cases where:

1. 12 months data is not available for an year, because either (a) the data was not available (from original source), e.g., F12_1994; or (b) the data was not available over India (from original source), e.g., F12_1995.
2. More than 12 months data is available for an year, because (a) the data was captured by multiple satellites for 1 or more months (e.g., [1999 from F12 and F14](https://code.earthengine.google.com/7d4180e61efe3b7e15c08b3e57adf39b)).
3. Exactly 12 months data is available for an year, but it is not for all months, because it is a combination of months from different satellites for the given year (e.g., [1994 from F10 and F12](https://code.earthengine.google.com/42428bd2274487b17e66e40a2e998e87)).

**The data is not temporally continuous. Users are advised to use the monthly data appropriately.**

#### Output Data Characteristics

The study generates a monthly time series of VIIRS-like nighttime light images for India, spanning the period from April 1992 to December 2013. The images have the following characteristics:

* **Spatial Resolution**: 15-arc seconds
* **Temporal Resolution**: Monthly
* **Data Range**: Radiance units of Watts cm−2sr−1

#### Citation

```
Jindal, M., Gupta, P. K., & Srivastav, S. K. (2024). Generation of monthly VIIRS nighttime lights time-series (1992–2013) images using
deep learning (cGAN) technique. Remote Sensing Applications: Society and Environment, 35, 101263. https://doi.org/10.1016/j.rsase.2024.101263
```

![ntl](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/5f75c2c0-070e-497f-b215-d36a3229b8f5)

#### Earth Engine Snippet

```js
var syn_ntl_india = ee.ImageCollection("projects/sat-io/open-datasets/gan-synthetic-viirs");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/SYNTHETIC-NTL-VIIRS-INDIA

#### License
Creative Commons Attribution 4.0 International

Provided by: Jindal et al

Curated in GEE by: Samapriya Roy

Keywords: VIIRS-DNB, Noise removal, DMSP-OLS, Monthly, Inter-calibration, Conditional GAN
