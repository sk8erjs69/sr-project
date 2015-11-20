import xml.etree.ElementTree as ET
import re
#-*- coding: utf-8 -*-
def stripxml():
    doc = './new-data/bladder.xml'
    tree = ET.parse(doc)
    root = tree.getroot()
    hit =[]
    xxx = []
    docsearch = []
    x=0
    count = 0
    for Abstract in root.iter('Abstract'):
        x+=1
        xml_string = ET.tostring(Abstract)
        #2 regex's: one to exclude words beginning w/ lowercase
        #the second to exclude common words (case ignored)
        find =re.findall(r'(?!\b[a-z])\b\w\w\w\b|\
(?!\b[a-z])\b\w\w\w\w\b|(?!\b[a-z])\b\w\w\w\w\w\b|(?!\b[a-z])\
\b\w\w\w\w\w\w\b|(?!\b[a-z])\b\w\w\w\w\w\w\w\b|\
(?!\b[a-z])\b\w\w\w\w\w\w\w\w\b|(?!\b[a-z])\b\w\w\w\w\w\w\w\w\w\b|(?!\b[a-z])\b\w\w\w\w\w\w\w\w\w\w\b',xml_string)
        find =re.findall(r'(?!(?i)the|and|for|are|but|not|you|all|\
any|can|had|her|was|one|our|out|day|get|has|him|his|how|man|new|now\
|old|see|two|way|who|boy|did|its|let|put|say|she|too|use|dna|rna)\b\w\w\w\b|(?!that|with|have|this|will|your|from|they|know|want|been|good|much|some|\
time|very|when|come|here|just|like|long|make|many|more|only|over|such|take\
|than|them|well|were|gene|coma|male)\b\w\w\w\w\b|(?!genes|bleed|\
blood|death|tumor|human|study|being|input|males)\b\w\w\w\w\w\b|(?!cancer|tumors|humans)\
\b\w\w\w\w\w\w\b|(?!genetic)\b\w\w\w\w\w\w\w\b|\
\b\w\w\w\w\w\w\w\w\b|\b\w\w\w\w\w\w\w\w\w\b|\b\w\w\w\w\w\w\w\w\w\w\b',str(find))
        for f in range(0, len(find)):
            #place all words in uppercase to eliminate repeats of genesymbols
            #necessary for dictionary search and accurrate results
           find[f] = find[f].upper()
        hit = set(find)
        hit= list(hit)
        hit.sort()
        hit = ','.join(hit)
        with open('./new-data/bladder-data.txt','a') as txtfile:
           txtfile.write(str(hit) + '\n')
         
def main():
    stripxml()

main()
