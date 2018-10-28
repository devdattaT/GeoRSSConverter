# Read GeoRSS Data

This is a simple Script to convert GeoRSS formated Data to GeoJSON

Right now it supports only Points & Lines

## How to Run

This can be run on the command line, by passing 3 parameters:

- First Parameter is the input GeoRSS file (Required)
- Second Parameter is the output GeoJSON file (Required)
- Third Parameter is to indicate whether the script should write the default attributes of `link`, `title`, & `guid`. This can be indicated by passing in `true` or `t` (Optional)

Example: `python convertGeoRSS.py canals.xml can.geojson`
