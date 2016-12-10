import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

DATADIR = ""
DATAFILE = "denhaag.osm"

expected = ["Den Haag", "Leidschendam", "'s-Gravenzande", "Den Hoorn", "Schipluiden", "Kwintsheul", "De Lier", "Berkel en Rodenrijs", "Delft", "Rijswijk", "Voorburg", "Pijnacker", "Naaldwijk", "Wassenaar", "Zoetermeer", "Voorschoten", "Rotterdam", "Maasdijk","Nootdorp", "Wateringen", "Schipluiden", "s-Gravenzande", "Poeldijk", "Monster", "Honselersdijk"]

#def audit_city(city_name):
 #   for item in city_name:
  #      if item not in expected:
   #         list.append(item)



def is_city_name(elem):
    return (elem.attrib['k'] == "addr:city")

def audit(datafile):
    datafile = open(datafile, "r")
    list = []
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(datafile, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_city_name(tag):
                    if tag.attrib['v'] not in expected:
                        if tag.attrib['v'] not in list:
                            list.append(tag.attrib['v'])

    datafile.close()
    # return street_types
    return list

pprint.pprint(audit(DATAFILE))

