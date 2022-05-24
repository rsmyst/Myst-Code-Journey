def count_primes(n):
    b = 0
    l = [2,3,5,7,9]
    j = 0
    for i in range(n):
        for bin in l:
            if i%bin != 0:
                b+=1
    print("Number of primes is, ", b)
num = int(input("enter the number you want to count primes too"))
count_primes(num)
