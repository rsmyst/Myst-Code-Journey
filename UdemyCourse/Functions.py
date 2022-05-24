# def say_hello(name="Default"):
#     print(f'Hello {name}')
# print(say_hello())
# def add_num(num1,num2):
#     return num1+num2
# result = add_num(20,60)
# print(result)
# def newfunc(a):
#     result = a%2 == 0
#     return result
#
# print(newfunc(25))
# def check_even_list(givenlist):
#     for number in givenlist:
#         if number%2 == 0:
#             return True
#         else:
#             pass
#     return False
#
# print(check_even_list((1,3,3,5)))
def newfunction(numberlist):
    listofeven = []
    for number in numberlist:
        if number % 2 == 0:
            listofeven.append(number)
        else:
            pass
    return listofeven
print(newfunction([1,2,3,4,2,1,5,1,2,3,5,6,4]))
