def spy_game(L):
    length = len(L)
    check = ""
    for i in range(length):
        if L[i] == 0 or L[i] == 7:
            check = check + str(L[i])
    if check.find("007") != -1:
        print("Spy was found")
    else:
        print("Spy wasn't found")

plist = eval(input("Enter the list you want to search for"))
spy_game(plist)