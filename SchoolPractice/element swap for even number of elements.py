#Input a list of numbers and swap elements at the even location
#with the elements at the odd location(LAB+THEORY)
lst = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
print("List before swapping: ",lst)
for i in range(0,num-1,2):
    lst[i], lst[i+1]=lst[i+1], lst[i]
print("List after swapping: ",lst)