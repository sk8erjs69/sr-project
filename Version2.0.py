import xml.etree.ElementTree as ET
import re
import csv

def extractGeneData(doc, cancer,gene_dict):
     with open(doc,'r') as txtfile:
      for line in txtfile:
        abstract = line.split(",")
        abstract = list(abstract)
        x = len(abstract)
        for i in range(0,x):
          word = str(abstract[i]).strip()##added to remove whitespace from last word in list
          try:
            valueMatch = gene_dict[word]
            gene_dict[word] = valueMatch + 1
          except Exception, e:
            continue;
      return gene_dict


def returnGeneList():
    with open('./data/genes.txt','rb') as csvfile:
        genereader = csv.reader(csvfile,delimiter='\n')
        genesym = []
        for row in genereader:
           row = ''.join(row)
           genesym.append(row) 
        genesym.pop(0)
        return genesym

def writecsv(data):
    csvfile = "./new-data/matrix.csv"
    with open(csvfile, "w") as output:
      writer = csv.writer(output, lineterminator='\n')
      writer.writerows(data)

def reset_dict():
  gene = returnGeneList();
  gene_dict = {}
  for  i in range(0,len(gene)):
    gene_dict[str(gene[i])] = 0
  return gene_dict

    
def main():
    # Define Matrix (col)(row)
    #39825
    Matrix = [[ x for x in range(4)] for x in range(39825)]
    Matrix[0][0] = "Gene Symbol"
    Matrix[0][1] = "Bladder Count"
    Matrix[0][2] = "Lung Count"
    Matrix[0][3] = "Brain Count"


    # Conduct the mining and inserting of the matrix.
    #39824
    gene_dict = reset_dict()
    print "Mining gene symbols"
    gene_dict = reset_dict()
    bladder = extractGeneData("./new-data/bladder-data.txt","bladder cancer",gene_dict)
    count = 0
    for key, value in bladder.iteritems():
      count = count + 1
      Matrix[count][0] = key
      Matrix[count][1] = value
   
    gene_dict = reset_dict()
    lung =  extractGeneData("./new-data/lung-data.txt","Lung Cancer",gene_dict)
    count = 0
    for key,value in lung.iteritems():
      count = count + 1
      Matrix[count][2] = value

    gene_dict = reset_dict()
    brain = extractGeneData("./new-data/brain-data.txt","Brain Cancer",gene_dict)
    count = 0 
    for key,value in brain.iteritems():   
      count = count + 1
      Matrix[count][3] = value

    writecsv(Matrix)
    print "Wrote Matrix to file in /new-data: Matrix.csv"

main()
