# photo-website-v2
A complete redesign and ground up rebuild of my personal photo website I share with friends.

## Info
index_template.html and album_template.html are filled automatically by templating.py, reading a dedicated folder structure.

All tasks including;
* image resizing to definable widths
* ordering of images within the albums
* ordering of albums on the landing page
* album descriptions

are completed by the python script and associated album based yaml files.

## Dependencies
Requires yaml and the python image library (PIL)

## How it works
Run templating.py to generate the resized images and html files.
Run push.sh to sync with the amazon s3 bucket and make the changes live.