import xml.etree.ElementTree as ET
import re
import csv

def extractGeneData(doc, cancer,gene,documentMatch):
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

def returnGeneList():
    with open('genes.txt','rb') as csvfile:
        genereader = csv.reader(csvfile,delimiter=' ')
        genesym = []
        for row in genereader:
            genechunk = row[0].split("\\")  
            genesubchunk =  genechunk[0].split("\t")
            genesym1 = genesubchunk[0].split("([^\s]+)")
            genesym.append(genesym1[0]) 
            
        return genesym


def main():
    gene = raw_input('Enter the gene you wish to find: ')
    documentMatch = []
    extractGeneData("./data/test1.xml","test1",gene,documentMatch)
    extractGeneData("./data/test.xml","test",gene,documentMatch)
    extractGeneData("./data/bladder.xml","bladder",gene,documentMatch)

main()
