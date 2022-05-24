L = eval(input("Enter the elements in list:"))
leng = len(L)
maxE= L[0]
for i in range(1,leng):
    if L[i]>maxE:
        maxE = L[i]
        maxpos = i
print("the given list is:", L)
print("the largest element in list is:", maxE, "found at index", maxpos)

