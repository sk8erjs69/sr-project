import xml.etree.ElementTree as ET
import re
#tree = ET.parse("test.xml")
tree = ET.parse("pubmed_result.xml")
root = tree.getroot()
hit =[]
hit1 =[]
docsearch = []
gene = str('HBV')
string1 = str(r'(?i)\b) + str( +gene+"\\b')
#print string
for Abstract in root.iter('Abstract'):
    hit =[]
    for AbstractText in Abstract.findall(".//AbstractText"):
        hit.append(AbstractText.text)
        #find  = re.findall(string,str(hit))
        find =re.findall(r'(?i)\HBV\b',str(hit))
        if (len(find) >= 1):
            docsearch.append(find)
        
    
print docsearch
print len(docsearch)
#docsearch = re.findall(r'(?i)\bHBV\b',lines)
