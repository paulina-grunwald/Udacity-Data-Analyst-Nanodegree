import xml.etree.ElementTree as ET
import pprint

#parse element into the tree
tree = ET.parse('exampleResearchArticle.xml')
#get the root
root = tree.getroot()

#print children of root
print "\nChildren of root"
for child in root:
    print child.tag


#extract title
#find a path to the title
title = root.find('./fm/bibl/title')
title_text = ""
#itarate over children of title
for text in title:
    #use text of the title
    title_text += text.text
print "\nTitle:\n", title_text


#find all e-mails
print "\nAuthor email addresses:\n",
for a in root.findall('./fm/bibl/aug/au'):
    email = a.find('email')
    snm = a.find('snm')
    if email is not None:
        print email.text

#extract name, surname, e-mail of the author

def get_authors(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {
            "snm": None,
            "fnm": None,
            "email": None
        }
        #since the names and email for authors are unique for each author, we use "find".
        data["snm"] = author.find("snm").text
        data["fnm"] = author.find("fnm").text
        data["email"] = author.find("email").text

        authors.append(data)

    return authors

print get_authors(root)


#Extract all the info about the authors
def getall_authors(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {
            "fnm": None,
            "snm": None,
            "email": None,
            "insr": []
        }

        data["fnm"] = author.find('./fnm').text
        data["snm"] = author.find('./snm').text
        data["email"] = author.find('./email').text
        insr = author.findall('./insr')

        for i in insr:
            data["insr"].append(i.attrib["iid"])

        authors.append(data)

    return authors

print getall_authors(root)