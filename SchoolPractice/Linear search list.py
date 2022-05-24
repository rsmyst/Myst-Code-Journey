l = eval(input("Enter the list of elements"))
val = eval(input("Enter the element you want to search for: "))
for i in range(0, len(l)):
    if val == l[i]:
        print(val, " was found at index ", i)
        break
else:
    print("Element wasn't found")
