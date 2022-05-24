L = eval(input("Enter the element in list:"))
leng = len(L)
minE = L[0]
for i in range(1,leng):
    if L[i]<minE:
        minE = L[i]
        minpos = i
print("The given list is:", L)
print("The smallest element in the given list is, ",minE, "found at index", mixpos)