# # # # # # s = 1,2,3,4
# # # # # # l = list(s)
# # # # # # print(l)
# # # # #
# # # # # l = [1,"hello", 4,1,2,5]
# # # # # print(l[1:2])
# # # #
# # # # L = eval(input("enter the list elements"))
# # # # Ltest = []
# # # # if type(L) == type(Ltest):
# # # #     print(L)
# # # l = [1,2,3,4]
# # # print(
# # l1 = [1,2,3,4]
# # l2 = [1,2,3,52135,1,4]
# # l3 = l1*3 + l2*4
# # print(l3)
# l = [1,2,34, 10, 2535]
# print(l[1:10])
# for i in l:
#     print(i)
# for i in range(len(l)):
#     print(l[i])
# l[:2] = [10,11]
# print(l)
#
l = [1,2,3,4,5,10]
# for i in range(10):
#     x = eval(input("Enter the thing you like and give mme your data:"))
#     l.append(x)
#     print(l)
print(l)
print(l.pop())
print(l)
l.reverse()
print(l)
b = sorted(l)
print(b)
print(max(l))
print((min(l)))
l.append((1,2))
print(l)