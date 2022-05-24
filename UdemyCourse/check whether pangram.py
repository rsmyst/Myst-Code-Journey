alpha_count = 26
alpha_list = []
for x in range(97,123):
    y = chr(x)
    alpha_list.append(y)
# for x in range(65, 91):
#     j = chr(x)
#     alpha_list.append(j)
n = 1
alpha_list.append(n)
print(alpha_list)
#print(alpha_list)

def ispangram(str):
    global alpha_list
    leng = len(str)
    empty = [1]
    for x in range(leng):
        if str[x].lower() in alpha_list:
            alpha_list.pop(0)
    if alpha_list == empty:
        print(alpha_list)
        print("it was a pangram")
    else:
        print("it wasn't a pangram")
qt = input("enter a string to check: ")
ispangram(qt)