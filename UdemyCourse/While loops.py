#while loops are basically for repeating a block of code as long as a condition is satiisfied.
#while some_condition == True:
    #Do something
#else:
    #Do something else

x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print(f'{x} is not less than 5, fix yo goddamn brain')

x = [1,2,3]
for item in x:
    pass


print("end of my script")

my_string = "sammy"
for letter in my_string:
    if letter == "a":
        continue
    print(letter)
for letter in my_string:
    if letter == "m":
        break
    print(letter)

x = 0

while x  < 5:
    if x == 3:
        break
    print(x)
    x += 1

# break goes out of the current closest enclosing loop, continue goes to the top of the current closest enclosing loop, pass does nothing and acts as placeholder
