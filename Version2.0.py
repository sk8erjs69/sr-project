import xml.etree.ElementTree as ET
import re
import csv

def extractGeneData(doc, cancer,gene,documentMatch):
    tree = ET.parse(doc)
    root = tree.getroot()
    hit =[]
    docsearch = []
    x=0
    count = 0
    for Abstract in root.iter('Abstract'):
        hit =[]
        x+=1
        for AbstractText in Abstract.findall(".//AbstractText"):
            hit.append(AbstractText.text)
            
        find =re.findall(r'(?i)\b%s\b'%gene,str(hit))
        if (len(find) >= 1):
            docsearch.append(find)
            count+= 1
           # print "number of times gene found in EACH article = " + str(len(find))
   # print docsearch
    
    #print "number of documents with this gene = " + str(len(docsearch))
    #print "x = " + str(x)
    #return documentMatch.append(len(docsearch))
    return count
def returnGeneList():
    with open('./data/genes.txt','rb') as csvfile:
        genereader = csv.reader(csvfile,delimiter=' ')
        genesym = []
        for row in genereader:
            genechunk = row[0].split("\\")  
            genesubchunk =  genechunk[0].split("\t")
            genesym1 = genesubchunk[0].split("([^\s]+)")
            genesym.append(genesym1[0]) 
        genesym.pop(0)
        return genesym
    
def main():
    Matrix = [[ x for x in range(4)] for x in range(4)]
    gene = returnGeneList();
    documentMatch = []
    for x in range(0,4):
       print "Mining genesym " + str(x) + " of 4"
       test1 = extractGeneData("./data/test1.xml","test1",gene[x],documentMatch)
       test = extractGeneData("./data/test.xml","test",gene[x],documentMatch)
       bladder = extractGeneData("./data/bladder.xml","bladder cancer",gene[x],documentMatch)
       Matrix[x][0] = gene[x]
       Matrix[x][1] = test1
       Matrix[x][2] = test
       Matrix[x][3] = bladder
       
    for row in Matrix:
        print row

main()
