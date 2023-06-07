# Santa Rita Experimental Range Drone Imagery

The technology around drones and image analysis is rapidly advancing which is making high volume workflows easier to implement. Larger quantities of monitoring data will significantly improve our understanding of the impact management actions have on land processes and ecosystem traits. This drone imagery data is used to support a research project investigating the ability to map ecological states across the Santa Rita Experimental Range (SRER) in southern Arizona. The imagery was collected in two campaigns: the first occurred in May 2019 and the second in Aug/Sept 2019. Imagery was collected using a DJI Phantom 4 RTK drone, flying 38 m above the ground and yielding ~1 cm ground sampling distance. The imagery is located at long-term transects and exclosures at SRER. The imagery was to be compared with field mapping of ecological states conducted by Dan Robbinett. The imagery and other data in this repository are connected with the 2021 Ecosphere publication [Innovations to expand drone data collection and analysis for rangeland monitoring, which you can read here](https://esajournals.onlinelibrary.wiley.com/doi/10.1002/ecs2.3649). You can find additional information about the researh site and experiments here [Santa Rita Exprimental Range Website](https://cals.arizona.edu/srer/).


#### Citation

```
Gillan, Jeffrey K., Guillermo E. Ponce‐Campos, Tyson L. Swetnam, Alessandra Gorlier, Philip Heilman, and Mitchel P. McClaran.
"Innovations to expand drone data collection and analysis for rangeland monitoring." Ecosphere 12, no. 7 (2021): e03649.
```

![srer_drone_img](https://github.com/samapriya/awesome-gee-community-datasets/assets/6677629/d4228e9f-3144-4bdd-a74e-77111b011933)

#### Earth Engine data location

```js
var full_ortho_srer_may_2019_1cm = ee.Image("users/gponce/usda_ars/assets/images/aes/srer/suas/2019/full_ortho_srer_may_2019_1cm");
var full_ortho_srer_sept_2019_1cm = ee.Image("users/gponce/usda_ars/assets/images/aes/srer/suas/2019/full_ortho_srer_sept_2019_1cm");
var chm_sept_2019 = ee.Image("users/gponce/usda_ars/assets/images/aes/srer/suas/2019/chm_sept_2019");
var chm_may_2019 = ee.Image("users/gponce/usda_ars/assets/images/aes/srer/suas/2019/chm_may_2019");

// Class mapping ['1', '2', '3', '4'] = ['Herb', 'Woody','Bareground','Shadow']
var class_sep_2019 = ee.Image("users/gponce/usda_ars/assets/images/aes/srer/suas/2019/full_ortho_classified_sep_2019_5cm");
var class_may_2019 = ee.Image("users/gponce/usda_ars/assets/images/aes/srer/suas/2019/full_ortho_classified_may_2019_5cm");
```

Sample code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:analysis-ready-data/SRER-HIGHRES-DRONE

[Data visualization tool in GEE App](https://gponce.users.earthengine.app/view/srer-drone-2019)

App code: https://code.earthengine.google.com/?scriptPath=users/sat-io/awesome-gee-catalog-examples:analysis-ready-data/SRER-APP-CODE

#### License
GNU GENERAL PUBLIC LICENSE

Version 3, 29 June 2007

Curated by: Jeffrey K. Gillan, Guillermo E. Ponce Campos


Keywords: cloud computing, high-performance computing, monitor,real-time kinematic (RTK), unmanned aerial systems

Last updated: 11/21/2019

