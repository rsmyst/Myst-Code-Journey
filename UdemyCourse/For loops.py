# mylist = [1,2,3,4,5,6,7,8,9,10]
# for num in mylist:
#     if num % 2 == 0:  #here % gives back the remainder. That is, if the remainder is 0 then return its an even number
#         print(num)
#     else:
#         print(f'Odd Number: {num}')
#
# list_sum = 0
# for num in mylist:
#     list_sum = list_sum + num
#
# if list_sum < 60:
#         print("chiki")
# elif list_sum == 55:
#         print("accuracte")
# else:
#         print("err")
#
# list1 = [(2,3,5),(4,5,2),(1,102,4)]
# for item in list1:
#     print(item)
# for a,b,c in list1:
#     print(a,b,c)
# THIS IS CALLED TUPLE UNPACKING

d = {'k1':1,'k2':2,'k3':3}
for item in d.items(): #if you want to get both key and value, use .items()
    print(item)
for key,value in d.items():
    print(value, key)