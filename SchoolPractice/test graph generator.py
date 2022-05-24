x = int(input("input x value"))
def grapher(x):
    y = x^3-3*x**2+4*x-5
    return y
print("X \t Y")
i = 0
while i < 20:
    y = grapher(x)
    print(x," \t", y)
    if x<20:
        n = 0
        for n in range(x):
            print("|")
            n+=1
    x +=1
    i += 1

