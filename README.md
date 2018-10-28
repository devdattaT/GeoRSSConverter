# Read GeoRSS Data

This is a simple Script to convert GeoRSS formated Data to GeoJSON

Right now it supports Points, Lines & Polygons, encoded in the [Simple Geometry](www.georss.org/simple.html) format.

## How to Run

This can be run on the command line, by passing 3 parameters:

- First Parameter is the input GeoRSS file (Required)
- Second Parameter is the output GeoJSON file (Required)
- Third Parameter is to indicate whether the script should write the default attributes of `link`, `title`, & `guid`. This can be indicated by passing in `true` or `t` (Optional)

Example: `python convertGeoRSS.py canals.xml can.geojson`

---

## Note

According to the [Simple GeoRSS Specs](http://www.georss.org/simple.html), only simple Lines & Polygons are supported. Multiline & MultiPolygons do not seem to be supported by the Spec

---

## License

Copyright 2018 devdatta@tengshe.in

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
