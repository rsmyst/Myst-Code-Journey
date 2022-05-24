lst=eval(input("ENTER LIST:"))
length=len(lst)
lst=list(lst)
mean=sum=0
for i in range (0,length):
    sum+=lst[i]
mean=sum/length
print("Given list is:",lst)
print("The mean of the given list is :",mean)