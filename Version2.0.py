import xml.etree.ElementTree as ET
import re
gene = raw_input('Enter the gene you wish to find: ')
documentMatch =[]
def extractGeneData(doc, cancer):
    print "Results for " + cancer
    print "------------------------------------------------"
    tree = ET.parse(doc)
    root = tree.getroot()
    hit =[]
    docsearch = []
    x=0
    for Abstract in root.iter('Abstract'):
        hit =[]
        x+=1
        for AbstractText in Abstract.findall(".//AbstractText"):
            hit.append(AbstractText.text)
            
        find =re.findall(r'(?i)\b%s\b'%gene,str(hit))
        if (len(find) >= 1):
            docsearch.append(find)
            print "number of times gene found in EACH article = " + str(len(find))
   # print docsearch
    
    print "number of documents with this gene = " + str(len(docsearch))
    print "x = " + str(x)
    return documentMatch.append(len(docsearch))    
extractGeneData("test1.xml","test1")
extractGeneData("test.xml","test")
extractGeneData("bladder.xml","bladder")
