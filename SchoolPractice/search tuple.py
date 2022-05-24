t = ()
l = eval(input("Enter the number of elements you want to enter: "))
for i in range(l):
    number = int(input("Enter the element you want to enter: "))
    t = t + (number, )
k = 0
val = int(input("Enter the number you want to search for: "))
for x in range(l):
    if val == t[x]:
        print(val, " was found at index ", x)
        break
    k +=1
if k == l:
    print("element wasn't found")
s = sum(t)
print(s)
