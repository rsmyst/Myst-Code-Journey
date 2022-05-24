L = []
leng = int(input("Enter the number of elements you want to enter: "))
for i in range(leng):
    no = int(input("Enter the element: "))
    L.append(no)
smallest = L[0]
smallest2 = None
for x in range(1, leng):
    if L[x] < smallest:
        smallest2 = smallest
        smallest = L[x]
    elif smallest2 == None or smallest2 > L[x]:
        smallest2 = L[x]
print("smallest value is ", smallest, "And second smallest is ", smallest2)