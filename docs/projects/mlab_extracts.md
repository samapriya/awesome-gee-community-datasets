# Measurement Lab Network Extracts (M-Lab)

Measurement Lab (M-Lab) is the largest open source Internet measurement effort in the world. The M-Lab Network Diagnostic Tool (NDT) dataset is a valuable resource for researchers and network engineers interested in understanding internet performance. It consists of a massive collection of test results gathered from users running the NDT tool. These tests measure various aspects of a user's internet connection, including download and upload bandwidth, latency (signal delay), and packet loss.

**This is a very small sample extract for 15,000 download and upload extracts from a single days worth of extract 2024-06-01**

The unique aspect of the NDT dataset lies in its user-initiated nature. Unlike traditional network monitoring conducted by service providers, the NDT data reflects real-world user experiences. Users often run the NDT tool when they encounter internet issues, resulting in a surge of tests during network outages or periods of poor performance. This makes the NDT dataset a rich source for analyzing trends in internet health, identifying bottlenecks, and understanding how network problems manifest for end-users. By studying the characteristics of NDT tests, researchers can gain valuable insights into the overall quality and performance of the internet.

#### Citation

```
Measurement Lab. "The M-Lab NDT Data Set." (February 11, 2009 -- December 21, 2015).
Accessed July 2, 2024. https://measurementlab.net/tests/ndt.
```

![mlab_extracts](https://github.com/user-attachments/assets/217c8016-0766-458f-8f4a-3bc1cdce91bf)

#### License

```
var mlab_download_extract = ee.FeatureCollection("projects/sat-io/open-datasets/network/MLAB/mlab_download_extract");
var mlab_upload_extract = ee.FeatureCollection("projects/sat-io/open-datasets/network/MLAB/mlab_upload_extract");
```

Sample Code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:global-utilities-assets-amenities/MLAB-EXTRACTS-NETWORK-SPEED

#### License
All data collected by M-Lab tests are available to the public without restriction under a No Rights Reserved [Creative Commons Zero](https://creativecommons.org/public-domain/cc0/) Waiver.

Dataset accessed: 2024-07-01

Dataset provided by: Measurement Lab (M-Lab)

Curated in GEE by: Samapriya Roy

Keywords: : analytics,network speed,cities,civic,infrastructure,internet,network traffic, telecommunications,isp

Last updated: 2024-07-02
