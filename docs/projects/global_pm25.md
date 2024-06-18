# Global Monthly Satellite-derived PM2.5

Global and regional PM2.5 concentrations are estimated using information from satellite-, simulation- and monitor-based sources. Aerosol optical depth from multiple satellites (MODIS, VIIRS, MISR, and SeaWiFS) and their respective retrievals (Dark Target, Deep Blue, MAIAC) is combined with simulation (GEOS-Chem) based upon their relative uncertainties as determined using ground-based sun photometer (AERONET) observations to produce geophysical estimates that explain most of the variance in ground-based PM2.5 measurements. A subsequent statistical fusion incorporates additional information from PM2.5 measurements.

We estimate annual and monthly ground-level fine particulate matter (PM2.5) for 1998-2022 by combining Aerosol Optical Depth (AOD) retrievals from the NASA MODIS, MISR, SeaWIFS, and VIIRS instruments with the GEOS-Chem chemical transport model, and subsequently calibrating to global ground-based observations using a Geographically Weighted Regression (GWR), as detailed in the below reference for V5.GL.01. V5.GL.04 follows the methodology of V5.GL.01, but updates the ground-based observations used to calibrate the geophysical PM2.5 estimates for the entire time series, extends temporal coverage through 2022, and includes retrievals from the SNPP VIIRS instrument.

#### Citation

```
Aaron van Donkelaar, Melanie S. Hammer, Liam Bindle, Michael Brauer, Jeffery R. Brook, Michael J. Garay, N. Christina Hsu, Olga V. Kalashnikova,
Ralph A. Kahn, Colin Lee, Robert C. Levy, Alexei Lyapustin, Andrew M. Sayer and Randall V. Martin (2021). Monthly Global Estimates of Fine
Particulate Matter and Their Uncertainty Environmental Science & Technology, 2021, doi:10.1021/acs.est.1c05309.
```

 [[Link]](https://pubs.acs.org/doi/abs/10.1021/acs.est.1c05309)

Download link: https://sites.wustl.edu/acag/datasets/surface-pm2-5/#V6.GL.02

### Earth Engine Snippet if dataset already in GEE

for example
```js
var pm25_monthly = ee.ImageCollection("path to your collection")
var pm25_yearly = ee.ImageCollection("path to your collection)
```
Sample Code: Add a sample code maybe just adding your datasets in the code editor


### Enter license information

Freely available as a public good via the Washington UniversityAtmospheric Composition Analysis Group

### Keywords

PM2.5
