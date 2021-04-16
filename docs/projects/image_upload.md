# Image Upload

The script creates an Image Collection from GeoTIFFs in your local directory. By default, the image name in the collection is the same as the local directory name. The upload tool now allows the user to copy cookie list from your browser and bypass selenium based authentication. It saves the cookie temporarily and uses it automatically till it expires when it asks you for cookie list again. Just use the ```--method cookies``` argument.


```
usage: geeup upload [-h] --source SOURCE --dest DEST -m METADATA
                    [--nodata NODATA] [-u USER] [--method METHOD]

optional arguments:
  -h, --help            show this help message and exit

Required named arguments.:
  --source SOURCE       Path to the directory with images for upload.
  --dest DEST           Destination. Full path for upload to Google Earth
                        Engine, e.g. users/pinkiepie/myponycollection
  -m METADATA, --metadata METADATA
                        Path to CSV with metadata.
  -u USER, --user USER  Google account name (gmail address).
  --method METHOD       Choose method <cookies> to use cookies to authenticate

Optional named arguments:
  --nodata NODATA       The value to burn into the raster as NoData (missing
                        data)
```

Example setup would be

![geeup_upimg](https://user-images.githubusercontent.com/6677629/114294175-5e083200-9a62-11eb-8801-dabd6218a21e.gif)

If you are using cookies for image upload setup would be

```
geeup upload --source "full path to folder with GeoTIFFs" --dest "Full path for upload to Google Earth Engine, e.g. users/pinkiepie/myponycollection" --metadata "Full path for metadata file.csv" --user "email@domain.com authenticated and used with GEE" --method "cookies"  
```
Example setup with cookies would be

![geeup_upimg_cookies](https://user-images.githubusercontent.com/6677629/114294176-62cce600-9a62-11eb-8d38-f786fbdbe4f3.gif)
