def count(term):
    u = 0
    l = 0
    leng = len(term)
    for x in range(leng):
        if term[x].upper() == term[x]:
            u += 1
        elif term[x].upper() != term[x]:
            l +=1
    print("Upper characters are, ", u)
    print("Lower characters are, ", l)
jstuff = input("Enter your desired string: ")
count(jstuff)