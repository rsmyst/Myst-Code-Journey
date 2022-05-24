def uniquer(list):
    u = []
#    b = []
    leng = len(list)
    for x in range(leng):
        term = list[x]
        if term in u:
            continue
        elif term not in u:
            u.append(term)
    print("unique list is, ", u)

listy = eval(input("Enter a list of your choice: "))
uniquer(listy)