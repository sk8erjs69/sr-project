import xml.etree.ElementTree as ET
import re
#tree = ET.parse("test1.xml")
tree = ET.parse("pubmed_result.xml")
root = tree.getroot()
hit =[]
docsearch = []
x=0
gene = raw_input('Enter the gene you wish to find: ')

for Abstract in root.iter('Abstract'):
    hit =[]
    x+=1
    for AbstractText in Abstract.findall(".//AbstractText"):
        hit.append(AbstractText.text)
        
    find =re.findall(r'(?i)\b%s\b'%gene,str(hit))
    if (len(find) >= 1):
        docsearch.append(find)
        print(len(find))
print docsearch
print len(docsearch)
print x

