list=[3,6,9,13,15]
size=len(list)
max1=list[0]
min1=list[0]
sum=0
for i in list:
    if i>max1:
        max1=i
    else:
        min1=i
    sum+=i
aver=sum/size
print(size,max1,min1,sum,aver)