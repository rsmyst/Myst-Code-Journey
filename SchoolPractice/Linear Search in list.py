list1 = []
num = eval(input("Enter the number of elements you want to enter:"))
for n in range(num):
    number = int(input("Enter the number:"))
    list1.append(number)
k = 0
key = int(input("Enter element to be searched for:"))
for i in range(0,num):
    if key==list1[i]:
        print(list[i], "found at index", i)
        break
    k+=1
if k==num:
    print("Element not found in list")