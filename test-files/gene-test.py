#!usr/bin/python/
import sys
import csv


with open('genes.txt','rb') as csvfile:
	genereader = csv.reader(csvfile,delimiter=' ')
	genesym = []
	for row in genereader:
		genechunk = row[0].split("\\")  
		genesubchunk =  genechunk[0].split("\t")
		genesym1 = genesubchunk[0].split("([^\s]+)")
		genesym.append(genesym1[0])	
		
	print len(genesym)




     
#f.close()
