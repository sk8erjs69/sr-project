##############################
#
# Senior Research Project R script
#
# Michael Gargano + Joseph Streigle
#################################

data = read.csv("/home/ganoh/Documents/homework/csc450-/project/matrix.csv")

data.sum = apply(data,2,sum)
data2 = data.frame[data.sum, row.names = data[0,]] 
pct = round(data.sum/sum(data.sum) * 100)
lbls <- paste(data[0,],pct)
lbls <- paste(pct,"%",sep="") # ad % to labels 

pie(data.sum,labels = lbls,main="Word Proportions over 3 documents")