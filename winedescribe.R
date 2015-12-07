whitewine<- read.csv("/Users/wensiwang/Desktop/I590/HW/Project/Code/winequality-white.csv", sep=";")
m=as.matrix(whitewine)

r= matrix(0, nrow=1, ncol=12)
ran= matrix(0, nrow=1, ncol=12)
IQR= matrix(0, nrow=1, ncol=12)
for (i in 1:12)
{ran=range(m[1:2898,i])
 r[i]=ran[2]-ran[1]
 quan=fivenum(m[1:2898,i])
 IQR[i]=quan[4]-quan[2]
}
v= matrix(0, nrow=1, ncol=12)
std= matrix(0, nrow=1, ncol=12)
aver=matrix(0, nrow=1, ncol=12)
cv=matrix(0, nrow=1, ncol=12)
for (i in 1:12)
{
  aver[i]=mean(m[,i])
  v[i]=var(m[1:2898,i])
 std[i]=sd(m[1:2898,i])
 cv[i]=std[i]/aver[i]
}
library("timeDate", lib.loc="/Library/Frameworks/R.framework/Versions/3.1/Resources/library")
sk= matrix(0, nrow=1, ncol=12)
kur= matrix(0, nrow=1, ncol=12)

for (i in 1:12)
{sk[i]=skewness(m[,i])
 kur[i]=kurtosis(m[,i])
}


library("stringi", lib.loc="/Library/Frameworks/R.framework/Versions/3.1/Resources/library")
num=matrix(0,nrow=1, ncol=12)
for (i in 1:12)
{
  indicator=(m[,i]<quan[1]-IQR[i]*1.5)&(m[,i]>quan[3]+IQR[i]*1.5)
  ind=stri_replace_all_fixed(indicator, "TRUE", "1")
  ind=stri_replace_all_fixed(ind, "FALSE", "0")
  ind=as.numeric(ind)
  num[i]=sum(ind)
}
summ=summary(m)

output=rbind(aver,r,IQR,v,std,cv,sk,kur,num)
rownames(output) <- c("mean","range","IQR","variance","standard deviation","cv","skewness","kurtosis","number of outliers")
colnames(output)<-colnames(m)
output=round(output,2)
View(output)
summ


