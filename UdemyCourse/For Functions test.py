def myfunc(word):
    out = []

    for i in range(len(word)):

        if i % 2 == 0:
            out.append(word[i].lower())

        else:
            out.append(word[i].upper())

    return ''.join(out)
