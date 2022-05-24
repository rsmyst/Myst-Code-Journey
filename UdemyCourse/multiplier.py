def mult(list):
    leng = len(list)
    j = 1
    for item in list:
        j = j*int(item)
    if j!= 1:
        print(j)
n = eval(input("Enter the list you want; "))
mult(n)