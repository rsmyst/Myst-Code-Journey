L = eval(input("Enter the list you want to swap elements for: "))
for i in range(0,len(L), 2):
    L[i], L[i+1] = L[i+1], L[i]
print(L)