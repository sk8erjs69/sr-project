import xml.etree.ElementTree as ET
#-*- coding: utf-8 -*-
def stripxml():
    doc = './data/brain.xml'
    tree = ET.parse(doc)
    root = tree.getroot()
    hit =[]
    docsearch = []
    x=0
    count = 0
    for Abstract in root.iter('Abstract'):
        hit = []
        x+=1
        for AbstractText in Abstract.findall(".//AbstractText"):
            hit.append(AbstractText.text)    
            xml_string = ET.tostring(Abstract)
            with open('./data/brain-data.xml','a') as xmlfile:
               data = xml_string
               xmlfile.write(data)
    

def main():
    stripxml()

main()
