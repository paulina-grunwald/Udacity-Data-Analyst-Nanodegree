import xml.etree.cElementTree as ET
import pprint
import os
datadir = ""
datafile = "denhaag_sample.osm"


#Parse through the file with ElementTree and count the number of unique element types to understand overall structure.
def count_tags(filename):
        #create empty dictionary
        tags = {}
        #interpase file name and extract top level tags keeping track
        #of the count of unique tags
        for event, elem in ET.iterparse(filename):
            if elem.tag in tags:
                tags[elem.tag] += 1
            else:
                tags[elem.tag] = 1
        #return tags and number of occurences
        return tags

#print tags and number of occurences of unique tags
pprint.pprint(count_tags(datafile))