import xml.etree.ElementTree as ET
import re
#-*- coding: utf-8 -*-
def stripxml():
    doc = './data/lungs.xml'
    tree = ET.parse(doc)
    root = tree.getroot()
    hit =[]
  
    docsearch = []
    x=0
    count = 0
    for Abstract in root.iter('Abstract'):
        x+=1
        xml_string = ET.tostring(Abstract)
        find =re.findall(r'(?!the|and|for|are|but|not|you|all|\
any|can|had|her|was|one|our|out|day|get|has|him|his|how|man|new|now\
|old|see|two|way|who|boy|did|its|let|put|say|she|too|use|dna|rna)(?i)\b\w\w\w\b|\
(?!that|with|have|this|will|your|from|they|know|want|been|good|much|some|\
time|very|when|come|here|just|like|long|make|many|more|only|over|such|take\
|than|them|well|were|gene|coma)(?i)\b\w\w\w\w\b|(?!genes|bleed|\
blood|death|tumor|human)(?i)\b\w\w\w\w\w\b|(?i)\b\w\w\w\w\w\w\b',xml_string)
        hit = set(find)
        hit= list(hit)
        hit.sort()
        hit = ','.join(hit)
        with open('./data/lung-data.txt','a') as txtfile:
           txtfile.write(str(hit) + '\n')

           
def main():
    stripxml()

main()