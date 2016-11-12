import xml.etree.cElementTree as ET
import pprint
import re
from collections import defaultdict

datadir = ""
datafile = "denhaag_sample.osm"

def audit_zipcode(invalid_zipcodes, good_zipcodes, zipcode):
    """ adds any invalid zipcodes (not in format `ddddd`) to a dict """
    if not re.match(r'^[1-9][0-9]{3}\s*(?:[a-zA-Z]{2})?$', zipcode):
        invalid_zipcodes[zipcode] += 1

    else:
        good_zipcodes[zipcode] += 1

def is_zipcode(elem):
    return (elem.attrib['k'] == "addr:postcode")


def audit(datafile):
    datafile = open(datafile, "r")
    invalid_zipcodes = defaultdict(int)
    good_zipcodes = defaultdict(int)
    counter = 0
    for event, elem in ET.iterparse(datafile, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_zipcode(tag):
                    audit_zipcode(invalid_zipcodes, good_zipcodes, tag.attrib['v'])
        counter += 1

    #return good_zipcodes
    return invalid_zipcodes

zip_types = audit(datafile)
pprint.pprint(zip_types)
