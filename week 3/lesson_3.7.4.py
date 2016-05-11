from xml.etree import ElementTree as ET
from lxml import etree

import requests

# ml = input()
ml = r'<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'
# tree = ElementTree.parse(ml)
# tree = ET.XMLParser(ml)
# root = tree.feed()

root = ET.fromstring(ml)
print(root)


cur_root.findall("cube"))
cur_root.findall("cube[@color='red']"))


# req = requests.get("https://docs.python.org/3/")
# print(req.status_code)
# print(req.headers["Content-Type"])
#
# parser = etree.HTMLParser()
# root = etree.fromstring(req.text, parser)
#
# # print(root)
# for elem in root.iter("a"):
#   print(elem, elem.attrib)
