import xml.etree.ElementTree as ET
import sys
import json


def readXMLFile(xmlFile):
    # create element tree object
    tree = ET.parse(xmlFile)

    # get root element
    root = tree.getroot()

    features = []
    for item in root.findall('./channel/item'):
        feature = {}
        # iterate child elements of item
        for child in item:
            feature[child.tag] = child.text
        # Add this to the array
        features.append(feature)

    # return the features
    return features


def getAttributes(a):
    # remove new lines if any
    xml = a.replace('\n', '')
    # This is a workaround, because there is no root element
    newXML = "<root>" + xml + "</root>"

    # sometimes an & sneaks in
    newXML = newXML.replace(' & ', ' &amp; ')

    props = {}
    # read the root
    tree = ET.fromstring(newXML)
    # read all the uls in this string
    for item in tree.findall('ul'):
        # Get all the attributes as children of this ul
        for child in item:
            # This is one property
            ob = {}  # temp object to store attribute name & value
            for sp in child.iter('span'):
                at_cls = sp.get('class')
                # set it on the temp object
                ob[at_cls] = sp.text
            # Set the data of this property on the props object
            key = ob['atr-name']
            val = ob['atr-value']
            props[key] = val

    return props


def getGeoJSON(geomStr, type):
    coords = geomStr.split(' ')  # split at the space

    if(type == 'point'):
        op = {
            "type": "Point",
            "coordinates": [
                float(coords[1]), float(coords[0])
            ]
        }
        return op
    if(type == 'line'):
        cs = []
        for i in xrange(0, len(coords), 2):
            x = coords[i+1]
            y = coords[i]
            cs.append([float(x), float(y)])
        op = {"type": "LineString",
              "coordinates": cs}
        return op
    if(type == 'polygon'):
        cs = []
        for i in xrange(0, len(coords), 2):
            x = coords[i+1]
            y = coords[i]
            cs.append([float(x), float(y)])
        op = {"type": "Polygon",
              "coordinates": [cs]}
        return op
    # unexpected Geometry type
    raise Exception(
        "Geometry Type not one of point, line or polygon. Cannot Proceed further")


def getGeometry(item):
    # the geometry is in the tag starting with georss
    # it could be point, line or polygon
    for k in item.keys():
        if(k.startswith(GEORSS_NAMESPACE)):
                # This is our Geometry tag
            geom = item[k]
            # The type is the part after the Namespace
            geomType = k[len(GEORSS_NAMESPACE):]
            # Get the geometry in GeoJSON format
            g = getGeoJSON(geom, geomType)
            return g
    # else
    return {}


GEORSS_NAMESPACE = '{http://www.georss.org/georss}'
addDefaultFields = False

args = sys.argv[1:]

try:
    input_file = args[0]  # first element is path of input file
except IndexError:
    input_file = 'input.xml'

try:
    output_file = args[1]  # Second element is path of output file
except IndexError:
    output_file = 'op.geojson'

try:
    # Third element indicated whether to write default fields
    valueSet = args[2]
    valueSet = valueSet.lower()
    if(valueSet in['t', 'true']):
        addDefaultFields = True
except IndexError:
    # do nothing
    pass


# read Input Data
xmlData = readXMLFile(input_file)


print "Read {0} elemnts in the input XML".format(len(xmlData))

features = []
# Parse this according to the GeoRSS format
for i in xmlData:
    f = {"type": "Feature"}

    # the actual attributes are in the description tag
    attribs = i['description']
    attributes = getAttributes(attribs)
    f['geometry'] = getGeometry(i)

    # default fields:
    if(addDefaultFields):
        attributes['link'] = i['link']
        attributes['title'] = i['title']
        attributes['guid'] = i['guid']

    f["properties"] = attributes

    # add it to the array
    features.append(f)

print"Parsed {0} elements as RSS features".format(len(features))

print "Writing data to {0}".format(output_file)

# Write this data
featColl = {"type": "FeatureCollection", "features": features}
with open(output_file, 'w') as of:
    json.dump(featColl, of)
