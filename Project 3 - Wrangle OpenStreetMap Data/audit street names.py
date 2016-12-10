import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint

DATADIR = ""
DATAFILE = "denhaag_sample.osm"
#a = ("kade", 'weg', 'straat', 'laan', 'plein', 'singel' 'gracht', 'hof', 'strand', 'weg', 'pad', 'dijk', 'zijde', 'haven', 'gracht', 'duin', 'kant', 'park', 'hout', 'land', 'park', 'wijk', 'waard', 'vaart', 'brug', 'plaats'  )
#for item in a:
   #street_type_re = re.compile(r'(.*a.*)',re.IGNORECASE)
    #continue

street_type_re = re.compile(r'(.*straat.*)|(.*einde.*)|(.*hoek.*)|(.*kamp.*)|(.*bos.*)|(.*molen.*)|(.*tuin.*)|(.*markt.*)|(.*steeg.*)|(.*rade.*)|(.*pad.*)|(.*laan.*)|(.*dreef.*)|(.*weg.*)|(.*plein.*)|(.*singel.*)|(.*gracht.*)|(.*kade.*)|(.*hof.*)|(.*kade.*)|(.*dijk.*)|(.*kade.*)|(.*haven.*)|(.*kade.*)|(.*zijde.*)|(.*duin.*)|(.*kant.*)|(.*land.*)|(.*zicht.*)|(.*park.*)|(.*wijk.*)|(.*wijck.*)|(.*waard.*)|(.*weide.*)|(.*vaart.*)|(.*veld.*)|(.*plaats.*)|(.*hout.*)|(.*zoom.*)|(.*berg.*)|(.*brug.*)|(.*gaarde.*)|(.*soen.*)|(.*strand.*)|(.*baan.*)|(.*horst.*)|(.*burg.*)|(.*daal.*)|(.*erf*)', re.IGNORECASE)


mapping = { "Rossinistraaat": "Rossinistraat",
            }

def audit_street_type(street_types, street_name):
    street_types2 = {}
    m = street_type_re.search(street_name)
    for item in street_name:
        if m:
            street_type = m.group()
            street_types[street_type].add(street_name)

def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(datafile):
    datafile = open(datafile, "r")
    list = []
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(datafile, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
                    if tag.attrib['v'] not in street_types:
                        if tag.attrib['v'] not in list:
                            list.append(tag.attrib['v'])

    datafile.close()
    #return street_types
    #return sorted(list, reverse = False)


def update_name(name, mapping):
    m = street_type_re.search(name)
        if m.group() in mapping.keys():
            if m not in expected:
                name = re.sub(m.group(), mapping[m.group()], name)
    return name


    # return the cleaned street name, if the street type condition
    # is met, or just return the original name
    #return name



    #return street_types2
pprint.pprint(update_name(name, mapping))

    #pprint.pprint(audit(DATAFILE))
#pprint.pprint(len(audit(DATAFILE)))
#pprint.pprint(len(dict(audit(DATAFILE))))