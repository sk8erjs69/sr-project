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

def writecsv(data):
    csvfile = "./data/matrix.csv"
    with open(csvfile, "w") as output:
      writer = csv.writer(output, lineterminator='\n')
      writer.writerows(data)

    
def main():
    # Define Matrix (col)(row)
    Matrix = [[ x for x in range(4)] for x in range(39827)]
    Matrix[0][0] = "Gene Symbol"
    Matrix[0][1] = "Bladder Count"
    Matrix[0][2] = "Lung Count"
    Matrix[0][3] = "Brain Count"

    # Get gene list
    gene = returnGeneList();
    documentMatch = []
    # Conduct the mining and inserting of the matrix.
    for x in range(0,39826):
       count = x + 1
       print "Mining gene symbol " + str(count) + " of 500"
       brain = extractGeneData("./data/brain-data.xml","Brain Cancer",gene[x],documentMatch)
       lung = extractGeneData("./data/lung-data.xml","Lung Cancer",gene[x],documentMatch)
       bladder = extractGeneData("./data/bladder-data.xml","bladder cancer",gene[x],documentMatch)
       Matrix[count][0] = gene[x]
       Matrix[count][1] = bladder
       Matrix[count][2] = lung
       Matrix[count][3] = brain
    writecsv(Matrix)
    print "Wrote Matrix to file in /data: Matrix.csv"

main()
