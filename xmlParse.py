import xml.etree.ElementTree as ET
tree = ET.parse("C:/Users/Owner/Desktop/Senior Research/test.xml")
root = tree.getroot()
hit =[]
hit1 =[]
for Abstract in root.iter('Abstract'):
    hit =[]
    for AbstractText in Abstract.findall(".//AbstractText"):
        hit.append(AbstractText.text)
    hit1.append(hit)
    print hit1
