lst=eval(input("ENTER LIST:"))
lst=list(lst)
print(lst)
element=int(input("Enter a number to search:"))
length=len(lst)
count=0
for i in range(0,length):
    if element==lst[i]:
        count+=1
if count==0:
    print(element," Not found in given list")
else:


    print(element,"has frequency of", count,"in given list")
