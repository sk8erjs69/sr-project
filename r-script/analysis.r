##############################
#
# Senior Research Project R script
#
# Michael Gargano + Joseph Streigle
#################################
# get data from csv file
data = read.csv("~/GitHub/sr-project/big-data/matrix.csv")

#remove insignificant values
data1 = data.frame(data[data$Prostate.Count>=3,])
data1 = data.frame(data1[data1$Lung.Count>=3,])
data1 = data.frame(data1[data1$Brain.Count>=3,])

#create and transpose matrix for fisher test
m = matrix(c(data1$Prostate.Count,data1$Lung.Count,data1$Brain.Count), ncol = 3, byrow = FALSE)
m= t(m)

#fisher test function
f <- function(r){
  x = r[1]
  y = r[2]
  z = r[3]
  mm = matrix(c(x,20000-x, 
               y, 20000 - y,
               z, 20000 - z ),nrow = 3, byrow = TRUE)
  
  f = fisher.test(mm, workspace = 800000,hybrid = TRUE)
  
  return (f$p.value)
}

#apply fisher test to entire matrix
fisher.p = apply(m,2,f)

#add back gene symbol names and pull out top 5 genes based on fisher.p value
fisher.frame = data.frame(data1$Gene.Symbol, fisher.p)
fisher.frame = fisher.frame[order(-fisher.frame$fisher.p),]
mtch = match(fisher.frame$data1.Gene.Symbol[1:5],data1$Gene.Symbol)
data1[mtch,]

#ATTEMPTED BOXPLOT NoT SURE IF THIS IS WORKING RIGHT
boxplot(data1[mtch,2:4])

#Pull out bottom five genes
fisher.frame = fisher.frame[order(fisher.frame$fisher.p),]
mtch = match(fisher.frame$data1.Gene.Symbol[1:5],data1$Gene.Symbol)
data1[mtch,]
#plot shows extreme differences between hits across these
barplot(t(as.matrix(data1[mtch,2:4])),xlab = "Gene Symbol", 
        col =c("red","green","blue"),names.arg = data[mtch,1], legend=colnames(data1[,2:4]), beside=TRUE)

#function for clustering
plot.clust <-function(x) {
  d = dist(t(x))
  print(d)
  h = hclust(d)
  plot(h)
}
#CLuster shows which cancer types are most similar
plot.clust(data1[,2:4])

#TODO: POSSIBLE CLUSTER TO SHOW COMPARISONS OF GENES

#data.sum = apply(as.integer(data1[2:4]),1,sum)
data.sum = apply(data1[,2:4],1,sum)
data2 = data.frame(data.sum, row.names = data1[1])
pct = round(data.sum/sum(data.sum) * 100)
lbls <- paste(data1[0,],pct)
lbls <- paste(pct,"%",sep="") # ad % to labels 

pie(data.sum,labels = lbls,main="Word Proportions over 3 documents")
