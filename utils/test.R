source("utils/myread.ENVI.R")
source("utils/imagematrix.R")
require(ggplot2)
require(reshape2)
require(ggthemes)

args=commandArgs(T)

imagepath <- args[1]

temp <- myread.ENVI(paste(imagepath,args[2], sep = ""),paste(imagepath,args[2],".hdr", sep = ""))

write.csv(temp,paste("results/",args[3],".csv", sep = ""))