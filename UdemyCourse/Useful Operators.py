# mylist = [1,3,2]
# for num in range(0,21,2):
#     print(num)
# print(list(range(5,10)))
# count = 0
# for letter in "abcde":
#     print('The index {} is letter {}'.format(count, letter))
#     count += 1
# word = "abcdefg"
# for index,letter in enumerate(word):
#     print(letter)
#     print(index)
#     print('\n')
#     break
#
# my_lists = [1,3,2,5,54,4,6]
# my_lists2 = ['a','v','c','r','w','anks','2','5wsfd']
# my_lists3 = [100,200,300]
# sorter = {1:mylist, 2:my_lists2, 3:my_lists3}
# requested_sorter = input("What is your filter? \n")
# if requested_sorter == 1:
#     for item in my_lists:
#         print(item)
# elif requested_sorter == "1,2":
#     for item in zip(my_lists, my_lists2):
#         print(item)
# elif requested_sorter == "1,3":
#     for item in zip(my_lists,my_lists3):
#         print(item)
#
# print(1 in [1,2,3])

# from random import shuffle, randint
# mylist = [1,2,3,5,2,3,2,]
# shuffle(mylist)
# print(mylist)
# s = randint(5,100)
# print(s)
oldpass = "Rahul"
count = 0
userpass = input("What is your old password? \n")
while userpass == oldpass:
    if count <= 3:
        new_pass = input("What do you want your new password to be? \n")
        if new_pass == oldpass:
            print("That's your old pass bro!")
            continue
        elif len(new_pass) >= 8:
            print("Great password, move ahead!")
            break
        elif len(new_pass) < 8:
            print("Try again!")
            continue
else:
    print("Try again!")
name = "Slapmaster15"
inputted_name = input("What is your old name? \n")
while inputted_name.lower() == name.lower():
    newname = input("What do you want your new name to be? \n")
    if len(newname) >= 5:
        print("Nice and long!")
        break
    elif len(newname) < 5:
        print("Try a different longer name")
        continue
    elif len(newname) == 0:
        print("nothingness exists too")
        continue
else:
    print("Did not match with old name! Try again.")

