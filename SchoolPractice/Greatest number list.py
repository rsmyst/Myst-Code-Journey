L = []
leng = int(input("Enter the number of elements you want to enter: "))
for i in range(leng):
    no = int(input("Enter the element: "))
    L.append(no)
greatest = L[0]
greatest2 = None
for x in range(1, leng):
    if L[x] > greatest:
        greatest2 = greatest
        greatest = L[x]
    elif greatest2 == None or greatest2 < L[x]:
        greatest2 = L[x]
print("greatest value is ", greatest, "And second greatest is ", greatest2)