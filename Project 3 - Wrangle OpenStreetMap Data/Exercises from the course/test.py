import xml.etree.ElementTree as ET
import pprint

string_xml = """<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>"""

#find root from string which is xml file
root = ET.fromstring(string_xml)

# finds children from root and it's attribute
print "\nChildren of root"
for child in root:
    print child.tag, child.attrib


#finds all the values of the rank in the xml
print "...."
rank_list = []
for a in root.findall('./'):
    rank = a.find('rank')
    if rank not in rank_list:
        rank_list.append(rank.text)

print "List of ranks:", rank_list


#Children are nested, and we can access specific child nodes by index:
for i in root:
    print root[1][2].text