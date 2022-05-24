def filter(x):
    y = ()
    z = ()
    for item in x:
        if item%2 == 0:
            print(y)
            y+= (item,)
        else:
            print(z)
            z+= (item,)
    print("Even numbers were, ", y)
    print("odd numbers/0 were, ", z)


x = eval(input("Enter a list of something: "))
filter(x)

def check_even(num):
    return num%2 == 0
mynums = [1,2,3,4,5,6]
y = list(filter(check_even, mynums))
print(y)
