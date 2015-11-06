import xml.etree.ElementTree as ET
#tree = ET.parse("C:/Users/Owner/Desktop/Senior Research/test.xml")
tree = ET.parse("C:/Users/Owner/Desktop/Senior Research/pubmed_result.xml")
root = tree.getroot()
hit =[]
hit1 =[]
for Abstract in root.iter('Abstract'):
    hit =[]
    for AbstractText in Abstract.findall(".//AbstractText"):
        hit.append(AbstractText.text)
    hit1.append(hit)
    print hit1
import re
lines=str(hit1[0])
docsearch = re.findall(r'(?i)\bHBV\b',lines)
print docsearch
print len(docsearch)
